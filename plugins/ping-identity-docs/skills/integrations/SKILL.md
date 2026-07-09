---
name: integrations
description: "Use when working with Integrations: pingone, amazon, google, azure, atlassian, github. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# Integrations

Descriptions of standard and advanced fields that you can configure for the Akamai Account Protector IdP Adapter.

## Live source of truth

- Product docs: https://docs.pingidentity.com/integrations/
- llms.txt index: https://docs.pingidentity.com/integrations/llms.txt
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
| Pingone: adding, authentication, based | pingone | https://docs.pingidentity.com/integrations/pingone/*.md | references/snapshots/pingone.md |
| Amazon: amazon, aws, configuring | amazon | https://docs.pingidentity.com/integrations/amazon/*.md | references/snapshots/amazon.md |
| Google: configuring, deploying, download | google | https://docs.pingidentity.com/integrations/google/*.md | references/snapshots/google.md |
| Azure: configuring, azure, adapter | azure | https://docs.pingidentity.com/integrations/azure/*.md | references/snapshots/azure.md |
| Atlassian: configuring, atlassian, configuration | atlassian | https://docs.pingidentity.com/integrations/atlassian/*.md | references/snapshots/atlassian.md |
| Github: provisioning, pingfederate, configure | github | https://docs.pingidentity.com/integrations/github/*.md | references/snapshots/github.md |
| Salesforce: provisioning, sso, enabling | salesforce | https://docs.pingidentity.com/integrations/salesforce/*.md | references/snapshots/salesforce.md |
| Java: configuration, sample, applications | java | https://docs.pingidentity.com/integrations/java/*.md | references/snapshots/java.md |
| Facebook: configuring, pingfederate, provisioning | facebook | https://docs.pingidentity.com/integrations/facebook/*.md | references/snapshots/facebook.md |
| Zscaler: sign, single, enabling | zscaler | https://docs.pingidentity.com/integrations/zscaler/*.md | references/snapshots/zscaler.md |
| Office365: configure, provisioning, add | office365 | https://docs.pingidentity.com/integrations/office365/*.md | references/snapshots/office365.md |
| Webaccessmanagement: configuring, custom, idp | webAccessManagement | https://docs.pingidentity.com/integrations/webAccessManagement/*.md | references/snapshots/webaccessmanagement.md |
| Agentless: integration, attribute, configuring | agentless | https://docs.pingidentity.com/integrations/agentless/*.md | references/snapshots/agentless.md |
| Php: deploying, sample, configuring | php | https://docs.pingidentity.com/integrations/php/*.md | references/snapshots/php.md |
| Slack: slack, sign, single | slack | https://docs.pingidentity.com/integrations/slack/*.md | references/snapshots/slack.md |
| Duosecurity: duo, security, adapter | duosecurity | https://docs.pingidentity.com/integrations/duosecurity/*.md | references/snapshots/duosecurity.md |
| Coreblox: coreblox, adapter, configuring | coreblox | https://docs.pingidentity.com/integrations/coreblox/*.md | references/snapshots/coreblox.md |
| Apache: apache, agent, session | apache | https://docs.pingidentity.com/integrations/apache/*.md | references/snapshots/apache.md |
| Net: integration, single, opentoken | net | https://docs.pingidentity.com/integrations/net/*.md | references/snapshots/net.md |
| Zendesk: zendesk, obtain, pingfederate | zendesk | https://docs.pingidentity.com/integrations/zendesk/*.md | references/snapshots/zendesk.md |
| Zoom: pingfederate, sign, single | zoom | https://docs.pingidentity.com/integrations/zoom/*.md | references/snapshots/zoom.md |
| Box: box, configure, sso | box | https://docs.pingidentity.com/integrations/box/*.md | references/snapshots/box.md |
| Contentful: pingfederate, sign, single | contentful | https://docs.pingidentity.com/integrations/contentful/*.md | references/snapshots/contentful.md |
| Sharepoint Peoplepicker: configuration, search, people | sharepoint-peoplepicker | https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/*.md | references/snapshots/sharepoint-peoplepicker.md |
| Aquera: pingfederate, sign, single | aquera | https://docs.pingidentity.com/integrations/aquera/*.md | references/snapshots/aquera.md |
| Coupa: coupa, sso, obtaining | coupa | https://docs.pingidentity.com/integrations/coupa/*.md | references/snapshots/coupa.md |
| Scim: pingfederate, provisioning, sign | scim | https://docs.pingidentity.com/integrations/scim/*.md | references/snapshots/scim.md |
| X509: integration, adapter, certificate | x509 | https://docs.pingidentity.com/integrations/x509/*.md | references/snapshots/x509.md |
| Iddataweb: dataweb, device, profiling | iddataweb | https://docs.pingidentity.com/integrations/iddataweb/*.md | references/snapshots/iddataweb.md |
| Oam: configuration, idp, adapter | oam | https://docs.pingidentity.com/integrations/oam/*.md | references/snapshots/oam.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.
