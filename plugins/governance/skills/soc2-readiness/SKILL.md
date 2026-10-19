---
name: soc2-readiness
description: Prepare or assess SOC 2 readiness for a defined service, commitments
  and examination scope. Use for system/control boundaries, operating evidence, exceptions
  and remediation priorities; does not perform an independent attestation.
license: MIT
metadata:
  scope: generic
  invocation: both
  role: support
  references: ../../references/sources.md
user-invocable: true
---

# Assess the service and its control evidence

Establish why the report is needed, the actual service/customer commitments, intended report type/timeframe and available auditor/scoping decisions. Reuse existing controls and evidence. SOC 2 is an assurance examination of scoped controls, not a regulation or a property created by a passing application test. Read [control and evidence reasoning](references/controls-and-evidence.md) and the [official source guide](../../references/sources.md) when scoping or mapping criteria.

## Define the relevant boundary

Describe the service, people/processes, software, infrastructure, data, vendors and customer responsibilities. Distinguish in-scope service commitments and system requirements from unaccepted future features. Establish relevant Trust Services categories and description requirements with the responsible assurance owner/auditor; do not require every category simply because it exists.

Identify dependencies and the selected treatment of subservice organizations and complementary controls. A cloud provider's report can support a dependency assessment but does not cover all application controls or the customer's responsibilities. Architecture and access/operating boundaries should agree with the described service.

## Connect criteria to operating controls

Map relevant criteria/commitments to actual controls, owners, frequency/triggers and evidence populations. Include applicable access lifecycle, changes, monitoring/incident handling, recovery, vendor and risk processes rather than equating readiness with application security. Reuse proportionate existing processes; a particular compliance platform, policy count or organizational template is unnecessary.

Distinguish suitable design and implementation at a point in time from operating effectiveness over a defined period; establish the intended Type 1/Type 2 scope with the auditor. Policies, configured jobs and generated screenshots are not proof that required activities happened. Check who performed a control, when, across which population, with what exceptions and follow-up.

## Assess evidence without manufacturing assurance

Inspect supplied evidence for relevance, completeness, integrity, period and traceability. Separate sampled observations from coverage of the population. Preserve missing evidence and exceptions; never backdate an activity, fabricate approval or treat a newly implemented control as historically operated. Keep source data and sensitive customer/personnel records protected.

Prioritize gaps by service risk, affected criteria and remediation lead time. Identify control improvements, operating evidence still needed and auditor/management decisions separately. Return a readiness assessment scoped to the actual evidence, not a promised audit outcome. External auditor communications, contractual commitments and live remediation require the corresponding authorization.
