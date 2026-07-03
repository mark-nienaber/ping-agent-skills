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

---

---
title: Before you begin
description: Review prerequisites, compatibility requirements, and configure PingOne Advanced Identity Cloud or PingAM before starting the iOS journeys tutorial
component: orchsdks
page_id: orchsdks:journey:try-it-out/ios/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/journey/try-it-out/ios/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Mon, 3 Jul 2023 18:00:37 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Tutorial", "SDK"]
section_ids:
  compatibility: Compatibility
  prerequisites: Prerequisites
  server_configuration: Server configuration
  aic-ios: PingOne Advanced Identity Cloud
  am-ios: PingAM
---

# Before you begin

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: apple, set=fab]iOS

* **Prepare**

* [Download](01_download_samples.html)

* [Configure](02_configure_sample_for_journeys.html)

* [Run](03_run_the_sample.html)

To successfully complete this tutorial refer to the prerequisites and compatibility requirements in this section.

The tutorial also requires a configured server.

## Compatibility

* iOS

  This sample app is compatible with iOS 16 and later.

## Prerequisites

* Xcode

  You can download the latest version for free from <https://developer.apple.com/xcode/>.

## Server configuration

This tutorial requires you to configure one of the following servers:

|                                                                                                                           |                                                                          |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| [![PingOneAICStacked](../../../_images/logos/PingOneAICStacked.png)](#aic-ios)[**PingOne Advanced Identity Cloud**](#aic) | [![PingAM](../../../_images/logos/PingAM.png)](#am-ios)**[PingAM](#am)** |

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

---

---
title: Before you begin
description: Complete prerequisites and configure PingOne Advanced Identity Cloud or PingAM before starting the JavaScript SDK journey tutorial
component: orchsdks
page_id: orchsdks:journey:try-it-out/javascript/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/journey/try-it-out/javascript/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Mon, 3 Jul 2023 18:00:37 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Tutorial", "SDK"]
section_ids:
  prerequisites: Prerequisites
  server_configuration: Server configuration
  aic-reactjs: PingOne Advanced Identity Cloud
  am-reactjs: PingAM
---

# Before you begin

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: js, set=fab]JavaScript

* **Prepare**

* [Download](01_download_samples.html)

* [Configure](02_configure_samples_for_journeys.html)

* [Run](03_run_the_samples.html)

To successfully complete this tutorial refer to the prerequisites in this section.

The tutorial also requires a configured server.

## Prerequisites

