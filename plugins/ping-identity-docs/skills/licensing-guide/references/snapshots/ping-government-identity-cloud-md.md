---
title: Ping Government Identity Cloud
description: Licensing information for Ping Government Identity Cloud, including dedicated deployment options, managed identity unit of measure, add-ons, and Secure Containers.
component: licensing-guide
page_id: licensing-guide::ping-government-identity-cloud
canonical_url: https://docs.pingidentity.com/licensing-guide/ping-government-identity-cloud.html
llms_txt: https://docs.pingidentity.com/licensing-guide/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  add-ons: Add-ons
  secure-containers: Secure Containers
---

# Ping Government Identity Cloud

The following products are supported in Ping Government Identity Cloud:

* PingAccess

* PingAuthorize

* PingCentral

* PingDirectory

* PingFederate

* PingAM

* PingDS

* PingGateway

* PingIDM

* Governance

You can find more information about these products in the Ping Identity [software documentation](https://docs.pingidentity.com/software.html).

* By default, Ping Government Identity Cloud Cloud includes production and non-production environments.

  * Ping Government Identity Cloud Cloud environments are operated by Ping Identity with multiregion availability.

* If deployed through software or with Secure Containers, the products chosen can be deployed by the customer, a third party, or by Ping Identity.

* Ping Government Identity Cloud uses a **managed (stored) identity** unit of measure.

  * A managed (stored) identity is a **unique identifier** for a user, device, or other object that is **stored and managed** by the product, regardless of activity, such as the number of records or entries in the directory or identity store governed by the license.

  * Each stored identity is counted once per contract year and not by the number of times an activity is performed with that identity.

* Licensed identities in the production environment count fully against your contracted limits, while non-production environments are intended for development and testing under the fair-use policies outlined in the [Product Specific Terms and Conditions](https://www.pingidentity.com/en/legal/product-terms.html).

## Add-ons

| Add-on                                                                                                          | Description                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Additional Non-Production Environment](https://docs.pingidentity.com/pgic/environments/pgic_environments.html) | Extra non-production environment (Dev, Test, or Stage) beyond the default production and non-production pair, for additional development, user acceptance testing (UAT), or staging while preserving FedRAMP and Impact Level 5 (IL5) controls. |

## Secure Containers

**Secure Containers** are self-contained software packages that bundle specific Ping Identity software together with the operating system and required middleware, delivered as **hardened container images**. They are designed so customers can run Ping Government Identity Cloud-hardened images in their own infrastructure while benefiting from Ping Identity's security hardening and maintenance pipeline.

Secure Containers can be deployed on a **dedicated platform** with the option of adding the following **software products**:

* PingAccess

* PingAuthorize

* PingCentral

* PingDirectory

* PingFederate

* AM

* DS

* PingGateway

* IDM

* Governance

You can find more information in [Secure Containers](https://docs.pingidentity.com/pgic/secure-containers.html) documentation.

* Secure Containers are licensed per Ping Identity product and per customer segment. Customer segments include Workforce, CIAM, Partner, or other segments identified in the applicable order form. Secure Containers are not licensed by runtime replica, pod, or container instance count unless expressly stated in the order form.

* Customers in any vertical must first license the applicable **Ping Government Identity Cloud** software for the product they plan to run. Secure Containers are an add-on entitlement that provides additional container-related benefits and do not replace the underlying product, user, or identity-based license.

| Feature                       | Description                                                                                                                                                                                                                   |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hardened container images     | Security-hardened Docker images for PingAccess, PingAM, PingAuthorize, PingDirectory (including PingDataSync), PingCentral, PingDS, PingFederate, PingGateway, PingIDM, and Governance, with vetted dependencies and base OS. |
| Preconfigured best practices  | Images packaged with recommended configuration patterns, scripts, and orchestrations so you can follow Ping Identity's container best practices out of the box.                                                               |
| Consistent, repeatable builds | Standardized images from Ping Identity's DevOps program ensure consistent behavior across development, test, and production environments and simplify audits and troubleshooting.                                             |
| Orchestrator-ready            | Images and Helm or Docker Compose assets designed to run on Kubernetes and other container platforms, including health checks, volumes, environment-based configuration, and scaling patterns.                                |
| Integrated observability      | Built-in logging and metrics patterns so containerized Ping Identity services can be wired into your existing monitoring and security information and event management (SIEM) tooling.                                        |
| Patch and upgrade efficiency  | Central image updates allow you to roll out security patches and version upgrades by replacing images instead of rebuilding servers manually.                                                                                 |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can review your current licenses and entitlements in the Ping Identity Support Portal. After signing on, go to the Licensing section. From this page, you can also access your support keys and open a support case if anything about your entitlements appears incorrect.You can find more information in Ping Identity's legal [Product terms and conditions](https://www.pingidentity.com/en/legal/product-terms.html). |
