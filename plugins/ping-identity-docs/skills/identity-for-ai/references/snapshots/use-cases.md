---
title: Securing AI agents with PingOne using delegation and least privilege
description: Configure PingOne and PingGateway to secure AI agents using OAuth 2.0 token exchange, consent workflows, and least-privilege MCP server protection.
component: identity-for-ai
page_id: identity-for-ai:use-cases:idai-securing-agents-pingone
canonical_url: https://developer.pingidentity.com/identity-for-ai/use-cases/idai-securing-agents-pingone.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-16T00:06:46Z
keywords: ["Identity for AI", "ai identity", "ai security", "ai agent", "personal agent", "digital assistant", "digital worker"]
page_aliases: ["identity:idai-securing-agents-pingone.adoc"]
section_ids:
  goals: Goals
  what-youll-do: What you'll do
  before-you-begin: Before you begin
  tasks: Tasks
  idai-add-p1-resources: Adding custom resources
  idai-add-p1-consent-agreement: Adding a consent agreement
  idai-add-p1-authn-policy: Adding an authentication policy
  idai-add-p1-agent: Adding an AI agent
  result: Result
  idai-configure-pinggateway-p1: Configuring PingGateway
  result-2: Result
  idai-start-mcp-agent-p1: Start the MCP agent
  result-3: Result
  validation: Validation
  result-4: Result
  troubleshooting: Troubleshooting
  token-exchange-fails-and-act-claim-is-null: Token exchange fails and act claim is null
  pinggateway-drops-mcp-traffic: PingGateway drops MCP traffic
  gateway-routing-errors: Gateway routing errors
  consent-prompt-issues: Consent prompt issues
  agent-can-list-tools-but-not-call-them: Agent can list tools but not call them
  whats-next: What's next
---

# Securing AI agents with PingOne using delegation and least privilege

PingOne PingGateway

Organizations are deploying AI-driven digital assistants to act on behalf of humans. To securely deploy these agents, treat them as first-class, non-human identities distinct from end users and enforce least-privilege access.

As an example scenario, consider a chatbot embedded in a banking app:

* Customers use the chatbot to retrieve account balances and make transactions.

* Acting on behalf of the customer, the chatbot accesses backend account resources.

* To secure these interactions, PingOne issues tokens and exchanges them as necessary, based on the agent's requested access and target resource.

* PingGateway validates the tokens, acting as a security proxy in front of account resources.

You can find more details about the process flow in [Securing digital assistants](idai-securing-digital-assistants.html).

## Goals

* Secure a digital assistant to ensure the agent only performs authorized actions on behalf of the user.

