---
name: orchsdks
description: "Use when the user explicitly names Orchestration SDKs or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Orchestration SDKs

Use the FIDO module to register and authenticate FIDO authenticators in JavaScript apps built with the DaVinci client.

## Live source of truth

- Product docs: https://developer.pingidentity.com/orchsdks/
- llms.txt index: https://developer.pingidentity.com/orchsdks/llms.txt
- Snapshot version: current
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
| Journey: configure, identity, device | journey | https://developer.pingidentity.com/orchsdks/journey/*.md | references/snapshots/journey.md |
| Davinci: davinci, configure, pingone | davinci | https://developer.pingidentity.com/orchsdks/davinci/*.md | references/snapshots/davinci.md |
| Oidc: oidc, before, sign | oidc | https://developer.pingidentity.com/orchsdks/oidc/*.md | references/snapshots/oidc.md |
| Release Notes: orchestration, sdk, release | release-notes | https://developer.pingidentity.com/orchsdks/release-notes/*.md | references/snapshots/release-notes.md |
| Security: security, orchestration, sdks | security | https://developer.pingidentity.com/orchsdks/security/*.md | references/snapshots/security.md |
| Concepts: concepts, multiple, system | concepts | https://developer.pingidentity.com/orchsdks/concepts/*.md | references/snapshots/concepts.md |
| Index.Md: orchestration, sdks, advanced | index.md | https://developer.pingidentity.com/orchsdks/index.md | references/snapshots/index-md.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.
