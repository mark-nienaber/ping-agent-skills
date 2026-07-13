---
name: devops
description: "Use when the user explicitly names DevOps or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# DevOps

DevOps documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://developer.pingidentity.com/devops/
- llms.txt index: https://developer.pingidentity.com/devops/llms.txt
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
| Docker Images: untitled, docker, base | docker-images | https://developer.pingidentity.com/devops/docker-images/*.md | references/snapshots/docker-images.md |
| Release Notes: version | release-notes | https://developer.pingidentity.com/devops/release-notes/*.md | references/snapshots/release-notes.md |
| How To: pingdirectory, profiles, server | how-to | https://developer.pingidentity.com/devops/how-to/*.md | references/snapshots/how-to.md |
| Deployment: deploy, cluster, kubernetes | deployment | https://developer.pingidentity.com/devops/deployment/*.md | references/snapshots/deployment.md |
| Reference: basics, configuration, application | reference | https://developer.pingidentity.com/devops/reference/*.md | references/snapshots/reference.md |
| Get Started: deploy, example, stack | get-started | https://developer.pingidentity.com/devops/get-started/*.md | references/snapshots/get-started.md |
| Home: devops, disclaimer, license | home | https://developer.pingidentity.com/devops/home/*.md | references/snapshots/home.md |
| Tools: pingctl, code, utility | tools | https://developer.pingidentity.com/devops/tools/*.md | references/snapshots/tools.md |
| Contact Us: community, contributing | contact-us | https://developer.pingidentity.com/devops/contact-us/*.md | references/snapshots/contact-us.md |
| Docker Builds: builds, docker, hooks | docker-builds | https://developer.pingidentity.com/devops/docker-builds/*.md | references/snapshots/docker-builds.md |
| Devops Landing Page.Md: devops, identity | devops-landing-page.md | https://developer.pingidentity.com/devops/devops-landing-page.md | references/snapshots/devops-landing-page-md.md |
| Overview.Md: overview | overview.md | https://developer.pingidentity.com/devops/overview.md | references/snapshots/overview-md.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.
