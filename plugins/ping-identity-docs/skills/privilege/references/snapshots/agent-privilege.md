---
title: Agent registry
description: Add an agent in Agent Registry to register it with Agent Privilege and choose how it authenticates.
component: privilege
page_id: privilege:agent-privilege:configuration/agent-registry
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/configuration/agent-registry.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 10, 2026
section_ids:
  registering-an-agent: Registering an agent
  before-you-begin: Before you begin
  step-1-configure-agent-identity-and-access: "Step 1: Configure agent identity and access"
  step-2-configure-ai-gateway-and-apps: "Step 2: Configure AI gateway and apps"
  option-1-configuring-models-for-llm-access: "Option 1: Configuring models for LLM access"
  option-2-configuring-tools-for-mcp-access: "Option 2: Configuring tools for MCP access"
  option-3-configuring-agents-for-a2a-access: "Option 3: Configuring agents for A2A access"
  step-3-configuring-ai-guard: "Step 3: Configuring AI guard"
  step-4-establish-connectivity-between-agent-and-gateway: "Step 4: Establish connectivity between agent and gateway"
  result: Result:
  result-2: Result:
  result-3: Result
---

# Agent registry

Agent registry is where each agent becomes a first-class identity with an owner, an authentication method, and a lifecycle. Registration is what every other control hangs on. Unregistered or revoked agents are denied, and registered ones get policy, attribution, and lifecycle control. At the AI Gateway, the registered agent's identity is validated on every call with a comprehensive, attributable audit trail.

## Registering an agent

Administrators can register an agent on the **Agent Registry** page. During configuration, you define what the agent acts on behalf of, when its access expires, how it authenticates, and what it may reach. The wizard steps through agent details, access configuration, runtime protection, and review.

### Before you begin

Ensure the following:

* If you're configuring tools for MCP access, you have configured one or more [MCP server](agentic-apps/mcp-server.html) applications that the agent will access.

* If you're configuring tools for A2A access, you have one or more configured [remote agent](agentic-apps/remote-agent.html) applications that the agent will access.

### Step 1: Configure agent identity and access

1. In the PingOne Privilege admin console, go to **AI Security > Agent Registry**.

2. Click **Add Agent**.

3. In the **Agent Details** section, configure:

   * **Agent Name**: A name for the agent, shown in audit logs.

   * **Custodian**: Select one of the following:

     * **User**: Actions performed by the agent are attributed to the user selected from this list.

     * **Non-human identity**: The key associated with this registered NHI acts as this identity and inherits its policy.

   * **Expires**: When the agent's access expires, such as in 30 days. Short-lived keys reduce blast radius; you can revoke keys instantly at any time.

4. Define how the agent will authenticate with the AI gateway:

   * **API Key**: PingOne Privilege generates a virtual API key at creation. The real API key is never exposed to the user or agent. You can copy it after the agent is created in **AI Security > Agent Registry** by clicking the **More options ([icon: ellipsis-v, set=fa])** icon on the created agent.

   * **Workload Identity**: The agent presents its own platform token:

     * Kubernetes service-account tokens.

     * Docker Host - Self-Signed Token

     * GitHub Actions and GitLab CI/CD job tokens.

     * SPIFFE JWT-SVIDs.

     * Any OIDC issuer with published keys.

5. For **Access Scopes**, define what the agent may reach through the AI gateway:

   ![The Access Scopes section of agent registry, showing the checkboxes for llms, mcps, and a2a scopes.](../_images/p1p_epaa_access_scopes.png)

   * **Models**: LLM providers the agent can call through AI Gateway.

   * **Tools**: MCP servers the agent can reach through MCP Gateway, with capability-level policy on the tools, prompts, and resources it may use.

   * **Agents**: Peer agents the agent can communicate with over A2A connections.

6. Click **Continue**.

### Step 2: Configure AI gateway and apps

In this step, the configuration depends on agent type:

