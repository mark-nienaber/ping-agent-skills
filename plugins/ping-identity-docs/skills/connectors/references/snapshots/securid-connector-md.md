---
title: SecurID Connector
description: Configure the SecurID connector to use RSA SecurID multi-factor authentication in your PingOne DaVinci flows
component: connectors
page_id: connectors::securid_connector
canonical_url: https://docs.pingidentity.com/connectors/securid_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-securid-connector: Configuring the SecurID connector
  connector-configuration: Connector configuration
  securid-authentication-api-rest-url: SecurID Authentication API REST URL
  client-key: Client Key
  using-the-connector-in-a-flow: Using the connector in a flow
  authenticating-users: Authenticating users
  capabilities: Capabilities
  initializeRSA: Multi-Factor Authentication (MFA)
  verifyRSA: User Verification
  pollingVerify: Verify Polling
---

# SecurID Connector

The SecurID connector lets you use RSA SecurID for multi-factor authentication (MFA) in your PingOne DaVinci flow.

## Setup

### Resources

Learn more in the following:

* SecurID documentation

  * [Manage the SecurID Authentication API Keys](https://community.securid.com/t5/securid-cloud-authentication/manage-the-securid-authentication-api-keys/ta-p/623093)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need an RSA SecurID Cloud Authentication license

### Configuring the SecurID connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### SecurID Authentication API REST URL

Your authentication API URL, such as `https://company.auth.securid.com`. Learn how to get your URL in [Copy the SecurID Authentication API REST URL](https://community.rsa.com/s/article/Configure-the-RSA-SecurID-Authentication-API-for-Authentication-Agents-b82a1744).

##### Client Key

Your SecurID authentication client key, such as `vowc450ahs6nry66vok0pvaizwnfr43ewsqcm7tz`. Learn how to get a client key in [Add a SecurID Authentication API Key](https://community.rsa.com/s/article/Configure-the-RSA-SecurID-Authentication-API-for-Authentication-Agents-b82a1744).

## Using the connector in a flow

### Authenticating users

![A screen capture of the complete MFA flow.](_images/connector-images/dvc-securid-mfa-flow.png)

This flow allows a user to authenticate with SecurID. It asks the user to enter their user ID in an HTML form, prompts them to select and complete a SecurID authentication method, then shows the results on an HTML page.

Because some authentication methods are completed on the user's mobile device, the flow includes a loop that polls SecurID until the authentication challenge is complete.

1. Download the [SecurID - MFA](https://marketplace.pingone.com/item/securid-mfa) flow template. Learn more in [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

2. (Optional) Customize the sign on form.

   ![A screen capture of the sign on form.](_images/connector-images/dvc-securid-sign-on-form.png)

   1. On the flow canvas, select the **Sign On** node.

   2. In the **Fields List**, customize the **Display Name** to help your users enter their identifier correctly, depending on whether your organization uses a name, ID, or email address.

      |   |                                                                                                                                                                                                                                                                |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The ID entered must match a user in one of the identity sources you have configured in SecurID. Learn more in [Identity Sources for the Cloud Authentication Service](https://community.rsa.com/s/article/Identity-Sources-for-Cloud-Access-Service-bfa10ce4). |

3. (Optional) Customize the assurance policy:

   1. On the flow canvas, select the **Multi-Factor Authentication (SecurID)** node.

   2. In the **Assurance Policy Name** field, enter the policy you want to use, such as `All Users Low Assurance Level`.

      |   |                                                                                                                                                                              |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You can find your policy names in SecurID in **Access > Policies**.![A screen shot of the Policies page in SecurID.](_images/connector-images/dvc-securid-policies-page.jpg) |

      |   |                                                                                                                |
      | - | -------------------------------------------------------------------------------------------------------------- |
      |   | You can set this value dynamically by clicking **{}** and selecting a variable from another node in your flow. |

4. (Optional) Customize the default **Select Authentication Method** interface.

   ![A screen capture of the select authentication method interface.](_images/connector-images/dvc-securid-select-authentication-method.png)

   1. On the flow canvas, select the **User Verification (SecurID)** node.

   2. On the **Select Authentication** tab, modify the **HTML Template**, **CSS**, and **Script** fields.

      |   |                                                                                                                                                                                                                                                                                                      |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | * Click **Switch View** to display the HTML formatted with syntax highlighting.

      * Click the **Maximize**([icon: expand, set=fas]) icon to give yourself more room to work.

      * To access a variety of useful tools, right-click the field when you're in syntax highlighting mode (dark background). |

5. (Optional) Customize the default **SecurID Token Code** interface on the **SecurID Token Code** tab.

   ![A screen capture of the default SecurID token code input interface.](_images/connector-images/dvc-securid-token-code-input.png)

6. (Optional) Customize the default **Emergency Access Token Code** interface on the **Emergency Access Token Code** tab.

   ![A screen capture of the default emergency access token code input interface.](_images/connector-images/dvc-securid-emergency-access.png)

7. (Optional) Customize the default **Check Your Device** interface.

   ![A screen capture of the Check Your Device interface.](_images/connector-images/dvc-securid-check-your-device.png)

   1. On the flow canvas, select the **Check Your Device** node.

   2. Modify the **Message Title**, **Message**, and other fields.

8. Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Multi-Factor Authentication (MFA)

Get the user's authentication methods and start the authentication process.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User Identifier textField
>
>   The unique identifier for the user, such as an email, account name, user ID.
>
> - Assurance Policy Name textField
>
>   The name of your SecurID policy, such as "All Users Low Assurance Level".
>
> - Keep Record toggleSwitch
>
>   When enabled, SecurID keeps a record of each completed transaction.
>
> - Authentication Attempt Timeout textField
>
>   A number in seconds representing how long the server will keep the authentication attempt ID available after each call. During this time is is possible to make other calls using the "authnAttemptId". The server may reject initialization requests if the value provided is beyond the allowable maximum. Defaults to a server-defined session lifetime. Optional.
>
> * default object
>
>   * properties object
>
>     * subjectName string required
>
>     * assurancePolicyId string required
>
>     * apiUrl string required
>
>     * clientKey string required
>
> - output object
>
>   * headers object
>
>     * vary string
>
>     * cache-control string
>
>     * content-type string
>
>     * strict-transport-security string
>
>     * date string
>
>     * keep-alive string
>
>     * expires string
>
>     * x-xss-protection string
>
>     * pragma string
>
>     * transfer-encoding string
>
>     * x-content-type-options string
>
>     * connection string
>
>     * x-frame-options string
>
>   * status integer
>
>   * data object
>
>     * context object
>
>       * authnAttemptId string
>
>       * messageId string
>
>       * inResponseTo string
>
>     * credentialValidationResults array
>
>       * Array Item Schema object
>
>         * methodId string
>
>         * methodResponseCode string
>
>         * methodReasonCode string
>
>         * authnAttributes array
>
>     * attemptResponseCode string
>
>     * attemptReasonCode string
>
>     * challengeMethods object
>
>       * challenges array
>
>         * Array Item Schema object
>
>           * methodSetId string
>
>           * requiredMethods array
>
>             * Array Item Schema object
>
>               * methodId string
>
>               * displayName string
>
>               * priority integer
>
>               * versions array
>
>                 * Array Item Schema object
>
>                   * versionId string
>
>                   * methodAttributes array
>
>                     * Array Item Schema object
>
>                       * name string
>
>                       * value string
>
>                       * dataType string
>
>                   * valueRequired boolean
>
>                   * referenceId null
>
>                   * prompt object
>
>                     * promptResourceId string
>
>                     * defaultText string
>
>                     * formatRegex null
>
>                     * defaultValue null
>
>                     * valueBeingDefined boolean
>
>                     * sensitive boolean
>
>                     * minLength null
>
>                     * maxLength null
>
>                     * promptArgs array

### User Verification

Prompt the user to select a method and complete the authentication process.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - default object
>
>   * properties object
>
>     * apiUrl string required
>
>     * clientKey string required
>
> * output object
>
>   * challenge string
>
>   * headers object
>
>     * vary string
>
>     * cache-control string
>
>     * content-type string
>
>     * strict-transport-security string
>
>     * date string
>
>     * keep-alive string
>
>     * expires string
>
>     * x-xss-protection string
>
>     * pragma string
>
>     * transfer-encoding string
>
>     * x-content-type-options string
>
>     * connection string
>
>     * x-frame-options string
>
>   * status integer
>
>   * data object
>
>     * context object
>
>       * authnAttemptId string
>
>       * messageId string
>
>       * inResponseTo string
>
>     * credentialValidationResults array
>
>       * Array Item Schema object
>
>         * methodId string
>
>         * methodResponseCode string
>
>         * methodReasonCode string
>
>         * authnAttributes array
>
>     * attemptResponseCode string
>
>     * attemptReasonCode string
>
>     * challengeMethods object
>
>       * challenges array
>
>         * Array Item Schema object
>
>           * methodSetId string
>
>           * requiredMethods array
>
>             * Array Item Schema object
>
>               * methodId string
>
>               * displayName string
>
>               * priority integer
>
>               * versions array
>
>                 * Array Item Schema object
>
>                   * versionId string
>
>                   * methodAttributes array
>
>                     * Array Item Schema object
>
>                       * name string
>
>                       * value string
>
>                       * dataType string
>
>                   * valueRequired boolean
>
>                   * referenceId null
>
>                   * prompt object
>
>                     * promptResourceId string
>
>                     * defaultText string
>
>                     * formatRegex null
>
>                     * defaultValue null
>
>                     * valueBeingDefined boolean
>
>                     * sensitive boolean
>
>                     * minLength null
>
>                     * maxLength null
>
>                     * promptArgs array

### Verify Polling

Use this to poll from securid

> **Collapse: Show details**
>
> * Input Schema
>
> * Output Schema
>
> - default object
>
>   * properties object
>
>     * apiUrl string required
>
>     * clientKey string required
>
> * output object
>
>   * result string