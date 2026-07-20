---
title: Agent Skills
description: Agent skills that extend AI coding assistants with Ping Identity domain expertise for building, integrating, and operating identity solutions.
component: build-with-ai
page_id: build-with-ai:agent-skills:overview
canonical_url: https://developer.pingidentity.com/build-with-ai/agent-skills/overview.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 8, 2026
keywords: ["agent skills", "SDK", "Android", "iOS", "ReactJS", "DaVinci", "AIC", "PingAM", "AI"]
section_ids:
  ping-identity-agent-plugins: Ping Identity Agent Plugins
  install-for-your-ai-agent: Install for your AI agent
  the-skills: The skills
  ping-quickstart: ping-quickstart
  ping-foundation: ping-foundation
  ping-orchestration: ping-orchestration
  ping-universal-services: ping-universal-services
  ping-app-integration: ping-app-integration
  ping-identity-for-ai: ping-identity-for-ai
  example-workflow: Example workflow
  mobile-web-app-integration: Mobile and Web App Integration Agent Skills
  what-you-can-build: What you can build
  install-for-your-ai-agent-2: Install for your AI agent
---

# Agent Skills

Agent Skills extend your AI coding assistant with Ping Identity domain expertise. Each skill is a curated set of instructions, code patterns, and best practices your AI agent loads on demand, so you can describe what you want to build and get meaningful, context-aware help without leaving your IDE.

