---
name: plan
description: Plan implementation of agreed work using repository context, dependencies,
  verification and release consequences. Use for a bounded feature/refactor plan;
  do not turn a small fix into a mandatory planning workflow.
user-invocable: true
disable-model-invocation: true
metadata:
  scope: generic
  invocation: user
  role: task
---

# Plan

Read [task guidance](../../TASKS.md). Reuse existing plans and commands; scale the plan to the agreed work.

## Establish the planning basis

- Agree on the outcome and completion evidence. Refine material gaps before assuming scope.
- Inspect affected architecture and contracts. Use [system-design](../system-design/SKILL.md) after product refinement or when the feature changes consequential architecture, before dependent planning or implementation.
- Read [project conventions](../project-conventions/SKILL.md) for existing constraints and [delivery guidance](../deliver-reliable-changes/SKILL.md) for acceptance and verification.
- Load optional stack/domain guidance selected by task guidance only when relevant and available. Use service-contract design expertise for changed service behavior.

## Order the work by its dependencies

Use relevant technical conventions to choose small increments. Include the consequences that apply:

| Affected concern | Include in the plan |
| --- | --- |
| UI or interaction behavior | UI/behavior design before dependent implementation |
| Persistence or consumers | Migration and compatibility work |
| Acceptance and regression risk | Focused tests and their evidence |
| Delivery and failure | Release and recovery consequences |

## Return an executable plan

Provide next steps in dependency order, assumptions and blockers. A tracker, a document per slice and parallel agents are optional. Planning alone does not implement or deploy the work.
