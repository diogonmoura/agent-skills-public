#!/usr/bin/env python3
"""Validate packages using bundled official 1.0.0 schemas, skill metadata and containment."""
import json
from pathlib import Path
import re
import sys

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]


def validate() -> list[str]:
    failures = []
    manifests = sorted((ROOT / "plugins").glob("*/plugin.json"))
    if not manifests:
        failures.append("No plugin packages found")
    schemas = {name: json.loads((ROOT / "schemas" / f"{name}.schema.json").read_text())
               for name in ("plugin", "mcp")}
    names = set()
    for manifest in manifests:
        package = manifest.parent.resolve()
        try:
            metadata = json.loads(manifest.read_text())
            jsonschema.validate(metadata, schemas["plugin"])
            name = metadata["name"]
            if name in names:
                raise ValueError(f"Duplicate plugin name {name}")
            names.add(name)
            for path in package.rglob("*"):
                if not path.resolve().is_relative_to(package):
                    raise ValueError(f"Escaping package path: {path}")
            mcp = package / "mcp.json"
            if mcp.exists():
                config = json.loads(mcp.read_text())
                jsonschema.validate(config, schemas["mcp"])
                for name, server in config["mcpServers"].items():
                    if {"PLUGIN_ROOT", "PLUGIN_DATA"} & set(server.get("env", {})):
                        raise ValueError(f"Reserved MCP environment variable: {name}")
                    for field in ("command", "cwd"):
                        value = server.get(field, "")
                        if value.startswith("./") and not (package / value).resolve().is_relative_to(package):
                            raise ValueError(f"Escaping MCP {field}: {name}")
            skill_names = set()
            for skill in sorted((package / "skills").glob("*/SKILL.md")):
                text = skill.read_text()
                parts = text.split("---", 2)
                if len(parts) != 3 or parts[0].strip():
                    raise ValueError(f"Missing frontmatter: {skill}")
                frontmatter = yaml.safe_load(parts[1])
                if not isinstance(frontmatter, dict):
                    raise ValueError(f"Invalid frontmatter: {skill}")
                skill_name = frontmatter.get("name", "")
                if not isinstance(skill_name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill_name) or len(skill_name) > 64:
                    raise ValueError(f"Invalid skill name: {skill}")
                if skill_name != skill.parent.name or skill_name in skill_names:
                    raise ValueError(f"Skill folder/name mismatch or duplicate: {skill}")
                description = frontmatter.get("description")
                if not isinstance(description, str) or not description.strip() or len(description) > 1024:
                    raise ValueError(f"Invalid skill description: {skill}")
                skill_names.add(skill_name)
        except (ValueError, TypeError, KeyError, jsonschema.ValidationError, yaml.YAMLError) as error:
            failures.append(f"{manifest.relative_to(ROOT)}: {error}")
    marketplace = ROOT / ".claude-plugin" / "marketplace.json"
    if marketplace.exists():
        entries = {entry["name"]: entry for entry in json.loads(marketplace.read_text()).get("plugins", [])}
        for manifest in manifests:
            metadata = json.loads(manifest.read_text())
            entry = entries.pop(metadata["name"], None)
            if entry is None:
                failures.append(f"marketplace.json: missing plugin {metadata['name']}")
            elif entry.get("source") != f"./plugins/{manifest.parent.name}" or entry.get("version") != metadata["version"]:
                failures.append(f"marketplace.json: source or version out of sync for {metadata['name']}")
        for name in entries:
            failures.append(f"marketplace.json: unknown plugin {name}")
    for profile in (ROOT / "profiles").glob("*.json"):
        data = json.loads(profile.read_text())
        referenced = data.get("plugins", []) + sum(data.get("optional_plugins", {}).values(), [])
        for name in referenced:
            if name not in names:
                failures.append(f"{profile.name}: unknown plugin {name}")
    return failures


if __name__ == "__main__":
    failures = validate()
    for failure in failures:
        print(failure, file=sys.stderr)
    if failures:
        raise SystemExit(1)
    print("Plugin manifests, skill metadata, profiles and package containment passed.")
