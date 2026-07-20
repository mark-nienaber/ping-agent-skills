---
title: About IDM
description: "Overview of PingIDM: Reconciling user accounts across distributed data stores and resources"
component: pingidm
version: 8.1
page_id: pingidm:getting-started:about-idm
canonical_url: https://docs.pingidentity.com/pingidm/8.1/getting-started/about-idm.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Getting Started"]
section_ids:
  gsg-what-openidm-cando: What Can You Do With IDM?
  gsg-integration: PingIDM Integrations
---

# About IDM

Whenever you need access to important information, administrators need to know who you are. They need to know your identity, which may be distributed in multiple accounts.

As a user, you might have several accounts even within your own company, for functions such as:

* Email

* Human Resources

* Payroll

* Engineering, Support, Accounting, and other functions

Each of these accounts may be stored in different resources, such as DS, Active Directory, OpenLDAP, and more. Keeping track of user identities in each of these resources (also known as data stores) can get complex. IDM simplifies the process, as it reconciles differences between resources.

With situational policies, IDM can handle discrepancies such as a missing or updated address for a specific user. The server includes default but configurable policies to handle such conditions. In this way, consistency and predictability is ensured, in an otherwise chaotic resource environment.

IDM can make it easier to track user identities across these resources. IDM has a highly scalable, modular, readily deployable architecture that can help you manage workflows and user information.

## What Can You Do With IDM?

This software allows you to simplify the management of identity, as it can help you synchronize data across multiple resources. Each organization can maintain control of accounts within their respective domains.

IDM works equally well with user, group, and device identities.

You can also configure workflows to help users manage how they sign up for accounts, as part of how IDM manages the life cycle of users and their accounts.

You can manage employee identities as they move from job to job. You will make their lives easier as their user accounts can be registered on different systems automatically. Later, IDM can increase productivity when it reconciles information from different accounts, saving users the hassle of entering the same information on different systems.

## PingIDM Integrations

Now that you have seen how IDM can help you manage users, review the features that IDM can bring to your organization:

* *Web-Based Administrative User Interface*

  Configure IDM with the Web-Based Administrative User Interface. You can configure many major server components without ever touching a text configuration file.

* *Role-Based Provisioning*

  Create and manage users based on attributes such as organizational need, job function, and geographic location.

* *Backend Flexibility*

  Choose the desired backend database for your deployment. IDM supports MySQL, Microsoft SQL Server, Oracle Database, IBM DB2, and PostgreSQL. For the supported versions of each database, refer to [Before you install](../release-notes/before-you-install.html).

* *Password Management*

  Set up fine-grained control of passwords to ensure consistent password policies across all applications and data stores. Supports separate passwords per external resource.

* *Logging, Auditing, and Reporting*

  IDM logs all activity, internally and within connected systems. With such logs, you can track information for access, activity, authentication, configuration, reconciliation, and synchronization.

* *Access to External Resources*

  IDM can access a generic scripted connector that allows you to set up communications with many external data stores.

---

---
title: Getting started
description: Guide to installing and evaluating PingIDM software. This software offers flexible services for automating management of the identity life cycle
component: pingidm
version: 8.1
page_id: pingidm:getting-started:preface
canonical_url: https://docs.pingidentity.com/pingidm/8.1/getting-started/preface.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Getting Started", "Demo", "Install", "Setup &amp; Configuration"]
page_aliases: ["index.adoc"]
---

# Getting started

> Guide to installing and evaluating PingIDM software. This software offers flexible services for automating management of the identity life cycle.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

Quick Start

[icon: eye, set=fad, size=3x]

#### [Start Here](about-idm.html)

Learn about what IDM does and how it can help your organization.

[icon: map-signs, set=fad, size=3x]

#### [Where To Go from Here](where-to-go.html)

Find pointers to the IDM product documentation to learn more about IDM.

---

---
title: Where to go from here
description: Pointers to PingIDM product documentation covering reconciliation, connectors, authentication, role management, workflows, and use cases
component: pingidm
version: 8.1
page_id: pingidm:getting-started:where-to-go
canonical_url: https://docs.pingidentity.com/pingidm/8.1/getting-started/where-to-go.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Getting Started", "Demo", "Reconciliation", "Authentication", "Roles", "Workflows", "Process", "Data Store"]
section_ids:
  gsg-recon: Reconciliation
  gsg-connectors: Connectors
  scripted_and_custom_connectors: Scripted and custom connectors
  try_it_out: Try it out
  gsg-auth-modules: Authentication Modules
  gsg-role-management: User Role Management
  gsg-bpmn: Business Processes and Workflows
  gsg-usecases: Additional Samples
---

# Where to go from here

IDM can do much more than reconcile data between two different sources. Read about the key product features in these sections:

## Reconciliation

IDM supports reconciliation between two data stores, as a source and a target.

In identity management, reconciliation compares the contents of objects in different data stores, and makes decisions based on configurable policies.

For example, if you have an application that maintains its own user store, IDM can ensure your canonical directory attributes are kept up-to-date by reconciling their values as they are changed.

For more information, refer to [Synchronization overview](../synchronization-guide/sync-overview.html).

## Connectors

PingIDM uses connectors to integrate with external resources, both on-premise and in the cloud. Connectors handle the communication between IDM and a target resource, letting you synchronize, provision, and reconcile identity data across your environment.

Connectors are provided for many external resources, including:

