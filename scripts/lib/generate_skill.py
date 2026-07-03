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


def generated_description(label: str, clusters: list) -> str:
    tasks = []
    for cluster in clusters[:6]:
        tasks.append(task_category(cluster).split(":", 1)[0].lower())
    task_text = ", ".join(dict.fromkeys(tasks))
    description = (
        f"Use when working with {label}: {task_text}. "
        "Routes to live Ping docs; snapshots fallback."
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
    for cluster in clusters[: args.max_routes]:
        snapshot = f"references/snapshots/{cluster.guide_slug}.md"
        if not (skill_root / snapshot).exists():
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

## Fetch strategy

1. Read references/llms.txt for page discovery.
2. Match the user task to page titles, page descriptions, and the routing table below.
3. Fetch the selected live `.md` URL from Ping documentation.
4. If live fetch is unavailable, read the closest file under references/snapshots/.

## Task routing

{chr(10).join(table_lines)}

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.
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
    parser.add_argument("--max-routes", type=int, default=30)
    return generate_skill(parser.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
