# SaaS and security forward tasks

These are three independent design deliverables from the supplied scenarios. No application, account, provider configuration, runtime, or tests were inspected or changed. Proposed behavior and verification are not execution evidence.

## 1. Invitations and access changes in the Django application

### Architecture and authority

Retain django-allauth login and Redis-backed sessions. The application database remains authoritative for organization membership and resource permission. A session establishes the user; an active-organization selection establishes requested context only after server-side membership validation. Neither a session role snapshot, client organization ID, email domain, nor a paid subscription grants resource access. Preserve the accepted ownership checks and add membership/lifecycle checks where missing; changing ownership policy is outside this design.

Represent account, organization membership, resource ownership/permission, invitation and commercial entitlement separately. A person has independently scoped memberships in multiple organizations; switching organizations never transfers authority between them. Scope queries, lists, counts, related resources, bulk actions, files, cache keys and exports to the verified organization. Existing endpoint ownership checks alone do not establish these other boundaries.

| Operation | Authority and lifecycle | Persisted effect and visible outcome |
| --- | --- | --- |
| Invite member | Current owner of the target organization, checked at submission; proposed default allows the member role only | Create an expiring invitation for one organization, intended recipient and permitted role; show pending delivery/acceptance separately |
| Accept invitation | Logged-in user with verified control of the invited email; unexpired, unrevoked invitation; recheck current grant policy and inviter authority | Atomically consume the invitation and create one membership; repeated acceptance returns the existing result without elevating a role |
| Change/remove membership | Current owner, target in the same organization, permitted transition; preserve at least one active owner | Commit the new membership state, increment its authorization version and record an audit entry; next protected operation sees the change |
| Manage billing | Finance administrator for that organization, or another explicitly authorized billing role | Change subscription administration only; cannot invite, grant roles, inspect resource exports or change ownership merely through billing authority |
| Transfer ownership | Existing owner with recent reauthentication; eligible recipient; product-approved transfer rule | Atomic transfer that preserves an owner; return an explicit result under concurrent transfers/removals |
| Run/download export | Current membership and accepted resource permissions, plus any independently applicable entitlement | Authorize creation, execution, publication and download against the export's immutable organization and requested scope |

Invitation defaults proposed for acceptance: cryptographically random opaque tokens, only a digest stored; seven-day expiry; revocation and resend invalidate the prior token; one active invitation per organization/recipient; bounded invitation/acceptance attempts; no account-existence disclosure. Tokens do not enter logs or analytics. Invitation creation and email-delivery intent commit together; failed delivery can be retried without creating a second invitation. An already-existing membership is not upgraded by replaying an invitation. Validate owner authority again when accepting so a former owner's outstanding invitation cannot confer authority. Store the intended role server-side and reject substituted recipient, organization or role fields. Match through the application's verified-email identity rules, without inventing new address-normalization rules.

Role updates use a transaction and concurrency control around the affected membership and owner invariant. Concurrent owner removals must not both pass a preflight count. Ownership and membership are separate: removing a member must not silently reassign or delete their resources. Proposed default is that removed members lose access immediately while resources remain in the organization under the accepted ownership rules; orphaned-resource administration needs the product decision below.

### Sessions, jobs and change timing

Do not embed durable authority in the Redis session. Check current membership and permission on each protected request. A changed organization membership does not log the user out of unrelated organizations. Explicit account deactivation or security revocation invalidates all relevant server sessions. Preserve the application's existing login, session rotation, cookie, CSRF and logout protections and verify their actual configuration before implementation.

Proposed revocation contract: once a role/removal transaction commits, any subsequently authorized operation must use the new authority. Do not permit a stale authorization cache to extend this window; first implementation can read the database, with any later cache requiring version validation. Redis/session failure must not turn an unauthenticated request into an authenticated one. Permission-store failure denies protected actions with a retryable service error.

Persist export requester, organization, exact resource scope and membership/permission version; these are audit/context inputs, not a permanent authorization grant. Recheck at dequeue and before each meaningful processing unit. A role change requests cancellation; workers cooperatively stop and withhold partial results. Before publication, recheck authority under the same ordering/locking discipline as the role change so a concurrent change cannot publish under stale authority. A job that cannot safely stop mid-unit may finish that unit privately, then discard or quarantine output. Download always checks current authority; avoid unrevocable public links. If direct signed download URLs already exist, their expiry becomes an explicit revocation limitation requiring a decision. Access already delivered to a client cannot be recalled.

Audit invitation creation/revocation/acceptance, role/owner changes and export denial/cancellation with actor, organization, target, time and outcome; omit secrets and exported contents. Decide retention/access for these records and temporary export files rather than retaining them indefinitely.

