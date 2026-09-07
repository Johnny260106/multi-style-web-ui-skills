#!/usr/bin/env python3
"""Dependency-free structural validation for the UI skill pack."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
ROUTER = "web-ui-design-router"
LEAVES = (
    "tech-blue-b2b-ui",
    "industrial-orange-b2b-ui",
    "green-operations-b2b-ui",
    "dark-cockpit-ui",
    "patient-medical-web-ui",
    "health-management-web-ui",
)
EXPECTED = (ROUTER, *LEAVES)
LEAF_REFERENCES = (
    "tokens.md",
    "patterns.md",
    "states-and-antipatterns.md",
    "visual-research.md",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_frontmatter(path: Path, expected_name: str) -> None:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"{path.relative_to(ROOT)} has no YAML frontmatter")
    header = match.group(1)
    if not re.search(rf"^name:\s*{re.escape(expected_name)}\s*$", header, re.MULTILINE):
        fail(f"{path.relative_to(ROOT)} has the wrong name")
    description = re.search(r"^description:\s*(.+)$", header, re.MULTILINE)
    if not description or len(description.group(1).strip()) < 40:
        fail(f"{path.relative_to(ROOT)} needs a discriminating description")
    if "TODO" in text:
        fail(f"{path.relative_to(ROOT)} contains TODO text")


actual = sorted(path.name for path in ROOT.iterdir() if path.is_dir() and (path / "SKILL.md").exists())
if actual != sorted(EXPECTED):
    fail(f"expected {len(EXPECTED)} skills, found: {', '.join(actual)}")

routing = (ROOT / ROUTER / "references" / "routing.md").read_text(encoding="utf-8")
tests = (ROOT / ROUTER / "references" / "trigger-tests.md").read_text(encoding="utf-8")

for name in EXPECTED:
    folder = ROOT / name
    validate_frontmatter(folder / "SKILL.md", name)
    metadata = folder / "agents" / "openai.yaml"
    if not metadata.exists() or f"${name}" not in metadata.read_text(encoding="utf-8"):
        fail(f"{name} has missing or inconsistent agents/openai.yaml")

for name in LEAVES:
    folder = ROOT / name
    for reference in LEAF_REFERENCES:
        if not (folder / "references" / reference).exists():
            fail(f"{name} is missing references/{reference}")
    if name not in routing:
        fail(f"router mapping is missing {name}")
    if tests.count(name) < 2:
        fail(f"trigger tests do not cover {name} twice")

print("Validated 7 skills, 6 routes, metadata, references, and trigger coverage.")
