# Official backend references

Use version-matched APIs, not remembered signatures.

- FastAPI: https://fastapi.tiangolo.com/
- Reference implementation: https://github.com/fastapi/full-stack-fastapi-template (adapt backend patterns only; upstream uses Vite/React and SQLModel, whereas this profile requires Next.js and SQLAlchemy).
- Uvicorn: https://www.uvicorn.org/
- uv: https://docs.astral.sh/uv/
- SQLAlchemy: https://docs.sqlalchemy.org/en/20/
- Alembic: https://alembic.sqlalchemy.org/en/latest/
- PostgreSQL: https://www.postgresql.org/docs/
- FastMCP: https://gofastmcp.com/ ; machine-readable index https://gofastmcp.com/llms.txt

No verified first-party unified skill for this precise backend stack was located during this design. This plugin supplies the project-specific integration policy, grounded in official references. Do not mislabel community skills as framework-maintainer guidance.

A typical application contains src/<domain>/ routes, schemas, services, models; src/core/ configuration/auth/DB; optional src/ai/ and src/mcp/; migrations/ and tests/. API and MCP adapters call the same services. Database credentials and schema changes never belong in frontend code.
