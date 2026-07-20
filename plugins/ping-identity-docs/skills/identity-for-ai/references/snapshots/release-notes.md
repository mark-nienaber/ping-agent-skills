---
title: What&#8217;s New?
description: "Learn about new developments in Identity for AI, Ping Identity's solution for securing,  managing, and governing AI systems and data."
component: identity-for-ai
page_id: identity-for-ai:release-notes:idai-whats-new
canonical_url: https://developer.pingidentity.com/identity-for-ai/release-notes/idai-whats-new.html
revdate: May 22, 2026
keywords: ["Identity for AI", "release notes", "what's new"]
page_aliases: ["index.adoc"]
section_ids:
  march-2026: March 2026
  march-31: March 31
  identity-for-ai-general-availability: Identity for AI general availability
  agent-identity: Agent identity
  agent-gateway: Agent gateway
  agent-detection: Agent detection
  get-started: Get started
  february-2026: February 2026
  february-10: February 10
  identifying-agents-with-token-exchange: Identifying agents with token exchange
  february-5: February 5
  secure-mcp-servers-with-pinggateway: Secure MCP servers with PingGateway
  january-2026: January 2026
  january-16: January 16
  secure-a-cloudflare-mcp-with-ping-identity: Secure a Cloudflare MCP with Ping Identity
  secure-aws-bedrock-agentcore-identity-with-ping-identity: Secure AWS Bedrock AgentCore Identity with Ping Identity
  december-2025: December 2025
  december-22: December 22
  best-practices: Best practices
  november-2025: November 2025
  november-13: November 13
  mcp-and-a2a: MCP and A2A
  october-2025: October 2025
  october-9: October 9
  secure-your-ai-agents-with-identity-for-ai: Secure your AI agents with Identity for AI
---

# What's New?

Keep up with new developments in Identity for AI.

Subscribe to get automatic updates: [icon: rss-square, set=fa][Identity for AI RSS feed](idai-whats-new.xml)

## March 2026

### March 31

#### Identity for AI general availability

We're excited to announce the general availability of Identity for AI, which extends Ping Identity's proven identity control plane to agentic architectures.

Identity for AI treats AI agents as first-class, non-human identities. This empowers your organization to safely deploy agents by ensuring they act with delegated authority, enforce least-privilege access to resources, and maintain human accountability through comprehensive auditing and human-in-the-loop (HITL) approvals.

Use the following new capabilities in Ping Identity platforms to secure AI behavior across your systems.

##### Agent identity

New PingOne PingOne Advanced Identity Cloud PingAM

Onboard and authorize your AI agents, enabling them to authenticate and request scoped access to enterprise tools and APIs.

* **First-class agent identity**: Securely register, update, and disable AI agents with a new dedicated admin experience. This includes assigning agent owners and modeling which applications, groups, and users an agent is authorized to interact with.

* **Delegation instead of impersonation**: OAuth 2.0 token exchange allows an agent to exchange a human user's subject token for a new, downscoped token. The delegation token securely passes the identity of the human subject alongside the identity of the agent using the `act` (actor) and `may_act` claims, maintaining a secure chain of custody for downstream authorization.

* **Least‑privilege access at runtime**: Limit an agent's blast radius with fine-grained control over exactly which APIs and data sources the agent can access, including HITL approvals for sensitive actions.

Agent identity is made available as part of our new Identity for AI solution. Contact your account executive to find out more.

Learn more:

