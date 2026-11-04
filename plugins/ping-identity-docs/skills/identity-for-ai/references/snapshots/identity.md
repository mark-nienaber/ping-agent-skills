---
title: Agent types
description: Classify AI agents into types (personal agents, digital assistants, and digital workers) and learn their identity security implications.
component: identity-for-ai
page_id: identity-for-ai:identity:idai-agent-types
canonical_url: https://developer.pingidentity.com/identity-for-ai/identity/idai-agent-types.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-16T00:06:46Z
keywords: ["Identity for AI", "ai identity", "ai security", "ai governance", "ai compliance", "ai agent", "ai agent types", "personal agent", "digital assistant", "digital worker"]
page_aliases: ["index.adoc"]
section_ids:
  personal-agents: Personal agents
  digital-assistants-for-consumers: Digital assistants for consumers
  digital-assistants-for-workforce: Digital assistants for workforce
  digital-workers: Digital workers
---

# Agent types

Artificial intelligence (AI) agents open up a new channel for businesses to engage with customers. As multiple agents collaborate to complete requests, understanding each agent type is critical for ensuring security and maintaining trust.

Not all agents are equal, and the identity implications vary depending on who manages the agent, where the agent is deployed, and the purpose of the agent.

![A graphic describing the difference between personal agents, digital assistants for consumers, digital assistants for workforce, and digital workers.](_images/idai-agent-types.png)

Ping Identity categorizes agents into four types, each serving a distinct use case with its own trust and security considerations:

