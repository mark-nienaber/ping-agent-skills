---
name: pingdirectory
description: "Use when the user explicitly names PingDirectory or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingDirectory

Landing page for the PingDirectory suite (PingDirectory, PingDirectoryProxy, PingDataSync, Delegated Admin) with links to release notes, get-started, admin, troubleshooting, and support resources.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingdirectory/
- llms.txt index: https://docs.pingidentity.com/pingdirectory/llms.txt
- Snapshot version: 11.1
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
| Pingdirectory Server Administration Guide: about, pingdirectory, attribute | pingdirectory_server_administration_guide | https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/*.md | references/snapshots/pingdirectory-server-administration-guide.md |
| Pingdirectory Security Guide: pingdirectory, understand, aci | pingdirectory_security_guide | https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/*.md | references/snapshots/pingdirectory-security-guide.md |
| Pingdirectoryproxy Server Administration Guide: about, pingdirectoryproxy, understand | pingdirectoryproxy_server_administration_guide | https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/*.md | references/snapshots/pingdirectoryproxy-server-administration-guide.md |
| Pingdatasync Server Administration Guide: sync, pingdatasync, configure | pingdatasync_server_administration_guide | https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/*.md | references/snapshots/pingdatasync-server-administration-guide.md |
| Installing The Pingdirectory Suite Of Products: pingdirectory, server, installing | installing_the_pingdirectory_suite_of_products | https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/*.md | references/snapshots/installing-the-pingdirectory-suite-of-products.md |
| Delegated Admin Application Guide: delegated, admin, configuring | delegated_admin_application_guide | https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/*.md | references/snapshots/delegated-admin-application-guide.md |
| Troubleshooting The Pingdirectory Suite Of Products: server, pingdirectory, pingdatasync | troubleshooting_the_pingdirectory_suite_of_products | https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/*.md | references/snapshots/troubleshooting-the-pingdirectory-suite-of-products.md |
| Managing Servers And Certificates: pingdirectory, certificate, certificates | managing_servers_and_certificates | https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/*.md | references/snapshots/managing-servers-and-certificates.md |
| Consent Solution Guide: consent, service, pingdirectory | consent_solution_guide | https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/*.md | references/snapshots/consent-solution-guide.md |
| Managing Access Control: access, pingdirectory, token | managing_access_control | https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/*.md | references/snapshots/managing-access-control.md |
| Monitoring The Pingdirectory Suite Of Products: monitoring, pingdirectory, server | monitoring_the_pingdirectory_suite_of_products | https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/*.md | references/snapshots/monitoring-the-pingdirectory-suite-of-products.md |
| Managing Scim: scim, pingdirectoryproxy, ldap | managing_scim | https://docs.pingidentity.com/pingdirectory/11.1/managing_scim/*.md | references/snapshots/managing-scim.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.
