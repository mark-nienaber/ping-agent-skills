---
title: Google Login Connector
description: The Google Login connector authenticates users with Google and retrieves user attributes for use in DaVinci flows.
component: connectors
page_id: connectors::google_login_connector
canonical_url: https://docs.pingidentity.com/connectors/google_login_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-google-as-an-idp: Configuring Google as an IdP
  registering-the-application-with-google: Registering the application with Google
  steps: Steps
  next-steps: Next steps
  enabling-the-google-people-api: Enabling the Google People API
  steps-2: Steps
  next-steps-2: Next steps
  configuring-the-google-login-connector: Configuring the Google Login connector
  connector-configuration: Connector configuration
  attributes: Attributes
  attribute-mapping: Attribute mapping
  using-the-connector-in-a-flow: Using the connector in a flow
  redirecting-users-to-google: Redirecting users to Google
  capabilities: Capabilities
  loginFirstFactor: Google Login
  getUserInfo: Get User Info from Google
---

# Google Login Connector

The Google Login connector authenticates users with Google and retrieves user attributes for use in DaVinci flows.

## Setup

### Resources

You can find more information and setup help in the following:

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A Google account.

### Configuring Google as an IdP

Before configuring the Google Login connector in DaVinci, register the application in the **Google API Console** and collect the values that Google generates to configure Google as an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)*.

You'll complete two tasks in the **Google API Console**:

