---
title: About ICF and ICF connectors
description: Overview of the Identity Connector Framework (ICF), its capabilities, and how to build, use, and deploy ICF connectors with PingIDM
component: openicf
page_id: openicf:connector-dev-guide:about-icf
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/about-icf.html
section_ids:
  openicf-functionality: Overview of ICF functionality
---

# About ICF and ICF connectors

The OpenICF (ICF) provides interoperability between identity, compliance, and risk management solutions. An ICF connector enables provisioning software, such as PingIDM, to manage the identities that are maintained by a specific identity provider.

ICF connectors provide a consistent layer between identity applications and target resources, and expose a set of operations for the complete lifecycle of an identity. The connectors provide a way to decouple applications from the target resources to which data is provisioned.

ICF focuses on provisioning and identity management, but also provides general purpose capabilities, including authentication, create, read, update, delete, search, scripting, and synchronization operations. Connector bundles rely on the ICF Framework, but applications remain completely separate from the connector bundles. This lets you change and update connectors without changing your application or its dependencies.

Many connectors have been built within the ICF framework, and are maintained and supported by Ping and by the ICF community. However, you can also develop your own ICF connector, to address a requirement that is not covered by one of the existing connectors. In addition, ICF provides two *scripted connector toolkits*, that let you write your own connectors based on Groovy or PowerShell scripts.

The ICF framework can use IDM, Sun Identity Manager, and Oracle Waveset connectors (version 1.1), and can use ConnID connectors up to version 1.4.

This guide provides the following information:

* An overview of the ICF framework and its components

* Information on how to use the ICF existing connectors in your application (both locally and remotely)

* Information on how to write your own Java and .NET connectors, scripted Groovy connectors, or scripted PowerShell connectors

## Overview of ICF functionality

ICF provides many capabilities, including the following:

* Connector pooling

* Timeouts on all operations

* Search filtering

* Search and synchronization buffering and result streaming

* Scripting with Groovy, JavaScript, shell, and PowerShell

* Classloader isolation

* An independent logging API/SPI

* Java and .NET platform support

* Opt-in operations that support both simple and advanced implementations for the same CRUD operation

* A logging proxy that captures all API calls

* A Maven connector archetype to create connectors
