---
title: Computer-Using Agents (CUAs)
description: A computer-using agent (CUA) is an AI agent that operates computers through human interfaces like GUIs or CLIs, rather than structured APIs.
component: identity-for-ai
page_id: identity-for-ai:agents:idai-computer-using-agents
canonical_url: https://developer.pingidentity.com/identity-for-ai/agents/idai-computer-using-agents.html
revdate: October 9, 2025
keywords: ["computer-using agents", "AI agent", "GUI automation", "CLI automation", "browser automation"]
section_ids:
  how-cuas-differ-from-api-driven-agents: How CUAs differ from API-driven agents
---

# Computer-Using Agents (CUAs)

A computer-using agent (CUA) is an agent that operates a computer like a human would, interacting with graphical user interfaces (GUIs) and command-line interfaces (CLIs) instead of structured APIs.

Using techniques like computer vision and accessibility hooks to navigate screens, CUAs can simulate mouse clicks, keystrokes, or terminal commands to perform tasks.

## How CUAs differ from API-driven agents

The following table highlights key differences between API-driven agents and CUAs across identity, security, and operational categories. This comparison shows why CUAs introduce unique security challenges compared to API-based approaches.

| Category                     | API-driven agents                                                     | CUAs                                                                  |
| ---------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Interface type               | Structured, machine-readable APIs                                     | Human-facing GUIs and CLIs                                            |
| Stability and resilience     | Predictable, versioned, and contract-based                            | Minor UI changes can easily break workflows                           |
| Authentication model         | Modern standards such as OAuth 2.0, OIDC, or workload identities      | Human-style logins (usernames, passwords, shared bot accounts)        |
| Authorization model          | Fine-grained, least-privilege policies enforceable at the API layer   | Broad access after sign-on; difficult to constrain privileges         |
| Auditability and attribution | Actions tied to unique workload identities or service principals      | Shared accounts reduce accountability and audit clarity               |
| Execution environment        | Cloud-native or service-based runtimes                                | Local desktops, VMs, or RDP sessions                                  |
| Security posture             | Supports IAM-native controls (short-lived tokens, conditional access) | Often relies on long-lived sessions vulnerable to hijacking or replay |
| Best suited for              | Modern systems with robust API coverage                               | Legacy, desktop, or closed-source applications without APIs           |

---

---
title: MCP servers and OAuth 2.0
description: When using MCP servers as an interface between AI agents and external tools, follow authentication and authorization best practices.
component: identity-for-ai
page_id: identity-for-ai:agents:idai-securing-mcp-servers
canonical_url: https://developer.pingidentity.com/identity-for-ai/agents/idai-securing-mcp-servers.html
revdate: February 5, 2026
keywords: ["MCP server", "MCP security", "least privlege", "token lifecycle"]
section_ids:
  the-role-of-oauth-2-0: The role of OAuth 2.0
  authorization-server-architecture: Authorization server architecture
  authorization-server-requirements: Authorization server requirements
  learn-more: Learn more
---

# MCP servers and OAuth 2.0

When connecting artificial intelligence (AI) agents to external tools with the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro), you should ensure that each MCP server enforces sufficient authentication and authorization. Following security best practices helps protect sensitive data, prevent unauthorized access, and maintain trust in agentic workflows.

With MCP, the same modularity and flexibility that enables interoperability between agents and tools also carries considerable security risks. Developers face the following challenges when building secure MCP servers and tools:

* **Overly permissive access tokens**: Static or long-lived tokens can grant overly broad access to all tools. If these tokens are compromised, they could allow unrestricted access to tools. To prevent this, use scoped, short-lived tokens or OAuth 2.0 flows with refresh mechanisms to limit exposure.

* **Insufficient authorization checks**: Authentication alone isn't enough. MCP servers must enforce fine-grained authorization to ensure clients only access capabilities they have permissions for. To adhere to least-privilege principles, apply access policies on a per-tool and per-action basis.

* **Potentially unsafe tools**: Registered tools can introduce vulnerabilities if not properly vetted. Limit tool registration to trusted sources and consider capability restrictions to mitigate risk.

## The role of OAuth 2.0

OAuth 2.0 plays a pivotal role in securing MCP servers by providing a standardized framework for authentication and authorization. By leveraging OAuth 2.0, MCP servers can ensure that only authorized clients access tools, resources, and prompts.

### Authorization server architecture

There are different ways to implement OAuth 2.0 with MCP, depending on the architecture and responsibilities of each component:

* Native authorization server

  The MCP server can act as an OAuth 2.0 authorization server, directly handling:

  * Authorization code issuance.

  * Token generation and refresh.

  * Scope-based access control.

  This approach gives the MCP server full control over security and the token lifecycle, but it requires deeper infrastructure and policy management.

* Proxy to external authorization server

  The MCP server exposes standard OAuth 2.0 endpoints (`/authorize`, `/token`) but proxies requests to an external authorization server, such as PingOne Advanced Identity Cloud. This architecture enables:

  * Seamless integration with existing identity providers.

  * Delegation of token issuance and verification.

  * Use of familiar login and consent mechanisms.

