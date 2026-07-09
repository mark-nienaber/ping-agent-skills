#!/usr/bin/env python3
"""Show deterministic routing proof for representative Ping documentation questions."""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
import re
from urllib.parse import urlparse

from ping_docsets import (
    Docset,
    GuideCluster,
    LlmEntry,
    STOPWORDS,
    cluster_entries,
    detect_latest_version,
    humanize_slug,
    load_docsets,
    parse_llms_file,
    routing_url_pattern,
    task_category,
)


EXTRA_STOPWORDS = {
    "about",
    "across",
    "after",
    "before",
    "build",
    "can",
    "complex",
    "configure",
    "configured",
    "configuring",
    "detailed",
    "guidance",
    "guide",
    "help",
    "need",
    "needs",
    "product",
    "production",
    "question",
    "questions",
    "should",
    "through",
    "when",
}


PRODUCT_ALIASES = {
    "openicf": (
        "connector framework",
        "icf",
        "ldap connector",
        "openicf",
        "rcs",
        "remote connector server",
    ),
    "pingoneaic": ("aic", "advanced identity cloud", "pingone advanced identity cloud"),
    "pingone-api": ("pingone api", "platform api", "pingone platform api"),
    "pingone-api-ea": ("early access api", "pingone early access"),
    "pingid-api": ("pingid api",),
    "java-agents": ("java agent", "java agents"),
    "web-agents": ("web agent", "web agents"),
}


@dataclass(frozen=True)
class Sample:
    name: str
    question: str
    expected_skill: str
    expected_guide: str


@dataclass(frozen=True)
class SkillRoute:
    docset: Docset
    skill_score: int
    guide: GuideCluster
    guide_score: int
    entry: LlmEntry
    entry_score: int
    route_pattern: str
    snapshot: str
    matched_skill_terms: tuple[str, ...]
    matched_guide_terms: tuple[str, ...]
    matched_entry_terms: tuple[str, ...]


SAMPLES = (
    Sample(
        name="pingam-auth-tree-callbacks",
        question=(
            "In PingAM, how do I create and configure authentication trees with "
            "callbacks, custom scripted nodes, webhooks, and REST-based "
            "authentication behavior?"
        ),
        expected_skill="pingam",
        expected_guide="am-authentication",
    ),
    Sample(
        name="davinci-subflows-variables-debugging",
        question=(
            "In DaVinci, how should I structure reusable sign-on flows with "
            "subflows, shared variables, connector outcomes, debugging analytics, "
            "and safe handling of sensitive data?"
        ),
        expected_skill="davinci",
        expected_guide="davinci_best_practices",
    ),
    Sample(
        name="pingfederate-sdk-oauth-adapters",
        question=(
            "For PingFederate, where do I look for building custom authentication "
            "adapters and SDK extensions that participate in OAuth or OIDC flows "
            "and expose the right attributes?"
        ),
        expected_skill="pingfederate",
        expected_guide="sdk_developers_guide",
    ),
    Sample(
        name="pingdirectory-replication-tls-backup",
        question=(
            "For PingDirectory, how do I plan replication with TLS certificates, "
            "server administration, access control, backups, monitoring, and "
            "operational recovery?"
        ),
        expected_skill="pingdirectory",
        expected_guide="pingdirectory_server_administration_guide",
    ),
    Sample(
        name="pingaccess-zero-downtime-app-upgrade",
        question=(
            "For PingAccess, how do I upgrade without downtime while preserving "
            "applications, sites, rules, token providers, web sessions, and agent "
            "integrations?"
        ),
        expected_skill="pingaccess",
        expected_guide="pingaccess_zero_downtime_upgrade",
    ),
    Sample(
        name="pingone-oidc-auth-policy-application",
        question=(
            "In PingOne, configure an OIDC web application with a custom "
            "authentication policy that uses identifier-first login, an external "
            "OIDC identity provider sign-on step, MFA, terms of service, and "
            "then apply the policy to the application."
        ),
        expected_skill="pingone",
        expected_guide="applications",
    ),
    Sample(
        name="pingone-authorize-oauth-policy",
        question=(
            "In PingOne, configure PingOne Authorize for API access management "
            "with a worker application, external OAuth server, decision endpoint, "
            "custom authorization attributes, resolvers, value processors, "
            "statements, and policy testing."
        ),
        expected_skill="pingone",
        expected_guide="authorization_using_pingone_authorize",
    ),
    Sample(
        name="aic-auth-journey-oauth-scripting",
        question=(
            "In PingOne Advanced Identity Cloud, create an authentication journey "
            "with custom scripted decision nodes and OAuth2 or OIDC custom "
            "scripting: access token modification scripts, authorize endpoint "
            "data provider scripts, OIDC claims scripts, and shared library "
            "scripts."
        ),
        expected_skill="pingoneaic",
        expected_guide="am-scripting",
    ),
    Sample(
        name="aic-rcs-ldap-ds-truststore",
        question=(
            "Hi - tearing my hair out on a problem with RCS in AIC. LDAP "
            "connector does not trust the DS certificate - cannot find validation "
            "path. Logs show RCS loading the correct truststore, and the "
            "truststore has the correct root CA for the DS certificate. openssl "
            "s_client verifies what DS is presenting. Any tips for troubleshooting "
            "beyond this?"
        ),
        expected_skill="openicf",
        expected_guide="connector-reference",
    ),
)


