---
title: Ping CLI
description: Overview of Ping CLI, a command-line tool for scripting and automating Ping identity configuration in agentic development and CI/CD pipelines.
component: build-with-ai
page_id: build-with-ai:pingcli:overview
canonical_url: https://developer.pingidentity.com/build-with-ai/pingcli/overview.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2026
section_ids:
  role-in-the-ai-first-stack: Role in the AI-first stack
  deployment-contexts: Deployment contexts
  development-and-sandbox: Development and sandbox
  cicd-and-production: CI/CD and production
  agent-skills-for-ping-cli: Agent Skills for Ping CLI
  get-started: Get started
  full-documentation: Full documentation
---

# Ping CLI

[icon: circle-check, set=far]PingOne [icon: circle-check, set=far]DaVinci [icon: circle-check, set=far]Authorize [icon: circle-check, set=far]Credentials [icon: circle-check, set=far]MFA [icon: circle-check, set=far]Protect [icon: circle-check, set=far]Verify [icon: circle-check, set=far]PingFederate

Ping CLI is a cross-platform command-line tool for performing AI-first headless identity operations against Ping Identity services. It's the workflow execution layer: the piece that lets AI agents and developers automate, script, and promote identity configuration without opening a browser console.

Where MCP servers give your AI agent interactive, natural language access to Ping Identity platforms, Ping CLI handles repeatable, scriptable operations: running commands in CI/CD pipelines, promoting configuration across environments, and automating tasks that happen outside of an IDE session.

Ping CLI plays two distinct roles in agentic workflows depending on the environment:

* In **development and sandbox** environments, it gives agent harnesses a direct interface to Ping Identity platform APIs when MCP is not available, enabling rapid prototyping with full CLI-managed authentication.

* In **production** environments, the agent uses Ping CLI to export configuration from a development environment, creates a pull request against a config-as-code repository, and initiates the GitOps promotion workflow. The agent can then drive that workflow — triggering runs, monitoring status, and retrying failures. The pipeline itself invokes Ping CLI to apply configuration deterministically to the target environment. The agent never calls production APIs directly; the pipeline is the governance gate.

## Role in the AI-first stack

| Layer                     | Tool                               | Context                                                              |
| ------------------------- | ---------------------------------- | -------------------------------------------------------------------- |
| Discovery                 | Agent-ready docs and `llms.txt`    | All environments                                                     |
| Domain expertise          | Agent Skills                       | All environments                                                     |
| Interactive configuration | AIC MCP Server, DaVinci MCP Server | IDE sessions with MCP host available                                 |
| Workflow execution        | **Ping CLI**, Terraform            | Sandbox (direct); production (export → GitOps PR → pipeline applies) |

