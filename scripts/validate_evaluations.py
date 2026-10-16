#!/usr/bin/env python3
"""Check scenario structure and flow references; never execute behavioral trials."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def validate(data):
    errors = []
    if not isinstance(data, dict):
        return ['Evaluation specification must be an object']

    def text(value):
        return isinstance(value, str) and bool(value.strip())

    def strings(value, nonempty=True):
        return isinstance(value, list) and (bool(value) or not nonempty) and all(text(v) for v in value)

    inventories = {}
    for group in ('cases', 'generation_trials', 'flow_matrix'):
        items = data.get(group)
        if not isinstance(items, list) or not items:
            errors.append(f'{group}: expected nonempty list')
            inventories[group] = set()
            continue
        ids = set()
        for item in items:
            if not isinstance(item, dict):
                errors.append(f'{group}: expected object')
                continue
            identity = item.get('id')
            if not text(identity) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', identity):
                errors.append(f'{group}: invalid id')
                continue
            label = f'{group}/{identity}'
            if identity in ids:
                errors.append(f'{label}: duplicate id')
            ids.add(identity)
            if group == 'cases':
                if not text(item.get('prompt')) or not strings(item.get('criteria')):
                    errors.append(f'{label}: prompt and nonempty criteria required')
            elif group == 'generation_trials':
                phases = item.get('phases')
                if not isinstance(phases, list) or not phases or any(
                    not isinstance(p, dict) or not text(p.get('task')) or not text(p.get('prompt')) for p in phases
                ):
                    errors.append(f'{label}: task/prompt phases required')
                if not strings(item.get('evaluation')):
                    errors.append(f'{label}: nonempty evaluation required')
            else:
                if not text(item.get('outcome')):
                    errors.append(f'{label}: outcome required')
                for field in ('case_ids', 'trial_ids'):
                    if not strings(item.get(field), nonempty=False):
                        errors.append(f'{label}: {field} must be a string list')
                if not item.get('case_ids') and not item.get('trial_ids'):
                    errors.append(f'{label}: at least one scenario reference required')
            for field in ('evidence', 'negative_controls'):
                if field in item and not strings(item[field]):
                    errors.append(f'{label}: {field} must be nonempty strings')
            if 'capability_gates' in item and not strings(item['capability_gates'], nonempty=False):
                errors.append(f'{label}: capability_gates must be strings')
            if 'evaluator_setup' in item and not text(item['evaluator_setup']):
                errors.append(f'{label}: evaluator_setup must be text')
        inventories[group] = ids

    covered = {'cases': set(), 'generation_trials': set()}
    flows = data.get('flow_matrix', [])
    for flow in flows if isinstance(flows, list) else []:
        if not isinstance(flow, dict):
            continue
        for field, group in (('case_ids', 'cases'), ('trial_ids', 'generation_trials')):
            refs = flow.get(field, [])
            if not strings(refs, nonempty=False):
                continue
            covered[group].update(refs)
            for missing in sorted(set(refs) - inventories[group]):
                errors.append(f'{flow.get("id")}: unknown {group} reference {missing}')
    for group, refs in covered.items():
        for missing in sorted(inventories[group] - refs):
            errors.append(f'{group}/{missing}: missing flow mapping')
    return errors


def main():
    data = json.loads((ROOT / 'evals/development-workflows.json').read_text())
    failures = validate(data)
    if failures:
        raise SystemExit('\n'.join(failures))
    print(f'Scenario definitions valid: {len(data["cases"])} cases, '
          f'{len(data["generation_trials"])} trials, {len(data["flow_matrix"])} flows; no trials executed.')


if __name__ == '__main__':
    main()
