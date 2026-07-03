---
title: Key Identity for AI Terminology
description: Learn about key terms related to AI concepts and Identity for AI, a solution for securing, managing, and governing AI systems and data.
component: identity-for-ai
page_id: identity-for-ai:glossary:idai-glossary
canonical_url: https://developer.pingidentity.com/identity-for-ai/glossary/idai-glossary.html
revdate: October 9, 2025
keywords: ["Identity for AI", "ai identity", "ai terms", "ai terminology", "ai glossary", "ai"]
page_aliases: ["index.adoc"]
section_ids:
  agent-types: Agent types
  digital-assistant: Digital assistant
  digital-worker: Digital worker
  personal-agent: Personal agent
  ai-and-ml-terms: AI and ML terms
  agent-card: Agent card
  artificial-intelligence-ai: Artificial intelligence (AI)
  computer-using-agent-cua: Computer-using agent (CUA)
  context-poisoning-prompt-injection: Context poisoning (prompt injection)
  explainable-ai-xai: Explainable AI (XAI)
  generative-artificial-intelligence-genai: Generative artificial intelligence (GenAI)
  large-language-model-llm: Large language model (LLM)
  machine-learning-ml: Machine learning (ML)
  managed-agents: Managed agents
  natural-language-processing-nlp: Natural language processing (NLP)
  retrieval-augmented-generation-rag: Retrieval-augmented generation (RAG)
  iam-terms: IAM terms
  agentic-identity: Agentic identity
  ai-for-identity: AI for identity
  attribute-based-access-control-abac: Attribute-based access control (ABAC)
  authenticated-delegation: Authenticated delegation
  bring-your-own-agent-byoa: Bring your own agent (BYOA)
  client-initiated-backchannel-authentication-ciba: Client-Initiated Backchannel Authentication (CIBA)
  delegated-authority: Delegated authority
  dynamic-client-registration-dcr: Dynamic Client Registration (DCR)
  idai-gloss-hitl: Human-in-the-loop (HITL)
  identity-for-ai: Identity for AI
  identity-lifecycle-management-ilm-for-ai: Identity lifecycle management (ILM) for AI
  idai-gloss-lp: Least privilege
  mutual-transport-layer-security-mtls: Mutual transport layer security (mTLS)
  non-human-identity-nhi: Non-human identity (NHI)
  pushed-authorization-requests-par: Pushed Authorization Requests (PAR)
  rich-authorization-requests-rar: Rich Authorization Requests (RAR)
  trust-boundary: Trust boundary
  protocols: Protocols
  model-context-protocol-mcp: Model Context Protocol (MCP)
  agent2agent-protocol-a2a: Agent2Agent protocol (A2A)
---

# Key Identity for AI Terminology

Learn about key terms related to artificial intelligence (AI) concepts and Identity for AI, a solution for securing, managing, and governing AI systems and data.

## Agent types

Learn more in [What Are AI Agents?](../agents/idai-what-are-agents.html) and [Agent Types](../identity/idai-agent-types.html).

### Digital assistant

A reactive agent that responds to direct commands from a user to perform specific tasks based on explicit prompts. Digital assistants can be thought of as front-line workers managed by an organization that lie mainly or completely within the organization's trust boundary. They can be both customer-facing and deployed for the workforce:

* **Consumer digital assistants** interact directly with customers or end users to provide services, answer questions, and perform tasks. These agents lie mainly within the organization's trust boundary, interacting with consumers outside the boundary. Examples of this type of *our agent works for you* digital assistant include a digital mortgage advisor, travel agent, or chatbot.

* **Workforce digital assistants** assist employees by automating routine tasks and providing information that improves the efficiency of the organization. These agents lie completely within the organization's trust boundary. Examples of this type of *our agent works internally for employees* digital assistant include an HR assistant that helps with time-off requests or a payroll assistant that answers pay-related questions.

### Digital worker

