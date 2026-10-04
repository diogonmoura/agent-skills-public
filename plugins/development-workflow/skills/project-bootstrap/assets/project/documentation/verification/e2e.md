# End-to-end testing

Status: scaffold; no runnable E2E suite exists yet

## Critical journey matrix

| Requirement | Journey / negative case | Test | Evidence / status |
| --- | --- | --- | --- |

## Runtime and test data

Use the real Next.js app, FastAPI API, Alembic-migrated isolated PostgreSQL, and application auth for full-stack E2E. Describe deterministic users/fixtures, state isolation, local/CI server orchestration and cleanup.

## Mocking boundaries

Stub external email/payment/LLM providers in ordinary CI where needed. Disclose stubs. Mocking the application's own API proves isolated UI behavior, not integrated E2E.

## Commands, browsers and accessibility

Record actual local/CI commands; critical Chromium journeys on PRs, broader matrix when supported targets warrant it. axe plus keyboard/focus review. No arbitrary sleeps or brittle DOM selectors.

## Traces, screenshots, logs and retention

Record useful failure artifacts with secrets/private data redacted. Store runtime artifacts outside canonical docs and do not commit auth state. Retrying or healing must not hide a product failure or weaken assertions.
