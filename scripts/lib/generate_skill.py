#!/usr/bin/env python3
"""Generate an Agent Skills SKILL.md scaffold from a cached Ping llms.txt."""

from __future__ import annotations

import argparse
import textwrap
from pathlib import Path

from ping_docsets import (
    cluster_entries,
    detect_latest_version,
    die,
    find_docset,
    load_docsets,
    parse_llms_file,
    product_summary,
    routing_url_pattern,
    task_category,
)


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def manifest_snapshot_names(manifest_path: Path) -> set[str]:
    """Return only snapshots declared by the current manifest source table."""
    if not manifest_path.is_file():
        return set()
    manifest = manifest_path.read_text(encoding="utf-8")
    if "## Source URLs" not in manifest:
        return set()
    source_section = manifest.split("## Source URLs", 1)[1].split("## Checksums", 1)[0]
    names: set[str] = set()
    for line in source_section.splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells and cells[0].endswith(".md"):
            names.add(cells[0])
    return names


def generated_description(label: str, clusters: list) -> str:
    del clusters
    description = (
        f"Use when the user explicitly names {label} or its exact docset and needs "
        "official, version-specific product documentation. Do not use for "
        "generic IAM or product-selection questions. Routes to live Ping docs; "
        "dated snapshots are the offline fallback."
    )
    if len(description) <= 500:
        return description
    return description[:497].rstrip() + "..."


def generate_skill(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    registry_path = repo_root / args.registry
    skills_root = repo_root / args.skills_root
    docset = find_docset(load_docsets(registry_path), args.slug)

    skill_root = skills_root / docset.skill_slug
    references_root = skill_root / "references"
    llms_path = references_root / "llms.txt"
    if not llms_path.exists():
        die(f"{llms_path} does not exist; run scripts/sync-docset.sh {docset.skill_slug}")

    entries = parse_llms_file(llms_path)
    if not entries:
        die(f"No llms.txt entries parsed from {llms_path}")
    selected_version = detect_latest_version(
        entries, docset.base_url, preferred_version=docset.preferred_version
    )
    clusters = cluster_entries(entries, docset.base_url, selected_version)
    if not clusters:
        die(f"No guide clusters found for {docset.skill_slug}")

    description = generated_description(docset.label, clusters)
    summary = product_summary(docset.label, entries)

    table_lines = [
        "| Task category | Guide slug | Live URL pattern | Snapshot |",
        "|---|---|---|---|",
    ]
    manifested_snapshots = manifest_snapshot_names(references_root / "MANIFEST.md")
    for cluster in clusters[: args.max_routes]:
        snapshot = f"references/snapshots/{cluster.guide_slug}.md"
        if (
            cluster.guide_slug + ".md" not in manifested_snapshots
            or not (skill_root / snapshot).exists()
        ):
            snapshot = "live-only"
        table_lines.append(
            f"| {task_category(cluster)} | {cluster.guide} | "
            f"{routing_url_pattern(docset.base_url, cluster)} | {snapshot} |"
        )

    body = f"""---
name: {docset.skill_slug}
description: {yaml_quote(description)}
license: MIT
---

# {docset.label}

{summary}

## Live source of truth

- Product docs: {docset.base_url}/
- llms.txt index: {docset.base_url}/llms.txt
- Snapshot version: {selected_version or "current"}
- Snapshot manifest: references/MANIFEST.md

## Retrieval strategy

1. Use the routing table to narrow the task to a guide when possible.
2. Search `references/llms.txt` for task terms and inspect at most 20 matching lines. Never load the whole index. Prefer `rg -i -n --max-count 20 '<term1>|<term2>' references/llms.txt` when shell access is available.
3. Fetch only the best matching live `.md` page from Ping documentation.
4. If that URL moved, fetch the live llms.txt index above and repeat the targeted search.
5. If live access is unavailable, read only the closest snapshot, check `references/MANIFEST.md`, and disclose its version, sync date, and partial-capture status.

## Task routing

{chr(10).join(table_lines)}

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.
"""

    skill_path = skill_root / "SKILL.md"
    skill_path.write_text(textwrap.dedent(body).strip() + "\n", encoding="utf-8")
    print(f"Wrote {skill_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="Docset skill slug from scripts/docsets.yaml")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--registry", default="scripts/docsets.yaml")
    parser.add_argument(
        "--skills-root", default="plugins/ping-identity-docs/skills"
    )
    parser.add_argument("--max-routes", type=int, default=12)
    return generate_skill(parser.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
