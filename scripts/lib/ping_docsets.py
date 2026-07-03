#!/usr/bin/env python3
"""Shared helpers for Ping Identity docset skill tooling."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from html import unescape
from pathlib import Path
from urllib.parse import urlparse
import hashlib
import json
import re
import sys
from typing import Iterable


LLMS_ENTRY_RE = re.compile(
    r"^\s*-\s+\[(?P<title>[^\]]+)\]\((?P<url>https?://[^)\s]+\.md)\)"
    r"(?:(?::|\s+-)\s*(?P<description>.*))?\s*$"
)
VERSION_RE = re.compile(r"^\d+(?:\.\d+)*$")
STOPWORDS = {
    "a",
    "an",
    "and",
    "api",
    "apis",
    "as",
    "for",
    "from",
    "how",
    "in",
    "including",
    "into",
    "of",
    "on",
    "or",
    "ping",
    "pingidentity",
    "the",
    "to",
    "using",
    "with",
}


@dataclass(frozen=True)
class Docset:
    skill_slug: str
    label: str
    source: str
    base_url: str
    enabled: bool = True
    preferred_version: str | None = None


@dataclass(frozen=True)
class LlmEntry:
    title: str
    url: str
    description: str
    heading: str


@dataclass(frozen=True)
class GuideCluster:
    guide: str
    version: str
    entries: tuple[LlmEntry, ...]
    first_page_url: str
    single_page_url: str
    single_page_urls: tuple[str, ...]

    @property
    def guide_slug(self) -> str:
        return slugify(self.guide)


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "root"


def humanize_slug(value: str) -> str:
    return re.sub(r"[-_]+", " ", value).strip().title() or "Root"


def load_docsets(path: str | Path) -> list[Docset]:
    """Parse scripts/docsets.yaml without requiring PyYAML."""
    docsets: list[Docset] = []
    current: dict[str, str] | None = None

    for raw_line in Path(path).read_text(encoding="utf-8").splitlines():
        line = raw_line.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        stripped = line.strip()
        if stripped == "docsets:":
            continue
        if stripped.startswith("- "):
            if current:
                docsets.append(_docset_from_mapping(current))
            current = {}
            key_value = stripped[2:]
        else:
            key_value = stripped
        if ":" not in key_value or current is None:
            continue
        key, value = key_value.split(":", 1)
        current[key.strip()] = _clean_yaml_scalar(value.strip())

    if current:
        docsets.append(_docset_from_mapping(current))
    return docsets


def _clean_yaml_scalar(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _docset_from_mapping(data: dict[str, str]) -> Docset:
    preferred_version = data.get("preferred_version")
    if preferred_version is not None and preferred_version.lower() in {"", "null", "~"}:
        preferred_version = None
    return Docset(
        skill_slug=data["skill_slug"],
        label=data.get("label", data["skill_slug"]),
        source=data.get("source", ""),
        base_url=data["base_url"].rstrip("/"),
        enabled=data.get("enabled", "true").lower() == "true",
        preferred_version=preferred_version or None,
    )


def find_docset(docsets: Iterable[Docset], slug: str) -> Docset:
    for docset in docsets:
        if docset.skill_slug == slug:
            return docset
    raise KeyError(f"Unknown docset slug: {slug}")


def parse_llms_text(text: str) -> list[LlmEntry]:
    entries: list[LlmEntry] = []
    heading = ""
    for line in text.splitlines():
        if line.startswith("## "):
            heading = line[3:].strip()
            continue
        match = LLMS_ENTRY_RE.match(line)
        if not match:
            continue
        entries.append(
            LlmEntry(
                title=unescape(match.group("title")).strip(),
                url=match.group("url").strip(),
                description=unescape(match.group("description") or "").strip(),
                heading=heading,
            )
        )
    return entries


def parse_llms_file(path: str | Path) -> list[LlmEntry]:
    return parse_llms_text(Path(path).read_text(encoding="utf-8"))


def relative_doc_path(url: str, base_url: str) -> str:
    parsed = urlparse(url)
    base = urlparse(base_url.rstrip("/"))
    if parsed.netloc != base.netloc:
        raise ValueError(f"URL host does not match docset base: {url}")
    base_path = base.path.rstrip("/")
    if parsed.path == base_path:
        return ""
    prefix = f"{base_path}/" if base_path else "/"
    if not parsed.path.startswith(prefix):
        raise ValueError(f"URL path is outside docset base {base_url}: {url}")
    return parsed.path[len(prefix) :].lstrip("/")


def detect_latest_version(
    entries: Iterable[LlmEntry], base_url: str, preferred_version: str | None = None
) -> str:
    if preferred_version:
        return preferred_version
    versions: set[str] = set()
    for entry in entries:
        try:
            first_segment = relative_doc_path(entry.url, base_url).split("/", 1)[0]
        except ValueError:
            continue
        if VERSION_RE.match(first_segment):
            versions.add(first_segment)
    if not versions:
        return ""
    return max(versions, key=_version_key)


def _version_key(version: str) -> tuple[int, ...]:
    return tuple(int(part) for part in version.split("."))


def cluster_entries(
    entries: Iterable[LlmEntry], base_url: str, selected_version: str
) -> list[GuideCluster]:
    grouped: dict[tuple[str, str], list[LlmEntry]] = {}
    for entry in entries:
        rel_path = relative_doc_path(entry.url, base_url)
        parts = rel_path.split("/") if rel_path else []
        if selected_version:
            if parts and parts[0] == selected_version:
                if len(parts) > 2:
                    guide = parts[1]
                else:
                    guide = "root"
                cluster_version = selected_version
            elif parts and VERSION_RE.match(parts[0]):
                continue
            else:
                guide = parts[0] if parts else "root"
                cluster_version = "current"
        else:
            guide = parts[0] if parts else "root"
            cluster_version = "current"
        grouped.setdefault((cluster_version, guide), []).append(entry)

    clusters: list[GuideCluster] = []
    for (cluster_version, guide), guide_entries in grouped.items():
        first_url = guide_entries[0].url
        single_urls: list[str]
        if cluster_version and cluster_version != "current":
            single_urls = [f"{base_url}/{cluster_version}/{guide}/single-page.md"]
            if guide == "root":
                single_urls = [f"{base_url}/{cluster_version}/single-page.md"]
            else:
                single_urls.append(f"{base_url}/{guide}/single-page.md")
        else:
            if guide == "root":
                single_urls = [f"{base_url}/single-page.md"]
            else:
                single_urls = [f"{base_url}/{guide}/single-page.md"]
        clusters.append(
            GuideCluster(
                guide=guide,
                version=cluster_version or "current",
                entries=tuple(guide_entries),
                first_page_url=first_url,
                single_page_url=single_urls[0],
                single_page_urls=tuple(dict.fromkeys(single_urls)),
            )
        )
    return sorted(clusters, key=lambda item: (-len(item.entries), item.guide_slug))


def routing_url_pattern(base_url: str, cluster: GuideCluster) -> str:
    if cluster.version and cluster.version != "current":
        if cluster.guide == "root":
            return f"{base_url}/{cluster.version}/*.md"
        return f"{base_url}/{cluster.version}/{cluster.guide}/*.md"
    if cluster.guide == "root":
        return f"{base_url}/*.md"
    return f"{base_url}/{cluster.guide}/*.md"


def task_category(cluster: GuideCluster) -> str:
    guide_name = humanize_slug(cluster.guide)
    words: dict[str, int] = {}
    for entry in cluster.entries[:20]:
        text = f"{entry.title} {entry.description}".lower()
        for word in re.findall(r"[a-z][a-z0-9]{2,}", text):
            if word in STOPWORDS:
                continue
            words[word] = words.get(word, 0) + 1
    top_words = [
        word
        for word, _count in sorted(words.items(), key=lambda item: (-item[1], item[0]))[:3]
    ]
    if top_words:
        return f"{guide_name}: {', '.join(top_words)}"
    return guide_name


def product_summary(label: str, entries: Iterable[LlmEntry]) -> str:
    for entry in entries:
        if entry.title.lower().replace(" ", "") == label.lower().replace(" ", "") and entry.description:
            return entry.description.rstrip(".") + "."
    for entry in entries:
        if entry.description:
            return entry.description.rstrip(".") + "."
    return f"{label} documentation is indexed in the bundled llms.txt and live Ping Markdown pages."


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def today_iso() -> str:
    return date.today().isoformat()


def dump_json(data: object) -> None:
    print(json.dumps(data, indent=2, sort_keys=True))


def die(message: str, code: int = 1) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(code)
