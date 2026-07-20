---
title: "Comparison: PingOne Advanced Services and PingOne Cloud Platform"
description: As you're transitioning to the cloud, you might wonder which Ping Identity solution will best meet your needs. This comparison shows the differences between our two cloud platforms and is designed to help you select the best solution for your organization.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:comparison_pingone_advanced_services_and_pingone_cloud_platform:p1as_cloud_comparison
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/comparison_pingone_advanced_services_and_pingone_cloud_platform/p1as_cloud_comparison.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 29, 2025
section_ids:
  _deployment_models: Deployment models
  _admin_exp: Admin experience
  _authentication: Authentication
  _authorization: Authorization
  _identity_federation: Identity federation
  _monitoring_and_logging: Monitoring and logging
  _provisioning: Provisioning
  _pingone_directory: PingOne Directory
---

# Comparison: PingOne Advanced Services and PingOne Cloud Platform

As you're transitioning to the cloud, you might wonder which Ping Identity solution will best meet your needs. This comparison shows the differences between our two cloud platforms and is designed to help you select the best solution for your organization.

| PingOne Cloud Platform                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | PingOne Advanced Services                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| With the PingOne Cloud Platform, your users access applications on a subscription basis and never have to download, install, or upgrade applications. PingOne is a software as a service (SaaS) solution that resides on a remote cloud network and can be accessed through the platform or APIs.The platform has a multi-tenancy SaaS architecture, which means that single instances of software and their supporting infrastructure serve multiple customers.It uses an organization-based model to define tenant accounts and their related entities within the platform and cannot be deployed as a single tenant.PingOne solutions can include any of these Ping Identity SaaS services:- PingOne SSO

- PingDirectory

- PingOne MFA / PingID

- PingOne

- PingOne Authorize (includes PingAccess capabilities)

- PingOne Protect

