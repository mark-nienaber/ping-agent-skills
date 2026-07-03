---
title: Microsoft Teams Connector
description: The Microsoft Teams connector lets you manage user memberships and send messages in Microsoft Teams from your PingOne DaVinci flow.
component: connectors
page_id: connectors::microsoft_teams_connector
canonical_url: https://docs.pingidentity.com/connectors/microsoft_teams_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  davinci-microsoft-teams-setting-up-microsoft-teams: Setting up Microsoft Teams
  configuring-the-microsoft-teams-connector: Configuring the Microsoft Teams connector
  connector-configuration: Connector configuration
  davinci-redirect-url: DaVinci Redirect URL
  application-redirect-url: Application Redirect URL
  client-id: Client ID
  client-secret: Client Secret
  tenant-id: Tenant ID
  using-the-connector-in-a-flow: Using the connector in a flow
  managing-team-and-channel-memberships: Managing team and channel memberships
  sending-a-message-to-a-channel: Sending a message to a channel
  sending-a-message-to-a-chat: Sending a message to a chat
  listing-a-users-chats: Listing a user's chats
  creating-a-custom-api-call: Creating a custom API call
  capabilities: Capabilities
  addMember: Add a Member to a Team
  removeMember: Remove a Member from a Team
  listMembers: List Team Members
  addMemberToChannel: Add a Member to a Channel
  removeMemberFromChannel: Remove a Member from a Channel
  listMembersInChannel: List Channel Members
  sendMessageChannel: Send Message in a Channel
  sendMessageChat: Send Message in a Chat
  listChats: List Chats
  initializeAuthorizationRequest: Sign on with Microsoft
  makeCustomApiCall: Make a Custom API Call
---

# Microsoft Teams Connector

The Microsoft Teams connector lets you manage user memberships and send messages in Microsoft Teams from your PingOne DaVinci flow.

You can use the Microsoft Teams connector to:

* Add, remove, and list members of a team

* Add, remove, and list members of a channel

* Send messages in channels and chats

* Define custom API calls to Microsoft Azure

## Setup

### Resources

Learn more in the following:

