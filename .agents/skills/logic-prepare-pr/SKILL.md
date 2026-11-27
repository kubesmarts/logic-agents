---
name: logic-prepare-pr
description: "logic-prepare-pr — prepare or revise a concise, issue-linked Logic pull request from its branch diff and verification evidence."
---
# logic-prepare-pr

Refresh the guidance using the product AGENTS.md entry point and logic-start-work with `--pre-pr`. Resolve any stale-source error before submitting. Confirm the target branch, inspect the merge-base diff, and separate any unstaged work. Read the issue, contribution guide and PR template.

An issue is required to open a PR. If none is identified, pause and ask the human to supply the issue or confirm creating one. Wait for its real number before opening the PR.

Use a Conventional Commit title. Answer the template’s three questions in your own words. Give reviewers enough context to judge the problem, the outcome and the evidence. Use a short paragraph or bullets as the change warrants. Include an implementation detail only when it explains a decision, risk or upgrade step that affects the review. Leave file inventories and line-by-line narration to the diff. Link longer evidence, report relevant skipped checks, and describe only verification you can substantiate. Exclude agent co-author attribution.

End with `Fix: #123` when this PR completes the issue. For a partial umbrella PR, use `Refs: kubesmarts/logic-agents#1` and leave closure to the final PR. Qualify every cross-repository reference with the issue owner and repository.

Update the Unreleased changelog for user-facing changes. Return the draft and follow product approval rules before publishing.