def tokenize(text: str) -> Counter[str]:
    tokens: Counter[str] = Counter()
    for token in re.findall(r"[a-z][a-z0-9]+", text.lower()):
        if token in STOPWORDS or token in EXTRA_STOPWORDS:
            continue
        tokens[token] += 1
    return tokens


def weighted_tokens(*weighted_texts: tuple[str, int]) -> Counter[str]:
    tokens: Counter[str] = Counter()
    for text, weight in weighted_texts:
        for token, count in tokenize(text).items():
            tokens[token] += count * weight
    return tokens


def weighted_token_set(*weighted_texts: tuple[str, int]) -> Counter[str]:
    tokens: Counter[str] = Counter()
    for text, weight in weighted_texts:
        for token in tokenize(text):
            tokens[token] = max(tokens[token], weight)
    return tokens


def overlap_score(query_tokens: Counter[str], corpus_tokens: Counter[str]) -> int:
    return sum(query_tokens[token] * corpus_tokens[token] for token in query_tokens)


def matched_terms(query_tokens: Counter[str], corpus_tokens: Counter[str]) -> tuple[str, ...]:
    terms = [token for token in query_tokens if corpus_tokens[token] > 0]
    terms.sort(key=lambda token: (-corpus_tokens[token], token))
    return tuple(terms[:8])


def phrase_bonus(query: str, docset: Docset) -> int:
    normalized = query.lower()
    phrases = {
        docset.skill_slug.replace("-", " "),
        docset.skill_slug,
        docset.label.lower(),
    }
    phrases.update(PRODUCT_ALIASES.get(docset.skill_slug, ()))
    return sum(80 for phrase in phrases if phrase and phrase in normalized)


def rel_url_path(url: str) -> str:
    return urlparse(url).path.replace("/", " ")


def skill_description(skill_dir: Path) -> str:
    skill_path = skill_dir / "SKILL.md"
    if not skill_path.exists():
        return ""
    text = skill_path.read_text(encoding="utf-8")
    match = re.search(r'^description:\s*["\']?(.*?)["\']?$', text, flags=re.MULTILINE)
    return match.group(1) if match else ""


def choose_skill(
    query: str,
    query_tokens: Counter[str],
    docsets: list[Docset],
    skills_root: Path,
) -> tuple[Docset, int, tuple[str, ...]]:
    best: tuple[int, Docset, Counter[str]] | None = None
    for docset in docsets:
        skill_dir = skills_root / docset.skill_slug
        description = skill_description(skill_dir)
        corpus = weighted_tokens(
            (docset.label, 12),
            (docset.skill_slug.replace("-", " "), 12),
            (description, 3),
        )
        score = overlap_score(query_tokens, corpus) + phrase_bonus(query, docset)
        if best is None or score > best[0]:
            best = (score, docset, corpus)
    if best is None:
        raise ValueError("no enabled docsets available")
    score, docset, corpus = best
    return docset, score, matched_terms(query_tokens, corpus)


def choose_guide(
    query_tokens: Counter[str],
    clusters: list[GuideCluster],
) -> tuple[GuideCluster, int, tuple[str, ...]]:
    best: tuple[int, GuideCluster, Counter[str]] | None = None
    for cluster in clusters:
        entry_text = " ".join(
            f"{entry.title} {entry.description} {rel_url_path(entry.url)}"
            for entry in cluster.entries
        )
        corpus = weighted_token_set(
            (humanize_slug(cluster.guide), 10),
            (cluster.guide.replace("_", " ").replace("-", " "), 10),
            (task_category(cluster), 6),
            (entry_text, 1),
        )
        score = overlap_score(query_tokens, corpus)
        if best is None or score > best[0]:
            best = (score, cluster, corpus)
    if best is None:
        raise ValueError("no route clusters available")
    score, cluster, corpus = best
    return cluster, score, matched_terms(query_tokens, corpus)


