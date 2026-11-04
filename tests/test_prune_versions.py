from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts" / "lib"))

from ping_docsets import prune_llms_text  # noqa: E402


class PruneLlmsTextTests(unittest.TestCase):
    def test_prunes_entries_under_other_versions(self) -> None:
        text = (
            "# PingAM\n\n"
            "## Pingam 8.1\n\n"
            "- [Keep](https://docs.pingidentity.com/pingam/8.1/security/a.md): keep me\n"
            "## Pingam 7.5\n\n"
            "- [Drop](https://docs.pingidentity.com/pingam/7.5/security/b.md): drop me\n"
            "- [Keep unversioned](https://docs.pingidentity.com/pingam/release-notes/changes-7.5.md): keep me\n"
        )
        result = prune_llms_text(text, "https://docs.pingidentity.com/pingam", "8.1")
        self.assertIn("/pingam/8.1/security/a.md", result)
        self.assertNotIn("/pingam/7.5/security/b.md", result)
        self.assertIn("/pingam/release-notes/changes-7.5.md", result)

    def test_no_selected_version_keeps_everything(self) -> None:
        text = "- [A](https://docs.example/product/2.0/x.md)\n- [B](https://docs.example/product/y.md)\n"
        self.assertEqual(text, prune_llms_text(text, "https://docs.example/product", None))

    def test_empty_version_string_behaves_like_none(self) -> None:
        text = "- [A](https://docs.example/product/2.0/x.md)\n"
        self.assertEqual(text, prune_llms_text(text, "https://docs.example/product", ""))

    def test_non_entry_lines_untouched(self) -> None:
        text = (
            "# Title\n\n"
            "> advisory line with https://developer.pingidentity.com/x.md link\n\n"
            "## Heading 8.1\n\n"
            "- [A](https://docs.pingidentity.com/pingam/8.1/a.md)\n"
        )
        self.assertEqual(text, prune_llms_text(text, "https://docs.pingidentity.com/pingam", "8.1"))

    def test_cross_host_entries_untouched(self) -> None:
        text = "- [Elsewhere](https://other.example/product/1.0/z.md)\n"
        self.assertEqual(text, prune_llms_text(text, "https://docs.example/product", "2.0"))

    def test_preserves_trailing_newline_and_headings(self) -> None:
        text = (
            "## A 8.1\n\n"
            "- [A](https://docs.pingidentity.com/pingam/8.1/a.md)\n\n"
            "## B 7.5\n\n"
            "- [B](https://docs.pingidentity.com/pingam/7.5/b.md)\n"
        )
        result = prune_llms_text(text, "https://docs.pingidentity.com/pingam", "8.1")
        self.assertTrue(result.endswith("## B 7.5\n\n"))


if __name__ == "__main__":
    unittest.main()
