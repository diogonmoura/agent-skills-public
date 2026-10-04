# Agent Plugins

Reusable portable plugins for business strategy, visual communication, and consistent application development. Work in progress.

Packages follow [Agent Plugins 1.0.0](https://agent-plugins.org/specification). Each standalone package has plugin.json, skills/, and optional mcp.json. Existing skill names and complete resources are preserved.

## Packages

| Plugin directory | Skills |
| --- | --- |
| plugins/business-strategy | business-strategy v2.2, business-opportunity-analysis compatibility |
| plugins/visual-communication | architecture-diagraming, presentation-building |
| plugins/development-workflow | project-bootstrap, maintain-documentation, verify-delivery |
| plugins/python-backend | build-python-backend |
| plugins/web-frontend | build-consistent-frontend |
| plugins/ai-development | build-evaluated-ai |

The [full-stack profile](profiles/full-stack.json) selects workflow, backend and frontend; AI, strategy and visuals are optional. Profiles are repository conventions, not standard dependency manifests.

## Use

Select/install a plugin directory through your compatible client's documented flow. There is no universal plugin installation command in this standard. Load the three full-stack plugins together and add AI only when needed.

Create conventions in a new/empty project:

```bash
python3 plugins/development-workflow/skills/project-bootstrap/scripts/scaffold.py /path/to/new-project --ai adk --mcp
```

Omit --ai/--mcp for a normal application. This creates governance and documentation, not runnable application code. Fill the PRD, choose compatible dependencies, implement the first end-to-end slice and configure real verification commands.

Legacy skills-only fallback:

```bash
./scripts/sync-skills.sh sync
./scripts/sync-skills.sh status
./scripts/sync-skills.sh remove
```

The script discovers plugins/*/skills/*, repairs owned legacy links and preserves unrelated links. It does not install manifests/MCP. Old root skills/ paths moved to plugins/<package>/skills/<skill>/; update manually configured paths. The legacy business opportunity skill retains its fallback and sibling routing.

## Design and checks

- [Design and migration](documentation/plugin-design.md)
- [Official and community sources](documentation/upstream-sources.md)

```bash
python3 -m pip install -r requirements-validation.txt
python3 scripts/validate_plugins.py
python3 -m unittest discover -s tests -v
```

Validation covers official manifest schemas, skill metadata, package containment, profile references and scaffold regressions. Structural checks do not establish application correctness or semantic documentation freshness.

Upstream skill content is referenced, not vendored or installed. No MCP server is automatically launched; configure optional project integrations with the actual application path.

## Contributing

Keep skills concise and packages self-contained. Use references/templates/scripts for repeated work. Keep docs and evaluations aligned with behavior. Review/pin upstream content and preserve attribution before redistribution. MIT; upstream sources retain their licenses.
