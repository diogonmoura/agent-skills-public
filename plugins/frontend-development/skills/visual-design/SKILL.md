---
name: visual-design
description: Derive an interface's visual direction from its users, tasks, content and environment. Use for a new product, substantial redesign, semantic tokens or a design-to-implementation handoff across web, desktop and mobile; preserve accepted identity during ordinary changes.
user-invocable: true
metadata:
  scope: generic
  invocation: both
  role: support
---

# Give the interface a product-specific visual direction

Define how the product's purpose becomes hierarchy, composition, typography, color, density and motion. Use the accepted product outcome and [interaction design](../interaction-design/SKILL.md) for behavior and affected surfaces. Preserve an established identity unless changing it is the objective. Routine copy or minor token changes need proportionate checks.

## Resolve the visual decision

Read the brief and work with the content the interface must actually carry. Identify what users need to notice first, how long they will spend reading or working, how much information they compare at once, and the environment in which they use the product. These questions give typography, density and composition a reason to take a particular form.

When direction is open, compare coherent alternatives that change the experience, rather than variations of the same starter. Explain how each handles the task and where it places attention. Choose a direction whose visual decisions can be traced to the brief: type should support the reading task, spacing should express relationships, color should establish roles, and motion should help explain change.

Distinguish requirements from inspiration and proposed choices. Use references for particular qualities you can name and adapt, not as whole layouts to imitate. Missing brand assets permit a reversible proposal that can be shown and critiqued; they do not require invented research or a blocked engagement.

Translate the direction into reusable roles. Give colors, type sizes, spacing and surfaces names that describe their use, then apply those roles consistently to shared components. These semantic tokens let the implementation preserve the design when a palette or component changes. Keep deliberate differences where the task needs them.

Use available visual-execution craft for composition, typography and critique when choices are open; the accepted identity and actual brief remain authoritative. Derive character from the content and the way people work with it. A decorative domain motif or recolored starter does not explain why the design suits the product. Read [visual direction and review](references/visual-direction.md) for substantial new work, redesign or handoff, including how to connect the design to components and inspect the implemented result.

## Build and inspect the design

Reuse accepted designs and choose an artifact that can answer the remaining question. Figma can support shared design work when available and authorized; local HTML/CSS can reveal responsive or interactive behavior; SVG can explain a static layout or flow. An explicitly required format remains part of the deliverable.

1. Build a representative part of the experience using realistic content. Include a difficult state, content growth and the layouts the task needs, so the design is judged beyond its most flattering empty screen.
2. Inspect where attention goes, whether content remains readable and how the composition handles those conditions. Repair mismatches with the intended direction before applying the pattern elsewhere.

Keep the reason for the choices, proposed versus accepted status, important states and reusable component/token roles in the existing design record. Technical guidance maps them to the chosen platform's real components; a generic design decision does not select React, Tailwind or a native framework.

Use [interface quality](../interface-quality/SKILL.md) for evidence-based critique and [UX writing](../ux-writing/SKILL.md) for task language. Reconcile the rendered implementation with the direction and report intentional deviations or unverified surfaces. A screenshot supports visual assessment; interaction, accessibility and persisted outcomes require their own evidence through the verification loop.

Return the direction, representative artifact, implementation mapping and actual review evidence within scope. Keep agent aesthetic assessment distinct from user acceptance and participant findings. A design-only request does not authorize implementation.
