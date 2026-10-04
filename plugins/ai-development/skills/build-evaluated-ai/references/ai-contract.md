# AI references and choices

- Google ADK skills: https://github.com/google/adk-python/tree/main/.agents/skills ; adk-agent-builder and adk-architecture are relevant sources, to be reviewed/pinned before installation.
- ADK docs: https://google.github.io/adk-docs/
- LangChain first-party skills: https://github.com/langchain-ai/langchain-skills ; select ecosystem-primer, dependencies, fundamentals, and LangGraph persistence where needed. Override upstream provider defaults explicitly with the project's Gemini configuration.
- Google GenAI SDK: https://googleapis.github.io/python-genai/
- Gemini pricing: https://ai.google.dev/gemini-api/docs/pricing
- Gemini rate limits: https://ai.google.dev/gemini-api/docs/rate-limits
- Audio/transcription: https://ai.google.dev/gemini-api/docs/audio
- Free tier regional availability: https://ai.google.dev/gemini-api/docs/billing/

Use one agent framework per application unless an ADR explains the need for both. Framework selection is a project decision; references do not automatically install skills or servers.

Free-tier access is model/account/quota-dependent, including audio support. Verify the actual chosen model and account; fail clearly rather than auto-upgrading to paid usage. Keep live evaluations opt-in. Ordinary CI is offline/deterministic. Distinguish uploaded-audio transcription from real-time voice and text-to-speech.

For transcription evals include synthetic or consented short clips, accents/noise where relevant, language handling, empty/invalid audio, and word error rate. For agents include schema validation, authorization failures, injection attempts, timeout/retry behavior, tool-call limits and task completion. Report provider/model/version/config with outcomes.
