---
name: privilege
description: "Use when the user explicitly names PingOne Privilege or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingOne Privilege

PingOne Privilege supports certificate-based SSH and Remote Desktop Protocol for secure access to your resources.

## Live source of truth

- Product docs: https://docs.pingidentity.com/privilege/
- llms.txt index: https://docs.pingidentity.com/privilege/llms.txt
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
| Privileged Access Management: access, user, managing | privileged-access-management | https://docs.pingidentity.com/privilege/privileged-access-management/*.md | references/snapshots/privileged-access-management.md |
| Configuration: access, configuring, privilege | configuration | https://docs.pingidentity.com/privilege/configuration/*.md | references/snapshots/configuration.md |
| Getting Started: pingone, privilege, access | getting-started | https://docs.pingidentity.com/privilege/getting-started/*.md | references/snapshots/getting-started.md |
| Integrations: integration, access, teams | integrations | https://docs.pingidentity.com/privilege/integrations/*.md | references/snapshots/integrations.md |
| Procyonreadpolicy: create, policy, enable | procyonreadpolicy | https://docs.pingidentity.com/privilege/procyonreadpolicy/*.md | references/snapshots/procyonreadpolicy.md |
| Troubleshooting: pingone, privilege, troubleshooting | troubleshooting | https://docs.pingidentity.com/privilege/troubleshooting/*.md | references/snapshots/troubleshooting.md |
| Index.Md: pingone, privilege | index.md | https://docs.pingidentity.com/privilege/index.md | references/snapshots/index-md.md |
| Release Notes: pingone, privilege, about | release-notes | https://docs.pingidentity.com/privilege/release-notes/*.md | references/snapshots/release-notes.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.
