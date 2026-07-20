---
title: Agentic Development
description: How AI agents interact with Ping Identity platforms directly in development and sandbox environments, and which tools to use.
component: build-with-ai
page_id: build-with-ai::agentic-development-environments
canonical_url: https://developer.pingidentity.com/build-with-ai/agentic-development-environments.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2026
keywords: ["agents", "agentic", "development", "sandbox", "MCP", "Ping CLI", "authentication", "OAuth", "headless"]
section_ids:
  which-tool-to-use: Which tool to use
  how-direct-access-works: How direct access works
  boundaries-between-development-and-production: Boundaries between development and production
  implementation-guides: Implementation guides
---

# Agentic Development

In development and sandbox environments, agents can interact with Ping Identity platforms directly. The environment is sandboxed, data is synthetic, and mistakes are recoverable, so the governance overhead of a full CI/CD pipeline is not required at this stage.

This is in contrast to production, where agents should operate pipelines rather than platform APIs directly. Refer to [Managing Production Environments](agentic-cicd-production.html) for that pattern.

## Which tool to use

Two tool layers are available depending on the agent's context:

**MCP servers**: best for IDE-based and interactive development. [AIC MCP Server](aic-mcp-server/overview.html) and [DaVinci MCP Server](davinci-mcp-server/overview.html) provide rich, natural-language tooling suited to interactive sessions. The agent describes what it wants to do; the MCP server translates that into the appropriate action on the backend. This is the preferred approach when an MCP host (for example, an IDE session or Claude Desktop) is available, providing the agent with direct configuration management to the Ping Identity platform.

**Ping CLI**: best for when you want the agent to act autonomously, and supporting CI/CD development. When there is no IDE session or MCP host, the CLI provides a composable, scriptable execution layer. Its subcommand structure is natively understood by LLMs, so agents can construct valid invocations without a separate tool definition layer. Ping CLI provides agents with the ability to directly configure environments for rapid prototyping and iteration.

Ping CLI is also best used when exporting configuration from a lower environment, to create Configuration-as-Code (CaC) packages for GitOps based pipelines. Where a development environment contains new features to be tested and promoted through to production, the agent can use Ping CLI to bundle up the changes and create pull requests on the main configuration code repository. In turn, this can initiate the deterministic promotion process.

**The two tools are complementary**.

An agent working interactively in an IDE might use MCP to prototype a configuration, then use Ping CLI to export and import that configuration as a reproducible baseline.

## How direct access works

In both cases, the agent invokes the tool; the tool manages authentication to Ping Identity platform APIs. The agent never holds credentials directly.

The tool acquires access tokens on behalf of whoever has authorized it; a human administrator in an interactive session, or a dedicated OAuth client in a headless harness. API calls are audited against that identity, not against the agent.

This delegation pattern is the same in development as in production. The difference is that in development, the scope of potential impact is limited to the sandbox environment.

|   |                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Even in development, where possible, use a dedicated OAuth client for each agent or harness. A shared client makes it impossible to attribute audit records to a specific agent, which complicates debugging. See [Ping CLI in development environments](pingcli/agentic-development.html) for OAuth client recommendations. |

## Boundaries between development and production

The direct-access pattern described here is appropriate only in development and sandbox environments.

In production, the non-deterministic nature of agents means that direct agent access creates governance risk. Configuration mistakes in a production identity environment affect all users and services that depend on it. The CI/CD pipeline pattern described in [Managing Production Environments](agentic-cicd-production.html) addresses this by putting a review gate between agent output and the live system.

## Implementation guides

[icon: terminal, set=fas, size=3x]

#### [Ping CLI in development environments](pingcli/agentic-development.html)

Authentication delegation patterns, OAuth client setup, and usage guidance for Ping CLI in agent harnesses.

[icon: plug, set=fas, size=3x]

#### [AIC MCP Server](aic-mcp-server/overview.html)

MCP server for PingOne Advanced Identity Cloud — natural-language tooling for interactive agent development.

[icon: plug, set=fas, size=3x]

#### [DaVinci MCP Server](davinci-mcp-server/overview.html)

MCP server for DaVinci — interactive agent tooling for flow development and environment management.