---
name: database-design
description: Design or evolve stored data, constraints, transactions and migration
  behavior independently of a database engine. Use for persistence choices, schema
  changes, consistency boundaries and data lifecycle decisions.
license: MIT
metadata:
  scope: generic
  invocation: both
  role: support
user-invocable: true
---

# Design data around invariants and use

Start with the accepted domain, workloads and data lifecycle. Identify authoritative records, derived representations, ownership, access paths and the consequences of stale, missing or conflicting data. Preserve the selected storage model unless evidence and scope justify changing it. A small schema change need not reopen the entire architecture.

## Choose representations and consistency boundaries

### Invariants

State the business facts that must remain true, including identity, uniqueness, relationships, lifecycle and tenant ownership.

- Determine which guarantees belong in durable constraints and which need coordinated application behavior.
- Consider deletion, history and correction semantics before choosing keys and references.
- Document units, precision, null/absent meanings and time semantics where ambiguity changes behavior.

### Storage and derived representations

Use expected reads, writes, distribution, growth and failure tolerance to compare relational, document, key/value, object, search or analytical storage.

- Extra representations carry synchronization and recovery costs.
- Treat replicas, caches and indexes as derived until their authority and consistency contract are explicit.
- Workload or availability requirements must justify denormalization, partitioning or a new engine.

### Atomic operations

Define the atomic operation and conflict behavior.

- Account for concurrent creation/update, retries, isolation, uniqueness and stale writers.

A transaction in one store does not make remote side effects atomic. Derive idempotency or reconciliation needs from actual failure boundaries, using suitable service-design expertise when available.

## Evolve without losing the contract

Assess readers, writers, queued work and supported application versions against a schema change.

- Separate structural changes, data conversion and final cleanup.
- Choose compatibility steps, bounded resumable backfills and validation from deployment constraints; an expand/migrate/contract approach is useful when versions overlap.
- Define completion, rejected/ambiguous data handling and recovery before irreversible conversion.

Code rollback may not undo stored data changes.

Include access, retention, export and deletion across derived stores, providers and restored backups. Define recovery objectives and seek operating expertise for actual restoration evidence. Distinguish missing guidance from missing database access; neither authorizes connecting to an unspecified target.

## Establish useful evidence

Verify invariants under relevant races and failures, migration from representative existing data, old/new consumer compatibility, access isolation and persisted behavior. Select matching engine/driver expertise from available descriptions; otherwise use project evidence and version-matched first-party documentation. Return the accepted/proposed data decisions, change strategy and actual verification limits at the requested stopping point.