A managed agent that's more autonomous than a digital assistant and designed to perform structured, repetitive tasks to automate business processes and workflows. These agents lie completely within the organization's trust boundary. Examples of this type of *our agent solves tasks autonomously for our organization* digital worker include a finance assistant, Salesforce [Agentforce](https://www.salesforce.com/agentforce/), and [Lindy.ai](https://www.lindy.ai/).

### Personal agent

A proactive and autonomous agent that acts on behalf of a user to achieve the user's goals. This type of agent is highly personalized and acts as a proxy for the user on the user's device. Personal agents aren't managed by your organization and lie outside of your organization's trust boundary. Examples of this type of *your agent works for you* personal agent include agents that book travel, help with investments or shopping, and large language models (LLMs) such as [ChatGPT](https://chatgpt.com), [Claude](https://www.anthropic.com/claude), and [Google Gemini](https://gemini.google).

## AI and ML terms

### Agent card

A JSON metadata document used in the agent2agent (A2A) protocol that describes an AI agent's purpose, skills, endpoint URL, and authentication requirements for discovery and collaboration.

### Artificial intelligence (AI)

The simulation or replication of human-like intelligence by machines, especially computer systems, to perform tasks such as learning, reasoning, problem-solving, and decision-making.

### Computer-using agent (CUA)

An agent that interacts directly with graphical user interfaces (GUIs) and command-line interfaces (CLIs), such as web browsers, buttons, menus, and text fields, by emulating human actions. Learn more in [Computer-Using Agents (CUAs)](../agents/idai-computer-using-agents.html).

### Context poisoning (prompt injection)

A security vulnerability where a malicious attacker manipulates the input context or prompts provided to an AI agent, subtly altering the agent's behavior and leading to unintended outputs.

### Explainable AI (XAI)

The field of AI that focuses on making AI decisions and outputs understandable to humans, addressing the *black box* problem of complex models.

### Generative artificial intelligence (GenAI)

AI systems that can create new content, such as text, images, audio, or video, based on learned patterns from existing data. Examples include LLMs, such as ChatGPT, Claude, or Google Gemini, and image generation models.

### Large language model (LLM)

A type of deep learning AI model designed to understand and generate human-like text by processing vast amounts of textual data. LLMs, such as OpenAI's GPT series, are capable of performing various natural language processing tasks, including translation, summarization, and question answering.

### Machine learning (ML)

A subset of AI focused on algorithms and statistical models that enable computers to learn from data and make predictions or decisions without explicit programming for specific tasks.

### Managed agents

AI agents that are developed, provisioned, centrally controlled, and governed by an organization, ensuring alignment with established security policies and compliance standards.

### Natural language processing (NLP)

A branch of AI that focuses on the interaction between computers and human (natural) languages, enabling machines to understand, interpret, and generate human language in a meaningful and useful way.

### Retrieval-augmented generation (RAG)

An AI technique that combines LLMs with external knowledge sources, such as databases or documents. This enhances the model's ability to generate accurate and contextually relevant responses by retrieving pertinent information during the generation process.

## IAM terms

### Agentic identity

The unique identity of an AI agent that acts autonomously and makes decisions. Agentic identity encompasses the agent's permissions, delegated authority, behavioral patterns, credentials, and roles in an identity and access management (IAM) framework.

### AI for identity

The application of AI and ML techniques to enhance IAM processes such as user authentication, fraud detection, and access control.

### Attribute-based access control (ABAC)

An authorization model that grants or denies access to resources based on a combination of attributes associated with users, AI agents, resources, and current environmental conditions (context).

### Authenticated delegation

The process of a human user securely authorizing a specific AI agent to access digital services or interact with other agents on the human's behalf, with verifiable permissions and scope.

### Bring your own agent (BYOA)

A security model in which employees or customers bring their own AI agents into an organization's environment. BYOAs aren't centrally managed or governed by the organization and might not adhere to the organization's policies and standards.

### Client-Initiated Backchannel Authentication (CIBA)

An OAuth 2.0-based authentication protocol that allows an AI agent to get human approval for a sensitive action. CIBA allows the AI agent to initiate an authentication request to an identity provider (IdP) without direct, real-time user interaction, enabling [human-in-the-loop (HITL)](#idai-gloss-hitl) for critical tasks.

### Delegated authority

A model that enables an AI agent to act on behalf of a user without using their personal credentials, allowing the agent to serve as a secure and limited proxy for the user.

### Dynamic Client Registration (DCR)

An OAuth 2.0 protocol enabling AI agents to programmatically register themselves as OAuth 2.0 clients with an identity provider (IdP) or authorization server (AS) at runtime to obtain unique credentials and define initial scopes and permissions.

### Human-in-the-loop (HITL)

A security and governance approach that requires human intervention and approval for critical actions performed by AI agents, ensuring oversight and accountability when full automation isn't feasible.

### Identity for AI

A comprehensive solution for securely managing, governing, and auditing the identities and access of AI systems, including autonomous agents, within an organization's digital ecosystem. Learn more in [What Is Identity for AI?](../getting-started/idai-what-is-identity-for-ai.html).

### Identity lifecycle management (ILM) for AI

The process of managing an AI's identity from creation to retirement to automate the provisioning, authentication, authorization, and deprovisioning of AI identities.

### Least privilege

A fundamental security principle that restricts an entity's (human or AI agent) access rights and permissions to the minimum necessary to perform its legitimate functions, reducing the risk of unauthorized access or actions.

### Mutual transport layer security (mTLS)

A security protocol that ensures both the client (AI agent) and server authenticate each other using digital certificates during communication, providing a higher level of trust and security.

### Non-human identity (NHI)

Any digital identity assigned to an automated system, application, or device rather than a human user to manage and secure the access of non-human entities to digital resources.

### Pushed Authorization Requests (PAR)

An OAuth 2.0 extension that allows an AI agent to securely send authorization requests directly to the authorization server (AS) instead of through a user agent such as a web browser. This separates the authorization request from the final authorization URL and is useful for AI agents that operate without direct human interaction.

### Rich Authorization Requests (RAR)

An extension to OAuth 2.0 that enables AI agents to include rich, detailed information about their intended actions in authorization requests, such as specific permissions, constraints, and context, allowing for more granular and dynamic access control decisions.

### Trust boundary

A conceptual line that separates an organization's digital assets into different levels of trust and security. Assets inside the boundary, such as employees, digital workers, and authorized applications, are managed and controlled by the organization's policies and operate with a higher baseline of implicit trust. Untrusted assets outside the boundary, such as external customers or personal agents, aren't managed by the organization and require additional authorization and verification.

## Protocols

### Model Context Protocol (MCP)

An open-source standard for how AI systems, particularly LLMs, securely and dynamically interact with external tools and data sources. MCP defines an MCP server as a standardized interface that exposes a specific tool, API, or data source to an AI agent. The MCP server acts as a *smart adapter* or *universal connector* for AI. Learn more in [What is Model Context Protocol (MCP)?](../agents/idai-what-is-mcp.html) and [MCP servers and OAuth 2.0](../agents/idai-securing-mcp-servers.html).

### Agent2Agent protocol (A2A)

An open-source protocol that enables secure and standardized communication between AI agents. A2A facilitates interoperability, allowing agents to share information, authenticate each other, delegate tasks, and coordinate actions while maintaining security and trust. Learn more in [What is Agent2Agent Protocol (A2A)?](../agents/idai-what-is-a2a.html).
