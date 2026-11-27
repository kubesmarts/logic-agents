---
name: logic-start-work
description: "logic-start-work — refresh shared guidance and resolve the issue, repository, and branch when starting or resuming Logic work."
---
# logic-start-work

Use the issue URL or fully qualified owner/repository#number, the target checkout, and its current branch as inputs. Take known values from the request and repository. Ask for missing issue information before choosing a branch.

1. From the canonical skill directory in the sibling or cached source checkout, run `python3 scripts/sync.py /absolute/path/to/product` (the script path is relative to this skill directory). When preparing a PR add `--pre-pr` to verify the source includes published main. Report local development revisions or uncommitted guidance in the verification summary. In logic-agents itself the canonical files are already local. Read the refreshed shared AGENTS.md and applicable component instructions.
2. Verify the issue repository, number and scope. If starting a new issue, use the target repository's bug or feature form, identify a testable outcome, and confirm authorization before posting.
3. Inspect the current branch and working tree. Use `issues/<number>` in the issue-owning repository and `issues/<issue-repository>-<number>` elsewhere. For kubesmarts/logic-agents#1 this means `issues/1` in logic-agents and `issues/logic-agents-1` in a product. If the right branch is missing or a switch is needed, ask before creating or switching unless the human already authorized it. Preserve existing work.
4. Never edit or commit on main. Omit agent co-author trailers and agent attribution in commits and PR bodies. Follow product-specific approval rules.