* [LLM](#models): Allows the agent to reach specific LLM providers through the gateway with a virtual API key, enforcing model controls, spend limits, with complete usage accounting.

* [MCP](#tools): Allows the agent to reach specific tools for the associated **MCP Server**.

* [A2A](#agents): Allows the agent to communicate with **Remote Agent** peer applications over agent-to-agent (A2A) connections.

#### Option 1: Configuring models for LLM access[]()

If you selected **LLM** as your **Access Scope** in the previous step, configure the following fields:

1. Select a **Provider** for your agent.

2. Enter the **Real Provider Key**.

   PingOne Privilege stores this key encrypted, injects it only inside the gateway, and never exposes it to the agent.

3. Configure model access and limits:

   * **Allowed models**: Restrict which models the agent may call. If you don't select any models, the agent can call all the provider's models.

   * **Rate limit - RPM**: Cap requests per minute (RPM).

   * **Rate limit - TPM**: Cap tokens per minute (TPM).

   * **Budget Period**: Set the period the budgets apply to, such as monthly.

   * **Budget - USD**: Cap spending in United States dollars (USD). Zero means unlimited.

   * **Budget - Tokens**: Cap spending in tokens. Zero means unlimited.

4. Click **Continue** to proceed to the next step.

The agent now authenticates to the selected providers with the virtual API key issued by PingOne Privilege, and its calls are subject to the model policy and spend limits enforced by the LLM Gateway.

#### Option 2: Configuring tools for MCP access[]()

If you selected **MCP** as your **Access Scope** in the previous step, configure the following fields:

1. Select one or more **MCP Servers** to access through this agent.

2. Click **Configure Tools**.

3. In the **MCP Server** list, select the MCP server you are configuring.

4. Click **Select Tools** to select tools or click **Match by pattern** to search by RegEx.

5. Click **Continue** to proceed to the next step.

The agent now reaches the selected MCP servers through the AI Gateway. Credentials and tokens terminate at the AI Gateway, are injected at request time, and are never forwarded downstream. Tool calls are logged in **Activity > Activity Logs**.

#### Option 3: Configuring agents for A2A access[]()

If you selected **A2A** as your **Access Scope** in the previous step, configure the following fields:

1. Select the **Remote Agents** to access through this agent.

2. Click **Continue** to proceed to the next step.

### Step 3: Configuring AI guard

AI Guard inspects the traffic between AI agents and the services they reach, whether that traffic is LLM, MCP, or A2A.

1. In the **AI Guard** section of the setup wizard, configure the following toggles:

   * **Enable AI Guard**: Enabled by default for AI guard protection. To disable it, click the toggle to the left (gray).

   * **Fail Closed**: To enable blocking traffic if the guard errors, click the toggle to the right (blue).

2. Under **Detector Policies**, you can review the policies for each detector category by clicking **View Details** in its tile.

3. For each detector tile, you can adjust the detection thresholds with the following rules:

   * **Alert**: Logs a warning.

   * **Sanitize**: Where available, redacts matching content and forwards.

   * **Block**: Stops the request.

     |   |                                                                                    |
     | - | ---------------------------------------------------------------------------------- |
     |   | The **Alert** configuration must always be lower than the **Block** configuration. |

4. You can adjust the following detector categories and parameters:

   * **Content & Prompt Safety**: Protect the model from manipulation and poisoned context. Click the gear icon to adjust the thresholds for this category:

     * **Prompt Injection**

     * **Jailbreak**

     * **Hidden Instructions**

     * **Memory Poisoning**

   * **Data Protection**: Protect the model from manipulation and poisoned context. Click the gear icon to adjust the thresholds for this category:

     * **PII**

     * **Data Exfiltration**

   * **Tool & Agent Safety**: Protect the model from manipulation and poisoned context. Click the gear icon to adjust the thresholds for this category:

     * **Tool Abuse**

     * **Tool Poisoning**

     * **Schema Violation**

     * **Inter-Agent Abuse**

   * **Content Safety**: Protect the model from manipulation and poisoned context. Click the gear icon to adjust the thresholds for this category:

     * **Malicious Content**

   * **External Inspection**: Send eligible content to an independently managed evaluator. Enable a detector in this category to configure its thresholds:

     * **External Guardrail**

   * **Advanced - ML Sidecar**: Configure the external evaluator endpoint and fail-safe behavior. Enable an External Guardrail detector in **External Inspection** to configure its fields:

     * **ML Sidecar URL**: Required when External Guardrail detector is enabled.

     * **Sidecar Timeout (ms)**: Per-call timeout. Default is `1000 (ms)`.

     * **Auth Header**: Sent with every sidecar, formatted as `Name: value`. Leave blank for no header.

     * **Block Agreement**: Controls how the ML sidecar verdict is merged with the deterministic detector layer. The following options are available in the list:

       * `off`: ML blocks alone so that no deterministic agreement needed.

       * `unit`: ML block honored only if a deterministic detector fired on the same content unit.

       * `inspection`: ML block honored if a deterministic detector fired anywhere in the request.

     * **Sidecar Fail Closed**: Block traffic if the Sidecar errors.

5. After you've reviewed and configured detection policies, click **Next**.

6. Review the overview of your configurations from previous steps. If these configurations are correct, click **Create Agent**.

### Step 4: Establish connectivity between agent and gateway

The final **Add Agent** page contains your **Agent Key** that you'll use to configure your agent to connect to an AI gateway.

|   |                                                                                     |
| - | ----------------------------------------------------------------------------------- |
|   | This key will only be displayed on this page and not available after configuration. |

1. Under **Integration**, select a configured **Gateway** from the list to point your agent at that gateway.

2. Copy the code containing your virtual key.

3. Use the code you just copied to connect to the **Agentic App** through your client. For example, you can paste the code into Claude Desktop.

   ### Result:

   The associated LLM, MCP, or A2A is now accessible through that client.

4. After pasting the key and establishing connectivity, click **Done - Go To Agents**.

   ### Result:

   On the Agent Registry page, the agent you registered should now be in the list.

5. Validate that the registered agent's tools appear in the client and that restricted tools don't appear.

### Result

Users can now get the **MCP Config** for connecting their client to the registered agent under **Agentic Apps** in the PingOne Privilege user console.

---

---
title: Agentic apps
description: Agentic apps in Agent Privilege integrate agentic applications so that AI agents can reach enterprise services securely.
component: privilege
page_id: privilege:agent-privilege:configuration/agentic-apps/index
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/configuration/agentic-apps/index.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 10, 2026
section_ids:
  available-applications: Available applications
  available-catalog-entries: Available catalog entries
---

# Agentic apps

Agentic apps are applications you can register in the PingOne Privilege admin console on the **Agentic Apps** page. The **Active Apps** tab shows you which applications are currently deployed in your environment. Available applications can be configured in the **Add Application** and **MCP Catalog** tabs.

Refer to the following tables for available applications, their uses, and links to their configuration guides.

## Available applications

Agentic apps are applications that allow AI agents to reach enterprise services through PingOne Privilege.

| Entry                               | Use case                                                                               |
| ----------------------------------- | -------------------------------------------------------------------------------------- |
| [Git Server](git-server.html)       | Host and secure Git repositories so that AI agent commits are attributable.            |
| [MCP Server](mcp-server.html)       | Front a backend MCP server with just-in-time access, credential injection, and policy. |
| [MCP Aggregate](mcp-aggregate.html) | Aggregate multiple MCP servers behind a single application.                            |
| [OpenAPI MCP](openapi-mcp.html)     | Expose OpenAPI-defined services to AI agents over MCP.                                 |
| [Remote Agent](remote-agent.html)   | Register a remote agent that connects to PingOne Privilege.                            |

## Available catalog entries

The MCP Catalog provides prebuilt integrations for commonly used MCP servers, so you can connect PingOne Privilege to enterprise services without deploying your own MCP server.

| Entry                               | Provides tools for                                   |
| ----------------------------------- | ---------------------------------------------------- |
| [Atlassian](atlassian.html)         | Jira, Confluence, and other Atlassian Cloud services |
| [Brave Search](brave-search.html)   | The Brave Search API for web search from AI agents   |
| [Elasticsearch](elasticsearch.html) | Elasticsearch clusters, indices, and queries         |
| [GitHub](github.html)               | GitHub repositories, issues, and pull requests       |
| [Grafana](grafana.html)             | Grafana dashboards, data sources, and alerts         |
| [MongoDB](mongodb.html)             | MongoDB databases and collections                    |
| [OpenSearch](opensearch.html)       | OpenSearch clusters, indices, and queries            |
| [PostgreSQL](postgresql.html)       | PostgreSQL databases, tables, and queries            |
| [Redis](redis.html)                 | Redis data stores                                    |

---

---
title: Atlassian
description: Connect PingOne Privilege to Jira, Confluence, and other Atlassian Cloud services through the MCP Catalog.
component: privilege
page_id: privilege:agent-privilege:configuration/agentic-apps/atlassian
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/configuration/agentic-apps/atlassian.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 10, 2026
section_ids:
  configure-an-atlassian-integration: Configure an Atlassian integration
  before-you-begin: Before you begin
  step-1-create-an-atlassian-application-in-pingone-privilege: "Step 1: Create an Atlassian application in PingOne Privilege"
  step-2-configure-policies-for-atlassian-tools: "Step 2: Configure policies for Atlassian tools"
  step-3-establish-connectivity-between-agent-and-gateway: "Step 3: Establish connectivity between agent and gateway"
  result: Result:
  result-2: Result
---

# Atlassian

The MCP Catalog provides a prebuilt integration for Jira, Confluence, and other Atlassian Cloud services.

This integration provides:

* Tools for working with Jira, Confluence, and other Atlassian Cloud services.

* Tool, prompt, and resource-level PingOne Privilege policy configuration.

* Full audit of agent tool calls in **Activity > Activity Logs**.

## Configure an Atlassian integration

Configuration involves creating an Atlassian application in PingOne Privilege, configuring policies for the application, and establishing connectivity between the agent and an Agent Privilege gateway.

### Before you begin

Ensure you have the following:

* An AI gateway configured in Directory > Nodes. Learn more in [AI gateways](../ai-gateways.html).

* You have an Atlassian administrator account with permission to create API tokens.

### Step 1: Create an Atlassian application in PingOne Privilege

1. In the PingOne Privilege admin console, go to **AI Security > Agentic Apps**.

2. Click the **MCP Catalog** tab.

3. In the **Atlassian** tile, click **Add** **[icon: plus, set=fa]**.

4. Enter an **Application Name** for the connection.

5. Select a configured **Mesh Cluster**.

6. Provide the following configuration details for your Jira URL:

   * **Jira URL**: Base URL for your Jira instance.

   * **Confluence URL**: Base URL for your Confluence instance.

   * **Jira Username**: Atlassian account email or username.

7. Click **Next** in the **Configuration** module.

8. Provide the following configuration details for your Jira API Token:

   * **Jira API Token**: Atlassian cloud API token for Jira.

   * **Confluence Username**: Atlassian cloud account email or username.

   * **Confluence API Token**: Atlassian cloud API token for Confluence.

9. Click **Next** in the **Configuration** module.

10. Provide the following configuration details for your Jira Personal Access Token:

    * **Jira Personal Access Token**: Personal Access Token for Jira.

    * **Confluence Personal Access Token**: Personal Access Token for Confluence.

11. Click **Create**.

### Step 2: Configure policies for Atlassian tools

1. In the PingOne Privilege admin console, go to **AI Security > Agentic Apps**.

2. In the list, find the **Atlassian** application.

3. Click **(⋮)**, then click **Create Policy**.

4. Select which operations from the Atlassian specification are available to agents.

5. Click **Update Configuration**.

6. Add the users or groups the policy will apply to.

7. Define the users or groups the policy will apply to.

8. Click **Continue**.

9. Configure the policy with the following fields:

   * **Policy Name**

   * **Select Timezone**

   * **Start Date** and **Start Time**

   * **End Date** in hours, days, weeks, months, or custom date.

10. Click **Submit** to save the policy.

### Step 3: Establish connectivity between agent and gateway

1. In the PingOne Privilege admin console, go to **AI Security > Agentic Apps**.

2. On the **Active Applications** tab, find the **Atlassian** application and click **More Info**.

3. On the **Overview** tab's **Resource Information** section, select a configured **AI Gateway** from the list.

4. Copy the **MCP Config** code.

5. Use the code you just copied to connect to the **Atlassian** app through your client. For example, you can paste the code into Claude Desktop.

   ### Result:

   The associated **Atlassian** app is now accessible through that client.

6. Validate that the Atlassian tools appear in the client and that restricted tools don't appear.

### Result

Users can now get the **MCP Config** for connecting their client to the **Atlassian** app under **Agentic Apps** in the PingOne Privilege user console.

---

---
title: Brave Search
description: Connect PingOne Privilege to the Brave Search API through the MCP Catalog.
component: privilege
page_id: privilege:agent-privilege:configuration/agentic-apps/brave-search
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/configuration/agentic-apps/brave-search.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 10, 2026
section_ids:
  configure-a-brave-search-integration: Configure a Brave Search integration
  before-you-begin: Before you begin
  step-1-create-a-brave-search-application-in-pingone-privilege: "Step 1: Create a Brave Search application in PingOne Privilege"
  step-2-configure-policies-for-brave-search-tools: "Step 2: Configure policies for Brave Search tools"
  step-3-establish-connectivity-between-agent-and-gateway: "Step 3: Establish connectivity between agent and gateway"
  result: Result:
  result-2: Result
---

# Brave Search

The MCP Catalog provides a prebuilt integration for the Brave Search API.

This integration provides:

* Tools for working with the Brave Search API for web search from AI agents.

* Tool, prompt, and resource-level PingOne Privilege policy configuration.

* Full audit of agent tool calls in **Activity > Activity Logs**.

## Configure a Brave Search integration

Configuration involves creating a Brave Search application in PingOne Privilege, configuring policies for the application, and establishing connectivity between the agent and an Agent Privilege gateway.

### Before you begin

Ensure you have the following:

* An AI gateway configured in Directory > Nodes. Learn more in [AI gateways](../ai-gateways.html).

* You have a Brave Search API subscription with an API key.

### Step 1: Create a Brave Search application in PingOne Privilege

1. In the PingOne Privilege admin console, go to **AI Security > Agentic Apps**.

2. Click the **MCP Catalog** tab.

3. In the **Brave Search** tile, click **Add** **[icon: plus, set=fa]**.

4. Enter an **Application Name** for the connection.

5. Select a **Mesh Cluster**.

6. Provide the required **Brave Search API key**.

   |   |                                                             |
   | - | ----------------------------------------------------------- |
   |   | This API key is located in your Brave Search API dashboard. |

7. Click **Create**.

The Brave Search integration is now available to AI agents as an MCP server, with PingOne Privilege policy applied to its tools.

### Step 2: Configure policies for Brave Search tools

1. In the PingOne Privilege admin console, go to **AI Security > Agentic Apps**.

2. In the list, find the **Brave Search** application.

3. Click **(⋮)**, then click **Create Policy**.

4. Select which operations from the Brave Search specification are available to agents.

5. Click **Update Configuration**.

6. Add the users or groups the policy will apply to.

7. Define the users or groups the policy will apply to.

8. Click **Continue**.

9. Configure the policy with the following fields:

   * **Policy Name**

   * **Select Timezone**

   * **Start Date** and **Start Time**

   * **End Date** in hours, days, weeks, months, or custom date.

10. Click **Submit** to save the policy.

### Step 3: Establish connectivity between agent and gateway

1. In the PingOne Privilege admin console, go to **AI Security > Agentic Apps**.

2. On the **Active Applications** tab, find the **Brave Search** application and click **More Info**.

3. On the **Overview** tab's **Resource Information** section, select a configured **AI Gateway** from the list.

4. Copy the **MCP Config** code.

5. Use the code you just copied to connect to the **Brave Search** app through your client. For example, you can paste the code into Claude Desktop.

   ### Result:

   The associated **Brave Search** app is now accessible through that client.

6. Validate that the Brave Search tools appear in the client and that restricted tools don't appear.

### Result

Users can now get the **MCP Config** for connecting their client to the **Brave Search** app under **Agentic Apps** in the PingOne Privilege user console.

---

---
title: Configure Agent Privilege for further use cases
description: Configure Agent Privilege to secure AI agent traffic beyond personal agent discovery.
component: privilege
page_id: privilege:agent-privilege:getting-started/configure-agent-privilege
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/getting-started/configure-agent-privilege.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 22, 2026
section_ids:
  configure-agent-privilege: Configure Agent Privilege
---

# Configure Agent Privilege for further use cases

Now that you've set up a PingOne environment for Agent Privilege, configured access to the PingOne Privilege admin console, and completed your first use case for personal agent discovery, you can explore more ways to configure and use Agent Privilege.

## Configure Agent Privilege

Configure Agent Privilege in the PingOne Privilege admin console for additional use cases:

* [Deploy the AI Gateway](../configuration/ai-gateways.html) to put Agent Privilege in the traffic path between agents and your resources.

* [Add agents in Agent Registry](../configuration/agent-registry.html) to register the agents that will authenticate to PingOne Privilege.

* [Require PingID Workforce Authentication](../configuration/pingid-mfa-app-connect.html) for PingOne Privilege app connections and step-up authentication.

* [Agent Privilege use cases](../use-cases/index.html) for workload agent, personal agent, and NHI agent management.

---

---
title: Configuring Agent Privilege
description: Configure Agent Privilege to secure AI agent access to agentic apps, LLM providers, and Git repositories through just-in-time, least-privilege access controls.
component: privilege
page_id: privilege:agent-privilege:index
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/index.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 10, 2026
section_ids:
  configurations-for-agentic-access: Configurations for agentic access
  configuration-for-mfa: Configuration for MFA
---

# Configuring Agent Privilege

This section describes how to configure Agent Privilege in the PingOne Privilege admin console. Agent Privilege secures the interactions between AI agents and the enterprise services they reach, through just-in-time access controls, approval automation, and session auditing.

## Configurations for agentic access

Complete these configurations in order to put Agent Privilege in the traffic path between AI agents and your enterprise resources:

1. [Deploy the AI Gateway](configuration/ai-gateways.html): The AI Gateway is the gateway that fronts your agentic apps, LLM providers, and peer agents. The MCP Gateway and LLM Gateway functionality is delivered through it during agent registry.

2. [Configure agentic apps](configuration/agentic-apps/index.html): Configure the applications your agents reach, such as MCP Server, MCP Aggregate, OpenAPI MCP, and Remote Agent, each associated with the AI Gateway through its Mesh Cluster. You can also register prebuilt integrations from the MCP Catalog.

3. [Register agents](configuration/agent-registry.html): Register each agent, select its access scopes, and configure its model, tool, and peer access. Enable AI Guard in the wizard's runtime protection step.

## Configuration for MFA

For organizations already using PingID for multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)*, you can require [PingID Workforce Authentication for PingOne Privilege app connections](configuration/pingid-mfa-app-connect.html).

---

---
title: Configuring AgentCore
description: Connect PingOne Privilege to AWS AgentCore so AI discovery can review its agent inventory.
component: privilege
page_id: privilege:agent-privilege:configuration/workload-agent-apps/agentcore
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/configuration/workload-agent-apps/agentcore.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 21, 2026
---

# Configuring AgentCore

Connect Amazon Web Services (AWS) *(tooltip: \<div class="paragraph">
\<p>An Amazon subsidiary providing cloud computing platforms.\</p>
\</div>)* AgentCore as a workload agent application so {p1priv-ai-discovery} for workload agents can review the agents running in the account. Learn more in [Discover and manage workload agents](../../use-cases/workload-agents.html).

1. In the PingOne Privilege admin console, go to **AI Security > AI Platform Agents**.

2. Click the **Add Application** tab.

3. In the list of available applications, find **AgentCore** and click **[icon: plus, set=fa]Integrate**.

4. Enter a **Name** for the connection.

5. (Optional) Enter a **Description**.

6. Click **Next**.

7. Add your credentials using one of the following methods:

   * Enter the **Template URL** and **External ID** directly in the setup wizard.

   * Click **Open CF Template** to launch into AWS to enter credentials there.

8. Click **Next**.

9. After the stack status is **CREATE_COMPLETE**, open the **Outputs** tab in CloudFormation and paste the **Cross Account Role ARN** into the setup wizard.

10. (Optional): Add comma-separated **Regions**. Leave this field empty to scan all regions.

11. Review the summary, then click **Add Connection**.

You can now validate that the connection is active in the **Active Applications** tab.

---

---
title: Configuring Agentforce
description: Connect PingOne Privilege to Salesforce Agentforce so AI discovery can review its agent inventory.
component: privilege
page_id: privilege:agent-privilege:configuration/workload-agent-apps/agentforce
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/configuration/workload-agent-apps/agentforce.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 21, 2026
---

# Configuring Agentforce

Connect Salesforce Agentforce as a workload agent application so {p1priv-ai-discovery} for workload agents can review the agents running in the platform. Learn more in [Discover and manage workload agents](../../use-cases/workload-agents.html).

1. In the PingOne Privilege admin console, go to **AI Security > AI Platform Agents**.

2. Click the **Add Application** tab.

3. In the list of available applications, find **Agentforce** and click **[icon: plus, set=fa]Integrate**.

4. Enter a **Name** for the connection.

5. (Optional) Enter a **Description**.

6. Click **Next**.

7. Create a **Connected App**:

   1. In Salesforce, go to **Salesforce Setup > App Manager**.

   2. Ensure **Client Credentials Flow** is enabled.

   3. Assign a `Run-As` user to the app.

   4. Ensure the app has the following OAuth *(tooltip: \<div class="paragraph">
      \<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
      \</div>)* scopes:

      * `api`

      * `wave_api`

   5. Ensure the app has the required IAM roles:

      * `BotDefinition: Read`

      * `BotVersion: Read`

      * `BotInvocableAction: Read`

      * `NamedCredential: Read (Tooling API)`

      * `Organization: Read`

      * `BotVersion: Edit`

      * `NamedCredential: Edit (Tooling API)`

      * `BotDefinition: Delete`

8. Click **Next**.

9. Provide credentials using one of these methods:

   * Enter the **Instance URL**, **Client ID**, and **Client Secret**.

   * Click **JWT Bearer Flow** as an alternative to **Client Secret** for certificate-based authentication.

     1. Enter your **Salesforce Username**.

     2. Paste your **JWT Private Key (PEM)**.

10. Click **Next**.

11. Review the summary, then click **Add Connection**.

You can now validate that the connection is active in the **Active Applications** tab.

---

---
title: Configuring AI Foundry
description: Connect PingOne Privilege to Azure AI Foundry so AI discovery can review its agent inventory.
component: privilege
page_id: privilege:agent-privilege:configuration/workload-agent-apps/ai-foundry
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/configuration/workload-agent-apps/ai-foundry.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 21, 2026
---

# Configuring AI Foundry

Connect Azure AI Foundry as a workload agent application so {p1priv-ai-discovery} for workload agents can review the agents running in the subscription. Learn more in [Discover and manage workload agents](../../use-cases/workload-agents.html).

1. In the PingOne Privilege admin console, go to **AI Security > AI Platform Agents**.

2. Click the **Add Application** tab.

3. In the list of available applications, find **AI Foundry** and click **[icon: plus, set=fa]Integrate**.

4. Enter a **Name** for the connection.

5. (Optional) Enter a **Description**.

6. Click **Next**.

7. Create an Entra ID App Registration and assign to it the following Azure role-based access control (RBAC) *(tooltip: \<div class="paragraph">
   \<p>Also known as non-discretionary access control, this authorization strategy bases user access on assigned roles.\</p>
   \</div>)* roles:

   * `Reader (Subscription)`

   * `Foundry User (Subscription)`

   * `Foundry Project Manager (Subscription)`

   * `Cognitive Services Contributor (AI Services account)`

   * `User Access Administrator (Subscription)` or `Custom role (roleAssignments/read + roleAssignments/delete)`

8. Click **Next**.

9. Enter your **Tenant ID**, **Client ID**, **Client Secret**, and **Subscription ID**, then click **Next**.

10. Review the summary, then click **Add Connection**.

You can now validate that the connection is active in the **Active Applications** tab.

---

---
title: Configuring AI gateways
description: The PingOne Privilege AI Gateway secures AI-agent interactions.
component: privilege
page_id: privilege:agent-privilege:configuration/ai-gateways
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/configuration/ai-gateways.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 28, 2026
page_aliases: ["agent-privilege:mcp-gateway.adoc"]
section_ids:
  configure-an-ai-gateway-using-the-setup-wizard: Configure an AI gateway using the setup wizard
  before-you-begin: Before you begin
  step-1-create-the-oidc-web-application-in-pingone: "Step 1: Create the OIDC web application in PingOne"
  result: Result:
  step-2-configure-the-ai-gateway-in-pingone-privilege: "Step 2: Configure the AI gateway in PingOne Privilege"
  next-steps: Next steps
  configure-an-ai-gateway-using-docker: Configure an AI gateway using Docker
  before-you-begin-2: Before you begin
  step-1-create-the-oidc-web-application-in-pingone-2: "Step 1: Create the OIDC web application in PingOne"
  result-2: Result:
  step-2-add-the-ai-gateway-in-pingone-privilege: "Step 2: Add the AI gateway in PingOne Privilege"
  step-3-run-the-gateway-container: "Step 3: Run the gateway container"
  result-3: Result
  troubleshooting-the-ai-gateway: Troubleshooting the AI gateway
---

# Configuring AI gateways

The PingOne Privilege {p1priv-ai-gateway} secures AI-agent interactions at a single enforcement point. It authenticates every caller, enforces policy at the tool, model, and agent boundaries, and injects backend credentials at runtime so agents never hold them. Every request and response is inspected for AI-specific threats, and all interactions are recorded in one audit trail.

PingOne Privilege allows you to add an AI gateway using a setup wizard or through Docker.

|   |                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Any user who uses personal agents through an AI gateway must have an allow policy for that agent. This applies only when the personal agent calls agentic apps through a registered agent. Learn more in [Registering an agent](agent-registry.html). |

## Configure an AI gateway using the setup wizard

### Before you begin

You must create a new virtual machine (VM) to deploy the proxy container. Ensure the VM meets the required specifications for optimal performance and connectivity:

* **CPU**: 4 vCPUs.

* **RAM**: 16 GB.

* **Storage**: 20 GB. Provision more storage if you deploy the MCP Catalog on this gateway.

* **Firewall Policy**:

  * **Outbound**: Allow all traffic.

  * **Inbound**: Open the following ports:

    * `8623`: AI clients to {p1priv-ai-gateway}

    * `8680`: Endpoint Controller to {p1priv-ai-gateway}

    * `8690`: Gateway to Gateway - Mesh Cluster

* **DNS**: A DNS record for the gateway's fully-qualified domain name (FQDN) *(tooltip: \<div class="paragraph">
  \<p>A domain name that specifies its exact location in the DNS tree hierarchy.\</p>
  \</div>)*, so that AI clients can resolve the **Gateway URL**.

* **TLS certificate**: Generate a TLS server certificate for the gateway FQDN and copy it to the gateway host. The wizard fills the **Cert Path** field with the default location.

* Supported Operating Systems:

  * `RHEL / CentOS (RPM x86_64)`

  * `Debian / Ubuntu AMD64`

  * `Debian / Ubuntu ARM64`

### Step 1: Create the OIDC web application in PingOne

1. In the PingOne admin console, go to **Applications > Applications**.

2. Click **[icon: plus, set=fa]**.

3. Enter an appropriate **Application Name** and optional **Description**.

4. Under **Application Type**, click the **OIDC Web App** application type.

5. Click **Save**.

   ### Result:

   The **Overview** panel for the application opens.

6. On the **Configuration** tab, click the **Pencil** icon ([icon: pencil, set=fa]).

7. Configure the **OIDC Settings**:

   * **Response Type**: The default **Code** checkbox.

   * **Grant Type**: The default **Authorization Code** checkbox.

   * **PKCE Enforcement**: The default **Optional** option.

   * **Redirect URI**: The AI gateway's server URL with `/callback` appended.

   * **Token Endpoint Authentication Method**: Select the **Client Secret Post** option.

8. Click **Save**.

9. Copy the **Client ID** and **Client Secret** values. You need them for configuring the AI gateway in PingOne Privilege.

### Step 2: Configure the AI gateway in PingOne Privilege

1. In the PingOne Privilege admin console, go to **Directory > Nodes**.

2. Click **Add New**, and then click **Add via Wizard**.

3. Review the requirements for your VM, then click **Next**.

4. Install Docker based on the official [Docker installation guide for your OS](https://docs.docker.com/engine/install/).

5. Verify Docker is running using the following command in your CLI:

   `sudo docker ps`

   If the command runs without errors, Docker is ready to use.

6. Select **AI Gateway** as your deployment mode. Click **Next**.

7. Enter a unique **AI Gateway Name** to identify the AI gateway.

8. Enter the **FQDN / Host IP** of the server where you installed the AI gateway.

9. Click **Next**.

10. Enter the following fields:

    * **AI Gateway Server** fields:

      * **Gateway URL**: FQDN from the VM.

        |   |                                                                   |
        | - | ----------------------------------------------------------------- |
        |   | This URL must include a port. The default gateway port is `8623`. |

      * **Cert Path**: The wizard fills this field by default.

      * **(Optional)**: **Redis URL**: Point the Gateway to your Redis URL.

    * Fill in the following fields with information from the OIDC app created in PingOne:

      * **Client ID**

      * **Client Secret**

      * **Auth URL**

      * **Token URL**

      * **User Info URL**

      * **User ID Claim**

11. Click **Next**.

12. Create the environment file with the following commands:

    1. To create the directory, if not already present, run:

       ```bash
       sudo mkdir -p /var/lib/procyon
       ```

    2. To create the file and open it, run:

       ```bash
       sudo vi /var/lib/procyon/procyon-guest-agent.env
       ```

    3. Copy the generated content from your setup tasks and paste it inside the newly created file and save it.

    4. In the setup wizard, click **Next**.

13. Select your operating system from the list. Click **Show Instructions** for the detailed steps for installing the package for your operating system.

14. Click **Finish**.

### Next steps

After adding the gateway, go to the **Directory > Nodes** page in the admin console. Your new AI gateway should be listed with a **Success** status, typically within a minute of startup.

## Configure an AI gateway using Docker

### Before you begin

Ensure the following inbound ports are open on the host where you install the Gateway Mesh Cluster:

* `8623`: AI clients to {p1priv-ai-gateway}

* `8680`: Endpoint Controller to {p1priv-ai-gateway}

* `8690`: Gateway to Gateway - Mesh Cluster

Create a DNS record for the gateway host's FQDN, so that AI clients can resolve the **AI Gateway Server URL**.

### Step 1: Create the OIDC web application in PingOne

1. In the PingOne admin console, go to **Applications > Applications**.

2. Click **[icon: plus, set=fa]**.

3. Enter an appropriate **Application Name** and optional **Description**.

4. Under **Application Type**, click the OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
   \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
   \</div>)* (**OIDC Web App**) application type.

5. Click **Save**.

   ### Result:

   The **Overview** panel for the application opens.

6. Click the **Configuration** tab, then click the **Pencil** ([icon: pencil, set=fa]) icon.

7. Configure the **OIDC Settings**:

   * **Response Type**: The default **Code** checkbox.

   * **Grant Type**: The default **Authorization Code** checkbox.

   * **PKCE Enforcement**: The default **Optional** option.

   * **Redirect URI**: The AI gateway's server URL with `/callback` appended.

   * **Token Endpoint Authentication Method**: Select the **Client Secret Post** option.

8. Click **Save**.

9. Copy the **Client ID** and **Client Secret** values. You need them for configuring the AI gateway in PingOne Privilege.

### Step 2: Add the AI gateway in PingOne Privilege

1. In the PingOne Privilege admin console, go to **Directory > Nodes**.

2. Click **Add New**, and then click **Add via Docker**.

3. Select **AI gateway**.

4. To generate a Docker command, fill in the following fields:

   * **Cluster ID**: A unique name for this gateway. You can't change this after registration.

   * **Host IP**: The gateway host's address. This field is informational only. Clients connect to the **AI Gateway Server URL**.

   * **AI Gateway Server URL**: The base URL that MCP clients call. The OIDC application's **Redirect URI** must match this value, with `/callback` appended.

   * **OIDC Client ID**: The client ID from the OIDC application configured in step 1.

   * **OIDC Client Secret**: The client secret from the OIDC application configured in step 1.

   * **OIDC Auth URL**: The authorization endpoint that starts the browser sign-on, for example, `https://auth.pingone.com/<environment-id>/as/authorize`.

   * **OIDC Token URL**: The token endpoint where the gateway exchanges authorization codes for tokens, for example, `https://auth.pingone.com/<environment-id>/as/token`.

   * **OIDC User URL**: The userinfo endpoint that resolves the user's profile after sign-on, for example, `https://auth.pingone.com/<environment-id>/as/userinfo`.

   * **User ID Claim**: The token claim that identifies the user for policy and audit. Use `sub` unless your OIDC application maps an email claim.

5. Click **Get Docker Command**.

6. Click **Copy Docker Command** to copy the command to your clipboard.

### Step 3: Run the gateway container

The Docker command copied in step 2 is self-contained and performs the following actions:

* Creates the gateway's configuration directory.

* Writes the configuration file with the values from the form.

* Runs the container with a short-lived registration token.

|   |                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Run the command promptly after copying it. If the registration token expires before the container starts, the container fails to register until you generate and run a new command. |

The Docker command has the following shape, with your values filled in:

```bash
mkdir -p /var/lib/procyon/config

cat > /var/lib/procyon/config/pingone.env <<'EOF'
SERVER_URL=https://localhost:8623
OIDC_CLIENT_ID=<client ID from step 1>
OIDC_CLIENT_SECRET=<client secret from step 1>
OIDC_AUTH_URL=https://auth.pingone.com/<environment-id>/as/authorize
OIDC_TOKEN_URL=https://auth.pingone.com/<environment-id>/as/token
OIDC_USER_URL=https://auth.pingone.com/<environment-id>/as/userinfo
OIDC_SCOPES=openid profile email
USER_ID_CLAIM=sub
EOF

docker run -itd -e ENV_PROXY_TOKEN=<registration token> \
  --net=host --name privilege-aigw \
  -v /var/log/procyon:/var/log/procyon \
  -v /var/lib/procyon/config:/procyon/config \
  -v /var/lib/procyon/ssl:/procyon/ssl \
  -v /var/lib/procyon/recordings:/procyon/recordings \
  <gateway image> \
  /procyon/bin/mcpgw -mcpconfpath /procyon/config/pingone.env -hostname 127.0.0.1
```

|   |                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | On a Linux host, run the Docker command as-is.On Docker Desktop for Mac:1) Replace `--net=host` with `-p 8623:8623 -p 8680:8680 -p 8690:8690`. Host networking publishes no ports on Docker Desktop.

