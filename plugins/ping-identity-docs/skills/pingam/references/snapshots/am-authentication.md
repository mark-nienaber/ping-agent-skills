---
title: AM as a RADIUS client
description: Configure PingAM as a RADIUS client to authenticate users against a RADIUS server using RADIUS Decision and Challenge Collector nodes
component: pingam
version: 8.1
page_id: pingam:am-authentication:radius-client
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authentication/radius-client.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Journeys", "Nodes &amp; Trees", "RADIUS"]
page_aliases: ["radius-server-guide:radius-auth-module.adoc", "radius-server:radius-auth-module.adoc"]
section_ids:
  configure_radius_authentication: Configure RADIUS authentication
---

# AM as a RADIUS client

The following diagram illustrates the flow of packets between AM (the RADIUS client) and the RADIUS server during an authentication conversation, where the RADIUS server requests a one-time password (OTP) from the user:

![Flows between a user, the authentication nodes, and an external RADIUS server.](_images/radius-auth-nodes-flow.svg)

All conversations between AM and the RADIUS server are secured with a shared secret (mapped to the `am.authentication.nodes.radius.identifier.secret` label).

## Configure RADIUS authentication

AM provides two authentication nodes to handle RADIUS authentication, where AM is acting as a RADIUS client:

* RADIUS Decision node

  The [RADIUS Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/radius-decision.html) performs authentication with the RADIUS server.

  The node performs the following actions:

  * Sends an `Access-Request` packet to the RADIUS server to initiate the authentication request.

  * Handles the RADIUS server's response to determine the outcome of the authentication attempt.

  * Sends additional `Access-Request` packets if the RADIUS server responds with an `Access-Challenge` packet requesting more information from the user.

* RADIUS Challenge Collector node

  The [RADIUS Challenge Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/radius-challenge-collector.html) presents challenge messages to users, such as requesting an OTP, and collects their response.

Create a journey using these nodes to implement RADIUS authentication:

![RADIUS authentication journey](_images/radius-journey.png)

Learn more in the [RADIUS authentication example](https://docs.pingidentity.com/auth-node-ref/8.1/radius-decision.html#example).
