# Working in the Logic repositories

At session start load [logic-start-work](.agents/skills/logic-start-work/SKILL.md). When drafting or submitting a PR load [logic-prepare-pr](.agents/skills/logic-prepare-pr/SKILL.md). In a product checkout resolve these paths from the product root. Use the issue forms and labels provided by the target repository.

Read the product's CONTRIBUTING.md when present and the instructions for the component you are changing. Follow local approval rules for implementation, commits, pushes, and GitHub writes.

Use the repository's build and generation commands. Edit generation inputs and verify the resulting diff. Identify affected consumers when changing a CRD, gateway contract, Data Index schema, or public console behavior. In reviews, describe the affected behavior, evidence, and suggested resolution. Distinguish blocking findings from optional suggestions.
