---
name: build-evaluated-ai
description: "Build or review AI features with Google ADK or LangChain/LangGraph, configurable Gemini LLM and audio-transcription testing, tool boundaries, deterministic fixtures, and live evaluations."
---

# Evaluated AI development

Read `references/ai-contract.md` and the local profile. Add AI infrastructure only for an AI requirement.

Prefer the Google GenAI SDK directly for simple generation/transcription. Use Google ADK for agent workflows with its useful session/tool/runtime model; use LangChain/LangGraph when ecosystem integrations or explicit stateful orchestration justify them. Record the framework choice in an ADR. Do not install both by default. Load relevant first-party skills from google/adk-python or langchain-ai/langchain-skills as described in references.

Define narrow provider-neutral interfaces for generation and transcription. Keep model IDs configurable as GEMINI_LLM_MODEL and GEMINI_STT_MODEL; keep GEMINI_API_KEY in environment-derived configuration. The scaffold does not pick a model or promise a free tier. Verify availability, audio support, quota, region, and pricing when selecting models. Do not silently fall back to a paid model/provider.

Use Gemini audio understanding for uploaded-audio transcription where supported. Treat live streaming voice as a separate capability with its own transport, transcription, latency, and pricing requirements. Test Portuguese from Portugal when it is a product requirement. Respect audio retention and consent requirements actually applicable to the project.

Keep prompts, tool definitions, fixtures, and evaluators versioned. Use structured output with schema validation. Apply timeouts, bounded retries, rate-limit handling, token budgets, and a loop/tool-call limit. Separate trusted instructions from retrieved content. Enforce authorization in tools, not only prompts. Require idempotency for repeatable side effects.

Run ordinary CI against deterministic mocks/recorded synthetic fixtures. Use opt-in Gemini smoke tests and curated live evals for schema adherence, tool selection, grounded answers, failure handling, latency, cost, and speech word error rate. Avoid exact-string assertions on live model output. Store model/config/evaluation metadata; never commit keys or private recordings.

Maintain architecture, AI evaluation guidance, limitations, and runbooks with the implementation.
