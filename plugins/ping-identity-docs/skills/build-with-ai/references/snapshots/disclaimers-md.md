---
title: Disclaimers and Limitations
description: Important disclaimers, warnings, and limitations to understand before using MCP servers, agent skills, and other AI tooling from Ping Identity.
component: build-with-ai
page_id: build-with-ai::disclaimers
canonical_url: https://developer.pingidentity.com/build-with-ai/disclaimers.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 9, 2026
keywords: ["disclaimers", "limitations", "security", "LLM", "AI", "MCP", "warnings"]
section_ids:
  data-privacy-and-llm-providers: Data privacy and LLM providers
  output-quality-and-model-variability: Output quality and model variability
  use-trusted-clients-and-agents-only: Use trusted clients and agents only
  non-production-environments: Non-production environments
---

# Disclaimers and Limitations

The MCP servers, agent skills, and other AI tooling on this site are powerful tools that interact directly with your Ping Identity environments. Before using them, understand the limitations and risks outlined here.

## Data privacy and LLM providers

|   |                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------- |
|   | All data returned from MCP tools might be sent to your LLM provider. Only use these tools with trusted MCP clients and AI agents. |

When an AI agent calls an MCP tool, the tool response (including any Ping Identity environment data it returns) is passed back to your AI agent as context. Depending on your AI agent and inference configuration, this data may be included in prompts sent to a third-party LLM provider.

This includes:

* User data and profile attributes

* Journey and flow definitions

* Application configurations and OAuth 2.0 client settings

* Logs and audit trail data

* Environment secrets and variables (where applicable)

Review the sensitivity of your environment data before using these tools with a third-party AI provider. Where possible, use non-production environments for development and testing.

## Output quality and model variability

Results vary based on the model you are using, the quality of your prompts, and the context available to the agent.

* **Different models produce different results.** A prompt that works well with one LLM may produce incomplete, incorrect, or unexpected output with another.

* **Agent skills improve grounding but do not guarantee accuracy.** Skills load domain expertise into the agent, but the agent still interprets that knowledge and can make mistakes.

* **Complex workflows require review.** For multi-step operations (such as creating journeys, modifying flows, or configuring applications), always review the output before applying it to a live environment.

|   |                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | AI-driven operations can make mistakes. Treat AI-generated configuration, code, and recommendations the same way you would treat any code review. Never promote AI-generated changes to production without reviewing them first. |

## Use trusted clients and agents only

Do not use Ping Identity MCP servers with untrusted MCP clients, agent code, or LLM inference endpoints.

MCP servers authenticate using your credentials and act on your behalf. An untrusted client could use that access to read sensitive environment data or, where write tools are enabled, make unintended changes to your Ping Identity environments.

## Non-production environments

Where possible, use a dedicated non-production or sandbox environment when:

* Evaluating MCP servers or agent skills for the first time

* Running agents in write mode

* Testing prompts and workflows before applying them to environments serving live identity and access requests