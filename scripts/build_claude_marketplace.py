#!/usr/bin/env python3
"""Add a Claude Code marketplace manifest to a complete build output."""
import argparse
import json
from pathlib import Path


def write_marketplace(destination, name, owner):
    plugins = []
    for manifest_path in sorted(destination.glob('*/plugin.json')):
        manifest = json.loads(manifest_path.read_text())
        plugins.append({
            'name': manifest['name'],
            'source': './' + manifest_path.parent.name,
            'description': manifest.get('description', ''),
            'version': manifest['version'],
        })
    marketplace = {
        'name': name,
        'owner': {'name': owner},
        'description': 'Portable SDLC, strategy and operations skill bundles built from agent-skills-public.',
        'plugins': plugins,
    }
    target = destination / '.claude-plugin' / 'marketplace.json'
    target.parent.mkdir()
    target.write_text(json.dumps(marketplace, indent=2, ensure_ascii=False) + '\n')
    return len(plugins)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--built', type=Path, required=True, help='Output of build_plugins.py --all')
    parser.add_argument('--name', default='agent-skills-public')
    parser.add_argument('--owner', default='João Aires')
    args = parser.parse_args()
    built = args.built.resolve()
    count = write_marketplace(built, args.name, args.owner)
    print(f'Added Claude Code marketplace manifest for {count} plugins at {built}')


if __name__ == '__main__':
    main()
