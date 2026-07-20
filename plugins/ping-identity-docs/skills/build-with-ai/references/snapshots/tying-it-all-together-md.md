---
title: Tying It All Together
description: How agent-ready docs, Ping agent skills, MCP servers, Ping CLI, and Terraform work together as a complete AI-first identity workflow.
component: build-with-ai
page_id: build-with-ai::tying-it-all-together
canonical_url: https://developer.pingidentity.com/build-with-ai/tying-it-all-together.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 13, 2026
section_ids:
  the-layers: The layers
  how-the-layers-connect: How the layers connect
  example-end-to-end: "Example: end to end"
  where-to-go-next: Where to go next
---

# Tying It All Together

The tools on this site are designed to work together. Each one covers a different layer of performing AI-first headless identity operations, and when combined, they form a complete AI-first developer workflow.

## The layers

| Layer                     | Problem it solves                                                                              | Tool                                                                                                   |
| ------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Discovery                 | AI agents can't navigate traditional documentation efficiently                                 | [Agent-ready docs and `llms.txt`](docs-for-agents.html)                                                |
| Domain expertise          | Agents lack context about the Ping Identity platform, SDKs, and identity patterns              | [Ping Identity Agent Plugins](agent-skills/overview.html)                                              |
| Interactive configuration | Configuring Ping Identity platforms requires clicking through consoles                         | [AIC MCP Server](aic-mcp-server/overview.html), [DaVinci MCP Server](davinci-mcp-server/overview.html) |
| Workflow execution        | Scripting, promoting, and automating configuration changes requires a headless execution layer | [Ping CLI](pingcli/overview.html), [Terraform](terraform/overview.html)                                |

## How the layers connect

A complete AI-first identity workflow typically moves through these layers in sequence, though you can enter at any point depending on what you're doing.

**1\. Your AI agent gets its bearings.** Before you prompt anything, your AI coding agent (Claude Code, Copilot, Cursor, Gemini CLI, etc.) can discover Ping Identity documentation through the `llms.txt` endpoint and Markdown alternates. It knows what documentation exists, where it is, and how to navigate it without you having to copy-paste reference material.

**2\. You install domain expertise.** Ping Identity Agent Plugins give your AI agent pre-loaded knowledge of Ping Identity platforms: which product to use, how to configure it, how to integrate it, and how to secure AI agents against it. Composable skills cover a range of identity work, and they are designed to be used together. `ping-quickstart` routes you to the right combination automatically.

**3\. Your agent configures and inspects the platform.** The AIC MCP Server connects your AI agent to your Ping Identity tenant so you can configure journeys, themes, and more through natural language. The DaVinci MCP Server gives your agent read access to DaVinci flows for inspection and troubleshooting, without leaving your IDE.

**4\. Your agent scripts, promotes, and automates.** Ping CLI and Terraform handle the execution layer: exporting and promoting configuration across environments, running commands in CI/CD pipelines, and maintaining declared infrastructure state. In development, agents use the CLI directly as a tool. In production, agents operate pipelines, and the pipeline applies changes through a governed review process.

## Example: end to end

The following shows how the layers combine in a single workflow:

1. Install the Ping Identity Agent Plugins in your AI coding agent. The MCP servers register automatically.

2. Use the DaVinci MCP Server to inspect your DaVinci flows and validate their configuration.

3. Make any necessary changes to your DaVinci flows, guided by `ping-orchestration`.

4. Use the `ping-app-integration` skill to integrate the Ping Orchestration SDK into your iOS and Android apps.

5. Use Ping CLI to export the validated flow configuration and promote it to a staging environment for testing.

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

[icon: terminal, set=fas, size=3x]

#### [Ping CLI](pingcli/overview.html)

Script, automate, and promote Ping Identity configuration from agent harnesses and CI/CD pipelines.

[icon: file-code, set=fas, size=3x]

#### [Terraform](terraform/overview.html)

Declare and maintain Ping Identity infrastructure configuration as code, applied through governed pipelines.