### Enterprise SSO and unresolved decisions

Record SSO as an uncommitted customer request; do not replace allauth, select a provider, purchase an edition or promise a delivery date. Discovery must settle OIDC versus SAML, customer IdP(s), organization-specific enforcement, multi-organization account behavior, linking proof, joiner/mover/leaver provisioning, recovery/break-glass, existing session revocation, audit needs, support responsibility and budget. Authentication federation and provisioning are separate scopes. Bind a future issuer/subject to a verified local identity; email/domain coincidence is insufficient for linking or membership.

Decisions for the customer/product owner: approve invitation expiry; who can grant owner or finance roles; ownership-transfer and orphaned-resource rules; whether immediate revocation includes already-issued download URLs; acceptable treatment of an in-progress export; SSO requirements, commercial scope and cost. The proposed conservative member-only invitation flow can be specified before these broader commitments; owner/finance grants stay unavailable until their policy is agreed.

### Verification plan

- Exercise owner invitation success and finance/member denial; forged role, recipient and organization inputs; expired/revoked/resend tokens; unverified or different recipient; duplicate and concurrent acceptance; inviter demotion before acceptance. Assert persisted membership and single-use outcomes, not just response status.
- Test organization switching and cross-tenant reads, writes, lists/counts, related resources, cache/file paths and bulk operations with a multi-organization user and a user removed from one organization.
- Race last-owner removal/transfer, role changes and resource operations. Verify existing sessions and stale cache entries cannot retain the removed authority while other memberships remain usable.
- Pause exports before dequeue, mid-processing, before publication and before download; change roles at each point. Assert cancellation/withheld artifacts, denial of old links within the accepted window, and no cross-tenant output.
- Inspect installed allauth/Django/session configuration and version-matched documentation during implementation; verify login rotation, CSRF, logout, account deactivation and Redis failure. No such inspection or execution has occurred here.

## 2. Operations dashboard design

### Wireframe and information hierarchy

Reuse the existing restrained palette, spacing, typography, tables, buttons, focus treatment and navigation components. Component inventory and visual matching remain unverified because no current UI was supplied. This is a wireframe description, not a redesign or setup prescription.

At the top, keep the organization switcher and current organization name visible. Put the page title **Operations** beside a scoped refresh control and explicit last-updated status. A compact navigation area contains Operations, Exports and Follow-ups; organization administration contains Subscription and Usage only for authorized billing users. The same person can have different permissions after switching organizations.

The main area begins with a work queue, **Needs attention**, rather than revenue or growth cards. A small linked count for stalled exports and a count for overdue/unassigned follow-ups can lead directly to their filtered queues. Each count states its scope and freshness. Do not show a stalled count derived from analytics delayed by 48 hours as though it describes today's queue.

Use two existing table sections or tabs, retaining whichever pattern the product already uses:

- **Exports:** export name, requester/customer label only where permitted, status, age, last progress time, next available action. Default sort puts eligible stalled work first, oldest first, with a stable tie-breaker. Rows open export details with progress history and a clear failure/stall explanation. Retry/cancel appears only if the domain and authority allow it; avoid inventing destructive actions.
- **Customer follow-ups:** customer, subject, owner, due time, status and last update. Default sort is overdue first, then due soon. A detail view keeps customer context and allows the accepted assign/resolve workflow, with required resolution fields only if existing domain rules require them. This design does not send customer messages.

The detail view uses the established drawer or detail-page component. Returning restores queue filters, sort, page and focus. Details show the same organization context. Analytics, if useful, live below the queues or on a secondary view: for example exports completed during an explicitly named period, with unit, organization time zone, aggregation cutoff and completeness. Omit decorative charts that do not guide a task.

Subscription/Usage is a separate administration destination for finance administrators: plan and effective status, pending cancellation/reactivation state, limits, period used and last reconciled time, followed by authorized management routes. Billing totals and allowance calculations must identify whether they are authoritative or delayed estimates; do not present delayed analytics as invoice truth. Finance authority does not expose export contents, customer follow-ups or resource counts without separate permission.

### Data, interaction and states

Operational export and follow-up status requires current transactional records or a clearly stated operational freshness guarantee. The 48-hour analytics allowance is acceptable for labeled historical summaries only. If current operational data is unavailable, the unresolved prerequisite is an operational status source; show “Status unavailable” and prevent unsafe retry/cancel decisions based solely on stale data.

Define “stalled” from the export lifecycle: no progress beyond an agreed threshold while a job is expected to progress, accounting for legitimate queue waits and long phases. Define “overdue” from due time in the displayed organization time zone. Thresholds, assignment ownership, authorized retry behavior and follow-up completion criteria require product agreement; no invented SLA is implied.

