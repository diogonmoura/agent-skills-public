#!/usr/bin/env python3
"""Build documentation/skill-flow.html from the skill sources and documentation/skill-flow.json.

The JSON file holds the curated workflow (stages, maintenance lanes, across-phase groups,
starting paths and technical expertise). This script merges it with each skill's frontmatter,
checks that every skill is placed exactly once, and embeds the result in the page.

By default the build never fails: skills missing from the JSON appear on the page as
"New, not yet placed" and references to removed skills are dropped, so a scheduled refresh
always publishes. Use --strict (as tests/test_skill_flow.py does) to require a complete mapping.
"""
import argparse
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
FLOW = ROOT / "documentation" / "skill-flow.json"
PAGE = ROOT / "documentation" / "skill-flow.html"
START, END = "/*DATA-START*/", "/*DATA-END*/"


def frontmatter(path):
    text = path.read_text()
    if not text.startswith("---"):
        return {}
    return yaml.safe_load(text.split("---", 2)[1]) or {}


def load_skills(root=ROOT):
    depot = json.loads((root / "agent-depot.json").read_text())["artifacts"]
    upstream = {a["destination"]: a["source"] for a in depot.values()}
    skills, folders = {}, {}
    for path in sorted(root.glob("plugins/*/skills/*/SKILL.md")):
        folder = path.parent
        key = f"{folder.parts[-3]}/{folder.name}"
        meta = frontmatter(path)
        labels = meta.get("metadata") or {}
        folders[key] = folder
        skills[key] = {
            "id": key,
            "plugin": folder.parts[-3],
            "name": folder.name,
            "description": " ".join(str(meta.get("description", "")).split()),
            "role": labels.get("role", "support"),
            "scope": labels.get("scope", "generic"),
            "upstream": upstream.get(folder.relative_to(root).as_posix(), ""),
        }
    for key, folder in folders.items():
        loads = set()
        for doc in folder.rglob("*.md"):
            for match in re.finditer(r"\]\(([^)#\s]+)", doc.read_text(errors="ignore")):
                target = (doc.parent / match[1]).resolve()
                if target.name == "SKILL.md":
                    tid = f"{target.parts[-4]}/{target.parts[-2]}"
                    if tid in skills and tid != key:
                        loads.add(tid)
        skills[key]["loads"] = sorted(loads)
    return skills


def placements(flow, skills):
    """Map each skill id to the places it appears; report unknown and unplaced skills."""
    placed, unknown = {}, []

    def put(skill_id, where):
        if skill_id not in skills:
            unknown.append(f"{skill_id} (in {where})")
        else:
            placed.setdefault(skill_id, []).append(where)

    put(flow["endToEnd"]["skill"], "end-to-end")
    for stage in flow["stages"]:
        for group in [stage, *stage.get("lanes", [])]:
            for kind in ("entry", "support"):
                for skill_id in group[kind]:
                    put(skill_id, group["id"])
    for group in flow["across"]:
        for kind in ("entry", "support"):
            for skill_id in group[kind]:
                put(skill_id, group["id"])
    for item in flow["expertise"]:
        members = item.get("only") or [k for k, s in skills.items() if s["plugin"] == item["plugin"]]
        if not members:
            unknown.append(f"plugin {item['plugin']} (in expertise)")
        for skill_id in members:
            put(skill_id, "expertise:" + item["plugin"])

    regions = {s["id"] for s in flow["stages"]} | {l["id"] for s in flow["stages"] for l in s.get("lanes", [])}
    regions |= {g["id"] for g in flow["across"]}
    for path in flow["paths"]:
        if path["entry"] not in skills:
            unknown.append(f"{path['entry']} (entry of path {path['id']})")
        for step in path["steps"]:
            for region in [step["stage"], *step.get("also", [])]:
                if region not in regions:
                    unknown.append(f"region {region} (in path {path['id']})")
            for skill_id in step["skills"]:
                if skill_id not in skills:
                    unknown.append(f"{skill_id} (in path {path['id']})")

    unplaced = sorted(set(skills) - set(placed))
    duplicated = {k: v for k, v in placed.items() if len(v) > 1}
    return placed, unknown, unplaced, duplicated


