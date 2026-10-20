import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtempSync, mkdirSync, readFileSync, writeFileSync, rmSync, copyFileSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { tmpdir } from 'node:os';
import { pathToFileURL } from 'node:url';
import test from 'node:test';

const tool = resolve('.agent-depot/tool/dist/cli.js');
const prepare = resolve('scripts/prepare_upstream_update.mjs');
function fixture(t) {
  const root = mkdtempSync(join(tmpdir(), 'skill-maintenance-'));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  const upstream = join(root, 'upstream');
  const consumer = join(root, 'consumer');
  const reports = join(root, 'reports');
  for (const dir of [upstream, consumer, reports]) mkdirSync(dir);
  function run(command, args, cwd = consumer, extra = {}) {
    return spawnSync(command, args, { cwd, encoding: 'utf8', timeout: 30000, ...extra });
  }
  function git(...args) {
    const result = run('git', ['-c', 'commit.gpgsign=false', '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid', '-c', `core.hooksPath=${join(root, 'no-hooks')}`, ...args], upstream);
    assert.equal(result.status, 0, result.stderr);
    return result.stdout.trim();
  }
  function commit(body) {
    writeFileSync(join(upstream, 'SKILL.md'), `---\nname: example\ndescription: Fixture\nlicense: MIT\n---\n${body}\n`);
    git('add', '.');
    git('commit', '-m', 'Fixture');
    return git('rev-parse', 'HEAD');
  }
  git('init', '-b', 'main');
  const first = commit('Accepted content');
  const next = commit('Candidate content');
  const unavailable = join(root, 'unavailable');
  git('clone', '--bare', upstream, unavailable);
  const manifest = {
    schemaVersion: 2,
    sources: { chosen: { repository: upstream }, unrelated: { repository: unavailable } },
    artifacts: {
      chosen: { source: 'chosen', commit: first, kind: 'skill', path: '.', destination: 'plugins/example/skills/example' },
      unrelated: { source: 'unrelated', commit: first, kind: 'skill', path: '.', destination: 'plugins/other/skills/example' }
    },
    metadata: { packaging: { chosen: { plugin: 'example' }, unrelated: { plugin: 'other' } } }
  };
  writeFileSync(join(consumer, 'agent-depot.json'), JSON.stringify(manifest));
  const cli = (...args) => {
    const result = run(process.execPath, [tool, '--json', ...args]);
    assert.equal(result.status, 0, result.stderr);
    return JSON.parse(result.stdout).result;
  };
  cli('lock');
  cli('sync');
  for (const plugin of ['example', 'other']) writeFileSync(join(consumer, `plugins/${plugin}/plugin.json`), JSON.stringify({ name: plugin, version: '1.0.0' }));
  // Run the real pinned CLI through the same relative entry point as CI.
  mkdirSync(join(consumer, '.agent-depot/tool/dist'), { recursive: true });
  writeFileSync(join(consumer, '.agent-depot/tool/package.json'), '{"type":"module"}');
  writeFileSync(join(consumer, '.agent-depot/tool/dist/cli.js'), `import ${JSON.stringify(pathToFileURL(tool).href)};\n`);
  copyFileSync(prepare, join(consumer, 'prepare.mjs'));
  const read = path => JSON.parse(readFileSync(join(consumer, path), 'utf8'));
  function execute(env = {}) {
    return run(process.execPath, ['prepare.mjs'], consumer, {
      env: { ...process.env, RUNNER_TEMP: reports, UPDATE_ARTIFACT: '', UPDATE_COMMIT: '', GITHUB_OUTPUT: join(reports, 'output'), ...env }
    });
  }
  return { consumer, upstream, unavailable, reports, first, next, manifest, cli, read, execute };
}

test('explicit artifact updates skip discovery for unrelated unavailable tracked repositories', t => {
  const f = fixture(t);
  f.manifest.artifacts.unrelated.track = { branch: 'main' };
  writeFileSync(join(f.consumer, 'agent-depot.json'), JSON.stringify(f.manifest));
  const policy = join(f.reports, 'policy.json');
  f.cli('plan', '--artifact', 'unrelated', '--to', f.first, '-o', policy);
  f.cli('update', '--plan', policy);
  const before = f.read('agent-depot.lock.json').artifacts.unrelated;
  rmSync(f.unavailable, { recursive: true });
  const result = f.execute({ UPDATE_ARTIFACT: 'chosen', UPDATE_COMMIT: f.next });
  assert.equal(result.status, 0, result.stderr);
  assert.equal(f.read('agent-depot.json').artifacts.chosen.commit, f.next);
  assert.deepEqual(f.read('agent-depot.lock.json').artifacts.unrelated, before);
  assert.equal(f.read('plugins/example/plugin.json').version, '1.0.1');
  assert.equal(f.read('plugins/other/plugin.json').version, '1.0.0');
  assert.equal(readFileSync(join(f.reports, 'output'), 'utf8'), 'changed=true\n');
  f.cli('verify');
});

test('scheduled discovery leaves untracked pins and package versions unchanged', t => {
  const f = fixture(t);
  const before = readFileSync(join(f.consumer, 'agent-depot.json'));
  rmSync(f.unavailable, { recursive: true });
  const result = f.execute();
  assert.equal(result.status, 0, result.stderr);
  assert.deepEqual(readFileSync(join(f.consumer, 'agent-depot.json')), before);
  assert.equal(f.read('plugins/example/plugin.json').version, '1.0.0');
  assert.equal(readFileSync(join(f.reports, 'output'), 'utf8'), 'changed=false\n');
});
