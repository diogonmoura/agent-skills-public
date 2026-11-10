#!/usr/bin/env python3
"""Embed the skill inventory and cross-skill references into documentation/skill-map.html.

Edges come from the maintained sources only:
- loads: a Markdown link from a skill (or its resources) to another SKILL.md
- mentions: another skill named in a skill's text (backticked, or a hyphenated name in prose)
- routes: plugin-level guidance (TASKS.md, WORKFLOW.md, references) naming a skill
"""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "documentation" / "skill-map.html"
START, END = "/*DATA-START*/", "/*DATA-END*/"
# Single-word names collide with ordinary prose; match them only as `name` with a plugin prefix.
AMBIGUOUS = {"test", "plan", "design", "review", "release", "setup", "research", "improve", "refine"}


def frontmatter(text):
    if not text.startswith("---"):
        return {}
    block = text.split("---", 2)[1]
    fields = {}
    for key in ("name", "description", "role", "scope", "invocation"):
        match = re.search(rf"^\s*{key}:\s*(.*(?:\n  (?![a-z_-]+:).*)*)", block, re.M)
        if match:
            fields[key] = re.sub(r"\s+", " ", match[1]).strip().strip("\"'>|- ")
    return fields


def collect(root=ROOT):
    depot = json.loads((root / "agent-depot.json").read_text())["artifacts"]
    upstream = {a["destination"]: a["source"] for a in depot.values()}
    skills, dirs = {}, {}
    for path in sorted(root.glob("plugins/*/skills/*/SKILL.md")):
        folder = path.parent
        plugin, name = folder.parts[-3], folder.name
        meta = frontmatter(path.read_text())
        key = f"{plugin}/{name}"
        dirs[key] = folder
        skills[key] = {
            "id": key, "plugin": plugin, "name": name,
            "description": meta.get("description", ""),
            "role": meta.get("role", "support"),
            "scope": meta.get("scope", "generic"),
            "invocation": meta.get("invocation", "both"),
            "upstream": upstream.get(folder.relative_to(root).as_posix(), ""),
            "resources": sum(1 for _ in (folder / "references").glob("*")) if (folder / "references").is_dir() else 0,
        }
    by_name = {}
    for key, skill in skills.items():
        by_name.setdefault(skill["name"], []).append(key)

    def resolve(name, plugin):
        candidates = by_name[name]
        same = [c for c in candidates if skills[c]["plugin"] == plugin]
        return (same or candidates)[0]

    def named(text, plugin):
        found = set()
        for match in re.finditer(r"`(?:([a-z0-9-]+):)?([a-z0-9-]+)`", text):
            name = match[2]
            if name in by_name and (name not in AMBIGUOUS or match[1]):
                found.add(resolve(name, plugin))
        for name in by_name:
            if "-" in name and re.search(rf"(?<![\w/-]){re.escape(name)}(?![\w-])", text):
                found.add(resolve(name, plugin))
        return found

    edges = {}
    for key, folder in dirs.items():
        plugin = skills[key]["plugin"]
        for doc in folder.rglob("*.md"):
            text = doc.read_text(errors="ignore")
            for match in re.finditer(r"\]\(([^)#\s]+)", text):
                target = (doc.parent / match[1]).resolve()
                if target.name == "SKILL.md":
                    tid = f"{target.parts[-4]}/{target.parts[-2]}"
                    if tid in skills and tid != key:
                        edges[(key, tid)] = "loads"
            for tid in named(text, plugin):
                if tid != key:
                    edges.setdefault((key, tid), "mentions")

    routes = set()
    plugin_docs = [*root.glob("plugins/*/*.md"), *root.glob("plugins/*/references/**/*.md")]
    for doc in plugin_docs:
        plugin = doc.relative_to(root).parts[1]
        text = doc.read_text(errors="ignore")
        hits = named(text, plugin)
        hits |= {resolve(n, plugin) for n in AMBIGUOUS & by_name.keys() if f"| {n} |" in text}
        routes |= {(plugin, doc.name, tid) for tid in hits}

    plugins = {}
    for manifest in sorted(root.glob("plugins/*/plugin.json")):
        data = json.loads(manifest.read_text())
        plugins[data["name"]] = {"description": data.get("description", ""), "version": data.get("version", "")}

    return {
        "plugins": plugins,
        "skills": list(skills.values()),
        "edges": [{"source": a, "target": b, "kind": k} for (a, b), k in sorted(edges.items())],
        "routes": [{"plugin": p, "doc": d, "target": t} for p, d, t in sorted(routes)],
    }


def main():
    data = collect()
    page = PAGE.read_text()
    head, rest = page.split(START, 1)
    _, tail = rest.split(END, 1)
    PAGE.write_text(head + START + json.dumps(data, separators=(",", ":")) + END + tail)
    print(f"{len(data['skills'])} skills, {len(data['edges'])} skill links, "
          f"{len(data['routes'])} plugin routes -> {PAGE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
