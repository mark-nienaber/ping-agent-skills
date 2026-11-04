---
title: Computer-using agents (CUAs)
description: Learn about the identity and security challenges of computer-using agents (CUAs) that interact with GUIs and CLIs instead of APIs.
component: identity-for-ai
page_id: identity-for-ai:agents:idai-computer-using-agents
canonical_url: https://developer.pingidentity.com/identity-for-ai/agents/idai-computer-using-agents.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-16T00:06:46Z
keywords: ["computer-using agents", "AI agent", "GUI automation", "CLI automation", "browser automation"]
section_ids:
  how-cuas-differ-from-api-driven-agents: How CUAs differ from API-driven agents
---

# Computer-using agents (CUAs)

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
title: How agents use tools
description: Learn how AI agents use external tools to perform actions and access real-time data, and how MCP and A2A protocols secure and govern tool use.
component: identity-for-ai
page_id: identity-for-ai:agents:idai-tools-intro
canonical_url: https://developer.pingidentity.com/identity-for-ai/agents/idai-tools-intro.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-16T00:06:46Z
keywords: ["AI agents", "tools", "external tools", "APIs", "services", "Model Context Protocol", "MCP", "Agent-to-Agent", "A2A", "security", "reasoning", "knowledge sources", "action tools"]
section_ids:
  why-tools-matter: Why tools matter
  integration-with-protocols: Integration with protocols
  idai-mcp-and-a2a: How MCP and A2A work together
---

# How agents use tools

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

  Learn more in [What is Model Context Protocol (MCP)?](../protocols/idai-what-is-mcp.html)

* A2A

  Sometimes an agent delegates a subtask to another agent instead of calling a traditional API. The same security and trust principles apply: the calling agent must authenticate, obtain authorization, and interact according to organizational policies.

  Learn more in [What is Agent2Agent (A2A) protocol?](../protocols/idai-what-is-a2a.html)

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
title: What are AI agents?
description: Learn about AI agent architecture, core components, reasoning loops, multi-agent workflows, and how agents automate real-world tasks.
component: identity-for-ai
page_id: identity-for-ai:agents:idai-what-are-agents
canonical_url: https://developer.pingidentity.com/identity-for-ai/agents/idai-what-are-agents.html
llms_txt: https://developer.pingidentity.com/identity-for-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-10-19T23:38:26Z
keywords: ["ai", "ai agents", "large language models", "agentic workflows", "multi-agent architecture"]
page_aliases: ["index.adoc"]
section_ids:
  architecture: Architecture
  core-components: Core components
  large-language-model-llm: Large language model (LLM)
  tools: Tools
  context: Context
  prompts: Prompts
  workflows: Workflows
  one-agent: One agent
  multi-agent-and-a2a: Multi-agent and A2A
  agent-lifecycle: Agent lifecycle
  use-cases: Use cases
  learn-more: Learn more
---

# What are AI agents?

Artificial intelligence (AI) agents are systems that can act autonomously on behalf of a user or another system to complete tasks.

A large language model (LLM) generates and predicts text. Agents combine this with reasoning and context to perform real-world actions. These capabilities allow agents to interact dynamically with external systems, maintain context across sessions, and solve complex problems with minimal human intervention.

## Architecture

Agent architectures define how intelligence, context, and action are organized into a functioning system. At the highest level, they specify where reasoning occurs, how agents coordinate, and how external systems integrate.

### Core components

Agents are built from several core components. Each component plays a distinct role in turning user goals into real-world solutions. Together, they provide the reasoning, context, and execution layers that make agents more than just LLMs.

![Diagram of core agent components](_images/idai-agent-components.png)

#### Large language model (LLM)

An LLM is the reasoning engine of an agent. It performs the high-level cognitive tasks that define an agent's intelligence, including natural language processing, reasoning, planning, and decision making.

The LLM interprets user goals and determines when and how to call other components, such as tools or context, to complete a task.

#### Tools

