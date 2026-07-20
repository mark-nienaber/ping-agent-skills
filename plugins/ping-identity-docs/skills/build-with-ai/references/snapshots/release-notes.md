---
title: What&#8217;s New?
description: Release notes and announcements for Build with AI and Ping.
component: build-with-ai
page_id: build-with-ai:release_notes:whats-new
canonical_url: https://developer.pingidentity.com/build-with-ai/release_notes/whats-new.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 13, 2026
keywords: ["release notes", "what's new", "MCP", "AIC", "changelog"]
section_ids:
  july-2026: July 2026
  july-13: July 13
  agentic-deployment-patterns: Agentic deployment patterns
  ping-cli-and-terraform: Ping CLI and Terraform
  june-2026: June 2026
  june-10: June 10
  ping-identity-agent-plugins: Ping Identity Agent Plugins
  may-2026: May 2026
  may-28: May 28
  docs-for-agents: Docs for Agents
  may-22: May 22
  ai-first-in-action-build-an-ios-sample-app-with-ai: "AI-First in Action: Build an iOS Sample App with AI"
  may-14: May 14
  davinci-mcp-server-v0-2-0: DaVinci MCP Server v0.2.0
  may-13: May 13
  mobile-and-web-app-integration-agent-skills: Mobile and Web App Integration Agent Skills
  may-1: May 1
  davinci-mcp-server-v0-1-0: DaVinci MCP Server v0.1.0
  april-2026: April 2026
  april-30: April 30
  aic-mcp-server-v0-2-1: AIC MCP Server v0.2.1
---

# What's New?

Keep up with new developments in Build with AI and Ping.

## July 2026

### July 13

#### Agentic deployment patterns

New

Guidance on how AI agents interact with Ping Identity platforms across different environments and governance models.

* [Agentic deployment patterns](../agentic-deployment-patterns.html): choosing the right interaction model (MCP, CLI, or IaC) based on environment and governance requirements.

* [Agentic development](../agentic-development-environments.html): direct agent interaction with Ping Identity platforms in sandbox environments.

* [Managing production environments](../agentic-cicd-production.html): how agents operate CI/CD pipelines to promote configuration safely into production.

#### Ping CLI and Terraform

New

Guidance on how to use AI agents with Ping CLI and Terraform to automate and promote Ping Identity platform configuration across sandbox and production environments.

* [Ping CLI overview](../pingcli/overview.html): the workflow execution layer for scripting and automating Ping Identity configuration in agentic development and CI/CD pipelines.

* [Ping CLI in development environments](../pingcli/agentic-development.html): authentication delegation patterns, OAuth client recommendations, and example operations for sandbox use.

* [Ping CLI with CI/CD pipelines](../pingcli/cicd-and-production.html): the full governance model, config-as-code patterns, and a worked production example.

* [Terraform for Ping Identity configuration](../terraform/overview.html): declarative infrastructure-as-code for managing Ping Identity environments, and how it works alongside Ping CLI.

## June 2026

### June 10

#### Ping Identity Agent Plugins

Initial release of the Ping Identity Agent Plugins, a collection of six composable agent skills covering the full Ping Identity platform. Install in Claude Code or Cursor to get Ping Identity domain expertise alongside automatic registration of the AIC MCP Server and DaVinci MCP Server.

Key highlights:

* Six skills: `ping-quickstart`, `ping-foundation`, `ping-orchestration`, `ping-universal-services`, `ping-app-integration`, and `ping-identity-for-ai`.

* Automatic MCP server registration when installed in Claude Code or Cursor.

* Includes the Mobile and Web App Integration Agent Skills within `ping-app-integration` for mobile and web app scaffolding.

* Install with a single command across Claude Code, Cursor, GitHub Copilot, and Gemini CLI.

Learn more:

* [Agent Skills](../agent-skills/overview.html)

* [GitHub repository](https://github.com/pingidentity/agent-plugins)

## May 2026

### May 28

#### Docs for Agents

We've added a **Docs for Agents** page that explains how AI agents can discover, navigate, and ingest Ping Identity documentation.

Learn more:

* [Docs for Agents](../docs-for-agents.html)

### May 22

#### AI-First in Action: Build an iOS Sample App with AI

PingOne Advanced Identity Cloud

New use case walkthrough showing AI-first headless identity end to end. Using Claude Code connected to the AIC MCP Server and the Mobile and Web App Integration Agent Skills, the demo covers creating an PingOne Advanced Identity Cloud device binding journey, enabling passwordless login with Face ID, configuring a native OIDC application, and scaffolding a SwiftUI iOS sample app, all from natural language prompts without leaving your IDE.

Learn more:

* [Build an iOS Sample App with AI](../use-cases/build-ios-app.html)

### May 14

#### DaVinci MCP Server v0.2.0

DaVinci

We've added a new `davinci_troubleshooting` tool collection to the DaVinci MCP Server that allows AI agents to validate DaVinci flow configurations and investigate flow execution history.

New tools:

* `validate_flow`: Checks a flow for configuration errors and best-practice warnings using the DVLinter engine. Zero errors indicate deployment-ready status.

* `list_flow_executions`: Lists executions for a specific flow. Supports filtering by timestamp range and transaction ID.

* `summarize_flow_execution`: Returns status, input/output data, errors, stack traces, and user context for a specific execution.

Learn more in [Troubleshooting tools](../davinci-mcp-server/available-tools.html#troubleshooting-tools).

### May 13

#### Mobile and Web App Integration Agent Skills

PingOne Advanced Identity Cloud DaVinci

Initial release of the Mobile and Web App Integration Agent Skills, an open-source collection of agent skills that extend AI coding assistants with deep knowledge of Ping Identity's client-side orchestration SDKs.

Skills are available for Android, iOS, and ReactJS across PingOne Advanced Identity Cloud / PingAM Journeys and DaVinci Flows. A migration skill is also included for teams moving from the legacy ForgeRock SDK to the Ping Orchestration Journey SDK.

Key highlights:

* Rapidly scaffold authentication flows for Android (Jetpack Compose), iOS (SwiftUI), and ReactJS (Vite + React 18).

* Covers both Journey and DaVinci integration patterns per platform.

* ForgeRock to Ping migration skill with automatic legacy detection and line-numbered migration report.

* Install with a single command across Claude Code, VS Code (GitHub Copilot), Cursor, Gemini CLI, and Codex.

Learn more:

* [Agent Skills](../agent-skills/overview.html)

* [GitHub repository](https://github.com/pingidentity/ping-sdk-agent-skills)

### May 1

#### DaVinci MCP Server v0.1.0

DaVinci

Initial release of the DaVinci MCP Server, an open-source MCP server that enables AI agents to manage DaVinci identity orchestration resources using natural language.

Available tool categories:

* **Applications:** List applications and inspect flow policies.

* **Flows:** List, describe, and inspect flow versions including full node graphs and edge definitions.

* **Connectors:** Browse the connector catalog and inspect deployed connector instances.

* **Variables:** List and inspect DaVinci flow variables.

* **Forms:** List and inspect DaVinci form definitions.

Key highlights:

* Secure OAuth 2.0 PKCE authentication with OS keychain token storage.

* Regional support for PingOne NA, EU, and APAC domains, with custom domain support.

* Read-oriented tools across all major DaVinci resource types.

Learn more:

* [Overview](../davinci-mcp-server/overview.html)

* [Try it out](../davinci-mcp-server/getting-started.html)

* [GitHub repository](https://github.com/pingidentity/davinci-mcp-server)

* [npm package](https://www.npmjs.com/package/@ping-identity/davinci-mcp-server)

## April 2026

### April 30

#### AIC MCP Server v0.2.1

PingOne Advanced Identity Cloud

Initial release of the AIC MCP Server, an open-source MCP server that enables AI agents to manage PingOne Advanced Identity Cloud environments using natural language.

Available tool categories:

* **Managed objects:** Full CRUD operations on users, roles, groups, organizations, custom types, and schema definitions.

* **Themes:** Create, update, and manage login and account page themes.

* **Logging:** Query and analyze authentication and activity logs by time range, source, and content.

* **ESVs:** Manage environment secrets and variables.

* **Feature management:** Inspect and enable optional IDM and platform features.

* **AM Journeys:** Manage authentication journeys, nodes, and Scripted Decision Node scripts.

* **OIDC applications:** CRUD operations on OAuth 2.0 / OIDC application configurations.

Key highlights:

* Secure OAuth 2.0 PKCE authentication with OS keychain token storage.

* Docker deployment support via Device Code Flow.

* 40+ tools across 7 categories.

* Read-only mode enabled by default.

* Tool inclusion/exclusion flags for granular control.

Learn more:

* [Overview](../aic-mcp-server/overview.html)

* [Try it Out](../aic-mcp-server/getting-started.html)

* [GitHub repository](https://github.com/pingidentity/aic-mcp-server)

* [npm package](https://www.npmjs.com/package/@ping-identity/aic-mcp-server)