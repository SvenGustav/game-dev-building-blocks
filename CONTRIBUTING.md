# Contributing

Help keep this a practical catalog of reusable game-development parts, not a showcase of finished games.

## What belongs

- A public GitHub repository with reusable code, an engine or framework, a working tool, a content pipeline, or a genuine starter template.
- At least 10 GitHub stars when checked.
- A clear use in game development, with an engine, game type, and development layer that can be stated from the repository itself.
- A repository-root URL (`https://github.com/owner/repo`) and a short factual description.

## What does not belong

- Repositories below 10 stars.
- Complete games, game/demo/sample projects, tutorials, learning-only repositories, resource roundups, or other awesome lists.
- Asset marketplaces, commercial products without a GitHub code repository, and general-purpose projects without a concrete game-development use.
- Entries with unclear provenance or descriptions that claim compatibility, security, quality, or maintenance without evidence.

A reusable engine or system may mention its own sample game; that does not make the repository a sample project. Explicit reusable templates are allowed when they provide a real base for new work.

## Add or update an entry

1. Check the repository is public, has at least 10 stars, and contains the code or tool being described.
2. Add one record to `data/catalog.json`: repository, URL, factual description, star count, engine tags, game-type tags, workflow, language, license, archive status, and last-push metadata.
3. Use `Cross-engine` only when the project is not tied to a named engine. Use `Cross-genre` when no game type is clearly supported.
4. Do not tag an engine or game type just because it appears incidentally in the README; tag only a stated integration or a clear use case.
5. Rebuild and validate:

   ```sh
   python3 scripts/build_catalog.py
   python3 scripts/validate.py
   ```

Star counts are snapshots and can fall below the threshold later. Refresh the metadata and remove entries that no longer meet the rule.

The catalog is a discovery index, not an endorsement. Each project retains its own license. Check current license terms, supported versions, maintenance, security, platforms, and integration fit before adopting any part.
