#!/usr/bin/env python3
"""Validate the star threshold, taxonomy, and generated catalog pages."""
from collections import Counter
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DATA = ROOT / "data" / "catalog.json"
DOCS = ROOT / "docs"
MIN_LINKS = 301
MIN_STARS = 10
REPO_ENTRY = re.compile(r"^- \[([^\]]+)\]\((https://github\.com/[^)]+)\) — (.+)$")
STAR_FIELD = re.compile(r"⭐\s+(\d+)")
INTERNAL_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+\.md(?:#[^)]+)?)\)")
BANNED_REPOS = {
    "alaingalvan/image-editor-effects", "ChessMax/awesome-game-engines", "JohnClarking/CoolEngines",
    "eug/awesome-opengl", "jslee02/awesome-graphics-libraries", "ConstructCommunity/awesome-construct",
    "devanshutak25/3d-resources", "BharathVishal/Singleton-Implementation-Unity",
    "ChadCSong/Unity3DCarGameSample", "keijiro/LowLevelDigger",
    "opentestdriveunlimited/OpenTestDriveUnlimited", "ATHellboy/SampleProject-FightingGame",
    "Dreaming381/lsss-wip", "Unity-Technologies/Addressables-Sample",
    "edgegap/netcode-game-sample-unity-ngo-3d-spaceshooter", "kevintr303/Unity-Steam-Multiplayer-Sample",
    "Unity-Technologies/com.unity.multiplayer.samples.coop", "Unity-Technologies/com.unity.services.samples.matchplay",
    "NVIDIA/nsight-aftermath-samples", "KhronosGroup/Vulkan-Samples", "mchancan/citylearn",
    "kidscancode/circle_jump", "Nokorpo/gato-godot-accessibility-toolkit",
    "RNIB-MediaAndCulture/Gaming_Devkit", "krs9851/video-game-accessibility",
    "game-ci/documentation", "mackysoft/Unity-GitHubActions-Tutorials",
    "MostlyAdequate/mostly-adequate-guide", "MrRobinOfficial/Guide-UnrealEngine",
    "nanshaws/LibgdxTutorial", "Overv/VulkanTutorial", "ronja-tutorials/ShaderTutorials",
    "steincodes/godot-shader-tutorials", "ZachGoldberg/Startup-CTO-Handbook",
    "0xFA11/MultiplayerNetworkingResources", "makkaX2/DroneFlames-PC-Port", "Blackvoxel/Blackvoxel",
    "eldioss21/gamebeast-api-lens", "pmndrs/react-spring", "projectchrono/chrono",
    "SanderMertens/ecs-faq", "patriciogonzalezvivo/thebookofshaders",
    "Pico-Developer/PlatformSamples-Unity-SpaceArenaParty", "vishwagw/Sky-Sim-drone-simulator-3.0",
    "udinmoInc/WindEffects", "OpenDungeons/OpenDungeons", "lschmid83/Dragon-Island",
    "lettier/3d-game-shaders-for-beginners",
}
DEMO_PHRASES = (
    "sample project", "game sample", "demo project", "demo scene", "tutorial project",
    "example game", "example project", "complete game source", "decompiled source code", "source port of",
    "step-by-step guide",
)
ALLOWED_KINDS = {"engine/framework", "starter-template", "content-tool", "library-or-tool"}


def fail(errors):
    print("Validation failed:")
    for error in errors[:40]:
        print(f"- {error}")
    return 1


def main():
    errors = []
    items = json.loads(DATA.read_text(encoding="utf-8"))
    if len(items) < MIN_LINKS:
        errors.append(f"only {len(items)} canonical repositories; need at least {MIN_LINKS}")
    by_repo = {}
    for item in items:
        repo = item.get("repo", "")
        key = repo.casefold()
        if key in by_repo:
            errors.append(f"duplicate catalog repository: {repo}")
        by_repo[key] = item
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
            errors.append(f"invalid owner/repo identifier: {repo}")
        parsed = urlparse(item.get("url", ""))
        if parsed.netloc.casefold() != "github.com" or parsed.path.strip("/").casefold() != key:
            errors.append(f"non-root or mismatched repository URL: {repo} -> {item.get('url')}")
        if not isinstance(item.get("stars"), int) or item["stars"] < MIN_STARS:
            errors.append(f"below 10-star threshold: {repo} ({item.get('stars')})")
        if item.get("reusable_kind") not in ALLOWED_KINDS:
            errors.append(f"invalid reusable kind: {repo} ({item.get('reusable_kind')})")
        if item.get("workflow") not in {
            "Engines & frameworks", "Project foundations & templates", "Game design & planning",
            "Architecture, ECS & scripting", "Gameplay systems, physics & AI",
            "Rendering, shaders & visual effects", "Art, sprites, animation & 3D",
            "Levels & world building", "Asset pipelines & formats", "Audio & music",
            "UI, input, accessibility & localization", "Networking & multiplayer",
            "Backend, persistence & live operations", "Testing & QA", "Debugging & profiling",
            "Build, CI & release", "Publishing & monetization",
        }:
            errors.append(f"unknown workflow: {repo} ({item.get('workflow')})")
        if not item.get("engines") or not item.get("game_types") or not item.get("description"):
            errors.append(f"missing discovery metadata: {repo}")
        for field in ("engines", "game_types"):
            tags = item.get(field)
            if not isinstance(tags, list) or not all(isinstance(tag, str) for tag in tags):
                errors.append(f"invalid {field} tag list: {repo}")
            elif len(tags) != len(set(tags)):
                errors.append(f"duplicate {field} tags: {repo} ({tags})")
        if key in {x.casefold() for x in BANNED_REPOS}:
            errors.append(f"excluded game/demo/tutorial/meta repository is present: {repo}")
        combined = (repo + " " + item.get("description", "")).casefold()
        if item.get("reusable_kind") not in {"engine/framework", "starter-template"} and any(p in combined for p in DEMO_PHRASES):
            errors.append(f"demo/sample project language needs review: {repo}")

    files = [README] + sorted(DOCS.rglob("*.md"))
    referenced = set()
    entry_counts = Counter()
    for path in files:
        text = path.read_text(encoding="utf-8")
        for number, line in enumerate(text.splitlines(), 1):
            if line.startswith("- [") and "https://github.com/" in line:
                match = REPO_ENTRY.match(line)
                if not match:
                    errors.append(f"{path.relative_to(ROOT)}:{number}: malformed repository entry")
                    continue
                repo, url, body = match.groups()
                key = repo.casefold()
                item = by_repo.get(key)
                if item is None:
                    errors.append(f"{path.relative_to(ROOT)}:{number}: uncurated repository link {repo}")
                    continue
                if url.rstrip("/").casefold() != item["url"].rstrip("/").casefold():
                    errors.append(f"{path.relative_to(ROOT)}:{number}: URL differs from catalog for {repo}")
                star = STAR_FIELD.search(body)
                if not star or int(star.group(1)) != item["stars"]:
                    errors.append(f"{path.relative_to(ROOT)}:{number}: missing or stale star count for {repo}")
                referenced.add(key)
                entry_counts[path.relative_to(ROOT).as_posix()] += 1
        for target in INTERNAL_LINK.findall(text):
            target_path = target.split("#", 1)[0]
            local = (path.parent / target_path).resolve()
            if not local.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link {target}")
    missing = set(by_repo) - referenced
    if missing:
        errors.append(f"{len(missing)} catalog entries are not shown in generated pages: {sorted(missing)[:10]}")
    readme_text = README.read_text(encoding="utf-8")
    count_match = re.search(r"\*\*(\d+) unique repositories", readme_text)
    if not count_match or int(count_match.group(1)) != len(items):
        errors.append("README unique-repository total does not match data/catalog.json")
    expected_engines = Counter(engine for item in items for engine in set(item["engines"]) if engine != "Cross-engine")
    root_engine_counts = {
        name: int(count) for name, count in re.findall(
            r"^- \*\*\[([^\]]+)\]\([^)]+\)\*\* — (\d+) engine-tagged (?:repository|repositories)$",
            readme_text, re.M,
        )
    }
    if root_engine_counts != dict(expected_engines):
        errors.append("README engine counts do not match unique catalog tags")
    engine_index = (DOCS / "engines" / "README.md").read_text(encoding="utf-8")
    index_engine_counts = {
        name: int(count) for name, count in re.findall(
            r"^- \[([^\]]+)\]\([^)]+\) — (\d+) tagged (?:repository|repositories)$",
            engine_index, re.M,
        )
    }
    if index_engine_counts != dict(expected_engines):
        errors.append("engine index counts do not match unique catalog tags")
    if errors:
        return fail(errors)
    print(f"Validated {len(items)} unique repositories; all have >= {MIN_STARS} stars.")
    print(f"Checked {len(files)} Markdown files and {len(referenced)} visible unique repositories.")
    print("Generated pages:")
    for name, count in sorted(entry_counts.items()):
        print(f"  {count:>4} repository entries across {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
