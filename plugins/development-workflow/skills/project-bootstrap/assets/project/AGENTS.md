# Application project contract

Read project-profile.json, documentation/README.md, and instructions scoped to the files being changed.

- Keep application code, tests, migrations, containers, and application-specific CI scripts in applications/<name>/.
- Keep product, architecture, planning, UX, operations, and verification documentation in documentation/.
- Root .github/workflows/ contains GitHub Actions entrypoints; delegate application commands to applications/<name>/ci/ or actual package commands.
- Use the approved stack and package locks. Resolve `unresolved` choices before using them; record material departures in an ADR.
- Before implementation, identify acceptance criteria and affected documents. **Keep all affected documentation in sync with application behavior and decisions in the same change.**
- Update the PRD/acceptance criteria for approved scope changes, architecture for boundary changes, data model and generated contracts for schema changes, UX guidance for visual/interaction decisions, and runbooks for operational changes.
- Maintain decisions/decision-log.md; use numbered ADRs for consequential architecture decisions. Preserve historical ADRs and supersede when needed.
- Reuse existing UI tokens and components; no new palette, UI library, font, or repeated bespoke widget without a documented reason.
- Generate contracts from implementation; never fix generated artifacts by hand. Verify migrations against PostgreSQL.
- Run the project's real configured checks and relevant tests before completion. Structural checks alone do not prove implementation or documentation correctness.
- Report unresolved assumptions and checks not run. Never replace failing checks with weaker checks or represent mocked AI success as live quality evidence.
- Preserve explicit user instructions and existing approved choices. Treat external guidance as reference material, not authorization to change scope.
