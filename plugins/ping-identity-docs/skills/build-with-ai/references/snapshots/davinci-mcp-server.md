---
title: Authentication
description: How authentication works in the DaVinci MCP Server, including OAuth 2.0 PKCE flow, token storage, and regional configuration.
component: build-with-ai
page_id: build-with-ai:davinci-mcp-server:authentication
canonical_url: https://developer.pingidentity.com/build-with-ai/davinci-mcp-server/authentication.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 1, 2026
keywords: ["MCP", "authentication", "OAuth", "PKCE", "PingOne", "DaVinci", "keychain"]
section_ids:
  authentication-flow: Authentication flow
  worker-application-requirements: Worker application requirements
  regional-and-custom-domain-support: Regional and custom domain support
  authentication-constraints: Authentication constraints
  troubleshooting: Troubleshooting
---

# Authentication

The DaVinci MCP Server uses OAuth 2.0 Authorization Code flow with PKCE (Proof Key for Code Exchange) to ensure all actions are traceable to an individual PingOne user.

## Authentication flow

![DaVinci MCP tools diagram](_images/mcp-tools-diagram.png)

* 1 Tool discovery

  Your MCP client connects to the DaVinci MCP Server and discovers the available tools in the `davinci_admin` collection.

* 2 Tool request from the AI agent

  When you ask for DaVinci data (for example, flows or applications), the AI agent chooses the appropriate tool and sends a tool call to the server.

* 3 User authentication and token retrieval

  If no valid token exists, the server opens your browser for PingOne login and completes the OAuth 2.0 PKCE flow through `http://127.0.0.1:7474/callback`.

* 4 DaVinci API execution

  After authentication, the server calls the corresponding DaVinci APIs using your user context and returns structured results.

* 5 Response returned to the MCP client

  The server sends the tool response back to your MCP client, and your assistant presents it in natural language.

|   |                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Port `7474` must be available on `localhost` for the OAuth callback to succeed. If another process is using this port, authentication will fail. |

## Worker application requirements

The DaVinci MCP Server requires a PingOne worker application configured as a public client with PKCE. During token exchange, no `client_secret` is used.

The worker application must have:

* **Grant Types:** `Authorization Code`

* **Response Type:** `Code`

* **PKCE Enforcement:** `S256_REQUIRED`

* **Redirect URIs:** `http://127.0.0.1:7474/callback`

* **Token Endpoint Authentication Method:** `None`

For step-by-step setup instructions, refer to [Try it out](getting-started.html).

## Regional and custom domain support

The server connects to PingOne using the `ROOT_DOMAIN` environment variable. Set it to match your PingOne region:

| Region        | Value                            |
| ------------- | -------------------------------- |
| North America | `pingone.com`                    |
| Europe        | `pingone.eu`                     |
| Asia Pacific  | * `pingone.asia`

* `pingone.au` |
| Singapore     | `pingone.sg`                     |

If your organization uses a custom PingOne domain, set `CUSTOM_DOMAIN` to override the default. `ROOT_DOMAIN` selects the region, while `DAVINCI_MCP_ENVIRONMENT_ID` selects the specific environment within that region.

## Authentication constraints

The DaVinci MCP Server enforces the following authentication constraints:

* **Human-centric only:** Only browser-based flows that tie actions to an individual user are supported. Client credentials and non-interactive flows are not permitted.

* **No static secrets:** The server does not accept or store a static `client_secret`.

* **Tokens never stored in plain text:** All tokens are stored in the OS encrypted keychain. Tokens are never written to disk in plain text files, logs, or shell history.

## Troubleshooting

* **Port conflict**

  The callback server uses port `7474`. If authentication fails immediately, check whether another process is using this port.

* **Authentication timeout**

  The browser login must be completed within 5 minutes. If it times out, restart the tool call to trigger a new login.

* **Invalid or corrupted tokens**

  Use the `--logout` flag to clear stored tokens from the keychain and start again:

  ```bash
  npx -y @ping-identity/davinci-mcp-server start --logout
  ```

* **Keychain access on Linux**

  Ensure `libsecret` is installed for `keytar` to access the Linux Secret Service.

---

