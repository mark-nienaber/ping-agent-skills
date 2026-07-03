---
name: openicf
description: "Use when developing or administering OpenICF connectors, including connector reference, connector development, releases, object operations, synchronization, or connector framework behavior. Routes to live docs; snapshots fallback."
license: MIT
---

# OpenICF

Overview of the Identity Connector Framework (ICF) for connecting external resources to Ping Identity products, with available connectors listed.

## Live source of truth

- Product docs: https://docs.pingidentity.com/openicf/
- llms.txt index: https://docs.pingidentity.com/openicf/llms.txt
- Snapshot version: current
- Snapshot manifest: references/MANIFEST.md

## Fetch strategy

1. Read references/llms.txt for page discovery.
2. Match the user task to page titles, page descriptions, and the routing table below.
3. Fetch the selected live `.md` URL from Ping documentation.
4. If live fetch is unavailable, read the closest file under references/snapshots/.

## Task routing

| Task category | Guide slug | Live URL pattern | Snapshot |
|---|---|---|---|
| Connector Reference: connector, pingidm, configure | connector-reference | https://docs.pingidentity.com/openicf/connector-reference/*.md | references/snapshots/connector-reference.md |
| Connector Dev Guide: connector, icf, connectors | connector-dev-guide | https://docs.pingidentity.com/openicf/connector-dev-guide/*.md | references/snapshots/connector-dev-guide.md |
| Connector Release Notes: release, notes, connector | connector-release-notes | https://docs.pingidentity.com/openicf/connector-release-notes/*.md | references/snapshots/connector-release-notes.md |
| Index.Md: identity, available, connecting | index.md | https://docs.pingidentity.com/openicf/index.md/*.md | references/snapshots/index-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.
