# Project contract

## Layout

- Root: AGENTS.md, README.md, project-profile.json, workspace orchestration/configuration.
- applications/api/: Python code, pyproject.toml, uv.lock, migrations, tests, Dockerfile, ci/ scripts, scoped AGENTS.md.
- applications/web/: Next.js code, package.json, package lock, components.json, tests, optional Dockerfile, ci/ scripts, scoped AGENTS.md.
- applications/tooling/: shared validation and development scripts.
- documentation/: product, architecture, decisions, planning, UX, operations, and verification.
- .github/workflows/: GitHub Actions entrypoints calling application-local commands/scripts.

AI and MCP modules default to applications/api/src/ai and src/mcp when used. Create a separate application only if lifecycle, scaling, or deployment requires it. Shared libraries are added only when actual reuse exists.

## Defaults and adoption

uv/Python and pnpm/TypeScript for greenfield work; preserve existing package management during adoption. Pin actual stable, compatible versions and commit lockfiles. Select hosting through an ADR; Vercel is a frontend option, not an automatic backend or PostgreSQL deployment decision.

Start with a walking skeleton that proves a browser → API → PostgreSQL flow. Establish design tokens and one representative screen. Add AI/MCP only after a requirement warrants it.

The bundled scaffold creates governance and docs only. Never overwrite an existing project with scaffold output; use it in a separate staging directory and merge deliberately.

## Done

Affected acceptance criteria satisfied; relevant lint/types/build/tests passed; migration and generated-contract checks passed where applicable; rendered UI inspected for UI changes; affected docs updated; unresolved risks stated. Structural validation does not prove semantic documentation correctness.
