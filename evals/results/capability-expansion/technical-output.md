# Bounded technical forward test

These are diagnosis and repair plans for the three supplied scenarios. Only the scenario descriptions and the guidance listed below were inspected. No application source, actual saved plan/configuration files, database target, packed artifact, or running service was supplied to this test; conclusions beyond the stated facts remain hypotheses. No queries, configuration changes, code edits, installations, publication, service execution, or tests were performed.

## 1. PostgreSQL report, pool pressure and tenant context

**Supported diagnosis.** A sequential scan for an estimated 60% of a table can be appropriate: fetching most rows through indexes can cost more than scanning. Estimated plan costs/cardinalities do not establish actual elapsed time or selectivity. End-to-end latency includes pool wait, so optimizing the scan alone may miss the dominant delay. Indexing every filter column and doubling `max_connections` are unsupported remedies; both can increase resource pressure, and indexes impose write/storage/maintenance costs.

**Scoped plan.** Preserve PostgreSQL, the application language, driver, hosting model and existing migration tooling. Establish deployed version, accepted latency/throughput commitments, pool mode and per-process limits from supplied configuration. From authorized saved traces/configuration only, separate acquisition wait, transaction/query time, result transfer and application work; compare tenant/parameter distributions, report frequency, tail latency, concurrent load and transaction duration. Inspect supplied plans for estimate quality, predicates, prepared/parameter-sensitive behavior, joins, sorting/spills and output volume. Treat absent telemetry as an evidence gap. Do not infer buffers, execution cardinalities or runtime from estimated plans.

Do not run `EXPLAIN ANALYZE`, even on a SELECT: report functions can write audit records. A transaction rollback is not a blanket safeguard for sequence or external effects. No diagnostic SQL, including non-executing EXPLAIN, is authorized against an unavailable target. A later bounded, separately authorized representative environment could compare actual plans and side effects after reviewing function behavior.

Choose one evidence-backed change at a time: narrower report/output or pagination where semantics permit; corrected statistics if demonstrated stale/skewed; an index whose column order, expressions, predicate and operator class match selective access; shorter transactions, controlled report concurrency or pool sizing if wait is dominant. Budget database connections across all app processes/workers, deployment overlap and administration; assess CPU/I/O/memory and server limits before any increase. Pool wait can mean blocked or long-lived work, not insufficient server connection slots. Preserve ordering, duplicates, null behavior and audit semantics.

**Tenant correctness is a separate required check.** `app.current_tenant` is mutable session state, not a trusted identity by itself. Trace verified request authority to tenant selection; inspect who can set the variable, absent/malformed behavior, checkout/reset/error paths and transaction-versus-session pooling. Where appropriate, design transaction-local tenant state scoped to each complete transaction; do not assume a reset convention establishes authorization. Inspect shared-role ownership, superuser/BYPASSRLS, RLS USING/WITH CHECK, views and SECURITY DEFINER/function privileges. Plan actual-app-role tests for cross-tenant reads/writes and audit attribution, including connection reuse, rollback and cancellation. Do not claim isolation before these execute.

**Later verification and recovery.** On an authorized representative PostgreSQL target, compare correctness, p50/p95/p99 request and pool/query latency, throughput, write/audit costs and CPU/I/O/memory under matching data, tenant mix, cache state and concurrency; record sample size/duration. If an index is chosen, plan lock impact, supported concurrent creation, invalid-index cleanup and recovery through accepted migrations. Define rollback/forward recovery and deployment regression signals before rollout. Here, no speedup, resource budget or tenant-isolation result was measured.

## 2. TypeScript utility library packaging and browser support

**Supported diagnosis.** Workspace source imports bypass the published `dist/index.js` entrypoint, so they cannot establish package usability. A `tsconfig` paths alias can satisfy type resolution without rewriting emitted imports or configuring runtime resolution. Transpilation without checking can ship type errors. Node `Buffer` availability in declarations does not provide the API in browsers.

**Scoped repair.** Retain the utility-library scope, current bundler, module format(s), runtime/browser commitments, compiler/package-manager versions and lockfile policy; introduce neither React nor compulsory dual ESM/CommonJS publishing. Inspect package exports/type/files metadata, scripts, relevant compiler settings, bundler alias behavior, emitted JS/declarations and accepted consumer matrix. Keep exports pointing to actual distributed artifacts. Resolve the internal import using the existing bundler's supported bundling/rewriting mechanism or a valid relative emitted import; verify both runtime JS and public declarations contain no unresolved private/source aliases or unpublished paths. Keep promised public types/values aligned and dependencies correctly declared.

Add a separate type-check step with the existing supported compiler and project configuration; a successful build is insufficient if it only transpiles. Use relevant strictness already accepted, without requiring a broad migration. Fix the Buffer helper within the browser contract: use suitable portable byte/encoding APIs, or maintain explicit runtime-specific implementations behind the already accepted export strategy. Preserve actual input/output, Unicode/binary and error semantics. Do not assume TextEncoder is a drop-in replacement for every Buffer operation, inject an unapproved global polyfill, or silently narrow browser support.

