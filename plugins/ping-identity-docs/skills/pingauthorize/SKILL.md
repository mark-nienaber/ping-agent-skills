---
name: pingauthorize
description: "Use when the user explicitly names PingAuthorize or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingAuthorize

Encrypt log files as they're written.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingauthorize/
- llms.txt index: https://docs.pingidentity.com/pingauthorize/llms.txt
- Snapshot version: 11.1
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
| Pingauthorize Server Administration Guide: about, log, tool | pingauthorize_server_administration_guide | https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/*.md | references/snapshots/pingauthorize-server-administration-guide.md |
| Pingauthorize Policy Administration Guide: resource, attribute, attributes | pingauthorize_policy_administration_guide | https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/*.md | references/snapshots/pingauthorize-policy-administration-guide.md |
| Installing And Uninstalling Pingauthorize: pingauthorize, policy, editor | installing_and_uninstalling_pingauthorize | https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/*.md | references/snapshots/installing-and-uninstalling-pingauthorize.md |
| Troubleshooting Pingauthorize Server: server, http, troubleshooting | troubleshooting_pingauthorize_server | https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/*.md | references/snapshots/troubleshooting-pingauthorize-server.md |
| Pingauthorize Integrations: pingauthorize, integration, gateway | pingauthorize_integrations | https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_integrations/*.md | references/snapshots/pingauthorize-integrations.md |
| Upgrading Pingauthorize: policy, upgrade, pingauthorize | upgrading_pingauthorize | https://docs.pingidentity.com/pingauthorize/11.1/upgrading_pingauthorize/*.md | live-only |
| Root: pingauthorize, architectural, introduction | root | https://docs.pingidentity.com/pingauthorize/11.1/*.md | live-only |
| Getting Started With Pingauthorize Tutorials: access, control, pingauthorize | getting_started_with_pingauthorize_tutorials | https://docs.pingidentity.com/pingauthorize/11.1/getting_started_with_pingauthorize_tutorials/*.md | live-only |
| Release Notes: notes, release | release_notes | https://docs.pingidentity.com/pingauthorize/11.1/release_notes/*.md | live-only |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.
