# Governance readiness assessments

Prepared 20 October 2026. These are bounded assessments of the supplied scenarios, not legal advice, an attestation or a verified inspection of either service. Suggested owners below are proposed assignments.

## 1. GDPR engineering readiness — US SaaS serving France/Germany

**The EU database region does not establish launch readiness.** It addresses one storage location. The described service also exposes records to US support and sends conversation text to a separate AI provider. There is insufficient implementation and operating evidence to support a readiness claim.

### Scope and working interpretation

Known facts: a US company has no EU establishment, actively sells in France/Germany, processes customer-uploaded support conversations, independently chooses account-analytics purposes, stores its primary database in an EU region, allows US support access and discloses text to an external AI provider. Personal data in conversations and account analytics is a working assumption; fields, people, volume, sensitivity, provider entities and contracts remain unknown.

Active EU selling supports an Article 3(2) targeting analysis for related processing of people in the Union. EU hosting alone neither establishes the company in the EU nor determines applicability. Confirm whether customers are organizations or individuals, whose personal data are processed, where those people are and how each operation relates to the offering or monitoring. An EU customer's GDPR status alone does not automatically make every non-EU vendor operation directly subject to GDPR. Treat applicability as a recorded, operation-specific decision. [EDPB territorial guidance, sections 1(d), 2 and 4](https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_3_2018_territorial_scope_after_public_consultation_en_1.pdf).

| Processing operation | Working role assessment and decision needed |
| --- | --- |
| Uploaded support conversations | Likely processor where the customer determines the purposes and essential means and the SaaS acts on documented instructions. Confirm actual reuse, contracts and assistance responsibilities. |
| Account analytics | The company appears to be controller because it independently chooses the purposes. Specify events, essential means and whether conversation content is reused. A customer processing agreement cannot by itself authorize the company's own analytics purposes. |
| AI processing | Could be a subprocessor for instructed conversation processing, a processor for the company's controller purposes, or a separate controller for its own purposes. Establish the actual processing, training/reuse, retention and contractual terms before assigning the role. |

