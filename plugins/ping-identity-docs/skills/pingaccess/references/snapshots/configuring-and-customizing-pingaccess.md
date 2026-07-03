---
title: Agent inventory logging
description: To log details about your PingAccess agents, you can add custom configuration to the agents and to the PingAccess system.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_agent_inventory_logging
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_agent_inventory_logging.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2023
section_ids:
  agent-header: Agent Header
  example: Example
  example-2: Example
  example-3: Example
---

# Agent inventory logging

To log details about your PingAccess agents, you can add custom configuration to the agents and to the PingAccess system.

Agent information isn't included in agent responses by default, except for the agent's name. To include additional information in the logs, customize your PingAccess agents to include the agent header.

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must edit the `/conf/log4j2.xml` file to log the information included in the agent header. For more information, see [Security audit logging](pa_security_audit_logging.html). |

For information about agent headers, see [PAAP agent request](../agents_and_integrations/pa_ap_agent_request.html).

## Agent Header

The optional header `vnd-pi-agent` allows the agent to communicate information about itself and its deployment environment to PingAccess.

The value of this header is a map of comma-separated key-value pairs. An agent can either use the custom keys that are specific to its deployment, or use one or more of the following well-known keys:

> **Collapse: Well-known keys**
>
> * v
>
>   The version of the agent making the request.
>
> * t
>
>   The type of agent and/or the type of platform where the agent resides.
>
> * h
>
>   The hostname of the server where the agent resides.

The syntax for the `vnd-pi-agent` value conforms to a dictionary in this specification, <https://datatracker.ietf.org/doc/rfc8941/>, where member-values are constrained to be an `sh-string` item.

The following header examples are all considered semantically equivalent:

## Example

```
vnd-pi-agent: v="1.0.0", h="apache.example.com", t="Apache 2.4.41"
```

## Example

```
vnd-pi-agent: v="1.0.0", h="apache.example.com"
vnd-pi-agent: t="Apache 2.4.41"
```

## Example

```
vnd-pi-agent: v="1.0.0"
vnd-pi-agent: h="apache.example.com"
vnd-pi-agent: t="Apache 2.4.41"
```