* [Google Apps](https://docs.pingidentity.com/openicf/connector-reference/google.html)

* [Salesforce](https://docs.pingidentity.com/openicf/connector-reference/salesforce.html)

* [LDAP](https://docs.pingidentity.com/openicf/connector-reference/ldap.html) (supports any LDAPv3-compliant directory, including [PingDS](https://docs.pingidentity.com/pingds/8.1/install-guide) and Active Directory)

* [CSV file](https://docs.pingidentity.com/openicf/connector-reference/csv.html)

* [Database table](https://docs.pingidentity.com/openicf/connector-reference/dbtable.html)

|   |                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------- |
|   | Check out the full list of [available connectors](https://docs.pingidentity.com/openicf/connector-reference/preface.html). |

### Scripted and custom connectors

If the resource you need isn't covered by a dedicated connector, use one of the scripted connector frameworks to connect to virtually any external resource:

* Groovy connector toolkit

  Run Groovy scripts to interact with any external resource that exposes a supported interface.

  Learn more in [Groovy connector toolkit](https://docs.pingidentity.com/openicf/connector-reference/groovy.html).

  For a sample implementation of the scripted Groovy connector, refer to [Connect to DS with ScriptedREST](../samples-guide/scripted-rest-with-dj.html).

* PowerShell connector toolkit

  Provision a variety of Microsoft services, including Active Directory, SQL Server, Microsoft Exchange, SharePoint, Microsoft Entra ID, and Microsoft 365.

  Learn more in [PowerShell connector](https://docs.pingidentity.com/openicf/connector-reference/powershell.html).

  For a sample configuration, refer to [Connect to Active Directory with the PowerShell connector](../samples-guide/scripted-powershell-with-ad.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Which connector should I use?First, check for a dedicated connector ([full list of connectors](https://docs.pingidentity.com/openicf/connector-reference/preface.html)). If one isn't available:* If your resource exposes a REST API, start with the [Groovy connector toolkit](https://docs.pingidentity.com/openicf/connector-reference/groovy.html) or [Scripted REST connector](https://docs.pingidentity.com/openicf/connector-reference/scripted-rest.html).

* For Microsoft services on Windows, use the [PowerShell connector toolkit](https://docs.pingidentity.com/openicf/connector-reference/powershell.html).

* For LDAP-compliant directories, use the [LDAP connector](https://docs.pingidentity.com/openicf/connector-reference/ldap.html).

* For SCIM-compliant cloud applications, use the [SCIM connector](https://docs.pingidentity.com/openicf/connector-reference/scim.html).

* For relational databases, use the [Database table connector](https://docs.pingidentity.com/openicf/connector-reference/dbtable.html) or [Scripted SQL connector](https://docs.pingidentity.com/openicf/connector-reference/scripted-sql.html). |

### Try it out

Many of the [samples provided with IDM](../samples-guide/samples-provided.html) walk you through connecting to different resources step-by-step. For example:

| Sample name                                                                        | Description                                          |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------- |
| [sync-with-csv](../samples-guide/sync-with-csv.html)                               | Synchronize data from a CSV file into IDM.           |
| [sync-with-ldap-bidirectional](../samples-guide/sync-with-ldap-bidirectional.html) | Two-way synchronization with an LDAP directory.      |
| [sync-with-salesforce](../samples-guide/sync-with-salesforce.html)                 | Synchronize users between Salesforce and IDM.        |
| [sync-with-google](../samples-guide/sync-with-google.html)                         | Synchronize accounts with the Google Apps connector. |
| [sync-with-scim](../samples-guide/sync-with-scim.html)                             | Synchronize data between IDM and a SCIM provider.    |

## Authentication Modules

IDM provides several authentication modules to help you protect your systems. For more information, refer to [Authentication and session modules](../auth-guide/auth-session-modules.html).

## User Role Management

Some users need accounts on multiple systems. For example, insurance agents may also have insurance policies with the company that they work for. In that situation, the insurance agent is also a customer of the company.

Alternatively, a salesperson may also test customer engineering scenarios. That salesperson may also need access to engineering systems.

Each of these user scenarios is known as a *role*. You can set up a consolidated set of attributes associated with each role. To do so, you would configure custom roles to assign to selected users. For example, you may assign both *insured* and *agent* roles to an agent, while assigning the *insured* role to all customers.

In a similar fashion, you can assign both *sales* and *engineering* roles to the sales engineer.

You can then synchronize users with those roles into appropriate data stores.

For more information, refer to [Managed Roles](../objects-guide/roles.html#managed-roles). For a sample of how you can configure external roles, refer to [Provision users with roles](../samples-guide/provisioning-with-roles.html).

## Business Processes and Workflows

A business process begins with an objective and includes a well-defined sequence of tasks to meet that objective.

You can also automate many of these tasks as a workflow.

After you configure the right workflows, a newly hired engineer can log in to IDM and request access to manufacturing information.

That request is sent to the appropriate manager for approval. After it is approved, IDM provisions the new engineer with access to manufacturing.

IDM supports workflow-driven provisioning activities, based on the embedded [Flowable](https://flowable.com/open-source/docs/) Process Engine, which complies with the [Business Process Model and Notation 2.0](https://www.omg.org/spec/BPMN/2.0/) (BPMN 2.0) standard.

## Additional Samples

IDM is a lightweight and highly customizable identity management product.

The documentation includes a number of additional use cases. Most of these are known as *Samples*, and are described in [Samples provided with IDM](../samples-guide/samples-provided.html).

These samples include step-by-step instructions on how you can connect to different data stores, customize product behavior using JavaScript and Groovy, and administer IDM with common REST API commands.