2) Replace the `/var/…​` host paths with local paths, for example `~/pingidentity-local/…​`. Docker creates any missing host directories automatically. |

### Result

Your new AI gateway should be listed with a **Success** status on the **Directory > Nodes** page.

|   |                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Endpoint Controller doesn't have automatic visibility into on-premise network topology. After deploying the gateway, you must manually configure which resources are accessible through it. |

The gateway writes its log to `/var/log/procyon/cyonproxy.log` on the gateway host, not to the container console, so container logging commands show no output. A successful startup and registration show the following in the log:

* `MCP Gateway starting in TLS mode on :8623`, the port MCP clients call.

* A line confirming that the node established its command stream to the cluster.

You can also confirm that the gateway enforces authentication by calling the well-known endpoint without credentials:

```bash
curl -sk https://<gateway-url>:8623/.well-known/openid-configuration
```

An HTTP 401 response is expected: the gateway acts as an OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)* protected resource and rejects unauthenticated callers.

## Troubleshooting the AI gateway

| Symptom                                                                            | Cause                                                                         | Fix                                                                                                                       |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| The container exits immediately, and the log shows `MCP Config path not specified` | The gateway binary requires the configuration path argument.                  | Run the generated Docker command, or make sure the command points to the gateway configuration file using `-mcpconfpath`. |
| The log shows `has same NodeURL …​ misconfigured Node`                             | The **Host IP** makes the mesh see the node as its own peer.                  | Benign for a single-node deployment; registration still succeeds. Use a real host address on multi-node deployments.      |
| The container restarts repeatedly after registration                               | The registration token expired before the container started.                  | Generate a new Docker command in the console, and run it promptly.                                                        |
| The log shows `token contains an invalid number of segments`                       | The registration token was pasted twice or was otherwise corrupted.           | Generate a new Docker command in the console, and run it.                                                                 |
| Clients receive HTTP 502 responses                                                 | The port clients call doesn't match the port the gateway actually bound.      | Find the port in the startup log line (`MCP Gateway starting in TLS mode on …​`), and use that port in client URLs.       |
| Sign-on fails, and the log shows `userinfo …​ yielded an empty user ID`            | The **User ID Claim** references a claim the OIDC application doesn't return. | Generate a new Docker command with the correct claim, typically `sub`, and run it.                                        |
| The log shows a transient `Failed to find the tenant` at startup                   | The tenant cache is cold in the first seconds after boot.                     | Ignore it if the node establishes its command stream immediately after.                                                   |

