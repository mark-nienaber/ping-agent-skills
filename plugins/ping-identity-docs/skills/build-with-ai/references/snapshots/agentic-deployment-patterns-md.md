---
title: Agentic Deployment Patterns
description: How to use AI agents safely and effectively against Ping Identity platforms, across three distinct deployment patterns.
component: build-with-ai
page_id: build-with-ai::agentic-deployment-patterns
canonical_url: https://developer.pingidentity.com/build-with-ai/agentic-deployment-patterns.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2026
keywords: ["agents", "agentic", "deployment", "patterns", "CI/CD", "MCP", "Terraform", "Ping CLI", "governance", "audit"]
section_ids:
  pattern-1-data-management: "Pattern 1: Data management"
  pattern-2-environment-monitoring: "Pattern 2: Environment monitoring"
  pattern-3-environment-configuration: "Pattern 3: Environment configuration"
  development-and-sandbox: Development and sandbox
  production: Production
  where-to-go-next: Where to go next
---

# Agentic Deployment Patterns

AI agents can interact with Ping Identity platforms in fundamentally different ways depending on what they are doing and what environment they are operating in. Choosing the wrong pattern for the task creates governance and audit risk: an agent that is appropriate for a sandbox can cause real harm if pointed at production.

This page introduces the three patterns and guides you to the right one.

![agentic-deployment-patterns-overview](https://kroki.io/plantuml/svg/eNqVVE2P2jAQvedXjOilewC0qbYHDpXSsFWRoEJdjkgrrz0EC8cTOYbdVdX_3rFDIHRTqh0khMdv3rz5wPVO20o4UYKksiKL1j_4V4PgUHphC4NJfYIo3Ii98St88ZnRhS0ZDZK_0HVQmXP0nJMhBx_uonUu8zbLVyF3haO9VUfot2i9UHIK3RGWRevAlkwkCnzLdxc-PcAuWx6tA_pBHvuk5fef_0Z1eaZsrCoR0vNxkM0gK1j5AEQNIvxKkqpJD4Ol8NwwC7drOxVewEJY9pcR_iuB8yBgsMiX8IDugC4ylbK6vQQstS1gaYTfkCvX9mPlSO2l12RvYkTF9yEkRMJw-OXo-N0jJ13be3vQjpqxLshqroXhV1RxRodCDcma15tWYtojMZ_P3mKl0en7y0mbctJTOZGDqTqOvvo-XdaXk93oYu9EYL9a4hjaEqIGhQdPZOrrymth1RO9nGU_ctxlSD4b51PmrtBoi01HtFT_6t4YVuicCPxt997fvMfg5LC2iFPPgjyYBD8aqkKHAjnLiYhjLqPP-EjEfY7bHd1xOy-OaecYh30-ngRc5uzgQ-4JnItIEsv_Ongi76kE2px2-_tsNQdRMfIgDHDx7NvqYjt0ut4BVdjMuB4laBUEkl6qsEY_2wUdwZyeIRCM2J3tlfYTqHkhtEQQUvLj4P_D17Y6PgSgnD5gmEEz7cDaTj5oN5ov5ZYfXOzq_APy2eUL)

## Pattern 1: Data management

In this pattern, agents perform user-oriented operations against identity data:

* Resetting passwords

* Unlocking accounts

* Retrieving profile information

* Processing identity verification requests

Agents in this pattern typically operate through MCP servers, which provide controlled, scoped access to platform APIs.

|   |                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------- |
|   | Because these operations affect real users, high-risk actions require human-in-the-loop (HITL) approval before the agent proceeds. |

|   |                                                                          |
| - | ------------------------------------------------------------------------ |
|   | It is important to trust the inference provider as data may include PII. |

In development and test environments, identity data is synthetic and doesn't represent real individuals, so HITL is not required. Agents can access data through MCP servers or Ping CLI, whichever is available in the harness.

## Pattern 2: Environment monitoring

In this pattern, agents observe and report on the health of live environments: querying audit logs, watching for anomalies, and surfacing failed authentication events.

Monitoring agents are generally read-only and carry lower risk than configuration agents. They can operate directly against production using **read-scoped** credentials. The AIC MCP Server and DaVinci MCP Server both support this pattern through their logging and diagnostic tools.

Agents can integrate with established logging, Security Information and Event Management (SIEM), and alerting platforms rather than act as the alert mechanism themselves:

* Splunk

* Datadog

* Elastic

* PagerDuty

When an agent detects an issue, it acts through those platforms: enriching an existing alert, opening an incident, or surfacing findings to an on-call workflow. The authoritative source for alerts remains your observability stack.

|   |                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Agents can also be invoked as a result of a webhook or alert trigger initiated by the Ping platform (where available). In this scenario, an agent may be invoked based on a change in platform state, and can use its defined access with MCP or CLI tools to perform further investigation. |

In development and sandbox environments, agents may query platform logs and diagnostics more directly because the risk of false positives is lower. The same principle applies: treat the existing observability stack as the source of truth, and do not route synthetic alerts through production incident management systems.

## Pattern 3: Environment configuration

In this pattern, agents read and change identity platform configuration: creating journeys, modifying flows, updating policies, exporting and promoting configuration across environments.

This is the highest-risk pattern because misconfigured identity infrastructure affects all users and services that depend on it. The right approach depends on the environment.

### Development and sandbox

In development and sandbox environments, where the impact of misconfiguration is low (and data is fully synthetic), agents can interact with Ping Identity platforms directly using MCP servers or Ping CLI.

MCP servers provide the native agent integration to Ping platforms and provide a rich set of tools that agents can use to manage configuration within those environments.

The Ping CLI may be used in agent sandboxes where MCP servers may not be available, or the agent may be running in a headless harness outside an IDE session. The CLI's composable command structure is natively understood by LLMs, and the CLI manages authentication so the agent inherits whatever authorization has been granted to it.

See [Agentic development environments](agentic-development-environments.html) for guidance on tool selection, authentication delegation, and OAuth client recommendations for headless harnesses.

### Production

In production environments, given the non-deterministic nature of agents and LLMs, do not use agents to configure environments directly. Instead, agents work best when operating deterministic CI/CD pipelines or as an intelligent step within them:

* Triggering pipeline runs

* Monitoring deployment status

* Retrying failed deployments

* Reviewing configuration changes

* Summarizing differences between environments

* Generating supporting documentation

The pipeline itself, not the agent, applies changes through a review gate that keeps configuration under strict governance (including human review, pre-defined checks and guardrails), and auditability of potentially harmful changes.

Ping CLI and Terraform both feed into this pattern. Ping CLI handles imperative operations and environment control. Terraform manages declarative configuration as `.tf` files in version control.

Refer to [Managing Production Environments](agentic-cicd-production.html) for the governance model, and [Terraform for Ping Identity Configuration](terraform/overview.html) for the Terraform execution layer.

## Where to go next

[icon: terminal, set=fas, size=3x]

#### [Development Environments](agentic-development-environments.html)

When direct agent access is appropriate, which tools to choose, and how authentication delegation works in development and sandbox environments.

[icon: code-branch, set=fas, size=3x]

#### [CI/CD and Production](agentic-cicd-production.html)

How agents manage CI/CD pipelines to promote configuration safely into production, with the review gate keeping changes under human oversight.

[icon: file-code, set=fas, size=3x]

#### [Terraform](terraform/overview.html)

Declarative infrastructure-level Ping Identity configuration as code, designed to run through governed pipelines rather than directly from an agent.