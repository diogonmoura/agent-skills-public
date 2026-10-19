---
name: compliance-design
description: Translate applicable legal, contractual and assurance requirements into
  system boundaries, controls, ownership and evidence. Use during product/system design
  or a scoped compliance assessment; distinguish engineering work from legal interpretation
  and independent assurance.
license: MIT
metadata:
  scope: generic
  invocation: both
  role: support
  references: ../../references/sources.md
user-invocable: true
---

# Connect obligations to system decisions

Establish the intended service, customers/jurisdictions, data processing, delivery model and requested decision. Identify existing commitments, authoritative interpretations and current evidence. Separate a statutory duty, customer contract, voluntary assurance goal and product preference; they have different applicability and decision owners. A small change needs assessment of affected obligations, not an exhaustive organizational audit.

## Establish applicability and authority

Investigate relevant facts before asking the user to settle a tradeoff. Record the source, version/date where useful, affected entity/process and why a requirement appears applicable. Consult primary material for substantive interpretation using the [source guide](../../references/sources.md). When legal or assurance interpretation remains material, identify the exact unresolved question and qualified decision owner; do not ask the user to guess technical facts or invent an approved interpretation.

Map the system boundary including people/processes, application and infrastructure, identity, vendors, support, telemetry, data movement and recovery. A requirement may apply to the organization or processing operation rather than a single code repository. Hosted region, encryption, a provider attestation or a passing scanner does not establish the customer's complete compliance.

## Derive proportionate controls

For each material applicable obligation or commitment, connect the intended outcome to a control, owner, implementation/operating scope and evidence. Compare prevention, detection and recovery where relevant; reuse adequate accepted controls rather than adding policy machinery. Distinguish a control's design, implementation, observed operation and independent assessment. Describe residual exposure and proposed acceptance honestly.

Carry decision consequences into affected product requirements, architecture, implementation, operating procedures and verification. Seek available security, data, delivery and operations expertise by capability; without it use project evidence and primary sources at the same standard. If obligations change intended usage, data handling, spending, retention or customer commitments, present concrete options and seek the unresolved authorized decision while continuing independent work.

## Make evidence useful and bounded

Evidence should identify the control/property, relevant population/period, actual source and reviewer/owner where needed. Preserve exceptions and gaps. Protect sensitive records and collect only what the assurance purpose needs. Versioned code or configuration supports implementation; a performed review or recovery exercise supports operation. Neither a generated policy nor a planned test proves the activity occurred.

Return the scoped applicability/control decisions, evidence and remaining gaps. Use existing project records; no fixed spreadsheet, tracker or compliance platform is required. A readiness assessment does not certify compliance, submit filings, accept terms or authorize production changes.
