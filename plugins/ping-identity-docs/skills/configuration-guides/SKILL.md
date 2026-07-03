---
name: configuration-guides
description: "Use when configuring third-party application integrations with Ping, including SAML, OIDC, SaaS app setup, provisioning, certificates, attribute mapping, or vendor-specific SSO guides. Routes to live docs; snapshots fallback."
license: MIT
---

# Configuration Guides

Configuration Guides documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/configuration_guides/
- llms.txt index: https://docs.pingidentity.com/configuration_guides/llms.txt
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
| Amazon: amazon, grafana, managed | amazon | https://docs.pingidentity.com/configuration_guides/amazon/*.md | references/snapshots/amazon.md |
| Github: configuring, enterprise, github | github | https://docs.pingidentity.com/configuration_guides/github/*.md | references/snapshots/github.md |
| Salesforce: salesforce, sign, configure | salesforce | https://docs.pingidentity.com/configuration_guides/salesforce/*.md | references/snapshots/salesforce.md |
| Tableau: configuring, tableau, pingfederate | tableau | https://docs.pingidentity.com/configuration_guides/tableau/*.md | references/snapshots/tableau.md |
| Atlassian Cloud: atlassian, cloud, configuring | atlassian_cloud | https://docs.pingidentity.com/configuration_guides/atlassian_cloud/*.md | references/snapshots/atlassian-cloud.md |
| Bamboohr: bamboohr, configuring, saml | bamboohr | https://docs.pingidentity.com/configuration_guides/bamboohr/*.md | references/snapshots/bamboohr.md |
| Box: box, configuring, saml | box | https://docs.pingidentity.com/configuration_guides/box/*.md | references/snapshots/box.md |
| Coupa: configuring, coupa, saml | coupa | https://docs.pingidentity.com/configuration_guides/coupa/*.md | references/snapshots/coupa.md |
| Docusign: configuring, docusign, saml | docusign | https://docs.pingidentity.com/configuration_guides/docusign/*.md | references/snapshots/docusign.md |
| Dropbox: configuring, dropbox, saml | dropbox | https://docs.pingidentity.com/configuration_guides/dropbox/*.md | references/snapshots/dropbox.md |
| Egnyte: configuring, egnyte, saml | egnyte | https://docs.pingidentity.com/configuration_guides/egnyte/*.md | references/snapshots/egnyte.md |
| Evernote: configuring, evernote, saml | evernote | https://docs.pingidentity.com/configuration_guides/evernote/*.md | references/snapshots/evernote.md |
| Hubspot: configuring, hubspot, saml | hubspot | https://docs.pingidentity.com/configuration_guides/hubspot/*.md | references/snapshots/hubspot.md |
| Jamf: configuring, jamf, pro | jamf | https://docs.pingidentity.com/configuration_guides/jamf/*.md | references/snapshots/jamf.md |
| Jira Confluence: configuring, confluence, jira | jira_confluence | https://docs.pingidentity.com/configuration_guides/jira_confluence/*.md | references/snapshots/jira-confluence.md |
| Jive: configuring, jive, saml | jive | https://docs.pingidentity.com/configuration_guides/jive/*.md | references/snapshots/jive.md |
| Marketo: configuring, marketo, saml | marketo | https://docs.pingidentity.com/configuration_guides/marketo/*.md | references/snapshots/marketo.md |
| Microsoft 365: configuring, microsoft, saml | microsoft_365 | https://docs.pingidentity.com/configuration_guides/microsoft_365/*.md | references/snapshots/microsoft-365.md |
| Mimecast: configuring, mimecast, saml | mimecast | https://docs.pingidentity.com/configuration_guides/mimecast/*.md | references/snapshots/mimecast.md |
| Namely: configuring, namely, saml | namely | https://docs.pingidentity.com/configuration_guides/namely/*.md | references/snapshots/namely.md |
| Sap Netweaver: configuring, netweaver, saml | sap_netweaver | https://docs.pingidentity.com/configuration_guides/sap_netweaver/*.md | references/snapshots/sap-netweaver.md |
| Slack: configuring, saml, slack | slack | https://docs.pingidentity.com/configuration_guides/slack/*.md | references/snapshots/slack.md |
| Splunk: cloud, configuring, saml | splunk | https://docs.pingidentity.com/configuration_guides/splunk/*.md | references/snapshots/splunk.md |
| Successfactors: configuring, saml, sso | successfactors | https://docs.pingidentity.com/configuration_guides/successfactors/*.md | references/snapshots/successfactors.md |
| Ultipro: configuring, saml, sso | ultipro | https://docs.pingidentity.com/configuration_guides/ultipro/*.md | references/snapshots/ultipro.md |
| Workato: configuring, saml, sso | workato | https://docs.pingidentity.com/configuration_guides/workato/*.md | references/snapshots/workato.md |
| Workday: configuring, saml, sso | workday | https://docs.pingidentity.com/configuration_guides/workday/*.md | references/snapshots/workday.md |
| Zendesk: configuring, saml, sso | zendesk | https://docs.pingidentity.com/configuration_guides/zendesk/*.md | references/snapshots/zendesk.md |
| Adobe Creative Suite: adobe, cloud, configuring | adobe_creative_suite | https://docs.pingidentity.com/configuration_guides/adobe_creative_suite/*.md | references/snapshots/adobe-creative-suite.md |
| Aha! Ideas: aha, configuring, ideas | aha!_ideas | https://docs.pingidentity.com/configuration_guides/aha!_ideas/*.md | references/snapshots/aha-ideas.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.
