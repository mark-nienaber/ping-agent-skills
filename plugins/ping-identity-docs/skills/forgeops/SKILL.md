---
name: forgeops
description: "Use when the user explicitly names ForgeOps or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# ForgeOps

Manage PingAM and PingIDM static and dynamic configuration, exports, and configuration profiles in ForgeOps.

## Live source of truth

- Product docs: https://docs.pingidentity.com/forgeops/
- llms.txt index: https://docs.pingidentity.com/forgeops/llms.txt
- Snapshot version: 2026.3
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
| Prepare: forgeops, secrets, deployment | prepare | https://docs.pingidentity.com/forgeops/2026.3/prepare/*.md | references/snapshots/prepare.md |
| Reference: forgeops, command, benchmarks | reference | https://docs.pingidentity.com/forgeops/2026.3/reference/*.md | references/snapshots/reference.md |
| Troubleshoot: forgeops, code, troubleshoot | troubleshoot | https://docs.pingidentity.com/forgeops/2026.3/troubleshoot/*.md | references/snapshots/troubleshoot.md |
| Deploy: forgeops, deploy, deployment | deploy | https://docs.pingidentity.com/forgeops/2026.3/deploy/*.md | references/snapshots/deploy.md |
| Customize: code, configuration, images | customize | https://docs.pingidentity.com/forgeops/2026.3/customize/*.md | references/snapshots/customize.md |
| Start: forgeops, kubernetes, release | start | https://docs.pingidentity.com/forgeops/2026.3/start/*.md | references/snapshots/start.md |
| Upgrade: forgeops, upgrade, migrate | upgrade | https://docs.pingidentity.com/forgeops/2026.3/upgrade/*.md | references/snapshots/upgrade.md |
| Rn: forgeops, limitations, review | rn | https://docs.pingidentity.com/forgeops/2026.3/rn/*.md | references/snapshots/rn.md |
| Setup: forgeops, local, tools | setup | https://docs.pingidentity.com/forgeops/2026.3/setup/*.md | references/snapshots/setup.md |
| Backup: backup, backups, dsbackup | backup | https://docs.pingidentity.com/forgeops/2026.3/backup/*.md | references/snapshots/backup.md |
| Integration: forgeops, pingone, integrate | integration | https://docs.pingidentity.com/forgeops/2026.3/integration/*.md | references/snapshots/integration.md |
| Root: forgeops, advanced, consolidated | root | https://docs.pingidentity.com/forgeops/2026.3/*.md | references/snapshots/root.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.
