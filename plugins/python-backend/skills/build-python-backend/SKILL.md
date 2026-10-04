---
name: build-python-backend
description: "Implement or review Python FastAPI APIs with Uvicorn, SQLAlchemy, Alembic, PostgreSQL, and optional FastMCP using repository conventions and official stack references."
---

# Python backend

Read `references/backend-contract.md` and the local application AGENTS.md. Respect project-profile.json; use official version-matched documentation for APIs and existing project tools for commands.

Use Python with uv for environments and a committed uv.lock. Use FastAPI and Uvicorn, Pydantic request/response schemas, SQLAlchemy 2-style models and queries, Alembic migrations, and PostgreSQL. Do not substitute SQLite, SQLModel, or a different web framework without an explicit project decision.

Organize by domain with thin HTTP routes, application services, persistence models, and adapters. Avoid mandatory layers that do not add value. Keep business logic independent of HTTP, MCP, and AI frameworks. Use dependency injection for database sessions and external services. Define transaction boundaries at the use-case level; do not share sessions across concurrent requests/tasks. Choose sync or async consistently based on dependencies; do not mix blocking database work into async handlers.

Use typed configuration, environment-derived secrets, structured logs, request IDs, health/readiness endpoints, and bounded timeouts. Validate authorization at resource boundaries; configure explicit CORS origins. Do not log tokens, raw audio, or private prompt contents.

Review generated Alembic migrations, including data backfills, locks, constraints, indexes, and rollback or forward-recovery strategy. Check migration from an empty database and the previous supported schema with PostgreSQL. Use expand/contract changes for deployments that require compatibility.

When MCP is needed, use FastMCP with narrow typed tools, explicit authorization, timeouts, and service-layer reuse. Expose chosen capabilities; do not automatically expose every API endpoint or raw database access. Verify the installed FastMCP transport and auth API in official docs. Use stdio for local integrations and Streamable HTTP for remote integrations as appropriate.

Test use-case behavior, request validation, authorization, persistence, and changed external adapters. Keep OpenAPI and data model documentation in sync.

For integration tests use migrated isolated PostgreSQL and actual application authorization. Generate OpenAPI and a version-aligned typed frontend client; check contract drift. Keep durable side effects idempotent and retry-bounded when they exist. Use explicit units and decimal arithmetic for monetary calculations, and property-based tests for important domain invariants where useful. These are capability-specific additions, not a requirement to add money, tenancy or background jobs to every application.
