---
name: terraform
description: "Use when the user explicitly names Terraform or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Terraform

Terraform documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://developer.pingidentity.com/terraform/
- llms.txt index: https://developer.pingidentity.com/terraform/llms.txt
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
| Products: asked, frequently, getting | products | https://developer.pingidentity.com/terraform/products/*.md | references/snapshots/products.md |
| Develop With Terraform: terraform, configuration, exporting | develop_with_terraform | https://developer.pingidentity.com/terraform/develop_with_terraform/*.md | live-only |
| Terraform At Ping: terraform, benefits, deployments | terraform_at_ping | https://developer.pingidentity.com/terraform/terraform_at_ping/*.md | live-only |
| Best Practices.Md: best, practices | best_practices.md | https://developer.pingidentity.com/terraform/best_practices.md | live-only |
| Develop With Terraform.Md: develop, terraform | develop_with_terraform.md | https://developer.pingidentity.com/terraform/develop_with_terraform.md | live-only |
| Terraform Landing Page.Md: identity, terraform | terraform_landing_page.md | https://developer.pingidentity.com/terraform/terraform_landing_page.md | live-only |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.