![pingcli-deployment-contexts](https://kroki.io/plantuml/svg/eNqdksFq3DAQhu9-isG5JJRkySE95BBwvQkshHYhPRaKIo2dIbJGyLKbtPS5eu-TdaT17prsQqBjbCzp0z-_ZtQ_k_MqqA40d54duvgQXy1CQB2Vay0W_Q4x2KjBxq_4EitLreuEBi0fDDOqCoF_1Gw5wMlVjtlivc3ySennNvDgzITe5TiKcjAYJqzKMcPWIqRaPNS7Ss8RcK5W55hBnzniMWv17ce31FxnKSGuCqWjDMtqBVUrzktQPaj0V-zqCeXNd1iTa6G-X2VAWyoKv3EH5RJHtOxzbRfwoJx55JcSfhWwbxGUSeCLw2_u9AMMjkYMvbLQYxhJY3-Wdf2lwfFw2x2KbxVxwzSJ-T3Lvw5sBh2JHZyOpKBeLerl2YGBPC3n8GjJbbQ0afM_Lr1kfNfmFpIccH5-M9u2m9kwcpZc8TyXSivvtEOOCtdgKPUCqvUKlBYb_Z5o3iNysmuIgdoWg_SnY0ep5QuQ5J1ci6Jw8oVHjpE74GbXBaNGcprg7x9QQ3ziQD8xDXSQg7pIyvZCdY1KkyIWkwX5laJR81qgM-CO6U9Vz_cN2Oea9RCfEPzUnAtZ3jYKlPeWEsApydTpi738P1wnY0g=)

## Deployment contexts

### Development and sandbox

In development and sandbox environments, an agent harness can use Ping CLI commands directly as tools. The CLI manages authentication to Ping Identity platform APIs, so the agent inherits whatever authorization has been granted to it, and can invoke commands without holding credentials directly.

This pattern supports rapid prototyping and is suitable for environments that are not subject to strict governance requirements.

Refer to [Using Ping CLI in development environments](agentic-development.html) for authentication delegation patterns, OAuth client recommendations for headless harnesses, and example operations.

### CI/CD and production

In production environments, Ping CLI is used alongside, or as an alternative to Terraform to feed configuration into a CI/CD pipeline. The agent triggers and monitors the pipeline; the pipeline applies changes to production after a review gate. The agent never holds production credentials, nor is it directly interacting with the live production instance configuration.

Refer to [Ping CLI with CI/CD pipelines](cicd-and-production.html) for the full governance model, config-as-code patterns, and a worked example.

## Agent Skills for Ping CLI

Ping CLI ships with its own [Agent Skills](https://agentskills.io) support. Installing a Ping CLI skill gives your AI coding assistant direct knowledge of available commands, subcommands, flags, and service connectors, so it can construct valid CLI invocations without trial and error.

|   |                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Agent Skills for Ping CLI are designed to be used for specific use cases relating to the CLI and are not included with the Ping Identity [agent plugins](../agent-skills/overview.html). |

You can install the "Ping CLI usage" skill, designed to reduce the need for agents to request and interpret `--help` output:

```console
pingcli agent-skills install pingcli-usage
```

After installation, your agent can reason about Ping CLI commands in context, alongside any active MCP tools or SDK skills.

## Get started

[icon: rocket, set=fas, size=3x]

#### [Install Ping CLI](https://developer.pingidentity.com/pingcli/latest/using_pingcli/getting-started.html)

Install Ping CLI and connect to your first Ping Identity service. The getting started guide walks you through installation, authentication, and your first command.

## Full documentation

The complete Ping CLI reference (installation, service connections, configuration profiles, command reference, and more) lives in the Ping CLI docs.

[Ping CLI documentation](https://developer.pingidentity.com/pingcli)

---

---
title: Ping CLI in CI/CD Pipelines
description: How Ping CLI operates as the execution layer in CI/CD pipelines for promoting Ping Identity configuration to production.
component: build-with-ai
page_id: build-with-ai:pingcli:cicd-and-production
canonical_url: https://developer.pingidentity.com/build-with-ai/pingcli/cicd-and-production.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2026
keywords: ["Ping CLI", "CI/CD", "production", "pipeline", "GitOps", "config as code", "governance", "promotion"]
section_ids:
  the-agents-role-vs-the-pipelines-role: The agent's role vs. the pipeline's role
  role-in-the-pipeline: Role in the pipeline
  authentication-in-a-pipeline-runner: Authentication in a pipeline runner
  full-documentation: Full documentation
---

# Ping CLI in CI/CD Pipelines

[icon: circle-check, set=far]PingOne [icon: circle-check, set=far]DaVinci [icon: circle-check, set=far]Authorize [icon: circle-check, set=far]Credentials [icon: circle-check, set=far]MFA [icon: circle-check, set=far]Protect [icon: circle-check, set=far]Verify [icon: circle-check, set=far]PingFederate

This page covers Ping CLI-specific usage in CI/CD pipelines: its role as the execution layer, how it authenticates in a pipeline runner, and the commands used for environment promotion.

For the broader governance model, why agents operate pipelines rather than production APIs, and how the review gate works, refer to [Agents in CI/CD and production environments](../agentic-cicd-production.html).

## The agent's role vs. the pipeline's role

In production workflows, Ping CLI is used at two distinct points:

1. **By the agent, against development environments**: the agent uses Ping CLI to export configuration from a development or sandbox environment, creates a pull request against a config-as-code repository, and initiates the GitOps promotion workflow. The agent can also drive the running pipeline: triggering runs, monitoring status, and retrying failures.

2. **By the pipeline, against production**: once configuration is merged and the pipeline is running, Ping CLI applies the configuration deterministically to the target environment. At this stage, the agent is not invoking Ping CLI directly; the pipeline is.

This separation keeps production changes under governance: the agent's non-deterministic reasoning is upstream of the review gate, not downstream of it.

**The pipeline is the authoritative, auditable execution layer**.

## Role in the pipeline

Ping CLI handles the imperative operations in the pipeline:

* **Exporting and applying configuration**: producing a snapshot of environment configuration as structured files for version control and through script, applying that configuration to alternate environments.

* **Promoting configuration**: applying configuration as code packages built from one environment to another using `pingcli` commands.

* **Querying current state**: introspecting an environment to confirm that a deployment succeeded and the live configuration matches expectations.

These are stateless operations. Ping CLI doesn't maintain a state file and doesn't reconcile drift, it executes what the pipeline instructs. For declarative state management, [Terraform](../terraform/overview.html) operates alongside Ping CLI in the same pipeline.

## Authentication in a pipeline runner

In a CI/CD pipeline runner, there is no human actor present. Ping CLI authenticates using a **client credentials grant** against a dedicated service account OAuth client.

The pipeline runner must have the following configured as environment variables or in a Ping CLI configuration profile:

* Client ID and client secret for the pipeline service account.

* The target environment's base URL.

* The required OAuth scopes for the operations being performed.

Don't use personal administrator credentials in pipeline runners. The service account must be scoped to the minimum permissions needed for promotion operations, and its credentials must be stored as secrets in the pipeline platform (not in source control).

|   |                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The pipeline service account should have write access only to the target environment for the specific pipeline stage it is running. A single service account with write access to all environments is a governance risk. Stage promotion pipelines; staging, pre-production, and production should each use a separate, scoped service account. |

## Full documentation

The complete Ping CLI reference: installation, service connections, configuration profiles, and the full command reference, refer to the [Ping CLI documentation site](https://developer.pingidentity.com/pingcli).

---

---
title: Using Ping CLI in Development Environments
description: Authentication delegation patterns and OAuth client setup for Ping CLI in agent harnesses.
component: build-with-ai
page_id: build-with-ai:pingcli:agentic-development
canonical_url: https://developer.pingidentity.com/build-with-ai/pingcli/agentic-development.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2026
keywords: ["Ping CLI", "agent harness", "development", "sandbox", "OAuth", "authentication", "audit", "client credentials"]
section_ids:
  authentication-delegation: Authentication delegation
  human-administrator-present: Human administrator present
  fully-automated-harness-no-human-actor: Fully automated harness (no human actor)
  full-documentation: Full documentation
---

# Using Ping CLI in Development Environments

[icon: circle-check, set=far]PingOne [icon: circle-check, set=far]DaVinci [icon: circle-check, set=far]Authorize [icon: circle-check, set=far]Credentials [icon: circle-check, set=far]MFA [icon: circle-check, set=far]Protect [icon: circle-check, set=far]Verify [icon: circle-check, set=far]PingFederate

This page covers Ping CLI-specific information for agentic development: how authentication is delegated from the agent to the CLI, and how to configure OAuth clients for development and headless harnesses.

For the broader concepts, when direct agent access is appropriate, which tools to choose, and how development differs from production, refer to [Agentic development environments](../agentic-development-environments.html).

## Authentication delegation

Ping CLI manages authentication to Ping Identity platform APIs. The agent invokes CLI commands; the CLI handles token acquisition, refresh, and the underlying API calls. The agent itself never holds credentials.

![pingcli-dev-auth-flow](https://kroki.io/plantuml/svg/eNqdU01v2zAMvetXEN2lPaQ7tYcAGeCl61qg6AJsx15YibaFyKIry9m6Xz9KcrKkHyhaBoghvcdH8tEe1tb3GLADQzWOLv6iP7FytvEd-Qha_iioYceqQuDfS3Yc4NNZjj1whSFabXv08SvqdRN49GYiX-Z4hczBUJiIVY494i1Heklu-e38KWtf50LiQOcnPYzkNX0Xnf654Fn6vUrfV17mUKr_PwEcVU3y6wqDp2E4AhwA080haWV9A8ub64xrZw_RH9UYW6kbNhQyg1EuXlBYOYw1B9nGqkhh_0SqGo2NcMNNgdNJqcUCrsYO_Yx7ChjJQFvahcVCqdwuzL6kvmAO1m94TaC5kwyj0qVguSNB80OzIWiCFLzz4ouhjdWUIQ72L0bLvsCqpO20UetUNUoBf-ePMcZg78fUUGRA01l_si0ok0mCzAkanVPpmG7zeHMIpGUx85ID1sgENj4q5eVlABYbp9EBiiFbfptsKFl2iOIFh1Mh3fLEAK4htlRWuHXpVJE3kKSzlZejc49pWu6yl5-hJTQuDfZhW-WYv7pAeRR0w9bfY1nZrGiV16RQT95nbc6filxfvNfkw-y3XX7ebjJ5-kTADtPCaov3jsDWgAIbMlZnQ6dKwhsHOfapTpNFdnv4B8sboXQ=)

### Human administrator present

When a human administrator is operating the agent harness, Ping CLI can authenticate using an **authorization code grant** or **device authorization grant**. The access token is issued on behalf of the administrator, so all API calls are audited against their identity in the Ping Identity platform audit logs.

The agent harness itself is not recorded in the audit log. The audit trail shows **what was done** and **by whom (the administrator)**, but not **that an agent was involved**.

This applies to interactive development and prototyping contexts where the administrator takes responsibility for the agent's actions and the risk of harm is negligible.

### Fully automated harness (no human actor)

When the CLI runs in a fully automated harness with no human actor present, for example, in a sandboxed agent or an automated test pipeline, authentication uses a **client credentials grant**. The access token is attributed to the OAuth client, not a person.

|   |                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Where possible, define a dedicated OAuth client for each agent, agent harness, or sandbox environment. Using a shared client makes it impossible to distinguish which agent or harness produced a given audit record. A per-agent client means audit logs can be reliably attributed to a specific agent or purpose, which is valuable for both debugging and governance. |

A client should be scoped to the minimum permissions needed for the agent's task. Prefer short token lifetimes and rotate client secrets regularly.

## Full documentation

The complete Ping CLI reference; installation, service connections, configuration profiles, and the full command reference is at the [Ping CLI documentation site](https://developer.pingidentity.com/pingcli).