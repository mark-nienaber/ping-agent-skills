from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
ADAPTER = ROOT / "evals" / "adapters" / "claude_code.py"
SPEC = importlib.util.spec_from_file_location("claude_code_adapter", ADAPTER)
assert SPEC and SPEC.loader
claude_code = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(claude_code)


class ClaudeAdapterTests(unittest.TestCase):
    def test_discovers_only_skill_directories(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            first = root / "nested" / "first"
            second = root / "second"
            first.mkdir(parents=True)
            second.mkdir()
            (first / "SKILL.md").write_text("---\nname: alpha\n---\n", encoding="utf-8")
            (second / "SKILL.md").write_text("---\nname: beta\n---\n", encoding="utf-8")
            (root / "not-a-skill.md").write_text("ignored\n", encoding="utf-8")

            found = claude_code.discover_skills(root)

            self.assertEqual([name for name, _ in found], ["alpha", "beta"])

    def test_sums_usage_across_runtime_models(self) -> None:
        usage = {
            "router": {"inputTokens": 10, "outputTokens": 2},
            "answer": {"inputTokens": 20, "outputTokens": 4},
        }

        self.assertEqual(claude_code.sum_model_usage(usage, "inputTokens"), 30)
        self.assertEqual(claude_code.sum_model_usage(usage, "outputTokens"), 6)

    def test_condition_skill_inventory_is_exact(self) -> None:
        baseline = claude_code.expected_skill_names("A")
        treatment = claude_code.expected_skill_names("B")

        self.assertEqual(6, len(baseline))
        self.assertNotIn("ping-docs", baseline)
        self.assertEqual(baseline | {"ping-docs"}, treatment)
        with self.assertRaises(ValueError):
            claude_code.expected_skill_names("unknown")

    def test_environment_is_allowlisted_and_provider_secrets_are_redacted(self) -> None:
        source = {
            "PATH": "/bin",
            "AWS_BEARER_TOKEN_BEDROCK": "bedrock-secret-value",
            "PILOT_CASE_FILE": "/hidden/answer-key.json",
            "UNRELATED_SECRET": "must-not-pass",
        }

        filtered = claude_code.filtered_environment(source)

        self.assertEqual({"PATH", "AWS_BEARER_TOKEN_BEDROCK"}, set(filtered))
        self.assertEqual(
            "credential=[REDACTED:AWS_BEARER_TOKEN_BEDROCK]",
            claude_code.redacted(
                "credential=bedrock-secret-value",
                filtered,
            ),
        )

    def test_settings_fail_closed_and_deny_host_home(self) -> None:
        settings = claude_code.build_claude_settings(
            Path("/Users/example"),
            ("/tmp", "/Users/example"),
        )
        sandbox = settings["sandbox"]
        permissions = settings["permissions"]

        self.assertTrue(sandbox["enabled"])
        self.assertTrue(sandbox["failIfUnavailable"])
        self.assertFalse(sandbox["allowUnsandboxedCommands"])
        self.assertEqual(["."], sandbox["filesystem"]["allowRead"])
        self.assertIn("Read(//Users/example/**)", permissions["deny"])
        self.assertIn("Read", permissions["allow"])


if __name__ == "__main__":
    unittest.main()
