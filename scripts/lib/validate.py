#!/usr/bin/env python3
"""Validate generated Ping Identity Agent Skills."""

from __future__ import annotations

import argparse
from datetime import date, datetime
import math
from pathlib import Path
import random
import re
import subprocess

from ping_docsets import load_docsets, parse_llms_file


ALLOWED_FRONTMATTER = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}
NAME_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$")
SNAPSHOT_RE = re.compile(r"references/snapshots/[A-Za-z0-9._-]+\.md")
MANIFEST_DATE_RE = re.compile(r"^- Sync date: (\d{4}-\d{2}-\d{2})$", re.MULTILINE)


class Reporter:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("unterminated YAML frontmatter")
    frontmatter: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.startswith(" "):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        frontmatter[key.strip()] = value
    return frontmatter, text[end + 4 :]


def validate_frontmatter(skill_dir: Path, reporter: Reporter) -> None:
    skill_path = skill_dir / "SKILL.md"
    try:
        frontmatter, _body = parse_frontmatter(skill_path)
    except ValueError as error:
        reporter.error(f"{skill_path}: {error}")
        return

    for required in ("name", "description"):
        if not frontmatter.get(required):
            reporter.error(f"{skill_path}: missing required frontmatter field {required}")
    unknown = sorted(set(frontmatter) - ALLOWED_FRONTMATTER)
    if unknown:
        reporter.error(f"{skill_path}: unsupported frontmatter fields: {', '.join(unknown)}")

    name = frontmatter.get("name", "")
    if name != skill_dir.name:
        reporter.error(f"{skill_path}: name must match parent directory")
    if not NAME_RE.match(name) or "--" in name:
        reporter.error(f"{skill_path}: invalid agentskills name {name!r}")

    description = frontmatter.get("description", "")
    if len(description) > 1024:
        reporter.error(f"{skill_path}: description exceeds 1024 characters")


def curl_ok(url: str) -> bool:
    result = subprocess.run(
        [
            "curl",
            "-fsSL",
            "--retry",
            "1",
            "-o",
            "/dev/null",
            url,
        ],
        check=False,
        text=True,
        capture_output=True,
    )
    return result.returncode == 0


def validate_references(
    skill_dir: Path,
    reporter: Reporter,
    sample_percent: float,
    sample_max: int,
    check_urls: bool,
) -> None:
    references = skill_dir / "references"
    llms_path = references / "llms.txt"
    manifest_path = references / "MANIFEST.md"

    if not llms_path.exists():
        reporter.error(f"{skill_dir}: missing references/llms.txt")
        return
    entries = parse_llms_file(llms_path)
    if not entries:
        reporter.error(f"{llms_path}: no markdown URLs parsed")

    if not manifest_path.exists():
        reporter.error(f"{skill_dir}: missing references/MANIFEST.md")
    else:
        manifest = manifest_path.read_text(encoding="utf-8")
        match = MANIFEST_DATE_RE.search(manifest)
        if not match:
            reporter.error(f"{manifest_path}: missing sync date")
        else:
            sync_date = datetime.strptime(match.group(1), "%Y-%m-%d").date()
            age_days = (date.today() - sync_date).days
            if age_days >= 90:
                reporter.error(f"{manifest_path}: manifest is {age_days} days old")
            elif age_days >= 60:
                reporter.warn(f"{manifest_path}: manifest is {age_days} days old")

    skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    for snapshot_ref in sorted(set(SNAPSHOT_RE.findall(skill_text))):
        if not (skill_dir / snapshot_ref).exists():
            reporter.error(f"{skill_dir / 'SKILL.md'}: missing {snapshot_ref}")

    for snapshot_path in sorted((references / "snapshots").glob("*.md")):
        if snapshot_path.stat().st_size == 0:
            reporter.error(f"{snapshot_path}: empty snapshot")

    if check_urls and entries:
        sample_size = max(1, math.ceil(len(entries) * sample_percent / 100.0))
        sample_size = min(sample_size, sample_max, len(entries))
        urls = sorted(entry.url for entry in entries)
        random.Random(skill_dir.name).shuffle(urls)
        for url in urls[:sample_size]:
            if not curl_ok(url):
                reporter.error(f"{llms_path}: sampled URL failed: {url}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--registry", default="scripts/docsets.yaml")
    parser.add_argument(
        "--skills-root", default="plugins/ping-identity-docs/skills"
    )
    parser.add_argument("--require-all-enabled", action="store_true")
    parser.add_argument("--skip-url-check", action="store_true")
    parser.add_argument("--url-sample-percent", type=float, default=5.0)
    parser.add_argument("--url-sample-max", type=int, default=25)
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    skills_root = repo_root / args.skills_root
    reporter = Reporter()

    if not skills_root.exists():
        reporter.error(f"{skills_root}: skills root does not exist")
        skill_dirs: list[Path] = []
    else:
        skill_dirs = sorted(path for path in skills_root.iterdir() if path.is_dir())

    if args.require_all_enabled:
        enabled = {
            docset.skill_slug
            for docset in load_docsets(repo_root / args.registry)
            if docset.enabled
        }
        present = {path.name for path in skill_dirs}
        missing = sorted(enabled - present)
        if missing:
            reporter.error("missing enabled skill directories: " + ", ".join(missing))

    for skill_dir in skill_dirs:
        if not (skill_dir / "SKILL.md").exists():
            reporter.error(f"{skill_dir}: missing SKILL.md")
            continue
        validate_frontmatter(skill_dir, reporter)
        validate_references(
            skill_dir,
            reporter,
            sample_percent=args.url_sample_percent,
            sample_max=args.url_sample_max,
            check_urls=not args.skip_url_check,
        )

    for warning in reporter.warnings:
        print(f"WARN: {warning}")
    for error in reporter.errors:
        print(f"ERROR: {error}")

    print(
        f"Validated {len(skill_dirs)} skill directories: "
        f"{len(reporter.errors)} errors, {len(reporter.warnings)} warnings"
    )
    return 1 if reporter.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
