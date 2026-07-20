---
title: Flow Conductor Connector
description: Configure the Flow Conductor connector in PingOne DaVinci to initiate out-of-band events with magic links and use other flows as reusable subflows
component: connectors
page_id: connectors::flow_conductor_connector
canonical_url: https://docs.pingidentity.com/connectors/flow_conductor_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  interacting-with-external-systems: Interacting with external systems
  links-to-subflows: Links to subflows
  setup: Setup
  setting-up-the-flow-conductor-connector-configuration: Setting up the Flow Conductor connector configuration
  connector-configuration: Connector configuration
  input-schema: Input Schema
  public-key: Public Key
  enforce-signed-token: Enforce Signed Token
  using-the-connector-in-a-flow: Using the connector in a flow
  emailing-a-magic-link-to-a-user-then-continuing-the-flow: Emailing a magic link to a user, then continuing the flow
  linking-to-a-subflow: Linking to a subflow
  capabilities: Capabilities
  receive-start-flow-redirect: Receive Start Flow Redirect
  out-of-band-start-links-only: Out-of-Band Start (Links Only)
  out-of-band-continue: Out-of-Band Continue
  invoke-subflow: Invoke Subflow
  invoke-ui-subflow: Invoke UI Subflow
---

# Flow Conductor Connector

The Flow Conductor connector lets your PingOne DaVinci flow initiate asynchronous events in external systems. It also allows you to use another flow as a subflow.

## Interacting with external systems

Some authentication workflows require the user to do something in another system, such as clicking a magic link in their email or verifying a document in a mobile app. The Flow Conductor connector simplifies these cases by allowing you to generate the magic link and create a challenge variable that's resolved when the link is clicked. Learn more about challenges in the [Challenge connector documentation](challenge_connector.html).

The Flow Conductor also allows you to create a secondary path in your flow that's triggered when the magic link is clicked:

1. In your main flow, a Flow Conductor **Out-of-Band Start (Links Only)** node generates a magic link or QR code. You can send this link to the user by email, SMS, or another method of your choice. This node also creates the challenge, which gives an [HTTP](http_connector.html) connector the ability to pause the flow until the status of the challenge changes.

2. When the user clicks the magic link, an **Out-of-Band Continue** node starts a secondary flow. You can use this flow to show a confirmation message, and to trigger the main flow to continue by updating the status of the challenge.

The Start and Continue nodes work as a pair, and they are always attached to the same parent node. PingOne DaVinci automatically follows the Start node first and activates the Continue node when the user clicks the magic link that contains the matching challenge ID.

## Links to subflows

By linking to subflows, you can simplify visually complex flows by breaking them into smaller components. You can also link to a subflow from as many main flows as you want, so this is a powerful way to centralize your maintenance work.

Subflows are best used for frequently-used groups of nodes that serve a specific purpose. For example, you might create a subflow for registering a multi-factor authentication (MFA) device or letting a user reset their password. Then you could include these in several of your main flows, such as your registration, authentication, and user self-service portal experiences.

## Setup

### Setting up the Flow Conductor connector configuration

In PingOne DaVinci, add a **Flow Conductor** connection. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

#### Connector configuration

##### Input Schema

