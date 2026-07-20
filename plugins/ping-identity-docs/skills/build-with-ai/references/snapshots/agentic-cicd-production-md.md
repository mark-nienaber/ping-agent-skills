---
title: Managing Production Environments
description: How AI agents manage CI/CD pipelines to promote Ping Identity configuration safely into production environments.
component: build-with-ai
page_id: build-with-ai::agentic-cicd-production
canonical_url: https://developer.pingidentity.com/build-with-ai/agentic-cicd-production.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2026
keywords: ["agents", "agentic", "CI/CD", "production", "pipeline", "GitOps", "config as code", "governance", "audit"]
section_ids:
  the-governance-model: The governance model
  what-agents-do: What agents do
  config-as-code-and-gitops: Config-as-code and GitOps
  execution-layer: Execution layer
  example-scenario: Example scenario
---

# Managing Production Environments

In production environments, due to their non-deterministic nature, agents directly managing production environments is highly discouraged. Instead, agents can operate CI/CD pipelines; triggering runs, monitoring status, retrying failed deployments, and promoting configuration across environments. The pipeline, not the agent, applies changes to production, through review gates that keep configuration under human oversight. Agents can also be embedded within the CI/CD process to augment the process.

|   |                                                                                |
| - | ------------------------------------------------------------------------------ |
|   | This is consistent with existing industry best practices for CI/CD and GitOps. |

The difference is that administrators are delegating the **operation** of the pipeline to an agent, not the **governance** of it. The role of agents is to assist with automation of promotion, but modification of production systems should remain deterministic.

|   |                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Coding agents can also be used to assist in the development process, creating or modifying configuration-as-code. For more information, refer to [Agentic Development](agentic-development-environments.html). |

## The governance model

![agentic-cicd-production-governance](https://kroki.io/plantuml/svg/eNp1Uk1v2zAMvftXEN1hK5Y1p-7QwwDP6bYAxWBkPfbCSrQjVJY0WkqTfz9KDlKnaynAEMT3Hj-exyfjAjIOoKnDZOM97WNtTe8GchGUfIir8YSqmf1z461n-HBdYpZskaNRJqCL31E99eyT00fwjxLvgD1r4iOwLjED_vaR3pJrbr--Rs11VhJnOn_obyKn6KfohP8Fr_N5Fz5XbkpUVXiZAC7qNdS9bOsCcATMt_N8s142K2hNIGscFZQySr8CedeZHja0M_T84D5p03XwGXqMdFkoXDLnpNs9qRSNd3CHB2KhNXdrWMI9MWPneZio0Xt7TmyN66G1GDNIaIG9TiorTYwg-aoqs8CXb6VduIHIpu-JgZN7cEsYvDNRtjJGjGnML0yRD9ChsYmpKixhT50LX6oEPxKoLbqepCztg-e4gHazgGDRXVZHrLBy08LBIKwd6XKzh6o8Szp3OEkOYj-osr7EmGeoKpffhMaTH4tp4TD5BD6QAEkWsyURmny5OqW1p9F9jLD1VsPLZkAxackbtONVRU5DrjKvdbQI4Fca0IGsBlP0g5TSxchcYpV9NSPszGgeLcEjiQU0Dfe2avFCekvaxJtTuzAS74wSplLyL8es3ZS9ZvXIqAizfvRlynYzE_8Ha99i9w==)

The agent has pipeline credentials, enough to trigger and query runs, but not direct write access to production Ping Identity environments. Configuration changes travel through the pipeline, where they can be reviewed, validated, and rolled back through standard version control.

## What agents do

Agents in this pattern handle the operational layer of the pipeline:

* **Triggering runs**: the agent initiates a pipeline run after a configuration change is committed or merged.

* **Monitoring status**: the agent polls or subscribes to pipeline events, watching for success or failure.

* **Retrying failures**: if a deployment fails due to a transient error, the agent retries the run without requiring human intervention for routine retries.

* **Promoting configuration**: the agent triggers a promotion pipeline to advance configuration from staging to production after a successful staging run.

|   |                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Under this model, agents never deploy configurations directly to production. When integrating agents into existing CI/CD workflows (such as code reviews, pipeline definitions, or infrastructure management) implementing strict guardrails is essential to maintain robust governance. |

## Config-as-code and GitOps

Configuration is expressed as files in a Git repository; exported snapshots, declarative state definitions, or both. This applies regardless of which execution layer the pipeline uses.

The pattern is the same in each case:

1. Configuration is authored or exported as files in a Git repository.

2. A pull request or merge triggers the CI/CD pipeline.

3. The pipeline validates the proposed change (a diff, a plan, or a promotion dry-run).

4. A human or automated review gate approves or rejects the change.

5. On approval, the pipeline applies the change to the target environment.

This approach reduces the risk of agent errors reaching production. The agent may propose configuration changes, but those changes go through a diff review and a CI gate before they are applied. The pipeline has the keys, not the agent.

|   |                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Always review pipeline-triggered configuration changes before approving a merge. An agent can construct plausible-looking configuration that contains subtle errors. The review gate is the primary mitigation. |

## Execution layer

The execution layer, the tool that actually applies configuration to Ping Identity environments, is separate from the agent and separate from the pipeline orchestration.

**Ping CLI** handles imperative operations: exporting configuration snapshots, running promotion commands between environments, and querying current state.

**Terraform** handles declarative state: expressing the target configuration as `.tf` files and reconciling the current environment to match.

Both can operate in the same pipeline. See [Ping CLI in CI/CD pipelines](pingcli/cicd-and-production.html) and [Terraform for Ping Identity configuration](terraform/overview.html) for tool-specific setup and usage.

## Example scenario

An agent monitoring a production environment detects elevated authentication error rates and failed health checks consistent with an outage.

1. The agent triages the incident: querying logs for error patterns, reviewing traffic metrics to establish a timeline, comparing recent pipeline changes against a known-good reference environment to identify configuration drift.

2. The agent determines that a misconfigured deployment is the likely cause and invokes the CI/CD pipeline to re-deploy the last known-good configuration.

3. The pipeline applies the change through the standard review gate and promotes the rollback to production.

4. The agent re-queries the observability signal to confirm recovery.

At no point does the agent hold production credentials or make changes to the Ping Identity platform directly. This way, the rollback activity was fully deterministic. The audit trail runs through the pipeline, not the agent. This is why it is important to use deterministic tools at the execution layer, such as Ping CLI and Terraform and not MCP servers.