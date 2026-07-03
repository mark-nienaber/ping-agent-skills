---
title: PingGateway and PingOne
description: Use PingGateway with PingOne for SSO and API security, including environment setup and test user configuration
component: pinggateway
version: 2026
page_id: pinggateway:pingone:preface
canonical_url: https://docs.pingidentity.com/pinggateway/2026/pingone/preface.html
revdate: 2025-04-01T17:53:34Z
keywords: ["Single sign-on (SSO)", "Security", "Authenticate"]
page_aliases: ["index.adoc"]
section_ids:
  before_you_start: Before you start
  ping-create-env: Create a PingOne environment
  ping-add-user: Add a PingOne test user
---

# PingGateway and PingOne

These pages show you how to use PingGateway with PingOne for SSO and API security. The examples target PingOne evaluators, administrators, and architects.

## Before you start

Unless otherwise stated, the examples in these pages assume you have:

* PingGateway [installed](../installation-guide/preface.html).

* The sample application [installed](../getting-started/start-sampleapp.html).

* A PingOne environment as described in [Create a PingOne environment](#ping-create-env).

* A PingOne test user as described in [Add a PingOne test user](#ping-add-user).

## Create a PingOne environment

In the PingOne console, create an environment with the following values:

* Select a solution for your Environment: Build your own solution

* Select solution(s) for your Environment: `PingOne SSO`

* ENVIRONMENT NAME: `My environment`

* DESCRIPTION: OIDC `My environment`

* ENVIRONMENT TYPE: `Sandbox`

Learn more in the PingOne documentation on [Adding an environment](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started_adding_environment.html).

## Add a PingOne test user

1. In the PingOne environment under Directory > Users, add a user.

   To match a user known to the sample application, use the following values:

   * Given Name: `Wilhelm`

   * Family Name: `Wolkig`

   * Username: `wolkig`

   * Email: `wolkig@example.com`

   * Password: Click Generate Password and record the generated password.

   Learn more in the PingOne documentation on [Adding a user](https://docs.pingidentity.com/pingone/directory/p1_adduser.html).

2. Under Settings > Environment Properties > URLs, copy the Self-Service Url for your environment.

3. In your browser's privacy or incognito mode, go to the URL you copied and sign on as the user you created.

4. When prompted, change the password so you won't have to change it again when trying an example.

   To match the credentials to those known to the sample application, set the new password to `Geh3imnis!`.
