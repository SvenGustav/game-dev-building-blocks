#!/usr/bin/env python3
"""Validate the repository-link catalog in README.md."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
MIN_LINKS = 301
CATEGORIES = [
    "Planning and game design",
    "Engines and frameworks",
    "Starter projects, samples, and complete games",
    "Architecture, ECS, and scripting",
    "Gameplay systems, physics, and AI",
    "Rendering, graphics, and shaders",
    "Art, animation, and 3D creation",
    "Levels, maps, and world building",
    "Asset pipelines and file formats",
    "Audio and music",
    "UI, input, accessibility, and localization",
    "Networking and multiplayer",
    "Persistence, backend, and live operations",
    "Testing, QA, and playtesting",
    "Debugging, profiling, and observability",
    "Build, CI, packaging, and release",
    "Publishing, distribution, and monetization",
    "Learning and reference implementations",
]
ENTRY = re.compile(r"^- \[([^\]]+)\]\((https://github\.com/[^)]+)\)(?: — .+)?$")
REPO = re.compile(r"^https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/?$")


def main() -> int:
    text = README.read_text(encoding="utf-8")
    current = None
    seen = set()
    counts = {category: 0 for category in CATEGORIES}
    errors = []
    for number, line in enumerate(text.splitlines(), 1):
        if line.startswith("## "):
            heading = line[3:].strip()
            current = heading if heading in counts else None
            continue
        if not line.startswith("- ["):
            continue
        match = ENTRY.match(line)
        if not match:
            if current:
                errors.append(f"line {number}: malformed entry in {current}")
            continue
        name, url = match.groups()
        if current is None:
            errors.append(f"line {number}: repository entry outside a catalog category")
            continue
        if not REPO.match(url):
            errors.append(f"line {number}: link is not a repository root URL: {url}")
        normalized = url.rstrip("/").lower()
        if normalized in seen:
            errors.append(f"line {number}: duplicate repository: {url}")
        seen.add(normalized)
        counts[current] += 1
    if len(seen) < MIN_LINKS:
        errors.append(f"only {len(seen)} unique repository links; need at least {MIN_LINKS}")
    empty = [category for category, count in counts.items() if not count]
    if empty:
        errors.append("empty categories: " + ", ".join(empty))
    if errors:
        print("Validation failed:")
        print("\n".join(f"- {error}" for error in errors[:40]))
        return 1
    print(f"Validated {len(seen)} unique GitHub repository links across {len(counts)} categories.")
    for category, count in counts.items():
        print(f"{count:>3}  {category}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
