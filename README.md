# Logic Agents

Shared contribution guidance, agent skills and GitHub Actions for Logic Apps, Operator and Consoles. Start with [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

## Distribute instructions

Each product tracks a bootstrap in AGENTS.md. It checks its ignored local copies on session start and before PR submission. A sibling logic-agents working tree takes precedence. Without one, the bootstrap clones or updates the published repository in the ignored cache. Before a PR, sync with `--pre-pr` to compare the source with published main. Sync records managed files in the ignored cache and retires them on subsequent runs. Merge shared guidance before adopting its product entry points.

Use `logic-start-work` at startup and `logic-prepare-pr` when preparing a PR. [AGENTS.md](AGENTS.md) links directly to each procedure.

## Workflow review and adoption

| Area | Shared implementation or local responsibility |
| --- | --- |
| PR titles | Reusable pr-title.yml preserves Apps' semantic title check. |
| Pages | build-antora packages the Node 24 install and build used by Operator and Consoles. Apps builds with Maven. Keep triggers, upload paths and environment permissions in each caller. |
| Image publication | Apps and Operator build their own OCI archives and select version and alias tags. The shared publish-quay-image.yml workflow uploads the archive to Quay, verifies Linux amd64 and arm64, applies aliases and returns the published digest. |
| Validation | Operator runs Go, generation, gateway and KIND checks. Apps builds and tests Data Index and checks Quarkus Flow snapshots. Consoles runs frontend and browser checks and reuses its CI on release. |
| Releases | Keep version sources, tag creation, Helm and CRD packaging, image publication, launcher builds and checksums with each product. |
| Maintenance | Apps' knowledge graph refresh operates on its own repository data. |

After publishing this repository, use its full commit SHA in the caller. Example PR-title caller:

```yaml
name: Check PR Title
on:
  pull_request_target:
    types: [opened, edited, synchronize, reopened]
permissions:
  pull-requests: read
jobs:
  title:
    uses: kubesmarts/logic-agents/.github/workflows/pr-title.yml@<full-commit-sha>
```

For Operator and Consoles docs builds, keep checkout and replace the Node setup, install and build steps with:

```yaml
- uses: kubesmarts/logic-agents/.github/actions/build-antora@<full-commit-sha>
```

Review required status check names before migrating a caller.
