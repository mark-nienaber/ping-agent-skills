---
title: Application Integration Guide
description: This guide will walk the developer through the steps to enable standards-based Single Sign-On (SSO) to an application by integrating the application with the Ping platform.
component: developer-resources
page_id: developer-resources:application_integration_guide:index
canonical_url: https://docs.pingidentity.com/developer-resources/application_integration_guide/index.html
revdate: May 3, 2021
page_aliases: ["dev_app_int_overview.adoc"]
---

# Application Integration Guide

This guide will walk the developer through the steps to enable standards-based Single Sign-On (SSO) to an application by integrating the application with the Ping platform.

Using the concept of "Integrate, Federate and Operate" we can describe the steps an application owner must complete to provide and manage federated SSO in their application:

* Integrate involves making the application federation-aware so that it can accept a federated security token and use the information in that token to authorize a user and create an application session.

* Federate consists of creating federated connections with partners (primarily exchanging metadata).

* Operate describes the management of these connections, adding new customers, managing connections at scale.

This guide will focus on the integrate step.
