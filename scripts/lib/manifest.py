#!/usr/bin/env python3
"""Write snapshot manifests."""

from __future__ import annotations

from pathlib import Path
from typing import Mapping, Sequence

from ping_docsets import sha256_file, today_iso


def write_manifest(
    *,
    path: str | Path,
    skill_slug: str,
    label: str,
    version: str,
    llms_url: str,
    llms_path: str | Path,
    total_pages: int,
    total_guides: int,
    snapshots: Sequence[Mapping[str, object]],
    sync_date: str | None = None,
) -> None:
    path = Path(path)
    normalized_snapshots: list[dict[str, object]] = []
    snapshot_files: set[str] = set()
    for snapshot in snapshots:
        # ``page_count`` is accepted for callers using the original manifest
        # API. New syncs must provide the independent indexed/captured counts.
        pages_indexed = int(snapshot.get("pages_indexed", snapshot.get("page_count", 0)))
        pages_captured = int(
            snapshot.get("pages_captured", snapshot.get("page_count", pages_indexed))
        )
        if pages_indexed < 0 or pages_captured < 0:
            raise ValueError("snapshot page counts cannot be negative")
        if pages_captured > pages_indexed:
            raise ValueError("snapshot pages captured cannot exceed pages indexed")
        snapshot_file = str(snapshot["file"])
        if snapshot_file in snapshot_files:
            raise ValueError(f"duplicate snapshot manifest entry: {snapshot_file}")
        snapshot_files.add(snapshot_file)
        coverage = "full" if pages_captured == pages_indexed else "partial"
        normalized_snapshots.append(
            {
                **snapshot,
                "file": snapshot_file,
                "pages_indexed": pages_indexed,
                "pages_captured": pages_captured,
                "coverage": coverage,
            }
        )

    if len(normalized_snapshots) > total_guides:
        raise ValueError("snapshot count cannot exceed discovered guide count")

    fully_captured = sum(
        snapshot["coverage"] == "full" for snapshot in normalized_snapshots
    )
    partially_captured = len(normalized_snapshots) - fully_captured
    captured_pages = sum(
        int(snapshot["pages_captured"]) for snapshot in normalized_snapshots
    )
    lines: list[str] = [
        f"# Snapshot Manifest - {skill_slug}",
        "",
        f"- Product: {label}",
        f"- Version: {version or 'current'}",
        f"- Sync date: {sync_date or today_iso()}",
        f"- Source: {llms_url}",
        f"- Guides discovered: {total_guides}",
        f"- Guides captured: {len(normalized_snapshots)}",
        f"- Guides fully captured: {fully_captured}",
        f"- Guides partially captured: {partially_captured}",
        f"- Guides without snapshots: {total_guides - len(normalized_snapshots)}",
        f"- Total pages indexed: {total_pages}",
        f"- Total snapshot pages captured: {captured_pages}",
        "",
        "## Source URLs",
        "",
        "| Snapshot | Source type | Source URL | Pages indexed | Pages captured | Coverage |",
        "|---|---|---|---|---|---|",
    ]
    for snapshot in normalized_snapshots:
        lines.append(
            "| {file} | {source_type} | {source_url} | {pages_indexed} | "
            "{pages_captured} | {coverage} |".format(**snapshot)
        )

    lines.extend(["", "## Checksums", "", "| File | SHA-256 |", "|---|---|"])
    lines.append(f"| llms.txt | {sha256_file(llms_path)} |")
    for snapshot in normalized_snapshots:
        snapshot_file = str(snapshot["file"])
        snapshot_path = path.parent / "snapshots" / snapshot_file
        lines.append(f"| snapshots/{snapshot_file} | {sha256_file(snapshot_path)} |")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
