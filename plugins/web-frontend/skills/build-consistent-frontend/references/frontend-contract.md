# Frontend sources and integration policy

Prefer first-party sources:
- shadcn official skill: https://ui.shadcn.com/docs/skills ; source https://github.com/shadcn-ui/ui ; CLI installation example `pnpm dlx skills add shadcn/ui`.
- shadcn MCP: https://ui.shadcn.com/docs/mcp ; configure access to this application's components.json, not the plugin directory. No automatic MCP configuration is bundled because the portable MCP default cwd is the plugin root and the application path is chosen at runtime.
- Vercel React, composition and web design skills: https://github.com/vercel-labs/agent-skills
- Next.js current skills: https://github.com/vercel/next.js/tree/canary/skills ; prefer release/version-matched framework docs. Former https://github.com/vercel-labs/next-skills points to this new location; do not rely on an obsolete next-best-practices installation.
- Vercel deployment/docs: https://vercel.com/docs ; opt-in hosting.
- UI/UX Pro Max: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill ; community guidance, constrained by local design-system.md.
- Anthropic frontend-design: https://github.com/anthropics/skills/tree/main/skills/frontend-design ; optional visual exploration only.

The prior user-selected recommendations are web-design-guidelines, React practices, constrained UI/UX Pro Max, and project-local frontend governance. Their current installation cannot be inferred from a reference or earlier recommendation. Read actual installed skill metadata when available. Do not redistribute private/plugin-provided skills merely because they are installed.

## First screen contract

Define semantic color tokens, spacing, type hierarchy, component variants, icon set, navigation, content density, responsive behavior, and loading/empty/error states. Implement one representative screen and reuse its components. Treat design changes as explicit decisions. shadcn primitives may use different base libraries; inspect components.json rather than assuming Radix.
