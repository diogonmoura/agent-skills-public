# Upstream source catalogue

Reviewed 2026-10-04. Reference-only: not bundled or installed. Review exact version/path/license before acquiring; select relevant skills rather than unrelated whole catalogues.

| Area | Source | Qualification |
| --- | --- | --- |
| React performance, composition, UX review | https://github.com/vercel-labs/agent-skills | First-party Vercel: React practices, composition, web-design-guidelines |
| Next.js | https://github.com/vercel/next.js/tree/canary/skills | Current source; match stable chosen framework release, do not adopt canary as an application dependency |
| shadcn skill | https://ui.shadcn.com/docs/skills | Official; reads actual project configuration |
| shadcn MCP | https://ui.shadcn.com/docs/mcp | Official; configure application path/components.json |
| UI/UX Pro Max | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | Community; constrain to established tokens and patterns |
| Visual exploration | https://github.com/anthropics/skills/tree/main/skills/frontend-design | First-party Anthropic; optional, avoid style drift during cleanup |
| ADK | https://github.com/google/adk-python/tree/main/.agents/skills | First-party agent-builder/architecture skills; review transitive resources |
| LangChain/LangGraph | https://github.com/langchain-ai/langchain-skills | First-party fundamentals/persistence/evaluation; override provider defaults with Gemini |
| Backend template | https://github.com/fastapi/full-stack-fastapi-template | Official reference; SQLModel/Vite defaults differ from requested SQLAlchemy/Next.js |
| FastAPI/Uvicorn/uv | https://fastapi.tiangolo.com/ ; https://www.uvicorn.org/ ; https://docs.astral.sh/uv/ | Official runtime/reference documentation |
| SQLAlchemy/Alembic/PostgreSQL | https://docs.sqlalchemy.org/en/20/ ; https://alembic.sqlalchemy.org/en/latest/ ; https://www.postgresql.org/docs/ | Official persistence documentation |
| FastMCP | https://gofastmcp.com/llms.txt | Official index; no unified backend skill asserted |
| Gemini | https://ai.google.dev/gemini-api/docs/audio ; https://ai.google.dev/gemini-api/docs/pricing ; https://ai.google.dev/gemini-api/docs/rate-limits | Verify selected LLM/audio model and free-tier quota |
| Architecture/ADRs | https://arc42.org/overview/ ; https://c4model.com/diagrams ; https://adr.github.io/madr/ | Recognised structures adapted into lean local templates |

Record source commit/release, selected skills, license, scripts/network behavior and actual install route in project-profile.json. The standard is not a universal dependency installer. Do not redistribute private skills.

Official documented skills CLI examples: `pnpm dlx skills add shadcn/ui`; `npx skills add vercel-labs/agent-skills`; `npx skills add vercel/next.js`. These acquire skills, not complete portable plugins. They have not been executed by this release.