---

---
title: Configuring Bedrock
description: Connect PingOne Privilege to AWS Bedrock so AI discovery can review its agent inventory.
component: privilege
page_id: privilege:agent-privilege:configuration/workload-agent-apps/bedrock
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/configuration/workload-agent-apps/bedrock.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 21, 2026
---

# Configuring Bedrock

Connect Amazon Web Services (AWS) *(tooltip: \<div class="paragraph">
\<p>An Amazon subsidiary providing cloud computing platforms.\</p>
\</div>)* Bedrock as a workload agent application so {p1priv-ai-discovery} for workload agents can review the agents running in the account. Learn more in [Discover and manage workload agents](../../use-cases/workload-agents.html).

1. In the PingOne Privilege admin console, go to **AI Security > AI Platform Agents**.

2. Click the **Add Application** tab.

3. In the list of available applications, find **Bedrock** and click **[icon: plus, set=fa]Integrate**.

4. Enter a **Name** for the connection, such as `my-bedrock-prod`.

5. (Optional) Enter a **Description**.

6. Click **Next**.

7. Add your credentials using one of the following methods:

   * Enter the **Template URL** and **External ID** directly in the setup wizard.

   * Click **Open CF Template** to launch into AWS to enter credentials there.

8. Click **Next**.

9. After the stack status is **CREATE_COMPLETE**, open the **Outputs** tab in CloudFormation and paste the **Cross Account Role ARN** into the setup wizard.

