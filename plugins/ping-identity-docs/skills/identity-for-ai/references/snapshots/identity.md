---
title: Agent Types
description: Understanding each type of AI agent is paramount for identity security.
component: identity-for-ai
page_id: identity-for-ai:identity:idai-agent-types
canonical_url: https://developer.pingidentity.com/identity-for-ai/identity/idai-agent-types.html
revdate: April 30, 2026
keywords: ["identity for ai", "ai identity", "ai security", "ai governance", "ai compliance", "ai agent", "ai agent types", "personal agent", "digital assistant", "digital worker"]
page_aliases: ["index.adoc"]
section_ids:
  personal-agents: Personal agents
  digital-assistants-for-consumers: Digital assistants for consumers
  digital-assistants-for-workforce: Digital assistants for workforce
  digital-workers: Digital workers
---

# Agent Types

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
title: Identifying Agents with Token Exchange
description: Correctly implement token exchange in your flows to achieve delegation, not impersonation.
component: identity-for-ai
page_id: identity-for-ai:identity:idai-token-exhange
canonical_url: https://developer.pingidentity.com/identity-for-ai/identity/idai-token-exhange.html
revdate: December 22, 2025
keywords: ["identity for ai", "ai identity", "ai security", "ai governance", "ai compliance", "ai agent", "ai agent types", "personal agent", "digital assistant", "digital worker"]
---

# Identifying Agents with Token Exchange

In a standard OAuth flow, an application might impersonate a user, holding a token that allows it to do anything a user can do. This makes the application's behavior indistinguishable from user-performed actions. In complex agentic architectures (where multiple AI agents are collaborating with each other), this is dangerous, especially if rogue agent activity has an inaccurate audit trail.

The OAuth 2.0 Token Exchange protocol ([RFC 8693](https://www.rfc-editor.org/rfc/rfc8693.html)) defines how to apply the concept of delegation to token exchange. In simple terms, an agent's authentication token can show "I'm Agent A, and I'm performing a specific action requested by Agent B, to complete a task for User C."

This approach is superior to others, such as secret vault retrieval, as the agent never possesses live credentials. The agent only possesses a finely-scoped access token after the end user triggers token exchange.

The following graphic illustrates a daisy-chain of these delegations, where multiple agents are working together and communicating with a Model Context Protocol (MCP) server to solve a problem on behalf of the user.

![A diagram showing each step of token exchange between a user, two agents, an MCP server and a resource server.](_images/idai-token-exchange.png)

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

4. MCP server calls the resource server

   The MCP server now needs to access the resource server to complete the user's task.

   * **The exchange:** The MCP server presents its token from agent 2 and requests a new token scoped for the resource server.

   * **Key claims:**

     * `sub`: user\@example.com (Still the user).

     * `aud`: https\://resource-server.example.com (Valid for the resource server).

     * The nested `act` claim:

       ```json
       "act":
       {
         "sub":"https://mcp-server1.example.com",
         {
           "sub":"https://agent2.example.com",
           "act":
           {
             "sub":"https://agent1.example.com",
           }
         }
       }
       ```

This demonstrates a perfect call stack. Every actor has its own unique token that identifies who it was called by in each stage of the flow. This separates an agent's activity from a human's, and ensures every action is accurately accounted for.