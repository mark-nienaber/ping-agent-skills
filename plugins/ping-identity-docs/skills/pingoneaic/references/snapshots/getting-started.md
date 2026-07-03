---
title: About the getting started guide
description: Understand the purpose, goals, prerequisites, and structure of the Advanced Identity Cloud getting started guide
component: pingoneaic
page_id: pingoneaic:getting-started:getting-started-about
canonical_url: https://docs.pingidentity.com/pingoneaic/getting-started/getting-started-about.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Getting started"]
section_ids:
  gs-about-goals: Goals
  gs-about-before-begin: Before you begin
---

# About the getting started guide

This guide is for new Advanced Identity Cloud tenant administrators. It provides a step-by-step path to build a working solution and get up and running.

To get started, it's best to begin with the basics and add more complex workflows and customizations later. The guide provides best practices and next steps so you can explore further after you've mastered the basics.

|   |                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------- |
|   | Before you begin, familiarize yourself with the [Key concepts](getting-started-concepts.html) in Advanced Identity Cloud. |

## Goals

By following this guide, you'll achieve the following goals:

* Register your tenant and invite other tenant administrators

* Explore the Advanced Identity Cloud platform

* Create end users to represent your customers or employees

* Configure and test basic end-user experiences, including:

  * Registration

  * Authentication

  * Account recovery

  * Profile management

* Apply basic branding (logo, colors) to your end-user pages

* Learn how to integrate an OpenID Connect (OIDC) application for single sign-on (SSO).

## Before you begin

Before getting started, make sure you meet the following prerequisites.

* **Knowledge requirements**:

  * A basic understanding of identity and access management (IAM) concepts. Learn more in [Identity Fundamentals](https://www.pingidentity.com/en/resources/identity-fundamentals.html).

  * A basic understanding of what Advanced Identity Cloud is. Learn more in [PingOne Advanced Identity Cloud](https://www.pingidentity.com/en/platform/pingone-advanced-identity-cloud.html).

* **System requirements**: A working Advanced Identity Cloud tenant with super administrator or tenant administrator access.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Advanced Identity Cloud has four administrator roles:* **Tenant administrator**: Can manage most tenant and realm settings, but can't manage other administrators.

* **Super administrator**: Has full administrative access, including the ability to manage other administrators. The initial account for a new tenant has this role.

* **Tenant auditor**: Has read-only access to all tenant settings and data.

* **Brand administrator**: Has permissions to only manage hosted pages settings.Learn more in [Tenant administrator groups](../tenants/tenant-administrator-settings.html#tenant-administrator-groups). |
