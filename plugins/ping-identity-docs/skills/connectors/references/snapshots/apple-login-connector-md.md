---
title: Apple Login Connector
description: The Apple Login connector authenticates users with Sign in with Apple and retrieves Apple ID attributes for use in DaVinci flows.
component: connectors
page_id: connectors::apple_login_connector
canonical_url: https://docs.pingidentity.com/connectors/apple_login_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-apple-as-an-idp: Configuring Apple as an IdP
  creating-an-app-id: Creating an App ID
  steps: Steps
  creating-a-services-id: Creating a Services ID
  steps-2: Steps
  creating-a-private-key: Creating a private key
  steps-3: Steps
  configuring-the-apple-login-connector: Configuring the Apple Login connector
  connector-configuration: Connector configuration
  attributes: Attributes
  attribute-mapping: Attribute mapping
  using-the-connector-in-a-flow: Using the connector in a flow
  redirecting-users-to-apple: Redirecting users to Apple
  capabilities: Capabilities
  loginFirstFactor: Sign in with Apple
---

# Apple Login Connector

The Apple Login connector authenticates users with **Sign in with Apple** and retrieves **Apple ID** attributes for use in DaVinci flows.

## Setup

### Resources

You can find more information and setup help in the following:

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

* Apple documentation:

  * [Incorporating Sign in with Apple into other platforms](https://developer.apple.com/documentation/signinwithapple/incorporating-sign-in-with-apple-into-other-platforms)

### Requirements

To use the connector, you'll need:

* An Apple Developer account.

### Configuring Apple as an IdP

Before configuring the Apple Login connector in DaVinci, register the application in the Apple Developer portal and collect the values that Apple generates to configure Apple as an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)*.

You'll complete three tasks in the Apple Developer portal:

* [Creating an App ID](#creating-an-app-id)

* [Creating a Services ID](#creating-a-services-id)

* [Creating a private key](#creating-a-private-key)

#### Creating an App ID

When you register your application, Apple generates an **App ID** to identify the application. You'll need this value to connect the application to DaVinci.

#### Steps

1. Go to the [Apple Developer site](https://developer.apple.com) and sign on to your Apple Developer account.

   If you don't have an Apple Developer account, you'll need to create one.

2. Click **Certificates, Identifiers & Profiles**.

3. On the left, click **Identifiers** and then click the **[icon: plus, set=fa]**icon.

4. In the **Register a New Identifier** section, select **App IDs**.

5. In the **Register an App ID** section, enter a value for the **Bundle ID**.

6. Copy the following values to a secure location:

   * **App ID prefix** (Team ID): Identifies your team or organization.

   * **Bundle ID**: Identifies a group of applications.

7. In the list of available capabilities, select **Sign in with Apple**.

8. Click **Continue and Register**.

#### Creating a Services ID

The **Services ID** identifies the particular instance of your application. The **Services ID** is equivalent to a client ID in DaVinci.

#### Steps

1. On the [Apple Developer site](https://developer.apple.com), sign on to your Apple Developer account and then click **Certificates, Identifiers & Profiles**.

2. In the **Register a New Identifier** section, select **Services ID**.

3. Enter the following information:

   * **Description**: A brief description of the application.

   * **Identifier**: The path to the application. This value will be used as the client ID in PingOne.

4. Click **Continue and Register**.

5. In the list, select the service you just created.

6. Select **Sign in with Apple** and click **Configure**.

7. Select the primary App ID and click the **[icon: plus, set=fa]**icon.

8. Enter a value for **Domains and subdomains**.

   This is the top-level domain for your application.

9. Leave the **Return URLs** blank for now.

   This is the path in your application that users are redirected to after they have authenticated with Apple. This value is equivalent to a callback URI. You'll enter this value after you set up your application in DaVinci.

10. Click **Next**, and then click **Done**.

11. Click **Continue**, and then click **Save**.

#### Creating a private key

When you register your application, Apple generates a private key for client authentication. You'll need this value when you add the application to DaVinci.

#### Steps

1. On the Apple Developer site, click **Certificates, Identifiers & Profiles**.

2. On the left, click **Keys**.

3. To register a new key, click the **[icon: plus, set=fa]**icon.

4. Enter a value for **Key Name**.

5. Select **Sign in with Apple** and click **Configure**.

6. Select the primary App ID you created earlier.

7. Click **Save** and then click **Continue**.

8. Click **Register**.

9. Copy the **Key ID** to a secure location.

   You'll use this value when you add the IdP in DaVinci.

10. To save the key to the local file system, click **Download**.

    The key is saved as a text file with a `.p8` file extension. The key will be used as the client secret signing key and its identifier will be used as the private key in DaVinci.

    |   |                                                                                                                                                                                                                                                    |
    | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | You can only download the key once. Save the file to a secure location because the key is not saved in your developer account, and you won't be able to download it again. If the **Download** button is disabled, you already downloaded the key. |

### Configuring the Apple Login connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

Use the values from the Apple Developer portal to populate the connector's general properties.

| Property                      | Description                                                                                                                                                                                                                                                                                                                          |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Issuer**                    | The Apple **Team ID**. Apple provides this value when the **App ID** is created.                                                                                                                                                                                                                                                     |
| **Key ID**                    | The **Key ID** for the **Sign in with Apple** private key. Apple provides this value when the key is created in **Keys** > **Certificates, Identifiers & Profiles**.                                                                                                                                                                 |
| **Issuer URL**                | `https://appleid.apple.com`                                                                                                                                                                                                                                                                                                          |
| **Authorization Endpoint**    | `https://appleid.apple.com/auth/authorize`                                                                                                                                                                                                                                                                                           |
| **Token Endpoint**            | `https://appleid.apple.com/auth/token`                                                                                                                                                                                                                                                                                               |
| **Client ID**                 | The **Services ID** from Apple Developer.                                                                                                                                                                                                                                                                                            |
| **Private Key**               | Paste the contents of the downloaded Apple private key file with the `.p8` extension. Apple generates this file when the **Sign in with Apple** key is created.	The file can be downloaded only once.                                                                                                                                |
| **Scope**                     | The scopes that determine which user information Apple can return. Configure this property according to the claims required by the application, such as email address or name-related data. Learn more in the [Scope property Apple documentation](https://developer.apple.com/documentation/signinwithapplejs/clientconfigi/scope). |
| **Application Return to URL** | The URL of the app that embeds the DaVinci flow. If you're using redirect, leave this blank.                                                                                                                                                                                                                                         |

#### Attributes

On the **Attributes** tab, review the default attributes available from Apple and define additional attributes when Apple includes them in the ID token returned for the application.

![A screen capture of the Apple Login connector attributes list.](_images/connector-images/dvc-apple-login-attributes-list.png)

|   |                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Apple provides name values only during the first successful **Sign in with Apple** authentication. Subsequent authentications might not include the same name data. |

#### Attribute mapping

On the **Attribute Mapping** tab, map the following default Apple attributes to the DaVinci attributes:

| **Apple Login Attributes** | **DaVinci Attributes** |
| -------------------------- | ---------------------- |
| `sub`                      | `username`             |
| `givenName`                | `firstName`            |
| `familyName`               | `lastName`             |
| `email`                    | `email`                |

## Using the connector in a flow

### Redirecting users to Apple

![A screen capture of the Apple redirect flow.](_images/connector-images/dvc-apple-login-flow.png)

This flow redirects the user to Apple for authentication. After the user signs in, DaVinci automatically completes the token exchange and returns identity claims to the flow for downstream logic.

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Sign in with Apple

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