10. (Optional): Add comma-separated **Regions**. Leave this field empty to scan all regions.

11. Review the summary, then click **Add Connection**.

You can now validate that the connection is active in the **Active Applications** tab.

---

---
title: Configuring Copilot Studio
description: Connect PingOne Privilege to Microsoft Copilot Studio so AI discovery can review its agent inventory.
component: privilege
page_id: privilege:agent-privilege:configuration/workload-agent-apps/copilot-studio
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/configuration/workload-agent-apps/copilot-studio.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 21, 2026
---

# Configuring Copilot Studio

Connect Microsoft Copilot Studio as a workload agent application so {p1priv-ai-discovery} for workload agents can review the agents running in the tenant. Learn more in [Discover and manage workload agents](../../use-cases/workload-agents.html).

1. In the PingOne Privilege admin console, go to **AI Security > AI Platform Agents**.

2. Click the **Add Application** tab.

3. In the list of available applications, find **Copilot Studio** and click **[icon: plus, set=fa]Integrate**.

4. Enter a **Name** for the connection.

5. (Optional) Enter a **Description**.

6. Click **Next**.

7. Register an Entra ID App, then complete three steps:

   1. Assign the service provider (SP) *(tooltip: \<div class="paragraph">
      \<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
      \</div>)* a directory role in Entra ID. This step enables tenant-level discovery.

      1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com/).

      2. Go to **Identity > Roles & admin > Roles & Admin**.

      3. Open **Power Platform Administrator**, then click **[icon: plus, set=fa]Add Assignments**.

      4. Add the service principal.

   2. Register the app as a **PP Admin Management App**. This step enables tenant-level admin API access.

      1. For this step, you can either:

         * Enter the following command in PowerShell:

           `New-PowerAppManagementApp -ApplicationId "<Your_App_Client_ID>"`

         * Use the following API call:

           `API: PUT https://api.bap.microsoft.com/providers/Microsoft.BusinessAppPlatform/adminApplications/<Your_App_Client_ID>?api-version=2020-10-01`

      2. Verify that `Get-PowerAppManagementApp` lists your app.

   3. Add the application user in each Dataverse environment. This step grants access to bots and flows inside the environment.

      1. Go to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).

      2. Go to **Environments > Select Environment**.

      3. Click **Settings > Users + permissions > Application users**.

      4. Click **New app user**.

      5. Select the app you created and assign the **System Administrator** role to it.

8. Click **Next**.

9. Enter your **Tenant ID**, **Client ID**, and **Client Secret**.

10. Click **Next**.

11. Review the summary, then click **Add Connection**.

You can now validate that the connection is active in the **Active Applications** tab.

---

---
title: Configuring Databricks AI
description: Connect PingOne Privilege to Databricks so AI discovery can review its agent inventory.
component: privilege
page_id: privilege:agent-privilege:configuration/workload-agent-apps/databricks-ai
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/configuration/workload-agent-apps/databricks-ai.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 21, 2026
---

# Configuring Databricks AI

Connect Databricks as a workload agent application so {p1priv-ai-discovery} for workload agents can review the agents running in the workspace. Learn more in [Discover and manage workload agents](../../use-cases/workload-agents.html).

1. In the PingOne Privilege admin console, go to **AI Security > AI Platform Agents**.

2. Click the **Add Application** tab.

3. In the list of available applications, find **Databricks AI** and click **[icon: plus, set=fa]Integrate**.

4. Enter a **Name** for the connection.

5. (Optional) Enter a **Description**.

6. Click **Next**.

7. To configure **Permissions**, you can either:

   * Create a Databricks service principal with the following permissions:

     * `GET /api/2.0/serving-endpoints`

     * `GET /api/2.0/permissions/serving-endpoints/<id>`

     * `GET /api/2.0/genie/spaces`

     * `CAN_VIEW` (or higher) on each serving endpoint

     * `CAN_MANAGE on the serving endpoint`

     * `PATCH /api/2.0/serving-endpoints/<name>/tags`

     * `PUT /api/2.0/serving-endpoints/<name>/ai-gateway`

     * `PATCH /api/2.0/permissions/serving-endpoints/<id>`

     * `PATCH /api/2.0/permissions/serving-endpoints/<id>`

     * `PATCH /api/2.0/permissions/serving-endpoints/<id>`

       |   |                                                                                                                                               |
       | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | Foundation Model API endpoints (no endpoint ID) do not support permission management.Genie spaces do not support permission write operations. |

   * Generate a personal access token:

     1. In your Databricks workspace, click **User Settings**.

     2. Go to **Developer > Access Tokens**.

     3. Click **Generate new token**.

     4. For service principals, use the Databricks CLI or the System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
        \<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
        \</div>)* API to create the principal and generate an OAuth M2M token.

8. When you are finished setting up **Permissions**, click **Next**.

9. Enter your **Workspace URL** and generated **Access Token**. Click **Next**.

10. Review the summary, then click **Add Connection**.

You can now validate that the connection is active in the **Active Applications** tab.

---

---
title: Configuring Lex V2
description: Connect PingOne Privilege to Amazon Lex V2 so AI discovery can review its agent inventory.
component: privilege
page_id: privilege:agent-privilege:configuration/workload-agent-apps/lex-v2
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/configuration/workload-agent-apps/lex-v2.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 21, 2026
---

