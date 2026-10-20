import { execFileSync } from 'node:child_process';
import { appendFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const temp = process.env.RUNNER_TEMP;
if (!temp) throw new Error('A trusted runner temporary directory is required');
const cli = (...args) => JSON.parse(execFileSync(process.execPath,
  ['.agent-depot/tool/dist/cli.js', '--json', ...args], { encoding: 'utf8', timeout: 600000 }));
const artifact = process.env.UPDATE_ARTIFACT || '';
const commit = process.env.UPDATE_COMMIT || '';
if (Boolean(artifact) !== Boolean(commit)) throw new Error('Supply both artifact and commit, or neither');
cli('verify');
const discovery = artifact
  ? { schemaVersion: 1, command: 'candidate', result: { artifact, commit, discovery: 'not-requested', artifacts: [] } }
  : cli('outdated');
writeFileSync(join(temp, 'upstream-discovery.json'), JSON.stringify(discovery, null, 2) + '\n');
let changed = false;
if (artifact || discovery.result.artifacts.some(a => a.status === 'update-available')) {
  const output = join(temp, 'upstream-plan.json');
  const report = cli('plan', ...(artifact ? ['--artifact', artifact, '--to', commit] : []), '--output', output);
  changed = report.result.changes.length > 0;
  if (changed) {
    cli('update', '--plan', output);
    // Provenance changes are part of the owning package's distribution contract.
    const { readFileSync } = await import('node:fs');
    const manifest = JSON.parse(readFileSync('agent-depot.json', 'utf8'));
    const plugins = new Set(report.result.changes.map(c => manifest.artifacts[c.artifact]?.metadata?.packaging?.plugin).filter(Boolean));
    for (const plugin of plugins) {
      if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(plugin)) throw new Error('Invalid owning plugin');
      const path = `plugins/${plugin}/plugin.json`;
      const data = JSON.parse(readFileSync(path, 'utf8'));
      const parts = data.version.split('.');
      if (parts.length !== 3 || !parts.every(p => /^\d+$/.test(p))) throw new Error('Expected stable package SemVer');
      parts[2] = String(Number(parts[2]) + 1);
      data.version = parts.join('.');
      writeFileSync(path, JSON.stringify(data, null, 2) + '\n');
    }
    const changes = report.result.changes.map(c => `- ${c.artifact}: ${c.oldCommit} → ${c.newCommit}; ${c.added.length} added, ${c.changed.length} changed, ${c.removed.length} removed files.`);
    writeFileSync(join(temp, 'upstream-update.md'), [
      '## Summary', '', 'Update accepted upstream skill snapshots at the exact commits in the attached plan, and bump owning package patch versions.', '', ...changes, '',
      '## Validation', '', 'The workflow verifies snapshot integrity and runs package validation, regression tests and a complete build before publishing this candidate.', '',
      '## Review', '', 'Inspect upstream instructions, resources, licenses and effective adapted output for semantic changes. File integrity and packaging checks do not establish agent behavior. No automatic merge or client installation is performed.', ''
    ].join('\n'));
  }
}
if (process.env.GITHUB_OUTPUT) appendFileSync(process.env.GITHUB_OUTPUT, `changed=${changed}\n`);
console.log(changed ? 'Prepared a candidate for validation.' : 'No eligible snapshot changes.');
