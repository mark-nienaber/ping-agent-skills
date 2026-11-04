---
name: configuration-guides
description: "Use when the user explicitly names Configuration Guides or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Configuration Guides

Assign the Grafana Admin role to users via PingOne SAML assertion attribute mapping during authentication.

## Live source of truth

- Product docs: https://docs.pingidentity.com/configuration_guides/
- llms.txt index: https://docs.pingidentity.com/configuration_guides/llms.txt
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
| Amazon: grafana, amazon, managed | amazon | https://docs.pingidentity.com/configuration_guides/amazon/*.md | references/snapshots/amazon.md |
| Github: enterprise, github, initiated | github | https://docs.pingidentity.com/configuration_guides/github/*.md | references/snapshots/github.md |
| Salesforce: initiated, salesforce, sign | salesforce | https://docs.pingidentity.com/configuration_guides/salesforce/*.md | references/snapshots/salesforce.md |
| Tableau: tableau, initiated, pingfederate | tableau | https://docs.pingidentity.com/configuration_guides/tableau/*.md | references/snapshots/tableau.md |
| Atlassian Cloud: atlassian, cloud, saml | atlassian_cloud | https://docs.pingidentity.com/configuration_guides/atlassian_cloud/*.md | references/snapshots/atlassian-cloud.md |
| Bamboohr: bamboohr, saml, sso | bamboohr | https://docs.pingidentity.com/configuration_guides/bamboohr/*.md | references/snapshots/bamboohr.md |
| Box: box, initiated, saml | box | https://docs.pingidentity.com/configuration_guides/box/*.md | references/snapshots/box.md |
| Coupa: coupa, initiated, saml | coupa | https://docs.pingidentity.com/configuration_guides/coupa/*.md | references/snapshots/coupa.md |
| Docusign: docusign, initiated, saml | docusign | https://docs.pingidentity.com/configuration_guides/docusign/*.md | references/snapshots/docusign.md |
| Dropbox: dropbox, initiated, saml | dropbox | https://docs.pingidentity.com/configuration_guides/dropbox/*.md | references/snapshots/dropbox.md |
| Egnyte: egnyte, initiated, saml | egnyte | https://docs.pingidentity.com/configuration_guides/egnyte/*.md | references/snapshots/egnyte.md |
| Evernote: evernote, initiated, saml | evernote | https://docs.pingidentity.com/configuration_guides/evernote/*.md | references/snapshots/evernote.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.
