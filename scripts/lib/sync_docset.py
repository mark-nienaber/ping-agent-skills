#!/usr/bin/env python3
"""Sync one Ping Identity docset into an Agent Skill references directory."""

from __future__ import annotations

import argparse
import os
import subprocess
import tempfile
import time
from pathlib import Path

from generate_skill import generate_skill
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
LAST_CURL_ERROR = ""
MAX_ASSEMBLED_PAGES = 20


def curl_fetch(url: str, destination: Path) -> bool:
    global LAST_CURL_ERROR
    LAST_CURL_ERROR = ""
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(delete=False, dir=str(destination.parent)) as tmp:
        tmp_path = Path(tmp.name)
    try:
        command = [
            "curl",
            "-fsSL",
            "--retry",
            os.environ.get("PING_DOCS_CURL_RETRIES", "5"),
            "--retry-delay",
            os.environ.get("PING_DOCS_CURL_RETRY_DELAY", "2"),
            "--connect-timeout",
            os.environ.get("PING_DOCS_CONNECT_TIMEOUT", "20"),
            "--max-time",
            os.environ.get("PING_DOCS_MAX_TIME", "120"),
            "-A",
            USER_AGENT,
            "-o",
            str(tmp_path),
            url,
        ]
        result = subprocess.run(command, check=False, text=True, capture_output=True)
        if result.returncode != 0:
            LAST_CURL_ERROR = (result.stderr or result.stdout).strip()
            tmp_path.unlink(missing_ok=True)
            return False
        tmp_path.replace(destination)
        return True
    finally:
        tmp_path.unlink(missing_ok=True)


def markdownish(path: Path) -> bool:
    prefix = path.read_text(encoding="utf-8", errors="ignore")[:512].lstrip().lower()
    return not (prefix.startswith("<!doctype html") or prefix.startswith("<html"))


