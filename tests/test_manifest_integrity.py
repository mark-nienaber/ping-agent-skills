from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts" / "lib"))

from manifest import write_manifest  # noqa: E402
from migrate_manifests import infer_pages_captured  # noqa: E402
from ping_docsets import sha256_file  # noqa: E402
from validate import Reporter, validate_manifest  # noqa: E402


class ManifestWriterTests(unittest.TestCase):
    def test_distinguishes_indexed_and_captured_pages(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            references = Path(temp_dir)
            snapshots = references / "snapshots"
            snapshots.mkdir()
            llms_path = references / "llms.txt"
            llms_path.write_text("index\n", encoding="utf-8")
            (snapshots / "guide.md").write_text("snapshot\n", encoding="utf-8")
            manifest_path = references / "MANIFEST.md"

            write_manifest(
                path=manifest_path,
                skill_slug="example",
                label="Example",
                version="current",
                llms_url="https://docs.example/llms.txt",
                llms_path=llms_path,
                total_pages=240,
                total_guides=1,
                snapshots=[
                    {
                        "file": "guide.md",
                        "guide": "guide",
                        "source_type": "assembled",
                        "source_url": "https://docs.example/llms.txt",
                        "pages_indexed": "240",
                        "pages_captured": "20",
                    }
                ],
            )

            manifest = manifest_path.read_text(encoding="utf-8")
            self.assertIn("- Guides fully captured: 0", manifest)
            self.assertIn("- Guides partially captured: 1", manifest)
            self.assertIn("- Total snapshot pages captured: 20", manifest)
            self.assertIn("| 240 | 20 | partial |", manifest)

            reporter = Reporter()
            validate_manifest(references, manifest_path, manifest, reporter)
            self.assertEqual([], reporter.errors)
            self.assertEqual([], reporter.warnings)

    def test_rejects_capture_count_greater_than_index(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            references = Path(temp_dir)
            (references / "snapshots").mkdir()
            llms_path = references / "llms.txt"
            llms_path.write_text("index\n", encoding="utf-8")
            (references / "snapshots" / "guide.md").write_text("snapshot\n")

            with self.assertRaisesRegex(ValueError, "cannot exceed"):
                write_manifest(
                    path=references / "MANIFEST.md",
                    skill_slug="example",
                    label="Example",
                    version="current",
                    llms_url="https://docs.example/llms.txt",
                    llms_path=llms_path,
                    total_pages=1,
                    total_guides=1,
                    snapshots=[
                        {
                            "file": "guide.md",
                            "source_type": "assembled",
                            "source_url": "https://docs.example/llms.txt",
                            "pages_indexed": 1,
                            "pages_captured": 2,
                        }
                    ],
                )

    def test_legacy_page_count_input_remains_supported(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            references = Path(temp_dir)
            (references / "snapshots").mkdir()
            llms_path = references / "llms.txt"
            llms_path.write_text("index\n", encoding="utf-8")
            (references / "snapshots" / "guide.md").write_text("snapshot\n")

            write_manifest(
                path=references / "MANIFEST.md",
                skill_slug="example",
                label="Example",
                version="current",
                llms_url="https://docs.example/llms.txt",
                llms_path=llms_path,
                total_pages=3,
                total_guides=1,
                snapshots=[
                    {
                        "file": "guide.md",
                        "source_type": "single-page",
                        "source_url": "https://docs.example/single-page.md",
                        "page_count": "3",
                    }
                ],
            )
            manifest = (references / "MANIFEST.md").read_text(encoding="utf-8")
            self.assertIn("| 3 | 3 | full |", manifest)

    def test_legacy_capture_inference_never_claims_all_indexed_pages(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            snapshot = Path(temp_dir) / "assembled.md"
            snapshot.write_text(
                "\n\n---\n\n".join(f"# Page {index}\n" for index in range(20)),
                encoding="utf-8",
            )

            self.assertEqual(20, infer_pages_captured(snapshot, "assembled", 240))
            self.assertEqual(240, infer_pages_captured(snapshot, "single-page", 240))
            self.assertEqual(1, infer_pages_captured(snapshot, "page", 240))


class ManifestValidatorTests(unittest.TestCase):
    def test_detects_false_capture_summary_and_coverage(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            references = Path(temp_dir)
            snapshots = references / "snapshots"
            snapshots.mkdir()
            llms_path = references / "llms.txt"
            llms_path.write_text("index\n", encoding="utf-8")
            snapshot_path = snapshots / "guide.md"
            snapshot_path.write_text("snapshot\n", encoding="utf-8")
            manifest_path = references / "MANIFEST.md"
            manifest = f"""# Snapshot Manifest - example

- Guides captured: 1
- Guides fully captured: 1
- Guides partially captured: 0
- Total snapshot pages captured: 240

## Source URLs

| Snapshot | Source type | Source URL | Pages indexed | Pages captured | Coverage |
|---|---|---|---|---|---|
| guide.md | assembled | https://docs.example/llms.txt | 240 | 20 | full |

## Checksums

| File | SHA-256 |
|---|---|
| llms.txt | {sha256_file(llms_path)} |
| snapshots/guide.md | {sha256_file(snapshot_path)} |
"""
            reporter = Reporter()
            validate_manifest(references, manifest_path, manifest, reporter)
            errors = "\n".join(reporter.errors)
            self.assertIn("coverage must be 'partial'", errors)
            self.assertIn("guides fully captured says 1, expected 0", errors)
            self.assertIn("guides partially captured says 0, expected 1", errors)
            self.assertIn(
                "total snapshot pages captured says 240, expected 20", errors
            )

    def test_detects_hash_mismatch_duplicates_missing_and_retained_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            references = Path(temp_dir)
            snapshots = references / "snapshots"
            snapshots.mkdir()
            llms_path = references / "llms.txt"
            llms_path.write_text("index\n", encoding="utf-8")
            snapshot_path = snapshots / "guide.md"
            snapshot_path.write_text("snapshot\n", encoding="utf-8")
            (snapshots / "retained.md").write_text("retained\n", encoding="utf-8")
            manifest_path = references / "MANIFEST.md"

            source_row = (
                "| guide.md | assembled | https://docs.example/llms.txt | "
                "5 | 2 | partial |"
            )
            manifest = f"""# Snapshot Manifest - example

## Source URLs

| Snapshot | Source type | Source URL | Pages indexed | Pages captured | Coverage |
|---|---|---|---|---|---|
{source_row}
{source_row}

## Checksums

| File | SHA-256 |
|---|---|
| llms.txt | {'0' * 64} |
| snapshots/guide.md | {sha256_file(snapshot_path)} |
| snapshots/guide.md | {sha256_file(snapshot_path)} |
| snapshots/missing.md | {'1' * 64} |
"""
            manifest_path.write_text(manifest, encoding="utf-8")

            reporter = Reporter()
            validate_manifest(references, manifest_path, manifest, reporter)
            errors = "\n".join(reporter.errors)
            warnings = "\n".join(reporter.warnings)
            self.assertIn("duplicate snapshot entry: guide.md", errors)
            self.assertIn("duplicate checksum entry: snapshots/guide.md", errors)
            self.assertIn("SHA-256 mismatch for llms.txt", errors)
            self.assertIn("checksummed file is missing: snapshots/missing.md", errors)
            self.assertIn(
                "snapshot checksum has no Source URLs entry: snapshots/missing.md",
                errors,
            )
            self.assertIn(
                "retained snapshots are not in the current manifest: snapshots/retained.md",
                warnings,
            )

    def test_accepts_legacy_source_table_with_valid_checksums(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            references = Path(temp_dir)
            snapshots = references / "snapshots"
            snapshots.mkdir()
            llms_path = references / "llms.txt"
            llms_path.write_text("index\n", encoding="utf-8")
            snapshot_path = snapshots / "guide.md"
            snapshot_path.write_text("snapshot\n", encoding="utf-8")
            manifest_path = references / "MANIFEST.md"
            manifest = f"""# Snapshot Manifest - example

## Source URLs

| Snapshot | Source type | Source URL | Pages indexed |
|---|---|---|---|
| guide.md | single-page | https://docs.example/single-page.md | 5 |

## Checksums

| File | SHA-256 |
|---|---|
| llms.txt | {sha256_file(llms_path)} |
| snapshots/guide.md | {sha256_file(snapshot_path)} |
"""
            manifest_path.write_text(manifest, encoding="utf-8")

            reporter = Reporter()
            validate_manifest(references, manifest_path, manifest, reporter)
            self.assertEqual([], reporter.errors)
            self.assertEqual([], reporter.warnings)


if __name__ == "__main__":
    unittest.main()