* Node and NPM

  The SDK requires a minimum Node.js version of `18`, and is tested on versions `18` and `20`. To get a supported version of Node.js, refer to the [Node.js download page](https://nodejs.org/en/download/).

  You will also need `npm` version 7 or newer to build the code and run the samples.

## Server configuration

This tutorial requires you to configure one of the following servers:

|                                                                                                                                      |                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| [![PingOneAICStacked](../../../_images/logos/PingOneAICStacked.png)](#aic-reactjs)[**PingOne Advanced Identity Cloud**](#aic-reactj) | [![PingAM](../../../_images/logos/PingAM.png)](#am-reactjs)**[PingAM](#am-reactjs)** |

### PingOne Advanced Identity Cloud

> **Collapse: Task 1. Configure CORS**
>
> [Cross-origin resource sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS) lets user agents make cross-domain server requests. In PingOne Advanced Identity Cloud, you can configure CORS to allow browsers from trusted domains to access PingOne Advanced Identity Cloud protected resources. For example, you might want a custom web application running on your own domain to get an end-user's profile information using the PingOne Advanced Identity Cloud REST API.
>
> The Orchestration SDK for JavaScript samples and tutorials use `https://localhost:8443` as the host domain, which you should add to your CORS configuration.
>
> If you are using a different domain for hosting SDK applications, ensure you add them to the CORS configuration as accepted origin domains.
>
> To update the CORS configuration in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. At the top right of the screen, click your name, and then select Tenant settings.
>
> 3. On the Global Settings tab, click Cross-Origin Resource Sharing (CORS).
>
> 4. Perform one of the following actions:
>
>    * If listed, click PingSDK.
>
>    * If there isn't an existing CORS configuration listed, click [icon: plus, set=fa]Add a CORS Configuration, select Ping SDK, and then click Next.
>
>      The **Ping SDK** template contains many of the default values used in these tutorials.
>
> 5. In Accepted Origins:
>
>    1. Ensure `https://localhost:8443` is listed.
>
>    2. Add any DNS aliases you use to host your Orchestration SDK for JavaScript applications.
>
> 6. Complete the remaining fields to suit your environment.
>
>    This documentation assumes the following configuration, required for the tutorials and sample applications:
>
>    | Property            | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
>    | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
>    | `Accepted Origins`  | `https://localhost:8443``http://localhost:9443`                                                                                                                                                                                                                                                                                                                                                                                                        |
>    | `Accepted Methods`  | `GET``POST`                                                                                                                                                                                                                                                                                                                                                                                                                                            |
>    | `Accepted Headers`  | `accept-api-version``x-requested-with``content-type``authorization``if-match``x-requested-platform``iPlanetDirectoryPro` \[[1](#_footnotedef_1 "View footnote.")]`ch15fefc5407912` \[[2](#_footnotedef_2 "View footnote.")]***[1](#_footnoteref_1). Cookie name value in PingAM servers.[2](#_footnoteref_2). In PingOne Advanced Identity Cloud tenants, go to **Tenant Settings > Global Settings > Cookie** to find this dynamic cookie name value. |
>    | `Exposed Headers`   | `authorization``content-type`                                                                                                                                                                                                                                                                                                                                                                                                                          |
>    | `Enable Caching`    | `True`                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
>    | `Max Age`           | `600`                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
>    | `Allow Credentials` | `True`                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
>
>    |   |                                                                       |
>    | - | --------------------------------------------------------------------- |
>    |   | Click Show advanced settings to be able to edit all available fields. |
>
> 7. Click Save CORS Configuration.

> **Collapse: Task 2. Create a demo user**
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

> **Collapse: Task 3. Create an authentication journey**
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

> **Collapse: Task 4. Register a public OAuth 2.0 client**
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
>        `https://localhost:8443/callback.html`
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

> **Collapse: Task 5. Register a confidential OAuth 2.0 client**
>
> Confidential clients are able to securely store credentials and are commonly used for server-to-server communication. For example, the "Todo" API backend provided with the SDK samples uses a confidential client to obtain tokens.
>
> To register a *confidential* OAuth 2.0 client application for use with the SDKs in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. In the left panel, click Applications.
>
> 3. Click [icon: plus, set=fa]Custom Application.
>
> 4. Select OIDC - OpenId Connect as the sign-in method, and then click Next.
>
> 5. Select Web as the application type, and then click Next.
>
> 6. In Name, enter a name for the application, such as `Confidential SDK Client`.
>
> 7. In Owners, select a user responsible for maintaining the application, and then click Next.
>
>    |   |                                                                                    |
>    | - | ---------------------------------------------------------------------------------- |
>    |   | When trying out the SDKs, you could select the `demo` user you created previously. |
>
> 8. On the Web Settings page:
>
>    1. In Client ID, enter `sdkConfidentialClient`
>
>    2. In Client Secret, enter a strong password and make a note of it for later use.
>
>       For example, `5tr0ngP@S5w0rd!`
>
>       |   |                                                                                                                                               |
>       | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
>       |   | The client secret is not available to view after this step.If you forget it, you must reset the secret and reconfigure any connected clients. |
>
>    3. Click Create Application.
>
>       PingOne Advanced Identity Cloud creates the application and displays the details screen.
>
> 9. On the Sign On tab, click Show advanced settings, and on the Access tab:
>
>    1. In Default Scopes, enter `am-introspect-all-tokens`.
>
> 10. Click Save.

> **Collapse: Task 6. Configure the OAuth 2.0 provider service**
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

> **Collapse: Task 1. Configure CORS**
>
> [Cross-origin resource sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS) lets user agents make cross-domain server requests. In PingAM, you can configure CORS to allow browsers from trusted domains to access PingAM protected resources. For example, you might want a custom web application running on your own domain to get an end-user's profile information using the PingAM REST API.
>
> The Orchestration SDK for JavaScript samples and tutorials all use `https://localhost:8443` as the host domain, which you should add to your CORS configuration.
>
> If you are using a different URL for hosting SDK applications, ensure you add them to the CORS configuration as accepted origin domains.
>
> To enable CORS in PingAM, and create a CORS filter to allow requests from your configured domain names, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to Configure > Global Services > CORS Service > Configuration, and set the Enable the CORS filter property to `true`.
>
>    |   |                                                                                                                      |
>    | - | -------------------------------------------------------------------------------------------------------------------- |
>    |   | If this property is not enabled, CORS headers are not added to responses from PingAM, and CORS is disabled entirely. |
>
> 3. On the Secondary Configurations tab, click Add a Secondary Configuration.
>
> 4. In the Name field, enter `OrchSDK`.
>
> 5. in the Accepted Origins field, enter any DNS aliases you use for your SDK apps.
>
>    This documentation assumes the following configuration:
>
>    | Property           | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
>    | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
>    | `Accepted Origins` | `https://localhost:8443``http://localhost:9443`                                                                                                                                                                                                                                                                                                                                                                                                        |
>    | `Accepted Methods` | `GET``POST`                                                                                                                                                                                                                                                                                                                                                                                                                                            |
>    | `Accepted Headers` | `accept-api-version``x-requested-with``content-type``authorization``if-match``x-requested-platform``iPlanetDirectoryPro` \[[3](#_footnotedef_3 "View footnote.")]`ch15fefc5407912` \[[4](#_footnotedef_4 "View footnote.")]***[3](#_footnoteref_3). Cookie name value in PingAM servers.[4](#_footnoteref_4). In PingOne Advanced Identity Cloud tenants, go to **Tenant Settings > Global Settings > Cookie** to find this dynamic cookie name value. |
>
> 6. Click Create.
>
>    PingAM displays the configuration of your new CORS filter.
>
> 7. On the CORS filter configuration page:
>
>    1. Ensure Enable the CORS filter is enabled.
>
>    2. Set the Max Age property to `600`
>
>    3. Ensure Allow Credentials is enabled.
>
> 8. Click Save Changes.

> **Collapse: Task 2. Create a demo user**
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

> **Collapse: Task 3. Create an authentication tree**
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

> **Collapse: Task 4. Register a public OAuth 2.0 client**
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
>    `https://localhost:8443/callback.html`
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

> **Collapse: Task 5. Register a confidential OAuth 2.0 client**
>
> Confidential clients are able to store credentials securely and are commonly used for server-to-server communication.
>
> To register a *confidential* OAuth 2.0 client application for use with the SDKs in AM, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to [icon: list-alt, set=fa]Applications > OAuth 2.0 > Clients, and then click [icon: plus, set=fa]Add Client.
>
> 3. In Client ID, enter `sdkConfidentialClient`.
>
> 4. In Client Secret, enter a strong password and make a note of it for later use.
>
>    For example, `5tr0ngP@S5w0rd!`
>
>    |   |                                                                                                                                               |
>    | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
>    |   | The client secret is not available to view after this step.If you forget it, you must reset the secret and reconfigure any connected clients. |
>
> 5. In Default Scopes, enter `am-introspect-all-tokens`.
>
>    PingAM creates the new OAuth 2.0 client and displays the properties for further configuration.
>
> 6. On the Advanced tab:
>
>    1. Enable the Implied consent property.
>
> 7. Click Save Changes.

> **Collapse: Task 6. Configure the OAuth 2.0 provider service**
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

---

---
title: Before you begin
description: Prerequisites, compatibility requirements, and server configuration steps needed before starting the React Native tutorial.
component: orchsdks
page_id: orchsdks:journey:try-it-out/react-native/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/journey/try-it-out/react-native/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Tutorial", "SDK", "React Native"]
section_ids:
  compatibility: Compatibility
  prerequisites: Prerequisites
  server_configuration: Server configuration
  aic-rn: PingOne Advanced Identity Cloud
  am-rn: PingAM
---

# Before you begin

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: react, set=fab]React Native

* **Prepare**

* [Download](01_download_samples.html)

* [Install](02_prepare-projects.html)

* [Configure](03_configure_sample.html)

* [Run](04_run_the_sample.html)

To successfully complete this tutorial refer to the prerequisites and compatibility requirements in this section.

The tutorial also requires a configured server.

## Compatibility

* React Native

  This sample app requires React Native 0.80.1 or later.

* iOS

  This sample app requires iOS 16.0 or later.

* Android

  This sample app requires Android 10 (API level 29) or later.

## Prerequisites

The React Native development environment must be fully configured before you begin. Follow the official [React Native environment setup guide](https://reactnative.dev/docs/set-up-your-environment) and ensure the following tools are installed:

* Node.js and Yarn

  Install [Node.js](https://nodejs.org/) version 20 or later.

  This project uses Yarn 4 workspaces. Install Yarn by running:

  ```shell
  corepack enable
  ```

* Xcode (iOS only)

  Download and install [Xcode](https://developer.apple.com/xcode/) from the Mac App Store.

  Xcode 15 or later is recommended.

* Ruby and Bundler (iOS only)

  Ruby is required to manage CocoaPods. Install [Bundler](https://bundler.io/) with:

  ```shell
  gem install bundler
  ```

* CocoaPods (iOS only)

  CocoaPods is installed locally during the tutorial. You do not need to install it globally.

* Android Studio (Android only)

  Download and install [Android Studio](https://developer.android.com/studio).

  An Android emulator or physical device is required to run the app. To add a virtual device, refer to [Create and manage virtual devices](https://developer.android.com/studio/run/managing-avds) on the Android Developers website.

* Java (Android only)

  Android Studio includes an embedded JDK. Java 17 is recommended and is bundled with recent versions of Android Studio.

* `keytool` (Android only)

  `keytool` is part of the Java Development Kit (JDK) and is used to generate the debug signing keystore required for the Android build. It is included with Android Studio's bundled JDK.

## Server configuration

This tutorial requires you to configure one of the following servers:

|                                                                                                                             |                                                                            |
| --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| [![PingOneAICStacked](../../../_images/logos/PingOneAICStacked.png)](#aic-rn)[**PingOne Advanced Identity Cloud**](#aic-rn) | [![PingAM](../../../_images/logos/PingAM.png)](#am-rn)**[PingAM](#am-rn)** |

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
>        `org.forgerock.demo://oauth2redirect`
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
>    `org.forgerock.demo://oauth2redirect`
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

---

---
title: Before you begin
description: Configure an OATH-based MFA authentication journey in PingOne Advanced Identity Cloud or PingAM before integrating OATH into your Android or iOS app
component: orchsdks
page_id: orchsdks:journey:use-cases/oath/before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/journey/use-cases/oath/before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Before you begin

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: android, set=fab]Android [icon: apple, set=fab]iOS

To integrate OATH-based MFA into your apps you must first configure an authentication journey in your server.

The journey registers the client to the user's profile if they have not done so already, then requests a one-time password from the device.

Follow the instructions to create the required authentication journey in your server:

* Advanced Identity Cloud

* Self-managed PingAM server

1. In the Advanced Identity Cloud admin UI

   1. Select the realm that will contain the authentication journey.

   2. Select Journeys, and click [icon: plus, set=fa]New Journey.

   3. Enter a name for your tree in Name page; for example, `MFAwithOATH`

   4. In Identity Object, select the identity type that will be authenticating, for example `group Alpha realm - Users`.

   5. Click Save.

      The authentication journey designer page is displayed with the default Start, Failure, and Success nodes.

2. Add the following nodes to the designer area:

   * [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html)

   * [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)

   * [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)

   * [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html)

   * [OATH Token Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/oath-token-verifier.html)

   * [OATH Registration node](https://docs.pingidentity.com/auth-node-ref/latest/oath-registration.html) or [Combined MFA Registration node](https://docs.pingidentity.com/auth-node-ref/latest/combined-mfa-registration.html) \[[1](#_footnotedef_1 "View footnote.")]

3. Connect the nodes as shown:

   ![Connect the nodes to identify the user, then verify their OATH token.](../../_images/mfa/idcloud/tree-idcloud-mfa-with-oath-en.png)Figure 1. Connect the nodes to identify the user, then verify their OATH token.

4. Ensure that the [OATH Token Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/oath-token-verifier.html) and the [OATH Registration node](https://docs.pingidentity.com/auth-node-ref/latest/oath-registration.html) or [Combined MFA Registration node](https://docs.pingidentity.com/auth-node-ref/latest/combined-mfa-registration.html) are using the same value for OATH Algorithm.

   For example, select `TOTP`.

5. Save your changes.

1) In the AM admin UI:

   1. Select the realm that will contain the authentication tree.

   2. Select Authentication > Trees, and click [icon: plus, set=fa]Create Tree.

   3. Enter a name for your tree in the New Tree page; for example, `MFAwithOATH`, and click Create.

      The authentication tree designer page is displayed with the default Start, Failure, and Success nodes.

2) Add the following nodes to the designer area:

   * [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html)

   * [Password Collector node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/password-collector.html)

   * [Username Collector node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/username-collector.html)

   * [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html)

   * [OATH Token Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/oath-token-verifier.html)

   * [OATH Registration node](https://docs.pingidentity.com/auth-node-ref/latest/oath-registration.html) or [Combined MFA Registration node](https://docs.pingidentity.com/auth-node-ref/latest/combined-mfa-registration.html) \[[1](#_footnotedef_1 "View footnote.")]

3) Connect the nodes as shown:

   ![Connect the nodes to identify the user, then verify their OATH token.](../../_images/mfa/onprem/tree-onprem-mfa-with-oath-en.png)Figure 2. Connect the nodes to identify the user, then verify their OATH token.

4) Ensure that the [OATH Token Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/oath-token-verifier.html) and the [OATH Registration node](https://docs.pingidentity.com/auth-node-ref/latest/oath-registration.html) or [Combined MFA Registration node](https://docs.pingidentity.com/auth-node-ref/latest/combined-mfa-registration.html) are using the same value for OATH Algorithm.

   For example, select `TOTP`.

5) Save your changes.

The tree you create is a simple example for the purposes of demonstrating a basic OATH authentication journey. In a production environment, you could include additional nodes, such as:

* [Get Authenticator App node](https://docs.pingidentity.com/auth-node-ref/latest/get-authenticator-app.html)

  Provides links to download the ForgeRock Authenticator for Android and iOS.

* [MFA Registration Options node](https://docs.pingidentity.com/auth-node-ref/latest/mfa-registration-options.html)

  Provides options for users to register a multi-factor authentication device, get the authenticator app, or skip the registration process.

* [Opt-out Multi-Factor Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/opt-out-multi-factor.html)

  Sets an attribute in the user's profile which lets them skip multi-factor authentication.

* [Recovery Code Display node](https://docs.pingidentity.com/auth-node-ref/latest/recovery-code-display.html)

  Lets a user view recovery codes to use in case they lose or damage the authenticator device they register.

* [Recovery Code Collector Decision node](https://docs.pingidentity.com/auth-node-ref/latest/recovery-code-collector-decision.html)

  Lets a user enter their recovery codes to authenticate in case they have lost or damaged their registered authenticator device.

* [Retry Limit Decision node](https://docs.pingidentity.com/auth-node-ref/latest/retry-limit-decision.html)

  Lets a journey loop a specified number of times, for example, to allow a user to retry entering their OATH token.

***

[1](#_footnoteref_1). Use the combined MFA registration node if you intend to add Push notifications as an MFA method.

---

---
title: Binding keys to a device in Android
description: Use the Android Device Binding module to bind cryptographic keys to a device and verify key possession using biometrics or a PIN
component: orchsdks
page_id: orchsdks:journey:use-cases/device-binding/android-device-binding
canonical_url: https://developer.pingidentity.com/orchsdks/journey/use-cases/device-binding/android-device-binding.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 29 Oct 2025 14:22:33 +0100
keywords: ["Device", "Hardware", "Source Code", "Integration", "SDK", "Android"]
section_ids:
  before_you_begin: Before you begin
  securing_access_to_the_keys: Securing access to the keys
  android_device-profile_modules: Installing modules
  binding_keys_to_a_device: Binding keys to a device
  customizing_binding_parameters: Customizing binding parameters
  verifying_bound_keys_on_a_device: Verifying bound keys on a device
  customizing_signing_parameters: Customizing signing parameters
  adding_custom_claims_when_signing_using_bound_keys: Adding custom claims when signing using bound keys
  handling_errors: Handling errors
  new-biometrics: Handling biometric enrollment invalidations
  key-removal: Handling key removal by the device
---

# Binding keys to a device in Android

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: android, set=fab]Android

The Device Binding module provides secure device registration and authentication capabilities for Android applications.

It enables applications to bind cryptographic keys to a device and restrict access to those keys, using biometrics, a PIN, and other authentication methods.

## Before you begin

You need to create an authentication journey in your server using the appropriate nodes to enable device binding.

The nodes you can use for device binding Journeys include the follows:

* [Device Binding node](https://docs.pingidentity.com/auth-node-ref/latest/device-binding.html)

  Allows users to register one or more devices to their account. A user can bind multiple devices, and each device can be bound to multiple users.

  The client receives a `DeviceBindingCallback` when reaching this node in a journey.

* [Device Signing Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/device-signing-verifier.html)

  Verifies possession of a registered bound device.

  The node requires the client device to sign a challenge string using the private key that corresponds to the public key stored on the server during initial binding.

  The client receives a `DeviceSigningVerifierCallback` when reaching this node in a journey.

* [Device Binding Storage node](https://docs.pingidentity.com/auth-node-ref/latest/device-binding-storage.html)

  Optionally persists collected device binding data to a user's profile in the identity store.

  By default, the **Device Binding node** stores device data in the user's profile. You can choose instead to store the device data in transient state, perhaps to run a custom script to extract additional context.

  In this case, you can use a **Device Binding Storage node** to store the data in the user's profile.

  This node runs entirely server-side, and doesn't send a callback to the client.

## Securing access to the keys

The Device Binding module supports four distinct methods for accessing the private key, each offering different levels of security and user experience.

You specify which authentication type your client uses in the configuration of the **Device Binding node**. To change the authentication type to access the keys, you'll need to rebind the client device

Supported authentication types to access bound keys

* Biometric Only

* Biometric with Fallback

* Application PIN

* No Authentication

|                     |                                                                                                                                                                                                                                                                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type name           | `BIOMETRIC_ONLY`                                                                                                                                                                                                                                                                                                                  |
| Description         | Requires strict biometric authentication with no fallback options                                                                                                                                                                                                                                                                 |
| Security level      | **High**                                                                                                                                                                                                                                                                                                                          |
| User experience     | Streamlined for devices with reliable biometric sensors                                                                                                                                                                                                                                                                           |
| Behavior            | - Only accepts biometric authentication, such as a fingerprint, face recognition, or an iris scan

- Fails immediately if biometric authentication is unavailable or unsuccessful

- No option to fall back to device PIN, pattern, or password

- Ideal for high-security applications where biometric verification is mandatory |
| Use cases           | Financial applications, enterprise security, medical applications                                                                                                                                                                                                                                                                 |
| Device requirements | Must have functional biometric sensors and enrolled biometric data                                                                                                                                                                                                                                                                |

|                     |                                                                                                                                                                                                                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type name           | `BIOMETRIC_ALLOW_FALLBACK`                                                                                                                                                                                                                                                                                                                   |
| Description         | Prefers biometric authentication but allows fallback to device credentials                                                                                                                                                                                                                                                                   |
| Security level      | **Medium** to **High**                                                                                                                                                                                                                                                                                                                       |
| User experience     | Flexible with multiple authentication options                                                                                                                                                                                                                                                                                                |
| Behavior            | * The primary method is a biometric authentication, such as a fingerprint, face recognition, or an iris scan

* If biometric authentication fails or is unavailable, users can use device credentials

  * Device credentials include a PIN, a pattern, or a password set at the system level

* Provides better accessibility and usability |
| Use cases           | Consumer applications, general-purpose authentication, accessibility-focused apps                                                                                                                                                                                                                                                            |
| Device requirements | - Biometric sensors preferred, but not required

- Must configure the device lock screen                                                                                                                                                                                                                                                     |

|                     |                                                                                                                                                                                                                                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type name           | `APPLICATION_PIN`                                                                                                                                                                                                                                                                               |
| Description         | Requires a custom PIN that the application manages entirely                                                                                                                                                                                                                                     |
| Security level      | **Medium**                                                                                                                                                                                                                                                                                      |
| User experience     | Consistent across all devices regardless of hardware capabilities                                                                                                                                                                                                                               |
| Behavior            | * Uses an application-specific PIN separate from device credentials

  * The application collects the PIN through a custom UI

  * The application securely stores PIN data using encrypted storage mechanisms

  * Independent of device biometric capabilities or system-level authentication |
| Use cases           | - Devices without biometric capabilities

- Applications requiring custom authentication flows

- Scenarios where users prefer PIN over biometric authentication

  * Cross-platform consistency requirements                                                                                   |
| Device requirements | None - works on all devices                                                                                                                                                                                                                                                                     |

|                         |                                                                                                                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type name               | `NONE`                                                                                                                                                                                                              |
| Description             | No user authentication required to access cryptographic keys                                                                                                                                                        |
| Security Level          | **Low**                                                                                                                                                                                                             |
| User Experience         | Seamless with no authentication prompts                                                                                                                                                                             |
| Behavior                | * Users can access keys immediately without any verification

* No authentication prompts or delays

* Cryptographic operations proceed without user interaction

* Relies solely on device possession for security |
| Use cases               | - Applications with alternative security measures                                                                                                                                                                   |
| Security Considerations | Anyone with device access can use the cryptographic keys                                                                                                                                                            |
| Device Requirements     | None                                                                                                                                                                                                                |

## Installing modules

Use the following module in your Android apps to bind keys to a device:

* `binding`

You can optionally also install the following modules:

* `binding-ui`

* `binding-migration`

* `bcpkix-jdk18on` ([BouncyCastle](https://www.bouncycastle.org/) open-source cryptographic library)

To install these modules into your Android app:

1. In the **Project** tree view of your Android Studio project, open the `build.gradle.kts` file.

2. In the `dependencies` section, add the `binding` module as a dependency:

   ```gradle
   dependencies {
     implementation("com.pingidentity.sdk:binding:2.0.1")
   }
   ```

3. Optionally, you can include the **binding-ui** dependency, which includes default UI components for the following user interactions:

   * **Application PIN Collection**

     A Jetpack Compose dialog for secure PIN entry with:

     * Custom PIN input field with masked characters

     * Show/hide PIN visibility toggle

     * Cancel and confirm buttons

     * Error handling and validation feedback

   * **User Key Selection**

     A default UI for multi-user scenarios that displays:

     * List of available user keys with user information

     * Selection interface when multiple users have registered devices

     * User-friendly key identification (username, creation date, etc.)

   To use the default UI dependency, add it as follows:

   ```gradle
   dependencies {
     implementation("com.pingidentity.sdk:binding:2.0.1")
     implementation("com.pingidentity.sdk:binding-ui:2.0.1")
   }
   ```

4. Optionally, you can include the **binding-migration** dependency, which helps to migrate users with binding keys created by versions of the legacy ForgeRock SDK for Android.

   The **binding-migration** module runs the following steps in the background and requires no additional configuration or user intervention:

   * **Detects Legacy Keys**: Scans for existing ForgeRock SDK device binding keys and metadata

   * **Seamless Migration**: Automatically migrates keys to the new SDK format during application startup

   * **Preserves User Experience**: Users don't need to re-register their devices after SDK upgrade

   * **One-Time Process**: Migration occurs once and removes legacy data after successful migration

   * **Backward Compatibility**: Ensures smooth transition from Legacy SDK without data loss

   To use the binding migration dependency, add it as follows:

   ```gradle
   dependencies {
     implementation("com.pingidentity.sdk:binding:2.0.1")
     implementation("com.pingidentity.sdk:binding-ui:2.0.1")
     implementation("com.pingidentity.sdk:binding-migration:2.0.1")
   }
   ```

5. Optionally, if you intend to use the **Application PIN** authentication method to access the private keys, add the following [BouncyCastle](https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk18on) dependency:

   ```gradle
   dependencies {
     implementation("com.pingidentity.sdk:binding:2.0.1")
     implementation("com.pingidentity.sdk:binding-ui:2.0.1")
     implementation("com.pingidentity.sdk:binding-migration:2.0.1")
     implementation("org.bouncycastle:bcpkix-jdk18on:1.82"
   }
   ```

## Binding keys to a device

To bind keys to a device, the Binding Module performs the following tasks:

1. **Validation**: Checks device support for authentication type

2. **Cleanup**: Removes existing keys for the user

3. **Key generation**: Creates new cryptographic key pair

4. **Authentication**: Verifies user identity

5. **JWT Signing**: Creates signed proof-of-possession

6. **Storage**: Saves user key meta data

Use the `deviceBindingCallback.bind()` method to bind keys to the device as follows:

Binding keys to an Android device

```kotlin
import com.pingidentity.device.binding.journey.DeviceBindingCallback

// Simple device binding with default configuration
val result = deviceBindingCallback.bind()

result.onSuccess { jwt ->
  // Device successfully bound, JWT contains proof
  println("Device bound successfully: $jwt")
}.onFailure { error ->
  // Handle binding failure
  println("Binding failed: ${error.message}")
}
```

### Customizing binding parameters

You can configure a number of parameters for binding, such as the device identifier, algorithm used, and the validity time:

Configuring key binding parameters on an Android device

```kotlin
val result = deviceBindingCallback.bind {
  // Device identification
  deviceName = "Babs' Phone"
  deviceIdentifier = DefaultDeviceIdentifier.id // Use the default device identifier strategy

  // Cryptographic settings
  signingAlgorithm = "RS256"

  // Timing configuration
  issueTime = { Instant.now() }
  expirationTime = { timeout -> Instant.now().plusSeconds(timeout.toLong()) }

  // Storage configuration
  userKeyStorage {
    storage {
      fileName = "user_keys"
    }
  }

  // Authentication configuration
  biometricAuthenticatorConfig {
    promptInfo = {
      setTitle("Device Registration")
      setSubtitle("Secure your account")
      setDescription("Use your fingerprint to register this device")
    }
  }
}
```

Learn about customizing the device identifier in [Customizing device identifiers on Android](android-device-ids.html).

## Verifying bound keys on a device

To verify that a device possesses a bound key, the Binding Module performs the following tasks:

1. **Validation**: Validates custom claims

2. **Key Lookup**: Finds appropriate user key

3. **Authentication**: Verifies user identity

4. **Challenge signing**: Signs server challenge

5. **JWT creation**: Creates verification JWT

Use the `deviceSigningVerifierCallback.sign()` method to verify possession of bound keys as follows:

Verifying key possession by signing data on an Android device

```kotlin
import com.pingidentity.device.binding.journey.DeviceSigningVerifierCallback

// Simple device signing
val result = deviceSigningVerifierCallback.sign()

result.onSuccess { jwt ->
  // Challenge successfully signed
  println("Challenge signed: $jwt")
}.onFailure { error ->
  // Handle signing failure
  println("Signing failed: ${error.message}")
}
```

### Customizing signing parameters

You can configure a number of device signing parameters, such as the algorithm used, and the prompts to display:

Configuring signing parameters on an Android device

```kotlin
val result = deviceSigningVerifierCallback.sign {
  // Signing algorithm
  signingAlgorithm = "RS512"

  appPinConfig {
    pinRetry = 3
    pinCollector {
      "1234".toCharArray()
    }
    prompt = Prompt("App Pin", "Enter your app pin", "App pin is required")
  }

  // User key selection strategy
  userKeySelector { keys ->
    // Select most recently created key
    keys.maxByOrNull { it.createdAt } ?: keys.first()
  }

  // Authentication configuration
  biometricAuthenticatorConfig {
    promptInfo = {
      setTitle("Verify Transaction")
      setDescription("Confirm this transaction with your fingerprint")
    }
  }
}
```

### Adding custom claims when signing using bound keys

When signing a server-provided challenge to verify possession of a bound key, you can add custom data to the resulting JSON Web Token (JWT). The server can access and use this data for context, or for auditing purposes.

Add a `claims` attribute to the configuration, including the key-value pairs you want to add to the JWT:

Adding custom claims to the JWT on an Android device

```kotlin
deviceSigningVerifierCallback.sign {
  claims {
    // Transaction details
    put("amount", "100.00")
    put("recipient", "babs@example.com")
    put("currency", "USD")

    // Device context
    put("ip_address", getClientIP())
    put("user_agent", getUserAgent())

    // Security context
    put("risk_score", calculateRiskScore())
    put("session_id", getSessionId())
  }
}
```

## Handling errors

The Device Binding module can generate several error messages when you call `bind()` or `sign()`. Handle these errors to ensure the best possible user experience.

**Common error codes and how to remediate them**

| Error                                | Description                                                                                                                                                                | Remediation                                                                                                                               |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `DeviceNotSupportedException`        | The device lacks required capabilities, or the user hasn't enrolled.                                                                                                       | Retry with alternative authentication requirements that don't require biometrics.                                                         |
| `DeviceNotRegisteredException`       | No keys are available for signing. Either the device hasn't been registered, or the user has removed the authentication methods that protected the private key.            | Redirect the user to bind a new key to the device.Learn more in [Handling key removal by the device](#key-removal).                       |
| `TimeoutCancellationException`       | Operation exceeded timeout.                                                                                                                                                | Allow retry with a longer timeout.                                                                                                        |
| `InvalidClaimException`              | Reserved claim names used in custom claims parameter.You can't add custom claims that match the standard required claims in a JWT, such as `sub`, `exp`, `iat`, and `iss`. | Remove or rename the claims listed in the error so they do not clash.                                                                     |
| `AbortException`                     | The user aborted the operation.For example the user clicked **Cancel** rather than provide their fingerprint.                                                              | Handle gracefully, and don't show error.The user chose not to continue the authentication flow.                                           |
| `BiometricAuthenticationException`   | Biometric authentication failed.                                                                                                                                           | Retry biometric authentication, or offer an alternative authentication method that doesn't require biometrics.                            |
| `InvalidCredentialException`         | The user provided invalid credentials.For example, the user entered an incorrect PIN number.                                                                               | Allow retry and prompt for the correct credentials.                                                                                       |
| `CancellationException`              | Coroutine operation cancelled.                                                                                                                                             | Re-throw the exception to preserve cancellation semantics.                                                                                |
| `KeyPermanentlyInvalidatedException` | User binds keys to their device with `BiometricOnly` authentication and later enrolls a new fingerprint.                                                                   | User must perform device binding again to generate new keys.Learn more in [Handling biometric enrollment invalidations](#new-biometrics). |

The following example shows how to handle some of these exceptions:

Handling exceptions when binding keys to a device

```kotlin
deviceBindingCallback.bind().fold(
  onSuccess = { jwt ->
    // Handle success
    processBindingSuccess(jwt)
  },
  onFailure = { error ->
    when (error) {
      is DeviceNotSupportedException -> {
        logger.w("Device not supported: ${error.message}")
        showFallbackAuthentication()
      }
      is TimeoutCancellationException -> {
        logger.w("Binding operation timed out")
        retryWithLongerTimeout()
      }
      else -> {
        logger.e("Binding failed", error)
        showGenericError(error.message)
      }
    }
  }
)
```

### Handling biometric enrollment invalidations

Setting the `setInvalidatedByBiometricEnrollment` parameter to `true` when binding a new key to a device invalidates the key if the user enrolls a new fingerprint or changes the registered biometrics on the device. The Device Binding module returns `KeyPermanentlyInvalidatedException` in this case.

If the authentication method for signing is set to `BIOMETRIC_ONLY` the invalidated keys won't be available, so the user will need to bind a new key:

Handling `KeyPermanentlyInvalidatedException` exceptions

```kotlin
// Configuration that makes keys sensitive to biometric changes
biometricAuthenticatorConfig {
    keyGenParameterSpec {
        // This setting makes keys invalid when new biometrics are enrolled
        setInvalidatedByBiometricEnrollment(true)
        //setUnlockedDeviceRequired(true)
        //setUserAuthenticationValidWhileOnBody(true)
        //setUserPresenceRequired(true)
        //setIsStrongBoxBacked(false)
        //setInvalidatedByBiometricEnrollment(false)
    }
}

// When user enrolls new fingerprint, subsequent signing will fail
deviceSigningCallback.sign().onFailure { error ->
  when (error) {
    is KeyPermanentlyInvalidatedException -> {
      // Keys are permanently invalidated due to biometric enrollment
      logger.w("Device keys invalidated by biometric enrollment")
      redirectToDeviceBinding() // User must re-bind device
    }
  }
}
```

|   |                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Not all Android devices support the `keyGenParameterSpec` options for configuring how they create keys.You should test the devices you want to support if you enable them |

### Handling key removal by the device

If a user disables all of the available authentication methods on their device, such as removing their fingerprints and the device PIN, Android automatically removes any keys protected by those methods from the KeyStore.

The Device Binding module returns `DeviceNotRegisteredException` in this case, and the user will need to bind a new key to their device:

Handling `DeviceNotRegisteredException` exceptions

```kotlin
// When all device authentication is removed, keys are deleted by Android KeyStore
deviceSigningCallback.sign().onFailure { error ->
  when (error) {
    is DeviceNotRegisteredException -> {
      logger.w("No device keys found - maybe removed due to authentication method removal")
      showMessage("Please enroll in biometrics or add a device PIN, then register your device")
      redirectToDeviceBinding() // User must re-bind device
    }
  }
}
```

---

---
title: Binding keys to a device in iOS
description: Bind cryptographic keys to an iOS device and verify key possession using the PingOne Advanced Identity Cloud PingBinding module with biometric and PIN authentication
component: orchsdks
page_id: orchsdks:journey:use-cases/device-binding/ios-device-binding
canonical_url: https://developer.pingidentity.com/orchsdks/journey/use-cases/device-binding/ios-device-binding.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 29 Oct 2025 14:22:33 +0100
keywords: ["Device", "Hardware", "Source Code", "Integration", "SDK", "iOS"]
section_ids:
  before_you_begin: Before you begin
  securing_access_to_the_keys: Securing access to the keys
  ios_device-binding_module: Installing modules
  binding_keys_to_a_device: Binding keys to a device
  verifying_bound_keys_on_a_device: Verifying bound keys on a device
  adding_custom_claims_when_signing_using_bound_keys: Adding custom claims when signing using bound keys
  configuring_authenticator_parameters: Configuring authenticator parameters
  replacing_the_default_system_ui: Replacing the default system UI
  creating_a_custom_ui_for_pin_entry: Creating a custom UI for PIN entry
  pin_ui_view: Step 1. Create a Custom UI for PIN Collection
  pin_ui_protocol: Step 2. Implement the PinCollector Protocol
  pin_ui_configure: Step 3. Use the custom collector for binding and signing
  creating_a_custom_ui_for_key_selection: Creating a custom UI for key selection
  key_ui_view: Step 1. Create a custom UI for key selection
  key_ui_protocol: Step 2. Implement the UserKeySelector Protocol
  key_ui_configure: Step 3. Use the custom key selector for signing
  handling_errors: Handling errors
---

# Binding keys to a device in iOS

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: apple, set=fab]iOS

The Device Binding module provides secure device registration and authentication capabilities for iOS applications.

It enables applications to bind cryptographic keys to a device and restrict access to those keys, using biometrics, a PIN, and other authentication methods.

## Before you begin

You need to create an authentication journey in your server using the appropriate nodes to enable device binding.

The nodes you can use for device binding Journeys include the follows:

* [Device Binding node](https://docs.pingidentity.com/auth-node-ref/latest/device-binding.html)

  Allows users to register one or more devices to their account. A user can bind multiple devices, and each device can be bound to multiple users.

  The client receives a `DeviceBindingCallback` when reaching this node in a journey.

* [Device Signing Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/device-signing-verifier.html)

  Verifies possession of a registered bound device.

  The node requires the client device to sign a challenge string using the private key that corresponds to the public key stored on the server during initial binding.

  The client receives a `DeviceSigningVerifierCallback` when reaching this node in a journey.

* [Device Binding Storage node](https://docs.pingidentity.com/auth-node-ref/latest/device-binding-storage.html)

  Optionally persists collected device binding data to a user's profile in the identity store.

  By default, the **Device Binding node** stores device data in the user's profile. You can choose instead to store the device data in transient state, perhaps to run a custom script to extract additional context.

  In this case, you can use a **Device Binding Storage node** to store the data in the user's profile.

  This node runs entirely server-side, and doesn't send a callback to the client.

## Securing access to the keys

The Device Binding module supports four distinct methods for accessing the private key, each offering different levels of security and user experience.

You specify which authentication type your client uses in the configuration of the **Device Binding node**. To change the authentication type to access the keys, you'll need to rebind the client device

Supported authentication types to access bound keys

* Biometric Only

* Biometric with Fallback

* Application PIN

* No Authentication

|                     |                                                                                                                                                                                                                                                                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type name           | `BIOMETRIC_ONLY`                                                                                                                                                                                                                                                                                                                  |
| Description         | Requires strict biometric authentication with no fallback options                                                                                                                                                                                                                                                                 |
| Security level      | **High**                                                                                                                                                                                                                                                                                                                          |
| User experience     | Streamlined for devices with reliable biometric sensors                                                                                                                                                                                                                                                                           |
| Behavior            | - Only accepts biometric authentication, such as a fingerprint, face recognition, or an iris scan

- Fails immediately if biometric authentication is unavailable or unsuccessful

- No option to fall back to device PIN, pattern, or password

- Ideal for high-security applications where biometric verification is mandatory |
| Use cases           | Financial applications, enterprise security, medical applications                                                                                                                                                                                                                                                                 |
| Device requirements | Must have functional biometric sensors and enrolled biometric data                                                                                                                                                                                                                                                                |

|                     |                                                                                                                                                                                                                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type name           | `BIOMETRIC_ALLOW_FALLBACK`                                                                                                                                                                                                                                                                                                                   |
| Description         | Prefers biometric authentication but allows fallback to device credentials                                                                                                                                                                                                                                                                   |
| Security level      | **Medium** to **High**                                                                                                                                                                                                                                                                                                                       |
| User experience     | Flexible with multiple authentication options                                                                                                                                                                                                                                                                                                |
| Behavior            | * The primary method is a biometric authentication, such as a fingerprint, face recognition, or an iris scan

* If biometric authentication fails or is unavailable, users can use device credentials

  * Device credentials include a PIN, a pattern, or a password set at the system level

* Provides better accessibility and usability |
| Use cases           | Consumer applications, general-purpose authentication, accessibility-focused apps                                                                                                                                                                                                                                                            |
| Device requirements | - Biometric sensors preferred, but not required

- Must configure the device lock screen                                                                                                                                                                                                                                                     |

|                     |                                                                                                                                                                                                                                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type name           | `APPLICATION_PIN`                                                                                                                                                                                                                                                                               |
| Description         | Requires a custom PIN that the application manages entirely                                                                                                                                                                                                                                     |
| Security level      | **Medium**                                                                                                                                                                                                                                                                                      |
| User experience     | Consistent across all devices regardless of hardware capabilities                                                                                                                                                                                                                               |
| Behavior            | * Uses an application-specific PIN separate from device credentials

  * The application collects the PIN through a custom UI

  * The application securely stores PIN data using encrypted storage mechanisms

  * Independent of device biometric capabilities or system-level authentication |
| Use cases           | - Devices without biometric capabilities

- Applications requiring custom authentication flows

- Scenarios where users prefer PIN over biometric authentication

  * Cross-platform consistency requirements                                                                                   |
| Device requirements | None - works on all devices                                                                                                                                                                                                                                                                     |

|                         |                                                                                                                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type name               | `NONE`                                                                                                                                                                                                              |
| Description             | No user authentication required to access cryptographic keys                                                                                                                                                        |
| Security Level          | **Low**                                                                                                                                                                                                             |
| User Experience         | Seamless with no authentication prompts                                                                                                                                                                             |
| Behavior                | * Users can access keys immediately without any verification

* No authentication prompts or delays

* Cryptographic operations proceed without user interaction

* Relies solely on device possession for security |
| Use cases               | - Applications with alternative security measures                                                                                                                                                                   |
| Security Considerations | Anyone with device access can use the cryptographic keys                                                                                                                                                            |
| Device Requirements     | None                                                                                                                                                                                                                |

## Installing modules

To install the Device Binding module for iOS, use Swift Package Manager (SPM) or Cocoapods to add the dependency to your project.

* SPM (Swift Package Manager)

* CocoaPods

You can install packages by using SPM (Swift Package Manager) on the iOS project.

1. In Xcode, in the Project Navigator, right-click your project, and then click Add Package Dependencies…​.

2. In the **Search or Enter Package URL** field, enter the URL of the repo containing the Orchestration SDK for iOS, `https://github.com/ForgeRock/ping-ios-sdk.git`.

3. In **Add to Project**, select the name of your project, and then click **Add Package**.

   Xcode shows a dialog containing the libraries available for iOS.

4. Select the `PingBinding` library, and in the **Add to Target** column select the name of your project.

5. Repeat the previous step for any other packages you want to use in your project.

6. Click **Add Package**.

   Xcode displays the chosen packages and any prerequisites they might have in the **Package Dependencies** pane of the Project Navigator.

1) If you don't already have CocoaPods, install the [latest version](https://guides.cocoapods.org/using/getting-started.html).

2) If you don't already have a Podfile, in a terminal window, run the following command to create a new [Podfile](https://guides.cocoapods.org/syntax/podfile.html):

   ```
   pod init
   ```

3) Add the following lines to your Podfile:

   ```
   pod 'PingBinding'
   ```

4) Run the following command to install pods:

   ```
   pod install
   ```

## Binding keys to a device

To bind keys to a device, the Binding Module performs the following tasks:

1. **Validation**: Checks device support for authentication type

2. **Cleanup**: Removes existing keys for the user

3. **Key generation**: Creates new cryptographic key pair

4. **Authentication**: Verifies user identity

5. **JWT Signing**: Creates signed proof-of-possession

6. **Storage**: Saves user key meta data

Use the `bind()` method to bind keys to the device as follows:

Binding keys to an iOS device

```swift
import PingBinding
import PingJourney

private func handleDeviceBinding() {
  Task {
    let result = await callback.bind()
    switch result {
      case .success(let json):
        print("Device binding success: \(json)")
      case .failure(let error):
        if let deviceBindingStatus = error as? DeviceBindingStatus {
          print("Device binding failed: \(deviceBindingStatus.errorMessage)")
        } else {
          print("Device binding failed: \(error.localizedDescription)")
        }
    }
    onNext()
  }
}
```

## Verifying bound keys on a device

To verify that a device possesses a bound key, the Binding Module performs the following tasks:

1. **Validation**: Validates custom claims

2. **Key Lookup**: Finds appropriate user key

3. **Authentication**: Verifies user identity

4. **Challenge signing**: Signs server challenge

5. **JWT creation**: Creates verification JWT

Use the `DeviceSigningVerifierCallback.sign()` method to verify possession of bound keys as follows:

Verifying key possession by signing data on an iOS device

```swift
import PingBinding
import PingJourney

func handleDeviceSigning(callback: DeviceSigningVerifierCallback, onNext: @escaping () -> Void) {
    Task {
        let result = await callback.sign()
        switch result {
        case .success:
            print("Signing successful")
        case .failure(let error):
            print("Signing failed: \(error.localizedDescription)")
        }
        // Continue to the next node
        onNext()
    }
}
```

### Adding custom claims when signing using bound keys

When signing a server-provided challenge to verify possession of a bound key, you can add custom data to the resulting JSON Web Token (JWT). The server can access and use this data for context, or for auditing purposes.

Add a `claims` attribute to the configuration, including the key-value pairs you want to add to the JWT:

Adding custom claims to the JWT on an iOS device

```swift
let result = await callback.sign { config in
  // Use custom claims
  config.claims = [
    "amount": "100.00",
    "recipient": "babs@example.com",
    "currency": "USD",
  ]
}
```

## Configuring authenticator parameters

You can configure a number of device binding parameters, such as the algorithm used, and the validity time.

Configuring AppPinAuthenticator parameters on iOS

```swift
import PingBinding

let result = await callback.bind { config in
    // Specify custom app PIN auth parameters
    let appPinConfig = AppPinConfig(
        logger: myCustomLogger,
        prompt: Prompt(title: "Enter PIN", subtitle: "Security", description: "Enter your 4-digit PIN"),
        pinRetry: 5,
        keyTag: "my-custom-key-tag",
        pinCollector: CustomPinCollector()
    )

    // Use the custom authenticator with the config
    config.deviceAuthenticator = AppPinAuthenticator(config: appPinConfig)
}
```

Configuring Biometric authenticator parameters on iOS

```swift
import PingBinding

let result = await callback.bind { config in
    // Specify custom biometric auth parameters
    let biometricConfig = BiometricAuthenticatorConfig(
        logger: myCustomLogger,
        keyTag: "my-biometric-key-tag",
    )

    // Set the authenticator config - uses the appropriate authenticator (BiometricOnlyAuthenticator
    // or BiometricDeviceCredentialAuthenticator) based on the callback type
    config.authenticatorConfig = biometricConfig
}
```

## Replacing the default system UI

The **PingBinding** module uses system dialogs and alerts by default in the following situations:

* Application PIN entry

  If the authentication journey specifies the `APPLICATION_PIN` authentication method to access the secure keys, the module uses a system alert to obtain the PIN from the user.

* Key selection

  If there are multiple keys available on the device that could be used to fulfil the request, the module uses `UIAlertController` with an action sheet to display the suitable keys to the user to choose the correct one.

You can implement your own custom user interface for both of these situations.

### Creating a custom UI for PIN entry

To implement a custom UI for accepting PIN codes from the user, complete the following steps:

1. [Step 1. Create a Custom UI for PIN Collection](#pin_ui_view)

2. [Step 2. Implement the PinCollector Protocol](#pin_ui_protocol)

3. [Step 3. Use the custom collector for binding and signing](#pin_ui_configure)

#### Step 1. Create a Custom UI for PIN Collection

You need to create a view that serves as your PIN entry screen.

The following example uses SwiftUI to create a simple view that collects a 4-digit PIN.

Creating a SwiftUI view to collect a 4-digit PIN

```swift
// In your application, e.g., PinCollectorView.swift
import SwiftUI
import PingBinding

struct PinCollectorView: View {
    let prompt: Prompt
    let completion: (String?) -> Void

    @State private var pin: String = ""

    var body: some View {
        VStack(spacing: 20) {
            Text(prompt.title)
                .font(.title)
            Text(prompt.description)
                .font(.subheadline)

            TextField("4-digit PIN", text: $pin)
                .keyboardType(.numberPad)
                .padding()

            HStack {
                Button("Cancel") { completion(nil) }
                Button("Submit") { completion(pin) }
                    .disabled(pin.count != 4)
            }
        }
        .padding()
    }
}
```

#### Step 2. Implement the PinCollector Protocol

To allow the **PingBinding** module to present your custom UI and return the collected PIN code, implement the `PinCollector` protocol.

Implementing the PinCollector protocol

```swift
// In your application, e.g., CustomPinCollector.swift
import UIKit
import SwiftUI
import PingBinding

class CustomPinCollector: PinCollector {
    func collectPin(prompt: Prompt, completion: @escaping @Sendable (String?) -> Void) {
        DispatchQueue.main.async {
            guard let topVC = UIApplication.shared.windows.first?.rootViewController else {
                completion(nil)
                return
            }

            let pinView = PinCollectorView(prompt: prompt) { pin in
                topVC.dismiss(animated: true) {
                    completion(pin)
                }
            }

            let hostingController = UIHostingController(rootView: pinView)
            topVC.present(hostingController, animated: true)
        }
    }
}
```

#### Step 3. Use the custom collector for binding and signing

To use your new UI for binding and signing, specify the implementation class in the configuration of the `sign()` and `bind()` methods.

Configure binding to use a custom UI for collecting app PINs

```swift
// In your view that handles the DeviceBindingCallback
import PingBinding

func handleDeviceBinding(callback: DeviceBindingCallback, onNext: @escaping () -> Void) {
    Task {
        let result = await callback.bind { config in
            // Customize the PIN collector for application PIN authentication
            config.pinCollector = CustomPinCollector()
        }

        // Handle result...
        onNext()
    }
}
```

Configure signing to use a custom UI for collecting app PINs

```swift
// In your view that handles the DeviceSigningVerifierCallback
import PingBinding

func handleDeviceSigning(callback: DeviceSigningVerifierCallback, onNext: @escaping () -> Void) {
    Task {
        let result = await callback.sign { config in
            // Customize the PIN collector for application PIN authentication
            config.pinCollector = CustomPinCollector()
        }

        // Handle result...
        onNext()
    }
}
```

### Creating a custom UI for key selection

Implementing a custom UI for displaying available key pairs to the user to select the correct one is useful in the following situations:

* Multiple users have bound keys on the same physical device

* You want to provide a branded UI for key selection

* You need to display additional context about each key to help with selection

To implement a custom UI for displaying available key pairs, complete the following steps:

. . .

#### Step 1. Create a custom UI for key selection

You need to create a view that displays the available keys and allow the user to select one.

The following example uses SwiftUI to create a view that allows key selection:

Creating a SwiftUI view to allow key selection

```swift
// In your application, e.g., UserKeySelectorView.swift
import SwiftUI
import PingBinding

struct UserKeySelectorView: View {
    let userKeys: [UserKey]
    let prompt: Prompt
    let completion: (UserKey?) -> Void

    var body: some View {
        NavigationView {
            VStack(spacing: 20) {
                if !prompt.description.isEmpty {
                    Text(prompt.description)
                        .font(.body)
                        .multilineTextAlignment(.center)
                        .padding()
                }

                List(userKeys, id: \.id) { userKey in
                    Button(action: {
                        completion(userKey)
                    }) {
                        VStack(alignment: .leading, spacing: 4) {
                            if !userKey.username.isEmpty {
                                Text(userKey.username)
                                    .font(.headline)
                            }
                            if !userKey.userId.isEmpty {
                                Text("User ID: \(userKey.userId)")
                                    .font(.caption)
                                    .foregroundColor(.secondary)
                            }
                            Text("Auth: \(userKey.authType.rawValue)")
                                .font(.caption)
                                .foregroundColor(.secondary)
                        }
                        .padding(.vertical, 4)
                    }
                }
            }
            .navigationTitle(prompt.title.isEmpty ? "Select Device Key" : prompt.title)
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") {
                        completion(nil)
                    }
                }
            }
        }
    }
}
```

#### Step 2. Implement the UserKeySelector Protocol

To allow the **PingBinding** module to present your custom UI and return the selected key, implement the `UserKeySelector` protocol.

Implementing the UserKeySelector protocol

```swift
// In your application, e.g., CustomUserKeySelector.swift
import UIKit
import SwiftUI
import PingBinding

class CustomUserKeySelector: UserKeySelector {
    func selectKey(userKeys: [UserKey], prompt: Prompt) async -> UserKey? {
        return await withCheckedContinuation { continuation in
            DispatchQueue.main.async {
                guard let topVC = self.getTopViewController() else {
                    continuation.resume(returning: nil)
                    return
                }

                let selectorView = UserKeySelectorView(
                    userKeys: userKeys,
                    prompt: prompt
                ) { selectedKey in
                    topVC.dismiss(animated: true) {
                        continuation.resume(returning: selectedKey)
                    }
                }

                let hostingController = UIHostingController(rootView: selectorView)
                hostingController.modalPresentationStyle = .formSheet
                topVC.present(hostingController, animated: true)
            }
        }
    }

    private func getTopViewController() -> UIViewController? {
        guard let windowScene = UIApplication.shared.connectedScenes.first as? UIWindowScene,
              let window = windowScene.windows.first(where: { $0.isKeyWindow }),
              let rootViewController = window.rootViewController else {
            return nil
        }

        var topViewController = rootViewController
        while let presentedViewController = topViewController.presentedViewController {
            topViewController = presentedViewController
        }

        return topViewController
    }
}
```

#### Step 3. Use the custom key selector for signing

To use your new UI signing, specify the implementation class in the configuration of the `sign()` and `bind()` methods.

Configure binding to use a custom UI for selecting keys

```swift
import PingBinding

func handleDeviceSigning(callback: DeviceSigningVerifierCallback, onNext: @escaping () -> Void) {
    Task {
        let result = await callback.sign { config in
            // Use custom UI for selecting from multiple device keys
            config.userKeySelector = CustomUserKeySelector()
        }

        switch result {
        case .success:
            print("Signing successful")
        case .failure(let error):
            print("Signing failed: \(error.localizedDescription)")
        }

        onNext()
    }
}
```

## Handling errors

If the Device Binding module returns `failure` when you call `bind()` or `sign()`, you can get the details of the error and take the appropriate action.

**Common error codes and how to remediate them**

| Error                 | Description                                                                                                                                                                | Remediation                                                                                     |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `unsupported`         | The device lacks required capabilities, or the user hasn't enrolled.                                                                                                       | Retry with alternative authentication requirements that don't require biometrics.               |
| `clientNotRegistered` | No keys are available for signing. Either the device hasn't been registered, or the user has removed the authentication methods that protected the private key.            | Redirect the user to bind a new key to the device.                                              |
| `timeout`             | Operation exceeded timeout.                                                                                                                                                | Allow retry with a longer timeout.                                                              |
| `invalidCustomClaims` | Reserved claim names used in custom claims parameter.You can't add custom claims that match the standard required claims in a JWT, such as `sub`, `exp`, `iat`, and `iss`. | Remove or rename the claims listed in the error so they do not clash.                           |
| `abort`               | The user aborted the operation.For example the user clicked **Cancel** rather than provide their fingerprint.                                                              | Handle gracefully, and don't show error.The user chose not to continue the authentication flow. |
| `unAuthorize`         | The user provided invalid credentials.For example, the user entered an incorrect PIN number.                                                                               | Allow retry and prompt for the correct credentials.                                             |

The following example shows how to handle some of these exceptions:

Handling exceptions when binding keys to a device

```swift
let result = await callback.sign()
switch result {
  case .success(let json):
    print("Device signing success: \(json)")
  case .failure(let error):
    if let deviceBindingStatus = error as? DeviceBindingStatus {
      print("Device signing failed: \(deviceBindingStatus.errorMessage)")
    } else {
      print("Device signing failed: \(error.localizedDescription)")
    }
}
onNext()
```

---

---
title: Binding keys to a device in React Native
description: Use the React Native binding module to bind cryptographic keys to a device, verify bound keys during journeys, and manage locally stored key metadata
component: orchsdks
page_id: orchsdks:journey:use-cases/device-binding/react-native-device-binding
canonical_url: https://developer.pingidentity.com/orchsdks/journey/use-cases/device-binding/react-native-device-binding.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Fri, 05 Jun 2026 14:22:33 +0100
keywords: ["Device", "Hardware", "Source Code", "Integration", "SDK", "React Native"]
section_ids:
  before_you_begin: Before you begin
  securing_access_to_the_keys: Securing access to the keys
  installing_modules: Installing modules
  create_the_binding_client: Create the binding client
  configuration_options: Configuration options
  binding_keys_to_a_device: Binding keys to a device
  bindforjourney_options: bindForJourney options
  collecting_a_device_name_from_the_user: Collecting a device name from the user
  verifying_bound_keys_on_a_device: Verifying bound keys on a device
  signforjourney_options: signForJourney options
  adding-custom-claims-when-signing: Adding custom claims when signing
  implementing_the_ui_for_pin_and_key_selection: Implementing the UI for PIN and key selection
  providing-a-custom-pin-collector: Providing a custom PIN collector
  bindingprompt_properties: BindingPrompt properties
  example_pin_collector_component: Example PIN collector component
  providing-a-custom-key-selector: Providing a custom key selector
  userkeyoption_properties: UserKeyOption properties
  managing_locally_stored_keys: Managing locally stored keys
  listing_all_keys: Listing all keys
  deleting_a_single_key: Deleting a single key
  deleting_all_keys: Deleting all keys
  key_management_functions: Key management functions
  handling_errors: Handling errors
  error_codes: Error codes
---

# Binding keys to a device in React Native

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: react, set=fab]React Native

The Device Binding module provides secure device registration and authentication capabilities for React Native applications. It enables applications to bind cryptographic keys to a device and restrict access to those keys using biometrics, a PIN, or other additional authentication methods.

## Before you begin

You need to create an authentication journey in your server using the appropriate nodes to enable device binding.

The nodes you can use for device binding Journeys include the follows:

* [Device Binding node](https://docs.pingidentity.com/auth-node-ref/latest/device-binding.html)

  Allows users to register one or more devices to their account. A user can bind multiple devices, and each device can be bound to multiple users.

  The client receives a `DeviceBindingCallback` when reaching this node in a journey.

* [Device Signing Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/device-signing-verifier.html)

  Verifies possession of a registered bound device.

  The node requires the client device to sign a challenge string using the private key that corresponds to the public key stored on the server during initial binding.

  The client receives a `DeviceSigningVerifierCallback` when reaching this node in a journey.

* [Device Binding Storage node](https://docs.pingidentity.com/auth-node-ref/latest/device-binding-storage.html)

  Optionally persists collected device binding data to a user's profile in the identity store.

  By default, the **Device Binding node** stores device data in the user's profile. You can choose instead to store the device data in transient state, perhaps to run a custom script to extract additional context.

  In this case, you can use a **Device Binding Storage node** to store the data in the user's profile.

  This node runs entirely server-side, and doesn't send a callback to the client.

## Securing access to the keys

The Device Binding module supports four distinct methods for accessing the private key, each offering different levels of security and user experience.

You specify which authentication type your client uses in the configuration of the **Device Binding node**. To change the authentication type to access the keys, you'll need to rebind the client device

Supported authentication types to access bound keys

* Biometric Only

* Biometric with Fallback

* Application PIN

* No Authentication

|                     |                                                                                                                                                                                                                                                                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type name           | `BIOMETRIC_ONLY`                                                                                                                                                                                                                                                                                                                  |
| Description         | Requires strict biometric authentication with no fallback options                                                                                                                                                                                                                                                                 |
| Security level      | **High**                                                                                                                                                                                                                                                                                                                          |
| User experience     | Streamlined for devices with reliable biometric sensors                                                                                                                                                                                                                                                                           |
| Behavior            | - Only accepts biometric authentication, such as a fingerprint, face recognition, or an iris scan

- Fails immediately if biometric authentication is unavailable or unsuccessful

- No option to fall back to device PIN, pattern, or password

- Ideal for high-security applications where biometric verification is mandatory |
| Use cases           | Financial applications, enterprise security, medical applications                                                                                                                                                                                                                                                                 |
| Device requirements | Must have functional biometric sensors and enrolled biometric data                                                                                                                                                                                                                                                                |

|                     |                                                                                                                                                                                                                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type name           | `BIOMETRIC_ALLOW_FALLBACK`                                                                                                                                                                                                                                                                                                                   |
| Description         | Prefers biometric authentication but allows fallback to device credentials                                                                                                                                                                                                                                                                   |
| Security level      | **Medium** to **High**                                                                                                                                                                                                                                                                                                                       |
| User experience     | Flexible with multiple authentication options                                                                                                                                                                                                                                                                                                |
| Behavior            | * The primary method is a biometric authentication, such as a fingerprint, face recognition, or an iris scan

* If biometric authentication fails or is unavailable, users can use device credentials

  * Device credentials include a PIN, a pattern, or a password set at the system level

* Provides better accessibility and usability |
| Use cases           | Consumer applications, general-purpose authentication, accessibility-focused apps                                                                                                                                                                                                                                                            |
| Device requirements | - Biometric sensors preferred, but not required

- Must configure the device lock screen                                                                                                                                                                                                                                                     |

|                     |                                                                                                                                                                                                                                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type name           | `APPLICATION_PIN`                                                                                                                                                                                                                                                                               |
| Description         | Requires a custom PIN that the application manages entirely                                                                                                                                                                                                                                     |
| Security level      | **Medium**                                                                                                                                                                                                                                                                                      |
| User experience     | Consistent across all devices regardless of hardware capabilities                                                                                                                                                                                                                               |
| Behavior            | * Uses an application-specific PIN separate from device credentials

  * The application collects the PIN through a custom UI

  * The application securely stores PIN data using encrypted storage mechanisms

  * Independent of device biometric capabilities or system-level authentication |
| Use cases           | - Devices without biometric capabilities

- Applications requiring custom authentication flows

- Scenarios where users prefer PIN over biometric authentication

  * Cross-platform consistency requirements                                                                                   |
| Device requirements | None - works on all devices                                                                                                                                                                                                                                                                     |

|                         |                                                                                                                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type name               | `NONE`                                                                                                                                                                                                              |
| Description             | No user authentication required to access cryptographic keys                                                                                                                                                        |
| Security Level          | **Low**                                                                                                                                                                                                             |
| User Experience         | Seamless with no authentication prompts                                                                                                                                                                             |
| Behavior                | * Users can access keys immediately without any verification

* No authentication prompts or delays

* Cryptographic operations proceed without user interaction

* Relies solely on device possession for security |
| Use cases               | - Applications with alternative security measures                                                                                                                                                                   |
| Security Considerations | Anyone with device access can use the cryptographic keys                                                                                                                                                            |
| Device Requirements     | None                                                                                                                                                                                                                |

## Installing modules

To install the module into your React Native project, use `yarn` or `npm` as follows:

* yarn

* npm

```shell
yarn add @ping-identity/rn-binding
```

```shell
npm install @ping-identity/rn-binding
```

For Journey-integrated collection, also install the Journey module if you have not already done so:

* yarn

* npm

```shell
yarn add @ping-identity/rn-journey
```

```shell
npm install @ping-identity/rn-journey
```

## Create the binding client

You create a binding client by calling `createBindingClient()`, which creates the client once at app startup or when configuring your journey integrations. You can reuse it for the lifetime of the app:

Creating the device binding client

```typescript
import { createBindingClient } from '@ping-identity/rn-binding';
import { logger } from '@ping-identity/rn-logger';

const bindingLogger = logger({ level: 'debug' });

const bindingClient = createBindingClient({
  logger: bindingLogger,
});
```

### Configuration options

| Option               | Required | Description                                                                                                                                                                                                                                            |
| -------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `logger`             | No       | A `LoggerInstance` created by `logger({ level })` from `@ping-identity/rn-logger`.Provides diagnostic output for binding operations.Learn more in [Configuring logging in React Native](../../customization/logging/react-native-custom-logging.html). |
| `ui.pinCollector`    | No       | A function `(prompt: BindingPrompt) => Promise<string>` that collects a PIN from the user.Replaces the default native PIN dialog. See [Providing a custom PIN collector](#providing-a-custom-pin-collector).                                           |
| `ui.userKeySelector` | No       | A function `(keys: UserKeyOption[]) => Promise<UserKeyOption>` that presents available keys for the user to select.Replaces the default native key selector. See [Providing a custom key selector](#providing-a-custom-key-selector).                  |
| `userKeyStorage`     | No       | A storage handle for persisting bound key metadata.Useful for sharing key state across app sessions.                                                                                                                                                   |

## Binding keys to a device

When a journey node contains a **Device Binding** step, the journey callback type is `DeviceBindingCallback`.

Call `bindingClient.bindForJourney()` to generate a cryptographic key pair, authenticate the user, and register the public key with the server:

Binding cryptographic keys to a device during a journey

```typescript
import { createBindingClient } from '@ping-identity/rn-binding';
import { useJourney } from '@ping-identity/rn-journey';

const bindingClient = createBindingClient();
const [node, actions] = useJourney(journeyClient);

async function handleDeviceBinding(deviceName?: string) {
  await bindingClient.bindForJourney(journeyClient, {
    deviceName,   // Optional: custom label for this device
  });

  // The callback has been fulfilled — advance the journey
  await actions.next();
}
```

The binding process performs the following steps:

1. Validates device support for the requested authentication type.

2. Removes any existing keys for the user on this device.

3. Generates a new cryptographic key pair.

4. Authenticates the user (biometric, PIN, or none, depending on server configuration).

5. Creates a signed proof-of-possession JWT.

6. Stores user key metadata locally.

### `bindForJourney` options

| Option             | Required | Description                                                                                                                                                                    |
| ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `index`            | No       | Zero-based index of the `DeviceBindingCallback` within the node, when a node contains multiple binding callbacks. Defaults to `0`.                                             |
| `deviceName`       | No       | A human-readable label for the device shown in the server's registered devices list. Defaults to the device model name when omitted.                                           |
| `signingAlgorithm` | No       | Override the signing algorithm for Android devices. It uses the server-configured default when omitted. This property is ignored by the iOS SDK, which uses ES256 exclusively. |
| `appPin`           | No       | A `BindingAppPinConfig` object that configures the pin dialog behavior.                                                                                                        |
| `biometric`        | No       | Override biometric authentication parameters.                                                                                                                                  |
| `jwt`              | No       | Override JWT generation parameters.                                                                                                                                            |

### Collecting a device name from the user

In a profile management journey you may want to let the user choose a name for their device. Detect the `DeviceBindingCallback` field in `useJourneyForm` and render a text input for the device name:

Collecting a device name from the user during binding

```typescript
import { useJourneyForm } from '@ping-identity/rn-journey';

const form = useJourneyForm(node);

const bindingField = form.getFieldByType('DeviceBindingCallback');

// The field has executionMode: 'integration_required'
// Render a text input and pass the entered value to bindForJourney

async function handleBind(enteredDeviceName: string) {
  await bindingClient.bindForJourney(journeyClient, {
    index: bindingField?.ref.typeIndex ?? 0,
    deviceName: enteredDeviceName.trim() || undefined,
  });
  await actions.next();
}
```

|   |                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | `DeviceBindingCallback` has `executionMode: 'integration_required'` but also exposes a device-name input field that is visible to the user. It is not auto-forwarded by default — the user must confirm the device name before binding proceeds. Contrast this with `DeviceSigningVerifierCallback`, which is fully auto-forwardable. |

## Verifying bound keys on a device

When a journey node contains a **Device Signing Verifier** step, the journey callback type is `DeviceSigningVerifierCallback`. Call `bindingClient.signForJourney()` to sign the server-provided challenge using the locally stored private key:

Signing a server challenge with a bound device key

```typescript
async function handleDeviceSigning() {
  await bindingClient.signForJourney(journeyClient);

  // The callback has been fulfilled — advance the journey
  await actions.next();
}
```

The signing process performs the following steps:

1. Validates any custom claims provided

2. Looks up the appropriate user key for the current user

3. Authenticates the user (biometric, PIN, or none)

4. Signs the server challenge with the private key

5. Creates a verification JWT

### `signForJourney` options

| Option             | Required | Description                                                                                                                        |
| ------------------ | -------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `index`            | No       | Zero-based index of the `DeviceSigningVerifierCallback` within the node. Defaults to `0`.                                          |
| `claims`           | No       | Custom key-value pairs added to the verification JWT. See [Adding custom claims when signing](#adding-custom-claims-when-signing). |
| `signingAlgorithm` | No       | Override the signing algorithm.                                                                                                    |
| `appPin`           | No       | Pre-supply an application PIN string.                                                                                              |
| `biometric`        | No       | Override biometric authentication parameters.                                                                                      |
| `jwt`              | No       | Override JWT generation parameters.                                                                                                |

### Adding custom claims when signing

When signing the server challenge you can add custom data to the resulting JWT. The server can use these claims for context or auditing:

Adding custom claims to the signing JWT

```typescript
await bindingClient.signForJourney(journeyClient, {
  claims: {
    amount: '100.00',
    recipient: 'babs@example.com',
    currency: 'USD',
  },
});
```

|   |                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You cannot use reserved JWT claim names (`sub`, `exp`, `iat`, `iss`, `nbf`, and `challenge`) as custom claim keys. Doing so causes the operation to fail with an `invalidCustomClaims` error. |

## Implementing the UI for PIN and key selection

The Device Binding module does not include built-in PIN or key-selection screens, so you must supply your own UI through two functions passed in the `ui` object of `createBindingClient`. The `pinCollector` function is required whenever the server configures `APPLICATION_PIN` authentication. The `userKeySelector` function handles the parallel `RNPingBinding_UserKeyRequired` event that fires when multiple users have bound keys on the same device.

### Providing a custom PIN collector

When the server configures `APPLICATION_PIN` authentication, the native SDK emits a `RNPingBinding_PinRequired` event requesting a PIN from the user. You must supply a `pinCollector` function in `createBindingClient` configuration because the module does not have a built-in PIN UI.

The `pinCollector` receives a `BindingPrompt` that is populated with configuration values from the server, and must return a `Promise<string>` that resolves to the PIN the user entered, or rejects to cancel the operation:

Providing a custom PIN collector to the binding client

```typescript
import { createBindingClient } from '@ping-identity/rn-binding';
import type { BindingPrompt } from '@ping-identity/rn-binding';

// Simple imperative promise resolver — replace with your UI implementation
let _resolvePinPromise: ((pin: string) => void) | null = null;
let _rejectPinPromise: (() => void) | null = null;

const bindingClient = createBindingClient({
  ui: {
    pinCollector: async (prompt: BindingPrompt): Promise<string> => {
      // Show your PIN modal here; resolve when the user submits
      return new Promise((resolve, reject) => {
        _resolvePinPromise = resolve;
        _rejectPinPromise = reject;
        showPinModal(prompt);  // your UI function
      });
    },
  },
});
```

#### `BindingPrompt` properties

| Property      | Type     | Description                                                               |
| ------------- | -------- | ------------------------------------------------------------------------- |
| `title`       | `string` | Modal heading. Typically `"Enter PIN"` or similar server-configured text. |
| `subtitle`    | `string` | Secondary heading line.                                                   |
| `description` | `string` | Instructional text shown below the heading.                               |

#### Example PIN collector component

Calling `pinCollector` bypasses the native default PIN dialog and calls your implementation instead. The prompt argument supplies `title`, `subtitle`, and `description` strings sourced from the server-side journey callback.

Implementing a PIN collector component

```typescript
  import { createBindingClient } from '@ping-identity/rn-binding';
  import type { BindingPrompt } from '@ping-identity/rn-binding';

  const pinCollector = (prompt: BindingPrompt): Promise<string> => {
    // prompt.title       - dialog title from the server callback
    // prompt.subtitle    - dialog subtitle from the server callback
    // prompt.description - dialog description from the server callback
    return new Promise((resolve, reject) => {
      // present your own PIN input UI here
      // call resolve(pin) with the entered PIN string
      // call reject() if the user cancels
    });
  };

  export const bindingClient = createBindingClient({
    ui: {
      pinCollector,
    },
  });
```

### Providing a custom key selector

When multiple users have bound keys on the same device, the native SDK emits a `RNPingBinding_UserKeyRequired` event to ask the user which key to use. You can supply a `userKeySelector` function to replace React Native's default behavior, which delegates key selection to the native platform UI:

Providing a custom key selector for multi-user devices

```typescript
import { createBindingClient } from '@ping-identity/rn-binding';
import type { UserKeyOption } from '@ping-identity/rn-binding';

const bindingClient = createBindingClient({
  ui: {
    userKeySelector: async (keys: UserKeyOption[]): Promise<UserKeyOption> => {
      // Show a list of keys to the user and resolve with the selected one.
      // Reject or throw to cancel the operation.
      return showKeySelectionSheet(keys);
    },
  },
});
```

#### `UserKeyOption` properties

| Property             | Type     | Description                                                                                     |
| -------------------- | -------- | ----------------------------------------------------------------------------------------------- |
| `id`                 | `string` | Unique key identifier (kid) used for deletion.                                                  |
| `userId`             | `string` | The user identifier associated with this key.                                                   |
| `username`           | `string` | Human-readable username shown in selection UI.                                                  |
| `authenticationType` | `string` | Authentication type configured for this key (for example, `BIOMETRIC_ONLY`, `APPLICATION_PIN`). |

## Managing locally stored keys

The module exposes three key-management functions that operate on locally stored binding key metadata. These are useful for building device management screens.

### Listing all keys

Listing all locally stored binding keys

```typescript
import { getAllKeys } from '@ping-identity/rn-binding';

const keys = await getAllKeys();
// Returns UserKeyOption[]
keys.forEach((key) => {
  console.log(`${key.username} (${key.authenticationType}) — id: ${key.id}`);
});
```

### Deleting a single key

Deleting a single binding key by UserKeyOption

```typescript
import { deleteKey } from '@ping-identity/rn-binding';

await deleteKey(key);   // key is a UserKeyOption returned by getAllKeys()
```

### Deleting all keys

Deleting all locally stored binding keys

```typescript
import { deleteAllKeys } from '@ping-identity/rn-binding';

await deleteAllKeys();
```

### Key management functions

Using key management functions together

```typescript
  import {
    getAllKeys,
    deleteKey,
    deleteAllKeys,
  } from '@ping-identity/rn-binding';
  import type { UserKeyOption } from '@ping-identity/rn-binding';

  /**
   * Retrieves all device binding keys stored locally on the device.
   * Returns an array of UserKeyOption, each with id, userId, username,
   * and authenticationType fields.
   */
  export const fetchAllKeys = async (): Promise<UserKeyOption[]> => {
    return await getAllKeys();
  };

  /**
   * Deletes a single device binding key by its userId and id.
   * Pass a UserKeyOption obtained from getAllKeys().
   */
  export const removeKey = async (key: UserKeyOption): Promise<void> => {
    await deleteKey(key);
  };

  /**
   * Deletes all locally stored device binding keys.
   * Use with caution — this cannot be undone and will require
   * the user to re-bind their device.
   */
  export const removeAllKeys = async (): Promise<void> => {
    await deleteAllKeys();
  };
```

## Handling errors

`bindForJourney` and `signForJourney` both reject with a `BindingError` when the native operation fails.

Catching and handling BindingError from journey operations

```typescript
import { BindingError } from '@ping-identity/rn-binding';

try {
  await bindingClient.bindForJourney(journeyClient, { deviceName });
} catch (err) {
  if (err instanceof BindingError) {
    console.error(`[${err.code}] ${err.message}`);
    handleBindingError(err.code);
  } else {
    throw err;
  }
}
```

### Error codes

| Error code              | Cause                                                                                                                                       | Remediation                                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `UNSUPPORTED`           | The device lacks required capabilities, or the user has not enrolled biometrics.                                                            | Retry with an alternative authentication type, or prompt the user to enroll biometrics in device settings. |
| `CLIENT_NOT_REGISTERED` | No keys are available for signing. The device has not been bound, or the user removed the authentication method protecting the private key. | Redirect the user to run a binding journey to register a new key.                                          |
| `TIMEOUT`               | The operation exceeded the configured timeout.                                                                                              | Allow retry, optionally with a longer timeout.                                                             |
| `INVALID_CUSTOM_CLAIMS` | Reserved claim names (`sub`, `exp`, `iat`, `iss`, and so on) were used in `claims`.                                                         | Remove or rename the conflicting claim keys.                                                               |
| `ABORT`                 | The user cancelled the operation, for example by tapping **Cancel** on the biometric prompt.                                                | Handle gracefully without showing an error — the user chose not to continue.                               |
| `UNAUTHORIZE`           | The user provided invalid credentials, for example an incorrect PIN.                                                                        | Allow retry and prompt for the correct credentials.                                                        |

---

---
title: Collecting device profiles in Android
description: Use the Device Profile module to collect hardware, network, and location attributes from an Android device for use in PingOne Advanced Identity Cloud and PingAM journeys
component: orchsdks
page_id: orchsdks:journey:use-cases/device-profiling/android-device-profile
canonical_url: https://developer.pingidentity.com/orchsdks/journey/use-cases/device-profiling/android-device-profile.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 29 Oct 2025 14:22:33 +0100
keywords: ["Device", "Hardware", "Source Code", "Integration", "SDK", "Android"]
section_ids:
  android_device-profile_modules: Step 1. Installing modules
  android_device-profile_permissions: Step 2. Declaring permissions
  step_3_collecting_device_profiles: Step 3. Collecting device profiles
  adding_collectors_conditionally: Adding collectors conditionally
  creating_custom_collectors: Creating custom collectors
  integrating_with_advanced_identity_cloud_and_pingam_journeys: Integrating with Advanced Identity Cloud and PingAM journeys
---

# Collecting device profiles in Android

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: android, set=fab]Android

The Device Profile module helps you to collect various attributes from an Android device.

It includes preconfigured collectors to collect attributes, and allows you to create your own collectors to suit your requirements.

## Step 1. Installing modules

For obtaining a device profile, you need this module:

* `device-profile`

To install the module into your Android app:

1. In the **Project** tree view of your Android Studio project, open the `build.gradle.kts` file.

2. In the `dependencies` section, add the `device-profile` module as a dependency:

   ```gradle
   dependencies {
       implementation("com.pingidentity.device:device-profile:2.0.1")
   }
   ```

## Step 2. Declaring permissions

The Device Profile module respects the Android permissions model, and certain collectors require that you declare the permissions needed.

To declare the permissions the app might request from the user:

1. Open the project's manifest file.

   For example, **app > manifests > AndroidManifest.xml**.

2. Add the relevant properties as a child of the `<manifest>` element:

   1. For `NetworkCollector`, add the `ACCESS_NETWORK_STATE` permission:

      ```xml
        <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
      ```

   2. For `LocationCollector`, optionally add the `ACCESS_FINE_LOCATION` and `ACCESS_COARSE_LOCATION` permissions:

      ```xml
        <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
        <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
      ```

      |   |                                                                                                                                                                  |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The `LocationCollector` automatically requests the relevant permission when gathering the data if needed, so adding the permissions to the manifest is optional. |

## Step 3. Collecting device profiles

To generate a device profile, create a list of the collectors you want to use, or specify `DefaultDeviceCollector` to use the default list, and then call the `collect()` method to create the device profile JSON:

Obtaining a device profile on an Android device

```kotlin
import com.pingidentity.device.profile.collector.DefaultDeviceCollector
import com.pingidentity.device.profile.collector.collect

suspend fun collectDeviceProfile() {

    // Specify which collectors to use
    val collectors = mutableListOf<DeviceCollector<*>>().apply {
        clear()
        add(PlatformCollector())
        add(HardwareCollector())
        add(NetworkCollector())
        add(TelephonyCollector())
        add(LocationCollector()) // Handles permissions automatically
    }

    // Or use the default list of collectors
    val collectors = mutableListOf<DeviceCollector<*>>().apply(DefaultDeviceCollector())

    // Collect device information
    val deviceProfile = collectors.collect()

    // Use the collected profile (JsonObject)
    println(deviceProfile.toString())
}
```

The **device-profile** module provides the following collectors:

**Included device profile collectors**

| Collector            | Attributes collected                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PlatformCollector`  | Gathers platform and device identification information, such as the brand and model.Example data returned by the `PlatformCollector````json
{
  "platform": {
    platform = "android",
    version = 31,
    device = "pixel6",
    deviceName = "Pixel 6",
    model = "Pixel 6",
    brand = "google",
    locale = "en_US",
    timeZone = "America/New_York",
    jailBreakScore = 0.0
  }
}
```                                                                      |
| `HardwareCollector`  | Gathers information about the hardware, such as the CPU and display.Example data returned by the `HardwareCollector````json
{
  "hardware": {
    "hardware": "flame",
    "manufacturer": "Google",
    "storage": 64,
    "memory": 6144,
    "cpu": 8,
    "display": {
      "width": 1080,
      "height": 2280,
      "orientation": 0
    },
    "camera": {
      "numberOfCameras": 2
    }
  }
}
```                                                             |
| `NetworkCollector`   | Whether the device has any network connectivity.Example data returned by the `NetworkCollector````json
{
   "network": {
      "connected": true
   }
}
```                                                                                                                                                                                                                                                                                                                |
| `TelephonyCollector` | Collects information about the carriers the device uses, such as the carrier name and the country code.Example data returned by the `TelephonyCollector````json
{
   "telephony": {
      "networkCountryIso": "US",
      "carrierName": "Verizon"
   }
}
```                                                                                                                                                                                                             |
| `LocationCollector`  | Collects latitude and longitude coordinates from the device.- Automatically requests permissions when needed

- Uses a transparent activity for seamless permission flow

- Gracefully handles permission denials

- Includes a 30-second protection against timeouts

- Returns `null` if a location is unavailable or deniedExample data returned by the `LocationCollector````json
{
   "location": {
      "latitude": 37.2431,
      "longitude": 115.7930
   }
}
``` |
| `BluetoothCollector` | Whether the device has any bluetooth support.Example data returned by the `BluetoothCollector````json
{
    "bluetooth": {
        "supported": true
    }
}
```                                                                                                                                                                                                                                                                                                           |
| `BrowserCollector`   | Collects the user-agent string of the default browser on the device.Example data returned by the `BrowserCollector````json
{
    "browser": {
        "userAgent": "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"
    }
}
```                                                                                                                                                                 |

### Adding collectors conditionally

You can add collectors by checking that the user has granted the necessary permissions:

Checking permissions before adding collectors

```kotlin
fun createCollectors(context: Context): List<DeviceCollector<*>> {
    return mutableListOf<DeviceCollector<*>>().apply {
        // Always include basic collectors
        add(PlatformCollector())
        add(HardwareCollector())

        // Conditionally add collectors based on permissions
        if (ContextCompat.checkSelfPermission(context, ACCESS_NETWORK_STATE) == PERMISSION_GRANTED) {
            add(NetworkCollector())
        }

        // LocationCollector handles its own permissions
        add(LocationCollector())

        // Add based on device capabilities
        if (packageManager.hasSystemFeature(FEATURE_TELEPHONY)) {
            add(TelephonyCollector)
        }
    }
}
```

## Creating custom collectors

You can create custom device collectors to gather specific attributes depending on your requirements, or the hardware you will support.

Use the `DeviceCollector` class to create your custom collector, using one of the following patterns:

* Factory function

* Data class

* Implement the interface

Using a factory function to create a custom collector

```kotlin
val BatteryCollector = DeviceCollector<Map<String, String>>("battery") {
    mapOf(
        "level" to "100",
        "isCharging" to "true",
    )
}
```

Using a data class to create a custom collector

```kotlin
@Serializable // Ensure the data class is serializable
data class BatteryData(val level: Int, val isCharging: Boolean, val capacity: Int)

val BatteryCollector = DeviceCollector<BatteryData>("battery") {
    BatteryData(
        level = 100,
        isCharging = true,
        capacity = 4000,
    )
}
```

Implementing the interface to create a custom collector

```kotlin
class SecurityCollector : DeviceCollector<SecurityInfo> {
    override val key = "security"
    override val serializer = SecurityInfo.serializer()

    override suspend fun collect(): SecurityInfo {
        return SecurityInfo(
            isDeviceSecure = checkDeviceSecuritySettings(),
            hasScreenLock = checkScreenLockStatus(),
            biometricsAvailable = checkBiometricCapabilities()
        )
    }
}

@Serializable
data class SecurityInfo(
    val isDeviceSecure: Boolean,
    val hasScreenLock: Boolean,
    val biometricsAvailable: Boolean
)
```

## Integrating with Advanced Identity Cloud and PingAM journeys

You can use the Device Profile module to collect the data the [**Device Profile Collector node**](https://docs.pingidentity.com/auth-node-ref/latest/device-profile-collector.html) requires when used as part of a Advanced Identity Cloud or PingAM auth journey.

The Device Profile module provides the `DeviceProfileCallback` class. The class includes a `collect()` method, which collects the data and formats it ready for return to the server.

Preparing a device profile for the Device Profile Collector node

```kotlin
import com.pingidentity.device.profile.DeviceProfileCallback
import kotlinx.coroutines.runBlocking

// Collect with default settings - use DefaultDeviceCollector
val result = deviceProfileCallback.collect {
    collectors.apply(DefaultDeviceCollector())
}

result.onSuccess { profile ->
    // Submit to AIC service
    node = node.next()
    // Note: Some collectors may return null values if data is unavailable
}.onFailure { e ->
    // Handle collection errors
    Log.e("DeviceProfile", "Failed to collect profile", e)
}
```

The module formats the resulting device profile for consumption by the device profile collector node, and includes a device identifier:

Example device profile for the Device Profile Collector node

```json
{
  "identifier": "unique-device-id",
  "platform": {
    "platform": "android",
    "device": "flame",
    "deviceName": "Pixel 4"
  },
  "hardware": {
    "manufacturer": "Google",
    "storage": 64,
    "memory": 6144
  },
  "network": {
    "connected": true
  },
  "location": {
    "latitude": 37.2431,
    "longitude": 115.7930
  }
}
```

You can customize which collectors to use when integrating with the device profile collector node, and also the device identifier the profile includes.

The **Device Profile** module automatically uses the **Device ID** module by default to generate this identifier, but you can customize how it's generated. Learn about customizing the device identifier in [Customizing device identifiers on Android](android-device-ids.html).

Customizing a device profile for the Device Profile Collector node

```kotlin
val profile = deviceProfileCallback.collect {
   // Set a custom device identifier if needed
   deviceIdentifier = object : DeviceIdentifier {
       override val id: suspend () -> String = { "your-custom-device-id" }
   }

   // Adds collectors in a metadata block
   collectors {
      // Clear default collectors
      clear()
      // Add specific collectors
      add(PlatformCollector())
      add(HardwareCollector())
      add(NetworkCollector())
      add(LocationCollector()) // Will automatically handle permissions
   }
}

// The profile is now ready for submission to AIC services
```

The `deviceProfileCallback` class automatically formats the device profile for use with the Device Profile Collector node.

---

---
title: Collecting device profiles in iOS
description: Use the Device Profile module to collect iOS device attributes and integrate with PingOne Advanced Identity Cloud and PingAM authentication journeys
component: orchsdks
page_id: orchsdks:journey:use-cases/device-profiling/ios-device-profile
canonical_url: https://developer.pingidentity.com/orchsdks/journey/use-cases/device-profiling/ios-device-profile.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 29 Oct 2025 14:22:33 +0100
keywords: ["Device", "Hardware", "Source Code", "Integration", "SDK", "iOS"]
section_ids:
  ios_device-profile_module: Step 1. Installing modules
  iOS_device-profile_permissions: Step 2. Declaring permissions
  step_3_collecting_device_profiles: Step 3. Collecting device profiles
  integrating_with_swiftui: Integrating with SwiftUI
  creating_custom_collectors: Creating custom collectors
  integrating_with_advanced_identity_cloud_and_pingam_journeys: Integrating with Advanced Identity Cloud and PingAM journeys
---

# Collecting device profiles in iOS

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: apple, set=fab]iOS

The Device Profile module helps you to collect various attributes from an iOS device.

It includes preconfigured collectors to collect attributes, and allows you to create your own collectors to suit your requirements.

## Step 1. Installing modules

To install the Device Profile module for iOS, use Swift Package Manager (SPM) or Cocoapods to add the dependency to your project.

* SPM (Swift Package Manager)

* CocoaPods

You can install packages by using SPM (Swift Package Manager) on the iOS project.

1. In Xcode, in the Project Navigator, right-click your project, and then click Add Package Dependencies…​.

2. In the **Search or Enter Package URL** field, enter the URL of the repo containing the Orchestration SDK for iOS, `https://github.com/ForgeRock/ping-ios-sdk.git`.

3. In **Add to Project**, select the name of your project, and then click **Add Package**.

   Xcode shows a dialog containing the libraries available for iOS.

4. Select the `PingDeviceProfile` library, and in the **Add to Target** column select the name of your project.

5. Repeat the previous step for any other packages you want to use in your project.

6. Click **Add Package**.

   Xcode displays the chosen packages and any prerequisites they might have in the **Package Dependencies** pane of the Project Navigator.

1) If you don't already have CocoaPods, install the [latest version](https://guides.cocoapods.org/using/getting-started.html).

2) If you don't already have a Podfile, in a terminal window, run the following command to create a new [Podfile](https://guides.cocoapods.org/syntax/podfile.html):

   ```
   pod init
   ```

3) Add the following lines to your Podfile:

   ```
   pod 'PingDeviceProfile'
   ```

4) Run the following command to install pods:

   ```
   pod install
   ```

## Step 2. Declaring permissions

The Device Profile module respects the iOS permissions model, and certain collectors require that you declare the permissions needed.

To declare the permissions the app might request from the user:

1. Right-click the project's `info.plist` file, and select **Open As** > **Source Code**.

   Xcode displays the contents of the plist file as XML, ready for editing.

2. Add the following properties as a child of the top-level `<dict>` element:

   ```xml
   <key>NSLocationWhenInUseUsageDescription</key>
   <string>This app needs location access to enhance security and provide personalized experiences.</string>
   <key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
   <string>This app needs location access to enhance security and provide personalized experiences.</string>
   <key>NSBluetoothAlwaysUsageDescription</key>
   <string>This app uses BLE to collect device information</string>
   ```

   |   |                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------- |
   |   | The `LocationCollector` automatically requests the relevant permission when gathering the data if needed. |

3. Save your changes.

## Step 3. Collecting device profiles

To create a device profile, create a list of the collectors you want to use, or specify `DefaultDeviceCollector.defaultDeviceCollectors()` to use the default list, and then call the `collect()` method to create the device profile JSON:

Obtaining a device profile on an iOS device

```swift
import DeviceProfile

func collectDeviceProfile() async {
    // Initialize collectors with default set
    let collectors = DefaultDeviceCollector.defaultDeviceCollectors()

    // Or manually select specific collectors
    let customCollectors: [any DeviceCollector] = [
        PlatformCollector(),
        HardwareCollector(),
        NetworkCollector(),
        TelephonyCollector(),
        BrowserCollector(),
        BluetoothCollector()
        // LocationCollector() // Add separately if needed
    ]

    do {
        // Collect device information
        let deviceProfile = try await collectors.collect()

        // Use the collected profile (Dictionary)
        print("Device Profile: \(deviceProfile)")
    } catch {
        print("Collection failed: \(error)")
    }
}
```

The **device-profile** module provides the following collectors:

**Included device profile collectors**

| Collector            | Attributes collected                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PlatformCollector`  | Gathers platform and device identification information, such as the brand and model.Example data returned by the `PlatformCollector````json
{
   "platform": {
      "platform": "iOS",
      "version": "17.0.1",
      "device": "iPhone",
      "deviceName": "Babs' iPhone",
      "model": "iPhone15,2",
      "brand": "Apple",
      "locale": "en",
      "timeZone": "America/New_York",
      "jailBreakScore": 0.0
   }
}
```                                                        |
| `HardwareCollector`  | Gathers information about the hardware, such as the CPU and display.Example data returned by the `HardwareCollector````json
{
   "hardware": {
      "manufacturer": "Apple",
      "memory": 6144,
      "cpu": 6,
      "display": {
         "width": 393,
         "height": 852,
         "orientation": 1
      },
      "camera": {
         "numberOfCameras": 3
      }
   }
}
```                                                                                                     |
| `NetworkCollector`   | Whether the device has any network connectivity.Example data returned by the `NetworkCollector````json
{
   "network": {
      "connected": true
   }
}
```                                                                                                                                                                                                                                                                                                                                     |
| `TelephonyCollector` | Collects information about the carriers the device uses, such as the carrier name and the country code.Example data returned by the `TelephonyCollector````json
{
   "telephony": {
      "networkCountryIso": "US",
      "carrierName": "Verizon"
   }
}
```                                                                                                                                                                                                                                  |
| `LocationCollector`  | Collects latitude and longitude coordinates from the device.- Automatically requests permissions when needed

- Handles both "when in use" and "always" authorization types

- Gracefully handles permission denials

- Includes intelligent caching, with 5-second validity

- Returns `null` if a location is unavailable or permission is deniedExample data returned by the `LocationCollector````json
{
   "location": {
      "latitude": 37.2431,
      "longitude": 115.7930
   }
}
``` |
| `BluetoothCollector` | Whether the device has any bluetooth support.Example data returned by the `BluetoothCollector````json
{
    "bluetooth": {
        "supported": true
    }
}
```                                                                                                                                                                                                                                                                                                                                |
| `BrowserCollector`   | Collects the user-agent string of the default browser on the device.Example data returned by the `BrowserCollector````json
{
   "browser": {
      "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15..."
   }
}
```                                                                                                                                                                                                                                     |

### Integrating with SwiftUI

The following example demonstrates how to integrate collection of a device profile with SwiftUI:

Integrating profile collection with SwiftUI

```swift
import SwiftUI
import DeviceProfile

struct ContentView: View {
    @State private var deviceProfile: [String: Any] = [:]
    @State private var isCollecting = false

    var body: some View {
        VStack {
            if isCollecting {
                ProgressView("Collecting device information…​")
            } else {
                Button("Collect Device Profile") {
                    Task {
                        await collectProfile()
                    }
                }
            }
        }
    }

    private func collectProfile() async {
        isCollecting = true
        defer { isCollecting = false }

        let collectors = DefaultDeviceCollector.defaultDeviceCollectors()

        do {
            deviceProfile = try await collectors.collect()
        } catch {
            print("Collection error: \(error)")
        }
    }
}
```

## Creating custom collectors

You can create custom device collectors to gather specific attributes, depending on your requirements or the hardware you will support.

Use the `DeviceCollector` protocol to create your custom collector:

Using `DeviceCollector` protocol to create a custom collector

```swift
struct BatteryCollector: DeviceCollector {
    typealias DataType = BatteryInfo

    let key = "battery"

    func collect() async throws -> BatteryInfo? {
        return BatteryInfo(
            level: UIDevice.current.batteryLevel,
            state: UIDevice.current.batteryState.rawValue
        )
    }
}

struct BatteryInfo: Codable {
    let level: Float
    let state: Int
}
```

## Integrating with Advanced Identity Cloud and PingAM journeys

You can use the Device Profile module to collect the data the [**Device Profile Collector node**](https://docs.pingidentity.com/auth-node-ref/latest/device-profile-collector.html) requires when used as part of a Advanced Identity Cloud or PingAM auth journey.

The Device Profile module provides the `DeviceProfileCallback` class. The class includes a `collect()` method, which collects the data and formats it ready for return to the server.

Preparing a device profile for the Device Profile Collector node

```swift
let result = await deviceProfileCallback.collect { config in
    // Configure custom collectors for enhanced AIC risk assessment
    config.collectors {
        return [
            PlatformCollector(),
            HardwareCollector(),
            NetworkCollector(),
            BrowserCollector(),
            BluetoothCollector(),
            SecurityCollector() // Custom collector
        ]
    }
}

// Handle the result
result
    .onSuccess { profile in
        // Device profile collected, submit to AIC service
        print("Profile collected successfully")
        node.next()
    }
    .onFailure { error in
        print("Collection failed: \(error)")
    }
```

The module formats the resulting device profile for consumption by the Device Profile Collector node, and includes a device identifier:

Example device profile for the Device Profile Collector node

```json
{
  "identifier": "unique-device-id",
  "metadata": {
    "platform": {
      "platform": "iOS",
      "version": "17.0.1",
      "device": "iPhone"
    },
    "hardware": {
      "manufacturer": "Apple",
      "memory": 6144,
      "cpu": 6
    },
    "network": {
      "connected": true
    }
  },
  "location": {
    "latitude": 37.2431,
    "longitude": 115.7930
  }
}
```

The **Device Profile** module automatically uses the **Device ID** module to generate this identifier, but you can customize how it's generated:

Customizing the device identifier on iOS

```swift
import PingDeviceId

// Define custom device identifier config:
let identifierConfig = DeviceIdentifierConfiguration(
    keychainAccount: "com.mycompany.myapp.deviceid",
    useEncryption: true,
    keySize: 2048
)

let customDeviceIdentifier = try? DefaultDeviceIdentifier(configuration: identifierConfig)

let result = await deviceProfileCallback.collect { @Sendable config in
  // Use custom identifier in the device profile
  config.deviceIdentifier = customDeviceIdentifier
}

// Handle the result
result
  .onSuccess { profile in
      // Device profile collected, submit to server
      print("Profile collected successfully")
      node.next()
  }
  .onFailure { error in
      print("Collection failed: \(error)")
  }
```

Learn more about customizing the device identifier in [Customizing device identifiers on iOS](ios-device-ids.html).

---

---
title: Collecting device profiles in React Native apps
description: Collect device profile data in React Native apps using rn-device-profile and integrate with PingOne Advanced Identity Cloud and PingAM journeys
component: orchsdks
page_id: orchsdks:journey:use-cases/device-profiling/react-native-device-profile
canonical_url: https://developer.pingidentity.com/orchsdks/journey/use-cases/device-profiling/react-native-device-profile.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 29 Oct 2025 14:22:33 +0100
keywords: ["Device", "Hardware", "Source Code", "Integration", "SDK", "React Native"]
section_ids:
  step_1_installing_the_module: Step 1. Installing the module
  native_module_setup: Native module setup
  step_2_declaring_permissions: Step 2. Declaring permissions
  ios: iOS
  android: Android
  step_3_collecting_device_profiles: Step 3. Collecting device profiles
  available_collectors: Available collectors
  recommended_collector_sets: Recommended collector sets
  step_4_integrating_with_advanced_identity_cloud_and_pingam_journeys: Step 4. Integrating with Advanced Identity Cloud and PingAM journeys
  the_journey_profile_payload: The journey profile payload
---

# Collecting device profiles in React Native apps

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: react, set=fab]React Native

This page guides you through collecting device profile data in a React Native application using `@ping-identity/rn-device-profile`.

It includes preconfigured collectors to collect attributes, and allows you to select which collectors to use to suit your requirements.

## Step 1. Installing the module

To install the module into your React Native project, use `yarn` or `npm` as follows:

* yarn

* npm

```shell
yarn add @ping-identity/rn-device-profile
```

```shell
npm install @ping-identity/rn-device-profile
```

For Journey-integrated collection, also install the Journey module if you have not already done so:

* yarn

* npm

```shell
yarn add @ping-identity/rn-journey
```

```shell
npm install @ping-identity/rn-journey
```

After installation, import the functions you need:

Importing device profile functions

```typescript
import {
  collectDeviceProfile,
  collectDeviceProfileForJourney,
} from '@ping-identity/rn-device-profile';
import type { DeviceProfileCollector } from '@ping-identity/rn-device-profile';
```

### Native module setup

`@ping-identity/rn-device-profile` is a TurboModule package. On React Native 0.80.1+ with the new architecture enabled, linking is automatic. On older projects using the legacy bridge, run:

```shell
npx pod-install     # iOS
```

No additional `android/` configuration is required.

## Step 2. Declaring permissions

Some collectors require platform permissions. Add the necessary declarations to your project before enabling those collectors.

### iOS

Open `ios/<AppName>/Info.plist` as source code and add the following entries as children of the top-level `<dict>` element:

Adding iOS permission entries to Info.plist

```xml
<!-- Required for LocationCollector -->
<key>NSLocationWhenInUseUsageDescription</key>
<string>This app needs location access to enhance security and provide personalised experiences.</string>
<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>This app needs location access to enhance security and provide personalised experiences.</string>

<!-- Required for BluetoothCollector -->
<key>NSBluetoothAlwaysUsageDescription</key>
<string>This app uses Bluetooth to collect device information.</string>
```

### Android

Open `android/app/src/main/AndroidManifest.xml` and add the following `<uses-permission>` entries inside `<manifest>`:

Adding Android permission entries to AndroidManifest.xml

```xml
<!-- Required for LocationCollector -->
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />

<!-- Required for BluetoothCollector (Android 12+) -->
<uses-permission android:name="android.permission.BLUETOOTH_SCAN"
    android:usesPermissionFlags="neverForLocation" />
<uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />

<!-- For Android 11 and earlier -->
<uses-permission android:name="android.permission.BLUETOOTH" />
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For `LocationCollector` and `BluetoothCollector`, you must also request the runtime permission in JavaScript before calling the collector. The SDK does not request permissions automatically on Android. Use React Native's `PermissionsAndroid` API or a library such as `react-native-permissions` to request them at an appropriate point in your UX flow\.On iOS, `LocationCollector` requests the permission automatically when the data is first gathered. |

## Step 3. Collecting device profiles

Call `collectDeviceProfile()` with an array of collector names to gather device attributes:

Collecting a device profile with selected collectors

```typescript
import { collectDeviceProfile } from '@ping-identity/rn-device-profile';
import { logger } from '@ping-identity/rn-logger';

const profileLogger = logger({ level: 'debug' });

const profile = await collectDeviceProfile(
['platform', 'hardware', 'network'],
// Add optional logger
{ logger: profileLogger },
);

// Output collected profile JSON
console.log(JSON.stringify(profile, null, 2));
```

The function returns a plain JavaScript object containing the merged output of all requested collectors. Collectors that fail are omitted from the result without throwing an error.

### Available collectors

| Collector value | Collector output                                                                                                                                                                                                                                                                  |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `'platform'`    | ```json
{
  "platform": {
    "platform": "iOS",
    "version": "17.0.1",
    "device": "iPhone",
    "deviceName": "Jane's iPhone",
    "model": "iPhone15,2",
    "brand": "Apple",
    "locale": "en",
    "timeZone": "America/New_York",
    "jailBreakScore": 0.0
  }
}
``` |
| `'hardware'`    | ```json
{
  "hardware": {
    "manufacturer": "Apple",
    "memory": 6144,
    "cpu": 6,
    "display": {
      "width": 393,
      "height": 852,
      "orientation": 1
    },
    "camera": {
      "numberOfCameras": 3
    }
  }
}
```                                       |
| `'network'`     | ```json
{
  "network": {
    "connected": true
  }
}
```                                                                                                                                                                                                                          |
| `'telephony'`   | ```json
{
  "telephony": {
    "networkCountryIso": "US",
    "carrierName": "Verizon"
  }
}
```                                                                                                                                                                                  |
| `'browser'`     | ```json
{
  "browser": {
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15..."
  }
}
```                                                                                                                                              |
| `'bluetooth'`   | ```json
{
  "bluetooth": {
    "supported": true
  }
}
```                                                                                                                                                                                                                        |
| `'location'`    | ```json
{
  "location": {
    "latitude": 37.2431,
    "longitude": 115.7930
  }
}
```                                                                                                                                                                                            |

### Recommended collector sets

For most applications, `platform`, `hardware`, and `network` provide a solid baseline signal without requiring any runtime permissions:

```typescript
const profile = await collectDeviceProfile(['platform', 'hardware', 'network']);
```

## Step 4. Integrating with Advanced Identity Cloud and PingAM journeys

When a journey reaches a **Device Profile Collector** node, the SDK receives a `DeviceProfileCallback`.

Call `collectDeviceProfileForJourney()` to collect the device signals and write them into the active journey callback, then call `actions.next()` to advance the node. `DeviceProfileJourneyResult` is an imported type that represents the resolved value from a device profile collection step inside a journey:

Handling a DeviceProfileCallback in a journey node

```typescript
import { collectDeviceProfileForJourney } from '@ping-identity/rn-device-profile';
import { collectDeviceProfileForJourney } from '@ping-identity/rn-device-profile';
import type { DeviceProfileJourneyResult } from '@ping-identity/rn-device-profile';
import { useJourney, useJourneyForm } from '@ping-identity/rn-journey';
import type { JourneyClient } from '@ping-identity/rn-journey';

function useDeviceProfileNode(journeyClient: JourneyClient) {
  const [node, actions] = useJourney(journeyClient);
  const form = useJourneyForm(node);

  const submit = async (): Promise<void> => {
    const hasDeviceProfile = form.fields.some(
      (f) => f.ref.type === 'DeviceProfileCallback',
    );

    if (!hasDeviceProfile) return;

    const result: DeviceProfileJourneyResult =
      await collectDeviceProfileForJourney(journeyClient, [
        'platform',
        'hardware',
        'network',
      ]);

    if (result.type === 'success') {
      await actions.next();
    }
  };
```

|   |                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Call `collectDeviceProfileForJourney` once per node. It inspects the active node from the journey client automatically. You do not need to pass individual callback references or indexes. |

### The journey profile payload

The profile written to the journey callback includes a device identifier generated by the native platform, the collector output, and any location data. The server-side Device Profile Collector node uses the `identifier` field to correlate the submission with a known device:

Example journey profile payload

```json
{
  "identifier": "a3f8d2...",
  "metadata": {
    "platform": {
      "platform": "iOS",
      "version": "17.0.1",
      "device": "iPhone"
    },
    "hardware": {
      "manufacturer": "Apple",
      "memory": 6144,
      "cpu": 6
    },
    "network": {
      "connected": true
    }
  },
  "location": {
    "latitude": 37.2431,
    "longitude": 115.7930
  }
}
```

For details on how the device identifier is generated and how to customize it, see [Customizing device identifiers in React Native apps](react-native-device-ids.html).

---

---
title: Compatibility
description: Find supported server versions for PingOne Advanced Identity Cloud and PingAM, and view supported operating systems and browsers for the Journey module across all platforms
component: orchsdks
page_id: orchsdks:journey:compatibility
canonical_url: https://developer.pingidentity.com/orchsdks/journey/compatibility.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 20 May 2023 16:11:17 +0100
keywords: ["Compatibility", "Features", "Source Code", "SDK"]
section_ids:
  supported-servers: Supported server versions
  supported-os: Supported operating systems and browsers
  webviews_unsupported_journey: JavaScript Compatibility with WebViews
  supported-journey-fields: Supported Nodes and Callbacks
  supported_authentication_journey_callbacks: Supported authentication journey callbacks
---

# Compatibility

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: android, set=fab]Android [icon: apple, set=fab]iOS [icon: js, set=fab]JavaScript [icon: react, set=fab]React Native

## Supported server versions

The **Journey** module is compatible with the following servers:

* PingOne Advanced Identity Cloud

  Current version.

* PingAM

  Currently supported versions.

  For information on supported PingAM versions, visit the [Ping Identity End of Life (EOL) Software Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pam).

## Supported operating systems and browsers

Select a platform below to view the supported operating systems and browsers.

* Android

* iOS

* JavaScript / Login Widget

* React Native

The Orchestration SDK for Android supports the following versions of the Android operating system:

**Supported Android versions and original release dates**

| Release    | API Levels | Released        |
| ---------- | ---------- | --------------- |
| Android 16 | 36         | August, 2025    |
| Android 15 | 35         | September, 2024 |
| Android 14 | 34         | October, 2023   |
| Android 13 | 33         | March, 2022     |
| Android 12 | 31, 32     | October, 2021   |
| Android 11 | 30         | September, 2020 |
| Android 10 | 29         | September, 2019 |

|   |                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | We have updated how we determine which Android versions form our support policy for the Orchestration SDK for Android.The support policy is as follows:- Every public major release of Android within the last 6 years.

  For example, this would mean support for **Android 10** and later versions. |

**Supported browsers on Android**

* Chrome - Two most recent major versions.

The Orchestration SDK for iOS supports the following versions of the iOS operating system:

**Supported iOS versions and original release dates**

| Release | Released        |
| ------- | --------------- |
| iOS 26  | September, 2025 |
| iOS 18  | September, 2024 |
| iOS 17  | September, 2023 |
| iOS 16  | September, 2022 |

|   |                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | We have updated how we determine which iOS versions form our support policy for the Orchestration SDK for iOS.The support policy is as follows:- Every public major release of iOS within the last 3 years.

  For example, this would mean support for **iOS 16** and later versions. |

**Supported browsers on iOS**

* Safari - Two most recent major versions.

The Orchestration SDK for JavaScript, and the Advanced Identity Cloud/PingAM Login Widget support the [desktop](#js-desktop-browsers) and [mobile](#js-desktop-browsers) browsers listed below.

**Minimum supported Desktop browser versions**

* Chrome 83

* Firefox 77

* Safari 13

* Microsoft Edge 83 (Chromium)

**Supported Mobile browsers**

* iOS (Safari) - Two most recent major versions of the operating system.

* Android (Chrome) - Two most recent major versions of the operating system.

The Orchestration SDK for React Native requires React Native 0.80.1 or later and supports both the New Architecture and the legacy bridge.

**Android**

**Supported Android versions and original release dates**

| Release    | API Levels | Released        |
| ---------- | ---------- | --------------- |
| Android 16 | 36         | August, 2025    |
| Android 15 | 35         | September, 2024 |
| Android 14 | 34         | October, 2023   |
| Android 13 | 33         | March, 2022     |
| Android 12 | 31, 32     | October, 2021   |
| Android 11 | 30         | September, 2020 |
| Android 10 | 29         | September, 2019 |

**iOS**

**Supported iOS versions and original release dates**

| Release | Released        |
| ------- | --------------- |
| iOS 26  | September, 2025 |
| iOS 18  | September, 2024 |
| iOS 17  | September, 2023 |
| iOS 16  | September, 2022 |

### JavaScript Compatibility with WebViews

A WebView allows you to embed a web browser into your native Android or iOS application to display HTML pages, and run JavaScript apps.

For example, the Android system WebView is based on the Google Chrome engine, and the iOS WebView is based on the Safari browser engine.

However, it is important to note that WebViews do not implement the full feature set of their respective browsers. For example, some of the browser-provided APIs that the Orchestration SDK for JavaScript requires are not available in a WebView, such as the WebAuthn APIs.

In addition, there are concerns that a WebView does not provide the same level of security as their full browser counterparts.

As the SDK requires full, spec-compliant, browser-supplied APIs for full functionality we **do not** support usage within a WebView.

We also do not support or test usage with any wrappers around WebViews.

Whilst you might be able to implement simple use-cases using the Orchestration SDK for JavaScript within a WebView, we recommend that you use an alternative such as opening a full browser, or using an in-app instance of a full browser such as [Custom Tabs](https://developer.android.com/develop/ui/views/layout/webapps/overview-of-android-custom-tabs) for Android or [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller) for iOS.

## Supported Nodes and Callbacks

The Journey modules support the following nodes and callbacks:

## Supported authentication journey callbacks

The Orchestration SDKs support the following authentication journey callbacks when using the following servers:

* PingOne Advanced Identity Cloud

* PingAM

| Callback name                                 | Callback description                                                                                                                                                                                               | Android                                          | iOS                        | JavaScript                 | React Native               |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ | -------------------------- | -------------------------- | -------------------------- |
| `BooleanAttributeInputCallback`               | Collects true or false.                                                                                                                                                                                            | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `ChoiceCallback`                              | Collects single user input from available choices, retrieves selected choice from user interaction.                                                                                                                | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `ConfirmationCallback`                        | Retrieve a selected option from a list of options.                                                                                                                                                                 | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `ConsentMappingCallback`                      | Prompts the user to consent to share their profile data.                                                                                                                                                           | [icon: check, set=fas] Yes                       | [icon: x, set=fas] No      | [icon: x, set=fas] No      | [icon: check, set=fas] Yes |
| `DeviceBindingCallback`                       | Cryptographically bind a mobile device to a user account.                                                                                                                                                          | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: x, set=fas] No      | [icon: check, set=fas] Yes |
| `DeviceProfileCallback`                       | Collects meta and/or location data about the authenticating device.                                                                                                                                                | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `DeviceSigningVerifierCallback`               | Verify ownership of a bound device by signing a challenge.                                                                                                                                                         | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: x, set=fas] No      | [icon: check, set=fas] Yes |
| `HiddenValueCallback`                         | Returns form values that are not visually rendered to the end user.                                                                                                                                                | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `IdPCallback`                                 | Provides the information required for connecting to an identity provider (IDP) for social sign-on.                                                                                                                 | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `KbaCreateCallback`                           | Collects knowledge-based answers. For example, the name of your first pet.                                                                                                                                         | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `MetadataCallback` [(1)](#webauthn-callback)  | Injects key-value metadata into the authentication process.For example, the [WebAuthn](#webauthn-callback) nodes use this callback to return the data the SDK requires to perform authentication and registration. | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `NameCallback`                                | Collects a username.                                                                                                                                                                                               | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `NumberAttributeInputCallback`                | Collects a number.                                                                                                                                                                                                 | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `PasswordCallback`                            | Collects a password or one-time pass code.                                                                                                                                                                         | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `PingOneProtectEvaluationCallback`            | Collects captured contextual data from the client to perform risk evaluations.                                                                                                                                     | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: x, set=fas] No      |
| `PingOneProtectInitializeCallback`            | Instructs the client to start capturing contextual data for risk evaluations                                                                                                                                       | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: x, set=fas] No      |
| `PollingWaitCallback`                         | Instructs the client to wait for the given period and resubmit the request.                                                                                                                                        | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `ReCaptchaCallback`                           | Provides data required to use a CAPTCHA in your apps.                                                                                                                                                              | [icon: check, set=fas] Yes [(2)](#play-services) | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: x, set=fas] No      |
| `ReCaptchaEnterpriseCallback`                 | Provides data required to use reCAPTCHA Enterprise in your apps.                                                                                                                                                   | [icon: check, set=fas] Yes [(2)](#play-services) | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: x, set=fas] No      |
| `RedirectCallback`                            | Redirects the user's browser or user-agent.                                                                                                                                                                        | [icon: x, set=fas] No                            | [icon: x, set=fas] No      | [icon: check, set=fas] Yes | [icon: x, set=fas] No      |
| `SelectIdPCallback`                           | Provides a list of identity providers (IDPs) users can choose from to perform social sign-on.                                                                                                                      | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `StringAttributeInputCallback`                | Collects the values of attributes for use elsewhere in a tree.                                                                                                                                                     | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `SuspendedTextOutputCallback`                 | Pause and resume authentication, sometimes known as "magic links".                                                                                                                                                 | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `TermsAndConditionsCallback`                  | Collects a user's acceptance of the configured Terms & Conditions.                                                                                                                                                 | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `TextInputCallback`                           | Collects text input from the end user. For example, a nickname for their account.                                                                                                                                  | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `TextOutputCallback`                          | Provides a message to be displayed to a user with a given message type.                                                                                                                                            | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `TextOutputCallback`*(`messageType` === `4`)* | Some nodes use the `TextOutputCallback` callback to include JavaScript that is intended to be run on the client.In this case the `mesageType` property equals `4`.                                                 | [icon: x, set=fas] No                            | [icon: x, set=fas] No      | [icon: check, set=fas] Yes | [icon: x, set=fas] No      |
| `ValidatedCreatePasswordCallback`             | Collects a password value with optional password policy validation.                                                                                                                                                | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |
| `ValidatedCreateUsernameCallback`             | Collects a username value with optional username policy validation.                                                                                                                                                | [icon: check, set=fas] Yes                       | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes | [icon: check, set=fas] Yes |

> **Collapse: Show the nodes that might return each callback**
>
> The table below lists the nodes that might return supported callbacks.
>
> The actual callbacks a node returns depends on its configuration. It might not return all the callbacks listed in this table.
>
> | Callback                                | Auth nodes that might return callback                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> | `BooleanAttributeInputCallback`         | * [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
> | `ChoiceCallback`                        | - [Choice Collector node](https://docs.pingidentity.com/auth-node-ref/latest/choice-collector.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | `ConfirmationCallback`                  | * [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ldap-decision.html)
>
> * [Message node](https://docs.pingidentity.com/auth-node-ref/latest/message.html)
>
> * [MFA Registration Options node](https://docs.pingidentity.com/auth-node-ref/latest/mfa-registration-options.html)
>
> * [OATH Token Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/oath-token-verifier.html)
>
> * [Polling Wait node](https://docs.pingidentity.com/auth-node-ref/latest/polling-wait.html)
>
> * [Push Wait node](https://docs.pingidentity.com/auth-node-ref/latest/push-wait.html)
>
> * [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html)
>
> * [OATH Registration node](https://docs.pingidentity.com/auth-node-ref/latest/oath-registration.html) |
> | `ConsentMappingCallback`                | - [Consent Collector node](https://docs.pingidentity.com/auth-node-ref/latest/consent-collector.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | `DeviceBindingCallback`                 | * [Device Binding node](https://docs.pingidentity.com/auth-node-ref/latest/device-binding.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> | `DeviceProfileCallback`                 | - [Device Profile Collector node](https://docs.pingidentity.com/auth-node-ref/latest/device-profile-collector.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | `DeviceSigningVerifierCallback`         | * [Device Signing Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/device-signing-verifier.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
> | `HiddenValueCallback`                   | - [Amster Jwt Decision node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/amster-jwt-decision.html)
>
> - [Push Wait node](https://docs.pingidentity.com/auth-node-ref/latest/push-wait.html)
>
> - [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html)
>
> - [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html)                                                                                                                                                                                                                                                                                                                                                                                     |
> | `IdPCallback`                           | * [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
> | `KbaCreateCallback`                     | - [KBA Definition node](https://docs.pingidentity.com/auth-node-ref/latest/kba-definition.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> | `MetaDataCallback`                      | * [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html)
>
> * [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
> | `NameCallback`                          | - [Username Collector node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/username-collector.html)
>
> - [Datastore Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html)
>
> - [OATH Token Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/oath-token-verifier.html)
>
> - [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)
>
> - [Configuration Provider node](https://docs.pingidentity.com/auth-node-ref/latest/config-provider.html)                                                                                                                                                                                                                                                                          |
> | `NumberAttributeInputCallback`          | * [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
> | `PasswordCallback`                      | - [Create Password node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/create-password.html)
>
> - [Password Collector node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/password-collector.html)
>
> - [Datastore Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html)
>
> - [KBA Verification node](https://docs.pingidentity.com/auth-node-ref/latest/kba-verification.html)
>
> - [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ldap-decision.html)
>
> - [One-time Password Collector Decision node](https://docs.pingidentity.com/auth-node-ref/latest/otp-collector-decision.html)
>
> - [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)                                                 |
> | `PingOneProtectEvaluationCallback`      | * [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> | `PingOneProtectInitializeCallback`      | - [PingOne Protect Initialization node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | `PollingWaitCallback`                   | * [Combined MFA Registration node](https://docs.pingidentity.com/auth-node-ref/latest/combined-mfa-registration.html)
>
> * [Push Registration node](https://docs.pingidentity.com/auth-node-ref/latest/push-registration.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
> | `ReCaptchaCallback`                     | - [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/latest/captcha.html)
>
> - [Legacy CAPTCHA node (deprecated)](https://docs.pingidentity.com/auth-node-ref/latest/legacy-captcha.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> | `ReCaptchaEnterpriseCallback`           | * [reCAPTCHA Enterprise node](https://docs.pingidentity.com/auth-node-ref/latest/recaptcha-enterprise.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | `RedirectCallback`                      | - [Provision IDM Account node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/provision-IDM-account.html)
>
> - [Identity Assertion node](https://docs.pingidentity.com/auth-node-ref/latest/identity-assertion-node.html)
>
> - [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
> | `SelectIdPCallback`                     | * [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/latest/select-identity-provider.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | `StringAttributeInputCallback`          | - [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
> | `SuspendedTextOutputCallback`           | * [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/latest/email-suspend.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
> | `TermsAndConditionsCallback`            | - [Accept Terms and Conditions node](https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
> | `TextInputCallback`                     | * [Configuration Provider node](https://docs.pingidentity.com/auth-node-ref/latest/config-provider.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
> | `TextOutputCallback`                    | - [Create Password node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/create-password.html)
>
> - [Display Username node](https://docs.pingidentity.com/auth-node-ref/latest/display-username.html)
>
> - [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ldap-decision.html)
>
> - [Message node](https://docs.pingidentity.com/auth-node-ref/latest/message.html)
>
> - [MFA Registration Options node](https://docs.pingidentity.com/auth-node-ref/latest/mfa-registration-options.html)                                                                                                                                                                                                                                                                                                          |
> | `TextOutputCallback (messageType == 4)` | * [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html)
>
> * [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
> | `ValidatedPasswordCallback`             | - [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | `ValidatedUsernameCallback`             | * [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

> **Collapse: Show the callbacks each node might return**
>
> The table below lists the supported callbacks that a node might return.
>
> The actual callbacks a node returns depends on its configuration. It might not return all the callbacks listed in this table.
>
> |                                                                                                                                   |                                                                                                      |
> | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
> | Auth node                                                                                                                         | Callbacks the node might return                                                                      |
> | [Accept Terms and Conditions node](https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html)           | `TermsAndConditionsCallback`                                                                         |
> | [Amster Jwt Decision node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/amster-jwt-decision.html)                   | `HiddenValueCallback`                                                                                |
> | [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html)                           | `BooleanAttributeInputCallback``NumberAttributeInputCallback``StringAttributeInputCallback`          |
> | [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/latest/captcha.html)                                                   | `ReCaptchaCallback`                                                                                  |
> | [Choice Collector node](https://docs.pingidentity.com/auth-node-ref/latest/choice-collector.html)                                 | `ChoiceCallback`                                                                                     |
> | [Combined MFA Registration node](https://docs.pingidentity.com/auth-node-ref/latest/combined-mfa-registration.html)               | `PollingWaitCallback`                                                                                |
> | [Configuration Provider node](https://docs.pingidentity.com/auth-node-ref/latest/config-provider.html)                            | `NameCallback``TextInputCallback`                                                                    |
> | [Consent Collector node](https://docs.pingidentity.com/auth-node-ref/latest/consent-collector.html)                               | `ConsentMappingCallback`                                                                             |
> | [Create Password node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/create-password.html)                           | `PasswordCallback``TextOutputCallback`                                                               |
> | [Datastore Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html)                            | `NameCallback``PasswordCallback`                                                                     |
> | [Device Binding node](https://docs.pingidentity.com/auth-node-ref/latest/device-binding.html)                                     | `DeviceBindingCallback`                                                                              |
> | [Device Profile Collector node](https://docs.pingidentity.com/auth-node-ref/latest/device-profile-collector.html)                 | `DeviceProfileCallback`                                                                              |
> | [Device Signing Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/device-signing-verifier.html)                   | `DeviceSigningVerifierCallback`                                                                      |
> | [Display Username node](https://docs.pingidentity.com/auth-node-ref/latest/display-username.html)                                 | `TextOutputCallback`                                                                                 |
> | [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/latest/email-suspend.html)                                       | `SuspendedTextOutputCallback`                                                                        |
> | [Identity Assertion node](https://docs.pingidentity.com/auth-node-ref/latest/identity-assertion-node.html)                        | `RedirectCallback`                                                                                   |
> | [KBA Definition node](https://docs.pingidentity.com/auth-node-ref/latest/kba-definition.html)                                     | `KbaCreateCallback`                                                                                  |
> | [KBA Verification node](https://docs.pingidentity.com/auth-node-ref/latest/kba-verification.html)                                 | `PasswordCallback`                                                                                   |
> | [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ldap-decision.html)                                       | `ConfirmationCallback``PasswordCallback``TextOutputCallback`                                         |
> | [Legacy CAPTCHA node (deprecated)](https://docs.pingidentity.com/auth-node-ref/latest/legacy-captcha.html)                        | `ReCaptchaCallback`                                                                                  |
> | [Message node](https://docs.pingidentity.com/auth-node-ref/latest/message.html)                                                   | `ConfirmationCallback``TextOutputCallback`                                                           |
> | [MFA Registration Options node](https://docs.pingidentity.com/auth-node-ref/latest/mfa-registration-options.html)                 | `ConfirmationCallback``TextOutputCallback`                                                           |
> | [OATH Registration node](https://docs.pingidentity.com/auth-node-ref/latest/oath-registration.html)                               | `ConfirmationCallback`                                                                               |
> | [OATH Token Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/oath-token-verifier.html)                           | `ConfirmationCallback``NameCallback`                                                                 |
> | [One-time Password Collector Decision node](https://docs.pingidentity.com/auth-node-ref/latest/otp-collector-decision.html)       | `PasswordCallback`                                                                                   |
> | [Password Collector node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/password-collector.html)                     | `PasswordCallback`                                                                                   |
> | [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html)     | `PingOneProtectEvaluationCallback`                                                                   |
> | [PingOne Protect Initialization node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html) | `PingOneProtectInitializeCallback`                                                                   |
> | [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)                               | `PasswordCallback``ValidatedPasswordCallback`                                                        |
> | [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)                               | `NameCallback``ValidatedUsernameCallback`                                                            |
> | [Polling Wait node](https://docs.pingidentity.com/auth-node-ref/latest/polling-wait.html)                                         | `ConfirmationCallback`                                                                               |
> | [Provision IDM Account node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/provision-IDM-account.html)               | `RedirectCallback`                                                                                   |
> | [Push Registration node](https://docs.pingidentity.com/auth-node-ref/latest/push-registration.html)                               | `PollingWaitCallback`                                                                                |
> | [Push Wait node](https://docs.pingidentity.com/auth-node-ref/latest/push-wait.html)                                               | `ConfirmationCallback``HiddenValueCallback`                                                          |
> | [reCAPTCHA Enterprise node](https://docs.pingidentity.com/auth-node-ref/latest/recaptcha-enterprise.html)                         | `ReCaptchaEnterpriseCallback`                                                                        |
> | [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/latest/select-identity-provider.html)                 | `SelectIdPCallback`                                                                                  |
> | [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html)                   | `IdPCallback``RedirectCallback`                                                                      |
> | [Username Collector node](https://docs.pingidentity.com/auth-node-ref/latest/am-only/username-collector.html)                     | `NameCallback`                                                                                       |
> | [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html)                   | `ConfirmationCallback``HiddenValueCallback``MetaDataCallback``TextOutputCallback (messageType == 4)` |
> | [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html)                       | `HiddenValueCallback``MetaDataCallback``TextOutputCallback (messageType == 4)`                       |

(1) The [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html) and the [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html) both use a `MetaDataCallback` when the Return challenge as JavaScript is *NOT* enabled.

You must *not* enable this option when handling WebAuthn journeys with the Orchestration SDK for Android and iOS.

The Orchestration SDK for JavaScript handles either the `MetaDataCallback` or the JavaScript-based payload.

(2) Requires the presence of [Google Play Services](https://developers.google.com/android/guides/overview).

---

---
title: Configure a JavaScript app for social sign-on
description: Configure a JavaScript app to perform social sign-on with an external identity provider using PingOne Advanced Identity Cloud or PingAM
component: orchsdks
page_id: orchsdks:journey:use-cases/external-idp/javascript/index
canonical_url: https://developer.pingidentity.com/orchsdks/journey/use-cases/external-idp/javascript/index.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 25 Mar 2025 11:00:37 +0100
keywords: ["DaVinci", "Flows", "Tutorial", "Source Code", "Integration", "SDK", "Android"]
section_ids:
  before_you_begin: Before you begin
  step_1_adding_core_dependencies: Step 1. Adding core dependencies
  step_2_authenticating_with_external_idps: Step 2. Authenticating with external IdPs
---

# Configure a JavaScript app for social sign-on

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: js, set=fab]JavaScript

Complete the following high-level tasks to configure a JavaScript client app to perform social sign-on with an external identity provider (IdP):

## [Before you begin](../before-you-begin.html)

Ensure that you have completed the prerequisites before starting the numbered steps on this page below.

You need to have configured Apple, Facebook, and Google as external identity providers in PingOne Advanced Identity Cloud or PingAM, and set up the social authentication journeys your client app will step through.

[**Complete prerequisites**[icon: chevrons-right, set=fas, size=xs]](../before-you-begin.html)

## [Step 1. Adding core dependencies](01_adding_core_dependencies.html)

These dependencies provide core support for social sign-on. These are the minimum required dependencies for redirecting users to the IdP for authentication.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_adding_core_dependencies.html)

## [Step 2. Authenticating with external IdPs](02_authenticate_with_external_idps.html)

Learn how to authenticate your users with the external IdPs you have configured in your authentication journeys.

[**Start step 3**[icon: chevrons-right, set=fas, size=xs]](02_authenticate_with_external_idps.html)

---

---
title: Configure a React Native app for OATH MFA
description: Configure OATH-based MFA in a React Native app using @ping-identity/rn-oath to manage credentials and generate HOTP and TOTP one-time passcodes
component: orchsdks
page_id: orchsdks:journey:use-cases/oath/react-native/index
canonical_url: https://developer.pingidentity.com/orchsdks/journey/use-cases/oath/react-native/index.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Wed, 03 Jun 2026 11:00:37 +0100
keywords: ["Journey", "Flows", "Tutorial", "Source Code", "Integration", "SDK", "React Native"]
section_ids:
  step_1_installing_the_module: Step 1. Installing the module
  step_2_creating_the_oath_client: Step 2. Creating the OATH client
  step_3_managing_credentials: Step 3. Managing credentials
  adding_oath_credentials_from_a_uri: Adding OATH credentials from a URI
  getting_oath_credentials: Getting OATH credentials
  updating_oath_credentials: Updating OATH credentials
  deleting_oath_credentials: Deleting OATH credentials
  step_4_generating_oath_based_one_time_passcodes: Step 4. Generating OATH-based one-time passcodes
  generating_hotp_codes: Generating HOTP codes
  generating_totp_codes: Generating TOTP codes
  step_5_handling_errors: Step 5. Handling errors
  error_codes: Error codes
  step_6_closing_the_oath_client: Step 6. Closing the OATH client
  health-check-policies: Enabling OATH device health check policies
  handling_device_health_check_policy_violations: Handling device health check policy violations
---

# Configure a React Native app for OATH MFA

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: react, set=fab]React Native

This page guides you through configuring OATH-based multi-factor authentication (MFA) in a React Native application using `@ping-identity/rn-oath`.

## Step 1. Installing the module

To install the module into your React Native project, use `yarn` or `npm` as follows:

* yarn

* npm

```shell
yarn add @ping-identity/rn-oath
```

```shell
npm install @ping-identity/rn-oath
```

After installation, import the functions you might need:

Importing the OATH module

```typescript
import {
  createOathClient,
  configureOathPolicyEvaluator,
  OathError,
} from '@ping-identity/rn-oath';
import type {
  OathClient,
  OathClientConfig,
  OathCodeInfo,
  OathCredential,
  OathMfaPolicy,
} from '@ping-identity/rn-oath';
```

## Step 2. Creating the OATH client

To use the **OATH** module you must initialize the OATH client in your application by calling the `createOathClient()` method:

Creating the OATH client

```typescript
import { createOathClient } from '@ping-identity/rn-oath';

const oathClient = await createOathClient();
```

You can customize the OATH client with a number of options:

Creating a customized OATH client

```typescript
import { createOathClient } from '@ping-identity/rn-oath';
import { logger } from '@ping-identity/rn-logger';

const oathLogger = logger({ level: 'debug' });

const oathClient = await createOathClient({
  logger: oathLogger,
  timeout: 30,
  enableCredentialCache: false,
});
```

The properties you can use to customize OATH client configuration are as follows:

| Option                  | Required | Description                                                                                                                                                                                                                                                                               |
| ----------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `logger`                | No       | A `LoggerInstance` created by `logger({ level })` from `@ping-identity/rn-logger`.Records credential operations at `debug`/`info` level and errors at `error` level.Learn more in [Configuring logging in React Native](../../../customization/logging/react-native-custom-logging.html). |
| `timeout`               | No       | Network timeout, in seconds. Must be greater than or equal to `0`.Default is `15` seconds.                                                                                                                                                                                                |
| `enableCredentialCache` | No       | Whether to cache credentials in memory for faster repeated reads.Default is `false`.                                                                                                                                                                                                      |
| `encryptionEnabled`     | No       | (iOS only) Whether to encrypt the credential store in the Keychain.Default is `true`.Do not disable in a production app.                                                                                                                                                                  |
| `storage`               | No       | An `OathStorageHandle` for custom storage. Omit to use the platform default; iOS Keychain or Android KeyStore.Learn more in [Customizing Journey module storage in React Native](../../../customization/storage/customize-react-native-storage.html).                                     |
| `policyEvaluator`       | No       | An `OathPolicyEvaluatorHandle` returned by `configureOathPolicyEvaluator()`.Enables device health check policy enforcement when generating codes.Learn more in [Enabling OATH device health check policies](#health-check-policies).                                                      |

## Step 3. Managing credentials

The **OATH** module relies on a set of credentials that you can create, retrieve, update, and delete.

Each credential contains the service and account details, and the parameters required to generate HOTP or TOTP codes.

### Adding OATH credentials from a URI

The OATH module lets the user register their device for OATH-based multi-factor authentication (MFA).

The information required to register a device is contained in a specially-encoded URI, which your client application decodes to create the credentials.

This URI is often delivered by QR codes that the client can scan, or directly in the callback output by the [OATH Registration node](https://docs.pingidentity.com/auth-node-ref/latest/oath-registration.html).

Use the `addCredentialFromUri()` method to create OATH credentials and register an MFA device:

Registering an OATH credential from a URI

```typescript
const credential = await oathClient.addCredentialFromUri(
  'otpauth://totp/Example%3Auser%40example.com?secret=JBSWY3DPEHPK3PXP&issuer=Example&algorithm=SHA1&digits=6&period=30',
);

console.log(credential.id);         // opaque stable identifier
console.log(credential.issuer);     // "Example"
console.log(credential.accountName); // "user@example.com"
console.log(credential.type);       // "TOTP"
```

The `otpauth://` URI format is `otpauth://TYPE/LABEL?PARAMETERS`

TOTP example

```none
otpauth://totp/Issuer:accountName?secret=BASE32SECRET&issuer=Issuer&algorithm=SHA1&digits=6&period=30
```

HOTP example

```none
otpauth://hotp/Issuer:accountName?secret=BASE32SECRET&issuer=Issuer&algorithm=SHA1&digits=6&counter=0
```

**OTPAUTH parameter reference**

| Parameter   | Required  | Description                                                                                                             |
| ----------- | --------- | ----------------------------------------------------------------------------------------------------------------------- |
| `secret`    | Yes       | Base32-encoded shared secret. Stored in the platform secure enclave; never accessible from JavaScript after enrollment. |
| `issuer`    | Yes       | Service name displayed to the user, for example, `Example Corp`.                                                        |
| `algorithm` | No        | The HMAC algorithm used to compute the one-time passcode.One of `SHA1` (default), `SHA256`, or `SHA512`.                |
| `digits`    | No        | Code length: `6` (default) or `8`.                                                                                      |
| `period`    | TOTP only | Code validity window, in seconds. Defaults to `30`.                                                                     |
| `counter`   | HOTP only | Starting counter value. Defaults to `0`.                                                                                |

|   |                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | `addCredentialFromUri()` throws `OathError` with code `OATH_DUPLICATE_CREDENTIAL` if a credential with the same issuer and account name already exists.Catch this case to prompt the user to replace or keep the existing credential. |

### Getting OATH credentials

Call `getCredentials()` to load all stored credentials, or `getCredential(id)` to load a single credential by its `id`:

* All credentials

* Single credential

```typescript
// All credentials
const credentials = await oathClient.getCredentials();
```

Retrieving a single OATH credential by ID

```typescript
// Single credential
const credential = await oathClient.getCredential('abc123');
if (credential === null) {
  console.log('Credential not found');
} else {
    console.log('id:', credential.id);
    console.log('deviceName:', credential.deviceName);
    console.log('uuid:', credential.uuid);
    console.log('createdDate:', credential.createdDate);
    console.log('lastAccessDate:', credential.lastAccessDate);
  }
```

### Updating OATH credentials

Use `saveCredential()` to persist changes to an existing credential. Retrieve the credential first, modify the desired fields, and save it back:

Updating an OATH credential

```typescript
const credential = await oathClient.getCredential('abc123');
if (credential) {
  const updated = await oathClient.saveCredential({
    ...credential,
    displayIssuer: 'My Company',
    displayAccountName: 'Work Account',
  });
}
```

Validation rules enforced by `saveCredential()`:

* `digits` must be `6` or `8`.

* `period` must be `> 0` for TOTP credentials.

* `counter` must be `>= 0` for HOTP credentials.

### Deleting OATH credentials

Call `deleteCredential(id)` to remove a credential and its stored secret permanently:

Deleting an OATH credential

```typescript
try {
  await oathClient.deleteCredential('abc123');
  console.log('Credential removed');
} catch (err) {
  if (err instanceof OathError) {
    if (err.code === 'OATH_CREDENTIAL_NOT_FOUND') {
      console.warn('Credential does not exist');
    } else {
      throw err;
    }
  }
}
```

## Step 4. Generating OATH-based one-time passcodes

When a journey reaches the [OATH Token Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/oath-token-verifier.html) node, it returns a `NameCallback` expecting a one-time passcode.

Generate the code from the stored credential, populate the callback, then advance the journey:

### Generating HOTP codes

HOTP codes are counter-based, so they do not expire.

A typical HOTP flow presents the user with their registered credential and a button to generate a code.

When the user taps the button, call `generateCode()` and submit the result to the journey.

Each call to `generateCode()` permanently increments the counter stored on the device. Do not call `generateCode()` until the user has confirmed they want a code, and submit it to the journey as soon as it is generated, as follows:

Generating an HOTP code and submitting it to a journey

```typescript
import { useJourney, useJourneyForm } from '@ping-identity/rn-journey';

const [node, actions] = useJourney(journeyClient);
const form = useJourneyForm(node);

const code = await oathClient.generateCode(credential.id);
form.setValueByType('NameCallback', code);

if (form.canSubmit) {
  await actions.next(form.input);
}
```

### Generating TOTP codes

For TOTP credentials, call `generateCodeWithValidity()` to get the current code along with its validity window, then submit it to the journey:

Generating a TOTP code and submitting it to a journey

```typescript
import { useJourney, useJourneyForm } from '@ping-identity/rn-journey';

const [node, actions] = useJourney(journeyClient);
const form = useJourneyForm(node);

const info = await oathClient.generateCodeWithValidity(credential.id);
form.setValueByType('NameCallback', info.code);

if (form.canSubmit) {
  await actions.next(form.input);
}
```

In addition to `info.code`, `generateCodeWithValidity()` returns timing metadata you can use to drive a countdown display:

| Field           | Type     | Description                                                                                      |
| --------------- | -------- | ------------------------------------------------------------------------------------------------ |
| `code`          | `string` | The current one-time passcode.                                                                   |
| `timeRemaining` | `number` | Seconds until the code expires.                                                                  |
| `progress`      | `number` | Fractional progress through the validity window (0.0–1.0). `0.0` when fresh, `1.0` when expired. |
| `totalPeriod`   | `number` | Total validity window in seconds.                                                                |
| `counter`       | `number` | Current HOTP counter value. `-1` for TOTP credentials.                                           |

## Step 5. Handling errors

All OATH operations throw `OathError` when something goes wrong.

Check `err instanceof OathError` to confirm the error is OATH-related, then inspect `err.code` to handle specific failure cases:

* Credential operations

* Code generation

Handling errors from credential operations

```typescript
import { OathError } from '@ping-identity/rn-oath';

try {
  const credential = await oathClient.addCredentialFromUri(uri);
} catch (err) {
  if (err instanceof OathError) {
    switch (err.code) {
      case 'OATH_DUPLICATE_CREDENTIAL':
        // Prompt the user to replace or keep the existing credential
        break;
      case 'OATH_INVALID_URI':
        // The scanned QR code is not a valid otpauth:// URI
        break;
      default:
        throw err;
    }
  }
}
```

Handling errors from code generation

```typescript
import { OathError } from '@ping-identity/rn-oath';

try {
  const info = await oathClient.generateCodeWithValidity(credential.id);
} catch (err) {
  if (err instanceof OathError) {
    switch (err.code) {
      case 'OATH_CREDENTIAL_LOCKED':
        // The credential is locked; inform the user
        break;
      case 'OATH_POLICY_VIOLATION':
        // A device health check policy blocked code generation
        break;
      default:
        throw err;
    }
  }
}
```

### Error codes

| Error code                    | Platform | Description                                                                            |
| ----------------------------- | -------- | -------------------------------------------------------------------------------------- |
| `OATH_CLEANUP_FAILED`         | iOS      | Native cleanup failed internally. Not thrown from `close()` — iOS always resolves.     |
| `OATH_CODE_GENERATION_FAILED` | Both     | The native SDK could not generate a code for this credential.                          |
| `OATH_CREDENTIAL_LOCKED`      | Both     | The credential is locked by a device policy; code generation is not allowed.           |
| `OATH_CREDENTIAL_NOT_FOUND`   | Both     | No credential with the given ID exists in the native store.                            |
| `OATH_DUPLICATE_CREDENTIAL`   | Both     | A credential with the same ID already exists in the native store.                      |
| `OATH_INITIALIZATION_FAILED`  | Both     | The native OATH session could not be created during `createOathClient`.                |
| `OATH_INVALID_PARAMETER`      | Both     | A method argument has an invalid value.                                                |
| `OATH_INVALID_URI`            | Both     | The provided `otpauth://` URI could not be parsed.                                     |
| `OATH_MISSING_PARAMETER`      | iOS      | A required method argument was not provided.                                           |
| `OATH_POLICY_VIOLATION`       | Both     | The operation was blocked by a device health check policy.                             |
| `OATH_STATE_ERROR`            | Both     | A method was called after `close()`, or the client is in an unexpected internal state. |
| `OATH_STORAGE_ACCESS_DENIED`  | iOS      | The app does not have permission to access the native credential store.                |
| `OATH_STORAGE_CORRUPTED`      | iOS      | Stored credential data is corrupted and cannot be read.                                |
| `OATH_STORAGE_FAILURE`        | Both     | The native credential store encountered an unspecified I/O error.                      |
| `OATH_UNKNOWN_ERROR`          | Both     | An unexpected error occurred that does not map to a specific code.                     |

## Step 6. Closing the OATH client

Call `close()` when the OATH client is no longer needed. This releases the native session and its associated memory:

Closing the OATH client

```typescript
try {
    // ... work with credentials
  } finally {
    await oathClient.close();
  }
```

Close the OATH client when the component is dismissed, for example in a `useEffect` cleanup function.

|   |                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Calling any method on a closed OATH client throws an `OathError` with code `OATH_STATE_ERROR`. Always check that the OATH client is still active before calling methods from asynchronous callbacks. |

## Enabling OATH device health check policies

The **OATH** module gates one-time passcode generation behind device health check policies.

When a policy is violated, calling `generateCode()` or `generateCodeWithValidity()` throws `OathError` with code `OATH_POLICY_VIOLATION` instead of returning a code.

To enable device health check policies, configure a policy evaluator before creating the OATH client:

Configuring a device health check policy evaluator

```typescript
import {
  configureOathPolicyEvaluator,
  createOathClient,
} from '@ping-identity/rn-oath';

const deviceHealthEvaluator = configureOathPolicyEvaluator({
  policies: [
    { kind: 'biometricAvailable' },
    { kind: 'deviceTampering' },
  ],
});

const oathClient = await createOathClient({
  policyEvaluator: deviceHealthEvaluator,
});
```

| Policy kind          | Description                                                                                                                                                                                                                         |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `biometricAvailable` | Code generation fails if the device has no enrolled biometrics.Enforces that the user has set up biometric authentication as a prerequisite for OATH codes.                                                                         |
| `deviceTampering`    | Code generation fails if the device's jailbreak or root score exceeds the threshold encoded in the credential's server-supplied `policies` field.The threshold is set server-side and is not a client-side configuration parameter. |

|   |                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | `configureOathPolicyEvaluator()` is synchronous and must be called before `createOathClient()`.Pass the returned `OathPolicyEvaluatorHandle` as `OathClientConfig.policyEvaluator`, as shown above. |

### Handling device health check policy violations

When a policy blocks code generation, catch `OATH_POLICY_VIOLATION` and display a contextual message:

Handling a device health check policy violation

```typescript
import { OathError } from '@ping-identity/rn-oath';

try {
  const code = await oathClient.generateCode(credential.id);
} catch (err) {
  if (err instanceof OathError) {
    if (err.code === 'OATH_POLICY_VIOLATION') {
      // Inform the user why the code cannot be generated
      setErrorMessage('This code cannot be generated on this device. Enroll biometrics or use an unmodified device.');
    } else {
      setErrorMessage(err.message);
    }
  }
}
```

---

---
title: Configure a React Native app for social sign-on
description: Configure a React Native app to authenticate users through social sign-on using an external IdP with PingOne Advanced Identity Cloud or PingAM journeys
component: orchsdks
page_id: orchsdks:journey:use-cases/external-idp/react-native/index
canonical_url: https://developer.pingidentity.com/orchsdks/journey/use-cases/external-idp/react-native/index.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 10 Jun 2026 00:00:00 +0000
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Use Case", "SDK", "IdP", "React Native"]
section_ids:
  before_you_begin: Before you begin
  step_1_adding_core_dependencies: Step 1. Adding core dependencies
  step_2_handling_uri_schemes: Step 2. Handling URI schemes
  step_3_configuring_native_provider_sdks: Step 3. Configuring native provider SDKs
  step_4_authenticating_with_external_idps: Step 4. Authenticating with external IdPs
---

# Configure a React Native app for social sign-on

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: react, set=fab]React Native

Complete the following steps to configure a React Native app to perform social sign-on with an external identity provider (IdP).

|   |                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Where a provider's native SDK is available on a platform, the **External IdP** module uses it to give users a smooth, integrated sign-in experience.Where no native SDK is available, the module falls back to a browser redirect flow using the URI scheme you register in step 2. |

## [Before you begin](../before-you-begin.html)

Ensure that you have completed the prerequisites before starting the numbered steps on this page below.

You need to have configured Apple, Facebook, and Google as external identity providers in PingOne Advanced Identity Cloud or PingAM, and set up the social authentication journeys your client app will step through.

[**Complete prerequisites**[icon: chevrons-right, set=fas, size=xs]](../before-you-begin.html)

## [Step 1. Adding core dependencies](01_adding_core_dependencies.html)

Install the **External IdP** module and link the native iOS dependencies.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_adding_core_dependencies.html)

## [Step 2. Handling URI schemes](02_handling_uri_schemes.html)

Register a URI scheme on Android and iOS so the OS can route provider redirects back to your app.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](02_handling_uri_schemes.html)

## [Step 3. Configuring native provider SDKs](03_configuring_native_provider_sdks.html)

Add and configure the native SDK for each provider you want to support.

[**Start step 3**[icon: chevrons-right, set=fas, size=xs]](03_configuring_native_provider_sdks.html)

## [Step 4. Authenticating with external IdPs](04_authenticate_with_external_idps.html)

Learn how to use the **External IdP** module to authenticate users through external providers in your journeys.

[**Start step 4**[icon: chevrons-right, set=fas, size=xs]](04_authenticate_with_external_idps.html)

---

---
title: Configure an Android app for OATH MFA
description: Configure an Android app to support OATH-based MFA using the OATH module, covering dependencies, client initialization, credential management, and passcode generation
component: orchsdks
page_id: orchsdks:journey:use-cases/oath/android/index
canonical_url: https://developer.pingidentity.com/orchsdks/journey/use-cases/oath/android/index.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 25 Mar 2025 11:00:37 +0100
keywords: ["DaVinci", "Flows", "Tutorial", "Source Code", "Integration", "SDK", "Android"]
section_ids:
  step_1_adding_core_dependencies: Step 1. Adding core dependencies
  step_2_initializing_the_oath_client: Step 2. Initializing the OATH Client
  default_oath_client_configuration: Default OATH client configuration
  custom_oath_client_configuration: Custom OATH client Configuration
  step_3_managing_oath_credentials: Step 3. Managing OATH credentials
  creating_oath_credentials: Creating OATH credentials
  getting_oath_credentials: Getting OATH credentials
  updating_oath_credentials: Updating OATH credentials
  deleting_oath_credentials: Deleting OATH credentials
  step_4_generating_oath_based_one_time_passcodes: Step 4. Generating OATH-based one-time passcodes
  generating_hotp_codes: Generating HOTP codes
  generating_totp_codes: Generating TOTP codes
  step_5_closing_the_oath_client: Step 5. Closing the OATH client
  handling_errors: Handling errors
  storage: Customizing credential storage
  customizing_the_default_sqlite_based_storage: Customizing the default SQLite-based storage
  implementing_your_own_storage_mechanism: Implementing your own storage mechanism
---

# Configure an Android app for OATH MFA

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: android, set=fab]Android

This page guides you through configuring your Android application to support OATH-based Multi-Factor Authentication (MFA) using the **OATH** module.

It covers dependency setup, OATH client initialization, credential management, passcode generation, and custom storage options.

## Step 1. Adding core dependencies

To add the core dependencies for OATH MFA:

1. In the **Project** tree view of your Android Studio project, open the `build.gradle.kts` file.

2. In the `dependencies` section, add the **OATH** module:

   ```gradle
   implementation("com.pingidentity.sdks:mfa:oath:2.0.1")
   ```

## Step 2. Initializing the OATH Client

To use the **OATH** module you must initialize the OATH client in your application.

You can use the default OATH client configuration, or provide your own configuration using a DSL-style builder.

### Default OATH client configuration

To use the default OATH client configuration, call the `OathClient()` method with no additional parameters.

When using the default configuration you will also need initialize the client, by using the `initialize()` method:

Initializing the OATH client with default config

```kotlin
val oathClient = OathClient()

// Initialize the client
oathClient.initialize()
```

### Custom OATH client Configuration

To customize the OATH client configuration, call the `OathClient()` method and pass the custom configuration as parameters.

When you pass a custom configuration the `OathClient()` also initializes the client, without having to manually call an initialize method:

Initializing the OATH client with custom config

```kotlin
val oathClient = OathClient {
    enableCredentialCache = true
    // Any other configuration options
}
```

The properties you can use to customize OATH client configuration are as follows:

* *enableCredentialCache*

  Whether to enable in-memory caching of credentials.

  By default, this is set to `false` for security reasons, as an attacker could potentially access cached credentials from memory dumps.

* *timeout*

  The timeout for network operations, in seconds.

  Default value is `15` seconds.

* *storage*

  The storage implementation to use for OATH credentials.

  If `null`, the default `SQLOathStorage` is used.

  Learn more in [Customizing credential storage](#storage).

* *policyEvaluator*

  The policy evaluator to use for credential policy validation.

  If `null`, the default `MfaPolicyEvaluator` is used.

* *logger*

  The logger instance used for logging messages.

  Defaults to the global logger instance.

  Learn more in [Logging](../../../customization/logging/index.html).

## Step 3. Managing OATH credentials

The **OATH** module relies on a set of credentials, that you can create, retrieve, update, and delete.

The credentials contain details such as the service and user they relate to, and details about how to generate the HOTP or TOTP key.

### Creating OATH credentials

The OATH module lets the user register their device for OATH-based multi-factor authentication (MFA).

The information required to register a device is contained in a specially-encoded URI, which your client application decodes to create the credentials.

This URI is often delivered by QR codes that the client can scan, or directly in the callback output by the [OATH Registration node](https://docs.pingidentity.com/auth-node-ref/latest/oath-registration.html).

Use the `addCredentialFromUri()` method to create OATH credentials and register an MFA device:

* onSuccess

* getOrThrow

* getOrNull

Creating OATH credentials using onSuccess

```kotlin
// Obtain OATH URI from journey callback or QR code
val uri = "otpauth://totp/Example:user@example.com?secret=JBSWY3DPEHPK3PXP&issuer=Example&algorithm=SHA1&digits=6&period=30"

// Create OATH credentials using onSuccess
oathClient.addCredentialFromUri(uri).onSuccess { credential ->
    // Handle the successfully created credential
    println("Created credential: ${credential.issuer}")
}.onFailure { exception ->
    // Handle error
    println("Failed to add credential: ${exception.message}")
}
```

Creating OATH credentials using getOrThrow

```kotlin
// Obtain OATH URI from journey callback or QR code
val uri = "otpauth://totp/Example:user@example.com?secret=JBSWY3DPEHPK3PXP&issuer=Example&algorithm=SHA1&digits=6&period=30"

// Create OATH credentials using getOrThrow
try {
    val credential = oathClient.addCredentialFromUri(uri).getOrThrow()
    // Use credential
} catch (e: Exception) {
    // Handle exception
}
```

Creating OATH credentials using getOrNull

```kotlin
// Obtain OATH URI from journey callback or QR code
val uri = "otpauth://totp/Example:user@example.com?secret=JBSWY3DPEHPK3PXP&issuer=Example&algorithm=SHA1&digits=6&period=30"

// Create OATH credentials using getOrNull
val credential = oathClient.addCredentialFromUri(uri).getOrNull()
if (credential != null) {
    // Use credential
} else {
    // Handle null case
}
```

### Getting OATH credentials

You can get a list of all the registered OATH credentials, or get an individual credential, by passing the credential ID as a parameter.

* All OATH credentials

* Specific OATH credential

Getting all OATH credentials

```kotlin
oathClient.getCredentials().onSuccess { credentials ->
    if (credentials.isEmpty()) {
        showMessage("No credentials found")
    } else {
        displayCredentials(credentials)
    }
}
```

Getting a specific OATH credential

```kotlin
oathClient.getCredential(credentialId).onSuccess { credential ->
    if (credential != null) {
        // Credential found, use it
        displayCredential(credential)
    } else {
        // Credential not found
        showMessage("Credential not found")
    }
}
```

### Updating OATH credentials

You can update the properties of a stored credential with new values, by using the `saveCredential()` method. Pass the updated credential object into the method as a parameter:

Updating an OATH credential

```kotlin
// Change display properties
credential.displayAccountName = "Babs Jensen"
credential.displayIssuer = "Example.com Checking Account"

oathClient.saveCredential(credential).onSuccess { updatedCredential ->
    // Handle successful update
    showMessage("Credential updated")
}.onFailure { exception ->
    // Handle failure
    showError("Failed to update credential: ${exception.message}")
}
```

### Deleting OATH credentials

Use the `deleteCredential()` method to remove individual credentials from the client device. Pass the credential ID into the method as a parameter:

Deleting an OATH credential

```kotlin
// Remove a credential by ID
oathClient.deleteCredential(credentialId).onSuccess { isDeleted ->
    if (isDeleted) {
        showMessage("Credential deleted")
    } else {
        showMessage("Credential not found")
    }
}.onFailure { exception ->
    showError("Failed to delete credential: ${exception.message}")
}
```

## Step 4. Generating OATH-based one-time passcodes

To perform OATH-based multi-factor authentication the user needs to enter the correct one-time passcode.

Your client app needs to generate these one-time passcodes and display them to the user.

### Generating HOTP codes

Use the `generateCode` method to create an HOTP code using the details within the specified credential:

Generating an HOTP for an OATH credential

```kotlin
// Generate code for a credential by its ID
oathClient.generateCode(credentialId).onSuccess { code ->
    // Implement displaying the generated code
    displayCode(code)
}.onFailure { exception ->
    // Handle error
    showError("Failed to generate code: ${exception.message}")
}
```

### Generating TOTP codes

For TOTP codes, the `code` object you generate contains timing and progress information that you can use to customize the user interface:

Generating a TOTP with timing and progress information

```kotlin
// Generate code with timing info for a credential
oathClient.generateCodeWithValidity(credentialId).onSuccess { codeInfo ->
    // Implement displaying the generated code
    displayCode(codeInfo.code)
    // Implement showing how long the code has been valid for
    updateProgressBar(codeInfo.progress)
    // Implement a countdown before generating a new code
    startCountdown(codeInfo.timeRemaining)
}.onFailure { exception ->
    // Handle error
    showError("Failed to generate code: ${exception.message}")
}
```

## Step 5. Closing the OATH client

You can close the client, clean up any temporary files, and regain the memory used by calling the `close()` method:

Closing an OATH client

```kotlin
// Close the OATH client and clean up
oathClient.close()
```

## Handling errors

The **OATH** module uses Kotlin's `Result` API for error handling, which provides a functional approach to error handling:

Handling errors using the Result API

```kotlin
// Using onSuccess/onFailure
oathClient.addCredentialFromUri(uri)
    .onSuccess { credential ->
        // Success path
    }
    .onFailure { exception ->
        when (exception) {
            is IllegalArgumentException -> // Handle invalid URI format
            is MfaException -> // Handle general MFA errors
            else -> // Handle other exceptions
        }
    }

// Using fold for combined handling
oathClient.addCredentialFromUri(uri).fold(
    onSuccess = { credential ->
        // Handle success
    },
    onFailure = { exception ->
        // Handle failure
    }
)

// Using runCatching for additional operations
runCatching {
    oathClient.addCredentialFromUri(uri).getOrThrow()
}.onSuccess { credential ->
    // Do something with credential
}.onFailure { exception ->
    // Handle error
}
```

## Customizing credential storage

The **OATH** module needs to store the credentials it uses on the client device.

By default, it uses an SQLite-based implementation, which you can customize.

You can also provide your own storage mechanism, by implementing the `OathStorage` interface.

### Customizing the default SQLite-based storage

The **OATH** module uses the `SQLOathStorage` implementation for storing OATH credentials by default.

You can customize this SQLite-based default as follows:

Customizing the `SQLOathStorage` implementation

```kotlin
// Create a custom storage instance with specific parameters
val customStorage = SQLOathStorage {
    context = applicationContext
    databaseName = "my_custom_oath_db.db"
    passphraseProvider = NonePassphraseProvider()
}

// Create the client with the custom storage
val oathClient = OathClient {
    storage = customStorage
    enableCredentialCache = true
}
```

The properties you can customize are as follows:

* `context`

  The Android application context is a required property.

* `databaseName`

  Optionally, rename the SQLite database.

* `databaseVersion`

  Customize the database version.

  The default is `1`.

* `passphraseProvider`

  Specify a custom passphrase provider for encrypting the SQLite database.

  * Use `KeyStorePassphraseProvider()` for encrypted storage using the Android KeyStore

  * Use `NonePassphraseProvider()` when you do not require the SQLite database to be encrypted.

  We recommend you encrypt the credential whenever possible.

### Implementing your own storage mechanism

You can implement a custom storage solution as alternative to the default `SQLOathStorage` by implementing the `OathStorage` interface:

Implementing custom OATH credential storage

```kotlin
class MyCustomStorage : OathStorage {
    override fun initialize() {
        // Initialize your custom storage
    }

    override fun close() {
        // Close storage
    }

    override fun clear() {
        // Remove all data
    }

    override fun storeOathCredential(credential: OathCredential) {
        // Store credential data
    }

    override fun retrieveOathCredential(credentialId: String): OathCredential? {
        // Retrieve credential data
        return null
    }

    override fun getAllOathCredentials(): List<OathCredential> {
        // Retrieve all credentials of a type
        return emptyList()
    }

    override fun removeOathCredential(credentialId: String): Boolean {
        // Delete credential data
        return true
    }

    override fun clearOathCredentials() {
        // Clear all credentials of a type
    }
}
```

For an example implementation that uses Android's SharedPreferences for storage, refer to [`SharedPrefsOathStorage`](https://github.com/ForgeRock/ping-android-sdk/blob/develop/mfa/oath/src/androidTest/kotlin/com/pingidentity/mfa/oath/storage/SharedPrefsOathStorage.kt) in the **ping-android-sdk** repo.

|   |                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `SharedPrefsOathStorage` implementation is for demonstration purposes only, and should not be used for storing potentially sensitive data such as OATH credentials. |

---

---
title: Configure an Android app for social sign-on
description: Configure an Android app to perform social sign-on with external identity providers using PingOne Advanced Identity Cloud or PingAM
component: orchsdks
page_id: orchsdks:journey:use-cases/external-idp/android/index
canonical_url: https://developer.pingidentity.com/orchsdks/journey/use-cases/external-idp/android/index.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 25 Mar 2025 11:00:37 +0100
keywords: ["PingOne", "DaVinci", "Flows", "Setup &amp; Configuration", "Source Code", "Use Case", "SDK", "IdP"]
section_ids:
  before_you_begin: Before you begin
  step_1_adding_core_dependencies: Step 1. Adding core dependencies
  step_2_handling_uri_schemes: Step 2. Handling URI schemes
  step_3_authenticating_with_external_idps: Step 3. Authenticating with external IdPs
  step_4_customizing_the_user_experience: Step 4. Customizing the user experience
---

# Configure an Android app for social sign-on

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: android, set=fab]Android

Complete the following high-level tasks to configure an Android client app to perform social sign-on with an external identity provider (IdP):

## [Before you begin](../before-you-begin.html)

Ensure that you have completed the prerequisites before starting the numbered steps on this page below.

You need to have configured Apple, Facebook, and Google as external identity providers in PingOne Advanced Identity Cloud or PingAM, and set up the social authentication journeys your client app will step through.

[**Complete prerequisites**[icon: chevrons-right, set=fas, size=xs]](../before-you-begin.html)

## [Step 1. Adding core dependencies](01_adding_core_dependencies.html)

These dependencies provide core support for social sign-on. These are the minimum required dependencies for redirecting users to the IdP for authentication.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_adding_core_dependencies.html)

## [Step 2. Handling URI schemes](02_handling_uri_schemes.html)

You must configure your Android app to open when the server redirects the user after authentication.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](02_handling_uri_schemes.html)

## [Step 3. Authenticating with external IdPs](03_authenticate_with_external_idps.html)

Learn how to authenticate your users with the external IdPs you have configured in your authentication journeys.

[**Start step 3**[icon: chevrons-right, set=fas, size=xs]](03_authenticate_with_external_idps.html)

## [Step 4. Customizing the user experience](04_customize_the_user_experience.html)

You can optionally tweak the user experience for authenticating with an external IdP.

[**Start step 4**[icon: chevrons-right, set=fas, size=xs]](04_customize_the_user_experience.html)

---

---
title: Configure an iOS app for OATH MFA
description: Configure an iOS app to support OATH-based MFA using the OATH module, covering dependencies, client initialization, credential management, and passcode generation
component: orchsdks
page_id: orchsdks:journey:use-cases/oath/ios/index
canonical_url: https://developer.pingidentity.com/orchsdks/journey/use-cases/oath/ios/index.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 25 Mar 2025 11:00:37 +0100
keywords: ["DaVinci", "Flows", "Tutorial", "Source Code", "Integration", "SDK", "iOS"]
section_ids:
  step_1_adding_core_dependencies: Step 1. Adding core dependencies
  swift_package_manager: Swift Package Manager
  cocoapods: CocoaPods
  step_2_initializing_the_oath_client: Step 2. Initializing the OATH Client
  step_3_managing_oath_credentials: Step 3. Managing OATH credentials
  creating_oath_credentials: Creating OATH credentials
  getting_oath_credentials: Getting OATH credentials
  updating_oath_credentials: Updating OATH credentials
  deleting_oath_credentials: Deleting OATH credentials
  step_4_generating_oath_based_one_time_passcodes: Step 4. Generating OATH-based one-time passcodes
  generating_hotp_codes: Generating HOTP codes
  generating_totp_codes: Generating TOTP codes
  step_5_closing_the_oath_client: Step 5. Closing the OATH client
  handling_errors: Handling errors
  storage: Customizing credential storage
  customizing_the_default_keychain_based_storage: Customizing the default keychain-based storage
  implementing_your_own_storage_mechanism: Implementing your own storage mechanism
---

# Configure an iOS app for OATH MFA

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: apple, set=fab]iOS

This page guides you through configuring your iOS application to support OATH-based Multi-Factor Authentication (MFA) using the **OATH** module.

It covers dependency setup, OATH client initialization, credential management, passcode generation, and custom storage options.

## Step 1. Adding core dependencies

You can use Swift Package Manager (SPM) or CocoaPods to add dependencies to your iOS project.

### Swift Package Manager

1. With your project open in **Xcode**, select File > Add Package Dependencies.

2. In the search bar, enter the Orchestration SDK for iOS repository URL: `https://github.com/ForgeRock/ping-ios-sdk`.

3. Select the `ping-ios-sdk` package, and then click Add Package.

4. In the Choose Package Products dialog, ensure that the `PingOath` library is added to your target project.

5. Click Add Package.

6. In your project, import the relevant dependencies:

   ```swift
   import PingOath
   ```

### CocoaPods

1. If you do not already have CocoaPods, install the [latest version](https://guides.cocoapods.org/using/getting-started.html).

2. If you do not already have a Podfile, in a terminal window, run the following command to create a new [Podfile](https://guides.cocoapods.org/syntax/podfile.html):

   ```
   pod init
   ```

3. Add the relevant dependencies to your Podfile:

   ```
   pod 'PingOath'
   ```

4. Run the following command to install pods:

   ```
   pod install
   ```

## Step 2. Initializing the OATH Client

To use the **OATH** module you must initialize the OATH client in your application by calling the `createClient()` method:

Initializing the OATH client with default config

```swift
// Create an OATH client
let client = try await OathClient.createClient { config in
    config.logger = LogManager.logger
    config.enableCredentialCache = false
}
```

The properties you can use to customize OATH client configuration are as follows:

* *enableCredentialCache*

  Whether to enable in-memory caching of credentials.

  By default, this is set to `false` for security reasons, as an attacker could potentially access cached credentials from memory dumps.

* *timeout*

  The timeout for network operations, in seconds.

  Default value is `15`.

* *storage*

  The storage implementation to use for OATH credentials.

  If `nil`, the default `OathKeychainStorage` is used.

  Learn more in [Customizing credential storage](#storage).

* *policyEvaluator*

  The policy evaluator to use for credential policy validation.

  If `nil`, the default `MfaPolicyEvaluator` is used.

* *encryptionEnabled*

  Whether data encryption is enabled for storing credentials.

  Default is `true`.

* *logger*

  The logger instance used for logging messages.

  Defaults to a global logger instance.

  Learn more in [Logging](../../../customization/logging/index.html).

## Step 3. Managing OATH credentials

The **OATH** module relies on a set of credentials, that you can create, retrieve, update, and delete.

The credentials contain details such as the service and user they relate to, and details about how to generate the HOTP or TOTP key.

### Creating OATH credentials

The OATH module lets the user register their device for OATH-based multi-factor authentication (MFA).

The information required to register a device is contained in a specially-encoded URI, which your client application decodes to create the credentials.

This URI is often delivered by QR codes that the client can scan, or directly in the callback output by the [OATH Registration node](https://docs.pingidentity.com/auth-node-ref/latest/oath-registration.html).

Use the `addCredentialFromUri()` method to create OATH credentials and register an MFA device:

Creating OATH credentials

```swift
let uri = "otpauth://hotp/Example:user@example.com?secret=JBSWY3DPEHPK3PXP&counter=0"

let credential = try await client.addCredentialFromUri(uri)
```

### Getting OATH credentials

You can get a list of all the registered OATH credentials, or get an individual credential, by passing the credential ID as a parameter.

* All OATH credentials

* Specific OATH credential

Getting all OATH credentials

```swift
do {
    let credentials = try await Task.detached(priority: .userInitiated) {
        try await client.getCredentials()
    }.value
} catch {
    throw AppError.oathError("Failed to load credentials: \(error.localizedDescription)")
}
```

Getting a specific OATH credential

```swift
let credential = try await Task.detached(priority: .userInitiated) {
    try await client.getCredential(credentialId)
}.value
```

### Updating OATH credentials

You can update the properties of a stored credential with new values, by using the `saveCredential()` method. Pass the updated credential object into the method as a parameter:

Updating an OATH credential

```swift
for credential in credentials {
    var updated = credential
    updated.displayIssuer = "Example.com Checking Account"
    updated.displayAccountName = "Babs Jensen"
    _ = try await client.saveCredential(updated)
}
```

### Deleting OATH credentials

Use the `deleteCredential()` method to remove individual credentials from the client device. Pass the credential ID into the method as a parameter:

Deleting an OATH credential

```swift
do {
    let removed = try await Task.detached(priority: .userInitiated) {
        try await client.deleteCredential(credentialId)
    }.value
    return removed
} catch {
    throw AppError.oathError("Failed to remove credential: \(error.localizedDescription)")
}
```

## Step 4. Generating OATH-based one-time passcodes

To perform OATH-based multi-factor authentication the user needs to enter the correct one-time passcode.

Your client app needs to generate these one-time passcodes and display them to the user.

### Generating HOTP codes

Use the `generateCode` method to create an HOTP code using the details within the specified credential:

Generating an HOTP for an OATH credential

```swift
// Generate code (counter increments automatically)
let code1 = try await client.generateCode(hotpCredential.id)  // Counter = 1
let code2 = try await client.generateCode(hotpCredential.id)  // Counter = 2
```

### Generating TOTP codes

For TOTP codes, the `code` object you generate contains timing and progress information that you can use to customize the user interface:

Generating a TOTP with timing and progress information

```swift
// Get code with timing and validity information
let codeInfo = try await client.generateCodeWithValidity(credential.id)

print("Code: \(codeInfo.code)")
print("Time remaining: \(codeInfo.timeRemaining) seconds")
print("Progress: \(codeInfo.progress * 100)%")
```

## Step 5. Closing the OATH client

You can close the client, clean up any temporary files, and regain the memory used by calling the `close()` method:

Closing an OATH client

```swift
// Close the OATH client and clean up
try await client.close()
```

## Handling errors

The **OATH** module provides comprehensive error handling:

Handling errors

```swift
do {
    let credential = try await client.addCredentialFromUri(uri)
} catch let error as OathError {
    switch error {
    case .invalidUri(let message):
        print("Invalid URI: \(message)")
    case .credentialNotFound(let id):
        print("Credential not found: \(id)")
    case .credentialLocked(let id):
        print("Credential is locked: \(id)")
    case .codeGenerationFailed(let message, let underlying):
        print("Code generation failed: \(message)")
    case .initializationFailed(let message, let underlying):
        print("Client initialization failed: \(message)")
    }
} catch let error as OathStorageError {
    switch error {
    case .storageFailure(let message, let underlying):
        print("Storage error: \(message)")
    }
}
```

## Customizing credential storage

The **OATH** module needs to store the credentials it uses on the client device.

By default, it uses an iOS keychain services-based implementation, which you can customize.

You can also provide your own storage mechanism, by implementing the `OathStorage` interface.

### Customizing the default keychain-based storage

The **OATH** module uses the `OathKeychainStorage` implementation for storing OATH credentials by default.

You can customize this keychain-based default as follows:

Customizing the `OathKeychainStorage` implementation

```swift
// Create a custom storage instance with specific parameters
let customStorage = OathKeychainStorage(
    service: "com.myapp.oath",
    accessGroup: "group.myapp",
    accessibility: kSecAttrAccessibleWhenUnlockedThisDeviceOnly
)

// Create the client with the custom storage
let client = try await OathClient.createClient { config in
    config.storage = customStorage
    config.enableCredentialCache = false
}
```

The properties you can customize are as follows:

* `service`

  The keychain service identifier.

  Defaults to "com.pingidentity.oath".

* `accessGroup`

  Optional keychain access group for shared access.

* `accessibility`

  Keychain accessibility level.

  Defaults to `kSecAttrAccessibleWhenUnlockedThisDeviceOnly`.

### Implementing your own storage mechanism

You can implement a custom storage solution as alternative to the default `OathKeychainStorage` by implementing the `OathStorage` interface:

Implementing custom OATH credential storage

```swift
class MyCustomStorage: OathStorage {

  func storeOathCredential(_ credential: OathCredential) async throws {
    // Store an OATH credential.
  }

  func retrieveOathCredential(credentialId: String) async throws -> OathCredential? {
    // Retrieve an OATH credential by its ID.
  }

  func getAllOathCredentials() async throws -> [OathCredential] {
    // Get all OATH credentials.
  }

  func removeOathCredential(credentialId: String) async throws -> Bool {
    // Remove an OATH credential by its ID.
  }

  func clearOathCredentials() async throws {
    // Clear all OATH credentials from the storage.
  }
}
```

---

---
title: Configure an iOS app for social sign-on
description: Configure an iOS app to perform social sign-on with external identity providers using PingOne Advanced Identity Cloud or PingAM
component: orchsdks
page_id: orchsdks:journey:use-cases/external-idp/ios/index
canonical_url: https://developer.pingidentity.com/orchsdks/journey/use-cases/external-idp/ios/index.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 25 Mar 2025 11:00:37 +0100
keywords: ["PingOne", "DaVinci", "Flows", "Setup &amp; Configuration", "Source Code", "Use Case", "SDK", "IdP"]
section_ids:
  before_you_begin: Before you begin
  step_1_adding_core_dependencies: Step 1. Adding core dependencies
  step_2_handling_uri_schemes: Step 2. Handling URI schemes
  step_3_authenticating_with_external_idps: Step 3. Authenticating with external IdPs
  step_4_customizing_the_user_experience: Step 4. Customizing the user experience
---

# Configure an iOS app for social sign-on

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: apple, set=fab]iOS

Complete the following high-level tasks to configure an Android client app to perform social sign-on with an external identity provider (IdP):

## [Before you begin](../before-you-begin.html)

Ensure that you have completed the prerequisites before starting the numbered steps on this page below.

You need to have configured Apple, Facebook, and Google as external identity providers in PingOne Advanced Identity Cloud or PingAM, and set up the social authentication journeys your client app will step through.

[**Complete prerequisites**[icon: chevrons-right, set=fas, size=xs]](../before-you-begin.html)

## [Step 1. Adding core dependencies](01_adding_core_dependencies.html)

These dependencies provide core support for social sign-on. These are the minimum required dependencies for redirecting users to the IdP for authentication.

[**Start step 1**[icon: chevrons-right, set=fas, size=xs]](01_adding_core_dependencies.html)

## [Step 2. Handling URI schemes](02_handling_uri_schemes.html)

You must configure your Android app to open when the server redirects the user after authentication.

[**Start step 2**[icon: chevrons-right, set=fas, size=xs]](02_handling_uri_schemes.html)

## [Step 3. Authenticating with external IdPs](03_authenticate_with_external_idps.html)

Learn how to authenticate your users with the external IdPs you have configured in your authentication journeys.

[**Start step 3**[icon: chevrons-right, set=fas, size=xs]](03_authenticate_with_external_idps.html)

## [Step 4. Customizing the user experience](04_customize_the_user_experience.html)

You can optionally tweak the user experience for authenticating with an external IdP.

[**Start step 4**[icon: chevrons-right, set=fas, size=xs]](04_customize_the_user_experience.html)

---

---
title: Configuring a Journey client in React Native
description: Configure the Journey client in React Native using createJourneyClient() to connect to your PingOne Advanced Identity Cloud or PingAM server
component: orchsdks
page_id: orchsdks:journey:usage/react-native/03-configuring-the-journey-module
canonical_url: https://developer.pingidentity.com/orchsdks/journey/usage/react-native/03-configuring-the-journey-module.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Wed, 6 May 2026 00:00:00 +0000
keywords: ["OAuth 2.0", "OpenID Connect", "Setup &amp; Configuration", "Source Code", "Integration", "SDK", "React Native"]
section_ids:
  integrating_the_oidc_module: Integrating the OIDC Module
---

# Configuring a Journey client in React Native

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: react, set=fab]React Native

* [Prepare](01-configuring-the-server.html)

* [Install](02-installing-the-journey-module.html)

* **Configure**

* [Start](04-starting-an-authentication-journey.html)

* [Navigate](05-navigating-an-authentication-journey.html)

* [Manage](06-handling-sessions.html)

***

You must configure a **Journey** client to connect to your Advanced Identity Cloud or PingAM server.

To configure a client, call the `createJourneyClient()` factory function and provide the configuration options as follows:

Configuring the createJourneyClient factory

```typescript
import { createJourneyClient } from '@ping-identity/rn-journey';
import { logger } from '@ping-identity/rn-logger';

// Optionally, set the log level to 'debug'
const debugLogger = logger({ level: 'debug' });

const journeyClient = createJourneyClient({
  serverUrl: 'https://openam-forgerock-sdks.forgeblocks.com/am',
  realm: 'alpha',
  cookie: 'ch15fefc5407912',
  timeout: 5000,
  logger: debugLogger,
});
```

Update the following properties with values that match your environment:

* *serverUrl*

  The URL of the Access Management service on your server. This is the only required property.

  * *Advanced Identity Cloud example:*

    `https://openam-forgerock-sdks.forgeblocks.com/am`

  * *PingAM example:*

    `https://openam.example.com:8443/openam`

* *realm*

  The realm containing your users and configuration.

  Usually `root` for PingAM and `alpha` or `bravo` for Advanced Identity Cloud.

* *cookie*

  The name of the cookie your PingOne Advanced Identity Cloud tenant uses to store SSO tokens in client browsers.

  * On a self-hosted PingAM server this value is usually `iPlanetDirectoryPro`.

  * On Advanced Identity Cloud tenants, the cookie name is a random string of characters, such as `ch15fefc5407912`.

    > **Collapse: How do I find my PingOne Advanced Identity Cloud cookie name?**
    >
    > To locate the cookie name in an PingOne Advanced Identity Cloud tenant:
    >
    > 1. Navigate to Tenant settings > Global Settings
    >
    > 2. Copy the value of the Cookie property.

* *timeout*

  The maximum time, in milliseconds, that the client waits for a response from the server.

  Default is `5000` (5 seconds).

* *logger*

  Optionally, specify the logger instance to use to output messages from the Orchestration SDK.

  Pass the `level` parameter to the instance to configure the amount of detail the Orchestration SDK outputs. Choose from, `debug`, `info`, `warn`, `error`, or `none`.

## Integrating the OIDC Module

You can choose to integrate the **oidc** module into your client configuration, to obtain and manage OpenID Connect 1.0 tokens on behalf of the user.

To integrate the **oidc** module, add the configuration when instantiating the journey client, as follows:

Integrating the `oidc` module with the `journey` client

```typescript
import { createJourneyClient } from '@ping-identity/rn-journey';

const journeyClient = createJourneyClient({
    serverUrl: 'https://openam-forgerock-sdks.forgeblocks.com/am',
    realm: 'alpha',
    cookie: 'ch15fefc5407912',
    modules: {
        oidc: {
          clientId: 'sdkPublicClient',
          discoveryEndpoint: 'https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/alpha/.well-known/openid-configuration',
          scopes: ['openid', 'email', 'address', 'profile'],
          redirectUri: 'com.example.demo://oauth2redirect'
        }
    }
});
```

Update the following properties with values that match your environment:

* *clientId*

  The client ID from your OAuth 2.0 application.

  For example, `sdkPublicClient`

* *discoveryEndpoint*

  The `.well-known` endpoint from your server.

  > **Collapse: How do I find my PingOne Advanced Identity Cloud  URL?**
  >
  > You can view the `.well-known` endpoint for an OAuth 2.0 client in the PingOne Advanced Identity Cloud admin console:
  >
  > 1. Log in to your PingOne Advanced Identity Cloud administration console.
  >
  > 2. Click Applications, and then select the OAuth 2.0 client you created earlier. For example, sdkPublicClient.
  >
  > 3. On the Sign On tab, in the Client Credentials section, copy the Discovery URI value.
  >
  >    For example, `https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/alpha/.well-known/openid-configuration`
  >
  > |   |                                                                                                                                                                                                                                                                                                                                 |
  > | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  > |   | If you are using a custom domain, your `.well-known` is formed as follows:`https://<custom-domain-fqdn>/.well-known/openid-configuration`Learn more in [Access OIDC configuration discovery endpoint](https://docs.pingidentity.com/pingoneaic/latest/realms/custom-domains.html#access-oidc-configuration-discovery-endpoint). |

  > **Collapse: How do I find my PingAM  URL?**
  >
  > To form the `.well-known` URL for an PingAM server, concatenate the following information into a single URL:
  >
  > 1. The base URL of the PingAM component of your deployment, including the port number and deployment path.
  >
  >    For example, `https://openam.example.com:8443/openam`
  >
  > 2. The string `/oauth2`
  >
  > 3. The hierarchy of the realm that contains the OAuth 2.0 client.
  >
  >    You must specify the entire hierarchy of the realm, starting at the Top Level Realm. Prefix each realm in the hierarchy with the `realms/` keyword.
  >
  >    For example, `/realms/root/realms/customers`
  >
  >    |   |                                                                                 |
  >    | - | ------------------------------------------------------------------------------- |
  >    |   | If you omit the realm hierarchy, the top level `ROOT` realm is used by default. |
  >
  > 4. The string `/.well-known/openid-configuration`
  >
  > For example, `https://openam.example.com:8443/openam/oauth2/realms/root/.well-known/openid-configuration`

  For example, `https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/alpha/.well-known/openid-configuration`

* *scopes*

  The scopes you added to your OAuth 2.0 application.

  For example, `'openid', 'email', 'address', 'profile'`

* *redirectUri*

  The `redirect_uri` as configured in the OAuth 2.0 client profile.

  This value must exactly match a value configured in your OAuth 2.0 client.

  For example, `com.example.demo://oauth2redirect`