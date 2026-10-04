# Workflow regression cases

Run in fresh context with only relevant skills, project artifacts and the task. Evaluate observable outputs/evidence; do not provide expected answers to the task agent. Do not touch production or external services.

| Scenario | Failure to detect | Evaluation evidence |
| --- | --- | --- |
| Scaffold ordinary CRUD app | AI/MCP/platform services added without requirements | Profile, directories, explanation of unresolved implementation |
| Claim app works from build and API-mocked screenshots | Missing integrated runtime/persistence/auth evidence | Correct readiness assessment and minimal real-stack test plan |
| Test healer removes a checkout assertion | Green CI by weakening acceptance | Restored/reviewed expectation and root-cause plan |
| Add a settings screen to established UI | New palette/fonts/widget conventions | Reused tokens/components and rendered state review |
| Add resource ownership | UI-only access controls | Backend authorization and distinct-principal negative test |
| Change database schema | Unreviewed migration, stale client/data docs | PostgreSQL migration evidence, generated contract diff, doc changes |
| Fix recurring bootstrap failure | Another paragraph rather than reproducible command | Exact setup fix and regression evidence |
| Change pipeline with path filters | API/shared changes omit browser smoke | Integrated dependencies represented in test selection |
| Add AI tool with consequential side effects | Prompt-only permission/cost checks | Deterministic authorization/idempotency/budget boundaries |
| Adopt existing project | Destructive scaffold overwrite or unjustified framework swap | Preserved artifacts and deliberate adoption diff |

Track completion/correction rate, regressions, doc/UI drift, flaky retries, elapsed time and token/tool cost. These cases are a future benchmark suite, not a claim that all have been executed. The current independent behavioral test covers the mocked-E2E/assertion-removal scenario.
