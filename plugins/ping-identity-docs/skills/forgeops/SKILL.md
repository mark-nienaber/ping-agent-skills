---
name: forgeops
description: "Use when deploying PingOne AIC or ForgeRock software with ForgeOps, including Kubernetes setup, customization, backup, upgrade, troubleshooting, and deployment reference. Routes to live docs; snapshots fallback."
license: MIT
---

# ForgeOps

ForgeOps documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/forgeops/
- llms.txt index: https://docs.pingidentity.com/forgeops/llms.txt
- Snapshot version: 2026.2
- Snapshot manifest: references/MANIFEST.md

## Fetch strategy

1. Read references/llms.txt for page discovery.
2. Match the user task to page titles, page descriptions, and the routing table below.
3. Fetch the selected live `.md` URL from Ping documentation.
4. If live fetch is unavailable, read the closest file under references/snapshots/.

## Task routing

| Task category | Guide slug | Live URL pattern | Snapshot |
|---|---|---|---|
| Prepare: deployment, monitoring, pinggateway | prepare | https://docs.pingidentity.com/forgeops/2026.2/prepare/*.md | references/snapshots/prepare.md |
| Reference: forgeops, command, span | reference | https://docs.pingidentity.com/forgeops/2026.2/reference/*.md | references/snapshots/reference.md |
| Deploy: deploy, deployment, forgeops | deploy | https://docs.pingidentity.com/forgeops/2026.2/deploy/*.md | references/snapshots/deploy.md |
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

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.
