#!/usr/bin/env python3
"""Sync one Ping Identity docset into an Agent Skill references directory."""

from __future__ import annotations

import argparse
import os
import subprocess
import tempfile
import time
from pathlib import Path

from manifest import write_manifest
from ping_docsets import (
    cluster_entries,
    detect_latest_version,
    die,
    find_docset,
    load_docsets,
    parse_llms_file,
)


USER_AGENT = "ping-agent-skills-sync/1.0 (+https://github.com/mark-nienaber/ping-agent-skills)"


def curl_fetch(url: str, destination: Path) -> bool:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(delete=False, dir=str(destination.parent)) as tmp:
        tmp_path = Path(tmp.name)
    try:
        command = [
            "curl",
            "-fsSL",
            "--retry",
            "2",
            "--retry-delay",
            "1",
            "-A",
            USER_AGENT,
            "-o",
            str(tmp_path),
            url,
        ]
        result = subprocess.run(command, check=False, text=True, capture_output=True)
        if result.returncode != 0:
            tmp_path.unlink(missing_ok=True)
            return False
        tmp_path.replace(destination)
        return True
    finally:
        tmp_path.unlink(missing_ok=True)


def markdownish(path: Path) -> bool:
    prefix = path.read_text(encoding="utf-8", errors="ignore")[:512].lstrip().lower()
    return not (prefix.startswith("<!doctype html") or prefix.startswith("<html"))


def sync_docset(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    registry_path = repo_root / args.registry
    skills_root = repo_root / args.skills_root
    docset = find_docset(load_docsets(registry_path), args.slug)

    skill_root = skills_root / docset.skill_slug
    references_root = skill_root / "references"
    snapshots_root = references_root / "snapshots"
    references_root.mkdir(parents=True, exist_ok=True)
    snapshots_root.mkdir(parents=True, exist_ok=True)

    llms_url = f"{docset.base_url}/llms.txt"
    llms_path = references_root / "llms.txt"
    print(f"[{docset.skill_slug}] fetching {llms_url}")
    if not curl_fetch(llms_url, llms_path):
        die(f"[{docset.skill_slug}] failed to fetch {llms_url}")

    entries = parse_llms_file(llms_path)
    if not entries:
        die(f"[{docset.skill_slug}] no markdown entries parsed from {llms_path}")

    selected_version = detect_latest_version(
        entries, docset.base_url, preferred_version=docset.preferred_version
    )
    clusters = cluster_entries(entries, docset.base_url, selected_version)
    if not clusters:
        die(f"[{docset.skill_slug}] no guide clusters found for version {selected_version or 'current'}")

    for old_snapshot in snapshots_root.glob("*.md"):
        old_snapshot.unlink()

    snapshots: list[dict[str, str]] = []
    delay = float(os.environ.get("PING_DOCS_SYNC_DELAY", "0.05"))
    for cluster in clusters:
        snapshot_file = f"{cluster.guide_slug}.md"
        snapshot_path = snapshots_root / snapshot_file
        source_type = "single-page"
        source_url = cluster.single_page_url
        if not curl_fetch(cluster.single_page_url, snapshot_path):
            if not args.page_fallback:
                print(f"[{docset.skill_slug}] skipped {cluster.guide}: no single-page.md")
                continue
            source_type = "page"
            source_url = cluster.first_page_url
            if not curl_fetch(cluster.first_page_url, snapshot_path):
                print(f"[{docset.skill_slug}] skipped {cluster.guide}: snapshot fetch failed")
                continue
            if not markdownish(snapshot_path):
                snapshot_path.unlink(missing_ok=True)
                print(f"[{docset.skill_slug}] skipped {cluster.guide}: fallback was not markdown")
                continue
        snapshots.append(
            {
                "file": snapshot_file,
                "guide": cluster.guide,
                "source_type": source_type,
                "source_url": source_url,
                "page_count": str(len(cluster.entries)),
            }
        )
        print(f"[{docset.skill_slug}] captured {snapshot_file} from {source_type}")
        if delay:
            time.sleep(delay)

    write_manifest(
        path=references_root / "MANIFEST.md",
        skill_slug=docset.skill_slug,
        label=docset.label,
        version=selected_version or "current",
        llms_url=llms_url,
        llms_path=llms_path,
        total_pages=sum(len(cluster.entries) for cluster in clusters),
        total_guides=len(clusters),
        snapshots=snapshots,
    )

    print(
        f"[{docset.skill_slug}] synced {len(entries)} llms entries; "
        f"{len(snapshots)}/{len(clusters)} snapshots captured"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="Docset skill slug from scripts/docsets.yaml")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--registry", default="scripts/docsets.yaml")
    parser.add_argument(
        "--skills-root", default="plugins/ping-identity-docs/skills"
    )
    parser.add_argument(
        "--single-page-only",
        action="store_false",
        dest="page_fallback",
        help="Do not fall back to the first page in a guide when single-page.md is absent",
    )
    parser.set_defaults(page_fallback=True)
    return sync_docset(parser.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
