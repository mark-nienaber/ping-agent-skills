---
title: Before you begin
description: Review prerequisites, compatibility requirements, and server configuration for PingOne Advanced Identity Cloud and PingAM before starting the Android journeys tutorial
component: orchsdks
page_id: orchsdks:journey:try-it-out/android/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/journey/try-it-out/android/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Mon, 3 Jul 2023 18:00:37 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Tutorial", "SDK"]
section_ids:
  compatibility: Compatibility
  prerequisites: Prerequisites
  server_configuration: Server configuration
  aic-android-qs: PingOne Advanced Identity Cloud
  am-android-qs: PingAM
---

# Before you begin

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: android, set=fab]Android

* **Prepare**

* [Download](01_download_samples.html)

* [Configure](02_configure_sample_for_journeys.html)

* [Run](03_run_the_sample.html)

To successfully complete this tutorial refer to the prerequisites and compatibility requirements in this section.

The tutorial also requires a configured server.

## Compatibility

* Android

  This sample requires at least Android 10 - API level 29.

  For more information, refer to [Supported operating systems and browsers](../../compatibility.html#supported-os).

* Java

  This sample requires at least Java 8 (v1.8).

## Prerequisites

* Android Studio

  Download and install [Android Studio](https://developer.android.com/studio), which is available for many popular operating systems.

* An Android emulator or physical device

  To try the quick start application as you develop it, you need an Android device. To add a virtual, emulated Android device to Android Studio, refer to [Create and manage virtual devices](https://developer.android.com/studio/run/managing-avds), on the **Android Developers** website.

## Server configuration

This tutorial requires you to configure one of the following servers:

|                                                                                                                                             |                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| [![PingOneAICStacked](../../../_images/logos/PingOneAICStacked.png)](#aic-android-qs)[**PingOne Advanced Identity Cloud**](#aic-android-qs) | [![PingAM](../../../_images/logos/PingAM.png)](#am-android-qs)**[PingAM](#am-android-qs)** |

### PingOne Advanced Identity Cloud

> **Collapse: Task 1. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. In the left panel, click Identities > Manage.
>
> 3. Click [icon: plus, set=fa]New Alpha realm - User.
>
> 4. Enter the following details:
>
>    * **Username** = `demo`
>
>    * **First Name** = `Demo`
>
>    * **Last Name** = `User`
>
>    * **Email Address** = `demo.user@example.com`
>
>    * **Password** = `Ch4ng3it!`
>
> 5. Click Save.

> **Collapse: Task 2. Create an authentication journey**
>
> Authentication journeys provide fine-grained authentication by allowing multiple paths and decision points throughout the flow. Authentication journeys are made up of nodes that define actions taken during authentication.
>
> Each node performs a single task, such as collecting a username or making a simple decision. Nodes can have multiple outcomes rather than just success or failure.
>
> You'll need an authentication journey configured on your server to try out the **Journey** module. That journey must only use [nodes, and therefore callbacks, that the Orchestration SDKs supports](../../compatibility.html#supported-authentication-journey-callbacks).
>
> |   |                                                                                                                |
> | - | -------------------------------------------------------------------------------------------------------------- |
> |   | You can use the default **Login** journey that both Advanced Identity Cloud and PingAM include out-of-the-box. |
>
> To create your own authentication journey for use when testing the Orchestration SDKs, follow these steps:
>
> 1. In your PingOne Advanced Identity Cloud tenant, navigate to Journeys, and click [icon: plus, set=fa]New Journey.
>
> 2. Enter a name, such as `sdkUsernamePasswordJourney` and click Save.
>
>    The authentication journey designer appears.
>
> 3. Drag the following nodes into the designer area:
>
>    * **Page Node**
>
>    * **Platform Username**
>
>    * **Platform Password**
>
>    * **Data Store Decision**
>
> 4. Drag and drop the **Platform Username** and **Platform Password** nodes onto the **Page Node**, so that they both appear on the same page when logging in.
>
> 5. Connect the nodes as follows:
>
>    ![sdk username password journey idcloud en](../../../_images/sdk-username-password-journey-idcloud-en.png)Figure 1. Example username and password authentication journey
>
> 6. Click Save.

> **Collapse: Task 3. Register a public OAuth 2.0 client**
>
> Public clients do not use a client secret to obtain tokens because they are unable to keep them hidden. The Orchestration SDKs commonly use this type of client to obtain tokens, as they cannot guarantee safekeeping of the client credentials in a browser or on a mobile device.
>
> To register a *public* OAuth 2.0 client application for use with the SDKs in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. In the left panel, click Applications.
>
> 3. Click [icon: plus, set=fa]Custom Application.
>
> 4. Select OIDC - OpenId Connect as the sign-in method, and then click Next.
>
> 5. Select Native / SPA as the application type, and then click Next.
>
> 6. In Name, enter a name for the application, such as `Public SDK Client`.
>
> 7. In Owners, select a user that is responsible for maintaining the application, and then click Next.
>
>    |   |                                                                                    |
>    | - | ---------------------------------------------------------------------------------- |
>    |   | When trying out the SDKs, you could select the `demo` user you created previously. |
>
> 8. In Client ID, enter `sdkPublicClient`
>
> 9. Select **Configure for SDK Sample Apps**.
>
> 10. Click Create Application.
>
>     PingOne Advanced Identity Cloud creates the application and displays the details screen.
>
> 11. On the Sign On tab:
>
>     1. In Sign-In URLs, ensure the following values appear, or add them if they don't:
>
>        `com.example.demo://oauth2redirect`
>
>        |   |                                                             |
>        | - | ----------------------------------------------------------- |
>        |   | Also add any other domains where you host SDK applications. |
>
>     2. In Grant Types, ensure the following values appear:
>
>        `Authorization Code`
>
>        `Refresh Token`
>
>     3. In Scopes, ensure the following values appear:
>
>        `openid profile email address`
>
> 12. Click Show advanced settings, and on the Authentication tab, confirm the following properties:
>
>     1. In Token Endpoint Authentication Method, select `none`.
>
>     2. In Client Type, select `Public`.
>
>     3. Enable the Implied Consent property.
>
> 13. Click Save.
>
> The application is now configured to accept client connections from and issue OAuth 2.0 tokens to the example applications and tutorials covered by this documentation.

> **Collapse: Task 4. Configure the OAuth 2.0 provider service**
>
> The provider specifies the supported OAuth 2.0 configuration options for a realm.
>
> To ensure the PingOne Advanced Identity Cloud OAuth 2.0 provider service is configured for use with the Orchestration SDKs, follow these steps:
>
> 1. In your PingOne Advanced Identity Cloud tenant, navigate to Native Consoles > Access Management.
>
> 2. In the left panel, click [icon: plug, set=fa]Services.
>
> 3. In the list of services, click OAuth2 Provider.
>
> 4. On the Core tab, ensure Issue Refresh Tokens is enabled.
>
> 5. On the Consent tab, ensure Allow Clients to Skip Consent is enabled.
>
> 6. Click Save Changes.

### PingAM

> **Collapse: Task 1. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingAM, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to [icon: address-card, set=fa]Identities, and then click [icon: plus, set=fa]Add Identity.
>
> 3. Enter the following details:
>
>    * **User ID** = `demo`
>
>    * **Password** = `Ch4ng3it!`
>
>    * **Email Address** = `demo.user@example.com`
>
> 4. Click Create.

> **Collapse: Task 2. Create an authentication tree**
>
> Authentication trees provide fine-grained authentication by allowing multiple paths and decision points throughout the authentication flow. Authentication trees are made up of nodes that define actions taken during authentication.
>
> Each node performs a single task, such as collecting a username or making a simple decision. Nodes can have multiple outcomes rather than just success or failure.
>
> To create a simple tree for use when testing the Orchestration SDKs, follow these steps:
>
> 1. Under Realm Overview, click Authentication Trees, then click Create Tree.
>
> 2. Enter a tree name, for example `sdkUsernamePasswordJourney`, and then click Create.
>
>    The authentication tree designer appears, showing the Start entry point connected to the Failure exit point.
>
> 3. Drag the following nodes from the Components panel on the left side into the designer area:
>
>    * **Page Node**
>
>    * **Username Collector**
>
>    * **Password Collector**
>
>    * **Data Store Decision**
>
> 4. Drag and drop the **Username Collector** and **Password Collector** nodes onto the **Page Node**, so that they both appear on the same page when logging in.
>
> 5. Connect the nodes as follows:
>
>    ![trees node login example](../../../_images/trees-node-login-example.png)Figure 2. Example username and password authentication tree
>
> 6. Select the **Page Node**, and in the Properties pane, set the Stage property to `UsernamePassword`.
>
>    |   |                                                                                                            |
>    | - | ---------------------------------------------------------------------------------------------------------- |
>    |   | You can configure the node properties by selecting a node and altering properties in the right-hand panel. |
>
>    One of the samples uses this specific value to determine the custom UI to display.
>
> 7. Click **Save**.

> **Collapse: Task 3. Register a public OAuth 2.0 client**
>
> Public clients do not use a client secret to obtain tokens because they are unable to keep them hidden. The Orchestration SDKs commonly use this type of client to obtain tokens, as they cannot guarantee safekeeping of the client credentials in a browser or on a mobile device.
>
> To register a *public* OAuth 2.0 client application for use with the SDKs in AM, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to [icon: list-alt, set=fa]Applications > OAuth 2.0 > Clients, and then click [icon: plus, set=fa]Add Client.
>
> 3. In Client ID, enter `sdkPublicClient`.
>
> 4. Leave Client secret empty.
>
> 5. In Redirection URIs, enter the following values:
>
>    `com.example.demo://oauth2redirect`
>
>    |   |                                                                        |
>    | - | ---------------------------------------------------------------------- |
>    |   | Also add any other domains where you will be hosting SDK applications. |
>
> 6. In Scopes, enter the following values:
>
>    `openid profile email address`
>
> 7. Click Create.
>
>    PingAM creates the new OAuth 2.0 client, and displays the properties for further configuration.
>
> 8. On the Core tab:
>
>    1. In Client type, select `Public`.
>
>    2. Disable Allow wildcard ports in redirect URIs.
>
>    3. Click Save Changes.
>
> 9. On the Advanced tab:
>
>    1. In Grant Types, enter the following values:
>
>       ```none
>       Authorization Code
>       Refresh Token
>       ```
>
>    2. In Token Endpoint Authentication Method, select `None`.
>
>    3. Enable the Implied consent property.
>
> 10. Click Save Changes.

> **Collapse: Task 4. Configure the OAuth 2.0 provider service**
>
> The provider specifies the supported OAuth 2.0 configuration options for a realm.
>
> To ensure the PingAM OAuth 2.0 provider service is configured for use with the Orchestration SDKs, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. In the left panel, click [icon: plug, set=fa]Services.
>
> 3. In the list of services, click OAuth2 Provider.
>
> 4. On the Core tab, ensure Issue Refresh Tokens is enabled.
>
> 5. On the Consent tab, ensure Allow Clients to Skip Consent is enabled.
>
> 6. Click Save Changes.
