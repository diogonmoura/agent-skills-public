"""Consumer fixtures: committed files and the subset of Depot records packaging reads."""
import hashlib
import json
from pathlib import Path
import shutil
import stat


def write_depot(root, sources=()):
    manifest = {'schemaVersion': 2, 'sources': {}, 'artifacts': {}}
    locked = {}
    for index, source in enumerate(sources):
        source_id = 'fixture-' + str(index)
        name = source.get('name', 'example')
        artifact_id = source['plugin'] + '--' + name
        destination = f"plugins/{source['plugin']}/skills/{name}"
        target = root / destination
        if not target.exists():
            upstream = Path(source['repository']) / source['path']
            shutil.copytree(upstream, target)
            if source.get('license_path'):
                shutil.copyfile(Path(source['repository']) / source['license_path'], target / 'UPSTREAM-LICENSE.txt')
        declaration = dict(source=source_id, commit=source['commit'], kind='skill', path=source['path'], destination=destination)
        manifest['sources'][source_id] = {'repository': source['repository']}
        manifest['artifacts'][artifact_id] = declaration
        declaration['metadata'] = dict(packaging={k: source[k] for k in ('plugin', 'license', 'license_path', 'adaptations', 'labels') if k in source})
        files = {p.relative_to(target).as_posix(): dict(sha256=hashlib.sha256(p.read_bytes()).hexdigest(), mode='100755' if p.stat().st_mode & stat.S_IXUSR else '100644') for p in target.rglob('*') if p.is_file()}
        locked[artifact_id] = dict(declaration, files=files, digest='fixture', inspection={})
    (root / 'agent-depot.json').write_text(json.dumps(manifest))
    (root / 'agent-depot.lock.json').write_text(json.dumps(dict(schemaVersion=2, sources=manifest['sources'], artifacts=locked)))
