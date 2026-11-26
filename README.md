# Logic Agents

Shared contribution guidance, agent skills and GitHub Actions for Logic Apps, Operator and Consoles. Start with [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

## Distribute instructions

From this repository, run `python3 scripts/sync.py ../logic-operator`. Substitute the Apps or Consoles checkout as needed. Commit the resulting files in the product through its usual review process. A standalone clone can then read its local copy. To verify the snapshot, check out the revision listed in the product's .logic-agents/revision in this source repository and repeat with --check.

## Workflow review and adoption

| Area | Shared implementation or local responsibility |
| --- | --- |
| PR titles | Reusable pr-title.yml preserves Apps' semantic title check. |
| Pages | build-antora packages the Node 24 install and build used by Operator and Consoles. Apps builds with Maven. Keep triggers, upload paths and environment permissions in each caller. |
| Image publication | Apps and Operator both use Skopeo and Quay. Their image matrices, additional tags and release orchestration differ. Keep these jobs local until their inputs and retry behavior have a common contract. |
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
