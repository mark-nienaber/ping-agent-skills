---
title: Agent Skills
description: Agent skills that extend AI coding assistants with Ping Identity domain expertise for building, integrating, and operating identity solutions.
component: build-with-ai
page_id: build-with-ai:agent-skills:overview
canonical_url: https://developer.pingidentity.com/build-with-ai/agent-skills/overview.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 12, 2026
keywords: ["agent skills", "agent plugins", "SDK", "Android", "iOS", "ReactJS", "React Native", "DaVinci", "AIC", "PingAM", "AI"]
section_ids:
  ping-identity-agent-plugins: Ping Identity Agent Plugins
  install-for-your-ai-agent: Install for your AI agent
  the-plugins: The plugins
  working-alongside-mcp-servers-and-the-ping-cli: Working alongside MCP servers and the Ping CLI
  mobile-web-app-integration: Mobile and Web App Integration Agent Skills
  install-for-your-ai-agent-2: Install for your AI agent
---

# Agent Skills

Agent Skills extend your AI coding assistant with Ping Identity domain expertise. Each skill is a curated set of instructions, code patterns, and best practices your AI agent loads on demand. You describe what you want to build and get meaningful, context-aware help without leaving your IDE.

Agent Skills are an [open standard](https://agentskills.io) for giving AI agents new capabilities and domain expertise.

The Ping Identity Agent Skills are published on GitHub:

* [Ping Identity Agent Plugins](https://github.com/pingidentity/agent-plugins)

* [Mobile and Web App Integration Agent Skills](https://github.com/pingidentity/ping-sdk-agent-skills)

## Ping Identity Agent Plugins

Ping Identity Agent Plugins give AI coding agents deep knowledge of Ping Identity platforms through composable skills, published as a collection of plugins in one repository. The repository includes plugins for several purposes, so it helps to know the types of plugins available rather than the individual skills:

* **Orientation:** A human-facing front door that detects your platform and goal, orients you, and routes you to the right place to start.

* **Cross-portfolio foundations:** Platform understanding across the Ping Identity portfolio, including products, deployment models, solutions, and application-integration concepts.

* **Product-specific:** Deep, agent-facing plugins for individual platforms, such as PingOne and PingOne Advanced Identity Cloud / PingAM, covering flow and journey design, app-side integration, live troubleshooting, and application-level migration to PingOne.

* **Companion SDK skills:** Deep client-side integration knowledge for the Ping Orchestration SDKs, provided by the [Mobile and Web App Integration Agent Skills](#mobile-web-app-integration).

New plugins and skills are added over time, and existing ones are subject to change. Refer to the repository for the current catalog and skill-level detail.

### Install for your AI agent

* Claude Code

* Cursor

* GitHub Copilot

* Gemini CLI

* Skills CLI (npx)

Run the following slash command directly inside Claude Code:

```bash
/plugin marketplace add https://github.com/pingidentity/agent-plugins
```

Go to Settings, then Plugins, and search for and add `https://github.com/pingidentity/agent-plugins`.

Clone the repository, then add the relevant `SKILL.md` files to `.github/copilot-instructions.md` in your project.

Add the relevant skill instructions to your `GEMINI.md`.

```bash
npx skills add pingidentity/agent-plugins
```

Or install individual plugins:

```bash
npx skills add pingidentity/agent-plugins/plugins/ping-identity-quickstart
npx skills add pingidentity/agent-plugins/plugins/ping-identity
npx skills add pingidentity/agent-plugins/plugins/ping-identity-pingone
npx skills add pingidentity/agent-plugins/plugins/ping-identity-pingone-aic
npx skills add pingidentity/agent-plugins/plugins/ping-identity-migration
```

Refer to [skills.sh](https://skills.sh) for agent-specific setup instructions.

|   |                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------- |
|   | The skills work better together. Install the full plugin collection rather than individual skills for the most benefit. |

### The plugins

The following table describes each plugin and shows example prompts for how it is typically used. Prompts that act on a live tenant work best with the relevant MCP server or the Ping CLI connected.

|   |                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For app-integration prompts, install the Mobile and Web App Integration Agent Skills as well. The app-integration skills in the product plugins pair with the Mobile and Web App Integration Agent Skills for deep client-side SDK scaffolding. |

| Plugin                      | Audience | What it is for                                                                                                                                                                                                                                                                                                                                                                                                                          | Example prompts                                                                                                                                                                                                                   |
| --------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ping-identity-quickstart`  | Human    | Orientation. Identifies your platform and goal and routes you to the right plugin or resource. Use when you are new to Ping Identity, comparing products, or planning a migration.                                                                                                                                                                                                                                                      | "I'm new to Ping Identity and need to add login to my app. Where do I start?" "What is the difference between PingOne, PingOne Advanced Identity Cloud, and PingFederate? Which one should I use?"                                |
| `ping-identity`             | Agent    | Cross-portfolio foundations. Platform understanding across products, deployment models, solutions, and application-integration concepts. Use when you need product selection, architecture guidance, or solution orientation.                                                                                                                                                                                                           | "Design a solution that uses PingOne for CIAM and PingOne Protect for risk scoring." "Compare hosted-page branding options across PingOne Advanced Identity Cloud and PingOne."                                                   |
| `ping-identity-pingone`     | Agent    | PingOne design, integration, and operations. DaVinci flow design, live flow-execution troubleshooting, and app-side integration against a PingOne environment.                                                                                                                                                                                                                                                                          | "Design a DaVinci registration flow with email verification and MFA enrollment." "Trace my failed DaVinci flow execution and identify the root cause." "Integrate my Android app with my PingOne environment using the Ping SDK." |
| `ping-identity-pingone-aic` | Agent    | PingOne Advanced Identity Cloud / PingAM design and integration. Journey and authentication tree design, and app-side integration against PingOne Advanced Identity Cloud.                                                                                                                                                                                                                                                              | "Build a passwordless login journey using passkeys in my Advanced Identity Cloud realm." "Integrate my React app with Advanced Identity Cloud journeys and handle the journey callbacks."                                         |
| `ping-identity-migration`   | Agent    | Application-level migration to PingOne from PingFederate or PingOne for Enterprise. Runs the extract, classify, apply, and validate steps, including classification rules, readiness assessment, wave planning, cutover, post-migration secret handling, and rollback. Use when you are moving identity applications off a source platform, assessing migration readiness, planning waves and cutover, or rolling back a migration run. | "Run a migration of our PingFederate OAuth clients to PingOne and tell me which apps can't move directly."                                                                                                                        |

## Working alongside MCP servers and the Ping CLI

The skills are designed to compose with the rest of the Build with AI toolchain. Connect the [AIC Remote MCP Server](../aic-remote-mcp-server/overview.html) or the [PingOne Remote MCP Server](../pingone-mcp-server/p1-overview.html) to give your agent live access to your tenant, and the [Ping CLI](../pingcli/overview.html) for command-line execution. When no MCP server or CLI is configured, the skills still produce designs, flows, and app-side implementation artifacts.

## Mobile and Web App Integration Agent Skills

The app-integration skills in the Ping Identity Agent Plugins reference the Mobile and Web App Integration Agent Skills for deep client-side integration work. The Mobile and Web App Integration Agent Skills are an open-source skill collection that gives your AI agent targeted knowledge of Ping Identity's client-side orchestration SDKs for building mobile and web authentication flows. They are designed as a companion to the app-integration skills, but you can also use them on their own if you only need mobile and web app scaffolding.

These skills are built on top of the [Ping Orchestration SDKs](https://developer.pingidentity.com/orchsdks) and are available for Android, iOS, ReactJS, and React Native across PingOne Advanced Identity Cloud / PingAM journeys and DaVinci flows. A migration skill is also included for teams moving from the legacy ForgeRock SDK to the Ping Orchestration SDKs.

|   |                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The Mobile and Web App Integration Agent Skills are distributed as the `ping-orchestration-sdks` plugin in the Ping Identity Agent Plugins repository. Installing the full plugin collection typically includes this plugin, but verify that it was pulled in with your other plugins. If it was not, install the Mobile and Web App Integration Agent Skills directly using the command that follows. |

### Install for your AI agent

Use the Skills CLI to install the collection, then refer to the repository for agent-specific setup instructions:

```bash
npx skills add pingidentity/ping-sdk-agent-skills
```

Refer to [skills.sh](https://skills.sh) for how to point your agent at the installed skills.