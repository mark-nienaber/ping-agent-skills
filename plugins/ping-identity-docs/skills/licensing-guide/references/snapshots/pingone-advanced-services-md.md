---
title: PingOne Advanced Services
description: Licensing for PingOne Advanced Services, a dedicated SaaS platform, covering supported products, identity-based usage measures, and infrastructure add-ons.
component: licensing-guide
page_id: licensing-guide::pingone-advanced-services
canonical_url: https://docs.pingidentity.com/licensing-guide/pingone-advanced-services.html
llms_txt: https://docs.pingidentity.com/licensing-guide/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  infrastructure-add-ons: Infrastructure add-ons
---

# PingOne Advanced Services

PingOne Advanced Services is deployed as a **dedicated SaaS platform tenant** with a separate platform fee SKU. The following **software products** can be added into your environment:

* PingAccess

* PingCentral

* PingDirectory

* PingFederate

You can find more information in the [Ping Identity software](https://docs.pingidentity.com/software.html) documentation.

* By default, you receive a dedicated tenant with two environments (Dev and Production) operated by Ping Identity.

* PingOne Advanced Services is licensed with **identity-based units of measure**: **Annual Active User (AAU)** or **Monthly Active User (MAU)**.

An **Annual Active User (AAU)** is a **unique identity** that is **active at least once** during a **365-day period** starting at the license start date.

* *Active* means at least one qualifying identity operation during the year, such as sign-on or authentication, token issuance, token validation, token refresh, password set, password change, or another identity operation explicitly covered in the Product Terms.

* Each identity is counted **once per contract year**, regardless of how many times it authenticates.

A **Monthly Active User (MAU)** is a unique identity that is **active at least once** in a given **calendar month**.

* *Active* means the identity is processed at least once by the product during that month, such as sign-on, token issuance, token validation, or password change.

**Annual Average Monthly Active User (AAMAU)** is an active-user metric based on the 365-day period starting on the license start date. An active user is a unique identity record processed at least once during the time period. AAMAU is the average of the 12 MAU values for the 12 months of each contract year.

* Platform health, environment details, and key operational metrics are surfaced through the **PingOne Advanced Services dashboard**, with further usage and configuration details available in the underlying product admin consoles.

* Licensed identities in the production environment count fully against your contracted limits, while non-production environments are intended for development and testing under the fair-use policies outlined in the [Product Specific Terms and Conditions](https://www.pingidentity.com/en/legal/product-terms.html).

## Infrastructure add-ons

| Add-on                                                                                                                                                                       | Description                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Additional Test Environment](https://docs.pingidentity.com/pingoneadvancedservices/environments/p1as_environments.html)                                                     | Extra non-production test environment used for development and functional testing separate from staging and production.                                                                            |
| [Additional Stage Environment](https://docs.pingidentity.com/pingoneadvancedservices/environments/p1as_environments.html)                                                    | Extra pre-production staging tenant that mirrors production for performance, load, and go-live rehearsals, allowing parallel staging alongside your primary non-production chain.                  |
| [Additional Region](https://docs.pingidentity.com/pingoneadvancedservices/network_guide/p1as_network_guide.html)                                                             | Adds an additional cloud region for your PingOne Advanced Services deployment beyond the base region, typically used for geo expansion, latency reduction, or regulatory and data-residency needs. |
| [Weekend Upgrade SKU](https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_platform_upgrades.html)                                                  | Allows requested platform upgrades to a production tenant over a weekend instead of during the normal window.                                                                                      |
| [Disaster Recovery Testing in Staging Environment](https://docs.pingidentity.com/pingoneadvancedservices/introduction_to_pingone_advanced_services/p1as_regulations.html)    | Disaster recovery test add-on for a staging environment. Includes one inter-regional disaster recovery test per year using automatic failover between regions.                                     |
| [Disaster Recovery Testing in Production Environment](https://docs.pingidentity.com/pingoneadvancedservices/introduction_to_pingone_advanced_services/p1as_regulations.html) | Disaster recovery test add-on for a production environment. Includes one inter-regional disaster recovery test per year using automatic failover between regions.                                  |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can review your current licenses and entitlements in the Ping Identity Support Portal. After signing on, go to the Licensing section. From this page, you can also access your support keys and open a support case if anything about your entitlements appears incorrect.You can find more information in Ping Identity's legal [Product terms and conditions](https://www.pingidentity.com/en/legal/product-terms.html). |