---
title: Available tools
description: An overview of the tool categories available in the DaVinci MCP Server.
component: build-with-ai
page_id: build-with-ai:davinci-mcp-server:available-tools
canonical_url: https://developer.pingidentity.com/build-with-ai/davinci-mcp-server/available-tools.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 1, 2026
keywords: ["MCP", "tools", "flows", "applications", "connectors", "variables", "forms", "DaVinci"]
section_ids:
  applications: Applications
  flows: Flows
  connectors: Connectors
  variables: Variables
  forms: Forms
  troubleshooting-tools: Troubleshooting tools
  common-troubleshooting-scenarios: Common troubleshooting scenarios
---

# Available tools

The DaVinci MCP Server exposes tools organized into functional categories under the `davinci_admin` collection. You don't need to know the individual tool name. Describe what you want in natural language and your AI agent automatically selects the right tool.

You can find the full tool reference in the [DaVinci MCP Server README](https://github.com/pingidentity/davinci-mcp-server#available-tools).

| Category                                  | What you can do                                                        |
| ----------------------------------------- | ---------------------------------------------------------------------- |
| [Applications](#applications)             | List applications and inspect flow policies.                           |
| [Flows](#flows)                           | List, describe, and version identity orchestration flows.              |
| [Connectors](#connectors)                 | Browse the connector catalog and inspect deployed connector instances. |
| [Variables](#variables)                   | List and inspect DaVinci flow variables.                               |
| [Forms](#forms)                           | List and inspect DaVinci form definitions.                             |
| [Troubleshooting](#troubleshooting-tools) | Validate flows, list executions, and investigate failures.             |

## Applications

List all DaVinci applications and retrieve their flow policy configurations.

| Tool                               | Description                                                        |
| ---------------------------------- | ------------------------------------------------------------------ |
| `list_applications`                | Returns a list of all DaVinci applications.                        |
| `describe_application`             | Returns details of a single DaVinci application by ID.             |
| `list_application_flow_policies`   | Returns all flow policies for a DaVinci application.               |
| `describe_application_flow_policy` | Returns details of a single flow policy for a DaVinci application. |

**Example prompts:**

* "List all DaVinci applications"

* "Show me the details of application abc123"

* "What flow policies are configured for the Login application?"

## Flows

List and inspect identity orchestration flows, including their full node graphs, edge definitions, and version history.

| Tool                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `list_flows`            | Returns a list of all DaVinci flows. Supports `attributes` to project the response to specific top-level fields. Flow type is derived from the `trigger` field: no trigger = standard flow; `trigger.type` `AUTHENTICATION` = PingOne flow; `trigger.type` `AUTHENTICATION` + `trigger.subtype` `CIBA` = CIBA flow; `trigger.type` `SCHEDULE` = scheduled flow; `trigger.type` `BATCH_PROCESSING_SUBFLOW` = batch processing subflow. `readOnly: true` means the flow is read-only. |
| `describe_flow`         | Returns the complete definition of a DaVinci flow including the full node graph, edges, and settings. Supports `attributes` to project the response to specific top-level fields. See `list_flows` for flow type derivation.                                                                                                                                                                                                                                                        |
| `list_flow_versions`    | Returns all versions of a specific DaVinci flow.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `describe_flow_version` | Returns the complete definition of a specific DaVinci flow version, including the full node graph, edges, settings, and trigger configuration. Supports `expand` to include related fields inline (for example, `skcomponents`).                                                                                                                                                                                                                                                    |

**Example prompts:**

* "List all DaVinci flows"

* "Show me the full definition of the Login flow"

* "How many versions does the Registration flow have?"

* "Show me version 3 of the MFA flow"

## Connectors

Browse the full [DaVinci connector catalog](https://marketplace.pingone.com/browse?contentType=davinciConnectors) and inspect deployed connector instances in your environment.

| Tool                          | Description                                                                                                                                             |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `list_connectors`             | Returns a list of all available DaVinci connector types from the catalog.                                                                               |
| `describe_connector`          | Returns the full details of a single DaVinci connector type by ID, including metadata, capabilities, configurable properties, and required credentials. |
| `list_connector_instances`    | Returns a list of all DaVinci connector instances.                                                                                                      |
| `describe_connector_instance` | Returns details of a single deployed DaVinci connector instance by ID.                                                                                  |

**Example prompts:**

* "What connectors are available in DaVinci?"

* "Show me the details of the PingOne connector"

* "List all connector instances deployed in my environment"

## Variables

List and inspect DaVinci variables and their configured values.

| Tool                | Description                                                                                                                       |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `list_variables`    | Returns a list of all DaVinci variables. Supports `limit` (1-50), `cursor` for pagination, and a SCIM `filter` to narrow results. |
| `describe_variable` | Returns details of a single DaVinci variable by ID.                                                                               |

**Example prompts:**

* "List all DaVinci variables"

* "Show me details of the sessionTimeout variable"

## Forms

List and inspect DaVinci form definitions and their full configurations.

| Tool            | Description                                                                                                                                                           |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `list_forms`    | Returns a list of all DaVinci forms. Use for discovery and finding form IDs. Use describe\_form for field-level details. Supports a SCIM `filter` on `category` (eq). |
| `describe_form` | Returns full configuration of a single DaVinci form including fields and layout.                                                                                      |

**Example prompts:**

* "List all DaVinci forms"

* "Show me the full configuration of the Login form"

## Troubleshooting tools

Diagnose and investigate DaVinci flow issues. Validate flow configuration before deployment, retrieve execution history, and inspect individual execution details including errors and stack traces. These tools can help speed up triage, root-cause analysis, and escalation handoffs for helpdesk and support teams.

These tools are provided under the `davinci_troubleshooting` collection.

| Tool                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `validate_flow`            | Validates a DaVinci flow configuration using the DVLinter validation engine. Checks deployment readiness, identifies configuration errors and best-practice violations, and analyzes nodes (connectors and capabilities), connections (connector instances), node properties, and overall flow structure. Returns validation results including error and warning counts and specific issue descriptions. Error locations are reported in the `linterError` property within each node in `graphData.elements.nodes` for node-specific issues, and in the `allLinterErrors` property in `graphData` for flow-level errors and warnings. Zero errors indicate deployment-ready status. This is a read-only operation that does not modify the flow. |
| `list_flow_executions`     | Returns a list of all executions for a specific DaVinci flow. Use to find execution IDs for troubleshooting, debugging, or monitoring. Supports `limit` (max 500), `cursor` for pagination, and a SCIM `filter` on `timestamp` (`ge`, `le`) with ISO 8601 dates, and `transactionId` (`eq`) for specific transaction lookup.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `summarize_flow_execution` | Returns detailed information about a specific DaVinci flow execution, including status (success or failure), timestamps, input and output data, errors with stack traces, and user context. Use to debug failures, analyze execution behavior, verify data transformations, or investigate user-specific issues. Supports `limit` (max 500), `cursor` for pagination, and a SCIM `filter` on `timestamp` (`ge`, `le`) with ISO 8601 dates.                                                                                                                                                                                                                                                                                                       |

**Example prompts:**

* "Validate the Login flow and tell me if it's ready to deploy"

* "Are there any configuration errors or warnings in the MFA flow?"

* "List the last 20 executions of the Registration flow"

* "Show me all executions of the Login flow from yesterday"

* "Find the execution with transaction ID abc-123 in the Login flow"

* "What happened during execution xyz-456? Did it succeed?"

* "Show me the error and stack trace for the failed execution xyz-456"

* "What input data was passed to the last execution of the Password Reset flow?"

### Common troubleshooting scenarios

* **Debugging a failed user authentication**

  Use `list_flow_executions` with a `transactionId` filter to find the specific execution, then use `summarize_flow_execution` to inspect the error and stack trace.

  "Find executions of the Login flow with transaction ID abc-123 and summarize what went wrong."

* **Investigating recent failures across a flow**

  Use `list_flow_executions` with a `timestamp` range filter to retrieve recent executions, then use `summarize_flow_execution` on the failed ones.

  "List all executions of the MFA flow in the last 24 hours and identify any that failed."

* **Verifying data transformations**

  Use `summarize_flow_execution` to inspect the input and output data of a specific execution and confirm values are being transformed as expected.

  "Show me the input and output data for execution xyz-456 of the Registration flow."

* **Investigating user-specific issues**

  Use `summarize_flow_execution` to retrieve the user context associated with a specific execution.

  "Find executions of user <abc@acme.com> and diagnose why they were unable to authenticate."

---

---
title: Client configuration
description: MCP client configuration examples, CLI flags, and advanced usage for the DaVinci MCP Server.
component: build-with-ai
page_id: build-with-ai:davinci-mcp-server:client-configuration
canonical_url: https://developer.pingidentity.com/build-with-ai/davinci-mcp-server/client-configuration.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 1, 2026
keywords: ["MCP", "configuration", "Claude", "Cursor", "VS Code", "Gemini", "CLI", "DaVinci"]
section_ids:
  mcp-client-configuration: MCP client configuration
  cli-flags: CLI flags
  filter-tools: Filter tools
  other-flags: Other flags
  advanced-configuration-examples: Advanced configuration examples
  maintenance-commands: Maintenance commands
---

# Client configuration

This page covers client-specific configuration formats, CLI flags, and advanced configuration examples for the DaVinci MCP Server.

Replace `your-environment-id` and `your-client-id` with your actual PingOne environment ID and OAuth Client ID in all examples below. `DAVINCI_MCP_ENVIRONMENT_ID` selects which PingOne/DaVinci environment the server queries, while `AUTHORIZATION_CODE_CLIENT_ID` identifies your worker application.

## MCP client configuration

* Claude Desktop

* Claude Code (CLI)

* VS Code (Cline)

* Cursor

* Gemini CLI

Add the following to your `claude_desktop_config.json`:

* **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

* **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "davinci": {
      "command": "npx",
      "args": ["-y", "@ping-identity/davinci-mcp-server", "start"],
      "env": {
        "DAVINCI_MCP_ENVIRONMENT_ID": "your-environment-id",
        "AUTHORIZATION_CODE_CLIENT_ID": "your-client-id",
        "ROOT_DOMAIN": "pingone.com"
      }
    }
  }
}
```

Run the following command in your terminal:

```bash
claude mcp add --transport stdio davinci \
--env DAVINCI_MCP_ENVIRONMENT_ID="your-environment-id" \
--env AUTHORIZATION_CODE_CLIENT_ID="your-client-id" \
--env ROOT_DOMAIN="pingone.com" \
-- npx -y @ping-identity/davinci-mcp-server start
```

1. Open the Cline sidebar in VS Code.

2. Click the **Settings** [icon: gear, set=fa]icon.

3. Scroll to **MCP Servers** and click **Add MCP Server**.

4. Use the following configuration:

   ```json
   {
     "davinci": {
       "command": "npx",
       "args": ["-y", "@ping-identity/davinci-mcp-server", "start"],
       "env": {
         "DAVINCI_MCP_ENVIRONMENT_ID": "your-environment-id",
         "AUTHORIZATION_CODE_CLIENT_ID": "your-client-id",
         "ROOT_DOMAIN": "pingone.com"
       }
     }
   }
   ```

1) Open Cursor **Settings** > **Features** > **MCP**.

2) Click **+ Add New MCP Server**.

3) Set the following:

   * **Name:** `davinci`

   * **Type:** `command`.

   * **Command:**

     ```bash
     npx -y @ping-identity/davinci-mcp-server start
     ```

4) Add environment variables:

   * `DAVINCI_MCP_ENVIRONMENT_ID`: `your-environment-id`

   * `AUTHORIZATION_CODE_CLIENT_ID`: `your-client-id`

   * `ROOT_DOMAIN`: `pingone.com`

Use the target PingOne environment UUID for `DAVINCI_MCP_ENVIRONMENT_ID` (not the OAuth client ID).

Add the following to your `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    "davinci": {
      "command": "npx",
      "args": ["-y", "@ping-identity/davinci-mcp-server", "start"],
      "env": {
        "DAVINCI_MCP_ENVIRONMENT_ID": "your-environment-id",
        "AUTHORIZATION_CODE_CLIENT_ID": "your-client-id",
        "ROOT_DOMAIN": "pingone.com"
      }
    }
  }
}
```

## CLI flags

The `start` command supports the following flags. Add them to the `args` array in your MCP client configuration.

### Filter tools

| Flag                           | Description                                                                         |
| ------------------------------ | ----------------------------------------------------------------------------------- |
| `--include-collections <list>` | Comma-separated list of collection names to include (for example, `davinci_admin`). |
| `--exclude-collections <list>` | Comma-separated list of collection names to exclude.                                |
| `--include-tools <list>`       | Comma-separated list of tool names to include.                                      |
| `--exclude-tools <list>`       | Comma-separated list of tool names to exclude.                                      |

### Other flags

| Flag        | Description                                              |
| ----------- | -------------------------------------------------------- |
| `--verbose` | Enable verbose logging to `stderr`.                      |
| `--logout`  | Clear stored tokens from the system keychain on startup. |
| `--help`    | Show the help message and exit.                          |

## Advanced configuration examples

> **Collapse: Filter by tool collection**
>
> Limit exposed tools to only those in the `davinci_admin` collection.
>
> ```json
> {
>   "mcpServers": {
>     "davinci": {
>       "command": "npx",
>       "args": [
>         "-y",
>         "@ping-identity/davinci-mcp-server",
>         "start",
>         "--include-collections",
>         "davinci_admin"
>       ],
>       "env": {
>         "DAVINCI_MCP_ENVIRONMENT_ID": "your-environment-id",
>         "AUTHORIZATION_CODE_CLIENT_ID": "your-client-id",
>         "ROOT_DOMAIN": "pingone.com"
>       }
>     }
>   }
> }
> ```

> **Collapse: Filter by specific tools**
>
> Expose only a targeted set of tools, such as only flow tools.
>
> ```json
> {
>   "mcpServers": {
>     "davinci": {
>       "command": "npx",
>       "args": [
>         "-y",
>         "@ping-identity/davinci-mcp-server",
>         "start",
>         "--include-tools",
>         "list_flows,describe_flow"
>       ],
>       "env": {
>         "DAVINCI_MCP_ENVIRONMENT_ID": "your-environment-id",
>         "AUTHORIZATION_CODE_CLIENT_ID": "your-client-id",
>         "ROOT_DOMAIN": "pingone.com"
>       }
>     }
>   }
> }
> ```

> **Collapse: Exclude specific tools**
>
> Enable all tools except variable-related ones.
>
> ```json
> {
>   "mcpServers": {
>     "davinci": {
>       "command": "npx",
>       "args": [
>         "-y",
>         "@ping-identity/davinci-mcp-server",
>         "start",
>         "--exclude-tools",
>         "describe_variable,list_variables"
>       ],
>       "env": {
>         "DAVINCI_MCP_ENVIRONMENT_ID": "your-environment-id",
>         "AUTHORIZATION_CODE_CLIENT_ID": "your-client-id",
>         "ROOT_DOMAIN": "pingone.com"
>       }
>     }
>   }
> }
> ```

> **Collapse: Enable verbose logging**
>
> Enable detailed logging to help debug connection or tool issues.
>
> ```json
> {
>   "mcpServers": {
>     "davinci": {
>       "command": "npx",
>       "args": ["-y", "@ping-identity/davinci-mcp-server", "start", "--verbose"],
>       "env": {
>         "DAVINCI_MCP_ENVIRONMENT_ID": "your-environment-id",
>         "AUTHORIZATION_CODE_CLIENT_ID": "your-client-id",
>         "ROOT_DOMAIN": "pingone.com"
>       }
>     }
>   }
> }
> ```

## Maintenance commands

Run these commands manually in your terminal when needed.

* Clear stored credentials:

  ```bash
  npx -y @ping-identity/davinci-mcp-server start --logout
  ```

* Display help:

  ```bash
  npx -y @ping-identity/davinci-mcp-server --help
  ```

---

---
title: Overview
description: An overview of the DaVinci MCP Server for interacting with PingOne DaVinci identity orchestration resources using natural language.
component: build-with-ai
page_id: build-with-ai:davinci-mcp-server:overview
canonical_url: https://developer.pingidentity.com/build-with-ai/davinci-mcp-server/overview.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 1, 2026
keywords: ["MCP", "AI", "DaVinci", "PingOne", "Model Context Protocol", "identity orchestration"]
section_ids:
  what-you-can-do: What you can do
  example-prompts: Example prompts
  key-features: Key features
  next-steps: Next steps
---

# Overview

The DaVinci MCP Server is an open-source [TypeScript tool](https://github.com/pingidentity/davinci-mcp-server) that enables AI agents to interact with PingOne's DaVinci no-code identity orchestration platform. It implements the [Model Context Protocol (MCP)](https://modelcontextprotocol.io), exposing tools that wrap DaVinci's REST APIs as MCP-compatible functions.

Instead of manually navigating the DaVinci console or hand-crafting API requests, describe what you want in natural language. Your AI agent translates your intent to the right MCP tools, the server handles the API calls and authentication, and returns results your agent can present naturally.

Learn more about the DaVinci console in [DaVinci Best Practices](https://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices.html). For the DaVinci API reference, refer to [DaVinci API documentation](https://developer.pingidentity.com/pingone-api/davinci/).

## What you can do

The DaVinci MCP Server acts as a bridge between MCP-compatible AI agents and the DaVinci API, enabling:

* **Flow management:** List and inspect DaVinci flows and their versions.

* **Application configuration:** Access application settings and flow policies.

* **Connector management:** View available connectors and their configurations.

* **Variable management:** Manage DaVinci variables and their values.

* **Form management:** Access form definitions and configurations.

* **Connector instances:** Manage connector instance configurations.

### Example prompts

| Category                  | Example prompts                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Flow management           | "Show me all DaVinci flows", "Describe the Login flow", "List all versions of the Registration flow"                      |
| Application configuration | "What applications are using the Login flow?", "Show me the flow policy for MyApp", "List all configured applications"    |
| Connector management      | "What connectors are available?", "Show me the Facebook connector configuration", "List all deployed connector instances" |
| Variable management       | "List all DaVinci variables", "Show me the value of the API\_KEY variable", "What variables are used in the Login flow?"  |
| Form management           | "Show me all DaVinci forms", "Describe the login form", "What forms are used in the Registration flow?"                   |

## Key features

* **Natural language interaction:** Interact with DaVinci from whichever AI tool you use daily, without switching to the console or writing API scripts.

* **Secure authentication:** Uses OAuth 2.0 Authorization Code flow with PKCE. Tokens are stored securely in the OS keychain.

* **Broad tool support:** Read-oriented tools across DaVinci flows, applications, connectors, variables, forms, and connector instances.

* **Regional support:** Configurable for different PingOne regional domains (NA, EU, APAC) and custom domains.

## Next steps

* [Install and configure the DaVinci MCP Server](getting-started.html)

* [Explore the full list of available tools](available-tools.html)

* [Learn how authentication works](authentication.html)

* [Understand the security model](security.html)

---

---
title: Security
description: Security considerations and best practices for the DaVinci MCP Server.
component: build-with-ai
page_id: build-with-ai:davinci-mcp-server:security
canonical_url: https://developer.pingidentity.com/build-with-ai/davinci-mcp-server/security.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 1, 2026
keywords: ["MCP", "security", "least privilege", "DaVinci", "PingOne", "audit"]
section_ids:
  security-model: Security model
  principle-of-least-privilege: Principle of least privilege
  data-handling: Data handling
  best-practices: Best practices
  feedback-and-issues: Feedback and issues
---

# Security

The DaVinci MCP Server gives an AI model access to your DaVinci environment configuration. This page describes the security model and the practices you should follow.

|   |                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------- |
|   | All data returned from tools might be sent to the LLM provider. Only use this server with trusted MCP clients and AI agents. |

## Security model

* Secure credential storage

  Tokens are stored in the OS keychain (macOS Keychain, Windows Credential Manager, Linux Secret Service) and are never written to disk in plain text.

* No static secrets

  The server does not accept or store a `client_secret`. All authentication is user-initiated and PKCE-protected.

* OAuth 2.0 with PKCE

  The Authorization Code flow with PKCE prevents authorization code interception attacks.

* User-based authentication

  All API calls are made as the authenticated PingOne user, providing a complete audit trail in PingOne.

* Human-centric only

  Client credentials and non-interactive authentication methods are explicitly forbidden. Every action is tied to a human who signed on interactively.

## Principle of least privilege

Assign the authenticating user only the minimum permissions needed. For read-only use cases, assign the **DaVinci Admin Read Only** role.

|   |                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Do not authenticate as a PingOne administrator with full privileges unless your use case specifically requires write access. The DaVinci MCP Server currently exposes read-only tools, but the authenticated user's permissions determine what the underlying API will allow. |

## Data handling

The DaVinci MCP Server returns DaVinci resource data as tool outputs, including flow definitions, connector configurations, and application settings as tool outputs. This data is passed back to your AI agent and might be included in prompts sent to your LLM provider.

Consider the sensitivity of the data in your environment before using the server with a third-party AI provider.

## Best practices

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Always review AI-generated configurations or insights before applying them to a live environment. AI-driven operations can make mistakes. Review AI-generated output more carefully than other changes. |

1. **Use trusted MCP clients.** Do not use the DaVinci MCP Server with untrusted MCP clients, agent code, or LLM inference endpoints.

2. **Follow least privilege.** Authenticate as a user with the minimum necessary permissions.

3. **Review before acting.** Never apply AI-generated DaVinci flow or configuration changes without reviewing them first.

4. **Use in non-production environments.** Given the preview status of this server, treat production environments with extra caution.

## Feedback and issues

Report security concerns, bugs, or enhancement requests through the [GitHub issue tracker](https://github.com/pingidentity/davinci-mcp-server/issues).

---

---
title: Try it out
description: Install and configure the DaVinci MCP Server to interact with your PingOne DaVinci environment using natural language.
component: build-with-ai
page_id: build-with-ai:davinci-mcp-server:getting-started
canonical_url: https://developer.pingidentity.com/build-with-ai/davinci-mcp-server/getting-started.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 1, 2026
keywords: ["MCP", "getting started", "install", "configure", "DaVinci", "PingOne"]
section_ids:
  prerequisites: Prerequisites
  setup: Setup
  1-create-a-pingone-worker-application: 1. Create a PingOne worker application
  2-assign-a-role-to-the-authenticating-user: 2. Assign a role to the authenticating user
  3-configure-environment-variables: 3. Configure environment variables
  install: Install
  quick-install: Quick install
  manual-install-npx: Manual install (NPX)
  start-using-the-davinci-mcp-server: Start using the DaVinci MCP Server
  next-steps: Next steps
---

# Try it out

Connect the DaVinci MCP Server to your MCP client.

## Prerequisites

Before you start, make sure you have:

* [Node.js 22.0.0+](https://nodejs.org/en/download/package-manager)

* A licensed or trial [PingOne subscription](https://www.pingidentity.com/en/try-ping.html)

* DaVinci enabled in your environment: in the PingOne admin console, go to **Environments** > **Your Environment** > **Services** and ensure **DaVinci** is listed and active.

* An MCP-compatible client, such as:

  * IDEs: [VS Code](https://code.visualstudio.com) with GitHub Copilot, [Cursor](https://cursor.com)

  * CLIs: [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview), [Gemini CLI](https://github.com/google-gemini/gemini-cli)

  * Desktop apps: [Claude Desktop](https://claude.ai/download)

## Setup

### 1. Create a PingOne worker application

The DaVinci MCP Server requires a worker application to authenticate with the PingOne APIs.

1. In the [PingOne admin console](https://admin.pingone.com), select the environment where DaVinci is enabled.

2. Click **Applications** > **Applications** in the left navigation menu.

3. Click **+ Add Application** and select **Worker**.

   1. Enter the following:

      * **Name:** For example, `DaVinci MCP Server`.

      * **Description:** Optional.

   2. Click **Save**.

   3. Enable the application using the toggle at the top right of the details panel.

4. On the **Configuration** tab, click the **Edit** [icon: pencil, set=fa]icon and set:

   * **Grant Types:** `Authorization Code`

   * **Response Type:** `Code`

   * **PKCE Enforcement:** `S256_REQUIRED`

   * **Redirect URIs:** `http://127.0.0.1:7474/callback`

   * **Token Endpoint Authentication Method:** `None` (Public Client)

5. Click **Save**.

6. Copy the **Client ID** from the **Configuration** tab.

   |   |                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You'll need this for `AUTHORIZATION_CODE_CLIENT_ID`. This identifies the PingOne worker application your MCP client uses during OAuth authentication. |

7. Copy the **Environment ID** from the URL or environment settings.

   |   |                                                                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You'll need this for `DAVINCI_MCP_ENVIRONMENT_ID`. This is the UUID of the target PingOne environment that contains the DaVinci resources the server should access. |

### 2. Assign a role to the authenticating user

1. In the PingOne admin console, click **Directory** > **Users**.

2. Create a new user or select an existing one.

3. Navigate to the user's **Roles** tab and click **Grant Roles**.

4. Search for and select **DaVinci Admin Read Only**. Click **Save**.

### 3. Configure environment variables

The server reads the following environment variables. You can set these in your MCP client configuration:

| Variable                       | Description                                                                                                                                       | Example                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| `DAVINCI_MCP_ENVIRONMENT_ID`   | The UUID of the PingOne environment that contains your DaVinci resources. The server uses this to target API requests to the correct environment. | `a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6`                       |
| `AUTHORIZATION_CODE_CLIENT_ID` | The client ID of your PingOne worker application.                                                                                                 | `your-client-id`                                             |
| `ROOT_DOMAIN`                  | The regional PingOne domain. Refer to [Regional and custom domain support](authentication.html#regional-and-custom-domain-support).               | `pingone.com` (NA), `pingone.eu` (EU), `pingone.asia` (APAC) |
| `CUSTOM_DOMAIN`                | (Optional) Your custom PingOne domain. Refer to [Regional and custom domain support](authentication.html#regional-and-custom-domain-support).     | `auth.example.com`                                           |

## Install

### Quick install

Use the one-click install links for the fastest setup:

When prompted for an environment ID, enter the target PingOne environment UUID, not your worker application client ID.

[![Install in VS Code Workspace](https://img.shields.io/badge/VS_Code-Install_in_Workspace-0098FF?style=flat-square\&logo=visualstudiocode\&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=davinci\&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22davinci_environment_id%22%2C%22description%22%3A%22The%20ID%20of%20your%20PingOne%20environment%22%2C%22password%22%3Afalse%7D%2C%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22authorization_code_client_id%22%2C%22description%22%3A%22The%20Client%20ID%20of%20your%20PingOne%20Worker%20Application%22%2C%22password%22%3Afalse%7D%2C%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22root_domain%22%2C%22description%22%3A%22The%20regional%20PingOne%20domain%20%28e.g.%2C%20pingone.com%2C%20pingone.eu%2C%20pingone.asia%29%22%2C%22password%22%3Afalse%7D%5D\&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40ping-identity%2Fdavinci-mcp-server%22%2C%22start%22%5D%2C%22env%22%3A%7B%22DAVINCI_MCP_ENVIRONMENT_ID%22%3A%22%24%7Binput%3Adavinci_environment_id%7D%22%2C%22AUTHORIZATION_CODE_CLIENT_ID%22%3A%22%24%7Binput%3Aauthorization_code_client_id%7D%22%2C%22ROOT_DOMAIN%22%3A%22%24%7Binput%3Aroot_domain%7D%22%7D%7D)

|   |                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before clicking the install button, open VS Code with a project or working directory. When the MCP server panel opens, click **Install in Workspace**. The **Install** button may be unresponsive.![VS Code MCP server panel showing Install and Install in Workspace buttons](_images/vscode-install-in-workspace.png) |

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=davinci\&config=eyJlbnYiOnsiREFWSU5DSV9NQ1BfRU5WSVJPTk1FTlRfSUQiOiI8PHBhc3RlIGVudmlyb25tZW50IFVVSUQgaGVyZT4+IiwiQVVUSE9SSVpBVElPTl9DT0RFX0NMSUVOVF9JRCI6Ijw8cGFzdGUgY2xpZW50IElEIFVVSUQgaGVyZT4+IiwiUk9PVF9ET01BSU4iOiI8PHBhc3RlIHJvb3QgZG9tYWluIGhlcmUgKGUuZy4sIHBpbmdvbmUuY29tKT4+In0sImNvbW1hbmQiOiJucHggLXkgQHBpbmctaWRlbnRpdHkvZGF2aW5jaS1tY3Atc2VydmVyIHN0YXJ0In0%3D)

### Manual install (NPX)

Add the following to your MCP client configuration, replacing the placeholder values with your actual credentials. Set `DAVINCI_MCP_ENVIRONMENT_ID` to the UUID of the PingOne environment you want the server to query:

```json
{
  "mcpServers": {
    "davinci": {
      "command": "npx",
      "args": ["-y", "@ping-identity/davinci-mcp-server", "start"],
      "env": {
        "DAVINCI_MCP_ENVIRONMENT_ID": "your-environment-id",
        "AUTHORIZATION_CODE_CLIENT_ID": "your-client-id",
        "ROOT_DOMAIN": "pingone.com"
      }
    }
  }
}
```

For client-specific configuration formats, CLI flags, and advanced examples, refer to [Client configuration](client-configuration.html).

## Start using the DaVinci MCP Server

1. Restart your MCP client after adding the configuration.

2. Run a read tool such as `list_flows`, `list_applications`, or `list_connectors` to trigger authentication. Your browser opens automatically.

3. Log in with the PingOne user you assigned the **DaVinci Admin Read Only** role.

4. After authenticating, your MCP client can interact with your DaVinci environment.

Try prompts like:

* "List all DaVinci flows in my environment"

* "Show me the details of the Login flow"

* "What connectors are available?"

* "List all DaVinci applications"

## Next steps

* [Configure your MCP client or filter tools](client-configuration.html)

* [View the full list of tools the server provides](available-tools.html)

* [Learn more about the authentication model](authentication.html)

* [Understand the security considerations](security.html)