def choose_entry(
    query_tokens: Counter[str],
    cluster: GuideCluster,
) -> tuple[LlmEntry, int, tuple[str, ...]]:
    best: tuple[int, LlmEntry, Counter[str]] | None = None
    for entry in cluster.entries:
        corpus = weighted_tokens(
            (entry.title, 8),
            (entry.description, 4),
            (entry.heading, 3),
            (rel_url_path(entry.url), 2),
        )
        score = overlap_score(query_tokens, corpus)
        if best is None or score > best[0]:
            best = (score, entry, corpus)
    if best is None:
        raise ValueError("selected cluster has no entries")
    score, entry, corpus = best
    return entry, score, matched_terms(query_tokens, corpus)


def route_question(
    question: str,
    repo_root: Path,
    registry: str,
    skills_root_arg: str,
) -> SkillRoute:
    skills_root = repo_root / skills_root_arg
    docsets = [
        docset
        for docset in load_docsets(repo_root / registry)
        if docset.enabled and (skills_root / docset.skill_slug / "SKILL.md").exists()
    ]
    query_tokens = tokenize(question)
    docset, skill_score, skill_terms = choose_skill(
        question, query_tokens, docsets, skills_root
    )
    llms_path = skills_root / docset.skill_slug / "references" / "llms.txt"
    entries = parse_llms_file(llms_path)
    selected_version = detect_latest_version(
        entries, docset.base_url, preferred_version=docset.preferred_version
    )
    clusters = cluster_entries(entries, docset.base_url, selected_version)
    guide, guide_score, guide_terms = choose_guide(query_tokens, clusters)
    entry, entry_score, entry_terms = choose_entry(query_tokens, guide)
    snapshot = f"references/snapshots/{guide.guide_slug}.md"
    if not (skills_root / docset.skill_slug / snapshot).exists():
        snapshot = "live-only"
    return SkillRoute(
        docset=docset,
        skill_score=skill_score,
        guide=guide,
        guide_score=guide_score,
        entry=entry,
        entry_score=entry_score,
        route_pattern=routing_url_pattern(docset.base_url, guide),
        snapshot=snapshot,
        matched_skill_terms=skill_terms,
        matched_guide_terms=guide_terms,
        matched_entry_terms=entry_terms,
    )


def print_route(sample: Sample, route: SkillRoute) -> None:
    print(f"CASE {sample.name}")
    print(f"Question: {sample.question}")
    print(
        f"Skill route: {route.docset.skill_slug} "
        f"(expected {sample.expected_skill}, score {route.skill_score}, "
        f"matched {', '.join(route.matched_skill_terms) or 'none'})"
    )
    print(
        f"Guide route: {route.guide.guide} "
        f"(expected {sample.expected_guide}, score {route.guide_score}, "
        f"matched {', '.join(route.matched_guide_terms) or 'none'})"
    )
    print(f"Live pattern: {route.route_pattern}")
    print(
        f"Selected live URL: {route.entry.url} "
        f"(entry score {route.entry_score}, "
        f"matched {', '.join(route.matched_entry_terms) or 'none'})"
    )
    print(f"Fallback snapshot: {route.snapshot}")
    print("Fetch order: live Markdown URL first; snapshot only if live fetch fails.")
    print()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--registry", default="scripts/docsets.yaml")
    parser.add_argument(
        "--skills-root", default="plugins/ping-identity-docs/skills"
    )
    parser.add_argument(
        "--assert-defaults",
        action="store_true",
        help="Fail unless built-in samples route to their expected skill and guide.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    failures: list[str] = []
    for sample in SAMPLES:
        route = route_question(sample.question, repo_root, args.registry, args.skills_root)
        print_route(sample, route)
        if args.assert_defaults:
            if route.docset.skill_slug != sample.expected_skill:
                failures.append(
                    f"{sample.name}: skill {route.docset.skill_slug} "
                    f"!= {sample.expected_skill}"
                )
            if route.guide.guide != sample.expected_guide:
                failures.append(
                    f"{sample.name}: guide {route.guide.guide} "
                    f"!= {sample.expected_guide}"
                )
            if route.snapshot != "live-only" and not (
                repo_root / args.skills_root / route.docset.skill_slug / route.snapshot
            ).exists():
                failures.append(f"{sample.name}: missing fallback {route.snapshot}")

    for failure in failures:
        print(f"ERROR: {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