def check(root=ROOT):
    flow = json.loads((root / "documentation" / "skill-flow.json").read_text())
    skills = load_skills(root)
    placed, unknown, unplaced, duplicated = placements(flow, skills)
    problems = [f"unknown: {u}" for u in unknown]
    problems += [f"not placed in the flow: {u}" for u in unplaced]
    problems += [f"placed more than once: {k} -> {', '.join(v)}" for k, v in sorted(duplicated.items())]
    return flow, skills, placed, problems


def prune(flow, skills):
    """Drop references to skills that no longer exist and repeated placements, so a refresh never breaks."""
    seen = set()

    def keep(ids):
        out = []
        for skill_id in ids:
            if skill_id in skills and skill_id not in seen:
                seen.add(skill_id)
                out.append(skill_id)
        return out

    if flow["endToEnd"]["skill"] in skills:
        seen.add(flow["endToEnd"]["skill"])
    for stage in flow["stages"]:
        for group in [stage, *stage.get("lanes", [])]:
            group["entry"], group["support"] = keep(group["entry"]), keep(group["support"])
    for group in flow["across"]:
        group["entry"], group["support"] = keep(group["entry"]), keep(group["support"])
    for item in flow["expertise"]:
        if "only" in item:
            item["only"] = keep(item["only"])
        else:
            keep([k for k, s in skills.items() if s["plugin"] == item["plugin"]])
    flow["expertise"] = [e for e in flow["expertise"] if e.get("only") != []
                         and any(s["plugin"] == e["plugin"] for s in skills.values())]
    flow["paths"] = [p for p in flow["paths"] if p["entry"] in skills]
    for path in flow["paths"]:
        for step in path["steps"]:
            step["skills"] = [k for k in step["skills"] if k in skills]
    return flow


def build(root=ROOT, commit=""):
    flow, skills, placed, problems = check(root)
    flow = prune(flow, skills)
    placed, _, unplaced, _ = placements(flow, skills)
    flow["unplaced"] = unplaced
    for key, where in placed.items():
        skills[key]["home"] = where[0]
    for key in unplaced:
        skills[key]["home"] = "new"
    plugins = {}
    for manifest in sorted(root.glob("plugins/*/plugin.json")):
        data = json.loads(manifest.read_text())
        plugins[data["name"]] = data.get("description", "")
    data = {"flow": {k: v for k, v in flow.items() if k != "$comment"}, "skills": skills, "plugins": plugins}
    digest = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:16]
    data["meta"] = {"hash": digest, "built": date.today().isoformat(), "commit": commit}
    return data, problems, unplaced


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="fail when skill-flow.json is out of date")
    parser.add_argument("--commit", default="", help="source commit to show on the page")
    parser.add_argument("--status", help="write a JSON summary (hash, unplaced skills, problems) to this file")
    args = parser.parse_args()
    data, problems, unplaced = build(commit=args.commit)
    if problems:
        print("skill-flow.json is out of date:\n  " + "\n  ".join(problems), file=sys.stderr)
        if args.strict:
            sys.exit(1)
    page = PAGE.read_text()
    head, rest = page.split(START, 1)
    _, tail = rest.split(END, 1)
    PAGE.write_text(head + START + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + END + tail)
    if args.status:
        Path(args.status).write_text(json.dumps({"hash": data["meta"]["hash"], "unplaced": unplaced,
                                                 "problems": problems}, indent=1))
    placed = len(data["skills"]) - len(unplaced)
    print(f"{placed} of {len(data['skills'])} skills placed, {len(unplaced)} new "
          f"(hash {data['meta']['hash']}) -> {PAGE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