# Configuring Lex V2

Connect Amazon Web Services (AWS) *(tooltip: \<div class="paragraph">
\<p>An Amazon subsidiary providing cloud computing platforms.\</p>
\</div>)* Lex V2 as a workload agent application so {p1priv-ai-discovery} for workload agents can review the agents running in the account. Learn more in [Discover and manage workload agents](../../use-cases/workload-agents.html).

1. In the PingOne Privilege admin console, go to **AI Security > AI Platform Agents**.

2. Click the **Add Application** tab.

3. In the list of available applications, find **Lex V2** and click **[icon: plus, set=fa]Integrate**.

4. Enter a **Name** for the connection.

5. (Optional) Enter a **Description**.

6. Click **Next**.

7. Add your credentials using one of the following methods:

   * Enter the **Template URL** and **External ID** directly in the setup wizard.

   * Click **Open CF Template** to launch into AWS to enter credentials there.

8. Click **Next**.

9. After the stack status is **CREATE_COMPLETE**, open the **Outputs** tab in CloudFormation and paste the **Cross Account Role ARN** into the setup wizard.

10. (Optional): Add comma-separated **Regions**. Leave this field empty to scan all regions.

11. Review the summary, then click **Add Connection**.

You can now validate that the connection is active on the **Active Applications** tab.

---

---
title: Configuring Snowflake Cortex
description: Connect PingOne Privilege to Snowflake Cortex so AI discovery can review its agent inventory.
component: privilege
page_id: privilege:agent-privilege:configuration/workload-agent-apps/snowflake-cortex
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/configuration/workload-agent-apps/snowflake-cortex.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 21, 2026
---

# Configuring Snowflake Cortex

Connect Snowflake Cortex as a workload agent application so {p1priv-ai-discovery} for workload agents can review the agents and MCP servers running in the account. Learn more in [Discover and manage workload agents](../../use-cases/workload-agents.html).

1. In the PingOne Privilege admin console, go to **AI Security > AI Platform Agents**.

2. Click the **Add Application** tab.

3. In the list of available applications, find **Snowflake Cortex** and click **[icon: plus, set=fa]Integrate**.

4. Enter a **Name** for the connection.

5. (Optional) Enter a **Description**.

6. Click **Next**.

7. Create a dedicated Snowflake service user and role with the following required privileges:

   * `SHOW AGENTS IN ACCOUNT`

   * `SHOW MCP SERVERS IN ACCOUNT`

   * `SHOW GRANTS ON AGENT <db>.<schema>.<name>`

   * `SHOW GRANTS ON MCP SERVER <db>.<schema>.<name>`

   * `SHOW GRANTS TO ROLE <role>`

   * `DESCRIBE AGENT <db>.<schema>.<name>`

   * `DESCRIBE MCP SERVER <db>.<schema>.<name>`

   * `USAGE ON WAREHOUSE`

   * `ALTER AGENT <fqn> SET COMMENT = $$<text>$$`

   * `ALTER MCP SERVER <fqn> SET COMMENT = $$<text>$$`

   * `DROP AGENT <fqn>`

   * `DROP MCP SERVER <fqn>`

   * `REVOKE USAGE ON AGENT <fqn> FROM ROLE PUBLIC`

   * `REVOKE USAGE ON AGENT <fqn> FROM ROLE <role>`

   * `REVOKE USAGE ON MCP SERVER <fqn> FROM ROLE PUBLIC`

   * `REVOKE USAGE ON MCP SERVER <fqn> FROM ROLE <role>`

   * `GRANT USAGE ON AGENT <fqn> TO ROLE <role>`

   * `GRANT USAGE ON MCP SERVER <fqn> TO ROLE <role>`

   * `GRANT OWNERSHIP ON AGENT <fqn> TO ROLE <role> REVOKE CURRENT GRANTS`

   * `GRANT OWNERSHIP ON MCP SERVER <fqn> TO ROLE <role> REVOKE CURRENT GRANTS`

8. When you're done creating the Snowflake service user, click **Next**.

9. Use the `org-account` format to enter an **Account Identifier**.

10. Enter a PingOne Privilege **User**.

11. Generate your **RSA Private Key (PEM)** with the following command:

    ```bash
    $ openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out rsa_key.pem
    ```

12. Paste the key into the required field in the wizard.

13. (Optional) Enter a **Warehouse**. Leave empty for user default.

14. (Optional) Enter a **Default Database**. Leave empty to scan all databases.

15. Click **Next**.

16. Review the summary, then click **Add Connection**.

You can now validate that the connection is active in the **Active Applications** tab.

---

---
title: Configuring Vertex AI
description: Connect PingOne Privilege to Google Vertex AI so AI discovery can review its agent inventory.
component: privilege
page_id: privilege:agent-privilege:configuration/workload-agent-apps/vertex-ai
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/configuration/workload-agent-apps/vertex-ai.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 21, 2026
---

# Configuring Vertex AI

Connect Google Vertex AI as a workload agent application so {p1priv-ai-discovery} for workload agents can review the agents running in the project. Learn more in [Discover and manage workload agents](../../use-cases/workload-agents.html).

1. In the PingOne Privilege admin console, go to **AI Security > AI Platform Agents**.

2. Click the **Add Application** tab.

3. In the list of available applications, find **Vertex AI** and click **[icon: plus, set=fa]Integrate**.

4. Enter a **Name** for the connection.

5. (Optional) Enter a **Description**.

6. Click **Next**.

7. Create a GCP service account, and assign it the required roles:

   * `roles/browser`

   * `roles/aiplatform.user`

   * `roles/dialogflow.reader`

   * `roles/discoveryengine.viewer`

   * `roles/iam.securityReviewer`

   * `roles/agentregistry.editor`

   * `roles/dialogflow.admin`

   * `roles/discoveryengine.editor`

   * `roles/CloudAgentVertexActions`

   * `resourcemanager.projects.setIamPolicy`

8. Click **Next**.

9. Paste the full contents of your GCP **Service Account JSON**, then click **Next**.

10. Review the summary, then click **Add Connection**.

You can now validate that the connection is active in the **Active Applications** tab.

---

---
title: Creating users and groups for Agent Privilege
description: Create the groups and users for your Agent Privilege evaluation and grant them access to PingOne Privilege.
component: privilege
page_id: privilege:agent-privilege:getting-started/users-and-groups
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/getting-started/users-and-groups.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 22, 2026
section_ids:
  before-you-begin: Before you begin
  create-groups-and-assign-roles: Create groups and assign roles
  result: Result:
  result-2: Result:
  result-3: Result:
  result-4: Result:
  create-users-and-add-to-groups: Create users and add to groups
  configure-access-to-pingone-privilege: Configure access to PingOne Privilege
  result-5: Result:
  result-6: Result
  next-steps: Next steps
---

# Creating users and groups for Agent Privilege

Create the groups and users for your Agent Privilege evaluation, then grant the groups access to the PingOne Privilege application.

## Before you begin

* Ensure you've completed [Starting a trial and setting up your environment](starting-a-trial.html).

## Create groups and assign roles

PingOne Privilege uses the PingOne environment you created for this evaluation as a directory for the users and groups that access the PingOne Privilege console.

Create at least two groups for PingOne Privilege:

1. In the PingOne admin console sidebar, click the Ping Identity logo to open the **Environments** page.

2. Select the environment you created for the Agent Privilege evaluation, then click **Manage Environment**.

   ### Result:

   You're directed to the **Groups** page in PingOne.

3. Create a group for admins:

   1. Click the **Plus** icon (**[icon: plus, set=fa]**).

   2. Enter a **Name** for the group, such as `PingOne Privilege Admins`.

   3. (Optional) Enter a **Description** for the group.

   4. Click **Save**.

      ### Result:

      The group for admins is created in PingOne and its details panel opens.

   5. Click the **Roles** tab in the details panel.

   6. Click **Grant Roles**.

   7. In the list, select the **PingOne Privilege Administrator** role.

      ### Result:

      Any user you add to this group is automatically granted admin permissions.

   8. Click **Save**.

4. Create a group for users:

   1. Click the **Plus** icon (** [icon: plus, set=fa]**).

   2. Enter a **Name** for the group, such as `PingOne Privilege Users`.

   3. (Optional) Enter a **Description** for the group.

   4. Click **Save**.

      ### Result:

      The group for users is created in PingOne.

## Create users and add to groups

Create an admin user to access the PingOne Privilege admin console for the first time.

1. In the PingOne admin console, go to **Directory > Users**.

2. Click the **Plus** icon (**[icon: plus, set=fa]**).

3. Enter a **Username** for the user, such as `adminuser`.

4. In the **Email** field, enter the email address for the administrator who performs the initial onboarding tasks.

5. (Optional) Select **Require Email to be Verified** to ensure the email is correct for later setup tasks.

6. In the **Group** list, select the admin group you created earlier.

7. Choose an authentication method for the admin user:

   * Set a policy under **Authoritative Identity Provider**.

   * Enter a **Password**.

8. Click **Save**.

## Configure access to PingOne Privilege

Now that you've created an admin group and added a user with the admin role to it, you need to enable access to PingOne Privilege for the admin group.

1. In the PingOne admin console, go to **Applications > Applications**.

2. In the list of applications, click **PingOne Privilege**.

   ### Result:

   The overview page for the PingOne Privilege application opens.

3. Click the **Access** tab and click the **Pencil** icon ([icon: pencil, set=fa]).

4. In the **Groups** list, select the checkboxes for the admin and user groups you created earlier. Click **Save**.

### Result