def assemble_guide_snapshot(cluster, destination: Path, delay: float = 0.02) -> int:
    """Assemble up to ``MAX_ASSEMBLED_PAGES`` and return the number captured.

    This is a bounded fallback for when ``single-page.md`` does not exist. A
    zero return value means that no usable page content was fetched.
    """
    if not cluster.entries:
        return 0

    assembled_parts: list[str] = []
    successful_fetches = 0

    for i, entry in enumerate(cluster.entries):
        with tempfile.NamedTemporaryFile(
            delete=False, suffix=".md", mode="w", encoding="utf-8"
        ) as tmp:
            tmp_path = Path(tmp.name)

        try:
            if curl_fetch(entry.url, tmp_path):
                content = tmp_path.read_text(encoding="utf-8", errors="replace").strip()
                if content:
                    assembled_parts.append(content)
                    successful_fetches += 1
                    if delay and i < len(cluster.entries) - 1:
                        time.sleep(delay)
            if successful_fetches >= MAX_ASSEMBLED_PAGES:
                # Keep offline fallbacks bounded even for very large guides.
                break
        finally:
            tmp_path.unlink(missing_ok=True)

    # Only write if we got at least some content
    if successful_fetches > 0:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text("\n\n---\n\n".join(assembled_parts), encoding="utf-8")
        return successful_fetches

    return 0


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
        detail = f": {LAST_CURL_ERROR}" if LAST_CURL_ERROR else ""
        die(f"[{docset.skill_slug}] failed to fetch {llms_url}{detail}")

    entries = parse_llms_file(llms_path)
    if not entries:
        die(f"[{docset.skill_slug}] no markdown entries parsed from {llms_path}")

    selected_version = detect_latest_version(
        entries, docset.base_url, preferred_version=docset.preferred_version
    )
    clusters = cluster_entries(entries, docset.base_url, selected_version)
    if not clusters:
        die(
            f"[{docset.skill_slug}] no guide clusters found for version "
            f"{selected_version or 'current'}"
        )

    snapshots: list[dict[str, str]] = []
    captured_files: set[str] = set()
    delay = float(os.environ.get("PING_DOCS_SYNC_DELAY", "0.05"))
    for cluster in clusters:
        snapshot_file = f"{cluster.guide_slug}.md"
        if snapshot_file in captured_files:
            print(
                f"[{docset.skill_slug}] skipped {cluster.guide} ({cluster.version}): "
                f"snapshot path collides with an earlier cluster: {snapshot_file}"
            )
            continue
        snapshot_path = snapshots_root / snapshot_file
        with tempfile.NamedTemporaryFile(
            delete=False, dir=snapshots_root, suffix=".md"
        ) as staged_file:
            staged_snapshot_path = Path(staged_file.name)
        try:
            source_type = ""
            source_url = ""
            pages_indexed = len(cluster.entries)
            pages_captured = 0
            for candidate_url in cluster.single_page_urls:
                if not curl_fetch(candidate_url, staged_snapshot_path):
                    continue
                if not markdownish(staged_snapshot_path):
                    print(
                        f"[{docset.skill_slug}] ignored non-Markdown single-page "
                        f"response for {cluster.guide}: {candidate_url}"
                    )
                    continue
                source_type = "single-page"
                source_url = candidate_url
                # A single-page endpoint represents the complete indexed guide.
                pages_captured = pages_indexed
                break

            if not source_type:
                if not args.page_fallback:
                    print(
                        f"[{docset.skill_slug}] skipped {cluster.guide}: "
                        "no Markdown single-page response"
                    )
                    continue

                # Try assembling from individual entries before giving up.
                pages_captured = assemble_guide_snapshot(
                    cluster, staged_snapshot_path, delay=0.01
                )
                if pages_captured:
                    source_type = "assembled"
                    source_url = llms_url
                else:
                    # Final fallback: fetch just the first page.
                    source_type = "page"
                    source_url = cluster.first_page_url
                    if not curl_fetch(cluster.first_page_url, staged_snapshot_path):
                        detail = f": {LAST_CURL_ERROR}" if LAST_CURL_ERROR else ""
                        print(
                            f"[{docset.skill_slug}] skipped {cluster.guide}: "
                            f"snapshot fetch failed{detail}"
                        )
                        continue
                    pages_captured = 1

            if not markdownish(staged_snapshot_path):
                print(
                    f"[{docset.skill_slug}] skipped {cluster.guide}: "
                    "content was not Markdown"
                )
                continue
            staged_snapshot_path.replace(snapshot_path)
        finally:
            staged_snapshot_path.unlink(missing_ok=True)

        snapshots.append(
            {
                "file": snapshot_file,
                "guide": cluster.guide,
                "source_type": source_type,
                "source_url": source_url,
                "pages_indexed": str(pages_indexed),
                "pages_captured": str(pages_captured),
                "coverage": "full" if pages_captured >= pages_indexed else "partial",
            }
        )
        captured_files.add(snapshot_file)
        print(
            f"[{docset.skill_slug}] captured {snapshot_file} from {source_type} "
            f"({pages_captured}/{pages_indexed} indexed pages)"
        )
        if delay:
            time.sleep(delay)

    if len(snapshots) == len(clusters):
        for old_snapshot in snapshots_root.glob("*.md"):
            if old_snapshot.name not in captured_files:
                old_snapshot.unlink()
    elif snapshots:
        print(
            f"[{docset.skill_slug}] retained existing snapshots because sync was partial"
        )

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

    # Keep generated routing metadata in step with the refreshed llms index and
    # the set of snapshots that this sync actually retained or captured.
    generate_skill(
        argparse.Namespace(
            repo_root=str(repo_root),
            registry=args.registry,
            skills_root=args.skills_root,
            slug=args.slug,
            max_routes=getattr(args, "max_routes", 12),
        )
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
    parser.add_argument(
        "--max-routes",
        type=int,
        default=12,
        help="Maximum routing rows regenerated in SKILL.md after a successful sync",
    )
    parser.set_defaults(page_fallback=True)
    return sync_docset(parser.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
