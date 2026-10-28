"""Validate the template's declared structure offline using Python 3.10+."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

REQUIRED = (
    "AGENTS.md", "README.md", "LICENSE", "THIRD-PARTY-NOTICES.md",
    "skills.registry.json", "sources.lock.json", "docs/PROJECT-BRIEF.md",
    "docs/WORKFLOW.md", "docs/CONFLICT-RESOLUTION.md", "docs/SOURCES.md",
    "evals/scenarios.json",
)


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []

    def fail(message: str) -> None:
        errors.append(message)

    def local_file(path: object) -> bool:
        if not isinstance(path, str) or not path:
            return False
        resolved = (root / path).resolve()
        return resolved.is_relative_to(root) and resolved.is_file()

    def read_json(path: str) -> dict:
        try:
            value = json.loads((root / path).read_text(encoding="utf-8"))
            if not isinstance(value, dict):
                raise ValueError("expected object")
            return value
        except (OSError, ValueError) as exc:
            fail(f"{path}: invalid JSON: {exc}")
            return {}

    for path in REQUIRED:
        if not local_file(path):
            fail(f"missing required file: {path}")

    registry = read_json("skills.registry.json")
    lock = read_json("sources.lock.json")
    scenarios = read_json("evals/scenarios.json")
    if registry.get("schema_version") != 1 or lock.get("schema_version") != 1:
        fail("unsupported registry or sources schema_version")
    if registry.get("policy") != "AGENTS.md":
        fail("registry must use the common AGENTS.md policy")

    sources = lock.get("sources", [])
    if not isinstance(sources, list):
        fail("sources must be a list")
        sources = []
    by_id: dict[str, dict] = {}
    for source in sources:
        if not isinstance(source, dict):
            fail("invalid source entry")
            continue
        sid = source.get("id")
        if not isinstance(sid, str) or not re.fullmatch(r"[a-z0-9-]+", sid):
            fail("invalid source id")
            continue
        if sid in by_id:
            fail(f"duplicate source: {sid}")
        by_id[sid] = source
        if not re.fullmatch(r"[0-9a-f]{40}", str(source.get("commit", ""))):
            fail(f"{sid}: source must use an immutable commit")
        if not source.get("license") or not source.get("reviewed_files"):
            fail(f"{sid}: missing license evidence or reviewed files")
        disposition = source.get("disposition")
        if disposition not in ("adapted", "reference_only"):
            fail(f"{sid}: invalid disposition")
        licenses = source.get("license_files")
        if not isinstance(licenses, list):
            fail(f"{sid}: license_files must be a list")
            licenses = []
        if disposition == "adapted" and not licenses:
            fail(f"{sid}: adapted source needs local license notices")
        for path in licenses:
            if not local_file(path):
                fail(f"{sid}: missing license file: {path}")

    entries = registry.get("skills", [])
    if not isinstance(entries, list):
        fail("skills must be a list")
        entries = []
    names: set[str] = set()
    registered: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            fail("invalid skill entry")
            continue
        name, path = entry.get("name"), entry.get("path")
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            fail("invalid skill name")
            continue
        if name in names:
            fail(f"duplicate skill: {name}")
        names.add(name)
        expected_path = f".agents/skills/{name}/SKILL.md"
        if path != expected_path:
            fail(f"{name}: unexpected skill path")
        if not local_file(path):
            fail(f"{name}: missing skill file")
            continue
        registered.add(path)
        text = (root / path).read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not match:
            fail(f"{name}: missing frontmatter")
            continue
        fields: dict[str, str] = {}
        for line in match.group(1).splitlines():
            if not line.strip():
                continue
            key, sep, value = line.partition(":")
            if not sep or key in fields:
                fail(f"{name}: unsupported or duplicate metadata")
                continue
            value = value.strip()
            if value.startswith('"'):
                try:
                    value = json.loads(value)
                except ValueError:
                    fail(f"{name}: invalid quoted metadata")
                    continue
            if not isinstance(value, str) or not value or value in (">", "|", ">-", "|-"):
                fail(f"{name}: metadata must use non-empty scalar text")
                continue
            fields[key] = value
        if fields.get("name") != name or not fields.get("description"):
            fail(f"{name}: invalid name or description")
        if fields.get("license") != entry.get("license") or not fields.get("license"):
            fail(f"{name}: license mismatch")
        source_ids = entry.get("source_ids", [])
        if not isinstance(source_ids, list) or not source_ids:
            fail(f"{name}: missing source_ids")
            continue
        for sid in source_ids:
            source = by_id.get(sid)
            if source is None:
                fail(f"{name}: unknown source: {sid}")
            elif source.get("disposition") != "adapted":
                fail(f"{name}: reference-only source cannot be imported: {sid}")

    discovered = {p.relative_to(root).as_posix() for p in (root / ".agents/skills").glob("*/SKILL.md")}
    for path in sorted(discovered - registered):
        fail(f"unregistered skill: {path}")

    # The template intentionally uses simple inline Markdown links without spaces.
    for path in sorted(root.rglob("*.md")):
        if path.is_symlink() or ".git" in path.relative_to(root).parts:
            continue
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("#") or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():
                fail(f"{path.relative_to(root)}: broken local link: {target}")

    cases = scenarios.get("cases", [])
    if scenarios.get("schema_version") != 1 or not isinstance(cases, list) or not cases:
        fail("evaluation scenarios must contain cases with schema_version 1")
        cases = []
    seen_cases: set[str] = set()
    for case in cases:
        if not isinstance(case, dict):
            fail("invalid scenario")
            continue
        cid = case.get("id")
        if not isinstance(cid, str) or not cid or cid in seen_cases:
            fail("missing or duplicate scenario id")
        else:
            seen_cases.add(cid)
        primary = case.get("primary_skill")
        negative = case.get("not_primary", [])
        if primary not in names:
            fail(f"{cid}: unknown primary skill")
        if not isinstance(negative, list) or any(name not in names for name in negative):
            fail(f"{cid}: unknown not_primary skill")
        elif primary in negative:
            fail(f"{cid}: contradictory scenario routing")
        if not case.get("prompt") or not isinstance(case.get("acceptance"), list) or not case["acceptance"]:
            fail(f"{cid}: missing prompt or acceptance")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: template structure, skill metadata, sources, notices, links and scenarios.")
    print("Agent behavior and native Cloud skill discovery are not verified by this check.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
