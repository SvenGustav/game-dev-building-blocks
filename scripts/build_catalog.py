#!/usr/bin/env python3
"""Build engine- and game-type-first catalog pages from data/catalog.json."""
from collections import Counter, defaultdict
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "catalog.json"
DOCS = ROOT / "docs"
MIN_STARS = 10
MIN_REPOSITORIES = 301

WORKFLOWS = [
    "Engines & frameworks",
    "Project foundations & templates",
    "Game design & planning",
    "Architecture, ECS & scripting",
    "Gameplay systems, physics & AI",
    "Rendering, shaders & visual effects",
    "Art, sprites, animation & 3D",
    "Levels & world building",
    "Asset pipelines & formats",
    "Audio & music",
    "UI, input, accessibility & localization",
    "Networking & multiplayer",
    "Backend, persistence & live operations",
    "Testing & QA",
    "Debugging & profiling",
    "Build, CI & release",
    "Publishing & monetization",
]
ENGINE_ORDER = [
    "Godot", "Unity", "Unreal Engine", "Bevy", "libGDX", "Stride", "GameMaker", "GDevelop", "Glide", "Construct 2",
    "Defold", "Phaser", "Cocos", "LÖVE", "Flame", "MonoGame", "HaxeFlixel", "Panda3D",
    "Three.js", "Babylon.js", "melonJS", "Wicked Engine", "PixiJS", "Raylib", "SDL/SFML", "OpenRA", "Quake/id Tech", "X-Ray",
    "Luanti", "Terasology", "UPBGE", "Acid", "Minecraft", "RPG Maker", "Ren’Py", "Other engines",
]
ENGINE_SLUGS = {
    "Godot": "godot", "Unity": "unity", "Unreal Engine": "unreal-engine",
    "Bevy": "bevy", "libGDX": "libgdx", "Stride": "stride", "GameMaker": "gamemaker", "GDevelop": "gdevelop", "Glide": "glide", "Construct 2": "construct-2",
    "Defold": "defold", "Phaser": "phaser", "Cocos": "cocos",
    "LÖVE": "love2d", "Flame": "flame", "MonoGame": "monogame", "HaxeFlixel": "haxeflixel",
    "Panda3D": "panda3d", "Three.js": "threejs", "Babylon.js": "babylonjs", "melonJS": "melonjs", "Wicked Engine": "wicked-engine", "PixiJS": "pixijs",
    "Raylib": "raylib", "SDL/SFML": "sdl-sfml", "OpenRA": "openra",
    "Quake/id Tech": "quake-idtech", "X-Ray": "x-ray", "Luanti": "luanti", "Terasology": "terasology", "UPBGE": "upbge", "Acid": "acid",
    "Minecraft": "minecraft",
    "RPG Maker": "rpg-maker", "Ren’Py": "renpy", "Other engines": "other-engines",
}
GAME_TYPES = [
    "2D", "3D", "RPG & roguelike", "Narrative & visual novel",
    "Platformer & metroidvania", "Strategy & simulation", "Puzzle & board games",
    "Multiplayer & online", "Racing & sports", "Action & shooter", "VR & XR",
    "Sandbox & procedural worlds",
]
PRIMARY_ENGINES = {"Godot", "Unity", "Unreal Engine", "Bevy"}
SHARED_WORKFLOWS = {
    "Game design & planning", "Rendering, shaders & visual effects",
    "Art, sprites, animation & 3D", "Levels & world building",
    "Asset pipelines & formats", "Audio & music",
}


def slug(text):
    text = text.casefold().replace("&", "and").replace("’", "")
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def entry_sort(item):
    return (-item["stars"], item["repo"].casefold())


def render_entry(item, show_genres=True):
    tags = []
    engines = [e for e in item["engines"] if e != "Cross-engine"]
    if engines:
        tags.append("engine: " + ", ".join(engines))
    elif "Cross-engine" in item["engines"]:
        tags.append("cross-engine")
    if show_genres and item["game_types"] != ["Cross-genre"]:
        tags.append("type: " + ", ".join(item["game_types"]))
    if item.get("language"):
        tags.append(item["language"])
    tags.append("license: " + (item.get("license") or "not detected"))
    tags.append(f"⭐ {item['stars']}")
    if item.get("archived"):
        tags.append("ARCHIVED")
    desc = item["description"].replace("\n", " ").strip()
    return f"- [{item['repo']}]({item['url']}) — {desc} · " + " · ".join(tags)


def group_by_workflow(items):
    groups = defaultdict(list)
    for item in items:
        groups[item["workflow"]].append(item)
    return groups


def render_groups(items, show_genres=True):
    groups = group_by_workflow(items)
    out = []
    for workflow in WORKFLOWS:
        values = sorted(groups.get(workflow, []), key=entry_sort)
        if not values:
            continue
        out.extend([f"### {workflow}", ""])
        out.extend(render_entry(x, show_genres=show_genres) for x in values)
        out.append("")
    return out


