---
name: connectors
description: "Use when the user explicitly names Connectors or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Connectors

Configure the AbuseIPDB connector in PingOne DaVinci to check whether an IP address has been associated with malicious activity and branch on the abuse confidence score.

## Live source of truth

- Product docs: https://docs.pingidentity.com/connectors/
- llms.txt index: https://docs.pingidentity.com/connectors/llms.txt
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
| Relnotes: davinci, notes, pingone | relnotes | https://docs.pingidentity.com/connectors/relnotes/*.md | references/snapshots/relnotes.md |
| Type: connectors, pingone, davinci | type | https://docs.pingidentity.com/connectors/type/*.md | references/snapshots/type.md |
| Abuseipdb Connector.Md: abuseipdb, connector, abuse | abuseipdb_connector.md | https://docs.pingidentity.com/connectors/abuseipdb_connector.md | references/snapshots/abuseipdb-connector-md.md |
| Accertify Connector.Md: accertify, connector, configure | accertify_connector.md | https://docs.pingidentity.com/connectors/accertify_connector.md | references/snapshots/accertify-connector-md.md |
| Adobe Experience Manager Connector.Md: adobe, experience, connector | adobe_experience_manager_connector.md | https://docs.pingidentity.com/connectors/adobe_experience_manager_connector.md | references/snapshots/adobe-experience-manager-connector-md.md |
| Akamai Account Protector Connector.Md: akamai, account, connector | akamai_account_protector_connector.md | https://docs.pingidentity.com/connectors/akamai_account_protector_connector.md | references/snapshots/akamai-account-protector-connector-md.md |
| Apple Login Connector.Md: apple, connector, login | apple_login_connector.md | https://docs.pingidentity.com/connectors/apple_login_connector.md | references/snapshots/apple-login-connector-md.md |
| Authentication Connector.Md: authentication, connector, use | authentication_connector.md | https://docs.pingidentity.com/connectors/authentication_connector.md | references/snapshots/authentication-connector-md.md |
| Authenticid Connector.Md: authenticid, connector, capture | authenticid_connector.md | https://docs.pingidentity.com/connectors/authenticid_connector.md | references/snapshots/authenticid-connector-md.md |
| Aws S3 Connector.Md: aws, connector, amazon | aws_s3_connector.md | https://docs.pingidentity.com/connectors/aws_s3_connector.md | references/snapshots/aws-s3-connector-md.md |
| Aws Secrets Manager Connector.Md: secrets, aws, manager | aws_secrets_manager_connector.md | https://docs.pingidentity.com/connectors/aws_secrets_manager_connector.md | references/snapshots/aws-secrets-manager-connector-md.md |
| Azure Ad User Management Connector.Md: azure, connector, management | azure_ad_user_management_connector.md | https://docs.pingidentity.com/connectors/azure_ad_user_management_connector.md | references/snapshots/azure-ad-user-management-connector-md.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.
