#!/usr/bin/env python3
"""Sync all enabled Ping Identity docsets in bounded parallel batches."""

from __future__ import annotations

import argparse
import concurrent.futures
import subprocess
from pathlib import Path

from ping_docsets import load_docsets


def run_sync(repo_root: Path, slug: str) -> tuple[str, int, str]:
    command = [str(repo_root / "scripts" / "sync-docset.sh"), slug]
    result = subprocess.run(command, cwd=repo_root, text=True, capture_output=True)
    output = result.stdout
    if result.stderr:
        output = output + result.stderr
    return slug, result.returncode, output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--registry", default="scripts/docsets.yaml")
    parser.add_argument("--batch-size", type=int, default=5)
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    docsets = [
        docset
        for docset in load_docsets(repo_root / args.registry)
        if docset.enabled
    ]
    print(f"Syncing {len(docsets)} enabled docsets with batch size {args.batch_size}")

    failures: list[str] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.batch_size) as executor:
        future_map = {
            executor.submit(run_sync, repo_root, docset.skill_slug): docset.skill_slug
            for docset in docsets
        }
        for future in concurrent.futures.as_completed(future_map):
            slug, returncode, output = future.result()
            status = "ok" if returncode == 0 else "failed"
            print(f"== {slug}: {status} ==")
            print(output.rstrip())
            if returncode != 0:
                failures.append(slug)

    print("")
    print(f"Summary: {len(docsets) - len(failures)} ok, {len(failures)} failed")
    if failures:
        print("Failures: " + ", ".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
