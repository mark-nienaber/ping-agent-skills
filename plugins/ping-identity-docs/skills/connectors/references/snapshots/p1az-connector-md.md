---
title: PingOne Authorize Connector
description: Configure the PingOne Authorize connector in PingOne DaVinci to make policy-based, fine-grained authorization decisions within your flows
component: connectors
page_id: connectors::p1az_connector
canonical_url: https://docs.pingidentity.com/connectors/p1az_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-pingone-authorize: Setting up PingOne Authorize
  choosing-a-pingone-worker-app: Choosing a PingOne worker app
  setting-up-the-pingone-authorize-connector-configuration: Setting up the PingOne Authorize connector configuration
  connector-configuration: Connector configuration
  client-id: Client ID
  client-secret: Client Secret
  endpoint: Endpoint
  using-the-connector-in-a-flow: Using the connector in a flow
  make-decision-request: Make Decision Request
  find-statements: Find Statements
  make-a-decision-request: Make a decision request
  find-statements-2: Find statements
  capabilities: Capabilities
  makeDecisionRequest: Make Decision Request
  findStatement: Find Statement(s)
---

# PingOne Authorize Connector

This connector lets you use PingOne Authorize for policy-based authorization decisions in your PingOne DaVinci flow.

PingOne Authorize controls what users can see and do inside of applications and APIs. It allows organizations to centrally configure authorization requirements, ranging from simple rules to real-time, fine-grained policies.

PingOne Authorize can integrate with other PingOne services, such as PingOne Protect, and exploit information in a PingOne user profile to augment authorization events in real-time.

Use the PingOne Authorize connector to:

* Externalize authorization from your PingOne DaVinci flows, allowing separation of duties between the team controlling the user experience and the team controlling what users are authorized to see and do.

* Leverage real-time data in fine-grained policies that go beyond identity and roles.

* Make adaptive, context-aware authorization decisions that result in permit, deny, or challenge outcomes.

* Assemble and provide PingOne DaVinci with authorized information used in flows, for example, retrieving the list of accounts that a user is authorized to access.

## Setup

### Resources

For information and setup help, learn more in the following documentation:

* PingOne Authorize documentation:

  * [Introduction to Authorization](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_introduction.html)

  * [Getting started with PingOne Authorize](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_getting_started.html)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A PingOne Authorize license

* A PingOne environment with a configured worker application

### Setting up PingOne Authorize

1. Follow the instructions in [Getting started with PingOne Authorize](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_getting_started.html).

2. In the [Trust Framework](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_trust_framework.html), define the resources needed to build policies.

3. [Write policies](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_policies.html) for authorization decisions that you want to include in your flow. Include advice in your policies for statements you want to return to your flows.

4. [Publish](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_version_history.html) the policies to a [Decision Endpoint](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_decision_endpoints.html).

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

### Setting up the PingOne Authorize connector configuration

In PingOne DaVinci, add a **PingOne Authorize** connection. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

#### Connector configuration

##### Client ID

The **Client ID** of the worker application that you identified in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app).

##### Client Secret

The **Client Secret** from the **Configuration** tab of your PingOne worker application that you identified in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app).

##### Endpoint

The decision endpoint to which the connector submits decision requests. On the [Decision Endpoints](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_decision_endpoints.html) page in PingOne Authorize, expand the appropriate endpoint to get the **URL** or the **Endpoint ID**.

## Using the connector in a flow

The PingOne Authorize connector provides these capabilities:

### Make Decision Request

Add authorization decision requests to your flows. Decision requests return permit, deny, indeterminate, or not applicable decisions that you can act on in your flows.

### Find Statements

Find statements returned in decision responses and use them as inputs in subsequent nodes. Add multiple PingOne Authorize connector nodes at different points in your flow to use the authorized information returned in statements.

When a statement code is found, you can act on it in your flow. For example, you can use it to determine if multi-factor authentication (MFA) is required or a risk update is needed. You can also extract authorized information from the statement payload, for use in scenarios such as reporting fraud case information or providing a list of authorized IDs or accounts in your flow.

In the following example, the first PingOne Authorize connector uses information about an authenticated user to make an authorization decision. The second PingOne Authorize connector finds a statement code in the decision response to determine if MFA is required.

![Screen capture of an example PingOne Authorize flow in DaVinci.](_images/connector-images/dvc-p1az-example-flow.png)

### Make a decision request

