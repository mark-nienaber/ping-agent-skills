---
title: Authentication
description: How authentication works in the AIC MCP Server, including OAuth 2.0 PKCE and Device Code flows.
component: build-with-ai
page_id: build-with-ai:aic-mcp-server:authentication
canonical_url: https://developer.pingidentity.com/build-with-ai/aic-mcp-server/authentication.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 20, 2026
keywords: ["MCP", "authentication", "OAuth", "PKCE", "Device Code", "AIC"]
section_ids:
  local-deployment-pkce: Local deployment (PKCE)
  docker-deployment-device-code: Docker deployment (Device Code)
  authentication-constraints: Authentication constraints
---

# Authentication

The AIC MCP Server uses human-centric authentication to ensure all actions are traceable to an individual user.

## Local deployment (PKCE)

When running the AIC MCP Server locally, the server uses the OAuth 2.0 Authorization Code flow with PKCE (Proof Key for Code Exchange):

![PKCE authentication flow diagram showing the four phases: first tool use, token storage, automatic reuse, and auto re-authentication](_images/pkce-auth-flow.svg)

* 1 First tool use

  Your browser opens automatically for user login at PingOne Advanced Identity Cloud when you use a tool for the first time in a session.

* 2 Token storage

  Access tokens are stored securely in the OS keychain:

  * macOS Keychain

  * Windows Credential Manager

  * Linux Secret Service (Freedesktop.org API)

* 3 Automatic reuse

  Cached tokens are used for subsequent tool calls within the same session.

* 4 Auto re-authentication

  When tokens expire during a session, your browser opens again for a new login.

|   |                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | **Administrator access required:** The AIC MCP Server requires administrative authentication and provides administrative capabilities to your PingOne Advanced Identity Cloud development and sandbox environments. All operations are performed as the authenticated administrator and are fully auditable. |

## Docker deployment (Device Code)

When running in a Docker container, the server uses the OAuth 2.0 Device Code Flow:

1. When authentication is required, your MCP client displays a URL and a code.

2. Open the URL in your browser and enter the code.

3. Accept the prompt in your client.

4. Tokens are stored ephemerally in the container filesystem and deleted on container restart.

|   |                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Docker deployment uses MCP form elicitation for the Device Code Flow. This requires MCP client support for form elicitation, which is currently limited. |

## Authentication constraints

The AIC MCP Server enforces several authentication constraints by design:

* **Human-centric only:** Only authentication flows that tie actions to an individual human are supported. Client credentials and non-interactive flows are explicitly forbidden.

* **No static secrets:** The server does not allow configuration with or storage of a static `client_secret`.

* **Tokens never stored in plain text:** All tokens are stored in the OS encrypted keychain (local) or ephemerally in memory (Docker). Tokens are never written to disk in plain text files, logs, or shell history.

* **Reauthentication on startup:** Each time the server starts, a fresh authentication is required.

* **Sandbox and Development only:** The AIC MCP Server configurations are only available in Development and Sandbox tenants.

---

---
title: Available tools
description: An overview of the tool categories available in the AIC MCP Server.
component: build-with-ai
page_id: build-with-ai:aic-mcp-server:available-tools
canonical_url: https://developer.pingidentity.com/build-with-ai/aic-mcp-server/available-tools.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 20, 2026
keywords: ["MCP", "tools", "managed objects", "themes", "logging", "ESVs", "journeys", "AIC"]
section_ids:
  managed-objects: Managed objects
  themes: Themes
  logging: Logging
  esvs: ESVs (Environment Secrets and Variables)
  feature-management: Feature management
  am-journeys: AM Journeys
  oidc-applications: OIDC Applications
  agent-skills: Agent Skills
  install-agent-skills: Install agent skills
---

# Available tools

The AIC MCP Server exposes 40+ tools organized into functional categories. You don't need to know the individual tool names. Just describe what you want in natural language and your AI agent selects the right tool automatically.