**Verification plan.** With existing available tooling, inspect a locally produced package archive and its file list; exercise the actual exported entrypoint from a representative external consumer that cannot resolve workspace source aliases. No publishing is required. Check declared public types with supported consumer compiler/resolution settings and load/run exported values in each promised runtime/module format. Produce the accepted bundler's browser production bundle, inspect Node built-ins/globals and execute helper behavior in the promised browser target, including encoding/error cases. Change relevant workspace checks to also consume intended exports/build outputs so source-only success cannot hide distribution failures; retain intentional direct-source workflows only where they are a separate supported contract. Verify current lint/tests/build plus the explicit type check, packaging and external-consumer checks. These are proposed checks only; no archive, compiler, consumer or browser execution was performed, and no package compatibility is established by this plan.

## 3. Go request goroutines and shutdown

**Supported diagnosis.** An unguarded result send can keep a goroutine blocked after its handler stops receiving. Cancellation is cooperative. Reusing an already-cancelled service context for `http.Server.Shutdown` prevents a useful graceful-drain budget. `context.WithoutCancel` alone removes cancellation/deadline propagation without supplying ownership, completion, a bound or durability. A passing race detector covers only observed data races on exercised paths; it does not prove absence of leaks, deadlocks, logical races or unexercised races.

**Scoped design.** Preserve framework, package layout, dependencies and supported Go version. Inventory each request task, application worker and WebSocket: owner, admission, cancellation, deadline, completion tracking, blocking points and cleanup. Prefer direct context-aware work if the per-handler goroutine has no necessary purpose. Where concurrency is required, propagate the request context through work and make result publication cancellation-aware; bound fan-out and ensure the consumer can depart without stranding the sender. A suitably bounded one-result buffer can avoid that particular blocked send, but cannot make blocked computation terminate. Assign channel closure to a clear owner and never close while a sender can still send. Ensure external operations honor deadlines or have a documented interruption strategy.

Give accepted background jobs an explicit service-owned, bounded lifecycle, completion/error tracking and a persistence/retry decision if they must survive restart. Do not detach all handler work with WithoutCancel. If supported and justified for a narrowly bounded cleanup, a detached context still needs an independent timeout and owned completion; choose APIs compatible with the project's version.

Design shutdown around actual ownership: stop admission/readiness; create a fresh independent context with a finite drain deadline; invoke server shutdown and await its result. Distinguish stopping admission from cancelling all in-flight request contexts: early service cancellation can abort requests intended to drain, so choose that timing deliberately for the existing BaseContext/framework behavior. Stop/drain or cancel tracked workers according to accepted-job semantics, preserving resources needed by in-flight work until it completes. Handle WebSockets/hijacked connections explicitly: stop upgrades, notify/close/drain tracked connections and wait within the budget; Server.Shutdown does not handle them automatically. Shutdown callbacks are not themselves a completion barrier. Define timeout escalation/forced closure, unfinished-work recovery and final client/resource cleanup, with errors returned to the responsible process boundary.

**Verification plan.** With the existing supported toolchain and project commands, run relevant build/static checks and behavioral tests, then race detection where supported. Use deterministic synchronization and bounded completion assertions for cancellation before work, during external work and while publishing results; abandoned receivers; normal results/errors; concurrent cancellation/shutdown; long-running handlers; tracked workers; WebSockets; deadline expiry and escalation. Verify no owned goroutine remains blocked, shutdown returns within its budget and resources are released once. Test accepted-work outcomes on forced exit according to the durability contract. Use existing diagnostics if leaks/blocking remain; neither a raw goroutine count nor a race-pass proves correctness. No Go command, service or concurrency test was executed here.

## Guidance/resources actually read

All paths below are under `plugins/`:

- `database-development/plugin.json`
- `database-development/skills/database-performance/SKILL.md`
- `database-postgresql-development/plugin.json`
- `database-postgresql-development/skills/postgresql-development/SKILL.md`
- `database-postgresql-development/skills/postgresql-performance/SKILL.md`
- `database-postgresql-development/skills/postgresql-operations/SKILL.md`
- `database-postgresql-development/references/sources.md`
- `typescript-development/plugin.json`
- `typescript-development/skills/typescript-conventions/SKILL.md`
- `typescript-development/skills/typescript-conventions/references/modules-and-packaging.md`
- `typescript-development/skills/typescript-conventions/references/sources.md`
- `go-development/plugin.json`
- `go-development/skills/go-conventions/SKILL.md`
- `go-development/skills/go-conventions/references/lifecycle-and-errors.md`
- `go-development/skills/go-conventions/references/verification-and-performance.md`
- `go-development/skills/go-conventions/references/sources.md`

The resource inventory was obtained by listing files in those four plugin directories. Linked upstream/first-party pages were not opened; their inclusion in the local source lists is provenance, not evidence of external reading or version-specific validation. No other skills, prior results or evaluation rubrics were read. The sole written artifact is this report.
