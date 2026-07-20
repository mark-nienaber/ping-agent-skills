---
title: ID DataWeb Connector
description: Configure the ID DataWeb connector to integrate AXN Verify identity verification into a PingOne DaVinci flow
component: connectors
page_id: connectors::id_dataweb_connector
canonical_url: https://docs.pingidentity.com/connectors/id_dataweb_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-id-dataweb-connector: Configuring the ID DataWeb connector
  connector-configuration: Connector configuration
  redirect-url: Redirect URL
  client-id: Client ID
  client-secret: Client Secret
  scope: Scope
  axn-federated-gateway-base-url: AXN Federated Gateway Base URL
  custom-gateway-base-url: Custom Gateway Base URL
  data-protection: Data protection
  public-encryption-key: Public Encryption Key
  application-redirect-url: Application Redirect URL
  using-the-connector-in-a-flow: Using the connector in a flow
  verifying-a-user-by-redirecting-them-to-id-dataweb: Verifying a user by redirecting them to ID DataWeb
  capabilities: Capabilities
  initializeAuthorizationRequest: Verification Workflow
---

# ID DataWeb Connector

The ID DataWeb connector lets you use ID DataWeb for identity verification in your PingOne DaVinci flow.

The connector allows you to direct users to ID DataWeb's AXN Verify service where they can enter their information for identity verification. By mapping attributes from your PingOne DaVinci flow, you can pre-populate some of the information requested in the identity verification process. After ID DataWeb verifies the user's identity, it sends the results to PingOne DaVinci where you can branch your flow accordingly.

## Setup

### Resources

Learn more in the following:

* ID DataWeb documentation:

  * [Getting Started](https://docs.iddataweb.com/docs/getting-started)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A configured ID DataWeb environment

* Your ID DataWeb client ID and secret

### Configuring the ID DataWeb connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### Redirect URL

This URL continues the PingOne DaVinci flow when ID DataWeb is finished. Add this URL to the **Redirect URL(s)** list on the **Basic Info** tab of your ID DataWeb verification service configuration. For help, ask an ID DataWeb representative.

##### Client ID

The client ID provided to you by ID DataWeb. This allows PingOne DaVinci to communicate with ID DataWeb.

##### Client Secret

The client secret provided to you by ID DataWeb.

##### Scope

Scopes customize the verification experience and determine the information provided by ID DataWeb. Learn more in [Scopes](https://docs.iddataweb.com/docs/scopes) in the ID DataWeb documentation and speak to an ID DataWeb representative.

Separate multiple scopes with a space. For example, `openid country.US`.

##### AXN Federated Gateway Base URL

The ID DataWeb AXN Federated Gateway to use. Select the production or preproduction server, or use your custom base URL.

* Production

  * PingOne DaVinci uses the live Gateway.

* Preproduction

  * PingOne DaVinci uses the preproduction Gateway. Use this for testing.

* Custom Base URL

**PingOne DaVinci uses the Gateway address that you enter in the \[.uicontrol]**Custom Gateway Base URL\*\* field. Use this if your organization has a custom domain or vanity URL configured for ID DataWeb.

##### Custom Gateway Base URL

When **AXN Federated Gateway Base URL** is set to **Custom Gateway Base URL**, this field determines the AXN Federated Gateway address. Enter your custom Gateway URL, such as `https://mycompany.com/preprod-axn/axn/oauth2`.

##### Data protection

Determines how PingOne DaVinci protects the user data it sends to ID DataWeb.

* Signed

  * PingOne DaVinci sends user data in a signed JSON Web Token (JWT). ID DataWeb can detect whether the data was modified in transit.

* Encrypted

  * PingOne DaVinci sends the user data in an encrypted JWT. Only ID DataWeb can read the data. Select this if you want to use a public encryption key provided by ID DataWeb.

##### Public Encryption Key

When **Data Protection** is set to **Encrypted**, PingOne DaVinci uses this key to encrypt the user data. Enter the a public encryption key provided by ID DataWeb.

##### Application Redirect URL

Your application's redirect URL, such as `http://app.yourorganization.com/`. Enter this URL if you embed the PingOne DaVinci widget in your application. This allows PingOne DaVinci to redirect the browser back to your application.

## Using the connector in a flow

### Verifying a user by redirecting them to ID DataWeb

![A screen capture of the complete verification flow.](_images/connector-images/dvc-id-dataweb-verification-flow.png)

In this flow, an HTML form gathers user data, then the connector directs the browser to ID DataWeb. When the user completes the identity verification process, a simple HTML message shows the result.

1. Download the [ID DataWeb Identity Verification](https://marketplace.pingone.com/item/id-dataweb-identity-verification-davinci-flow) flow template and use it for a new flow. Learn more in [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

2. (Optional) Customize the registration form:

   ![A screen capture of the registration form.](_images/connector-images/dvc-id-dataweb-registration-form.jpg)

   1. Select the **Registration** node.

   2. (Optional) Customize the **Title** field.

   3. (Optional) In the **Fields List** section, customize the user data fields by clicking **Add** to add a new field or clicking **Edit** to remove fields.

   4. (Optional) Customize the **Next Button Text** field.

   5. Click **Apply**.

3. If you customized the user data fields in the **Registration** node, update the attribute mappings for ID DataWeb:

   1. Select the **ID DataWeb** node.

   2. In the **PII Parameters** section, find the ID DataWeb parameter in the **Key** column, then click **{}** in the **Value** column and select the related variable from your **HTML Form** node.

      ![An animated image that shows the user inserting the username variable in the Subject field.](_images/connector-images/dvc-id-dataweb-username-variable.gif)

   3. Click **Apply**.

4. Test the flow:

   1. Click **Save**, **Deploy**, then **Try Flow**.

   2. On the **Registration** page, enter a username, given name, and family name. Click **Sign Up**.

   3. Complete the ID DataWeb verification process.

      Notice that some of the fields are already populated, such as first name and last name.

      ![A screen capture that shows the user's first and last names already populated from the HTML Form node.](_images/connector-images/dvc-id-dataweb-pre-populated-field.jpg)

   4. On the **Verification complete** page, the verification result displays.

      ![A screen capture that shows the verification result in the Custom HTML Message node.](_images/connector-images/dvc-id-dataweb-verification-result.jpg)

## Capabilities

### Verification Workflow

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Subject textField required
>
>   Username/friendly reference to the transaction.
>
> - PII Parameters keyValueList
>
>   Provide ID DataWeb with user information for verification.
>
> - * Display Name button
>   * showPoweredBy toggleSwitch
>   * skipButtonPress toggleSwitch
>
> * default object
>
>   * properties object
>
>     * subject string required
>
>     * piiParams array
>
>     * clientId string required
>
>     * clientSecret string required
>
>     * scope string required
>
>     * gatewayBaseUrl string required
>
>     * customGatewayBaseUrl string
>
>     * dataProtection string required
>
>     * publicEncryptionKey string
>
> - output object
>
>   * statusCode integer
>
>   * rawResponse object
>
>   * policyDecision string
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