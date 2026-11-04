---
title: Authentication (early access)
description: Authenticate AI clients to the PingOne Remote MCP Server using PingOne OAuth sign-on and role-based tool access control.
component: build-with-ai
page_id: build-with-ai:pingone-mcp-server:p1-authentication
canonical_url: https://developer.pingidentity.com/build-with-ai/pingone-mcp-server/p1-authentication.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-28T00:00:00Z
keywords: ["MCP", "AI", "PingOne", "Model Context Protocol", "identity orchestration"]
section_ids:
  before-you-begin: Before you begin
  how-it-works: How it works
  roles-and-access: Roles and access
---

# Authentication (early access)

The PingOne Remote Model Context Protocol (MCP) Server uses PingOne authentication to securely connect your artificial intelligence (AI) client to your PingOne environment. The first time you connect, your client opens a browser window and asks you to sign on with your PingOne credentials. After you sign on and approve access, your client can use PingOne MCP tools.

## Before you begin

Make sure you have:

* Access to the PingOne Remote MCP Server.

* The remote server URL.

* The required PingOne MCP Server system application set up.

* PingOne administrator credentials.

* An MCP-compatible client.

## How it works

1. You add the PingOne Remote MCP Server to your AI client.

2. The client opens a browser window and sends you to PingOne to sign on.

3. You sign on with your PingOne account and approve the connection.

4. The client returns to the previous window and connects to the remote MCP server.

5. You can begin using MCP tools from your client.

