---
name: pingintelligence
description: "Use when the user explicitly names PingIntelligence or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingIntelligence

PingIntelligence documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingintelligence/
- llms.txt index: https://docs.pingidentity.com/pingintelligence/llms.txt
- Snapshot version: 5.2
- Snapshot manifest: references/MANIFEST.md

## Retrieval strategy

1. Use the routing table to narrow the task to a guide when possible.
2. Search `references/llms.txt` for task terms and inspect at most 20 matching lines. Never load the whole index. Prefer `rg -i -n --max-count 20 '<term1>|<term2>' references/llms.txt` when shell access is available.
3. Fetch only the best matching live `.md` page from Ping documentation.
4. If that URL moved, fetch the live llms.txt index above and repeat the targeted search.
5. If live access is unavailable, read only the closest snapshot, check `references/MANIFEST.md`, and disclose its version, sync date, and partial-capture status.

## Task routing

| Task category | Guide slug | Live URL pattern | Snapshot |
|---|---|---|---|
| Pingintelligence Reference Guide: abs, based, logs | pingintelligence_reference_guide | https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/*.md | references/snapshots/pingintelligence-reference-guide.md |
| Pingintelligence Integrations: policy, pingintelligence, adding | pingintelligence_integrations | https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/*.md | references/snapshots/pingintelligence-integrations.md |
| Installing Pingintelligence For Apis: ase, changing, abs | installing_pingintelligence_for_apis | https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/*.md | references/snapshots/installing-pingintelligence-for-apis.md |
| Managing Pingintelligence For Apis: discovery, activity, client | managing_pingintelligence_for_apis | https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/*.md | references/snapshots/managing-pingintelligence-for-apis.md |
| Release Notes: pingintelligence, august, december | release_notes | https://docs.pingidentity.com/pingintelligence/5.2/release_notes/*.md | references/snapshots/release-notes.md |
| Root: pingintelligence, untitled, introduction | root | https://docs.pingidentity.com/pingintelligence/5.2/*.md | references/snapshots/root.md |
| Getting Started With Pingintelligence: discovery, ase, configuring | getting_started_with_pingintelligence | https://docs.pingidentity.com/pingintelligence/5.2/getting_started_with_pingintelligence/*.md | live-only |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.
