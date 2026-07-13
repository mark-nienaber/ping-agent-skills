from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SEARCH_SCRIPT = (
    ROOT
    / "plugins"
    / "ping-identity-docs"
    / "runtime-skills"
    / "ping-docs"
    / "scripts"
    / "search_docs.py"
)
WRAPPER = ROOT / "scripts" / "search-docs.sh"

SPEC = importlib.util.spec_from_file_location("search_docs", SEARCH_SCRIPT)
assert SPEC and SPEC.loader
search_docs = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = search_docs
SPEC.loader.exec_module(search_docs)


class SearchDocsTests(unittest.TestCase):
    def test_pingam_account_lockout_finds_exact_page_and_offline_fallback(self) -> None:
        response = search_docs.search(
            "How do I configure account lockout in PingAM?",
            product_filter="pingam",
            top_k=3,
        )

        self.assertEqual(response["status"], "ok")
        first = response["results"][0]
        self.assertEqual(first["product"], "PingAM")
        self.assertEqual(first["title"], "Account lockout")
        self.assertIn("/pingam/8.1/", first["live_markdown_url"])
        self.assertTrue(first["live_markdown_url"].endswith("/security/account-lockout.md"))
        self.assertTrue(first["local_snapshot"].endswith("/pingam/references/snapshots/security.md"))
        self.assertTrue(first["local_manifest"].endswith("/pingam/references/MANIFEST.md"))
        self.assertTrue(first["snapshot_sync_date"])

    def test_pingauthorize_policy_task_finds_specific_policy_page(self) -> None:
        response = search_docs.search(
            "In PingAuthorize, create a policy to dynamically modify a resource based on its SCIM resource type",
            top_k=3,
        )

        self.assertEqual(response["status"], "ok")
        first = response["results"][0]
        self.assertEqual(first["product"], "PingAuthorize")
        self.assertIn("dynamically modify a resource", first["title"].lower())
        self.assertIn("/pingauthorize/11.1/", first["live_markdown_url"])
        self.assertTrue(first["live_markdown_url"].endswith("/paz_create_policy_modify.md"))
        self.assertTrue(
            first["local_snapshot"].endswith(
                "/pingauthorize/references/snapshots/pingauthorize-policy-administration-guide.md"
            )
        )

    def test_unrelated_prompt_abstains_without_loading_indexes(self) -> None:
        response = search_docs.search("Write a Python hello world program", top_k=5)

        self.assertEqual(response["status"], "no_results")
        self.assertEqual(response["results"], [])
        self.assertIn("IAM-specific signal", response["reason"])

    def test_json_cli_and_product_alias(self) -> None:
        completed = subprocess.run(
            [
                str(WRAPPER),
                "--json",
                "--product",
                "AM",
                "--top-k",
                "1",
                "OAuth 2.0 pushed authorization request endpoint",
            ],
            check=True,
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        response = json.loads(completed.stdout)

        self.assertEqual(response["status"], "ok")
        self.assertEqual(len(response["results"]), 1)
        self.assertEqual(response["results"][0]["product_slug"], "pingam")
        self.assertTrue(response["results"][0]["live_markdown_url"].endswith("/oauth2-par-endpoint.md"))

    def test_requested_older_version_does_not_claim_current_snapshot(self) -> None:
        response = search_docs.search(
            "PingAM 7.5 account lockout",
            product_filter="pingam",
            top_k=1,
        )

        first = response["results"][0]
        self.assertEqual(first["document_version"], "7.5")
        self.assertIn("/pingam/7.5/", first["live_markdown_url"])
        self.assertIsNone(first["local_snapshot"])
        self.assertEqual(first["snapshot_version"], "8.1")

    def test_standalone_data_root_layout(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            tmp_path = Path(temporary_directory)
            docset = tmp_path / "references" / "docsets" / "pingam" / "references"
            snapshots = docset / "snapshots"
            snapshots.mkdir(parents=True)
            (docset / "llms.txt").write_text(
                "# PingAM\n\n## PingAM 8.1\n\n"
                "- [Account lockout](https://docs.pingidentity.com/pingam/8.1/security/account-lockout.md): Configure account lockout.\n",
                encoding="utf-8",
            )
            (docset / "MANIFEST.md").write_text(
                "# Snapshot Manifest - pingam\n\n"
                "- Product: PingAM\n"
                "- Version: 8.1\n"
                "- Sync date: 2026-07-10\n"
                "- Source: https://docs.pingidentity.com/pingam/llms.txt\n\n"
                "| Snapshot | Source type | Source URL | Pages indexed |\n"
                "|---|---|---|---|\n"
                "| security.md | assembled | <1 pages from security> | 1 |\n",
                encoding="utf-8",
            )
            (snapshots / "security.md").write_text("# Account lockout\n", encoding="utf-8")

            response = search_docs.search(
                "PingAM account lockout",
                data_root=tmp_path / "references" / "docsets",
                top_k=1,
            )

            self.assertEqual(response["status"], "ok")
            self.assertEqual(
                response["results"][0]["local_snapshot"],
                str((snapshots / "security.md").resolve()),
            )

    def test_unmanifested_retained_snapshot_is_not_presented_as_current(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            tmp_path = Path(temporary_directory)
            docset = tmp_path / "references" / "docsets" / "pingds" / "references"
            snapshots = docset / "snapshots"
            snapshots.mkdir(parents=True)
            (docset / "llms.txt").write_text(
                "# PingDS\n\n## PingDS 8.1\n\n"
                "- [Account status](https://docs.pingidentity.com/pingds/8.1/security/account-status.md): Inspect account status.\n",
                encoding="utf-8",
            )
            (docset / "MANIFEST.md").write_text(
                "# Snapshot Manifest - pingds\n\n"
                "- Product: PingDS\n"
                "- Version: 8.1\n"
                "- Sync date: 2026-07-13\n"
                "- Source: https://docs.pingidentity.com/pingds/llms.txt\n\n"
                "| Snapshot | Source type | Source URL | Pages captured | Pages indexed | Coverage |\n"
                "|---|---|---|---|---|---|\n",
                encoding="utf-8",
            )
            (snapshots / "security.md").write_text("# Stale retained content\n", encoding="utf-8")

            response = search_docs.search(
                "PingDS account status",
                data_root=tmp_path / "references" / "docsets",
                top_k=1,
            )

            self.assertEqual(response["status"], "ok")
            self.assertIsNone(response["results"][0]["local_snapshot"])


if __name__ == "__main__":
    unittest.main()