* Microsoft documentation:

  * [Register an application with the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A Microsoft Teams account

* Administrator access to Microsoft Azure

### Setting up Microsoft Teams

1. Sign on to the [Azure portal](https://portal.azure.com/).

2. Create the application:

   1. Search for and select **Azure Active Directory**.

   2. Under **Manage**, select **App registrations > New registration**.

   3. On the **Register an Application** page, for **Supported account types**, select **Accounts in any organizational directory and personal Microsoft accounts**.

   4. In the **Redirect URI** section, select **Web** and add the redirect URL for your DaVinci environment, such as:

      ```
      https://auth.pingone.com/79d0edb0-4421-1bcb-acb5-222e3132eb5b/davinci/oauth2/callback
      ```

      To get your redirect URL, add a **Microsoft Teams** connection in DaVinci, open the connection settings, and copy the **Redirect URL**. Learn more about adding the connection in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

      ![A screen capture of the Redirect URL on the Microsoft Teams connector settings window.](_images/connector-images/dvc-microsoft-teams-redirect-url.png)

   5. Click **Register**.

3. On your app's **Overview** page, note the **Application (client) ID** and **Directory (tenant) ID**. You'll use these in the connector configuration.

   ![A screen capture of the application details page in Microsoft Azure.](_images/connector-images/dvc-microsoft-teams-application-details.png)

4. Create a client secret:

   1. Under **Manage**, click **Certificates & secrets**. On the **Client secrets** tab, click **New client secret**.

   2. Enter a name and select an expiry time. Click **Add.**

   3. Note the **Value** of the secret. You'll use this in the connector configuration.

      ![A screen capture of the client secret in Microsoft Azure.](_images/connector-images/dvc-microsoft-teams-client-secret.png)

5. Give the connector permission to manage users and send messages:

   1. Under **Manage**, click **API permissions**.

   2. Click **Add a permission** and add the following Microsoft Graph API permissions:

      | Type            | Permission                        |
      | --------------- | --------------------------------- |
      | **Delegated**   | **User.Read**                     |
      | **Delegated**   | **ChannelMessage.Send**           |
      | **Delegated**   | **Chat.ReadWrite**                |
      | **Delegated**   | **ChatMessage.Send**              |
      | **Delegated**   | **offline\_access**               |
      | **Application** | **ChannelMember.ReadWrite.All**   |
      | **Application** | **ChannelSettings.ReadWrite.All** |
      | **Application** | **Chat.ReadWrite.All**            |
      | **Application** | **Group.Read.All**                |
      | **Application** | **TeamMember.ReadWrite.All**      |
      | **Application** | **User.ReadWrite.All**            |

### Configuring the Microsoft Teams connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### DaVinci Redirect URL

Your DaVinci redirect URL. This allows Microsoft to redirect the browser back to DaVinci. after the user authenticates with the **Sign on with Microsoft** capability. Use this in [Setting up Microsoft Teams](#davinci-microsoft-teams-setting-up-microsoft-teams).

##### Application Redirect URL

Your application's redirect URL, such as `https://app.yourorganization.com`. Enter this URL if you embed the DaVinci widget in your application. This allows DaVinci to redirect the browser back to your application.

##### Client ID

The **Application (client) ID** that you noted in [Setting up Microsoft Teams](#davinci-microsoft-teams-setting-up-microsoft-teams).

##### Client Secret

The client secret **Value** that you noted in [Setting up Microsoft Teams](#davinci-microsoft-teams-setting-up-microsoft-teams).

##### Tenant ID

The **Directory (tenant) ID** that you noted in [Setting up Microsoft Teams](#davinci-microsoft-teams-setting-up-microsoft-teams).

## Using the connector in a flow

### Managing team and channel memberships

The connector has several capabilities that allow you to manage the users that belong to each team or channel in Microsoft Teams:

* Teams:

  * **Add a Member to a Team**

  * **Remove a Member from a Team**

  * **List Team Members**

* Channels:

  * **Add a Member to a Channel**

  * **Remove a Member from a Channel**

  * **List Channel Members**

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Sending a message to a channel

![A screen capture of the complete send message flow.](_images/connector-images/dvc-microsoft-teams-send-message-flow.png)

You can use the connector to send a message to a channel.

This flow requires the user to sign on with Microsoft and agree to let the connector send messages on their behalf. The **Sign on with Microsoft** node directs the browser to Microsoft. After the user signs on, Microsoft redirects the browser back to DaVinci to continue the flow.

1. Download the [Microsoft Teams Channel Message](https://marketplace.pingone.com/item/microsoft-teams-channel-message-davinci-flow) flow template. Learn more in [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

2. Select the **Send Message in Channel** node.

3. In the **Team** list, select the team associated with the channel or select **Use Team ID** and enter an ID in the **Team ID** field, such as `98c28bef-98f1-a658-435b-71eee19c8f5e`.

4. In the **Channel** list, select the channel or select **Use Channel ID** and enter an ID in the **Channel ID** field, such as `98c28bef-a658-435b-98f1-71eee19c8f5e`.

5. Click **Apply**.

6. Test the flow:

   1. Click **Save**, **Deploy**, and **Try Flow**.

   2. In Microsoft Teams, check the channel to display the message.

### Sending a message to a chat

![A screen capture of the complete send message flow.](_images/connector-images/dvc-microsoft-teams-send-message-chat.png)

You can use the connector to send a message to a chat.

This flow requires the user to sign on with Microsoft and agree to let the connector send messages on their behalf. The **Sign on with Microsoft** node directs the browser to Microsoft. After the user signs on, Microsoft redirects the browser back to DaVinci to continue the flow.

The flow also requires a chat ID. You can find more information about getting a chat ID, in **Listing a User's Chats**.

1. Download the [Microsoft Teams - Chat message](https://marketplace.pingone.com/item/microsoft-teams-chat-message) flow template. Learn more in [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

2. Select the **Send a Message in a Chat** node.

3. In the **Chat ID** field, enter the unique ID of one of the user's chats, such as `19:ce95abaa0e9f4d22a0e0faa6aad76c56@thread.v2`. You can find more information about getting a chat ID in **Listing a User's Chats**.

4. In the **Message Object** field, create a JSON object with the message details. This allows you to use all features supported by the Microsoft Graph API, such as HTML formatting, user @mentions, and file attachments.

   For example:

   ```json
   {
     "body": {
       "contentType": "html",
       "content": "Welcome, <at id=\"0\">Jane Smith</at>"
     },
     "mentions": [
       {
         "id": 0,
         "mentionText": "Jane Smith",
         "mentioned": {
           "user": {
             "displayName": "Jane Smith",
             "id": "19:ce95abaa0e9f4d22a0e0faa6aad76c56@thread.v2",
             "userIdentityType": "aadUser"
           }
         }
       }
     ]
   }
   ```

   Learn more about creating the JSON object in [Chat message](https://docs.microsoft.com/en-us/graph/api/resources/chatmessage?view=graph-rest-1.0) in the Microsoft Graph API documentation.

5. Click **Apply**.

6. Test the flow:

   1. Click **Save**, **Deploy**, and **Try Flow**.

   2. In Microsoft Teams, check the chat to display the message.

### Listing a user's chats

![A screen capture of the complete List Chats flow.](_images/connector-images/dvc-microsoft-teams-listing-chats.png)

You can use the connector to get a list of chats that the user belongs to. You can use the chat IDs from this flow to send messages to specific chats.

Download the [Microsoft Teams - Chat list](https://marketplace.pingone.com/item/microsoft-teams-chat-list) flow template. Learn more in [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

This flow requires the user to sign on with Microsoft and agree to let the connector send messages on their behalf. The **Sign on with Microsoft** node directs the browser to Microsoft. After the user signs on, Microsoft redirects the browser back to DaVinci to continue the flow.

The **Custom HTML Message** node shows a list of chats. You can copy a chat ID to send messages to that chat on behalf of the user.

![A screen capture of the output from the List Chats capability.](_images/connector-images/dvc-microsoft-teams-chats-list.png)

### Creating a custom API call

If you want to do something that isn't supported by one of the provided capabilities, you can use the **Make a Custom API Call** capability to define your own action.

This capability uses the credentials from your connection to make an API call with the HTTP method, headers, query parameters, and body you specify.

## Capabilities

### Add a Member to a Team

Add a member to a team and assign a display name.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Member dropDown required
>
>   The member to target. For a dynamic value, select Use Member ID and enter a value in the Member ID field.
>
>   * Use Member/Membership ID
>
> - Member ID textField
>
>   The ID of the member, such as "0b2b7c5b-4eb2-5c7b-a94b-bea34ac31c30".
>
> - Team dropDown required
>
>   The team to target. For a dynamic value, select Use Team ID and enter a value in the Team ID field.
>
>   * Use team ID
>
> - Team ID textField
>
>   The ID of the team, such as "0b2b7c5b-4eb2-5c7b-a94b-bea34ac31c30".
>
> - Roles textFieldArrayView
>
>   The roles to assign to the member, such as "owner" or "guest". Basic members should not have any assigned roles. Type a role name and press Enter to add it.
>
> - Display Name textField
>
>   The display name to assign to the member.
>
> * default object
>
>   * properties object
>
>     * clientId string required
>
>     * clientSecret string required
>
>     * tenantId string required
>
>     * members string required
>
>     * memberId string
>
>     * teams string required
>
>     * teamId string
>
>     * roles array
>
>     * displayName string
>
> - output object
>
>   * rawResponse object
>
>     * @odata.context string
>
>     * @odata.type string
>
>     * id string
>
>     * roles array
>
>     * displayName string
>
>     * visibleHistoryStartDateTime string
>
>     * userId string
>
>     * email string
>
>     * tenantId string
>
>   * statusCode integer
>
>   * headers object
>
>     * transfer-encoding string
>
>     * content-type string
>
>     * location string
>
>     * strict-transport-security string
>
>     * request-id string
>
>     * client-request-id string
>
>     * x-ms-ags-diagnostic string
>
>     * odata-version string
>
>     * date string
>
>     * connection string

### Remove a Member from a Team

Remove a member from team.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Team dropDown required
>
>   The team to target. For a dynamic value, select Use Team ID and enter a value in the Team ID field.
>
>   * Use team ID
>
> - Team ID textField
>
>   The ID of the team, such as "0b2b7c5b-4eb2-5c7b-a94b-bea34ac31c30".
>
> - Member dropDown required
>
>   The member to target. For a dynamic value, select Use Member ID and enter a value in the Member ID field.
>
>   * Use Member/Membership ID
>
> - Membership ID textField
>
>   The ID of the membership, such as "MCMjMSMjMDdlYzlhZjItN2NlNS00YWI3LTg2MzgtMTE1NzM2YmJmOTkwIyM5OGMyOGJlZi05OGYxLTQzNWItYTY1OC03MWVlZTE5YzhmNWUjI2U5MTk4MzA3LTRlMzItNDgwMC1hM2M1LTExNTUxYWQ4MzFhMg=="
>
> * default object
>
>   * properties object
>
>     * clientId string required
>
>     * clientSecret string required
>
>     * tenantId string required
>
>     * members string required
>
>     * membershipId string
>
>     * teams string required
>
>     * teamId string
>
> - output object
>
>   * rawResponse string
>
>   * statusCode integer
>
>   * headers object
>
>     * strict-transport-security string
>
>     * request-id string
>
>     * client-request-id string
>
>     * x-ms-ags-diagnostic string
>
>     * date string
>
>     * connection string

### List Team Members

Get a list of members of a team.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Team dropDown required
>
>   The team to target. For a dynamic value, select Use Team ID and enter a value in the Team ID field.
>
>   * Use team ID
>
> - Team ID textField
>
>   The ID of the team, such as "0b2b7c5b-4eb2-5c7b-a94b-bea34ac31c30".
>
> * default object
>
>   * properties object
>
>     * clientId string required
>
>     * clientSecret string required
>
>     * tenantId string required
>
>     * teams string required
>
>     * teamId string
>
> - output object
>
>   * rawResponse object
>
>     * @odata.context string
>
>     * @odata.count integer
>
>     * value array
>
>       * Array Item Schema object
>
>         * @odata.type string
>
>         * id string
>
>         * roles array
>
>         * displayName string
>
>         * visibleHistoryStartDateTime string
>
>         * userId string
>
>         * email null/string
>
>         * tenantId string
>
>   * statusCode integer
>
>   * headers object
>
>     * transfer-encoding string
>
>     * content-type string
>
>     * strict-transport-security string
>
>     * request-id string
>
>     * client-request-id string
>
>     * x-ms-ags-diagnostic string
>
>     * odata-version string
>
>     * date string
>
>     * connection string

### Add a Member to a Channel

Add a member to a channel and assign a display name.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Team dropDown required
>
>   The team to target. For a dynamic value, select Use Team ID and enter a value in the Team ID field.
>
>   * Use team ID
>
> - Team ID textField
>
>   The ID of the team, such as "0b2b7c5b-4eb2-5c7b-a94b-bea34ac31c30".
>
> - Channel dropDown required
>
>   The channel to target. For a dynamic value, select Use Channel ID and enter a value in the Channel ID field.
>
>   * Use channel ID
>
> - Channel ID textField required
>
>   The ID of the channel to target, such as "0b2b7c5b-4eb2-5c7b-a94b-bea34ac31c30".
>
> - Member dropDown required
>
>   The member to target. For a dynamic value, select Use Member ID and enter a value in the Member ID field.
>
>   * Use Member/Membership ID
>
> - Member ID textField
>
>   The ID of the member, such as "0b2b7c5b-4eb2-5c7b-a94b-bea34ac31c30".
>
> - Roles textFieldArrayView
>
>   The roles to assign to the member, such as "owner" or "guest". Basic members should not have any assigned roles. Type a role name and press Enter to add it.
>
> - Display Name textField
>
>   The display name to assign to the member.
>
> * default object
>
>   * properties object
>
>     * clientId string required
>
>     * clientSecret string required
>
>     * tenantId string required
>
>     * teams string required
>
>     * teamId string
>
>     * channels string required
>
>     * channelId string
>
>     * members string required
>
>     * memberId string
>
>     * roles array
>
>     * displayName string
>
> - output object
>
>   * rawResponse object
>
>     * @odata.context string
>
>     * @odata.type string
>
>     * id string
>
>     * roles array
>
>     * displayName string
>
>     * visibleHistoryStartDateTime string
>
>     * userId string
>
>     * email string
>
>     * tenantId string
>
>   * statusCode integer
>
>   * headers object
>
>     * transfer-encoding string
>
>     * content-type string
>
>     * location string
>
>     * strict-transport-security string
>
>     * request-id string
>
>     * client-request-id string
>
>     * x-ms-ags-diagnostic string
>
>     * odata-version string
>
>     * date string
>
>     * connection string

### Remove a Member from a Channel

Remove a member from a channel.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Team dropDown required
>
>   The team to target. For a dynamic value, select Use Team ID and enter a value in the Team ID field.
>
>   * Use team ID
>
> - Team ID textField
>
>   The ID of the team, such as "0b2b7c5b-4eb2-5c7b-a94b-bea34ac31c30".
>
> - Channel dropDown required
>
>   The channel to target. For a dynamic value, select Use Channel ID and enter a value in the Channel ID field.
>
>   * Use channel ID
>
> - Channel ID textField required
>
>   The ID of the channel to target, such as "0b2b7c5b-4eb2-5c7b-a94b-bea34ac31c30".
>
> - Member dropDown required
>
>   The member to target. For a dynamic value, select Use Member ID and enter a value in the Member ID field.
>
>   * Use Member/Membership ID
>
> - Membership ID textField
>
>   The ID of the membership, such as "MCMjMSMjMDdlYzlhZjItN2NlNS00YWI3LTg2MzgtMTE1NzM2YmJmOTkwIyM5OGMyOGJlZi05OGYxLTQzNWItYTY1OC03MWVlZTE5YzhmNWUjI2U5MTk4MzA3LTRlMzItNDgwMC1hM2M1LTExNTUxYWQ4MzFhMg=="
>
> * default object
>
>   * properties object
>
>     * clientId string required
>
>     * clientSecret string required
>
>     * tenantId string required
>
>     * teams string required
>
>     * teamId string
>
>     * channels string required
>
>     * channelId string
>
>     * members string required
>
>     * membershipId string
>
> - output object
>
>   * rawResponse string
>
>   * statusCode integer
>
>   * headers object
>
>     * strict-transport-security string
>
>     * request-id string
>
>     * client-request-id string
>
>     * x-ms-ags-diagnostic string
>
>     * date string
>
>     * connection string

### List Channel Members

Get a list of members in a channel.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Team dropDown required
>
>   The team to target. For a dynamic value, select Use Team ID and enter a value in the Team ID field.
>
>   * Use team ID
>
> - Team ID textField
>
>   The ID of the team, such as "0b2b7c5b-4eb2-5c7b-a94b-bea34ac31c30".
>
> - Channel dropDown required
>
>   The channel to target. For a dynamic value, select Use Channel ID and enter a value in the Channel ID field.
>
>   * Use channel ID
>
> - Channel ID textField required
>
>   The ID of the channel to target, such as "0b2b7c5b-4eb2-5c7b-a94b-bea34ac31c30".
>
> * default object
>
>   * properties object
>
>     * clientId string required
>
>     * clientSecret string required
>
>     * tenantId string required
>
>     * teams string required
>
>     * teamId string
>
>     * channels string required
>
>     * channelId string
>
> - output object
>
>   * rawResponse object
>
>     * @odata.context string
>
>     * @odata.count integer
>
>     * value array
>
>       * Array Item Schema object
>
>         * @odata.type string
>
>         * id string
>
>         * roles array
>
>           * Array Item Schema string
>
>         * displayName string
>
>         * visibleHistoryStartDateTime string
>
>         * userId string
>
>         * email string
>
>         * tenantId string
>
>   * statusCode integer
>
>   * headers object
>
>     * transfer-encoding string
>
>     * content-type string
>
>     * strict-transport-security string
>
>     * request-id string
>
>     * client-request-id string
>
>     * x-ms-ags-diagnostic string
>
>     * odata-version string
>
>     * date string
>
>     * connection string

### Send Message in a Channel

Send a message in a channel on behalf of a user.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Team dropDown required
>
>   The team to target. For a dynamic value, select Use Team ID and enter a value in the Team ID field.
>
>   * Use team ID
>
> - Team ID textField
>
>   The ID of the team, such as "0b2b7c5b-4eb2-5c7b-a94b-bea34ac31c30".
>
> - Channel dropDown required
>
>   The channel to target. For a dynamic value, select Use Channel ID and enter a value in the Channel ID field.
>
>   * Use channel ID
>
> - Channel ID textField required
>
>   The ID of the channel to target, such as "0b2b7c5b-4eb2-5c7b-a94b-bea34ac31c30".
>
> - User Access Token textField
>
>   The user's access token. This token is provided by the Sign on with Microsoft capability.
>
> - Message Object textArea
>
>   The JSON object that contains the message body. Learn more in "Chat message" in the Microsoft Graph REST API documentation.
>
> * default object
>
>   * properties object
>
>     * clientId string required
>
>     * clientSecret string required
>
>     * tenantId string required
>
>     * teams string required
>
>     * teamId string
>
>     * channels string required
>
>     * channelId string
>
>     * userAccessToken string required
>
>     * messageBodyData string required
>
> - output object
>
>   * rawResponse object
>
>     * @odata.context string
>
>     * id string
>
>     * replyToId string
>
>     * etag string
>
>     * messageType string
>
>     * createdDateTime string
>
>     * lastModifiedDateTime string
>
>     * lastEditedDateTime string
>
>     * deletedDateTime string
>
>     * subject string
>
>     * summary string
>
>     * chatId string
>
>     * importance string
>
>     * locale string
>
>     * webUrl string
>
>     * policyViolation string
>
>     * eventDetail string
>
>     * from object
>
>       * application string
>
>       * device string
>
>       * user object
>
>         * id string
>
>         * displayName string
>
>         * userIdentityType string
>
>     * body object
>
>       * contentType string
>
>       * content string
>
>     * channelIdentity object
>
>       * teamId string
>
>       * channelId string
>
>     * attachments array
>
>     * mentions array
>
>     * reactions array
>
>   * statusCode integer
>
>   * headers object
>
>     * transfer-encoding string
>
>     * content-type string
>
>     * location string
>
>     * strict-transport-security string
>
>     * request-id string
>
>     * client-request-id string
>
>     * x-ms-ags-diagnostic string
>
>     * odata-version string
>
>     * date string
>
>     * connection string

### Send Message in a Chat

Send a message in a chat on behalf of a user.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User Access Token textField
>
>   The user's access token. This token is provided by the Sign on with Microsoft capability.
>
> - Chat ID textField
>
>   The ID of the chat, such as "19:ce95abaa0e9f4d22a0e0faa6aad76c56\@thread.v2".
>
> - Message Object textArea
>
>   The JSON object that contains the message body. Learn more in "Chat message" in the Microsoft Graph REST API documentation.
>
> * default object
>
>   * properties object
>
>     * clientId string required
>
>     * clientSecret string required
>
>     * tenantId string required
>
>     * chatId string required
>
>     * userAccessToken string required
>
>     * messageBodyData string required
>
> - output object
>
>   * rawResponse object
>
>     * @odata.context string
>
>     * id string
>
>     * replyToId string
>
>     * etag string
>
>     * messageType string
>
>     * createdDateTime string
>
>     * lastModifiedDateTime string
>
>     * lastEditedDateTime string
>
>     * deletedDateTime string
>
>     * subject string
>
>     * summary string
>
>     * chatId string
>
>     * importance string
>
>     * locale string
>
>     * webUrl string
>
>     * channelIdentity string
>
>     * policyViolation string
>
>     * eventDetail string
>
>     * from object
>
>       * application string
>
>       * device string
>
>       * user object
>
>         * id string
>
>         * displayName string
>
>         * userIdentityType string
>
>     * body object
>
>       * contentType string
>
>       * content string
>
>     * attachments array
>
>     * mentions array
>
>     * reactions array
>
>   * statusCode integer
>
>   * headers object
>
>     * transfer-encoding string
>
>     * content-type string
>
>     * location string
>
>     * strict-transport-security string
>
>     * request-id string
>
>     * client-request-id string
>
>     * x-ms-ags-diagnostic string
>
>     * odata-version string
>
>     * date string
>
>     * connection string

### List Chats

Get a list of chats for a user.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User Access Token textField
>
>   The user's access token. This token is provided by the Sign on with Microsoft capability.
>
> * default object
>
>   * properties object
>
>     * clientId string required
>
>     * clientSecret string required
>
>     * tenantId string required
>
>     * userAccessToken string required
>
> - output object
>
>   * rawResponse object
>
>     * @odata.context string
>
>     * @odata.count integer
>
>     * value array
>
>       * Array Item Schema object
>
>         * id string
>
>         * topic string
>
>         * createdDateTime string
>
>         * lastUpdatedDateTime string
>
>         * chatType string
>
>         * webUrl string
>
>         * tenantId string
>
>         * onlineMeetingInfo string
>
>   * statusCode integer
>
>   * headers object
>
>     * transfer-encoding string
>
>     * content-type string
>
>     * strict-transport-security string
>
>     * request-id string
>
>     * client-request-id string
>
>     * x-ms-ags-diagnostic string
>
>     * odata-version string
>
>     * date string
>
>     * connection string

### Sign on with Microsoft

Redirect the browser and prompt the user to authenticate with Microsoft. This creates a token needed to list the user's chats or send messages as the user.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - - Display Name button
>   - showPoweredBy toggleSwitch
>   - skipButtonPress toggleSwitch
>
> * default object
>
>   * properties object
>
>     * clientId string required
>
>     * clientSecret string required
>
>     * tenantId string required
>
> - output object
>
>   * rawResponse object
>
>     * token\_type string
>
>     * scope string
>
>     * expires\_in integer
>
>     * ext\_expires\_in integer
>
>     * access\_token string
>
>     * refresh\_token string
>
>   * statusCode integer
>
>   * headers object
>
>     * cache-control string
>
>     * pragma string
>
>     * content-type string
>
>     * expires string
>
>     * strict-transport-security string
>
>     * x-content-type-options string
>
>     * p3p string
>
>     * x-ms-request-id string
>
>     * x-ms-ests-server string
>
>     * x-xss-protection string
>
>     * set-cookie array
>
>       * Array Item Schema string
>
>       * Array Item Schema string
>
>       * Array Item Schema string
>
>     * date string
>
>     * connection string
>
>     * content-length string
>
>   * tokens string
>
>   * connectionId string
>
>   * connectorId string

### Make a Custom API Call

Define and use your own call to the Microsoft Team REST API

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Endpoint textField required
>
>   The API endpoint, such as "https\://admin.googleapis.com/admin/directory/v1/users/user\@example.com".
>
> - HTTP Method dropDown required
>
>   The HTTP method of the API call.
>
>   * GET
>
>   * POST
>
>   * PUT
>
>   * DELETE
>
> - Query Parameters keyValueList
>
>   Query parameters for the request.
>
> - Additional Headers keyValueList
>
>   Define additional headers to send to Microsoft Teams. Learn more in the API documentation.
>
> - Body codeEditor
>
>   The body of the API call.
>
> * default object
>
>   * properties object
>
>     * clientId string required
>
>     * clientSecret string required
>
>     * tenantId string required
>
>     * endpoint string required
>
>     * method string required
>
> - output object
>
>   * rawResponse object
>
>   * statusCode integer
>
>   * headers object