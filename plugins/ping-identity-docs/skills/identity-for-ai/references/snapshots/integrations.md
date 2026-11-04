---
title: Authorizing autonomous Gemini agents with Ping Identity solutions
description: Authorize an autonomous Gemini agent calling an MCP tool with scoped, short-lived delegation tokens.
component: identity-for-ai
page_id: identity-for-ai:integrations:idai-authorizing-gemini-autonomous-agents-with-ping
canonical_url: https://developer.pingidentity.com/identity-for-ai/integrations/idai-authorizing-gemini-autonomous-agents-with-ping.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-10-14T18:43:00Z
keywords: ["Identity for AI", "ai identity", "ai security", "Google Cloud Gemini Enterprise", "Gemini Enterprise Agent Platform", "PingOne Authorize", "authentication", "authorization", "AI agent", "autonomous agent", "MCP", "token exchange", "delegation", "least privilege"]
section_ids:
  how-this-works: How this works
  components: Components
  token-chain: Token chain
  benefits-of-this-approach: Benefits of this approach
  goals: Goals
  what-youll-do: What you'll do
  before-you-begin: Before you begin
  tasks: Tasks
  idai-gemini-aut-mcp-server: Deploy the Supply Chain MCP Tool
  idai-gemini-aut-policies: Create authorization policies in PingOne Authorize
  idai-gemini-aut-extension-service: Deploy the Agent Gateway Service Extension
  idai-gemini-aut-agent-gateway: Create the Agent Gateway
  idai-gemini-aut-deploy-agent: Deploy the CRM Agent
  validation: Validation
  troubleshooting: Troubleshooting
  whats-next: What's next
---

# Authorizing autonomous Gemini agents with Ping Identity solutions

This use case secures an autonomous agent that calls protected tools without human interaction. Because the agent doesn't act on behalf of a human, it proves only its own identity. The Agent Gateway Service Extension requests an authorization decision from PingOne Authorize. Upon an permit decision, the service extension mints a scoped, short-lived token and injects it into the tool request.