Instead of relying solely on static training data, agents use tools to interact dynamically with the world. Tools are external functions, services, or APIs that an agent invokes to perform specific actions. This can include retrieving up-to-date information from the web, querying a database, sending an email, executing code, or interacting with a third-party application.

An LLM decides when and how to invoke a tool by generating a structured command. The agent's runtime executes this command, bridging the gap between language prediction and real-world action.

Agents integrate with tools in the following ways:

* **Direct-to-interface**: The agent interacts directly with a service through a well-defined interface, such as an API endpoint or an SDK library.

* **Abstract intention**: The agent expresses an intention, and a mediation layer such as Model Context Protocol (MCP) translates this intention into an API call.

Learn more about tool calling in [How agents use tools](idai-tools-intro.html).

#### Context

Context enables agents to maintain continuity across stateful, multistep tasks. Without context, each agent interaction would be independent and isolated, limiting the agent's ability to perform complex work. Because LLMs have a limited context window (the amount of text they can process at once), agents must carefully manage context.

* **Active context**: Keeps track of the current conversation or workflow. This is typically managed by passing recent interactions directly into the LLM's context window to ensure immediate continuity. For example, remembering what the user asked three steps earlier in the workflow.

* **Long-term context**: Stores historical knowledge, user preferences, and facts relevant to recurring tasks. When needed, the agent retrieves this data and injects it into the prompt, providing the LLM with relevant context without overwhelming its active context limits. Long-term context enables agents to improve across sessions and adapt to individual users.

#### Prompts

Prompts define how an LLM interprets and responds to tasks. They provide instructions, context, and constraints that shape agent behavior. In agentic systems, prompts aren't limited to user input. They can also include system prompts (defining role, goals, or style) and dynamically generated prompts (created as the agent reasons through steps).

Well-designed prompts serve as the operating instructions that guide the agent's reasoning.

### Workflows

The structure of an agentic workflow depends on the number of agents involved, how responsibilities are delegated, and how coordination is managed. Two common patterns are a workflow with one agent and an [Agent2Agent (A2A)](../protocols/idai-what-is-a2a.html) workflow.

#### One agent

In a workflow with one agent, only one LLM manages reasoning, tool use, and context. This model is simple to deploy and delivers quick results because there's no orchestration overhead. It works best for narrow, task-driven scenarios such as scheduling meetings, resolving straightforward support tickets, or generating reports. Although efficient, a single agent could struggle with problems that span multiple domains or require deeper specialization.

#### Multi-agent and A2A

Multi-agent workflows distribute tasks across specialized agents that collaborate to reach a shared outcome. This is typically powered by A2A orchestration, a mechanism that allows agents to directly communicate, delegate, and hand off tasks to one another.

In multi-agent environments, a coordinator or manager agent often oversees A2A interactions. This model mirrors human teamwork and excels in complex, multi-domain scenarios. For example, one agent might gather research, pass the data to another with A2A integration to summarize findings, and signal a third to generate tailored recommendations. In business contexts, this approach might divide agent responsibilities across data extraction, compliance checks, and payment processing.

## Agent lifecycle

Agents operate in a reasoning-action loop that enables them to interpret user input, determine a course of action, and dynamically adapt based on results.

1. **Input**: The process begins with a user instruction, system event, or scheduled task.

2. **Interpretation**: The LLM processes the input, consulting the active context to maintain continuity with previous interactions.

3. **Reasoning**: The agent evaluates next steps, determining whether the task requires external tools, additional context, or further reasoning.

4. **Action**: If the agent requires external data or capabilities, it invokes a tool to perform a specific action, such as querying long-term context or triggering an integration.

5. **Observation**: The agent processes the retrieved context and incorporates it into its reasoning.

6. **Feedback**: The agent evaluates whether the outcome meets the intended objective. If not, it refines its reasoning or actions in the next cycle.

7. **Response**: The LLM generates a final response or executes the requested action.

8. **Context update**: The agent stores relevant details so it can improve future interactions.

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

* [Agent types](../identity/idai-agent-types.html)

* [Securing digital assistants](../use-cases/idai-securing-digital-assistants.html)