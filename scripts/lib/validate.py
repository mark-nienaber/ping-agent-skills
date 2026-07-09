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

from ping_docsets import (
    Docset,
    cluster_entries,
    detect_latest_version,
    load_docsets,
    parse_llms_file,
    routing_url_pattern,
)


USER_AGENT = "ping-agent-skills-validate/1.0 (+https://github.com/mark-nienaber/ping-agent-skills)"
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
ROUTING_TABLE_HEADER = "| Task category | Guide slug | Live URL pattern | Snapshot |"


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
    if len(name) > 64:
        reporter.error(f"{skill_path}: name exceeds 64 characters")
    if not NAME_RE.match(name) or "--" in name:
        reporter.error(f"{skill_path}: invalid agentskills name {name!r}")

    description = frontmatter.get("description", "")
    if not description.startswith("Use when"):
        reporter.error(f"{skill_path}: description must start with 'Use when'")
    if len(description) > 500:
        reporter.error(f"{skill_path}: description exceeds 500 characters")


def curl_ok(url: str) -> bool:
    result = subprocess.run(
        [
            "curl",
            "-fsSL",
            "--retry",
            "2",
            "--retry-delay",
            "1",
            "-A",
            USER_AGENT,
            "-o",
            "/dev/null",
            url,
        ],
        check=False,
        text=True,
        capture_output=True,
    )
    return result.returncode == 0


def parse_routing_rows(skill_text: str) -> list[tuple[str, str, str, str]]:
    rows: list[tuple[str, str, str, str]] = []
    in_table = False
    for line in skill_text.splitlines():
        stripped = line.strip()
        if stripped == ROUTING_TABLE_HEADER:
            in_table = True
            continue
        if not in_table:
            continue
        if stripped.startswith("|---"):
            continue
        if not stripped.startswith("|"):
            if rows:
                break
            continue
        columns = [column.strip() for column in stripped.strip("|").split("|")]
        if len(columns) < 4:
            continue
        rows.append((columns[0], columns[1], columns[2], columns[3]))
    return rows


def validate_routing_table(
    skill_dir: Path,
    docset: Docset | None,
    entries: list,
    skill_text: str,
    reporter: Reporter,
) -> None:
    rows = parse_routing_rows(skill_text)
    skill_path = skill_dir / "SKILL.md"
    if not rows:
        reporter.error(f"{skill_path}: missing task routing rows")
        return
    if docset is None:
        reporter.warn(f"{skill_path}: no registry entry available for routing validation")
        return

    selected_version = detect_latest_version(
        entries, docset.base_url, preferred_version=docset.preferred_version
    )
    clusters = cluster_entries(entries, docset.base_url, selected_version)
    if len(rows) > len(clusters):
        reporter.error(
            f"{skill_path}: routing table has {len(rows)} rows but only "
            f"{len(clusters)} llms.txt-derived clusters"
        )
        return

    for index, ((_category, guide, pattern, snapshot), cluster) in enumerate(
        zip(rows, clusters), start=1
    ):
        expected_pattern = routing_url_pattern(docset.base_url, cluster)
        expected_snapshot = f"references/snapshots/{cluster.guide_slug}.md"
        if not (skill_dir / expected_snapshot).exists():
            expected_snapshot = "live-only"
        if guide != cluster.guide:
            reporter.error(
                f"{skill_path}: routing row {index} guide is {guide!r}, "
                f"expected {cluster.guide!r}"
            )
        if pattern != expected_pattern:
            reporter.error(
                f"{skill_path}: routing row {index} pattern is {pattern!r}, "
                f"expected {expected_pattern!r}"
            )
        if snapshot != expected_snapshot:
            reporter.error(
                f"{skill_path}: routing row {index} snapshot is {snapshot!r}, "
                f"expected {expected_snapshot!r}"
            )


def validate_references(
    skill_dir: Path,
    docset: Docset | None,
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
    validate_routing_table(skill_dir, docset, entries, skill_text, reporter)
    for snapshot_ref in sorted(set(SNAPSHOT_RE.findall(skill_text))):
        if not (skill_dir / snapshot_ref).exists():
            reporter.error(f"{skill_dir / 'SKILL.md'}: missing {snapshot_ref}")

    for snapshot_path in sorted((references / "snapshots").glob("*.md")):
        if snapshot_path.stat().st_size == 0:
            reporter.error(f"{snapshot_path}: empty snapshot")

    if check_urls and entries:
        if docset is not None:
            llms_url = f"{docset.base_url}/llms.txt"
            if not curl_ok(llms_url):
                reporter.error(f"{llms_path}: live llms.txt failed: {llms_url}")
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

    docsets = load_docsets(repo_root / args.registry)
    docsets_by_slug = {docset.skill_slug: docset for docset in docsets}
    if args.require_all_enabled:
        enabled = {
            docset.skill_slug
            for docset in docsets
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
            docsets_by_slug.get(skill_dir.name),
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
