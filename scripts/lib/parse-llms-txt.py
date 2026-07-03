#!/usr/bin/env python3
"""Parse Ping Identity llms.txt files."""

from __future__ import annotations

import argparse
from pathlib import Path

from ping_docsets import (
    cluster_entries,
    detect_latest_version,
    dump_json,
    parse_llms_file,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    entries_parser = subparsers.add_parser("entries", help="Emit parsed entries as JSON")
    entries_parser.add_argument("llms_txt")

    guides_parser = subparsers.add_parser("guides", help="Emit clustered guides as TSV")
    guides_parser.add_argument("llms_txt")
    guides_parser.add_argument("--base-url", required=True)
    guides_parser.add_argument("--version")

    args = parser.parse_args()
    entries = parse_llms_file(Path(args.llms_txt))

    if args.command == "entries":
        dump_json([entry.__dict__ for entry in entries])
        return 0

    selected_version = args.version
    if selected_version is None:
        selected_version = detect_latest_version(entries, args.base_url)
    clusters = cluster_entries(entries, args.base_url, selected_version)
    for cluster in clusters:
        print(
            "\t".join(
                [
                    cluster.guide_slug,
                    cluster.guide,
                    cluster.version,
                    str(len(cluster.entries)),
                    cluster.single_page_url,
                    cluster.first_page_url,
                ]
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
