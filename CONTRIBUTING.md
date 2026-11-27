# Contributing

Update the canonical AGENTS.md for shared policy and the skill directory for task procedures. Add a concrete acceptance scenario when changing skill behavior. Check product instructions for conflicting rules before distribution.

Review Actions changes against the triggers, permissions and expected output of each caller. Keep release credentials and publishing approvals in product workflows. Pin external actions to reviewed commits.

Use a Conventional Commit PR title. Explain why the change is shared, which consumers it affects, and how you tested it. Validate the ignored product cache with .agents/skills/logic-start-work/scripts/sync.py <product-root> --check.

## Add a Logic skill

Use one name throughout: `logic-<task>`. The folder name, frontmatter name and name in AGENTS.md must match. Each skill has one source directory under `.agents/skills/`.

1. Create `.agents/skills/logic-triage-issue/SKILL.md` for a task named `logic-triage-issue`. Start with the frontmatter below, then describe the inputs, expected outcome and decisions that require the engineer.
2. Keep scripts in the skill’s `scripts/` directory. Add a realistic prompt and observable acceptance criteria in `spec.md`.
3. Link the procedure from [AGENTS.md](AGENTS.md) and say when to load it. Product sync discovers the new `logic-*` directory automatically.
4. From this repository, run `python3 .agents/skills/logic-start-work/scripts/sync.py ../logic-operator`, then repeat with `--check`. Exercise the acceptance scenario in each client for which you claim support.

```yaml
---
name: logic-triage-issue
description: Classify a reported Logic issue and identify missing reproduction details.
---
```

For explicit invocation after sync, Codex accepts `$logic-prepare-pr`. In Claude Code or IBM Bob, ask the agent to follow `.agents/skills/logic-prepare-pr/SKILL.md` directly. The synced directory contains the procedure and all its supporting files.

The canonical GitHub issue forms, PR template and release categories live in .github here. Carry their changes to the product repositories through reviewed PRs so GitHub can read them from each default branch. Keep shared label names, colors and descriptions aligned with .github/labels.json and preserve product-specific labels.

For user-facing changes, add one outcome under Unreleased in CHANGELOG.md. Use Added, Changed, Deprecated, Removed, Fixed or Security. At release, move those entries to a dated version heading. Use the same categories for GitHub release notes, state breaking changes and migration steps explicitly, and verify generated notes against the curated changelog before publication.
