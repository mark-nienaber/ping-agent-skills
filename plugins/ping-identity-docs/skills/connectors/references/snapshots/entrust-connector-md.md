---
title: Entrust Connector
description: The Entrust connector lets you use Entrust adaptive authentication in your PingOne DaVinci flow.
component: connectors
page_id: connectors::entrust_connector
canonical_url: https://docs.pingidentity.com/connectors/entrust_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  adding-an-application-in-entrust: Adding an application in Entrust
  configuring-the-entrust-connector: Configuring the Entrust connector
  connector-configuration: Connector configuration
  service-domain: Service Domain
  application-id: Application ID
  using-the-connector-in-a-flow: Using the connector in a flow
  authentication: Authentication
  capabilities: Capabilities
  auth: Authenticate
---

# Entrust Connector

The Entrust connector lets you use Entrust adaptive authentication in your PingOne DaVinci flow.

You can use the Entrust connector to:

* Profile a user's device and perform multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
  \<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
  \</div>)* using:

  * A one-time passcode (OTP) *(tooltip: \<div class="paragraph">
    \<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
    \</div>)* through SMS or email

  * A time-based one-time passcode (TOTP) through a hardware or software token

## Setup

### Resources

Learn more in the following:

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need an Entrust license.

### Adding an application in Entrust

The connector needs an application ID to communicate with Entrust.

To get the application ID, complete the steps in "Integrate Authentication API with Identity as a Service" in the Entrust administrator documentation.

For a direct link to the documentation, modify the following URL: `https://<your Entrust domain>/documentation/help/admin/index.htm#t=Resources%2FAdd_Authentication_API.htm`

1. For **Source of Client IP Address for Risk Conditions**, select **From the incoming HTTP connection**.

2. Copy the **Application ID**. You'll use it when you set up the connector configuration.

3. Configure a resource rule as described in the Entrust documentation.

### Configuring the Entrust connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### Service Domain

Your Entrust domain. For example, "company.us.trustedauth.com".

##### Application ID

The ID of your Entrust application.

## Using the connector in a flow

### Authentication

![A screen capture of the complete authentication flow.](_images/connector-images/dvc-entrust-authentication-flow.png)

This flow asks a user to authenticate with Entrust. It asks the user to enter their user ID in an HTML form, prompts them to select and complete a Entrust authentication method, then shows the results on an HTML page.

1. Download the [Entrust Authentication](https://support.pingidentity.com/s/marketplace-integration/a7iDo0000010wzNIAQ/entrust-authentication-davinci-flow) flow template. Learn more in [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

2. (Optional) Add transaction details:

   1. On the flow canvas, select the **Authenticate (Entrust)** node.

   2. On the **General** tab, in the **Transaction Details** section, add attributes as key-value pairs. These are sent to Entrust as part of the authentication process.

      |   |                                                                                                              |
      | - | ------------------------------------------------------------------------------------------------------------ |
      |   | You can dynamically populate values by clicking **{}** and selecting a variable from elsewhere in your flow. |

3. (Optional) Customize the default **Authenticator Selection** interface.

   ![A screen capture of the default authenticator selection interface.](_images/connector-images/dvc-entrust-default-authenticator-selection.png)

   1. On the flow canvas, select the **Authenticate (Entrust)** node.

   2. On the **Custom** tab, in the **Select Authenticator** section, modify the **HTML Template**, **CSS**, and **Script** fields.

      |   |                                                                                                                                                                                                                                                                                                                                                                                |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | * Click **Switch View** to display the HTML formatted with syntax highlighting.

      * Click the **Maximize**(![A screen capture of the Maximize icon.](_images/connector-images/dvc-entrust-maximize-icon.jpg)) icon to give yourself more room to work.

      * To access a variety of useful tools, right-click the field when you're in syntax highlighting mode (dark background). |

4. (Optional) Modify the default **OTP Input** interface on the **Custom** tab.

   ![A screen capture of the default OTP input interface.](_images/connector-images/dvc-entrust-detault-otp-input.png)

5. (Optional) Modify the default **Token Input** interface on the **Custom** tab.

   ![A screen capture of the default token input interface.](_images/connector-images/dvc-entrust-default-token-input.png)

6. Test the flow.

   1. Click **Save**, **Deploy**, then **Try Flow**.

   2. On the **Sign On** page, enter your Entrust user ID, such as `jsmith@example.com`.

   3. Select your authentication method and complete the authentication process.

   4. See the result of the authentication process.

## Capabilities

### Authenticate

Authenticate users with Entrust.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField required
>
>   The unique ID of the user you want to authenticate.
>
> - Transaction Details keyValueList
>
>   Additional transaction details to send to Entrust.
>
> * default object
>
>   * properties object
>
>     * serviceDomain string required
>
>     * applicationId string required
>
>     * userId string required
>
> - output object
>
>   * statusCode integer
>
>   * rawResponse object