You now have the necessary users, groups, and permissions configured to onboard users to the admin console.

### Next steps

After you set up necessary users, groups, and permissions, you're ready to install the Endpoint Controller and use it to access the PingOne Privilege admin console.

Continue with [Installing the Endpoint Controller and accessing the admin console](onboarding-endpoint-controller.html).

---

---
title: Deploying the node sensor
description: Deploy the Privilege node sensor on Kubernetes or Docker hosts to discover agents, model servers, and MCP servers in your containers.
component: privilege
page_id: privilege:agent-privilege:configuration/node-sensor
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/configuration/node-sensor.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 21, 2026
section_ids:
  deploying-the-sensor-on-kubernetes: Deploying the sensor on Kubernetes
  before-you-begin: Before you begin
  registering-the-sensors-identity: Registering the sensor's identity
  installing-the-sensor: Installing the sensor
  verifying-the-deployment: Verifying the deployment
  deploying-the-sensor-on-a-docker-host: Deploying the sensor on a Docker host
  before-you-begin-2: Before you begin
  node-sensor-register-host: Registering the host identity
  result: Result:
  running-the-sensor-container: Running the sensor container
  next-steps: Next steps
---

# Deploying the node sensor

The PingOne Privilege node sensor is an eBPF sensor that observes the AI workloads running in your containers. One sensor runs on each Linux node. A host-based security tool cannot see inside a container because the process namespace is isolated from the host. The sensor observes process execution and network activity at kernel observation points and attributes every finding to the pod or container that produced it.

The sensor discovers the following workloads:

* AI agents and agent frameworks, recognized from their binaries, runtime catalogues, and startup arguments.

* Self-hosted model servers listening on conventional inference ports.

* MCP servers, detected by correlating a process with the port it later listens on.

* The model endpoints each workload calls, identified from the unencrypted handshake (TLS SNI and JA4, or the HTTP host header). No TLS is terminated and no traffic is decrypted.

* Workloads with no recognizable name, characterized by the AI SDKs and credential environment variables installed for them.

## Deploying the sensor on Kubernetes[]()

On Kubernetes *(tooltip: \<div class="paragraph">
\<p>An open-source system for automating deployment and management of containerized applications.\</p>
\</div>)*, the sensor runs as a DaemonSet with one pod per node, installed with Helm. The cluster's OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* provider issues the sensor's identity, and PingOne Privilege verifies it.

### Before you begin

Ensure you have the following:

* Helm 3 installed on your workstation.

* Your cluster's OIDC issuer URL.

* A workload identity registered in PingOne Privilege for the sensor. Learn more in [Registering non-human identities](non-human-identities.html).

### Registering the sensor's identity

The sensor proves its identity with a short-lived service-account token. You register a workload identity in PingOne Privilege naming the cluster's issuer and the sensor's service account. The kubelet mints a token for the registered audience and mounts it in the pod, and the sensor presents it with every report.

