---
name: pingdirectory
description: "Use when administering PingDirectory, PingDirectoryProxy, PingDataSync, delegated admin, consent, server configuration, security, installation, upgrades, and troubleshooting. Routes to live docs; snapshots fallback."
license: MIT
---

# PingDirectory

Configure a Kafka sync source to consume change events from a Kafka topic and apply them to a sync destination.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingdirectory/
- llms.txt index: https://docs.pingidentity.com/pingdirectory/llms.txt
- Snapshot version: 11.1
- Snapshot manifest: references/MANIFEST.md

## Fetch strategy

1. Read references/llms.txt for page discovery.
2. Match the user task to page titles, page descriptions, and the routing table below.
3. Fetch the selected live `.md` URL from Ping documentation.
4. If live fetch is unavailable, read the closest file under references/snapshots/.

## Task routing

| Task category | Guide slug | Live URL pattern | Snapshot |
|---|---|---|---|
| Pingdirectory Server Administration Guide: about, managing, attribute | pingdirectory_server_administration_guide | https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/*.md | references/snapshots/pingdirectory-server-administration-guide.md |
| Pingdirectory Security Guide: aci, auditing, account | pingdirectory_security_guide | https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/*.md | references/snapshots/pingdirectory-security-guide.md |
| Pingdirectoryproxy Server Administration Guide: about, connection, log | pingdirectoryproxy_server_administration_guide | https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/*.md | references/snapshots/pingdirectoryproxy-server-administration-guide.md |
| Pingdatasync Server Administration Guide: sync, configure, configuration | pingdatasync_server_administration_guide | https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/*.md | references/snapshots/pingdatasync-server-administration-guide.md |
| Installing The Pingdirectory Suite Of Products: installing, installation, server | installing_the_pingdirectory_suite_of_products | https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/*.md | references/snapshots/installing-the-pingdirectory-suite-of-products.md |
| Troubleshooting The Pingdirectory Suite Of Products: problems, server, information | troubleshooting_the_pingdirectory_suite_of_products | https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/*.md | references/snapshots/troubleshooting-the-pingdirectory-suite-of-products.md |
| Delegated Admin Application Guide: configuring, delegated, admin | delegated_admin_application_guide | https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/*.md | references/snapshots/delegated-admin-application-guide.md |
| Managing Servers And Certificates: certificate, certificates, enabling | managing_servers_and_certificates | https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/*.md | references/snapshots/managing-servers-and-certificates.md |
| Consent Solution Guide: consent, configuring, service | consent_solution_guide | https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/*.md | references/snapshots/consent-solution-guide.md |
| Managing Access Control: access, token, control | managing_access_control | https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/*.md | references/snapshots/managing-access-control.md |
| Monitoring The Pingdirectory Suite Of Products: monitoring, snmp, configuring | monitoring_the_pingdirectory_suite_of_products | https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/*.md | references/snapshots/monitoring-the-pingdirectory-suite-of-products.md |
| Managing Scim 11 And 20 Servlet Extensions: scim, extension, operations | managing_scim_11_and_20_servlet_extensions | https://docs.pingidentity.com/pingdirectory/11.1/managing_scim_11_and_20_servlet_extensions/*.md | references/snapshots/managing-scim-11-and-20-servlet-extensions.md |
| Root: server, introduction, pingdirectory | root | https://docs.pingidentity.com/pingdirectory/11.1/*.md | references/snapshots/root.md |
| Fips 140 2 Compliance For Pingdirectory: fips, compliant, comparison | fips_140-2_compliance_for_pingdirectory | https://docs.pingidentity.com/pingdirectory/11.1/fips_140-2_compliance_for_pingdirectory/*.md | references/snapshots/fips-140-2-compliance-for-pingdirectory.md |
| Release Notes: notes, release | release_notes | https://docs.pingidentity.com/pingdirectory/11.1/release_notes/*.md | references/snapshots/release-notes.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.
