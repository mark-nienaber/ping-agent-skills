---
description: PingAccess
component: pingdirectory
version: 11.1
page_id: pingdirectory::common_product_keydefs
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/common_product_keydefs.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

PingAccess

PingAuthorize

Policy Editor

PingCentral

PingCloud

PingDataGovernance

PingDataMetrics

PingDataSync

PingDirectory

PingDirectory Consent API

PingDirectoryProxy

Delegated Admin

PingFederate

PingFederate Bridge

PingID

PingID SDK

PingID desktop app

PingID mobile app

PingIntelligence

PingIntelligence for APIs

PingOne

PingOne Authorize

PingOne SSO for SaaS Apps

PingOne

PingOne MFA

PingID

PingOne Protect

PingOne Verify

PingOne for Enterprise

the PingOne administration console

Customer360

Workforce360

DaVinci

PingOne Advanced Identity Cloud

Advanced Identity Cloud

PingOne

PingOne Neo

PingOne Solutions

PingOne for Customers

PingOne for Workforce

PingOne for Individuals

PingOne for Government

PingOne Services

PingOne SSO

PingOne Credentials

PingOne Advanced Services

PingOne Advanced Services Single Sign-on

PingOne Advanced Services Security

PingOne Advanced Services Directory

PingOne Dynamic Authorization

PingOne Advanced API Security

PingOne Advanced Central Administration

PingOne Fraud

PingOne API Intelligence

PingOne API Access Management

ShoCard

PingOne for Individuals SDK

PingOne for Customers Passwordless

PingOne for Customers Plus

NET

AD Connect

AirWatch

Akana

Amazon Web Services

AWS

Apache

Apigee

Atlassian

Axway

Azure AD

Box

Citrix

Cloud Identity

Concur

CoreBlox

Coupa

Dropbox

Duo Security

Egnyte

Evernote

Facebook

G Suite

Google

Google Apps

Heroku

IIS

Intune

Java

LinkedIn

Linux

Microsoft

MobileIron

Mulesoft

NGINX

Office 365

Oracle Access Manager

Oracle Directory Server Enterprise Edition

PHP

Palo Alto Networks

RSA SecurID

SAP NetWeaver

Salesforce

ServiceNow

SharePoint

Slack

Splunk

Symantec VIP

Twitter

VMware

WebEx

WebLogic

WebSphere

Windows Live

Workday

Workplace by Facebook

YubiCloud

YubiKey

Zendesk

---

---
title: Feature statuses
description: Learn about testing and using new server features that are still in development.
component: pingdirectory
version: 11.1
page_id: pingdirectory::feature_status
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/feature_status.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  preview: Preview
  evolving: Evolving
---

# Feature statuses

The following statuses describe how to approach using features that are still in development.

|   |                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Read the status description before using a feature in development. These features have status labels applied in both the release notes and in the relevant feature topics. |

## Preview

