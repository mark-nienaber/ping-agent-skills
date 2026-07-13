#!/usr/bin/env python3
"""Score deterministic and optional SME metrics for a completed pilot run."""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
import re
import statistics
import sys
from typing import Any, Iterable
from urllib.parse import urlsplit, urlunsplit


EVALS_DIR = Path(__file__).resolve().parent
DEFAULT_CASES = EVALS_DIR / "cases.json"
URL_RE = re.compile(r"https?://[^\s<>()\[\]{}\"']+", re.IGNORECASE)
PING_DOC_HOSTS = {"docs.pingidentity.com", "developer.pingidentity.com"}
SME_DIMENSIONS = ("correctness", "completeness", "evidence", "safety", "actionability")


class ScoreError(RuntimeError):
    """Raised for invalid score inputs."""


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ScoreError(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ScoreError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ScoreError(f"Expected a JSON object in {path}")
    return value


def normalize_url(raw: str) -> str:
    raw = raw.rstrip(".,;:!?`*_~)")
    parts = urlsplit(raw)
    scheme = "https" if parts.scheme.lower() in {"http", "https"} else parts.scheme.lower()
    host = (parts.hostname or "").lower()
    port = parts.port
    netloc = host
    if port and not ((scheme == "https" and port == 443) or (scheme == "http" and port == 80)):
        netloc = f"{host}:{port}"
    path = re.sub(r"/{2,}", "/", parts.path)
    if path != "/":
        path = path.rstrip("/")
    return urlunsplit((scheme, netloc, path, "", ""))


def extract_urls(text: str) -> list[str]:
    seen: set[str] = set()
    urls: list[str] = []
    for match in URL_RE.findall(text):
        normalized = normalize_url(match)
        if normalized not in seen:
            seen.add(normalized)
            urls.append(normalized)
    return urls


def is_ping_doc(url: str) -> bool:
    return (urlsplit(url).hostname or "").lower() in PING_DOC_HOSTS


def patterns_pass(text: str, patterns: list[str], require_all: bool) -> bool:
    if not patterns:
        return False
    matches = [re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE) is not None for pattern in patterns]
    return all(matches) if require_all else any(matches)


def metric_mean(values: Iterable[float | int | None]) -> float | None:
    present = [float(value) for value in values if value is not None]
    return round(statistics.fmean(present), 6) if present else None


def percentile(values: Iterable[float | int], percentile_value: float) -> float | None:
    ordered = sorted(float(value) for value in values)
    if not ordered:
        return None
    index = max(0, math.ceil(percentile_value * len(ordered)) - 1)
    return round(ordered[index], 6)


def numeric_metadata(metadata: Any) -> dict[str, float]:
    if not isinstance(metadata, dict):
        return {}
    result: dict[str, float] = {}
    for key in ("tool_calls", "input_tokens", "output_tokens", "total_tokens", "cached_tokens", "cost_usd"):
        value = metadata.get(key)
        if key == "tool_calls" and isinstance(value, list):
            result[key] = float(len(value))
        elif isinstance(value, (int, float)) and not isinstance(value, bool):
            result[key] = float(value)
    if "tool_calls" not in result and isinstance(metadata.get("tools"), list):
        result["tool_calls"] = float(len(metadata["tools"]))
    return result


