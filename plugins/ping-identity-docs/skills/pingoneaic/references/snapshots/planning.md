---
title: Approach
description: Discover, rationalize, and implement identity data models aligned to business requirements
component: pingoneaic
page_id: pingoneaic:planning:plan-object-modeling-approach
canonical_url: https://docs.pingidentity.com/pingoneaic/planning/plan-object-modeling-approach.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Object modeling", "Data object model", "Framework", "Planning"]
page_aliases: ["plan-deploy:planning-object-modeling-approach.adoc"]
---

# Approach

The approach to data object modeling in PingOne Advanced Identity Cloud consists of three main phases: discovery, rationalization, and implementation.

* Discovery

  This stage involves the discovery of the current state of the identity and future requirements, including:

  * Sources of identity information, such as customer databases, directories, and third-party identity providers

  * Business application requirements, including the authorization model and identity data required for operation

  * Authentication requirements

  * Actors and entities within the identity space, including users, roles, and organizations

* Rationalization

  This stage involves analyzing the results from the discovery phase and defining privileges to deliver a workable object model. This step involves the following:

  * Includes all entities and attributes required for authentication, authorization, and identity management

  * Excludes identity data that is not relevant to business requirements

  * Defines all privileges for access to identity data at the field level

  * Maps all identity data from Advanced Identity Cloud to external repositories and vice-versa

* Implementation

  This stage involves configuring the managed data object model within the PingOne Advanced Identity Cloud tenant, following the detailed plan developed during the rationalization phase. This step includes the following configuration:

  * Ping Identity object attributes, roles, and internal privileges

  * Connector definitions for external repositories, including the attributes returned by each connector

  * Synchronization mappings for Advanced Identity Cloud to external repositories and vice-versa
