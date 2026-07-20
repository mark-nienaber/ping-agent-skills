---
title: HYPR Connector
description: Configure the HYPR connector in PingOne DaVinci to enable passwordless authentication using HYPR in your identity flows
component: connectors
page_id: connectors::hypr_connector
canonical_url: https://docs.pingidentity.com/connectors/hypr_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-hypr-connector: Configuring the HYPR connector
  connector-configuration: Connector configuration
  api-url: API URL
  client-id: Client ID
  client-secret: Client secret
  scope: Scope
  using-the-connector-in-a-flow: Using the connector in a flow
  authenticating-users-with-hypr: Authenticating users with HYPR
  capabilities: Capabilities
  initializeAuthorizationRequest: Authenticate
---

# HYPR Connector

The HYPR connector lets you use HYPR for passwordless authentication in your PingOne DaVinci flow.

## Setup

### Resources

Learn more in the following:

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A configured HYPR environment

* A HYPR user account and mobile app to use for testing

### Configuring the HYPR connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

To get your API URL and credentials, speak to a HYPR representative.

##### API URL

The API URL provided to you by HYPR.

##### Client ID

The client ID provided to you by HYPR.

##### Client secret

The client secret provided to you by HYPR.

##### Scope

The [OpenID Connect scopes](https://www.openid.net/specs/openid-connect-basic-1_0.html) to send to HYPR to customize the verification process. Separate multiple scopes with a space, such as `openid email profile`.

## Using the connector in a flow

### Authenticating users with HYPR

![A screen capture of the complete authentication flow.](_images/connector-images/dvc-hypr-authentication-flow.jpg)

This flow asks the user to enter their username in an HTML form, redirects the user to HYPR for authentication, then shows the results on an HTML page.

1. Download the [HYPR Authentication](https://marketplace.pingone.com/item/hypr-authentication-davinci-flow) flow template. Learn more in [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

2. (Optional) Customize the sign on form:

   ![A screen capture of the HTML Form asking for a username.](_images/connector-images/dvc-hypr-sign-on-form.jpg)

   1. Select the **Sign On Form** node.

   2. (Optional) Customize the **Title** field.

   3. (Optional) Customize the **Next Button Text** field.

   4. Click **Apply**.

3. (Optional) Show a HYPR sign-on button rather than automatically redirecting the user to HYPR:

   |   |                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This approach lets you include a HYPR sign-on button alongside other sign-on options in an **IDP Container** connector or as part of a custom HTML page using an [HTTP Connector](http_connector.html) connector. |

   1. Select the **HYPR** node.

   2. Turn off **Skip Button Press**.

   3. In the **Display Name** field, enter the button text, such as `Sign on with HYPR`.

   4. (Optional) In the **CSS** field, add CSS to customize the appearance of the prompt.

   5. (Optional) Turn on **Show Powered By** to display **Powered by Ping Identity** at the bottom of the prompt page.

4. Test the flow:

   1. Click **Save**, **Deploy**, then **Run**.

   2. On the **Sign On** page, enter the username for your HYPR test user account. Click **Sign On**.

      The browser redirects to the HYPR, which prompts you to authenticate.

      ![A screen capture of the HYPR authentication prompt.](_images/connector-images/dvc-hypr-authentication-prompt.jpg)

   3. Complete the MFA process with HYPR.

      ![A screen capture showing the HYPR authentication challenge.](_images/connector-images/dvc-hypr-authentication-challenge.jpg)

      HYPR shows a success message and then redirects the browser back to PingOne DaVinci.

      Your **Custom HTML Message** shows the complete response from HYPR.

      ![A screen capture that shows the Custom HTML Message node with the output from HYPR.](_images/connector-images/dvc-hypr-custom-html-message.jpg)

## Capabilities

### Authenticate

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Username textField
>
>   The username of the authenticating user.
>
> - * Display Name button
>   * showPoweredBy toggleSwitch
>   * skipButtonPress toggleSwitch
>
> * default object
>
>   * properties object
>
>     * username string
>
>     * clientId string required
>
>     * clientSecret string required
>
>     * scope string required
>
>     * apiUrl string required
>
> - output object
>
>   * statusCode integer
>
>   * rawResponse object
>
>   * tokenResponse object
>
>     * id\_token string
>
>     * access\_token string
>
>     * token\_type string
>
>     * expires\_in number