---
name: write-scannable-documentation
description: Write or revise product and engineering documents so readers can find
  decisions, behaviour, constraints and procedures quickly. Use for PRDs,
  requirements, architecture, feature plans, operational guides and documentation
  readability reviews. Preserve technical meaning and existing document ownership.
metadata:
  scope: generic
  invocation: both
---

Read [workflow framing](../../WORKFLOW.md) for scope and invocation boundaries.

# Write documentation readers can scan

Apply this guidance when drafting or revising persistent product and engineering documents. Keep the project's language, terminology and established conventions. Improve presentation without changing scope, requirements or architecture unless that work was requested.

## Start with the reader's task

Identify what the reader needs to find, decide or do. Open with the document's purpose and its relevant status or scope in a few lines. Link supporting contracts instead of repeating their background. Keep implementation review dates separate from editorial updates; reformatting does not verify behaviour.

## Give each topic a useful heading

Use a single title and descriptive, sentence-case headings. Use second-level headings for major concerns and third-level headings for independently useful topics within them. Split a section when its paragraphs answer different questions, such as runtime, ownership and migrations. Keep related detail together; do not create a heading for every sentence or impose a fixed section count.

For a long reference, add a short linked contents list when the renderer does not provide adequate navigation. Headings should let someone locate a topic without reading the surrounding paragraphs. Prefer “Migration execution” to “Other considerations”. Avoid heading levels skipped merely for visual size.

## Choose the form that fits the information

| Information | Useful presentation |
| --- | --- |
| Explanation, rationale or a tradeoff | Short paragraphs, each developing one point |
| Independent rules, capabilities or constraints | Bullets with parallel phrasing |
| A procedure with dependencies | Numbered steps with prerequisites and expected results |
| Comparable options, responsibilities or states | A compact table with consistent columns |
| Relationships, boundaries or event flow | A diagram with a short explanation and links to detail |
| Exact commands, schemas or examples | Fenced blocks with the necessary context |

Lead paragraphs with their main point. Two to four sentences often suffice; split when the subject changes, not to meet a word quota. Use concrete actors and verbs. Explain unfamiliar acronyms on first use. Keep identifiers and units exact.

Tables support comparison, not paragraphs squeezed into cells. Move long conditions into a nearby subsection, keep tables narrow enough to read, and preserve the association between a rule and its exception. Use lists only when the items really are parallel or sequential. Do not fragment causal reasoning into unrelated bullets.

## Adapt to the document

- PRDs and requirements: make outcomes, acceptance criteria and constraints easy to locate. Preserve requirement IDs and status.
- Architecture: separate runtime responsibilities, data/authority boundaries and important flows. Keep rationale beside the design it explains.
- Work packages: expose scope, dependencies, decisions, open questions and completion evidence without copying the whole PRD.
- Operational guides: make prerequisites, ordered actions, verification, failure handling and recovery easy to find. Keep safety conditions beside the affected step.

These are presentation choices within the existing document, not instructions to create new files or mandatory templates.

## Preserve accuracy and review the result

Keep links, code, quantities, exceptions, assumptions and evidence. Distinguish implemented, proposed, approved, measured and verified claims. Do not promote a target or configuration into a delivered capability to shorten a sentence. Leave generated inventories intact unless their generator is in scope.

Review headings alone: can the reader find each major topic? Then skim the opening sentences, lists and tables: are the conclusions visible and the qualifications still attached? Finally compare the revision against the source for omitted facts, changed meaning and broken links. Check the rendered document when the repository offers a preview; a prose rewrite alone does not require application tests.

Apply `humanizer` for wording and voice where available. Keep the useful headings, procedures and comparisons; removing formulaic prose does not mean flattening the document into paragraphs. Checks for links and packaging establish structural validity, not writing quality.
