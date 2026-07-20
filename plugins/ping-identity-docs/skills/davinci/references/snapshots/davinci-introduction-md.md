---
title: Introduction to PingOne DaVinci
description: PingOne DaVinci is an orchestration platform that lets you create flows to guide users through IAM activities.
component: davinci
page_id: davinci::davinci_introduction
canonical_url: https://docs.pingidentity.com/davinci/davinci_introduction.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 21, 2024
---

# Introduction to PingOne DaVinci

PingOne DaVinci is an orchestration platform that lets you create flows to guide users through IAM activities.

A [flow](flows/davinci_flows.html) is a set of paths that define the user journey through a given IAM process, such as registration or authentication, using a set of logically linked nodes. Each node in a flow either takes an action on the backend or presents the user with a page. The path a user follows through a flow is determined by logical decision operators that sit between the nodes, enabling you to control how a user progresses based on the information they provide, existing user information, or other parameters.

Each node performs a single task in the flow. When you place a node, you associate it with a [connector](connectors/davinci_connections.html) and then select a capability provided by that connector. These capabilities include retrieving information from third parties, presenting customized pages to users, modifying the value of variables, or performing other actions.

You can add new connectors to your environment to make new capabilities available in your flows. These connectors can communicate with other Ping products or third parties. You can also configure multiple instances of a connector to use different environments or settings. The [connector documentation](https://docs.pingidentity.com/connectors/) and the [Ping Identity Marketplace](https://marketplace.pingone.com/home) contain information about the available connectors and the capabilities they provide.

After you create a flow, you add it to an [application](applications/davinci_applications.html) and create a flow policy to control how and when the flow gets used. Applications enable you to run flows using a widget, API calls, OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* calls, or Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">
\<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>
\</div>)* 2.0 calls. The application also lets you perform A/B testing by splitting traffic between different flows or versions of the same flow.

DaVinci includes tools to enable customization and information tracking in your flows. The [UI Studio](ui_studio/davinci_ui_studio.html) lets you configure HTML pages that match your company's style and branding, which you can then present to users within flows. [Variables](variables/davinci_variables.html) let you track data within flows or across multiple flows and use that data to determine a user's path.

Use this documentation for the core functions and usage of DaVinci. For details about individual connectors, see the [integration directory](https://marketplace.pingone.com/browse?products=davinci).