To register the identity, follow the Kubernetes option in [Registering non-human identities](non-human-identities.html#kubernetes), with the following settings:

* **Token issuer type**: **Kubernetes - ServiceAccount Token**.

* **Issuer (iss)**: Your cluster's OIDC issuer URL.

  To get the issuer URL, run the following command:

  ```bash
  $ kubectl get --raw /.well-known/openid-configuration | jq -r .issuer
  ```

* **ServiceAccount**: Either a new service account, which the sensor installation creates, or an existing one, entering the **namespace** and **serviceaccount** exactly as they exist in the cluster.

* **Permissions**: A sensor that reports findings only needs the **shadowai:write** permission.

* **Audience**: PingOne Privilege generates the audience at registration. Copy it into the Helm installation's `auth.audience` value.

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | The registered subject must match the deployed namespace and service account exactly. A mismatch is refused rather than mis-attributed. |

If your cluster runs SPIFFE with SPIRE, the same chart accepts a SPIFFE identity instead, so the sensor joins the trust domain you already operate. Register the identity with the SPIFFE / SPIRE token source and name it in the Helm installation.

### Installing the sensor

To install the PingOne Privilege node sensor, run the following command:

```bash
$ helm install procyon-nodesensor \
   oci://public.ecr.aws/v2s2h8i9/procyon-nodesensor-chart --version 0.1.14 \
   --namespace <your-namespace> --set-string clusterID=<your-cluster> \
   --set-string serviceAccount.name=<your-service-account> \
   --set-string auth.audience=<audience-from-console> \
   --set controller.enabled=true \
   --set-string controller.endpoint=<your-privilege-endpoint>:443
```

The command options are:

* `clusterID=<your-cluster>`: A name that identifies your cluster in PingOne Privilege.

* `serviceAccount.name=<your-service-account>`: The service account the chart deploys. This must match the registered subject.

* `auth.audience=<audience-from-console>`: The audience generated when you registered the identity.

* `controller.endpoint=<your-privilege-endpoint>:443`: Your PingOne Privilege controller endpoint.

The chart creates the following:

* A namespace and service account, or you point the chart at ones you manage.

* Read-only role-based access control (RBAC) *(tooltip: \<div class="paragraph">
  \<p>Also known as non-discretionary access control, this authorization strategy bases user access on assigned roles.\</p>
  \</div>)*: `get`, `list`, and `watch` on pods, services, and endpoint slices.

* A DaemonSet with one pod per node and the projected service-account token on a memory-backed volume.

* A security context that is not privileged, with escalation disabled, all capabilities dropped except the two that eBPF needs, and read-only root and `/sys` filesystems.

The sensor re-reads the projected token file with every report, so token rotation is picked up automatically.

### Verifying the deployment

```bash
$ kubectl -n <your-namespace> rollout status ds/procyon-nodesensor
```

```bash
$ kubectl -n <your-namespace> logs -l app.kubernetes.io/name=procyon-nodesensor-chart --tail=20
```

## Deploying the sensor on a Docker host[]()

On a Docker host there are no pods, so the sensor attributes each workload to its container. The container name is used wherever a pod's namespace would go. A rule naming `ollama-prod` matches the container called `ollama-prod`; nothing in the policy model changes.

### Before you begin

* A supported Linux Docker host.

* Your PingOne Privilege controller endpoint.

* A workload identity registered in PingOne Privilege for the sensor. Learn more in [Registering non-human identities](non-human-identities.html).

### Registering the host identity

A Docker host has no issuer such as the Kubernetes kubelet, so the host holds a signing key and issues its own tokens. The public half of the key is registered on the identity, which makes the tokens verifiable. Each host receives its own key, created readable only by its owner.

The audience does not exist until you register the identity: create the key first, receive the audience from the console after registration, and then start the sensor with it.

1. On the Docker host, create the signing key and generate the registration values by running the following command:

   ```bash
   $ docker run --rm -v /etc/procyon:/etc/procyon \
   public.ecr.aws/v2s2h8i9/procyon-nodesensor -mint-jwks -cluster <your-cluster>
   ```

   ### Result:

   If a signing key doesn't exist, the command creates one and returns the **Issuer**, **Subject**, and **JWKS** information to use for NHI configuration.

2. To register the identity, follow [Registering non-human identities](non-human-identities.html#docker), with the following settings:

   * **Token issuer type**: **Docker Host - Self-Signed Token**.

   * Paste the **Issuer (iss)**, **Subject (sub)**, and **JWKS URL** generated from the Docker command.

   * **Permissions**: A sensor that reports findings only needs the **shadowai:write** permission.

   * **Audience**: PingOne Privilege generates the audience at registration. Copy it into the sensor container's `-mint-audience` flag.

### Running the sensor container

```bash
$ docker run -d --name procyon-nodesensor --restart=always \
   --pid=host --cgroupns=host \
   --cap-drop=ALL --cap-add=BPF --cap-add=PERFMON --cap-add=KILL \
   --cap-add=NET_ADMIN --cap-add=SYS_PTRACE --cap-add=SYS_ADMIN \
   --security-opt apparmor=unconfined \
   -v /sys:/sys:ro \
   -v /var/lib/docker/containers:/var/lib/docker/containers:ro \
   -v /etc/procyon:/etc/procyon:ro \
   <registry>/procyon-nodesensor:latest \
     -docker -node "$(hostname)" -cluster <host-label> \
     -controller <your-privilege-endpoint>:8610 \
     -mint-audience <audience-from-console>
```

The command flags are:

* `-docker`: Runs the sensor on a Docker host rather than in a cluster.

* `-node <hostname>`: The host name of the node running the sensor.

* `-cluster <host-label>`: A label that identifies this host in PingOne Privilege.

* `-controller <your-privilege-endpoint>:8610`: Your PingOne Privilege controller endpoint.

* `-mint-audience <audience-from-console>`: The audience returned when you registered the identity.

The container mounts give the sensor a read-only view of the host's system state, container metadata, and its own configuration directory.

Hosts with a stricter policy can run the sensor without the following capabilities. The sensor still discovers and reports, and it reports what it has given up.

| Capability            | Needed for                                       | Cost of dropping it                                                           |
| --------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------- |
| `NET_ADMIN`           | The outbound connection filter.                  | A rule that denies a connection terminates the workload instead.              |
| `SYS_PTRACE`          | Reading another process's details.               | You lose idle-workload detection and binary-path classification.              |
| `SYS_ADMIN`           | Entering a workload's network namespace.         | The sensor cannot probe servers on networks it cannot otherwise route to.     |
| `AppArmor unconfined` | Making the two preceding capabilities effective. | On AppArmor hosts the capabilities are held, but the reads are still refused. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The sensor identifies listening servers by connecting to them. If the sensor does not share a network with the workloads it monitors, those servers cannot be identified by name. Execution and destinations are still detected, but name-based identification is weaker. Connect the sensor to the workload network or run it on the host network, and the sensor logs the condition explicitly. |

## Next steps

After the sensor reports, review the workloads it discovers on the **AI Security > Self-Hosted Agents** dashboard. Learn more in [Discover and manage NHI agents](../use-cases/nhi-agents.html).

---

---
title: Discover agents running on a workstation
description: Turn on personal agent discovery and review the first agents found on your onboarded workstation.
component: privilege
page_id: privilege:agent-privilege:getting-started/discover-agents
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/getting-started/discover-agents.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 22, 2026
section_ids:
  before-you-begin: Before you begin
  enable-discovery-for-personal-agents: Enable discovery for personal agents
  review-your-first-discovery-results: Review your first discovery results
  next-steps: Next steps
---

# Discover agents running on a workstation

After the Endpoint Controller is installed and onboarded, enable discovery for personal agents in the PingOne Privilege admin console. Discovery then automatically finds the personal agents operating on the desktops where the Endpoint Controller is deployed, so you can see and govern them.

## Before you begin

Ensure the following:

* You've completed [Starting a trial and setting up your environment](starting-a-trial.html).

* You've [created the necessary users, groups, and permissions](users-and-groups.html).

* You've installed the Endpoint Controller and it reports a `Connected` status. Learn more in [Installing the Endpoint Controller and accessing the admin console](onboarding-endpoint-controller.html).

* You can access the PingOne Privilege admin console as an administrator.

## Enable discovery for personal agents

One of the quickest use cases to implement for Agent Privilege is discovery for personal agents. The Endpoint Controller finds any personal agents running in your environment and provides an inventory that you can audit and govern.

1. In the PingOne Privilege admin console, go to **Settings**.

2. Click the **Personal Agents** tab.

3. Ensure that **Discover personal agents** is **Enabled**. If it's **Disabled**:

   1. Click **Edit**.

   2. Click the **Discover personal agents** toggle to the right (blue).

   3. Click **Save Changes**.

## Review your first discovery results

After discovery is enabled, give the Endpoint Controller time to scan the workstation, then review what it finds:

1. In the PingOne Privilege admin console, go to **AI Security > Personal Agents**.

   Your **Personal Agents** dashboard provides an overview of all AI agents and local LLMs detected across managed devices.

2. Click the tabs to review different findings:

   * **Users**: A list of users using agents.

   * **Agents**: Discovered personal agents, including their users and associated device, and when the agent was last seen.

   * **LLMs**: Discovered LLMs, including their users and associated device, and when the LLM was last seen.

   * **MCPs**: Discovered MCP servers, including their type, the URL or command used, their users and associated device, and when the MCP was last seen.

   * **Graph**: Select a discovered personal agent to view its graph.

3. Open a personal agent or MCP server on your test workstation and investigate the finding.

If no agents appear, confirm that the Endpoint Controller is running and connected, then run an agent on the workstation and wait for the next discovery cycle. Learn more in [Discover and manage personal agents](../use-cases/personal-agents.html).

## Next steps

Your evaluation environment is up and running with Agent Privilege. Continue with [Configure Agent Privilege](configure-agent-privilege.html).

---

---
title: Discover and manage NHI agents
description: AI Discovery for NHI agents finds non-human identity agents operating in your environment and helps you govern them.
component: privilege
page_id: privilege:agent-privilege:use-cases/nhi-agents
canonical_url: https://docs.pingidentity.com/privilege/agent-privilege/use-cases/nhi-agents.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 21, 2026
page_aliases: ["agent-privilege:use-cases/ai-discovery-nhi-agents.adoc"]
section_ids:
  how-the-pieces-fit-together: How the pieces fit together
  before-you-begin: Before you begin
  nhi-agents-discovery: NHI agents discovery
  creating-a-node-policy: Creating a node policy
  result: Result:
  managing-node-policies: Managing node policies
---

# Discover and manage NHI agents

{p1priv-ai-discovery} for non-human identity (NHI) agents finds the AI workloads running in your containers and helps you govern them. The PingOne Privilege node sensor observes these workloads, and PingOne Privilege both inventories them and enforces policy on them.

Discovery does not require every AI workload to be registered as an NHI before the sensor can find it. The sensor identity must be registered so the sensor can authenticate to PingOne Privilege. Register a workload identity separately when you need to associate the workload with that identity or match it in identity-based policy. Learn more in [Registering non-human identities](../configuration/non-human-identities.html).

## How the pieces fit together

The workflow is:

1. Register a non-human identity for the sensor itself. Learn more in [Registering non-human identities](../configuration/non-human-identities.html).

2. Deploy the sensor on your Kubernetes *(tooltip: \<div class="paragraph">
   \<p>An open-source system for automating deployment and management of containerized applications.\</p>
   \</div>)* clusters or Docker hosts. Learn more in [Deploying the node sensor](../configuration/node-sensor.html).

3. Review the discovery findings on the **Self-Hosted Agents** dashboard.

4. Configure NHI agent policy for the sensor to enforce.

## Before you begin

To discover and manage NHI agents, ensure you have the following:

* A non-human identity registered in PingOne Privilege for the sensor, so the sensor can authenticate its reports. Learn more in [Registering non-human identities](../configuration/non-human-identities.html).

* The node sensor deployed on your Kubernetes *(tooltip: \<div class="paragraph">
  \<p>An open-source system for automating deployment and management of containerized applications.\</p>
  \</div>)* clusters or Docker hosts. Learn more in [Deploying the node sensor](../configuration/node-sensor.html).

* For identity-based policy, the non-human identities your agents use registered in the directory. Learn more in [Registering non-human identities](../configuration/non-human-identities.html).

## NHI agents discovery

![The NHI Agents dashboard showing identities, workloads, agents, LLMs, and MCPs count tiles, the AI types breakdown, and the top workloads list.](../_images/p1p_nhi_agents_dashboard.png)

To review what discovery finds for NHI agents:

1. In the PingOne Privilege admin console, go to **AI Security > Self-Hosted Agents**.

   Your **Self-Hosted Agents** dashboard provides an overview of the agents operating under non-human identities in your environment.

2. Review the overview. The dashboard shows the following:

   * What discovery found, including:

     * The number of registered identities reporting

     * The workloads observed

     * The agents, LLMs, and MCP servers discovered

   * The time of the most recent detection and the sensor instance that produced it.

   * The share of each AI type among the findings, and the workloads with the most findings.

3. Explore the other tabs in the dashboard:

   * The **Identities** tab displays the non-human identities registered in PingOne Privilege.

   * The **Agents**, **LLMs**, and **MCPs** tabs show what has been discovered for each kind of workload. Each finding gives the classification of the workload and attributes it to the pod or container that produced it:

     * AI agents and agent frameworks observed running in your containers.

     * MCP servers, detected from process execution and the port the process listens on.

     * Self-hosted model servers listening on inference ports.

     * The model endpoints each workload calls, identified from the unencrypted handshake. No TLS is terminated and no traffic is decrypted.

   * The **Policies** tab lists the policies you configured.

4. Investigate findings to decide what remediation actions to take.

## Creating a node policy

Create policies to govern the AI workloads in the **Policies** tab on the **Self-Hosted Agents** page.

|   |                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can also create policies for specific NHI agents found in the **Agents**, **LLMs**, and **MCPs** tabs. Creating a policy for an agent in the list populates the fields specific to the agent you're configuring a policy for. |

1. In the PingOne Privilege admin console, go to **AI Security > Self-Hosted Agents**.

2. Click the **Policies** tab.

3. Click **Create Node Policy**.

4. Enter a **Name** and **Description** for the policy.

5. Select the entities the policy applies to:

   * **Agents**

   * **Local models**

   * **MCP servers**

     |   |                                                            |
     | - | ---------------------------------------------------------- |
     |   | If you don't select any, the policy applies to every kind. |

6. Click **Next**.

7. Create one or more **Matches** for the policy to apply to:

   * **Name**: Process name on execution. An interpreted agent is named by its script and interpreter.

   * **Process path**: Full path of the binary, which is never truncated. Select this option when several programs share one process name.

   * **Host**: Where the workload connects to, read from the TLS handshake.

   * **Tool**: A tool an MCP server advertises when probed.

   * **Identity key**: What the software was identified as, whatever the process is called.

8. Click **Next**.

9. Configure the identities for the policy:

   1. In the **Token issuer type** list, select the platform the policy is for.

   2. In the **Non-human identities** list, select the hosts the policy reaches through those identities. Leave empty to deliver this policy to every reporting identity.

10. Review the **Summary** for the policy.

11. In the **Namespace** list, select an option for which namespaces the policy applies to:

    * **All namespaces**: The policy reaches every node and matches nothing.

    * **Named namespaces**: A node checks the namespace before acting. Enter the specific Kubernetes namespaces in the text field.

12. Select an action for the policy:

    * **Monitor**: Reports the process and doesn't take any action.

    * **Allow**: Exempts it from a broader deny.

    * **Warn**: Reports a warning, but the process still runs.

    * **Deny**: Terminates the process when it starts.

13. For policy state, you can either:

    * Leave the policy **Enabled** by default, which enacts the policy when it's created.

    * Click the policy toggle to the left (gray) to disable it (**Disabled**). The policy appears in the list of policies, but delivers no actions to nodes.

14. Click **Create Policy**.

    ### Result:

    The policy appears in the list of policies.

### Managing node policies

1. In the PingOne Privilege admin console, go to **AI Security > Self-Hosted Agents**.

2. Click the **Policies** tab.

3. In the list, find the node policy you want to manage.

4. (Optional) From the list, you can either:

   * Click **Edit** to view and change any of the node policy configuration fields.

   * Click **Delete** to delete the policy.