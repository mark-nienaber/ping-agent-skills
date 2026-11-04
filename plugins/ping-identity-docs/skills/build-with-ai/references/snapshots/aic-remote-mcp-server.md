---
title: Available Tools
description: Full list of tools exposed by the AIC Remote MCP Server, organized by category and grouped by required scope.
component: build-with-ai
page_id: build-with-ai:aic-remote-mcp-server:available-tools
canonical_url: https://developer.pingidentity.com/build-with-ai/aic-remote-mcp-server/available-tools.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-10-28T00:00:00Z
keywords: ["MCP", "AI", "Advanced Identity Cloud", "tools", "managed objects", "journeys", "themes", "applications", "logs", "reports", "PingOne Advanced Identity Cloud"]
section_ids:
  managed-objects: Managed objects
  example-prompts: Example prompts
  themes: Themes
  example-prompts-2: Example prompts
  logging: Logging
  example-prompts-3: Example prompts
  esvs: ESVs (Environment Secrets and Variables)
  example-prompts-4: Example prompts
  feature-management: Feature management
  example-prompts-5: Example prompts
  applications: Applications
  example-prompts-6: Example prompts
  am-journeys-nodes-and-scripts: AM journeys, nodes, and scripts
  example-prompts-7: Example prompts
  am-services-and-identity-providers: AM services and identity providers
  example-prompts-8: Example prompts
  cors-policies: CORS policies
  example-prompts-9: Example prompts
  policy-and-notifications: Policy and notifications
  example-prompts-10: Example prompts
  reporting: Reporting
  example-prompts-11: Example prompts
---

# Available Tools