These are functional assessments, not labels inherited from being a SaaS vendor. [EDPB controller/processor guidance, executive summary and paragraphs 74–81](https://www.edpb.europa.eu/system/files/documents/2023-10/EDPB_guidelines_202007_controllerprocessor_final_en.pdf).

### Decisions that block a defensible launch assessment

1. **Founder/privacy owner: accept the territorial and responsibility map.** If Article 3(2) applies, resolve Article 27 representation; ongoing service processing should not casually be called occasional. Determine the lawful basis and transparency for each controller purpose, and instructions, processing agreements and subprocessor authorization for customer data. Screen sensitivity, children, profiling, scale and impact for Articles 9, 35 and 37 consequences. Neither a privacy notice nor blanket consent settles these matters. These are unresolved decisions, not findings that every assessment or officer is required. [GDPR Articles 6, 9, 13–14, 27–28, 35 and 37](https://eur-lex.europa.eu/eli/reg/2016/679/oj).
2. **Engineering/privacy owner: map each disclosure and access path by legal entity.** Include customer-to-US-SaaS processing, EU hosting provider-to-US-SaaS access, support employers/contractors and AI recipients. Remote access by a third-country processor to EU customer data can constitute a transfer (EDPB example 11). Access by an employee within the same controller is not automatically a separate Chapter V transfer (example 8); that does not remove security/accountability duties or settle upstream disclosures. Establish exporters, importers, locations and onward transfers. For qualifying transfers, the privacy owner must select and substantiate an applicable Chapter V mechanism; no provider eligibility, adequacy coverage or safeguards have been verified. [EDPB transfer guidance, sections 2–3](https://www.edpb.europa.eu/system/files/documents/2023-02/edpb_guidelines_05-2021_interplay_between_the_application_of_art3-chapter_v_of_the_gdpr_v2_en_0.pdf).
3. **Product/engineering owner: decide what actually reaches the AI provider.** Identify whether full text is necessary, which fields can be removed and what outputs, embeddings, logs and caches are generated. Set purpose boundaries, support visibility and retention by store. Proposed evidence: a redacted data-flow inventory and synthetic request trace showing the actual payload and recipients, plus reviewed provider terms. These are proposed checks; none were run.
4. **Engineering/support owner: exercise the lifecycle.** With synthetic subjects across two tenants, demonstrate authorized lookup, correction, scoped export and deletion through primary and derived stores, provider handling and backup restoration. Specify justified retention exceptions, restricted use and expiry; prevent restored records from silently re-entering processing. Include tenant isolation, least privilege, support access approval/logging and revocation. Retention and defaults must be effective, including copies, backups and logs; the EU region setting proves none of this. [EDPB design/default guidance, sections 2.2 and 3.7–3.8](https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_201904_dataprotection_by_design_and_by_default_v2.0_en.pdf).
5. **Privacy/support/security owners: define operating handoffs.** Route customer-data requests to the appropriate controller and handle the company's controller requests; assign identity checks, deadlines, incident escalation, processing records and provider-change review. Processor breach escalation and controller notification duties differ; a universal “notify everyone within 72 hours” rule is inaccurate. [GDPR Articles 12–22, 30, 32–34](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

Unresolved product choices: allow unrestricted free-text uploads or constrain sensitive content; allow AI training/reuse or prohibit it; retain conversation-derived analytics or minimize to account events; permit routine US support access or use a restricted escalation route. These choices change the design and assessment. If account analytics uses cookies/device tracking, commission the applicable France/Germany ePrivacy analysis; no tracking implementation or national-law assessment was supplied or performed.

**Exit evidence for another readiness review:** accepted operation/role/basis decisions, complete recipient/transfer map and arrangements, lifecycle/security demonstrations, documented retention and operating owners. Completion would support an engineering assessment, not a legal compliance conclusion.

## 2. SOC 2 readiness — report requested next month

**The supplied facts do not support three months of effectively operating controls.** Enabling a reminder last week is not a completed access review. A new deployment-approval rule supports an implementation date, not a three-month history of performed approvals. Missing earlier review records remain an evidence gap; they are not proof either that reviews happened or that no other controls existed.

SOC 2 is an independent examination of a defined system, rather than a certification produced by enabling a tool. [AICPA SOC overview](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services), [AICPA assurance leader's explanation](https://www.journalofaccountancy.com/podcast/2026/apr/the-risks-of-quick%E2%80%91turn-soc-engagements-and-what-cpas-should-know/).

### Scope and report options

The service architecture, commitments, workforce, vendors and control inventory were not supplied. Management must define the actual production service and relevant people, processes, application, infrastructure and data, including administrative access and deployment paths. Select categories from actual commitments and system requirements with the assurance owner/CPA; do not assume every category applies. Prepare a faithful system description, including relevant customer responsibilities. [AICPA Trust Services Criteria resource](https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022), [AICPA description criteria resource](https://www.aicpa-cima.com/resources/download/get-description-criteria-for-your-organizations-soc-2-r-report).

- **Type 1:** management and CPA could consider an as-of date after suitable controls are designed and implemented. This does not assert historical operating effectiveness. Next-month issuance remains unconfirmed and depends on readiness and examination work.
- **Type 2:** evaluates design and operation over a specified period. Choose dates and sufficient evidence with the CPA. A newly implemented control cannot be represented as operating before implementation. If older manual or alternative controls existed, assess authentic contemporaneous evidence against the relevant risk; do not retroactively relabel activities as the new controls.
- **Readiness assessment now:** a realistic interim deliverable if examination scope or evidence is not ready. It is not an independent SOC 2 report. No particular observation period or favorable opinion is promised.

The point-in-time/period distinction is supported by AICPA's published guide excerpt, paragraph 1.05. The same excerpt explains inclusive versus carve-out treatment of subservice organizations. Its 2018 edition is useful for these concepts; the engagement must use applicable current standards. [AICPA guide excerpt hosted by its publisher](https://catalogimages.wiley.com/images/db/pdf/9781945498602.excerpt.pdf).

The cloud provider report is dependency evidence, not the SaaS service's report. Obtain the actual report and inspect the covered provider services/regions, report type, period, opinion, exceptions, subservice treatment and complementary user entity controls. Map the latter to the team's implemented controls. Agree carve-out/inclusive treatment and how any period gap is addressed; a bridge representation does not create an audited extension. None of the provider report was supplied.

### Evidence still needed

The following are proposed evidence requests, not assertions that these controls already exist or a prescribed document suite.

| Area | Evidence and decision needed |
| --- | --- |
| Access reviews | Actual review date, reviewer/authority, complete in-scope identity/privilege population (including cloud, app, source control, service accounts), decisions, removals, exceptions and follow-up. A reminder screenshot proves only configuration. Establish review cadence and what was due during the claimed period. |
| Access lifecycle | Population of joiners, changes and departures; authorized grants, removal timestamps, privileged authentication and exceptions. Reconcile identity sources to avoid proving only one selected account. |
| Deployment approvals | Activation/change history, enforcement scope and bypass rights; complete production deployment population linked to changes, independent approvals, test results and artifact identity; emergency approvals and remediation. Inspect actual runs, not just the rule definition. |
| Monitoring/incidents | Relevant alert and incident populations, owner response, investigation, closure and follow-up. If no incidents occurred, retain supporting population/query evidence; do not invent an incident. |
| Recovery | Stated recovery commitments, backup records and exercised restoration evidence demonstrating the relevant data/service recovery. Backup configuration alone does not demonstrate restoration. |
| Risk, vendors and governance | Actual risk decisions, owners, accepted exceptions and remediation; provider reviews and complementary-control mapping; proportionate policy/people evidence linked to operation. |

For each item preserve source, original event date, collection date, owner, control assertion, period, population, completeness checks and exceptions. Protect customer and personnel information. A handful of selected examples cannot establish population completeness or entire-period coverage; the CPA determines sampling and sufficiency. A report normally also contains management's assertion, system description, auditor reporting and, for Type 2, tests/results. [AICPA illustrative Type 2 report resource](https://www.aicpa-cima.com/resources/download/illustrative-soc-2-r-report-with-description-and-assertion).

### Prioritized next steps and unresolved decisions

1. **Now — founder/assurance owner:** withdraw the unsupported three-month assertion from proposed wording. Use: “The access-review reminder and deployment-approval rule were enabled last week. Historical operating effectiveness has not been established.” Decide intended recipients, contractual need, Type 1 versus Type 2 and whether next month is an issuance deadline or a readiness milestone.
2. **Now — service/control owners:** inventory the actual service and risks; record implementation dates; preserve existing authentic records and gaps. Complete a current access review with its true date and fix actual exceptions. Do not backdate or recreate missing reviews as if they occurred historically.
3. **Next — assurance owner and CPA, in a separately authorized engagement:** settle system boundary, applicable criteria/categories, report date/period, subservice treatment, evidence populations and treatment of any control changes or gaps. This assessment has not contacted a CPA.
4. **During the agreed period — control owners:** perform controls at their true frequency/triggers, retain traceable evidence and verify remediation. Reassess readiness against the full service before making an assurance claim. If next month cannot meet the agreed examination needs, change the deliverable/date rather than the historical facts.

## Guidance, sources and evidence limits

Local resources actually read, all under `plugins/governance/`:

- `skills/gdpr-readiness/SKILL.md`
- `skills/gdpr-readiness/references/applicability-and-decisions.md`
- `skills/soc2-readiness/SKILL.md`
- `skills/soc2-readiness/references/controls-and-evidence.md`
- `references/sources.md`

Public sources actually consulted: the linked GDPR text; final EDPB territorial guidance v2.1, controller/processor guidance, transfer guidance v2.0 and design/default guidance v2.0 (including relevant PDF sections); AICPA SOC overview; the linked April 2026 Journal of Accountancy discussion with AICPA's assurance leader; the AICPA Trust Services Criteria, description criteria and illustrative-report landing pages; AICPA's 2018 guide excerpt hosted by Wiley. The AICPA SOC 2/SOC 3 FAQ landing page was also opened but its full material was not available. Search-result snippets from other sources were not used as substantive authority.

Access limits: the Trust Services Criteria and description criteria downloads required an account; the illustrative report download required membership. No account was used, so only their public descriptions were read. The full current criteria, full illustrative report and engagement-specific interpretations remain for the qualified assurance owner/CPA; this is not a completed criterion-by-criterion mapping. The original `aicpa.com` illustrative-report and FAQ URLs failed to load; equivalent `aicpa-cima.com` public pages were inspected. No national ePrivacy, DPIA-list or provider-specific transfer eligibility conclusion was made.

Service evidence consists solely of the two synthetic requests. No code, configurations, contracts, logs, live data, provider report or prior records were inspected, and no tests, submissions, accounts, installations, infrastructure changes or auditor communications occurred. Proposed remediation and evidence collection are not completed work. Only this deliverable was written.
