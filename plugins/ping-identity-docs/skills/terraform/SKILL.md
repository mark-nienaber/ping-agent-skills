---
name: terraform
description: "Use when automating Ping configuration with Terraform, including provider setup, products, best practices, configuration examples, pipelines, and infrastructure workflows. Routes to live docs; snapshots fallback."
license: MIT
---

# Terraform

Terraform documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://developer.pingidentity.com/terraform/
- llms.txt index: https://developer.pingidentity.com/terraform/llms.txt
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
| Products: asked, frequently, getting | products | https://developer.pingidentity.com/terraform/products/*.md | references/snapshots/products.md |
| Develop With Terraform: terraform, configuration, exporting | develop_with_terraform | https://developer.pingidentity.com/terraform/develop_with_terraform/*.md | references/snapshots/develop-with-terraform.md |
| Terraform At Ping: terraform, benefits, deployments | terraform_at_ping | https://developer.pingidentity.com/terraform/terraform_at_ping/*.md | references/snapshots/terraform-at-ping.md |
| Best Practices.Md: best, practices | best_practices.md | https://developer.pingidentity.com/terraform/best_practices.md/*.md | references/snapshots/best-practices-md.md |
| Develop With Terraform.Md: develop, terraform | develop_with_terraform.md | https://developer.pingidentity.com/terraform/develop_with_terraform.md/*.md | references/snapshots/develop-with-terraform-md.md |
| Terraform Landing Page.Md: identity, terraform | terraform_landing_page.md | https://developer.pingidentity.com/terraform/terraform_landing_page.md/*.md | references/snapshots/terraform-landing-page-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.
