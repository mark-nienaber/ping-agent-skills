#!/usr/bin/env python3
"""Prune stale doc versions from already-cached llms.txt indexes.

One-time maintenance for repositories synced before version pruning was part
of sync. Idempotent: re-running changes nothing. For each enabled docset with
a cached index, rewrite the index keeping only the selected version's entries
plus version-independent pages, then refresh the llms.txt checksum row in the
manifest so validation stays green.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))

from ping_docsets import (  # noqa: E402
    detect_latest_version,
    find_docset,
    load_docsets,
    parse_llms_file,
    prune_llms_text,
    sha256_file,
)


MANIFEST_CHECKSUM_RE = re.compile(r"^(\| llms\.txt \| )[0-9a-fA-F]{64}( \|)$", re.MULTILINE)


def prune_docset(docset, skills_root: Path, dry_run: bool) -> bool:
    llms_path = skills_root / docset.skill_slug / "references" / "llms.txt"
    if not llms_path.is_file():
        return False

    entries = parse_llms_file(llms_path)
    if not entries:
        print(f"[{docset.skill_slug}] no entries parsed; skipping")
        return False

    selected_version = detect_latest_version(
        entries, docset.base_url, preferred_version=docset.preferred_version
    )
    original = llms_path.read_text(encoding="utf-8")
    pruned = prune_llms_text(original, docset.base_url, selected_version)
    if pruned == original:
        return False

    before_entries = len(entries)
    before_bytes = len(original.encode("utf-8"))
    after_entries = len(prune_llms_text(original, docset.base_url, selected_version).strip().splitlines())
    after_entries = sum(
        1 for line in pruned.splitlines() if line.lstrip().startswith("- [")
    )
    after_bytes = len(pruned.encode("utf-8"))
    if not dry_run:
        llms_path.write_text(pruned, encoding="utf-8")
        manifest_path = llms_path.parent / "MANIFEST.md"
        if manifest_path.is_file():
            manifest = manifest_path.read_text(encoding="utf-8")
            checksum = sha256_file(llms_path)
            updated, count = MANIFEST_CHECKSUM_RE.subn(
                rf"\g<1>{checksum}\g<2>", manifest, count=1
            )
            if count == 1 and updated != manifest:
                manifest_path.write_text(updated, encoding="utf-8")
            elif count != 1:
                print(f"[{docset.skill_slug}] WARNING: manifest llms.txt checksum row not found")

    print(
        f"[{docset.skill_slug}] {before_entries} -> {after_entries} entries, "
        f"{before_bytes / 1e6:.1f} -> {after_bytes / 1e6:.1f} MB "
        f"(keeping {selected_version or 'current'}"
        f"{' DRY RUN' if dry_run else ''})"
    )
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--registry", default="scripts/docsets.yaml")
    parser.add_argument(
        "--skills-root", default="plugins/ping-identity-docs/skills"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="report changes without writing"
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    skills_root = repo_root / args.skills_root
    changed = 0
    for docset in load_docsets(repo_root / args.registry):
        if not docset.enabled:
            continue
        if prune_docset(docset, skills_root, args.dry_run):
            changed += 1
    print(f"{changed} docset index(es) {'would change' if args.dry_run else 'pruned'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