Collect user information with an HTML form, then use the first PingOne Authorize connector to send the information to PingOne Authorize, and use the decision response in your flow.

1. In your flow, build a sign-on flow that populates a **User ID** field in an **HTTP** connector with the **HTML Form** capability.

2. Send user information to PingOne Authorize:

   1. After your sign-on flow, add the **PingOne Authorize** connector and select the node in your flow.

   2. Select the **Make Decision Request** capability.

   3. In the **User ID** field, click **{}** and select the **User ID** variable from your **HTML Form** node.

3. Populate attribute information in the decision request:

   1. In the **Fields** section, click **[icon: plus, set=fa]**to add one or more key-value pairs. These pairs map to attributes in PingOne Authorize.

   2. In the **Key** field, enter the full name of the attribute that you want to map to the decision request.

   3. In the **Value** field, click **{}** and select a variable from a node. Alternatively, you can enter a hard-coded value.

      |   |                                                                                                                                                                                                                                                                                                                                                              |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | To edit key-value pairs, click the **Pencil** icon. In edit mode, the icon turns into an **X** icon. Click the **X** icon to leave edit mode. To delete a Key-Value pair in edit mode, click the **-** icon under **Key**.![Screen capture of Key/Value field options including the Delete button.](_images/connector-images/dvc-p1az-key-value-options.png) |

   4. Click **Apply**.

4. Add a node to capture the decision response from PingOne Authorize:

   1. After the **PingOne Authorize** node, add a **Function** connector and select the node in your flow.

   2. Select the **A == B (Multiple Conditions)** trigger.

   3. In the **Value A** field, click **{}** and select the **decision** variable from your **PingOne Authorize** node.

   4. Click **Add** and enter `PERMIT` in the **Value 1** field.

   5. Click **Add** and enter `DENY` in the **Value 2** field.

      |   |                                                                                                                            |
      | - | -------------------------------------------------------------------------------------------------------------------------- |
      |   | In this example flow, Not Applicable and Indeterminate decisions fall under **No Match** and connect to an **Error** node. |

   6. Click **Apply**.

5. Add nodes to your flow that act on the **Permit**, **Deny**, and **No Match** decision responses.

6. Test your flow:

   1. Click **Save**, **Deploy**, then **Run**.

   2. Review status messages.

### Find statements

Use the second PingOne Authorize connector to find a statement code that matches advice in a policy, then use the code in your flow to determine if MFA is required. If the code is found in decision response statements, then the outcome of the node is true.

1. Find a statement code in the decision response from the first **PingOne Authorize** node:

   1. After the first **PingOne Authorize** node in your flow, add another **PingOne Authorize** connector and select the node in your flow.

   2. Select the **Find Statement(s)** capability.

   3. In the **Statement Code** field, enter the statement **Code** from **Advice and Obligations** in your policy rule. For example, the following image shows the `MFA_REQ` advice code in a PingOne Authorize rule.

      ![Screen capture of Advice and Obligations in a PingOne Authorize policy rule.](_images/connector-images/dvc-p1az-advice-obligations.png)

   4. In the **Statements** field, click **{}** and select the **statements (array)** output variable from the first **PingOne Authorize** node in your flow.

      ![Screen capture of Statements options for a PingOne Authorize connector.](_images/connector-images/dvc-p1az-statements-options.png)

   5. Click **Apply**.

2. After the second **PingOne Authorize** node in your flow, add nodes for an MFA flow.

3. Test your flow:

   1. Click **Save**, **Deploy**, then **Run**.

   2. Review status messages.

## Capabilities

### Make Decision Request

Submit a decision request to a PingOne Authorize endpoint

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Parameters keyValueList
>
>   Input parameters for the decision request
>
> - User ID textField
>
>   The ID of the PingOne user on whose behalf the connector is making a decision request
>
> * default object
>
>   * properties object
>
>     * parameters array
>
>     * userId string
>
>     * clientId string
>
>     * clientSecret string
>
>     * endpointUrl string
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * statements array
>
>   * decision string
>
>   * headers object

### Find Statement(s)

Filter decision response statements by code

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Statement Code textField
>
>   The advice code from a PingOne Authorize policy rule to search for in an array of statements from a decision response
>
> - Statements textField
>
>   The array of statements to search through in a decision response
>
> * default object
>
>   * properties object
>
>     * statements string
>
>     * code string
>
> - output object
>
>   * statements array