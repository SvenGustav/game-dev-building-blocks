# Game Dev Building Blocks [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome#readme)

A curated, engine-first index of reusable game-development foundations: engines, frameworks, gameplay systems, shaders, art and asset tools, story systems, networking, testing, and release tooling. It helps developers and coding agents assemble working parts instead of starting from an empty project.

**309 unique repositories · minimum 10 GitHub stars · no complete-game or demo-project listings**

Star counts are point-in-time GitHub metadata. They are a discovery threshold, not a quality, security, maintenance, or compatibility guarantee. Check each repository's current status, license, supported versions, and integration requirements.

## Choose an engine stack

Each engine page groups the same development layers. Godot, Unity, Unreal, and Bevy pages include shared tools for art, sprites, animation, shaders, levels, and assets alongside engine-specific projects.

- **[Godot](docs/engines/godot.md)** — 40 engine-tagged repositories
- **[Unity](docs/engines/unity.md)** — 60 engine-tagged repositories
- **[Unreal Engine](docs/engines/unreal-engine.md)** — 14 engine-tagged repositories
- **[Bevy](docs/engines/bevy.md)** — 5 engine-tagged repositories
- **[libGDX](docs/engines/libgdx.md)** — 1 engine-tagged repository
- **[Stride](docs/engines/stride.md)** — 2 engine-tagged repositories
- **[GameMaker](docs/engines/gamemaker.md)** — 1 engine-tagged repository
- **[GDevelop](docs/engines/gdevelop.md)** — 1 engine-tagged repository
- **[Glide](docs/engines/glide.md)** — 1 engine-tagged repository
- **[Construct 2](docs/engines/construct-2.md)** — 1 engine-tagged repository
- **[Defold](docs/engines/defold.md)** — 2 engine-tagged repositories
- **[Phaser](docs/engines/phaser.md)** — 2 engine-tagged repositories
- **[Cocos](docs/engines/cocos.md)** — 1 engine-tagged repository
- **[LÖVE](docs/engines/love2d.md)** — 2 engine-tagged repositories
- **[Flame](docs/engines/flame.md)** — 1 engine-tagged repository
- **[MonoGame](docs/engines/monogame.md)** — 3 engine-tagged repositories
- **[HaxeFlixel](docs/engines/haxeflixel.md)** — 1 engine-tagged repository
- **[Three.js](docs/engines/threejs.md)** — 7 engine-tagged repositories
- **[Babylon.js](docs/engines/babylonjs.md)** — 1 engine-tagged repository
- **[melonJS](docs/engines/melonjs.md)** — 1 engine-tagged repository
- **[Wicked Engine](docs/engines/wicked-engine.md)** — 1 engine-tagged repository
- **[PixiJS](docs/engines/pixijs.md)** — 2 engine-tagged repositories
- **[Raylib](docs/engines/raylib.md)** — 3 engine-tagged repositories
- **[SDL/SFML](docs/engines/sdl-sfml.md)** — 7 engine-tagged repositories
- **[OpenRA](docs/engines/openra.md)** — 1 engine-tagged repository
- **[Quake/id Tech](docs/engines/quake-idtech.md)** — 2 engine-tagged repositories
- **[X-Ray](docs/engines/x-ray.md)** — 1 engine-tagged repository
- **[Luanti](docs/engines/luanti.md)** — 1 engine-tagged repository
- **[Terasology](docs/engines/terasology.md)** — 1 engine-tagged repository
- **[UPBGE](docs/engines/upbge.md)** — 1 engine-tagged repository
- **[Acid](docs/engines/acid.md)** — 1 engine-tagged repository
- **[Minecraft](docs/engines/minecraft.md)** — 1 engine-tagged repository
- **[RPG Maker](docs/engines/rpg-maker.md)** — 1 engine-tagged repository
- **[Ren’Py](docs/engines/renpy.md)** — 1 engine-tagged repository
- **[Other engines](docs/engines/other-engines.md)** — 25 engine-tagged repositories
- **[Cross-engine building blocks](docs/shared-building-blocks.md)** — libraries and tools not tied to one engine.

## Browse by game type

These pages surface repositories whose descriptions or topics show a clear fit. They contain reusable tools and systems, not collections of finished games or demos.

- [2D](docs/game-types.md#2d) — 49 tagged repositories
- [3D](docs/game-types.md#3d) — 59 tagged repositories
- [RPG & roguelike](docs/game-types.md#rpg-and-roguelike) — 3 tagged repositories
- [Narrative & visual novel](docs/game-types.md#narrative-and-visual-novel) — 6 tagged repositories
- [Platformer & metroidvania](docs/game-types.md#platformer-and-metroidvania) — 2 tagged repositories
- [Strategy & simulation](docs/game-types.md#strategy-and-simulation) — 2 tagged repositories
- [Puzzle & board games](docs/game-types.md#puzzle-and-board-games) — 2 tagged repositories
- [Multiplayer & online](docs/game-types.md#multiplayer-and-online) — 29 tagged repositories
- [VR & XR](docs/game-types.md#vr-and-xr) — 8 tagged repositories
- [Sandbox & procedural worlds](docs/game-types.md#sandbox-and-procedural-worlds) — 3 tagged repositories

## Build a reusable stack

1. Pick an engine and game type.
2. Choose working parts by layer: project foundation, gameplay, visual assets, story, audio, services, testing, and release.
3. Check upstream compatibility, license terms, maintenance, and platform support before integrating.
4. Keep engine-specific packages separate from cross-engine assets and libraries so the stack stays replaceable.

## Scope and curation

- Include public GitHub repositories with reusable code, tools, engines, frameworks, libraries, content pipelines, or explicit starter templates.
- Require at least 10 GitHub stars at the recorded snapshot.
- Exclude complete games, demo/sample projects, tutorials, resource roundups, and unrelated software.
- Tag repositories by engine, game type, and development layer; a tag is a discovery hint, not a compatibility promise.
- The unique source of truth is [`data/catalog.json`](data/catalog.json); generated browsing pages live under [`docs/`](docs/).

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). Run `python3 scripts/build_catalog.py` after editing the catalog, then `python3 scripts/validate.py`.
