---
name: helm
description: "Use when the user explicitly names Helm Charts or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Helm Charts

Configure replica count, resource limits, node placement, and liveness, readiness, and startup probes for Ping Identity Helm chart workloads.

## Live source of truth

- Product docs: https://developer.pingidentity.com/helm/
- llms.txt index: https://developer.pingidentity.com/helm/llms.txt
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
| Configs: helm, identity, chart | configs | https://developer.pingidentity.com/helm/configs/*.md | references/snapshots/configs.md |
| Examples: helm, examples, gateway | examples | https://developer.pingidentity.com/helm/examples/*.md | references/snapshots/examples.md |
| Getting Started: identity, devops, helm | getting-started | https://developer.pingidentity.com/helm/getting-started/*.md | references/snapshots/getting-started.md |
| Release Notes: chart, current, devops | release-notes | https://developer.pingidentity.com/helm/release-notes/*.md | references/snapshots/release-notes.md |
| Helm Charts Landing Page.Md: helm, charts, devops | helm-charts-landing-page.md | https://developer.pingidentity.com/helm/helm-charts-landing-page.md | references/snapshots/helm-charts-landing-page-md.md |
| How To: image, product, tags | how-to | https://developer.pingidentity.com/helm/how-to/*.md | references/snapshots/how-to.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.
