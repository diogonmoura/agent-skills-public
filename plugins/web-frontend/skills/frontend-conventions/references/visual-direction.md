# Derive and verify a product-specific visual direction

Use this for a new application, substantial redesign or a brief without an established visual system. Keep the result in the existing product/design note; a new document or approval ceremony is not required.

## Connect product intent to appearance

Read the accepted product brief/PRD: who uses the product, their primary task, meaningful content, frequency, environment and constraints. Distinguish accepted requirements from proposals. If no brief exists, establish a concise first-slice product/UX brief rather than inventing research or commercial decisions. Carry its main scenarios and states into implementation and evaluation.

Choose a coherent direction, considering a few genuinely different alternatives where useful. Explain why the recommendation fits. Use relevant visual references when available; identify what each contributes without copying assets or assuming that popularity establishes fit. With no supplied reference, make a reversible recommendation and show it. Do not block routine work waiting for brand assets.

Define the choices that materially shape the experience: information hierarchy, composition, density, type hierarchy, reading/editing measure, palette and contrast, spacing, surfaces, iconography, motion and distinctive domain details. Ground character in actual content and workflows. A research notebook may benefit from editorial reading and useful note metadata; an architecture canvas prioritizes drawing space, legible labels and quiet contextual tools. These illustrate reasoning, not mandatory themes. Avoid fake metrics, excessive decoration and domain-themed gimmicks. A recolored starter layout is insufficient evidence of contextual design.

## Implement through the chosen system

For a new React DOM app, including a Tauri webview, use compatible Tailwind and actual shadcn primitives as the default. Record a justified exception. Preserve the selected component API/preset, semantic CSS-variable theme pairs and a coherent Tailwind theme mapping. Theme typography, spacing, radii and states as a system; compose product-specific layouts rather than replacing primitives with handwritten lookalikes or scattering literal overrides. Preserve accepted existing libraries.

For React Native use native components and supported styling/theming tools, carrying over design intent and appropriate semantic tokens. Do not install web shadcn widgets to satisfy this preference. Native navigation, keyboard, safe areas and accessibility remain platform-specific.

Follow current version-matched [shadcn theming](https://ui.shadcn.com/docs/theming) and [Tailwind theme guidance](https://tailwindcss.com/docs/theme); use the bundled upstream skills for unfamiliar implementation details. Do not mix documentation generations or layer a competing token system over the selected preset.

## Render one useful slice, then propagate

Build and inspect a representative real screen with realistic content before rolling out the pattern. Include a difficult state or interaction, not just an attractive empty shell. Compare hierarchy, readability, density, alignment, component consistency and product character with the direction. Repair and re-render when the result misses it. Keep concrete screenshots/findings so the next iteration can be compared.

Then apply the system to all affected surfaces and states: populated/empty, loading, error/retry, selection, editing and relevant narrow or native layouts. Protect existing behavior with meaningful regression tests. Do not fill the app with invented data just to make screenshots look finished.

## Separate evidence and completion claims

| Claim | Evidence |
| --- | --- |
| Product fit | Main scenarios and content trace to the accepted brief; assumptions remain explicit. |
| Visual quality reviewed | Actual target screenshots compared with the direction/references; concrete findings repaired or openly unresolved. Human/user aesthetic feedback is separate from the agent's review. |
| Interaction/accessibility checked | Keyboard/focus, labels, contrast, relevant screen-reader and responsive/native states exercised; automation plus targeted manual operation. |
| Feature verified | Committed component/regression tests and a critical UI/API/persistence journey, including relevant failure/denial cases. |
| Visual regression protected | Meaningful screen/state baselines reviewed against the intended design; new screenshots are not automatically approved as correct. |

No test score proves taste, and a passing build or component suite cannot establish any of the other rows. Do not claim user approval that was never obtained. Finish within the requested scope with evidence or a precise partial result; do not require approval for every screen. Use actual user feedback to revise the direction and its acceptance criteria.