def score_record(result: dict[str, Any], case: dict[str, Any]) -> dict[str, Any]:
    answer_key = case["answer_key"]
    text = str(result.get("stdout", ""))
    urls = extract_urls(text)
    ping_doc_urls = [url for url in urls if is_ping_doc(url)]
    groups = answer_key.get("gold_source_groups", [])
    group_hits: dict[str, bool] = {}
    gold_urls: set[str] = set()
    for group in groups:
        acceptable = {normalize_url(str(url)) for url in group.get("urls", [])}
        gold_urls.update(acceptable)
        group_hits[str(group.get("id"))] = bool(acceptable.intersection(urls))
    gold_recall = metric_mean(int(hit) for hit in group_hits.values()) if group_hits else None
    gold_citations = [url for url in urls if url in gold_urls]
    gold_precision = len(gold_citations) / len(ping_doc_urls) if ping_doc_urls else None

    fact_results: dict[str, bool] = {}
    for check in answer_key.get("fact_checks", []):
        fact_results[str(check.get("id"))] = patterns_pass(text, list(check.get("patterns", [])), require_all=True)
    fact_recall = metric_mean(int(hit) for hit in fact_results.values()) if fact_results else None

    behavior_results: dict[str, bool] = {}
    for check in answer_key.get("behavior_checks", []):
        behavior_results[str(check.get("id"))] = patterns_pass(
            text, list(check.get("patterns", [])), require_all=False
        )
    behavior_score = metric_mean(int(hit) for hit in behavior_results.values()) if behavior_results else None

    citation_policy = answer_key.get("citation_policy")
    if citation_policy == "gold":
        citation_policy_pass: bool | None = bool(group_hits) and all(group_hits.values())
    elif citation_policy == "no_ping_docs":
        citation_policy_pass = not ping_doc_urls
    else:
        citation_policy_pass = None

    protocol = result.get("protocol") or {}
    execution_success = (
        result.get("exit_code") == 0
        and not result.get("timed_out")
        and bool(text.strip())
        and bool(protocol.get("isolation_verified", True))
    )
    row = {
        "run_id": result.get("run_id"),
        "condition": result.get("condition", {}).get("id"),
        "case_id": case["id"],
        "case_type": case.get("case_type"),
        "product": case.get("product"),
        "attempt": result.get("attempt"),
        "execution_success": execution_success,
        "exit_code": result.get("exit_code"),
        "timed_out": bool(result.get("timed_out")),
        "isolation_verified": bool(protocol.get("isolation_verified", False)),
        "elapsed_seconds": result.get("elapsed_seconds"),
        "citation_count": len(urls),
        "ping_doc_citation_count": len(ping_doc_urls),
        "gold_group_recall": gold_recall,
        "gold_citation_precision": round(gold_precision, 6) if gold_precision is not None else None,
        "citation_policy_pass": citation_policy_pass,
        "fact_coverage_heuristic": fact_recall,
        "behavior_heuristic": behavior_score,
        "gold_group_hits": group_hits,
        "fact_check_hits": fact_results,
        "behavior_check_hits": behavior_results,
        "cited_urls": urls,
        "metadata": numeric_metadata(result.get("agent_metadata")),
        "prompt": case.get("prompt", ""),
        "response_text": text,
    }
    return row


