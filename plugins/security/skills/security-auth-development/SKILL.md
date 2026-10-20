---
name: security-auth-development
description: Design, implement or review authentication, authorization and identity
  lifecycle across application stacks. Use for sessions, federation, passkeys, machine
  identity, tenant/resource access and contextual identity-framework selection.
license: MIT
metadata:
  scope: generic
  invocation: both
  role: support
  references: references/sources.md
user-invocable: true
---

# Establish identity and authority through the lifecycle

Read the accepted application, actors, trust boundaries and deployment. Identify who authenticates whom, what each actor may do to each resource, and how authority changes over time. Preserve accepted providers and protocols unless the request or evidence justifies reconsideration. Identity proves a subject; authorization decides an operation in context. Read [pattern selection](references/patterns-and-selection.md) when comparing approaches and [research sources](references/sources.md) for first-party contracts and inspected project examples.

## Choose the smallest sufficient identity architecture

Separate browser, native, service and delegated-agent clients; their credential handling and trust differ. Compare framework-native sessions, a protocol client, an identity broker/platform and a managed identity service against required recovery, MFA/passkeys, enterprise federation/provisioning, data location, cost and operating capability. Reuse mature protocol/cryptographic implementations. A provider feature or starter is not evidence that the complete application boundary is protected.

For federation, distinguish authentication, delegated access and provisioning. Bind the actual issuer/subject to the local identity and verify tokens and redirects with compatible libraries and current protocol guidance. Treat account linking as an ownership operation; matching email strings or a claimed organization domain alone does not prove authority. Define how existing sessions, linked providers and recovery methods interact.

## Enforce resource and tenant permissions

Choose roles, attributes, relationships or a combination according to the domain. Determine the enforcement points for HTTP/API calls, jobs, exports, support tools and AI/MCP actions. Verify subject, resource, action, tenant and relevant lifecycle/context at the trusted boundary; default-deny unknown operations and prevent authority from client-supplied role/tenant fields. Listing/search, related resources and bulk operations need the same semantics as individual reads/writes.

Keep membership, authentication and paid entitlements distinct. Scope and expire invitations; validate intended recipients and permitted role grants. Check ownership transfer, last-owner removal and privileged support access against accepted product rules. An external policy engine introduces model-version, consistency, cache, availability and synchronization choices; loading one does not solve them automatically.

## Make lifecycle and recovery explicit

Define issuance, storage, expiry, refresh, rotation, revocation and logout for each credential/session. Match cookie/browser protections, native secure storage and service credentials to the actual client. Token format alone does not determine security; JWTs do not automatically provide immediate revocation or current membership. Bound stale authorization according to accepted risk, and invalidate/recheck when relevant authority changes.

Treat enrollment, account recovery, factor changes, linking and deprovisioning as security-sensitive flows. Use appropriate proof of control, reauthentication/step-up and abuse limits without creating trivial account-lockout attacks. Define service-identity ownership and least privilege, automated rotation/revocation and effects of credential compromise. Keep audit evidence useful without recording tokens or recovery secrets.

## Verify behavior and preserve scope

Exercise allowed and denied resource operations, cross-user/tenant requests, expiry/revocation, recovery/linking, privilege changes, replay and applicable provider/key-rotation or outage behavior. Check stale caches and existing sessions against the accepted revocation window. Use available implementation/test expertise or version-matched primary documentation when specialists are absent.

Return the architecture, framework tradeoffs, authority/lifecycle contract and actual evidence. Ask about unresolved consequential choices such as enterprise identity requirements or recovery policy; choose ordinary implementation details within accepted scope. Installing identity guidance does not authorize a provider account, migration, credential rotation or live configuration change.