You can use preview features to test new technology in non-production environments. You can also make comments and provide suggestions about these features in the associated [forums](https://support.pingidentity.com/s/topic/0TO1W000000Q9oHWAS/pingdirectory).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Preview features aren't supported. Don't deploy them in production environments.

* Ping Identity provides them as-is for evaluation purposes only and accepts no liability or obligations for their use. These features might be functionally incomplete, and the functionality as implemented could change without notice.

* Ping Identity doesn't guarantee that a preview feature will be included in future releases, and the feature could change before its final version. Once a preview feature is completed, that feature becomes a part of the PingDirectory suite of products. |

## Evolving

You can use evolving features in both pre-production and production environments, however, the development team could make significant changes. These changes can occur in backwards-incompatible ways and might be delivered in a minor release. Any changes are documented at the time of release.

|   |                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | An evolving feature is ready for production environments but has a high likelihood of changing with any product release. Any integration of this functionality into your environments could require significant maintenance until the feature development has stabilized. |

---

---
title: Introduction to the PingDataSync server
description: The PingDataSync server uses a dataless approach that synchronizes changes directly from the data sources in the background so that applications can continue to update their data sources directly. PingDataSync doesn't store any data from the endpoints themselves, which reduces hardware and administration costs. The server's high-availability mechanisms allow for easy failover from the main PingDataSync server to redundant instances.
component: pingdirectory
version: 11.1
page_id: pingdirectory::pd_sync_main_intro
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pd_sync_main_intro.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  pingdatasync-server-features: PingDataSync server features
---

# Introduction to the PingDataSync server

The PingDataSync server uses a dataless approach that synchronizes changes directly from the data sources in the background so that applications can continue to update their data sources directly. PingDataSync doesn't store any data from the endpoints themselves, which reduces hardware and administration costs. The server's high-availability mechanisms allow for easy failover from the main PingDataSync server to redundant instances.

## PingDataSync server features

PingDataSync is designed to run with little administrative maintenance and includes the following features:

* High performance and availability with built-in redundancy.

* Dataless [virtual architecture](pingdatasync_server_administration_guide/pd_sync_data_sync_process.html) for a small-memory footprint and ease of maintenance.

* Comprehensive and straightforward setup that enables mapping [attribute names](pingdatasync_server_administration_guide/pd_sync_about_attr_mapping.html), values, and [distinguished names (DNs)](pingdatasync_server_administration_guide/pd_sync_config_dn_maps.html) between endpoints. For directory server endpoints, this enables schema and directory information tree (DIT) changes without custom coding and scripting.

* Multi-vendor directory server support, including:

  * PingDirectory server

  * [PingDirectoryProxy server](pingdatasync_server_administration_guide/pd_sync_thru_pdproxy_server.html)

  * Sun Directory Server Enterprise Edition

  * Sun Directory Server

  * Oracle Unified Directory

  * OpenDJ

  * [Microsoft AD](pingdatasync_server_administration_guide/pd_sync_ad_systems.html)

  * Generic LDAP directories

* [RDBMS support](pingdatasync_server_administration_guide/pd_sync_with_relational_databases.html), including Oracle Database and Microsoft SQL server systems.

* Proxy server support including PingDirectoryProxy server.

* A [notification mode](pingdatasync_server_administration_guide/pd_sync_in_notification_mode.html) that sends real-time change notifications to the application or service of your choice through the server SDK.

---

---
title: Introduction to the PingDirectory server
description: The PingDirectory server is a high-performance, extensible Lightweight Directory Access Protocol (LDAP) directory that provides seamless data management over a distributed system while meeting the constant performance demands for today's markets.
component: pingdirectory
version: 11.1
page_id: pingdirectory::pd_ds_intro_pindirectory_server
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pd_ds_intro_pindirectory_server.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["pingdirectory_server_administration_guide:pd_ds_intro_pindirectory_server.adoc"]
section_ids:
  server-features: Server features
  administration-framework: Administration framework
  server-tools-location: Server tools location
---

# Introduction to the PingDirectory server

The PingDirectory server is a high-performance, extensible Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* directory that provides seamless data management over a distributed system while meeting the constant performance demands for today's markets.

The PingDirectory server centralizes consumer and user identity management information, subscriber data management, application configurations, and user credentials into a network, enterprise, or virtualized database environment.

The PingDirectory server can:

* Simplify administration

* Reduce costs

* Secure information in systems that scale for large numbers of users

You can find the latest information on PingDirectory server releases in the [Release notes](release_notes/pd_release_notes.html).

## Server features

The PingDirectory server provides the following features and tools.

* Full LDAP version 3 implementation

  The PingDirectory server fully supports [LDAP v3](https://docs.oracle.com/javase/jndi/tutorial/ldap/models/v3.html), which supports the Request For Comments (RFCs) specified in the protocol. It provides a feature-rich solution that supports the core LDAP v3 protocol in addition to server-specific controls and extended operations.

* High availability

  The PingDirectory server supports N-way multi-primary [replication](pingdirectory_server_administration_guide/pd_ds_manage_replication.html) that eliminates single points of failure and ensures high availability for a networked topology. It allows you to store data across multiple machines and disk partitions for fast replication. It also supports replication in [entry-balancing proxy server](pingdirectoryproxy_server_administration_guide/pd_proxy_deploy_entry_balancing_dps.html) deployments.

* Administration tools

  The PingDirectory server provides a full set of [command-line tools](pingdirectory_server_administration_guide/pd_ds_available_cmdline_tools.html), an [admin console](pingdirectory_server_administration_guide/pd_ds_using_the_console.html), and a Java-based setup tool to configure, monitor, and manage any part of the server.

  The server has a task-based subsystem that provides automated scheduling of basic functions, such as:

  * Backups

  * Restores

  * Imports

  * Exports

  * Restarts

  * Shutdowns

  The set of utilities includes a [troubleshooting support tool](troubleshooting_the_pingdirectory_suite_of_products/pd_ds_collect_support_data_tool.html) that aggregates system metrics into a `.zip` archive, which administrators can send to your authorized support provider for analysis.

* Self-service account manager application

  The Self Service Account Manager project, hosted at <https://github.com/pingidentity/ssam>, is a customizable web application allowing users to perform their own account registration, profile updates, and password changes. The project is for testing and development purposes only and is not a supported application.

* Delegated admin application

  A JavaScript-based web application can be installed for business users to manage identities stored in the PingDirectory server. The application provides delegated administration of identities for:

  * Help desk or customer service representatives initiating a password reset and unlock

  * An employee in HR updating an address stored within another employee profile

  * An application administrator updating identity attributes or group membership to allow application single sign-on (SSO) access.

  Learn more in the [Delegated Admin application guide](delegated_admin_application_guide/pd_da_admin_guide.html).

* Security mechanisms

  The PingDirectory server provides extensive security mechanisms to protect data and prevent unauthorized access. Access control list (ACL) instructions are available down to the attribute value level and can be stored within each entry.

  The server allows connections over SSL through an encrypted communication tunnel. Clients can also use the StartTLS extended operation over standard, non-encrypted ports. Other security features include:

  * A privilege subsystem for fine-grained granting of rights

  * A password policy subsystem that allows configurable password validators and storage schemes

  * SASL authentication mechanisms to secure data integrity, such as:

    * PLAIN

    * ANONYMOUS

    * EXTERNAL

    * CRAM-MD5

    * Digest-MD

    * GSSAPI

  The PingDirectory server supports various providers and mappers for certificate-based authentication in addition to the ability to encrypt specific entries or sensitive attributes. Learn more in the [PingDirectory Security Guide](pingdirectory_security_guide/pd_sec_security_guide.html).

* Monitoring and notifications

  The PingDirectory server supports monitoring entries using:

  * JConsole

  * SNMP

  * The admin console

  Administrators can track the response times for LDAP operations using a monitoring histogram as well as record performance statistics down to sub-second granularity. The PingDirectory server supports configurable notifications, auditing, and logging subsystems with filtered logging capabilities. Learn more in [Monitoring the PingDirectory Suite of Products](monitoring_the_pingdirectory_suite_of_products/pd_ds_manage_monitoring.html).

* Powerful LDAP SDK

  The PingDirectory server is based on a feature-rich LDAP SDK for Java. The LDAP SDK is a Java API standard that overcomes the limitations of the Java Naming and Directory Interface (JNDI) model. For example, JNDI does not address the use of LDAP controls and extended operations. The LDAP SDK for Java provides support for controls and extended operations to leverage Ping Identity's extensible architecture for their applications.

  |   |                                                                           |
  | - | ------------------------------------------------------------------------- |
  |   | For more information on the LDAP SDK for Java, see <http://www.LDAP.com>. |

* System for Cross-domain Identity Management (SCIM) extension

  The PingDirectory server provides a SCIM servlet extension to facilitate moving users to, from, and between cloud-based software as a service (SaaS) applications in a secure and fast manner.

  Learn more in [Managing the SCIM 2.0 servlet extension](managing_scim_11_and_20_servlet_extensions/pd_ds_scim_servlet_ext_mgmt.html).

* Directory REST API

  The PingDirectory server provides a [REST API](pingdirectory_server_administration_guide/pd_ds_directory_rest_api.html) as the native interface for client access. Instead of trying to manage directory hierarchy or requiring attribute mapping, the Directory REST API provides direct access to directory data in a way that is dynamic, discoverable, and efficient. Learn more in the [Developer portal](https://developer.pingidentity.com/en.html).

* Server SDK

  The Server SDK is a library of Java packages, classes, and build tools to help in-house or third-party developers create client extensions for:

  * PingDirectory server

  * PingDirectoryProxy server

  * PingDataSync server

  The servers have a highly extensible and scalable architecture with multiple plugin points for your customization needs. The Server SDK provides APIs to alter the behavior of each server's components without affecting its code base.

## Administration framework

The PingDirectory server provides an administration and configuration framework capable of managing stand-alone servers, server groups, and highly available deployments that include multiple redundant server instances.

Administrators can configure changes locally or remotely:

* On a single server

* On all servers in a server group

Each server configuration is stored as a flat file (LDIF) that can be accessed under the `cn=config` branch of the directory information tree (DIT). Administrators can tune the configuration and perform maintenance functions over LDAP using a suite of command-line tools or an admin console (for configuration and monitoring). The PingDirectory server provides plugins to extend the functionality of its components.

## Server tools location

The PingDirectory server stores a full set of command-line tools for maintaining your system in the `PingDirectory/bin` directory for UNIX or Linux machines and the `PingDirectory\bat` directory for Microsoft Windows machines.

The PingDirectory server, admin console, and LDAP SDK for Java are distributed in `.zip` format. After extracting the file, you can access the `setup` utility in the server root directory, located at `PingDirectory`.

Before installing the PingDirectory server, refer to [Preparing the operating system (Linux)](installing_the_pingdirectory_suite_of_products/pd_ds_prepare_operating_system_linux.html) for important information on setting up your machines. Refer to [Installing the PingDirectory server](installing_the_pingdirectory_suite_of_products/pd_ds_install_server.html) for information on installing a server instance using the `setup` utility. You can run this utility in either interactive command-line or non-interactive command-line. You can find information on modifying the configuration of a server instance or a group of servers using the command-line tools and the admin console in [Configuring the PingDirectory server](pingdirectory_server_administration_guide/pd_ds_configuring_server.html).

---

---
title: Introduction to the PingDirectoryProxy server
description: The following overview describes the PingDirectoryProxy server's features and capabilities.
component: pingdirectory
version: 11.1
page_id: pingdirectory::pd_proxy_overview_pdproxy_features
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pd_proxy_overview_pdproxy_features.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pingdirectoryproxy_server_administration_guide:pd_proxy_overview_pdproxy_features.adoc"]
---

# Introduction to the PingDirectoryProxy server

The following overview describes the PingDirectoryProxy server's features and capabilities.

The PingDirectoryProxy server is a fast, scalable, and easy-to-use LDAP proxy server that provides high availability and additional security for the PingDirectory server while remaining largely invisible to client applications. From a client perspective, request processing is the same, whether communicating with the PingDirectory server directly or going through the PingDirectoryProxy server.

The PingDirectoryProxy server provides the following features:

* High availability

  The PingDirectoryProxy server allows you to transparently fail over between servers if a problem occurs as well as ensuring that the workload is balanced across the topology. If a client does not support following referrals, the server can follow them on the client's behalf.

* Data mapping and transformation

  The PingDirectoryProxy server can perform distinguished name (DN) mapping and attribute mapping *(tooltip: \<div class="paragraph">
  \<p>Matching corresponding attributes between an IdP and an SP to identify federated users or add supplemental user information.\</p>
  \</div>)* to allow clients to interact with the server using older names for directory content. It allows clients to continue working when they would not be able to work directly with the PingDirectory server, either because of changes that have occurred at the data layer or to inherent design limitations in the clients.

  Learn more in [Configuring proxy transformations](pingdirectoryproxy_server_administration_guide/pd_proxy_config_proxy_transformations.html).

* Horizontal scalability and performance

  Reads can be horizontally scaled using load balancing. In large data centers, if the data set is too large to be cached or to provide horizontal scalability for writes, the PingDirectoryProxy server can automatically split the data across multiple systems. This feature allows the PingDirectoryProxy server to improve scalability and performance of the PingDirectory server environment.

* Load balancing and failover

  You can spread the workload across multiple directory servers in a large data center using load-balancing algorithms. Load balancing is also useful when a server becomes degraded or non-responsive because client process requesting directs to a different server.

  Learn more in [Configuring load balancing](pingdirectoryproxy_server_administration_guide/pd_proxy_config_load_balancing.html).

* Security and access control

  The PingDirectoryProxy server can add additional firewall capabilities as well as constraints and filtering to help protect the PingDirectory server from attacks.

  You can use a PingDirectoryProxy server in a DMZ as opposed to allowing clients to directly access the PingDirectoryProxy server in the internal network or providing the data in the DMZ. It can help provide secure access to the data and you can define what actions clients are allowed to do. For example, you can prevent clients from making modifications to data when connected through a VPN no matter what their identity or permissions.

* Tracking of operations across the environment

  In the past, administrators have complained that when they see a request in the access log they have no idea where it came from and cannot track it back to a particular client. The PingDirectoryProxy server contains controls that allow administrators to track requests back to the client that issued them.

  Whenever the PingDirectoryProxy server forwards a request to the PingDirectory server, it includes a control in the request so that the PingDirectory server's access log has the IP address of the client, address and connection ID of the PingDirectory server. In the response back to the client, it similarly includes information about the PingDirectory server that processed the request, such as the connection ID and operation ID. This feature makes it easier for administrators to monitor in their environment.

* Monitoring and management tools

  Because the PingDirectoryProxy server uses many of the components of PingDirectory, it can leverage them to provide protocol support, logging, management tools for configuration and monitoring, and schema. You can use the `dsconfig` tool and the admin console to manage the PingDirectoryProxy server.

  Learn more in [Managing the PingDirectoryProxy server](pingdirectoryproxy_server_administration_guide/pd_proxy_managing_dps.html).

---

---
title: PingDirectory
description: The PingDirectory suite of products includes the PingDirectory server, the PingDirectoryProxy server, the PingDataSync server, and the Delegated Admin application.
component: pingdirectory
version: 11.1
page_id: pingdirectory::pd_ds_landing_page
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pd_ds_landing_page.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 15, 2023
page_aliases: ["_@pingdirectory::index.adoc"]
section_ids:
  release-notes: Release Notes
  get-started-with-pingdirectory: Get Started with PingDirectory
  use-pingdirectory: Use PingDirectory
  troubleshoot-pingdirectory: Troubleshoot PingDirectory
  learn-more: Learn More
---

# PingDirectory

The PingDirectory suite of products includes the PingDirectory server, the PingDirectoryProxy server, the PingDataSync server, and the Delegated Admin application.

|   |                                                                                              |
| - | -------------------------------------------------------------------------------------------- |
|   | This is a short-term support release. Learn more in [Release statuses](release_status.html). |

## Release Notes

* [Current](release_notes/pd_release_notes.html)

* [Previous releases](release_notes/pd_release_notes.html#prevrel)

## Get Started with PingDirectory

* PingDirectory

  A high-performance, extensible LDAP directory.

  * [Server overview](pd_ds_intro_pindirectory_server.html)

  * [Installing the server](installing_the_pingdirectory_suite_of_products/pd_ds_install_server.html)

  * [Next steps after installation](pingdirectory_server_administration_guide/pd_ds_get_started.html)

  * [Signing on to the admin console](pingdirectory_server_administration_guide/pd_ds_sign_on_admin_console.html)

* PingDirectoryProxy

  A fast and scalable LDAPv3 gateway for the PingDirectory server.

  * [Server overview](pd_proxy_overview_pdproxy_features.html)

  * [Installing the server](installing_the_pingdirectory_suite_of_products/pd_proxy_install_dir_proxy_server.html)

  * [Configuring the server](pingdirectoryproxy_server_administration_guide/pd_proxy_config_dps.html)

* PingDataSync

  An efficient, Java-based server that provides high throughput, low latency, and bidirectional real-time synchronization between two endpoint topologies.

  * [Server overview](pd_sync_main_intro.html)

  * [Installing the server](installing_the_pingdirectory_suite_of_products/pd_sync_installing_pds.html)

  * [Configuring the server](pingdatasync_server_administration_guide/pd_sync_config_pds.html)

* Delegated Admin

  An add-on to PingDirectory that enables the delegation of user and group management.

  * [Application overview](delegated_admin_application_guide/pd_da_introduction.html)

  * [Installing the application](installing_the_pingdirectory_suite_of_products/pd_da_install_delegated_admin.html)

  * [Configuring the application](delegated_admin_application_guide/pd_da_config_delegated_admin.html)

## Use PingDirectory

* [Best practices for PingDirectory application integration](https://docs.pingidentity.com/solution-guides/best_practice_guides/bp_pd_operational_support.html)

* [PingDirectory admin guide](pingdirectory_server_administration_guide/pd_ds_amin_guide.html)

* [PingDirectoryProxy admin guide](pingdirectoryproxy_server_administration_guide/pd_proxy_admin_guide.html)

* [PingDataSync admin guide](pingdatasync_server_administration_guide/pd_sync_admin_guide.html)

* [Delegated Admin admin guide](delegated_admin_application_guide/pd_da_admin_guide.html)

## Troubleshoot PingDirectory

* [PingDirectory and PingDirectoryProxy](troubleshooting_the_pingdirectory_suite_of_products/pd_pdproxy_troubleshooting_main.html)

* [PingDataSync](troubleshooting_the_pingdirectory_suite_of_products/pd_sync_troubleshooting.html)

## Learn More

* [Try PingDirectory](https://www.pingidentity.com/en/platform/capabilities/directory/pingdirectory.html)

* [PingDirectory community page](https://support.pingidentity.com/s/question/0D51W00007KMHjqSAH/welcome-to-the-pingdirectory-community-page)

* [PingDirectory customer training (existing customers only)](https://www.pingidentity.com/en/support/training/course-details/389.html)

* [Partner portal (partners)](https://support.pingidentity.com/s/not-an-authorized-partner)

---

---
title: Release statuses
description: Learn about the PingDirectory release support statuses and related best practices.
component: pingdirectory
version: 11.1
page_id: pingdirectory::release_status
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/release_status.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  versioning: Versioning
  status-types: Status types
  resources: Resources
---

# Release statuses

The following statuses represent the different types of releases for the PingDirectory suite of products. Each status includes best practices that can help you decide when you need to upgrade your server.

Learn more about the timelines and policies for each type of release in the [Resources](#resources) section of this topic.

|   |                                       |
| - | ------------------------------------- |
|   | This is a short-term support release. |

## Versioning

The PingDirectory suite of products follows a four-digit semantic versioning format. Its third digit is always a placeholder value of `0`, as follows:

`major.minor.0.maintenance`

The following release status types are based on the `major.minor` versions of a release.

## Status types

* Long-term support releases

  A long-term support (LTS) release is designed for critical environments and prioritizes consistent performance and extended maintenance over immediate access to new features.

  Use LTS versions for deployments requiring long, predictable support windows. Plan your upgrades to the next LTS release before the end of support. Apply maintenance releases promptly and follow Ping Identity's security guidance.

* Short-term support releases

  A short-term support (STS) release is designed for environments that need immediate access to new functionality rather than a long maintenance window.

  Use STS releases for rapid feature access, but plan your upgrades to the latest LTS release (or to later STS releases) before the end of maintenance. Keep the deployment on a supported, actively maintained version, apply maintenance releases promptly, and follow Ping Identity's security guidance.

## Resources

* [Software end-of-life policy](https://www.pingidentity.com/en/legal/end-of-life-policy.html): Outlines the specifics of the end-of-life policy for Ping Identity products, including support and maintenance timelines.

* [Software end-of-life tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker): Find the latest version-specific information about the support and maintenance lifecycles for the PingDirectory suite of products.