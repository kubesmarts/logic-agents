# Working in the Logic repositories

Read the product's CONTRIBUTING.md when present and the instructions for the component you are changing. Follow local approval rules for implementation, commits, pushes, and GitHub writes.

Use the prepare-pr skill under the product root's .agents/skills/prepare-pr/ when drafting or revising a pull request. For issues, describe the observed problem or user need, the affected version, and an observable acceptance criterion. Select labels that exist in the target repository.

Use the repository's build and generation commands. Edit generation inputs and verify the resulting diff. Identify affected consumers when changing a CRD, gateway contract, Data Index schema, or public console behavior. In reviews, describe the affected behavior, evidence, and suggested resolution. Distinguish blocking findings from optional suggestions.
