---
name: prepare-pr
description: Draft or revise a pull request title and body for a Logic repository using the actual branch diff, issue, repository template, and verification evidence.
---
# Prepare a pull request

1. Confirm the target branch and compare from its merge base. Inspect committed changes and identify any uncommitted changes separately. Read the applicable repository instructions, contribution guide and PR template. Retrieve the linked issue when available.
2. Write a Conventional Commit title describing the outcome, for example `fix(gateway): preserve namespace on retry`. Mark breaking changes and describe migration impact.
3. Follow the repository template. Otherwise use Why, What changed, and Validation. Link the issue when known. Use a closing keyword only when the change satisfies its acceptance criteria.
4. Run the relevant checks within scope. Report exact commands, outcomes and skipped checks. Identify relevant generated files, compatibility evidence or UI proof. Include the changelog entry when the repository requires one.
5. Return the proposed title and body. Apply the repository's approval rules before committing, pushing or posting.
