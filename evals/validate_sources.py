#!/usr/bin/env python3
"""Check that every gold documentation URL in the pilot is reachable."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
from pathlib import Path
import subprocess


def gold_urls(cases_path: Path) -> list[str]:
    document = json.loads(cases_path.read_text(encoding="utf-8"))
    urls: set[str] = set()
    for case in document.get("cases", []):
        for group in case.get("answer_key", {}).get("gold_source_groups", []):
            urls.update(str(url) for url in group.get("urls", []))
    return sorted(urls)


def check_url(url: str, timeout: int) -> tuple[str, bool]:
    result = subprocess.run(
        [
            "curl",
            "-fsSL",
            "--retry",
            "1",
            "--connect-timeout",
            str(min(timeout, 10)),
            "--max-time",
            str(timeout),
            "-o",
            "/dev/null",
            url,
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    return url, result.returncode == 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=Path(__file__).with_name("cases.json"))
    parser.add_argument("--jobs", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args()

    urls = gold_urls(args.cases)
    failures: list[str] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.jobs)) as executor:
        futures = [executor.submit(check_url, url, args.timeout) for url in urls]
        for future in concurrent.futures.as_completed(futures):
            url, ok = future.result()
            print(f"{'OK' if ok else 'FAIL'} {url}")
            if not ok:
                failures.append(url)
    print(f"Checked {len(urls)} gold URLs: {len(failures)} failures")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