* Agent redirected to external authorization server

  The MCP server doesn't directly expose OAuth 2.0 endpoints. Instead, it:

  * Instructs the client agent to begin the OAuth 2.0 flow with an external authorization server.

  * Relies on the client agent to manage tokens and present them back to the MCP server.

  This architecture minimizes operational burden for the MCP server by entrusting the agent with token security and refresh logic.

### Authorization server requirements

When deploying an MCP server for AI agents, your choice of authorization server is critical to ensuring secure client onboarding, token issuance, and delegated access. The authorization server should support the following:

* **Authorization Code Flow**: This flow ensures that AI agents acting as confidential clients can securely exchange authorization codes for tokens, reducing the risk of token exposure when compared to implicit flows. This flow provides a secure foundation for agent-user interactions.

  Learn more about the [Authorization code grant](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant.html) in the Advanced Identity Cloud documentation.

* **Proof Key for Code Exchange (PKCE)**: PKCE is important for public clients, such as AI agents running in browsers or user devices, that can't safely store a client secret. By requiring a dynamically generated code verifier and challenge, PKCE mitigates code interception attacks during the Authorization Code Flow.

  Learn more about the [Authorization code grant with PKCE](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant-pkce.html) in the Advanced Identity Cloud documentation.

* **Dynamic Client Registration (DCR)**: DCR enables new AI agents to onboard without manual administrative intervention. This is critical in environments where agents are created dynamically or updated frequently. DCR enables automatic provisioning of credentials and redirect URIs in a standardized, secure way.

  Learn more about [Dynamic client registration](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/oauth2-dynamic-client-registration.html) in the Advanced Identity Cloud documentation.

* **Fine-grained scopes and claims**: Your authorization server should allow granular token scopes and claims to ensure tokens issued to AI agents follow the principle of least privilege. For example, one agent might require the `prices:read` scope, while another requires the `orders:write` scope. Narrow scopes reduce negative impact if a token is exposed or misused.

  Learn more about [Scopes](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-scopes.html) in the Advanced Identity Cloud documentation.

