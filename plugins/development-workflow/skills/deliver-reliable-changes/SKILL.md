---
name: deliver-reliable-changes
description: "Configure or review application CI/CD, reproducible setup, safe migrations/releases, security and observability essentials, post-deploy smoke tests and recovery appropriate to project risk."
---

# Reliable application delivery

Read `references/delivery-contract.md`, the actual environment and project-profile.json. Scale mechanisms to product risk and lifecycle; do not impose Kubernetes, a platform control plane, paid telemetry or a new cloud account on every prototype.

Make local verification and CI use the same committed scripts/locks/runtime versions. Configure fast lint/type/unit checks, real PostgreSQL integration/migrations, build/contract checks and critical browser E2E. Keep full-stack smoke coverage when path filtering changes any integrated dependency. Cache keyed by locks; never cache secrets. Set job timeouts and deliberate concurrency cancellation.

Keep GitHub workflow entrypoints at root and application implementation scripts in applications/. Review upstream GitHub Actions hardening guidance: least token permissions, pinned reviewed third-party action revisions, environment scoping, untrusted PR handling and OIDC where supported. Record actual permissions and deployment authority; CI configuration is not blanket authorization to deploy.

Build immutable artifacts where the hosting model permits and promote the tested revision. Use isolated previews/staging without production credentials/data. Configure release and post-deploy smoke commands plus a rollback or forward-recovery path. Plan database expand/contract and backfills; an application rollback does not automatically reverse a schema migration.

Embed project-relevant security: resource authorization, validated inputs, protected secrets, dependency/secret scanning, safe upload/webhook handling and narrow CORS. Add tenant isolation only where multi-tenancy exists. For money/calculation-heavy code use decimal handling and explicit units; for async side effects use idempotency and bounded retries. Treat these as project-specific contracts, not speculative features.

Provide structured logs/request correlation, useful health/readiness, and observable critical failures. Add basic user-flow latency/error indicators and explicit performance/resource/AI-cost budgets as needs arise. Use existing telemetry or vendor-neutral instrumentation rather than a mandatory vendor. Record retention/redaction and recovery procedures.

Report runnable verification, release evidence, known limitations and operational ownership. Never label a prototype production-ready solely from lint/build/structure checks.