|   |                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The AIC Remote MCP Server is currently available in sandbox\[[1](#_footnotedef_1 "View footnote.")] environments only. Support for development, UAT\[[2](#_footnotedef_2 "View footnote.")], staging, and production environments is rolling out over the coming weeks. |

The AIC Remote MCP Server exposes tools for administering your PingOne Advanced Identity Cloud environment through an AI client. You don't need to know the individual tool names. Describe what you want in natural language and your AI agent selects the right tool automatically.

Every request must include the mandatory `aic:mcp:access` scope. Each category table below groups its tools by the additional scope required. For the full scope reference and per-tier request lists, refer to [Scopes](scopes.html). Available tools also depend on environment mutability. Refer to [Environments and access](overview.html#environments-and-access).

| Category                                                                  | What you can do                                                                                                                           |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [Managed objects](#managed-objects)                                       | Create, query, update, and delete managed objects, object types, and custom relationships.                                                |
| [Themes](#themes)                                                         | List, create, update, delete, and set default themes.                                                                                     |
| [Logging](#logging)                                                       | List log sources and query authentication and activity logs.                                                                              |
| [ESVs](#esvs)                                                             | Query, create, update, and delete environment variables and secrets, and publish ESV changes.                                             |
| [Feature management](#feature-management)                                 | Inspect and install optional IDM and platform features.                                                                                   |
| [Applications](#applications)                                             | List, retrieve, create, update, and delete applications, including SAML applications, application templates, and provisioning connectors. |
| [AM journeys, nodes, and scripts](#am-journeys-nodes-and-scripts)         | Manage authentication journeys, node types, and Scripted Decision Node scripts.                                                           |
| [AM services and identity providers](#am-services-and-identity-providers) | Inspect and configure AM services and social identity providers.                                                                          |
| [CORS policies](#cors-policies)                                           | Manage cross-origin resource sharing policies.                                                                                            |
| [Policy and notifications](#policy-and-notifications)                     | Manage email templates, outbound email, password policies, and terms and conditions.                                                      |
| [Reporting](#reporting)                                                   | Query, run, and author reports.                                                                                                           |

## Managed objects

Generic CRUD operations for any managed object type in your environment, plus administrative tools for managing object type definitions and custom relationship properties.

| Scope                      | Tool                             | Description                                                                                                |
| -------------------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `aic:mcp:identities.read`  | `listManagedObjects`             | Discover all managed object types in your environment.                                                     |
|                            | `getManagedObjectSchema`         | Get the schema definition for an object type.                                                              |
|                            | `queryManagedObjects`            | Query objects with filters, pagination, and sorting.                                                       |
|                            | `getManagedObject`               | Retrieve an object's complete profile.                                                                     |
| `aic:mcp:identities.write` | `createManagedObject`            | Create a new managed object.                                                                               |
|                            | `patchManagedObject`             | Update object fields.                                                                                      |
|                            | `deleteManagedObject`            | Delete an object.                                                                                          |
|                            | `createManagedObjectDefinition`  | Create a new managed object type definition.                                                               |
|                            | `patchManagedObjectDefinition`   | Modify an existing managed object type definition.                                                         |
|                            | `deleteManagedObjectDefinition`  | Delete a managed object type definition.                                                                   |
|                            | `patchManagedObjectRelationship` | Add, update, or remove a custom relationship property. Custom relationships must use the `custom_` prefix. |

### Example prompts

* "List all managed object types in my tenant"

* "Show me the schema for the alpha_user managed object"

* "Find users whose email starts with admin@"

* "Create a managed object for this user"

## Themes

Customize login and account page appearance.

| Scope                  | Tool              | Description                              |
| ---------------------- | ----------------- | ---------------------------------------- |
| `aic:mcp:themes.read`  | `getThemeSchema`  | Get complete theme schema documentation. |
|                        | `getThemes`       | List all themes in a realm.              |
|                        | `getTheme`        | Get a theme's complete configuration.    |
| `aic:mcp:themes.write` | `createTheme`     | Create a new theme.                      |
|                        | `updateTheme`     | Update theme properties.                 |
|                        | `deleteTheme`     | Delete a theme.                          |
|                        | `setDefaultTheme` | Set a theme as the realm default.        |

### Example prompts

* "List all themes in my realm"

* "Show me the current login theme"

* "Create a new theme with this primary color"

* "Set this theme as the default"

## Logging

Query and analyze authentication and activity logs.

| Scope               | Tool            | Description                                              |
| ------------------- | --------------- | -------------------------------------------------------- |
| `aic:mcp:logs.read` | `getLogSources` | List available log sources.                              |
|                     | `queryLogs`     | Query logs with time range, source, and content filters. |

### Example prompts

* "List available log sources"

* "Show authentication errors from the last hour"

* "Query activity logs for failed requests"

## ESVs (Environment Secrets and Variables)

Manage environment variables used for configuration across your tenant.

| Scope                 | Tool             | Description                                                           |
| --------------------- | ---------------- | --------------------------------------------------------------------- |
| `aic:mcp:esv.read`    | `queryESVs`      | Query variables or secrets by ID pattern.                             |
|                       | `getVariable`    | Retrieve a variable with its decoded value.                           |
| `aic:mcp:esv.write`   | `setVariable`    | Create or update a variable.                                          |
|                       | `deleteVariable` | Delete a variable.                                                    |
| `aic:mcp:esv.restart` | `publishESVs`    | Restart PingOne Advanced Identity Cloud to apply pending ESV changes. |

### Example prompts

* "List the environment variables in my tenant"

* "Get the value of this environment variable"

* "Set an environment variable for this configuration"

* "Publish my ESV changes"

## Feature management

Inspect and enable optional IDM and platform features.

| Scope                  | Tool                 | Description                                                               |
| ---------------------- | -------------------- | ------------------------------------------------------------------------- |
| `aic:mcp:idm.read`     | `listFeatures`       | List all features (IDM + AIC platform) and their install status.          |
|                        | `validateIdmFeature` | Check whether an IDM feature can be installed without making any changes. |
| `aic:mcp:idm.write`    | `installIdmFeature`  | Install an IDM feature. Run `validateIdmFeature` first.                   |
| `aic:mcp:agents.write` | `enableAiAgent`      | Enable AI Agents on the tenant. Re-running is safe.                       |

### Example prompts

* "Which IDM features are installed?"

* "Can I install the groups feature?"

* "Enable AI Agents"

## Applications

Manage OIDC/SAML SSO integration, application provisioning, and data reconciliation.

| Scope                | Tool                          | Description                                                                                                                                      |
| -------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `aic:mcp:apps.read`  | `listApplications`            | List all applications in a realm regardless of type, with summary fields only.                                                                   |
|                      | `getApplication`              | Retrieve a single application by name or ID, regardless of type.                                                                                 |
|                      | `getOidcAppSchema`            | Get the OIDC application schema.                                                                                                                 |
|                      | `listOidcApps`                | List OIDC applications in a realm with summary fields.                                                                                           |
|                      | `getOidcApp`                  | Retrieve a complete OIDC application configuration.                                                                                              |
|                      | `listApplicationTemplates`    | List available application templates.                                                                                                            |
|                      | `getApplicationTemplate`      | Get a complete application template definition.                                                                                                  |
|                      | `getConnectorSchema`          | Discover available connector bundles, or get a configuration skeleton for a selected connector.                                                  |
|                      | `getProvisioningAppConfig`    | Read a provisioning application's persisted connector and mapping configuration, including sync-engine diagnostics.                              |
|                      | `verifyConnectorConnectivity` | Test one connector or all connectors, and report connectivity and discovered object types.                                                       |
|                      | `getReconciliationStatus`     | Check the result of a reconciliation run, or list recent runs.                                                                                   |
| `aic:mcp:apps.write` | `createOidcApp`               | Create a new OIDC application.                                                                                                                   |
|                      | `updateOidcApp`               | Update an OIDC application. Partial updates. Send only changed fields.                                                                           |
|                      | `createSamlApp`               | Create a SAML SSO application from the service provider's metadata XML: a hosted IdP entity, a remote SP entity, and Circle of Trust membership. |
|                      | `createProvisioningApp`       | Validate and persist a connector configuration, then build and persist its sync mappings.                                                        |
|                      | `runReconciliation`           | Trigger a mapping reconciliation and poll briefly for its result.                                                                                |
|                      | `deleteApplication`           | Delete an application regardless of type (OIDC, SAML, or provisioning), cascading to its linked AM or connector configuration.                   |

### Example prompts

* "List the OIDC applications in my realm"

* "Show me the configuration for this application"

* "Create an OIDC application named Customer Portal"

* "Update the redirect URI for my application"

* "Create a SAML application for Salesforce from this metadata XML"

* "What application templates are available?"

* "Is the Salesforce connector working?"

* "Connect our ServiceNow instance for provisioning"

* "Did the last reconciliation run finish?"

## AM journeys, nodes, and scripts

Manage authentication journeys, node types, and Scripted Decision Node scripts.

| Scope                    | Tool                              | Description                                                                                |
| ------------------------ | --------------------------------- | ------------------------------------------------------------------------------------------ |
| `aic:mcp:journeys.read`  | `listJourneys`                    | List all authentication journeys in a realm.                                               |
|                          | `getJourney`                      | Get a journey with node schemas and configs automatically included.                        |
|                          | `getJourneyPreviewUrl`            | Generate a preview URL to test a journey in a browser.                                     |
|                          | `exportJourney`                   | Export a journey with its nodes, inner trees, SAML entities, circles of trust, and themes. |
|                          | `listNodeTypes`                   | Discover all available authentication node types.                                          |
|                          | `getNodeTypeDetails`              | Get the schema, template, and outcomes for a node type.                                    |
|                          | `getDynamicNodeOutcomes`          | Calculate outcomes for a node based on its configuration.                                  |
|                          | `listScripts`                     | List Scripted Decision Node scripts in a realm.                                            |
|                          | `getAMScript`                     | Get an AM script with automatic base64 decoding.                                           |
|                          | `getScriptedDecisionNodeBindings` | Get available bindings and allowed imports for scripting.                                  |
| `aic:mcp:journeys.write` | `createJourney`                   | Create or replace an authentication journey atomically.                                    |
|                          | `updateJourney`                   | Update an existing journey's metadata and node graph.                                      |
|                          | `deleteJourney`                   | Delete a journey and its associated nodes.                                                 |
|                          | `setDefaultJourney`               | Set the default authentication journey for a realm.                                        |
|                          | `updateJourneyNode`               | Update a single node's configuration.                                                      |
|                          | `deleteJourneyNodes`              | Batch delete orphaned node instances.                                                      |
|                          | `createScript`                    | Create a new Scripted Decision Node script.                                                |
|                          | `updateScript`                    | Update an existing script's name, description, or content.                                 |
|                          | `deleteScript`                    | Delete an AM script.                                                                       |

### Example prompts

* "List the authentication journeys in the alpha realm"

* "Show me the node types available for authentication journeys"

* "Get the configuration for the Login journey"

* "Create a script for this authentication decision"

## AM services and identity providers

Manage AM services and social/third-party identity providers.

| Scope                    | Tool                      | Description                                                                       |
| ------------------------ | ------------------------- | --------------------------------------------------------------------------------- |
| `aic:mcp:journeys.read`  | `listAmServices`          | List AM services (configured or all/creatable types) in a realm.                  |
|                          | `getAmService`            | Retrieve the full configuration of a single AM service.                           |
|                          | `getAmServiceSchema`      | Return the JSON Schema for a configurable AM service type.                        |
|                          | `listSocialIdps`          | List configured social/third-party identity providers, or discover IdP sub-types. |
|                          | `getSocialIdp`            | Retrieve the full configuration of a single social/third-party identity provider. |
| `aic:mcp:journeys.write` | `createOrUpdateAmService` | Create or update an AM service configuration (upsert, partial payloads).          |
|                          | `deleteAmService`         | Permanently delete an AM service configuration.                                   |
|                          | `configureOidcIdp`        | Create or update a social/third-party OIDC identity provider.                     |
|                          | `deleteIdp`               | Permanently remove a social/third-party identity provider.                        |

### Example prompts

* "List the AM services configured in the alpha realm"

* "Show me the available social identity provider types"

* "Configure a Google identity provider"

* "Get the configuration for this AM service"

## CORS policies

Manage cross-origin resource sharing policies for AM.

| Scope               | Tool               | Description                                                           |
| ------------------- | ------------------ | --------------------------------------------------------------------- |
| `aic:mcp:idm.read`  | `listCorsPolicies` | List all CORS policies configured in PingOne Advanced Identity Cloud. |
|                     | `getCorsPolicy`    | Retrieve a single CORS policy by ID.                                  |
| `aic:mcp:idm.write` | `createCorsPolicy` | Create a new CORS policy.                                             |
|                     | `updateCorsPolicy` | Update an existing CORS policy (full replacement).                    |
|                     | `deleteCorsPolicy` | Permanently delete a CORS policy.                                     |

### Example prompts

* "List the CORS policies configured in my tenant"

* "Show me the CORS policy with ID policy-1"

* "Create a CORS policy for https\://example.com"

## Policy and notifications

Manage email templates, outbound email provider config, password policy, and terms and conditions.

| Scope                    | Tool                                  | Description                                                                   |
| ------------------------ | ------------------------------------- | ----------------------------------------------------------------------------- |
| `aic:mcp:idm.read`       | `listEmailTemplates`                  | List all end-user email templates.                                            |
|                          | `configureTermsAndConditions` (read)  | Read the current terms and conditions configuration.                          |
| `aic:mcp:idm.write`      | `createEmailTemplate`                 | Create a new end-user email template.                                         |
|                          | `updateEmailTemplate`                 | Update an existing email template (full replacement).                         |
|                          | `configureEmailProvider`              | Create or update the tenant outbound email provider (SMTP config, singleton). |
|                          | `configureTermsAndConditions` (write) | Add and activate a new terms and conditions version.                          |
| `aic:mcp:journeys.read`  | `getPasswordPolicy`                   | Retrieve the password policy for a managed object type.                       |
| `aic:mcp:journeys.write` | `setPasswordPolicy`                   | Update the password policy for a managed object type.                         |

### Example prompts

* "List the email templates in my tenant"

* "Update the outbound email provider configuration"

* "Show me the password policy for alpha_user"

* "Update the terms and conditions configuration"

## Reporting

Query, run, and author PingOne Advanced Identity Cloud reports. Includes out-of-the-box (OOTB) reports every tenant has, plus custom reports built through the Advanced Reporting add-on.

|   |                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Reporting tools are available in all environments, including UAT\[[1](#_footnotedef_1 "View footnote.")], staging, and production. This lets you author and run reports in upper environments even when write tools are otherwise restricted. |

| Scope                   | Tool                   | Description                                                                      |
| ----------------------- | ---------------------- | -------------------------------------------------------------------------------- |
| `aic:mcp:reports.read`  | `listReportTemplates`  | List available OOTB and custom report templates.                                 |
|                         | `getReportDefinition`  | Get a single report's parameters and fields by name.                             |
|                         | `runReport`            | Run a published report with parameters, polling briefly for completion.          |
|                         | `getReportResults`     | Fetch paginated results for a report run by jobId.                               |
|                         | `exportReport`         | Export a completed report run's results as CSV or JSON Lines.                    |
|                         | `exportReportTemplate` | Export a custom report template definition as JSON.                              |
| `aic:mcp:reports.write` | `duplicateReport`      | Copy an existing report (OOTB or custom) into a new draft.                       |
|                         | `createCustomReport`   | Author and auto-publish a custom report. Requires the Advanced Reporting add-on. |
|                         | `importReportTemplate` | Import a previously exported custom report template.                             |

### Example prompts

* "List the report templates available in my tenant"

* "Run the sign-on report for the last 30 days"

* "Show me the results for this report run"

* "Create a custom report for failed authentications"

***

[1](#_footnoteref_1). A sandbox environment is an Advanced Identity Cloud add-on capability.[2](#_footnoteref_2). A user acceptance testing (UAT) environment is an Advanced Identity Cloud add-on capability.

---

---
title: Getting Started
description: Configure a supported AI client to connect to the AIC Remote MCP Server.
component: build-with-ai
page_id: build-with-ai:aic-remote-mcp-server:getting-started
canonical_url: https://developer.pingidentity.com/build-with-ai/aic-remote-mcp-server/getting-started.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-21T00:00:00Z
keywords: ["MCP", "AI", "Advanced Identity Cloud", "PingOne Advanced Identity Cloud", "Model Context Protocol", "client configuration"]
section_ids:
  prerequisites: Prerequisites
  server-details: Server details
  configure-your-mcp-client: Configure your MCP client
  validation: Validation
  content-security-policy-csp: Content Security Policy (CSP)
---

# Getting Started

|   |                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The AIC Remote MCP Server is currently available in sandbox\[[1](#_footnotedef_1 "View footnote.")] environments only. Support for development, UAT\[[2](#_footnotedef_2 "View footnote.")], staging, and production environments is rolling out over the coming weeks. |

To enable the AIC Remote MCP Server for your PingOne Advanced Identity Cloud tenant, follow the enablement procedure in [Overview](overview.html).

Connect a supported AI client to the AIC Remote MCP Server.

## Prerequisites

Before you configure a client, make sure you have:

* A PingOne Advanced Identity Cloud tenant with the AIC Remote MCP Server enabled.

* An MCP-compatible client. This page provides step-by-step configuration for Claude Code, VS Code with GitHub Copilot, OpenAI Codex CLI, and Cursor. If your client isn't listed, use the General JSON tab below and adapt it.

## Server details

Use these values in every client configuration below:

| Field           | Value                                                                         |
| --------------- | ----------------------------------------------------------------------------- |
| Server URL      | `https://<tenant-env-fqdn>/mcp`                                               |
| OAuth client ID | `AICRemoteMCPClient` (public client, authorization code with PKCE, no secret) |

|   |                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Only the [tenant environment FQDN](https://docs.pingidentity.com/pingoneaic/tenants/environments.html#tenant-environment-fqdns) is supported as the server URL. Custom domain aliases are not supported and result in a CORS error. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some MCP clients let you specify the OAuth redirect URI instead of using a fixed value. If your client provides this option, use a loopback URI such as `http://localhost:3000`, and make sure the client listens on that address for the OAuth callback. Use the exact same URI in the `form-action` directive if your tenant enforces a [Content Security Policy (CSP)](#content-security-policy-csp). |

|   |                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Clients that support [RFC 9728 Protected Resource Metadata](https://datatracker.ietf.org/doc/html/rfc9728) discover the authorization server and required scopes automatically. Clients that don't must list them explicitly. Learn more in [Scopes](scopes.html). |

## Configure your MCP client

* Claude Code (CLI)

* VS Code

* Codex (OpenAI)

* Cursor

* General JSON

**Where to apply the configuration**

Run the MCP add command in your terminal. Claude Code auto-discovers the authorization server and required scopes.

**Configuration steps**

1. Open a terminal window.

2. Run the command to add the AIC Remote MCP Server.

3. Run `claude mcp list` to confirm that the server appears in the list.

4. On first tool use, complete the OAuth sign-on flow in the browser window that opens.

   **Example command**

   ```shell
   claude mcp add \
     --transport http \
     --client-id AICRemoteMCPClient \
     --callback-port 3000 \
     aic-mcp-server \
     https://<tenant-env-fqdn>/mcp
   ```

   **Example configuration**

   Alternatively, add an entry to `.mcp.json` (project) or `~/.claude.json`:

   ```json
   {
     "mcpServers": {
       "aic-remote-mcp": {
         "type": "http",
         "url": "https://<tenant-env-fqdn>/mcp",
         "oauth": {
           "clientId": "AICRemoteMCPClient",
           "callbackPort": 3000
         }
       }
     }
   }
   ```

   Claude Desktop uses the same JSON shape in `claude_desktop_config.json`.

   Learn more in [Claude Code MCP documentation](https://docs.anthropic.com/en/docs/claude-code/mcp).

**Where to apply the configuration**

Open the **Command Palette** and select **MCP: Open User Configuration**. Update the `mcp.json` file.

**Configuration steps**

1. Open VS Code.

2. Open the Command Palette.

3. Run **MCP: Add Server**.

4. Select **HTTP** as the transport type.

5. When prompted for the server URL, enter:

   `https://<tenant-env-fqdn>/mcp`

6. Set the Server ID or Name to your preferred name, for example, `aic-remote-mcp`.

7. Choose whether to store the configuration at the global or workspace level.

8. Open the Command Palette again and run **MCP: List Servers**.

9. If prompted for the OAuth client ID, enter `AICRemoteMCPClient`.

10. If prompted for a client secret, leave the field empty and press Enter to continue.

11. Complete the browser authentication flow when prompted. Scopes are discovered automatically.

    **Example configuration**

    ```json
    {
      "servers": {
        "aic-mcp-server": {
          "url": "https://<tenant-env-fqdn>/mcp",
          "type": "http"
        }
      }
    }
    ```

    Learn more in [Microsoft's MCP documentation](https://code.visualstudio.com/docs/copilot/customization/mcp-servers).

**Where to apply the configuration**

Run the MCP add command in your terminal. Alternatively, add the server to your Codex MCP configuration file.

|   |                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Codex might not correctly discover the scopes offered by the server and can send incorrect scopes during sign-on. Request scopes explicitly when you sign on. |

**Configuration steps**

1. Open a terminal window.

2. Run the command to add the AIC Remote MCP Server.

3. If you manage MCP servers through a config file, add the same server definition there.

4. Run `codex mcp login aic-remote-mcp --scopes aic:mcp:access,aic:mcp:identities.read` to complete the OAuth sign-on flow. Request the scopes your use case requires; this example requests the scopes needed to list managed object types. Refer to [Scopes](scopes.html) for other scope combinations.

5. If Codex does not request the correct scopes automatically, run `codex mcp login aic-remote-mcp --scopes {add MCP scopes}`. Replace `{add MCP scopes}` with a comma-separated list of the scopes your use case requires.

6. In an interactive Codex session, enter `/mcp` to list the configured MCP tools. Enter `/mcp verbose` to view more details.

   **Example command**

   ```shell
   codex mcp add aic-remote-mcp \
     --url https://<tenant-env-fqdn>/mcp \
     --oauth-client-id AICRemoteMCPClient

   codex mcp login aic-remote-mcp \
     --scopes aic:mcp:access,aic:mcp:identities.read
   ```

   **Example configuration file**

   Place the following in `~/.codex/config.toml`:

   ```toml
   [mcp_servers.aic-remote-mcp]
   url = "https://<tenant-env-fqdn>/mcp"
   auth = "oauth"

   [mcp_servers.aic-remote-mcp.oauth]
   client_id = "AICRemoteMCPClient"
   scopes = ["aic:mcp:access", "aic:mcp:identities.read"]
   ```

   Learn more in [Codex MCP documentation](https://developers.openai.com/codex/mcp/).

**Where to apply the configuration**

In Cursor, configure the server through **Settings** > **Tools & MCP**.

**Configuration steps**

1. Open Cursor.

2. Go to **Cursor Customize** > **MCPs**.

3. Click **Add New MCP Server**.

4. Edit the config file with the example below.

5. Save the file.

6. Cursor discovers scopes automatically. If you use the Cursor CLI, run `cursor-agent mcp login aic-remote-mcp` to trigger the OAuth flow.

   **Example configuration file**

   Edit `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` (workspace):

   ```json
   {
     "mcpServers": {
       "aic-remote-mcp": {
         "url": "https://<tenant-env-fqdn>/mcp",
         "auth": {
           "CLIENT_ID": "AICRemoteMCPClient"
         }
       }
     }
   }
   ```

   Learn more in [Cursor's MCP documentation](https://cursor.com/docs/mcp).

**Where to apply the configuration**

Add the server definition to your MCP client's configuration file. Refer to your client's MCP documentation for the exact file location and schema.

**Configuration steps**

1. Open your client's MCP configuration file.

2. Add the AIC Remote MCP Server using the shape below. Some clients (VS Code, for example) use `servers` as the top-level key instead of `mcpServers`.

3. For clients that don't auto-discover scopes, list the scopes your use case requires. Learn more in [Scopes](scopes.html).

4. Save the file and restart the client.

5. Complete the OAuth sign-on flow when prompted.

   **Example configuration**

   ```json
   {
     "mcpServers": {
       "aic-remote-mcp": {
         "type": "http",
         "url": "https://<tenant-env-fqdn>/mcp",
         "oauth": {
           "clientId": "AICRemoteMCPClient"
         }
       }
     }
   }
   ```

## Validation

After configuring any client:

* Confirm that the client shows the AIC Remote MCP Server as connected or available.

* Test the connection with a simple prompt, such as *"List the managed object types in my PingOne Advanced Identity Cloud tenant"*.

* Confirm that the OAuth redirect URI configured for your client is allowed by the tenant's Content Security Policy (CSP), if CSP is enforced. See [Content Security Policy (CSP)](#content-security-policy-csp).

The first tool invocation opens a browser for the OAuth sign-on flow. After you authenticate, the server returns the list of managed object types in your tenant. A successful response confirms that the MCP client is authorized and the connection is working.

|   |                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can add MCP configurations for multiple PingOne Advanced Identity Cloud tenants to the same client. Use a different server name for each tenant in the MCP client configuration. |

## Content Security Policy (CSP)

If your PingOne Advanced Identity Cloud tenant enforces a [Content Security Policy](https://docs.pingidentity.com/pingoneaic/tenants/content-security-policy.html) (CSP), the `form-action` directive must include the OAuth redirect URI used by your MCP client. Without this entry, the browser blocks the OAuth redirect and sign-on fails.

For each client you configured above, identify the redirect URI it uses for OAuth callbacks (this varies by client and by how you've configured it) and add that URI as a source under the `form-action` directive in your tenant's CSP configuration. The example below shows `http://localhost:3000` added, which is the default callback for Claude Code. Your value differs based on your MCP client and its configuration.

![Content Security Policy page in the Advanced Identity Cloud admin console with a redirect URI added to the form-action directive](_images/csp-form-action.png)

Refer to the Advanced Identity Cloud documentation on [managing Content Security Policy directives](https://docs.pingidentity.com/pingoneaic/tenants/content-security-policy.html) for step-by-step instructions.

***

[1](#_footnoteref_1). A sandbox environment is an Advanced Identity Cloud add-on capability.[2](#_footnoteref_2). A user acceptance testing (UAT) environment is an Advanced Identity Cloud add-on capability.

---

---
title: Overview
description: An overview of the AIC Remote MCP Server, a hosted HTTP-based Model Context Protocol server for administering PingOne Advanced Identity Cloud environments using natural language.
component: build-with-ai
page_id: build-with-ai:aic-remote-mcp-server:overview
canonical_url: https://developer.pingidentity.com/build-with-ai/aic-remote-mcp-server/overview.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-15T00:00:00Z
keywords: ["MCP", "AI", "Advanced Identity Cloud", "PingOne Advanced Identity Cloud", "Model Context Protocol", "remote", "HTTP"]
section_ids:
  remote-versus-local: Remote versus local
  environments-and-access: Environments and access
  use-cases: Use cases
  key-features: Key features
---

# Overview

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The AIC Remote MCP Server is an opt-in feature. Ping Identity Support must enable it per tenant before you can use it.> **Collapse: To request enablement**
>
> Open a support case and provide the following information:
>
> 1. Select **PingOne Advanced Identity Cloud** as the product family.
>
> 2. Select **Tenant Settings** as the product.
>
> 3. Select **AIC Remote MCP Server** as the affected component.
>
> 4. For **What Hostname(s) or Tenant ID(s) does this apply to?**, list every PingOne Advanced Identity Cloud tenant FQDN that should have the server enabled. For example: `https://openam-example.forgeblocks.com/`.
>
> 5. Enter `Enable AIC Remote MCP` as both the issue title and the issue description.
>
> &#xA;&#xA;If the support form asks for a product version or sub-component, select the not-applicable option.> **Collapse: Support case screenshots**
>
> ![Support case product](_images/temp-enable-remote-aic-mcp-server-sandbox-1.png)
>
> Enablement request: product and tenant details
>
> ![Support case title and issue description](_images/temp-enable-remote-aic-mcp-server-sandbox-2.png)
>
> Enablement request: issue details |

|   |                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The AIC Remote MCP Server is currently available in sandbox\[[1](#_footnotedef_1 "View footnote.")] environments only. Support for development, UAT\[[2](#_footnotedef_2 "View footnote.")], staging, and production environments is rolling out over the coming weeks. |

The AIC Remote MCP Server is an HTTP-based [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server hosted by Ping Identity that lets AI agents interact with your PingOne Advanced Identity Cloud environments over the network. Point your MCP client at a hosted endpoint, sign on with your Advanced Identity Cloud administrator account through OAuth 2.0, and issue natural-language prompts. MCP exposes Advanced Identity Cloud's REST APIs as a set of tools the AI agent can invoke.

## Remote versus local

Use the AIC Remote MCP Server for new projects. Future tooling and features are prioritized here over the local [stdio AIC MCP Server](../aic-mcp-server/overview.html).

## Environments and access

Available tools are gated by the mutability of the PingOne Advanced Identity Cloud [environment](https://docs.pingidentity.com/pingoneaic/tenants/environments.html) you connect to:

| Environment                                                                      | Available tools                                                                                                     |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Sandbox\[[1](#_footnotedef_1 "View footnote.")] and development (mutable)        | Full tool set. Read, write, and delete across every category.                                                       |
| UAT\[[2](#_footnotedef_2 "View footnote.")], staging, and production (immutable) | Read-only tools, plus the report-authoring tools (`createCustomReport`, `duplicateReport`, `importReportTemplate`). |

## Use cases

| Category                                     | Example prompts                                                                                       |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Journey and script management                | "Create a new MFA journey", "Add a scripted decision node to the registration flow"                   |
| Application and identity provider management | "Create an OIDC app called MyPortal", "Configure a Google OIDC identity provider"                     |
| Identity operations                          | "Find all users with admin in their username", "Update the email for user xyz123"                     |
| Themes and branding                          | "Create a branded theme with our corporate colors", "Set the new theme as default"                    |
| Policy and notifications                     | "Set the minimum password length to 12 for alpha users", "Configure the outbound SMTP provider"       |
| CORS and network policies                    | "Create a CORS policy allowing https\://example.com"                                                  |
| Reporting                                    | "Run the user last login report for the past 30 days", "Create a custom report showing users by city" |
| Audit and logging                            | "Show me failed login attempts in the last hour", "Find all logs for transaction abc-123"             |
| ESVs and feature management                  | "Create a new API key variable", "Enable AI Agents"                                                   |

## Key features

* **Hosted by Ping:** Ping deploys and updates the server for each tenant. You don't install or maintain anything locally.

* **Natural language interaction:** Administer PingOne Advanced Identity Cloud from whichever AI client you use daily.

* **Broad tool coverage:** Across identity, orchestration, applications, branding, policy, network, observability, and reporting. Refer to [Available Tools](available-tools.html) for the full catalog.

***

[1](#_footnoteref_1). A sandbox environment is an Advanced Identity Cloud add-on capability.[2](#_footnoteref_2). A user acceptance testing (UAT) environment is an Advanced Identity Cloud add-on capability.

---

---
title: Scopes
description: OAuth scopes required by the AIC Remote MCP Server and how to request them from each environment tier.
component: build-with-ai
page_id: build-with-ai:aic-remote-mcp-server:scopes
canonical_url: https://developer.pingidentity.com/build-with-ai/aic-remote-mcp-server/scopes.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-10-26T00:00:00Z
keywords: ["MCP", "AI", "Advanced Identity Cloud", "OAuth", "scopes", "PingOne Advanced Identity Cloud", "Model Context Protocol"]
section_ids:
  scope-reference: Scope reference
  requesting-scopes-by-environment-mutability: Requesting scopes by environment mutability
  sandbox-and-development: Sandbox and development
  uat-staging-and-production: UAT, staging, and production
---

# Scopes

|   |                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The AIC Remote MCP Server is currently available in sandbox\[[1](#_footnotedef_1 "View footnote.")] environments only. Support for development, UAT\[[2](#_footnotedef_2 "View footnote.")], staging, and production environments is rolling out over the coming weeks. |

The AIC Remote MCP Server uses OAuth 2.0 scopes to gate which tools an MCP client is permitted to invoke. Every bearer token the server accepts must include the scopes required by the tools the client wants to call.

Your MCP client requests scopes when it obtains an access token during sign-on.

* **Automatic discovery.** Clients such as Claude Code, Cursor, VS Code with GitHub Copilot, and OpenAI Codex CLI discover the required scopes from the authorization server's metadata endpoint (or from [RFC 9728 Protected Resource Metadata](https://datatracker.ietf.org/doc/html/rfc9728)). You don't need to list scopes in these clients' configuration files.

* **Explicit scope lists.** Some MCP clients require you to name the scopes you want in the client's configuration. For these clients, the server URL must also be configured as the OAuth `resource` parameter. If it's missing or doesn't match, sign-on fails.

|   |                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | While some clients' perform automatic discovery and request all scopes available, narrower scope sets limit what the server is permitted to do on your behalf. |

## Scope reference

Every request must include the mandatory `aic:mcp:access` scope in addition to the scopes required by the tools you want to call.

The `Environment` column in the following table indicates where each scope is honored:

* **Mutable:** Available in sandbox\[[1](#_footnotedef_1 "View footnote.")] and development environments only

* **All:** Available in all environments

The only write scope honored in immutable environments (UAT\[[2](#_footnotedef_2 "View footnote.")], staging, and production) is `aic:mcp:reports.write`. All other write, delete, and restart scopes are only available in mutable environments.

| Scope                      | Environment | Purpose                                                                                                                                    |
| -------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `aic:mcp:access`           | All         | **Required on every request.** Gates access to the MCP endpoint itself.                                                                    |
| `aic:mcp:identities.read`  | All         | Read managed objects (users, roles, groups, organizations, custom types) and their schemas.                                                |
| `aic:mcp:identities.write` | Mutable     | Create, update, and delete managed objects, managed object type definitions, and custom relationship properties.                           |
| `aic:mcp:journeys.read`    | All         | Read authentication journeys, nodes, scripts, AM services, social identity providers, and read the password policy.                        |
| `aic:mcp:journeys.write`   | Mutable     | Create, update, and delete authentication journeys, nodes, scripts, AM services, and identity providers, and update the password policy.   |
| `aic:mcp:apps.read`        | All         | Read OIDC applications, cross-type application lookups, application templates, and provisioning connector configuration.                   |
| `aic:mcp:apps.write`       | Mutable     | Create, update, and delete applications, including OIDC and SAML applications and provisioning applications.                               |
| `aic:mcp:themes.read`      | All         | Read theme schemas and configurations.                                                                                                     |
| `aic:mcp:themes.write`     | Mutable     | Create, update, and delete themes, and set the default theme for a realm.                                                                  |
| `aic:mcp:idm.read`         | All         | Read features, CORS policies, email templates, and terms and conditions.                                                                   |
| `aic:mcp:idm.write`        | Mutable     | Install features, and create, update, and delete CORS policies, email templates, outbound email provider config, and terms and conditions. |
| `aic:mcp:esv.read`         | All         | Read environment secrets and variables (ESVs).                                                                                             |
| `aic:mcp:esv.write`        | Mutable     | Create, update, and delete environment secrets and variables.                                                                              |
| `aic:mcp:esv.restart`      | Mutable     | Publish pending ESV changes (restarts PingOne Advanced Identity Cloud to apply variable updates).                                          |
| `aic:mcp:logs.read`        | All         | List log sources and query logs.                                                                                                           |
| `aic:mcp:agents.write`     | Mutable     | Enable AI Agents on the tenant.                                                                                                            |
| `aic:mcp:reports.read`     | All         | List, run, and export reports.                                                                                                             |
| `aic:mcp:reports.write`    | All         | Author custom reports, duplicate existing reports, and import report templates.                                                            |

For the exact list of tools each scope unlocks, refer to [Available Tools](available-tools.html).

## Requesting scopes by environment mutability

Copy the appropriate scope list into your MCP client's configuration if it doesn't auto-discover. Some clients use a JSON or TOML array of scope strings; others use a single space-separated scope string. Adapt the list to your client's format.

### Sandbox and development

```none
aic:mcp:access
aic:mcp:identities.read
aic:mcp:identities.write
aic:mcp:journeys.read
aic:mcp:journeys.write
aic:mcp:apps.read
aic:mcp:apps.write
aic:mcp:themes.read
aic:mcp:themes.write
aic:mcp:idm.read
aic:mcp:idm.write
aic:mcp:esv.read
aic:mcp:esv.write
aic:mcp:esv.restart
aic:mcp:logs.read
aic:mcp:agents.write
aic:mcp:reports.read
aic:mcp:reports.write
```

### UAT, staging, and production

```none
aic:mcp:access
aic:mcp:identities.read
aic:mcp:journeys.read
aic:mcp:apps.read
aic:mcp:themes.read
aic:mcp:idm.read
aic:mcp:esv.read
aic:mcp:logs.read
aic:mcp:reports.read
aic:mcp:reports.write
```

***

[1](#_footnoteref_1). A sandbox environment is an Advanced Identity Cloud add-on capability.[2](#_footnoteref_2). A user acceptance testing (UAT) environment is an Advanced Identity Cloud add-on capability.

---

---
title: Security, Governance, and Administrative Controls
description: Security, governance, and least-privilege controls for the AIC Remote MCP Server.
component: build-with-ai
page_id: build-with-ai:aic-remote-mcp-server:security
canonical_url: https://developer.pingidentity.com/build-with-ai/aic-remote-mcp-server/security.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-21T00:00:00Z
keywords: ["MCP", "AI", "Advanced Identity Cloud", "security", "audit", "OAuth", "PingOne Advanced Identity Cloud", "Model Context Protocol"]
section_ids:
  overview-and-general-guidance: Overview and general guidance
  security-layers: Security layers
  server-enablement-and-default-state: Server enablement and default state
  tool-exposure: Tool exposure
  execution-boundaries-and-token-isolation: Execution boundaries and token isolation
  auditability-and-siem-logging: Auditability and SIEM logging
  oauth-clients-used-by-the-server: OAuth clients used by the server
  dual-context-attribution: Dual-context attribution
  tracing-an-action-to-the-mcp-server: Tracing an action to the MCP server
---

# Security, Governance, and Administrative Controls

## Overview and general guidance

The AIC Remote MCP Server gives an AI client administrative access to your PingOne Advanced Identity Cloud environment. Tool outputs are returned to the AI client and might be included in prompts sent to a large language model (LLM) provider. Use the AIC Remote MCP Server only with trusted MCP clients, trusted AI agents, and approved AI endpoints. For general disclaimers on AI-generated output, refer to [Disclaimers and Limitations](../disclaimers.html).

* **Protect sensitive data.** Before enabling the server on an environment, evaluate the sensitivity of that environment's configuration and identity data. Tool outputs might contain configuration information, application settings, identity details, and other administrative metadata that could be transmitted to an external AI provider as part of the client workflow.

* **Request only the scopes you need.** Narrower scope sets limit what the server is permitted to do on your behalf. Learn more in [Scopes](scopes.html).

## Security layers

| Layer                        | What it does                                                                                                                                                                                                                            |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stateless JWT validation     | Bearer tokens are verified against the PingOne Advanced Identity Cloud JWKS endpoint on every request. No server-side token storage.                                                                                                    |
| OAuth 2.0 authentication     | Your MCP client authenticates users through OAuth 2.0 authorization code with PKCE. The server never handles user credentials directly.                                                                                                 |
| Scoped-down execution tokens | For each downstream API call, the server performs an RFC 8693 token exchange to obtain a token narrowed to the specific scope the tool needs. The original Bearer token is not passed to PingOne Advanced Identity Cloud APIs directly. |
| User-based authentication    | Every API call is authenticated as the user who signed on, producing audit trails attributed to that individual.                                                                                                                        |
| Tenant isolation             | Tokens are validated against the configured PingOne Advanced Identity Cloud tenant URL to prevent accidental cross-tenant operations.                                                                                                   |

Tool exposure is also gated by environment tier and by the OAuth scopes on the Bearer token. Learn more in [Tool exposure](#tool-exposure).

## Server enablement and default state

* **Disabled by default.** The AIC Remote MCP Server is turned off by default across all PingOne Advanced Identity Cloud tenants.

* **Human administrator required.** AI agents do not have access to any tools capable of enabling or disabling the AIC Remote MCP Server.

* **Content Security Policy.** If your tenant enforces a Content Security Policy, the `form-action` directive must include each MCP client's OAuth redirect URI, or sign-on fails. Learn more in [Content Security Policy (CSP)](getting-started.html#content-security-policy-csp).

## Tool exposure

* **Environment tier gates tool exposure.** When the server is enabled, tool availability is determined by the PingOne Advanced Identity Cloud environment tier. Sandbox and Development receive the full read, write, and delete tool set. UAT, Staging, and Production receive read-only tools plus the report-authoring tools.

* **Roles gate what a user can do.** The tools an AI session can invoke are further constrained by the administrative roles assigned to the authenticated user and the OAuth scopes present on the Bearer token. Learn more in [Scopes](scopes.html).

* **Production usage.** When available, enabling the server in Production exposes read-only and report-authoring tools only. Review the tool set for a tier before enabling in that tier.

  |   |                                                                                                                                                                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The AIC Remote MCP Server is currently available in sandbox\[[1](#_footnotedef_1 "View footnote.")] environments only. Support for development, UAT\[[2](#_footnotedef_2 "View footnote.")], staging, and production environments is rolling out over the coming weeks. |

## Execution boundaries and token isolation

* **Token isolation.** The OAuth access token resides exclusively within the client transport layer. It is never passed to, accessible by, or readable within the LLM prompt context.

* **Execution boundary.** The AI agent operates strictly by generating structured JSON tool calls. It cannot make arbitrary direct HTTP requests to PingOne Advanced Identity Cloud REST endpoints or alter its token permissions. If a tool does not exist or is not exposed, the agent has no technical mechanism to execute that action.

## Auditability and SIEM logging

Every action taken through the AIC Remote MCP Server is executed with a token issued to the authenticated administrator. PingOne Advanced Identity Cloud records that action in its audit logs against the individual user identity, not a service account.

### OAuth clients used by the server

The AIC Remote MCP Server uses two pre-registered OAuth 2.0 clients:

| Client ID                    | Purpose                                                                                                                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AICRemoteMCPClient`         | Public client used by the MCP client for the interactive user login (authorization code + PKCE). This is the client ID you reference in your MCP client configuration. |
| `AICRemoteMCPExchangeClient` | Confidential client used by the server itself to obtain scoped-down tokens for each tool call through RFC 8693 token exchange.                                         |

### Dual-context attribution

Every audit event produced through the AIC Remote MCP Server carries two identifiers:

* **User context:** The individual human administrator who authenticated the session.

* **Client context:** The OAuth client ID (`AICRemoteMCPClient` or `AICRemoteMCPExchangeClient`).

SIEM operations teams can filter by client ID to isolate, baseline, and monitor AI-assisted administrative activity separately from direct admin console or automation activity.

### Tracing an action to the MCP server

To determine whether a change in your tenant was made through the AIC Remote MCP Server:

1. **Identify the user.** The server attributes every action to the authenticated administrator. Query the PingOne Advanced Identity Cloud admin console for logs against that user in the relevant time window.

2. **Filter by client ID.** Filter the `am-authentication` log source for `AICRemoteMCPClient` or `AICRemoteMCPExchangeClient` to surface all MCP authentication and token-exchange events.

3. **Inspect the audit event.** Configuration changes (journeys, scripts, OIDC apps, AM services, identity providers, CORS policies) appear in AM audit logs. Identity and IDM operations (managed objects, email templates, terms and conditions, password policy) appear in IDM audit logs. The audit logs attribute all of them to the user identity.

|   |                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can use an AI client connected to the AIC Remote MCP Server itself to query MCP activity. Try prompts like *"Show me all am-authentication logs from the last hour where the client ID is AICRemoteMCPClient or AICRemoteMCPExchangeClient"* or *"Find configuration changes made in my tenant since yesterday"*. |

***

[1](#_footnoteref_1). A sandbox environment is an Advanced Identity Cloud add-on capability.[2](#_footnoteref_2). A user acceptance testing (UAT) environment is an Advanced Identity Cloud add-on capability.