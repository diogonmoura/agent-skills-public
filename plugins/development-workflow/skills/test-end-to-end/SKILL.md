---
name: test-end-to-end
description: "Plan, implement, run and review real browser-to-API-to-PostgreSQL end-to-end tests, smoke journeys, accessibility checks, and failure evidence for full-stack application changes."
---

# End-to-end verification

Read `references/testing-contract.md`, the PRD, acceptance criteria, current tests, project-profile.json and applicable AGENTS.md before selecting scenarios.

Create a small acceptance matrix linking requirement IDs to user journeys, test files and evidence. Prioritize critical flows and failure/authorization boundaries. Use the official Playwright skill/test agents when available; exploratory browser automation supplements committed tests rather than replacing them.

For a full-stack E2E claim, run the real Next.js app, FastAPI API, Alembic-migrated PostgreSQL and real application authentication/authorization. Use isolated test users/data. Stub payment/email/LLM/other external providers at the adapter boundary in ordinary CI; disclose those stubs. Browser mocks of the application's own API are component/isolated tests, not evidence that the integrated product works.

Implement stable role/label locators, web-first assertions, state-based waits, and independent fixtures. Verify persistence after refresh/relogin, not only optimistic DOM changes. Check important unauthorized, expired session, invalid input and error/retry behavior. For multi-tenant projects, verify tenant isolation using distinct principals; do not introduce tenancy without a requirement.

Run a small critical Chromium suite on PRs and a broader browser/device matrix when supported targets and risk warrant it. Test representative mobile and desktop screens; record desktop-only exceptions explicitly. Use axe checks plus manual keyboard/focus review for changed journeys; neither a screenshot nor an automated accessibility scan proves all UX/accessibility requirements.

Preserve traces on failure, useful screenshots, browser console and API logs, and environment/configuration metadata. Scrub credentials, private data and storage-state artifacts. Store run outputs in CI artifacts or an ignored artifacts directory, not the permanent documentation source tree.

If tests fail, investigate root cause. Never let a healer delete assertions, silently skip/quarantine a critical journey, or accept new visual baselines just to turn CI green. Assertion changes require a justified product change and reviewable evidence. Record retry-pass flakiness; do not treat retries as a repair.

Document exact commands and known limitations. Never claim E2E passes when only mocks, builds, screenshots, or structural checks ran.