When you call on this subflow, it receives information from your main flow. The input schema defines the structure of that information. Learn more in [JSON-Schema.org](https://json-schema.org/).

##### Public Key

To make sure the flow is only called by an authorized source, enter your public encryption key here.

##### Enforce Signed Token

Turn this on to require that the token is signed.

## Using the connector in a flow

### Emailing a magic link to a user, then continuing the flow

![A screen capture that shows how the Flow Conductor branches a registration flow.](_images/connector-images/dvc-flow-conductor-registration-flow-form.jpg)

When a guest registers a new user account, you can verify that they own the email address that they entered. We want to pause our main flow until the user clicks the link in their email inbox. We also want to show them a confirmation message in a new browser tab when they click the link. After they click the magic link, our secondary flow will trigger our main flow to bring the user to the User Account Portal.

For this flow, you'll need:

* A registration form in your flow, made using the [HTTP](http_connector.html) connector.

* A way to send an email to the user, such as the SMTP connector.

* A [Challenge](challenge_connector.html) connector available in your environment.

1. Generate the magic link and the challenge:

   1. In your flow, following the registration form, add the **Flow Conductor** connector, and select the **Out-of-Band Start (Links only)** capability. Select the node that appears in your flow.

   2. In our case, we want to send a text link rather than a QR code, so we'll leave **Generate QR Code** turned off.

   3. In the **Challenge Length** field, you can customize the length of the challenge ID. This is a number that PingOne DaVinci generates to keep track of this challenge. We'll refer to this ID elsewhere in our flow, but we don't need to know the number. Leave it as the default of 32.

   4. In the **Challenge Expiry** field, specify how long you want the flow to wait before timing out.

   5. It won't take the user long to click a magic link, but if your flow has the user taking photos of their drivers license for identity verification, you should give them more time.

   6. We're sending a normal link to the user, so we'll leave **Use Custom Link** turned off.

   7. You can turn this on in your own flow if you need to customize the URL to point to a mobile app. To customize the URL, point to your equivalent of `com.myApp://skSKD?challenge=`.

2. Send the magic link to the user:

   1. Following your **Out-of-Band Start** node, add an **SMTP** connector and select the **Send Email** capability. Select the node that appears in your flow.

   2. In the **To Email Address** field, select the email address variable from your registration form.

   3. In the **HTML Message** field, include a hyperlink. For the `href` part of the link, click **{}** and select the `continueLink` variable from your Flow Conductor node.

      ![An animation that shows the user inserting the continueLink variable into the HTML Message field.](_images/connector-images/dvc-flow-conductor-html-message-variable.gif)

      This inserts the magic link with the unique challenge ID associated with our flow.

3. Show a page with a "waiting" animation until the user clicks the link:

   1. Parallel to your SMTP node, add an [HTTP](http_connector.html) connector and select the **Custom HTML Template** capability. Select the node that appears in your flow.

   2. Build your message in the **HTML Template** field. To show a "waiting" animation on the page, click **{}** and select the **skpolling** variable from **SK-Component**.

   3. In the **Challenge** field, click **{}** and select the **challenge** variable from your Flow Conductor node.

      ![An animation that shows the user inserting the skpolling variable into the HTML Template field.](_images/connector-images/dvc-flow-conductor-html-template-variable.gif)

      This pauses the main flow on this page until the challenge status changes. We'll update the challenge status in the secondary flow. Any change in the challenge status, regardless of the value, will cause this flow to continue.

4. Build a secondary flow that thanks the user for clicking the link and signals the main flow to continue by resolving the challenge:

   1. Following your registration form, add another **Flow Conductor** connector parallel to the first one. Select the **Out-of-Band Continue** capability, and click **Apply**.

      |   |                                                                                                     |
      | - | --------------------------------------------------------------------------------------------------- |
      |   | You don't need to configure this node. It starts automatically when the user clicks the magic link. |

   2. Following your **Out-of-Band Continue** node, add a **Challenge** connector and select the **Update Transaction Status** capability.

   3. In the **Challenge** field, click **{}** and select the `challenge` variable from your **Out-of-Band Continue** node.

   4. In the **Challenge Status** list, select **approved**. Click **Apply**.

      Because our **Custom HTML Template** page in the main flow is waiting for this challenge status to change, this update will trigger the flow to continue.

   5. Add a "Thanks for verifying" page after your **Out-of-Band Continue** node. This page will appear when the user clicks the magic link.

5. Following your **Custom HTML Template** "waiting" page in the main flow, continue building the rest of your flow.

   For example, you could direct the user to their user account self-service portal.

### Linking to a subflow

![A diagram that shows a main flow linking to a subflow.](_images/connector-images/dvc-flow-conductor-subflow-link.jpg)

Using subflows lets you organize large flows into smaller pieces that are more manageable and modular. This approach includes a main flow and one or more subflows.

In the example scenario below, the main flow allows guests to register a new user account. As part of the process, the user is prompted to add a multi-factor authentication (MFA) device.

This example organization created a subflow for MFA device management so it can be reused in an authentication flow and a user self-service portal flow.

Before you start, you need a main flow and a subflow. You can create these yourself, or import the **PingOne - Register with verify email and MFA enrollment** and **PingOne - Device registration sub-flow** flows in the [Ping Identity Marketplace](https://marketplace.pingone.com/home).

1. In your main flow, create a link to your subflow:

   1. Add the Flow Conductor connector and select the **Invoke UI Subflow** capability. Select the node that appears in your flow.

      |   |                                                                                                                                                                                                  |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | We need this capability because there is a user interface component to our MFA setup experience. If your own flow doesn't have a UI component, select the **Invoke Subflow** capability instead. |

   2. In the **Flow** list, select the flow that you want to invoke. You can choose any flow in your environment, but you should only choose a flow that would work well in the middle of your main flow.

   3. In the **Flow Version Id** field, enter a version number.

      |   |                                                                                                                                                                                                                                                                                                  |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | If you want to link to the latest version of the subflow, enter `-1`.If you want to use a specific version, click **Edit Subflow** to open the **Flow Studio** in a new tab. Open the subflow and click **More Options ( [icon: ellipsis-v, set=fa]) > Flow Versions** for the list of versions. |

   4. Click **Apply** to save your changes.

2. Configure the input schema to pass properties from your main flow to your subflow:

   1. Click the **Edit Subflow** link to open the **Flow Studio** in a new tab.

   2. Open your subflow. In the example scenario, this is the MFA device registration flow.

   3. Click **More Options ( [icon: ellipsis-v, set=fa]) > Input Schema**

   4. Click **Add**.

   5. In the **Property Name** field, enter the attribute that your subflow needs. In our example case, it's `pingone_userId`.

   6. In the **Data Type** list, we'll select **String** because it matches the data for the PingOne user ID.

   7. (Optional) Click **Add** to any more properties that your subflow needs.

   8. Click **Save** to save your changes.

   9. Click **Save** to save your flow.

3. Configure the output schema to pass properties from your subflow to back to your main flow. To determine the output schema, you can get an example payload and convert it in using an online tool.

   1. Copy your raw JSON output:

      1. At the end of your subflow, add an [HTTP](http_connector.html) connector and select the **Custom HTML Message** capability. Click the new node in your flow.

      2. In the **Message** field, click **{}** and insert the **output (object)** variable from your the node immediately preceding the HTTP node you're editing.

      3. Click **Apply**, save, deploy, and run your changes.

      4. Copy the JSON payload that appears in your HTML message.

      5. Remove the **Custom HTML Message** node from your flow.

   2. In a browser, open the [Online JSON Schema Validator and Generator](https://extendsclass.com/json-schema-validator.html) tool.

   3. Paste the JSON response you copied into the **JSON** field. Click **Generate Schema From JSON**. Copy the output from the **JSON SCHEMA** field.

      ![A screen capture that shows the JSON Schema Validator and Generator tool after generating the JSON schema.](_images/connector-images/dvc-flow-conductor-json-schema-validator.jpg)

   4. In your subflow, click **More Options ( [icon: ellipsis-v, set=fa]) > Output Schema**.

   5. In the **Output Schema** field, paste the output schema that you copied.

   6. Click **Save** to save your changes.

   7. Click **Save** to save your flow.

4. Run your main flow to test it.

   When your main flow reaches the Flow Conductor node, it jumps over to the MFA setup subflow and passes the necessary properties. When that flow completes, properties from the subflow are carried over and the main flow continues.

## Capabilities

### Receive Start Flow Redirect

Receive the redirect URI to start the flow.

> **Collapse: Show details**
>
> * Details
>
>   * * Properties
>     * authenticatedRequest `dropDown`
>     * tokenSigningMethod `dropDown`
>     * clientId `textField`
>     * clientSecret `textField`
>     * issuerUrl `textField`
>     * jwksKeys `textArea`
>     * tokenHint `textField`
>     * connectionId `dropDown`
>     * claimsMapping `mapping`
>
>     Default:
>
>     ```
>     [
>     	{
>     		"value1": "username",
>     		"value2": "sub",
>     		"deleteAllowed": false
>     	},
>     	{
>     		"value1": "name",
>     		"value2": "name",
>     		"deleteAllowed": false
>     	},
>     	{
>     		"value1": "email",
>     		"value2": "email",
>     		"deleteAllowed": false
>     	}
>     ]
>     ```

### Out-of-Band Start (Links Only)

Receive links through email, SMS, or push notifications to continue the flow outside of the typical path.

> **Collapse: Show details**
>
> * Details
>
>   * * Properties
>     * generateQr `toggleSwitch`
>     * challengeLength `textField`
>     * challengeExpiry `textField`
>     * useCustomLink `toggleSwitch`
>     * customLink `textField`
>
> - - Output Schema
>   - output `object`
>   - challenge `string`
>   - continueLink `string`
>   - continueQr `string`

### Out-of-Band Continue

Continue the flow in the out-of-band path.

> **Collapse: Show details**
>
> * Details
>
>   * * Properties
>     * Node ID when this OOB link expires `textField`
>
> Select Node ID when this OOB link expires
>
> * * Output Schema
>   * output `object`
>   * status `string`
>   * detailStatus `string`
>   * rawStatus `string`
>   * challenge `string`
>   * credId `string`

### Invoke Subflow

Invoke API-based subflows.

> **Collapse: Show details**
>
> * Details
>
>   * * Properties
>     * subFlowId `dropDownAsync`
>     * subFlowVersionId `textField`
>     * Input Schema
>     * default `object`
>     * cookies `object`
>
>     List of cookies associated with the user.
>
>   * ip `string` `minLength: 1` `maxLength: 255`
>
>     Ip address of the user in current session.
>
>   * userAgent `string` `minLength: 1` `maxLength: 250`
>
>     Information about browser, OS, etc. of user in current session.
>
>   * skOpenId `object`
>
>     Object containing client id of user.
>
>   * origin `string` `minLength: 0` `maxLength: 500`
>
>     Origin
>
>   * originCookies `string` `minLength: 0` `maxLength: 5000`
>
>     OriginCookies

### Invoke UI Subflow

Invoke UI-based subflows.

> **Collapse: Show details**
>
> * Details
>
>   * * Properties
>     * subFlowId `dropDownAsync`
>     * subFlowVersionId `textField`
>     * Input Schema
>     * default `object`
>     * cookies `object`
>
>     List of cookies associated with the user.
>
>   * ip `string` `minLength: 1` `maxLength: 255`
>
>     Ip address of the user in current session.
>
>   * userAgent `string` `minLength: 1` `maxLength: 250`
>
>     Information about browser, OS, etc. of user in current session.
>
>   * skOpenId `object`
>
>     Object containing client id of user.
>
>   * origin `string` `minLength: 0` `maxLength: 500`
>
>     Origin
>
>   * originCookies `string` `minLength: 0` `maxLength: 5000`
>
>     OriginCookies