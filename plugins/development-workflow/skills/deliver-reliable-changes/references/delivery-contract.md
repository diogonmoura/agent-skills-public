# Delivery contract

## Progressive readiness

- Scaffold: instructions/templates only, no claim of a runnable app.
- Implemented: deterministic setup and dev commands; real primary user journey; tests and usable error/empty/loading states; no fake-data dependency in the claimed flow.
- Deployed: actual environment and smoke evidence; scoped credentials/config; logs and recovery path.
- Production: risk-appropriate auth/security, monitoring, backup/restore, migration/release safety, ownership and cost controls.

These labels communicate verified capability, not arbitrary certification. Critical checks remain required; later lifecycle stages add operational evidence. Optional infrastructure is introduced when justified.

## Defaults to resolve per project

Authentication/session policy; authorization ownership; data classification/retention; deployment provider; contract generation; background jobs and side-effect idempotency; configuration/secrets; backups; observed error/latency goals; resource/cost limits; rollback and migration recovery. Do not turn unknowns into assumed decisions.

## Skill sources

https://github.com/github/awesome-copilot/blob/main/skills/github-actions-hardening/SKILL.md
https://github.com/github/awesome-copilot/blob/main/instructions/github-actions-ci-cd-best-practices.instructions.md
https://github.com/trailofbits/skills
https://github.com/getsentry/skills/blob/main/skills/code-review/SKILL.md

GitHub-hosted awesome-copilot content is community-contributed; its instructions/agent definitions are not all portable SKILL.md packages. Trail of Bits contains specialist skills; select narrowly and preserve its CC-BY-SA license if redistributing. No content is copied into this MIT package merely because a source is referenced.