For a full list of every tool and its parameters, refer to the [AIC MCP Server README](https://github.com/pingidentity/aic-mcp-server#available-tools).

| Category                                  | What you can do                                                                               |
| ----------------------------------------- | --------------------------------------------------------------------------------------------- |
| [Managed Objects](#managed-objects)       | CRUD operations on users, roles, groups, organizations, custom types, and schema definitions. |
| [Themes](#themes)                         | Create, update, and manage login and account page themes.                                     |
| [Logging](#logging)                       | Query and analyze authentication and activity logs.                                           |
| [ESVs](#esvs)                             | Manage environment secrets and variables.                                                     |
| [Feature Management](#feature-management) | Inspect and enable optional IDM and platform features.                                        |
| [AM Journeys](#am-journeys)               | Manage authentication journeys, nodes, and scripts.                                           |
| [OIDC Applications](#oidc-applications)   | CRUD operations on OAuth 2.0 / OIDC application configurations.                               |

|   |                                                                                                  |
| - | ------------------------------------------------------------------------------------------------ |
|   | Tools are only available in **Sandbox and Development** PingOne Advanced Identity Cloud tenants. |

## Managed objects

Create, read, update, and delete any managed object type in your environment, including users, roles, groups, organizations, and custom types. You can also define new object types, modify schemas, and manage custom relationship properties.

**Example prompts:**

* "Find all users with admin in their username"

* "Create a new developer role"

* "What fields are required for alpha\_user?"

* "Add a custom\_manager relationship to alpha\_user"

## Themes

Customize the appearance of login and account pages. Create new themes, update colors and logos, and set the default theme for a realm.

**Example prompts:**

* "Create a theme called Corporate Brand with primary color #0066cc"

* "Show me all themes in the alpha realm"

* "Set the new theme as default"

## Logging

Query and analyze authentication and activity logs. Filter by time range, log source, and content to quickly find relevant events.

**Example prompts:**

* "Show me failed login attempts in the last hour"

* "Find all logs for transaction abc-123"

* "What log sources are available?"

## ESVs (Environment Secrets and Variables)

Manage environment variables used for configuration across your tenant. Query, create, update, and delete variables.

**Example prompts:**

* "List all environment variables"

* "Create a new variable esv-api-key"

* "What is the value of esv-database-url?"

## Feature management

Inspect and enable optional IDM and platform features in your PingOne Advanced Identity Cloud environment.

|   |                                                                               |
| - | ----------------------------------------------------------------------------- |
|   | Feature install operations are one-way and cannot be undone from these tools. |

**Example prompts:**

* "What features are available?"

* "Is AI Agents enabled?"

* "Install the groups feature"

## AM Journeys

Manage authentication journeys, including creating and updating complete journey trees, configuring individual nodes, and working with Scripted Decision Node scripts.

|   |                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | AM Journey tools are **not available** when using Docker because they require browser-based PKCE authentication, which is incompatible with the Device Code Flow used in containers. |

**Example prompts:**

* "Show me the Login journey"

* "Create a new MFA journey"

* "Add a scripted decision node to the registration flow"

* "List all scripts in the alpha realm"

* "Set Login as the default journey"

## OIDC Applications

|   |                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | OIDC Application tools are **not available** when using Docker because they require browser-based PKCE authentication, which is incompatible with the Device Code Flow used in containers. |

Create, read, update, and delete OAuth 2.0 / OpenID Connect application configurations in your tenant. Use these tools to register new OIDC clients, update redirect URIs, manage grant types, and inspect existing application settings.

**Example prompts:**

* "List all OIDC applications"

* "Create a new public OIDC client called my-spa with redirect URI http\://localhost:3000/callback"

* "Show me the configuration for the my-app client"

* "Update the redirect URIs for client xyz"

* "What grant types are configured for my-app?"

## Agent Skills

The AIC MCP Server repository ships agent skills that extend your AI agent's ability to work with the MCP server. Once installed, your agent can take on operational tasks without needing explicit instructions.

| Skill           | What it does                                                                                                                         | Try it                                                |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| `monitor-usage` | Audits MCP server activity in PingOne Advanced Identity Cloud logs: authentication events, user-attributed actions, and API traffic. | *"Show me what's been done via the MCP server today"* |

### Install agent skills

Clone the [AIC MCP Server repository](https://github.com/pingidentity/aic-mcp-server) and copy the skills from `.claude/skills/` to your agent's skills directory. Refer to your agent's documentation for the correct location.

Once installed, verify by asking your agent *"What skills do you have?"* You should see `monitor-usage` in the list.

---

---
title: Overview
description: An overview of the AIC MCP Server, a Model Context Protocol server for managing PingOne Advanced Identity Cloud environments using natural language.
component: build-with-ai
page_id: build-with-ai:aic-mcp-server:overview
canonical_url: https://developer.pingidentity.com/build-with-ai/aic-mcp-server/overview.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 20, 2026
keywords: ["MCP", "AI", "AIC", "PingOne Advanced Identity Cloud", "Model Context Protocol"]
section_ids:
  what-is-an-mcp-server: What is an MCP server?
  use-cases: Use cases
  example-prompts: Example prompts
  key-features: Key features
  next-steps: Next steps
---

# Overview

The AIC MCP Server is an open-source [TypeScript tool](https://github.com/pingidentity/aic-mcp-server) that enables AI agents to interact with PingOne Advanced Identity Cloud environments. It implements the [Model Context Protocol (MCP)](https://modelcontextprotocol.io), exposing 40+ tools that wrap PingOne Advanced Identity Cloud's REST APIs as MCP-compatible functions.

Instead of manually navigating the admin console or hand-crafting API requests, describe what you want in natural language. Your AI agent translates your intent to the right MCP tools, the server handles the API calls and authentication, and returns results your agent can present in natural language.

|   |                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The AIC MCP Server is currently available for **Sandbox and Development** PingOne Advanced Identity Cloud tenants only. It is not enabled for production environments. |

## What is an MCP server?

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io) is a specification that allows AI agents to discover and interact with external tools and services. MCP servers provide non-deterministic agents with deterministic actions and outcomes, based on natural language input.

The AIC MCP Server implements this protocol, exposing your PingOne Advanced Identity Cloud environment's APIs as a set of "tools" the AI can use. When you type a prompt, the agent translates the intent to an action and maps that action to the appropriate tool.

## Use cases

The AIC MCP Server enhances developer productivity by enabling AI-assisted operations for routine tasks. Developers don't have to context switch or learn the PingOne Advanced Identity Cloud admin console to develop faster, test faster, and debug faster.

### Example prompts

| Category                     | Example prompts                                                                                                                                      |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Journey management           | "Show me the Login journey", "Create a new MFA journey", "Add a scripted decision node to the registration flow", "Set Login as the default journey" |
| Authentication customization | "Create a branded theme with our corporate colors", "Show me all themes in production", "Set the new theme as default"                               |
| Audit and monitoring         | "Show me failed login attempts in the last hour", "Find all logs for transaction abc-123", "What log sources are available?"                         |
| Identity operations          | "Find all users with admin in their username", "Create a new developer role", "Update the email for user xyz123"                                     |
| Application management       | "Create a new OIDC application called MyApp with authorization code grant", "List all OAuth 2.0 applications", "Update the redirect URIs for MyApp"  |
| Feature enablement           | "What optional features are available?", "Enable the password policy feature", "Show me all currently enabled features"                              |
| Configuration management     | "List all environment variables", "Create a new API key variable", "Update the database connection string"                                           |

## Key features

* **Natural language interaction:** Interact with PingOne Advanced Identity Cloud from whichever AI tool you use daily. No need to switch to the admin console or write API scripts.

* **Secure authentication:** Supports OAuth 2.0 PKCE flow for local deployment and Device Code Flow for containerized deployment. All actions are user-based and auditable. Tokens are stored securely in the OS keychain.

* **Broad tool support:** Full CRUD operations against any managed object type in your environment (users, roles, groups, organizations, and custom types), authentication journey and script management, theme customization, advanced log querying, and environment variable configuration.

## Next steps

* [Install and configure the AIC MCP Server](getting-started.html)

* [Explore the full list of available tools](available-tools.html)

* [Learn how authentication works](authentication.html)

* [Understand the security model](security.html)

---

---
title: Security
description: Security considerations and best practices for the AIC MCP Server.
component: build-with-ai
page_id: build-with-ai:aic-mcp-server:security
canonical_url: https://developer.pingidentity.com/build-with-ai/aic-mcp-server/security.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 20, 2026
keywords: ["MCP", "security", "best practices", "AIC", "audit"]
section_ids:
  security-layers: Security layers
  audit-and-traceability: Audit and traceability
  tracing-actions-to-the-mcp-server: Tracing actions to the MCP server
  identifying-mcp-traffic: Identifying MCP traffic
  best-practices: Best practices
  feedback-and-issues: Feedback and issues
---

# Security

The AIC MCP Server is built with a "secure by design" philosophy. This page describes the security layers and best practices to follow when using the server.

## Security layers

The AIC MCP Server implements multiple security layers:

* Secure credential storage

  Tokens stored in the OS keychain (macOS Keychain, Windows Credential Manager, Linux Secret Service) for local deployment, or ephemerally in the container filesystem for Docker.

* No plain text secrets

  No sensitive information stored in configuration files.

* OAuth 2.0 authentication

  PKCE flow for local deployment prevents authorization code interception. Device Code flow for containerized deployment.

* User-based authentication

  All API calls are authenticated as the user who logged in, providing complete audit trails.

* Input validation

  Built-in protections against path traversal and query injection attacks.

* Tenant isolation

  Tokens are validated against the configured `AIC_BASE_URL` to prevent accidental cross-tenant operations.

## Audit and traceability

Every API call made by the AIC MCP Server is authenticated with an OAuth 2.0 access token tied to the administrator who logged in. PingOne Advanced Identity Cloud logs all API activity against this authenticated identity, providing a complete audit trail.

### Tracing actions to the MCP server

Because the AIC MCP Server requires administrator authentication via PKCE (or Device Code for Docker), every action is recorded in PingOne Advanced Identity Cloud audit logs under the authenticated user's identity. If an administrator needs to determine whether a change was made through the MCP server, they can use the following approach:

1. **Identify the user:** The AIC MCP Server authenticates using two registered OAuth 2.0 clients:

   * `AICMCPClient` - used for the initial user login (PKCE or Device Code flow)

   * `AICMCPExchangeClient` - used to obtain scoped tokens for each tool call via RFC 8693 token exchange

     All API requests carry an access token issued on behalf of the logged-in administrator. Each token exchange references the original user login, providing a complete chain from the tool call back to the authenticated identity.

2. **Query audit logs:** Use the PingOne Advanced Identity Cloud admin console or the AIC MCP Server logging tools to query audit logs filtered by:

   * The administrator's username

   * The time window of the suspected action

   * The `am-authentication` or other relevant log source

     Filtering the `am-authentication` log source for either of the client IDs above surfaces all MCP authentication activity.

     For example, ask your AI agent: *"Show me all logs for user <admin@example.com> from 2 PM to 3 PM yesterday"*

3. **Correlate with the OAuth client:** API calls originating from the AIC MCP Server use the `AICMCPClient` or `AICMCPExchangeClient` client IDs. Look for these identifiers in the log entries to distinguish MCP server actions from direct admin console or API activity.

|   |                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The AIC MCP Server's own logging tools can help with this investigation. Use prompts like *"Find all logs for transaction abc-123"* or *"Show me authentication events from the last hour"* to quickly locate relevant activity. |

### Identifying MCP traffic

All requests from the AIC MCP Server include a `User-Agent` header in the form `aic-mcp-server/<version>`. You can use this to filter access logs and isolate MCP-originated traffic from browser sessions, automated reconciliation jobs, and other API clients.

## Best practices

|   |                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | **Review all generated configuration** before promoting to production environments or those serving live identity and access requests. AI-driven operations can make mistakes. Treat AI-generated changes the same as any code review. |

Follow these best practices when using the AIC MCP Server:

1. **Use trusted AI agents.** Do not use the AIC MCP Server with untrusted MCP clients, agent code, or LLM inference. Depending on requests made to the server, tenant configuration or data can be returned.

2. **Review changes before promotion.** Configuration generated dynamically using LLM feedback can be represented dynamically back to agents and conversations. Always review before promoting to higher environments.

## Feedback and issues

Report security concerns, bugs, or enhancement requests through the [GitHub issue tracker](https://github.com/pingidentity/aic-mcp-server/issues).

---

---
title: Try it Out
description: Install and configure the AIC MCP Server to interact with your PingOne Advanced Identity Cloud environment using natural language.
component: build-with-ai
page_id: build-with-ai:aic-mcp-server:getting-started
canonical_url: https://developer.pingidentity.com/build-with-ai/aic-mcp-server/getting-started.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 20, 2026
keywords: ["MCP", "getting started", "install", "configure", "AIC"]
section_ids:
  prerequisites: Prerequisites
  install: Install
  npx-recommended: NPX (recommended)
  docker-deployment: Docker
  build-from-source: Build from source
  start-using-the-aic-mcp-server: Start using the AIC MCP Server
  next-steps: Next steps
---

# Try it Out

Get the AIC MCP Server running in your AI agent in minutes.

## Prerequisites

Before you start, make sure you have:

* [Node.js 18+](https://nodejs.org)

* A [Sandbox or Development](https://docs.pingidentity.com/pingoneaic/latest/tenants/environments.html) PingOne Advanced Identity Cloud tenant

* An MCP-compatible client, such as:

  * IDEs: [VS Code](https://code.visualstudio.com) with GitHub Copilot, [Cursor](https://cursor.com)

  * CLIs: [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [Codex](https://github.com/openai/codex)

  * Desktop apps: [Claude Desktop](https://claude.ai/download)

## Install

Choose an installation method:

* [NPX (recommended)](#npx-recommended)

* [Docker](#docker-deployment)

* [Build from source](#build-from-source)

### NPX (recommended)

The AIC MCP Server requires the `AIC_BASE_URL` environment variable to be set to your PingOne Advanced Identity Cloud hostname.

Add this to your MCP client configuration:

```json
{
  "mcpServers": {
    "aic-mcp-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@ping-identity/aic-mcp-server"],
      "env": {
        "AIC_BASE_URL": "your-tenant.forgeblocks.com"
      }
    }
  }
}
```

* VS Code (GitHub Copilot)

* Claude Code / Claude Desktop

* Cursor

* Gemini CLI

* Codex (OpenAI)

[![Install in VS Code Workspace](https://img.shields.io/badge/VS_Code-Install_in_Workspace-0098FF?style=flat-square\&logo=visualstudiocode\&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=aic-mcp-server\&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22pingone_aic_base_url%22%2C%22description%22%3A%22The%20base%20URL%20of%20the%20AIC%20tenant%22%2C%22password%22%3Afalse%7D%5D\&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40ping-identity%2Faic-mcp-server%22%5D%2C%22env%22%3A%7B%22AIC_BASE_URL%22%3A%22%24%7Binput%3Apingone_aic_base_url%7D%22%7D%7D)

|   |                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before clicking the install button, open VS Code with a project or working directory. When the MCP server panel opens, click **Install in Workspace**. The **Install** button may be unresponsive.![VS Code MCP server panel showing Install and Install in Workspace buttons](_images/vscode-install-in-workspace.png) |

Or add the configuration above to your Copilot MCP settings (`mcp.json`).

For more information, refer to [Microsoft's MCP documentation](https://code.visualstudio.com/docs/copilot/customization/mcp-servers).

Add the configuration to your Claude MCP configuration file:

* Claude Code: `claude.json`

* Claude Desktop: `claude_desktop_config.json`

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=pingone-aic\&config=eyJlbnYiOnsiQUlDX0JBU0VfVVJMIjoieW91ci10ZW5hbnQuZm9yZ2VibG9ja3MuY29tIn0sImNvbW1hbmQiOiJucHggLXkgQHBpbmctaWRlbnRpdHkvYWljLW1jcC1zZXJ2ZXIifQ%3D%3D)

Or add the configuration to your Cursor MCP configuration (`.cursor/mcp.json`).

Add the configuration to your Gemini CLI MCP configuration (`settings.json`).

Add the following to your Codex configuration file (`~/.codex/config.toml`):

```toml
[mcp_servers.aic-mcp-server]
command = "npx"
args = ["-y", "@ping-identity/aic-mcp-server"]
env = {"AIC_BASE_URL" = "your-tenant.forgeblocks.com"}
```

### Docker

You can also run the AIC MCP Server in a Docker container.

|   |                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Docker deployment uses OAuth 2.0 Device Code Flow with MCP form elicitation. This requires MCP client support for form elicitation, which is currently limited. If your client doesn't support it, use the [NPX](#npx-recommended) method instead. |

Add this to your MCP client configuration:

```json
{
  "mcpServers": {
    "aic-mcp-server": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "-e",
        "AIC_BASE_URL=your-tenant.forgeblocks.com",
        "pingidentity/aic-mcp-server:latest"
      ]
    }
  }
}
```

When authentication is required, your MCP client displays a URL. Click it to authenticate in your browser, then accept the prompt in your client.

|   |                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Authentication-related operations such as journey creation, app creation, and other AM-based tools are not currently available when using Docker. These tools require browser-based PKCE authentication, which is incompatible with the Device Code Flow used in containers. |

### Build from source

To build the AIC MCP Server from source:

```bash
# Clone the repository
git clone https://github.com/pingidentity/aic-mcp-server.git
cd aic-mcp-server

# Install dependencies
npm install

# Compile TypeScript
npm run build
```

Then configure your MCP client to use the local build:

```json
{
  "mcpServers": {
    "aic-mcp-server": {
      "command": "node",
      "args": ["/absolute/path/to/aic-mcp-server/dist/index.js"],
      "env": {
        "AIC_BASE_URL": "your-tenant.forgeblocks.com"
      }
    }
  }
}
```

## Start using the AIC MCP Server

1. Restart your MCP client after adding the configuration.

2. Start asking questions about your PingOne Advanced Identity Cloud environment.

3. On first tool use, your browser opens automatically for authentication at PingOne Advanced Identity Cloud.

4. After authenticating, your AI agent can interact with your tenant.

Try prompts like:

* "What managed object types are available in my environment?"

* "Show me all themes in the alpha realm"

* "Find all users with admin in their username"

## Next steps

* [See the full list of tools the server provides](available-tools.html)

* [Learn more about the authentication model](authentication.html)

* [Understand the security considerations](security.html)