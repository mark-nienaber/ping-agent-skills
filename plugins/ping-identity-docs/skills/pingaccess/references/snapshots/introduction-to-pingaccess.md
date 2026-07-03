---
title: How do I choose a deployment model?
description: "PingAccess supports three deployment models: gateway, agent, and sideband. Review the advantages and disadvantages of each deployment model before selecting one for your environment."
component: pingaccess
version: 9.1
page_id: pingaccess:introduction_to_pingaccess:pa_choose_a_deployment_model
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/introduction_to_pingaccess/pa_choose_a_deployment_model.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 7, 2026
section_ids:
  gateway: Gateway model
  what-is-the-gateway-model: What is the gateway model?
  pros: Pros
  cons: Cons
  agent: Agent model
  what-is-the-agent-model: What is the agent model?
  pros-2: Pros
  cons-2: Cons
  sideband: Sideband model
  what-is-the-sideband-model: What is the sideband model?
  pros-3: Pros
  cons-3: Cons
---

# How do I choose a deployment model?

PingAccess supports three deployment models: gateway, agent, and sideband. Review the advantages and disadvantages of each deployment model before selecting one for your environment.

## Gateway model

### What is the gateway model?

In the gateway model, traffic is initially directed to a PingAccess node, and PingAccess grants or denies access directly. The application in PingAccess is configured with the site as the destination.

### Pros

* Less cross-team coordination required

  You can implement and maintain a gateway deployment with less coordination with application teams because the PingAccess infrastructure is installed on separate systems from the web servers.

* Simpler setup

  Because the PingAccess nodes are the only required components, this deployment model can be set up more quickly than the other models.

* Simpler upgrade

  The only components you must upgrade in a gateway deployment are the PingAccess nodes.

  |   |                                                                           |
  | - | ------------------------------------------------------------------------- |
  |   | You can upgrade PingAccess with zero downtime in a clustered environment. |

* Simpler troubleshooting

  Issues are easier to isolate because there are fewer components sharing a system with the PingAccess infrastructure.

* Simpler logging

  All transactions that PingAccess processes are audited by the engine node, making it easier to view logs for a specific event.

### Cons

* Network impact

  Using the gateway deployment model requires that you restructure your existing network to route traffic through PingAccess.

* Additional network overhead

  The overhead of an additional network hop can theoretically exceed a latency budget. This rarely happens in practice, and the agent model often makes a similar addition to latency, but this might occur in some environments.

## Agent model

### What is the agent model?

In the agent model, traffic is directed to the application, which has an agent plugin installed on the web server. The agent grants or denies access, and queries the PingAccess node when it requires additional information. The application in PingAccess is configured with the agent as the destination.

### Pros

* No network changes

  Because the PingAccess agents are installed on the web servers, no network changes are required.

* Minor performance improvements

  In some cases, the agent can determine whether to grant access using cached data, which can reduce latency. In most cases, though, the agent must communicate with a PingAccess node, which results in latency similar to the gateway model.

### Cons

* Greater maintenance effort

  You must maintain and upgrade agents independently on each web server.

* Unavailable features

  Some features can't be used in an agent deployment. For example, you can't:

  * Rewrite the request URL

  * Rewrite response headers

  * Rewrite request or response body content

    Learn more in [Agent deployments](../pingaccess_user_interface_reference_guide/pa_rules.html#agent-deployments).

* Cross-team coordination

  Because the agents are installed directly on the web server, you might have to coordinate with other teams to install and maintain them.

* Complex tracking

  Keeping track of all agents can be difficult.

* Difficult troubleshooting

  Because the agent model involves more systems which can be varied in their OS and web server versions, troubleshooting issues can be more difficult.

* Version dependencies

  Because the agent must be installed as a plugin on the web server, there are dependencies on the web server and OS versions that aren't present in the gateway model.

* Less centralized logging

  To view the logging for a specific transaction, you must review the agent audit log and the web server access logs.

## Sideband model

### What is the sideband model?

In the sideband model, traffic is directed to an application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* gateway, such as [Apigee](../agents_and_integrations/pa_apigee_api_gateway_integration.html) or [Kong](../agents_and_integrations/pa_kong_api_gateway_integration.html). The API gateway makes a backchannel *(tooltip: \<div class="paragraph">
\<p>A direct, cross-domain communication path using a protocol that doesn't rely on a browser as an intermediary.\</p>
\</div>)* call to PingAccess to determine if it should grant or deny the request and to determine what modifications should be made to the request or response. The application in PingAccess is configured with the sideband client as the destination.

### Pros

* No network changes

  Because the PingAccess sideband clients are installed on the API gateways, no network changes are required.

* Simpler troubleshooting

  Issues are easier to isolate because there are fewer components sharing a system with the PingAccess infrastructure.

* Simpler logging

  All transactions processed by PingAccess are audited by the engine node, making it easier to view logs for a specific event.

### Cons

* Greater maintenance effort

  You must maintain and upgrade API gateway integration kits independently on each API gateway.

* Unavailable features

  Some features may not be available depending on your API gateway.

* Additional network overhead

  The overhead of an additional network hop can theoretically exceed a latency budget. This rarely happens in practice, and the gateway and agent models often make a similar addition to latency, but this might occur in some environments.

* Cross-team coordination

  Because the sideband clients are installed directly on the API gateways, you might have to coordinate with other teams to install and maintain them.

* Complex tracking

  A sideband deployment has more components to maintain than a gateway deployment.

* Version dependencies

  Because the sideband client must be installed on the API gateway, there are dependencies on the API gateway and operating system versions that are not present in the gateway model.
