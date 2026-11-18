# Contributing

Thanks for helping make this a practical catalog of reusable game-development building blocks.

## What belongs

- A public GitHub repository with source code, a working tool, a reusable library, a starter/template, a complete game, or a reference implementation.
- A clear use in one or more phases of game development.
- A repository URL at the project root (`https://github.com/owner/repo`).
- A short, factual description. State what the project does; do not make unsupported quality, compatibility, security, or maintenance claims.

## What does not belong

- Non-repository links, asset marketplaces, commercial products without a GitHub code repository, or general programming projects with no concrete game-development use.
- Duplicate entries, forks that add no distinct value, abandoned experiments presented as maintained tools, or promotional submissions.
- Descriptions that imply universal compatibility. Identify the engine, language, or platform when known.

## Submit a change

1. Pick the best-fit section in `README.md`.
2. Add one bullet in this format: `- [owner/repo](https://github.com/owner/repo) — concise description.`
3. Keep the link at the repository root and check for duplicates.
4. If the repository is archived, mark it as `[Archived]` in the description or omit it unless it remains useful as a reference.
5. Run `python3 scripts/validate.py` and include the result in your pull request.

The list is a discovery index, not an endorsement. Readers must check upstream licensing, activity, compatibility, and security before adopting a project. Each linked repository retains its own terms.