Use server-scoped search, status/assignee/date filters, stable sort and bounded pagination for 50,000 records. Proposed default is 50 rows per page with permitted alternatives and an honest result count; never fetch the full tenant dataset into the browser. Search/filter/sort operates across all authorized matching records. Avoid bulk actions until an actual need is established. If retained from the product, distinguish “this page” from “all matching,” show exact eligible scope, clear selection when scope changes and reauthorize every record at execution.

Switching organization cancels or ignores old in-flight responses, clears tenant-specific selection/detail/form state and loads separately keyed data. Do not flash the former tenant's rows or summaries. Preserve only non-sensitive preferences that remain meaningful; revalidate saved links and filters in the new organization. An unsaved follow-up edit needs the product's existing save/discard behavior before switching.

| State | Presentation and recovery |
| --- | --- |
| First use / no activity | Explicit “No exports yet” or “No follow-ups” with an authorized next step; do not fabricate trend percentages |
| No actionable work | “No stalled exports” is a successful work-queue state, distinct from no exports existing |
| Filtered empty | State that no records match; offer clear filters while preserving organization context |
| Loading | Bounded skeleton or progress label; announce updates accessibly and do not show prior-tenant data |
| Stale / incomplete analytics | Visible cutoff and completeness warning adjacent to values; distinguish unknown from zero; preserve usable current operational queues |
| Partial failure | Show which section failed and retry that section; do not blank successful sections or convert errors to zero |
| Denied / membership removed | Clear permission message, safe organization switch route, no restricted counts or payloads; discard no-longer-authorized cached detail |
| Action pending | Disable duplicate submission and show accepted/requested status; a retry request is not an export completion |
| Completed / failed / conflict | Confirm persisted outcome; show actionable failure; if another user changed the record, refresh and require reconsideration rather than silently overwriting |

### Verification plan

Walk through two tasks: identify a truly stalled export and take its permitted recovery action; find an overdue follow-up, resolve it, and return to the same queue position. Separately, a finance administrator inspects plan/usage and cannot access the resource queues without permission. Verify permissions on the server independently of hidden navigation.

Use fixtures for no activity, no stalled work, filtered empty, long names/missing fields, 50,000 records, 48-hour-old analytics, partial failures and concurrent changes. Confirm that filters/sorting cover the full dataset and actions survive retries without duplication. Test rapid organization switches while old responses arrive and after membership removal. Inspect keyboard order, focus restoration, accessible table/action names, non-color status explanations, loading/result announcements, 200% zoom and narrow-screen reading order. A rendered UI, accessibility test and user observation are separate evidence still to obtain; no usability findings or performance measurements are claimed.

## 3. Subscription integration behavior

### Finding and required contract

The current sequence is not crash-safe. Recording an event ID before changing entitlements can cause a retry to skip unfinished work. Changing entitlements before email can lose the email; email success followed by timeout can cause a duplicate on retry. Deduplicating delivery is different from completing business effects. Database/provider/email effects do not share a transaction.

Preserve the existing database and processing mechanism. A small durable inbox plus local notification outbox can be handled by an existing worker or bounded scheduled recovery process; this proposal does not require a workflow platform.

1. Verify signatures using the actual provider's raw-body and replay requirements. Map the verified provider account, environment, subscription and billing customer to exactly one local organization. Reject invalid signatures; quarantine unmapped or conflicting identities without granting access. Never trust a client organization field or checkout redirect as entitlement proof.
2. Insert a durable inbox row keyed by provider/account/environment/event ID, recording receipt and processing state. A duplicate of a pending or failed row makes it eligible for continued work; it does not mean “already completed.” Acknowledge only after durable acceptance. Database failure returns the provider's retryable failure response; after acceptance, local recovery must not depend solely on another provider delivery.
3. Serialize work per subscription. Within a local transaction, apply the accepted commercial transition, persist the entitlement projection and source state/version, add uniquely keyed notification intent if needed, and mark the inbox effect complete. These writes commit together or roll back. Bound worker leases and retries so crashed claims can be reclaimed; retain attempt/error information and surface exhausted recovery to an operator.
4. Deliver notification intents separately. Record sent, retryable failure or ambiguous outcome; keep entitlements committed even if email is unavailable. The email describes a committed transition, not a promise that a provider action succeeded merely because a request was accepted.

### Ordering, cancellation and reconciliation