* [AI agents in PingOne Advanced Identity Cloud](https://docs.pingidentity.com/pingoneaic/release-notes/rapid-channel/ai-agents.html)

* [Managing AI agents in PingOne Advanced Identity Cloud](https://docs.pingidentity.com/pingoneaic/release-notes/rapid-channel/ai-agents-ui.html)

* [AI agents in PingOne](https://docs.pingidentity.com/pingone/ai_agents/p1_ai_agents.html)

* [Managing AI Agents in PingOne](https://docs.pingidentity.com/pingone/ai_agents/p1_managing_ai_agents.html)

* [Configuring OAuth 2.0 token exchange in PingOne](https://docs.pingidentity.com/pingone/use_cases/p1_oauth_2_token_exchange.html)

* [Configuring a CIBA flow in PingOne](https://docs.pingidentity.com/pingone/use_cases/p1_configure_ciba_flow.html)

##### Agent gateway

New PingGateway

PingGateway now provides runtime security for the backend resources and MCP servers your agents need to access, without requiring your developers to build complex security logic into individual MCP servers.

Acting as a security proxy for MCP servers, the agent gateway:

* Validates delegation tokens and enforces scopes and fine-grained authorization before agent requests reach backend resources.

* Audits, throttles, and terminates agent traffic.

* Includes specialized MCP filters.

Agent gateway is made available as part of our new Identity for AI solution. Contact your account executive to find out more.

Learn more:

* [MCP security gateway](https://docs.pingidentity.com/pinggateway/latest/mcp/index.html)

* [McpAuditFilter](https://docs.pingidentity.com/pinggateway/latest/reference/McpAuditFilter.html): Record centralized audit trails of all agent requests

* [McpProtectionFilter](https://docs.pingidentity.com/pinggateway/latest/reference/McpProtectionFilter.html): Bind OAuth 2.0 resource server configurations to MCP endpoints

* [McpValidationFilter](https://docs.pingidentity.com/pinggateway/latest/reference/McpValidationFilter.html): Validate JSON-RPC payloads and client message formats

##### Agent detection

Improved PingOne Protect

PingOne Protect now detects agentic automation acting on behalf of a user or system. It can:

* Identify a subset of specific agent types in the risk evaluation response.

* Use browser fingerprinting, behavioral telemetry, and device attributes to distinguish human traffic from agentic activity.

Agent detection is made available as part of our PingOne Protect solution. Contact your account executive to find out more.

Learn more in [Bot detection](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_predictors.html#bot-detection).

##### Get started

To start securing your AI agents with Identity for AI:

* Configure runtime identity to secure AI agents with [PingOne](../use-cases/idai-securing-agents-pingone.html) and [PingFederate](../use-cases/idai-securing-agents-pingfed.html)

* Integrate with [AWS Bedrock](../agents/idai-securing-aws-ping.html) and [Cloudflare](../agents/idai-securing-cloudflare-pingfed.html) MCP servers

* Explore additional [Identity for AI](../index.html) resources

## February 2026

### February 10

#### Identifying agents with token exchange

New

We've added documentation on [identifying agents with token exchange](../identity/idai-token-exhange.html).

### February 5

#### Secure MCP servers with PingGateway

New PingGateway

We've linked to a tutorial on [securing MCP servers](../agents/idai-securing-mcp-servers-gateway.html) with PingGateway.

## January 2026

### January 16

#### Secure a Cloudflare MCP with Ping Identity

New PingOne PingOne Advanced Identity Cloud DaVinci PingFederate

We've added documentation on how to integrate a Cloudflare Workers MCP server with Ping Identity products:

* [PingOne](../agents/idai-securing-cloudflare-pingone.html)

* [PingOne Advanced Identity Cloud](../agents/idai-securing-cloudflare-aic.html)

* [DaVinci](../agents/idai-securing-cloudflare-davinci.html)

* [PingFederate](../agents/idai-securing-cloudflare-pingfed.html)

#### Secure AWS Bedrock AgentCore Identity with Ping Identity

New PingOne PingOne Advanced Identity Cloud PingFederate

We've added documentation on how to integrate AWS Bedrock AgentCore Identity with Ping Identity products:

* [PingOne](../agents/idai-securing-aws-ping.html#p1-steps)

* [PingOne Advanced Identity Cloud](../agents/idai-securing-aws-ping.html#aic-steps)

* [PingFederate](../agents/idai-securing-aws-ping.html#pf-steps)

## December 2025

### December 22

#### Best practices

Improved

We've added a video to demonstrate [best practices](../getting-started/idai-what-is-identity-for-ai.html#idai-best-practices) when implementing agentic architecture.

## November 2025

### November 13

#### MCP and A2A

Improved

We've added information on [how MCP and A2A work together](../agents/idai-tools-intro.html#idai-mcp-and-a2a).

## October 2025

### October 9

#### Secure your AI agents with Identity for AI

New

We're excited to announce the launch of the **Identity for AI** portal, Ping Identity's dedicated resource for securing and governing the next generation of autonomous AI.

The rapid shift to agentic AI introduces countless security challenges. AI agents capable of actions such as booking flights and executing code must become trusted digital users. Our foundational Identity for AI framework integrates AI agents securely into your existing IAM ecosystem and helps you implement core best practices such as delegation, not impersonation and least privilege for every AI agent. Learn more in [What Is Identity for AI?](../getting-started/idai-what-is-identity-for-ai.html)

Start building trusted, secure, and compliant AI systems by [securing your digital assistants](../use-cases/idai-securing-digital-assistants.html).

Check back often for new Identity for AI resources, including additional use cases.