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

---

---
title: How does PingAccess work?
description: Access requests are either routed through a PingAccess gateway to the target site or intercepted at the target web application server by a PingAccess agent, which coordinates access policy decisions with a PingAccess policy server.
component: pingaccess
version: 9.1
page_id: pingaccess:introduction_to_pingaccess:pa_how_does_pa_work
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/introduction_to_pingaccess/pa_how_does_pa_work.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 7, 2025
section_ids:
  wam-session-initiation: WAM session initiation
  token-mediation: Token mediation
---

# How does PingAccess work?

Access requests are either routed through a PingAccess [gateway](pa_choose_a_deployment_model.html#gateway) to the target site or intercepted at the target web application server by a PingAccess [agent](pa_choose_a_deployment_model.html#agent), which coordinates access policy decisions with a PingAccess policy server.

In either instance, PingAccess evaluates the [policies](../pingaccess_user_interface_reference_guide/pa_rules.html) applied to access requests for the target application and makes a policy-based decision to grant or deny access to the requested resource. After access is granted, PingAccess can modify client requests and server responses to provide additional identity information required by the target application.

## WAM session initiation

When a user authenticates, PingAccess applies your configured application and resource-level policies to the Web Access Management (WAM) request.

After completing policy evaluation and determining that the authenticated user should be granted access to a site, PingAccess performs any required token mediation between the backend site and the authenticated user. PingAccess then grants the user access to the site.

Diagram illustrating the WAM flow between and .

> **Collapse: Processing steps:**
>
> 1. When a user requests access to a web resource from PingAccess, PingAccess inspects the request for a PingAccess token.
>
> 2. If the PingAccess token is missing, PingAccess redirects the user to an OpenID Provider (OP) *(tooltip: \<div class="paragraph">
>    \<p>In OAuth terms, an authorization server (AS). The OP/AS issues access tokens to protected resources for approved clients (relying parties). The clients use the access token to access the protected resources hosted by the OAuth resource server.\</p>
>    \</div>)* for authentication.
>
>    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
>    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>    |   | When using an OP, you must already have an OAuth client *(tooltip: \<div class="paragraph">&#xA;\<p>The application in an OAuth framework that requests access to resources. If the request is approved by the authorization server, the client is issued an access token for the resources.\</p>&#xA;\</div>)* configured in PingAccess.- For information on configuring an OAuth client within PingFederate, see [Configure PingFederate as the token provider for PingAccess](../token_providers/pa_configure_pf_as_the_token_provider_for_pa.html) and the [Administrator's Reference Guide](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_administrators_reference_guide.html) in the PingFederate documentation.
>
>    - To configure the OAuth client within PingAccess, see [Connect PingAccess to PingFederate](../token_providers/pa_connect_pa_to_pf.html). |
>
> 3. The OP follows the appropriate authentication process, evaluates domain-level policies, and issues an OIDC ID token to PingAccess.
>
> 4. PingAccess validates the ID token and issues a PingAccess token and sends it to the browser in a cookie during a redirect to the original target resource.
>
>    After gaining access to the resource, PingAccess evaluates application and resource-level policies and can optionally audit the request.
>
>    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
>    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
>    |   | PingAccess can perform token mediation by exchanging the PingAccess token for the appropriate security token from the PingFederate Security Token Service (STS) *(tooltip: \<div class="paragraph">&#xA;\<p>An entity responsible for responding to WS-Trust requests for validation and issuance of security tokens used for SSO authentication to web services.\</p>&#xA;\</div>)* or from a cache if token mediation occurred recently. |
>
> 5. PingAccess forwards the request to the target site.
>
> 6. PingAccess processes the response from the site to the browser (step not pictured).
>
> |   |                                                                                                                                                |
> | - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | For more information, see the [Session management configuration](../configuring_and_customizing_pingaccess/pa_session_management_config.html). |

## Token mediation

Token mediation allows a PingAccess gateway to use a PingFederate token generator to exchange the PingAccess token or an OAuth bearer token for a security token used by the foreign authentication system.

|   |                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When planning a PingAccess deployment, take an inventory of existing applications and their authentication requirements and mechanisms. When an existing token-based authentication mechanism is in use, retrofitting that mechanism might not always be desirable or cost-effective. |

The access request is transparent to the user, allowing PingAccess to transparently manage access to systems using those foreign tokens. The request is also transparent to the protected application, which handles the access request as if it came from the user directly. After token mediation, PingAccess caches the token used to access the application for continued use during the session.

The following illustration shows an example of token mediation using PingFederate to exchange a PingAccess token or OAuth bearer token for a different security token.

Diagram illustrating token mediation between and .

> **Collapse: Processing steps:**
>
> 1. A user requests a resource from PingAccess with a PingAccess token or OAuth bearer token.
>
>    |   |                                                                                                                                                                                                                                                                                                                                    |
>    | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>    |   | This example assumes the user has already obtained a PingAccess token or OAuth bearer token. For information on how users authenticate with PingFederate and obtain a PingAccess token or OAuth bearer token, see [Session management configuration](../configuring_and_customizing_pingaccess/pa_session_management_config.html). |
>
> 2. PingAccess evaluates resource-level policies and performs token mediation by acquiring the appropriate security token from the PingFederate STS specified by the site authenticator.
>
> 3. PingAccess sends the request to the site (web application) with the appropriate token.
>
> 4. PingAccess returns the response to the client (step not pictured).
>
>    |   |                                                                                                                          |
>    | - | ------------------------------------------------------------------------------------------------------------------------ |
>    |   | You can't access a mediated token through a Groovy rule because token mediation occurs after PingAccess rule processing. |

> **Collapse: Token mediation cache settings**
>
> You can configure token mediation cache settings in the `run.properties` file using the following parameters:
>
> * pa.ehcache.ServiceTokenCache.maxEntriesLocalHeap
>
>   Defines the maximum number of entries in the local heap for token mediation. The default value is 10000.
>
> * pa.ehcache.ServiceTokenCache.timeToIdleSeconds
>
>   Defines, in seconds, the time an entry in the token mediation cache can be idle before it is expired. The default value is 1800.
>
> * pa.ehcache.ServiceTokenCache.timeToLiveSeconds
>
>   Defines, in seconds, the maximum time an entry can be in the token mediation cache. The default value is 14400.

---

---
title: Introduction to PingAccess
description: PingAccess is an identity-enabled access management product that protects web applications and APIs by applying security policies to client requests.
component: pingaccess
version: 9.1
page_id: pingaccess:introduction_to_pingaccess:pa_intro_to_pa
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/introduction_to_pingaccess/pa_intro_to_pa.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
---

# Introduction to PingAccess

PingAccess is an identity-enabled access management product that protects web applications and APIs by applying security policies to client requests.

PingAccess allows you to protect sites, APIs, and other resources using rules and other authentication criteria. Working in conjunction with a configured token provider, PingAccess integrates identity-based access management policies through a federated corporate identity store using open standards access protocols.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Valid token providers include PingFederate and other common token providers with the OAuth *(tooltip: \<div class="paragraph">&#xA;\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>&#xA;\</div>)* 2.0 and OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">&#xA;\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>&#xA;\</div>)* protocols. For more information, see [System requirements](../installing_and_uninstalling_pingaccess/pa_installation_requirements.html). |

To help you get the most from PingAccess, this document offers insights about the product, such as:

* [What can I do with PingAccess?](pa_what_can_i_do_with_pa.html)

* [How does PingAccess work?](pa_how_does_pa_work.html)

* [What can I configure with PingAccess?](pa_what_can_i_configure_with_pa.html)

* [How do I choose a deployment model?](pa_choose_a_deployment_model.html)

As you learn about PingAccess's features and functions, review [Configuring and Customizing PingAccess](../configuring_and_customizing_pingaccess/pa_configuring_and_customizing_pa_landing_topic.html) for instructions on how to configure them.

For a comprehensive set of instructions on using the PingAccess interface, see the [PingAccess User Interface Reference Guide](../pingaccess_user_interface_reference_guide/pa_ui_ref_guide.html).

---

---
title: PingAccess for Azure AD Overview
description: PingAccess for Azure AD is a free version of PingAccess for users of Microsoft Entra ID (formerly Microsoft Azure AD) that allows you to protect up to 20 applications.
component: pingaccess
version: 9.1
page_id: pingaccess:introduction_to_pingaccess:pa_for_azure_ad_intro
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/introduction_to_pingaccess/pa_for_azure_ad_intro.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December, 2024
---

# PingAccess for Azure AD Overview

PingAccess for Azure AD is a free version of PingAccess for users of Microsoft Entra ID (formerly Microsoft Azure AD) that allows you to protect up to 20 applications.

|   |                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingAccess for Azure AD program ends on December 31, 2025. To continue using PingAccess, you must upgrade to a commercial PingAccess license. Learn more in:- [Manage license keys](https://support.pingidentity.com/s/manage-license-keys)

- [View or upload a new license](../pingaccess_user_interface_reference_guide/pa_license.html) |

The goal of this solution is to allow for greater control over access to legacy on-premise applications through the use of PingAccess identity mapping functionality.

Learn more about configuring PingAccess for Azure AD in [PingAccess for Azure AD](../token_providers/pa_for_azure_ad.html).

PingAccess for Azure AD requires a premium license for Microsoft Entra ID. Learn more about licensing in <https://learn.microsoft.com/en-us/azure/active-directory/app-proxy/application-proxy-ping-access-publishing-guide> in the Microsoft documentation.

This free version of PingAccess includes a limited feature set that's intended to support the basic requirements for application protection using this solution. Users of PingAccess for Azure AD can upgrade to a full license allowing the use of the full PingAccess feature set.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When your PingAccess for Azure AD license expires, you won't be able to access the PingAccess administrative application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)* or configure the product. Though managed access to configured applications continues, you must upload a new license file before you can make any additional configuration changes. |

|   |                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingAccess for Azure AD provides a limited feature set that may not be compatible with existing PingAccess configurations. For this reason, upgrading from an earlier full version of PingAccess to PingAccess for Azure AD isn't supported. |

The following table details the capabilities of PingAccess for Azure AD compared to a full version of PingAccess. These capabilities are available in both the PingAccess administrative console and administrative API.

| Capability                                                                                                                                                                                                                                                             | PingAccess | PingAccess for Azure AD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Create applications                                                                                                                                                                                                                                                    | Yes        | Limited to 20 web session applications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Create site authenticators                                                                                                                                                                                                                                             | Yes        | Limited to Basic and Mutual TLS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Configure identity mappings                                                                                                                                                                                                                                            | Yes        | Limited to Header and JSON Web Token (JWT) *(tooltip: \<div class="paragraph">&#xA;\<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>&#xA;\</div>)*.                                                                                                                                                                  |
| Create load balancing strategies                                                                                                                                                                                                                                       | Yes        | Limited to Header-Based and Round Robin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Configure web sessions                                                                                                                                                                                                                                                 | Yes        | Limited to web sessions with OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">&#xA;\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>&#xA;\</div>)* sign-on type CODE. |
| Configure token provider                                                                                                                                                                                                                                               | Yes        | Limited to Microsoft Entra ID authentication source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Export/Import configuration                                                                                                                                                                                                                                            | Yes        | Limited to configurations that include only the features permitted by your license type.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Configure policies                                                                                                                                                                                                                                                     | Yes        | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Specify authentication requirements                                                                                                                                                                                                                                    | Yes        | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Create and configure custom plugins using the SDK                                                                                                                                                                                                                      | Yes        | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Configure sites                                                                                                                                                                                                                                                        | Yes        | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Configure agents                                                                                                                                                                                                                                                       | Yes        | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Create virtual hosts                                                                                                                                                                                                                                                   | Yes        | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Configure unknown resource handling                                                                                                                                                                                                                                    | Yes        | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Configure availability profiles                                                                                                                                                                                                                                        | Yes        | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Configure HTTP request *(tooltip: \<div class="paragraph">&#xA;\<p>A client transaction sent over HTTP to the server specifying a request method, such as GET, POST, and DELETE, to execute against a resource or resources on the server.\</p>&#xA;\</div>)* handling | Yes        | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Configure listeners                                                                                                                                                                                                                                                    | Yes        | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Configure forward proxy settings                                                                                                                                                                                                                                       | Yes        | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Manage certificates                                                                                                                                                                                                                                                    | Yes        | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Manage key pairs                                                                                                                                                                                                                                                       | Yes        | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Configure administrator authentication                                                                                                                                                                                                                                 | Yes        | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Configure clustering                                                                                                                                                                                                                                                   | Yes        | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Manage licenses                                                                                                                                                                                                                                                        | Yes        | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

---

---
title: What can I configure with PingAccess?
description: PingAccess includes a wide range of features to customize your identity access management deployment.
component: pingaccess
version: 9.1
page_id: pingaccess:introduction_to_pingaccess:pa_what_can_i_configure_with_pa
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/introduction_to_pingaccess/pa_what_can_i_configure_with_pa.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  agents: Agents
  applications: Applications
  authentication-requirements: Authentication requirements
  auth-token-management: Auth token management
  availability-profiles: Availability profiles
  certificates: Certificates
  clustering: Clustering
  http-requests: HTTP requests
  identity-mappings: Identity mappings
  key-pairs: Key pairs
  listeners: Listeners
  load-balancing-strategies: Load balancing strategies
  policies: Policies
  proxies: Proxies
  rules-rule-sets-and-rule-set-groups: Rules, rule sets, and rule set groups
  sites: Sites
  site-authenticators: Site authenticators
  token-provider: Token provider
  unknown-resources: Unknown resources
  virtual-hosts: Virtual hosts
  web-sessions: Web sessions
---

# What can I configure with PingAccess?

PingAccess includes a wide range of features to customize your identity access management deployment.

## Agents

Agents are web server plugins that are installed on the web server hosting the target application. Agents intercept client requests to protected applications and allow or deny the request to proceed by consulting the policy manager or using cached information. Agents communicate with the PingAccess policy server through the PingAccess Agent Protocol (PAAP), which defines the possible interactions between agents and policy server.

Agents have a name to identify them and a shared secret for authentication with the policy server. Agents do not need to be unique. There can be any number of agents using the same name and secret, and they are all treated equally by policy server. This is useful in complex deployments where unique agents would be difficult to manage. Agents can be assigned as the destination for one or more applications by name.

## Applications

Applications represent the protected web applications and APIs to which client requests are sent. Applications are composed of one or more resources and have a common virtual host and context root corresponding to a single target site. Applications also use a common web session and identity mapping.

To protect applications and their resources, you can apply access control and request processing rules on the policy manager page using the following options:

* PingAccess gateway

  In a gateway deployment, the target application is specified as a site.

* PingAccess agent

  In an agent deployment, the application destination is an agent.

## Authentication requirements

Authentication requirements are policies that dictate how a user must authenticate before access is granted to a protected web application. Authentication methods are string values and ordered in a list by preference. At runtime, the type of authentication attempted is determined by the order of the authentication methods.

For example:

1. A user attempts to access a PingAccess web application configured with an authentication requirement list containing the values, such as password and certificate.

2. PingAccess redirects the user to PingFederate requesting either password or certificate *(tooltip: \<div class="paragraph">
   \<p>A digital file used for identity verification and other security purposes. The certificate, which is often issued by a CA, contains a public key, which can be used to verify the originator's identity.\</p>
   \</div>)* user authentication.

3. PingFederate authenticates the user based on the password and issues an OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
   \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
   \</div>)* ID token to PingAccess, containing the authentication method that was used.

4. PingAccess ensures that the authentication method matches the requirements and redirects the user to the originally requested application with the PingAccess cookie set.

5. The user navigates to the application and access is granted.

   When the user attempts to access a more sensitive application, configured with an authentication requirement list containing the value (certificate), they are redirected to PingFederate to authenticate with a certificate.

If you configure applications with authentication requirement lists that have no overlap, a user navigating between those applications might be required to authenticate each time they visit an application. So, when you're configuring authentication requirement lists to protect higher value applications with step-up authentication, consider including stronger forms of authentication on lower value applications as well.

## Auth token management

Auth token management settings define the issuer and signing configuration used by JSON Web Token (JWT) *(tooltip: \<div class="paragraph">
\<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>
\</div>)* identity mappings.

## Availability profiles

Availability profiles are used in a site configuration to define how PingAccess classifies a backend target server as failed. Sites require the selection of an availability profile even if only one target is provided.

If multiple targets are specified in a site configuration but a load balancing strategy is not applied, then the availability profile causes the first listed target in the site configuration to be used unless it fails. Secondary targets are only used if the first target is not available.

## Certificates

Certificates are used to establish anchors used to define trust to certificates presented during secure HTTPS connections. Outbound secure HTTPS connections, such as communication with PingFederate for OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)* access token *(tooltip: \<div class="paragraph">
\<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>
\</div>)* validation, identity mediation, and communication with a target site, require a certificate trusted by PingAccess. If one does not exist, communication is not allowed.

Certificates used by PingAccess can be issued by a certificate authority (CA) *(tooltip: \<div class="paragraph">
\<p>An entity that issues digital certificates.\</p>
\</div>)* or self-signed. Use CA-issued certificates to simplify trust establishment and minimize routine certificate management operations. Implementations of an X.509-based PKI (PKIX) typically have a set of root CAs that are trusted, and the root certificates are used to establish chains of trust to certificates presented by a client or a server during communication.

The following formats for X.509 certificates are supported:

* Base64 encoded DER (PEM)

* Binary encoded DER

## Clustering

To provide higher scalability and availability for critical services, configure PingAccess in a clustered environment.

PingAccess clusters are made up of three types of nodes:

* Administrative node

  Provides the administrator with a configuration interface.

* Replica administrative node

  Provides the administrator with the ability to recover a failed administrative node using a manual failover procedure.

* Engine node

  Handles incoming client requests and evaluates policy decisions based on the configuration replicated from the administrative node.

|   |                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can configure any number of clustered engines in a cluster, but you can only configure one administrative console and one replica administrative console in a cluster. |

## HTTP requests

HTTP Requests are used to match a served resource with the originating client when one or more reverse proxies are between the client and the served resource. For example, when a reverse proxy sits between the client and the PingAccess server or a PingAccess agent, the additional proxy might be identified as the client. Such proxies can be configured to inject additional headers to relay the originating client address.

## Identity mappings

Identity mappings make user attributes available to back-end sites that use them for authentication. There are multiple types of identity mappings, each with different behavior and a distinct set of fields to specify the identity mapping behavior.

## Key pairs

Key pairs are required for secure HTTPS communication. A key pair *(tooltip: \<div class="paragraph">
\<p>The private key and public key represented by a certificate.\</p>
\</div>)* includes a private key and an X.509 certificate. The certificate includes a public key and the metadata about the owner of the private key.

PingAccess listens for client requests on the administrative console port and on the PingAccess engine port. To enable these ports for HTTPS, the first time you start up PingAccess, it generates and assigns a key pair for each port. These generated key pairs are assigned on the **HTTPS Listeners** page.

Additionally, key pairs are used by the mutual TLS site authenticator to authenticate PingAccess to a target site. When initiating communication, PingAccess presents the client certificate from a key pair to the site during the mutual TLS transaction. The site must be able to trust this certificate for authentication to succeed.

## Listeners

Listeners monitor ports for incoming requests. PingAccess can place listeners on ADMIN, ENGINE, and AGENT ports.

## Load balancing strategies

Load balancing strategies are used in a site configuration to distribute the load between multiple backend target servers. Load balancing settings are optional and are only available if more than one target is listed for a site. This functionality can replace a load balancer appliance between the PingAccess engine nodes and the target servers, allowing for a simpler network architecture.

The header-based strategy requires a header be included in the request that defines the target to select from the site configuration. This strategy has an option to fall back if the requested target is unavailable or if the header is missing from the request.

The round robin strategy has a sticky session option that permits a browser session to be pinned to a persistent backend target. This strategy works in conjunction with the availability profile to select a target based on its availability, and the load balancer does not select a target that is in a failed state.

## Policies

Policies are rules, rule sets, or groups of rule sets applied to an application and its resources. Policies define how and when a client can access target sites. The policy manager is a rich drag-and-drop interface where you can manage policies by:

* Creating rules

* Building rule sets and rule set groups

* Applying them to applications and resources

When a client attempts to access an application resource identified in one of the policy's rules, rule sets, or rule set groups, PingAccess uses the information contained in the policy to decide whether the client can access the application resource and whether any additional actions need to take place prior to granting access.

Rules can restrict access in a number of ways such as testing user attributes, time of day, request IP addresses, or OAuth access token scopes. Rules can also perform request processing, such as modifying headers or rewriting URLs.

## Proxies

Configure settings to authenticate with a forward proxy server when PingAccess makes requests to sites or token providers.

## Rules, rule sets, and rule set groups

Rules are the building blocks for access control and request processing. There are many types of rules, each with different behavior and a distinct set of fields to specify the rule behavior. Rule sets allow you to group multiple rules into re-usable sets which can be applied to applications and resources. Rule set groups can contain rule sets or other rule set groups, allowing the creation of hierarchies of rules to any level of depth. Rule sets and rule set groups can be applied to applications and resources as required.

## Sites

Sites are the target applications or APIs that PingAccess gateway is protecting and to which authorized client requests are ultimately forwarded to.

## Site authenticators

When a client attempts to access a target web site, that site can limit access to only authenticated clients. PingAccess integrates with those security models using site authenticators. PingAccess supports a variety of site authenticators that range from basic username and password authentication to certificate and token-based authentication. Create a site authenticator for the type of authentication the site requires.

## Token provider

Token providers are used as a method of providing credentials for secure access to a given target.

## Unknown resources

Unknown resources are resources for which there is no PingAccess definition. You can specify the default and per-agent handling behavior for unknown resource requests and configure custom error responses.

## Virtual hosts

Virtual hosts enable PingAccess to protect multiple application domains and hosts. A virtual host is defined by the host name and host port.

## Web sessions

Web sessions define the policy for web application session creation, lifetime, timeouts, and their scope. You can configure multiple web sessions to scope the session to meet the needs of a target set of applications. This improves the security model of the session by preventing unrelated applications from impersonating the end user.

---

---
title: What can I do with PingAccess?
description: PingAccess provides a highly customizable solution to identity and access management (IAM) that allows you to control access by specifying the conditions that users must meet to access protected application and API resources.
component: pingaccess
version: 9.1
page_id: pingaccess:introduction_to_pingaccess:pa_what_can_i_do_with_pa
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/introduction_to_pingaccess/pa_what_can_i_do_with_pa.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 7, 2025
---

# What can I do with PingAccess?

PingAccess provides a highly customizable solution to identity and access management (IAM) that allows you to control access by specifying the conditions that users must meet to access protected application and API resources.

The upcoming PingAccess features section describes the methods that PingAccess uses to control access and perform system functions. You can find more information on how you can use PingAccess in the following resources:

* [Configuring and Customizing PingAccess](../configuring_and_customizing_pingaccess/pa_configuring_and_customizing_pa_landing_topic.html)

* [Reference Guides](../reference_guides/pa_reference_guides_landing_topic.html)

* [PingAccess User Interface Reference Guide](../pingaccess_user_interface_reference_guide/pa_ui_ref_guide.html)

The main functionality of PingAccess enables you to protect an application or application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)*. You can:

* Use PingAccess to protect the application and API resources to which client requests are forwarded.

* Partition applications for tighter access control through the use of resources.

* Customize the configuration of site authenticators and authentication requirements to suit the security needs of your organization.

* Incorporate legacy authentication mechanisms through [token mediation](pa_how_does_pa_work.html#token-mediation).

* Apply policies to define how and when a client can access target resources.

> **Collapse: PingAccess features**
>
> Customize your identity access management configuration with the following features:
>
> * Apply policies
>
>   Use policies, made up of rules, set of rules, or groups of rule sets applied to an application and its resources, to define how and when a client can access target sites. [Rules](../pingaccess_user_interface_reference_guide/pa_rules.html) are the building blocks for access control and request processing.
>
> * Backup and restore
>
>   [Backup or restore](../backing_up_and_restoring_pingaccess/pa_backing_up_and_restoring_pa.html) a PingAccess configuration with just a few clicks.
>
> * Configure a token provider
>
>   You can configure PingAccess to use PingFederate as the token provider or to use a common token provider through the OAuth *(tooltip: \<div class="paragraph">
>   \<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
>   \</div>)* 2.0 or OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
>   \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
>   \</div>)* protocols.
>
>   * Learn more about how to configure a token provider in the PingAccess admin console in [Token provider](../pingaccess_user_interface_reference_guide/pa_token_provider.html).
>
>   * You can find more information on how to set up a connection between a token provider and PingAccess in [Token Providers](../token_providers/pa_token_providers_landing_topic.html).
>
>     |   |                                                                                                                                                                                                                                                            |
>     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>     |   | This section of the documentation provides information on how to configure a few common token providers as the token provider for PingAccess, while the previous link includes information on how to set up PingAccess to connect with the token provider. |
>
> * Configure administrator authentication
>
>   Allow administrators to authenticate with a simple username and password or configure them to authenticate using single sign-on (SSO) *(tooltip: \<div class="paragraph">
>   \<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
>   \</div>)* or an API in conjunction with PingFederate. Learn more in [Admin authentication](../pingaccess_user_interface_reference_guide/pa_admin_authn.html).
>
> * Configure advanced network settings
>
>   Create an [availability profile](../pingaccess_user_interface_reference_guide/pa_availability_profiles.html) to determine how you want to classify a target server as having failed, configure listener ports, define a [load balancing strategy](../pingaccess_user_interface_reference_guide/pa_load_balancing_strategies.html), or use HTTP requests to match a served resource with the originating client.
>
> * Configure logging
>
>   Capture several log types, including those for the engine, security auditing, and cookies. Store logs in Splunk, in an Oracle, PostgreSQL, or SQL Server database, or in a file. Learn more in [Log configuration](../configuring_and_customizing_pingaccess/pa_logging_configuration.html).
>
> * Configure single logout (SLO) *(tooltip: \<div class="paragraph">
>   \<p>The process of signing a user out of multiple sites where the user has started a SSO session.\</p>
>   \</div>)*
>
>   End PingAccess sessions easily when used in conjunction with PingFederate managed sessions or compatible third-party OIDC *(tooltip: \<div class="paragraph">
>   \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
>   \</div>)* providers. Learn more in [Configuring a PingFederate runtime](../pingaccess_user_interface_reference_guide/pa_pf_runtime.html) or [Configuring OpenID Connect token providers](../pingaccess_user_interface_reference_guide/pa_configuring_oidc.html).
>
> * Create clusters
>
>   Deploy PingAccess in a clustered environment to provide higher scalability and availability for critical services. Place a load balancer in front of the cluster to distribute connections to the nodes in the cluster. Learn more in [Clustering in PingAccess](../reference_guides/pa_clustering_ref_guide.html).
>
> * Customize PingAccess look and feel
>
>   [Customize and localize](../configuring_and_customizing_pingaccess/pa_customize_localize_landing_topic.html) the PingAccess pages that your users see, including those for error messages and logout confirmation.
>
> * Customize with SDKs
>
>   Customize development with SDKs to extend the functionality of the PingAccess server. Learn more in [PingAccess Add-on SDK for Java](../agents_and_integrations/pa_add_on_sdk_for_java.html).
>
> * Manage certificates and key pairs
>
>   Import [certificates](../pingaccess_user_interface_reference_guide/pa_certificates.html) to establish trust with certificates presented during secure HTTPS sessions. Import or generate [key pairs](../pingaccess_user_interface_reference_guide/pa_key_pairs.html) that include the private key and X.509 Attribute Sharing Profile (XASP) *(tooltip: \<div class="paragraph">
>   \<p>Defines a specialized extension of the general attribute query profile and enables organizations with an investment in PKI (Public Key Infrastructure) to issue and receive attribute queries based on user-certificate authentication.\</p>
>   \</div>)* certificate required for HTTPS communication.
>
> * Manage sessions
>
>   Use [web sessions](../pingaccess_user_interface_reference_guide/pa_web_sessions.html) to define the policies for web application session creation, lifetime, timeout, and scope *(tooltip: \<div class="paragraph">
>   \<p>In OAuth, a parameter on an access request and resulting, issued access token that specifies a limitation or limitations on access to the protected resource or resources.\</p>
>   \</div>)*. Use multiple web sessions to scope the session to meet the needs of a target set of applications. Web sessions improve the security model of the session by preventing unrelated applications from impersonating the end user.
>
> * Manually configure runtime parameters
>
>   Use a text editor to modify configuration file settings used by PingAccess at runtime. You can find more information in the [Configuration file reference](../reference_guides/pa_config_file_ref.html).
>
> * Protect an application or API
>
>   Use PingAccess to protect the application and API resources to which client requests are forwarded. Partition [applications](../pingaccess_user_interface_reference_guide/pa_applications_operations.html) for tighter access control through the use of [resources](../pingaccess_user_interface_reference_guide/pa_application_resources.html). Customize configuration of [site authenticators](../pingaccess_user_interface_reference_guide/pa_site_authenticators.html) and [authentication requirements](../pingaccess_user_interface_reference_guide/pa_authentication.html) to suit the security needs of your organization.
>
>   The [developers page](http://developer.pingidentity.com/pingaccess.html) contains additional resources for developing applications to work with PingAccess.
>
> * Tune performance
>
>   Optimize a wide variety of PingAccess components for maximum performance. Learn more in [Performance tuning](../reference_guides/pa_performance_tuning.html).
>
> * Upgrade an existing installation
>
>   Upgrade an existing installation using the installer or selectively manage the upgrade process with the PingAccess upgrade utility. Learn more in [Installing and Uninstalling PingAccess](../installing_and_uninstalling_pingaccess/pa_installing_and_uninstalling_pa.html).
>
> * Use APIs
>
>   Use the PingAccess APIs to provide a powerful configuration and management experience outside the PingAccess user interface. Learn more in [Accessing the PingAccess administrative API](../installing_and_uninstalling_pingaccess/pa_accessing_the_pa_admin_api.html).