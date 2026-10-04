# Harness contract

## Context layers

Root AGENTS.md contains enduring invariants and exact entrypoints, scoped AGENTS.md contains domain-specific rules, project-profile.json contains structured decisions and command arguments, docs contain current product/architecture state, skills provide task-specific procedure, scripts/CI enforce mechanical rules.

Prefer explicit documentation retrieval and version-matched knowledge over remembered framework APIs. Essential rules cannot rely only on optional skill activation. Each rule has one canonical owner; avoid contradictions and duplicating a rule across every document.

## Engineering workflow

Build a complete small user flow early. Architecture defaults to a modular backend with clear adapters unless independent deployment justifies more services. Define API/schema contracts before independent frontend/backend tasks and verify their integration afterward. Reproducible setup and feedback are part of the feature, not later cleanup.

Use narrow task scopes, checkpoint state for long-running work, request/tool/time/token limits where configured, and scoped credentials for consequential tool use. Keep authorization, tenant boundaries, budget enforcement, idempotency and state transitions deterministic outside LLM reasoning. No requirement to use multi-agent execution for ordinary application work.

## Recovery and learning

Capture repeatable setup failures, flaky tests, design drift and stale context. Prefer mechanical fixes to more prose. Track harness changes with a small representative evaluation suite: new CRUD flow, resource auth failure, schema change, component reuse, dependency upgrade, external API failure, AI tool authorization, existing-repo adoption.

## References

https://agents.md/
https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
https://github.com/obra/superpowers/tree/main/skills/systematic-debugging
https://github.com/obra/superpowers/tree/main/skills/verification-before-completion
