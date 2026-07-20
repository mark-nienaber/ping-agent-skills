---
title: Facebook Login Connector
description: The Facebook Login connector authenticates users with Facebook and retrieves user attributes for use in PingOne DaVinci flows
component: connectors
page_id: connectors::facebook_login_connector
canonical_url: https://docs.pingidentity.com/connectors/facebook_login_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-facebook-as-an-idp: Configuring Facebook as an IdP
  registering-your-application-with-facebook-for-developers: Registering your application with Facebook for Developers
  steps: Steps
  result: Result:
  next-steps: Next steps
  enabling-facebook-login: Enabling Facebook Login
  steps-2: Steps
  configuring-the-facebook-login-connector: Configuring the Facebook Login connector
  connector-configuration: Connector configuration
  attributes: Attributes
  attribute-mapping: Attribute mapping
  using-the-connector-in-a-flow: Using the connector in a flow
  redirecting-users-to-facebook: Redirecting users to Facebook
  capabilities: Capabilities
  loginFirstFactor: Login with Facebook
---

# Facebook Login Connector

The Facebook Login connector authenticates users with Facebook and retrieves user attributes for use in PingOne DaVinci flows.

## Setup

### Resources

You can find more information and setup help in the following:

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A Facebook Developer account.

### Configuring Facebook as an IdP

Before configuring the Facebook Login connector in PingOne DaVinci, register the application in **Facebook for Developers** and collect the values that Facebook generates to configure Facebook as an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)*.

You'll complete two tasks in your **Facebook Developer Account**:

* [Registering your application with Facebook for Developers](#registering-your-application-with-facebook-for-developers)

* [Enabling Facebook Login](#enabling-facebook-login)

#### Registering your application with Facebook for Developers

Facebook generates an app ID and app secret for your application. You'll need these values to connect the application to PingOne DaVinci.

#### Steps

1. Sign on to your [Facebook Developer Account](https://developers.facebook.com).

   If you haven't created a Facebook Developer Account, you can do so now.

2. At the top of the page, click **My Apps** and then click **Create app**.

3. Select the appropriate application type and then click **Continue**.

4. Enter the following information:

   * **App Display name**: The name you want to associate with this application ID.

   * **App Contact email**: The primary contact information for the application.

5. Click **Create app**, and then complete the security check, if required.

   #### Result:

   The application dashboard displays.

6. On the left side of the page, go to **Settings** > **Basic** and enter the following information:

   * **App domains**: The path in your application that users are redirected to after they have authenticated with Facebook. This is your **DaVinci Redirect URL**: `https://auth.pingone.com/[companyID]/davinci/oauth2/callback`.

     Leave **App domains** blank for now.

   * **Privacy policy URL** (optional): The URL that contains your privacy policy.

   * **Terms of service URL** (optional): The URL that contains your terms of service.

7. At the top of the page, locate the **App ID** and **App secret** and copy their values to a secure location.

8. Click **Save changes**.

#### Next steps

Learn more in [Meta App Development](https://developers.facebook.com/docs/apps).

#### Enabling Facebook Login

You must enable Facebook Login for your application if it's not enabled already.

#### Steps

1. Go to [Facebook for Developers](https://developers.facebook.com).

2. At the top of the page, click **My Apps**, and then select the appropriate app.

3. On the left side of the page, click **Products**

4. Locate the **Facebook Login** card and click **Set up**.

5. Follow the instructions to set up Facebook Login.

### Configuring the Facebook Login connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

Use the values from Facebook to populate the connector's general properties.

| Property                         | Description                                                                                                                                                                                         |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PingOne DaVinci Redirect URL** | `https://auth.pingone.com/[.varname[companyID]/davinci/oauth2/callback`                                                                                                                             |
| **Application ID**               | The application ID that you copied earlier from the IdP. You can find this information on the **Basic settings** page in the [Facebook for Developers portal](https://developers.facebook.com).     |
| **Client Secret**                | The application secret that you copied earlier from the IdP. You can find this information on the **Basic settings** page on the [Facebook for Developers portal](https://developers.facebook.com). |
| **Scope**                        | The default scopes are `openid email profile`. Add additional scopes if you want to retrieve additional attributes that require specific permissions from Facebook.                                 |
| **Application Return to URL**    | The URL of the app that embeds the PingOne DaVinci flow. If you're using redirect, leave this blank.                                                                                                |

#### Attributes

On the **Attributes** tab, review the default attributes available from Facebook and define additional attributes when Facebook includes them in the ID token returned for the application.

![A screen capture of the Facebook Login connector attributes list.](_images/connector-images/dvc-facebook-login-attribute-list.png)

#### Attribute mapping

On the **Attribute Mapping** tab, map the following default Facebook attributes to the PingOne DaVinci attributes:

| **Facebook Login Attributes** | **PingOne DaVinci Attributes** |
| ----------------------------- | ------------------------------ |
| `id`                          | `username`                     |
| `givenName`                   | `firstName`                    |
| `familyName`                  | `lastName`                     |
| `email`                       | `email`                        |

## Using the connector in a flow

### Redirecting users to Facebook

![A screen capture of the Facebook redirect flow.](_images/connector-images/dvc-facebook-login-flow.png)

This flow redirects the user to Facebook for authentication. After the user signs in, PingOne DaVinci automatically completes the token exchange and returns identity claims to the flow for downstream logic.

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Login with Facebook

enables a user to use Facebook account to log in

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