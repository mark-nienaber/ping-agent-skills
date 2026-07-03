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