An event is evidence of a provider change, not automatically the newest subscription state. If the provider guarantees an object revision/sequence, compare it under a database lock and ignore older projections while recording the decision. Event delivery time, event ID sorting and unrelated-object timestamps are insufficient ordering rules. If no reliable ordering exists, treat events as reconciliation triggers: obtain current authoritative subscription state through the supported provider API, serialize projection for that subscription, and avoid overlapping stale fetches overwriting newer results. Verify the provider's snapshot/consistency guarantees; if freshness cannot be established, retain the last confirmed state and expose pending reconciliation rather than guessing.

Store provider observed state, local entitlement policy/result, desired customer action and observed usage separately. Cancellation requested, cancellation effective at period end, immediately canceled and reactivated are different domain transitions. A delayed cancellation event must not undo a newer confirmed reactivation; an old activation event must not restore a currently canceled subscription. Do not delete data or remove organization membership because a billing event arrives. Whether canceled subscriptions retain read/export access, when background jobs stop and whether a payment grace period exists are unresolved product decisions. Preserve the accepted policy if one exists; otherwise do not invent a grace duration or irreversible effect.

For customer cancel/reactivate commands, persist intent and a stable operation key before a remote request. Use provider idempotency if supported, including its retention limits. On remote timeout, mark the command uncertain and reconcile/query the result before issuing a conflicting command. A provider change can succeed before the local transaction fails; retries and scheduled reconciliation must repair that divergence. The dashboard should say “Cancellation requested” until authoritative confirmation, then display the effective time. No provider configuration or command is performed by this design.

Run bounded reconciliation for overdue pending inbox rows, uncertain commands and provider/local subscription discrepancies, plus a periodic check whose cadence is agreed from allowed entitlement staleness and provider limits. Only genuine entitlement transitions generate unique notification intents; duplicate events or repeated reconciliation do not regenerate email. Key notifications by subscription, transition/version and recipient/purpose, not merely event ID, since multiple events can describe one change.

Exactly-once email cannot be guaranteed from the database alone. If the email provider supports durable idempotency or status lookup, reuse the same message key and reconcile the ambiguous response. Otherwise a timeout after possible delivery remains ambiguous: blind retry risks duplicates; no retry risks a missing notice. Record this state and require an explicit product choice for that class of notice (at-least-once with duplicate risk, or manual/no automatic resend). Do not mislabel it delivered or claim deduplication solves it. A later confirmed reactivation can supersede a pending cancellation email; define which transition notices must be retained and which should be suppressed or replaced before sending.

### Verification plan and unresolved decisions

Use a provider simulator or later-authorized sandbox plus persisted database assertions. Terminate processing after inbox insertion, after claim, during the local transaction, after commit before dispatch, and after email acceptance before its response is received. Recovery must yield one entitlement projection and one notification intent per real transition; test ambiguous delivery separately from confirmed send failure. Assert lease reclamation and bounded recovery after process death.

Deliver duplicates concurrently and replay old events after cancel/reactivate/cancel sequences; vary order across event types and subscription/customer IDs. Test stale fetches, concurrent command/webhook updates, unknown mappings, wrong environment, invalid signatures, database outages, provider/email outages, expired idempotency windows and worker retry exhaustion. Verify reconciliation repairs provider-success/local-failure and does not regrant access from obsolete events. Run entitlement checks through representative API/job paths, not only by examining subscription rows. No sandbox or integration verification was executed here.

Decisions still required: actual provider/API version and ordering/retry/idempotency contracts; cancellation/reactivation effective-time policy; paid capability and in-flight job behavior; acceptable entitlement convergence delay and reconciliation owner; ambiguous-email resend policy; notification supersession; retention/access for event payloads and audit records. Persist only fields needed for processing/support, redact secrets and personal data from logs, and agree restricted payload retention rather than storing full provider events forever.

## Guidance actually read and verification limits

All paths below are under `plugins/`:

- `security/skills/security-auth-development/SKILL.md`
- `security/skills/security-auth-development/references/patterns-and-selection.md`
- `security/skills/security-auth-development/references/sources.md`
- `security/skills/security-and-privacy-design/SKILL.md`
- `saas-development/skills/saas-design/SKILL.md`
- `saas-development/skills/saas-design/references/lifecycle.md`
- `saas-development/skills/saas-dashboard-design/SKILL.md`
- `saas-development/skills/saas-dashboard-design/references/dashboard-decisions.md`
- `saas-development/skills/saas-readiness/SKILL.md` (read for scope/evidence limits; no launch verdict was requested or inferred)
- `saas-development/references/sources.md`

The source reviews were read as contextual summaries; their linked repositories, standards and provider documentation were not fetched or independently inspected. No other skills, prior outputs or evaluation rubrics were read. No browsing, installations, live-account/provider actions, application edits or subagents were used. Verification plans above remain unexecuted and require the accepted implementation, UI and selected provider contracts before making security, performance, accessibility or integration claims.
