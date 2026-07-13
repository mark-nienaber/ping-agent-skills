from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


EVALS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EVALS_DIR))

import run as pilot_run  # noqa: E402
import score as pilot_score  # noqa: E402


OFFICIAL_SKILLS = (
    "ping-quickstart",
    "ping-foundation",
    "ping-app-integration",
    "ping-orchestration",
    "ping-universal-services",
    "ping-identity-for-ai",
)


class PilotHarnessTest(unittest.TestCase):
    def test_suite_has_fifteen_natural_cases_and_control_cases(self) -> None:
        cases_doc = pilot_run.load_json(EVALS_DIR / "cases.json")
        pilot_run.validate_inputs(pilot_run.load_json(EVALS_DIR / "pilot.json"), cases_doc)
        cases = cases_doc["cases"]
        self.assertEqual(15, len(cases))
        self.assertIn("ambiguous", {case["case_type"] for case in cases})
        self.assertIn("out_of_domain", {case["case_type"] for case in cases})
        for case in cases:
            self.assertNotRegex(case["prompt"].lower(), r"\b(use|load|invoke)\b.{0,20}\bskill\b")

    def test_url_normalization_and_gold_group_scoring(self) -> None:
        self.assertEqual(
            "https://docs.pingidentity.com/path/page.md",
            pilot_score.normalize_url("http://DOCS.PINGIDENTITY.COM/path/page.md?x=1#part"),
        )
        case = {
            "id": "x",
            "prompt": "test",
            "answer_key": {
                "expected_behavior": "answer",
                "citation_policy": "gold",
                "gold_source_groups": [{"id": "g", "urls": ["https://docs.pingidentity.com/x.md"]}],
                "fact_checks": [{"id": "f", "patterns": ["safe", "verify"]}],
            },
        }
        result = {
            "run_id": "r",
            "condition": {"id": "A"},
            "case": {"id": "x"},
            "attempt": 1,
            "exit_code": 0,
            "timed_out": False,
            "elapsed_seconds": 1.0,
            "stdout": "A safe step. Verify it. https://docs.pingidentity.com/x.md",
            "protocol": {"isolation_verified": True},
            "agent_metadata": {"tool_calls": ["fetch"]},
        }
        row = pilot_score.score_record(result, case)
        self.assertEqual(1.0, row["gold_group_recall"])
        self.assertEqual(1.0, row["fact_coverage_heuristic"])
        self.assertTrue(row["execution_success"])
        self.assertEqual(1.0, row["metadata"]["tool_calls"])

    def test_end_to_end_runner_and_report(self) -> None:
        with tempfile.TemporaryDirectory() as raw_tmp:
            tmp = Path(raw_tmp)
            umbrella = tmp / "umbrella"
            umbrella.mkdir()
            for name in OFFICIAL_SKILLS:
                skill = umbrella / name
                skill.mkdir()
                (skill / "SKILL.md").write_text(f"# {name}\n", encoding="utf-8")
            deep = tmp / "deep"
            deep.mkdir()
            (deep / "SKILL.md").write_text("# deep docs\n", encoding="utf-8")
            results = tmp / "results"
            env = os.environ.copy()
            env["PING_UMBRELLA_SKILLS_DIR"] = str(umbrella)
            env["PING_DEEP_DOC_LAYER_DIR"] = str(deep)
            command = f"{sys.executable} {EVALS_DIR / 'tests' / 'mock_agent.py'}"
            completed = subprocess.run(
                [
                    sys.executable,
                    str(EVALS_DIR / "run.py"),
                    "--output",
                    str(results),
                    "--run-id",
                    "test-run",
                    "--agent-command",
                    command,
                    "--case",
                    "pingid-device-switch",
                    "--repetitions",
                    "1",
                    "--jobs",
                    "2",
                    "--discard-workspaces",
                ],
                cwd=EVALS_DIR.parent,
                env=env,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(0, completed.returncode, completed.stderr + completed.stdout)
            run_dir = results / "test-run"
            records = [json.loads(line) for line in (run_dir / "results.jsonl").read_text().splitlines()]
            self.assertEqual(2, len(records))
            self.assertTrue(all(record["protocol"]["isolation_verified"] for record in records))

            scored = subprocess.run(
                [sys.executable, str(EVALS_DIR / "score.py"), str(run_dir)],
                cwd=EVALS_DIR.parent,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(0, scored.returncode, scored.stderr + scored.stdout)
            summary = json.loads((run_dir / "report" / "summary.json").read_text())
            self.assertEqual(2, summary["record_count"])
            self.assertEqual(1.0, summary["conditions"]["A"]["gold_group_recall"])
            self.assertTrue((run_dir / "report" / "sme-review-key.csv").exists())


if __name__ == "__main__":
    unittest.main()
