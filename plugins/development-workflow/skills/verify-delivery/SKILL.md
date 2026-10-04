---
name: verify-delivery
description: "Review application changes against project conventions, acceptance criteria, documentation impact, generated contracts, tests, and deployment readiness before marking work complete."
---

# Verify delivery

1. Read project-profile.json and applicable AGENTS.md files. Determine the actual scope and acceptance criteria from the PRD or change request.
2. Inspect the diff for stack changes, design drift, secrets, authorization gaps, migrations, external side effects, and documentation impact. Apply only checks relevant to the change.
3. Run `python3 applications/tooling/check_project.py .`. Run configured application lint, type checks, build, and meaningful tests. Do not weaken checks or regenerate snapshots merely to make failures disappear.
4. For backend changes, test changed API behavior and use PostgreSQL for persistence integration tests. For frontend changes, inspect rendered screens and test affected user journeys, keyboard use, and responsive states. For AI changes, use deterministic fixtures and a separate live evaluation where appropriate.
5. Update affected docs and generated contracts. If no documentation update is warranted for a meaningful behavior change, explain why in the PR or delivery report.
6. State what changed, validation results, unresolved issues, and any migration/deployment requirements. Do not call a change production-ready solely because structural checks passed.