Reauthentication requirements depend on the [administrator security settings](https://docs.pingidentity.com/pingone/settings/p1_configure_administrator_security.html) in your environment.

## Roles and access

All MCP tools adhere to the PingOne [Roles and Permissions](https://developer.pingidentity.com/pingone-api/platform/reference/roles-and-permissions-in-pingone.html) model. Admins can only access and use tools supported by their existing permissions.

* The tools that appear in your client depend on the roles assigned to your administrator account. You must be assigned an administrator role to use PingOne tools.

  |   |                                                                                                                       |
  | - | --------------------------------------------------------------------------------------------------------------------- |
  |   | You must have the Environment Admin role or a custom role with permissions to view or edit the **MCP settings** page. |

* Assign the DaVinci Admin role to use DaVinci tools exposed through the remote MCP server.

* If your roles change, you must reconnect your MCP client to refresh the list of available tools.

* Only the Environment Admin built-in role or a custom role with the `adminMcp:update:settings` permission can enable or disable MCP server tool access against any given environment.

---

---
title: Available Tools (early access)
description: List available PingOne MCP server tools for managing environments, populations, applications, resources, users, and DaVinci flows.
component: build-with-ai
page_id: build-with-ai:pingone-mcp-server:p1-available-tools
canonical_url: https://developer.pingidentity.com/build-with-ai/pingone-mcp-server/p1-available-tools.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-10-08T00:00:00Z
keywords: ["MCP", "AI", "PingOne", "Model Context Protocol", "identity orchestration"]
section_ids:
  environments: Environments
  example-prompts: Example prompts
  populations: Populations
  example-prompts-2: Example prompts
  applications: Applications
  core-application-management: Core application management
  example-prompts-3: Example prompts
  resources: Resources
  example-prompts-4: Example prompts
  users: Users
  example-prompts-5: Example prompts
  experiences: Experiences
  provisioning: Provisioning
  audit: Audit activity
  roles: Roles
  groups: Groups
  davinci: DaVinci
  flows: Flows
  applications-2: Applications
  connectors: Connectors
  variables: Variables
  forms: Forms
  ui-templates: UI templates
  example-prompts-6: Example prompts
---

# Available Tools (early access)

Use the PingOne Remote Model Context Protocol (MCP) Server to connect your artificial intelligence (AI) client to PingOne through a PingOne-hosted remote endpoint. After you configure a supported client and sign on with PingOne OAuth 2.0, you can use MCP tools to work on PingOne administrative tasks directly from your AI client.

You don't need to install or maintain a local MCP server. PingOne hosts and manages the service, giving you a single entry point for headless administration and centrally managed updates.

The PingOne Remote MCP Server exposes available tools organized into functional categories.

You don't need to know the individual tool names. Describe what you want in natural language and your AI agent automatically selects the right tool.

| Category                      | What you can do                                                                                                                                                 |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Environments](#environments) | List, create, update environments, and manage their enabled services.                                                                                           |
| [Populations](#populations)   | Create and manage user populations.                                                                                                                             |
| [Applications](#applications) | Full CRUD for OpenID Connect (OIDC), SAML, and worker applications, plus grants, policies, attribute mappings, secrets, push credentials, and role assignments. |
| [Resources](#resources)       | Create and manage OAuth 2.0 protected resources and their scopes.                                                                                               |
| [Users](#users)               | Create, update, and manage users, including passwords, MFA, and account lockout.                                                                                |
| [Experiences](#experiences)   | Create and manage design center experiences that configure sign-on flows.                                                                                       |
| [DaVinci](#davinci)           | Work with DaVinci flows, applications, connectors, variables, forms, and execution history.                                                                     |

## Environments

List accessible environments or manage their configuration and enabled services.

The following table describes the environment tools:

| Tool                | Description                                                                                                                                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `listEnvironments`  | List PingOne environments accessible to the authenticated user.                                                                                                                                                       |
| `getEnvironment`    | Retrieve an environment's complete configuration, including its enabled services (Bill of Materials).                                                                                                                 |
| `createEnvironment` | Create a new sandbox PingOne environment for development or testing.&#xA;&#xA;Production environments cannot be created here. They must be created via the admin console.                                             |
| `updateEnvironment` | Update an environment's configuration. You can:- Rename an environment

- Promote a sandbox to production

- Change the license

- Change enabled services (Bill of Materials)&#xA;&#xA;The region cannot be changed. |

### Example prompts

* "List all my PingOne environments"

* "Create a sandbox environment called Dev Testing in the NA geography"

* "What services are enabled in my environment?"

* "Enable PingOne MFA in my sandbox environment"

## Populations

Create and manage populations to organize users within an environment.

The following table describes the population tools:

| Tool               | Description                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------- |
| `listPopulations`  | List populations in an environment.                                                            |
| `createPopulation` | Create a new population to organize users.                                                     |
| `getPopulation`    | Retrieve a population's full configuration.                                                    |
| `updatePopulation` | Update a population's configuration and assign its default identity provider.                  |
| `deletePopulation` | Permanently delete a population.&#xA;&#xA;Non-empty and default populations cannot be deleted. |

### Example prompts

* "List all populations in my environment"

* "Create a new population called External Users"

* "Update the description of the Employees population"

## Applications

Register and configure OIDC, SAML, worker, and catalog template applications. Manage their grants, authentication policies, attribute mappings, push credentials, client secrets, and role assignments.

### Core application management

The following table describes the core application tools:

| Tool                     | Description                                                                                                                                                                                                                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `listApplications`       | List applications in the environment.                                                                                                                                                                                                                                                 |
| `getApplication`         | Retrieve the full configuration of a single application along with its sub-resources:- Metadata

- Masked secret and rotation state

- Attribute mappings

- Flow policy assignments

- Grants

- Push credentials

- Role assignments

- Sign-on policy assignments                  |
| `createApplication`      | Create a new application. Automatically inject grant-type defaults. Available subtypes include:- `oidc_web_app`

- `oidc_native`

- `oidc_single_page`

- `oidc_worker`

- `oidc_device_authorization`

- `saml`

- `template_app`                                                    |
| `updateApplication`      | Update an existing application's base configuration or its sub-resources:- Attribute mappings

- Flow-policy assignments

- Sign-on-policy assignments

- Grants

- Push credentials

- Role assignments

- Secret rotation

- Metadata&#xA;&#xA;Type and protocol cannot be changed. |
| `deleteApplication`      | Permanently delete an application.&#xA;&#xA;System-managed applications (Admin Console, Portal, Self-Service) cannot be deleted.                                                                                                                                                      |
| `listApplicationCatalog` | Browse the PingOne application catalog of prebuilt integration templates, or inspect a specific template to review its requirements.                                                                                                                                                  |

### Example prompts

* "List all applications in my environment"

* "Create a single-page app called My SPA with redirect URI http\://localhost:3000/callback"

* "Create a worker application from the Salesforce template in the catalog"

* "What grants does the My API app have?"

* "Add the `openid` and `email` scopes to the My App grant for the PingOne API resource"

* "Rotate the client secret for My Worker App and keep the old one valid for 24 hours"

* "Assign the Identity Data Admin role to My Worker App for environment xyz"

## Resources

Create and manage OAuth 2.0 protected resources representing APIs that applications request access to.

The following table describes the resource tools:

| Tool             | Description                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `listResources`  | List all resources in an environment to view the protected APIs that applications request access to.                                 |
| `getResource`    | Retrieve a single resource, including its scopes, attributes, and masked client secret.                                              |
| `createResource` | Create a new custom resource representing a protected API.                                                                           |
| `updateResource` | Update a custom resource, including its scopes, attributes, and client secret.&#xA;&#xA;Built-in system resources cannot be changed. |
| `deleteResource` | Permanently delete a custom resource and its scopes.&#xA;&#xA;Built-in OpenID Connect and PingOne API resources cannot be deleted.   |

### Example prompts

* "List all resources in my environment"

* "Create a new resource called My API with audience https\://api.example.com"

* "Add read and write scopes to My API resource"

* "What scopes does the PingOne API resource have?"

## Users

Create, read, update, and manage users in an environment, including their passwords, MFA enrollment, and account status.

The following table describes the user tools:

| Tool                 | Description                                                                                                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `listUsers`          | Search for users in an environment.                                                                                                                                                                                            |
| `getUser`            | Retrieve a specific user's profile and related state:- MFA

- Password

- Roles

- Groups

- Consents

- Linked accounts

- Sessions                                                                                           |
| `createUser`         | Create a new user in an environment, with optional email verification.                                                                                                                                                         |
| `updateUser`         | Update a user's profile or relationships:- Enable or disable account

- Account lock

- Identity provider

- Population

- Admin and application roles

- Groups

- Agreement consents

- Linked external accounts

- Sessions |
| `deleteUser`         | Permanently delete a user, along with their MFA devices, sessions, and role assignments.                                                                                                                                       |
| `updateUserMfa`      | Manage a user's MFA configuration:- Enablement

- Temporary bypass

- Enrolled devices

- Device pairing keys                                                                                                                  |
| `updateUserPassword` | Manage a user's password:- Force a password change at next sign-on

- Unlock a locked-out password

- Send the user a recovery code                                                                                            |

### Example prompts

* "Find all users with @example.com email addresses"

* "Create a test user with username testuser1 in the Employees population"

* "Force a password reset for user abc\@example.com"

* "Disable MFA for user xyz\@example.com for 30 minutes"

* "Unlock the account for user abc123"

* "List users who have been locked out"

## Experiences

Create and manage design center experiences that configure the sign-on flow, first-factor settings, MFA, registration, account recovery, and theme of an environment.

The following table describes the experience tools:

| Tool               | Description                                                                                                                     |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| `listExperiences`  | List the design center experiences in an environment, or find one by its exact name.                                            |
| `getExperience`    | Retrieve the full configuration of a design center experience.                                                                  |
| `createExperience` | Create a design center experience for a username-and-password, identifier-first, or identity-provider-first sign-on flow.       |
| `updateExperience` | Update a design center experience's configuration, changing only the fields provided.&#xA;&#xA;The flow type cannot be changed. |
| `deleteExperience` | Permanently delete a design center experience.                                                                                  |

## Provisioning

The following table describes the provisioning tools:

| Tool                           | Description                                                                                                                                                                                                                                       |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `listProvisioningConnections`  | List provisioning connections (stores) in an environment to view their status and advanced action settings.                                                                                                                                       |
| `getProvisioningConnection`    | Retrieve the full configuration of a single provisioning connection, including advanced action settings:- User create, update, or disable

- Group sync

- Membership sync                                                                        |
| `updateProvisioningConnection` | Enable or disable a provisioning connection.&#xA;&#xA;Before enabling non-internal connections, a connectivity test is run. The enable is rejected if the connection is unreachable.                                                              |
| `listProvisioningRules`        | List provisioning rules in an environment to view their direction and active state.                                                                                                                                                               |
| `getProvisioningRule`          | Retrieve the full configuration of a single provisioning rule, including all attribute mappings.                                                                                                                                                  |
| `createProvisioningRule`       | Create a new provisioning rule or clone an existing one.                                                                                                                                                                                          |
| `updateProvisioningRule`       | Update a provisioning rule's configuration or active state.                                                                                                                                                                                       |
| `deleteProvisioningRule`       | Permanently and irreversibly delete a provisioning rule and all its attribute mappings.&#xA;&#xA;If another rule references this one as a parent, it cannot be deleted. Workday writeback rules must be deleted before their parent inbound rule. |
| `syncProvisioningRule`         | Trigger a sync on a provisioning rule. Available modes:- Full: Replicates all users from source to target.

- Partial: Applies only changes since the last poll.                                                                                  |

## Audit activity

The following table describes the audit activity tools:

| Tool                    | Description                                                                                                                                                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `searchAuditActivities` | Search audit events for a PingOne environment to:- Investigate activity history

- Trace actor actions

- Identify what changed on a resource

- Review compliance events&#xA;&#xA;Without a time range, it returns only the last 24 hours. |
| `getAuditActivity`      | Retrieve the complete detail of a single audit event by ID.                                                                                                                                                                                 |

## Roles

The following table describes the role tools:

| Tool        | Description                                                                   |
| ----------- | ----------------------------------------------------------------------------- |
| `listRoles` | List the predefined (built-in) admin roles available for assignment.          |
| `getRole`   | Review the privileges granted by a specific predefined (built-in) admin role. |

## Groups

The following table describes the group tools:

| Tool          | Description                                                                                                 |
| ------------- | ----------------------------------------------------------------------------------------------------------- |
| `listGroups`  | List groups in an environment by name, population, or external ID.                                          |
| `getGroup`    | Retrieve a group's full configuration, including:- Members

- Total member count

- Role assignments        |
| `createGroup` | Create a new group in an environment, optionally scoped to a population.                                    |
| `updateGroup` | Update a group's settings, including:- Direct memberships

- Nested-group relationships

- Role assignments |
| `deleteGroup` | Permanently delete a group.                                                                                 |

## DaVinci

Manage DaVinci flows, applications, connectors, variables, forms, and execution history.

|   |                                                                                            |
| - | ------------------------------------------------------------------------------------------ |
|   | DaVinci tools are only available when your environment has the DaVinci capability enabled. |

### Flows

The following table describes the DaVinci flow tools:

| Tool                        | Description                                                                                                                                                                                                       |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `createDavinciFlow`         | Create, clone, or import a DaVinci flow.                                                                                                                                                                          |
| `listDavinciFlows`          | List available DaVinci flows.                                                                                                                                                                                     |
| `getDavinciFlow`            | Retrieve the complete definition of a DaVinci flow, including its full node graph and settings. Run the DVLinter engine to view errors and warnings, list saved versions, or export specific historical versions. |
| `listDavinciFlowExecutions` | List past executions of a DaVinci flow.                                                                                                                                                                           |
| `getDavinciFlowExecution`   | Retrieve the event log of a single flow execution to debug failures, verify data transformations, or investigate user-specific issues.                                                                            |
| `updateDavinciFlow`         | Manage a DaVinci flow to:- Replace the flow definition

- Enable or disable the flow

- Deploy the flow to production

- Assign an alias to a flow version

- Revert the flow to a specific saved version         |
| `deleteDavinciFlow`         | Permanently delete a DaVinci flow or a specific flow version.                                                                                                                                                     |

### Applications

The following table describes the DaVinci application tools:

| Tool                       | Description                                                                                                                                        |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `listDavinciApplications`  | List DaVinci applications.                                                                                                                         |
| `getDavinciApplication`    | Retrieve the full configuration of a single DaVinci application or flow policy.                                                                    |
| `createDavinciApplication` | Create a new DaVinci application.                                                                                                                  |
| `updateDavinciApplication` | Update an existing DaVinci application to:- Modify OAuth and API-key configurations

- Rotate its API key or secret

- Add or update a flow policy |
| `deleteDavinciApplication` | Permanently delete a DaVinci application or detach a specific flow policy from it.                                                                 |

### Connectors

The following table describes the DaVinci connector tools:

| Tool                                   | Description                                                                                                                  |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `listDavinciConnectors`                | Discover available DaVinci connector types and deployed instances.                                                           |
| `getDavinciConnector`                  | Retrieve full details for a specific DaVinci connector type or instance.                                                     |
| `createDavinciConnector`               | Create a new DaVinci connector instance, either from scratch or by cloning an existing instance.                             |
| `updateDavinciConnector`               | Update the mutable fields of an existing DaVinci connector instance.                                                         |
| `deleteDavinciConnector`               | Permanently delete a DaVinci connector instance.&#xA;&#xA;Deletion is blocked if any flow references the connector instance. |
| `getDavinciConnectorCapabilityOptions` | View the available option values for a connector instance's capability fields.                                               |

### Variables

The following table describes the DaVinci variable tools:

| Tool                    | Description                                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------------------- |
| `listDavinciVariables`  | List DaVinci variables with their data types and context.                                                     |
| `getDavinciVariable`    | Retrieve the full configuration of a single DaVinci variable, including its context, type, and default value. |
| `createDavinciVariable` | Create a new DaVinci variable.                                                                                |
| `updateDavinciVariable` | Update the mutable fields of an existing DaVinci variable.                                                    |
| `deleteDavinciVariable` | Permanently delete a DaVinci variable.&#xA;&#xA;Deletion is blocked if any flow references the variable.      |

### Forms

The following table describes the DaVinci form tools:

| Tool                | Description                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------- |
| `listDavinciForms`  | List DaVinci forms.                                                                           |
| `getDavinciForm`    | Retrieve the full configuration of a single DaVinci form, including all fields and layout.    |
| `createDavinciForm` | Create a new DaVinci form for sign-on, registration, password reset, or other identity forms. |
| `updateDavinciForm` | Update an existing DaVinci form's fields and layout.                                          |
| `deleteDavinciForm` | Permanently delete a DaVinci form.                                                            |

### UI templates

The following table describes the DaVinci UI template tools:

| Tool                      | Description                                                                                                                   |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `listDavinciUiTemplates`  | List DaVinci UI templates for the environment.                                                                                |
| `getDavinciUiTemplate`    | Retrieve the full configuration of a DaVinci UI template.                                                                     |
| `createDavinciUiTemplate` | Create a new DaVinci UI template for login, registration, or other identity experiences.                                      |
| `updateDavinciUiTemplate` | Update an existing DaVinci UI template.                                                                                       |
| `deleteDavinciUiTemplate` | Permanently delete a DaVinci UI template.&#xA;&#xA;Unless forced, deletion is blocked if the template is referenced by flows. |

### Example prompts

* "List all DaVinci flows"

* "Show me the last 10 executions of the Registration flow"

* "What happened during execution xyz-456?"

* "List all DaVinci connector instances in my environment"

* "Create a new DaVinci variable called sessionTimeout with value 3600"

* "Show me all DaVinci forms"

---

---
title: Client Configuration (early access)
description: Configure AI clients such as VS Code, Cursor, and Codex CLI to connect to the PingOne Remote MCP Server.
component: build-with-ai
page_id: build-with-ai:pingone-mcp-server:p1-client-configuration
canonical_url: https://developer.pingidentity.com/build-with-ai/pingone-mcp-server/p1-client-configuration.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-10-13T00:00:00Z
keywords: ["MCP", "AI", "PingOne", "Model Context Protocol", "identity orchestration"]
section_ids:
  before-you-begin: Before you begin
  understanding-cross-environment-permissions-and-mcp-server-opt-in: Understanding cross-environment permissions and MCP server opt-in
  global-configuration-details: Global configuration details
  steps: Steps
  validation: Validation
---

# Client Configuration (early access)

Connect supported artificial intelligence (AI) clients to the PingOne Remote MCP Server.

## Before you begin

Make sure you have:

* An administrator role assigned in a PingOne environment.

  |   |                                                                                                                                                                                                            |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | To allow or disallow MCP tool calls against a specific environment, an administrator with the `adminMcp:update:settings` permission (Environment Admin role only or a custom role) must enable the server. |

* The remote server configuration URL obtained from the **MCP Server** page in the **Settings** section of the PingOne admin console or **Overview** tab of the MCP Server system application.

### Understanding cross-environment permissions and MCP server opt-in

To successfully authorize MCP clients, you must understand the cross-environment permissions model in PingOne. Learn more in [Sharing MCP Server URLs (early access)](p1-sharing-mcp-configuration.html).

PingOne Remote MCP Server access is managed on a per-environment basis. To operate against an environment using an MCP client, you must opt in and enable the MCP server for that specific environment.

* Administrators environment opt-in

  In most cases, administrators must first opt in to the remote MCP server within the designated administrator environment for their organization.

  Opting in at the administrator environment level creates the backend **PingOne MCP Server Platform** system application. It does not enable MCP execution on the administrator environment itself.

  Learn more about the administrator environment in [Administrators environment](https://docs.pingidentity.com/pingone/introduction_to_pingone/p1_introduction.html#administrators-environment) in the PingOne admin documentation.

* Target environment opt-in

  You must opt in and enable the MCP server in every target environment you want to operate against using an MCP client.

* Single-environment setup

  If your administrator identity resides directly in the MCP target environment (rather than in a separate administrators environment), you only need to opt in and enable it in your target environment. You don't need to enable it in your administrator environment.

Learn more about enabling the PingOne Remote MCP Server in your environments in [PingOne Remote MCP Server (early access)](https://docs.pingidentity.com/pingone/early-access-features/ea-p1_mcp_server_settings_app.html) in the PingOne administrator documentation.

### Global configuration details

* Universal MCP client ID: `pingone-mcp-server`

* Default redirect URIs: `http://127.0.0.1/` for all supported clients and `cursor://anysphere.cursor-mcp/oauth/callback` for Cursor

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | During the OAuth 2.0 sign-on flow, PingOne forwards the response to a redirect URI registered on the PingOne MCP Server platform application. If your MCP client uses a different redirect URI, such as a custom callback port or host name, you can add custom redirect URIs to the platform application in the PingOne admin console. Learn more in [Configuring custom redirect URIs](https://docs.pingidentity.com/pingone/early-access-features/ea-p1_mcp_server_settings_app.html#configuring-custom-redirect-uris). |

* Base URL format: https\://mcp.pingone.region/admin/envId/mcp

  | Geography     | Geographical domain | Example MCP server URL                      |
  | ------------- | ------------------- | ------------------------------------------- |
  | North America | .com                | https\://mcp.pingone.com/admin/envId/mcp    |
  | Europe        | .eu                 | https\://mcp.pingone.eu/admin/envId/mcp     |
  | Canada        | .ca                 | https\://mcp.pingone.ca/admin/envId/mcp     |
  | Asia-Pacific  | .com.au             | https\://mcp.pingone.com.au/admin/envId/mcp |
  | Singapore     | .sg                 | https\://mcp.pingone.sg/admin/envId/mcp     |

|   |                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For the Asia-Pacific geography, new organizations are registered under the pingone.com.au domain. While Ping Identity also supports existing organizations registered under the pingone.asia domain, .asia domains aren't supported for MCP use. Both domains provide Australia-only data residency. |

## Steps

Configure your AI client using the following instructions.

* Claude Code (CLI)

* VS Code

* OpenAI Codex CLI

* Cursor

* General JSON

**Where to apply the configuration**

Run the MCP add command in your terminal.

**Configuration steps**

1. Open a terminal window.

2. Run the MCP add command to add the PingOne Remote MCP Server.

3. Run `mcp list` or `claude mcp list` (if you haven't invoked Claude) to confirm that the server appears in the list.

4. On first use, complete the OAuth 2.0 sign-on flow in the browser window that opens.

   **Example configuration**

   The name of the server in the following example is user-provided and varies based on your preference. The server name is used to reference the server in future commands.

   ```shell
   claude mcp add \
     --transport http \
     --client-id pingone-mcp-server \
     --callback-port 7474 \
     pingone-remote \
     https://mcp.pingone.region/admin/envId/mcp
   ```

**Where to apply the configuration**

Open the **Command Palette** and select **MCP: Open User Configuration**. Update the `mcp.json` file.

**Configuration steps**

1. Open VS Code.

2. Open the **Command Palette**.

3. Run **MCP: Add Server**.

4. Select **HTTP** as the transport type.

5. When prompted for the server URL, enter https\://mcp.pingone.region/admin/envId/mcp

6. Set the **Server ID/Name** to your preferred name, for example: `pingone-remote`

7. Choose whether to store the configuration at the global or workspace level.

   Result

   A pop-up window opens to prompt you to allow the authentication to auth.pingone.com.

8. Click **Allow** to continue.

9. Open the **Command Palette** again and run **MCP: List Server**.

10. If you clicked **Cancel** on the pop-up window to allow the authentication to auth.pingone.com, the window appears again. Click **Allow** to continue.

11. Select **pingone-remote** and choose **Start Server**.

12. When prompted for authentication details or to bypass dynamic registration, enter `pingone-mcp-server` as the client ID and complete the browser authentication flow.

    **Example configuration**

    ```json
    {
      "servers": {
        "pingone-remote-test": {
          "url": "https://mcp.pingone.com/admin/envId/mcp",
          "type": "http"
        },
          "inputs": []
      }
    }
    ```

**Where to apply the configuration**

Run the MCP add command in your terminal. Alternatively, add the server to your Codex MCP configuration file.

**Configuration steps**

1. Open a terminal window.

2. Run the MCP add command to add the PingOne Remote MCP Server.

3. If you manage MCP servers through a config file, add the same server definition to the config file.

4. Complete the OAuth 2.0 sign-on flow if prompted.

   **Example command**

   ```shell
   codex mcp add
   --url "https://mcp.pingone.region/admin/envId/mcp"
   --oauth-client-id "pingone-mcp-server"
   codex mcp login
   ```

   **Example configuration file**

   Place the following in `~/.codex/config.toml`:

   ```toml
   [mcp_servers.pingone-mcp-prod]
   url = "https://mcp.pingone.region/admin/envId/mcp"

   [mcp_servers.pingone-mcp-prod.oauth]
   client_id = "pingone-mcp-server"
   ```

**Where to apply the configuration**

In Cursor, configure the server from **Settings > Tools & MCP**.

**Configuration steps**

1. Open Cursor.

2. Go to **Cursor Customize > MCPs**.

3. Click **Add New MCP Server**.

4. Edit the config file using the following example.

   **Example configuration file**

   You can also configure Cursor by editing `~/.cursor/mcp.json`:

   ```json
   {
       "mcpServers": {
         "pingone": {
           "url": "https://mcp.pingone.com/admin/envId/mcp",
           "transport": "http",
           "auth": {
             "CLIENT_ID": "pingone-mcp-server"
           }
         }
       }
     }
   ```

**Where to apply the configuration**

Add the server definition to your MCP client's configuration file. Refer to your client's MCP documentation for the exact file location and schema.

**Configuration steps**

1. Open your client's MCP configuration file.

2. Add the PingOne Remote MCP Server using the shape below. Some clients (VS Code, for example) use `servers` as the top-level key instead of `mcpServers`.

3. If your client doesn't auto-discover the authorization server, set the OAuth client ID to `pingone-mcp-server`.

4. Save the file and restart the client.

5. Complete the OAuth 2.0 sign-on flow when prompted.

   **Example configuration**

   ```json
   {
     "mcpServers": {
       "pingone-remote": {
         "type": "http",
         "url": "https://mcp.pingone.com/admin/envId/mcp",
         "oauth": {
           "clientId": "pingone-mcp-server"
         }
       }
     }
   }
   ```

## Validation

After configuring any client:

* Confirm that the client shows the PingOne Remote MCP Server as connected or available.

* Test the connection with a simple prompt, such as `List my PingOne environments`.

* Confirm the default `redirect_uri` for all supported clients is `http://127.0.0.1/`. For Cursor, the default `redirect_uri` is `cursor://anysphere.cursor-mcp/oauth/callback`. If your client uses a different `redirect_uri`, you must add it as a custom redirect URI to the PingOne MCP Server platform application. Learn more in [Configuring custom redirect URIs](https://docs.pingidentity.com/pingone/early-access-features/ea-p1_mcp_server_settings_app.html).

A successful response confirms that the MCP client is authorized and the connection is working.

If the PingOne Remote MCP Server doesn't appear or doesn't respond after configuration, make sure any existing local MCP servers named "PingOne" or "DaVinci" are disabled in the same directory to avoid conflicts.

|   |                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must reauthenticate your MCP client based on the [administrator security settings](https://docs.pingidentity.com/pingone/settings/p1_configure_administrator_security.html). |

---

---
title: PingOne Remote MCP Server Overview (early access)
description: Connect AI clients to PingOne through the hosted PingOne Remote MCP Server to administer environments, applications, and users.
component: build-with-ai
page_id: build-with-ai:pingone-mcp-server:p1-overview
canonical_url: https://developer.pingidentity.com/build-with-ai/pingone-mcp-server/p1-overview.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-21T00:00:00Z
keywords: ["MCP", "AI", "PingOne", "Model Context Protocol", "identity orchestration"]
section_ids:
  what-you-can-do: What you can do
  example-prompts: Example prompts
  key-features: Key features
  special-considerations: Special considerations
---

# PingOne Remote MCP Server Overview (early access)

The PingOne Remote MCP Server is a PingOne-hosted service that lets artificial intelligence (AI) clients connect to PingOne through a single remote Model Context Protocol (MCP) endpoint. The PingOne Remote MCP Server doesn't require you to install or run a local MCP server yourself.

|   |                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne Remote MCP Server is currently an Early Access feature. Learn more about how to enable early access features in [PingOne Early Access](https://docs.pingidentity.com/pingone/early-access-features/p1_early_access_features.html) in the PingOne administrator documentation. |

After you configure a supported client, you authenticate through PingOne with OAuth 2.0 and can securely use MCP tools to administer PingOne.

## What you can do

The PingOne Remote MCP Server uses a dedicated PingOne MCP Server platform application. This centralizes configuration and ensures a consistent connection model across supported MCP clients.

* Connect supported AI clients, such as Claude Desktop, VS Code, Cursor, and OpenAI Codex CLI, to PingOne through a single remote server endpoint.

* Sign on securely through PingOne using OAuth 2.0 instead of managing local server credentials on each machine.

* Use MCP tools to work with PingOne administrative capabilities from your AI client, rather than depending only on the UI.

## Example prompts

| Category                                           | Example prompts                                                                                                             |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Find applications                                  | "List the applications in my PingOne environment" — review existing application configuration before making changes.        |
| Create an application                              | "Create a new OIDC web application named Customer Portal" — add a new PingOne application through MCP tools.                |
| Update an application                              | "Update my application to add a new redirect URI" — change application settings without manually editing them in the UI.    |
| Manage users                                       | "Find user jamie\@example.com and update their mobile number" — look up a user and change profile attributes.               |
| Password or multi-factor authentication (MFA) help | "Enable MFA for this user" — complete common user security and access tasks.                                                |
| Investigate audit logs                             | "Investigate audit logs for suspicious activity" — jamie\@example.com had trouble signing on this afternoon. What happened? |

## Key features

* Hosted, centrally managed, and automatically updated by PingOne, so you don't need to install or run a local MCP server.

* Access to standards-based MCP tools for PingOne administrative tasks.

* Differentiated audit trail for human administrators versus MCP client actions.

* Requires authentication using an [PingOne Administrators Security Policy](https://docs.pingidentity.com/pingone/settings/p1_configure_administrator_security.html) for secure access.

* Supports headless administration through a unified entry point across supported PingOne services.

## Special considerations

Consider the following when using the PingOne Remote MCP Server to manage DaVinci flows.

* [DaVinci tools](p1-available-tools.html#davinci) are only available when your environment has the DaVinci capability enabled.

* **Flow size**: `createDaVinciFlow`/`updateDaVinciFlow` tools aren't optimized for creating or modifying flows larger than 50 KB.

* **Flow JSON generation**: The DaVinci tools don't generate flow JSON. They expect a valid DaVinci flow JSON payload to already be available. Use a skill to generate the flow JSON before invoking these tools.

* **Recommended approach**: For larger or more complex flows, use [Ping CLI](https://developer.pingidentity.com/build-with-ai/pingcli/overview.html) together with a skill that generates the flow JSON for more reliable flow creation and modification.

---

---
title: Security, Governance, and Administrative Controls (early access)
description: Apply security, governance, and least-privilege controls when connecting the PingOne Remote MCP Server to AI clients and agents.
component: build-with-ai
page_id: build-with-ai:pingone-mcp-server:p1-security
canonical_url: https://developer.pingidentity.com/build-with-ai/pingone-mcp-server/p1-security.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-21T00:00:00Z
keywords: ["MCP", "AI", "PingOne", "Model Context Protocol", "identity orchestration"]
section_ids:
  server-enablement-and-default-state: Server enablement and default state
  tool-exposure-and-production-usage-policy: Tool exposure and production usage policy
  execution-boundaries-and-token-isolation: Execution boundaries and token isolation
  auditability-and-siem-logging: Auditability and SIEM logging
---

# Security, Governance, and Administrative Controls (early access)

The PingOne Remote MCP Server gives an artificial intelligence (AI) client access to information and actions within your PingOne environment. Tool outputs are returned to your AI client and might be included in prompts sent to a large language model (LLM) provider. As a result, use the remote MCP server only with trusted MCP clients, trusted AI agents, and approved AI endpoints. For general disclaimers on AI-generated output, refer to [Disclaimers and Limitations](../disclaimers.html).

* **Use Trusted Clients and Agents:** Only connect the PingOne Remote MCP Server to MCP clients and AI agents that your organization explicitly trusts. Any data returned by MCP tools can be exposed to the underlying AI system, including configuration details and environment metadata.

* **Protect Sensitive Data:** Before enabling the remote MCP server in a given environment, evaluate the sensitivity of that environment's data. Tool outputs might contain configuration information, application settings, identity details, and other administrative metadata that could be transmitted to an external AI provider as part of the client workflow.

## Server enablement and default state

* **Disabled by Default:** The PingOne Remote MCP Server is turned off by default across all environments.

* **Environment-Level Scope:** Enablement is explicitly controlled on a per-environment basis within the PingOne admin console or using the PingOne Management APIs.

* **Human Administrator Required:** AI agents don't have access to any MCP tools capable of modifying MCP server settings or administrative permissions. Enabling or disabling the MCP server requires a human administrator operating directly in the PingOne admin console or using the management APIs.

## Tool exposure and production usage policy

* **Environment Tool Exposure:** When the MCP server is enabled for an environment, all supported read, write, and delete tools for that environment become active. The tools available to an AI session are strictly constrained by the administrative roles assigned to the authenticated user account (for example, Environment Admin, DaVinci Admin).

* **Production Recommendation:** Because enabling the server exposes all available read, write, and delete tools for that environment, use of the PingOne Remote MCP Server against production environments is currently not recommended.

* **Granular Tool Controls:** Granular tool controls will be available in a future release.

## Execution boundaries and token isolation

* **Token Isolation:** The OAuth 2.0 access token resides exclusively within the client transport layer. It is never passed to, accessible by, or readable within the LLM prompt context.

* **Execution Boundary:** The AI agent operates strictly by generating structured JSON tool calls. It can't make arbitrary direct HTTP requests to PingOne REST endpoints or alter its token permissions. If a tool doesn't exist or isn't exposed, the agent has no technical mechanism to execute that action.

## Auditability and SIEM logging

* **Auditability:** All write and sensitive (read: secret) operations executed through the MCP server are recorded in the PingOne audit event stream with dual-context attribution:

  * User Context (`user_id`): The individual human administrator who authenticated the session.

  * Client Context (`client_id`): The dedicated platform client ID (`pingone-mcp-server`).

* **SIEM Logging:** Security information and event management (SIEM) operations teams can filter SIEM logs by `client_id == pingone-mcp-server` to isolate, baseline, and monitor all AI-assisted administrative activity across tenants.

---

---
title: Sharing MCP Server URLs (early access)
description: Share the PingOne Remote MCP Server configuration URL across environments and administrators using the home environment ID.
component: build-with-ai
page_id: build-with-ai:pingone-mcp-server:p1-sharing-mcp-configuration
canonical_url: https://developer.pingidentity.com/build-with-ai/pingone-mcp-server/p1-sharing-mcp-configuration.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-21T00:00:00Z
keywords: ["MCP", "AI", "PingOne", "Model Context Protocol", "identity orchestration", "cross-environment administration"]
section_ids:
  before-you-begin: Before you begin
  mcp-server-url-structure: MCP server URL structure
  cross-environment-url-sharing: Cross-environment URL sharing
  default-behavior: Default behavior
  sharing-across-environments: Sharing across environments
---

# Sharing MCP Server URLs (early access)

PingOne uses a cross-environment administration model, which lets administrators manage environments other than their own home environment.

## Before you begin

To view and copy the MCP server configuration URL in the PingOne admin console, your administrator role must include the `adminMcp:read:settings` permission.

## MCP server URL structure

The MCP server URL uses the following format:

```none
https://mcp.pingone.region/admin/envId/mcp
```

## Cross-environment URL sharing

|   |                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------- |
|   | The `/envId` path parameter must be the home environment ID of the administrator who authenticates the request to the MCP server. |

### Default behavior

When you view the URL in the PingOne admin console, PingOne automatically populates `/envId` with your own home environment ID. Learn more about home environments in [Best Practices for Managing PingOne Admin Users](https://support.pingidentity.com/s/article/Best-Practices-for-Managing-PingOne-Admin-Users) in the Ping Identity Support knowledgebase.

### Sharing across environments

If you share this URL with an administrator whose identity resides in a different home environment, they must replace `/envId` with their own home environment ID before they connect their MCP client. Otherwise, their MCP client can't authenticate successfully to the PingOne Remote MCP Server.