---
name: auth-node-ref
description: "Use when the user explicitly names Auth Node Ref or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Auth Node Ref

Prompts users to accept the active terms and conditions during registration or sign-on journeys in PingAM.

## Live source of truth

- Product docs: https://docs.pingidentity.com/auth-node-ref/
- llms.txt index: https://docs.pingidentity.com/auth-node-ref/llms.txt
- Snapshot version: 8.1
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
| Latest: node, identity, advanced | latest | https://docs.pingidentity.com/auth-node-ref/latest/*.md | references/snapshots/latest.md |
| Root: node, pingam, user | root | https://docs.pingidentity.com/auth-node-ref/8.1/*.md | references/snapshots/root.md |
| Pingone: pingone, node, credentials | pingone | https://docs.pingidentity.com/auth-node-ref/8.1/pingone/*.md | references/snapshots/pingone.md |
| Am Only: node, deprecated, pingam | am-only | https://docs.pingidentity.com/auth-node-ref/8.1/am-only/*.md | references/snapshots/am-only.md |
| Self Managed: node, thing, authenticate | self-managed | https://docs.pingidentity.com/auth-node-ref/8.1/self-managed/*.md | references/snapshots/self-managed.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.