* Configure [OAuth 2.0 token exchange](https://docs.pingidentity.com/pingone/use_cases/p1_oauth_2_token_exchange.html) to issue downscoped access tokens that preserve the chain of delegation using the `act` claim.

* Protect backend Model Context Protocol (MCP) servers and APIs using PingGateway.

## What you'll do

To enable secure delegation, you'll set up PingOne and PingGateway:

* [Add custom resources](#idai-add-p1-resources).

* [Add a consent agreement](#idai-add-p1-consent-agreement).

* [Add an authentication policy](#idai-add-p1-authn-policy).

* [Add an AI agent](#idai-add-p1-agent).

* [Configure PingGateway](#idai-configure-pinggateway-p1).

* [Start the MCP agent](#idai-start-mcp-agent-p1).

## Before you begin

To complete this use case, you'll need:

* Administrator access in a PingOne environment that's configured to work with PingGateway. Learn more in [PingGateway and PingOne](https://docs.pingidentity.com/pinggateway/latest/pingone/preface.html) in the PingGateway documentation.

* PingGateway installed and configured with server-side SSL (TLS). Learn more in [MCP security gateway](https://docs.pingidentity.com/pinggateway/latest/mcp/index.html) and [Configuring PingGateway for TLS (server-side)](https://docs.pingidentity.com/pinggateway/latest/installation-guide/securing-connections.html#server-side-tls) in the PingGateway documentation. The sample application isn't required for this use case.

  > **Collapse: Example admin.json file**
  >
  > This is an example `.openig/config/admin.json` connector for SSL. The user is `macuser` and the secrets folder `/Users/macuser/.openig/secrets` contains the self-signed certificate for ig.example.com.
  >
  > ```json
  > {
  >   "adminConnector": {
  >     "host": "localhost",
  >     "port": 8085
  >   },
  >   "connectors": [
  >     {
  >       "port": 8080
  >     },
  >     {
  >       "port": 8443,
  >       "tls": "ServerTlsOptions-1"
  >     }
  >   ],
  >   "streamingEnabled": true,
  >   "heap": [
  >     {
  >       "name": "ServerTlsOptions-1",
  >       "type": "ServerTlsOptions",
  >       "config": {
  >         "keyManager": {
  >           "type": "SecretsKeyManager",
  >           "config": {
  >             "signingSecretId": "key.manager.secret.id",
  >             "secretsProvider": "ServerIdentityStore"
  >           }
  >         }
  >       }
  >     },
  >     {
  >       "name": "ServerIdentityStore",
  >       "type": "FileSystemSecretStore",
  >       "config": {
  >         "format": "PLAIN",
  >         "directory": "/Users/macuser/.openig/secrets",
  >         "suffix": ".pem",
  >         "mappings": [{
  >           "secretId": "key.manager.secret.id",
  >           "format": {
  >             "type": "PemPropertyFormat"
  >           }
  >         }]
  >       }
  >     }
  >   ]
  > }
  > ```

* A deployed MCP server capable of exposing tools the agent will access, such as `banking:read_balance` and `banking:transfer`. You can use the sample MCP and agent software described in [MCP security gateway preparation](https://docs.pingidentity.com/pinggateway/latest/mcp/index.html#preparation) in the PingGateway documentation.

  |   |                                                                                                                                                            |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The sample MCP and agent software is for a weather application, but you can adapt them for this use case if you don't already have an MCP server or agent. |

## Tasks

### Adding custom resources

Add custom resources that represent the services the agent is allowed to access. You can find more details in [Adding a custom resource](https://docs.pingidentity.com/pingone/applications/p1_adding_custom_resource.html) in the PingOne documentation.

You'll add two resources that serve different purposes in the delegation flow:

* The **test** resource represents the backend service that the agent calls through PingGateway. Its attributes map the human user into `sub` and, when delegation is valid, copy the user's `may_act` into `act` so the backend can see that this agent is acting on behalf of this user for a specific audience.

* The **agent** resource represents the agent itself and the delegation relationship between the user and the agent, populated in `may_act`. This relationship establishes who is allowed to act (which client ID the user delegated to) when the agent calls the backend. The backend resource uses `may_act` information to enforce what the agent is allowed to do with protected resources.

|   |                                                                                                 |
| - | ----------------------------------------------------------------------------------------------- |
|   | Settings for your own custom resources might vary from those used as examples in this use case. |

1. In the PingOne admin console, go to **Applications > Resources** and click the **[icon: plus, set=fa]**icon.

2. Add the test resource:

   1. Name the resource `test`, enter `https://ig.example.com:8443/mcp` for the **Audience**, and click **Next**.

   2. Click the **Gear** icon ([icon: gear, set=fa]) next to the `sub` attribute, enter the expression `#root.context.requestData.subjectToken.sub`, and click **Save**.

      Attribute mappings can pass complex information to applications through an access token. This expression copies the user's `sub` (subject) claim from the incoming subject token to let downstream services know which human the agent is acting on behalf of. Learn more about expressions in [Using the expression builder](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_use_expression_builder.html) in the PingOne documentation.

   3. Click **+ Add** and name the attribute `act`.

   4. Click [icon: gear, set=fa]next to the `act` attribute, enter the following expression, and click **Save**.

      `(#root.context.requestData.subjectToken.may_act.sub == #root.context.requestData.actorToken.client_id)?#root.context.requestData.subjectToken.may_act:null`

      This expression copies the `may_act` delegation from the user's token into `act` when the delegated client ID matches the current agent's `client_id`. When there isn't a match, `act` is left empty to prevent unauthorized delegation.

   5. Click **Next**, then click **+ Add Scope**.

   6. Name the scope `test` and click **Save**.

   7. Click the **test** resource to display the **Overview** tab.

   8. Copy the **Resource ID** and **Client Secret** and store them somewhere convenient. You'll use them for PingGateway configuration.

   9. Close the **test** resource.

3. Add the agent resource:

   1. Click the **[icon: plus, set=fa]**icon.

   2. Name the resource `agent`, keep the default `agent` for the **Audience**, and click **Next**.

   3. For the `sub` attribute, select **Username** in the **PingOne Mappings** list.

   4. Click **+ Add** and name the attribute `may_act`.

   5. Click [icon: gear, set=fa]next to the `may_act` attribute, enter the following expression, and click **Save**.

      `(#root.context.requestData.grantType == "client_credentials")?null:({ "sub": #root.context.appConfig.clientId })`

      This expression omits `may_act` for pure `client_credentials` requests, and otherwise builds a simple delegation object that records this agent's `client_id` as the subject of `may_act`.

   6. Click **Next**, then click **+ Add Scope**.

   7. Name the scope `agent` and click **Save**.

### Adding a consent agreement

Add an agreement for the user's consent for agent actions. You can find more details in [Agreements](https://docs.pingidentity.com/pingone/user_experience/p1_agreements.html) and [Adding an agreement](https://docs.pingidentity.com/pingone/user_experience/p1_add_an_agreement.html) in the PingOne documentation.

1. In the PingOne admin console, go to **User Experience > Agreements** and click the **[icon: plus, set=fa]**icon.

2. Name the agreement `Agent Consent` and enter a description such as `Consent for a digital assistant agent`.

3. For **Reconsent Every**, select **Number of Days** and keep the default `180`.

4. Click **Save**.

5. Add a language:

   1. Click **Edit Localized Content** and click the **Languages +** icon.

   2. For **Language**, select **English (en)**, and click **Save**.

   3. In **Localized Agreement Content**, enter `I consent to allow digital assistants created by MyCompany to act on my behalf`, then click **Save**.

      The language is enabled by default.

   4. Close the language.

6. On the **Agreements page**, click the toggle to enable the **Agent Consent** agreement.

### Adding an authentication policy

Add an authentication policy for the agent. The authentication policy ensures that users explicitly agree to let a digital assistant act on their behalf before any delegated access is granted. By prompting for consent during sign-on, PingOne can issue user tokens that record this approval, which token exchange uses later to build the `act` and `may_act` claims. This keeps delegation transparent, auditable, and aligned with least-privilege and human-in-the-loop (HITL) requirements. Learn more in [Adding an authentication policy](https://docs.pingidentity.com/pingone/authentication/p1_add_an_auth_policy.html) in the PingOne documentation.

1. In the PingOne admin console, go to **Authentication > Authentication** and click **+ Add Policy**.

2. Name the policy `Agent-Consent-Login`.

3. For **Step Type**, select **Login**, then click **+ Add step**.

4. For **Step Type**, select **Agreement Prompt**.

5. Select the **Agent Consent** terms of service agreement and click **Save**.

### Adding an AI agent

Register the agent as an identity in PingOne and configure its authentication settings, such as scopes for the actions the agent can perform. You can find more details in [Managing AI agents](https://docs.pingidentity.com/pingone/ai_agents/p1_managing_ai_agents.html) in the PingOne documentation.

In our example scenario, the agent will interact with an application hosted locally, on the 3000 port.

1. In the PingOne admin console, go to **AI Agents** and click the **[icon: plus, set=fa]**icon.

2. Name the agent `MCP Tutorial`, enter a description such as `MCP agent for PingGateway tutorial`, and click **Save**.

3. On the **Configuration** tab, click the **Pencil** icon ([icon: pencil, set=fa]) to edit configuration settings.

   |   |                                   |
   | - | --------------------------------- |
   |   | Keep all of the default settings. |

   1. For **Grant Type**, select **Client Credentials**, **Refresh Token**, and **Token Exchange**.

      These settings allow the agent to authenticate autonomously and exchange user tokens for delegation tokens at runtime.

   2. In **Redirect URIs**, enter `http://localhost:3000/callback`.

   3. Click **Save**.

4. On the **Resources** tab, click the **Pencil** icon ([icon: pencil, set=fa]) to edit resource settings:

   1. Select the **agent** and **test** scopes.

      These scopes ensure that the agent can get its own access token and exchange user tokens for MCP access.

   2. Click **Save**.

5. On the **Policies** tab, click **+ Add Policies**.

   1. Select the **Agent-Consent-Login** policy.

   2. Click **Save**.

6. Click the toggle at the top of the panel to enable the agent.

7. On the **Overview** tab, copy the **Client ID** and store it somewhere convenient. You'll use it when restarting the MCP agent.

#### Result

You've successfully configured PingOne to act as the authorization server.

### Configuring PingGateway

PingGateway serves as the enforcement point that protects the MCP server and validates tokens.

1. In the `admin.json` file for PingGateway, enable streaming:

   ```json
   "streamingEnabled": true
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This is already enabled in the example `admin.json` file you set up as a prerequisite. PingGateway requires this setting for server-side events (SSE), an MCP transport option. Learn more about [server-side events (SSE)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) in the Mozilla documentation. |

2. Export a RESOURCE_SECRET_ID environment variable with the base64 encoded client secret for the PingOne test resource:

   ```bash
   bash: export RESOURCE_SECRET_ID=$(echo -n "<Resource client secret>" | base64)
   ```

   |   |                                         |
   | - | --------------------------------------- |
   |   | Make sure you don't include a new line. |

3. Add the following route to PingGateway:

   * Linux

     `$HOME/.openig/config/routes/mcp.json`

   * Windows

     `%appdata%\OpenIG\config\routes\mcp.json`

   > **Collapse: Route configuration**
   >
   > Enter the `PingOne environment ID` and `PingOne test resource ID` for your deployment.
   >
   > ```json
   > {
   >   "name": "mcp",
   >   "condition": "${find(request.uri.path, '^/mcp')}",
   >   "properties": {
   >     "pingOneEnvID": "https://auth.pingone.com/<PingOne environment ID>",
   >     "pingOneResourceID": "<PingOne test resource ID>",
   >     "gatewayUrl": "https://ig.example.com:8443",
   >     "mcpServerUrl": "http://localhost:8000"
   >   },
   >   "baseURI": "&{mcpServerUrl}",
   >   "heap": [
   >     {
   >       "name": "SystemAndEnvSecretStore-1",
   >       "type": "SystemAndEnvSecretStore"
   >     },
   >     {
   >       "name": "AuditService",
   >       "type": "AuditService",
   >       "config": {
   >         "eventHandlers": [
   >           {
   >             "class": "org.forgerock.audit.handlers.json.JsonAuditEventHandler",
   >             "config": {
   >               "name": "json",
   >               "logDirectory": "&{ig.instance.dir}/audit",
   >               "topics": ["access", "mcp"]
   >             }
   >           }
   >         ]
   >       }
   >     },
   >     {
   >       "name": "rsFilter",
   >       "type": "OAuth2ResourceServerFilter",
   >       "config": {
   >         "requireHttps": false,
   >         "scopes": ["test"],
   >         "accessTokenResolver": {
   >           "type": "TokenIntrospectionAccessTokenResolver",
   >           "config": {
   >             "endpoint": "&{pingOneEnvID}/as/introspect",
   >             "providerHandler": {
   >               "type": "Chain",
   >               "config": {
   >                 "filters": [
   >                       {
   >                         "type": "HttpBasicAuthenticationClientFilter",
   >                         "config": {
   >                           "username": "&{pingOneResourceID}",
   >                           "passwordSecretId": "resource.secret.id",
   >                           "secretsProvider": "SystemAndEnvSecretStore-1"
   >                         }
   >                       }
   >                     ],
   >                 "handler": "ForgeRockClientHandler"
   >               }
   >             }
   >           }
   >         }
   >       }
   >     }
   >   ],
   >   "handler": {
   >     "type": "Chain",
   >     "config": {
   >       "filters": [
   >         {
   >           "type": "McpAuditFilter",
   >           "config": {
   >             "auditService": "AuditService"
   >           }
   >         },
   >         {
   >           "type": "UriPathRewriteFilter",
   >           "config": {
   >             "mappings": { "/mcp": "/" }
   >           }
   >         },
   >         {
   >           "type": "McpProtectionFilter",
   >           "config": {
   >             "resourceId": "&{gatewayUrl}/mcp",
   >             "authorizationServerUri": "&{pingOneEnvID}/as",
   >             "resourceServerFilter": "rsFilter",
   >             "supportedScopes": ["test"],
   >             "resourceIdPointer": "/aud/0"
   >           }
   >         },
   >         {
   >           "type": "McpValidationFilter",
   >           "config": {
   >             "acceptedOrigins": ".*"
   >           }
   >         }
   >       ],
   >       "handler": {
   >         "type": "ReverseProxyHandler",
   >         "config": {
   >           "soTimeout": "20 seconds"
   >         }
   >       }
   >     }
   >   }
   > }
   > ```
   >
   > Features of the sample route:
   >
   > * This route uses a secret obtained from an environment variable.
   >
   > * PingGateway acts as an OAuth 2.0 resource server (RS) when protecting the sample MCP server.
   >
   > * The [McpAuditFilter](https://docs.pingidentity.com/pinggateway/latest/reference/McpAuditFilter.html) audits MCP requests. PingGateway records MCP audit events in an `audit/mcp.audit.json` file.
   >
   > * The [UriPathRewriteFilter](https://docs.pingidentity.com/pinggateway/latest/reference/UriPathRewriteFilter.html) sends the request to the root resource of the MCP server. The MCP server expects requests at `/`.
   >
   > * The [McpProtectionFilter](https://docs.pingidentity.com/pinggateway/latest/reference/McpProtectionFilter.html) uses the RS configuration, extending it for MCP.
   >
   > * PingGateway validates MCP requests with an [McpValidationFilter](https://docs.pingidentity.com/pinggateway/latest/reference/McpValidationFilter.html).
   >
   > * The [ReverseProxyHandler](https://docs.pingidentity.com/pinggateway/latest/reference/ReverseProxyHandler.html) uses a long `"soTimeout"` setting to accommodate an MCP agent receiving few or infrequent SSE updates.

4. Restart PingGateway to apply the route changes.

5. (Optional) Add [throttling](https://docs.pingidentity.com/pinggateway/latest/reference/ThrottlingPolicies.html) or fine-grained access control as necessary to meet your security requirements.

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | This simple route doesn't include those features. |

6. Check the PingGateway log to verify the route loads successfully.

#### Result

You've successfully configured PingGateway to protect the sample MCP server.

### Start the MCP agent

1. In the directory where you unpacked the sample MCP agent, export the AI agent secret as an environment variable called AGENT_SECRET.

2. Start the sample MCP agent again with the added option `–client id`.

   You'll need the client ID from the [MCP Tutorial agent](#idai-add-p1-agent). Point it to the PingGateway route for MCP requests.

   ```bash
   bash-3.2$ export AGENT_SECRET=yjS0IWMX9LS91...
   bash-3.2$ python3 sample-mcp-agent.py --client-id <PingOne AI agent client ID> --mcp-server-url https://ig.example.com:8443/mcp
   ```

#### Result

You've successfully started the sample MCP agent.

## Validation

To validate this use case, you'll confirm the full flow:

* The agent can discover tools from the MCP server.

* The agent can open a browser and redirect to PingOne.

* The user can sign on and grant consent.

* The agent can make a tool call and receive a response.

* PingGateway logs show the MCP request with a valid act claim.

With PingGateway protecting the MCP server, the sample MCP agent directs you to the authorization server to sign on as an end user and authorize access to make MCP requests.

1. Allow the agent to open a browser automatically, or:

   1. Select `'n'`.

   2. Copy the authorization URL that the sample MCP agent displays in your terminal.

   3. Paste the URL into a browser.

      The URL should look similar this:

      ```
      https://auth.pingone.com/082e56dd-1a0f-4e1d-a28e-77d51ecf1705/as/authorize?response_type=code&client_id=3fffb1bf-106c-4449-a9bd-df6fa76d8f41&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fcallback&state=…
      ```

2. Sign on as the test user and consent to allow a digital assistant (if asked) before you close the browser tab.

   The following commands are available in the terminal where the sample MCP agent is running:

   ```
   [INFO] Discovered tools [https://ig.example.com:8443/mcp]:
   [INFO] - geocode: Returns a list of objects containing city name, latitude, longitude, country, admin1 (region), and timezone for each matching city
   [INFO] - forecast_daily: Returns a multi-day weather forecast for a given location
   [INFO] - forecast_periods: Returns weather forecasts for each representative period of the current day
   [INFO] - forecast_hourly: Returns an hourly weather forecast for the current day
   [INFO] - weather_at_time: Returns the forecasted weather for a specific time at a given location

   Enter your message (or 'exit|quit|q'):
   ```

3. Enter a prompt and get a response from the MCP server through PingGateway, then exit the agent.

   The following example uses the forecast_daily tool to get the daily forecast for Tokyo:

   ```
   Enter your message (or 'exit|quit|q'): What is the daily forecast for Tokyo?
   Agent: The daily forecast for Tokyo is:

   <MCP server response with forecast details>

   Enter your message (or 'exit|quit|q'): exit
   User requested exit. Goodbye!
   ```

   The following tokens are used in the transaction:

   * Actor token: The AI agent's access token.

     > **Collapse: Agent token (actor token) example**
     >
     > ```json
     > {
     >   "aud": [
     >     "agent"
     >   ],
     >   "client_id": "adeeb901-7b64-453d-92bc-059bcbcc5958",
     >   "env": "4631af52-7ec7-48cf-848f-48cf8ca8e1ab",
     >   "exp": 1774043329,
     >   "iat": 1774039729,
     >   "iss": "https://auth.pingone.com/4631af52-7ec7-48cf-848f-48cf8ca8e1ab/as",
     >   "jti": "722238d2-4748-4681-889d-7fe7a321b037",
     >   "org": "84c4c0c0-0ca2-43b4-a62c-d830882855bc",
     >   "p1.rid": "722238d2-4748-4681-889d-7fe7a321b037",
     >   "scope": "agent"
     > }
     > ```

   * Subject token: The end user's access token. The `may_act` claim asserts that the agent is allowed to act on the user's behalf.

     > **Collapse: User token (subject token) example**
     >
     > ```json
     > {
     >   "acr": "Agent-Consent-Login",
     >   "aud": [
     >     "agent"
     >   ],
     >   "auth_time": 1774039361,
     >   "client_id": "adeeb901-7b64-453d-92bc-059bcbcc5958",
     >   "env": "4631af52-7ec7-48cf-848f-48cf8ca8e1ab",
     >   "exp": 1774043333,
     >   "iat": 1774039733,
     >   "iss": "https://auth.pingone.com/4631af52-7ec7-48cf-848f-48cf8ca8e1ab/as",
     >   "jti": "3121e22a-5958-4bf1-a369-ba296b444930",
     >   "may_act": {
     >     "sub": "adeeb901-7b64-453d-92bc-059bcbcc5958"
     >   },
     >   "org": "84c4c0c0-0ca2-43b4-a62c-d830882855bc",
     >   "p1.userId": "cf025143-501a-4d70-9c80-95d69121d7b3",
     >   "scope": "agent",
     >   "sid": "2dd6d4a4-0b59-4c99-8a57-4c189f09b24f",
     >   "sub": "demouser"
     > }
     >
     > [INFO] Exchanging actor token and subject token for a new mcp token (scope='test')
     > ```

   * MCP token: An on-behalf-of token obtained through PingOne token exchange. The `act` and `sub` claims assert that this token is used by the agent on behalf of the test user.

     > **Collapse: Exchanged on-behalf-of token (mcp token) example**
     >
     > ```json
     > {
     >   "acr": "Agent-Consent-Login",
     >   "act": {
     >     "sub": "adeeb901-7b64-453d-92bc-059bcbcc5958"
     >   },
     >   "aud": [
     >     "https://ig.example.com:8443/mcp"
     >   ],
     >   "auth_time": 1774039361,
     >   "client_id": "adeeb901-7b64-453d-92bc-059bcbcc5958",
     >   "env": "4631af52-7ec7-48cf-848f-48cf8ca8e1ab",
     >   "exp": 1774043333,
     >   "iat": 1774039733,
     >   "iss": "https://auth.pingone.com/4631af52-7ec7-48cf-848f-48cf8ca8e1ab/as",
     >   "jti": "e1e90599-b09f-4549-8ea9-6a297490e53c",
     >   "org": "84c4c0c0-0ca2-43b4-a62c-d830882855bc",
     >   "p1.userId": "cf025143-501a-4d70-9c80-95d69121d7b3",
     >   "scope": "test",
     >   "sid": "2dd6d4a4-0b59-4c99-8a57-4c189f09b24f",
     >   "sub": "demouser"
     > }
     > ```

     |   |                                                                                                                                                           |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | You can decode tokens using your preferred JSON Web Token (JWT) viewer. Don't paste sensitive tokens from production environments into third-party sites. |

   If your delegation token is missing the `act` claim, verify:

   * PingOne resource attribute mappings for act are configured correctly.

   * The subject token contains a `may_act` claim.

   * The agent's `client_id` matches `may_act.sub`.

4. Check the PingGateway log for additional details about the MCP request.

### Result

You've successfully validated that PingGateway can protect the MCP server.

## Troubleshooting

If you encounter issues while configuring this use case, use the following information to help resolve common problems.

### Token exchange fails and `act` claim is null

Verify that the attribute expressions in your custom resources accurately match client IDs and that the `act` claim is properly mapped in the token.

### PingGateway drops MCP traffic

Verify that `streamingEnabled` is set to true in your `admin.json` file. PingGateway requires this setting for SSE utilized by the MCP protocol.

### Gateway routing errors

Verify that the UriPathRewriteFilter is properly stripping the `/mcp` path down to `/` before it reaches the backend MCP server, as most MCP servers expect requests at the root.

### Consent prompt issues

If the user doesn't receive an agent consent prompt, verify these things in PingOne:

* The Agent-Consent-Login policy is assigned to the agent on the **Policies** tab in **AI Agents**.

* The **Redirect URI** is correct on the **Configuration** tab in **AI Agents**.

If the user receives a consent prompt on every sign-on, verify these things in PingOne:

* The **Reconsent Every** interval isn't too short. You can edit the interval on the **Overview** tab in **User Experience > Agreements**.

* Scopes aren't changing between sessions.

### Agent can list tools but not call them

Verify the following:

* The MCP scope (**test** in the example) isn't missing or incorrect.

* The PingGateway route includes MCP filters and the **Resource ID** is configured correctly.

## What's next

Add fine-grained authorization policies to secure agent actions using real-time contextual signals. Learn more about [authorization](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_introduction.html) in the PingOne Authorize documentation.

---

---
title: Securing digital assistants
description: Secure AI agents using explicit agent identity, delegation with OAuth 2.0 token exchange, and an agent gateway for least-privilege enforcement.
component: identity-for-ai
page_id: identity-for-ai:use-cases:idai-securing-digital-assistants
canonical_url: https://developer.pingidentity.com/identity-for-ai/use-cases/idai-securing-digital-assistants.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-16T00:06:46Z
keywords: ["Identity for AI", "ai identity", "ai security", "ai agent", "personal agent", "digital assistant", "digital worker"]
page_aliases: ["tutorials:idai-authorizing-agents-aic.adoc", "identity:idai-securing-digital-assistants.adoc"]
section_ids:
  key-concepts: Key concepts
  how-this-works: How this works
  whats-next: What's next
---

# Securing digital assistants

Secure your organization's AI-driven digital assistants by treating them as first-class identities, distinct from the humans they act on behalf of, and enforcing least-privilege access at runtime.

AI agents are serving both consumers and employees (for example, as chatbots on retail websites helping users navigate products, and as workforce assistants managing employee calendars and drafting emails). Securing these assistants means verifying not just what the agent is doing, but whose identity and permissions it's exercising at any given moment. Runtime identity distinguishes the agent from the human while ensuring the agent has explicit authority to act on the user's behalf.

## Key concepts

* Explicit agent identity

  Register every digital assistant as a unique identity with its own credentials and lifecycle. This enables centralized management of your agents, their owners, and their resource permissions from a single console across your customer and workforce use cases.

* Delegation, not impersonation

  Using OAuth 2.0 token exchange, agents swap a user's token for a delegation token that has an `act` (actor) claim, explicitly identifying both the user and the agent. The actor claim provides a clear audit trail of which agent took what action, enabling enforcement decisions at runtime based on both the user and the agent. The agent never sees the user's credentials.

* Least-privilege permissions

  The delegation token is short-lived and might require additional token exchanges as the agent performs new actions or accesses different resources. Audience restriction ensures the token is only valid at a specific resource server, preventing acceptance of unauthorized tokens.

* Runtime Enforcement

  The agent gateway acts as a security proxy, validating tokens and enforcing fine-grained policies before an agent can reach backend resources such as APIs or Model Context Protocol (MCP) servers. The gateway provides a consistent security layer for AI developers building on MCP or traditional REST architectures.

## How this works

As an example scenario, consider a chatbot embedded in a banking app. Customers use the chatbot to retrieve account balances and make transactions. Acting on behalf of the customer, the chatbot accesses backend account resources.

![Diagram showing the request flow from users to an AI agent requesting access to a resources secured by the agent gateway.](_images/idai-agent-flow-simple.png)

To secure these interactions, an authorization server issues and exchanges tokens. An agent gateway validates the tokens, acting as a security proxy in front of account resources.

Example process flow:

![UML diagram of token exchange flow for an AI agent secured with an authorization server and agent gateway.](_images/idai-agent-flow-general.png)

1. **User authentication**: The customer signs on to the banking app and receives an initial access token (the subject token).

2. **Request for action**: The customer asks the chatbot for their account balance. The banking app passes the customer's subject token to the chatbot.

3. **Token exchange**: The chatbot sends the customer's token and its own credentials (the actor token) to the authorization server.

4. **Issuance of delegation token**: The authorization server issues a new, short-lived token. This token includes the customer as the `sub` (subject) and the chatbot in the `act` (actor) claim.

5. **Gateway validation**: The chatbot sends the request to the backend. The agent gateway intercepts the call, validates the `act` claim, the user (`sub`), and target resource (`aud`), and ensures the chatbot has the specific scope (`account:read_balance`) required for the task.

6. **Secure execution**: The backend account API processes the request, knowing exactly which agent performed the action for which user.

A delegation token issued by the authorization server carries a precise record of the delegation:

```json
{
  "iss": "https://as.example.com",
  "aud": "https://acount.api.example.com",
  "sub": "customer@example.com",
  "act": {
    "sub": "https://bank-agent.example.com"
  },
  "scope": "account:read_balance",
  "iat": 1742200000,
  "exp": 1742200300
}
```

The token contains the following claims:

| Claim     | Description                                                   |
| --------- | ------------------------------------------------------------- |
| `sub`     | The human user who authorized the action.                     |
| `act.sub` | The AI agent performing the action.                           |
| `scope`   | Constrained permissions granted to the agent for this action. |
| `aud`     | Restricts the token to a specific downstream resource.        |

The delegation token provides downstream services with everything they need for authorization decisions: who is the human, who is the agent, what are they allowed to do, and how to trace this specific action.

Ping Identity authorization servers that support this scenario include PingOne, PingOne Advanced Identity Cloud, and Ping Identity software, such as PingFederate and PingAM. PingGateway serves as the agent gateway.

## What's next

Get started with your preferred platform:

* [Securing AI agents with PingOne using delegation and least privilege](idai-securing-agents-pingone.html)

* [Securing AI Agents with PingFederate using delegated access tokens](idai-securing-agents-pingfed.html)