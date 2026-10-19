---
name: postgresql-development
description: Develop or review PostgreSQL schemas, transactions, migrations and access
  policies. Use for SQL, data integrity, concurrency and engine-specific persistence
  behavior with the actual application roles and server version.
license: MIT
metadata:
  scope: stack-specific
  invocation: both
  role: support
  stack: PostgreSQL
  references: ../../references/sources.md
user-invocable: true
---

# Implement the PostgreSQL data contract

Identify the actual PostgreSQL version, hosting model, extensions, application roles, driver and migration tooling. Preserve accepted project choices. Establish the affected invariants and workload; if broader design is unresolved, use available data/service-design expertise or project evidence without requiring another plugin. Read [source selection](../../references/sources.md) for provenance and version-matched primary references.

## Represent facts and authority

Choose types, constraints and keys from meaning and access patterns. Use appropriate numeric/time semantics and distinguish null, empty and absent values. Enforce durable uniqueness and relationships where they express the contract. JSONB, arrays, generated columns, partitioning and extensions are conditional tools with update, validation, indexing and operational consequences.

Use parameterized values through the actual driver; dynamic identifiers need separate validation/quoting. Derive tenant/resource authority from verified context. Application authorization remains necessary for allowed operations. Where row-level security is selected, verify role ownership, BYPASSRLS/superuser behavior, USING and WITH CHECK semantics, and relevant functions/views. A custom session variable alone does not establish a trusted identity; check who can set it and how pools scope/reset it. Test policies through the actual application role, including cross-tenant reads and writes.

## Handle concurrent operations deliberately

Choose transaction/isolation and locking behavior for the invariant. Keep transactions bounded and avoid waiting on remote work while holding locks. Use constraints and atomic statements where they settle races. Serializable/deadlock retries must repeat the complete logical transaction safely, with bounded attempts and durable side-effect handling. Advisory locks require a stable ownership/lifecycle convention; they do not replace constraints or authorization.

## Change schemas with operational evidence

Examine lock modes, table size, existing values, write traffic, replicas and concurrent application versions before migration. Separate compatible structure, bounded backfill, constraint validation and cleanup when appropriate. Concurrent index creation has transaction, failure and invalid-index consequences; choose it for the deployment rather than requiring it for every index. Set bounded lock/statement behavior through the accepted tooling and plan retry/forward recovery. Verify before removing old representations.

Exercise the affected SQL and migration on representative PostgreSQL data with actual roles, not an engine substitute. Inspect persisted state after failures, duplicate/conflicting requests and version transitions. Report proposed versus executed work and keep live mutation inside the user's named target and authorization.
