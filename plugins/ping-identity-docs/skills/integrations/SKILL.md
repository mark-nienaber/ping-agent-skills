---
name: integrations
description: "Use when the user explicitly names Integrations or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Integrations

Descriptions of standard and advanced fields that you can configure for the Akamai Account Protector IdP Adapter.

## Live source of truth

- Product docs: https://docs.pingidentity.com/integrations/
- llms.txt index: https://docs.pingidentity.com/integrations/llms.txt
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
| Pingone: adding, authentication, based | pingone | https://docs.pingidentity.com/integrations/pingone/*.md | references/snapshots/pingone.md |
| Amazon: amazon, aws, configuring | amazon | https://docs.pingidentity.com/integrations/amazon/*.md | references/snapshots/amazon.md |
| Google: configuring, deploying, download | google | https://docs.pingidentity.com/integrations/google/*.md | references/snapshots/google.md |
| Azure: configuring, azure, adapter | azure | https://docs.pingidentity.com/integrations/azure/*.md | references/snapshots/azure.md |
| Atlassian: configuring, atlassian, configuration | atlassian | https://docs.pingidentity.com/integrations/atlassian/*.md | references/snapshots/atlassian.md |
| Github: provisioning, pingfederate, configure | github | https://docs.pingidentity.com/integrations/github/*.md | references/snapshots/github.md |
| Salesforce: provisioning, sso, enabling | salesforce | https://docs.pingidentity.com/integrations/salesforce/*.md | references/snapshots/salesforce.md |
| Net: configuring, integration, opentoken | net | https://docs.pingidentity.com/integrations/net/*.md | references/snapshots/net.md |
| Java: configuration, sample, applications | java | https://docs.pingidentity.com/integrations/java/*.md | references/snapshots/java.md |
| Facebook: configuring, pingfederate, provisioning | facebook | https://docs.pingidentity.com/integrations/facebook/*.md | references/snapshots/facebook.md |
| Zscaler: sign, single, enabling | zscaler | https://docs.pingidentity.com/integrations/zscaler/*.md | references/snapshots/zscaler.md |
| Office365: configure, provisioning, add | office365 | https://docs.pingidentity.com/integrations/office365/*.md | references/snapshots/office365.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.
