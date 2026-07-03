---
name: helm
description: "Use when deploying Ping products with Helm charts, including chart configuration, examples, values, getting started, release notes, and Kubernetes deployment patterns. Routes to live docs; snapshots fallback."
license: MIT
---

# Helm Charts

Helm Charts documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://developer.pingidentity.com/helm/
- llms.txt index: https://developer.pingidentity.com/helm/llms.txt
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
| Configs: configuration, image, values | configs | https://developer.pingidentity.com/helm/configs/*.md | references/snapshots/configs.md |
| Examples: examples, chart, csi | examples | https://developer.pingidentity.com/helm/examples/*.md | references/snapshots/examples.md |
| Getting Started: contributing, devops, getting | getting-started | https://developer.pingidentity.com/helm/getting-started/*.md | references/snapshots/getting-started.md |
| Release Notes: current, previous, release | release-notes | https://developer.pingidentity.com/helm/release-notes/*.md | references/snapshots/release-notes.md |
| Helm Charts Landing Page.Md: welcome | helm-charts-landing-page.md | https://developer.pingidentity.com/helm/helm-charts-landing-page.md/*.md | references/snapshots/helm-charts-landing-page-md.md |
| How To: image, product, tags | how-to | https://developer.pingidentity.com/helm/how-to/*.md | references/snapshots/how-to.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.
