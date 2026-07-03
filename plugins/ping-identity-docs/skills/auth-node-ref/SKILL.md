---
name: auth-node-ref
description: "Use when choosing or configuring Ping authentication tree nodes, callbacks, journeys, PingOne nodes, AM-only nodes, self-managed nodes, node inputs/outputs, or node reference behavior. Routes to live docs; snapshots fallback."
license: MIT
---

# Auth Node Ref

Prompts users to accept the active terms and conditions during registration or sign-on journeys in PingAM.

## Live source of truth

- Product docs: https://docs.pingidentity.com/auth-node-ref/
- llms.txt index: https://docs.pingidentity.com/auth-node-ref/llms.txt
- Snapshot version: 8.1
- Snapshot manifest: references/MANIFEST.md

## Fetch strategy

1. Read references/llms.txt for page discovery.
2. Match the user task to page titles, page descriptions, and the routing table below.
3. Fetch the selected live `.md` URL from Ping documentation.
4. If live fetch is unavailable, read the closest file under references/snapshots/.

## Task routing

| Task category | Guide slug | Live URL pattern | Snapshot |
|---|---|---|---|
| Root: node, pingam, user | root | https://docs.pingidentity.com/auth-node-ref/8.1/*.md | references/snapshots/root.md |
| Pingone: pingone, node, credentials | pingone | https://docs.pingidentity.com/auth-node-ref/8.1/pingone/*.md | references/snapshots/pingone.md |
| Am Only: node, deprecated, pingam | am-only | https://docs.pingidentity.com/auth-node-ref/8.1/am-only/*.md | references/snapshots/am-only.md |
| Self Managed: node, thing, authenticate | self-managed | https://docs.pingidentity.com/auth-node-ref/8.1/self-managed/*.md | references/snapshots/self-managed.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.
