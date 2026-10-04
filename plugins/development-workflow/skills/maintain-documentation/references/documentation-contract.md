# Documentation contract

Use short Markdown documents with status, owner, review trigger, and related requirement/ADR links where useful. Start lean; expand sections only as facts and complexity require.

| Path | Purpose and contents |
| --- | --- |
| README.md | Navigation, implemented versus planned scope, how to run and verify |
| product/prd.md | Problem, users, outcomes, scope/non-goals, functional requirements with IDs, acceptance criteria, constraints, risks, open questions |
| product/roadmap.md | Now/next/later outcomes, rationale, dependencies; estimates explicitly labelled |
| plans/ | Feature plans: requirement IDs, slices, dependencies, validation, rollout, status |
| architecture/overview.md | arc42-inspired goals/constraints, context, solution strategy, building blocks, runtime/deployment, quality scenarios, risks, glossary |
| architecture/c4/ | System context and container diagram sources; components when useful |
| architecture/data-model.md | Entities, relations, constraints, ownership, lifecycle, indexes |
| architecture/schemas/ | Generated API/JSON/database contracts and regeneration instructions |
| decisions/adr/ | Numbered ADRs: status, context, decision, alternatives, consequences, supersession |
| decisions/decision-log.md | Dated smaller decisions and ADR links; authoritative history |
| ux/design-system.md | Tokens, components, navigation/forms/states, accessibility, responsive patterns |
| operations/runbook.md | Deployment, configuration, health, alerts, backup/restore, recovery and incidents |
| verification/strategy.md | Appropriate tests, CI commands, acceptance evidence, generated-contract checks |
| verification/traceability.md | Requirement → implementation → test/evidence mapping |
| verification/ai-evaluations.md | Conditional AI datasets, criteria, fixture/live split, provider configuration, limitations |

Review documentation in the same change when behavior, boundaries, contracts, schema, deployment, UX, or decisions change. Record rejected alternatives only when relevant to the decision. Generated schemas derive from code; SQL migrations remain the database evolution authority. Documentation must not promise features that exist only in a plan.

References: https://arc42.org/overview/ ; https://c4model.com/diagrams ; https://adr.github.io/madr/

Additional default documents: engineering/agent-harness.md (context/command map), engineering/lessons.md (evidence-based correction log), verification/e2e.md (journey matrix and runtime/evidence), operations/delivery.md (CI/release/recovery), operations/observability.md (signals and budgets), architecture/security.md (actual trust/data boundaries). Apply a change-impact review; expand depth with real complexity rather than filling templates with invented facts.