* [Registering the application with Google](#registering-the-application-with-google)

* [Enabling the Google People API](#enabling-the-google-people-api)

#### Registering the application with Google

When you register your application, Google generates an **App ID** and **App Secret** for the application. You'll need these values to connect the application to DaVinci.

#### Steps

1. Go to the [Google API Console](https://console.developers.google.com).

   If you haven't created a Google account, you can do so now.

2. In the **Projects** list, select a project or create a new one.

3. On the left, click **Credentials**.

4. Click **Create credentials**, then select **OAuth client ID**.

   If you're prompted to configure an OAuth consent screen with information about your application, you can do that now.

5. Select the appropriate application type for your project and enter the following information:

   * **Name**: The name of the OAuth client ID, not the display name of the application.

   * **Authorized JavaScript origins**: The origin URI of the client application, for use with requests from a browser.

   * **Authorized redirect URIs**: The path in your application that users are redirected to after they authenticate with Google. This is your **DaVinci Redirect URL**: `https://auth.pingone.com/[companyID]/davinci/oauth2/callback`.

6. Click **Create**.

7. On the **OAuth client** page, copy the client ID and client secret to a secure location.

   You can always access the client ID and client secret from the **Credentials** page in the API Console.

#### Next steps

Learn more in [Manage OAuth Clients](https://support.google.com/cloud/answer/15549257?sjid=17163377939720277440-NC) in the Google Cloud Platform Console Help documentation.

#### Enabling the Google People API

You must enable the Google People API if it's not enabled already.

#### Steps

1. Go to the [Google API Console](https://console.developers.google.com).

2. In the **Projects** list, select a project or create a new one.

3. On the left, click **Library**.

4. Locate the **Google People API**.

   |   |                                                       |
   | - | ----------------------------------------------------- |
   |   | If you need help finding the API, use the search bar. |

5. Click **Enable**.

#### Next steps

Learn more in [Enable and disable APIs](https://support.google.com/googleapi/answer/6158841) in the Google API Console Help documentation.

### Configuring the Google Login connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

Use the values from Google to populate the connector's general properties.

| Property                      | Description                                                                                                                                                                           |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DaVinci Redirect URL**      | `https://auth.pingone.com/[companyID]/davinci/oauth2/callback`                                                                                                                        |
| **Issuer URL**                | `https://accounts.google.com`                                                                                                                                                         |
| **Authorization Endpoint**    | `https://accounts.google.com/o/oauth2/auth`                                                                                                                                           |
| **Token Endpoint**            | `https://oauth2.googleapis.com/token`                                                                                                                                                 |
| **UserInfo Endpoint**         | `https://www.googleapis.com/oauth2/v3/userinfo`                                                                                                                                       |
| **App ID**                    | The **Client ID** that you copied earlier from the IdP. You can find this information on the **Credentials** page in the [Google API Console](https://console.developers.google.com). |
| **Client Secret**             | The client secret that you copied earlier from the IdP. You can find this information on the **Credentials** page in the [Google API Console](https://console.developers.google.com). |
| **Scope**                     | The default scopes are `openid email profile`. Add additional scopes if you want to retrieve additional attributes that require specific permissions from Google.                     |
| **Application Return to URL** | The URL of the app that embeds the DaVinci flow. If you're using redirect, leave this blank.                                                                                          |

#### Attributes

On the **Attributes** tab, review the default attributes available from Google and define additional attributes when Google includes them in the ID token returned for the application.

![A screen capture of the Google Login connector attributes list.](_images/connector-images/dvc-google-login-attribute-list.png)

#### Attribute mapping

On the **Attribute Mapping** tab, map the following default Google attributes to the DaVinci attributes:

| **Google Login Attributes** | **DaVinci Attributes** |
| --------------------------- | ---------------------- |
| `sub`                       | `username`             |
| `givenName`                 | `firstName`            |
| `familyName`                | `lastName`             |
| `email`                     | `email`                |

## Using the connector in a flow

### Redirecting users to Google

![A screen capture of the Google redirect flow.](_images/connector-images/dvc-google-login-flow.png)

This flow redirects the user to Google for authentication. After the user signs in, DaVinci automatically completes the token exchange and returns identity claims to the flow for downstream logic.

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Google Login

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - - Display Name button
>   - showPoweredBy toggleSwitch
>   - skipButtonPress toggleSwitch
>
> * output object
>
>   * at\_hash string
>
>   * aud boolean
>
>   * azp boolean
>
>   * email string
>
>   * email\_verified boolean
>
>   * exp number
>
>   * family\_name string
>
>   * given\_name string
>
>   * hd string
>
>   * iat number
>
>   * iss string
>
>   * locale string
>
>   * name string
>
>   * picture string
>
>   * sub string
>
> Output Example
>
> ```json
> {
>   "at_hash": "ISKFDARoPOftzcYcXWjDuw",
>   "aud": "470515226752-ffprd36ul6trmb0gmcjv24jlv5v54efn.apps.googleusercontent.com",
>   "azp": "470515226752-ffprd36ul6trmb0gmcjv24jlv5v54efn.apps.googleusercontent.com",
>   "email": "johndoe@example.com",
>   "email_verified": true,
>   "exp": 1603874413,
>   "family_name": "Doe",
>   "given_name": "John",
>   "hd": "example.com",
>   "iat": 1603870813,
>   "iss": "https://accounts.google.com",
>   "locale": "en",
>   "name": "John Doe",
>   "picture": "https://lh3.googleusercontent.com/a-/imagehash",
>   "sub": "123456789012345678901"
> }
> ```

### Get User Info from Google

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - - Display Name button
>   - showPoweredBy toggleSwitch
>   - skipButtonPress toggleSwitch
>
> * output object
>
>   * at\_hash string
>
>   * aud boolean
>
>   * azp boolean
>
>   * email string
>
>   * email\_verified boolean
>
>   * exp number
>
>   * family\_name string
>
>   * given\_name string
>
>   * hd string
>
>   * iat number
>
>   * iss string
>
>   * locale string
>
>   * name string
>
>   * picture string
>
>   * sub string
>
> Output Example
>
> ```json
> {
>   "at_hash": "ISKFDARoPOftzcYcXWjDuw",
>   "aud": "470515226752-ffprd36ul6trmb0gmcjv24jlv5v54efn.apps.googleusercontent.com",
>   "azp": "470515226752-ffprd36ul6trmb0gmcjv24jlv5v54efn.apps.googleusercontent.com",
>   "email": "johndoe@example.com",
>   "email_verified": true,
>   "exp": 1603874413,
>   "family_name": "Doe",
>   "given_name": "John",
>   "hd": "example.com",
>   "iat": 1603870813,
>   "iss": "https://accounts.google.com",
>   "locale": "en",
>   "name": "John Doe",
>   "picture": "https://lh3.googleusercontent.com/a-/imagehash",
>   "sub": "123456789012345678901"
> }
> ```