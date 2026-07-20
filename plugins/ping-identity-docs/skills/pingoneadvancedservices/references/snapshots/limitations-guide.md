---
title: Limitations guide
description: Many of you have used on-premise versions of Ping Identity products, such as PingFederate, PingAccess, PingCentral, and the PingDirectory suite of products. Many of you have also used a variety of different cloud services, including Amazon Web Services (AWS).
component: pingoneadvancedservices
page_id: pingoneadvancedservices:limitations_guide:p1as_limitations
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/limitations_guide/p1as_limitations.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 23, 2025
section_ids:
  p1as_infrastructure: Infrastructure
  p1as_product_features: Product features and configurations
  pingfederate: PingFederate
  pingdirectory: PingDirectory
  pingaccess: PingAccess
  general-platform-features: General platform features
  p1as_logging: Observability and logging
  p1as_loading_access: Data loading and access
  web-servers-and-ingress: Web servers and Ingress
---

# Limitations guide

Many of you have used on-premise versions of Ping Identity products, such as PingFederate, PingAccess, PingCentral, and the PingDirectory suite of products. Many of you have also used a variety of different cloud services, including Amazon Web Services (AWS).

However, it's important to understand that some of the product features and configuration options that you might be accustomed to using are not available with PingOne Advanced Services. Even if you're an experienced AWS user, PingOne Advanced Services has a variety of infrastructure and networking requirements that you should be aware of.

This guide lists the product features that are not available in PingOne Advanced Services, and explains how the product log files differ from the on-premise versions. It also outlines our data loading and access policies.

Refer to the following for details:

