# Tenant and commercial lifecycle decisions

Read when a change affects customer lifecycle, payment state or persisted tenant work. Use only the transitions relevant to the requested product.

| Transition | Establish | Evidence that matters |
| --- | --- | --- |
| Create/join organization | Creator authority, recipient proof, duplicate joins, initial roles and resource ownership | Concurrent creation/invitation, rejected recipients and persisted membership |
| Transfer/remove membership | Grant limits, last-owner policy, active sessions/jobs and resource ownership | Old and new identities after the change, including stale cache/token windows |
| Trial/upgrade/downgrade | Effective time, entitlements, existing data/work, quotas and customer-visible consequences | Before/after capability decisions and in-flight operations |
| Receive provider event | Authentic source, event/business identity, environment mapping and durable progress | Duplicate, delayed, conflicting and interrupted handling; reconciliation to provider state |
| Record usage | Definition/unit, tenant/billing attribution, late/corrected events and idempotency | Reconciliation from authoritative events to aggregated allowance/invoice inputs |
| Suspend/cancel/reactivate | Access versus processing versus billing, grace/retention and reinstatement rules | Existing sessions, jobs, scheduled operations and restored entitlements |
| Export/delete tenant | Requesting authority, retention exceptions, derived stores/providers and backups | Accessible export, scoped deletion and prevention of unintended data reactivation on restore |

A durable handler needs a recovery story for incomplete work, not just an event-ID table. Separate received, progressing and completed effects when those states matter. Choose atomic local updates, an outbox or reconciliation from actual failure boundaries; a universal workflow engine is unnecessary. Provider API versions and retries/order guarantees must be verified against the selected integration.

For model ownership and lifecycle evidence, inspect the pinned references in the [package source review](../../../references/sources.md). Starter examples illustrate concerns, not complete production contracts.
