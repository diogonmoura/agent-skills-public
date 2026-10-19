---
name: postgresql-performance
description: Diagnose and improve PostgreSQL query, locking, connection and maintenance
  performance using representative workload evidence. Use for slow queries, pool pressure,
  plan regressions and resource bottlenecks.
license: MIT
metadata:
  scope: stack-specific
  invocation: both
  role: support
  stack: PostgreSQL
  references: ../../references/sources.md
user-invocable: true
---

# Explain PostgreSQL workload behavior

Establish the server/extension versions, deployment, roles and affected workload before choosing diagnostics. Use existing service objectives or state provisional targets. Read [sources and selection](../../references/sources.md) for upstream context and primary diagnostic documentation.

## Find where time and resources go

Use available pg_stat_statements, activity/wait statistics, locks, pool telemetry and system evidence to distinguish expensive SQL from connection waits, blocked transactions, I/O, CPU, serialization and excessive result transfer. Confirm extension access and collection/reset intervals before interpreting totals. Inspect representative parameter/data/tenant distributions and concurrency; averages can hide a consequential tail.

Start with a non-executing EXPLAIN when execution would exceed the authorized impact.

- EXPLAIN ANALYZE executes the statement, including writes and invoked functions; even SELECT can be expensive or cause effects.
- A rollback cannot undo sequence consumption or external function effects.
- Use a suitable bounded target and privacy-safe inputs.
- Match available EXPLAIN options to the server version.

Compare estimated versus actual cardinality, loops, filtering, buffers and spills. A sequential scan may be optimal; an index-only scan still depends on visibility information. Statistics, skew, parameter-sensitive/prepared plans, expression shape, sort/pagination and result volume can matter more than a missing index. Diagnose one supported hypothesis rather than turning every plan node into a defect.

## Choose changes with explicit costs

Derive index keys/order, included columns, predicates and operator classes from real access patterns and selectivity.

- Account for index size, write amplification and vacuum/maintenance.
- Partition only when workload pruning or lifecycle/maintenance needs justify its restrictions.
- Compare query rewrites against semantics, including nulls, order and duplicate behavior.

Budget connections across processes, workers, rollout overlap and administration.

- Pool wait may reveal long transactions or blocked work; increasing max_connections alone can worsen pressure.
- Verify transaction/session pooling against prepared statements, temporary/session state and tenant identity handling.
- Memory settings multiply across operations and concurrent sessions; tune the measured scope rather than applying global recipes.

Investigate long transactions, dead tuples, autovacuum progress and replication lag together. Repeated manual vacuum or larger resources can hide the cause. Avoid reducing durability or changing isolation merely to obtain a benchmark win.

## Verify the workload result

Validate comparable before/after latency, throughput, correctness and write/resource costs.

- State data size, load, cache conditions and evidence limits.
- Return the supported explanation and tested change; use actual deployment signals for regression monitoring only when that action is authorized.