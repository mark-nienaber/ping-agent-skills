#!/usr/bin/env python3
"""Migrate legacy snapshot manifests to honest captured-page metadata."""

from __future__ import annotations

import argparse
from pathlib import Path
import re

from manifest import write_manifest
from ping_docsets import load_docsets
from validate import parse_manifest_table


FIELD_RE = re.compile(r"^- (?P<key>[^:]+):\s*(?P<value>.*)$")


def manifest_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in text.splitlines():
        match = FIELD_RE.match(line)
        if match:
            fields[match.group("key").strip().lower()] = match.group("value").strip()
    return fields


def infer_pages_captured(snapshot_path: Path, source_type: str, pages_indexed: int) -> int:
    """Infer the old syncer's actual bounded capture without claiming full coverage."""
    if pages_indexed <= 0 or not snapshot_path.is_file():
        return 0
    normalized_type = source_type.strip().lower()
    if normalized_type == "single-page":
        return pages_indexed
    if normalized_type == "page":
        return 1
    top_level_headings = sum(
        1
        for line in snapshot_path.read_text(encoding="utf-8", errors="replace").splitlines()
        if line.startswith("# ")
    )
    if normalized_type == "assembled":
        # Legacy assembly stopped after 20 successful pages. Each fetched Ping
        # Markdown page has one top-level page heading in the assembled file.
        inferred = top_level_headings or min(20, pages_indexed)
        return min(pages_indexed, 20, inferred)
    return min(pages_indexed, max(1, top_level_headings))


def migrate_manifest(manifest_path: Path, *, check: bool = False) -> bool:
    text = manifest_path.read_text(encoding="utf-8")
    headers, rows = parse_manifest_table(text, "## Source URLs")
    if not headers or "pages captured" in headers:
        return False
    fields = manifest_fields(text)
    references = manifest_path.parent
    snapshots: list[dict[str, object]] = []
    for row in rows:
        filename = row.get("snapshot", "").strip().strip("`")
        if not filename:
            continue
        snapshot_path = references / "snapshots" / filename
        if not snapshot_path.is_file():
            continue
        pages_indexed = int(row.get("pages indexed", "0"))
        source_type = row.get("source type", "")
        snapshots.append(
            {
                "file": filename,
                "source_type": source_type,
                "source_url": row.get("source url", ""),
                "pages_indexed": pages_indexed,
                "pages_captured": infer_pages_captured(
                    snapshot_path, source_type, pages_indexed
                ),
            }
        )

    if check:
        return True
    write_manifest(
        path=manifest_path,
        skill_slug=manifest_path.parent.parent.name,
        label=fields.get("product", manifest_path.parent.parent.name),
        version=fields.get("version", "current"),
        llms_url=fields.get("source", ""),
        llms_path=references / "llms.txt",
        total_pages=int(fields.get("total pages indexed", "0")),
        total_guides=int(fields.get("guides discovered", str(len(rows)))),
        snapshots=snapshots,
        sync_date=fields.get("sync date") or None,
    )
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--registry", default="scripts/docsets.yaml")
    parser.add_argument("--skills-root", default="plugins/ping-identity-docs/skills")
    parser.add_argument("--slug", action="append", default=[])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    requested = set(args.slug)
    migrated: list[str] = []
    for docset in load_docsets(repo_root / args.registry):
        if requested and docset.skill_slug not in requested:
            continue
        manifest_path = repo_root / args.skills_root / docset.skill_slug / "references" / "MANIFEST.md"
        if manifest_path.is_file() and migrate_manifest(manifest_path, check=args.check):
            migrated.append(docset.skill_slug)
    action = "need migration" if args.check else "migrated"
    print(f"{len(migrated)} manifests {action}")
    if migrated:
        print("\n".join(migrated))
    return 1 if args.check and migrated else 0


if __name__ == "__main__":
    raise SystemExit(main())