def read_results(run_dir: Path) -> list[dict[str, Any]]:
    jsonl = run_dir / "results.jsonl"
    results: list[dict[str, Any]] = []
    if jsonl.exists():
        for line_number, line in enumerate(jsonl.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ScoreError(f"Invalid JSON at {jsonl}:{line_number}: {exc}") from exc
            if isinstance(value, dict):
                results.append(value)
    else:
        for path in sorted((run_dir / "records").glob("*/*/attempt-*/result.json")):
            results.append(load_json(path))
    if not results:
        raise ScoreError(f"No result records found in {run_dir}")
    return results


def response_id(row: dict[str, Any]) -> str:
    import hashlib

    raw = f"{row['run_id']}|{row['condition']}|{row['case_id']}|{row['attempt']}"
    return "r-" + hashlib.sha256(raw.encode("utf-8")).hexdigest()[:12]


def load_sme_reviews(
    path: Path | None, rows: list[dict[str, Any]]
) -> dict[tuple[str, str, int], dict[str, Any]]:
    if path is None:
        return {}
    reviews: dict[tuple[str, str, int], dict[str, Any]] = {}
    blind_lookup = {response_id(row): (str(row["condition"]), str(row["case_id"]), int(row["attempt"])) for row in rows}
    with path.open(newline="", encoding="utf-8") as handle:
        for row_number, row in enumerate(csv.DictReader(handle), 2):
            try:
                if (row.get("response_id") or "").strip():
                    key = blind_lookup[row["response_id"].strip()]
                else:
                    key = (row["condition"], row["case_id"], int(row["attempt"]))
            except (KeyError, TypeError, ValueError) as exc:
                raise ScoreError(f"Invalid SME review key on CSV row {row_number}") from exc
            for dimension in SME_DIMENSIONS:
                raw = (row.get(dimension) or "").strip()
                if raw:
                    try:
                        score = float(raw)
                    except ValueError as exc:
                        raise ScoreError(f"Invalid {dimension} score on CSV row {row_number}: {raw}") from exc
                    if not 0 <= score <= 4:
                        raise ScoreError(f"{dimension} must be between 0 and 4 on CSV row {row_number}")
                    row[dimension] = score
                else:
                    row[dimension] = None
            reviews[key] = row
    return reviews


def aggregate(rows: list[dict[str, Any]], reviews: dict[tuple[str, str, int], dict[str, Any]]) -> dict[str, Any]:
    by_condition: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        by_condition.setdefault(str(row["condition"]), []).append(row)

    conditions: dict[str, Any] = {}
    for condition, condition_rows in sorted(by_condition.items()):
        latencies = [float(row["elapsed_seconds"]) for row in condition_rows if row["elapsed_seconds"] is not None]
        metrics: dict[str, Any] = {
            "records": len(condition_rows),
            "execution_success_rate": metric_mean(int(row["execution_success"]) for row in condition_rows),
            "isolation_verified_rate": metric_mean(int(row["isolation_verified"]) for row in condition_rows),
            "gold_group_recall": metric_mean(row["gold_group_recall"] for row in condition_rows),
            "gold_citation_precision": metric_mean(row["gold_citation_precision"] for row in condition_rows),
            "citation_policy_pass_rate": metric_mean(
                int(row["citation_policy_pass"]) if row["citation_policy_pass"] is not None else None
                for row in condition_rows
            ),
            "fact_coverage_heuristic": metric_mean(row["fact_coverage_heuristic"] for row in condition_rows),
            "behavior_heuristic": metric_mean(row["behavior_heuristic"] for row in condition_rows),
            "latency_median_seconds": round(statistics.median(latencies), 6) if latencies else None,
            "latency_p95_seconds": percentile(latencies, 0.95),
        }
        metadata_keys = sorted({key for row in condition_rows for key in row["metadata"]})
        metrics["agent_metadata_means"] = {
            key: metric_mean(row["metadata"].get(key) for row in condition_rows) for key in metadata_keys
        }
        reviewed = []
        for row in condition_rows:
            key = (condition, row["case_id"], int(row["attempt"]))
            if key in reviews:
                reviewed.append(reviews[key])
        metrics["sme_review_count"] = len(reviewed)
        metrics["sme_means"] = {
            dimension: metric_mean(review.get(dimension) for review in reviewed) for dimension in SME_DIMENSIONS
        }
        conditions[condition] = metrics

    condition_ids = sorted(conditions)
    comparison: dict[str, Any] = {}
    if len(condition_ids) == 2:
        baseline, treatment = condition_ids
        comparable = (
            "execution_success_rate",
            "gold_group_recall",
            "gold_citation_precision",
            "citation_policy_pass_rate",
            "fact_coverage_heuristic",
            "behavior_heuristic",
            "latency_median_seconds",
            "latency_p95_seconds",
        )
        deltas: dict[str, float | None] = {}
        for metric in comparable:
            a = conditions[baseline].get(metric)
            b = conditions[treatment].get(metric)
            deltas[metric] = round(b - a, 6) if a is not None and b is not None else None
        comparison = {"baseline": baseline, "treatment": treatment, "treatment_minus_baseline": deltas}

    return {"conditions": conditions, "comparison": comparison}


def write_case_scores(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "run_id", "condition", "case_id", "case_type", "product", "attempt", "execution_success",
        "exit_code", "timed_out", "isolation_verified", "elapsed_seconds", "citation_count",
        "ping_doc_citation_count", "gold_group_recall", "gold_citation_precision", "citation_policy_pass",
        "fact_coverage_heuristic", "behavior_heuristic", "gold_group_hits", "fact_check_hits",
        "behavior_check_hits", "cited_urls", "metadata",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: json.dumps(row[key], sort_keys=True) if isinstance(row[key], (dict, list)) else row[key] for key in fields})


def write_sme_packets(
    review_path: Path,
    key_path: Path,
    rows: list[dict[str, Any]],
    reviews: dict[tuple[str, str, int], dict[str, Any]],
) -> None:
    review_fields = ["response_id", "case_id", "prompt", "response", *SME_DIMENSIONS, "reviewer", "notes"]
    key_fields = ["response_id", "run_id", "condition", "case_id", "attempt"]
    blinded_rows = sorted(rows, key=response_id)
    with review_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=review_fields)
        writer.writeheader()
        for row in blinded_rows:
            key = (str(row["condition"]), str(row["case_id"]), int(row["attempt"]))
            existing = reviews.get(key, {})
            writer.writerow(
                {
                    "response_id": response_id(row),
                    "case_id": row["case_id"],
                    "prompt": row["prompt"],
                    "response": row["response_text"],
                    **{dimension: existing.get(dimension, "") if existing.get(dimension) is not None else "" for dimension in SME_DIMENSIONS},
                    "reviewer": existing.get("reviewer", ""),
                    "notes": existing.get("notes", ""),
                }
            )
    with key_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=key_fields)
        writer.writeheader()
        for row in blinded_rows:
            writer.writerow(
                {
                    "response_id": response_id(row),
                    "run_id": row["run_id"],
                    "condition": row["condition"],
                    "case_id": row["case_id"],
                    "attempt": row["attempt"],
                }
            )


