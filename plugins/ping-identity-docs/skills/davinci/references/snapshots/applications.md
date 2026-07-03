---
title: Applications
description: An application in DaVinci represents one of your applications and gives you fine-grained control over which flows can be run through that application and by what methods.
component: davinci
page_id: davinci:applications:davinci_applications
canonical_url: http://docs.pingidentity.com/davinci/applications/davinci_applications.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2024
---

# Applications

An application in DaVinci represents one of your applications and gives you fine-grained control over which flows can be run through that application and by what methods.

An application acts as a gateway between your site and the flows you have created in DaVinci. The application contains settings to determine how external sites can send requests for flows, what flows can be requested, and how users and resources from other sites are managed. External sites can only run flows that are made available through an application.

The **General** and **OIDC** tabs let you configure receivers for incoming requests. Other tools can send requests to launch flows using API endpoints described in the **General** tab or the OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* parameters in the **OIDC** tab.

The **Flow Policy** tab lets you control which flows are run through the application. A flow policy is an entity that points to one or more flows or versions of flows. You can use a flow policy to make sure that a specific version of a flow, such as the latest version, is always used. You can also split traffic between different flows or flow versions for A/B testing or other purposes.

The **Connections** tab lets you direct requests to specific connectors.
