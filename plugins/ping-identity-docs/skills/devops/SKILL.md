---
name: devops
description: "Use when working with DevOps: docker images, release notes, how to, deployment, reference, get started. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# DevOps

DevOps documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://developer.pingidentity.com/devops/
- llms.txt index: https://developer.pingidentity.com/devops/llms.txt
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
| Readme.Md: welcome | README.md | https://developer.pingidentity.com/devops/README.md | references/snapshots/readme-md.md |
| Videos: videos | videos | https://developer.pingidentity.com/devops/videos/*.md | references/snapshots/videos.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.
