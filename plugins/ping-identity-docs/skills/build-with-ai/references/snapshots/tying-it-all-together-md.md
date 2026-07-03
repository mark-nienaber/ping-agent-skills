---
title: Tying It All Together
description: The tools on this site are designed to work together. Each one covers a different layer of performing AI-first headless identity operations, and when combined, they form a complete AI-first developer workflow.
component: build-with-ai
page_id: build-with-ai::tying-it-all-together
canonical_url: https://developer.pingidentity.com/build-with-ai/tying-it-all-together.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 8, 2026
section_ids:
  the-three-layers: The three layers
  how-the-layers-connect: How the layers connect
  example-end-to-end: "Example: end to end"
  where-to-go-next: Where to go next
---

# Tying It All Together

The tools on this site are designed to work together. Each one covers a different layer of performing AI-first headless identity operations, and when combined, they form a complete AI-first developer workflow.

## The three layers

| Layer                     | Problem it solves                                                                 | Tool                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Discovery                 | AI agents can't navigate traditional documentation efficiently                    | [Agent-ready docs and `llms.txt`](docs-for-agents.html)                                                |
| Domain expertise          | Agents lack context about the Ping Identity platform, SDKs, and identity patterns | [Ping Identity Agent Plugins](agent-skills/overview.html)                                              |
| Interactive configuration | Configuring Ping Identity platforms requires clicking through consoles            | [AIC MCP Server](aic-mcp-server/overview.html), [DaVinci MCP Server](davinci-mcp-server/overview.html) |

## How the layers connect

A complete AI-first identity workflow typically moves through these layers in sequence, though you can enter at any point depending on what you're doing.

**1\. Your AI agent gets its bearings.** Before you prompt anything, your AI coding agent (Claude Code, Copilot, Cursor, Gemini CLI, etc.) can discover Ping Identity documentation through the `llms.txt` endpoint and Markdown alternates. It knows what documentation exists, where it is, and how to navigate it without you having to copy-paste reference material.

**2\. You install domain expertise.** Ping Identity Agent Plugins give your AI agent pre-loaded knowledge of Ping Identity platforms: which product to use, how to configure it, how to integrate it, and how to secure AI agents against it. Six composable skills cover a range of identity work, and they are designed to be used together. `ping-quickstart` routes you to the right combination automatically.

**3\. Your agent configures the platform.** The AIC MCP Server and DaVinci MCP Server connect your AI agent directly to your Ping Identity tenant. You describe what you want (a journey, a theme, a flow) and the agent calls the right APIs to make it happen, all through natural language from inside your IDE.

## Example: end to end

The following shows how the layers combine in a single workflow:

1. Install the Ping Identity Agent Plugins in your AI coding agent. The MCP servers register automatically.

2. Use the DaVinci MCP Server to inspect your DaVinci flows and validate their configuration.

3. Make any necessary changes to your DaVinci flows, guided by `ping-orchestration`.

4. Use the `ping-app-integration` skill to integrate the Ping Orchestration SDK into your iOS and Android apps.

Each step uses a different tool, but none of them require you to leave your terminal or IDE.

## Where to go next

[icon: puzzle-piece, set=fas, size=3x]

#### [Agent Skills](agent-skills/overview.html)

Install Ping Identity platform expertise into your AI coding assistant, from tenant setup and orchestration to app integration and securing AI agents.

[icon: chart-diagram, set=fas, size=3x]

#### [AIC MCP Server](aic-mcp-server/overview.html)

Configure PingOne Advanced Identity Cloud journeys, apps, themes, and more through natural language.

[icon: chart-diagram, set=fas, size=3x]

#### [DaVinci MCP Server](davinci-mcp-server/overview.html)

Explore and troubleshoot DaVinci flows from your AI agent.
