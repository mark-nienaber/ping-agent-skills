---
name: pingintelligence
description: "Use when working with PingIntelligence: pingintelligence reference guide, pingintelligence integrations, installing pingintelligence for apis, managing pingintelligence for apis, release notes, root. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# PingIntelligence

PingIntelligence documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingintelligence/
- llms.txt index: https://docs.pingidentity.com/pingintelligence/llms.txt
- Snapshot version: 5.2
- Snapshot manifest: references/MANIFEST.md

## Fetch strategy

1. Read references/llms.txt for page discovery.
2. Match the user task to page titles, page descriptions, and the routing table below.
3. Fetch the selected live `.md` URL from Ping documentation.
4. If live fetch is unavailable, read the closest file under references/snapshots/.

## Task routing

| Task category | Guide slug | Live URL pattern | Snapshot |
|---|---|---|---|
| Pingintelligence Reference Guide: abs, based, logs | pingintelligence_reference_guide | https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/*.md | references/snapshots/pingintelligence-reference-guide.md |
| Pingintelligence Integrations: policy, pingintelligence, adding | pingintelligence_integrations | https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/*.md | references/snapshots/pingintelligence-integrations.md |
| Installing Pingintelligence For Apis: ase, changing, abs | installing_pingintelligence_for_apis | https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/*.md | references/snapshots/installing-pingintelligence-for-apis.md |
| Managing Pingintelligence For Apis: discovery, activity, client | managing_pingintelligence_for_apis | https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/*.md | references/snapshots/managing-pingintelligence-for-apis.md |
| Release Notes: pingintelligence, august, december | release_notes | https://docs.pingidentity.com/pingintelligence/5.2/release_notes/*.md | references/snapshots/release-notes.md |
| Root: pingintelligence, untitled, introduction | root | https://docs.pingidentity.com/pingintelligence/5.2/*.md | references/snapshots/root.md |
| Getting Started With Pingintelligence: discovery, ase, configuring | getting_started_with_pingintelligence | https://docs.pingidentity.com/pingintelligence/5.2/getting_started_with_pingintelligence/*.md | references/snapshots/getting-started-with-pingintelligence.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.
