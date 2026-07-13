---
name: forgeops
description: "Use when the user explicitly names ForgeOps or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# ForgeOps

ForgeOps documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/forgeops/
- llms.txt index: https://docs.pingidentity.com/forgeops/llms.txt
- Snapshot version: 2026.2
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
| Prepare: deployment, monitoring, pinggateway | prepare | https://docs.pingidentity.com/forgeops/2026.2/prepare/*.md | references/snapshots/prepare.md |
| Reference: forgeops, command, span | reference | https://docs.pingidentity.com/forgeops/2026.2/reference/*.md | references/snapshots/reference.md |
| Deploy: deploy, deployment, forgeops | deploy | https://docs.pingidentity.com/forgeops/2026.2/deploy/*.md | live-only |
| Troubleshoot: code, troubleshooting, amster | troubleshoot | https://docs.pingidentity.com/forgeops/2026.2/troubleshoot/*.md | references/snapshots/troubleshoot.md |
| Customize: code, image, about | customize | https://docs.pingidentity.com/forgeops/2026.2/customize/*.md | references/snapshots/customize.md |
| Start: forgeops, assess, here | start | https://docs.pingidentity.com/forgeops/2026.2/start/*.md | references/snapshots/start.md |
| Upgrade: upgrade, advanced, docker | upgrade | https://docs.pingidentity.com/forgeops/2026.2/upgrade/*.md | references/snapshots/upgrade.md |
| Rn: code, forgeops, evolution | rn | https://docs.pingidentity.com/forgeops/2026.2/rn/*.md | references/snapshots/rn.md |
| Setup: aws, azure, cloud | setup | https://docs.pingidentity.com/forgeops/2026.2/setup/*.md | references/snapshots/setup.md |
| Backup: backup, restore, span | backup | https://docs.pingidentity.com/forgeops/2026.2/backup/*.md | references/snapshots/backup.md |
| Root: forgeops, consolidated, documentation | root | https://docs.pingidentity.com/forgeops/2026.2/*.md | references/snapshots/root.md |
| Quick: deployment, minikube, quick | quick | https://docs.pingidentity.com/forgeops/2026.2/quick/*.md | references/snapshots/quick.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.
