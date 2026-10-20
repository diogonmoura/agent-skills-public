---
name: test
description: Select, add where needed and run checks for the current change or named
  journey, component or application. Use for unit/integration/contract/web/desktop/mobile verification
  and relevant performance/resilience checks within the authorized target scope.
user-invocable: true
disable-model-invocation: true
metadata:
  scope: generic
  invocation: user
  role: task
---

# Test

Read [task guidance](../../TASKS.md). Read [deliver-reliable-changes](../deliver-reliable-changes/SKILL.md) for evidence and suite health, [journey-testing](../journey-testing/SKILL.md) for changed user journeys. Load the optional stack/domain guidance selected by task guidance only when relevant and available.

## Select meaningful coverage

Resolve the target from the supplied scope/current change and project instructions.

- Use deliver-reliable-changes to select meaningful checks and existing required suites.
- Add missing coverage for requested behavior where needed; do not silently alter production behavior, weaken assertions or inflate retries to pass.

## Execute and report the actual boundary

Select the evidence for the claim:

| Claim | Relevant boundary and guidance |
| --- | --- |
| Component/state behavior | Journey-testing guidance on Storybook when adopted; building the catalogue alone does not establish interaction coverage. |
| Full-stack behavior | Actual persistence and authorization contracts. |
| Web, desktop or mobile journey | Journey-testing and the actual target platform. |
| Load | Implementation expertise matching the selected load-test tool. |
| Bounded failure and recovery | Resilience-testing. |

A bare test request does not authorize deployed load or fault injection. Execute supported checks and diagnose failures, distinguishing application defects, fixture/environment issues and unexecuted checks.

Return results, artifacts, actual boundaries and the next action. A green build alone does not establish behavior.
