---
title: Infrastructure and supported regions
description: Items to keep in mind regarding Ping Government Identity Cloud infrastructure include:
component: pgic
page_id: pgic::pgic_infrastructure
canonical_url: http://docs.pingidentity.com/pgic/pgic_infrastructure.html
section_ids:
  supported-regions: Supported regions
---

# Infrastructure and supported regions

Items to keep in mind regarding Ping Government Identity Cloud infrastructure include:

* Ping Government Identity Cloud is built on AWS GovCloud, but because it's a SaaS platform, it doesn't provide access to the features and tools that you might be accustomed to using in Amazon Web Services (AWS).

* The Ping Government Identity Cloud environment is set up as configuration as code.

* Multicloud deployments aren't supported.

* A Simple Mail Transfer Protocol (SMTP) server isn't included. If you need one, as AWS blocks port 25 outbound by default, Simple Mail Transfer Protocol Secure (SMTPS) must be used.

* Each AWS region is isolated from other AWS regions, and each zone is supported by at least one physical data center in that region. Although a single availability zone can span multiple data centers, zones don't share a data center to reduce the likelihood of two zones failing simultaneously.

## Supported regions

With Ping Government Identity Cloud, you specify the region where you want your data to reside. This helps you meet data residency compliance requirements while letting you place data as close to your users as possible.

The following table lists the supported regions:

| Region group      | Code (region)                     | Name                   |
| ----------------- | --------------------------------- | ---------------------- |
| **United States** | us-gov-east-1 (url region "us1" ) | AWS GovCloud (US-East) |
|                   | us-gov-west-2 (url region "us2" ) | AWS GovCloud (US-West) |

Keep the following in mind:

* All regions guarantee uptimes of 99.99%.

* Session migration on interregional failover is supported only if the products are correctly configured, and should be addressed during the planning phase.

  |   |                                                                                              |
  | - | -------------------------------------------------------------------------------------------- |
  |   | SNS and SES can be configured, however, SMS isn't currently available in the US-East region. |

* You have one production environment and one non-production environment that you can use to develop and test your code and configurations. You can also add up to three additional environments (Dev, Test, and Stage) if you need them. The staging environment is a replica of the production environment infrastructure but isn't subject to Ping Identity's uptime and Severity 1 and 2 service-level agreements.

  Determine which types of non-production environments you want to use upfront, as it's arduous to add environments after Ping Government Identity Cloud is deployed.

* The Dev and Test environments can support up to 10,000 identities or objects. If this limit is exceeded, you could encounter performance or stability issues.

* Load and performance testing isn't permitted on the Dev and Test environments.

* Don't auto-scale resources for the number of pods needed.