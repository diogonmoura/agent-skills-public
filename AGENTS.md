# Repository instructions

This repository distributes portable Agent Plugins v1.0.0. Read documentation/plugin-design.md before restructuring it.

- Canonical plugin packages live in plugins/<name>/ with plugin.json and skills/<name>/SKILL.md; optional mcp.json belongs at that package root.
- Preserve existing skill names and full references/assets/evals during migration.
- Keep each plugin self-contained: no skill reference or symlink may escape its plugin root. Profiles do not imply portable runtime dependency resolution.
- Keep README, profiles, source catalogue, templates, docs, and validators consistent with changes. Mark unimplemented behavior accurately.
- Research and pin third-party sources before vendoring; preserve license and attribution. Never copy user-private installed skills into this public repository.
- Validate manifests against bundled official schemas and run the scaffold regression suite before delivery.
- Do not embed credentials, assume upstream skills are installed, or claim AI validation based only on mocks.