* **Token introspection and UserInfo endpoints**: Downstream services integrated with the MCP server often need to validate tokens before serving requests. [Introspection](https://datatracker.ietf.org/doc/html/rfc7662) and [UserInfo](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo) endpoints allow the MCP server to verify token status, audience, and claims, ensuring that expired, revoked, or mis-scoped token are rejected.

  You can find information about OAuth 2.0 endpoints supported by Advanced Identity Cloud in [OAuth 2.0 endpoints](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-client-endpoints.html) in the Advanced Identity Cloud documentation.

## Learn more

Use the following resources in the MCP specification to learn more about securing MCP servers:

* [Authorization](https://modelcontextprotocol.io/specification/draft/basic/authorization)

* [Security Best Practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)

---

---
title: Secure a Cloudflare Workers MCP server with PingFederate
description: The Cloudflare Workers Model Context Protocol (MCP) server functions as a resource server within the OAuth architecture. It validates incoming requests and facilitates token exchange, ensuring secure communication between the MCP client and downstream APIs.
component: identity-for-ai
page_id: identity-for-ai:agents:idai-securing-cloudflare-pingfed
canonical_url: https://developer.pingidentity.com/identity-for-ai/agents/idai-securing-cloudflare-pingfed.html
section_ids:
  how-does-it-work: How does it work?
  authentication-and-client-bootstrapping: Authentication and client bootstrapping
  cloudflare-agents-state-and-transport: Cloudflare agents (state and transport)
  mcp-sdk-tool-logic: MCP SDK (tool logic)
  before-you-begin: Before you begin
  tasks: Tasks
---

# Secure a Cloudflare Workers MCP server with PingFederate

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

\<https\://players.brightcove.net/771836189001/default\_default/index.html?videoId=6387820424112>

---

---
title: Secure a Cloudflare Workers MCP server with PingOne
description: In this configuration, the Cloudflare Workers Model Context Protocol (MCP) server uses the Cloudflare Workers OAuth Provider, which delegates authentication to PingOne. This enables clients, such as AI agents, to call a protected API on behalf of an authenticated end user.
component: identity-for-ai
page_id: identity-for-ai:agents:idai-securing-cloudflare-pingone
canonical_url: https://developer.pingidentity.com/identity-for-ai/agents/idai-securing-cloudflare-pingone.html
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

# Secure a Cloudflare Workers MCP server with PingOne

In this configuration, the Cloudflare Workers Model Context Protocol (MCP) server uses the Cloudflare Workers OAuth Provider, which delegates authentication to PingOne. This enables clients, such as AI agents, to call a protected API on behalf of an authenticated end user.

|   |                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | While serving as a resource server for MCP clients, this MCP server also fulfills two distinct OAuth roles:- An OAuth server to your MCP clients

- An OpenID Connect (OIDC) client for your PingOne environment |

This configuration uses Cloudflare to manage consent. To use this configuration with PingOne DaVinci-managed consent, refer to [Secure a Cloudflare Workers MCP server with PingOne DaVinci](idai-securing-cloudflare-davinci.html).

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

   2. **PKCE Enforcement** is set to **S256\_REQUIRED**.

   3. **Redirect URI** is set to your Cloudflare worker's callback endpoint, for example `<mcp_server>/callback`.\
      If the worker is not yet deployed, use a placeholder and update it later.

4. On the **Resources** tab of the application, allow the standard OIDC scopes, `openid` and `profile`, and the Todo API scopes, `todo_api:read` and `tode_api:write`.

5. On the **Policies** tab of the application, enable **Single\_Factor** or your preferred policy.

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

\<https\://players.brightcove.net/771836189001/default\_default/index.html?videoId=6387826562112>

---

---
title: Secure a Cloudflare Workers MCP server with PingOne Advanced Identity Cloud
description: In this configuration, the Cloudflare Workers Model Context Protocol (MCP) server delegates authentication to PingOne Advanced Identity Cloud. This enables clients, such as AI agents, to call a protected API on behalf of an authenticated end user.
component: identity-for-ai
page_id: identity-for-ai:agents:idai-securing-cloudflare-aic
canonical_url: https://developer.pingidentity.com/identity-for-ai/agents/idai-securing-cloudflare-aic.html
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

# Secure a Cloudflare Workers MCP server with PingOne Advanced Identity Cloud

In this configuration, the Cloudflare Workers Model Context Protocol (MCP) server delegates authentication to PingOne Advanced Identity Cloud. This enables clients, such as AI agents, to call a protected API on behalf of an authenticated end user.

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

   | Name                        | Description                                        | Example                                             |
   | --------------------------- | -------------------------------------------------- | --------------------------------------------------- |
   | PING\_AIC\_ISSUER           | PingOne Advanced Identity Cloud environment domain | `https://<ENV>.forgeblocks.com:443/am/oauth2/alpha` |
   | MCP\_SERVER\_URL            | URL of the deployed MCP server                     | `https://remote-mcp-ping-aic.<ENV>.workers.dev`     |
   | MCP\_SERVER\_CLIENT\_ID     | ID of the MCP server client                        | `mcp_server`                                        |
   | MCP\_SERVER\_CLIENT\_SECRET | Secret of the MCP server client                    | `[A long, random, alphanumeric string]`             |
   | API\_URL                    | URL of the downstream Todo API                     | `https://todo-api-ping-aic.<ENV>.workers.dev`       |

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

   ![A screenshot of the MCP Inspector initiating authentication and self-registering with Advanced Identity Cloud.](_images/idai-mcp-inspector-connect.png)

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

   * The subject token retains the user's full, broader permissions. The delegation token is limited to only whats necessary for its target audience.

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

\<https\://players.brightcove.net/771836189001/default\_default/index.html?videoId=6387779240112>

---

---
title: Secure a Cloudflare Workers MCP server with PingOne DaVinci
description: In this configuration, the Cloudflare Workers Model Context Protocol (MCP) server uses the Cloudflare Workers OAuth Provider, which delegates authentication to PingOne DaVinci. This enables clients, such as AI agents, to call a protected API on behalf of an authenticated end user.
component: identity-for-ai
page_id: identity-for-ai:agents:idai-securing-cloudflare-davinci
canonical_url: https://developer.pingidentity.com/identity-for-ai/agents/idai-securing-cloudflare-davinci.html
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

# Secure a Cloudflare Workers MCP server with PingOne DaVinci

In this configuration, the Cloudflare Workers Model Context Protocol (MCP) server uses the Cloudflare Workers OAuth Provider, which delegates authentication to PingOne DaVinci. This enables clients, such as AI agents, to call a protected API on behalf of an authenticated end user.

|   |                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | While serving as a resource server for MCP clients, this MCP server also fulfills two distinct OAuth roles:- Acts as an OAuth Server to your MCP clients

- Acts as an OpenID Connect (OIDC) Client to your PingOne environment |

This configuration uses DaVinci to manage consent. To use this configuration with Cloudflare-managed consent, see [Secure a Cloudflare Workers MCP server with PingOne](idai-securing-cloudflare-pingone.html).

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

   2. **PKCE Enforcement** is set to **S256\_REQUIRED**.

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

![A screenshot of the DaVinci flow in PingOne.](_images/idai-davinci-mcp-flow.png)

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

![A screenshot of the DaVinci flow in PingOne.](_images/idai-mcp-inspector-dv.png)

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

\<https\://players.brightcove.net/771836189001/default\_default/index.html?videoId=6387777951112>

---

---
title: Secure an MCP server with PingGateway
description: Secure any MCP server with PingGateway.
component: identity-for-ai
page_id: identity-for-ai:agents:idai-securing-mcp-servers-gateway
canonical_url: https://developer.pingidentity.com/identity-for-ai/agents/idai-securing-mcp-servers-gateway.html
revdate: February 10, 2026
keywords: ["MCP server", "MCP security", "AI security"]
---

# Secure an MCP server with PingGateway

When [securing any MCP server](idai-securing-mcp-servers.html), implementing an appropriate, consistent, documented, auditable, and adaptable security model can be challenging.

![PingGateway acts as an MCP gateway in your AI security architecure.](_images/idai-mcp-gateway.png)

In this architecture, PingGateway:

1. Intercepts and validates an MCP request from an AI agent to an MCP server. It optionally audits and throttles traffic.

2. Authorizes the AI agent request using OAuth 2.0.

3. Protects the MCP server by enforcing OAuth 2.0 scopes. It optionally acts as a policy decision point and transforms security tokens.

PingGateway addresses the challenges in protecting any MCP server by providing a unified layer to:

* Allow only valid MCP requests.

* Audit MCP requests and actors.

* Throttle request rates.

* Enforce coarse-grained OAuth 2.0 security controls.

* Enforce fine-grained access control policies.

* Perform token transformation mapped to your security models.

The [MCP security gateway](https://docs.pingidentity.com/pinggateway/latest/mcp/index.html) tutorial in the PingGateway documentation shows how to protect any MCP server with PingOne Advanced Identity Cloud acting as the OAuth 2.0 authorization server.

---

---
title: Secure AWS Bedrock AgentCore Identity with the Ping Identity Platform
description: You can integrate Ping Identity's identity providers (IdPs) with AWS Bedrock AgentCore Identity to secure agent-based workloads.
component: identity-for-ai
page_id: identity-for-ai:agents:idai-securing-aws-ping
canonical_url: https://developer.pingidentity.com/identity-for-ai/agents/idai-securing-aws-ping.html
section_ids:
  goals: Goals
  aws-bedrock-agentcore-identity-model: AWS Bedrock AgentCore Identity model
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

# Secure AWS Bedrock AgentCore Identity with the Ping Identity Platform

You can integrate Ping Identity's identity providers (IdPs) with AWS Bedrock AgentCore Identity to secure agent-based workloads.

Specifically, you can configure each IdP, PingOne, PingOne Advanced Identity Cloud, and PingFederate, as an:

* Inbound IdP for AgentCore Gateway and Runtime

  This enables agents to authenticate and authorize end users using OpenID Connect (OIDC) tokens issued by Ping Identity.

* Outbound credential provider for AgentCore Identity

  This enables agents to securely obtain OIDC access tokens from Ping Identity in order to call downstream APIs and protected resources.

## Goals

* Centralize authentication and authorization for Bedrock AgentCore agents using the Ping Identity Platform.

* Enforce consistent OIDC controls such as audience (`aud`) validation, scopes, and grant types across inbound and outbound agent interactions.

* Support both user-based flows (authorization code grants) and machine-to-machine flows (client credentials grants) as defined in the AWS Bedrock AgentCore Identity model.

This aligns with AWS's recommended IdP integration pattern for AgentCore, as described in the [AWS Bedrock AgentCore Identity documentation](https://docs.aws.amazon.com/bedrock-agentcore/), and demonstrates how Ping Identity products act as both trusted token issuers and credential providers within agent-based architectures.

## AWS Bedrock AgentCore Identity model

AWS Bedrock AgentCore Identity provides a standardized mechanism for:

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

7. Create a custom resource.

   1. Go to Applications > Resources and click the [icon: plus, set=fa]icon to create a new resource.

   2. In the **Resource Name** field, enter a name for the resource, and then click **Next**.

   3. In the **PingOne Mappings** list, select a value to map to the `sub` attribute, and the click **Next**.

   4. Click **+ Add Scope+** to define a scope and assign it to the application.

   5. Click **Save**.

   |   |                                                                                          |
   | - | ---------------------------------------------------------------------------------------- |
   |   | You will set this resource name as the `aud` claim for Client Credentials access tokens. |

8. Configure the AgentCore inbound authentication:

   1. In the **Discovery URL** field, enter the **OIDC Discovery Endpoint** value from the **Overview** tab on the PingOne application details pane.

   2. In the **Allowed Audiences** field, enter the resource name you created in [step 7](#create-resource).

You can find more information in the [PingOne API documentation](http://developer.pingidentity.com/pingone-api/).

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

   1. In the **Discovery URL** field, enter the **OIDC Discovery Endpoint** from the **Sign-On** tab.

   2. In the **Allowed Audiences** field, enter the **Client ID**.

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

3. Go to System > OAuth Settings > Scope Management and create one or more scopes.

4. Go to Applications > OAuth > Access Token Management and configure the `aud` claim by setting the **Audience Claim Value**.

5. Allow the client to request the appropriate scopes and grant types.

6. Configure AgentCore inbound authentication:

   1. Set **Discovery URL** to `https://<PINGFED_SERVER_HOSTNAME>/.well-known/oauth-authorization-server`.

   2. Set **Allowed Audiences** to the configured audience value.

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

You've successfully integrated PingOne, PingOne Advanced Identity Cloud, or PingFederate with AWS Bedrock AgentCore Identity and can apply consistent enterprise identity controls to AI agents.

---

---
title: Tools
description: Agents can extend their capabilities with external tools.
component: identity-for-ai
page_id: identity-for-ai:agents:idai-tools-intro
canonical_url: https://developer.pingidentity.com/identity-for-ai/agents/idai-tools-intro.html
revdate: April 23, 2026
keywords: ["AI agents", "tools", "external tools", "APIs", "services", "Model Context Protocol", "MCP", "Agent-to-Agent", "A2A", "security", "reasoning", "knowledge sources", "action tools"]
section_ids:
  why-tools-matter: Why tools matter
  integration-with-protocols: Integration with protocols
  idai-mcp-and-a2a: How MCP and A2A work together
---

# Tools

Artificial intelligence (AI) agents can extend their capabilities far beyond static training data by leveraging external tools to autonomously solve complex, real-world tasks. Tools are external functions, services, or APIs that an agent can invoke to perform specific actions, retrieve information, or augment reasoning.

## Why tools matter

Tools allow AI agents to perform tasks that would be difficult using only their built-in knowledge. With tools, agents can:

* Access up-to-date information

  Tools enable agents to query external knowledge sources in real time. For example, an agent might:

  * Query a company's internal database to check a customer's policy details

  * Access a public API to retrieve the latest stock prices

* Perform actions on behalf of users

  Agents can interact with systems or services to execute tasks, such as:

  * Scheduling a meeting through a calendar API

  * Sending an email

  * Booking travel arrangements through an external service API

* Enhance reasoning and decision-making

  Agents can leverage specialized tools to improve accuracy and efficiency, including:

  * Calculators or logic solvers for precise computation

  * Vector databases for semantic search or similarity queries

  * Analytics or simulation engines to evaluate complex scenarios

## Integration with protocols

To ensure secure, auditable, and trustworthy tool usage, agents rely on protocols such as Model Context Protocol (MCP) and Agent-to-Agent (A2A).

* MCP

  MCP provides a standardized framework for agents to discover and invoke tools securely. It enforces identity, authorization, and trust boundaries.

  For example, an agent calling a sensitive HR API would require MCP-managed credentials and scopes to perform the action safely.

  Learn more in [What is Model Context Protocol (MCP)?](idai-what-is-mcp.html)

* A2A

  Sometimes an agent delegates a subtask to another agent instead of calling a traditional API. The same security and trust principles apply: the calling agent must authenticate, obtain authorization, and interact according to organizational policies.

  Learn more in [What is Agent2Agent Protocol (A2A)?](idai-what-is-a2a.html)

### How MCP and A2A work together

The emerging landscape of AI agents requires efficient collaboration and specialization. Complex tasks require not only individual agents but cohesive teams of agents, each excelling in a specific domain. MCP and A2A are the keys to enabling this sophisticated ecosystem.

Rather than competing standards, these two protocols are complementary. Each addresses a distinct, yet essential layer of the agentic architecture. An agent primarily uses A2A to communicate with other agents and MCP to interact with its specific tools and resources.

Think of MCP as vertical integration, that is, how a single agent interacts with the external world of tools, data, and APIs. It acts as the agent's nervous system, standardizing the connection between a Large Language Model (LLM) and the resources required to complete a task.

In contrast, A2A addresses horizontal integration, which is how independent, autonomous agents communicate and collaborate as peers. A2A is the backbone of multi-agent architecture, governing the agent-to-agent communication that enables complex, multi-step workflows.

The following diagram illustrates how MCP and A2A work together to enable a seamless workflow from collaboration to execution:

![A diagram showing the relationship between a user, an orchestrating agent, and sub-agents.](_images/idai-a2a-and-mcp.png)

* Orchestration with A2A

  A complex user request first goes to an orchestrating agent. This agent uses A2A to delegate sub-tasks to specialized peer agents. For example, a travel agent might use A2A to communicate with a flight agent and a hotel agent.

* Execution with MCP

  Each specialized agent, having received its delegated task, uses MCP internally to perform the specific steps. The flight agent uses MCP to call the airline API tool to check prices, book a flight, and so on.

* Reporting with A2A

  The specialized agents package the results of the tool executions as artifacts and return them to the orchestrating agent using the A2A protocol. The orchestrating agent synthesizes these results to provide a comprehensive, final answer back to the user.

By leveraging MCP and A2A capabilities, agents can access information, perform tasks, and collaborate with other agents while maintaining security, user consent, and auditability.

---

---
title: What Are AI Agents?
description: AI agents are systems that can act autonomously on behalf of a user or another system to complete tasks.
component: identity-for-ai
page_id: identity-for-ai:agents:idai-what-are-agents
canonical_url: https://developer.pingidentity.com/identity-for-ai/agents/idai-what-are-agents.html
revdate: May 13, 2026
keywords: ["ai", "ai agents", "large language models", "agentic workflows", "multi-agent architecture"]
page_aliases: ["index.adoc"]
section_ids:
  architecture: Architecture
  core-components: Core components
  large-language-models: Large language models
  tools: Tools
  memory: Memory
  prompts: Prompts
  workflows: Workflows
  single-agent-workflow: Single-agent workflow
  multi-agent-workflow: Multi-agent workflow
  agent-lifecycle: Agent lifecycle
  use-cases: Use cases
  learn-more: Learn more
---

# What Are AI Agents?

Artificial intelligence (AI) agents are systems that can act autonomously on behalf of a user or another system to complete tasks.

Unlike other AI models that only generate or predict text, agents combine reasoning, memory, and the capacity for real-world action. These capabilities allow agents to interact dynamically with external systems, maintain context across sessions, and solve complex problems with minimal human intervention.

## Architecture

Agent architectures define how intelligence, memory, and action are organized into a functioning system. At the highest level, they specify where reasoning occurs, how agents coordinate, and how external systems integrate.

### Core components

Agents are built from several core components. Each component plays a distinct role in turning user goals into real-world solutions. Together, they provide the reasoning, context, and execution layers that make agents more than just large language models (LLMs).

![Diagram of core agent components](_images/idai-agent-components.png)

#### Large language models

An LLM is the reasoning engine of an agent. It performs the high-level cognitive tasks that define an agent's intelligence, including natural language processing, reasoning, planning, and decision making.

The LLM interprets user goals and determines when and how to call on other components, such as tools or memory, to complete a task.

#### Tools

Instead of relying solely on static training data, agents use tools to interact dynamically with the world. Tools are external functions, services, or APIs that an agent invokes to perform specific actions. This can include retrieving up-to-date information from the web, querying a database, sending an email, executing code, or interacting with a third-party application.

An LLM decides when and how to invoke a tool by generating a structured command. The agent's runtime executes this command, bridging the gap between language prediction and real-world action.

Agents integrate with tools in the following ways:

* **Direct-to-interface**: The agent interacts directly with a service through a well-defined interface, such as an API endpoint or an SDK library.

* **Abstract intention**: The agent expresses an intention, and a mediation layer such as Model Context Protocol (MCP) translates this intention into an API call.

Learn more about tool calling in [Tools](idai-tools-intro.html).

#### Memory

Memory provides agents with the ability to store and retrieve information from previous interactions, enabling them to maintain context and handle stateful, multistep tasks. Without memory, each agent interaction would be independent and isolated, limiting the agent's ability to perform complex work.

* **Short-term memory**: Keeps track of the current conversation or task, ensuring continuity. For example, remembering what the user asked three steps earlier in a workflow.

* **Long-term memory**: Stores knowledge over time, such as user preferences, historical actions, or facts relevant to recurring tasks. Long-term memory enables agents to improve across sessions and adapt to individual users.

#### Prompts

Prompts define how an LLM interprets and responds to tasks. They provide instructions, context, and constraints that shape agent behavior. In agentic systems, prompts aren't limited to user input. They can also include system prompts (defining role, goals, or style) and dynamically generated prompts (created as the agent reasons through steps).

Well-designed prompts serve as the operating instructions that guide the agent's reasoning.

### Workflows

The structure of an agentic workflow depends on the number of agents involved, how responsibilities are delegated, and how coordination is managed. Two common patterns are single-agent workflows and multi-agent workflows.

#### Single-agent workflow

In a single-agent workflow, one LLM manages reasoning, tool use, and memory. This model is simple to deploy and delivers quick results because there's no orchestration overhead. It works best for narrow, task-driven scenarios such as scheduling meetings, resolving straightforward support tickets, or generating reports. Although efficient, a single agent could struggle with problems that span multiple domains or require deeper specialization.

#### Multi-agent workflow

Multi-agent workflows distribute tasks across specialized agents that collaborate to reach an outcome. A coordinator or manager agent often handles communication and delegation. This model mirrors human teamwork and excels in complex, multi-domain scenarios.

For example, one agent might gather research, another summarize findings, and a third generate tailored recommendations. In business contexts, agents might divide responsibilities across data extraction, compliance checks, and payment processing.

## Agent lifecycle

Agents operate in a reasoning-action loop that enables them to interpret user input, determine a course of action, and dynamically adapt based on results.

1. **Input**: The process begins with a user instruction, system event, or scheduled task.

2. **Interpretation**: The LLM processes the input, consulting short-term memory to maintain continuity with previous interactions.

3. **Reasoning**: The agent evaluates next steps, determining whether the task requires external tools, additional context, or further reasoning.

4. **Action**: If the agent requires external data or capabilities, it invokes a tool to perform a specific action, such as querying long-term memory or triggering an integration.

5. **Observation**: The agent processes the retrieved context and incorporates it into its reasoning.

6. **Feedback**: The agent evaluates whether the outcome meets the intended objective. If not, it refines its reasoning or actions in the next cycle.

7. **Response**: The LLM generates a final response or executes the requested action.

8. **Memory update**: The agent stores relevant details so it can improve future interactions.

This loop is iterative. Agents repeat reasoning and action cycles until a satisfactory result is produced. By chaining together reasoning, action, and feedback, agents become continuously learning, adaptive assistants.

## Use cases

Agents are automating work and augmenting human decision making across industries. Examples of such applications:

| Use case                   | What the agent does                                                                                                                                                                                                | Example                                                                                                                                                                                                         |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Digital shopping assistant | Guides customers through a retail site by answering questions, recommending products, assisting with checkout, and tracking orders. Provides a conversational interface that personalizes the shopping experience. | A retail agent helps a customer find running shoes in their size, compares styles based on budget and activity, adds the chosen pair to the cart, applies a promo code, and provides delivery tracking updates. |
| Customer support           | Resolves common inquiries (password resets, billing, order tracking), maintains continuity across channels, and escalates complex cases with summaries.                                                            | An airline agent handles rebooking and baggage claims, while routing loyalty point or status discrepancies to live agents.                                                                                      |
| Personal productivity      | Manages scheduling, email triage, and travel bookings across apps. Acts directly on behalf of the user instead of just sending reminders.                                                                          | A personal agent summarizes daily email threads, drafts responses, and generates weekly travel itineraries.                                                                                                     |
| Business automation        | Orchestrates multi-step workflows like invoice validation, compliance checks, and HR onboarding. Adapts to system changes or exceptions.                                                                           | A bank agent automates compliance tasks, such as collecting documents, verifying identities, and escalating suspicious cases.                                                                                   |

## Learn more

Use the following resources to learn more about agent types and corresponding security challenges:

* [Agent Types](../identity/idai-agent-types.html)

* [Securing Digital Assistants](../use-cases/idai-securing-digital-assistants.html)

---

---
title: What is Agent2Agent Protocol (A2A)?
description: "Learn about Google's Agent to Agent protocol, which defines how AI agents interact with each other"
component: identity-for-ai
page_id: identity-for-ai:agents:idai-what-is-a2a
canonical_url: https://developer.pingidentity.com/identity-for-ai/agents/idai-what-is-a2a.html
revdate: October 9, 2025
keywords: ["identity for ai", "ai identity", "ai security", "ai governance", "agent to agent", "a2a"]
page_aliases: ["a2a:index.adoc"]
section_ids:
  why-use-a2a: Why use A2A?
  how-a2a-works: How A2A works
  workflow: Workflow
  learn-more: Learn more
---

# What is Agent2Agent Protocol (A2A)?

Whereas Model Context Protocol (MCP) defines how agents interact with tools, Google's [Agent2Agent Protocol (A2A)](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) defines how agents interact with each other.

In an ecosystem where agents exist in different domains and are built upon different frameworks, A2A defines a standardized way for agents to collaborate as autonomous peers. In practice, this means an HR agent could securely call out to a payroll agent to adjust a salary, or a travel agent could ask a calendar agent to reschedule meetings, all under a trusted, reliable framework.

## Why use A2A?

To make agent-to-agent communication as streamlined as possible, A2A is designed around the following core principles:

**Discovery:** Agents can find other agents with the desired permissions and capabilities.

**Interoperability:** Agents can pass goals, intents, and structured requests regardless of which framework they're built on.

**Delegation and Chaining:** Agents can hand off tasks to better-suited agents without the end user needing to manually orchestrate it.

**Trust and Identity:** As with tools, agents need to authenticate with each other. A2A defines how identity and permissions are enforced when agents collaborate.

## How A2A works

An A2A interaction involves the following components:

* Agent card

  A discoverable JSON file that acts as an agent's public profile. It advertises the agent's identity, capabilities, supported data modalities, and authentication requirements.

  This allows other agents to determine the most suitable agent to interact with.

* Task

  The fundamental unit of work. A task has a unique ID and progresses through a defined lifecycle, such as working, completed, or input required.

* Message and artifact

  Messages are the units of communication exchanged between agents to manage a task, while artifacts are the final, tangible outputs generated upon task completion.

### Workflow

The typical A2A workflow involves a client agent discovering an agent card, authenticating as required, and then monitoring tasks through a series of API exchanges until the remote agent delivers the artifacts to the end user.

1. A client agent, acting on behalf of the user, discovers an agent card. This could be through open discovery, a curated registry, or private API endpoints.

2. The client agent authenticates and receives a token from the remote agent's authorization server.

3. The client agent invokes the `POST /sendMessage` API to send details about the task along with its access token to the remote agent.

   The remote agent can respond with a `Message` object to negotiate the scope of a request or with a `Task` object if the agent accepts the task request, containing the `contextId` and `taskId`.

4. The client agent invokes the `POST /sendMessageStream` API with the remote agent for real-time updates of long-running tasks using Server-Sent Events (SSE).

   When the task is complete, the remote agent responds with the artifacts and the `taskId` in completed status.

## Learn more

Use the following resources to learn more about implementing A2A:

* [Agent2Agent (A2A) Protocol](https://a2a-protocol.org/dev/)

* [Tutorials and Samples](https://a2a-protocol.org/dev/tutorials/)

Together, MCP defines how agents call tools, while A2A defines how agents call each other. Both rely on strong Identity for AI to ensure that every request, whether to a tool or to another agent, is authenticated, authorized, and auditable. Learn more about how MCP and A2A interact in [A2A and MCP: Complementary Protocols for Agentic Systems](https://a2a-protocol.org/dev/topics/a2a-and-mcp/#a2a-mcp-complementary-protocols-for-agentic-systems).

---

---
title: What is Model Context Protocol (MCP)?
description: The Model Context Protocol introduces a standardized integration layer for agent-tool communication.
component: identity-for-ai
page_id: identity-for-ai:agents:idai-what-is-mcp
canonical_url: https://developer.pingidentity.com/identity-for-ai/agents/idai-what-is-mcp.html
revdate: April 30, 2026
keywords: ["model context protocol", "agent-tool integration", "capability discovery", "MCP", "tool connectors"]
section_ids:
  key-benefits: Key benefits
  architecture: Architecture
  workflow: Workflow
  security-challenges: Security challenges
---

# What is Model Context Protocol (MCP)?

The foundational challenge in scaling agentic systems is managing the connections between artificial intelligence (AI) agents and the vast array of tools they need to perform their work.

To solve real-world problems, AI agents require connections to external data and services, such as APIs and databases. Without a common standard, each integration must be written and maintained separately, creating brittle connections and duplicated effort. This approach doesn't scale, especially when multiple agents use the same tools.

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro), developed by Anthropic, addresses this challenge by standardizing how agents connect to tools. By providing a consistent layer for agent-tool interaction, MCP reduces friction for developers, simplifies maintenance, and creates a foundation for interoperable, secure agent ecosystems.

## Key benefits

MCP's standardized integration layer delivers:

* **Consistent connection semantics**: Developers can swap in a new tool without rewriting core integration logic.

* **Secure authentication and authorization**: MCP servers support OAuth 2.0, eliminating the need for hard-coded secrets or long-lived credentials.

* **Capability discovery**: Agents can automatically discover available tools, resources, and prompts instead of relying on hard-coded lists.

* **Reduced duplication**: Multiple agents can reuse the same MCP server, reducing the operational burden of maintaining separate connectors.

## Architecture

![Example agentic MCP flow](_images/idai-mcp-flow.png)

The MCP architecture includes three core components:

* MCP host

  The application that manages MCP clients and initiates connections to MCP servers. It provides the environment in which agents operate and interact with tools and resources. For example, an AI-powered IDE.

* MCP client

  The component inside the host that maintains a standardized connection with the MCP server. It acts as a bridge between the agent's reasoning and the server's tools, resources, and prompts. The client translates agent requests into MCP-compliant messages and processes server responses in a consistent way. For example, an embedded IDE client or chatbot agent connector.

* MCP server

  A program that exposes capabilities to AI applications in a standardized and discoverable way. It acts as the central repository of tools, resources, and prompts that agents can invoke. MCP servers support OAuth 2.0 for authentication and authorization, ensuring secure access, and can run locally within a host or remotely as a centralized service.

  An MCP server can expose three main types of capabilities:

  * **Tools**: Executable functions that an agent can invoke to perform specific actions.

  * **Resources**: Contextual data that informs agent reasoning, such as files, database records, or configuration information.

  * **Prompts**: Pre-defined, templated messages or workflows that agents can present to users or use internally to structure reasoning.

MCP's technical architecture is based on the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) message format. This ensures that all interactions, such as tool invocation, resource retrieval, and prompt execution, follow a consistent pattern. Each message contains a unique identifier, method name, and parameters.

## Workflow

A typical MCP workflow unfolds as part of an agent's reasoning-action loop:

1. **Initialization**: The MCP host launches an MCP client, which connects to the MCP server. The client queries the server for available tools, resources, and prompts. The agent inspects this metadata to understand which capabilities are available before taking action.

2. **Invocation**: When the agent determines that a specific tool or resource is needed, the MCP client sends a JSON-RPC request to the server, specifying the method and any required parameters.

3. **Execution**: The server applies authentication and authorization checks using OAuth 2.0 and least-privilege scopes, ensuring the client is permitted to execute the requested action. The server then performs the requested operation.

4. **Response**: Results are returned in a standardized JSON-RPC response. If an error occurs, the response includes a structured error object. The client relays the results to the agent, which incorporates them into its reasoning.

5. **Iteration**: Based on the results, the agent might issue additional MCP requests, chaining tool calls or resource queries to achieve higher-level goals. This iterative process allows the agent to refine its reasoning and dynamically adapt to changing conditions or new data.

6. **Observability & Logging** (Optional): Hosts or clients might log requests, responses, and execution traces to support debugging, auditing, or performance monitoring.

In the following example, an agent is connected to a support team's ticketing system. The MCP server exposes a tool called `searchTickets`, which lets agents query tickets by status, assignee, or other fields.

Suppose a support agent makes the following query to an AI agent:

Show me all my open tickets.

The LLM then processes this request and makes the following MCP call:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "searchTickets",
  "params": {
    "status": "open",
    "assignee": "me"
  }
}
```

* `method`: The MCP tool being called (`searchTickets`)

* `params`: The query parameters for filtering tickets

The MCP server returns a structured list of open tickets:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "ticketId": "123",
      "title": "Login issue",
      "priority": "high"
    },
    {
      "ticketId": "124",
      "title": "Billing discrepancy",
      "priority": "medium"
    }
  ]
}
```

The agent acting as the MCP client can now summarize tickets for the user, suggest next steps, or chain further requests by calling other MCP tools.

## Security challenges

While MCP streamlines tool integration, it also introduces new identity and security challenges. Each MCP server must enforce strong authentication and authorization to ensure only trusted clients can access tools and resources.

Common security challenges include:

* Configuring OAuth 2.0 correctly to avoid reliance on static secrets

* Implementing least-privilege scopes so agents can only access the data they need

* Securing multi-tenant MCP servers with fine-grained access control to prevent data leakage across users

* Protecting against denial-of-service with unbounded tool calls, and mitigating risks from prompt injection that could trigger malicious tool execution

Learn more about MCP security best practices in [MCP servers and OAuth 2.0](idai-securing-mcp-servers.html).