def display(value: Any) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value)


def render_report(summary: dict[str, Any], rows: list[dict[str, Any]]) -> str:
    conditions = summary["conditions"]
    lines = [
        "# Ping Agent Skills A/B pilot report",
        "",
        "Deterministic scores measure execution, cited gold-page recall, citation policy, latency, and explicitly labelled answer-text heuristics. They do not replace SME scoring.",
        "",
        "## Condition summary",
        "",
        "| Metric | " + " | ".join(sorted(conditions)) + " |",
        "|---|" + "---|" * len(conditions),
    ]
    metrics = [
        ("Records", "records"),
        ("Execution success rate", "execution_success_rate"),
        ("Isolation verified rate", "isolation_verified_rate"),
        ("Gold source-group recall", "gold_group_recall"),
        ("Gold citation precision (diagnostic)", "gold_citation_precision"),
        ("Citation policy pass rate", "citation_policy_pass_rate"),
        ("Fact coverage heuristic", "fact_coverage_heuristic"),
        ("Clarification behavior heuristic", "behavior_heuristic"),
        ("Median latency (seconds)", "latency_median_seconds"),
        ("P95 latency (seconds)", "latency_p95_seconds"),
        ("SME-reviewed records", "sme_review_count"),
    ]
    for label, key in metrics:
        lines.append(f"| {label} | " + " | ".join(display(conditions[c].get(key)) for c in sorted(conditions)) + " |")

    comparison = summary.get("comparison", {})
    if comparison:
        lines.extend(["", "## Treatment minus baseline", ""])
        lines.append(f"Baseline: `{comparison['baseline']}`. Treatment: `{comparison['treatment']}`.")
        lines.extend(["", "| Metric | Delta |", "|---|---:|"])
        for key, value in comparison["treatment_minus_baseline"].items():
            lines.append(f"| {key.replace('_', ' ')} | {display(value)} |")

    lines.extend(["", "## Case-level deterministic results", ""])
    lines.extend([
        "| Condition | Case | Attempt | Success | Gold recall | Citation policy | Fact heuristic | Behavior heuristic | Seconds |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for row in sorted(rows, key=lambda item: (item["case_id"], item["attempt"], item["condition"])):
        lines.append(
            f"| {row['condition']} | {row['case_id']} | {row['attempt']} | "
            f"{int(row['execution_success'])} | {display(row['gold_group_recall'])} | "
            f"{display(row['citation_policy_pass'])} | {display(row['fact_coverage_heuristic'])} | "
            f"{display(row['behavior_heuristic'])} | {display(row['elapsed_seconds'])} |"
        )

    lines.extend([
        "",
        "## Interpretation guardrails",
        "",
        "- Treat fact and behavior regex scores as triage signals only; an SME must assess technical correctness and completeness.",
        "- Gold citation precision is diagnostic because a correct answer may cite useful, non-gold supporting pages.",
        "- Do not publish comparisons when isolation verification is below 100% in either condition.",
        "- Compare repeated paired cases and inspect failures; aggregate means alone can conceal product-specific regressions.",
        "",
    ])
    return "\n".join(lines)


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--cases-file", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--sme-reviews", type=Path)
    parser.add_argument("--output", type=Path)
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        run_dir = args.run_dir.absolute()
        cases_doc = load_json(args.cases_file.absolute())
        cases = {case["id"]: case for case in cases_doc.get("cases", [])}
        results = read_results(run_dir)
        rows: list[dict[str, Any]] = []
        for result in results:
            case_id = result.get("case", {}).get("id")
            if case_id not in cases:
                raise ScoreError(f"Result refers to unknown case: {case_id}")
            rows.append(score_record(result, cases[case_id]))
        reviews = load_sme_reviews(args.sme_reviews.absolute() if args.sme_reviews else None, rows)
        summary = aggregate(rows, reviews)
        summary.update(
            {
                "schema_version": 1,
                "run_id": results[0].get("run_id"),
                "record_count": len(rows),
                "case_count": len({row["case_id"] for row in rows}),
            }
        )

        output = (args.output or (run_dir / "report")).absolute()
        output.mkdir(parents=True, exist_ok=True)
        (output / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        write_case_scores(output / "case-scores.csv", rows)
        write_sme_packets(output / "sme-reviews.csv", output / "sme-review-key.csv", rows, reviews)
        (output / "report.md").write_text(render_report(summary, rows), encoding="utf-8")
        print(json.dumps({"report_dir": str(output), "records": len(rows)}, indent=2))
        return 0
    except (ScoreError, OSError, re.error) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