* [Infrastructure](#p1as_infrastructure)

* [Product features and configurations](#p1as_product_features)

* [Observability and logging](#p1as_logging)

* [Data loading and access](#p1as_loading_access)

## Infrastructure

Items to keep in mind regarding PingOne Advanced Services infrastructure:

* The PingOne Advanced Services SaaS platform is built on AWS, which hosts resources in multiple locations worldwide. No other cloud provider is supported.

  |   |                                                                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | PingOne Advanced Services is built on AWS, but because it is a SaaS platform, it does not provide access to the features and tools that you might be accustomed to using in AWS. |

* Multi-cloud deployments are not supported.

* A Simple Mail Transfer Protocol (SMTP) server is not included. If one is needed and because AWS blocks port 25 outbound by default, Simple Mail Transfer Protocol Secure (SMTPS) must be used.

* If integration kits are used with PingOne Advanced Services, they must be provided by Ping Identity product or engineering teams. Kits created by customers or other third parties are not allowed.

* Each AWS region is isolated from other AWS regions, and each zone is supported by at least one physical data center in that region. Although a single availability zone can span multiple data centers, no two zones share a data center to reduce the likelihood of two zones failing simultaneously.

  The following table lists the regions supported:

  | Region group      | Code (region)                      | Name                     |
  | ----------------- | ---------------------------------- | ------------------------ |
  | **Asia**          | ap-Southeast-1 (url region "sg1" ) | Asia Pacific (Singapore) |
  |                   | ap-Southeast-2 (url region "au1" ) | Asia Pacific (Sydney)    |
  |                   | ap-Southeast-4 (url region "au2")  | Asia Pacific (Melbourne) |
  | **Canada**        | ca-Central-1 (url region "ca1" )   | Canada (Central)         |
  | **Europe**        | eu-Central-1 (url region "eu1" )   | Europe (Frankfurt)       |
  |                   | eu-West-1 (url region "eu2" )      | Europe (Ireland)         |
  | **United States** | us-East-2 (url region "us1" )      | US East (Ohio)           |
  |                   | us-West-2 (url region "us2" )      | US West (Oregon)         |

  You have one region with the PingOne Cloud Platform and can have between one and three different regions with PingOne Advanced Services. All regions guarantee uptimes of 99.99%.

  |   |                                                                                                                                                                               |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Session migration on inter-regional fail-over is only supported if the products are properly configured, and should be addressed during the system planning and design phase. |

* You have one production environment and up to three non-production environments (Dev, Test, and Stage) that you can use to develop and test your code and configurations. Dev and Test environments:

  * Are provisioned with 8GB of RAM and 40GB of disk space.

  * Do not auto-scale resources for the number of pods needed.

  * Only exist in the primary region for multi-region deployments.

  * Support a limited number of identities or objects:

    * The limit of identities or objects in Dev and Test is 10,000.

    * More identities or objects can be loaded, however, doing so is at your own risk.

    * Performance or stability issues might be encountered if the limit is exceeded.

  The staging environment is a replica of the production environment infrastructure but is not subject to Ping Identity's uptime and Severity 1 and 2 service level agreements.

  Load and performance testing is not permitted on the Dev or Test environments.

  See [Environments](../environments/p1as_environments.html) for additional information about each of these environments.

  |   |                                                                                                                                                                |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Determine which types of non-production environments you want to use upfront, as it's arduous to add environments after PingOne Advanced Services is deployed. |

## Product features and configurations

Although most functionality available in the on-premise products is also available in PingOne Advanced Services, some features and configurations are not.

For example, heartbeat health checks are not available for our products and services. However, you can submit a service request and ask for health checks to be run on the staging server.

The following sections list some of the product-specific features and configurations you should keep in mind.

### PingFederate

* Integration kits that add an application (war file) are not supported, however, JavaScript or other scripts are allowed.

* PingFederate provisioning is only available from the primary region with no fail-over.

* The [PingFederate Agentless Integration Kit](https://marketplace.pingone.com/item/agentless-integration-kit) cannot use dots in header names (only dashes).

* The OAuth Playground is not supported in Production environments.

* The persistent session datastore for PingFederate can only be PingDirectory.

* The X509/mTLS uses the alternate Hostname format, (not the alternate port format).

* There is no self-service report or way to view administrator-level permissions (roles) for admin users.

* An administrator audit log file is not available.

* When configuring CRL checking, the **Treat Unretrievable CRLs as Revoked** option cannot be used with PingOne Advanced Services. As soon this option is selected in PingFederate and the configuration is replicated to the engines, the outage starts. After PingFederate is restarted with the option selected, a support ticket is required, as PingFederate will no longer start.

|   |                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If changes to the PingFederate `config-store` are needed, you must make them yourself using an API call or the API interactive documentation. Your organization owns the data in both `config-store` and `config-archive`, and our Support team isn't allowed to make updates. |

### PingDirectory

* The number of customer-specific directory backends is limited to five.

* HSMs that require extra libraries are not supported.

* Automatic certificate management in a truststore is not supported.

* Certain privileges are not available to PingOne Advanced Services, including `config-read`, `privilege-change`, and `bypass-acl`.

* There is no access to backends other than customer backends and no privileges or configuration changes that would impact those backends, (for example, no access to the default password policy or virtual attributes that impact non-customer backends).

* No changes can be made to root users or root privileges.

* PingDataSync supports sync pipe source and destination types, as documented in the [PingDataSync product documentation](https://docs.pingidentity.com/pingdirectory/11.0/pingdatasync_server_administration_guide/pd_sync_admin_guide.html). The steps you take to configure connections depend on which PingOne Advanced Services networking configuration you choose. Supported outbound connectivity options are described in the [Network guide](../network_guide/p1as_network_guide.html).

* Kafka sync destinations are supported. Connectivity to a customer-managed Kafka cluster requires outbound network access from the PingOne Advanced Services environment. Work with your account team to determine which network option is right for you.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are a PingDirectory administrator, be aware that using static groups, especially large groups with more than 1000 members, can significantly impact performance. Also, if you make changes to a large static group, manually or through the referential integrity plugin, PingDirectory server performance can be significantly affected and outages could occur. Ensure that your administrators and application developers work together to minimize the potential impact on the user experience.This is one of the many reasons it's recommended not to use static groups. Dynamic groups or inverted static groups that use an attribute of the user entry to determine the user's membership, are recommended instead.However, if you can't avoid using large, static groups, here are a few recommendations that could help improve performance:* Don't directly update the static group for each user record. Instead, collect the changes and create a single operation that adds or removes many users using a single group modify operation.

* Set the referential integrity plugin update interval to a non-zero value. Note that this only delays the effort that the directory servers must take.

* Modify the replication assurance policies to exclude group operations so that they don't require local assurance. Note that this also only delays the effort the directory servers must take.

* Increase the new generation memory to reduce the risk of premature promotion and the number of young generation collections. By default, 2G is provided. |

### PingAccess

* With PingAccess, request sizes cannot be larger than 1 MB.

* This product cannot be used as a proxy for PingFederate.

* There is no self-service report or way to view administrator-level permissions (roles) for admin users.

* An administrator audit log file is not available.

* Customers can only use port 443 for PingAccess-protected application URLs (virtual hosts).

### General platform features

* Customer-managed PingFederate and PingAccess admin accounts are not supported.

* If you have many internal certificate authorities (CAs), more than 20 virtual hosts must be created in PingOne Advanced Services. Application code will also need to be updated to reflect the virtual hosts for agentless drop-off and pick-up.

## Observability and logging

Our Support team and the Site Reliability Engineers proactively monitor your infrastructure and deployments and attempt to address issues before they become problems. If outages occur, we'll notify you using standard support methods.

You are responsible for monitoring your Ping applications and configurations, but we will stream log files to you, which will help you identify, monitor, and quickly resolve any issues you might encounter. You can also subscribe to receive alerts from PingOne Advanced Services, which will notify you of events occurring within your network.

See [Monitoring and logging](../monitoring_and_logging/p1as_monitoring_logging.html) for additional information.

Although the on-premise products you might be accustomed to using allow you to customize your log files, the log files in PingOne Advanced Services are limited.

Items to keep in mind regarding PingOne Advanced Services observability and logging:

* Log fields cannot be customized.

* Debugging is turned off for the production and Stage environments, but can be turned on for brief periods of time for troubleshooting purposes.

* Only the default product logs are available.

* Parsed log files are available (on a best-effort basis) in OpenSearch for 30 days (subject to change).

* S3 Log Replay is an internal tool used only by internal teams for troubleshooting purposes.

* Customer-requested log replay isn't available for either OpenSearch or customer endpoints.

The log names that you might be used to seeing in PingFederate, PingAccess, and the PingDirectory suite of products might be different in the PingOne Advanced Services log files. These differences are listed here by product.

**PingFederate**

| On-premise log name        | PingOne Advanced Services log name |
| -------------------------- | ---------------------------------- |
| server.log                 | pf-server-\*                       |
| audit.log                  | pf-audit-\*                        |
| transaction.log            | pf-transaction-\*                  |
| provisioner.log            | pf-provisioner-\*                  |
| provisioner-audit.log      | pf-provisioner-audit-\*            |
| \<date.>request.log        | pf-request-\*                      |
| admin.log                  | pf-admin-log-\*                    |
| admin-event-detail.log     | pf-admin-event-detail-\*           |
| admin-api.log              | pf-admin-api-\*                    |
| runtime-api.log            | pf-runtime-api-\*                  |
| init.log                   | pf-init-\*                         |
| jvm-garbage-collection.log | pf-jvm-garbage-collection-\*       |

**PingAccess**

| On-premise log name                          | PingOne Advanced Services log name |
| -------------------------------------------- | ---------------------------------- |
| pingaccess.log                               | pa-pingaccess-\*                   |
| pingaccess\_engine\_audit.log                | pa-engine-audit-\*                 |
| pingaccess\_agent\_audit.log                 | pa-agent-audit-\*                  |
| pingaccess\_api\_audit\_har.log              | pa-api-audit-har-\*                |
| pingaccess\_api\_audit.log                   | pa-api-audit-log-\*                |
| pingaccess\_sideband\_audit.log              | pa-sideband-audit-\*               |
| pingaccess\_sideband\_client\_audit.log      | pa-sideband-client-audit-\*        |
| pingaccess.log                               | pa-was-pingaccess-\*               |
| audit.log                                    | pa-was-engine-audit-\*             |
| pingaccess\_was\_api\_audit\_har.log         | pa-was-api-audit-har-\*            |
| pingaccess\_was\_api\_audit.log              | pa-was-api-audit-log-\*            |
| pingaccess\_was\_sideband\_audit.log         | pa-was-sideband-audit-\*           |
| pingaccess\_was\_sideband\_client\_audit.log | pa-was-sideband-audit-\*           |

**PingAccess Web Application Security (WAS)**

| On-premise log name                     | PingOne Advanced Services log name |
| --------------------------------------- | ---------------------------------- |
| pingaccess.log                          | pa-was-system\*                    |
| audit.log                               | pa-was-audit\*                     |
| pingaccess\_engine\_audit.log           | pa-was-audit\*                     |
| pingaccess\_api\_audit.log              | pa-was-audit\*                     |
| pingaccess\_agent\_audit.log            | pa-was-audit\*                     |
| pingaccess\_sideband\_audit.log         | pa-was-audit\*                     |
| pingaccess\_sideband\_client\_audit.log | pa-was-audit\*                     |
| pingaccess.log                          | pa-was-admin-system\*              |
| audit.log                               | pa-was-admin-audit\*               |
| pingaccess\_engine\_audit.log           | pa-was-admin-audit\*               |
| pingaccess\_api\_audit.log              | pa-was-admin-audit\*               |

**PingDirectory**

| On-premise log name  | PingOne Advanced Services log name |
| -------------------- | ---------------------------------- |
| access               | pd-access-\*                       |
| errors               | pd-errors-\*                       |
| server.out           | pd-server-\*                       |
| replication          | pd-replication-\*                  |
| failed-ops           | pd-failed-ops-\*                   |
| expensive-write-ops  | pd-expensive-write-ops-\*          |
| http-detailed-access | pd-http-detailed-access-\*         |

**PingDataSync**

| On-premise log name | PingOne Advanced Services log name |
| ------------------- | ---------------------------------- |
| access              | pds-access-\*                      |
| errors              | pds-errors-\*                      |
| server.out          | pds-server-\*                      |
| failed-ops          | pds-failed-ops-\*                  |

## Data loading and access

When transitioning to PingOne Advanced Services, you'll need to load your existing data from your legacy systems into your PingOne Advanced Services deployment.

For security reasons, Ping Identity will not, and should not, have access to your data.

However, our Professional Services team will work closely with you to ensure the transition is as painless as possible. We'll discuss the methods we'll use during the system planning and design phase.

These methods include but are not limited to:

* Importing an LDIF file remotely through an LDAP browser

* Using PingDataSync

### Web servers and Ingress

Web servers proxies HTTP requests to web application servers, while Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. Traffic routing is controlled by rules defined on the Ingress resource.

PingOne Advanced Services is deployed with a variety of hostname URLs by default, but it's important that you use your own hostname URLs. Using the default URLs can cause issues for your users if you have a multi-region deployment, or plan to in the future.

The pre-authorized ciphers are:

* ECDHE-ECDSA-AES128-GCM-SHA256:

* ECDHE-RSA-AES128-GCM-SHA256:

* ECDHE-ECDSA-AES256-GCM-SHA384:

* ECDHE-RSA-AES256-GCM-SHA384:

* ECDHE-ECDSA-CHACHA20-POLY1305:

* ECDHE-RSA-CHACHA20-POLY1305:

* DHE-RSA-AES256-GCM-SHA384:

* ECDHE-RSA-AES256-SHA384:

* ECDHE-RSA-AES128-SHA256:

* ECDHE-ECDSA-AES256-GCM-SHA384: