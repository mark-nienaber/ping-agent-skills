---
title: What&#8217;s New?
description: Release notes and announcements for Build with AI and Ping.
component: build-with-ai
page_id: build-with-ai:release_notes:whats-new
canonical_url: https://developer.pingidentity.com/build-with-ai/release_notes/whats-new.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-10-28
keywords: ["release notes", "what's new", "MCP", "Advanced Identity Cloud", "changelog"]
section_ids:
  october-2026: October 2026
  october-28: October 28
  expanded-application-and-esv-tooling-for-the-aic-remote-mcp-server: Expanded application and ESV tooling for the AIC Remote MCP Server
  october-14: October 14
  new-experiences-tools-for-the-pingone-remote-mcp-server: New Experiences tools for the PingOne Remote MCP Server
  october-12: October 12
  ping-identity-agent-plugins: Ping Identity Agent Plugins
  september-2026: September 2026
  september-21: September 21
  agent-skills: Agent Skills
  august-2026: August 2026
  august-31: August 31
  aic-remote-mcp-server-early-access: AIC Remote MCP Server (early access)
  pingone-remote-mcp-server-early-access: PingOne Remote MCP Server (early access)
  july-2026: July 2026
  july-13: July 13
  agentic-deployment-patterns: Agentic deployment patterns
  ping-cli-and-terraform: Ping CLI and Terraform
  june-2026: June 2026
  june-10: June 10
  ping-identity-agent-plugins-2: Ping Identity Agent Plugins
  may-2026: May 2026
  may-28: May 28
  docs-for-agents: Docs for agents
  may-22: May 22
  ai-first-in-action-build-an-ios-sample-app-with-ai: "AI-first in action: Build an iOS sample app with AI"
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

## October 2026

### October 28

#### Expanded application and ESV tooling for the AIC Remote MCP Server

NEW PingOne Advanced Identity Cloud

The AIC Remote MCP Server now includes expanded application management and ESV tooling.

New tools:

* SAML and application deletion:

  * `createSamlApp`: Creates a SAML SSO application from the service provider's metadata XML, including the hosted IdP entity, the remote SP entity, and Circle of Trust membership.

  * `deleteApplication`: Deletes an application regardless of type (OIDC, SAML, or provisioning), cascading to its linked AM or connector configuration.

* Application templates:

  * `listApplicationTemplates` and `getApplicationTemplate`: List application templates and retrieve a template's complete definition.

* Provisioning connectors:

  * `getConnectorSchema`: Discovers available connector bundles, or returns a configuration skeleton for a selected connector.

  * `createProvisioningApp`: Validates and persists a connector configuration, then builds and persists its sync mappings.

  * `getProvisioningAppConfig`: Reads a provisioning application's persisted connector and mapping configuration, including sync-engine diagnostics.

  * `verifyConnectorConnectivity`: Tests one connector or all connectors and reports connectivity and discovered object types.

  * `runReconciliation` and `getReconciliationStatus`: Trigger a mapping reconciliation and check its result.

* ESVs:

  * `publishESVs`: Restarts PingOne Advanced Identity Cloud to apply pending ESV changes.

The `deleteOidcApp` tool has been removed. Use `deleteApplication`, which deletes applications of any type.

Learn more in [Available Tools](../aic-remote-mcp-server/available-tools.html).

### October 14

#### New Experiences tools for the PingOne Remote MCP Server

NEW PingOne

The PingOne Remote MCP Server now includes an Experiences tool category for creating and managing design center experiences. Experiences configure the sign-on flow, first-factor settings, MFA, registration, account recovery, and theme of an environment.

New tools:

* `listExperiences`: Lists the design center experiences in an environment, or finds one by its exact name.

* `getExperience`: Retrieves the full configuration of a design center experience.

* `createExperience`: Creates a design center experience for a username-and-password, identifier-first, or identity-provider-first sign-on flow.

* `updateExperience`: Updates a design center experience's configuration, changing only the fields provided. The flow type can't be changed.

* `deleteExperience`: Permanently deletes a design center experience.

Learn more in [Available Tools (early access)](../pingone-mcp-server/p1-available-tools.html).

### October 12

#### Ping Identity Agent Plugins

NEW

The Ping Identity Agent Plugins repository now includes the `ping-identity-migration` plugin, an agent-facing plugin for running application-level migrations to PingOne from PingFederate or PingOne for Enterprise. The `ping-migration` skill orchestrates the extract, classify, apply, and validate steps, covering classification rules, migration-readiness assessment, wave planning, cutover, post-migration secret handling, and rollback.

Learn more:

* [Agent Skills](../agent-skills/overview.html)

* [GitHub repository](https://github.com/pingidentity/agent-plugins)

## September 2026

### September 21

#### Agent Skills

The Agent Skills page was restructured to reflect the new design pattern of the Ping Identity Agent Plugins repository, which now distributes plugins for orientation, cross-portfolio foundations, and product-specific PingOne and PingOne Advanced Identity Cloud design and integration, along with the companion Mobile and Web App Integration Agent Skills.

Learn more:

* [Agent Skills](../agent-skills/overview.html)

* [GitHub repository](https://github.com/pingidentity/agent-plugins)

## August 2026

### August 31

#### AIC Remote MCP Server (early access)

NEW PingOne Advanced Identity Cloud

The early access release of the AIC Remote MCP Server enables AI clients to administer PingOne Advanced Identity Cloud environments through a hosted remote MCP endpoint. Learn more in [Overview (early access)](../aic-remote-mcp-server/overview.html).

#### PingOne Remote MCP Server (early access)

NEW PingOne

You can opt in to use the early access release of the PingOne Remote MCP Server, enabling cross-environment administration and management of the PingOne platform. Learn more about the capabilities in [Overview (early access)](../pingone-mcp-server/p1-overview.html).

## July 2026

### July 13

#### Agentic deployment patterns

Guidance on how AI agents interact with Ping Identity platforms across different environments and governance models.

* [Agentic deployment patterns](../agentic-deployment-patterns.html): choosing the right interaction model (MCP, CLI, or IaC) based on environment and governance requirements.

* [Agentic development](../agentic-development-environments.html): direct agent interaction with Ping Identity platforms in sandbox environments.

* [Managing production environments](../agentic-cicd-production.html): how agents operate CI/CD pipelines to promote configuration safely into production.

#### Ping CLI and Terraform

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

#### Docs for agents

We've added a **Docs for Agents** page that explains how AI agents can discover, navigate, and ingest Ping Identity documentation.

Learn more:

* [Docs for Agents](../docs-for-agents.html)

### May 22

#### AI-first in action: Build an iOS sample app with AI

PingOne Advanced Identity Cloud

New use case walkthrough showing AI-first headless identity end to end. Using Claude Code connected to the AIC MCP Server and the Mobile and Web App Integration Agent Skills, the demo covers creating an PingOne Advanced Identity Cloud device binding journey, enabling passwordless login with Face ID, and configuring a native OIDC application and SwiftUI iOS sample app from natural language prompts, all without leaving your IDE.

Learn more:

* [Build an iOS Sample App with AI](../use-cases/build-ios-app.html)

### May 14

#### DaVinci MCP Server v0.2.0

PingOne DaVinci

We've added a new `davinci_troubleshooting` tool collection to the DaVinci MCP Server that allows AI agents to validate DaVinci flow configurations and investigate flow execution history.

New tools:

* `validate_flow`: Checks a flow for configuration errors and best-practice warnings using the DVLinter engine. Zero errors indicate deployment-ready status.

* `list_flow_executions`: Lists executions for a specific flow. Supports filtering by timestamp range and transaction ID.

* `summarize_flow_execution`: Returns status, input/output data, errors, stack traces, and user context for a specific execution.

Learn more in [Troubleshooting tools](../davinci-mcp-server/available-tools.html#troubleshooting-tools).

### May 13

#### Mobile and Web App Integration Agent Skills

PingOne Advanced Identity Cloud PingOne DaVinci

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

PingOne DaVinci

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

* [Try It Out](../davinci-mcp-server/getting-started.html)

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

* [Try It Out](../aic-mcp-server/getting-started.html)

* [GitHub repository](https://github.com/pingidentity/aic-mcp-server)

* [npm package](https://www.npmjs.com/package/@ping-identity/aic-mcp-server)