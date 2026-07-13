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

    def test_ping_docs_html_and_markdown_urls_are_equivalent(self) -> None:
        markdown = "https://docs.pingidentity.com/pingauthorize/11.1/guide/page.md"
        html = "http://DOCS.PINGIDENTITY.COM/pingauthorize/11.1/guide/page.html?view=latest#section"
        self.assertEqual(pilot_score.normalize_url(markdown), pilot_score.normalize_url(html))
        self.assertNotEqual(
            pilot_score.normalize_url("https://example.com/guide/page.md"),
            pilot_score.normalize_url("https://example.com/guide/page.html"),
        )

    def test_protocol_requires_exact_staged_skills_and_sandbox_metadata(self) -> None:
        skills_dir = Path("/isolated/pilot/skills")
        staged = ["ping-docs", "ping-foundation"]
        metadata = {
            "condition_id": "B",
            "loaded_skill_roots": [str(skills_dir)],
            "loaded_skills": list(reversed(staged)),
            "filesystem_sandbox": True,
        }
        verified, issues = pilot_run.verify_protocol(
            metadata, "B", skills_dir, staged, True, True
        )
        self.assertTrue(verified, issues)

        metadata["loaded_skills"] = ["ping-foundation", "unexpected"]
        metadata["filesystem_sandbox"] = False
        verified, issues = pilot_run.verify_protocol(
            metadata, "B", skills_dir, staged, True, True
        )
        self.assertFalse(verified)
        self.assertTrue(any("exactly match" in issue for issue in issues))
        self.assertIn("metadata filesystem_sandbox must be true", issues)

    def test_scorer_reports_numeric_coverage_and_builtin_inventory_mismatch(self) -> None:
        case = pilot_run.load_json(EVALS_DIR / "cases.json")["cases"][0]

        def scored(condition: str, metadata: dict[str, object]) -> dict[str, object]:
            return pilot_score.score_record(
                {
                    "run_id": "r",
                    "condition": {"id": condition},
                    "case": {"id": case["id"]},
                    "attempt": 1,
                    "exit_code": 0,
                    "timed_out": False,
                    "elapsed_seconds": 1.0,
                    "protocol": {"isolation_verified": True},
                    "agent_metadata": metadata,
                    "stdout": "A non-empty response.",
                },
                case,
            )

        summary = pilot_score.aggregate(
            [
                scored(
                    "A",
                    {
                        "tool_calls": 2,
                        "cost_usd": 0.25,
                        "runtime_builtin_skills": ["provider-help"],
                    },
                ),
                scored(
                    "B",
                    {
                        "tool_calls": 3,
                        "runtime_builtin_skills": ["provider-help", "provider-search"],
                    },
                ),
            ],
            {},
        )
        self.assertEqual(
            {"records": 1, "rate": 1.0},
            summary["conditions"]["A"]["agent_numeric_metadata_coverage"]["cost_usd"],
        )
        self.assertEqual(
            {"records": 0, "rate": 0.0},
            summary["conditions"]["B"]["agent_numeric_metadata_coverage"]["cost_usd"],
        )
        self.assertTrue(summary["runtime_builtin_skills_comparison"]["comparable"])
        self.assertFalse(
            summary["runtime_builtin_skills_comparison"]["identical_across_conditions"]
        )

    def test_revised_pingauthorize_gold_accepts_task_specific_html_citations(self) -> None:
        cases = pilot_run.load_json(EVALS_DIR / "cases.json")["cases"]
        case = next(item for item in cases if item["id"] == "paz-conditional-redaction")
        result = {
            "run_id": "r",
            "condition": {"id": "B"},
            "case": {"id": case["id"]},
            "attempt": 1,
            "exit_code": 0,
            "timed_out": False,
            "elapsed_seconds": 1.0,
            "protocol": {"isolation_verified": True},
            "agent_metadata": {},
            "stdout": """
Permit both callers, but remove the fields for the non-investigator group and test both paths.
https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_sec_gw_request_response_flow.html
https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/paz_create_policy_modify.html
https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_api_security_gw_policy_reqs.html
""",
        }
        row = pilot_score.score_record(result, case)
        self.assertEqual(
            {
                "gateway-outbound-processing": True,
                "response-redaction-statement": True,
                "verification": True,
            },
            row["gold_group_hits"],
        )
        self.assertEqual(1.0, row["gold_group_recall"])
        self.assertTrue(row["citation_policy_pass"])

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
            (deep / "SKILL.md").write_text(
                "---\nname: ping-docs\n---\n# deep docs\n", encoding="utf-8"
            )
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
            self.assertEqual(
                sorted([*OFFICIAL_SKILLS, "ping-docs"]),
                next(
                    record["protocol"]["expected_loaded_skills"]
                    for record in records
                    if record["condition"]["id"] == "B"
                ),
            )

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
            self.assertEqual(
                1.0,
                summary["conditions"]["A"]["agent_metadata_means"]["tool_calls"],
            )
            self.assertEqual(
                140.0,
                summary["conditions"]["B"]["agent_metadata_means"]["total_tokens"],
            )
            self.assertEqual(
                {"records": 1, "rate": 1.0},
                summary["conditions"]["A"]["agent_numeric_metadata_coverage"]["tool_calls"],
            )
            self.assertEqual(
                {"records": 0, "rate": 0.0},
                summary["conditions"]["A"]["agent_numeric_metadata_coverage"]["cost_usd"],
            )
            self.assertTrue(summary["runtime_builtin_skills_comparison"]["comparable"])
            self.assertTrue(
                summary["runtime_builtin_skills_comparison"]["identical_across_conditions"]
            )
            self.assertIn(
                "## Agent efficiency",
                (run_dir / "report" / "report.md").read_text(encoding="utf-8"),
            )
            report = (run_dir / "report" / "report.md").read_text(encoding="utf-8")
            self.assertIn("## Agent metadata coverage", report)
            self.assertIn("Inventories identical across A/B: **yes**", report)
            self.assertTrue((run_dir / "report" / "sme-review-key.csv").exists())


if __name__ == "__main__":
    unittest.main()