* [Personal agents](#personal-agents)

* [Digital assistants for consumers](#digital-assistants-for-consumers)

* [Digital assistants for workforce](#digital-assistants-for-workforce)

* [Digital workers](#digital-workers)

These types can also be classified based on the level of control you have:

* Unmanaged agents

  Agents that operate outside your organization's trust boundary, such as a user's personal agent. These agents interact with your services but aren't governed or controlled by your organization.

* Managed agents

  Agents that your organization creates and controls. You can monitor their activity, enforce policies, and grant access to sensitive resources as needed. Managed agents include digital assistants and digital workers.

In the following sections, we'll discuss what distinguishes each agent type and the identity challenges associated with each. We'll also explore how Ping Identity brings together existing and new identity and access management (IAM) concepts to secure agentic identities.

## Personal agents

A personal agent can be accessed on your device and perform a wide array of tasks for you. For example, you might prompt ChatGPT to aggregate the best flight deals between airlines.

Personal agents are unmanaged agents that are governed by a third party.

In this case, the agent lies outside of your organization's trust boundary.

The following diagram shows a simplified flow of a personal agent interacting with your services:

![A diagram showing a personal agent interacting with an identity provider.](_images/idai-personal-agent-flow.png)

Since the agent above could come from anywhere, it's operating outside of the organizational trust boundary. If your organization is an insurance company, the interactions in the flow could resemble the following:

1. A user prompts their personal agent, such as ChatGPT, to shop for the latest deals on car insurance.

2. The agent attempts to access that user's account in your organization to look at their existing policy. Your organization uses Ping Identity as their identity provider and authorization server (AS), and you require the agent to be dynamically registered with the AS and tied to an end user. With the user registered with Ping Identity, the OAuth 2.0 client requires human-in-the-loop (HITL), meaning it requires the user to approve this access.

3. The user completes an authentication journey.

4. After the user authenticates successfully, the AS issues minimally scoped tokens back to the agent.

5. With an access token, the agent can now access the user's current insurance rate information.

## Digital assistants for consumers

Digital assistants for consumers are customer-facing agents owned by an organization to help users complete specific tasks, such as a chatbot that assists with booking an appointment.

Unlike a personal agent, a digital assistant is a managed agent that's created and governed by your organization. They interact directly with users, but often require access to protected information to complete user requests.

The following diagram details high-level interactions between the digital assistant for consumers agent, the end user, and an organization's backend resources. It doesn't delve into how to securely integrate Model Context Protocol (MCP) servers just yet.

![A diagram showing a digital assistant interacting with an end user and an organization's backend resources.](_images/idai-digital-assistants-for-consumers-flow.png)

Compared to the personal agent, the digital assistant is now within the organizational trust boundary. An organization would create their digital assistant agent, and then preregister it using Ping Identity as the IdP and AS.

In this example, your organization is again an insurance company. This time, you want to create a digital assistant chatbot on your website. The chatbot must be able to access the backend resources and APIs required to assist customers while ensuring that:

* The user authenticates and approves the chatbot's actions.

* The chatbot operates with only the permissions granted by the user.

* You can monitor the chatbot's activities (logging and auditing).

|   |                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Chatbots and agents aren't inherently secure. They shouldn't be given user credentials, user tokens, or long-lived tokens. Instead, register them with their own identity, and use short-lived tokens to access protected resources. |

The flow is as follows:

1. With the chatbot registered with Ping Identity as an OAuth 2.0 client, the end user prompts the chatbot to change their payments from every 6 months to a monthly basis.

2. The chatbot doesn't have sufficient access to perform this change, so it interacts with Ping Identity as the IdP through the Client Credentials grant flow to gain the necessary tokens.

3. With Ping Identity as the IdP and the AS, the flow requires a HITL interaction to grant tokens. With Client-Initiated Backchannel Authentication (CIBA), the end user is sent a push notification, and they approve the action of the chatbot.

4. Ping Identity issues tokens.

5. The chatbot receives the tokens.

6. The chatbot sends the request to the MCP server with the tokens to access protected resources.

7. The MCP server accesses the backend API to update the user's payment plan.

## Digital assistants for workforce

Digital assistants for workforce are similar to digital assistants for consumers. They're agents managed by your organization, they need to access backend resources to perform tasks on behalf of the user, and they'll use MCP and Agent2Agent (A2A) protocol to do so.

However, digital assistants for workforce are targeted internally to increase the efficiency of an organization. For example, an organization might implement a HR digital assistant to help employees submit time-off requests.

Now, both the agent and the user are within the organizational trust boundary, as the end user is an employee within the organization's purview.

## Digital workers

A digital worker is a managed agent that's semi-autonomous to fully autonomous within an enterprise designed to perform internal tasks.

Similar to an intern with a simple set of tasks who checks in periodically to ensure they're on the right path, a digital worker performs tasks on its own and checks in with a human when required.

For example, let's say you create a digital worker to manage inventory and coordinate logistics. This digital worker can reason and understand external factors that influence the quantity and cadence of inventory purchases. The digital worker is completely within your organization's trust boundary. It requires:

* Its own identity and set of credentials to perform actions as itself.

* Depending on business requirements, a human supervisor to approve certain actions.

Consider the following diagram:

![A diagram showing a digital worker interacting with a human in the loop, an IdP, and web services.](_images/idai-digital-workers-flow.png)

1. Just as an end user would, the digital worker signs on with Ping Identity as the IdP and AS.

2. After signing on, the worker receives appropriately scoped tokens to access purchasing and manage inventory.

   The worker also accesses the organization's web app to interact and view the status of delivery on inventory.

3. For high-sensitivity transactions, a HITL interaction is required. Additionally, the worker is monitored just like a human user to ensure that the worker has the minimal access it needs to perform its tasks.

---

---
title: Identifying agents with token exchange
description: Use OAuth 2.0 token exchange to identify AI agents in a delegation chain with nested act claims, creating an audit trail back to the human user.
component: identity-for-ai
page_id: identity-for-ai:identity:idai-token-exchange
canonical_url: https://developer.pingidentity.com/identity-for-ai/identity/idai-token-exchange.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-16T00:06:46Z
keywords: ["Identity for AI", "ai identity", "ai security", "ai governance", "ai compliance", "ai agent", "ai agent types", "personal agent", "digital assistant", "digital worker"]
section_ids:
  the-value-of-preserving-the-delegation-chain: The value of preserving the delegation chain
  token-exchange-in-an-agent-to-agent-flow: Token exchange in an agent-to-agent flow
  configuring-token-exchange-with-ping-identity: Configuring token exchange with Ping Identity
---

# Identifying agents with token exchange

In a standard OAuth flow, an application might impersonate a user, holding a token that allows it to do anything a user can do. This makes the application's behavior indistinguishable from user-performed actions. In complex agentic architectures (where multiple AI agents are collaborating with each other), this is dangerous, especially if rogue agent activity cannot be traced.

The OAuth 2.0 Token Exchange protocol ([RFC 8693](https://www.rfc-editor.org/rfc/rfc8693.html)) defines how to apply the concept of delegation to token exchange. The advantage of delegation over other approaches, such as secret vault retrieval, is that an agent never possesses live credentials. An agent only possesses a finely-scoped access token after the end user triggers token exchange.

## The value of preserving the delegation chain

Token exchange supports two essential pillars of agentic systems: accountability and authorization.

First, the delegation chain provides a complete audit trail. Rather than agent activity appearing as if it were performed by the user, the `sub` and `act` claims preserve who acted on whose behalf. Combined with security telemetry, this allows for a full story behind each action, making agent actions attributable and traceable. In other words, a token can show "I'm Agent A, and I'm performing a specific action requested by Agent B, to complete a task for User C."

Second, this context enables more precise authorization decisions. A resource server can evaluate not only what the user is allowed to do, but also whether a particular agent is allowed to do it for the user. This allows policies to account for not only the user, but also the specific actors involved.

## Token exchange in an agent-to-agent flow

The following graphic illustrates an agent-to-agent flow, where multiple agents are working together and communicating with a Model Context Protocol (MCP) server to solve a problem on behalf of the user.

![A diagram showing each step of token exchange between a user, two agents, and an MCP server.](_images/idai-token-exchange.png)

The key to this flow is the `act` (actor) claim within the JSON Web Token (JWT). With each new agent authentication, a new `act` claim is appended, creating a nested audit trail of collaboration between agents and servers.

The following describes each authentication in the flow:

1. User authentication

   The process begins with a human user authenticating with an identity provider (IdP) to use an agent.

   * **The exchange:** Ping Identity (the IdP) issues a JWT.

   * **Key claims:**

     * `sub` (subject): user\@example.com (The human).

     * `aud` (audience): https\://agent1.example.com (The "orchestrator" agent the human is communicating with).

   * **Meaning:** The user is interacting directly with agent 1, so there is no `act` claim yet.

2. Agent 1 delegates to agent 2

   Agent 1 needs to offload a task to agent 2. Agent 1 can't just pass the user's token because that token is scoped for agent 1, not agent 2.

   * **The exchange:** Agent 1 contacts the IdP and requests token exchange. It presents the user's token and asks for a new token valid for agent 2.

   * **Key claims:**

     * `sub`: user\@example.com (Still the user).

     * `aud`: https\://agent2.example.com (Now valid for agent 2).

     * The `act` claim:

       ```json
       "act":
       {
         "sub":"https://agent1.example.com",
       }
       ```

   * **Meaning:** Agent 1 is the actor requesting agent 2 to perform a task on behalf of the user.

3. Agent 2 delegates to MCP server

   Agent 2 now needs to access a tool or resource through an MCP server.

   * **The exchange:** Agent 2 sends the token it received from agent 1 to the IdP and requests a token scoped for the MCP server.

   * **Key claims:**

     * `sub`: user\@example.com (Still the user).

     * `aud`: https\://mcp-server1.example.com (Valid for the MCP server).

     * The nested `act` claim:

       ```json
       "act":
       {
         "sub":"https://agent2.example.com",
         "act":
         {
           "sub":"https://agent1.example.com",
         }
       }
       ```

   * **Meaning:** Now, agent 2 is the actor performing token exchange with the MCP server, having been triggered by agent 1. The user is still the original owner of the request.

This demonstrates a complete chain of delegation. Because every actor appends its own identifier at each stage of the flow, the final token distinguishes agent activity from the original human request, resulting in an audit trail of every action.

To complete the user's task, the MCP server will access the target resource server. This backend connection is typically authenticated using an API key, an access token, or a dedicated service account.

## Configuring token exchange with Ping Identity

The following product documentation covers token exchange configuration for each supported IdP:

* [PingAM](https://docs.pingidentity.com/pingam/latest/am-oauth2/token-exchange.html)

* [PingOne](https://docs.pingidentity.com/pingone/use_cases/p1_oauth_2_token_exchange.html)

* [PingOne Advanced Identity Cloud](https://docs.pingidentity.com/pingoneaic/am-oauth2/token-exchange.html)

* [PingFederate](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_oauth_exchange.html)

---

---
title: Securing an MCP server with PingGateway
description: Use PingGateway as a security gateway to intercept, validate, audit, and enforce OAuth 2.1 authorization on AI agent requests to MCP servers.
component: identity-for-ai
page_id: identity-for-ai:identity:idai-securing-mcp-servers-gateway
canonical_url: https://developer.pingidentity.com/identity-for-ai/identity/idai-securing-mcp-servers-gateway.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-10-01T13:02:33Z
keywords: ["MCP server", "MCP security", "AI security"]
page_aliases: ["agents:idai-securing-mcp-servers-gateway.adoc"]
---

# Securing an MCP server with PingGateway

When [securing any MCP server](idai-securing-mcp-servers-oauth.html), implementing an appropriate, consistent, documented, auditable, and adaptable security model can be challenging.

![PingGateway acts as an MCP gateway in your AI security architecture.](_images/idai-mcp-gateway.png)

In this architecture, PingGateway:

1. Intercepts and validates an MCP request from an AI agent to an MCP server. It optionally audits and throttles traffic.

2. Authorizes the AI agent request using OAuth 2.1.

3. Protects the MCP server by enforcing OAuth 2.1 scopes. It optionally acts as a policy enforcement point and transforms security tokens.

PingGateway addresses the challenges in protecting any MCP server by providing a unified layer to:

* Allow only valid MCP requests.

* Audit MCP requests and actors.

* Throttle request rates.

* Enforce coarse-grained OAuth 2.1 security controls.

* Enforce fine-grained access control policies.

* Perform token transformation mapped to your security models.

The [MCP security gateway](https://docs.pingidentity.com/pinggateway/latest/mcp/index.html) tutorial in the PingGateway documentation shows how to protect any MCP server using PingOne or PingOne Advanced Identity Cloud, both supported OAuth 2.1 authorization servers.

---

---
title: Securing MCP servers with OAuth 2.0
description: Best practices for securing MCP servers with OAuth 2.0, covering authorization server architectures and requirements.
component: identity-for-ai
page_id: identity-for-ai:identity:idai-securing-mcp-servers-oauth
canonical_url: https://developer.pingidentity.com/identity-for-ai/identity/idai-securing-mcp-servers-oauth.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-16T00:06:46Z
keywords: ["MCP server", "MCP security", "least privlege", "token lifecycle"]
page_aliases: ["agents:idai-securing-mcp-servers.adoc"]
section_ids:
  the-role-of-oauth-2-0: The role of OAuth 2.0
  authorization-server-architecture: Authorization server architecture
  authorization-server-requirements: Authorization server requirements
  learn-more: Learn more
---

# Securing MCP servers with OAuth 2.0

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

  Learn more about the [Authorization code grant](https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-authz-grant.html) in the Advanced Identity Cloud documentation.

* **Proof Key for Code Exchange (PKCE)**: PKCE is important for public clients, such as AI agents running in browsers or user devices, that can't safely store a client secret. By requiring a dynamically generated code verifier and challenge, PKCE mitigates code interception attacks during the Authorization Code Flow.

  Learn more about the [Authorization code grant with PKCE](https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-authz-grant-pkce.html) in the Advanced Identity Cloud documentation.

* **Dynamic Client Registration (DCR)**: DCR enables new AI agents to onboard without manual administrative intervention. This is critical in environments where agents are created dynamically or updated frequently. DCR enables automatic provisioning of credentials and redirect URIs in a standardized, secure way.

  Learn more about [Dynamic client registration](https://docs.pingidentity.com/pingoneaic/am-oidc1/oauth2-dynamic-client-registration.html) in the Advanced Identity Cloud documentation.

* **Fine-grained scopes and claims**: Your authorization server should allow granular token scopes and claims to ensure tokens issued to AI agents follow the principle of least privilege. For example, one agent might require the `prices:read` scope, while another requires the `orders:write` scope. Narrow scopes reduce negative impact if a token is exposed or misused.

  Learn more about [Scopes](https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-scopes.html) in the Advanced Identity Cloud documentation.

* **Token introspection and UserInfo endpoints**: Downstream services integrated with the MCP server often need to validate tokens before serving requests. [Introspection](https://datatracker.ietf.org/doc/html/rfc7662) and [UserInfo](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo) endpoints allow the MCP server to verify token status, audience, and claims, ensuring that expired, revoked, or mis-scoped token are rejected.

  You can find information about OAuth 2.0 endpoints supported by Advanced Identity Cloud in [OAuth 2.0 endpoints](https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-client-endpoints.html) in the Advanced Identity Cloud documentation.

## Learn more

Use the following resources in the MCP specification to learn more about securing MCP servers:

* [Authorization](https://modelcontextprotocol.io/specification/draft/basic/authorization)

* [Security Best Practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)