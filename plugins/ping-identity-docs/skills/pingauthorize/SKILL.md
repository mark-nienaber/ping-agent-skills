---
name: pingauthorize
description: "Use when administering PingAuthorize, including policy administration, server configuration, trust framework, SCIM, integrations, installation, upgrades, and troubleshooting. Routes to live docs; snapshots fallback."
license: MIT
---

# PingAuthorize

Encrypt log files as they're written.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingauthorize/
- llms.txt index: https://docs.pingidentity.com/pingauthorize/llms.txt
- Snapshot version: 11.1
- Snapshot manifest: references/MANIFEST.md

## Fetch strategy

1. Read references/llms.txt for page discovery.
2. Match the user task to page titles, page descriptions, and the routing table below.
3. Fetch the selected live `.md` URL from Ping documentation.
4. If live fetch is unavailable, read the closest file under references/snapshots/.

## Task routing

| Task category | Guide slug | Live URL pattern | Snapshot |
|---|---|---|---|
| Pingauthorize Server Administration Guide: about, log, tool | pingauthorize_server_administration_guide | https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/*.md | references/snapshots/pingauthorize-server-administration-guide.md |
| Pingauthorize Policy Administration Guide: resource, attribute, attributes | pingauthorize_policy_administration_guide | https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_policy_administration_guide/*.md | references/snapshots/pingauthorize-policy-administration-guide.md |
| Installing And Uninstalling Pingauthorize: pingauthorize, policy, editor | installing_and_uninstalling_pingauthorize | https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/*.md | references/snapshots/installing-and-uninstalling-pingauthorize.md |
| Troubleshooting Pingauthorize Server: server, http, troubleshooting | troubleshooting_pingauthorize_server | https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/*.md | references/snapshots/troubleshooting-pingauthorize-server.md |
| Pingauthorize Integrations: pingauthorize, integration, gateway | pingauthorize_integrations | https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_integrations/*.md | references/snapshots/pingauthorize-integrations.md |
| Upgrading Pingauthorize: policy, upgrade, pingauthorize | upgrading_pingauthorize | https://docs.pingidentity.com/pingauthorize/11.1/upgrading_pingauthorize/*.md | references/snapshots/upgrading-pingauthorize.md |
| Root: pingauthorize, architectural, introduction | root | https://docs.pingidentity.com/pingauthorize/11.1/*.md | references/snapshots/root.md |
| Getting Started With Pingauthorize Tutorials: access, control, pingauthorize | getting_started_with_pingauthorize_tutorials | https://docs.pingidentity.com/pingauthorize/11.1/getting_started_with_pingauthorize_tutorials/*.md | references/snapshots/getting-started-with-pingauthorize-tutorials.md |
| Release Notes: notes, release | release_notes | https://docs.pingidentity.com/pingauthorize/11.1/release_notes/*.md | references/snapshots/release-notes.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.
