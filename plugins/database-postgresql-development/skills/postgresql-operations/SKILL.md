---
name: postgresql-operations
description: Plan or perform scoped PostgreSQL backup/recovery, maintenance, replication
  and upgrades. Use for operating procedures and readiness with the actual hosting
  model, recovery objectives and authorized target.
license: MIT
metadata:
  scope: stack-specific
  invocation: both
  role: support
  stack: PostgreSQL
  references: ../../references/sources.md
user-invocable: true
---

# Operate PostgreSQL with a verified recovery path

Identify the authorized cluster/database, version, hosting model, topology and operating commitments. Reuse accepted recovery objectives and procedures. Read [sources](../../references/sources.md) for version-specific PostgreSQL and reviewed upstream material. Managed-service controls differ from self-hosted server access; do not invent superuser, filesystem or control-plane capabilities.

## Establish recoverability

Choose logical backup, physical backup/WAL recovery, managed snapshots/PITR or a combination from the recovery unit, downtime, retention and failure model.

- Include roles/global objects, extensions, encryption/access, dependencies and recovery configuration.
- A replica shares many failure and deletion modes and is not an independent backup.
- Continuous recovery depends on a usable base and the required WAL chain; monitor retention and restoreability, not just successful job completion.

Exercise recovery on an authorized isolated target.

- Verify a known recovery point, application compatibility, representative records/invariants and access, then measure actual recovery time and attainable data loss.
- Keep restored deletion/retention obligations and traffic cutover explicit.
- Distinguish a documented procedure, successful backup and successful restore; none automatically establishes full application recovery.

## Maintain health without hiding risk

Assess connections, long transactions, disk/WAL growth, vacuum/freeze, replication slots and lag against workload and retention.

- Slots can retain WAL; replicas can lag or conflict with recovery.
- Investigate cause and consequences before dropping slots, cancelling work or changing durability.
- Define primary/failover authority and fencing against split-brain; promotion alone does not prove clients moved or application writes are correct.

For minor/major upgrades, check supported server/extension/driver combinations, storage needs and tooling.

- Compare in-place, logical replication or dump/restore strategies against downtime and reversibility.
- Rehearse meaningful data and query/role compatibility, validate the new target, and define cutover, stale-writer prevention and forward recovery.
- Avoid claiming binary rollback after new writes unless that path is demonstrated.

## Execute and report within scope

Use the named target and supported operational tooling. Confirm impact, resource/traffic boundaries and recovery route before consequential live work; existing authorization remains valid. Continue independent planning when access is unavailable. Protect backups and reports from secrets/personal-data exposure, retire temporary restored targets only within authorized cleanup, and report actual actions, evidence, remaining risks and operating ownership.
