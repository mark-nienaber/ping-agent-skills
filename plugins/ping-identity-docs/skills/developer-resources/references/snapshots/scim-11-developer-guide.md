---
title: SCIM 1.1 Developer Guide
description: SCIM or System for Cross-Domain Identity Management is a federated provisioning protocol. Providing a consistent API for user and group CRUD (Create, Read, Update and Delete) actions.
component: developer-resources
page_id: developer-resources:scim_11_developer_guide:index
canonical_url: https://docs.pingidentity.com/developer-resources/scim_11_developer_guide/index.html
revdate: May 3, 2021
page_aliases: ["dev_scim11_overview.adoc"]
---

# SCIM 1.1 Developer Guide

SCIM or System for Cross-Domain Identity Management is a federated provisioning protocol. Providing a consistent API for user and group CRUD (Create, Read, Update and Delete) actions.

SCIM can be used by developers to standardize the way user profile information is retrieved from a data source (i.e. instead of having to manage connections to SQL tables, LDAP datastores and other data stores SCIM can provide a single interface to this data).

SCIM can also be used to provision user and group information from an enterprise to a partner (i.e. SaaS application) either as an out-of-band process or as part of an authentication action.

This developers guide provides a reference for developers to build against a SCIM data store interface to help standardize the method used to access identity data in a federated manner. It uses information from the SCIM v1.1 specifications (specifically the core schema and the SCIM API).

This developer guide references the SCIM v1.1 specifications:

* [SCIM Core Schema 1.1](http://www.simplecloud.info/specs/draft-scim-core-schema-01.html)

* [SCIM Protocol API 1.1](http://www.simplecloud.info/specs/draft-scim-api-01.html)

|   |                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Although this guide provides raw protocol calls, it is highly recommended a developer utilize existing libraries to avoid implementation specific errors. |