This use case builds on the [Integrating Gemini Enterprise Agent Platform with Ping Identity solutions](idai-integrating-gemini-agent-platform-with-ping.html) architecture by adding a delegation token exchange to the flow. You can find more information about [token exchange with delegation](https://docs.pingidentity.com/pingone/use_cases/p1_oauth_2_token_exchange_delegation.html) in the PingOne documentation.

## How this works

Consider a CRM agent that calls an external supply chain Model Context Protocol (MCP) tool to restock inventory. The following diagram shows the flow and components:

![Diagram showing an AI agent requesting access to a resource without human involvement.](_images/idai-gemini-autonomous-agent-flow.png)

1. The agent authenticates to PingOne to establish its own client identity.

2. The agent runtime routes MCP requests through the Agent Gateway to the service extension.

3. The service extension requests an authorization decision from PingOne Authorize.

4. If the decision is permit, the service extension performs a delegation token exchange, mints a token specifically for the Supply Chain MCP Tool, and injects it into the request before forwarding it to the MCP server. If the decision is deny, the service extension returns an error that blocks agent access to the tool.

### Components

| Component                                                                                                                                                                                                     | Role                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| [Agent](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/baseline-autonomous-agent-to-tool/services/agent)                                                     | CRM Agent that acts as an MCP client and obtains its own token.                                                                              |
| [Agent Gateway](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/baseline-autonomous-agent-to-tool/services/agent-gateway)                                     | Google-managed policy enforcement point that forwards agent requests to the service extension over the gRPC remote procedure call framework. |
| [Agent Gateway Service Extension](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/baseline-autonomous-agent-to-tool/services/agent-gateway-extension-service) | Service extension that sends requests to PingOne Authorize, exchanges the agent's token, and injects the resulting token into the request.   |
| [Supply Chain MCP Tool](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/baseline-autonomous-agent-to-tool/services/supply-chain-mcp-tool)                     | Downstream resource that the agent invokes to restock inventory.                                                                             |
| [PingOne](https://docs.pingidentity.com/pingone/use_cases/p1_oauth_2_token_exchange_delegation.html)                                                                                                          | Identity provider that issues the agent's token and the delegated tool token.                                                                |
| [PingOne Authorize](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_introduction.html)                                                                                       | External policy decision point that evaluates authorization requests.                                                                        |

### Token chain

The token flow begins when the autonomous agent obtains a subject token from PingOne using the Client Credentials grant. The agent presents this subject token to the Agent Gateway Service Extension, which exchanges it, along with the Agent Gateway's actor token, for a delegated token restricted to the MCP server. The resulting token preserves the agent as the subject and identifies the service extension as the actor. For simplicity, the Agent Gateway's actor token isn't included here.

* Subject token: the agent's token

  ```json
  {
    "iss": "https://auth.pingone.<region>/<env>/as",
    "client_id": "<agent-client-id>",
    "aud": "agent-gateway",
    "scope": "supply-chain:restock",
    "grant_type": "client_credentials",
    "may_act": { "sub": "<agent-gw-extension-client-id>" }
  }
  ```

  * `client id`: Identifies the agent as the OAuth client that requested the token.

  * `aud`: Identifies the Agent Gateway as the intended recipient of the token.

  * `scope`: Grants the privileges required to invoke the downstream restock tool.

  * `may_act`: Authorizes the service extension to act on behalf of the agent during a token exchange.

* MCP tool token: the Agent Gateway's delegated (exchanged) token

  ```json
  {
    "iss": "https://auth.pingone.<region>/<env>/as",
    "sub": "<agent-client-id>",
    "client_id": "<agent-gw-extension-client-id>",
    "aud": "supply-chain-mcp-tool",
    "scope": "supply-chain:restock",
    "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
    "act": { "sub": "<agent-gw-extension-client-id>" }
  }
  ```

  * `sub`: Identifies the agent as the principal subject of the token.

  * `client id`: Identifies the service extension as the OAuth client that requested the exchanged token.

  * `aud`: Identifies the Supply Chain MCP Tool as the intended recipient of the token.

  * `scope`: Grants the privileges required to invoke the Supply Chain MCP Tool.

  * `act`: Identifies the service extension as the current actor to whom authority has been delegated.

### Benefits of this approach

* **No standing tool credentials in the agent:** The agent never holds a token that grants access to the tool, preventing a compromised agent from leaking credentials.

* **Least privilege:** Each tool token is scoped to a single resource and expires quickly.

* **Delegation proof:** The tool token carries an `act` claim specifying that the service extension acted for the agent. PingOne mints this claim only after confirming that the agent's token authorizes the extension (using the `may_act` claim).

* **Centralized policy:** PingOne Authorize owns the authorization decision. Administrators can update policies centrally without modifying or redeploying the agent or the MCP server.

## Goals

* Securely authenticate an autonomous agent with PingOne and perform a token exchange that mints a delegated token for a downstream tool.

* Deploy the Agent Gateway to act as the central Policy Enforcement Point (PEP) for all outbound requests originating from the agent.

* Use PingOne Authorize to evaluate runtime context and make authorization decisions before the agent reaches downstream tools.

## What you'll do

1. [Deploy the Supply Chain MCP Tool](#idai-gemini-aut-mcp-server) to Google Cloud Run and register it in Google Agent Registry.

2. [Create authorization policies](#idai-gemini-aut-policies) that decide whether the service extension permits agent request to the MCP server.

3. [Deploy the Agent Gateway Service Extension](#idai-gemini-aut-extension-service) to Cloud Run and configure it to request authorization decisions on every tool call.

4. [Deploy the Agent Gateway](#idai-gemini-aut-agent-gateway) and attach the service extension to it.

5. [Deploy the agent](#idai-gemini-aut-deploy-agent) and create a PingOne resource that licenses the service extension as the only actor allowed to exchange tokens bound for the gateway.

## Before you begin

Ensure you meet the prerequisites in the [Gemini Enterprise Agent Platform](idai-integrating-gemini-agent-platform-with-ping.html#idai-gemini-prereqs) integration overview.

## Tasks

You can find implementation files and code samples for this use case in the [Baseline Autonomous Agent to Tool](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/baseline-autonomous-agent-to-tool) GitHub repository.

### Deploy the Supply Chain MCP Tool

The [Supply Chain MCP Tool](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/baseline-autonomous-agent-to-tool/services/supply-chain-mcp-tool) is an MCP server that simulates a supply chain tool. It exposes a single restock tool (a mock tool that returns a hard-coded accepted order), which is the downstream resource the agent will invoke. To access the tool, the agent's request is routed through the Agent Gateway and the Agent Gateway Service Extension. The MCP server verifies the OAuth token injected by the gateway.

You'll deploy the Supply Chain MCP Tool to Cloud Run, register it in Agent Registry, and configure it with a matching resource in PingOne to ensure every token issued for tool access carries claims that prove delegation.

> **Collapse: Create the Supply Chain MCP Tool resource in PingOne**
>
> Add a custom resource in PingOne that represents the Supply Chain MCP Tool the agent accesses to restock inventory.
>
> Two grant types are used to request tokens for this resource: the `client_credentials` grant (which has no subject or actor) and the token exchange grant, where the subject is an autonomous agent with no `sub` claim. You'll configure two attributes with attribute mappings to ensure each grant yields the correct claims:
>
> * `sub` attribute: For a standard `client_credentials` grant involving no delegation, this mapping assigns the literal value `no-subject`. During a token exchange, the agent's subject token lacks a `sub` claim, so the mapping extracts the subject token's `client_id` instead. This dynamic mapping ensures the resulting tool token identifies the calling agent.
>
> * `act` attribute: For `client_credentials` grants, this mapping assigns the literal value `noActor`. During a token exchange, it sets the `act` claim to the exchanging actor's identity only if the subject token's `may_act` claim explicitly authorizes that actor (the service extension). If there's no match, it returns `null`. Because you'll make this attribute required, a `null` value fails the token exchange outright. This enforces the security boundary that only the service extension can exchange an agent token for this resource.
>
> |   |                                                                                                                                                                            |
> | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [adding custom resources](https://docs.pingidentity.com/pingone/applications/p1_adding_custom_resource.html) in the PingOne documentation. |
>
> 1. In the PingOne admin console, go to **Applications > Resources** and click the **[icon: plus, set=fa]**icon.
>
> 2. Define the resource:
>
>    1. **Resource Name**: `BAATT Supply Chain MCP Tool`
>
>    2. **Audience**: `supply-chain-mcp-tool`
>
> 3. Click **Next**.
>
> 4. Define attributes for the resource:
>
>    Detailed steps follow the table.
>
>    | Attribute | Required | Expression                                                                                                                                                                                                                                               |
>    | --------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>    | `sub`     | No       | ```spel
>    (#root.context.requestData.grantType == "client_credentials") ? "no-subject" : #root.context.requestData.subjectToken.client_id
>    ```                                                                                                              |
>    | `act`     | Yes      | ```spel
>    (#root.context.requestData.grantType == "client_credentials")?"noActor":((#root.context.requestData.subjectToken.may_act.sub == #root.context.requestData.actorToken.client_id)?{"sub":#root.context.requestData.actorToken.client_id}:null)
>    ``` |
>
>    1. Click the **Gear** icon ([icon: gear, set=fa]) next to the `sub` attribute, enter the expression, and click **Save**.
>
>       Learn more about expressions in [Using the expression builder](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_use_expression_builder.html) in the PingOne documentation.
>
>    2. Click **+ Add** and name the attribute `act`.
>
>    3. Click [icon: gear, set=fa], enter the expression, and click **Save**.
>
>    4. Select the **Required** checkbox for the `act` attribute.
>
>       This ensures that any token exchange that fails to set `act` is rejected.
>
> 5. Click **Next**, then click **+ Add Scope**.
>
> 6. Name the scope `supply-chain:restock`.
>
> 7. Click **Save**.

> **Collapse: Deploy the Supply Chain MCP Tool to Google Cloud Run**
>
> Build the MCP server with configured environment variables and deploy it as a Google Cloud Run service.
>
> 1. Set environment variables for the MCP server:
>
>    1. In the cloned Gemini Enterprise Agent Platform Integrations repository, go to the `pingone/baseline-autonomous-agent-to-tool/services/supply-chain-mcp-tool` directory.
>
>    2. Make a copy of the `.env.sample` file and name it `.env`:
>
>       ```bash
>       cp .env.sample .env
>       ```
>
>    3. Set environment variables in the `.env` file:
>
>       | Variable                    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
>       | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       | `GC_REGION`                 | Your Google Cloud Platform region. For example: `us-central1`.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
>       | `GC_CLOUD_RUN_SERVICE_NAME` | The Cloud Run service name: `baatt-supply-chain-mcp-tool`.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
>       | `IDP_ISSUER`                | The PingOne issuer URL: `https://auth.pingone.<region>/<env-id>/as`.Set the placeholders:- \<region>: The country code top-level domain (ccTLD), such as `.com`, `.eu`, `.asia`. You can find this in your PingOne admin console URL. For example, `https://console.pingone.com/index.html?env=12345678-1234-1234-1234-123456789012` has a ccTLD of `.com`.
>
>       - \<env-id>: The PingOne environment ID. In the example PingOne admin console URL, the ID is `12345678-1234-1234-1234-123456789012`. |
>       | `IDP_REQUIRED_AUDIENCE`     | The expected `aud` claim. Enter the audience you gave the BAATT Supply Chain MCP Tool resource in PingOne: `supply-chain-mcp-tool`.                                                                                                                                                                                                                                                                                                                                                               |
>       | `IDP_REQUIRED_SCOPE`        | The scope the inbound token must carry. Enter the scope you gave the BAATT Supply Chain MCP Tool resource in PingOne: `supply-chain:restock`.                                                                                                                                                                                                                                                                                                                                                     |
>
> 2. In the `pingone/baseline-autonomous-agent-to-tool/services/supply-chain-mcp-tool` directory, run the following command:
>
>    ```bash
>    make deploy
>    ```
>
>    This builds the Docker image, pushes it to Google Container Registry, and deploys it to Cloud Run.

> **Collapse: Register the Supply Chain MCP Tool in Agent Registry**
>
> Register the MCP server in Agent Registry to ensure the Agent Gateway recognizes it as an approved egress destination.
>
> 1. In Google Cloud, go to **Agent Platform > Govern > Agent Registry** and click **Add MCP Server**.
>
> 2. Enter the following values:
>
>    * **Name**: `BAATT Supply Chain MCP Tool`
>
>    * **Description**: `Simple Restock tool for BAATT demo`
>
> 3. Select your **Region**. For example: `us-central1`.
>
> 4. Enter the MCP server URL:
>
>    1. To find the URL, duplicate the browser tab and go to **Cloud Run > Services**. Click the **baatt-supply-chain-mcp-tool service**.
>
>    2. Copy the URL at the top of the page. For example: `https://baatt-supply-chain-mcp-tool-909399354423.us-central1.run.app`.
>
>    3. In Agent Registry, paste the URL in the **MCP server URL** field, and then add `/mcp` to the end of the URL.
>
> 5. Enter the MCP specification JSON, which defines the MCP server's endpoints and expected request and response formats.
>
>    1. In the cloned repository, go to the `pingone/baseline-autonomous-agent-to-tool/services/supply-chain-mcp-tool` directory and copy the contents of the `tool-spec.json` file.
>
>    2. In Agent Registry, paste the copied contents into the **JSON** field.
>
>    3. Click **Next**.
>
> 6. Click **Save** to complete the registration.
>
> |   |                                                                                                                                                                                                                                                |
> | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | Keep the `tool-spec.json` file in sync with the `RestockInput struct` and `RestockOutput struct` tag definitions in the `restock.go` file. If the definitions change, update `tool-spec.json` and reregister the MCP server in Agent Registry. |

### Create authorization policies in PingOne Authorize

Create policies that decide whether the service extension permits the agent's request to the MCP server. You'll create a policy for the agent's identity and another policy for the time of the request.

> **Collapse: Create attributes in the Trust Framework**
>
> Create attributes in PingOne Authorize that extract information from service extension decision requests. These attributes are used in authorization policies to determine whether the agent is allowed to access the MCP server.
>
> |   |                                                                                                                                                                                                                     |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [adding authorization attributes](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1_az_adding_attributes.html) in the PingOne Authorize documentation. |
>
> | Name              | Type       | Resolver Parameter |
> | ----------------- | ---------- | ------------------ |
> | `Agent Client ID` | **String** | `agent_client_id`  |
> | `Request Hour`    | **Number** | `request_hour`     |
>
> 1. In the PingOne admin console, go to **Authorization > Trust Framework**.
>
> 2. On the **Attributes** tab, click the **[icon: plus, set=fa]**icon.
>
> 3. Name the attribute `Agent Client ID`.
>
>    The attribute name must match the parameter key in the decision request. It's case-sensitive.
>
> 4. In the **Resolvers** section, click **[icon: plus, set=fa]Add Resolver** and keep the default **Request Parameter** resolver.
>
> 5. (Optional) Name the resolver `agent_client_id` to match the parameter name in the agent's request.
>
>    Request Parameter resolvers extract values from decision requests and pass them to PingOne Authorize for evaluation. The resolver name is a label only and isn't matched to the parameter name in the request.
>
> 6. For the Value Settings **Type**, keep the default value of **String**.
>
> 7. Click **Save Changes**.
>
> 8. Repeat the steps above to add the `Request Hour` attribute, with a resolver optionally named `request_hour` and the value settings type **Number**. Delete the **Parent** to keep the attribute at the top level.

> **Collapse: Create the BAATT Agent Gateway Policies policy set**
>
> Create a policy set in PingOne Authorize that contains the policies governing the agent's access to the MCP server.
>
> |   |                                                                                                                                                                                                                 |
> | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [adding policy sets](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_policy_or_policy_set.html) in the PingOne Authorize documentation. |
>
> 1. In the PingOne admin console, go to **Authorization > Policies**.
>
> 2. Click the **[icon: plus, set=fa]**icon and select **Add Policy Set**.
>
> 3. Name the policy set `BAATT Agent Gateway Policies`.
>
> 4. For the **Combining Algorithm**, select **Unless one decision is deny, the decision will be permit**.
>
> 5. Click **Save changes**.

> **Collapse: Create the Only Permit CRM Agent policy**
>
> Create a policy that permits only the CRM Agent to access the MCP server. Agents that don't match the CRM Agent's client ID are denied access.
>
> |   |                                                                                                                                                                                                              |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> |   | You can find more details about [adding policies](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_policy_or_policy_set.html) in the PingOne Authorize documentation. |
>
> 1. In **Authorization > Policies**, select the **BAATT Agent Gateway Policies** policy set.
>
> 2. Click the **[icon: plus, set=fa]**icon and select **Add Policy**.
>
> 3. Name the policy `Only Permit CRM Agent`.
>
> 4. In **Applies When**:
>
>    1. Click **+ Comparison** and select the **Agent Client ID** attribute.
>
>    2. Select the **Does Not Equal** operator.
>
>    3. []()For the value, enter this placeholder: `<CRM_AGENT_CLIENT_ID>`.
>
>       Later, you'll [replace this with the client ID](#idai-gemini-aut-deployed-agent-id) of the CRM Agent you want to permit.
>
> 5. For the **Combining Algorithm**, select **Unless one decision is deny, the decision will be permit**.
>
> 6. Click **+ Add Rule**, name the rule `Deny`, then for **Effect**, select **Deny**.
>
> 7. Click **Save changes**.

> **Collapse: Create the Only Permit During Business Hours policy**
>
> Create a policy that permits access to the MCP server only during business hours. PingOne Authorize will deny access if the request hour is before 8:00 AM or after 5:00 PM.
>
> The service extension converts from UTC before sending a decision request to ensure permitted hours are in local time. For example, a request at 3:00 PM UTC is converted to 8:00 AM Pacific and is permitted, while a request at 3:00 AM UTC is converted to 8:00 PM Pacific and is denied.
>
> |   |                                                                                                                                                                                                              |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> |   | You can find more details about [adding policies](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_policy_or_policy_set.html) in the PingOne Authorize documentation. |
>
> 1. In **Authorization > Policies**, select the **BAATT Agent Gateway Policies** policy set.
>
> 2. Click the **[icon: plus, set=fa]**icon and select **Add Policy**.
>
> 3. Name the policy `Only Permit During Business Hours`.
>
> 4. In **Applies When**:
>
>    1. Click **+ Comparison**, then select **Any**.
>
>    2. Select the **Request Hour** attribute.
>
>    3. Select the **Greater Than** operator.
>
>    4. For the value, enter `17`.
>
>    5. Click **+ Comparison** and select the **Request Hour** attribute.
>
>    6. Select the **Less Than** operator.
>
>    7. For the value, enter `8`.
>
> 5. For the **Combining Algorithm**, select **Unless one decision is deny, the decision will be permit**.
>
> 6. Click **+ Add Rule**, name the rule `Deny`, then for **Effect**, select **Deny**.
>
> 7. Click **Save changes**.

> **Collapse: Publish an authorization policy version**
>
> Publish a policy version to deploy your policies to a decision endpoint and make them available in decision evaluations.
>
> |   |                                                                                                                                                                                                                 |
> | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [publishing policy versions](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_publishing_versions.html) in the PingOne Authorize documentation. |
>
> 1. In the PingOne admin console, go to **Authorization > Version History**.
>
> 2. Click the **More Options (⋮)** icon next to the **Latest Version** and select **Publish Version**.
>
> 3. In the **Publish to** list, select a decision endpoint.
>
> 4. For the version **Name**, enter `BAATT`.
>
> 5. Click **Publish**.
>
>    The version name and the endpoint the version is published to are displayed in **Version History**.
>
> 6. []()Go to **Authorization > Decision Endpoints** and expand the decision endpoint where you published the policy version. Copy the decision endpoint URL and save it somewhere convenient. You'll need it [later](#idai-gemini-aut-authz-dec-endpoint).

### Deploy the Agent Gateway Service Extension

The [Agent Gateway Service Extension](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/baseline-autonomous-agent-to-tool/services/agent-gateway-extension-service) is an Envoy `ext_proc` gRPC handler that the Agent Gateway calls to request authorization decisions and perform token exchanges.

You'll deploy the service extension to Cloud Run to govern requests bound for the Supply Chain MCP Tool. During this flow, the service extension:

* Validates the agent's token, specifically checking the `iss`, `aud`, and `scope` claims.

* Calls PingOne Authorize on `tools/call` requests to evaluate the agent's identity and the request hour. Non-invocation requests (`initialize`, `tools/list`) skip this authorization check.

* Upon a permit decision, performs an [RFC 8693](https://datatracker.ietf.org/doc/html/rfc8693) token exchange to generate a token restricted to the supply chain tool (`aud`).

* Injects the new credential as an `Authorization: Bearer` header before forwarding the request to the Supply Chain MCP Tool.

> **Collapse: Create a PingOne worker application**
>
> Create a PingOne worker application that the service extension uses to call PingOne Authorize for authorization decisions.
>
> |   |                                                                                                                                                                               |
> | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [adding applications](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html) in the PingOne documentation. |
>
> 1. In the PingOne admin console, go to **Applications > Applications**.
>
> 2. Click the **[icon: plus, set=fa]**icon and create the application profile:
>
>    1. Name the application `BAATT PingOne Authorize Worker App`.
>
>    2. For the **Application Type**, click **Worker**.
>
>    3. Click **Save**.
>
> 3. To enable the application, click the toggle next to the application name in the details panel.
>
> 4. On the **Configuration** tab, click the Pencil icon ([icon: pencil, set=fa]), make sure **Client Credentials** is the **Grant Type**, then click **Cancel**.
>
> 5. On the **Roles** tab, click **Grant Roles**.
>
> 6. Expand the **Environment Admin** role and select your environment.
>
> 7. Click **Save**.

> **Collapse: Create a PingOne application for token exchange**
>
> Create a PingOne OIDC application that the service extension uses to perform token exchanges for the MCP server.
>
> |   |                                                                                                                                                                               |
> | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [adding applications](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html) in the PingOne documentation. |
>
> 1. In the PingOne admin console, go to **Applications > Applications**.
>
> 2. Click the **[icon: plus, set=fa]**icon and create the application profile:
>
>    1. Name the application `BAATT Agent Gateway Extension`.
>
>    2. For the **Application Type**, click **OIDC Web App**.
>
>    3. Click **Save**.
>
> 3. To enable the application, click the toggle next to the application name in the details panel.
>
> 4. On the **Configuration** tab, click [icon: pencil, set=fa]:
>
>    1. For **Grant Type**, select **Client Credentials** and **Token Exchange**.
>
>    2. Clear the **Code** and **Authorization Code** checkboxes.
>
>    3. Click **Save**
>
> 5. On the **Resources** tab, click [icon: pencil, set=fa], then select the **supply-chain:restock** scope on the BAATT Supply Chain MCP Tool.
>
> 6. Click **Save**.

> **Collapse: Deploy the Agent Gateway Service Extension to Cloud Run**
>
> Build the service extension with configured environment variables and deploy it as a Google Cloud Run service.
>
> 1. Set environment variables for the service extension:
>
>    1. In the cloned repository, go to the `pingone/baseline-autonomous-agents-to-tool/services/agent-gateway-extension-service` directory.
>
>    2. Make a copy of the `.env.sample` file and name it `.env`:
>
>       ```bash
>       cp .env.sample .env
>       ```
>
>    3. Set environment variables in the `.env` file:
>
>       | Variable                      | Value                                                                                                                                                                                                                                                                                                                                                                                                |
>       | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       | `GC_REGION`                   | Your Google Cloud Platform region. For example: `us-central1`.                                                                                                                                                                                                                                                                                                                                       |
>       | `GC_CLOUD_RUN_SERVICE_NAME`   | The Cloud Run service name: `baatt-agent-gateway-extension-service`.                                                                                                                                                                                                                                                                                                                                 |
>       | `GC_SERVICE_EXTENSION_NAME`   | The deployed service extension's name (created when the service extension was registered): `baatt-agent-gateway-extension`.                                                                                                                                                                                                                                                                          |
>       | `IDP_ISSUER`                  | The PingOne issuer URL: `https://auth.pingone.<region>/<env-id>/as`.To find this endpoint, go to the BAATT Agent Gateway Extension application in PingOne. Copy the **Issuer ID** under **Connection Details** on the **Overview** tab.                                                                                                                                                              |
>       | `EXCHANGE_CLIENT_ID`          | The BAATT Agent Gateway Extension application's **Client ID**. This is located above **Connection Details** on the **Overview** tab.                                                                                                                                                                                                                                                                 |
>       | `EXCHANGE_CLIENT_SECRET`      | The BAATT Agent Gateway Extension application's **Client Secret**. This is located above **Connection Details** on the **Overview** tab.                                                                                                                                                                                                                                                             |
>       | `AUTHZ_CLIENT_ID`             | The BAATT PingOne Authorize Worker App's **Client ID**. This is located above **Connection Details** on the **Overview** tab for this application.                                                                                                                                                                                                                                                   |
>       | `AUTHZ_CLIENT_SECRET`         | The BAATT PingOne Authorize Worker App's **Client Secret**. This is located above **Connection Details** on the **Overview** tab.                                                                                                                                                                                                                                                                    |
>       | []()`AUTHZ_DECISION_ENDPOINT` | The PingOne Authorize decision endpoint URL where you published the policy version [earlier](#idai-gemini-aut-decision-endpoint).                                                                                                                                                                                                                                                                    |
>       | `IDP_REQUIRED_AUDIENCE`       | The expected `aud` on the inbound token. Enter the audience you gave the BAATT Supply Chain MCP Tool resource in PingOne: `google-cloud-agent-gateway`.                                                                                                                                                                                                                                              |
>       | `IDP_REQUIRED_SCOPE`          | The scope the inbound token must carry. Enter the scope you gave the BAATT Supply Chain MCP Tool resource in PingOne: `supply-chain:restock`.                                                                                                                                                                                                                                                        |
>       | `TOOL_URL`                    | The MCP tool's Cloud Run base URL: `https://baatt-supply-chain-mcp-tool-<your-project-number>.<your-deployment-region>.run.app`.To find this URL, go to **Cloud Run > Services** and click the **baatt-supply-chain-mcp-tool** service. Copy the URL at the top of the page (for example, `https://baatt-supply-chain-mcp-tool-909399354423.us-central1.run.app`). Paste the URL in the `.env` file. |
>       | `TOOL_SCOPE`                  | The scope the service extension requests during token exchange to authorize access to the downstream MCP server: `supply-chain:restock`.                                                                                                                                                                                                                                                             |
>
> 2. In the `pingone/baseline-autonomous-agent-to-tool/services/agent-gateway-extension-service` directory, run the following commands:
>
>    ```bash
>    make deploy
>    ```
>
>    This builds the Docker image, pushes it to Google Container Registry, and deploys it to Cloud Run.
>
>    ```bash
>    make register
>    ```
>
>    This command registers your deployed Cloud Run service as an available service extension in Google Cloud. Behind the scenes, it renders the `service-extension.tmpl.yaml` template with the live Cloud Run URL and imports the configuration, preparing the extension for use by the Agent Gateway.

### Create the Agent Gateway

The [Agent Gateway](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/baseline-autonomous-agent-to-tool/services/agent-gateway) is a Google-managed resource that acts as the policy enforcement point for all agent egress traffic. It intercepts all outbound traffic bound for downstream tools and routes it to the service extension.

You'll configure the gateway to call the service extension, using [Envoy external processing](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_proc_filter) (`ext_proc`), on every request to the Supply Chain MCP Tool. This includes attaching the Agent Gateway Service Extension to the gateway, registering the egress destinations it can reach, and creating the PingOne resource that licenses the service extension as the only actor allowed to exchange tokens bound for the gateway.

> **Collapse: Configure Agent Gateway environment variables**
>
> Configure the environment variables required to deploy the Agent Gateway and link it to the service extension.
>
> 1. Set environment variables for the Agent Gateway:
>
>    1. In the cloned repository, go to the `pingone/baseline-autonomous-agents-to-tool/services/agent-gateway` directory.
>
>    2. Make a copy of the `.env.sample` file and name it `.env`:
>
>       ```bash
>       cp .env.sample .env
>       ```
>
>    3. Check the environment variables in the `.env` file. Most are already defined.
>
>       | Variable                    | Value                                                                                                                       |
>       | --------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
>       | `GC_REGION`                 | Your Google Cloud Platform region. For example: `us-central1`.                                                              |
>       | `GC_GATEWAY_NAME`           | The Agent Gateway's name: `baatt-agent-gateway`.                                                                            |
>       | `GC_SERVICE_EXTENSION_NAME` | The deployed service extension's name (created when the service extension was registered): `baatt-agent-gateway-extension`. |
>       | `GC_AUTHZ_POLICY_NAME`      | The name of the Google Cloud authorization policy resource that binds the extension to the gateway: `baatt-authz-policy`.   |

> **Collapse: Create the Agent Gateway in Google Cloud**
>
> Use the Google Cloud Console to deploy the Agent Gateway. This creates the service that intercepts agent egress and hands requests to the service extension.
>
> 1. In Google Cloud, go to **Agent Platform > Govern > Gateways** and click **Add gateway**.
>
> 2. Enter the following values:
>
>    * **Name**: `baatt-agent-gateway`.
>
>    * **Region**: Your Google Cloud Platform region. For example: `us-central1`.
>
>    * **Deployment mode**: Keep the default **Google-managed**.
>
>    * **Agent registries**: Keep the default **Regional registry**.
>
>    * **Governed Access Path**: Keep the default **Agent-to-Anywhere (egress)**.
>
>    * **Access Authorization**: Select **Enforce policies**.
>
>    * **Policy Model**: Select **Allow Policy**.
>
> 3. Click **Save gateway**.

> **Collapse: Attach the Agent Gateway Service Extension to the Agent Gateway**
>
> To enforce your access policies, you must connect the service extension to the Agent Gateway. The `make attach` command populates `authz-policy.tmpl.yaml` with your project, region, and gateway name, and then imports it with `gcloud`. This creates an authorization policy that binds the extension to the gateway as a `CONTENT_AUTHZ` policy scoped to the `/mcp` path.
>
> 1. In the `pingone/baseline-autonomous-agent-to-tool/services/agent-gateway` directory, run the following command:
>
>    ```bash
>    make attach
>    ```
>
>    |   |                                                                                  |
>    | - | -------------------------------------------------------------------------------- |
>    |   | You can run `make render` alone to inspect the generated YAML without importing. |
>
> There are now two complementary authorization extensions attached to the Agent Gateway:
>
> | Extension                                | Service role    | Target                      | Description                                                                                                                                                                                                                                                          |
> | ---------------------------------------- | --------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `baatt-agent-gateway-iap-authzextension` | `REQUEST_AUTHZ` | `iap.googleapis.com`        | A Google-managed extension automatically created with the gateway. It enforces the Identity-Aware Proxy (IAP) identity and egress check (`iap.egressor`), which appears on the gateway as the **Auth provider: Google Cloud Identity-Aware Proxy**.                  |
> | `baatt-agent-gateway-extension`          | `CONTENT_AUTHZ` | Cloud Run service extension | The extension created in the previous step. It routes traffic to your Cloud Run host and requests an authorization decision. Upon permit, the extension performs the PingOne token exchange and injects the resulting delegated token in the `Authorization` header. |

> **Collapse: Register egress destinations for the Agent Gateway**
>
> Because the Agent Gateway governs all agent egress, every host the agent communicates with must be registered as a destination in Agent Registry. Your environment currently includes the following registered destinations:
>
> * **MCP tools:** The BAATT Supply Chain MCP Server was registered as an MCP server (rather than a standard endpoint) when you deployed it.
>
> * **Google APIs:** Endpoints for `aiplatform`, `iamcredentials`, and telemetry (`*.mtls.googleapis.com`) were automatically generated during the gateway deployment to support the runtime's internal egress. Don't modify these endpoints.
>
> You'll register the PingOne host as the final required egress endpoint.
>
> 1. In Google Cloud, go to **Agent Platform > Govern > Agent Registry** and click **Add Endpoint**.
>
> 2. Enter the following values:
>
>    * **Name**: `PingOne`.
>
>    * **Region**: Your Google Cloud Platform region. For example: `us-central1`.
>
>    * **Destination URL**: Your PingOne host. For example: `https://auth.pingone.com`.
>
> 3. Click **Save**.

> **Collapse: Create the Agent Gateway resource in PingOne**
>
> The Agent Gateway resource is used to issue the agent's initial subject token. To ensure secure delegation, this resource must explicitly authorize the service extension to perform token exchanges on the agent's behalf.
>
> You'll configure a `may_act` attribute to identify the service extension as the sole authorized actor. During a token exchange, the downstream tool resource evaluates the `may_act` claim to verify the extension's authority. Any other client attempting an exchange will fail the tool's validation.
>
> Because tokens for this gateway resource are only generated using the `client_credentials` grant, and never through a token exchange, an `act` attribute isn't required. The delegation proof is handled by the downstream tool resource (you've already mapped a corresponding `act` attribute to validate this delegation). The agent's identity is preserved in the `client_id`.
>
> |   |                                                                                                                                                                            |
> | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [adding custom resources](https://docs.pingidentity.com/pingone/applications/p1_adding_custom_resource.html) in the PingOne documentation. |
>
> 1. In the PingOne admin console, go to **Applications > Resources** and click the **[icon: plus, set=fa]**icon.
>
> 2. Define the resource:
>
>    1. **Resource Name**: `BAATT Google Cloud Agent Gateway`
>
>    2. **Audience**: `google-cloud-agent-gateway`
>
> 3. Click **Next**.
>
> 4. Define an attribute for the resource:
>
>    | Attribute | Required | Expression                                |
>    | --------- | -------- | ----------------------------------------- |
>    | `may_act` | No       | ```spel
>    {"sub":"<EXT-SVC-CLIENT-ID>"}
>    ``` |
>
>    1. Click **+ Add** and name the attribute `may_act`.
>
>    2. Click the **Gear** icon ([icon: gear, set=fa]) next to the `may_act` attribute, enter the expression, and click **Save**.
>
>       Learn more about expressions in [Using the expression builder](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_use_expression_builder.html) in the PingOne documentation.
>
> 5. Click **Next**, then click **+ Add Scope**.
>
> 6. Name the scope `supply-chain:restock`.
>
> 7. Click **Save**.

### Deploy the CRM Agent

The [CRM Agent](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/baseline-autonomous-agent-to-tool/services/agent) is an ADK-based agent deployed to the Google Cloud Agent Runtime. Operating as an MCP client, it connects to the Supply Chain MCP Tool to execute the restock tool.

The agent authenticates to PingOne as an independent client and includes its token in the `Authorization: Bearer` header of each outbound MCP request. The Agent Runtime routes this egress traffic through the Agent Gateway, where the service extension uses the agent's token as the subject of an RFC 8693 token exchange to generate a new token scoped specifically for the downstream tool.

You'll create an identity for the agent in PingOne and deploy the agent to the Agent Runtime, binding it to the Agent Gateway.

> **Collapse: Create the CRM Agent in PingOne**
>
> Create an AI agent in PingOne to establish a dedicated identity for the CRM Agent. This identity enables the agent to authenticate and acquire an initial access token. The Agent Gateway will use the agent's token as the subject token during the delegation exchange.
>
> |   |                                                                                                                                                              |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> |   | You can find more details about [adding AI agents](https://docs.pingidentity.com/pingone/ai_agents/p1_managing_ai_agents.html) in the PingOne documentation. |
>
> 1. In the PingOne admin console, go to **AI Agents** and click the **[icon: plus, set=fa]**icon.
>
> 2. Name the agent `BAATT CRM Agent`.
>
> 3. Click **Save**.
>
> 4. To enable the agent, click the toggle next to the agent name in the details panel.
>
> 5. On the **Configuration** tab, click [icon: pencil, set=fa]:
>
>    1. In **Grant Type**, select **Client Credentials**.
>
>    2. Clear the **Code** and **Authorization Code** checkboxes.
>
>    3. Click **Save**
>
> 6. On the **Resources** tab, click [icon: pencil, set=fa], then select the **supply-chain:restock** scope on the BAATT Google Cloud Agent Gateway.
>
> 7. Click **Save**.
>
> 8. []()On the **Overview** tab, copy the agent's **Client ID**. Use this value to replace the `<CRM_AGENT_CLIENT_ID>` [placeholder](#idai-gemini-aut-agent-id) in the Only Permit CRM Agent policy you created earlier.

> **Collapse: Deploy and register the CRM Agent in Agent Registry**
>
> To finish CRM Agent setup, deploy it to the Google Cloud Agent Runtime. This deployment automatically registers the agent in Agent Registry and routes all of its egress traffic through the Agent Gateway.
>
> 1. Set environment variables for the agent:
>
>    1. In the cloned repository, go to the `pingone/baseline-autonomous-agents-to-tool/services/agent` directory.
>
>    2. Make a copy of the `.env.sample` file and name it `.env`:
>
>       ```bash
>       cp .env.sample .env
>       ```
>
>    3. Set environment variables in the `.env` file:
>
>       | Variable              | Value                                                                                                                                                                                                                                                                                                                                                                                                                              |
>       | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       | `GC_REGION`           | Your Google Cloud Platform region. For example: `us-central1`.                                                                                                                                                                                                                                                                                                                                                                     |
>       | `AGENT_DISPLAY_NAME`  | Display name for the Reasoning Engine: `baatt-crm-agent`.                                                                                                                                                                                                                                                                                                                                                                          |
>       | `IDP_ISSUER`          | The PingOne issuer URL: `https://auth.pingone.<region>/<env-id>/as`.To find this endpoint, go to the BAATT CRM Agent in PingOne. Copy the **Issuer ID** under **Connection Details** on the **Overview** tab.                                                                                                                                                                                                                      |
>       | `GC_AGENT_GATEWAY`    | The Agent Gateway resource name: `baatt-agent-gateway`.                                                                                                                                                                                                                                                                                                                                                                            |
>       | `AGENT_CLIENT_ID`     | The BAATT CRM Agent's **Client ID**. This is located above **Connection Details** on the agent's **Overview** tab in PingOne.                                                                                                                                                                                                                                                                                                      |
>       | `AGENT_CLIENT_SECRET` | The BAATT CRM Agent's **Client Secret**. This is located above **Connection Details** on the agent's **Overview** tab.                                                                                                                                                                                                                                                                                                             |
>       | `TOOL_MCP_URL`        | The MCP tool's Cloud Run base URL: `https://baatt-supply-chain-mcp-tool-<your-project-number>.<your-deployment-region>.run.app/mcp`.To find this URL, go to **Cloud Run > Services** and click the **baatt-supply-chain-mcp-tool** service. Copy the URL at the top of the page (for example, `https://baatt-supply-chain-mcp-tool-909399354423.us-central1.run.app`). Paste the URL in the `.env` file and add `/mcp` at the end. |
>       | `TOOL_SCOPE`          | The scope the agent requests during token exchange to authorize access to the downstream MCP server: `supply-chain:restock`.                                                                                                                                                                                                                                                                                                       |
>
> 2. In the `pingone/baseline-autonomous-agent-to-tool/services/agent` directory, run the following command:
>
>    ```bash
>    make deploy
>    ```
>
>    The `deploy.py` script provisions the Reasoning Engine using `identity_type = AGENT_IDENTITY`. The script also binds the engine to the gateway and grants it the `roles/iap.egressor` role on Agent Registry, authorizing the agent to securely reach all registered downstream endpoints.

## Validation

To validate the autonomous workflow, trigger a test restock to prompt the CRM Agent to invoke the Supply Chain MCP Server. A successful run ends with the agent returning a restock confirmation.

1. In the `pingone/baseline-autonomous-agent-to-tool` directory, run the following command:

   ```bash
   make test
   ```

   A successful run ends with the agent reporting back. For example:

   ```json
   Your restock order for 500 units of WIDGET-9000 has been accepted.
   The order ID is ORD-20240101-001.
   ```

2. To trace the delegation, follow the Cloud Run service logs (`baatt-agent-gateway-extension-service` and `baatt-supply-chain-mcp-tool`) while the command runs. In order, you should see:

   ```bash
   # service extension: every MCP request (initialize, tools/list, tools/call)
   # is validated, exchanged, and forwarded with a fresh tool token.
   [ExtSvc] request authority="baatt-supply-chain-mcp-tool-...run.app" path="/mcp" governed=true
   [ExtSvc] delegated tool token minted
   [ExtSvc] injecting delegated token for baatt-supply-chain-mcp-tool-...run.app

   # service extension: {p1-paz} is consulted on tools/call only.
   [ExtSvc] authorize agent=<agent-client-id> hour=15
   [ExtSvc] {p1-paz} PERMIT agent=<agent-client-id>

   # Supply chain tool: every request's token is verified (signature, issuer,
   # audience, scope) before handling. The log shows who the call is for (sub),
   # which audience it was minted for (aud), who acted for it (act.sub, the
   # delegation proof), and the granted scope.
   [SupplyChain] Token verified — sub=<agent-client-id> aud=[supply-chain-mcp-tool] act.sub=<ext-svc-client-id> scope="supply-chain:restock" forwarding to MCP handler

   # Supply chain tool: the restock itself runs only after the PERMIT above.
   [SupplyChain] tools/call restock — 500 units of WIDGET-9000 for region us-west-2
   ```

When reviewing the logs, the following is important:

* The initial `initialize` and `tools/list` requests represent the agent and the MCP server negotiating the tool schema. Only the final `tools/call` request is subject to PingOne Authorize policy enforcement.

* If the restock operation fails, review the service extension log. It includes PingOne Authorize deny decisions, failed token exchanges, and token validation errors.

## Troubleshooting

If you encounter issues while deploying or testing the agent, use the following information to help resolve common problems.

* Agent requests are dropped before authorization

  Check the service extension logs in Cloud Run to determine if the request was blocked during initial token validation before it reached PingOne Authorize.

* PingOne Authorize denies the agent's request

  * Verify that you replaced the \<CRM_AGENT_CLIENT_ID> [placeholder](#idai-gemini-aut-agent-id) in the Only Permit CRM Agent policy with the client ID of the deployed CRM agent. If this placeholder isn't updated, the policy can't identify the agent and will reject the request.

  * Review [Recent Decisions](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_recent_decisions.html) in PingOne Authorize to identify which policy condition caused the denial.

    |   |                                                                                                                                                                                                                           |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Enable **Record recent decisions** on your PingOne Authorize decision endpoint to view full request payloads and step-by-step policy evaluation results. This provides visibility into why a specific request was denied. |

* Token exchange fails

  Verify that the `TOOL_SCOPE` environment variable configured in Cloud Run exactly matches the scope defined on the downstream tool resource in PingOne. Additionally, confirm that the Agent Gateway resource's `may_act` attribute correctly licenses the service extension.

* The agent can't reach egress destinations

  If the gateway returns a 403 Forbidden error indicating that the egress request isn't authorized, verify that the Reasoning Engine identity has the `roles/iap.egressor` role in Google Cloud. The agent requires this role on Agent Registry to pass the IAP egress check. You can also verify IAP allow or deny decisions in the Google Cloud IAP audit logs.

## What's next

Learn how to [authorize Gemini agents to act on behalf of users](idai-authorizing-gemini-on-behalf-of-users-with-ping.html).

|   |                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To prepare your environment for authorizing agents on behalf of users, clean up the resources you deployed for autonomous agents. From the `pingone/baseline-autonomous-agent-to-tool` directory, run the `make destroy` command to safely remove the Google Cloud infrastructure specific to this use case. |

---

---
title: Authorizing Gemini Agent2Agent (A2A) chains with Ping Identity solutions
description: "Authorize a Gemini Agent2Agent chain that delegates the user's token throughout the chain."
component: identity-for-ai
page_id: identity-for-ai:integrations:idai-authorizing-gemini-agent2agent-with-ping
canonical_url: https://developer.pingidentity.com/identity-for-ai/integrations/idai-authorizing-gemini-agent2agent-with-ping.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-10-14T19:08:24Z
keywords: ["Identity for AI", "ai identity", "ai security", "Google Cloud Gemini Enterprise", "Gemini Enterprise Agent Platform", "PingOne Authorize", "authentication", "authorization"]
section_ids:
  how-this-works: How this works
  components: Components
  token-chain: Token chain
  benefits-of-this-approach: Benefits of this approach
  goals: Goals
  what-youll-do: What you'll do
  before-you-begin: Before you begin
  tasks: Tasks
  idai-gemini-a2a-mcp-server: Deploy the Order Status MCP Server
  idai-gemini-a2a-policies: Create authorization policies in PingOne Authorize
  idai-gemini-a2a-extension-service: Deploy the Agent Gateway Service Extension
  idai-gemini-a2a-agent-gateway: Create the Agent Gateway
  idai-gemini-a2a-order-status-agent: Deploy the Order Status Agent
  idai-gemini-a2a-support-agent: Deploy the Support Agent
  idai-gemini-a2a-agent-bridge: Deploy the Agent Bridge
  idai-gemini-a2a-chat-ui: Deploy the Chat UI
  validation: Validation
  troubleshooting: Troubleshooting
  whats-next: What's next
---

# Authorizing Gemini Agent2Agent (A2A) chains with Ping Identity solutions

This use case secures multiple agents in an A2A chain to reach a downstream tool, requiring authorization at each step in the chain.

After the user authenticates through a Chat UI, each agent uses [RFC 8693](https://datatracker.ietf.org/doc/html/rfc8693) token exchange to generate a token scoped for the next destination in the chain. The Google Cloud Agent Gateway Service Extension intercepts these requests, validates tokens, and executes subsequent token exchanges for every agent interaction. A token for a specific agent isn't usable anywhere else in the chain. The downstream tool eventually receives a narrowly scoped, short-lived token with a nested `act` claim recording the delegation chain from the original user to the downstream tool.

This use case extends the core [Integrating Gemini Enterprise Agent Platform with Ping Identity solutions](idai-integrating-gemini-agent-platform-with-ping.html) architecture by introducing a multi-agent delegation chain.

## How this works

Consider a scenario where a user-facing Support Agent answers questions about orders by delegating tasks to a specialized Order Status Agent, which in turn queries an Order Status MCP Server.

![Diagram showing an Agent2Agent flow.](_images/idai-gemini-a2a-flow.png)

This multi-agent architecture follows a sequence of validation, policy enforcement, and token exchange:

1. The user authenticates through the Chat UI.

2. The Support Agent exchanges the user's token for a delegated token licensed for the Agent Gateway, then initiates an A2A request to the Order Status Agent. The Agent Gateway intercepts this outbound call.

3. The Agent Gateway Service Extension validates the token and requests an authorization decision from PingOne Authorize. Upon a `PERMIT` decision, the service extension performs a token exchange to generate a new token scoped for the Order Status Agent, then forwards the request.

4. The Order Status Agent validates the received token. To call the downstream tool, it performs its own token exchange targeting the Agent Gateway.

5. The Agent Gateway intercepts the Order Status Agent's outbound MCP request. The service extension requests another authorization decision and performs the final token exchange to generate a token scoped for the Order Status MCP Server.

6. The request reaches the MCP server. The server validates the token, which contains a nested `act` claim recording the complete delegation history (service extension to Order Status Agent, to service extension, to Support Agent). The MCP server executes the action.

If PingOne Authorize returns a `DENY` decision, the service extension blocks the request and returns an error, preventing unauthorized agent access to downstream resources.

### Components

| Component                                                                                                                                                                                  | Role                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [Chat UI](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-chaining/services/chat-ui)                                                 | User chat interface with PingOne PKCE sign-on.                                                                                            |
| [Agent Bridge](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-chaining/services/agent-bridge)                                       | Google Cloud entry point. Validates the user token and stores it in the agent session state.                                              |
| [Support Agent](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-chaining/services/support-agent)                                     | User-facing agent. Exchanges the user's token and delegates to the Order Status Agent over A2A.                                           |
| [Order Status Agent](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-chaining/services/order-status-agent)                           | Specialized agent that owns order lookup. Validates the inbound delegation token, then does a token exchange and calls the MCP server.    |
| [Agent Gateway](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-chaining/services/agent-gateway)                                     | Google-managed policy enforcement point that intercepts both agent egress exchanges and forwards each to the service extension over gRPC. |
| [Agent Gateway Service Extension](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-chaining/services/agent-gateway-extension-service) | Service extension that sends requests to PingOne Authorize, exchanges tokens, and injects resulting tokens into requests.                 |
| [Order Status MCP Server](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-chaining/services/order-status-mcp-server)                 | Downstream resource that the agent chain invokes to check order status. It validates the final delegated token.                           |
| [PingOne](https://docs.pingidentity.com/pingone/use_cases/p1_oauth_2_token_exchange_delegation.html)                                                                                       | Identity provider (IdP) that issues the user token and every delegated token in the chain.                                                |
| [PingOne Authorize](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_introduction.html)                                                                    | External policy decision point that evaluates authorization requests.                                                                     |

### Token chain

The token flow begins when the user authenticates through the Chat UI. The Support Agent presents the user's token to PingOne as the subject of an RFC 8693 token exchange, alongside its own actor token (obtained using the Client Credentials grant). PingOne evaluates the user token's `may_act` claim against the acting client before issuing the delegated token, preserving the user as the subject.

The Agent Gateway Service Extension then exchanges the delegated token, generating the token that the Order Status Agent consumes. The Order Status Agent repeats this pattern for its outbound request to the MCP server. During each exchange, PingOne nests the acting client in the `act` claim, recording the full delegation history.

For simplicity, the individual actor tokens requested by the agents and the gateway aren't included here.

* User token: Chat UI's initial sign-on token

  ```json
  {
    "iss": "https://auth.pingone.<region>/<env>/as",
    "sub": "<alice-user-id>",
    "client_id": "<chat-ui-client-id>",
    "aud": "support-agent",
    "scope": "openid support-agent:invoke",
    "grant_type": "authorization_code",
    "may_act": { "sub": "<support-agent-client-id>" }
  }
  ```

  * `sub`: Represents the user.

  * `client_id`: Generated by the Chat UI.

  * `aud`: Scoped for use on the Support Agent resource.

  * `scope`: Grants the ability to invoke the Support Agent.

  * `may_act`: Licenses the Support Agent as the sole authorized next actor.

* Delegated token 1: Support agent's outbound A2A token

  ```json
  {
    "iss": "https://auth.pingone.<region>/<env>/as",
    "sub": "<alice-user-id>",
    "client_id": "<support-agent-client-id>",
    "aud": "google-agent-gateway",
    "scope": "order-status:invoke",
    "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
    "act": { "sub": "<support-agent-client-id>", "act": null },
    "may_act": { "sub": "<agent-gw-extension-client-id>" }
  }
  ```

  * `sub`: Represents the user (the agent acts on behalf of the user, not itself).

  * `client_id`: Generated by the Support Agent.

  * `aud`: Scoped for use on the intermediate Agent Gateway resource.

  * `scope`: Grants the ability to invoke the Order Status Agent.

  * `act`: Records the Support Agent as the first delegate (the original sign-on token had no actor, resulting in an explicit null).

  * `may_act`: Licenses the Agent Gateway Service Extension as the sole authorized next actor.

* Delegated token 2: Agent Gateway's inbound A2A token for the Order Status Agent

  ```json
  {
    "iss": "https://auth.pingone.<region>/<env>/as",
    "sub": "<alice-user-id>",
    "client_id": "<agent-gw-extension-client-id>",
    "aud": "order-status-agent",
    "scope": "order-status:invoke",
    "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
    "act": {
      "sub": "<agent-gw-extension-client-id>", "act": {
        "sub": "<support-agent-client-id>", "act": null
      }
    },
    "may_act": { "sub": "<order-status-agent-client-id>" }
  }
  ```

  * `sub`: Represents the user (identity is preserved end-to-end).

  * `client_id`: Generated by the Agent Gateway Service Extension.

  * `aud`: Scoped for use on the Order Status Agent.

  * `scope`: Grants the ability to invoke the Order Status Agent.

  * `act`: Records the service extension as the next delegate, on behalf of the Support Agent.

  * `may_act`: Licenses the Order Status Agent as the sole authorized next actor.

* Delegated token 3: Order Status Agent's outbound MCP token

  ```json
  {
    "iss": "https://auth.pingone.<region>/<env>/as",
    "sub": "<alice-user-id>",
    "client_id": "<order-status-agent-client-id>",
    "aud": "google-agent-gateway",
    "scope": "order:read",
    "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
    "act": {
      "sub": "<order-status-agent-client-id>", "act": {
        "sub": "<agent-gw-extension-client-id>", "act": {
          "sub": "<support-agent-client-id>", "act": null
        }
      }
    },
    "may_act": { "sub": "<agent-gw-extension-client-id>" }
  }
  ```

  * `sub`: Represents the user (identity is preserved end-to-end).

  * `client_id`: Generated by the Order Status Agent.

  * `aud`: Scoped for use on the intermediate Agent Gateway resource.

  * `scope`: Grants the ability to read orders from the downstream MCP server.

  * `act`: Records the Order Status Agent as the next delegate, on behalf of the previous delegation chain.

  * `may_act`: Licenses the Agent Gateway Service Extension as the sole authorized next actor.

* MCP tool token: Agent Gateway's final token for the MCP server

  ```json
  {
    "iss": "https://auth.pingone.<region>/<env>/as",
    "sub": "<alice-user-id>",
    "client_id": "<agent-gw-extension-client-id>",
    "aud": "order-status-mcp-server",
    "scope": "order:read",
    "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
    "act": {
      "sub": "<agent-gw-extension-client-id>", "act": {
        "sub": "<order-status-agent-client-id>", "act": {
          "sub": "<agent-gw-extension-client-id>", "act": {
            "sub": "<support-agent-client-id>", "act": null
          }
        }
      }
    }
  }
  ```

  * `sub`: Represents the user (identity is preserved end-to-end).

  * `client_id`: Generated by the Agent Gateway Service Extension.

  * `aud`: Scoped for use on the Order Status MCP Server.

  * `scope`: Grants the ability to read orders.

  * `act`: Contains the complete delegation chain (service extension, on behalf of Order Status Agent, on behalf of service extension, on behalf of Support Agent).

  * `may_act`: Because this is the final token, it doesn't include this claim. There are no further downstream token exchanges.

### Benefits of this approach

* Strictly scoped credentials

  Agents possess short-lived tokens that aren't broadly applicable. Through continuous RFC 8693 token exchanges, each stage of the delegation chain generates a new token scoped exclusively for its immediate destination. A token generated for one agent is invalid anywhere else in the chain, ensuring that least privilege compounds across every interaction.

* Dual-layer trust boundary

  A2A interaction requires both a Google credential, to satisfy Google Cloud identity and access management (IAM) at the Agent Runtime endpoint, and a PingOne delegated token to provide verifiable user identity and delegation context. This defense-in-depth approach ensures that compromising one trust layer doesn't grant access to the other.

* Continuous centralized authorization

  The Agent Gateway and service extension enforce authorization decisions at every stage of the chain (both A2A and MCP). Because policies are centralized in PingOne Authorize, you can update access rules dynamically without modifying or redeploying agents, the gateway, or the MCP server.

* End-to-end delegation record

  The final token delivered to the downstream tool contains a nested `act` claim that records every actor in the sequence. Because PingOne strictly enforces the `may_act` claim during each exchange, the downstream tool receives proof of who acted on behalf of the user, from the initial Chat UI sign-on to the final server invocation.

## Goals

* **Propagate user identity through a multi-agent chain**: Authenticate users at the Chat UI and configure PingOne to preserve the complete delegation history (using the `act` claim) across all A2A interactions.

* **Centralize policy enforcement for agent actions**: Deploy the Agent Gateway and service extension to consult PingOne Authorize for authorization decisions at runtime, restricting agent and tool invocations based on group membership and business hours.

* **Scope downstream access with token exchange**: Use RFC 8693 token exchanges at each stage of the delegation chain to translate inbound credentials into narrowly scoped tokens for the next authorized actor.

## What you'll do

1. [Deploy the Order Status MCP Server](#idai-gemini-a2a-mcp-server) to Google Cloud Run and register it in Google Agent Registry.

2. [Create authorization policies](#idai-gemini-a2a-policies) that limit agent invocations to business hours and to members of the support group.

3. [Deploy the Agent Gateway Service Extension](#idai-gemini-a2a-extension-service) to Cloud Run and configure it to request authorization decisions on every tool call.

4. [Deploy the Agent Gateway](#idai-gemini-a2a-agent-gateway) and attach the service extension to it.

5. [Deploy the Order Status Agent](#idai-gemini-a2a-order-status-agent) and create its PingOne resource.

6. [Deploy the Support Agent](#idai-gemini-a2a-support-agent) and create its PingOne resource.

7. [Deploy the Agent Bridge](#idai-gemini-a2a-agent-bridge) to Cloud Run and configure it to validate the user's token and pass it to the Support Agent.

8. [Deploy the Chat UI](#idai-gemini-a2a-chat-ui) and configure it to pass the user's token to the Support Agent through the Agent Bridge.

## Before you begin

Ensure you meet the prerequisites in the [Gemini Enterprise Agent Platform](idai-integrating-gemini-agent-platform-with-ping.html#idai-gemini-prereqs) integration overview.

## Tasks

You can find implementation files and code samples for this use case in the [Agent Chaining](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-chaining) GitHub repository.

### Deploy the Order Status MCP Server

The [Order Status MCP Server](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-chaining/services/order-status-mcp-server) exposes a `get_order_status` tool. This service holds the order data and is the final enforcement point for the agent chaining delegation model. To access the tool, the agent's request is routed through the Agent Gateway and the Agent Gateway Service Extension. This MCP server verifies the OAuth token injected by the gateway.

You'll deploy the supply chain MCP server to Cloud Run, register it in Agent Registry as an approved egress destination, and configure it with a matching resource in PingOne to ensure every token issued for tool access carries claims that prove delegation.

> **Collapse: Create the Order Status MCP Server resource in PingOne**
>
> Add a custom resource in PingOne that represents the Order Status MCP Server the agent is allowed to access.
>
> |   |                                                                                                                                                                            |
> | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [adding custom resources](https://docs.pingidentity.com/pingone/applications/p1_adding_custom_resource.html) in the PingOne documentation. |
>
> You'll configure the following custom attributes to govern how tokens are generated during both token exchanges and standard client credential requests:
>
> * `sub`: Determines the subject of the issued token based on the request type. During a token exchange, it copies the `sub` claim from the subject token to preserve the user's identity across the delegation chain. During a `client_credentials` request (used by the gateway extension to fetch its own actor token), it outputs the literal string `no-subject` because no user context exists.
>
> * `act`: Manages the token delegation chain. During a `client_credentials` request, it outputs the constant value `noActor`. During a token exchange, it verifies that the subject token's `may_act` claim matches the actor token's `client_id`. If they match, it nests the actor's identity in the subject token's existing `act` claim. If they don't match, the expression returns a null value. Because this is the only attribute where you must select the **Required** checkbox, a null return explicitly fails the unauthorized exchange.
>
> * `grant_type` (Optional): This attribute can enrich the final token by adding the authorization grant type (such as `urn:ietf:params:oauth:grant-type:token-exchange`) as a first-class claim.
>
> |   |                                                                                                                                                                                                      |
> | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | Because the Order Status MCP Server resource is terminal, a `may_act` attribute isn't necessary. The MCP server validates the token, then the chain ends without further downstream token exchanges. |
>
> 1. In the PingOne admin console, go to **Applications > Resources** and click the **[icon: plus, set=fa]**icon.
>
> 2. Define the resource:
>
>    1. **Resource Name**: `AC Order Status MCP Server`
>
>    2. **Audience**: `order-status-mcp-server`
>
> 3. Click **Next**.
>
> 4. Define attributes for the resource:
>
>    Detailed steps follow the table.
>
>    | Attribute    | Required | Expression                                                                                                                                                                                                                                                                                                |
>    | ------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>    | `sub`        | No       | ```spel
>    (#root.context.requestData.grantType == "client_credentials") ? "no-subject" : #root.context.requestData.subjectToken.sub
>    ```                                                                                                                                                                     |
>    | `act`        | Yes      | ```spel
>    (#root.context.requestData.grantType == "client_credentials")?"noActor":((#root.context.requestData.subjectToken.may_act.sub == #root.context.requestData.actorToken.client_id)?{"sub":#root.context.requestData.actorToken.client_id,"act":#root.context.requestData.subjectToken.act}:null)
>    ``` |
>    | `grant_type` | No       | ```spel
>    #root.context.requestData.grantType
>    ```                                                                                                                                                                                                                                                           |
>
>    1. Click the **Gear** icon ([icon: gear, set=fa]) next to the `sub` attribute, enter the expression, and click **Save**.
>
>       |   |                                                                                                                               |
>       | - | ----------------------------------------------------------------------------------------------------------------------------- |
>       |   | Leave the **Required** checkbox cleared for this attribute to prevent validation errors during `client_credentials` requests. |
>
>       Learn more about expressions in [Using the expression builder](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_use_expression_builder.html) in the PingOne documentation.
>
>    2. Click **+ Add** and name the attribute `act`.
>
>    3. Click [icon: gear, set=fa], enter the expression, and click **Save**.
>
>    4. Select the **Required** checkbox for the `act` attribute.
>
>       This ensures that any token exchange that fails to set `act` is rejected.
>
>    5. (Optional) Click **+ Add**, name the attribute `grant_type`, click [icon: gear, set=fa], enter the expression, and click **Save**.
>
> 5. Click **Next**, then click **+ Add Scope**.
>
> 6. Name the scope `order:read`.
>
> 7. Click **Save**.

> **Collapse: Create a support team group in PingOne**
>
> Create a group in PingOne to manage user access to the Support Order MCP Server.
>
> |   |                                                                                                                                                       |
> | - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [creating groups](https://docs.pingidentity.com/pingone/directory/p1_create_group.html) in the PingOne documentation. |
>
> 1. In the PingOne admin console, go to **Directory > Groups**.
>
> 2. Click the **[icon: plus, set=fa]**icon.
>
> 3. Name the group `support_team` and click **Save**.
>
> 4. Add any PingOne users authorized to invoke the Support Order MCP Server:
>
>    1. On the **Users** tab, click **Add Individually**.
>
>    2. In the **All Users** list, select checkboxes for the users you want to add.
>
> 5. Click **Save**.

> **Collapse: Deploy the Order Status MCP Server to Cloud Run**
>
> Build the MCP server with configured environment variables and deploy it as a Google Cloud Run service.
>
> 1. Set environment variables for the MCP server:
>
>    1. In the cloned Gemini Enterprise Agent Platform Integrations repository, go to the `pingone/agent-chaining/services/order-status-mcp-server` directory.
>
>    2. Make a copy of the `.env.sample` file and name it `.env`:
>
>       ```bash
>       cp .env.sample .env
>       ```
>
>    3. Set environment variables in the `.env` file:
>
>       | Variable                    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
>       | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       | `GC_REGION`                 | Your Google Cloud Platform region. For example: `us-central1`.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
>       | `GC_CLOUD_RUN_SERVICE_NAME` | The Cloud Run service name: `ac-order-status-mcp-server`.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
>       | `IDP_ISSUER`                | The PingOne issuer URL: `https://auth.pingone.<region>/<env-id>/as`.Set the placeholders:- \<region>: The country code top-level domain (ccTLD), such as `.com`, `.eu`, `.asia`. You can find this in your PingOne admin console URL. For example, `https://console.pingone.com/index.html?env=12345678-1234-1234-1234-123456789012` has a ccTLD of `.com`.
>
>       - \<env-id>: The PingOne environment ID. In the example PingOne admin console URL, the ID is `12345678-1234-1234-1234-123456789012`. |
>       | `IDP_REQUIRED_AUDIENCE`     | The expected `aud` claim. Enter the audience you gave the Order Status MCP Server resource in PingOne: `order-status-mcp-server`.                                                                                                                                                                                                                                                                                                                                                                 |
>       | `IDP_REQUIRED_SCOPE`        | The scope the inbound token must carry. Enter the scope you gave the AC Order Status MCP Server resource in PingOne: `order:read`.                                                                                                                                                                                                                                                                                                                                                                |
>
> 2. In the `pingone/agent-chaining/services/order-status-mcp-server` directory, run the following command:
>
>    ```bash
>    make deploy
>    ```
>
>    This builds the Docker image, pushes it to Google Container Registry, and deploys it to Cloud Run.

> **Collapse: Register the Order Status MCP Server in Agent Registry**
>
> Register the MCP server in Agent Registry to ensure the Agent Gateway recognizes it as an approved egress destination.
>
> |   |                                                                                                                                                                                                                               |
> | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | No additional IAM configuration is required after registration. The registry-wide `roles/iap.egressor` binding, which is applied automatically by each agent's `deploy.py` script, provides all necessary egress enforcement. |
>
> 1. In Google Cloud, go to **Agent Platform > Govern > Agent Registry** and click **Add MCP Server**.
>
> 2. Enter the following values:
>
>    * **Name**: `ac-order-status-mcp-server`
>
>    * **Description**: `Order status MCP server for the Agent Chaining demo`
>
> 3. Select your **Region** (for example, `us-central1`).
>
> 4. Enter the MCP server URL:
>
>    1. To find the URL, duplicate the browser tab and go to **Cloud Run > Services**. Click the **order-status-mcp-server**.
>
>    2. Copy the URL at the top of the page. For example: `https://agent-chain-order-status-mcp-server-909399354423.us-central1.run.app`.
>
>    3. In Agent Registry, paste the URL in the **MCP server URL** field, and then add `/mcp` to the end of the URL.
>
>       |   |                                                                                                                                                                                                                                                                                                                                 |
>       | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       |   | The registered URL must match the host URL the agent calls exactly (defined by the `MCP_ORDER_STATUS_SERVER_URL` variable in the agent's `.env` file). Identity-Aware Proxy (IAP) resolves egress destinations by host. If the host doesn't match, IAP denies the request before it ever reaches the gateway service extension. |
>
> 5. Enter the MCP specification JSON, which defines the MCP server's endpoints and expected request and response formats:
>
>    1. In the cloned repository, go to the `pingone/agent-chaining/services/order-status-mcp-server` directory and copy the contents of the `tool-spec.json` file.
>
>    2. In Agent Registry, paste the copied contents into the **JSON** field.
>
>    3. Click **Next**.
>
> 6. Click **Save** to complete the registration.

### Create authorization policies in PingOne Authorize

Create policies that decide whether the service extension permits the agent's request to the MCP server. These policies limit access to members of the support group during business hours.

> **Collapse: Create attributes in the Trust Framework**
>
> Create attributes in PingOne Authorize that extract information from service extension decision requests. These attributes are used in authorization policies to determine whether the agent is allowed to access the MCP server.
>
> |   |                                                                                                                                                                                                                     |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [adding authorization attributes](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1_az_adding_attributes.html) in the PingOne Authorize documentation. |
>
> | Name           | Type       | Extension parameter key |
> | -------------- | ---------- | ----------------------- |
> | `User Sub`     | **String** | `User Sub`              |
> | `Request Hour` | **Number** | `Request Hour`          |
>
> 1. In the PingOne admin console, go to **Authorization > Trust Framework**.
>
> 2. On the **Attributes** tab, click the **[icon: plus, set=fa]**icon.
>
> 3. Name the attribute `User Sub`.
>
>    The attribute name must match the parameter key in the decision request. It's case-sensitive.
>
> 4. If the attribute has a **Parent**, click [icon: trash, set=fa]to clear the parent value, ensuring the attribute isn't nested under another attribute.
>
> 5. In the **Resolvers** section, click **[icon: plus, set=fa]Add Resolver** and keep the default **Request Parameter** resolver.
>
> 6. (Optional) Name the resolver `user_sub` to match the parameter name in the agent's request.
>
>    Request Parameter resolvers extract values from decision requests and pass them to PingOne Authorize for evaluation. The resolver name is a label only and isn't matched to the parameter name in the request.
>
> 7. For the Value Settings **Type**, keep the default value of **String**.
>
> 8. Click **Save Changes**.
>
> 9. If you don't already have the `Request Hour` attribute, repeat the steps above to add it, with a resolver parameter optionally named `request_hour` and the value settings type **Number**.

> **Collapse: Create the AC Agent Gateway Policies policy set**
>
> Create a policy set in PingOne Authorize that contains the policies governing the agent's access to the MCP server.
>
> |   |                                                                                                                                                                                                                 |
> | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [adding policy sets](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_policy_or_policy_set.html) in the PingOne Authorize documentation. |
>
> 1. In the PingOne admin console, go to **Authorization > Policies**.
>
> 2. Click the root **Policies** policy set, then click the **[icon: plus, set=fa]**icon and select **Add Policy Set**.
>
> 3. Name the policy set `AC Agent Gateway Policies`.
>
> 4. For the **Combining Algorithm**, select **Unless one decision is deny, the decision will be permit**.
>
> 5. Click **Save changes**.

> **Collapse: Create the Only Permit During Business Hours policy**
>
> Create a policy that permits access to the MCP server only during business hours. PingOne Authorize denies access if the request hour is before 8:00 AM or after 6:00 PM.
>
> The service extension converts from UTC before sending a decision request to ensure permitted hours are in local time. For example, a request at 3:00 PM UTC is converted to 8:00 AM Pacific and is permitted, while a request at 3:00 AM UTC is converted to 8:00 PM Pacific and is denied.
>
> |   |                                                                                                                                                                                                              |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> |   | You can find more details about [adding policies](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_policy_or_policy_set.html) in the PingOne Authorize documentation. |
>
> 1. In **Authorization > Policies**, select the **AC Agent Gateway Policies** policy set.
>
> 2. Click the **[icon: plus, set=fa]**icon and select **Add Policy**.
>
> 3. Name the policy `Only Permit Within Business Hours`.
>
> 4. In **Applies When**:
>
>    1. Click **+ Comparison**, then select **Any**.
>
>    2. Select the **Request Hour** attribute.
>
>    3. Select the **Greater Than** operator.
>
>    4. For the value, enter `18`.
>
>    5. Click **+ Comparison** and select the **Request Hour** attribute.
>
>    6. Select the **Less Than** operator.
>
>    7. For the value, enter `8`.
>
> 5. For the **Combining Algorithm**, select **Unless one decision is deny, the decision will be permit**.
>
> 6. Click **+ Add Rule**, name the rule `Deny Outside Business Hours`, then for **Effect**, select **Deny**.
>
> 7. Click **Save changes**.

> **Collapse: Create the Only Permit Users in Support Group policy**
>
> Create a policy that permits only members of the support group to access the MCP server. Agents are denied access when `user_sub` isn't a member of the support team.
>
> |   |                                                                                                                                                                                                              |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> |   | You can find more details about [adding policies](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_policy_or_policy_set.html) in the PingOne Authorize documentation. |
>
> 1. In **Authorization > Policies**, select the **AC Agent Gateway Policies** policy set.
>
> 2. Click the **[icon: plus, set=fa]**icon and select **Add Policy**.
>
> 3. Name the policy `Only Permit Users in Support Group`.
>
> 4. In **Applies When**:
>
>    1. Click **+ Comparison** and select the **User Sub** attribute.
>
>    2. Select the **Is Not Member Of** operator.
>
>    3. For the value, select the **support_team** attribute.
>
> 5. For the **Combining Algorithm**, select **Unless one decision is deny, the decision will be permit**.
>
> 6. Click **+ Add Rule**, name the rule `Deny Non-Members`, then for **Effect**, select **Deny**.
>
> 7. Click **Save changes**.

> **Collapse: Publish an authorization policy version**
>
> Publish a policy version to deploy your policies to a decision endpoint and make them available in decision evaluations.
>
> |   |                                                                                                                                                                                                                 |
> | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [publishing policy versions](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_publishing_versions.html) in the PingOne Authorize documentation. |
>
> 1. In the PingOne admin console, go to **Authorization > Version History**.
>
> 2. Click the **More Options (⋮)** icon next to the **Latest Version** and select **Publish Version**.
>
> 3. In the **Publish to** list, select a decision endpoint.
>
> 4. For the version **Name**, enter `AC`.
>
> 5. Click **Publish**.
>
>    The version name and the endpoint the version is published to are displayed in **Version History**.
>
> 6. []()Go to **Authorization > Decision Endpoints** and expand the decision endpoint where you published the policy version. Copy the decision endpoint URL and save it somewhere convenient. You'll need it later when you [deploy the service extension](#idai-gemini-a2a-authz-dec-endpoint).

### Deploy the Agent Gateway Service Extension

The [Agent Gateway Service Extension](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-chaining/services/agent-gateway-extension-service) is an Envoy `ext_proc` gRPC handler that the Agent Gateway calls to request authorization decisions and perform token exchanges.

The service extension governs two interaction paths:

* **A2A:** The Support Agent calls the Order Status Agent.

* **Agent to tool (MCP):** The Order Status Agent calls the Order Status MCP Server.

For requests matching either target, the service extension performs the following operations:

* Validates the agent's delegated token, specifically checking the `iss`, `aud`, and `scope` claims.

* Calls PingOne Authorize on A2A `message:send` or MCP `tools/call` requests to evaluate the user's identity and the time of the request.

* Upon a deny decision, error, or unknown request body, blocks the request and returns a `403 Forbidden` error.

* Upon a permit decision, performs a token exchange to generate a token scoped to the target audience. The injection method depends on the destination:

  * For A2A requests, injects the new token into the body metadata. The `Authorization` header is reserved for the Google credential required to pass the receiving endpoint's IAM check.

  * For MCP requests, injects the new token into the `Authorization: Bearer` header.

> **Collapse: Create a PingOne worker application**
>
> Create a PingOne worker application that the service extension uses to call PingOne Authorize for authorization decisions.
>
> |   |                                                                                                                                                                               |
> | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [adding applications](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html) in the PingOne documentation. |
>
> 1. In the PingOne admin console, go to **Applications > Applications**.
>
> 2. Click the **[icon: plus, set=fa]**icon and create the application profile:
>
>    1. Name the application `AC PingOne Authorize Worker App`.
>
>    2. For the **Application Type**, click **Worker**.
>
>    3. Click **Save**.
>
> 3. To enable the application, click the toggle next to the application name in the details panel.
>
> 4. On the **Configuration** tab, click the Pencil icon ([icon: pencil, set=fa]), make sure **Client Credentials** is the **Grant Type**, then click **Cancel**.
>
> 5. On the **Roles** tab, click **Grant Roles**.
>
> 6. Expand the **Environment Admin** role and select your environment.
>
> 7. Expand the **Identity Data Read Only** role and select your environment.
>
> 8. Click **Save**.

> **Collapse: Create a PingOne application for token exchange**
>
> Create a PingOne OIDC application that the service extension uses to perform token exchanges for the MCP server.
>
> |   |                                                                                                                                                                               |
> | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [adding applications](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html) in the PingOne documentation. |
>
> 1. In the PingOne admin console, go to **Applications > Applications**.
>
> 2. Click the **[icon: plus, set=fa]**icon and create the application profile:
>
>    1. Name the application `AC Agent Gateway Extension`.
>
>    2. For the **Application Type**, click **OIDC Web App**.
>
>    3. Click **Save**.
>
> 3. To enable the application, click the toggle next to the application name in the details panel.
>
> 4. On the **Configuration** tab, click [icon: pencil, set=fa]:
>
>    1. For **Grant Type**, select **Client Credentials** and **Token Exchange**.
>
>    2. Clear the **Code** and **Authorization Code** checkboxes.
>
>    3. Click **Save**
>
> 5. On the **Resources** tab, click [icon: pencil, set=fa], then select the **order:read** scope on the AC Order Status MCP Server.
>
> 6. []()Select the **order_status:invoke** scope on the AC Order Status Agent.
>
>    This scope isn't available yet. Skip this step for now and complete it after you [deploy the Order Status Agent](#idai-gemini-a2a-order-status-deployed-scope).
>
> 7. Click **Save**.
>
> 8. []()On the **Overview** tab, copy the **Client ID** for this application and save it somewhere convenient. You'll need it later when you [configure attributes](#idai-gemini-a2a-gateway-attr) for the Agent Gateway resource in PingOne.

> **Collapse: Deploy the Agent Gateway Service Extension to Cloud Run**
>
> Build the service extension with configured environment variables and deploy it as a Google Cloud Run service.
>
> 1. Set environment variables for the service extension:
>
>    1. In the cloned repository, go to the `pingone/agent-chaining/services/agent-gateway-extension-service` directory.
>
>    2. Make a copy of the `.env.sample` file and name it `.env`:
>
>       ```bash
>       cp .env.sample .env
>       ```
>
>    3. Set environment variables in the `.env` file:
>
>       | Variable                      | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
>       | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       | `GC_REGION`                   | Your Google Cloud Platform region. For example: `us-central1`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
>       | `GC_CLOUD_RUN_SERVICE_NAME`   | The Cloud Run service name: `ac-agent-gateway-extension-service`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
>       | `GC_SERVICE_EXTENSION_NAME`   | The deployed service extension's name (created when the service extension was registered): `ac-agent-gateway-extension`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
>       | `IDP_ISSUER`                  | The PingOne issuer URL: `https://auth.pingone.<region>/<env-id>/as`.To find this endpoint, go to the AC Agent Gateway Extension application in PingOne. Copy the **Issuer ID** under **Connection Details** on the **Overview** tab.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
>       | `EXCHANGE_CLIENT_ID`          | The AC Agent Gateway Extension application's **Client ID**. This is located above **Connection Details** on the **Overview** tab.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
>       | `EXCHANGE_CLIENT_SECRET`      | The AC Agent Gateway Extension application's **Client Secret**. This is located above **Connection Details** on the **Overview** tab.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
>       | `AUTHZ_CLIENT_ID`             | The AC PingOne Authorize Worker App's **Client ID**. This is located above **Connection Details** on the **Overview** tab for this application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
>       | `AUTHZ_CLIENT_SECRET`         | The AC PingOne Authorize Worker App's **Client Secret**. This is located above **Connection Details** on the **Overview** tab.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
>       | []()`AUTHZ_DECISION_ENDPOINT` | The PingOne Authorize decision endpoint URL where you [published the policy version](#idai-gemini-a2a-decision-endpoint) earlier.To find the URL, go to **Authorization > Decision Endpoints** and expand the decision endpoint where you published the policy version. Copy the decision endpoint URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
>       | `IDP_REQUIRED_AUDIENCE`       | The intermediate audience targeted by the initial token exchanges for both the Support Agent and the Order Status Agent. This is `ac-google-cloud-agent-gateway`.No downstream service validates this audience directly. Instead, the gateway uses this intermediate audience as the source to generate the final token for the target destination (defined by either `AGENT_AUDIENCE` or `TOOL_AUDIENCE`). This ensures the final PingOne resources remain terminal, requiring only `sub` and `act` attributes rather than processing multiple chained exchanges.                                                                                                                                                                                                                                              |
>       | `IDP_REQUIRED_SCOPE_AGENT`    | The scope the inbound token must carry to invoke the Order Status Agent. This is `order_status:invoke`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
>       | `IDP_REQUIRED_SCOPE_TOOL`     | The scope the inbound token must carry to invoke the Order Status MCP Server. This is `order:read`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
>       | []()`AGENT_ENGINE_ID`         | The Reasoning Engine's identifier for the Order Status Agent. In this example, the ID follows `reasoningEngines:` in the Order Status Agent's Uniform Resource Name (URN): `urn:agent:projects-909399354423:projects:909399354423:locations:us-central1:aiplatform:reasoningEngines:7390548000881246208`.You'll populate this placeholder after you [deploy the Order Status Agent](#idai-gemini-a2a-order-status-deployed-engine-id) in a later task. To find the ID at that point, go to the `ac-order-status-agent` service in **Agent Registry**. After you populate this variable, redeploy the service extension.&#xA;&#xA;The Reasoning Engine ID changes each time you redeploy the Order Status Agent. If you redeploy the agent, update this environment variable and redeploy the service extension. |
>       | `AGENT_SCOPE`                 | The scope the service extension requests during token exchange to authorize access to the downstream Order Status Agent: `order-status:invoke`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
>       | `AGENT_AUDIENCE`              | The final target audience generated during the A2A request token exchange. This is the audience you'll give the agent resource in PingOne: `order-status-agent`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
>       | `TOOL_URL`                    | The Order Status MCP Server's Cloud Run base URL: `https://ac-order-status-mcp-server-<your-project-number>.<your-deployment-region>.run.app`.To find this URL, go to **Cloud Run > Services** and click the **order-status-mcp-server** service. Copy the URL at the top of the page (for example, `https://ac-order-status-mcp-server-f447x3emfq-uc.a.run.app`).                                                                                                                                                                                                                                                                                                                                                                                                                                              |
>       | `TOOL_SCOPE`                  | The scope the service extension requests during token exchange to authorize access to the downstream MCP server: `order:read`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
>       | `TOOL_AUDIENCE`               | The final target audience generated during the MCP request token exchange. This is the audience you gave the AC Order Status MCP Server resource in PingOne: `order-status-mcp-server`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
>
> 2. In the `pingone/agent-chaining/services/agent-gateway-extension-service` directory, run the following commands:
>
>    ```bash
>    make deploy
>    ```
>
>    This builds the Docker image, pushes it to Google Container Registry, and deploys it to Cloud Run.
>
>    ```bash
>    make register
>    ```
>
>    This command registers your deployed Cloud Run service as an available service extension in Google Cloud. Behind the scenes, it renders the `service-extension.tmpl.yaml` template with the live Cloud Run URL and imports the configuration, preparing the extension for use by the Agent Gateway.

### Create the Agent Gateway

The [Agent Gateway](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-chaining/services/agent-gateway) is a Google-managed resource that acts as the policy enforcement point for all agent egress traffic. It intercepts all outbound traffic bound for downstream tools and routes it to the service extension.

Because the Support Agent and the Order Status Agent operate concurrently, this gateway is configured to govern both the A2A interaction path (between the agents) and the MCP interaction path (to the downstream server).

You'll configure the gateway to call the service extension, using [Envoy external processing](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_proc_filter) (`ext_proc`), on every request to the Order Status MCP Server. This includes attaching the service extension to the gateway, registering the egress destinations it can reach, and creating the PingOne resource that licenses the service extension as the only actor allowed to exchange tokens bound for the gateway.

> **Collapse: Configure Agent Gateway environment variables**
>
> Configure the environment variables required to deploy the Agent Gateway and link it to the service extension.
>
> 1. Set environment variables for the Agent Gateway:
>
>    1. In the cloned repository, go to the `pingone/agent-chaining/services/agent-gateway` directory.
>
>    2. Make a copy of the `.env.sample` file and name it `.env`:
>
>       ```bash
>       cp .env.sample .env
>       ```
>
>    3. Check the environment variables in the `.env` file. Most are already defined.
>
>       | Variable                    | Value                                                                                                                    |
>       | --------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
>       | `GC_REGION`                 | Your Google Cloud Platform region. For example: `us-central1`.                                                           |
>       | `GC_GATEWAY_NAME`           | The Agent Gateway's name: `ac-agent-gateway`.                                                                            |
>       | `GC_SERVICE_EXTENSION_NAME` | The deployed service extension's name (created when the service extension was registered): `ac-agent-gateway-extension`. |
>       | `GC_AUTHZ_POLICY_NAME`      | The name of the Google Cloud authorization policy resource that binds the extension to the gateway: `ac-authz-policy`.   |

> **Collapse: Create the Agent Gateway in Google Cloud**
>
> Use the Google Cloud Console to deploy the Agent Gateway. This creates the service that intercepts agent egress and hands requests to the service extension.
>
> 1. In Google Cloud, go to **Agent Platform > Govern > Gateways** and click **Add gateway**.
>
> 2. Enter the following values:
>
>    * **Name**: `ac-agent-gateway`.
>
>    * **Region**: Your Google Cloud Platform region. For example: `us-central1`.
>
>    * **Deployment mode**: Keep the default **Google-managed**.
>
>    * **Agent registries**: Keep the default **Regional registry**.
>
>    * **Governed Access Path**: Keep the default **Agent-to-Anywhere (egress)**.
>
>    * **Access Authorization**: Select **Enforce policies**.
>
>    * **Policy Model**: Select **Allow Policy**.
>
> 3. Click **Add gateway**.

> **Collapse: Attach the Agent Gateway Service Extension to the Agent Gateway**
>
> To enforce your access policies, you must connect the service extension to the Agent Gateway. The `make attach` command populates `authz-policy.tmpl.yaml` with your project, region, and gateway name, and then imports it with `gcloud`. This creates an authorization policy that binds the extension to the gateway as a `CONTENT_AUTHZ` policy scoped to both the Reasoning Engine A2A path (`/v1beta1/projects/…/reasoningEngines/`) and the `/mcp` path.
>
> 1. In the `pingone/baseline-autonomous-agent-to-tool/services/agent-gateway` directory, run the following command:
>
>    ```bash
>    make attach
>    ```
>
>    |   |                                                                                  |
>    | - | -------------------------------------------------------------------------------- |
>    |   | You can run `make render` alone to inspect the generated YAML without importing. |
>
> There are now two complementary authorization extensions attached to the Agent Gateway:
>
> | Extension                             | Service role    | Target                      | Description                                                                                                                                                                                                                                                          |
> | ------------------------------------- | --------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `ac-agent-gateway-iap-authzextension` | `REQUEST_AUTHZ` | `iap.googleapis.com`        | A Google-managed extension automatically created with the gateway. It enforces the IAP identity and egress check (`iap.egressor`), which appears on the gateway as the **Auth provider: Google Cloud Identity-Aware Proxy**.                                         |
> | `ac-agent-gateway-extension`          | `CONTENT_AUTHZ` | Cloud Run service extension | The extension created in the previous step. It routes traffic to your Cloud Run host and requests an authorization decision. Upon permit, the extension performs the PingOne token exchange and injects the resulting delegated token in the `Authorization` header. |

> **Collapse: Register egress destinations for the Agent Gateway**
>
> Because the Agent Gateway governs all agent egress, every host the agent communicates with must be registered as a destination in Agent Registry. Your environment currently includes the following registered destinations:
>
> * **Order Status MCP Server:** This was registered as an MCP server (rather than a standard endpoint) when you deployed it.
>
>   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
>   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | The registered URL must match the host URL invoked by the agent exactly. Because IAP resolves egress destinations by host name, any mismatch causes IAP to block the request before it ever reaches the service extension. For example, a failure occurs if the registry holds the stable Cloud Run URL (`…​-<project-number>.<region>.run.app`), but the agent calls a direct revision URL (`…​-<hash>-<region>.a.run.app`). If this happens, you'll see a `DENIED` entry in the gateway logs with no `agentRegistryResource`. |
>
> * **Google APIs:** Endpoints for `aiplatform`, `iamcredentials`, and telemetry (`*.mtls.googleapis.com`) were automatically generated during the gateway deployment to support the runtime's internal egress. Don't modify these endpoints.
>
> You'll register the PingOne host as the final required egress endpoint.
>
> |   |                                                                                                                                                                                                                                                                                                                  |
> | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | If you completed the [authorizing autonomous agents](idai-authorizing-gemini-autonomous-agents-with-ping.html) and [authorizing agents on behalf of users](idai-authorizing-gemini-on-behalf-of-users-with-ping.html) use cases, you already registered the PingOne host as an endpoint. You can skip this task. |
>
> 1. In Google Cloud, go to **Agent Platform > Govern > Agent Registry** and click **Add Endpoint**.
>
> 2. Enter the following values:
>
>    * **Name**: `PingOne`.
>
>    * **Region**: Your Google Cloud Platform region. For example: `us-central1`.
>
>    * **Destination URL**: Your PingOne host. For example: `https://auth.pingone.com`.
>
> 3. Click **Save**.

> **Collapse: Create the Agent Gateway resource in PingOne**
>
> The Agent Gateway resource acts as an intermediate target for both agents' initial token exchanges. The gateway service extension uses the output of these initial exchanges to perform subsequent exchanges targeting the next actor.
>
> Custom attributes secure this delegation chain. While a basic token exchange can function without them, omitting these attributes means an actor token could be accepted at face value. By defining them, PingOne explicitly attests to the actor's identity and refuses to generate a token if the subject token didn't authorize the exchanging actor.
>
> You'll configure the following attributes:
>
> * `sub`: Determines the subject of the token based on the grant type. During a token exchange, it copies the subject token's `sub` claim to carry the user's identity through the transaction. During a `client_credentials` request (used when the agents fetch their own actor tokens), it outputs the string `no-subject`.
>
> * `act`: Preserves the complete delegation history. During an exchange, it verifies that the incoming token's `may_act` claim matches the exchanging agent's `client_id`. If authorized, it nests the incoming token's `act` claim inside the new one, ensuring the entire chain survives the transaction rather than just the previous actor.
>
> * `may_act`: Explicitly licenses the gateway service extension as the sole authorized next actor on every token minted for this resource. For both token exchanges, the extension is the only client whose client ID matches, ensuring the downstream resource's required act check passes for it and fails closed for anyone else.
>
> * `grant_type` (Optional): Enriches the token by exposing the authorization grant type (such as `urn:ietf:params:oauth:grant-type:token-exchange`) as a first-class claim.
>
> |   |                                                                                                                                                                            |
> | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [adding custom resources](https://docs.pingidentity.com/pingone/applications/p1_adding_custom_resource.html) in the PingOne documentation. |
>
> 1. In the PingOne admin console, go to **Applications > Resources** and click the **[icon: plus, set=fa]**icon.
>
> 2. Define the resource:
>
>    1. **Resource Name**: `AC Google Cloud Agent Gateway`
>
>    2. **Audience**: `ac-google-cloud-agent-gateway`
>
> 3. Click **Next**.
>
> 4. Define attributes for the resource:
>
>    Detailed steps follow the table.
>
>    | Attribute    | Required | Expression                                                                                                                                                                                                                                                                                                |
>    | ------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>    | `sub`        | No       | ```spel
>    (#root.context.requestData.grantType == "client_credentials") ? "no-subject" : #root.context.requestData.subjectToken.sub
>    ```                                                                                                                                                                     |
>    | `act`        | Yes      | ```spel
>    (#root.context.requestData.grantType == "client_credentials")?"noActor":((#root.context.requestData.subjectToken.may_act.sub == #root.context.requestData.actorToken.client_id)?{"sub":#root.context.requestData.actorToken.client_id,"act":#root.context.requestData.subjectToken.act}:null)
>    ``` |
>    | `may_act`    | No       | ```spel
>    {"sub":"<extension-client-id>"}
>    ```                                                                                                                                                                                                                                                               |
>    | `grant_type` | No       | ```spel
>    #root.context.requestData.grantType
>    ```                                                                                                                                                                                                                                                           |
>
>    1. Click the **Gear** icon ([icon: gear, set=fa]) next to the `sub` attribute, enter the expression, and click **Save**.
>
>       |   |                                                                                                                                                                           |
>       | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       |   | Leave the **Required** checkbox cleared. If marked required, standard `client_credentials` requests are rejected by PingOne before the attribute expression is evaluated. |
>
>       Learn more about expressions in [Using the expression builder](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_use_expression_builder.html) in the PingOne documentation.
>
>    2. Click **+ Add** and name the attribute `act`.
>
>    3. Click [icon: gear, set=fa], enter the expression, and click **Save**.
>
>    4. Select the **Required** checkbox for the `act` attribute.
>
>       This ensures that any token exchange that fails to set `act` is rejected. Unauthorized requests evaluate to null and explicitly fail.
>
>    5. Click **+ Add** and name the attribute `may_act`.
>
>    6. []()Click [icon: gear, set=fa], enter the expression, replace the `<extension-client-id>` placeholder with the AC Agent Gateway Extension application's **Client ID** you saved [earlier](#idai-gemini-a2a-ext-client-id), and click **Save**.
>
>    7. (Optional) Click **+ Add**, name the attribute `grant_type`, click [icon: gear, set=fa], enter the expression, and click **Save**.
>
> 5. Click **Next**, then click **+ Add Scope**.
>
> 6. Name the scope `order-status:invoke`.
>
>    The Support Agent requests this scope when it exchanges the user's sign-on token during the first exchange.
>
> 7. Click **+ Add Scope** and name it `order:read`.
>
>    The Order Status Agent requests this scope when it exchanges the Support Agent's delegated token during the third exchange.
>
> 8. Click **Save**.

### Deploy the Order Status Agent

The [Order Status Agent](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-chaining/services/order-status-agent) acts as the specialized downstream agent in the agent delegation chain. In the A2A path, it receives `get_order_status` requests from the Support Agent and serves as the only client authorized to call the Order Status MCP Server.

When the gateway extension routes an A2A message to this agent, it delivers a delegated token with the `metadata.delegatedAuthorization` property. The agent independently validates this token, verifying its signature, issuer, the `order-status-agent` audience, and the `order-status:invoke` scope. The agent then executes its own token exchange (using the validated token as the subject and its own PingOne client credentials as the actor), targeting the shared intermediate `ac-google-cloud-agent-gateway` audience.

As the agent initiates the outbound call to the MCP server, the Agent Runtime routes the egress traffic through the Agent Gateway. The service extension intercepts this request and performs the final token exchange, generating a token scoped to the `order-status-mcp-server` audience.

You'll create an identity for the agent in PingOne and deploy the agent to the Agent Runtime, binding it to the Agent Gateway.

> **Collapse: Create the Order Status Agent in PingOne**
>
> Create an AI agent in PingOne to establish a dedicated identity for the Order Status Agent. This identity enables the agent to authenticate and acquire access tokens during delegation exchanges.
>
> |   |                                                                                                                                                              |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> |   | You can find more details about [adding AI agents](https://docs.pingidentity.com/pingone/ai_agents/p1_managing_ai_agents.html) in the PingOne documentation. |
>
> 1. In the PingOne admin console, go to **AI Agents** and click the **[icon: plus, set=fa]**icon.
>
> 2. Name the agent `AC Order Status Agent`.
>
> 3. Click **Save**.
>
> 4. To enable the agent, click the toggle next to the agent name in the details panel.
>
> 5. On the **Configuration** tab, click [icon: pencil, set=fa]:
>
>    1. In **Grant Type**, select **Client Credentials** and **Token Exchange**.
>
>    2. Clear the **Code** and **Authorization Code** checkboxes.
>
>    3. Click **Save**
>
> 6. On the **Resources** tab, click [icon: pencil, set=fa], then select the **order:read** scope on the AC Google Cloud Agent Gateway resource.
>
> 7. Click **Save**.
>
> 8. []()On the **Overview** tab, copy the **Client ID** for this agent and save it somewhere convenient. You'll need it later when you [configure attributes](#idai-gemini-a2a-osa-attr) for the Order Status Agent resource in PingOne.

> **Collapse: Create the Order Status Agent resource in PingOne**
>
> The Order Status Agent resource acts as the primary destination target for the A2A invocation. Only the gateway service extension generates tokens against this resource, using either an RFC 8693 token exchange (for the A2A request) or a `client_credentials` grant (to fetch its own actor token for the A2A scope). Because no tokens are generated here with a direct user sign-on (`authorization_code` grant), you must configure the following custom attributes to securely manage the delegation chain:
>
> * `sub`: Determines the subject of the token based on the grant type. During a token exchange, it copies the incoming token's `sub` claim to carry the user's identity through the A2A interaction. During a `client_credentials` request, it outputs the string `no-subject`.
>
>   |   |                                                                                                                                                                                                                                                                                                                                       |
>   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | Configure this expression using only the `subjectToken.sub` and `no-subject` branches. Do not include a `#root.user.id` branch. Because no user context exists during a `client_credentials` grant, referencing the user object causes the entire expression evaluation to fail, which drops the `sub` claim from the token entirely. |
>
> * `act`: Preserves the delegation history across the A2A interaction. During an exchange, it verifies that the incoming token's `may_act` claim identifies the exchanging service extension. If authorized, it nests the subject token's `act` claim one level deeper in the new token. If the original sign-on token lacked an `act` claim, it flows through the nesting as an explicit null at the innermost position.
>
> * `may_act`: Licenses the Order Status Agent as the sole authorized next actor on every token minted for this resource. By assigning a constant value containing this agent's PingOne client ID, this attribute ensures the agent's subsequent token exchange (which targets the shared gateway audience), carries a valid `act` claim and passes the gateway resource's delegation check, failing closed for anyone else.
>
> * `grant_type` (Optional): Enriches the token by exposing the authorization grant type (such as `urn:ietf:params:oauth:grant-type:token-exchange`) as a first-class claim.
>
> |   |                                                                                                                                                                            |
> | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [adding custom resources](https://docs.pingidentity.com/pingone/applications/p1_adding_custom_resource.html) in the PingOne documentation. |
>
> 1. In the PingOne admin console, go to **Applications > Resources** and click the **[icon: plus, set=fa]**icon.
>
> 2. Define the resource:
>
>    1. **Resource Name**: `AC Order Status Agent`
>
>    2. **Audience**: `order-status-agent`
>
> 3. Click **Next**.
>
> 4. Define attributes for the resource:
>
>    Detailed steps follow the table.
>
>    | Attribute    | Required | Expression                                                                                                                                                                                                                                                                                                |
>    | ------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>    | `sub`        | No       | ```spel
>    (#root.context.requestData.grantType == "client_credentials") ? "no-subject" : #root.context.requestData.subjectToken.sub
>    ```                                                                                                                                                                     |
>    | `act`        | Yes      | ```spel
>    (#root.context.requestData.grantType == "client_credentials")?"noActor":((#root.context.requestData.subjectToken.may_act.sub == #root.context.requestData.actorToken.client_id)?{"sub":#root.context.requestData.actorToken.client_id,"act":#root.context.requestData.subjectToken.act}:null)
>    ``` |
>    | `may_act`    | No       | ```spel
>    {"sub":"<ORDER-STATUS-AGENT-CLIENT-ID>"}
>    ```                                                                                                                                                                                                                                                      |
>    | `grant_type` | No       | ```spel
>    #root.context.requestData.grantType
>    ```                                                                                                                                                                                                                                                           |
>
>    1. Click the **Gear** icon ([icon: gear, set=fa]) next to the `sub` attribute, enter the expression, and click **Save**.
>
>       |   |                                                                                                                                                                           |
>       | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       |   | Leave the **Required** checkbox cleared. If marked required, standard `client_credentials` requests are rejected by PingOne before the attribute expression is evaluated. |
>
>       Learn more about expressions in [Using the expression builder](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_use_expression_builder.html) in the PingOne documentation.
>
>    2. Click **+ Add** and name the attribute `act`.
>
>    3. Click [icon: gear, set=fa], enter the expression, and click **Save**.
>
>    4. Select the **Required** checkbox for the `act` attribute.
>
>       This ensures that any token exchange that fails to set `act` is rejected. Unauthorized requests evaluate to null and explicitly fail.
>
>    5. Click **+ Add** and name the attribute `may_act`.
>
>    6. []()Click [icon: gear, set=fa], enter the expression, replace the `<ORDER-STATUS-AGENT-CLIENT-ID>` placeholder with the AC Order Status Agent's **Client ID** you saved [earlier](#idai-gemini-a2a-osa-client-id), and click **Save**.
>
>    7. (Optional) Click **+ Add**, name the attribute `grant_type`, click [icon: gear, set=fa], enter the expression, and click **Save**.
>
> 5. Click **Next**, then click **+ Add Scope**.
>
> 6. Name the scope `order-status:invoke`.
>
>    The Support Agent requests this scope when it exchanges the user's sign-on token during the first exchange.
>
> 7. Click **Save**.

> **Collapse: Deploy and register the Order Status Agent in Agent Registry**
>
> To finish Order Status Agent setup, deploy it to the Google Cloud Agent Runtime. This deployment automatically registers the agent in Agent Registry and routes all of its egress traffic through the Agent Gateway.
>
> 1. Set environment variables for the agent:
>
>    1. In the cloned repository, go to the `pingone/agent-chaining/services/order-status-agent` directory.
>
>    2. Make a copy of the `.env.sample` file and name it `.env`:
>
>       ```bash
>       cp .env.sample .env
>       ```
>
>    3. Set environment variables in the `.env` file:
>
>       | Variable                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
>       | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       | `GC_REGION`             | Your Google Cloud Platform region. For example: `us-central1`.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
>       | `AGENT_DISPLAY_NAME`    | Display name for the Reasoning Engine: `ac-order-status-agent`.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
>       | `IDP_ISSUER`            | The PingOne issuer URL: `https://auth.pingone.<region>/<env-id>/as`.To find this endpoint, go to the AC Order Status Agent in PingOne. Copy the **Issuer ID** under **Connection Details** on the **Overview** tab.                                                                                                                                                                                                                                                                                                       |
>       | `GC_AGENT_GATEWAY`      | The gateway name: `ac-agent-gateway`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
>       | `AGENT_CLIENT_ID`       | The AC Order Status Agent's **Client ID**. This is located above **Connection Details** on the agent's **Overview** tab in PingOne.                                                                                                                                                                                                                                                                                                                                                                                       |
>       | `AGENT_CLIENT_SECRET`   | The AC Order Status Agent's **Client Secret**. This is located above **Connection Details** on the agent's **Overview** tab.                                                                                                                                                                                                                                                                                                                                                                                              |
>       | `IDP_REQUIRED_AUDIENCE` | The audience accepted on the inbound A2A token exchange: `order-status-agent`.The gateway service extension validates this audience before generating the outbound token for the MCP server.                                                                                                                                                                                                                                                                                                                              |
>       | `IDP_REQUIRED_SCOPE`    | The scope accepted on the inbound A2A token exchange: `order-status:invoke`.The gateway service extension validates this scope before generating the outbound token for the MCP server.                                                                                                                                                                                                                                                                                                                                   |
>       | `TOOL_URL`              | The Order Status MCP Server's Cloud Run base URL: `https://ac-order-status-mcp-server-<your-project-number>.<your-deployment-region>.run.app/mcp`.To find this URL, go to **Cloud Run > Services** and click the **order-status-mcp-server**. Copy the URL at the top of the page. Paste the URL in the `.env` file, making sure `/mcp` is at the end of the URL.                                                                                                                                                         |
>       | `TOOL_SCOPE`            | The scope the agent requests during token exchange to authorize access to the downstream MCP server: `order:read`.                                                                                                                                                                                                                                                                                                                                                                                                        |
>       | `GATEWAY_AUDIENCE`      | The audience the agent requests during token exchange to authorize access to the Agent Gateway: `ac-google-cloud-agent-gateway`.The agent doesn't target the final `order-status-mcp-server` audience directly. Instead, it exchanges its token for this intermediate audience. The gateway service extension then intercepts the outbound request and performs the final token exchange to the MCP server. This value must exactly match the `AGENT_GATEWAY_AUDIENCE` value configured in the gateway service extension. |
>
> 2. In the `pingone/agent-chaining/services/order-status-agent` directory, run the following command:
>
>    ```bash
>    make deploy
>    ```
>
>    The `deploy.py` script provisions the Reasoning Engine using `identity_type = AGENT_IDENTITY`. The script also binds the engine to the gateway and grants it the `roles/iap.egressor` role on Agent Registry, authorizing the agent to securely reach all registered downstream endpoints.
>
> 3. []()Complete the Order Status Agent's `AGENT_ENGINE_ID` [placeholder](#idai-gemini-a2a-order-status-engine-id) in the service extension's `.env` file, then redeploy the service extension.
>
> 4. []()In PingOne, go to the AC Agent Gateway Extension application and [assign](#idai-gemini-a2a-order-status-scope) the **order_status:invoke** scope on the AC Order Status Agent.

### Deploy the Support Agent

The [Support Agent](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-chaining/services/support-agent) serves as the user-facing entry point in the delegation chain. Instead of interacting with the downstream Order Status MCP Server directly, it delegates order status requests to the Order Status Agent over A2A.

The Agent Bridge stores the user's PingOne sign-on token in ADK session state. This token is initially scoped to the agent's own `support-agent` audience. The agent manages the token through this sequence:

* The agent independently verifies the token's signature, issuer, audience, and the `support-agent:invoke` scope before using it.

* The agent performs a token exchange using the user's token as the subject and its own PingOne client credentials as the actor. This targets the intermediate `ac-google-cloud-agent-gateway` audience.

* As the agent initiates the outbound A2A request, the Agent Runtime routes egress traffic through the Agent Gateway. The service extension intercepts this request and performs the final token exchange, generating a token scoped to the `order-status-agent` audience.

You'll create the agent's PingOne application and deploy the agent to the Agent Runtime, binding it to the Agent Gateway.

> **Collapse: Create the Support Agent in PingOne**
>
> Create an AI agent in PingOne to establish a dedicated identity for the Support Agent. This identity enables the agent to authenticate and acquire access tokens during delegation exchanges.
>
> |   |                                                                                                                                                              |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> |   | You can find more details about [adding AI agents](https://docs.pingidentity.com/pingone/ai_agents/p1_managing_ai_agents.html) in the PingOne documentation. |
>
> 1. In the PingOne admin console, go to **AI Agents** and click the **[icon: plus, set=fa]**icon.
>
> 2. Name the agent `AC Support Agent`.
>
> 3. Click **Save**.
>
> 4. To enable the agent, click the toggle next to the agent name in the details panel.
>
> 5. On the **Configuration** tab, click [icon: pencil, set=fa]:
>
>    1. In **Grant Type**, select **Client Credentials** and **Token Exchange**.
>
>    2. Clear the **Code** and **Authorization Code** checkboxes.
>
>    3. Click **Save**.
>
> 6. On the **Resources** tab, click [icon: pencil, set=fa], then select the **order-status:invoke** scope on the AC Google Cloud Agent Gateway resource.
>
> 7. Click **Save**.
>
> 8. []()On the **Overview** tab, copy the **Client ID** for this agent and save it somewhere convenient. You'll need it later when you [configure attributes](#idai-gemini-a2a-sa-attr) for the Support Agent resource in PingOne.

> **Collapse: Create the Support Agent resource in PingOne**
>
> The Support Agent resource generates the Chat UI's sign-on token, establishing the user identity that enters the delegation chain.
>
> Because this resource exclusively processes direct user sign-ons with the `authorization_code` grant and doesn't process `client_credentials` requests, the default User ID mapping for the `sub` claim is sufficient. This mirrors the AOBOU Financial Agent resource in the [authorizing agents on behalf of users](idai-authorizing-gemini-on-behalf-of-users-with-ping.html) use case.
>
> You don't need to configure an `act` attribute. Because no actor exists during a direct user sign-on, the initial sign-on token doesn't include an `act` claim. During subsequent token exchanges, the gateway resource's nesting logic translates this absence into a null at the innermost position of every downstream token.
>
> To initialize the delegation chain, you'll configure the following custom attributes:
>
> * `may_act`: Licenses the Support Agent as the only authorized next actor on every token minted for this resource. Assigning a constant value (the agent's PingOne client ID) to this attribute ensures the Support Agent's subsequent token exchange, which targets the shared gateway audience, carries a valid `act` claim. This allows the exchange to pass the gateway resource's delegation check while failing closed for anyone else.
>
> * `grant_type` (Optional): Enriches the token by exposing the authorization grant type (such as `authorization_code`) as a first-class claim.
>
> |   |                                                                                                                                                                            |
> | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [adding custom resources](https://docs.pingidentity.com/pingone/applications/p1_adding_custom_resource.html) in the PingOne documentation. |
>
> 1. In the PingOne admin console, go to **Applications > Resources** and click the **[icon: plus, set=fa]**icon.
>
> 2. Define the resource:
>
>    1. **Resource Name**: `AC Support Agent`
>
>    2. **Audience**: `support-agent`
>
> 3. Click **Next**.
>
> 4. Define attributes for the resource:
>
>    Detailed steps follow the table.
>
>    | Attribute    | Required | Expression                                      |
>    | ------------ | -------- | ----------------------------------------------- |
>    | `may_act`    | No       | ```spel
>    {"sub":"<SUPPORT-AGENT-CLIENT-ID>"}
>    ``` |
>    | `grant_type` | No       | ```spel
>    #root.context.requestData.grantType
>    ``` |
>
>    1. Click **+ Add** and name the attribute `may_act`.
>
>    2. []()Click [icon: gear, set=fa], enter the expression, replace the `<SUPPORT-AGENT-CLIENT-ID>` placeholder with the AC Support Agent's **Client ID** you saved [earlier](#idai-gemini-a2a-sa-client-id), and click **Save**.
>
>       Learn more about expressions in [Using the expression builder](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_use_expression_builder.html) in the PingOne documentation.
>
>    3. (Optional) Click **+ Add**, name the attribute `grant_type`, click [icon: gear, set=fa], enter the expression, and click **Save**.
>
> 5. Click **Next**, then click **+ Add Scope**.
>
> 6. Name the scope `support-agent:invoke`.
>
>    The Order Status Agent requests this scope when it exchanges the Support Agent's delegated token during the second exchange.
>
> 7. Click **Save**.

> **Collapse: Deploy and register the Support Agent in Agent Registry**
>
> To finish Support Agent setup, deploy it to the Google Cloud Agent Runtime. This deployment automatically registers the agent in Agent Registry and routes all of its egress traffic through the Agent Gateway.
>
> 1. Set environment variables for the agent:
>
>    1. In the cloned repository, go to the `pingone/agent-chaining/services/support-agent` directory.
>
>    2. Make a copy of the `.env.sample` file and name it `.env`:
>
>       ```bash
>       cp .env.sample .env
>       ```
>
>    3. Set environment variables in the `.env` file:
>
>       | Variable                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
>       | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       | `GC_REGION`             | Your Google Cloud Platform region. For example: `us-central1`.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
>       | `AGENT_DISPLAY_NAME`    | Display name for the Reasoning Engine: `ac_support_agent`.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
>       | `IDP_ISSUER`            | The PingOne issuer URL: `https://auth.pingone.<region>/<env-id>/as`.To find this endpoint, go to the AC Support Agent in PingOne. Copy the **Issuer ID** under **Connection Details** on the **Overview** tab.                                                                                                                                                                                                                                                                                                   |
>       | `GC_AGENT_GATEWAY`      | The gateway name: `ac-agent-gateway`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
>       | `AGENT_CLIENT_ID`       | The AC Support Agent's **Client ID**. This is located above **Connection Details** on the agent's **Overview** tab in PingOne.                                                                                                                                                                                                                                                                                                                                                                                   |
>       | `AGENT_CLIENT_SECRET`   | The AC Support Agent's **Client Secret**. This is located above **Connection Details** on the agent's **Overview** tab.                                                                                                                                                                                                                                                                                                                                                                                          |
>       | `IDP_REQUIRED_AUDIENCE` | The expected audience used to validate the user's incoming PKCE sign-on token provided by the Agent Bridge: `support-agent`.The gateway service extension validates the token against this audience before using it as the subject token in the outbound token exchange. The validation process is independent of the agent's own client credentials.                                                                                                                                                            |
>       | `IDP_REQUIRED_SCOPE`    | The expected scope on the inbound browser token: `support-agent:invoke`.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
>       | `AGENT_ENGINE_ID`       | The Reasoning Engine's identifier for the Order Status Agent. In this example, the ID follows `reasoningEngines:` in the Order Status Agent's URN: `urn:agent:projects-909399354423:projects:909399354423:locations:us-central1:aiplatform:reasoningEngines:7390548000881246208`.To find this ID, go to the `ac-order-status-agent` service in **Agent Registry**.                                                                                                                                               |
>       | `AGENT_SCOPE`           | The scope requested on the delegated A2A token: `order-status:invoke`. The gateway service extension validates this scope before generating the outbound token for the Order Status Agent.                                                                                                                                                                                                                                                                                                                       |
>       | `GATEWAY_AUDIENCE`      | The audience the agent requests during token exchange to authorize access to the Agent Gateway: `ac-google-cloud-agent-gateway`.The agent doesn't target the `order-status-agent` audience directly. Instead, it exchanges its token for this intermediate audience. The gateway service extension then intercepts the outbound request and performs the token exchange to the Order Status Agent. This value must exactly match the `AGENT_GATEWAY_AUDIENCE` value configured in the gateway service extension. |
>
> 2. In the `pingone/agent-chaining/services/support-agent` directory, run the following command:
>
>    ```bash
>    make deploy
>    ```
>
>    The `deploy.py` script provisions the Reasoning Engine using `identity_type = AGENT_IDENTITY`. The script also binds the engine to the gateway and grants it the `roles/iap.egressor` role on Agent Registry, authorizing the agent to securely reach all registered downstream endpoints.

### Deploy the Agent Bridge

The [Agent Bridge](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-chaining/services/agent-bridge) acts as the secure integration layer between the Chat UI and the Support Agent. This server-side bridge mediates the connection between the browser, which holds only a PingOne identity, and the agent running on the Google Cloud Agent Runtime. When it receives a chat request, the bridge validates the user's PingOne token against the PingOne JSON Web Key Set (JWKS), verifying the signature, issuer, `support-agent` audience, and `sub` claim. The bridge then resolves the agent session and stores the token in the session state for the Support Agent to consume.

> **Collapse: Deploy the Agent Bridge to Cloud Run**
>
> Build the Agent Bridge with configured environment variables and deploy it as a Google Cloud Run service.
>
> 1. Set environment variables for the Agent Bridge:
>
>    1. In the cloned repository, go to the `pingone/agent-chaining/services/agent-bridge` directory.
>
>    2. Make a copy of the `.env.sample` file and name it `.env`:
>
>       ```bash
>       cp .env.sample .env
>       ```
>
>    3. Set environment variables in the `.env` file:
>
>       | Variable                    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
>       | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       | `GC_REGION`                 | Your Google Cloud Platform region. For example: `us-central1`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
>       | `GC_CLOUD_RUN_SERVICE_NAME` | The Cloud Run service name: `ac-agent-bridge`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
>       | `IDP_ISSUER`                | The PingOne issuer URL: `https://auth.pingone.<region>/<env-id>/as`.To find this endpoint, go to the AC Support Agent in PingOne. Copy the **Issuer ID** under **Connection Details** on the **Overview** tab.                                                                                                                                                                                                                                                                                                                    |
>       | []()`CORS_ORIGIN`           | The Chat UI Cloud Run URL. For example: `https://ac-chat-ui-<project-id>.<region>.run.app`.This is a placeholder. After you [deploy the Chat UI](#idai-gemini-a2a-chat-ui-deployed-cors-origin) in a later task, update this value with the actual URL, then redeploy the Agent Bridge.                                                                                                                                                                                                                                           |
>       | `IDP_REQUIRED_AUDIENCE`     | The expected audience for the browser's PKCE sign-on token: `support-agent`.This is the Support Agent's PingOne resource audience. The Agent Bridge validates the token against this audience before storing it in session state for the Support Agent to consume.                                                                                                                                                                                                                                                                |
>       | `AGENT_ENGINE_ID`           | The Reasoning Engine's identifier for the Support Agent. In this example, the ID follows `reasoningEngines:` in the Support Agent's URN: `urn:agent:projects-909399354423:projects:909399354423:locations:us-central1:aiplatform:reasoningEngines:5246834578252890112`.To find this ID, go to the `ac_support-agent` service in **Agent Registry**.&#xA;&#xA;The Reasoning Engine ID changes each time you redeploy the Support Agent. If you redeploy the agent, update this environment variable and redeploy the Agent Bridge. |
>
> 2. In the `pingone/agent-chaining/services/agent-bridge` directory, run the following command:
>
>    ```bash
>    make deploy
>    ```
>
>    This builds the Docker image, pushes it to Google Container Registry, and deploys it to Cloud Run.

### Deploy the Chat UI

The [Chat UI](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-chaining/services/chat-ui) is a React and Vite single-page application (SPA) that serves as the frontend interface for users. It handles user authentication directly against PingOne using an OAuth 2.0 Authorization Code grant with PKCE. After a user authenticates, the application routes chat requests and the resulting sign-on token to the Support Agent through the Agent Bridge.

> **Collapse: Create the Chat UI application in PingOne**
>
> Create a SPA in PingOne that represents the Chat UI. This application manages initial user authentication using PKCE. It acquires the user's baseline sign-on token and passes it to the Agent Bridge, which uses the token to initialize the downstream delegation chain.
>
> 1. In the PingOne admin console, go to **Applications > Applications**.
>
> 2. Click the **[icon: plus, set=fa]**icon and create the application profile:
>
>    1. Name the application `Agent Chaining Chat UI`.
>
>    2. For the **Application Type**, click **Single-Page**.
>
>    3. Click **Save**.
>
> 3. To enable the application, click the toggle next to the application name in the details panel.
>
> 4. On the **Configuration** tab, click [icon: pencil, set=fa]:
>
>    1. Make sure **Authorization Code** with **S256_REQUIRED** is the **Grant Type**.
>
>    2. []()In the **Redirect URIs** and **Signoff URLs** fields, enter the Chat UI URL from Cloud Run. For example: `https://ac-chat-ui-<project-id>.<region>.run.app`.
>
>       These are placeholders. After you [deploy the Chat UI](#idai-gemini-a2a-chat-deployed-redirect-uri) in a later task, update these values with the actual URL.
>
> 5. Click **Save**.
>
> 6. On the **Resources** tab, click [icon: pencil, set=fa], then select scopes:
>
>    * **email**
>
>    * **openid** (selected by default)
>
>    * **profile**
>
>    * **support-agent:invoke** scope on the AC Support Agent resource (at the bottom of the scopes list)
>
> 7. Click **Save**.

> **Collapse: Deploy the Chat UI to Cloud Run**
>
> Configure environment variables and deploy the Chat UI to Cloud Run. The deployment process compiles the Vite application, packages the static web assets into an NGINX Docker image, and deploys the container to connect to the Agent Bridge.
>
> 1. Set environment variables for the Chat UI:
>
>    1. In the cloned repository, go to the `pingone/agent-chaining/services/chat-ui` directory.
>
>    2. Make a copy of the `.env.sample` file and name it `.env`:
>
>       ```bash
>       cp .env.sample .env
>       ```
>
>    3. Set environment variables in the `.env` file:
>
>       | Variable                    | Value                                                                                                                                                                                                                                                                                                                                                                                                                         |
>       | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       | `GC_REGION`                 | Your Google Cloud Platform region. For example: `us-central1`.                                                                                                                                                                                                                                                                                                                                                                |
>       | `GC_CLOUD_RUN_SERVICE_NAME` | The Chat UI's Cloud Run service name: `ac-chat-ui`.                                                                                                                                                                                                                                                                                                                                                                           |
>       | `VITE_IDP_ISSUER`           | The PingOne issuer URL: `https://auth.pingone.<region>/<env-id>/as`.To find this endpoint, go to the Agent Chaining Chat UI application in PingOne. Copy the **Issuer ID** under **Connection Details** on the **Overview** tab.                                                                                                                                                                                              |
>       | `VITE_CLIENT_ID`            | The Agent Chaining Chat UI application's **Client ID**. This is located above **Connection Details** on the **Overview** tab.                                                                                                                                                                                                                                                                                                 |
>       | []()`VITE_REDIRECT_URI`     | The Chat UI Cloud Run URL: `https://ac-chat-ui-<project-id>.<region>.run.app`.After you deploy the Chat UI to Cloud Run, update this value with the actual URL. To find the URL, go to **Cloud Run > Services** and click the **ac-chat-ui** service. Copy the URL at the top of the page.&#xA;&#xA;This redirect URL must exactly match the Redirect URIs and Signoff URLs configured in the Chat UI application in PingOne. |
>       | `VITE_AGENT_BRIDGE_URL`     | Your Agent Bridge Cloud Run URL. For example: `https://ac-agent-chain-bridge-<project-id>.<region>.run.app`.To find this URL, go to **Cloud Run > Services** and click the **ac-agent-bridge** service. Copy the URL at the top of the page.                                                                                                                                                                                  |
>       | `VITE_SCOPES`               | The OAuth 2.0 scopes the Chat UI requests from PingOne during the user authentication flow: `openid profile email support-agent:invoke`.This includes standard OpenID Connect scopes (such as `openid` and `profile`) along with the specific scope required to authorize the request to the Support Agent (`support-agent:invoke`).                                                                                          |
>
> 2. In the `pingone/agent-chaining/services/chat-ui` directory, run the following command:
>
>    ```bash
>    make deploy
>    ```
>
>    This builds the Vite app, packages it in an NGINX Docker image, and deploys it to Cloud Run.
>
>    Vite statically embeds all `VITE_*` environment variables (such as `VITE_SCOPES`) directly into the JavaScript bundle during the build phase. Updating variables on a running Cloud Run container has no effect. You must run `make deploy` to rebuild the application and apply your changes.
>
>    Docker can silently reuse a cached build layer even after you modify your local `.env` file. If a variable change doesn't appear in the deployed application (which you can verify by checking if the served `index-*.js` filename remains identical to the previous build), force a clean build using the `--no-cache` flag. Always rule out a stale Docker cache before troubleshooting your PingOne or backend configurations.
>
> 3. []()Complete the Chat UI's `CORS_ORIGIN` [placeholder](#idai-gemini-a2a-chat-ui-cors-origin) in the Agent Bridge's `.env` file, then redeploy the Agent Bridge.
>
> 4. Complete the Chat UI's `VITE_REDIRECT_URI` [placeholder](#idai-gemini-a2a-chat-redirect-uri) in the Chat UI's `.env` file, then redeploy the Chat UI.
>
> 5. []()In the [Chat UI application](#idai-gemini-a2a-p1-redirect-uri) in PingOne, enter the deployed `ac-chat-ui` service's [Cloud Run URL](#idai-gemini-a2a-chat-redirect-uri) in the **Redirect URIs** and **Signoff URLs** placeholders.
>
>    This ensures that the Chat UI can successfully redirect users back to the application after authentication.

## Validation

To validate your configuration, sign on to the Chat UI as a PingOne user belonging to the `support_team` group and query the status of an order. This initiates a request that the Support Agent delegates to the Order Status Agent, which calls the Order Status MCP Server to retrieve the order status. Because the delegation chain is recorded at every stage of the interaction, you can verify that the correct tokens are exchanged and validated.

1. Go to the Chat UI URL (`https://ac-chat-ui-<project-id>.<region>.run.app`) and click **Sign In**.

2. Authenticate as a PingOne user assigned to the `support_team` group.

3. Ask the agent: `What is the status of order ORD-123?`

   The agent should reply with the correct order status (for example, `ORD-123` returns as shipped, and `ORD-456` returns as processing).

You can observe the full delegation sequence by monitoring the Cloud Run logs for the service extension and the Order Status MCP Server, along with the Reasoning Engine logs for the Order Status Agent.

While the chat runs, the logs should display the following progression:

```text
# service extension (A2A hop): the Support Agent's delegated token is validated
# against the shared gateway audience, reminted for the Order Status Agent, and
# injected alongside the Google credential the A2A endpoint's IAM check requires.
[ExtSvc] onHeaders authority="us-central1-aiplatform.mtls.googleapis.com" path="<redacted>/reasoningEngines/<order-status-agent-id>/a2a/message:send" matched=true
[ExtSvc] delegated token minted target=A2A ttl=59m30s
[ExtSvc] validated delegated token — sub=<user-sub> aud=ac-google-cloud-agent-gateway scope="order-status:invoke"
[ExtSvc] injecting Google credential + reminted token (aud=order-status-agent scope=order-status:invoke) for A2A

# service extension: {p1-paz} is consulted on every governed action
# (A2A message:send and MCP tools/call alike).
[ExtSvc] authorize user=<user-sub> action=get_order_status hour=10
[ExtSvc] {p1-paz} PERMIT user=<user-sub>
[ExtSvc] PERMIT target=A2A action=get_order_status order=ORD-123 (authz=pingone-authorize)

# Order Status Agent: the gateway-reminted A2A token is validated independently
# (signature, issuer, audience, and scope) before use. The log shows who the call
# is for (sub, the user throughout), which audience it was minted for (aud),
# who acted for it (act, the delegation chain so far), and the granted scope.
[OrderStatusAgent] Delegated token verified — sub=<user-sub> aud=['order-status-agent'] act=<ext-svc-client-id> -> <support-agent-client-id> scope="order-status:invoke"

# Order Status Agent: its own exchange mints the MCP-scoped token, then the
# MCP call runs only after the PERMIT above.
[OrderStatusAgent] get_order_status start order_id=ORD-123
[OrderStatusAgent] exchanged for MCP token (aud=order-status-mcp-server), calling MCP server order_id=ORD-123

# service extension (MCP hop): the Order Status Agent's token is validated and
# reminted for the MCP server; Authorization now carries the PingOne token
# directly (no Google credential needed on this hop).
[ExtSvc] onHeaders authority="<order-status-mcp-server-url>" path="/mcp" matched=true
[ExtSvc] delegated token minted target=MCP ttl=59m30s
[ExtSvc] validated delegated token — sub=<user-sub> aud=ac-google-cloud-agent-gateway scope="order:read"
[ExtSvc] injecting reminted token (aud=order-status-mcp-server scope=order:read) for MCP
[ExtSvc] authorize user=<user-sub> action=get_order_status hour=10
[ExtSvc] {p1-paz} PERMIT user=<user-sub>
[ExtSvc] PERMIT target=MCP action=get_order_status order=ORD-123 (authz=pingone-authorize)

# Order Status MCP server: every request's token is verified (signature,
# issuer, audience, and scope) before handling. The log shows who the call is
# for (sub, the user throughout), which audience it was minted for (aud), who
# acted for it (act.sub — the full chain: extension -> Order Status Agent ->
# extension -> Support Agent, the delegation).
[OrderStatusMCP] Token verified — sub=<user-sub> aud=[order-status-mcp-server] act.sub=<ext-svc-client-id> -> <order-status-agent-client-id> -> <ext-svc-client-id> -> <support-agent-client-id> scope="order:read"

# Order Status MCP server: the lookup itself.
[OrderStatusMCP] tool=get_order_status — caller=<user-sub> order=ORD-123 status=shipped
```

Outside the governed execution paths, the service extension also logs the Reasoning Engine's internal Agent Runtime session calls (`matched=false`). These internal calls pass through untouched. Only the `matched=true` lines above represent governed interactions. If PingOne Authorize issues a deny decision (for example, if the request occurs outside business hours or the user isn't on the support team), the logs surface an `[ExtSvc] DENY target=…​` entry followed by an immediate 403 Forbidden error, and the agent notifies the user that the request was denied.

## Troubleshooting

If you encounter issues while deploying or testing the A2A chain, use the following information to resolve common problems:

* Chat UI authentication fails

  Verify that the Agent Chaining Chat UI application in PingOne is configured with the Authorization Code grant type with PKCE. Additionally, check that the configured redirect URI exactly matches the URL of your deployed Cloud Run service.

* Chat UI configuration changes aren't applied after deployment

  If you update a `VITE_*` environment variable (such as `VITE_SCOPES`) but the deployed UI doesn't reflect the change, the Docker build cache probably reused a stale compilation layer. Rebuild and deploy the application using the `--no-cache` flag to force Vite to statically embed the new variables in the JavaScript bundle.

* Support Agent doesn't receive the user token

  Verify that the Agent Bridge is correctly deployed to Cloud Run and that the Chat UI is successfully sending the token to the bridge payload during the initial chat request.

* Requests are blocked before they reach the service extension

  If the Agent Gateway returns a 403 Forbidden error or logs a `DENIED` message with no `agentRegistryResource`, the request is failing Google Cloud's IAP egress check.

  * Make sure the Reasoning Engine identity has the `roles/iap.egressor` role applied.

  * Verify that the downstream URL registered in Agent Registry exactly matches the host URL the agent is configured to call. IAP resolves egress destinations by host name, and a mismatch causes an immediate denial.

* Order Status Agent or MCP server doesn't receive the delegated token

  Confirm that the Agent Gateway Service Extension is correctly deployed and attached to the Agent Gateway. Check the service extension logs in Cloud Run to verify that it's successfully intercepting the request and performing the RFC 8693 token exchange for the target audience.

  If the Order Status MCP Server fails to receive the delegated token, check that the Agent Gateway Service Extension is correctly reminting the token for the MCP server and that the MCP server is correctly validating the token.

* Token validation or token exchange fails

  Verify that your PingOne resources are configured with the correct custom attributes.

  * Ensure the `may_act` claims are set to the client ID of the next permitted actor in the delegation chain.

  * If a token exchange fails with a 400 error during a `client_credentials` grant, verify that the **Required** checkbox is cleared for the `sub` attribute on the target PingOne resource.

* PingOne Authorize policies aren't enforced

  Make sure the PingOne Authorize decision endpoint URL is correctly configured in your service extension environment variables. In PingOne Authorize **Version History**, verify that your policies are published to the correct version.

## What's next

A2A delegation is a powerful pattern for enabling secure, governed interactions between autonomous agents. Consider extending this architecture to support additional agents, tools, and services in your environment.

|   |                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you're finished working with the A2A use case, you can clean up the resources you deployed in this environment. From the `pingone/agent-chaining` directory, run the `make destroy` command to safely remove the Google Cloud infrastructure specific to this use case. |

---

---
title: Authorizing Gemini agents on behalf of users with Ping Identity solutions
description: Authorize a Gemini agent acting on behalf of a user to call an MCP tool with scoped, short-lived delegation tokens.
component: identity-for-ai
page_id: identity-for-ai:integrations:idai-authorizing-gemini-on-behalf-of-users-with-ping
canonical_url: https://developer.pingidentity.com/identity-for-ai/integrations/idai-authorizing-gemini-on-behalf-of-users-with-ping.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-10-14T20:28:12Z
keywords: ["Identity for AI", "ai identity", "ai security", "Google Cloud Gemini Enterprise", "Gemini Enterprise Agent Platform", "PingOne Authorize", "authentication", "authorization"]
section_ids:
  how-this-works: How this works
  components: Components
  token-chain: Token chain
  benefits-of-this-approach: Benefits of this approach
  goals: Goals
  what-youll-do: What you'll do
  before-you-begin: Before you begin
  tasks: Tasks
  deploy-mcp-server: Deploy the Stripe MCP Server
  create-policies: Create the policies in PingOne Authorize
  deploy-extension-service: Deploy the Agent Gateway Service Extension
  create-gateway: Create the Agent Gateway
  deploy-agent: Deploy the Financial Agent
  deploy-bridge: Deploy the Agent Bridge
  deploy-chat-ui: Deploy the Chat UI
  validation: Validation
  troubleshooting: Troubleshooting
  whats-next: What's next
---

# Authorizing Gemini agents on behalf of users with Ping Identity solutions

This use case secures an agent that calls protected tools and resources on behalf of a human user. The human proves their identity, and that identity is preserved through every delegation boundary between the user, agent, and downstream services. The Agent Gateway Service Extension asks PingOne Authorize for a policy decision and, when approved, mints a scoped, short-lived token that identifies the human user. The extension then forwards the request to the MCP server, which calls downstream resources to execute operations for the human.

This use case builds on the [Integrating Gemini Enterprise Agent Platform with Ping Identity solutions](idai-integrating-gemini-agent-platform-with-ping.html) architecture by adding a human in the loop to the flow. You can find more information about [token exchange with delegation](https://docs.pingidentity.com/pingone/use_cases/p1_oauth_2_token_exchange_delegation.html) in the PingOne documentation.

## How this works

Consider an agent that purchases products on behalf of an authenticated user. The following diagram shows the components involved:

![Diagram showing an AI agent requesting access to a resource with human involvement.](_images/idai-gemini-agent-user-flow.png)

1. The user signs on with PingOne through the Chat UI.

2. The agent exchanges the user's token for a delegated token that names the agent as the actor.

3. The agent runtime routes Model Context Protocol (MCP) requests through the Agent Gateway to the Agent Gateway Service Extension.

4. The Agent Gateway Service Extension validates the delegated token, resolves the user's email, and asks PingOne Authorize whether this agent is permitted to act for this user on this transaction.

5. Upon permit, the Agent Gateway Service Extension performs a second token exchange, minting a token audienced for the Stripe MCP Server that preserves the user's identity and records the full delegation chain. The extension then injects the token and forwards the request.

### Components

| Component                                                                                                                                                                                           | Role                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Chat UI](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/blob/main/pingone/agent-on-behalf-of-user/services/chat-ui)                                                 | Chat interface that the user signs on to PingOne and interacts with.                                                                                       |
| [Agent](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/blob/main/pingone/agent-on-behalf-of-user/services/agent)                                                     | Financial agent acting as an MCP client. Reads the user token and performs token exchange.                                                                 |
| [Agent Bridge](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/blob/main/pingone/agent-on-behalf-of-user/services/agent-bridge)                                       | Google Cloud entry point. Validates the user token and stores it in the agent session state.                                                               |
| [Agent Gateway](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/blob/main/pingone/agent-on-behalf-of-user/services/agent-gateway)                                     | Google-managed policy enforcement point that forwards agent requests to the Agent Gateway Service Extension over the gRPC remote procedure call framework. |
| [Agent Gateway Service Extension](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/blob/main/pingone/agent-on-behalf-of-user/services/agent-gateway-extension-service) | Handler that sends requests to PingOne Authorize, exchanges the agent's token, and injects the resulting token into the request.                           |
| [Stripe MCP Server](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/blob/main/pingone/agent-on-behalf-of-user/services/stripe-mcp-server)                             | Downstream resource that the agent invokes to make a purchase.                                                                                             |
| [PingOne](https://docs.pingidentity.com/pingone)                                                                                                                                                    | Identity provider (IdP) that issues the agent's token, the delegated agent token, and the delegated tool token.                                            |
| [PingOne Authorize](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_overview.html)                                                                                 | External policy decision point that evaluates authorization requests.                                                                                      |

### Token chain

The token flow begins when the user signs on with PingOne through the Chat UI. The Financial Agent presents the user's token to PingOne as the subject of a token exchange, together with its own client credentials token as the actor. PingOne checks the user token's `may_act` claim against the acting client before minting the delegated token, which still names the user as the subject. The Agent Gateway Service Extension later exchanges that delegated token the same way, minting the final tool token for the Stripe MCP Server. Each exchange adds its actor to the `act` claim, so the final token records the full delegation chain. The agent and Agent Gateway's actor tokens are omitted from this overview for simplicity.

* User token: the Chat UI's token

  ```json
  {
    "iss": "https://auth.pingone.<region>/<env-id>/as",
    "sub": "<alice-user-id>",
    "client_id": "<chat-ui-client-id>",
    "aud": "finance-agent",
    "scope": "openid stripe_mcp:invoke",
    "grant_type": "authorization_code",
    "may_act": { "sub": "<finance-agent-client-id>" }
  }
  ```

  * `sub`: Identifies the human user as the principal subject of the token.

  * `client_id`: Identifies the chat bot as the OAuth client that requested the token.

  * `aud`: Identifies the Financial Agent resource as the recipient of the token.

  * `scope`: Grants the privileges required to invoke the Stripe tools.

  * `may_act`: Authorizes the Financial Agent to delegate next.

* Delegated token: the agent's exchanged token

  ```json
  {
    "iss": "https://auth.pingone.<region>/<env-id>/as",
    "sub": "<alice-user-id>",
    "client_id": "<finance-agent-client-id>",
    "aud": "google-agent-gateway",
    "scope": "stripe_mcp:invoke",
    "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
    "act": { "sub": "<finance-agent-client-id>", "act": null },
    "may_act": { "sub": "<agent-gw-extension-client-id>" }
  }
  ```

  * `sub`: Identifies the human user as the principal subject of the token.

  * `client_id`: Identifies the Financial Agent as the OAuth client that requested the token.

  * `aud`: Identifies the Agent Gateway as the recipient of the token.

  * `scope`: Grants the privileges required to invoke the Stripe tools.

  * `act`: Identifies the Financial Agent as the source of delegation.

  * `may_act`: Authorizes only the Agent Gateway Service Extension to delegate next.

* MCP tool token: the Agent Gateway's delegated (exchanged) token

  ```json
  {
    "iss": "https://auth.pingone.<region>/<env-id>/as",
    "sub": "<alice-user-id>",
    "client_id": "<agent-gw-extension-client-id>",
    "aud": "stripe-mcp-server",
    "scope": "stripe_mcp:invoke",
    "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
    "act": {
      "sub": "<agent-gw-extension-client-id>", "act": {
        "sub": "<finance-agent-client-id>", "act": null
      }
    }
  }
  ```

  * `sub`: Identifies the human user as the principal subject of the token. The user's identity is preserved end to end.

  * `client_id`: Identifies the Agent Gateway Service Extension as the OAuth client that requested the token.

  * `aud`: Identifies the Stripe MCP Server as the recipient of the token.

  * `scope`: Grants the privileges required to invoke the Stripe tools.

  * `act`: Identifies the Agent Gateway Service Extension as the source of delegation, on behalf of the agent.

### Benefits of this approach

* **No standing credentials in the agent:** The agent never holds a token that acts directly on a resource. It only receives a delegated token scoped to the Agent Gateway.

* **Compound authorization:** PingOne Authorize evaluates the user and the agent together. A rogue agent can't use a stolen user token, and a user can't call the tool through an unauthorized agent.

* **Delegation proof:** The tool token carries a nested `act` chain naming every actor in order: the Agent Gateway Service Extension and then the agent. PingOne only builds that chain after checking each token's `may_act` claim at exchange time, so the tool can see exactly who acted for whom, end to end.

* **Centralized policy:** PingOne Authorize owns the authorization decision. Policies can be updated centrally without modifying or redeploying the agent, the gateway, or the MCP server.

## Goals

* Demonstrate how to authorize an agent to call a protected tool on behalf of a human user.

* Use PingOne to perform a token exchange that mints a delegated token for a downstream tool.

## What you'll do

1. [Deploy the MCP server](#deploy-mcp-server) to Google Cloud Run and register it in Google Agent Registry.

2. [Create PingOne Authorize policies](#create-policies) that decide whether the Agent Gateway Service Extension permits agent requests to the MCP server.

3. [Deploy the Agent Gateway Service Extension](#deploy-extension-service) to Cloud Run.

4. [Create the Agent Gateway](#create-gateway) and attach the Service Extension to it.

5. [Deploy the agent](#deploy-agent) and create a PingOne resource that licenses the Agent Gateway Service Extension as the only actor allowed to exchange tokens bound for the Agent Gateway.

6. [Deploy the Agent Bridge](#deploy-bridge) to Cloud Run.

7. [Deploy the Chat UI](#deploy-chat-ui) to Cloud Run.

## Before you begin

In addition to meeting the prerequisites in the [integration overview](idai-integrating-gemini-agent-platform-with-ping.html#idai-gemini-prereqs), ensure you have a Stripe account with products and customers configured. Learn more in [Set up your account](https://docs.stripe.com/get-started/account/set-up) in the Stripe documentation.

## Tasks

You can find implementation files and code samples for this use case in the [Agent On-Behalf-Of User](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-on-behalf-of-user) GitHub repository.

### Deploy the Stripe MCP Server

The [Stripe MCP Server](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-on-behalf-of-user/services/stripe-mcp-server) exposes Stripe tools to an agent.

On every request, it:

* Validates the `iss`, `aud`, `scope`, and `signature` claims of the inbound token injected by the Agent Gateway Service Extension.

* Reads the caller's email from the `X-User-Email` header injected by the Agent Gateway Service Extension.

* Executes Stripe operations on behalf of that user.

You'll configure Stripe, deploy the MCP Server to Cloud Run, register it in Agent Registry, and configure a matching resource in PingOne to ensure every token issued for tool access carries claims that prove delegation.

> **Collapse: Configure Stripe**
>
> In the Stripe Dashboard, create the products and customers the agent operates on. Each customer must have a saved payment method attached to their account so that the `create_stripe_payment_intent` tool can charge them without requiring card details at runtime.
>
> |   |                                                                      |
> | - | -------------------------------------------------------------------- |
> |   | The customer email in Stripe must match the user's email in PingOne. |

> **Collapse: Create the MCP server resource in PingOne**
>
> Add a custom resource in PingOne that represents the Stripe MCP Server the agent is allowed to access.
>
> Two grant types are used to request tokens for this resource: the Agent Gateway Service Extension's `client_credentials` grant (which has no subject or actor) and the token exchange grant, where the subject token carries the user's identity. You'll configure three attributes with attribute mappings to ensure each grant yields the correct claims:
>
> * `sub`: Stamps `no-subject` on the `client-credentials` grant. On a token exchange, it carries the subject token's `sub` through, so the user's identity is preserved all the way to the Stripe MCP Server.
>
> * `act`: Stamps `noActor` on the `client-credentials` grant. On a token exchange, `act` is set only if the subject token's `may_act` claim names the exchanging actor. Otherwise it returns `null`, and because `act` is required, a `null` fails the exchange. This enforces the security boundary that only the agent can exchange a user token onto this resource.
>
> |   |                                                                                                                                                                             |
> | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can find more details about [adding custom resources](https://docs.pingidentity.com/pingone/applications/p1_adding_custom_resources.html) in the PingOne documentation. |
>
> 1. In the PingOne admin console, go to **Applications > Resources** and click the **[icon: plus, set=fa]**icon.
>
> 2. Define the resource:
>
>    1. **Resource Name**: `AOBOU Stripe MCP Server`
>
>    2. **Audience**: `stripe-mcp-server`
>
> 3. Click **Next**.
>
> 4. Define attributes for the resource:
>
>    Detailed steps follow the table.
>
>    | Attribute    | Required | Expression                                                                                                                                                                                                                                                                                                |
>    | ------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>    | `sub`        | No       | ```spel
>    (#root.context.requestData.grantType == "client_credentials") ? "no-subject" : #root.context.requestData.subjectToken.sub
>    ```                                                                                                                                                                     |
>    | `act`        | Yes      | ```spel
>    (#root.context.requestData.grantType == "client_credentials")?"noActor":((#root.context.requestData.subjectToken.may_act.sub == #root.context.requestData.actorToken.client_id)?{"sub":#root.context.requestData.actorToken.client_id,"act":#root.context.requestData.subjectToken.act}:null)
>    ``` |
>    | `grant_type` | No       | ```spel
>    #root.context.requestData.grantType
>    ```                                                                                                                                                                                                                                                           |
>
>    1. Click the **Gear** icon ([icon: gear, set=fa]) next to the `sub` attribute, enter the expression, and click **Save**.
>
>       Learn more about expressions in [Using the expression builder](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_use_expression_builder.html) in the PingOne documentation.
>
>    2. Click **+ Add** and name the attribute `act`.
>
>    3. Click [icon: gear, set=fa], enter the expression, and click **Save**.
>
>    4. Select the **Required** checkbox for the `act` attribute.
>
>       This ensures that any token exchange that fails to set `act` is rejected.
>
>    5. Click **+ Add** and name the attribute `grant_type`.
>
>    6. Click [icon: gear, set=fa], enter the expression, and click **Save**.
>
> 5. Click **Next**, then click **+ Add Scope**.
>
> 6. Name the scope `stripe_mcp:invoke`.
>
> 7. Click **Save**.

> **Collapse: Deploy the MCP server to Cloud Run**
>
> Build the MCP server with configured environment variables and deploy it as a Cloud Run service.
>
> 1. Set environment variables for the MCP server:
>
>    1. In the cloned Gemini Enterprise Agent Platform Integrations repository, go to the `pingone/agent-on-behalf-of-user/services/stripe-mcp-server` directory.
>
>    2. Make a copy of the `.env.sample` file and name it `.env`:
>
>       ```bash
>       cp .env.sample .env
>       ```
>
>    3. Set environment variables in the `.env` file:
>
>       | Variable                    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
>       | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       | `GC_REGION`                 | Your Google Cloud Platform region. For example: `us-central1`.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
>       | `GC_CLOUD_RUN_SERVICE_NAME` | The Cloud Run service name: `` aobou-stripe-mcp-server` ``.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
>       | `IDP_ISSUER`                | The PingOne issuer URL: `[.userinput]`https\://auth.pingone.\<region>/\<env-id>/as\`\`.Set the placeholders:- \<region>: The country code top-level domain (ccTLD), such as `.com`, `.eu`, `.asia`. You can find this in your PingOne admin console URL. For example:" `https://console.pingone.com/index.html?env=12345678-1234-1234-1234-123456789012` has a ccTLD of `.com`.
>
>       - \<env-id>: The PingOne environment ID. In the example PingOne admin console URL, the ID is `12345678-1234-1234-1234-123456789012`. |
>       | `STRIPE_SECRET_KEY`         | The Stripe secret key. To find this value, in the Stripe Dashboard, go to **Developers > API keys** and copy the value of the **Secret key** field.                                                                                                                                                                                                                                                                                                                                                                   |
>       | `IDP_REQUIRED_AUDIENCE`     | The expected `aud` claim. This matches the audience you gave the Stripe MCP Server resource in PingOne: `stripe-mcp-server`.                                                                                                                                                                                                                                                                                                                                                                                          |
>       | `IDP_REQUIRED_SCOPE`        | The scope the inbound token must carry to invoke the Stripe MCP Server: `stripe_mcp:invoke`.                                                                                                                                                                                                                                                                                                                                                                                                                          |
>
> 2. In the `pingone/agent-on-behalf-of-user/services/stripe-mcp-server` directory, run the following command:
>
>    ```bash
>    make deploy
>    ```
>
>    This builds the Docker image, pushes it to Google Container Registry, and deploys it to Cloud Run.

> **Collapse: Register the MCP server in Agent Registry**
>
> Register the MCP server in Agent Registry so the Agent Gateway recognizes it as an approved egress destination.
>
> 1. In Google Cloud, go to **Agent Platform > Agents > Govern > Agent Registry** and click **Add MCP Server**.
>
> 2. Enter the following values:
>
>    * **Name**: `AOBOU Stripe MCP Server`
>
>    * **Description**: `Stripe MCP Server for Agent On-Behalf-Of User demo`
>
> 3. Select your **Region**. For example: `us-central1`.
>
> 4. Enter the MCP server URL:
>
>    1. To find the URL, duplicate the browser tab and go to **Cloud Run > Services**. Click the **aobou-stripe-mcp-server service**. Copy the URL at the top of the page. For example: `https://aobou-stripe-mcp-server-909399354423.us-central1.run.app`.
>
>    2. In the Agent Registry, paste the URL in the **MCP server URL** field and then add `/mcp` to the end of the URL.
>
> 5. Enter the MCP specification JSON. This is the tool specification that describes the MCP server's endpoints and expected request and response formats.
>
>    1. In the `pingone/agent-on-behalf-of-user/services/stripe-mcp-server` directory in the cloned repository, copy the contents of the `tool-spec.json` file.
>
>    2. In the Agent Registry, paste the contents of the `tool-spec.json` file in the **JSON** field, then click **Next**.
>
>       |   |                                                                                                                                                                           |
>       | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       |   | Keep `tool-spec.json` in sync with the `mcp.NewTool` definitions in `mcp_tools.go`. If the definitions change, update `tool-spec.json` and re-register in Agent Registry. |
>
> 6. Click **Save** to complete the registration.

> **Collapse: Create a Stripe customers group in PingOne**
>
> 1. In the PingOne admin console, go to **Directory > Groups** and click the **[icon: plus, set=fa]**icon.
>
> 2. In the **Name** field, enter `stripe_customers`, and then click **Save**.
>
> 3. In the **Users** tab, click **Add Individually**.
>
> 4. Select any PingOne users who have a matching customer email in Stripe, and then click **Save**.

### Create the policies in PingOne Authorize

Create the policies that decide whether the Agent Gateway Service Extension permits the agent's request to the MCP Server. You'll create a policy for the agent's identity, one for the user's group membership, and one for the purchase amount.

> **Collapse: Add attributes in the Trust Framework**
>
> Add the following attributes that will be used to make a decision.
>
> | Name            | Type   | Resolver Parameter |
> | --------------- | ------ | ------------------ |
> | Agent Client ID | String | agent_client_id    |
> | User Sub        | String | user_sub           |
> | Tool Name       | String | tool_name          |
> | Amount Cents    | Number | amount_cents       |
>
> 1. In the PingOne admin console, go to **Authorization > Trust Framework**.
>
> 2. On the **Attributes** tab, click the **[icon: plus, set=fa]**icon.
>
> 3. Name the attribute `Agent Client ID`.
>
> 4. In the **Resolvers** section, click **[icon: plus, set=fa]Add Resolver** and keep the default **Request Parameter** resolver.
>
> 5. **Optional:** Name the resolver `agent_client_id` to match the parameter name in the agent's request.
>
> 6. For the Value Settings **Type**, keep the default value of **String**.
>
> 7. Click **Save Changes**.
>
> 8. Repeat the steps above to add the `User Sub`, `Tool Name`, and `Amount Cents` attributes, with the corresponding value settings types and optional resolver parameters.

> **Collapse: Create the AOBOU Agent Gateway Policies policy set**
>
> Add a policy set in PingOne Authorize that contains the policies governing the agent's access to the MCP server.
>
> 1. In the PingOne admin console, go to **Authorization > Policies**.
>
> 2. Click the **[icon: plus, set=fa]**icon and select **Add Policy Set**.
>
> 3. Name the policy set `AOBOU Agent Gateway Policies`.
>
> 4. For the **Combining Algorithm**, select **Unless one decision is deny, the decision will be permit**.
>
> 5. Click **Save changes**.

> **Collapse: Create the Only Permit Delegated Agent policy**
>
> Create a policy that permits only the delegated agent to access the MCP server.
>
> 1. In **Authorization > Policies**, select the **AOBOU Agent Gateway Policies** policy set.
>
> 2. Click the **[icon: plus, set=fa]**icon and select **Add Policy**.
>
> 3. Name the policy `Only Permit Delegated Agent`.
>
> 4. In **Applies When**:
>
>    1. Click **+ Comparison** and select the **Agent Client ID** attribute.
>
>    2. Select the **Does Not Equal** operator.
>
>    3. []()For the value, enter this placeholder: `<FINANCE_AGENT_CLIENT_ID>`.
>
>       Later, you'll replace this with the client ID of the agent you want to permit.
>
> 5. For the **Combining Algorithm**, select **Unless one decision is deny, the decision will be permit**.
>
> 6. Click **+ Add Rule**, then for **Effect**, select **Deny**.
>
> 7. Click **Save changes**.

> **Collapse: Create the Only Permit Users in Stripe Group policy**
>
> Create a policy that permits only users in the `stripe_customers` group to access the MCP server.
>
> 1. In **Authorization > Policies**, select the **AOBOU Agent Gateway Policies** policy set.
>
> 2. Click the **[icon: plus, set=fa]**icon and select **Add Policy**.
>
> 3. Name the policy `Only Allow Stripe Group`.
>
> 4. In **Applies When**:
>
>    1. Click **+ Comparison** and select the **User Sub** attribute.
>
>    2. Select the **Is Not Member Of** operator.
>
>    3. For the value, enter `stripe_customers`.
>
> 5. For the **Combining Algorithm**, select **Unless one decision is deny, the decision will be permit**.
>
> 6. Click **+ Add Rule**, then for **Effect**, select **Deny**.
>
> 7. Click **Save changes**.

> **Collapse: Create the Only Permit Stripe Purchases Below $100 policy**
>
> Create a policy that permits only purchases below $100 (10,000 cents) to access the MCP server.
>
> 1. In **Authorization > Policies**, select the **AOBOU Agent Gateway Policies** policy set.
>
> 2. Click the **[icon: plus, set=fa]**icon and select **Add Policy**.
>
> 3. Name the policy `Only Permit Stripe Purchases Below $100`.
>
> 4. In **Applies When**:
>
>    1. Click **+ Comparison** and select the **Tool Name** attribute.
>
>    2. Select the **Equals** operator.
>
>    3. For the value, enter `create_stripe_payment_intent`.
>
>    4. Click **+ Comparison** and select the **Amount Cents** attribute.
>
>    5. Select the **Greater Than** operator.
>
>    6. For the value, enter `10000`.
>
> 5. For the **Combining Algorithm**, select **Unless one decision is deny, the decision will be permit**.
>
> 6. Click **+ Add Rule**, then for **Effect**, select **Deny**.
>
> 7. Click **Save changes**.

> **Collapse: Publish an authorization policy version**
>
> Publish a policy version to deploy your policies to a decision endpoint and make them available for decision evaluations.
>
> 1. In the PingOne admin console, go to **Authorization > Version History**.
>
> 2. Click the **More Options (⋮)** icon next to the **Latest Version** and select **Publish Version**.
>
> 3. In the **Publish to** list, select a decision endpoint.
>
> 4. For the version **Name**, enter `AOBOU`.
>
> 5. Click **Publish**.
>
>    The version name and the endpoint the version is published to are displayed in **Version History**.
>
> 6. Go to **Authorization > Decision Endpoints** and expand the decision endpoint where you published the policy version. Copy the decision endpoint URL and save it somewhere convenient. You'll need it in the next task when you [deploy the Agent Gateway Service Extension](#authz-dec-endpoint).

### Deploy the Agent Gateway Service Extension

The [Agent Gateway Service Extension](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-on-behalf-of-user/services/agent-gateway-extension-service) is an Envoy `ext_proc` gRPC handler that the Agent Gateway calls to request authorization decisions and perform token exchanges.

You'll deploy the service to Cloud Run to govern requests bound for the Stripe MCP Server. During this flow, the service:

* Validates the agent's delegated token, specifically checking the `iss`, `aud`, and `scope` claims.

* Calls PingOne Authorize on `tools/call` requests to evaluate the agent's identity and the purchase amount. Non-invocation requests (`initialize`, `tools/list`) skip this authorization check.

* Upon a permit decision, performs a token exchange to generate a token restricted to the Stripe MCP Server (`aud`).

* Injects the new credential as an `Authorization: Bearer` header before forwarding the request to the Stripe MCP Server.

> **Collapse: Create a PingOne worker application**
>
> Create a PingOne worker application that the Agent Gateway Service Extension uses to call PingOne Authorize for authorization decisions.
>
> 1. In the PingOne admin console, go to **Applications > Applications**.
>
> 2. Click the **[icon: plus, set=fa]**icon and create the application profile:
>
>    1. Name the application `AOBOU PingOne Authorize Worker App`.
>
>    2. For the **Application Type**, click **Worker**.
>
>    3. Click **Save**.
>
> 3. To enable the application, click the toggle next to the application name in the details panel.
>
> 4. On the **Configuration** tab, click the Pencil icon ([icon: pencil, set=fa]), make sure **Client Credentials** is the **Grant Type**, then click **Cancel**.
>
> 5. On the **Roles** tab, click **Grant Roles**.
>
> 6. Expand the **Environment Admin** and **Identity Data Read Only** roles and select your environment for each.
>
> 7. Click **Save**.

> **Collapse: Create a PingOne application for token exchange**
>
> Create a PingOne application that the Agent Gateway Service Extension uses to perform token exchanges for the MCP server.
>
> 1. In the PingOne admin console, go to **Applications > Applications**.
>
> 2. Click the **[icon: plus, set=fa]**icon and create the application profile:
>
>    1. Name the application `AOBOU Agent Gateway Extension`.
>
>    2. For the **Application Type**, click **OIDC Web App**.
>
>    3. Click **Save**.
>
> 3. To enable the application, click the toggle next to the application name in the details panel.
>
> 4. On the **Configuration** tab, click [icon: pencil, set=fa].
>
>    1. For **Grant Type**, select **Client Credentials** and **Token Exchange**.
>
>    2. Clear the **Code** and **Authorization Code** checkboxes.
>
>    3. Click **Save**
>
> 5. On the **Resources** tab, click [icon: pencil, set=fa], then select the **stripe_mcp:invoke** scope on the AOBOU Stripe MCP Server.
>
>    This scope isn't available yet. Complete this step after you [deploy the Financial Agent](#deploy-agent).
>
> 6. Click **Save**.
>
> 7. On the **Overview** tab, copy the **Client ID** for this application and save it somewhere convenient. You'll need it later when you [create the Agent Gateway resource in PingOne](#create-gateway-resource).

> **Collapse: Deploy the Agent Gateway Service Extension to Cloud Run**
>
> Build the service with configured environment variables and deploy it as a Google Cloud Run service.
>
> 1. Set environment variables for the Agent Gateway Service Extension:
>
>    1. In the cloned repository, go to the `pingone/agent-on-behalf-of-user/services/agent-gateway-extension-service` directory.
>
>    2. Make a copy of the `.env.sample` file and name it `.env`:
>
>       ```bash
>       cp .env.sample .env
>       ```
>
>    3. Set environment variables in the `.env` file:
>
>       | Variable                      | Value                                                                                                                                                                                                                                                            |
>       | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       | `GC_REGION`                   | Your Google Cloud Platform region. For example: `us-central1`.                                                                                                                                                                                                   |
>       | `GC_SERVICE_EXTENSION_NAME`   | The name of the Service Extension resource created when this service is registered: `aobou-agent-gateway-extension`.                                                                                                                                             |
>       | `GC_CLOUD_RUN_SERVICE_NAME`   | The Cloud Run service name: `aobou-agent-gateway-extension-service`.                                                                                                                                                                                             |
>       | `IDP_ISSUER`                  | The AOBOU PingOne Authorize Worker App token endpoint: `https://auth.pingone.<region>/<env-id>/as`. Copy this from the **Connection Details > Issuer ID** field on the **Overview** tab of the AOBOU PingOne Authorize Worker App application in PingOne.        |
>       | `EXCHANGE_CLIENT_ID`          | Token-exchange worker app Client ID.                                                                                                                                                                                                                             |
>       | `EXCHANGE_CLIENT_SECRET`      | Token-exchange worker app Client Secret.                                                                                                                                                                                                                         |
>       | `AUTHZ_CLIENT_ID`             | Authorize worker app Client ID.                                                                                                                                                                                                                                  |
>       | `AUTHZ_CLIENT_SECRET`         | Authorize worker app Client Secret.                                                                                                                                                                                                                              |
>       | []()`AUTHZ_DECISION_ENDPOINT` | The PingOne Authorize decision endpoint URL from when you published the policy version in the previous task.                                                                                                                                                     |
>       | `IDP_REQUIRED_AUDIENCE`       | The expected `aud` on the inbound token from the gateway resource: `google-agent-gateway`.                                                                                                                                                                       |
>       | `IDP_REQUIRED_SCOPE`          | The scope the inbound token must carry to invoke the Stripe MCP Server: `stripe_mcp:invoke`.                                                                                                                                                                     |
>       | `TOOL_URL`                    | The MCP tool's Cloud Run base URL. To find this URL:1) Go to **Cloud Run > Services** and click the `aobou-stripe-mcp-server` service.
>
>       2) Copy the URL at the top of the page (for example `https://aobou-stripe-mcp-server-909399354427.us-central1.run.app`). |
>       | `TOOL_SCOPE`                  | The scope requested on the outbound tool token: `stripe_mcp:invoke`.                                                                                                                                                                                             |
>
> 2. In the `pingone/agent-on-behalf-of-user/services/agent-gateway-extension-service` directory, run the following commands:
>
>    ```bash
>    make deploy
>    ```
>
>    This builds the Docker image, pushes it to Google Container Registry, and deploys it to Cloud Run.
>
>    ```bash
>    make register
>    ```
>
>    This registers your deployed Cloud Run service as an available service extension in Google Cloud. Behind the scenes, it renders the `service-extension.tmpl.yaml` template with the live Cloud Run URL and imports the configuration, preparing the extension for use by the Agent Gateway.

### Create the Agent Gateway

The [Agent Gateway](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-on-behalf-of-user/services/agent-gateway) is a Google-managed resource that acts as the policy enforcement point for all agent egress traffic. It intercepts all outbound traffic bound for downstream tools and routes it to the Agent Gateway Service Extension.

You'll configure the gateway to call the Agent Gateway Service Extension, using [Envoy external processing](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_proc_filter) (`ext_proc`), on every request to the Stripe MCP Server. This includes attaching the Agent Gateway Service Extension to the gateway, registering the egress destinations it can reach, and creating the PingOne resource that licenses the Agent Gateway Service Extension as the only actor allowed to exchange tokens bound for the gateway.

> **Collapse: Configure environment variables**
>
> 1. In the cloned Gemini Enterprise Agent Platform Integrations repository, go to the `pingone/agent-on-behalf-of-user/services/agent-gateway` directory.
>
> 2. Make a copy of the `.env.sample` file and name it `.env`:
>
>    ```bash
>    cp .env.sample .env
>    ```
>
> 3. Check the environment variables in the `.env` file. Most are already defined.
>
>    | Variable                    | Value                                                                                                                                               |
>    | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
>    | `GC_REGION`                 | Your Google Cloud Platform region. For example: `us-central1`.                                                                                      |
>    | `GC_GATEWAY_NAME`           | The Agent Gateway's name. For example: `aobou-agent-gateway`.                                                                                       |
>    | `GC_SERVICE_EXTENSION_NAME` | The deployed Agent Gateway Service Extension name, created when the service extension was registered. For example: `aobou-agent-gateway-extension`. |
>    | `GC_AUTHZ_POLICY_NAME`      | Name of the policy resource this creates. For example: `aobou-authz-policy`.                                                                        |

> **Collapse: Create the Agent Gateway in the Google Cloud Console**
>
> Create the Egress Agent Gateway in the Google Cloud Console.
>
> 1. In Google Cloud, go to **Agent Platform > Agents > Govern > Gateways** and click **Add gateway**.
>
> 2. Enter the following values:
>
>    * **Name**: Name the gateway `aobou-agent-gateway`.
>
>    * **Region**: Your Google Cloud Platform region. For example: `us-central1`.
>
>    * **Deployment mode**: Keep the default **Google-managed**.
>
>    * **Governed Access Path**: Keep the default **Agent-to-Anywhere (egress)**.
>
>    * **Access Authorization**: Select **Enforce policies**.
>
>    * **Policy Model**: Select **Allow Policy**.
>
> 3. Click **Save gateway**.

> **Collapse: Attach the Agent Gateway Service Extension to the Agent Gateway**
>
> To enforce your access policies, you must connect the Agent Gateway Service Extension to the Agent Gateway. The `make attach` command populates `authz-policy.tmpl.yaml` with your project, region, and gateway name, and then imports it with `gcloud`, creating an authorization policy that binds the extension to the gateway as a `CONTENT_AUTHZ` policy scoped to the `/mcp` path.
>
> In the `pingone/agent-on-behalf-of-user/services/agent-gateway` directory, run the following command:
>
> ```bash
> make attach
> ```
>
> |   |                                                                                  |
> | - | -------------------------------------------------------------------------------- |
> |   | You can run `make render` alone to inspect the generated YAML without importing. |
>
> There are now two complementary authorization extensions attached to the Agent Gateway:
>
> | Extension                                | Service role    | Target                      | Description                                                                                                                                                                                                                                                          |
> | ---------------------------------------- | --------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `aobou-agent-gateway-iap-authzextension` | `REQUEST_AUTHZ` | `iap.googleapis.com`        | A Google-managed extension automatically created with the gateway. It enforces the Identity-Aware Proxy (IAP) identity and egress check (`iap.egressor`), which appears on the gateway as the **Auth provider: Google Cloud Identity-Aware Proxy**.                  |
> | `aobou-agent-gateway-extension`          | `CONTENT_AUTHZ` | Cloud Run service extension | The extension created in the previous step. It routes traffic to your Cloud Run host and requests an authorization decision. Upon permit, the extension performs the PingOne token exchange and injects the resulting delegated token in the `Authorization` header. |

> **Collapse: Register egress destinations for the Agent Gateway**
>
> The gateway governs all agent egress, so every host the agent reaches must be a registered destination in Agent Registry. Your environment currently includes the following registered destinations:
>
> * **Stripe MCP Server:** This was registered as an MCP server (rather than a standard endpoint) when you deployed it.
>
>   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
>   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | The registered URL must match the host URL invoked by the agent exactly. Because IAP resolves egress destinations by host name, any mismatch causes IAP to block the request before it ever reaches the service extension. For example, a failure occurs if the registry holds the stable Cloud Run URL (`…​-<project-number>.<region>.run.app`), but the agent calls a direct revision URL (`…​-<hash>-<region>.a.run.app`). If this happens, you'll see a `DENIED` entry in the gateway logs with no `agentRegistryResource`. |
>
> * **Google APIs:** Endpoints for `aiplatform`, `iamcredentials`, and telemetry (`*.mtls.googleapis.com`) were automatically generated during the gateway deployment to support the runtime's internal egress. Don't modify these endpoints.
>
> You'll register the PingOne host as the final required egress endpoint.
>
> |   |                                                                                                                                                                              |
> | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | If you completed xref:integrations:idai-authorizing-gemini-autonomous-agents-with-ping.adoc, you already registered the PingOne host as an endpoint. You can skip this task. |
>
> 1. In Google Cloud, go to **Agent Platform > Agents > Govern > Agent Registry** and click **Add Endpoint**.
>
> 2. Enter the following values:
>
>    * **Name**: `PingOne`.
>
>    * **Region**: Your Google Cloud Platform region. For example: `us-central1`.
>
>    * **Destination URL**: Your PingOne host. For example: `https://auth.pingone.com`.
>
> 3. Click **Save**.

> **Collapse: Create the Agent Gateway resource in PingOne**
>
> Add a custom resource in PingOne that represents the Agent Gateway.
>
> In addition to configuring the `sub`, `act`, and `grant_type` attributes, you'll configure the `may_act` attribute to license the Agent Gateway Service Extension as the next actor on every token minted for this resource. Any other client presenting an exchanged token fails the tool resource's `act` check.
>
> |   |                                                                                                                   |
> | - | ----------------------------------------------------------------------------------------------------------------- |
> |   | Set the `may_act` value to the client ID of the AOBOU Agent Gateway Extension application you created in PingOne. |
>
> 1. In the PingOne admin console, go to **Applications > Resources** and click the **[icon: plus, set=fa]**icon.
>
> 2. Define the resource:
>
>    1. **Resource Name**: `AOBOU Google Cloud Agent Gateway`
>
>    2. **Audience**: `google-agent-gateway`
>
> 3. Click **Next**.
>
> 4. Define attributes for the resource:
>
>    Detailed steps follow the table.
>
>    | Attribute    | Required | Expression                                                                                                                                                                                                                                                                                                |
>    | ------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>    | `sub`        | No       | ```spel
>    (#root.context.requestData.grantType == "client_credentials") ? "no-subject" : #root.context.requestData.subjectToken.sub
>    ```                                                                                                                                                                     |
>    | `act`        | Yes      | ```spel
>    (#root.context.requestData.grantType == "client_credentials")?"noActor":((#root.context.requestData.subjectToken.may_act.sub == #root.context.requestData.actorToken.client_id)?{"sub":#root.context.requestData.actorToken.client_id,"act":#root.context.requestData.subjectToken.act}:null)
>    ``` |
>    | `may_act`    | No       | ```spel
>    {"sub":"<GATEWAY_SERVICE_EXT_CLIENT_ID>"}
>    ```                                                                                                                                                                                                                                                     |
>    | `grant_type` | No       | ```spel
>    #root.context.requestData.grantType
>    ```                                                                                                                                                                                                                                                           |
>
>    1. Click the **Gear** icon ([icon: gear, set=fa]) next to the `sub` attribute, enter the expression, and click **Save**.
>
>       |   |                                                                                                                                                                           |
>       | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       |   | Leave the **Required** checkbox cleared. If marked required, standard `client_credentials` requests are rejected by PingOne before the attribute expression is evaluated. |
>
>       Learn more about expressions in [Using the expression builder](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_use_expression_builder.html) in the PingOne documentation.
>
>    2. Click **+ Add** and name the attribute `act`.
>
>    3. Click [icon: gear, set=fa], enter the expression, and click **Save**.
>
>    4. Select the **Required** checkbox for the `act` attribute.
>
>       This ensures that any token exchange that fails to set `act` is rejected. Unauthorized requests evaluate to null and explicitly fail.
>
>    5. Click **+ Add** and name the attribute `may_act`.
>
>    6. Click [icon: gear, set=fa], enter the expression, replace the `<GATEWAY_SERVICE_EXT_CLIENT_ID>` placeholder with the Agent Gateway Service Extension application's **Client ID** in PingOne that you created in the [previous task](#create-pingone-service-ext-app), and click **Save**.
>
>    7. Repeat the steps to configure the `grant_type` attribute with its respective values.
>
> 5. Click **Next**, then click **+ Add Scope**.
>
> 6. Name the scope `stripe_mcp:invoke`.
>
> 7. Click **Save**.

### Deploy the Financial Agent

The [Financial Agent](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-on-behalf-of-user/services/agent) is an ADK-based agent deployed to the Google Cloud Agent Runtime. Operating as an MCP client, it connects to the Stripe MCP Server to execute the `stripe_mcp:invoke` tool.

You'll create an identity for the agent in PingOne and deploy the agent to the Agent Runtime, binding it to the Agent Gateway.

> **Collapse: Create the Financial Agent in PingOne**
>
> 1. In the PingOne admin console, go to **AI Agents** and click the **[icon: plus, set=fa]**icon.
>
> 2. In the **Name** field, enter `AOBOU Financial Agent`.
>
> 3. Click **Save**.
>
> 4. To enable the application, click the toggle next to the application name in the details panel.
>
> 5. On the **Configuration** tab, click [icon: pencil, set=fa]:
>
>    1. For **Grant Type**, select **Token Exchange** and **Client Credentials**.
>
>    2. Clear the **Code** check box.
>
>    3. Click **Save**.
>
> 6. On the **Resources** tab, click [icon: pencil, set=fa], then select the **stripe_mcp:invoke** scope on the AOBOU Google Cloud Agent Gateway.
>
> 7. Click **Save**.
>
> 8. On the **Overview** tab, copy the **Client ID** for this agent and save it somewhere convenient. You'll need it in the next step when you [create the Financial Agent resource in PingOne](#create-financial-agent-resource).

> **Collapse: Create the Financial Agent resource in PingOne**
>
> Create a custom resource in PingOne to represent the Financial Agent.
>
> This resource mints the Chat UI's sign-on token, the user identity that enters the delegation chain at hop 1. Only the `authorization_code` grant type requests tokens from this resource at login, so you'll just configure the **may_act** attribute.
>
> 1. In the PingOne admin console, go to **Applications > Resources** and click the **[icon: plus, set=fa]**icon.
>
> 2. Define the resource:
>
>    1. **Resource Name**: `AOBOU Financial Agent`
>
>    2. **Audience**: `finance-agent`
>
> 3. Click **Next**.
>
> 4. Define an attribute for the resource:
>
>    | Attribute | Required | Expression                              |
>    | --------- | -------- | --------------------------------------- |
>    | `may_act` | No       | ```spel
>    {"sub":"<AGENT_CLIENT_ID>"}
>    ``` |
>
>    1. Click **+ Add** and name the attribute `may_act`.
>
>    2. Click [icon: gear, set=fa], enter the expression, replace the `<AGENT_CLIENT_ID>` placeholder with the Financial Agent application's **Client ID** in PingOne that you created in the [previous step](#create-financial-agent-pingone-app), and click **Save**.
>
>       Learn more about expressions in [Using the expression builder](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_use_expression_builder.html) in the PingOne documentation.
>
> 5. Click **Next**, then click **+ Add Scope**.
>
> 6. Name the scope `stripe_mcp:invoke`.
>
>    The Financial Agent requests this scope when it exchanges the user's sign-on token during token exchange.
>
> 7. Click **Save**.

> **Collapse: Deploy and register the agent in Agent Registry**
>
> To finish the agent setup, deploy it to the Google Cloud Agent Runtime. This deployment automatically registers the agent in the Agent Registry and routes all of its egress traffic through the Agent Gateway.
>
> 1. Set environment variables for the agent:
>
>    1. In the cloned Gemini Enterprise Agent Platform Integrations repository, go to the `pingone/agent-on-behalf-of-user/services/agent` directory.
>
>    2. Make a copy of the `.env.sample` file and name it `.env`:
>
>       ```bash
>       cp .env.sample .env
>       ```
>
>    3. Set environment variables in the `.env` file:
>
>       | Variable              | Value                                                                                                                                                                                                                                                                                                                             |
>       | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       | `GC_REGION`           | Your Google Cloud Platform region. For example: `us-central1`.                                                                                                                                                                                                                                                                    |
>       | `AGENT_DISPLAY_NAME`  | Display name for the Reasoning Engine: `aobou-financial-agent`.                                                                                                                                                                                                                                                                   |
>       | `IDP_ISSUER`          | The PingOne issuer URL: `https://auth.pingone.<region>/<env-id>/as`.To find this endpoint, go to the AOBOU Financial Agent in PingOne. Copy the **Issuer ID** under **Connection Details** on the **Overview** tab.                                                                                                               |
>       | `GC_AGENT_GATEWAY`    | Display name for the Agent Gateway: `aobou-agent-gateway`.                                                                                                                                                                                                                                                                        |
>       | `GATEWAY_AUDIENCE`    | Audience that the Agent Gateway Service Extension expects: `google-agent-gateway`.                                                                                                                                                                                                                                                |
>       | `AGENT_CLIENT_ID`     | The AOBOU Financial Agent's **Client ID**. This is located above **Connection Details** on the agent's **Overview** tab in PingOne.                                                                                                                                                                                               |
>       | `AGENT_CLIENT_SECRET` | The AOBOU Financial Agent's **Client Secret**. This is located above **Connection Details** on the agent's **Overview** tab.                                                                                                                                                                                                      |
>       | `TOOL_MCP_URL`        | The MCP tool's Cloud Run base URL. To find this URL:1) Go to **Cloud Run > Services** and click the **aobou-stripe-mcp-server** service.
>
>       2) Copy the URL at the top of the page (for example: `https://aobou-stripe-mcp-tool-909399354453.us-central1.run.app`).
>
>       3) Paste the URL in the `.env` file and add `/mcp` at the end. |
>       | `TOOL_SCOPE`          | The scope the agent requests during token exchange to authorize access to the downstream MCP server: `stripe_mcp:invoke`.                                                                                                                                                                                                         |
>
> 2. In the `pingone/agent-on-behalf-of-user/services/agent` directory, run the following command:
>
>    ```bash
>    make deploy
>    ```
>
>    The `deploy.py` script provisions the Reasoning Engine using `identity_type = AGENT_IDENTITY`. The script also binds the engine to the gateway and grants it the `roles/iap.egressor` role on the Agent Registry, authorizing the agent to securely reach all registered downstream endpoints.
>
> 3. Complete the Financial Agent's `AGENT_ENGINE_ID` placeholder in the service extension's `.env` file, then redeploy the service extension.
>
> 4. In PingOne, go to the Agent Gateway Service Extension application and assign the `stripe_mcp:invoke` scope on the Financial Agent.

### Deploy the Agent Bridge

The [Agent Bridge](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-on-behalf-of-user/services/agent-bridge) links the PingOne identity of the Chat UI with the Google Agent Runtime identity of the agent. It receives each chat request, validates the user's PingOne token, creates the agent session, and stores the token in the session state where the agent reads it.

> **Collapse: Deploy the Agent Bridge to Cloud Run**
>
> Build the Agent Bridge with configured environment variables and deploy it as a Google Cloud Run service.
>
> 1. Set environment variables for the Agent Bridge:
>
>    1. In the cloned repository, go to the `pingone/agent-on-behalf-of-user/services/agent-bridge` directory.
>
>    2. Make a copy of the `.env.sample` file and name it `.env`:
>
>       ```bash
>       cp .env.sample .env
>       ```
>
>    3. Set environment variables in the `.env` file:
>
>       | Variable                    | Value                                                                                                                                                                                                                                                      |
>       | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       | `GC_REGION`                 | Your Google Cloud Platform region. For example: `us-central1`.                                                                                                                                                                                             |
>       | `GC_CLOUD_RUN_SERVICE_NAME` | The Cloud Run service name: `aobou-agent-bridge`.                                                                                                                                                                                                          |
>       | `IDP_ISSUER`                | The PingOne issuer URL: `https://auth.pingone.<region>/<env-id>/as`. Copy this from the **Connection Details > Issuer ID** field on the **Overview** tab of the AOBOU Financial Agent configuration in PingOne.                                            |
>       | `IDP_REQUIRED_AUDIENCE`     | The required audience for this resource: `finance-agent`.                                                                                                                                                                                                  |
>       | `CORS_ORIGIN`               | The Chat UI Cloud Run URL. For example: `https://aobou-chat-ui-<project-id>.<region>.run.app`.This is a placeholder. After you deploy the Chat UI in the next task, update this value with the actual URL, then redeploy the Agent Bridge.                 |
>       | `AGENT_ENGINE_ID`           | The Financial Agent's Reasoning Engine ID. To find this ID, go to **Agents > Agent Registry** in Google Agent Platform and copy the value following `reasoningEngines:` in the `aobou-financial-agent`'s **Agent ID**. For example: `6179839738431282994`. |
>
> 2. In the `pingone/agent-on-behalf-of-user/services/agent-bridge` directory, run the following command:
>
>    ```bash
>    make deploy
>    ```
>
>    This builds the Docker image, pushes it to Google Container Registry, and deploys it to Cloud Run.

### Deploy the Chat UI

The [Chat UI](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations/tree/main/pingone/agent-on-behalf-of-user/services/chat-ui) is a single-page application (SPA) built with React/Vite. End users authenticate with PingOne PKCE and chat with the Financial Agent through the Agent Bridge.

> **Collapse: Create the Chat UI application in PingOne**
>
> 1. In the PingOne admin console, go to **Applications > Applications**.
>
> 2. Click the **[icon: plus, set=fa]**icon and create the application profile:
>
>    1. Name the application `AOBOU Chat UI`.
>
>    2. For the **Application Type**, click **Single-Page**.
>
>    3. Click **Save**.
>
> 3. To enable the application, click the toggle next to the application name in the details panel.
>
> 4. On the **Configuration** tab, click [icon: pencil, set=fa]:
>
>    1. Make sure **Authorization Code** with **S256_REQUIRED** is the **Grant Type**.
>
>    2. In the **Redirect URIs** and **Signoff URLs** fields, enter your Chat UI URL from Cloud Run. For example: `https://aobou-chat-ui-PROJECT_ID.REGION.run.app`.
>
>       These are placeholders. After you [deploy the Chat UI to Cloud Run](#deploy-chat-ui-to-cloud-run) in the next step, update these values with the actual URL.
>
> 5. Click **Save**.
>
> 6. On the **Resources** tab, click [icon: pencil, set=fa], and select `stripe_mcp:invoke` on the AOBOU Financial Agent.
>
> 7. Click **Save**.

> **Collapse: Deploy the Chat UI to Cloud Run**
>
> Configure the environment variables required to deploy the Chat UI and connect it to the Agent Bridge.
>
> 1. Set environment variables for the Chat UI:
>
>    1. In the cloned repository, go to the `pingone/agent-on-behalf-of-user/services/chat-ui` directory.
>
>    2. Make a copy of the `.env.sample` file and name it `.env`:
>
>       ```bash
>       cp .env.sample .env
>       ```
>
>    3. Set environment variables in the `.env` file:
>
>       | Variable                    | Value                                                                                                                                                                                                                                                                                                                                                                                                                       |
>       | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       | `GC_REGION`                 | Your Google Cloud Platform region. For example: `us-central1`.                                                                                                                                                                                                                                                                                                                                                              |
>       | `GC_CLOUD_RUN_SERVICE_NAME` | The Cloud Run service name: `aobou-chat-ui`.                                                                                                                                                                                                                                                                                                                                                                                |
>       | `VITE_IDP_ISSUER`           | Your PingOne issuer: `https://auth.pingone.<region>/<env-id>/as`.To find this endpoint, go to the AOBOU Chat UI application in PingOne. Copy the **Issuer ID** under **Connection Details** on the **Overview** tab.                                                                                                                                                                                                        |
>       | `VITE_CLIENT_ID`            | The AOBOU Chat UI application's **Client ID**. This is located above **Connection Details** on the **Overview** tab.                                                                                                                                                                                                                                                                                                        |
>       | `VITE_REDIRECT_URI`         | Your Chat UI Cloud Run URL: `https://aobou-chat-ui-<project-id>.<region>.run.app`.After you deploy the Chat UI to Cloud Run, update this value with the actual URL. To find the URL, go to **Cloud Run > Services** and click the **aobou-chat-ui** service. Copy the URI at the top of the page.	This redirect URI must exactly match the Redirect URIs and Signoff URLs configured in the Chat UI application in PingOne. |
>       | `VITE_AGENT_BRIDGE_URL`     | Your Agent Bridge Cloud Run URL. For example: `https://aobou-agent-bridge-<project-id>.<region>.run.app`.                                                                                                                                                                                                                                                                                                                   |
>       | `VITE_SCOPES`               | Enter `openid profile email stripe_mcp:invoke`.                                                                                                                                                                                                                                                                                                                                                                             |
>
> 2. In the `pingone/agent-on-behalf-of-user/services/chat-ui` directory, run the following command:
>
>    ```bash
>    make deploy
>    ```
>
>    This builds the Vite app, packages it in a Docker image, and deploys it to Cloud Run.
>
> 3. Complete the Chat UI's `CORS_ORIGIN` placeholder in the Agent Bridge's `.env` file, then redeploy the Agent Bridge.
>
> 4. Complete the Chat UI's `VITE_REDIRECT_URI` placeholder in the Chat UI's `.env` file, then redeploy the Chat UI.
>
> 5. In the [Chat UI application in PingOne](#create-chat-ui-app-pingone), enter the deployed `aobou-chat-ui` service's Cloud Run URL in the **Redirect URIs** and **Signoff URLs** placeholders.
>
>    This ensures that the Chat UI can successfully redirect users back to the application after authentication.

## Validation

Use the Chat UI as an end user to make a purchase through Stripe.

1. Go to the Chat UI URL (https\://aobou-chat-ui-\<project-id>.\<region>.run.app) and click **Sign In**.

2. Authenticate as a PingOne user that has a matching email configured in Stripe.

3. Ask the agent to list the products and make a purchase.

4. Confirm the amount and payment method.

The transaction completes and a receipt email is sent.

You can observe the delegation by following the logs of the two Cloud Run services (`aobou-agent-gateway-extension-service` and `aobou-stripe-mcp-server`) while the chat runs. In order, you should see:

```text
# Extension service: every MCP request (initialize, tools/list, tools/call)
# is validated, exchanged, and forwarded with a fresh tool token.
[ExtSvc] request authority="aobou-stripe-mcp-server-...run.app" path="/mcp"
[ExtSvc] aobou-stripe-mcp-server-... /mcp — user=<user-sub> agent=<agent-client-id> email=alice@example.com
[ExtSvc] tool token minted (ttl 59m30s)
[ExtSvc] injecting tool token for aobou-stripe-mcp-server-...run.app

# Extension service: PingOne Authorize is consulted on tools/call only.
[ExtSvc] authorize user=<user-sub> agent=<agent-client-id> tool=create_stripe_payment_intent amount_cents=10000 hour=14
[ExtSvc] PingOne Authorize PERMIT user=<user-sub> agent=<agent-client-id>

# Stripe MCP server: every request's token is verified (signature, issuer,
# audience, scope) before handling. The log shows who the call is for (sub,
# the user throughout), which audience it was minted for (aud), who acted for
# it (act.sub, the extension service - the delegation proof), the granted
# scope, and the resolved caller email.
[SupplyChain] Token verified — sub=<user-sub> aud=[stripe-mcp-server] act.sub=<ext-svc-client-id> scope="stripe_mcp:invoke" caller=alice@example.com

# Stripe MCP server: the purchase itself runs only after the PERMIT above.
[SupplyChain] tool=create_stripe_payment_intent - caller=alice@example.com product_id=prod_... quantity=1 total_price=100.00
[SupplyChain] tool=create_stripe_payment_intent - success: caller=alice@example.com product_id=prod_... quantity=1
```

|   |                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `initialize` and `tools/list` requests are the agent and tool negotiating the tool schema. Only the final `tools/call` is routed through PingOne Authorize, which is why the `authorize` line appears once per purchase and not during browsing. |

## Troubleshooting

If you encounter issues while deploying or testing the agent, use the following information to help resolve common problems:

* Chat UI authentication fails

  Verify that the AOBOU Chat UI application in PingOne is configured with the Authorization Code grant type with PKCE. Additionally, check that the configured redirect URI exactly matches the URL of your deployed Cloud Run service.

* Chat UI configuration changes aren't applied after deployment

  If you update a `VITE_*` environment variable (such as `VITE_SCOPES`) but the deployed UI doesn't reflect the change, the Docker build cache probably reused a stale compilation layer. Rebuild and deploy the application using the `--no-cache` flag to force Vite to statically embed the new variables in the JavaScript bundle.

* Financial Agent doesn't receive the user token

  Verify that the Agent Bridge is correctly deployed to Cloud Run and that the Chat UI is successfully sending the token to the bridge payload during the initial chat request.

* Requests are blocked before they reach the service extension

  If the Agent Gateway returns a 403 Forbidden error or logs a `DENIED` message with no `agentRegistryResource`, the request is failing Google Cloud's IAP egress check.

  * Make sure the Reasoning Engine identity has the `roles/iap.egressor` role applied.

  * Verify that the downstream URL registered in Agent Registry exactly matches the host URL the agent is configured to call. IAP resolves egress destinations by host name, and a mismatch causes an immediate denial.

* Order Status Agent or MCP server doesn't receive the delegated token

  Confirm that the Agent Gateway Service Extension is correctly deployed and attached to the Agent Gateway. Check the service extension logs in Cloud Run to verify that it's successfully intercepting the request and performing the RFC 8693 token exchange for the target audience.

  If the Order Status MCP Server fails to receive the delegated token, check that the Agent Gateway Service Extension is correctly reminting the token for the MCP server and that the MCP server is correctly validating the token.

* Token validation or token exchange fails

  Verify that your PingOne resources are configured with the correct custom attributes.

  * Ensure the `may_act` claims are set to the client ID of the next permitted actor in the delegation chain.

  * If a token exchange fails with a 400 error during a `client_credentials` grant, verify that the **Required** checkbox is cleared for the `sub` attribute on the target PingOne resource.

* PingOne Authorize policies aren't enforced

  Make sure the PingOne Authorize decision endpoint URL is correctly configured in your service extension environment variables. In PingOne Authorize **Version History**, verify that your policies are published to the correct version.

* PingOne Authorize denies the agent's request

  * Verify that you replaced the \<FINANCE_AGENT_CLIENT_ID> [placeholder](#idai-gemini-aut-agent-id) in the Only Permit Delegated Agent policy with the client ID of the deployed Finance Agent. If this placeholder isn't updated, the policy can't identify the agent and will reject the request.

  * Review [Recent Decisions](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_recent_decisions.html) in PingOne Authorize to identify which policy condition caused the denial.

    |   |                                                                                                                                                                                                                           |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Enable **Record recent decisions** on your PingOne Authorize decision endpoint to view full request payloads and step-by-step policy evaluation results. This provides visibility into why a specific request was denied. |

## What's next

Learn how to [authorize Gemini Agent2Agent chains](idai-authorizing-gemini-agent2agent-with-ping.html).

|   |                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To prepare your environment for agent chaining, clean up the resources you deployed for agents on behalf of users. From the `pingone/agent-on-behalf-of-user` directory, run the `make destroy` command to safely remove the Google Cloud infrastructure specific to this use case. |

---

---
title: Integrating Gemini Enterprise Agent Platform with Ping Identity solutions
description: Introduction to Gemini Agent Platform integration with Ping Identity authorization solutions, including architecture and prerequisites.
component: identity-for-ai
page_id: identity-for-ai:integrations:idai-integrating-gemini-agent-platform-with-ping
canonical_url: https://developer.pingidentity.com/identity-for-ai/integrations/idai-integrating-gemini-agent-platform-with-ping.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-10-14T18:43:00Z
keywords: ["Identity for AI", "ai identity", "ai security", "Google Cloud Gemini Enterprise", "Gemini Enterprise Agent Platform", "PingOne Authorize", "authentication", "authorization"]
section_ids:
  authorization-scenarios: Authorization scenarios
  reference-architecture: Reference architecture
  technologies: Technologies
  idai-gemini-prereqs: Before you begin
  google-cloud-access-requirements: Google Cloud access requirements
  whats-next: What's next
---

# Integrating Gemini Enterprise Agent Platform with Ping Identity solutions

The Gemini Enterprise Agent Platform enables organizations to deploy and manage artificial intelligence (AI) agents. The platform provides tools and services for building and deploying AI agents, and managing their lifecycles.

Integrating Gemini Enterprise Agent Platform with Ping Identity's authorization solution, PingOne Authorize, transforms how your organization secures AI agents, shifting from simple network connectivity to dynamic runtime authorization. In this integration, Google Cloud Agent Gateway acts as a central enforcement point and PingOne Authorize acts as the decision point, authorizing agent actions in real time without relying on standing credentials.

Benefits of this integration include:

* Decoupled policy management

  A single authorization decision point governs all agent access (to MCP tools, external APIs, or other agents), enforcing read-only constraints and role-based policies, and eliminating the need to hard code business rules into every agent implementation or API integration.

* Continuous contextual authorization

  Static credentials alone can't stop over-privileged agents from accessing downstream tools. Instead, upon every request approved by PingOne Authorize, the gateway coordinates with PingOne to exchange the incoming credential for a narrowly scoped, short-lived token. By checking identity, delegation history, and policy at runtime, PingOne Authorize prevents compromised agents from using stolen tokens to reach downstream tools.

* End-to-end traceability

  Combining the gateway's trace IDs with Ping Identity's delegated identity model allows you to follow each request to see exactly which user was represented, which agent made the call, and which policy allowed or blocked the action.

## Authorization scenarios

This integration supports three primary authorization use cases based on the identity and delegation requirements of the agent and the downstream tool:

| Use case                                                                             | Scenario                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Autonomous agent to tool](idai-authorizing-gemini-autonomous-agents-with-ping.html) | An agent calls a supply chain MCP server using an agent-only identity. No user context is involved.                                                                                                |
| [Agent on behalf of user](idai-authorizing-gemini-on-behalf-of-users-with-ping.html) | A user invokes an agent that subsequently calls an MCP server. The user's identity is delegated directly through the agent.                                                                        |
| [Agent2Agent chaining](idai-authorizing-gemini-agent2agent-with-ping.html)           | A user interacts with a support agent that delegates to an order status agent. The order status agent subsequently calls an MCP server. The user's identity is delegated through the entire chain. |

## Reference architecture

Enforcing authorization policies on agents and MCP servers running on the Gemini Enterprise Agent Platform relies on a central gateway approach. In this architecture, the calling agent never holds a credential for the downstream agent or tool it calls. Instead, Google Cloud Agent Gateway uses a service extension to validate the inbound token and consult PingOne Authorize for a permit or deny decision. Upon a permit decision, the gateway performs a delegation token exchange, minting a narrowly scoped token before forwarding the request to an agent or MCP server.

![Diagram showing the Gemini reference architecture with an agent, Agent Gateway, Envoy service extension, and PingOne Authorize.](_images/idai-gemini-platform-architecture.png)

### Technologies

PingOne Authorize integrates into the Google Cloud Agent Gateway flow through a custom Envoy `ext_proc` service extension. The gateway streams each governed request to the extension, which validates the inbound token and requests an authorization decision from PingOne Authorize. Upon a permit decision, the extension exchanges the credential for a narrowly scoped, short-lived token before forwarding the request.

| Component                                                                                                                           | Role                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform)                                  | Google Cloud platform, which manages agent lifecycles.                                                                        |
| [Google Cloud Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) | Policy enforcement point that forwards agent requests to the service extension over the gRPC remote procedure call framework. |
| [Envoy external processing filter](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_proc_filter)     | Gateway mechanism that streams intercepted requests to the service extension over gRPC.                                       |
| [PingOne](https://docs.pingidentity.com/pingone/use_cases/p1_oauth_2_token_exchange_delegation.html)                                | Identity provider that authenticates agents and exchanges tokens with delegation.                                             |
| [PingOne Authorize](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_introduction.html)             | External policy decision point that evaluates authorization requests.                                                         |

## Before you begin

1. Ensure you have:

   * A Google Cloud project with billing enabled.

   * The Google Cloud CLI authenticated against the target project.

     You can find information about [installing the Google Cloud CLI](https://cloud.google.com/sdk/docs/install) in the Google Cloud documentation.

   * A PingOne environment with PingOne Authorize and the following roles:

     * Environment Admin

     * Application Admin

   * Docker installed and running on your local machine. Docker is used to build service images.

2. Clone the [Gemini Enterprise Agent Platform Integrations](https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations) repository to your local machine. For example:

   ```bash
   git clone https://github.com/pingidentity/gemini-enterprise-agent-platform-integrations.git
   ```

   This repository contains implementation files, code samples, and detailed instructions.

### Google Cloud access requirements

Google Cloud authentication requires credentials in three separate stores. You must authenticate all three stores, because an expired credential in any store causes deployment failures.

```bash
# Authenticate the gcloud CLI for deploy commands
gcloud auth login

# Authenticate Application Default Credentials (ADC) for the Python agent SDK
gcloud auth application-default login

# Authenticate Docker for pushing images (doesn't read the gcloud CLI sign-on)
gcloud auth configure-docker
```

You can deploy the solution from an Apple Silicon Mac without additional configuration. The Makefiles build for the `linux/amd64` platform, and the agent virtual environment targets Python 3.13.

|   |                                                                               |
| - | ----------------------------------------------------------------------------- |
|   | If you're using an earlier version of Python, run `brew install python@3.13`. |

To deploy the solution, your Google Cloud user account requires specific permissions beyond the basic `roles/editor` role:

| Role                                                 | Description                                                                           |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `roles/secretmanager.admin`                          | Allows the `make setup` command to add IAM policy bindings to the secrets it creates. |
| `roles/iap.admin`                                    | Grants the necessary egress permissions during the agent deployment.                  |
| `roles/run.admin` and `roles/iam.serviceAccountUser` | Allows the deployment of Cloud Run services and the attachment of service accounts.   |
| `roles/storage.admin`                                | Enables Docker image pushes and manages the staging bucket.                           |
| `roles/aiplatform.user`                              | Permits Reasoning Engine deployments and queries.                                     |

To grant these roles to a deploying user, run the following bash script:

```bash
for ROLE in roles/secretmanager.admin roles/iap.admin roles/run.admin \
            roles/iam.serviceAccountUser roles/storage.admin roles/aiplatform.user; do
  gcloud projects add-iam-policy-binding <PROJECT_ID> --member=user:<EMAIL> --role=$ROLE
done
```

## What's next

Learn how to [authorize autonomous Gemini agents](idai-authorizing-gemini-autonomous-agents-with-ping.html).

---

---
title: Securing a Cloudflare Workers MCP server with PingFederate
description: Configure a Cloudflare Workers Model Context Protocol (MCP) server that delegates authentication to PingFederate. This enables AI agents to call a protected API on behalf of an authenticated end user.
component: identity-for-ai
page_id: identity-for-ai:integrations:idai-securing-cloudflare-pingfed
canonical_url: https://developer.pingidentity.com/identity-for-ai/integrations/idai-securing-cloudflare-pingfed.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  how-does-it-work: How does it work?
  authentication-and-client-bootstrapping: Authentication and client bootstrapping
  cloudflare-agents-state-and-transport: Cloudflare agents (state and transport)
  mcp-sdk-tool-logic: MCP SDK (tool logic)
  before-you-begin: Before you begin
  tasks: Tasks
---

# Securing a Cloudflare Workers MCP server with PingFederate

Configure a Cloudflare Workers Model Context Protocol (MCP) server that delegates authentication to PingFederate. This enables AI agents to call a protected API on behalf of an authenticated end user.

The Cloudflare Workers Model Context Protocol (MCP) server functions as a resource server within the OAuth architecture. It validates incoming requests and facilitates token exchange, ensuring secure communication between the MCP client and downstream APIs.

This tutorial uses the `remote-mcp-ping-federate` directory in the Ping Identity [cloudflare-mcp Git repository](https://github.com/pingidentity/cloudflare-mcp/tree/main).

|   |                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This tutorial is designed to help you get started quickly. Although we have implemented several security controls, you must implement all preventive and defense-in-depth security measures before deploying to production. Learn more in [Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) in the MCP documentation. |

## How does it work?

This architecture bridges the stateless nature of Cloudflare Workers with the stateful requirements of an authenticated MCP session.

### Authentication and client bootstrapping

When an unregistered MCP client tries to connect to the MCP server without a token, the server provides the necessary details for the client to perform Dynamic Client Registration (DCR). This allows the client to handle the user login and consent with PingFederate automatically, provisioning the tokens required to both connect to the MCP server and for the MCP server to execute delegated token exchanges.

|   |                                                                                                                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This implementation utilizes DCR to handle client onboarding.Although the MCP protocol recommends Client ID Metadata Document (CIMD) as the new standard, DCR remains the only production-ready option currently supported by enterprise identity providers (IdPs) like PingFederate.Future versions of this architecture might transition to CIMD as support becomes available. |

### Cloudflare agents (state and transport)

The MCP server extends the `McpAgent` class, which automatically wraps the MCP logic in a durable object. This handles the following infrastructure requirements:

* Session persistence

  It creates a dedicated, isolated environment for each MCP connection and securely persists the PingFederate tokens in the durable object's storage (`this.props`).

* Network transport

  The agent manages the raw HTTP connection. It accepts incoming requests and keeps the response open as a Server-Sent Events (SSE) stream, enabling the durable object to push real-time updates back to the client over the single endpoint.

### MCP SDK (tool logic)

The official `@modelcontextprotocol/sdk` is used to define the actual capabilities of the MCP server. Inside the agent is an `McpServer` instance that manages the serialization of JSON-RPC messages and tool definitions.

## Before you begin

1. Deploy the [Todo API](https://github.com/pingidentity/cloudflare-mcp/tree/main/remote-mcp-ping-federate/api).

2. Deploy the [MCP server](https://github.com/pingidentity/cloudflare-mcp/tree/main/remote-mcp-ping-federate/mcp).

|   |                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can use any PingFederate-secured API. This tutorial uses a Cloudflare Workers API, but you can connect any API to an MCP server with this architecture. |

## Tasks

1. Access the remote MCP server from the Cloudflare Workers AI LLM Playground.

   1. Go to <https://playground.ai.cloudflare.com>.

   2. Connect to your MCP server using the following URL pattern:

      ```
      https://remote-mcp-ping-federate.<your-subdomain>.workers.dev/mcp
      ```

2. Access the remote MCP server from Claude Desktop.

   1. Open Claude Desktop and go to Settings > Developer > Edit Config.

      This opens the configuration file that controls which MCP servers Claude can access.

   2. Replace the content with the following configuration, and then save:

      ```
      {
        "mcpServers": {
          "todo-mcp": {
            "command": "npx",
            "args": [
              "mcp-remote",
              "https://remote-mcp-ping-federate.<ENV>.workers.dev/mcp"
            ]
          }
        }
      }
      ```

   3. Restart Claude Desktop.

      A browser window opens showing your OAuth sign-on page.

   4. Complete the authentication flow to grant Claude access to your MCP server.

      After granting access, the tools are available for you to use.

   5. You can ask Claude to use the tools that populate the **Tools** list. For example: "Can you tell me what is in my Todo list?"

      Claude invokes the tool and shows the result generated by the MCP server.

**Video (Brightcove)**

\<https\://players.brightcove.net/771836189001/default_default/index.html?videoId=6387820424112>

---

---
title: Securing a Cloudflare Workers MCP server with PingOne
description: Configure a Cloudflare Workers Model Context Protocol (MCP) server that uses the Cloudflare Workers OAuth Provider to delegate authentication to PingOne. This enables AI agents to call a protected API on behalf of an authenticated end user.
component: identity-for-ai
page_id: identity-for-ai:integrations:idai-securing-cloudflare-pingone
canonical_url: https://developer.pingidentity.com/identity-for-ai/integrations/idai-securing-cloudflare-pingone.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before-you-begin: Before you begin
  stack: Stack
  requirements: Requirements
  structure: Structure
  tasks: Tasks
  configuring-the-mcp-server-as-an-oidc-client-in-pingone: Configuring the MCP server as an OIDC Client in PingOne
  deploying-to-cloudflare: Deploying to Cloudflare
  testing-the-mcp-server-with-the-mcp-inspector: Testing the MCP Server with the MCP Inspector
  accessing-the-remote-mcp-server-from-claude-desktop: Accessing the remote MCP server from Claude Desktop
---

# Securing a Cloudflare Workers MCP server with PingOne

Configure a Cloudflare Workers Model Context Protocol (MCP) server that uses the Cloudflare Workers OAuth Provider to delegate authentication to PingOne. This enables AI agents to call a protected API on behalf of an authenticated end user.

|   |                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | While serving as a resource server for MCP clients, this MCP server also fulfills two distinct OAuth roles:- An OAuth server to your MCP clients

- An OpenID Connect (OIDC) client for your PingOne environment |

This configuration uses Cloudflare to manage consent. To use this configuration with PingOne DaVinci-managed consent, refer to [Securing a Cloudflare Workers MCP server with PingOne DaVinci](idai-securing-cloudflare-davinci.html).

## Before you begin

This tutorial uses the `remote-mcp-pingone/mcp` directory in Ping Identity's [cloudflare-mcp Git repository](https://github.com/pingidentity/cloudflare-mcp/tree/main).

### Stack

| Role            | Name                                                                                      | Description                                                       |
| --------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Platform        | [Cloudflare Workers](https://workers.cloudflare.com/)                                     | Serverless execution                                              |
| Framework       | [Hono](https://hono.dev/)                                                                 | Lightweight API endpoints                                         |
| Agent Execution | [Cloudflare Agents SDK](https://developers.cloudflare.com/agents)                         | Base class for implementing the stateful MCP server               |
| Session State   | [Cloudflare Durable Objects](https://developers.cloudflare.com/durable-objects)           | Provides stateful, isolated storage for each MCP connection       |
| OAuth Core      | [Cloudflare Workers OAuth Provider](https://github.com/cloudflare/workers-oauth-provider) | Orchestrates the OAuth flow, delegating authentication to PingOne |
| Ephemeral State | [Cloudflare Workers KV](https://developers.cloudflare.com/kv)                             | Stores OAuth state required by the workers oauth provider         |

### Requirements

* Node.js v20 or later

* A PingOne environment

* A Cloudflare account and [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/install-and-update) enabled

* [Todo API](https://github.com/pingidentity/cloudflare-mcp/tree/main/remote-mcp-pingone/api) deployed

* [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) installed

### Structure

```
mcp/
├── package.json                     # Dependencies and scripts
├── tsconfig.json                    # TypeScript compiler settings
│── wrangler.jsonc                   # Worker configuration
└── src/
    ├── index.ts                     # OAuth server flow and MCP server routing
    ├── mcp.ts                       # Stateful MCP server as a Cloudflare McpAgent (durable object)
    ├── config.ts                    # Worker bindings and Cloudflare durable object session data
    ├── todoApi.client.ts            # HTTP client to the downstream Todo API
    └── auth/
        ├── workers-oauth-utils.ts   # Cloudflare OAuth utility functions
        ├── ping-handler.ts          # Endpoints that connect the auth flow between OAuth provider and PingOne
        ├── ping-utils.ts            # PingOne OAuth utility functions
        └── ping-types.ts            # PingOne OAuth types
```

## Tasks

### Configuring the MCP server as an OIDC Client in PingOne

This step enables the Cloudflare worker to exchange authorization codes on behalf of the end user. Note that the MCP server, not the MCP client, receives the PingOne access token. The MCP server then issues a separate reference token to the MCP client for session lookups. This distinction ensures proper audience scoping: the MCP client token is intended for the MCP server, while the MCP server token is intended for the target API.

1. In the PingOne admin console, go to **Applications** and click the [icon: plus, set=fa]icon to add a new application.

2. In the **Application Type** section, click **OIDC Web App** and then click **Save**.

3. On the **Configuration** tab of the application, ensure that:

   1. **Grant Type** is set to **Authorization Code**.

   2. **PKCE Enforcement** is set to **S256_REQUIRED**.

   3. **Redirect URI** is set to your Cloudflare worker's callback endpoint, for example `<mcp_server>/callback`.\
      If the worker is not yet deployed, use a placeholder and update it later.

4. On the **Resources** tab of the application, allow the standard OIDC scopes, `openid` and `profile`, and the Todo API scopes, `todo_api:read` and `tode_api:write`.

5. On the **Policies** tab of the application, enable **Single_Factor** or your preferred policy.

### Deploying to Cloudflare

1. In your terminal, install dependencies and build:

   ```
   npm install
   npm run build
   ```

2. Use the Wrangler CLI to set the following remote environment variables:

   | Name                       | Description                            | Example                                       |
   | -------------------------- | -------------------------------------- | --------------------------------------------- |
   | `PINGONE_ISSUER`           | PingOne environment domain             | `https://auth.pingone.<REGION>/<ENV_ID>/as`   |
   | `MCP_SERVER_CLIENT_ID`     | ID of the MCP server client            | `0c24f3a0-0522-4f76-9bcf-89643029e3e0`        |
   | `MCP_SERVER_CLIENT_SECRET` | Secret of the MCP server client        | `[A long, random, alphanumeric string]`       |
   | `API_IDENTIFIER`           | ID of the downstream Todo API resource | `https://todo.api.com`                        |
   | `API_URL`                  | URL of the downstream Todo API         | `https://todo-api-ping-aic.<ENV>.workers.dev` |
   | `COOKIE_ENCRYPTION_KEY`    | Key used to sign browser cookies       | `[A long, random, base64 string]`             |

   ```
   wrangler secret put PINGONE_ISSUER
   wrangler secret put MCP_SERVER_CLIENT_ID
   wrangler secret put MCP_SERVER_CLIENT_SECRET
   wrangler secret put API_IDENTIFIER
   wrangler secret put API_URL
   wrangler secret put COOKIE_ENCRYPTION_KEY
   ```

3. Configure remote KV storage.

   ```
   wrangler kv namespace create OAUTH_KV
   ```

   |   |                                                                                         |
   | - | --------------------------------------------------------------------------------------- |
   |   | After running this command, update `wrangler.jsonc` with the generated KV namespace ID. |

4. Deploy to Cloudflare.

   ```
   npm run deploy
   ```

### Testing the MCP Server with the MCP Inspector

The MCP Inspector is a developer tool that allows you to test and debug MCP servers by simulating a client connection. This enables you to validate the authentication flow and tool execution interactively. It confirms that the Cloudflare OAuth Provider successfully captures user consent locally before delegating identity verification to PingOne.

1. Launch the Inspector.

   ```
   npx @modelcontextprotocol/inspector
   ```

   The Inspector starts on port 6277 and initiates the authentication flow. No CORS rules are needed because authentication occurs server-to-server (MCP server to PingOne), bypassing browser restrictions.

   > **Collapse: Authentication flow**
   >
   > 1. The Inspector initiates a request to the MCP endpoint (`<mcp_server>/mcp`).
   >
   > 2. The MCP server intercepts the request and presents the local, worker-hosted consent dialog.
   >
   > 3. Upon approval, the MCP server redirects the user to PingOne for authentication.
   >
   > 4. The MCP server exchanges the returned authorization code for an downstream access token.
   >
   > 5. The server binds this downstream token to a new, isolated client session.
   >
   > 6. The server establishes the connection and issues a session handle to the Inspector.

2. Verify that the MCP server is working properly by using the Inspector to confirm the following behaviour:

   * Connection initiates the full Cloudflare consent and PingOne login sequence.

   * Reconnecting (without clearing cookies and using the same MCP client ID) recovers the existing session silently.

   * Clearing browser cookies forces a new consent and authentication cycle upon reconnect.

   * The server correctly populates the tool list in the Inspector.

   * The `whoAmI` tool returns the PingOne access token audienced for the Todo API.

   * Downstream API actions (adding/deleting todos) complete successfully.

### Accessing the remote MCP server from Claude Desktop

1. In Claude Desktop, click your profile icon, and then click **Settings**.

2. Go to **Connectors** and then click **Add Custom Connector**.

3. In the **Remote MCP server URL** field, enter the URL in this format: `https://remote-mcp-ping-federate.<ENV>.workers.dev/mcp`

   No OAuth Client ID or Secret is required, as Claude will perform Dynamic Client Registration.

4. Click **Save**.

5. Connect to the MCP server and authenticate with PingFederate.

6. After they're connected, you can ask Claude: "Can you tell me what is in my Todo list?"

7. Claude sees the connected tools and calls the appropriate tool after asking for consent.

**Video (Brightcove)**

\<https\://players.brightcove.net/771836189001/default_default/index.html?videoId=6387826562112>

---

---
title: Securing a Cloudflare Workers MCP server with PingOne Advanced Identity Cloud
description: Configure a Cloudflare Workers Model Context Protocol (MCP) server that delegates authentication to PingOne Advanced Identity Cloud. This enables AI agents to call a protected API on behalf of an authenticated end user.
component: identity-for-ai
page_id: identity-for-ai:integrations:idai-securing-cloudflare-aic
canonical_url: https://developer.pingidentity.com/identity-for-ai/integrations/idai-securing-cloudflare-aic.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before-you-begin: Before you begin
  stack: Stack
  requirements: Requirements
  structure: Structure
  tasks: Tasks
  configuring-pingone-advanced-identity-cloud: Configuring PingOne Advanced Identity Cloud
  1-enable-dynamic-client-registration-dcr-for-mcp-client-onboarding: 1. Enable Dynamic Client Registration (DCR) for MCP client onboarding
  2-configure-mcp-server-for-token-exchange: 2. Configure MCP server for token exchange
  cors-setup: 3. Setup Cross-Origin Resource Sharing (CORS)
  deploying-to-cloudflare: Deploying to Cloudflare
  testing-the-mcp-server-with-mcp-inspector: Testing the MCP server with MCP Inspector
  accessing-the-remote-mcp-server-from-claude-desktop: Accessing the remote MCP server from Claude Desktop
---

# Securing a Cloudflare Workers MCP server with PingOne Advanced Identity Cloud

Configure a Cloudflare Workers Model Context Protocol (MCP) server that delegates authentication to PingOne Advanced Identity Cloud. This enables AI agents to call a protected API on behalf of an authenticated end user.

## Before you begin

This tutorial uses the `remote-mcp-pingone-aic` directory in the Ping Identity [cloudflare-mcp Git repository](https://github.com/pingidentity/cloudflare-mcp/tree/main).

### Stack

| Role            | Name                                                                            | Description                                                 |
| --------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Platform        | [Cloudflare Workers](https://workers.cloudflare.com/)                           | Serverless execution                                        |
| Framework       | [Hono](https://hono.dev/)                                                       | Lightweight API endpoints                                   |
| Agent Execution | [Cloudflare Agents SDK](https://developers.cloudflare.com/agents)               | Base class for implementing the stateful MCP server         |
| Session State   | [Cloudflare Durable Objects](https://developers.cloudflare.com/durable-objects) | Provides stateful, isolated storage for each MCP connection |

### Requirements

* Node.js v20 or later

* A PingOne Advanced Identity Cloud tenant

* A Cloudflare account and [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/install-and-update) enabled

* [Todo API](https://github.com/pingidentity/cloudflare-mcp/tree/main/remote-mcp-pingone-aic/api) deployed

### Structure

```
mcp/
├── package.json               # Dependencies and scripts
├── tsconfig.json              # TypeScript compiler settings
├── wrangler.jsonc             # Worker configuration
└── src/
    ├── index.ts               # Defines the HTTP interface, handling MCP server discovery and MCP server routing
    ├── mcp.ts                 # Stateful MCP server as a cloudflare McpAgent (durable object)
    ├── config.ts              # Worker bindings and durable object session data
    ├── auth.ts                # Manages auth middleware and executes token exchange (delegation grant)
    └── todoApi.client.ts      # HTTP client to the downstream Todo API
```

## Tasks

### Configuring PingOne Advanced Identity Cloud

#### 1. Enable Dynamic Client Registration (DCR) for MCP client onboarding

This step allows MCP clients to automatically register themselves as public OpenID Connect (OIDC) clients and request the necessary scopes to call the downstream Todo API. The MCP client uses the MCP server's protected resource metadata to determine how to register and which scopes to request.

1. In the PingOne Advanced Identity Cloud **Access Management** console, go to Services > OAuth2 Provider.

2. On the **Client Dynamic Registration** tab, enable **Allow Open Dynamic Client Registration**.

3. On the **Advanced** tab, allow the following Todo API scopes:

   * `todo_api:read`

   * `todo_api:write`

#### 2. Configure MCP server for token exchange

This step configures delegation and authorizes the MCP server to act on the end user's behalf. This allows the MCP server to swap the end user's token for a new token used to call the downstream Todo API. This new token is properly audienced for the target API and includes the `act` claim, identifying the MCP server as the trusted intermediary.

1. Enable grant types and scopes:

   1. From the PingOne Advanced Identity Cloud **Access Management** console, go to Applications > OAuth2 > Clients.

   2. Create a new client for the MCP server.

   3. On the **Core** tab, set the scopes to maximum allowable permissions.

   4. On the **Advanced** tab, add the **Client Credentials** and **Token Exchange** grant types to allow the MCP server to request its own token and perform the delegation, respectively.

2. Flag eligible tokens for token exchange with the `may_act` claim:

   Run a script upon user token issuance to inject a claim designating the MCP server as the trusted delegate. Because DCR prevents you from knowing the MCP client's client ID, the script will be applied to all tokens but include safeguards to only target access tokens intended for the MCP server.

   1. In the PingOne Advanced Identity Cloud **Access Management** console, go to Services > OAuth2 Provider > Scripts.

   2. Create a new script of type **OAuth2 May Act**.

   3. Copy and paste the following script, replacing placeholder values with your configuration values:

      ```javascript
      (function () {
        var frJava = JavaImporter(org.forgerock.json.JsonValue);
        var normalizeUrl = function(url) { return url.replace(/\/$/, '') };

        var mcpServerClientId = 'MCP_SERVER_CLIENT_ID';  // placeholder
        var mcpServerUrl = 'URL_OF_DEPLOYED_MCP_SERVER'; // placeholder

        try {
          var requestedResourceList = requestProperties.requestParams.get('resource');
          var requestedResource = String(requestedResourceList.get(0));

          // Only modify tokens intended for the MCP server
          if (normalizeUrl(requestedResource) === normalizeUrl(mcpServerUrl)) {

            // Explicitly set the MCP server as the audience of this token
            token.setField("aud", mcpServerUrl);

            // Authorize MCP server to exchange this token
            var mayAct = frJava.JsonValue.json(frJava.JsonValue.object());
            mayAct.put('client_id', mcpServerClientId);
            mayAct.put('sub', mcpServerClientId);
            token.setMayAct(mayAct);
          };
        } catch (error) {};
      }());
      ```

   4. In the PingOne Advanced Identity Cloud **Access Management** console, go to Services > OAuth2 Provider.

   5. On the **Core** tab, set the **OAuth2 Access Token May Act Script**.

3. Control exchanged token audience with an access token modification script.

   This step ensures the downstream API accepts the exchanged token. Because Advanced Identity Cloud doesn't automatically set the necessary audience claim during token exchange, use an access token modification script tied specifically to the MCP server's client profile.

   1. In the Advanced Identity Cloud **Access Management** console, go to Services > OAuth2 Provider > Scripts.

   2. Create a new script of type **OAuth2 Access Token Modification (Next Gen)**.

   3. Copy and paste the following script, replacing the placeholder value with your downstream API URL:

      ```javascript
      (function () {
        var frJava = JavaImporter(org.forgerock.json.JsonValue);
        var normalizeUrl = function(url) { return url.replace(/\/$/, '') };

        // Only modify MCP server access tokens granted with token exchange
        var grantType = requestProperties.requestParams.get('grant_type');
        if (!grantType || grantType.toString() !== '[urn:ietf:params:oauth:grant-type:token-exchange]') {
          return;
        };

        // Only allow MCP server to call these APIs
        var whitelistedAPIs = [
          'URL_OF_DEPLOYED_API', // placeholder value
        ];

        try {
          var requestedResourceList = requestProperties.requestParams.get('resource');
          var requestedResource = JSON.stringify(requestedResourceList).slice(2, -2);

          for (var i = 0; i < whitelistedAPIs.length; i++) {
            var whitelistedApi = normalizeUrl(whitelistedAPIs[i])
            if (normalizeUrl(requestedResource) === whitelistedApi) {
              // Resulting token will be audienced for the requested & whitelisted API
              accessToken.setField("aud", whitelistedApi);
              break;
            };
          };
        } catch (error) {};
      }());
      ```

#### 3. Setup Cross-Origin Resource Sharing (CORS)

For external MCP clients to communicate with Advanced Identity Cloud during the OAuth flow, explicitly allow the MCP inspector.

1. In the PingOne Advanced Identity Cloud dashboard, go to Tenant Settings > Global Settings.

2. Click **Cross-Origin Resource Sharing (CORS)**, and then **Add a CORS Configuration**.

3. Configure the rule for the local MCP Inspector using the following values:

   1. In the **Accepted Origins** field, enter `http://localhost:6277`.

   2. In the **Accepted Methods** field, enter `GET` and `POST`.

   3. In the **Accepted Headers** field, enter `authorization` and `content-type`.

4. Click **Save CORS Configuration**.

### Deploying to Cloudflare

1. Install dependencies and deploy the MCP server:

   ```
   npm install
   npm run deploy
   ```

2. Use the Wrangler CLI to configure the remote environment variables:

   | Name                     | Description                                        | Example                                             |
   | ------------------------ | -------------------------------------------------- | --------------------------------------------------- |
   | PING_AIC_ISSUER          | PingOne Advanced Identity Cloud environment domain | `https://<ENV>.forgeblocks.com:443/am/oauth2/alpha` |
   | MCP_SERVER_URL           | URL of the deployed MCP server                     | `https://remote-mcp-ping-aic.<ENV>.workers.dev`     |
   | MCP_SERVER_CLIENT_ID     | ID of the MCP server client                        | `mcp_server`                                        |
   | MCP_SERVER_CLIENT_SECRET | Secret of the MCP server client                    | `[A long, random, alphanumeric string]`             |
   | API_URL                  | URL of the downstream Todo API                     | `https://todo-api-ping-aic.<ENV>.workers.dev`       |

   ```
   wrangler secret put PING_AIC_ISSUER
   wrangler secret put MCP_SERVER_URL
   wrangler secret put MCP_SERVER_CLIENT_ID
   wrangler secret put MCP_SERVER_CLIENT_SECRET
   wrangler secret put API_URL
   ```

3. Ensure the `mcpServerUrl` is correct in the Advanced Identity Cloud `may_act` script that you created in [step 2.2](#may-act).

### Testing the MCP server with MCP Inspector

1. To validate the deployed MCP server, launch MCP Inspector:

   ```
   npx @modelcontextprotocol/inspector
   ```

   MCP Inspector starts on port 6277, which you allowed in the [CORS configuration](#cors-setup). To confirm that DCR is operational, the Inspector acts as an unregistered client and establishes a secure connection.

   ![A screen capture of the MCP Inspector initiating authentication and self-registering with Advanced Identity Cloud.](_images/idai-mcp-inspector-connect.png)

   > **Collapse: Authentication flow**
   >
   > 1. The Inspector attempts an initial, unauthenticated request to the MCP endpoint (`<mcp_server>/mcp`).
   >
   > 2. The MCP server responds with the protected resource metadata, triggering the discovery process.
   >
   > 3. The MCP inspector consumes the metadata, performs discovery of the authorization server, and self-registers with Advanced Identity Cloud as a public OIDC client.
   >
   > 4. The MCP Inspector initiates the OAuth authorization flow, securing the necessary user consent and establishing a stateful MCP connection.

2. To validate token exchange, observe how the MCP server acquires a new token audienced for the downstream API. Use the `who_am_I` and `peek_api_token_claims` tools to compare the two tokens and confirm the following behavior:

   * Both tokens share the same `sub` claim, confirming they identify the same authenticated end user.

   * The subject token contains the `may_act` claim, explicitly authorizing the MCP server for exchange. The resulting delegation token contains the `act` claim, identifying the MCP server as the trusted intermediary acting on the user's behalf.

   * The subject token is audienced for the MCP server, while the delegation token is audienced for the downstream API.

   * The subject token retains the user's full, broader permissions. The delegation token is limited to only what's necessary for its target audience.

   ![The original end user token and the MCP server delegation token shown side-by-side.](_images/idai-token-exchange-tokens.png)

### Accessing the remote MCP server from Claude Desktop

1. In Claude Desktop, click your profile icon, and then click **Settings**.

2. Go to **Connectors** and then click **Add Custom Connector**.

3. In the **Remote MCP server URL** field, enter the URL in this format: `https://remote-mcp-ping-federate.<ENV>.workers.dev/mcp`

   No OAuth Client ID or Secret is required, as Claude will perform Dynamic Client Registration.

4. Click **Save**.

5. Connect to the MCP server and authenticate with PingFederate.

6. After they're connected, you can ask Claude: "Can you tell me what is in my Todo list?"

7. Claude sees its connected tools and calls the appropriate tool after asking for consent.

**Video (Brightcove)**

\<https\://players.brightcove.net/771836189001/default_default/index.html?videoId=6387779240112>

---

---
title: Securing a Cloudflare Workers MCP server with PingOne DaVinci
description: Configure a Cloudflare Workers Model Context Protocol (MCP) server that uses the Cloudflare Workers OAuth Provider to delegate authentication to PingOne DaVinci. This enables AI agents to call a protected API on behalf of an authenticated end user.
component: identity-for-ai
page_id: identity-for-ai:integrations:idai-securing-cloudflare-davinci
canonical_url: https://developer.pingidentity.com/identity-for-ai/integrations/idai-securing-cloudflare-davinci.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before-you-begin: Before you begin
  stack: Stack
  requirements: Requirements
  structure: Structure
  tasks: Tasks
  task-1: Configuring the MCP server as an OIDC client in PingOne
  creating-a-worker-application-to-handle-mcp-server-consent: Creating a Worker application to handle MCP server consent
  task-3: Creating the DaVinci flow using the MCP server OIDC client and the consent service worker
  task-4: Creating a DaVinci policy for the DaVinci flow
  binding-the-davinci-policy-to-the-mcp-server-client-profile: Binding the DaVinci policy to the MCP server client profile
  deploying-to-cloudflare: Deploying to Cloudflare
  testing-the-mcp-server-with-mcp-inspector: Testing the MCP server with MCP Inspector
  accessing-the-remote-mcp-server-from-claude-desktop: Accessing the remote MCP server from Claude Desktop
---

# Securing a Cloudflare Workers MCP server with PingOne DaVinci

Configure a Cloudflare Workers Model Context Protocol (MCP) server that uses the Cloudflare Workers OAuth Provider to delegate authentication to PingOne DaVinci. This enables AI agents to call a protected API on behalf of an authenticated end user.

|   |                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | While serving as a resource server for MCP clients, this MCP server also fulfills two distinct OAuth roles:- Acts as an OAuth Server to your MCP clients

- Acts as an OpenID Connect (OIDC) Client to your PingOne environment |

This configuration uses DaVinci to manage consent. To use this configuration with Cloudflare-managed consent, see [Securing a Cloudflare Workers MCP server with PingOne](idai-securing-cloudflare-pingone.html).

## Before you begin

This tutorial uses the `remote-mcp-pingone/mcp-dv` directory in Ping Identity's [cloudflare-mcp Git repository](https://github.com/pingidentity/cloudflare-mcp/tree/main).

### Stack

| Role            | Name                                                                                      | Description                                                       |
| --------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Platform        | [Cloudflare Workers](https://workers.cloudflare.com/)                                     | Serverless execution                                              |
| Framework       | [Hono](https://hono.dev/)                                                                 | Lightweight API endpoints                                         |
| Agent Execution | [Cloudflare Agents SDK](https://developers.cloudflare.com/agents)                         | Base class for implementing the stateful MCP server               |
| Session State   | [Cloudflare Durable Objects](https://developers.cloudflare.com/durable-objects)           | Provides stateful, isolated storage for each MCP connection       |
| OAuth Core      | [Cloudflare Workers OAuth Provider](https://github.com/cloudflare/workers-oauth-provider) | Orchestrates the OAuth flow, delegating authentication to PingOne |
| Ephemeral State | [Cloudflare Workers KV](https://developers.cloudflare.com/kv)                             | Stores OAuth state required by the workers oauth provider         |

### Requirements

* Node.js v20 or later

* A PingOne environment

* A Cloudflare account and [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/install-and-update) enabled

* [Todo API](https://github.com/pingidentity/cloudflare-mcp/tree/main/remote-mcp-pingone/api) deployed

* [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) installed

### Structure

```
mcp-dv/
├── package.json                     # Dependencies and scripts
├── tsconfig.json                    # TypeScript compiler settings
│── wrangler.jsonc                   # Worker configuration
└── src/
    ├── index.ts                     # OAuth server flow and MCP server routing
    ├── mcp.ts                       # Stateful MCP server as a Cloudflare McpAgent (durable object)
    ├── config.ts                    # Worker bindings and Cloudflare durable object session data
    ├── todoApi.client.ts            # HTTP client to the downstream Todo API
    └── auth/
        ├── workers-oauth-utils.ts   # Cloudflare OAuth utility functions
        ├── ping-handler.ts          # Endpoints that connect the auth flow between OAuth provider and PingOne
        ├── ping-utils.ts            # PingOne OAuth utility functions
        └── ping-types.ts            # PingOne OAuth types
```

## Tasks

### Configuring the MCP server as an OIDC client in PingOne

This step enables the Cloudflare worker to exchange authorization codes on behalf of the end user. Note that the MCP server, not the MCP client, receives the PingOne access token. The MCP server then issues a separate reference token to the MCP client for session lookups. This distinction ensures proper audience scoping: the MCP client token is intended for the MCP server, while the MCP server token is intended for the target API.

1. In the PingOne admin console, go to **Applications** and click the [icon: plus, set=fa]icon to add a new application.

2. In the **Application Type** section, click **OIDC Web App** and then click **Save**.

3. On the **Configuration** tab of the application, ensure that:

   1. **Grant Type** is set to **Authorization Code**.

   2. **PKCE Enforcement** is set to **S256_REQUIRED**.

   3. **Redirect URI** is set to your Cloudflare worker's callback endpoint, for example `<mcp_server>/callback`. If the worker is not yet deployed, use a placeholder and update it later.

4. On the **Resources** tab of the application, allow the standard OIDC scopes, `openid` and `profile`, and the Todo API scopes, `todo_api:read` and `tode_api:write`.

5. On the **Policies** tab of the application, leave the policy blank for now. You'll configure this in a later step.

### Creating a Worker application to handle MCP server consent

1. In the PingOne admin console, go to **Applications** and click the [icon: plus, set=fa]icon to add a new application.

2. Select **Worker** and click **Save**.

3. On the **Overview** tab of the application, note the **Client ID** and **Client Secret**.

4. On the **Configuration** tab, set **Token Auth Method** to **Client Secret Basic**.

5. On the **Roles** tab, assign the **Environment Admin** and **Identity Data Admin** roles to the application to authorize it to manage user consent.

### Creating the DaVinci flow using the MCP server OIDC client and the consent service worker

Create the DaVinci flow that orchestrates both authentication and consent for the MCP server. You'll modify a standard PingOne sign-on flow to include the consent logic.

1. In DaVinci, add the PingOne Scope Consent connector and configure it using the client ID and client secret from the consent service worker.

2. Go to **Flows** and clone the **PingOne Sign On with Registration, Password Reset and Recovery** flow.

3. Locate the **Sign on Success** node and add a **Get User Consent** node immediately after it.

4. Configure the **Get User Consent** node by entering the application ID of the MCP server OIDC Client.

5. Configure the PingOne authentication terminal nodes and make sure the flow is a PingOne flow in the flow settings.

![A screen capture of the DaVinci flow in PingOne.](_images/idai-davinci-mcp-flow.png)

### Creating a DaVinci policy for the DaVinci flow

Add the DaVinci flow to an application and create a flow policy to control how and when the flow gets used.

1. In DaVinci, go to **Applications** and create a new application.

2. Add a PingOne flow policy to the application and target the DaVinci flow created in [task 3](#task-3).

### Binding the DaVinci policy to the MCP server client profile

This ensures that when the MCP server initiates an OAuth request, PingOne routes the user through the DaVinci flow to capture the required consent.

1. In the PingOne admin console, select the MCP server client created in [task 1](#task-1).

2. On the **Policies** tab, add the DaVinci Policy created in [task 4](#task-4).

### Deploying to Cloudflare

1. In your terminal, install dependencies and build.

   ```
   npm install
   npm run build
   ```

2. Use the Wrangler CLI to set the following remote environment variables:

   | Name                       | Description                            | Example                                       |
   | -------------------------- | -------------------------------------- | --------------------------------------------- |
   | `PINGONE_ISSUER`           | PingOne environment domain             | `https://auth.pingone.<REGION>/<ENV_ID>/as`   |
   | `MCP_SERVER_CLIENT_ID`     | ID of the MCP server client            | `0c24f3a0-0522-4f76-9bcf-89643029e3e0`        |
   | `MCP_SERVER_CLIENT_SECRET` | Secret of the MCP server client        | `[A long, random, alphanumeric string]`       |
   | `API_IDENTIFIER`           | ID of the downstream Todo API resource | `https://todo.api.com`                        |
   | `API_URL`                  | URL of the downstream Todo API         | `https://todo-api-ping-aic.<ENV>.workers.dev` |
   | `COOKIE_ENCRYPTION_KEY`    | Key used to sign browser cookies       | `[A long, random, base64 string]`             |

   ```
   wrangler secret put PINGONE_ISSUER
   wrangler secret put MCP_SERVER_CLIENT_ID
   wrangler secret put MCP_SERVER_CLIENT_SECRET
   wrangler secret put API_IDENTIFIER
   wrangler secret put API_URL
   wrangler secret put COOKIE_ENCRYPTION_KEY
   ```

3. Configure remote KV storage.

   ```
   wrangler kv namespace create OAUTH_KV
   ```

   |   |                                                                                         |
   | - | --------------------------------------------------------------------------------------- |
   |   | After running this command, update `wrangler.jsonc` with the generated KV namespace ID. |

4. Deploy to Cloudflare.

   ```
   npm run deploy
   ```

### Testing the MCP server with MCP Inspector

MCP Inspector is a developer tool that allows you to test and debug MCP servers by simulating a client connection. This enables you to validate the authentication flow and tool execution interactively. It confirms that the Cloudflare OAuth Provider successfully captures user consent locally before delegating identity verification to PingOne.

1. Launch the Inspector.

   ```
   npx @modelcontextprotocol/inspector
   ```

   The Inspector starts on port 6277 and initiates the authentication flow. No CORS rules are needed because authentication occurs server-to-server (MCP server to PingOne), bypassing browser restrictions.

   > **Collapse: Authentication flow**
   >
   > 1. The Inspector initiates a request to the MCP endpoint (`<mcp_server>/mcp`).
   >
   > 2. The MCP server intercepts the request and presents the local, worker-hosted consent dialog.
   >
   > 3. Upon approval, the MCP server redirects the user to PingOne for authentication.
   >
   > 4. The MCP server exchanges the returned authorization code for an downstream access token.
   >
   > 5. The server binds this downstream token to a new, isolated client session.
   >
   > 6. The server establishes the connection and issues a session handle to the Inspector.

2. Verify that the MCP server is working properly by using the Inspector to confirm the following behaviour:

   * Connection initiates the full Cloudflare consent and PingOne login sequence.

   * Reconnecting (without clearing cookies and using the same MCP client ID) recovers the existing session silently.

   * Clearing browser cookies forces a new consent and authentication cycle upon reconnect.

   * The server correctly populates the tool list in the Inspector.

   * The `whoAmI` tool returns the PingOne access token audienced for the Todo API.

   * Downstream API actions (adding/deleting todos) complete successfully.

![A screen capture of the DaVinci flow in PingOne.](_images/idai-mcp-inspector-dv.png)

### Accessing the remote MCP server from Claude Desktop

1. In Claude Desktop, click your profile icon, and then click **Settings**.

2. Go to **Connectors** and then click **Add Custom Connector**.

3. In the **Remote MCP server URL** field, enter the URL in this format: `https://remote-mcp-ping-federate.<ENV>.workers.dev/mcp`

   No OAuth Client ID or Secret is required, as Claude will perform Dynamic Client Registration.

4. Click **Save**.

5. Connect to the MCP server and authenticate with PingFederate.

6. After they're connected, you can ask Claude: "Can you tell me what is in my Todo list?"

7. Claude sees the connected tools and calls the appropriate tool after asking for consent.

**Video (Brightcove)**

\<https\://players.brightcove.net/771836189001/default_default/index.html?videoId=6387777951112>

---

---
title: Securing Amazon Bedrock AgentCore Identity with Ping Identity
description: You can integrate Ping Identity's identity providers (IdPs) with Amazon Bedrock AgentCore Identity to secure agent-based workloads.
component: identity-for-ai
page_id: identity-for-ai:integrations:idai-securing-aws-ping
canonical_url: https://developer.pingidentity.com/identity-for-ai/integrations/idai-securing-aws-ping.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  goals: Goals
  amazon-bedrock-agentcore-identity-model: Amazon Bedrock AgentCore Identity model
  p1-steps: PingOne integration
  configuring-pingone-for-inbound-authentication: Configuring PingOne for inbound authentication
  configuring-outbound-authentication: Configuring outbound authentication
  agentcore-outbound-resource-provider-configuration: AgentCore outbound resource provider configuration
  aic-steps: PingOne Advanced Identity Cloud integration
  configuring-pingone-advanced-identity-cloud-for-inbound-authentication: Configuring PingOne Advanced Identity Cloud for inbound authentication
  configuring-outbound-authentication-2: Configuring outbound authentication
  agentcore-outbound-resource-provider-configuration-2: AgentCore outbound resource provider configuration
  pf-steps: PingFederate integration
  configuring-pingfederate-for-inbound-authentication: Configuring PingFederate for inbound authentication
  configuring-outbound-authentication-3: Configuring outbound authentication
  agentcore-outbound-resource-provider-configuration-3: AgentCore outbound resource provider configuration
  result: Result
---

# Securing Amazon Bedrock AgentCore Identity with Ping Identity

You can integrate Ping Identity's identity providers (IdPs) with [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) to secure agent-based workloads.

You can configure PingOne, PingOne Advanced Identity Cloud, or PingFederate, as an:

* Inbound IdP for AgentCore Gateway and Runtime

  This enables agents to authenticate and authorize end users using OpenID Connect (OIDC) tokens issued by Ping Identity.

* Outbound credential provider for AgentCore Identity

  This enables agents to securely obtain OIDC access tokens from Ping Identity in order to call downstream APIs and protected resources.

## Goals

* Centralize authentication and authorization for Bedrock AgentCore agents with Ping Identity IdPs.

* Enforce consistent OIDC controls such as audience (`aud`) validation, scopes, and grant types across inbound and outbound agent interactions.

* Support both user-based flows (OAuth 2.0 Authorization Code grant) and machine-to-machine flows (OAuth 2.0 Client Credentials grant) as implemented in the Amazon Bedrock AgentCore Identity model.

This aligns with AWS's recommended IdP integration pattern for AgentCore, as described in the [AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) documentation, and demonstrates how Ping Identity products act as both trusted token issuers and credential providers within agent-based architectures.

## Amazon Bedrock AgentCore Identity model

Amazon Bedrock AgentCore Identity provides a standardized mechanism for:

* Inbound authentication

  Validating OAuth 2.0/OIDC tokens presented to AgentCore Gateway and Runtime by agent users.

* Outbound credential acquisition

  Securely retrieving OAuth 2.0 access tokens that agents use to access external systems.

AgentCore Identity relies on:

* OIDC discovery metadata to locate authorization, token, and JSON Web Key Set (JWKS) endpoints.

* Audience (`aud`) and scope validation to ensure tokens are issued for the correct resource.

* Explicit configuration of IdPs and credential providers.

PingOne, PingOne Advanced Identity Cloud, and PingFederate all satisfy these requirements and can be integrated with the following patterns.

## PingOne integration

You can configure Ping Identity as an IdP for accessing AgentCore Gateway and Runtime, or as an AgentCore Identity credential provider for outbound resource access. This allows your agents to authenticate and authorize agent users with PingOne as the IdP and authorization server, or your agents to obtain credentials to access resources authorized by PingOne.

To add PingOne as an IdP and authorization server for AgentCore Gateway and Runtime, you must:

* Configure the discovery URL for your PingOne environment so AgentCore Identity can retrieve OAuth and OIDC metadata.

* Configure and validate expected `aud` claims to ensure access tokens are issued for the correct protected resource.

### Configuring PingOne for inbound authentication

1. Sign on to the PingOne admin console.

2. Go to Applications > Applications.

3. Click the [icon: plus, set=fa]icon to create a new application.

4. In the **Application Name** field, enter a name.

5. In the **Application Type** section, click **OIDC Web App**, and then click **Save**.

6. Configure your application as a user federation OAuth 2.0 client:

   1. Select your application and go to the **Configuration** tab.

   2. In the **Response Type** section, select the **Code** checkbox.

   3. In the **Grant Type** section, select the **Authorization Code** checkbox, the **Client Credentials** checkbox, or both depending on your use case.

   4. In the **Token Endpoint Authentication Method** list, select **Client Secret Post**.

   5. (Optional) If using the authorization code grant type, enter the **Redirect URI**.

   Learn more in [Editing an application - OIDC](https://docs.pingidentity.com/pingone/applications/p1_edit_application_oidc.html) in the PingOne documentation.

7. Create a custom resource.

   1. Go to Applications > Resources and click the [icon: plus, set=fa]icon to create a new resource.

   2. In the **Resource Name** field, enter a name for the resource, and then click **Next**.

   3. In the **PingOne Mappings** list, select a value to map to the `sub` attribute, and the click **Next**.

   4. Click **+ Add Scope+** to define a scope and assign it to the application.

   5. Click **Save**.

      |   |                                                                                          |
      | - | ---------------------------------------------------------------------------------------- |
      |   | You will set this resource name as the `aud` claim for Client Credentials access tokens. |

   Learn more in [Adding a custom resource](https://docs.pingidentity.com/pingone/applications/p1_adding_custom_resource.html) in the PingOne documentation.

8. Configure the AgentCore inbound authentication:

   1. For `discoveryURL`, use the **OIDC Discovery Endpoint** value from the **Overview** tab on the PingOne application details pane.

   2. For `allowedAudiences`, use the resource name you created in [step 7](#create-resource).

   Learn more in [Connect to private identity providers](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-private-idp.html) in the Amazon Bedrock AgentCore documentation.

### Configuring outbound authentication

Outbound configuration mirrors inbound configuration, with the additional step of adding the AgentCore Identity callback URL to the application's redirect URIs.

#### AgentCore outbound resource provider configuration

```
{
  "name": "PingOne",
  "credentialProviderVendor": "PingOneOauth2",
  "oauth2ProviderConfigInput": {
    "includedOauth2ProviderConfig": {
      "clientId": "<CLIENT_ID>",
      "clientSecret": "<CLIENT_SECRET>",
      "authorizeEndpoint": "https://auth.pingone.com/<ENV_ID>/as/authorize",
      "tokenEndpoint": "https://auth.pingone.com/<ENV_ID>/as/token",
      "issuer": "https://auth.pingone.com/<ENV_ID>/as"
    }
  }
}
```

## PingOne Advanced Identity Cloud integration

You can configure PingOne Advanced Identity Cloud as an IdP for accessing AgentCore Gateway and Runtime, or as an AgentCore Identity credential provider for outbound resource access. This enables both user-based and machine-based agent interactions secured by PingOne Advanced Identity Cloud.

### Configuring PingOne Advanced Identity Cloud for inbound authentication

1. In the PingOne Advanced Identity Cloud admin console, go to Applications > Custom Application.

2. Select **OIDC - OpenID Connect** and then click **Service**.

3. Complete the following fields:

   1. `Application Name`

   2. `Description`

   3. `Owner`

4. Create the **Client ID** and **Client Secret**.

5. On the **Sign-On** tab, configure the following fields:

   1. Authorization code or client credentials grant types.

   2. **Redirect URI** if using Authorization Code.

6. Configure AgentCore inbound authentication:

   1. For `discoveryURL`, use the **OIDC Discovery Endpoint** from the **Sign-On** tab.

   2. For `allowedAudiences`, use the **Client ID**.

   Learn more in [Connect to private identity providers](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-private-idp.html) in the Amazon Bedrock AgentCore documentation.

### Configuring outbound authentication

Outbound configuration mirrors inbound configuration, with the additional step of adding the AgentCore Identity callback URL to the application's redirect URIs.

#### AgentCore outbound resource provider configuration

```
{
  "name": "PingOne AIC",
  "credentialProviderVendor": "CustomOauth2",
  "oauth2ProviderConfigInput": {
    "includedOauth2ProviderConfig": {
      "clientId": "CLIENT_ID",
      "clientSecret": "CLIENT_SECRET",
      "oauthDiscovery": {
        "discoveryUrl": "https://<PINGONE_AIC_TENANT>/am/oauth2/realms/root/realms/<REALM>/.well-known/openid-configuration"
      }
    }
  }
}
```

## PingFederate integration

You can configure PingFederate as an IdP for accessing AgentCore Gateway and Runtime, or as an AgentCore Identity credential provider for outbound resource access, supporting enterprise OAuth deployments and fine-grained token control.

### Configuring PingFederate for inbound authentication

1. In the PingFederate admin console, go to Applications > OAuth > Clients and click **Add Client**.

2. Configure the following fields:

   1. **Client ID** and **Client Secret**.

   2. **Redirect URI**, if applicable.

   3. For **Allowed Grant Types**, select **Authorization Code** or **Client Credentials**.

3. Go to **System > OAuth Settings > Scope Management** and create one or more scopes.

4. Go to **Applications > OAuth > Access Token Management** and configure the `aud` claim by setting the **Audience Claim Value**.

5. Allow the client to request the appropriate scopes and grant types.

6. Configure AgentCore inbound authentication:

   1. For `discoveryURL`, use `https://<PINGFED_SERVER_HOSTNAME>/.well-known/oauth-authorization-server`.

   2. For `allowedAudiences`, use the configured audience value.

   Learn more in [Connect to private identity providers](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-private-idp.html) in the Amazon Bedrock AgentCore documentation.

### Configuring outbound authentication

Outbound configuration mirrors inbound configuration, with the additional step of adding the AgentCore Identity callback URL to the application's redirect URIs.

#### AgentCore outbound resource provider configuration

```
{
  "name": "PingFederate",
  "credentialProviderVendor": "CustomOauth2",
  "oauth2ProviderConfigInput": {
    "includedOauth2ProviderConfig": {
      "clientId": "<CLIENT_ID>",
      "clientSecret": "<CLIENT_SECRET>",
      "oauthDiscovery": {
        "discoveryUrl": "https://<PINGFED_SERVER_HOSTNAME>/.well-known/oauth-authorization-server
      }
    }
  }
}
```

## Result

You've successfully integrated PingOne, PingOne Advanced Identity Cloud, or PingFederate with Amazon Bedrock AgentCore Identity and can apply consistent enterprise identity controls to AI agents.