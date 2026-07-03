#!/usr/bin/env python3
"""Write snapshot manifests."""

from __future__ import annotations

from pathlib import Path
from typing import Sequence

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
    snapshots: Sequence[dict[str, str]],
) -> None:
    path = Path(path)
    lines: list[str] = [
        f"# Snapshot Manifest - {skill_slug}",
        "",
        f"- Product: {label}",
        f"- Version: {version or 'current'}",
        f"- Sync date: {today_iso()}",
        f"- Source: {llms_url}",
        f"- Guides discovered: {total_guides}",
        f"- Guides captured: {len(snapshots)}",
        f"- Total pages indexed: {total_pages}",
        "",
        "## Source URLs",
        "",
        "| Snapshot | Source type | Source URL | Pages indexed |",
        "|---|---|---|---|",
    ]
    for snapshot in snapshots:
        lines.append(
            "| {file} | {source_type} | {source_url} | {page_count} |".format(**snapshot)
        )

    lines.extend(["", "## Checksums", "", "| File | SHA-256 |", "|---|---|"])
    lines.append(f"| llms.txt | {sha256_file(llms_path)} |")
    for snapshot in snapshots:
        snapshot_path = path.parent / "snapshots" / snapshot["file"]
        lines.append(f"| snapshots/{snapshot['file']} | {sha256_file(snapshot_path)} |")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