def load_catalog():
    items = json.loads(DATA.read_text(encoding="utf-8"))
    if len(items) < MIN_REPOSITORIES:
        raise SystemExit(f"Catalog has {len(items)} repos; need at least {MIN_REPOSITORIES}.")
    seen = set()
    for item in items:
        key = item["repo"].casefold()
        if key in seen:
            raise SystemExit(f"Duplicate canonical repository: {item['repo']}")
        seen.add(key)
        if item["stars"] < MIN_STARS:
            raise SystemExit(f"Below-threshold repository: {item['repo']} ({item['stars']} stars)")
        if item["workflow"] not in WORKFLOWS:
            raise SystemExit(f"Unknown workflow for {item['repo']}: {item['workflow']}")
        if item.get("reusable_kind") not in {"engine/framework", "starter-template", "content-tool", "library-or-tool"}:
            raise SystemExit(f"Invalid reusable kind for {item['repo']}: {item.get('reusable_kind')}")
        if not item["engines"] or not item["game_types"]:
            raise SystemExit(f"Missing engine/type tags: {item['repo']}")
    return items


def build_engine_page(engine, items):
    slug_name = ENGINE_SLUGS[engine]
    path = DOCS / "engines" / f"{slug_name}.md"
    direct = [x for x in items if engine in x["engines"]]
    shared = [x for x in items if "Cross-engine" in x["engines"]]
    if engine in PRIMARY_ENGINES:
        selected = {x["repo"].casefold(): x for x in direct}
        for item in shared:
            selected[item["repo"].casefold()] = item
        intro = "This is a full stack view: engine-specific repositories plus shared tools that can provide reusable assets, systems, or formats. Shared does not mean drop-in compatible; check integration and versions."
    else:
        selected = {x["repo"].casefold(): x for x in direct}
        for item in shared:
            if item["workflow"] in SHARED_WORKFLOWS:
                selected[item["repo"].casefold()] = item
        intro = "Engine-specific repositories are grouped with shared design, art, level, asset, shader, and audio tools. Shared tools may need an adapter or import step."
    selected_items = list(selected.values())
    out = [
        f"# {engine} Game Development Stack", "",
        f"{intro} The catalog includes repositories with at least {MIN_STARS} GitHub stars.", "",
        "**Browse:** [all engines](README.md) · [game types](../game-types.md) · [shared building blocks](../shared-building-blocks.md)", "",
        "Use the sections below to assemble a stack by function. Star counts are snapshots, not quality or maintenance guarantees. Check upstream engine versions, licenses, and project status before adopting anything.", "",
    ]
    if direct:
        out.extend([f"**{engine}-tagged repositories:** {len(direct)}", ""])
    if engine not in PRIMARY_ENGINES:
        out.extend(["[Browse every cross-engine tool by workflow →](../shared-building-blocks.md)", ""])
    out.extend(render_groups(selected_items))
    if not selected_items:
        out.append("No repositories currently match this engine tag.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    return len(selected_items)


def build_shared_page(items):
    shared = [x for x in items if "Cross-engine" in x["engines"]]
    out = [
        "# Cross-engine Building Blocks", "",
        "Repositories here are not tied to one engine in this catalog. Some are libraries or toolchains that still need integration work; confirm formats, APIs, and platform support before reuse.", "",
        "Each item has at least 10 GitHub stars. Star counts are snapshots, not proof of quality, security, compatibility, or maintenance.", "",
        f"**Unique cross-engine repositories:** {len(shared)} · [engine stacks](engines/README.md) · [game types](game-types.md)", "",
    ]
    out.extend(render_groups(shared))
    (DOCS / "shared-building-blocks.md").parent.mkdir(parents=True, exist_ok=True)
    (DOCS / "shared-building-blocks.md").write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


def build_game_types(items):
    out = [
        "# Game-Type Index", "",
        "Use these facets to find building blocks for a genre or format. Entries are tagged only when the repository description or topics signal a clear fit; tags are discovery hints, not compatibility guarantees. No complete game or demo-project collection is listed.", "",
        "[Engine stacks →](engines/README.md) · [shared building blocks →](shared-building-blocks.md)", "",
    ]
    for game_type in GAME_TYPES:
        selected = [x for x in items if game_type in x["game_types"]]
        if not selected:
            continue
        out.extend([f"<a id=\"{slug(game_type)}\"></a>", f"## {game_type}", "", f"{len(selected)} repositories tagged for this game type.", ""])
        out.extend(render_groups(selected))
    general = [x for x in items if x["game_types"] == ["Cross-genre"]]
    out.extend(["## Cross-genre foundations", "", "General-purpose engines, systems, and tools are grouped in the [engine stacks](engines/README.md) and [shared building blocks](shared-building-blocks.md).", ""])
    out.extend(render_groups(general))
    (DOCS / "game-types.md").parent.mkdir(parents=True, exist_ok=True)
    (DOCS / "game-types.md").write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


def build_engine_index(items):
    counts = Counter(engine for item in items for engine in set(item["engines"]) if engine != "Cross-engine")
    out = [
        "# Engine Stacks", "",
        "Choose an engine, then browse the same stack categories: project foundations, gameplay, visuals and assets, story, audio, services, QA, and release.", "",
        "Core engine pages also include shared tools so that art, sprites, animation, shaders, and assets are close to engine-specific code. Secondary engine pages link to the complete shared-tool catalog.", "",
    ]
    for engine in ENGINE_ORDER:
        if not counts[engine]:
            continue
        name = f"[{engine}]({ENGINE_SLUGS[engine]}.md)"
        count_label = "repository" if counts[engine] == 1 else "repositories"
        out.append(f"- {name} — {counts[engine]} tagged {count_label}")
    out.extend(["", "[Cross-engine building blocks →](../shared-building-blocks.md)", "", "All repositories in this catalog have at least 10 GitHub stars at the recorded snapshot."])
    (DOCS / "engines" / "README.md").parent.mkdir(parents=True, exist_ok=True)
    (DOCS / "engines" / "README.md").write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


def build_root_readme(items):
    counts = Counter(engine for item in items for engine in set(item["engines"]) if engine != "Cross-engine")
    types = Counter(game_type for item in items for game_type in set(item["game_types"]) if game_type != "Cross-genre")
    out = [
        "# Game Dev Building Blocks [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome#readme)", "",
        "A curated, engine-first index of reusable game-development foundations: engines, frameworks, gameplay systems, shaders, art and asset tools, story systems, networking, testing, and release tooling. It helps developers and coding agents assemble working parts instead of starting from an empty project.", "",
        f"**{len(items)} unique repositories · minimum 10 GitHub stars · no complete-game or demo-project listings**", "",
        "Star counts are point-in-time GitHub metadata. They are a discovery threshold, not a quality, security, maintenance, or compatibility guarantee. Check each repository's current status, license, supported versions, and integration requirements.", "",
        "## Choose an engine stack", "",
        "Each engine page groups the same development layers. Godot, Unity, Unreal, and Bevy pages include shared tools for art, sprites, animation, shaders, levels, and assets alongside engine-specific projects.", "",
    ]
    for engine in ENGINE_ORDER:
        if counts[engine]:
            count_label = "repository" if counts[engine] == 1 else "repositories"
            out.append(f"- **[{engine}](docs/engines/{ENGINE_SLUGS[engine]}.md)** — {counts[engine]} engine-tagged {count_label}")
    out.extend([
        "- **[Cross-engine building blocks](docs/shared-building-blocks.md)** — libraries and tools not tied to one engine.", "",
        "## Browse by game type", "",
        "These pages surface repositories whose descriptions or topics show a clear fit. They contain reusable tools and systems, not collections of finished games or demos.", "",
    ])
    for game_type in GAME_TYPES:
        count = types[game_type]
        if count:
            out.append(f"- [{game_type}](docs/game-types.md#{slug(game_type)}) — {count} tagged repositories")
    out.extend([
        "", "## Build a reusable stack", "",
        "1. Pick an engine and game type.",
        "2. Choose working parts by layer: project foundation, gameplay, visual assets, story, audio, services, testing, and release.",
        "3. Check upstream compatibility, license terms, maintenance, and platform support before integrating.",
        "4. Keep engine-specific packages separate from cross-engine assets and libraries so the stack stays replaceable.", "",
        "## Scope and curation", "",
        "- Include public GitHub repositories with reusable code, tools, engines, frameworks, libraries, content pipelines, or explicit starter templates.",
        "- Require at least 10 GitHub stars at the recorded snapshot.",
        "- Exclude complete games, demo/sample projects, tutorials, resource roundups, and unrelated software.",
        "- Tag repositories by engine, game type, and development layer; a tag is a discovery hint, not a compatibility promise.",
        "- The unique source of truth is [`data/catalog.json`](data/catalog.json); generated browsing pages live under [`docs/`](docs/).", "",
        "## Contribute", "",
        "See [CONTRIBUTING.md](CONTRIBUTING.md). Run `python3 scripts/build_catalog.py` after editing the catalog, then `python3 scripts/validate.py`.",
    ])
    (ROOT / "README.md").write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


def main():
    items = load_catalog()
    build_root_readme(items)
    build_engine_index(items)
    build_shared_page(items)
    build_game_types(items)
    engine_dir = DOCS / "engines"
    active_slugs = {
        ENGINE_SLUGS[engine] for engine in ENGINE_ORDER
        if any(engine in item["engines"] for item in items)
    }
    for stale_page in engine_dir.glob("*.md"):
        if stale_page.name != "README.md" and stale_page.stem not in active_slugs:
            stale_page.unlink()
    page_counts = {}
    for engine in ENGINE_ORDER:
        if any(engine in item["engines"] for item in items):
            page_counts[engine] = build_engine_page(engine, items)
    print(json.dumps({
        "unique_repositories": len(items),
        "minimum_stars": min(x["stars"] for x in items),
        "engine_pages": page_counts,
        "game_type_counts": {t: sum(t in x["game_types"] for x in items) for t in GAME_TYPES},
        "shared_repositories": sum("Cross-engine" in x["engines"] for x in items),
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
