# Testing contract

## Layers

| Layer | Purpose | Default |
| --- | --- | --- |
| Unit/use case | Domain invariants and failure branches | pytest for backend; suitable TS test runner for frontend logic |
| API/integration | Validation, authorization, persistence and migrations | Real PostgreSQL; application auth; isolated data |
| Contract | Backend/frontend API alignment | Generated OpenAPI and typed TS client; check schema drift |
| Browser E2E | Critical user outcomes across the application | Playwright Test against Next.js → FastAPI → PostgreSQL |
| Component/visual | Reusable UI states and deliberate visual changes | Focused component cases and reviewed screenshot baselines |
| Accessibility | Keyboard/focus and detectable accessibility violations | axe plus human/agent rendered interaction review |
| AI evaluation | Tool/schema behavior and model quality | Offline fixtures; separate opt-in live Gemini evaluation |
| Performance | User latency and resource/cost constraints | Explicit budgets; load testing as scale/risk requires |

Tests follow product behavior; avoid mirror tests, arbitrary coverage quotas and gigantic brittle E2E suites. Use unit/integration tests for exhaustive edge cases; E2E proves critical integration and user journeys. Property-based tests help calculation/schema/state invariants when worthwhile.

## E2E cases

Document login/session/logout when auth exists; the primary create/read/update journey; persisted state after reload; important negative cases; resource authorization; meaningful loading/empty/error states; a deployed smoke journey where deployment exists. Add payment/webhook/upload/AI scenarios only if the product contains them.

## Reproducibility

Use committed locks, isolated disposable PostgreSQL with Alembic migrations and deterministic synthetic seed data. Run the same project commands locally and in CI. Allocate independent data per parallel worker. Bound execution times and clean up servers/containers even on failure. Live-provider tests must not silently charge or send external messages.

## Evidence

Record commit, environment, command, outcome and artifact location. Report skipped checks and mocked dependencies. Retain failure traces and logs with appropriate retention. Never commit authentication state, tokens or raw private prompts/audio. Add a regression test for fixed behavior bugs.

## Official references

https://playwright.dev/docs/best-practices
https://playwright.dev/docs/test-agents
https://playwright.dev/docs/accessibility-testing
https://github.com/microsoft/playwright-cli