Agent Skills are an [open standard](https://agentskills.io) for giving AI agents new capabilities and domain expertise.

|   |                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Skills are actively developed and new collections will be added over time. All skills are subject to change.Interoperability with our MCP servers and CLIs will continue to be enhanced and are limited at this time. |

## Ping Identity Agent Plugins

Ping Identity Agent Plugins give AI coding agents deep knowledge of Ping Identity platforms through composable skills. Each skill targets a specific layer of identity work, from platform setup and orchestration to app integration and securing AI agents, and they are designed to be used together.

Installing the plugin in Claude Code or Cursor also automatically registers the [AIC MCP Server](../aic-mcp-server/overview.html) and [DaVinci MCP Server](../davinci-mcp-server/overview.html), giving your agent live access to your tenant alongside the skills.

[View on GitHub](https://github.com/pingidentity/agent-plugins)

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

Add the following to your `GEMINI.md`:

```yaml
plugins:
  - https://github.com/pingidentity/agent-plugins
```

```bash
npx skills add pingidentity/agent-plugins
```

See [skills.sh](https://skills.sh) for agent-specific setup instructions.

You can also install a single skill instead of the full plugin:

```bash
npx skills add pingidentity/agent-plugins/plugins/ping-identity/skills/ping-quickstart
```

|   |                                                                                |
| - | ------------------------------------------------------------------------------ |
|   | The skills work better together. Install the full plugin for the most benefit. |

### The skills

Each skill provides targeted context to help your AI agent reason about Ping Identity platforms and common identity patterns. Think of them as a *starting point*: they grow over time, and work best alongside documentation, MCP tools, and your own prompts.

| Skill                     | What it does                                                                                                                                                                                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ping-quickstart`         | Routes to other skills and acts as the front door for all Ping Identity work. Identifies which platform you are on, what you are trying to accomplish, and routes you to the right skill. Start here when the platform or starting point is unknown.                                                         |
| `ping-foundation`         | General platform setup, administration, and core configuration across PingOne, PingOne Advanced Identity Cloud, self-managed software. Covers environments, app registration, SSO, directories, policies, and branding.                                                                                      |
| `ping-orchestration`      | Guidance around designing and building authentication flows, journeys, and orchestration logic across DaVinci, PingOne Advanced Identity Cloud / PingAM.. Covers login, registration, MFA, passwordless, step-up, progressive profiling, and social login.                                                   |
| `ping-universal-services` | Understanding of Ping's shared services: PingOne Protect (risk scoring), PingOne Verify (identity proofing), PingOne MFA, PingOne Credentials (verifiable credentials), PingOne IGA (governance), and PingOne Authorize (fine-grained authorization).                                                        |
| `ping-app-integration`    | Integration knowledge of Ping Identity into web, mobile, and server-side applications. Covers Android, iOS, React, and JavaScript SDKs; OIDC / OAuth 2.0 wiring; backend token validation; and SDK troubleshooting. Includes the [Mobile and Web App Integration Agent Skills](#mobile-web-app-integration). |
| `ping-identity-for-ai`    | Assistance with securing AI agents and LLM-powered apps with Ping Identity. Covers agent identity registration, machine-to-machine auth, Verified Trust signals, PingGateway as an MCP gateway, CIBA human-in-the-loop approvals, and bot / agent detection.                                                 |

|   |                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------- |
|   | A complete solution typically spans two or three skills. `ping-quickstart` tells you which combination to load. |

#### ping-quickstart

`ping-quickstart` is the entry point for all Ping Identity work. It detects which platform you are working on, what you are trying to accomplish, and routes you to the one or two skills best suited for the task.

Use it when:

* You are new to Ping Identity and are not sure which product handles your use case

* The platform has not been established yet in your conversation

* You want to compare or evaluate Ping Identity products

* You receive a generic request like "help me add login to my app" without further context

`ping-quickstart` does not answer questions directly. It orients your agent and hands off to the right skill.

#### ping-foundation

`ping-foundation` can help with platform setup, administration, and core configuration across Ping Identity platforms.

Things it can help with include:

* Provisioning environments and tenants across PingOne, PingOne Advanced Identity Cloud, PingFederate, PingAccess, PingDirectory, and PingID

* Registering OIDC, SAML, and OAuth 2.0 applications

* Configuring SSO and Platform SSO

* Managing directories, user populations, and schema

* Setting up sign-on policies, authentication policies, branding, and custom domains

* Advising on tenant architecture: how to structure environments, profiles, and populations

#### ping-orchestration

`ping-orchestration` can help with the design and construction of authentication flows, journeys, and orchestration logic.

It can assist with flow work across DaVinci, PingOne Advanced Identity Cloud / PingAM, and PingFederate, including:

* Login, registration, account recovery, and MFA enrollment flows

* Passwordless authentication using passkeys, FIDO2, magic links, and biometrics

* Step-up authentication and progressive profiling

* Social login and consent flows

* Authenticator app enrollment, TOTP, and push MFA

* Transaction approvals and CIBA (human-in-the-loop out-of-band)

* Node sequencing, flow troubleshooting, and pattern advice ("what nodes do I need for X?")

#### ping-universal-services

`ping-universal-services` can help configure and invoke Ping Identity's shared strategic services: the capabilities typically invoked from within a flow rather than standing alone.

It can assist with:

* **PingOne Protect:** risk scoring, risk policies, behavioral predictors, and the Signals SDK

* **PingOne Verify:** identity proofing, KYC, document verification, and liveness checks

* **PingOne MFA:** device management, MFA policies, enrollment APIs, and MFA-as-a-service

* **PingOne Credentials:** verifiable credential issuance, presentation, and revocation

* **PingOne IGA:** access requests, access reviews, provisioning, and entitlements

* **PingOne Authorize:** fine-grained authorization and attribute-based access control (ABAC) policies

When a Protect, Verify, IGA, or Authorize node or connector appears inside a DaVinci flow or PingOne Advanced Identity Cloud journey, configuring that node belongs to this skill, not `ping-orchestration`.

#### ping-app-integration

`ping-app-integration` can help with code-level integration work against Ping Identity platforms. It includes the [Mobile and Web App Integration Agent Skills](#mobile-web-app-integration) for mobile and web app authentication scaffolding.

Things it can help with include:

* Android (Kotlin, Jetpack Compose) and iOS (Swift, SwiftUI) SDK integration

* React and JavaScript SDK integration

* Embedding DaVinci flows and PingOne Advanced Identity Cloud journeys into web and mobile apps

* OIDC authorization code + PKCE flow wiring for client-side apps

* Server-side backend OIDC for Node.js, Java, Python, and .NET

* Token validation, refresh, and session management

* Client credentials (M2M) and token exchange patterns

* Troubleshooting: redirect\_uri\_mismatch, CORS errors, token refresh failures

* ForgeRock SDK to Ping Orchestration SDK migration

* On-premises PingFederate and PingAccess agent integration

#### ping-identity-for-ai

`ping-identity-for-ai` can help with securing AI agents and LLM-powered applications with Ping Identity. It draws on the Identity for AI five-pillar architecture: Agent Identity, Agent Security, Agent Gateway, Agent Detection, and Verified Trust.

Things it can help with include:

* Registering a verified identity for AI agents using client credentials and short-lived tokens

* Machine-to-machine (M2M) authentication and token rotation for autonomous agents

* Using PingGateway as an MCP gateway to front AI-facing APIs with OAuth validation, auditing, rate limiting, and policy enforcement

* CIBA human-in-the-loop approvals for high-risk agent actions

* Delegated tokens for helpdesk AI agents or workforce AI agents acting on behalf of users

* Bot and agent detection using PingOne Protect

* Verified Trust signals for AI applications and verifiable credentials for AI-to-AI interactions

### Example workflow

You start with a single prompt:

*"Build me a passwordless login flow using Face ID for my iOS app, connected to my AIC sandbox."*

Your AI agent works through each layer using the skills and MCP tools that fit the task:

1. `ping-orchestration` designs the device binding journey structure and node sequence.

2. `ping-foundation` registers the OIDC application in your PingOne Advanced Identity Cloud sandbox with the correct redirect URIs and scopes.

3. The AIC MCP Server creates the journey and OIDC application directly in your tenant.

4. `ping-app-integration` scaffolds the SwiftUI iOS app using the Ping Orchestration SDK, wired to the journey that was just created.

No context switching. No manual coordination between tools.

## Mobile and Web App Integration Agent Skills

The Mobile and Web App Integration Agent Skills are an open-source skill collection that gives your AI agent deep, targeted knowledge of Ping Identity's client-side orchestration SDKs for building mobile and web authentication flows.

|   |                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Mobile and Web App Integration Agent Skills are referenced and used directly within the `ping-app-integration` skill in the [Ping Identity Agent Plugins](#ping-identity-agent-plugins). When you install the full plugin, this expertise is included automatically. You can also install the Mobile and Web App Integration Agent Skills on their own if you only need mobile and web app scaffolding. |

These skills are built on top of the [Ping Orchestration SDKs](https://developer.pingidentity.com/orchsdks/) and are available for Android, iOS, and ReactJS across PingOne Advanced Identity Cloud / PingAM Journeys and DaVinci Flows. A migration skill is also included for teams moving from the legacy ForgeRock SDK to the Ping Orchestration Journey SDK.

[View on GitHub](https://github.com/pingidentity/ping-sdk-agent-skills)

### What you can build

| Platform                    | What the skill delivers                                                                                                                                                |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Android (Jetpack Compose)   | Complete MVVM authentication flows for DaVinci or Journey, including all collectors and callbacks, OIDC token exchange, device binding, and FIDO2.                     |
| iOS (SwiftUI)               | Complete MVVM authentication flows for DaVinci or Journey, including all collectors and callbacks, OIDC token exchange, device binding, and FIDO2/passkeys.            |
| ReactJS (Vite + React 18)   | Full SPA authentication flows for DaVinci or Journey, including dynamic collector and callback rendering, OIDC token exchange, protected routes, and user profile.     |
| ForgeRock to Ping Migration | Automatic detection of legacy ForgeRock SDK usage across Android, iOS, and JavaScript projects, with a line-numbered migration report and commented-out rollback path. |

### Install for your AI agent

* VS Code (GitHub Copilot)

* Claude Code

* Cursor

* Gemini CLI

* Codex (OpenAI)

```bash
npx skills add pingidentity/ping-sdk-agent-skills
```

Or install manually by cloning the repository and copying skill files to `~/.copilot/skills/`.

For more information, refer to the [VS Code agent skills documentation](https://code.visualstudio.com/docs/copilot/customization/agent-skills).

There are two ways to install skills in Claude Code.

**Option 1: Skills marketplace (in-app)**

```bash
/plugins marketplace add pingidentity/ping-sdk-agent-skills
```

**Option 2: Skills CLI**

```bash
npx skills add pingidentity/ping-sdk-agent-skills
```

For more information, refer to the [Claude Code skills documentation](https://docs.anthropic.com/en/docs/claude-code/skills).

**Option 1: In-app (Remote Rule)**

1. Open Cursor Settings (**Cmd+Shift+J** on Mac, **Ctrl+Shift+J** on Windows/Linux).

2. Navigate to **Rules**.

3. In the **Project Rules** section, click **Add Rule** and select **Remote Rule (GitHub)**.

4. Enter `https://github.com/pingidentity/ping-sdk-agent-skills` and save.

**Option 2: Skills CLI**

```bash
npx skills add pingidentity/ping-sdk-agent-skills
```

For more information, refer to the [Cursor skills documentation](https://cursor.com/docs/skills).

**Option 1: Gemini CLI command**

```bash
gemini skills install https://github.com/pingidentity/ping-sdk-agent-skills.git
```

**Option 2: Skills CLI**

```bash
npx skills add pingidentity/ping-sdk-agent-skills
```

For more information, refer to the [Gemini CLI skills documentation](https://geminicli.com/docs/cli/skills).

**Option 1: Skill installer**

```bash
$skill-installer pingidentity/ping-sdk-agent-skills
```

**Option 2: Skills CLI**

```bash
npx skills add pingidentity/ping-sdk-agent-skills
```

For more information, refer to the [Codex skills documentation](https://developers.openai.com/codex/skills).