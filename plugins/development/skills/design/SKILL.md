---
name: design
description: Design UI interactions, backend contracts or architecture for a requested
  change before implementation. Use for flows, navigation, shared components, API/data/state
  behavior or consequential design alternatives; produce concise text and useful wireframes/mockups
  when needed.
user-invocable: true
disable-model-invocation: true
metadata:
  scope: generic
  invocation: user
  role: task
---

# Design

Read [task guidance](../../TASKS.md). Use [system-design](../system-design/SKILL.md) after product refinement or when the feature changes consequential architecture, before dependent planning/implementation. When data or authority boundaries change, seek relevant security/privacy design expertise from available descriptions; retain the affected authority, data-flow and verification reasoning when a specialist is absent. Load the optional stack/domain guidance selected by task guidance only when relevant and available.

Establish the audience, intended outcome, accepted decisions and affected boundaries from supplied references and repository evidence. Choose the supporting methods through task guidance; keep the result proportionate to the uncertainty.

## Design the affected interface

For UI work establish contextual visual direction, flows, state and affected-surface coverage. Choose methods for the unresolved question:

| Question | Relevant expertise or artifact |
| --- | --- |
| Product-specific visual direction | Available visual design expertise |
| Flow, state and behavior | Available interaction design expertise |
| Layout or navigation uncertainty | Text, wireframes, Figma or local prototypes, according to the question and available tools |
| Rendered quality or consequential language | Available interface assessment or interface-language expertise |
| A question needing participant evidence | Available usability research expertise |

Establish a representative design before propagating it. Connect agreed decisions to tokens/components and the implementation handoff. Stack conventions map the design to implementation; Storybook can verify implemented component states later.


## Establish service behavior

For backend work, establish public contracts, actor authority, invariants, state/failure and compatibility before choosing implementation layers or framework APIs. Use available service-contract design expertise for behavior and system-design for architectural boundaries.

## Resolve choices and hand off

Compare consequential alternatives against constraints and tradeoffs; retain existing decisions where suitable. Ask about unresolved high-impact choices, record reversible assumptions and continue when the direction is sufficiently established.

Return the agreed/proposed design, acceptance evidence and explicit unknowns. A design request does not silently authorize implementation or impose a design-document approval gate on trivial edits.
