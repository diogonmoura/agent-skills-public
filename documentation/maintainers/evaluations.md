# Evaluating the collection

[Maintainer guide](../maintainer-reference.md) · [Trial procedure](#generation-trials) · [Evidence](#recorded-evidence-and-limits) · [Local agy example](#local-runner-example-agy)

The [evaluation cases](../../evals/development-workflows.json) contain 19 behavior prompts and eight generation trials, with separate evaluator criteria. They assess engineering behavior, evidence accuracy and unnecessary complexity. Planning exercises and package checks do not prove a working application. These trials do not run automatically in CI.

## Generation trials

The specification is harness-independent: interactive or automated execution, supported plugin/skill loading, explicit selection or plain-language requests, and conversation continuation or factual handoffs. Preserve resources and native controls; record unsupported capabilities. No particular CLI, slash syntax or trace format is required.

| Trial | Phases | Evidence |
| --- | --- | --- |
| New saved-search application | setup → agreed answers → develop | Working startup/migrations, private persisted journeys, rendered UI, checks, feature worktree and local commit |
| Existing SQLModel library | improve → approve a finding → implement | Real reproduction/baseline, focused fix, preserved tools/contracts, regression checks and local commit |
| Small documentation change | implement | Focused contribution without unnecessary setup, UI design or application testing |

1. Prepare a disposable repository with no production credentials or writable publication remote. Confirm guidance inventory, tools, authentication, allowed actions and run limits.
2. Establish baseline behavior and expected acceptance before implementation. Give the acting agent only the raw phase prompt, repository and product context; keep evaluator criteria and prior diagnoses separate.
3. Answer consequential setup questions and carry accepted answers forward. Approve one real OSS finding before implementation; select another task if no useful finding exists instead of inventing a defect.
4. Continue the phases with their accepted context. Use fresh checkout/context for independent reruns. Preserve explicit-only invocation controls.
5. Inspect actual diffs, commits, commands and runtime evidence. Classify completed, partial or blocked; distinguish guidance failures from missing capabilities. Process exit and self-rating alone cannot establish success.

| Record | Include |
| --- | --- |
| Inputs | Repository/guidance revisions, harness/model versions/configuration, inventory, capabilities, scope and limits |
| Execution | Commands/results, diff/commit, runtime artifacts, interventions and redacted session/tool events where available |
| Limits | Unexecuted checks, mocked boundaries and unknown routing evidence; reported time/token usage only when available |

If skill reads cannot be observed, routing remains unknown. Keep secrets out of prompts and artifacts. Repair a demonstrated failure and independently rerun the affected case. Grade behavior rather than phrase matching or an arbitrary passing percentage. A single run cannot guarantee quality.

## Compare and simplify

Compare complete bundles with pristine upstream guidance and its native dependency groups. Hold application baseline, outcome, context, harness, model, tools and permissions constant. Use equivalent plain-language requests where local activity names do not exist upstream, recording the difference. Unavailable prerequisites remain limitations; do not invent tracker setup or weaken controls. Cross-harness/model comparisons cannot isolate the effect of the skills.

Inspect observed behavior, missed pointers, repeated reading, unnecessary work and available cost/latency evidence. Consolidate one repeated rule at a time and rerun the affected full and small-change cases. Keep short authority boundaries beside live actions. Preserve upstream bodies/resources and record adapter changes. [Rule ownership](../maintainer-reference.md#keep-guidance-focused) identifies where shared guidance belongs.

## Recorded evidence and limits

| Check | Recorded result | Boundary |
| --- | --- | --- |
| Collection packaging | Seven bundles: 50 local + 37 upstream skills. Metadata, 18 repository tests, all-plugin builds and complete inventory/resource checks pass. | Package checks establish packaging, not application behavior. |
| Copilot CLI 1.0.95 | Earlier session-local discovery of 85 skills and the default 56-skill set. | Revised 87-skill collection has not been rerun in Copilot. Menu filtering/compliance remains unproven. |
| agy 1.3.5 | Revised seven bundles installed locally with 87 skills; initial default-bundle resource parity checked. | Installation does not establish use or compliance; model selection was not exposed by these trial records. |
| Original generation trials | Small README change and focused SQLModel change completed; SQLModel full suite passed 270 tests. Saved-search application demonstrated PostgreSQL persistence and cross-user denial. | Saved-search setup omitted delivery foundations and frontend regression coverage; independent keyboard checks found dialog focus defects. |
| Revised foundations | Explicit setup created an objective worktree, component READMEs, Dockerfiles, CI and release/deployment procedures. Independent API tests (10), frontend tests (2), build and lint pass. | Root README and final commit are missing; runner ended with an unfinished progress narrative despite SUCCESS. Remote CI, image publication, deployment and recovery were not executed. |
| Tauri desktop | Packaged macOS app launched; independent create, PostgreSQL persistence, app restart, identity separation and failed-save/retry worked. API tests (19), frontend tests (20), web build/lint and API Docker image build pass. | Edited a branch in the base checkout instead of a worktree; fixture identities default enabled and native auth uses web session storage. Other desktop targets, signing and production readiness unverified. |
| Expo iOS/Android | Python tests (14), JavaScript iOS-filtered tests (16), Android-filtered tests (17), typecheck and lint pass. | Filtered Jest suites are not native-device runs; shared cases overlap. Full Xcode and Android SDK/emulators are absent. Both native runtime outcomes remain blocked. |
| AG-UI/A2UI | Python tests (17) and frontend tests (14) pass. Independent published A2UI 0.9.1 schema check rejects the private payload. | Production web build fails: missing index.html; lint fails: ESLint absent. Own-format tests and installed SDK names do not establish A2UI interoperability or an end-to-end app. |
| Canvas strategy/design | Initial strategy and design exercised; fresh strategy rerun improved decision status to proposed. | Unsupported competitor/economic claims remained; first pass misstated tldraw licensing and ACP attachment guarantees. Revisions address guidance; successful correction is not yet established. |
| Canvas diagnosed implementation | Local commit bd01ab7; independent 14 backend tests passed with one live test skipped; production frontend build and lint (with warnings) passed. Dedicated agy conversation continuity demonstrated; semantic provider-error guard repaired. | Browser showed unlabeled sample shapes, no visible proposed annotation/session card and an empty canvas after saved-state reload. Private events still fail AG-UI schema; live ACP/voice and complete foundations remain unverified/incomplete. No frontend regression suite. This was a diagnosed repair with coordinator intervention, not a blind rerun. |
| VS Code and deployment | Loading instructions follow official documentation. | Revised client behavior, remote CI/publication, deployment, restore and live voice/model quality remain unverified. |

These are revision-specific local observations, not a controlled estimate of skill effectiveness. Initial revised trials used revision 27bc2cc; strategy rerun used the f9e1612 business bundle; canvas implementation uses a8695b8. Later guidance changes require their own reruns. Some agy runs returned backend 503 errors alongside completion prose; preserve both execution status and actual artifact evidence. No broad claims of native parity, live AI quality or production readiness follow from the passing checks.

## Local runner example: agy

I chose `agy` for my local tests. The [README](../../README.md#2-load-them-in-your-client) owns installation instructions; this example adds no dependency to the trial specification or plugins.

```bash
agy plugin validate "$AGENT_PLUGINS_DIR/development-workflow"
agy plugin list --json
agy -p '<phase prompt>' --output-format stream-json --print-timeout 20m
```

Run from the target repository, capture stdout/stderr outside it, and use the installed client's conversation option for continuation. The 20-minute limit is a local choice. Check tool events and soft denials even on exit zero. Use scoped permissions and the client's sign-in flow; never put sign-in codes in prompts/traces. The recorded discovery run used workflow 0.17.0; fresh sign-in and Docker availability blocked application/Compose execution independently.

## Foundation, native-client and AI trials

The expanded generation set adds project-foundations, tauri-desktop-application, expo-ios-android-application, agui-a2ui-application and ai-canvas-product-to-implementation. The mobile trial shares TypeScript/Expo and a Python backend but grades iOS and Android separately. The canvas trial carries the accepted engineer audience and tldraw/existing-session direction through strategy, system design and implementation; consequential unresolved choices remain phase blockers.

New application foundations are evaluated as actual artifacts and runnable commands: human READMEs, configuration checks, behavior tests, containerizable app Dockerfiles/Compose, GitHub Actions and release/deployment/recovery process. Registry defaults configure GHCR and PyPI for distributable Python packages without authorizing publication. Native runtime/signing, live model/voice and real harness attachment are recorded separately from source, browser and fixture checks.

The initial local application trial demonstrated API tests and persistence/ownership, but omitted CI/containers/root onboarding, wrote directly on main, seeded test identities without an environment guard and used dialogs without focus containment/restoration. These observations motivate the revised guidance and grader criteria; keep the diagnosis out of independent actor inputs. The initial READMEs and backend tests existed, but scaffold text and API-only evidence did not establish complete setup or UI verification. Updated trial results must be recorded from execution rather than inferred from the revised instructions.

The first engineer-canvas strategy trial also presented unaccepted pivots as decisions, overstated competitor/pricing certainty and incorrectly treated the tldraw SDK as MIT-licensed. Strategy evidence and template guidance now require current sources, explicit unknowns and proposed versus user-accepted decision status. Preserve that failed output before a fresh-context rerun; changed instructions alone do not establish a successful correction.

Independent validation of the first AG-UI/A2UI setup found that its private surface tree failed the published A2UI 0.9.1 envelope schema while its own format tests passed. Protocol guidance now requires published-schema and independent renderer/conformance evidence. Native runtime and live provider checks remain separate capabilities.

## Visual-quality follow-up

The desktop trace recorded native-client guidance reads but no observed frontend-conventions or interaction-design reads. Its manifest had no shadcn/Tailwind dependencies. Functional/native checks therefore did not establish compliance with the product/visual/UX process. The local frontend fallback also prescribed generic neutral/blue styling. Revised routing retains frontend/interaction guidance for Tauri; visual direction now derives from the brief and requires representative rendered review/repair. A new behavioral case and UI-trial criteria distinguish visual quality, usability/accessibility and functional regression evidence. These changes are not yet validated by a fresh generation; screenshot evidence from the earlier app is not a passing visual baseline.

## Lifecycle and licensing follow-up

Most creation probes entered with prescribed features/stacks through setup and develop; they were not blind tests of business-to-product discovery. Canvas strategy/design ran but did not resolve SDK licensing or actual existing-session feasibility before implementation. Revised develop guidance owns explicit new-application outcomes, setup clarifies its narrower scope, system-design requires consequential dependency decisions and a behavioral case checks commercial SDK constraints. Repair and fresh desktop trials are distinct: repair receives the known defects; fresh generation receives the product brief and constraints without old implementation or grader diagnoses. New guidance alone does not establish compliance.

Consequential-finding decisions are now owned by shared workflow guidance across all phases; system-design and operations supply evidence rather than defining separate approval policies. A cross-lifecycle case checks security/privacy and reliability choices plus an independent routine fix as a control against unnecessary questioning. These policy changes occur after the desktop trials were dispatched; their recorded source revision remains 99ea936.
