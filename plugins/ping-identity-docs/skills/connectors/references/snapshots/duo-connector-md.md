---
title: Duo Connector
description: Configure the Duo connector to add Duo multi-factor authentication to your PingOne DaVinci flows
component: connectors
page_id: connectors::duo_connector
canonical_url: https://docs.pingidentity.com/connectors/duo_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  getting-your-application-credentials: Getting your application credentials
  setting-up-the-duo-connector-configuration: Setting up the Duo connector configuration
  connector-configuration: Connector configuration
  client-id: Client ID
  client-secret: Client secret
  api-hostname: API Hostname
  using-the-connector-in-a-flow: Using the connector in a flow
  authenticating-users-with-duo-multi-factor-authentication: Authenticating users with Duo multi-factor authentication
  capabilities: Capabilities
  initializeMfa: Multi-factor authentication (MFA)
---

# Duo Connector

The Duo connector lets you use Duo for multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* in your PingOne DaVinci flow.

## Setup

### Resources

Learn more in the following documentation:

* Duo documentation

  * [Getting Started with Duo Security](https://duo.com/docs/getting-started)

  * [Protect an Application](https://duo.com/docs/protecting-applications)

  * [Policy & Control](https://duo.com/docs/policy)

  * [What is the Duo Universal Prompt?](https://help.duo.com/s/article/6340?language=en_US)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A configured Duo environment

* A Duo user account to use for testing

### Getting your application credentials

1. In Duo, add an application. Learn more in [Protecting an application](https://duo.com/docs/protecting-applications) in the Duo documentation.

2. Select **PingFederate** as the application type.

3. Note your **Client ID**, **Client secret** , and **API hostname**. You'll use these in the connector configuration.

4. Click **Save**.

### Setting up the Duo connector configuration

In PingOne DaVinci, add a **Duo** connection. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

#### Connector configuration

##### Client ID

The **Client ID** that you noted in **Getting your application credentials**.

##### Client secret

The **Client secret** that you noted in **Getting your application credentials**.

##### API Hostname

The **API hostname** that you noted in **Getting your application credentials**.

## Using the connector in a flow

### Authenticating users with Duo multi-factor authentication

![A screen capture of the complete MFA flow.](_images/connector-images/dvc-duo-mfa-flow.jpg)

Complete the steps below to create a flow that asks the user to enter their username in an HTML form, uses the connector to redirect them to Duo, then shows the results on an HTML page.

|   |                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Duo's Universal Prompt experience doesn't provide a "Cancel" option that would let the user exit MFA and return to the PingOne DaVinci flow. Because of this, it's possible for Duo to become a dead end in the user experience if they can't successfully complete MFA. |

1. Create a sign on form:

   1. In a new flow, add the **HTTP** connector and select the **HTML Form** capability. Select the node that appears in your flow.

      |   |                                                                                                                                                               |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | In this example flow, we'll collect the username in a form. When you build your own flow, this is where you should add your first-factor authentication step. |

      ![A screen capture of the HTML Form asking for a username.](_images/connector-images/dvc-duo-username-form.jpg)

      |   |                                                                                                   |
      | - | ------------------------------------------------------------------------------------------------- |
      |   | Learn more in the [HTTP](https://docs.pingidentity.com/connectors/http_connector.html) connector. |

   2. In the **Title** field, enter a title, such as `Sign On`.

   3. In the **Fields List** section, click **Add**.

   4. In the **Property Name** field, enter `username`.

   5. In the **Display Name** field, enter `Username`

   6. In the **Next Button Text** field, enter `Sign On`.

   7. Click **Apply**.

2. Redirect the user to Duo for MFA:

   1. Following your **HTML Form** node in your flow, add the **Duo** connector and select the **Multi-factor authentication (MFA)** capability. Select the node that appears in your flow.

   2. In the **User ID** field, click **{}** and select the **username** variable from your **HTML Form** node.

      ![An animated screen capture that shows the user inserting the username variable in the User ID field.](_images/connector-images/dvc-duo-username-variable.gif)

   3. (Optional) If you want the flow to show a Duo sign-on button rather than automatically redirecting the user to Duo, do the following:

      |   |                                                                                                                                                                                                                                        |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | This lets you include a Duo sign-on button alongside other sign-on options in an **IDP Container** connector or as part of a custom HTML page using an [HTTP](https://docs.pingidentity.com/connectors/http_connector.html) connector. |

      1. Turn off **Skip Button Press**.

      2. In the **Display Name** field, enter the button text, such as `Sign on with Duo`.

      3. (Optional) In the **CSS** field, add CSS to customize the appearance of the prompt.

      4. (Optional) Turn on **Show Powered By** to display **Powered by Ping Identity** at the bottom of the prompt page.

   4. Click **Apply**.

3. Show the response from Duo:

   1. Following your **Multi-factor authentication (MFA)** node, add an **HTTP** connector and select the **Custom HTML Message** capability. Select the node that appears in your flow.

      |   |                                                                                                                                                                                             |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | In this example flow, we'll show the user the response from Duo. When you build your own flow, this is where you should redirect the user to the resource they originally wanted to access. |

   2. In the **Title** field, enter `Sign on complete`.

   3. In the **Message** field, click **{}** and select the **rawResponse** variable from your **Multi-factor authentication (MFA)** node.

      ![An animated screen capture that shows the user inserting the rawResponse variable in the Message field.](_images/connector-images/dvc-duo-rawresponse-variable.gif)

   4. Click **Apply**.

4. Test the flow.

   1. Click **Save**, **Deploy**, then **Run**.

   2. On the **Sign On** page, enter the username for your Duo test user account. Click **Sign On**.

      Result: The browser redirects to the Duo MFA experience, such as Universal Prompt.

      ![A screen capture of the Duo Universal Prompt experience.](_images/connector-images/dvc-duo-universal-prompt.jpg)

   3. Complete the MFA process with Duo.

      Duo shows a success message, then redirects the browser back to PingOne DaVinci.

      ![A screen capture showing the Universal Prompt success message.](_images/connector-images/dvc-duo-universal-prompt-success-message.jpg)

      Your **Custom HTML Message** shows the complete response from Duo.

      ![A screen capture that shows the Custom HTML Message node with the raw response from Duo.](_images/connector-images/dvc-duo-raw-response.jpg)

Learn more in the [Creating an authentication flow](https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_creating_an_authentication_flow.html) guide.

## Capabilities

### Multi-factor authentication (MFA)

Redirect to Duo for multi-factor authentication.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - - Username textField required
>   - Display Name button
>   - showPoweredBy toggleSwitch
>   - skipButtonPress toggleSwitch
>
> * default object
>
>   * properties object
>
>     * username string required
>
>       Username
>
>     * clientSecret string required
>
>     * clientId string required
>
>     * apiHostname string required
>
>       API Hostname
>
> - output object
>
>   * rawResponse object
>
>     * access\_token string
>
>     * id\_token string
>
>     * expires\_in integer
>
>     * token\_type string
>
>   * statusCode integer
>
>   * headers object
>
>     * server string
>
>     * date string
>
>     * content-type string
>
>     * content-length string
>
>     * connection string
>
>     * cache-control string
>
>     * pragma string
>
>     * strict-transport-security string
>
>     * content-security-policy string
>
>   * tokens object
>
>     * access\_token string
>
>     * id\_token string
>
>     * expires\_in integer
>
>     * token\_type string
>
>   * iss string
>
>   * sub string
>
>   * aud string
>
>   * exp integer
>
>   * iat integer
>
>   * auth\_time integer
>
>   * auth\_result object
>
>     * result string
>
>     * status string
>
>     * status\_msg string
>
>   * auth\_context object
>
>     * txid string
>
>     * timestamp integer
>
>     * user object
>
>       * name string
>
>       * key string
>
>       * groups array
>
>     * application object
>
>       * name string
>
>       * key string
>
>     * auth\_device object
>
>       * ip string
>
>       * location object
>
>         * city string
>
>         * state string
>
>         * country string
>
>       * name string
>
>     * access\_device object
>
>       * ip string
>
>       * location object
>
>         * city string
>
>         * state string
>
>         * country string
>
>       * hostname null
>
>       * epkey string
>
>     * factor string
>
>     * event\_type string
>
>     * result string
>
>     * reason string
>
>     * alias string
>
>     * isotimestamp string
>
>     * email string
>
>     * ood\_software null
>
>   * preferred\_username string
>
>   * nonce string