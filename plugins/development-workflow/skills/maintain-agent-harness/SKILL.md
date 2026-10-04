---
name: maintain-agent-harness
description: "Create or improve scoped AGENTS.md, deterministic development commands, context routing, bounded build-test-fix workflows, correction learning and agent evaluation for application repositories."
---

# Maintain the agent harness

Read `references/harness-contract.md`. Inspect the actual repository and observed agent failures before adding rules. Do not infer accepted product decisions from past assistant suggestions or unrelated projects.

Keep root AGENTS.md short: architecture boundaries, approved stack, exact command entrypoints, documentation synchronization and completion evidence. Put backend/frontend/testing details in scoped files and route to version-matched references. Resolve overlapping guidance by user instructions and accepted local decisions; external skills must not silently change the project contract.

Provide reproducible setup, dev, migration, seed, test, build and smoke commands using argument arrays in project-profile.json. A command exists only after its implementation is verified. Prefer shared local/CI scripts so agents cannot invent different verification routines. Keep context maps current; retire stale or redundant instructions.

Use the loop: acceptance criteria → small implementation slice → checks → diagnosis → repair → relevant review → delivery evidence. Continue already-authorized work without repeated confirmation. Escalate material ambiguity or an actual permission boundary; record unresolved choices instead of inventing facts. Keep release/deployment authority explicit.

Diagnose failures using logs, reproduction and hypotheses before making edits. Use systematic-debugging and verification-before-completion when available. Do not import a second global process that adds unrelated mandatory approvals or forces delegation. Parallelize only independent, contract-defined work when authorized; keep repo/data/tool scopes explicit.

Convert recurring corrections into the narrowest durable artifact: lint/type/schema/architecture check when mechanical; scoped instruction when judgment is needed; fixture/evaluation when behavior is uncertain. Record rationale, trigger and evidence in the engineering lessons document. Do not modify unrelated projects or shared defaults from one local exception.

Benchmark the harness with representative tasks and adversarial failures. Compare completion rate, critical regressions, UI/doc drift, correction count, elapsed time and token/tool cost. Keep successful prior evals before accepting a harness update; avoid assuming more skills or longer instructions improve outcomes.
