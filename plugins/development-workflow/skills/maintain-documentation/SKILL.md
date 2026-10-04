---
name: maintain-documentation
description: "Create or update application PRDs, ADRs, roadmaps, plans, C4 architecture, data models, schemas, decision logs, runbooks, and requirements traceability when implementation or decisions change."
---

# Maintain application documentation

Read `references/documentation-contract.md`. Use the project's canonical `documentation/` tree; avoid creating parallel sources of truth.

Before changing code, identify affected requirements, architecture, contracts, persistence, UX, and operations. Read their current documents. Apply explicit user scope without adding speculative features.

For every meaningful change, update affected documents in the same change. Record an ADR for a consequential architectural choice; use the decision log for smaller decisions. Link accepted ADRs from the log rather than copying them. Supersede old ADRs; do not rewrite their historical reasoning.

Distinguish current implementation, approved future work, proposals, and unresolved questions. Keep the roadmap outcome-focused and plans task-focused. Give requirements stable IDs and link them to implementation and verification evidence.

Generate OpenAPI, JSON Schema, and database schema snapshots from the implementation when possible. Never edit generated schemas manually. Put generators and their commands in the application; check generated diffs in CI. Describe ownership, constraints, and relationships in the data model.

Use arc42 for architecture narrative, C4 context/container diagrams by default, and component/runtime/deployment diagrams when they add information. Store text diagram sources in Git. Interactive HTML diagrams may supplement these sources.

Before completion, inspect code/doc consistency and broken local links. A touched document is not proof of semantic consistency. Explain material limitations and missing evidence; never invent passing validation.