- PingIntelligence for APIsAdopting a cloud-first or cloud-only strategy also helps you comply with rapidly changing electronic data handling regulations, especially in heavily regulated industries such as healthcare and financial services. You also trade capital costs, such as those associated with physical servers and data centers, for variable expenses with a pay-as-you-go system.Whether you just want single sign-on (SSO) *(tooltip: \<div class="paragraph">&#xA;\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>&#xA;\</div>)*, or a risk-based, adaptive authentication authority, starting off with a PingOne solution package lets you only pay for what you need and gives you room to grow. | PingOne Advanced Services has a single-tenancy architecture and provides you with your own virtual private cloud (VPC) network that you define. This virtual network can connect to any data source and closely resembles the network that you operate in your data centers, but in a scalable, secure, cloud environment.This network is hosted by Amazon Web Services (AWS) and isolated from other virtual networks. Your development environments are also isolated from each other within the network and communicate with each other through a central hub.This hub not only facilitates communication, but it also collects data from across your accounts and environments and helps you identify trends and potential threats.PingOne Advanced Services includes:- PingFederate

- PingDirectory

- PingDirectory/ Delegated Admin

- PingAccess

- PingCentral

- PingDataSyncThese services can also be integrated with the PingOne Advanced Services, but are not deployed with the platform by default:- PingOne MFA/ PingID

- PingOne

- PingOne Authorize

- PingOne Protect

- PingIntelligence for APIsMost importantly, PingOne Advanced Services can connect to anything and everything, including legacy systems based on proprietary standards. This solution can also integrate with on-premise data or authentication sources, and act as either an identity provider (IdP) *(tooltip: \<div class="paragraph">&#xA;\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>&#xA;\</div>)* or a service provider (SP) *(tooltip: \<div class="paragraph">&#xA;\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>&#xA;\</div>)*, which makes complex authentication flows possible. |

## Deployment models

Both platforms are built on Amazon Web Services (AWS) *(tooltip: \<div class="paragraph">
\<p>An Amazon subsidiary providing cloud computing platforms.\</p>
\</div>)*, which hosts resources in multiple locations worldwide.Each AWS region is isolated from other AWS regions and contains between two and five availability zones.Each zone is supported by at least one physical data center in that region.Although a single availability zone can span multiple data centers, to reduce the likelihood of two zones failing simultaneously, no two zones share a data center.

You have one region with the PingOne Cloud Platform, and you can have between one and three different regions with PingOne Advanced Services. All regions guarantee uptimes of 99.99%:

* With the PingOne Cloud Platform, your region can be in the United States, Canada, EMEA (Germany or Ireland), or Australia.

* With PingOne Advanced Services, your regions can be in North America (US-West, US-East, or Canada), in EMEA (Germany or Ireland), or in APAC (Australia or Singapore).

PingOne SaaS services can be replicated within their geographic region, and PingOne Advanced Services can be replicated across all regions and across all availability zones within a region.

Both of these solutions are deployed using active-active configurations, which means the database contains at least two active nodes that share data and write to the database. If one connection becomes unavailable, all traffic is routed through the other connection.

Having this type of configuration in place improves application availability, scalability, security, and performance, and reduces, if not eliminates, downtime from new application deployments or database upgrades and patching.

## Admin experience

With the PingOne Cloud Platform, you can manage all of your organization's environments and the users, applications, connections, and experiences within them, directly from the PingOne admin console. Applications are accessible from a catalog.

An administrative console is not yet available for PingOne Advanced Services, but admin consoles are available for PingFederate and PingAccess. These consoles allow you to manage your applications, authentication policies, and data sources yourself. For tasks that you can't complete yourself, submit a service request. See the [Task summary table](../task_summary_table/p1as_task_summary_table.html) for a complete list of these tasks.

PingCentral is also included in PingOne Advanced Services to help you manage your applications across your environments.

| PingOne Cloud Platform                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | PingOne Advanced Services                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The PingOne Cloud Platform also includes:- A self-service admin portal for end users to update their profiles, passwords, and authentication methods.

- The ability to change the look and feel of your registration pages, sign-on pages, and verification pages to match your organization's branding.

- OpenID Connect (OIDC) scope and grant administration capabilities.

- Customizable domain names and notifications. Notification templates are included to help you get started.

- Agreements that users must consent to during the sign-on process. You can present these agreements in different languages and for different locales. | With the PingOne Advanced Services, you work with our Professional Services team to design your virtual network.This virtual network can connect to any data source and can closely resemble the network you operate in your data centers, but in a scalable, secure, cloud environment.Connections can be made using integration kits, or you can use customized integrations to connect to the resources you need.You can also:- Bulk import and export JSON files.

- Import and export SAML metadata.

- Import and export configuration archive `.ZIP` files and even automatically create backup files. |

## Authentication

Authentication is the process of determining whether someone, or something, is who or what they say they are. The ways in which users prove their identities often depend on the sensitivity of the data and digital resources involved. Learn more about how it works in [Authentication](https://www.pingidentity.com/en/resources/identity-fundamentals/authentication.html) in [Identity Fundamentals](https://www.pingidentity.com/en/resources/identity-fundamentals.html).

Both the PingOne Cloud Platform and PingOne Advanced Services support a variety of authentication standards, adapters, and policies, which makes it possible to provide a wide variety of authentication experiences to your customers and workforce.

See the following:

> **Collapse: Customer authentication**
>
> With both platforms, you can use OIDC and SAML 2.0 to design SSO authentication experiences for your customers. PingOne Advanced Services also supports SAML 1.X. These experiences can include any of these features:
>
> * Email verification
>
> * Passive profiling
>
> * Changing and resetting passwords
>
> * Unlocking accounts
>
> * Account linking
>
> * Self-service account management
>
> With PingOne Advanced Services, you can also provide a way for your customers to recover their usernames, and use CAPTCHA for challenge-response authentication.

> **Collapse: Workforce authentication**
>
> Both platforms also support SSO experiences for your employees, partners, and vendors, and can include:
>
> * Browser-based SSO
>
> * Single logout (SLO)
>
> * IdP discovery
>
> * Attribute mapping
>
> With PingOne SaaS products, attribute manipulation can be performed using the Spring Expression Language (SpEL).With PingOne Advanced Services, attribute manipulation is done using Object-Graph Navigation Language (OGNL), which is an open-source expression language for Java.
>
> PingOne Advanced Services also supports WS-Trust, an OASIS standard that directs web service clients and providers to interact with the Security Token Service (STS) *(tooltip: \<div class="paragraph">
> \<p>An entity responsible for responding to WS-Trust requests for validation and issuance of security tokens used for SSO authentication to web services.\</p>
> \</div>)* to issue, renew, and validate security tokens so that a trusted connection can be established. If the receiving entity successfully validates the security token from the requesting entity, the connection is established. If it's unsuccessful, the request is denied.

> **Collapse: Authentication adapters**
>
> The PingOne Cloud Platform and PingOne Advanced Services support a wide variety of adapters to connect your authentication applications and services to the platform:
>
> * **Identifier-first login**: Authenticates users in two separate steps, which is useful if you need to display a separate, branded sign-on page based on an email address or user domain. It can also be used to trigger additional security mechanisms based on user IDs or email addresses.
>
> * **Social login**: Authenticates users by using existing sign-on information from a social network provider like Facebook, Twitter, or Google to sign on to a third-party website instead of creating a new account specifically for that website.
>
> * **External IdPs**: Authenticates users using SAML or OIDC and your external databases, applications, and services.
>
> * **Active Directory (AD) *(tooltip: \<div class="paragraph">
>   \<p>A directory service for Windows domain networks, included in most Windows Server operation systems.\</p>
>   \</div>)*** or another identity repository authenticates users in those databases using LDAP or RADIUS gateways.
>
> * **Kerberos**: Authenticates users and client-server applications using time-limited secret-key cryptography, multiple secret keys, and a third-party service.
>
> * **PingOne MFA or PingID**: Authenticates users after they present at least two pieces of evidence that they are who they claim to be.
>
> PingOne Advanced Services also supports the [OpenToken adapter](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_opentoken_adapt.html), the Agentless Integration Kit, and Microsoft Entra certificate-based authentication (CBA), which enables users to authenticate directly with client certificates (X.509) against Microsoft Entra ID.

> **Collapse: Authentication policies**
>
> Authentication policies determine the order and conditions in which various authentication mechanisms are used to successfully authenticate a user:
>
> * With the PingOne Cloud Platform, you can configure sign-on policies, PingOne policies, and authentication API policies.
>
> * With PingOne Advanced Services, not only can you configure sign-on, include::partial$common\_product\_keydefs.adoc\[tags=singularkey], and API policies, but you can also use authentication selectors, reusable policy fragments, and policy builders to design unique authentication experiences for your users.

## Authorization

With the PingOne Cloud Platform, you can manage all of your organization's environments and the users, applications, connections, and experiences within them, directly from the PingOne admin console. Applications are accessible from a catalog.

An administrative console is not yet available for PingOne Advanced Services, but admin consoles are available for PingFederate and PingAccess. These consoles allow you to manage your applications, authentication policies, and data sources yourself. For tasks that you can't complete yourself, submit a service request. See the [Task summary table](../task_summary_table/p1as_task_summary_table.html) for a complete list of these tasks.

PingCentral is also included in PingOne Advanced Services to help you manage your applications across your environments.

| PingOne Cloud Platform                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | PingOne Advanced Services                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The PingOne Cloud Platform also includes:- A self-service admin portal for end users to update their profiles, passwords, and authentication methods.

- The ability to change the look and feel of your registration pages, sign-on pages, and verification pages to match your organization's branding.

- OpenID Connect (OIDC) scope and grant administration capabilities.

- Customizable domain names and notifications. Notification templates are included to help you get started.

- Agreements that users must consent to during the sign-on process. You can present these agreements in different languages and for different locales. | With the PingOne Advanced Services, you work with our Professional Services team to design your virtual network.This virtual network can connect to any data source and can closely resemble the network you operate in your data centers, but in a scalable, secure, cloud environment.Connections can be made using integration kits, or you can use customized integrations to connect to the resources you need.You can also:- Bulk import and export JSON files.

- Import and export SAML metadata.

- Import and export configuration archive `.ZIP` files and even automatically create backup files. |

## Identity federation

Federated identity management (FIM) is a system that allows users in separate organizations to access the same networks, applications, and resources using one set of credentials. Each organization maintains their own identity management systems, which are linked to a third-party Idp that stores user credentials and authenticates users across organizations.

Both the PingOne Cloud Platform and PingOne Advanced Services support a variety of functions that help ensure communication between federated entities remains secure:

* Metadata URL consuming and publishing, which provides additional information about a site that's embedded into its code.

* OAuth redirect URI validation, which helps ensure users are directed to appropriate locations after they successfully sign-on.

* SSL and TLS encryption, which helps ensure that communications between a client and server are secure.

* Key rotation policies, which define when a signing key should be retired and replaced with a new cryptographic key.

* Self-signed certificates. PingOne Advanced Services supports both signed and self-signed certificates. There is no cryptographic difference between the two as they use the same algorithm and have the same key length, but some partners might not support unanchored trust models.

PingOne Advanced Services also supports:

* Mutual TLS authentication, where the two parties authenticate each other using the TLS protocol.

* The certificate revocation list (CRL) *(tooltip: \<div class="paragraph">
  \<p>A list of revoked signing certificates, maintained by the issuing authority at a public URL.\</p>
  \</div>)*, which is a list of revoked certificates downloaded from the certificate authority (CA) *(tooltip: \<div class="paragraph">
  \<p>An entity that issues digital certificates.\</p>
  \</div>)*, and Online Certificate Status Protocol (OCSP) *(tooltip: \<div class="paragraph">
  \<p>The protocol used by CAs to check the revocation status of an X.509 certificate.\</p>
  \</div>)*, which is used to check revocation of a single certificate interactively using an online service called an OCSP responder.

## Monitoring and logging

Both the PingOne Cloud Platform and PingOne Advanced Services have a variety of monitoring and logging tools to help you stay informed about the health of your network and to help you troubleshoot issues if they arise:

* With the PingOne Cloud Platform, you use webhooks, also known as subscriptions, to monitor events in PingOne.You can retrieve logs through the admin console or through the API.Audit logs, which record all actions performed in the admin console and in PingDirectory, are also available.Learn more in [PingOne Platform logging and reporting](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_logging_reporting_overview.html) in the PingOne documentation.

* With PingOne Advanced Services, your organization has its own dedicated cloud network that you define, without having to manage cloud resources, containers, networking, scaling, healing, and backup and restoration.

  Our Support team and our Site Reliability Engineers proactively monitor your infrastructure and deployments and attempt to address issues before they become problems. If outages occur, we'll notify you using standard support methods.

  You are responsible for monitoring your Ping applications and configurations, but we will stream log files to you, which will help you identify, monitor, and resolve any issues you might encounter. You can also subscribe to receive alerts from PingOne Advanced Services, which will notify you of events occurring within your network. Learn more in the [Monitoring and logging](../monitoring_and_logging/p1as_monitoring_logging.html) section of this guide.

## Provisioning

Provisioning is a process for creating, updating, and deleting users and accounts across your IT infrastructure. In any enterprise, users access many different applications and resources daily.

Managing accounts and permissions across a variety of systems for a large number of users might seem like a daunting task. Fortunately, automated provision is available in both PingOne and PingOne Advanced Services.

Using automated user and account provisioning ensures that your users can access the applications, files, and other resources they need while minimizing the need for system administrators to be involved.

* With PingOne SaaS, inbound and outbound AD and LDAP directory synchronization is performed using the PingOne gateway.

* With PingOne Advanced Services, inbound and outbound synchronization is performed using either PingFederate or PingDataSync.

## PingOne Directory

Both PingOne SaaS and PingOne Advanced Services use [PingDirectory](https://docs.pingidentity.com/pingdirectory/latest/pd_ds_landing_page.html) as the identity repository for their platforms. Not only does PingDirectory simplify administration, reduces costs, and secures information in systems that scale for large numbers of users, but it also acts as your single source of identity truth across your organization.

Although both cloud solutions use PingDirectory, the ways in which it can be used differ between them.See the following for details regarding those differences.

> **Collapse: Data modeling**
>
> Data modeling is a process that you use to define the structure of a database before implementing it. The database can simply store information about customers and products, or it could be used for something much more complicated, such as tracking sales and trends across a global network of stores.
>
> * PingOne SaaS uses PingDirectory as its database, which is only used to manage user identities.
>
> * With PingOne Advanced Services, you can use data modeling to manage:
>
>   * Structured and unstructured data
>
>   * Any type of object, such as devices, tokens, and consents
>
>   * Custom data requests

> **Collapse: Schemas**
>
> Schemas are sets of rules that define the directory structures, which guarantee that new data entries and modifications meet and conform to these predetermined rules and definitions:
>
> * PingOne SaaS comes with a standard extendable schema for all of your environments, which you can build upon and customize to meet your needs.
>
>   You can add single-valued, multivalued, and custom attributes, which are all validated, including regex and enumerated values. Learn more about schemas in [About the schema](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_schema.html) in the PingDirectory documentation.
>
> * The PingOne Advanced Services schema uses LDAP v3. Schemas and global ACIs, which are completely customizable.
>
>   Submit a [Schema - attribute type](../task_summary_table/p1as_pd_schema_att_type.html), a [Schema - objectClass](../task_summary_table/p1as_pd_schema_objectclass.html), or [ACI service request](../task_summary_table/p1as_pd_acis.html) to your Ping Identity support team, who will build the schema and customize global ACIs to best meet your needs.

> **Collapse: Identities and attributes**
>
> In each PingOne Saas environment, you can have a maximum of:
>
> * Twenty million identities without incurring additional costs
>
> * One hundred declared attributes (200 attributes by the end of Q2, 2023)
>
> * 100 JSON attributes
>
> With PingOne Advanced Services, there is no limit to the number of identities or attributes you can have in each environment. The largest number of identities currently supported is 170 million.

> **Collapse: Admin experience**
>
> With PingOne SaaS, you can manage your users, user groups, and attributes through the administrative console or through the [REST](https://docs.pingidentity.com/pingdirectory/latest/pingdirectoryproxy_server_administration_guide/pd_proxy_directory_rest_api.html) or [Identity Access APIs](https://docs.pingidentity.com/pingdirectory/latest/managing_scim_11_and_20_servlet_extensions/pd_proxy_identity_access_api.html).
>
> [PingOne DaVinci](https://docs.pingidentity.com/davinci/davinci_introduction.html), an orchestration platform that lets you create flows to guide users through defined tasks, can be connected to PingOne.
>
> An administrative console is not available for PingOne Advanced Services, but [Delegated Admin](https://docs.pingidentity.com/pingdirectory/latest/delegated_admin_application_guide/pd_da_introduction.html) is.
>
> You can also use LDAP to directly manage your users, groups, and attributes within the directory, and submit a [PingDirectory service request](../task_summary_table/p1as_pd_service_requests.html) to request additional customization.
>
> PingOne DaVinci can also be connected to PingOne using an LDAP gateway.

> **Collapse: Password policies**
>
> Password policies are sets of rules that user passwords must adhere to. For example, a password policy might require that passwords contain at least five characters and include at least one special character. With PingDirectory, you can also specify:
>
> * Whether passwords should expire
>
> * Whether users are allowed to modify their own passwords
>
> * Whether too many failed authentication attempts should result in an account lockout
>
> To help get you started quickly, PingDirectory provides three different out-of-the-box password policies that you can apply to your entries or as templates for configuring customized policies. Learn more about these policies in [Viewing password policies](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_view_password_policies.html) in the PingDirectory documentation.
>
> * With PingOne SaaS, password policies are highly customizable and assigned at the population level. These policies can also be used with a wide variety of password validators, except Regex.
>
> * PingOne Advanced Services provides more flexibility and can be assigned at the group or user level.
>
>   Not only can this platform be integrated with most password validators, such as Dictionary, Haystack, and Regex, it can also be integrated with Have I Been Pwned?. This application allows users to check and see if their personal data has been compromised in a data breach.

> **Collapse: Password authentication**
>
> Passthrough authentication allows your users to sign on to both on-premises and cloud-based applications using the same passwords. This feature provides your users a better experience because there's one less password to remember, which reduces IT help desk costs.
>
> With PingOne SaaS, passthrough authentication is performed using either:
>
> * [PingOne SSO](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_p1sso_start.html)
>
> * [PingOne gateways](https://docs.pingidentity.com/pingone/integrations/p1_gateways.html)
>
> With PingOne Advanced Services, passthrough authentication can be performed using either:
>
> * [PingOne SSO](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_p1sso_start.html)
>
> * [Active Directory](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)
>
> * Custom authentication plugins

> **Collapse: Replication**
>
> Replication is a data synchronization mechanism that ensures that updates made to a database are automatically duplicated to other servers. Replication improves data availability when unforeseen or planned outages occur and improves search performance by allowing client requests to be distributed across multiple servers.
>
> With PingOne SaaS, PingDirectory handles replication and redundancy, but with PingOne Advanced Services, you can use any replication system you choose.

> **Collapse: External directory syncing**
>
> Data synchronization is the ongoing process of synchronizing data between two or more devices and updating changes automatically between them to maintain consistency between systems.
>
> Synchronization and replication are not the same thing. With replication, exact replicas of the data are created and stored in a variety of different locations. Synchronization can:
>
> * Transform data between two different directory information tree (DIT) structures.
>
> * Map attribute types.
>
> * Synchronize subsets of branches and specific object classes.
>
> With PingOne SaaS, inbound and outbound AD and LDAP directory synchronization is performed using the PingOne gateway.
>
> With PingOne Advanced Services, inbound and outbound synchronization is performed using PingDataSync.

> **Collapse: Encryption and algorithms**
>
> Encryption is a way of scrambling data so that only authorized parties can understand the information, which is standardized across PingOne SaaS and PingOne Advanced Services environments. Entry and attribute-level encryption is also available with PingOne Advanced Services.
>
> * PingOne SaaS uses the standard hashing algorithm, SSHA-512, to ensure that the data is stored in a scrambled state, so it's harder to steal.
>
>   A variety of other password hashing algorithms can also be used, but are rehashed after the initial authentication.
>
> * PingOne Advanced Services supports additional password hashing algorithms including SSHA, PBKDF2, bcrypt, msCrypto, and Argon2.