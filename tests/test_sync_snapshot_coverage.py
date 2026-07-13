from __future__ import annotations

import argparse
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts" / "lib"))

import sync_docset  # noqa: E402
from generate_skill import manifest_snapshot_names  # noqa: E402
from ping_docsets import GuideCluster, LlmEntry  # noqa: E402


def make_cluster(page_count: int) -> GuideCluster:
    entries = tuple(
        LlmEntry(
            title=f"Page {index}",
            url=f"https://docs.example/product/guide/page-{index}.md",
            description="",
            heading="Guide",
        )
        for index in range(page_count)
    )
    return GuideCluster(
        guide="guide",
        version="current",
        entries=entries,
        first_page_url=entries[0].url if entries else "",
        single_page_url="https://docs.example/product/guide/single-page.md",
        single_page_urls=("https://docs.example/product/guide/single-page.md",),
    )


class AssembleGuideSnapshotTests(unittest.TestCase):
    def test_returns_actual_pages_captured_and_stops_at_cap(self) -> None:
        cluster = make_cluster(25)
        calls: list[str] = []

        def fake_fetch(url: str, destination: Path) -> bool:
            calls.append(url)
            destination.write_text(f"# {url.rsplit('/', 1)[-1]}\n", encoding="utf-8")
            return True

        with tempfile.TemporaryDirectory() as temp_dir:
            destination = Path(temp_dir) / "snapshot.md"
            with patch.object(sync_docset, "curl_fetch", side_effect=fake_fetch):
                captured = sync_docset.assemble_guide_snapshot(
                    cluster, destination, delay=0
                )

            self.assertEqual(sync_docset.MAX_ASSEMBLED_PAGES, captured)
            self.assertEqual(sync_docset.MAX_ASSEMBLED_PAGES, len(calls))
            self.assertEqual(19, destination.read_text(encoding="utf-8").count("\n---\n"))

    def test_counts_only_successful_nonempty_pages(self) -> None:
        cluster = make_cluster(5)

        def fake_fetch(url: str, destination: Path) -> bool:
            page_number = int(url.rsplit("-", 1)[-1].removesuffix(".md"))
            if page_number == 0:
                return False
            destination.write_text("" if page_number == 1 else f"# Page {page_number}\n")
            return True

        with tempfile.TemporaryDirectory() as temp_dir:
            destination = Path(temp_dir) / "snapshot.md"
            with patch.object(sync_docset, "curl_fetch", side_effect=fake_fetch):
                captured = sync_docset.assemble_guide_snapshot(
                    cluster, destination, delay=0
                )

            self.assertEqual(3, captured)
            self.assertEqual(2, destination.read_text(encoding="utf-8").count("\n---\n"))


class SyncDocsetCoverageTests(unittest.TestCase):
    def test_sync_records_partial_assembly_and_regenerates_routes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            registry = repo_root / "scripts" / "docsets.yaml"
            registry.parent.mkdir(parents=True)
            registry.write_text(
                """docsets:
  - skill_slug: example
    label: Example Product
    source: test
    base_url: https://docs.example/product
    enabled: true
""",
                encoding="utf-8",
            )
            skill_root = repo_root / "skills" / "example"
            skill_root.mkdir(parents=True)
            (skill_root / "SKILL.md").write_text("stale\n", encoding="utf-8")

            llms_text = "## Guide\n" + "\n".join(
                f"- [Page {index}](https://docs.example/product/guide/page-{index}.md)"
                for index in range(25)
            )

            def fake_fetch(url: str, destination: Path) -> bool:
                if url.endswith("/llms.txt"):
                    destination.write_text(llms_text, encoding="utf-8")
                    return True
                if url.endswith("/single-page.md"):
                    return False
                destination.write_text(f"# {url.rsplit('/', 1)[-1]}\n", encoding="utf-8")
                return True

            args = argparse.Namespace(
                repo_root=str(repo_root),
                registry="scripts/docsets.yaml",
                skills_root="skills",
                slug="example",
                page_fallback=True,
                max_routes=12,
            )
            with (
                patch.object(sync_docset, "curl_fetch", side_effect=fake_fetch),
                patch.object(sync_docset.time, "sleep"),
                patch.dict("os.environ", {"PING_DOCS_SYNC_DELAY": "0"}),
            ):
                result = sync_docset.sync_docset(args)

            self.assertEqual(0, result)
            manifest = (skill_root / "references" / "MANIFEST.md").read_text(
                encoding="utf-8"
            )
            self.assertIn("- Guides fully captured: 0", manifest)
            self.assertIn("- Guides partially captured: 1", manifest)
            self.assertIn("- Total pages indexed: 25", manifest)
            self.assertIn("- Total snapshot pages captured: 20", manifest)
            self.assertIn("| guide.md | assembled |", manifest)
            self.assertIn("| 25 | 20 | partial |", manifest)

            skill_text = (skill_root / "SKILL.md").read_text(encoding="utf-8")
            self.assertNotEqual("stale\n", skill_text)
            self.assertIn("references/snapshots/guide.md", skill_text)


class GeneratedRouteSnapshotTests(unittest.TestCase):
    def test_only_current_manifest_source_rows_enable_snapshot_routes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            manifest = Path(temp_dir) / "MANIFEST.md"
            manifest.write_text(
                "## Source URLs\n\n"
                "| Snapshot | Source type | Source URL | Pages indexed | Pages captured | Coverage |\n"
                "|---|---|---|---|---|---|\n"
                "| current.md | page | https://docs.example/current.md | 1 | 1 | full |\n\n"
                "## Checksums\n\n"
                "| File | SHA-256 |\n"
                "|---|---|\n"
                "| snapshots/current.md | abc |\n"
                "| snapshots/retained.md | def |\n",
                encoding="utf-8",
            )

            self.assertEqual({"current.md"}, manifest_snapshot_names(manifest))


if __name__ == "__main__":
    unittest.main()
