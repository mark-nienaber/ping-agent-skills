---
title: PingOne Notifications Connector
description: Configure the PingOne Notifications connector in PingOne DaVinci to send custom voice, SMS, and email notifications using PingOne templates
component: connectors
page_id: connectors::p1_notifications_connector
canonical_url: https://docs.pingidentity.com/connectors/p1_notifications_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  choosing-a-pingone-worker-app: Choosing a PingOne worker app
  setting-up-the-connector: Setting up the connector
  connector-configuration: Connector configuration
  environment-id: Environment ID
  notification-policy-id: Notification Policy ID
  client-id: Client ID
  client-secret: Client Secret
  region: Region
  using-the-connector-in-a-flow: Using the connector in a flow
  capabilities: Capabilities
  sendEmail: Send Email
  sendSms: Send SMS
  sendVoice: Send Voice Message
---

# PingOne Notifications Connector

The PingOne Notifications connector enables you to send custom voice, SMS, and email notifications to cover a wide range of use cases for your customers.

You can create a custom **General** notifications template in PingOne and reference it in the Notifications connector. Learn more in [Notification templates](https://docs.pingidentity.com/pingone/user_experience/p1_notifications.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To add notifications for multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">&#xA;\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>&#xA;\</div>)* use cases, such as push notifications for pairing and authentication within an MFA flow, use the [PingOne MFA Connector](p1_mfa_connector.html). |

## Setup

### Resources

Learn more in the following:

* PingOne documentation:

  * [Introduction to PingOne](https://docs.pingidentity.com/pingone/introduction_to_pingone/p1_introduction.html)

  * [Getting started with PingOne](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started.html)

  * [Notification templates](https://docs.pingidentity.com/pingone/user_experience/p1_notifications.html)

* PingOne DaVinci documentation:

  * [Introduction to PingOne](https://docs.pingidentity.com/pingone/introduction_to_pingone/p1_introduction.html)

  * [Getting started with PingOne](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started.html)

  * [Adding an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html)

### Requirements

To use the PingOne Notifications connector, you must configure a PingOne environment and create the relevant users.

#### Choosing a PingOne worker app

Most environments include a preconfigured worker app that you can use with DaVinci connectors.

To add a worker app:

1. Decide whether to connect to the host PingOne tenant or a different PingOne tenant.

2. In the PingOne admin console, go to **Applications > Applications**.

3. Select the preconfigured **PingOne DaVinci Connection** worker app.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A small number of older environments might not have the preconfigured worker app. If that applies to your environment, you can:- Reuse a worker app you've already created.

- Create a new worker app.

  > **Collapse: Details**
  >
  > To create a new worker app for this connector:
  >
  > 1. Sign on to PingOne.
  >
  > 2. Create a worker app as described in the [PingOne documentation](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html).
  >
  > 3. Make sure you set the authentication method as `Client secret basic`.
  >
  >    The PingOne connector receives a token using your application's credentials.
  >
  > 4. Assign the following roles to the worker app:
  >
  >    * **Identity Data Admin**
  >
  >    * **Environment Admin**
  >
  > 5. Note the **Client ID**, **Client Secret**, and **Environment ID** for the worker app.
  >
  > 6. Click **Finish**.
  >
  > 7. Go to **Applications > Applications**, click the application to open the application details, and click the toggle switch in the upper right to enable the application. |

### Setting up the connector

Add the connector in PingOne DaVinci as shown in [Introduction to PingOne](https://docs.pingidentity.com/pingone/introduction_to_pingone/p1_introduction.html), then configure it as follows.

#### Connector configuration

##### Environment ID

Your PingOne Environment ID. In PingOne, go to **Settings > Environment Properties**.

##### Notification Policy ID

(Optional) The unique identifier of the PingOne notification policy. You can define a notification policy and reference it as part of the connector setup. Learn more in [Notification policies](https://docs.pingidentity.com/pingone/user_experience/p1_creating_a_notification_policy.html).

If a Notification Policy ID is not specified, the default policy is used. In PingOne, go to **User Experience > Notification Policies** and in the **Notification Policies** list, select the **Policy ID** for the policy you want to use.

##### Client ID

The Client ID of your PingOne Worker application that you identified in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app). In PingOne, go to **Applications > Applications > (Your Application) > Configuration**. Expand the **General** section.

##### Client Secret

The Client Secret of your PingOne Worker application that you identified in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app). In PingOne, go to **Applications > Applications > (Your Application) > Configuration**. Expand the **General** section and then click the button to reveal the client secret.

##### Region

Your PingOne environment region. In PingOne, go to **Settings > Environment Properties**.

## Using the connector in a flow

You can use the PingOne Notifications connector to add custom voice, SMS, or email notifications in a flow. The PingOne Notifications connector uses the configurations defined in PingOne, including any customer sender configurations, if defined. You can also specify a PingOne notification policy to apply to the connector.

The PingOne Notifications connector is usually added to an existing flow at the point that you want a notification to be sent.

## Capabilities

### Send Email

Send users customized email messages.

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
>   The unique identifier for the user.
>
> - Email textField required
>
>   The email address to which notifications are sent.
>
> - Notification Name dropDown
>
>   The name of a custom notification defined in PingOne. If the form you want is not listed, select Enter Custom Value.
>
>   * Enter Custom Value
>
> - Custom Value textField
>
>   You can enter a custom template name, or leave blank to use the default template. You can also enter a parameter from a previous connector, or any text.
>
> - Notification Locale textField
>
>   Add a locale to allow localized notifications for end-users. ISO Language Codes are supported.
>
> - Notification Variables variableInputList
>
>   If custom variables are defined in the notification body, map them here.
>
> - Wait For Vendor Response toggleSwitch
>
>   Indicates whether the connector should wait for the notification vendor to respond to the message request.
>
> * default object
>
>   * properties object
>
>     * userId string minLength: 0 maxLength: 100
>
>     * templateVariant null/string
>
>     * customTemplateVariant null/string/object
>
>     * templateLocale null/string
>
>     * templateVariables array
>
>     * email string
>
>     * sendSync boolean
>
>       Send synchronize notification
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * policy object
>
>       * id string
>
>     * deliveryMethod string
>
>     * from string
>
>     * subject string
>
>     * body string
>
>     * address string
>
>     * updatedAt string
>
>     * createdAt string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "id": "00584480-5795-448f-8ade-fcc792c7dbbe",
>     "environment": {
>       "id": "602cc283-b258-444e-acd0-5553330a206c"
>     },
>     "user": {
>       "id": "1528312c-ccff-48ff-be64-3c56d0110aba"
>     },
>     "policy": {
>       "id": "6f5377b1-df6f-4999-9a24-70a7cb534e8e"
>     },
>     "deliveryMethod": "Email",
>     "from": "\"{pingone}\" <noreply@pingidentity.com>",
>     "subject": "Custom email notification",
>     "body": "Hi John, Enter your custom message here",
>     "address": "galdalal@pingidentity.com",
>     "updatedAt": "2022-08-01T14:21:50.010Z",
>     "createdAt": "2022-08-01T14:21:49.560Z"
>   }
> }
> ```

### Send SMS

Send users customized SMS messages.

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
>   The unique identifier for the user.
>
> - Phone Number textField required
>
>   The phone number to which notifications are sent.
>
> - Notification Name dropDown
>
>   The name of a custom notification defined in PingOne. If the form you want is not listed, select Enter Custom Value.
>
>   * Enter Custom Value
>
> - Custom Value textField
>
>   You can enter a custom template name, or leave blank to use the default template. You can also enter a parameter from a previous connector, or any text.
>
> - Notification Locale textField
>
>   Add a locale to allow localized notifications for end-users. ISO Language Codes are supported.
>
> - Notification Variables variableInputList
>
>   If custom variables are defined in the notification body, map them here.
>
> - Wait For Vendor Response toggleSwitch
>
>   Indicates whether the connector should wait for the notification vendor to respond to the message request.
>
> * default object
>
>   * properties object
>
>     * userId string minLength: 0 maxLength: 100
>
>     * templateVariant null/string
>
>     * customTemplateVariant null/string/object
>
>     * templateLocale null/string
>
>     * templateVariables array
>
>     * phone string
>
>     * sendSync boolean
>
>       Send synchronize notification
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * policy object
>
>       * id string
>
>     * deliveryMethod string
>
>     * content string
>
>     * phone string
>
>     * sender string
>
>     * updatedAt string
>
>     * createdAt string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "id": "001b1fc7-a41f-4018-a70e-1c3f7b97a970",
>     "environment": {
>       "id": "602cc283-b258-444e-acd0-5553330a206c"
>     },
>     "user": {
>       "id": "1528312c-ccff-48ff-be64-3c56d0110aba"
>     },
>     "policy": {
>       "id": "6f5377b1-df6f-4999-9a24-70a7cb534e8e"
>     },
>     "deliveryMethod": "SMS",
>     "content": "Enter your custom message here",
>     "phone": "+972547639689",
>     "sender": "+19895464225",
>     "updatedAt": "2022-08-01T14:21:50.010Z",
>     "createdAt": "2022-08-01T14:21:49.560Z"
>   }
> }
> ```

### Send Voice Message

Send users customized voice messages..

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
>   The unique identifier for the user.
>
> - Phone Number textField required
>
>   The phone number to which notifications are sent.
>
> - Notification Name dropDown
>
>   The name of a custom notification defined in PingOne. If the form you want is not listed, select Enter Custom Value.
>
>   * Enter Custom Value
>
> - Custom Value textField
>
>   You can enter a custom template name, or leave blank to use the default template. You can also enter a parameter from a previous connector, or any text.
>
> - Notification Locale textField
>
>   Add a locale to allow localized notifications for end-users. ISO Language Codes are supported.
>
> - Notification Variables variableInputList
>
>   If custom variables are defined in the notification body, map them here.
>
> - Wait For Vendor Response toggleSwitch
>
>   Indicates whether the connector should wait for the notification vendor to respond to the message request.
>
> * default object
>
>   * properties object
>
>     * userId string minLength: 0 maxLength: 100
>
>     * templateVariant null/string
>
>     * customTemplateVariant null/string/object
>
>     * templateLocale null/string
>
>     * templateVariables array
>
>     * phone string
>
>     * sendSync boolean
>
>       Send synchronize notification
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * policy object
>
>       * id string
>
>     * deliveryMethod string
>
>     * content string
>
>     * phone string
>
>     * sender string
>
>     * updatedAt string
>
>     * createdAt string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "id": "002855e3-f505-4142-91b4-bcc252c5efcb",
>     "environment": {
>       "id": "602cc283-b258-444e-acd0-5553330a206c"
>     },
>     "user": {
>       "id": "1528312c-ccff-48ff-be64-3c56d0110aba"
>     },
>     "policy": {
>       "id": "6f5377b1-df6f-4999-9a24-70a7cb534e8e"
>     },
>     "deliveryMethod": "Voice",
>     "content": "Enter your custom message here",
>     "phone": "+972547639689",
>     "sender": "+12106102319",
>     "updatedAt": "2022-08-01T14:21:50.010Z",
>     "createdAt": "2022-08-01T14:21:49.560Z"
>   }
> }
> ```