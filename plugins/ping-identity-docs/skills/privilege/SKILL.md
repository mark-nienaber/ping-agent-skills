---
name: privilege
description: "Use when working with PingOne Privilege: privileged access management, configuration, getting started, integrations, procyonreadpolicy, troubleshooting. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# PingOne Privilege

PingOne Privilege supports certificate-based SSH and Remote Desktop Protocol for secure access to your resources.

## Live source of truth

- Product docs: https://docs.pingidentity.com/privilege/
- llms.txt index: https://docs.pingidentity.com/privilege/llms.txt
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
| Privileged Access Management: access, user, managing | privileged-access-management | https://docs.pingidentity.com/privilege/privileged-access-management/*.md | references/snapshots/privileged-access-management.md |
| Configuration: access, configuring, privilege | configuration | https://docs.pingidentity.com/privilege/configuration/*.md | references/snapshots/configuration.md |
| Getting Started: pingone, privilege, access | getting-started | https://docs.pingidentity.com/privilege/getting-started/*.md | references/snapshots/getting-started.md |
| Integrations: integration, access, teams | integrations | https://docs.pingidentity.com/privilege/integrations/*.md | references/snapshots/integrations.md |
| Procyonreadpolicy: create, policy, enable | procyonreadpolicy | https://docs.pingidentity.com/privilege/procyonreadpolicy/*.md | references/snapshots/procyonreadpolicy.md |
| Troubleshooting: pingone, privilege, troubleshooting | troubleshooting | https://docs.pingidentity.com/privilege/troubleshooting/*.md | references/snapshots/troubleshooting.md |
| Index.Md: pingone, privilege | index.md | https://docs.pingidentity.com/privilege/index.md | references/snapshots/index-md.md |
| Release Notes: pingone, privilege, about | release-notes | https://docs.pingidentity.com/privilege/release-notes/*.md | references/snapshots/release-notes.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.
