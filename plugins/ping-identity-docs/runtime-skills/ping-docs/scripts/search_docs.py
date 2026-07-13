#!/usr/bin/env python3
"""Deterministically search cached Ping Identity llms.txt indexes.

This command never performs a network request. It returns live Markdown URLs for use when
network access exists and local snapshot paths for safe offline fallback.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from html import unescape
import json
import math
import os
from pathlib import Path
import re
import sys
from typing import Iterable, Sequence
from urllib.parse import urlparse


ENTRY_RE = re.compile(
    r"^\s*-\s+\[(?P<title>[^\]]+)\]\((?P<url>https?://[^)\s]+\.md)\)"
    r"(?:(?::|\s+-)\s*(?P<description>.*))?\s*$"
)
TOKEN_RE = re.compile(r"[a-z0-9]+")
VERSION_RE = re.compile(r"^\d+(?:\.\d+)*$")
MANIFEST_FIELD_RE = re.compile(r"^- (?P<key>[^:]+):\s*(?P<value>.*)$")

STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "be",
    "can",
    "could",
    "do",
    "does",
    "for",
    "from",
    "how",
    "i",
    "in",
    "into",
    "is",
    "it",
    "me",
    "my",
    "of",
    "on",
    "or",
    "please",
    "show",
    "the",
    "to",
    "using",
    "want",
    "with",
}

# These signals keep broad lexical matches from routing out-of-domain prompts into Ping docs.
DOMAIN_TOKENS = {
    "amster",
    "authentication",
    "authorization",
    "authorize",
    "ciba",
    "davinci",
    "federation",
    "fido",
    "forgeops",
    "iam",
    "identity",
    "introspection",
    "introspect",
    "jose",
    "journey",
    "jwt",
    "ldap",
    "mfa",
    "oauth",
    "oauth2",
    "oidc",
    "openid",
    "passkey",
    "passwordless",
    "pkce",
    "provisioning",
    "radius",
    "saml",
    "scim",
    "sso",
    "uma",
    "webfinger",
}
DOMAIN_PHRASES = {
    "access token",
    "account lockout",
    "authorization code",
    "authorization policy",
    "authentication node",
    "authentication tree",
    "client credential",
    "identity store",
    "policy decision",
    "policy information",
    "policy set",
    "refresh token",
    "resource owner",
    "service account",
    "single sign on",
    "user store",
}

PRODUCT_ALIASES = {
    "aic": "pingoneaic",
    "advanced identity cloud": "pingoneaic",
    "am": "pingam",
    "authorize": "pingauthorize",
    "directory": "pingdirectory",
    "ds": "pingds",
    "federate": "pingfederate",
    "gateway": "pinggateway",
    "idm": "pingidm",
    "pa": "pingaccess",
    "paz": "pingauthorize",
    "ping am": "pingam",
    "ping authorize": "pingauthorize",
    "ping directory": "pingdirectory",
    "ping federate": "pingfederate",
    "ping one": "pingone",
    "pingone aic": "pingoneaic",
}


@dataclass(frozen=True)
class Docset:
    slug: str
    label: str
    directory: Path
    index_path: Path
    manifest_path: Path | None
    base_url: str
    version: str
    sync_date: str
    snapshot_rows: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class Entry:
    product: Docset
    title: str
    url: str
    description: str
    heading: str


@dataclass(frozen=True)
class Candidate:
    entry: Entry
    title_matches: frozenset[str]
    description_matches: frozenset[str]
    heading_matches: frozenset[str]
    url_matches: frozenset[str]
    product_matches: frozenset[str]
    searchable_text: str

    @property
    def matches(self) -> frozenset[str]:
        return frozenset().union(
            self.title_matches,
            self.description_matches,
            self.heading_matches,
            self.url_matches,
            self.product_matches,
        )


def _compact(value: str) -> str:
    return "".join(TOKEN_RE.findall(value.lower()))


def _slugify(value: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", value.lower())).strip("-")


def _token_variants(token: str) -> set[str]:
    variants = {token}
    if len(token) > 5 and token.endswith("ies"):
        variants.add(token[:-3] + "y")
    elif len(token) > 5 and token.endswith("ing"):
        variants.add(token[:-3])
        variants.add(token[:-3] + "e")
    elif len(token) > 4 and token.endswith("ed"):
        variants.add(token[:-2])
        variants.add(token[:-1])
    elif len(token) > 4 and token.endswith("s") and not token.endswith("ss"):
        variants.add(token[:-1])
    return variants


def tokenize(value: str, *, remove_stopwords: bool = True) -> frozenset[str]:
    tokens: set[str] = set()
    for raw_token in TOKEN_RE.findall(unescape(value).lower()):
        if len(raw_token) < 2:
            continue
        if remove_stopwords and raw_token in STOPWORDS:
            continue
        tokens.update(_token_variants(raw_token))
    return frozenset(tokens)


def _parse_manifest(path: Path | None) -> tuple[dict[str, str], tuple[tuple[str, str], ...]]:
    if path is None or not path.is_file():
        return {}, ()
    fields: dict[str, str] = {}
    rows: list[tuple[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        field_match = MANIFEST_FIELD_RE.match(line)
        if field_match:
            fields[field_match.group("key").strip().lower()] = field_match.group("value").strip()
            continue
        if not line.startswith("|") or line.startswith("|---") or "Snapshot" in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 3 and cells[0].endswith(".md"):
            rows.append((cells[0], cells[2].strip("<>")))
    return fields, tuple(rows)


def _first_heading(path: Path) -> str:
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("# "):
                return line[2:].strip()
    return path.parent.parent.name


def _normalise_data_root(candidate: Path) -> Path | None:
    candidate = candidate.expanduser().resolve()
    roots = (candidate, candidate / "skills")
    for root in roots:
        if root.is_dir() and any(root.glob("*/references/llms.txt")):
            return root
    return None


def discover_data_root(explicit: str | Path | None = None) -> Path:
    """Find docsets in an explicit, standalone-skill, or repository layout."""
    if explicit is not None:
        root = _normalise_data_root(Path(explicit))
        if root is None:
            raise ValueError(f"No docsets found under data root: {explicit}")
        return root

    env_root = os.environ.get("PING_DOCS_DATA_ROOT")
    if env_root:
        root = _normalise_data_root(Path(env_root))
        if root is None:
            raise ValueError(f"No docsets found under PING_DOCS_DATA_ROOT: {env_root}")
        return root

    script_path = Path(__file__).resolve()
    standalone = script_path.parent.parent / "references" / "docsets"
    root = _normalise_data_root(standalone)
    if root is not None:
        return root

    for ancestor in script_path.parents:
        repository = ancestor / "plugins" / "ping-identity-docs" / "skills"
        root = _normalise_data_root(repository)
        if root is not None:
            return root

    raise ValueError(
        "No Ping documentation indexes found. Set PING_DOCS_DATA_ROOT or install "
        "references/docsets beside the ping-docs skill."
    )


def load_docsets(data_root: Path) -> list[Docset]:
    docsets: list[Docset] = []
    for index_path in sorted(data_root.glob("*/references/llms.txt")):
        directory = index_path.parent.parent
        manifest_path = index_path.parent / "MANIFEST.md"
        manifest = manifest_path if manifest_path.is_file() else None
        fields, snapshot_rows = _parse_manifest(manifest)
        label = fields.get("product") or _first_heading(index_path)
        source = fields.get("source", "")
        base_url = source.removesuffix("/llms.txt").removesuffix("llms.txt").rstrip("/")
        docsets.append(
            Docset(
                slug=directory.name,
                label=label,
                directory=directory,
                index_path=index_path,
                manifest_path=manifest,
                base_url=base_url,
                version=fields.get("version", ""),
                sync_date=fields.get("sync date", ""),
                snapshot_rows=snapshot_rows,
            )
        )
    return docsets


def _product_keys(docset: Docset) -> set[str]:
    keys = {
        docset.slug.lower(),
        docset.slug.lower().replace("-", " "),
        docset.label.lower(),
        _compact(docset.slug),
        _compact(docset.label),
    }
    keys.update(alias for alias, slug in PRODUCT_ALIASES.items() if slug == docset.slug)
    return keys


def select_product(docsets: Sequence[Docset], product_filter: str | None) -> list[Docset]:
    if not product_filter:
        return list(docsets)
    needle = product_filter.strip().lower()
    compact_needle = _compact(needle)
    alias_slug = PRODUCT_ALIASES.get(needle)
    exact = [
        docset
        for docset in docsets
        if needle in _product_keys(docset)
        or compact_needle in {_compact(key) for key in _product_keys(docset)}
        or (alias_slug is not None and docset.slug == alias_slug)
    ]
    if len(exact) == 1:
        return exact
    if not exact:
        raise ValueError(f"Unknown product filter: {product_filter}")
    labels = ", ".join(docset.slug for docset in exact)
    raise ValueError(f"Ambiguous product filter {product_filter!r}; choose one of: {labels}")


def _iter_entries(docset: Docset) -> Iterable[Entry]:
    heading = ""
    with docset.index_path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("## "):
                heading = line[3:].strip()
                continue
            match = ENTRY_RE.match(line)
            if match:
                yield Entry(
                    product=docset,
                    title=unescape(match.group("title")).strip(),
                    url=match.group("url").strip(),
                    description=unescape(match.group("description") or "").strip(),
                    heading=heading,
                )


def _query_has_domain_signal(query: str, docsets: Sequence[Docset]) -> bool:
    lowered = " ".join(TOKEN_RE.findall(query.lower()))
    compact_query = _compact(query)
    query_tokens = tokenize(query, remove_stopwords=False)
    if query_tokens & DOMAIN_TOKENS:
        return True
    if any(phrase in lowered for phrase in DOMAIN_PHRASES):
        return True
    for docset in docsets:
        for key in _product_keys(docset):
            compact_key = _compact(key)
            if len(compact_key) >= 4 and compact_key in compact_query:
                return True
    return False


def _matched(tokens: frozenset[str], query_tokens: frozenset[str]) -> frozenset[str]:
    return tokens & query_tokens


def _snapshot_for(entry: Entry) -> Path | None:
    docset = entry.product
    entry_version = _entry_version(entry)
    if entry_version and docset.version and entry_version != docset.version:
        # Never present a current-version snapshot as an offline copy of an older live page.
        return None
    snapshots_dir = docset.directory / "references" / "snapshots"
    if not snapshots_dir.is_dir():
        return None

    # Prefer a manifest row that records this exact page or its assembled guide.
    for filename, source in docset.snapshot_rows:
        if source == entry.url:
            candidate = snapshots_dir / filename
            if candidate.is_file():
                return candidate.resolve()

    parsed_url = urlparse(entry.url)
    base_path = urlparse(docset.base_url).path.rstrip("/") if docset.base_url else ""
    relative = parsed_url.path
    if base_path and relative.startswith(base_path + "/"):
        relative = relative[len(base_path) + 1 :]
    else:
        relative = relative.lstrip("/")
    parts = [part for part in relative.split("/") if part]
    if parts and (parts[0] == docset.version or VERSION_RE.match(parts[0])):
        parts = parts[1:]
    guide = parts[0] if len(parts) > 1 else "root"

    for filename, source in docset.snapshot_rows:
        source_slug = _slugify(source)
        if guide != "root" and re.search(rf"\bfrom-{re.escape(_slugify(guide))}\b", source_slug):
            candidate = snapshots_dir / filename
            if candidate.is_file():
                return candidate.resolve()

    basename = parts[-1] if parts else "root.md"
    candidate_names = [
        f"{_slugify(basename)}.md",
        f"{_slugify(Path(basename).stem)}.md",
        f"{_slugify(guide)}.md",
        "root.md",
    ]
    manifest_names = {filename for filename, _source in docset.snapshot_rows}
    if docset.manifest_path is not None and not manifest_names:
        # A current manifest with no captured rows means any files left on disk are
        # retained legacy data whose age and provenance are unknown.
        return None
    for filename in dict.fromkeys(candidate_names):
        if manifest_names and filename not in manifest_names:
            continue
        candidate = snapshots_dir / filename
        if candidate.is_file():
            return candidate.resolve()
    return None


def _entry_version(entry: Entry) -> str:
    parsed_url = urlparse(entry.url)
    base_path = urlparse(entry.product.base_url).path.rstrip("/")
    if not base_path or not parsed_url.path.startswith(base_path + "/"):
        return ""
    relative = parsed_url.path[len(base_path) + 1 :]
    first_segment = relative.split("/", 1)[0]
    return first_segment if VERSION_RE.match(first_segment) else ""


def _canonical_page_key(entry: Entry) -> tuple[str, str]:
    """Identify the same page across versions so top-k contains distinct pages."""
    parsed_url = urlparse(entry.url)
    parts = [part for part in parsed_url.path.split("/") if part]
    version = _entry_version(entry)
    if version and version in parts:
        parts.remove(version)
    return entry.product.slug, "/".join(parts)


def _result_dict(candidate: Candidate, score: float) -> dict[str, object]:
    entry = candidate.entry
    snapshot = _snapshot_for(entry)
    return {
        "product": entry.product.label,
        "product_slug": entry.product.slug,
        "title": entry.title,
        "live_markdown_url": entry.url,
        "document_version": _entry_version(entry) or None,
        "score": round(score, 3),
        "description": entry.description,
        "local_snapshot": str(snapshot) if snapshot else None,
        "local_manifest": (
            str(entry.product.manifest_path.resolve()) if entry.product.manifest_path else None
        ),
        "snapshot_sync_date": entry.product.sync_date or None,
        "snapshot_version": entry.product.version or None,
    }


def search(
    query: str,
    *,
    product_filter: str | None = None,
    top_k: int = 5,
    data_root: str | Path | None = None,
) -> dict[str, object]:
    query = query.strip()
    root = discover_data_root(data_root)
    all_docsets = load_docsets(root)
    selected_docsets = select_product(all_docsets, product_filter)
    query_tokens = tokenize(query)
    response: dict[str, object] = {
        "query": query,
        "product_filter": product_filter,
        "data_root": str(root),
        "status": "no_results",
        "reason": "",
        "results": [],
    }
    if not query_tokens:
        response["reason"] = "The query has no searchable terms."
        return response
    if not product_filter and not _query_has_domain_signal(query, all_docsets):
        response["reason"] = "The query has no Ping Identity or IAM-specific signal."
        return response

    document_frequency = {token: 0 for token in query_tokens}
    candidates: list[Candidate] = []
    total_entries = 0
    query_phrase = " ".join(
        token for token in TOKEN_RE.findall(query.lower()) if token not in STOPWORDS
    )

    for docset in selected_docsets:
        product_tokens = tokenize(f"{docset.slug} {docset.label}", remove_stopwords=False)
        for entry in _iter_entries(docset):
            total_entries += 1
            title_tokens = tokenize(entry.title, remove_stopwords=False)
            description_tokens = tokenize(entry.description, remove_stopwords=False)
            heading_tokens = tokenize(entry.heading, remove_stopwords=False)
            url_tokens = tokenize(urlparse(entry.url).path, remove_stopwords=False)
            combined = title_tokens | description_tokens | heading_tokens | url_tokens | product_tokens
            present = combined & query_tokens
            for token in present:
                document_frequency[token] += 1
            if not present:
                continue
            candidates.append(
                Candidate(
                    entry=entry,
                    title_matches=_matched(title_tokens, query_tokens),
                    description_matches=_matched(description_tokens, query_tokens),
                    heading_matches=_matched(heading_tokens, query_tokens),
                    url_matches=_matched(url_tokens, query_tokens),
                    product_matches=_matched(product_tokens, query_tokens),
                    searchable_text=" ".join(
                        TOKEN_RE.findall(f"{entry.title} {entry.description}".lower())
                    ),
                )
            )

    scored: list[tuple[float, Candidate]] = []
    query_count = len(query_tokens)
    requested_versions = set(re.findall(r"(?<!\d)\d+(?:\.\d+)+(?!\d)", query))
    for candidate in candidates:
        score = 0.0
        for token in candidate.matches:
            frequency = document_frequency[token]
            inverse_frequency = math.log(
                1.0 + (total_entries - frequency + 0.5) / (frequency + 0.5)
            )
            field_weight = 0.0
            if token in candidate.title_matches:
                field_weight = max(field_weight, 4.5)
            if token in candidate.description_matches:
                field_weight = max(field_weight, 2.0)
            if token in candidate.heading_matches:
                field_weight = max(field_weight, 0.75)
            if token in candidate.url_matches:
                field_weight = max(field_weight, 1.5)
            if token in candidate.product_matches:
                field_weight = max(field_weight, 3.0)
            score += inverse_frequency * field_weight
        coverage = len(candidate.matches) / query_count
        score *= 0.4 + 0.6 * coverage
        if query_phrase and query_phrase in candidate.searchable_text:
            score += 8.0
        if product_filter:
            score += 1.0
        entry_version = _entry_version(candidate.entry)
        if requested_versions:
            if entry_version in requested_versions:
                score += 4.0
        elif entry_version and entry_version == candidate.entry.product.version:
            score += 2.0
        if score >= 2.0:
            scored.append((score, candidate))

    scored.sort(
        key=lambda item: (
            -item[0],
            item[1].entry.product.slug,
            item[1].entry.title.lower(),
            item[1].entry.url,
        )
    )
    unique: list[tuple[float, Candidate]] = []
    seen_pages: set[tuple[str, str]] = set()
    for item in scored:
        page_key = _canonical_page_key(item[1].entry)
        if page_key in seen_pages:
            continue
        seen_pages.add(page_key)
        unique.append(item)
        if len(unique) == top_k:
            break

    if not unique:
        response["reason"] = "No cached documentation page met the relevance threshold."
        return response
    response["status"] = "ok"
    response["reason"] = None
    response["results"] = [_result_dict(candidate, score) for score, candidate in unique]
    return response


def _print_human(response: dict[str, object]) -> None:
    if response["status"] != "ok":
        print(f"No relevant Ping documentation found: {response['reason']}")
        return
    for position, result in enumerate(response["results"], start=1):
        assert isinstance(result, dict)
        print(f"{position}. {result['product']} — {result['title']} (score {result['score']})")
        print(f"   Live: {result['live_markdown_url']}")
        if result["local_snapshot"]:
            freshness = f", synced {result['snapshot_sync_date']}" if result["snapshot_sync_date"] else ""
            print(f"   Snapshot: {result['local_snapshot']}{freshness}")
        if result["local_manifest"]:
            print(f"   Manifest: {result['local_manifest']}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="+", help="Specific Ping documentation task")
    parser.add_argument("--product", help="Optional product name or docset slug")
    parser.add_argument("--top-k", type=int, default=5, help="Number of results (1-20)")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    parser.add_argument("--data-root", help="Override the cached docset root")
    args = parser.parse_args(argv)
    if not 1 <= args.top_k <= 20:
        parser.error("--top-k must be between 1 and 20")
    try:
        response = search(
            " ".join(args.query),
            product_filter=args.product,
            top_k=args.top_k,
            data_root=args.data_root,
        )
    except (OSError, ValueError) as exc:
        if args.json:
            print(json.dumps({"status": "error", "error": str(exc)}, indent=2))
        else:
            print(f"Error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(response, indent=2))
    else:
        _print_human(response)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
