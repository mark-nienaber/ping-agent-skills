---
title: Identity federation, identity repositories, and identity provisioning
description: If you work for or with federal, state, and local government agencies, you understand how important it's to keep your data secure and that you must comply with stricter standards and regulations than most industries.
component: pgic
page_id: pgic:identity_federation:pgic_federation
canonical_url: http://docs.pingidentity.com/pgic/identity_federation/pgic_federation.html
section_ids:
  federation: Identity federation
  repositories: Identity repositories
  provisioning: Identity provisioning
---

# Identity federation, identity repositories, and identity provisioning

If you work for or with federal, state, and local government agencies, you understand how important it's to keep your data secure and that you must comply with stricter standards and regulations than most industries.

The ways in which Ping Government Identity Cloud handles identity federation, identity repositories, and provisioning help ensure that your data is safely provisioned, stored, and remains secure.

Learn more:

* [Identity federation](#federation)

* [Identity repositories](#repositories)

* [Identity provisioning](#provisioning)

## Identity federation

Federated Identity Management (FIM) is a system that makes it possible for users in separate organizations to access the same networks, applications, and resources using one set of credentials. This system improves user experiences by reducing password fatigue and enhances security by centralizing identity management and access control.

Ping Government Identity Cloud supports a variety of functions that help ensure communication between federated entities remains secure:

* Metadata URL consuming and publishing, which provides additional information about a site that's embedded into its code.

* OAuth redirect URI validation, which helps ensure users are directed to appropriate locations after they successfully sign on to the system.

* SSL and TLS encryption, which helps ensure that communications between a client and server are secure.

* Key rotation policies, which specify when a signing key should be retired and replaced with a new cryptographic key.

* Self-signed certificates. Ping Government Identity Cloud supports both signed and self-signed certificates. There is no cryptographic difference between the two as they use the same algorithm and have the same key length, but some partners might not support unanchored trust models.

Ping Government Identity Cloud also supports:

* Mutual TLS authentication, where two parties authenticate each other using the TLS protocol.

* The certificate revocation list (CRL), which is a list of revoked certificates downloaded from the certificate authority (CA), and Online Certificate Status Protocol (OCSP), which is used to check revocation of a single certificate interactively using an online service called an OCSP responder.

## Identity repositories

Ping Government Identity Cloud can use [PingDirectory](https://docs.pingidentity.com/pingdirectory/latest/pd_ds_landing_page.html) or the [PingDirectory](https://docs.pingidentity.com/pingdirectory/latest/pd_ds_intro_pindirectory_server.html) server as the identity repository for your organization. Not only do these applications simplify administration, reduce costs, and secure information in systems that scale for large numbers of users, but it also acts as the single source of identity truth for your organization.

Repository processes, policies, and features used with Ping Government Identity Cloud include:

* Data modeling

  Data modeling is a process that you use to define the structure of a database before implementing it. The database can simply store information about customers and products, or it could be used for something much more complicated, such as tracking sales and trends across a global network of stores.

  You can use data modeling to manage:

  * Structured and unstructured data

  * Any type of object, such as devices, tokens, and consents

  * Custom data requests

* Schemas

  Schemas are sets of rules that define the directory structures, which guarantee that new data entries and modifications meet and conform to predetermined rules and definitions.

  The Ping Government Identity Cloud schema uses LDAP v3. Schemas and global ACIs, which are completely customizable. Our Professional Services team will work with you to set these up to meet your needs.

* Unlimited number of identities and attributes

  With Ping Government Identity Cloud, there is no limit to the number of identities or attributes you can have in each environment.

* Administrator experience

  You can manage your users, user groups, and attributes through the administrative console, or through a [PingDirectory REST API](https://docs.pingidentity.com/pingdirectory/10.3/pingdirectory_server_administration_guide/pd_ds_directory_rest_api.html) or the [Identity Access API](https://docs.pingidentity.com/pingdirectory/10.3/managing_scim_11_and_20_servlet_extensions/pd_proxy_identity_access_api.html).

  You can also use LDAP to directly manage your users, groups, and attributes within the directory, and submit a service request to request additional customization.

* Password policies

  Password policies are sets of rules that user passwords must adhere to. For example, a password policy might require that passwords contain at least five characters and include at least one special character. With [PingDirectory](https://docs.pingidentity.com/pingdirectory/10.3/pd_ds_landing_page.html) or the [PingDirectory server](https://docs.pingidentity.com/pingdirectory/10.3/pd_ds_intro_pindirectory_server.html), you can also specify whether:

  * Passwords should expire

  * Users are allowed to modify their own passwords

  * Too many failed authentication attempts should result in an account lockout

    These policies can be assigned at the group or user level.

    To help get you started quickly, [PingDirectory](https://docs.pingidentity.com/pingdirectory/10.3/pd_ds_landing_page.html) and [PingDirectory server](https://docs.pingidentity.com/pingdirectory/10.3/pd_ds_intro_pindirectory_server.html), provide three different out-of-the-box password policies that you can apply to your entries, or use as templates for configuring customized policies. Learn more about these policies in [Viewing password policies](https://docs.pingidentity.com/pingdirectory/10.3/pingdirectory_server_administration_guide/pd_ds_view_password_policies.html) in the PingDirectory documentation.

* Passthrough authentication

  Passthrough authentication allows your users to sign on to both on-premises and cloud-based applications using the same passwords. This feature provides your users a better experience because there's one less password to remember, and helps reduce IT help desk costs.

  Passthrough authentication can be performed using either:

  * [Active Directory](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)

  * Custom authentication plugins, such as an X509 adapter

* Replication

  Replication is a data synchronization mechanism that ensures that updates made to a database are automatically duplicated to other servers. Replication improves data availability when unforeseen or planned outages occur, and improves search performance by allowing client requests to be distributed across multiple servers.

* External directory syncing

  Data synchronization is the ongoing process of synchronizing data between two or more devices and updating changes automatically between them to maintain consistency between systems.

  Synchronization and replication are not the same thing. With replication, exact copies of the data are created and stored in a variety of different locations.

  Synchronization can:

  * Transform data between two different directory information tree (DIT) structures

  * Map attribute types

  * Synchronize subsets of branches and specific object classes with Ping Government Identity Cloud. Inbound and outbound synchronization is performed using [PingDataSync](https://docs.pingidentity.com/pingdirectory/10.3/pingdatasync_server_administration_guide/pd_sync_data_sync_process.html) or [PingIDM](https://docs.pingidentity.com/pingidm/8/getting-started/preface.html).

* Encryption and algorithms

  Encryption is a way of scrambling data so that only authorized parties can understand the information, which is standardized in Ping Government Identity Cloud environments. Ping Government Identity Cloud supports leading algorithms including SSHA (Seeded Secure Hash Algorithm), PBKDF2 (Password-Based Key Derivation Function 2), bcrypt, msCrypto, and Argon2.

## Identity provisioning

Provisioning accounts is the process of creating, updating, and deleting users and accounts across different systems and applications within an organization.

Provisioning accounts and managing permissions across a variety of systems for a large number of users might seem like a daunting task. Fortunately, automated provisioning is available in Ping Government Identity Cloud.

Using automated user and account provisioning ensures that your users can access the applications, files, and other resources they need while minimizing the need for system administrators to be involved.
