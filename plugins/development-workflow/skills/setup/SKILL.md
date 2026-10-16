---
name: setup
description: Establish a new application or adopt an existing repository, discover
  working commands and accepted constraints, and prepare a useful first slice. Use
  for explicit project setup or adoption; preserve an existing project layout and
  tooling.
user-invocable: true
disable-model-invocation: true
metadata:
  scope: generic
  invocation: user
  role: task
---

# Setup

Read [task guidance](../../TASKS.md). Read [git-contributions](../git-contributions/SKILL.md) before foundation writes and [delivery-pipelines](../delivery-pipelines/SKILL.md) for CI, containers and release foundations. Read [project-conventions](../project-conventions/SKILL.md) for repository foundations and working commands. Load the optional stack/domain guidance selected by task guidance only when relevant and available.

Setup is technical foundation work, not a substitute for product discovery. Before architecture-dependent writes, establish the intended usage, bounded journey and material platform/licensing/budget constraints. For a rough idea needing end-to-end development, use the outcomes in [new-application flow](../develop/references/new-application-flow.md) within the requested scope; a setup-only request does not authorize feature implementation or an unsolicited full business study.

Use project-conventions to discover the repository, accepted stack, commands, identity model, environments and critical journey. In a new project establish only useful foundations for the requested first slice; in an existing one identify missing context without restructuring it. Ask about consequential product/platform choices, then record commands and accepted constraints in existing instructions/docs. Verify available startup/migration/test paths and identify missing prerequisites. Setup is not a claim that an application feature is complete. Use develop when the request is to build the application end to end.

For a new application, setup includes the complete applicable foundation contract in project-conventions: authored root/component READMEs, scoped instructions, configured code/configuration checks, runnable tests, app Dockerfiles/Compose where containerizable, GitHub Actions CI and artifact-release workflows, and a documented deployment/recovery process. Create and locally validate these files within the setup objective worktree. Identify unresolved delivery targets or unavailable native tools explicitly; foundation completion cannot hide missing applicable artifacts behind “first slice”. Preserve scope and working foundations when adopting an existing project.
