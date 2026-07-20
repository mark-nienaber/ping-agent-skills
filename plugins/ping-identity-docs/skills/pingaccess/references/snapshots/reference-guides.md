---
title: Administrative API endpoints
description: PingAccess ships with interactive documentation for both developers and non-developers to explore the PingAccess application programming interface (API) endpoints, view a reference of the metadata for each API, and experiment with API calls.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_admin_api_endpoints
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_admin_api_endpoints.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 3, 2023
section_ids:
  admin-api-documentation-swagger-ui-specifications: Admin API documentation Swagger-UI specifications
---

# Administrative API endpoints

PingAccess ships with interactive documentation for both developers and non-developers to explore the PingAccess application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* endpoints, view a reference of the metadata for each API, and experiment with API calls.

PingAccess APIs are REST APIs that provide complete administrative capabilities of the product. They can be called from custom applications or from command line tools, such as cURL.

These endpoints are only available on the `admin.port` defined in the `/pa-admin-api/v3/api-docs/<PA_HOME>/conf/run.properties` file. For example, https\://*\<PA\_HOME>*:*\<PORT>*/pa-admin-api/v3/api-docs/.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you selected the **Use context root as reserved resource base path** check box in your PingAccess application, this feature creates an instance of any reserved PingAccess resources under the application's context root. As such, the context root of the application needs to prepend the reserved context application root (`/pa` by default) in any file paths that reference it. If the context root of your application is `myApp`, the file path would start with `/myApp/pa`. |

|   |                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | For enhanced API security, you must include `X-XSRF-Header: PingAccess` in all requests and use the `application/json` content type for `PUT` and `POST` requests. |

## Admin API documentation Swagger-UI specifications

The Swagger-UI component that displays the PingAccess admin API documentation uses OpenAPI specification (OAS) 2.0.

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The specification that the PingAccess admin API docs used previously, Swagger 1.2, has been deprecated. The Swagger 1.2 specification is still available at https\://*\<PA\_HOME>*:*\<PORT>*/pa-admin-api/v3/api-docs/pa/api-docs.json but might be removed from future versions of PingAccess. |

You can find the PingAccess admin API's OAS 2.0 specifications at either of the following:

* https\://*\<PA\_HOME>*:*\<PORT>*/pa-admin-api/v3/api-docs/pa/api-docs-v2.json

* https\://*\<PA\_HOME>*:*\<PORT>*/pa-admin-api/v3/api-docs/pa/api-docs-v2.yaml

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | Access to these specifications simplifies the process of integrating the PingAccess admin API with modern API clients, such as Postman. |

---

---
title: Agent tuning reference
description: Modify the properties of your PingAccess agents to improve performance.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_agent_tuning_ref
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_agent_tuning_ref.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
section_ids:
  maximum-connections: Maximum Connections
  maximum-tokens: Maximum Tokens
---

# Agent tuning reference

Modify the properties of your PingAccess agents to improve performance.

You can configure several properties in the `agent.properties` file for increased performance. For more information on agent configuration and setting properties, see the agent documentation for [Apache](../agents_and_integrations/pa_apache_rhel_configuration.html) or [IIS](../agents_and_integrations/pa_iis_configuration.html).

## Maximum Connections

Connections from the agent to PingAccess are limited by the `agent.engine.configuration.maxConnections` property. Though the default value is set to `10`, the PingAccess policy server sees optimal performance at 50 concurrent requests per CPU. In certain situations it can be advantageous to increase the number of connections. In the event that all connections in the pool are in use, a requesting thread waits for one to become available. Assuming that the response time to PingAccess is sufficiently fast, the time spent waiting for a connection is likely to be less than if the system becomes overloaded.

|   |                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This is the maximum number of connections per worker process, and not simply the total number of workers the agent has access to. Setting the `agent.engine.configuration.maxConnections` value too low might create a bottleneck to PingAccess, and setting the value too high might cause PingAccess to become overloaded. |

## Maximum Tokens

By default, the maximum number of cached tokens in an agent is unlimited. In certain situations, it can be advantageous to limit the size of the cache for the agent, as a smaller cache has a smaller memory footprint, freeing up memory available to the application for servicing requests. However, when the token cache limit is reached, the least-recently used token-policy mapping will be removed from the cache. If that token-policy mapping happens to be needed again, the agent will have a cache miss, resulting in the need to obtain a new token-policy mapping from PingAccess.

---

---
title: API Access Management Gateway deployment table
description: The following table describes the important configuration options for deploying an API Gateway. You can find specific use case information in Deploying for Gateway API Access Management.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_api_access_management_gateway_deployment_table
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_api_access_management_gateway_deployment_table.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 18, 2025
---

# API Access Management Gateway deployment table

The following table describes the important configuration options for deploying an API Gateway. You can find specific use case information in [Deploying for Gateway API Access Management](pa_deploy_for_gateway_api_access_management.html).

> **Collapse: Configuration steps**
>
> | Step                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                        |
> | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> | [Configure the connection to the PingFederate OAuth Authorization Server](../pingaccess_user_interface_reference_guide/pa_configuring_oauth_resource_servers.html).           | PingAccess uses this connection and credentials to validate incoming access tokens for securing application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)* calls. |
> | [Configure the OpenID Connect Relying Party Client for PingAccess](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_client_management.html). | You must register the client with PingFederate and the client credentials configured in PingAccess to authenticate PingAccess when validating incoming access tokens.                                                                                                                                              |
> | [Generate or Import Key Pairs and configure HTTP Listeners](../pingaccess_user_interface_reference_guide/pa_key_pairs.html).                                                  | Define the certificates and keys used to secure access to the PingAccess admin console and secure incoming HTTPS requests at runtime.                                                                                                                                                                              |
> | [Set up your cluster for high availability](pa_clustering_ref_guide.html).                                                                                                    | Configure a cluster to facilitate high availability of critical services and increase performance and overall system throughput.                                                                                                                                                                                   |
> | [Add trusted CA certificates](../pingaccess_user_interface_reference_guide/pa_importing_certificates.html).                                                                   | Defines trust to certificates presented during outbound secure HTTPS connections.                                                                                                                                                                                                                                  |
> | [Create a trusted certificate group](../pingaccess_user_interface_reference_guide/pa_creating_trusted_certificate_groups.html).                                               | Provides a trusted set of anchor certificates for use when authenticating outbound secure HTTPS connections.                                                                                                                                                                                                       |
> | [Define virtual servers for protected applications](../pingaccess_user_interface_reference_guide/pa_creating_new_virtual_hosts.html).                                         | Allow one server to share PingAccess resources without requiring all sites on the server to use the same host name.You can assign specific key pairs to virtual hosts.                                                                                                                                             |

---

---
title: API access management production deployment architecture
description: This production deployment environment shows an API access management architecture.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_api_access_management_production_deployment_architecture
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_api_access_management_production_deployment_architecture.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# API access management production deployment architecture

This production deployment environment shows an API access management architecture.

There are many considerations when deploying a production environment. For high availability and redundancy, the environment requires clustering and load-balancing. Load balancers are required as part of the networking infrastructure to achieve high availability by ensuring that requests are sent to available servers they are front-ending. Best practices in network design and security also include firewalls to ensure that only required ports and protocols are permitted across zones.

|   |                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingAccess provides high availability and basic load balancing for the protected web apps in the protected zone. For more information, see [Managing load balancing strategies](../pingaccess_user_interface_reference_guide/pa_load_balancing_strategies.html). |

The following environment example is a recommended production quality deployment architecture for an API access management use case.

![rcz1564006721062](_images/rcz1564006721062.svg)

The following table describes the three zones within this proposed architecture.

|                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| External Zone  | External network where incoming application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)* requests originate.                                                                                                                                                                    |
| DMZ            | Externally exposing segment where PingAccess is accessible to API clients. A minimum of two PingAccess engine nodes will be deployed in the DMZ to achieve high availability. Depending on your scalability requirements, you might require more nodes.                                                                                                                                                                            |
| Protected Zone | Backend controlled zone in which Sites hosting the protected APIs are located. All requests to these APIs must be designed to pass through PingAccess. PingFederate is accessible to API clients in this zone. A minimum of two PingFederate engine nodes will be deployed in the protected zone. Administrative nodes for both PingAccess and PingFederate can be co-located on a single machine to reduce hardware requirements. |

---

---
title: API access management proof of concept deployment architecture
description: The proof of concept environment emulates an API access management environment for testing purposes.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_api_access_management_proof_of_concept_deployment_architecture
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_api_access_management_proof_of_concept_deployment_architecture.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# API access management proof of concept deployment architecture

The proof of concept environment emulates an API access management environment for testing purposes.

In the test environment, PingAccess can be set up with the minimum hardware requirements. Given these conditions, do not use this proposed architecture in a production deployment because it does not provide high availability.

![quh1564006721035](_images/quh1564006721035.svg)

The following table describes the three zones within this proposed architecture.

| Zone           | Description                                                                                                                                                                                                                                                                                       |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| External Zone  | External network where incoming application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)* requests originate.                                   |
| DMZ            | Externally exposing segment where PingAccess is accessible to API clients. PingAccess is a standalone instance in this environment, serving as both a runtime and an administrative port.                                                                                                         |
| Protected Zone | Backend controlled zone in which sites hosting the protected APIs are located. All requests to these APIs must be designed to pass through PingAccess. PingFederate is accessible to API clients in this zone and is a standalone instance, serving as both a runtime and an administrative port. |

---

---
title: Auditing and proxying Gateway deployment table
description: The following table describes the important configuration options for an auditing or proxying deployment. You can find specific use case information in Deploying for Auditing and Proxying.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_auditing_and_proxying_gateway_deployment_table
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_auditing_and_proxying_gateway_deployment_table.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 18, 2025
---

# Auditing and proxying Gateway deployment table

The following table describes the important configuration options for an auditing or proxying deployment. You can find specific use case information in [Deploying for Auditing and Proxying](pa_deploy_for_auditing_and_proxying.html).

> **Collapse: Configuration steps**
>
> | Step                                                                                                                               | Description                                                                                                                            |
> | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
> | [Generate or Import Key Pairs and configure HTTP Listeners](../pingaccess_user_interface_reference_guide/pa_key_pairs.html).       | Defines the certificates and keys used to secure access to the PingAccess admin console and secure incoming HTTPS requests at runtime. |
> | [Set up your cluster for high availability](pa_clustering_ref_guide.html).                                                         | Configure a cluster to facilitate high availability of critical services and increase performance and overall system throughput.       |
> | [Add trusted CA certificates](../pingaccess_user_interface_reference_guide/pa_importing_certificates.html).                        | Define trust to certificates presented during outbound secure HTTPS connections.                                                       |
> | [Create a trusted certificate group](../pingaccess_user_interface_reference_guide/pa_creating_trusted_certificate_groups.html).    | Provide a trusted set of anchor certificates for authenticating outbound secure HTTPS connections.                                     |
> | [Define virtual servers for protected resources](../pingaccess_user_interface_reference_guide/pa_creating_new_virtual_hosts.html). | Allows one server to share PingAccess resources without requiring all sites on the server to use the same host name.                   |

---

---
title: Auditing and proxying production deployment architecture
description: This production deployment environment shows an auditing and proxying architecture in PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_auditing_and_proxying_production_deployment_architecture
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_auditing_and_proxying_production_deployment_architecture.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# Auditing and proxying production deployment architecture

This production deployment environment shows an auditing and proxying architecture in PingAccess.

There are many considerations when deploying a production environment. For high availability and redundancy, the environment requires clustering and load-balancing. Load balancers are required as part of the networking infrastructure to achieve high availability by ensuring that requests are sent to available servers they are front-ending. Best practices in network design and security also include firewalls to ensure that only required ports and protocols are permitted across zones.

|   |                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingAccess can provide high availability and basic load balancing for the protected web apps in the protected zone. For more information, see [Managing load balancing strategies](../pingaccess_user_interface_reference_guide/pa_load_balancing_strategies.html). |

The following environment example is a recommended production quality deployment architecture for an auditing and proxying use case.

![wjs1564006721195](_images/wjs1564006721195.svg)

The following table describes the three zones within this proposed architecture.

|                |                                                                                                                                                                                                                                                     |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| External Zone  | External network where incoming requests originate.                                                                                                                                                                                                 |
| DMZ            | Externally exposing segment where PingAccess is accessible to clients. A minimum of two PingAccess engine nodes will be deployed in the DMZ. Depending on your scalability requirements, you might require more nodes.                              |
| Protected Zone | Contains backend Sites audited and proxied through PingAccess. Audit results are sent to an audit repository or digested by reporting tools. Many types of audit repository tools are supported such as SIEM/GRC, Splunk, database, and flat files. |

---

---
title: Auditing and proxying proof of concept deployment architecture
description: This proof of concept deployment environment is used to emulate an auditing and proxying environment for testing purposes in PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_auditing_and_proxying_proof_of_concept_deployment_architecture
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_auditing_and_proxying_proof_of_concept_deployment_architecture.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# Auditing and proxying proof of concept deployment architecture

This proof of concept deployment environment is used to emulate an auditing and proxying environment for testing purposes in PingAccess.

In the test environment, you can set up PingAccess with the minimum hardware requirements. Given these conditions, do not use this proposed architecture in a production deployment because it does not provide high availability.

![oyc1564006721175](_images/oyc1564006721175.svg)

The following table describes the three zones within this proposed architecture.

| Zone           | Description                                                                                                                                                                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| External Zone  | External network where incoming requests originate.                                                                                                                                                                                                  |
| DMZ            | Externally exposing segment where PingAccess is accessible to clients. PingFederate and PingAccess are standalone instances in this environment, serving as both runtime and administrative ports.                                                   |
| Protected Zone | Contains back-end sites audited and proxied through PingAccess. Audit results are sent to an audit repository or digested by reporting tools. Many types of audit repository/tools are supported such as SIEM/GRC, Splunk, database, and flat files. |

---

---
title: Authentication Token Management endpoint
description: This page describes the endpoint used to validate JSON Web Tokens.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_authn_token_management_endpoint
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_authn_token_management_endpoint.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 6, 2023
section_ids:
  paauthtokenjwks: /pa/authtoken/JWKS
---

# Authentication Token Management endpoint

This page describes the endpoint used to validate JSON Web Tokens.

## /pa/authtoken/JWKS

Backend sites use the Authentication Token Management endpoint to validate the signature of a JSON Web Token (JWT) *(tooltip: \<div class="paragraph">
\<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>
\</div>)*.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you selected the **Use context root as reserved resource base path** check box on your PingAccess application, this feature creates an instance of any reserved PingAccess resources under the application's context root. As such, the context root of the application needs to prepend the reserved context application root (`/pa` by default) in any file paths that reference it.If the context root of your application is `myApp`, the path to the Authentication Token Management endpoint would be `myApp/pa/authtoken/JWKS` instead. |

---

---
title: Backend server connections
description: PingAccess provides a max connections option to control and optimize connections to the proxied site.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_backend_server_connections
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_backend_server_connections.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
section_ids:
  maximum-connections: Maximum Connections
---

# Backend server connections

PingAccess provides a max connections option to control and optimize connections to the proxied site.

## Maximum Connections

Connections to PingAccess are not explicitly connections to the proxied site. PingAccess creates a pool of connections, unlimited in size by default, that are multiplexed to fulfill client requests. Maintenance of the pool includes creating connections to the site when needed, if none are available, and removing connections when they are closed by the backend server due to inactivity.

In certain situations, it can be advantageous to limit the number of connections in the pool for a given website. If, for example, the website is limited to the number of concurrent connections it can handle or has specific HTTP Keep Alive settings, limiting the number of connections from PingAccess can improve overall performance by not overloading the backend server. In the event that all connections in the pool are in use, a requesting thread waits for one to become available. Assuming that the response time from the backend site is sufficiently fast, the time spent waiting for a connection is likely to be less than if the system becomes overloaded.

|   |                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | It is important to understand the limits and tuning of the server application being proxied. Setting the **Maximum Connections** value too low might create a bottleneck to the proxied site, setting the value too high, or unlimited, might cause PingAccess to overload the server. |

For information on setting the **Maximum Connections**, see [Sites documentation](../pingaccess_user_interface_reference_guide/pa_site_field_descriptions_ref.html).

---

---
title: Body object reference
description: This object accesses the Body object in Groovy exc?.request?.body or exc?.response?.body.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_body_object_ref
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_body_object_ref.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  purpose: Purpose
  groovy-sample: Groovy sample
  method-summary: Method summary
---

# Body object reference

This object accesses the Body object in Groovy `exc?.request?.body` or `exc?.response?.body`.

## Purpose

The Body object contains the HTTP body from the application request or the HTTP body from the site response. The request HTTP body is sent on to the site after the rules are evaluated. The response HTTP body is sent on to the User-Agent after the response rules are evaluated.

## Groovy sample

```
//Checks the actual length of the body content and set the Content-Length response header
def body = exc?.response?.body;
def header = exc?.response?.header;
header?.setContentLength(body?.getLength());
pass();
```

## Method summary

| Method               | Description                                          |
| -------------------- | ---------------------------------------------------- |
| byte\[] getContent() | Returns the body content of the request or response. |
| int getLength()      | Returns the length of the body content.              |

---

---
title: Choose between an agent or gateway deployment
description: Deploy PingAccess using Agents, as a Gateway (or reverse proxy), or using a combination of both. Before choosing a deployment, understand the pros and cons of each deployment scenario and determine how they impact your strategy.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_choose_between_an_agent_or_gateway_deployment
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_choose_between_an_agent_or_gateway_deployment.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  gateway: Gateway
  agents: Agents
---

# Choose between an agent or gateway deployment

Deploy PingAccess using Agents, as a Gateway (or reverse proxy), or using a combination of both. Before choosing a deployment, understand the pros and cons of each deployment scenario and determine how they impact your strategy.

## Gateway

Pros:

* Fewer number of deployed components that require maintenance

* Independent of target application platform

* No impact on web or app server processing and performance

* Works with existing security token types, such as creating third party Web Access Management (WAM) tokens

Cons:

* Requires networking changes

* Requires strategy for securing direct access to backend web or app servers (network routing or service level authentication)

* Depending on the application, might require content/request/response rewriting

* Another layer that requires HA/DR planning

## Agents

Pros:

* No networking or server level authentication changes required

* Tight integration with web server handling requests

* Scales with application

Cons:

* High cost of ownership when many agent instances are deployed, although should be upgradable or patchable independently of PingAccess policy server

* Policy evaluation is cached, and although periodically flushed or re-evaluated (for new sessions, updates to session token, etc.) , isn't as "real time" as proxy

* Tight dependency on web server version and platform

---

---
title: Clustered engine node endpoint
description: The following endpoint enables clustered PingAccess engine nodes to automatically pull updated certificate information from the admin node.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa-engine-endpoints
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa-engine-endpoints.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 18, 2026
section_ids:
  enginesrestconfig-query-certificate: /engines/rest/config-query-certificate
---

# Clustered engine node endpoint

The following endpoint enables clustered PingAccess engine nodes to automatically pull updated certificate information from the admin node.

This endpoint is available on the `clusterconfig.temp.rotation.port` port defined in the `<PA_HOME>/conf/run.properties` file.

## `/engines/rest/config-query-certificate`

PingAccess engine nodes poll this endpoint continually to detect when the admin node begins using a new key pair for the config query HTTPS listener. If a new key pair is in use, each engine node [automatically rotates](../pingaccess_user_interface_reference_guide/pa_assigning_key_pairs.html#autorotation) the key pair it's using to match the new key pair on the admin node.

During every polling check, the engine node also sends a fingerprint header indicating which key pair the engine is currently using. This lets the admin node track when all engine nodes have switched to the new key pair.

---

---
title: Clustering in PingAccess
description: PingAccess provides clustering features that allow a group of PingAccess servers to appear as a single system.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_clustering_ref_guide
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_clustering_ref_guide.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 6, 2024
section_ids:
  components-of-a-pingaccess-cluster: Components of a PingAccess Cluster
  node-failure-implications: Node failure implications
  cluster-properties: Cluster properties
  cluster-node-status: Cluster node status
  using-multiple-network-interface-cards-to-route-traffic: Using multiple network interface cards to route traffic
---

# Clustering in PingAccess

PingAccess provides clustering features that allow a group of PingAccess servers to appear as a single system.

Server clustering can facilitate high availability of critical services and can also increase performance and overall system throughput. However, availability and performance are often at opposite ends of the deployment spectrum. You might need to make some configuration tradeoffs that balance availability with performance to accommodate specific deployment goals.

|   |                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Settings in the configuration file could affect the features documented here. For more information, see the [Configuration file reference](pa_config_file_ref.html) guide. |

## Components of a PingAccess Cluster

PingAccess clusters are made up of three types of nodes:

* The Administrative Node

  Provides the administrator with a configuration interface.

* The Replica Administrative Node

  Provides the administrator with the ability to recover a failed administrative node using a manual failover procedure. For more information, see [Manually promoting the replica administrative node](pa_manually_promoting_the_replica_admin_node.html).

* The Engine Nodes

  Handle incoming client requests and evaluate policy decisions based on the configuration replicated from the administrative node.

|   |                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can configure any number of engine nodes in a cluster, but you can configure only one administrative node and one replica administrative node in a cluster. State information is not shared between engine nodes. |

Configuration information from the administrative console and API is replicated to all of the engine nodes and the replica administrative node from the administrative node, as is the license file on the administrative node. Engine nodes do not require a license to function, but some default templates look different depending on the information in the license.

You should manage incoming traffic to the engine nodes using load balancers or other mechanisms. PingAccess clusters do not dynamically manage or load-balance request traffic to individual engine nodes. ![eoc1564006721359](_images/eoc1564006721359.svg)

## Node failure implications

Node failure within a PingAccess cluster can have short-term or long-term implications for your environment, depending on the state of your network and the type of node or nodes that failed. The following table describes some common node issues and recommends what kind of action to take.

| Node issue                                                    | Result                                                                                                                                                                                                                                               | Recommendation                                                                                                       |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Administrative node failure                                   | The engine nodes can function using their stored configurations but cannot update their configurations.                                                                                                                                              | Fail over to the replica administrative node until the administrative node can be restarted.                         |
| Replica administrative node failure                           | The engine nodes and administrative node can function normally, but you won't be able to fail over to the replica administrative node if something happens to the administrative node.                                                               | Restart the replica administrative node as soon as possible.                                                         |
| Administrative and replica node failure                       | The engine nodes can function using their stored configurations, but cannot update their configurations. No failover option is available.                                                                                                            | Restart the administrative node as soon as possible, or restart the replica administrative node and fail over to it. |
| One or more engine nodes cannot reach the administrative node | Affected engine nodes can function using their stored configurations, if any but cannot update their configurations. If the administrative node performs key rolling, the affected engine nodes cannot recognize the new PingAccess internal cookie. | Restore access to the administrative node as soon as possible.                                                       |

## Cluster properties

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | Use the `run.properties` and `bootstrap.properties` files to configure your environment. |

In a cluster, you can configure each PingAccess node to serve as either an administrative node, a replica administrative node, or an engine node in the `run.properties` file. The `run.properties` file for the administrative node also contains server-specific configuration data.

At startup, a clustered PingAccess engine node checks its local configuration and then makes a call to the administrative node to check for changes. You can configure how often each engine node in a cluster checks the administrative node for changes in the engine `run.properties` file.

Information needed to bootstrap an engine node is stored in the `bootstrap.properties` file on each engine node.

**bootstrap.properties**

| Property                                          | Description                                                                                             |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `engine.admin.configuration.host`                 | Defines the host where the administrative console is available. The default is `localhost`.             |
| `engine.admin.configuration.port`                 | Defines the port where the administrative console is running. The default is `9000`.                    |
| `engine.admin.configuration.userid`               | Defines the name of the engine.                                                                         |
| `engine.admin.configuration.keypair`              | Defines an elliptic curve key pair that is in the JSON Web Key (JWK) format.                            |
| `engine.admin.configuration.bootstrap.truststore` | Defines the trust store, in JWK format, that is used for communication with the administrative console. |

|   |                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can tune the cache using the EHCache Configuration Properties, `pa.ehcache.*`, listed in the [Configuration file reference guide](pa_config_file_ref.html). |

## Cluster node status

The administrative console provides two important visual elements which communicate the current status of the replica administrative node and the engine nodes:

* A status indicator, which communicates whether the node is healthy.

* A **Last Updated** field, which communicates the date and time that the node was last updated.

You can find this information on the **Administrative Nodes** page and the **Engines** page.

Status indicators use the value for *\<admin.polling.delay>* as an interval to measure node health. A node's status can be green (good status), yellow (degraded status), or red (failed status):

* Green (good status)

  The node contacted the administrative node on the last pull request.

* Yellow (degraded status)

  The node contacted the administrative node between 2 and 10 intervals.

* Red (failed status)

  The node has either never contacted the administrative node or it has been more than 10 intervals since the nodes communicated.

## Using multiple network interface cards to route traffic

PingAccess binds to all network interfaces by default to support routing traffic over multiple network interfaces. The default bind address PingAccess uses is 0.0.0.0. To prevent PingAccess from binding to all network interfaces, you can edit one or more of the following parameters in the `conf/run.properties` file:

```
admin.bindAddress=0.0.0.0
clusterconfig.bindAddress=0.0.0.0
engine.http.bindAddress=0.0.0.0
agent.http.bindAddress=0.0.0.0
```

Specify a new bind address for the parameter that you want to modify.

---

---
title: Configuration by use case
description: Configuration steps vary depending on what type of deployment you are implementing.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_configuration_by_use_case
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_configuration_by_use_case.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  next-steps: Next steps
---

# Configuration by use case

Configuration steps vary depending on what type of deployment you are implementing.

For a detailed discussion of deployment considerations and best practices in designing your architecture, see the [Deployment Guide](pa_deployment_guide.html). The following sections describe the configuration steps for the most common use cases:

* [API Access Management Gateway Deployment](pa_api_access_management_gateway_deployment_table.html)

* [Web Access Management Agent Deployment](pa_wam_agent_deployment_table.html)

* [Web Access Management Gateway Deployment](pa_wam_gateway_deployment_table.html)

* [Auditing and Proxying Gateway Deployment](pa_auditing_and_proxying_gateway_deployment_table.html)

## Next steps

After you complete the above configuration settings, the following steps are similar for all use cases:

* Configure sites and agents to define the target applications you want protected. Sites might need site authenticators to define the credentials the site expects for access control.

* Configure applications and resources to define the assets you want to allow clients to access.

* Create policies for the defined applications and resources to protect them.

---

---
title: Configuration file reference
description: You can configure any of the following properties used by PingAccess at runtime in the <PA_HOME>/conf/run.properties file.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_config_file_ref
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_config_file_ref.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2026
section_ids:
  pa-operational-mode: Operational mode
  pa-admin-properties: Administrative properties
  pa-token-provider-communication-settings: Token provider communication settings
  pa-cluster-config-settings: Cluster configuration settings
  pa-engine-properties: Engine properties
  pa-agent-properties: Agent properties
  pa-sideband-properties: Sideband properties
  pa-url-filtering-settings: URL filtering settings
  pa-monitoring: Monitoring
  pa-tls-ssl: TLS/SSL
  pa-post-preservation-properties: POST preservation properties
  pa-config-database-and-key-store-settings: Configuration database and key store settings
  pa-pf-admin-integration-properties: PingFederate administration integration properties
  pa-admin-console-settings: Administrative console settings
  pa-ehcache-config-properties: EHCache configuration properties
  pa-security-headers-properties: Security headers properties
  pa-localization-settings: Localization settings
  pa-cert-rotation: Cert rotation
---

# Configuration file reference

You can configure any of the following properties used by PingAccess at runtime in the `<PA_HOME>/conf/run.properties` file.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When making changes to the `run.properties` file, use the following guidelines:- When storing passwords in `run.properties`, obfuscate them using the `obfuscate.bat or obfuscate.sh` utility to mask the password value. You can find this utility in the `<PA_HOME>/bin` folder.

- In a clustered environment, each node has a unique `run.properties` file. Because changes to the `run.properties` file can significantly impact performance, use an identical `run.properties` configuration on all engine nodes.

- Changes made to the `run.properties` file only take effect after you restart the PingAccess service on the given node. |

If you're running PingAccess in FIPS mode, PingAccess ignores all Secure Sockets Layer (SSL) *(tooltip: \<div class="paragraph">
\<p>A protocol for authenticated and encrypted links between networked machines, typically over HTTPS. SSL was deprecated in 1999 in favor of Transport Layer Security (TLS).\</p>
\</div>)* cipher and protocol settings in the `run.properties` file. Learn more about the protocols and ciphers used in this mode in [Managing Federal Information Processing Standards (FIPS) mode](../configuring_and_customizing_pingaccess/pa_fips_mode.html).

## Operational mode

> **Collapse: Click to expand or collapse the whole section**
>
> * pa.operational.mode
>
>   Controls the operational mode of the PingAccess server in a cluster. The following table describes the acceptable values:
>
> > **Collapse: Value**
> >
> > | Value                       | Description                                                                                                                                                        |
> > | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> > | `STANDALONE`                | Use this value for a standalone (un-clustered) PingAccess instance that runs both the administrative console and the engine. This is the default value.            |
> > | `CLUSTERED_CONSOLE`         | Use this value for the server instance that you want to use as the administrative console server.	Only one engine in a cluster can run the administrative console. |
> > | `CLUSTERED_CONSOLE_REPLICA` | Use this value for the server instance that you want to use as the backup administrative console server.                                                           |
> > | `CLUSTERED_ENGINE`          | Use this value to indicate a server engine.                                                                                                                        |
>
> |   |                                                                                                                                                                                                                                                                                                                                                                                                        |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> |   | Define the following engine and administrative properties depending on what operational mode an engine is using:- Define all engine and administrative properties when `pa.operational.mode` is set to `STANDALONE`.
>
> - Define only administrative properties when using `CLUSTERED_CONSOLE` or `CLUSTERED_CONSOLE_REPLICA` mode.
>
> - Define only engine properties when using `CLUSTERED_ENGINE` mode. |
>
> > **Collapse: Learn more**
> >
> > * Learn more about configuring nodes using clustered operational mode in the [Clustering Reference Guide](pa_clustering_ref_guide.html).
> >
> > * Learn more about installing PingAccess in standalone mode in [Installing and Uninstalling PingAccess](../installing_and_uninstalling_pingaccess/pa_installing_and_uninstalling_pa.html).

## Administrative properties

> **Collapse: Click to expand or collapse the whole section**
>
> * admin.port
>
>   Defines the TCP port on which the PingAccess administrative console runs. The default value is `9000`.
>
> * admin.bindAddress
>
>   Defines the Internet Protocol (IP) *(tooltip: \<div class="paragraph">
>   \<p>The method by which data is sent across the internet from the source host to the destination host.\</p>
>   \</div>)* address that `admin.port` binds to. Typically required on multi-homed servers with multiple IP addresses. The default value of `0.0.0.0` means that the port will bind to all the server's IP addresses.
>
> * admin.ssl.protocols
>
>   Defines the protocols for use with administrative HTTPS ports. The default value is `$\{tls.default.protocols}`, which uses the protocols specified by the `tls.default.protocols` property.
>
> * admin.ssl.ciphers
>
>   Defines the type of cryptographic ciphers available for use with administrative HTTPS ports. The default value is `$\{tls.default.cipherSuites}`, which uses the ciphers specified by the `tls.default.cipherSuites` property.
>
> * admin.acceptors
>
>   Defines the number of admin acceptor threads used to establish connections. The default value is `1`.
>
> * admin.backlog
>
>   Defines the maximum queue length for incoming admin connection indications. The default value is `512`.
>
> * admin.httptransport.coreThreadPoolSize
>
>   Defines the number of threads to keep in the admin transport pool, even if they're idle. The default value is `5`.
>
> * admin.httptransport.ioThreads
>
>   Defines the number of I/O threads for the admin host. The default value is `0`, which indicates that PingAccess should automatically calculate the appropriate number of I/O threads for the host.
>
> * admin.httptransport.maxThreadPoolSize
>
>   Defines the maximum number of threads for the admin transport pool. The default value is `-1`, which denotes no limit.
>
> * admin.httptransport.socketTimeout
>
>   Defines, in milliseconds, the admin socket timeout. The default value is `30000`.
>
> * admin.auth
>
>   Overrides the administrator authentication method. For example, if single sign-on (SSO) *(tooltip: \<div class="paragraph">
>   \<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
>   \</div>)* authentication is enabled and becomes misconfigured, this property can be used to bypass the database configuration and force the use of Basic authentication. The default value is `default`. A value of `native` overrides the administrator authentication method, meaning that only the local administrator credentials can be used to access the PingAccess console.
>
> * admin.reuseAddress
>
>   When enabled, allows a process to bind to a port which remains in a `TIME_WAIT` state for the admin transport. The default value is `true`.
>
> * admin.max.request.bodylength
>
>   Defines, in megabytes, the maximum body length for a request to the administrative application programming interface (API) *(tooltip: \<div class="paragraph">
>   \<p>A specification of interactions available for building software to access an application or service.\</p>
>   \</div>)* endpoint *(tooltip: \<div class="paragraph">
>   \<p>One end in a communication channel, typically a URI.\</p>
>   \</div>)*. The default value is `15`.
>
> * admin.ui.max.sessions
>
>   Defines the maximum number of sessions for the admin UI when admin single logout (SLO) *(tooltip: \<div class="paragraph">
>   \<p>The process of signing a user out of multiple sites where the user has started a SSO session.\</p>
>   \</div>)* isn't enabled. The default value is `100`.
>
> * admin.export.encryption.mode
>
>   Specifies how sensitive data should be encrypted on export. The default value is `MASTER_KEY`, which uses the system default master key for encryption.
>
>   |   |                                                                                                                                                                                                                                                                                                                                                    |
>   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | The `PORTABLE_INSECURE` value uses a randomly generated key for each export and includes the key in the export data.This method allows the exported data to be imported anywhere, including another cluster with a different master key. However, because the exported data includes the key, this method can present a significant security risk. |
>
> * admin.startup.config.import.failfast
>
>   Defines the behavior when attempting to import a configuration file on startup. A value of `true` stops at the first failure, while a value of `false` continues and notes all errors. The default value is `false`.
>
> > **Collapse: Learn more**
> >
> > * Learn more about how some properties are configured during installation in [Installing and Uninstalling PingAccess](../installing_and_uninstalling_pingaccess/pa_installing_and_uninstalling_pa.html).
> >
> > * Learn more about how some properties impact administrative use in [PingAccess User Interface Reference Guide](../pingaccess_user_interface_reference_guide/pa_ui_ref_guide.html).
> >
> > * Learn more about how some SSL properties are overridden in FIPS mode in [Managing Federal Information Processing Standards (FIPS) mode](../configuring_and_customizing_pingaccess/pa_fips_mode.html).

## Token provider communication settings

> **Collapse: Click to expand or collapse the whole section**
>
> * pa.default.availability.ondemand.maxRetries
>
>   Defines the maximum number of retries before marking the target system down. The default value is `2`.
>
> * pa.default.availability.ondemand.connectTimeout
>
>   Defines, in milliseconds, the amount of time to wait before trying to connect to the remote host. The default value is `10000`.
>
> * pa.default.availability.ondemand.retryDelay
>
>   Defines, in milliseconds, the amount of time to wait after a timeout before retrying the host. The default value is `250`.
>
> * pa.default.availability.ondemand.failedRetryTimeout
>
>   Defines, in seconds, the amount of time to wait before retrying a failed host. The default value is `60`.
>
> * pa.default.availability.ondemand.pooledConnectionTimeout
>
>   Defines, in milliseconds, the amount of time to wait before timing out the request for a pooled connection to the target site. The default value is `-1`, which indicates no timeout.
>
> * pa.default.availability.ondemand.readTimeout
>
>   Defines, in milliseconds, the amount of time to wait before timing out the read response for a target site. The default value is `-1`, which indicates no timeout.
>
> > **Collapse: Learn more**
> >
> > * Learn more in the token providers section of the [PingAccess User Interface Reference Guide](../pingaccess_user_interface_reference_guide/pa_ui_ref_guide.html).

## Cluster configuration settings

> **Collapse: Click to expand or collapse the whole section**
>
> * clusterconfig.enabled
>
>   When enabled, uses the cluster configuration port for cluster replication. When disabled, the admin port is used for cluster configuration replication. The default value is `true`.
>
>   |   |                                                                                                                                           |
>   | - | ----------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | This property is set to `false` by the PingAccess upgrade utility after a PingAccess cluster is upgraded from a version earlier than 4.0. |
>
> * clusterconfig.port
>
>   Defines the optional port used for cluster configuration. The default value is `9090`.
>
> * clusterconfig.temp.rotation.port
>
>   Defines the port used during the config query certificate rotation window to keep the old key pair for the config query HTTPS listener active while the PingAccess engines are switching over to the new key pair. The default value is `9095`.
>
> * clusterconfig.bindAddress
>
>   Defines the optional address used for cluster configuration. The default value is `0.0.0.0`.
>
> * clusterconfig.acceptors
>
>   Defines the number of cluster configuration acceptor threads used to establish connections. The default value is `1`.
>
> * clusterconfig.backlog
>
>   Defines the maximum queue length for incoming cluster configuration connection indications. The default value is `512`.
>
> * clusterconfig.reuseAddress
>
>   When enabled, allows a process to bind to a port, which remains in a `TIME_WAIT` state for the cluster configuration transport. The default value is `true`.
>
> * clusterconfig.httptransport.socketTimeout
>
>   Defines, in milliseconds, the cluster configuration socket timeout. The default value is `30000`.
>
> * clusterconfig.httptransport.ioThreads
>
>   Defines the number of I/O threads for the cluster configuration host. The default value is `0`, which indicates that PingAccess should automatically calculate the appropriate number of I/O threads for the host.
>
> * clusterconfig.httptransport.coreThreadPoolSize
>
>   Defines the number of threads to keep in the cluster configuration transport pool, even if they are idle. The default value is `5`.
>
> * clusterconfig.httptransport.maxThreadPoolSize
>
>   Defines the maximum number of threads for the cluster configuration transport pool. The default value is `-1`, which denotes no limit.
>
> * engine.admin.configuration.audience
>
>   Defines the audience used for cluster authentication. This property must be set to the same value on all nodes in a PingAccess cluster. The default value is `PingAccessAdminServer`.
>
> * engine.polling.initialdelay
>
>   Defines, in milliseconds, how long after the engine starts up before it begins to poll the administrative console for configuration information. The default value is `500`.
>
> * engine.polling.delay
>
>   Defines, in milliseconds, how long after the prior query to the administrative console that the engine begins a new query for configuration information. The default value is `2000`.
>
> * engine.polling.test.delay
>
>   Defines, in milliseconds, how long after detecting an engine's `lastUpdated` value to be `null` or `zero` that PingAccess should wait before double-checking the value. The default value is `6000`.
>
>   |   |                                                                                                                                                                                                                                                             |
>   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | This property determines whether a replacement engine should self-register if PingAccess detects that there's an existing engine with the same name that isn't running. Changing this value changes PingAccess's behavior according to the following table: |
>
>   > **Collapse: Self-registration settings**
>   >
>   > | engine.polling.test.delayvalue                                | PingAccess behavior                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
>   > | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   > | A negative number                                             | Self-registration always fails, even if the existing engine with the same name was never updated or isn't polling.                                                                                                                                                                                                                                                                                                                                                           |
>   > | A number from `0` up to the `engine.polling.delay` value      | Self-registration happens automatically if the existing engine's `lastUpdated` value is `null` or `0`.                                                                                                                                                                                                                                                                                                                                                                       |
>   > | A number that's greater than the `engine.polling.delay `value | Self-registration happens if the existing engine's `lastUpdated` value is `null` or `0`. If the value is greater than `0`, PingAccess waits for a number of milliseconds equal to the `engine.polling.test.delay` value, then checks the `lastUpdated` value a second time.If the value doesn't change, PingAccess allows self-registration. Otherwise, this indicates that the existing engine is active, so PingAccess fails self-registration for the replacement engine. |
>
> * admin.polling.initialdelay
>
>   Defines, in milliseconds, how long after the replica administrative node starts up before it begins to poll the administrative console for configuration information. The default value is `500`.
>
> * admin.polling.delay
>
>   Defines, in milliseconds, how long after the prior query to the administrative console that the replica administrative node begin a new query for configuration information. The default value is `2000`.
>
> * pa.config.replication.readTimeout
>
>   Defines, in milliseconds, the amount of time to wait before timing out the read response for the administrative node. The default value is `30000`.
>
> * pa.config.replication.maxRetries
>
>   Defines the maximum number of retries before marking the administrative node system down. The default value is `5`.
>
> * pa.config.replication.connectTimeout
>
>   Defines, in milliseconds, the amount of time to wait before trying to connect to the administrative node. The default value is `5000`.
>
> * pa.config.replication.retryDelay
>
>   Defines, in milliseconds, the amount of time to wait after a timeout before retrying the administrative node. The default value is `2000`.
>
> * pa.config.replication.failedRetryTimeout
>
>   Defines, in seconds, the amount of time to wait before retrying a failed connection to the administrative node. The default value is `-1`, which indicates no timeout.
>
> * pa.config.replication.pooledConnectionTimeout
>
>   Defines, in milliseconds, the amount of time to wait before timing out the request for a pooled connection to the administrative node. The default value is `-1`, which indicates no timeout.
>
> > **Collapse: Learn more**
> >
> > * Learn more about cluster configuration in the [Clustering Reference Guide](pa_clustering_ref_guide.html).

## Engine properties

> **Collapse: Click to expand or collapse the whole section**
>
> * engine.http.bindAddress
>
>   Defines the address for an engine in a clustered environment. The default value is `0.0.0.0`.
>
> * engine.http.acceptors
>
>   Defines the number of engine acceptor threads used to establish connections. The default value is `1`.
>
> * engine.http.backlog
>
>   Defines the maximum queue length for incoming engine connection indications. The default value is `512`.
>
> * engine.http.reuseAddress
>
>   When enabled, allows a process to bind to a port which remains in a `TIME_WAIT` state for the engine transport. The default value is `true`.
>
> * engine.http.enabled
>
>   Defines whether the engine node (either `STANDALONE` or `CLUSTERED_ENGINE`, if you're running PingAccess in a cluster) listens for requests on the ports defined by the engine listeners. The default value is `true`.
>
> * engine.httptransport.coreThreadPoolSize
>
>   Defines the number of threads to keep in the engine transport pool, even if they are idle. The default value is `5`.
>
> * engine.httptransport.maxThreadPoolSize
>
>   Defines the maximum number of threads for the engine transport pool. The default value is `-1`, which denotes no limit.
>
> * engine.httptransport.socketTimeout
>
>   Defines, in milliseconds, the engine socket timeout. The default value is `30000`.
>
> * engine.httptransport.ioThreads
>
>   Defines the number of I/O threads for the engine host. The default value is `0` which denotes that PingAccess should automatically calculate the appropriate number of I/O threads for the host.
>
> * engine.websocket.maxConnections
>
>   Sets the maximum number of allowed web socket connections. The default value is `-1`, which denotes no limit.
>
> * engine.ssl.protocols
>
>   Defines the protocols used with engine HTTPS ports. The default value is `TLSv1, TLSv1.1, TLSv1.2, TLSv1.3`.
>
> * engine.ssl.ciphers
>
>   Defines the type of cryptographic ciphers available for use with engine HTTPS ports. The default value is `$\{tls.default.cipherSuites}`, which uses the ciphers specified by the `tls.default.cipherSuites` property.
>
> * client.ioThreads
>
>   Defines the number of threads for client connections to backend sites. The default value is `0`, which denotes no limit.
>
> * pa.default.contentRewrite.buffer.min
>
>   Defines, in bytes, the minimum buffer size used when using a rewrite content rule. The default value is `1024`.
>
> * pa.default.contentRewrite.buffer.default
>
>   Defines, in bytes, the default buffer size when using a rewrite content rule to do a search and replace of content. The default value is `2048`.
>
> * pa.default.limitRequestLine
>
>   Defines the maximum number of bytes to read from the request line. The default value is `8192`.
>
> * pa.default.maxHeaderCount
>
>   Defines the maximum number of headers to read from a request. The default value is `100`.
>
> * pa.default.maxHttpHeaderSize
>
>   Defines the maximum number of bytes to read when reading headers. The default value is `8192`.
>
> * pa.default.maxRequestBodySize
>
>   Defines the maximum number of bytes to read from a request body. The default value is `204800`.
>
> * pa.default.maxConnectionsPerSite
>
>   Defines the maximum number of connections PingAccess can open to the PingFederate admin or engine. The default value is `-1`, which denotes no limit.
>
> * pa.default.session.cookie.attributes.httponly
>
>   Defines the default setting for the **HTTP-Only Cookie** setting for newly created web sessions. The default value is `true`.
>
> * pa.default.session.cookie.attributes.secure
>
>   Defines the default setting for the **Secure Cookie** setting for newly created web sessions. The default value is `true`.
>
> * pa.default.session.cookie.size.threshold
>
>   Defines, in bytes, the default maximum session cookie size. The default value is `4093`.
>
> * pa.websession.cookie.sameSiteExcludedUserAgentPatterns
>
>   A comma-separated list of regex that specifies whether an end-user browser should have `SameSite=None` applied to cookies issued to it. If the user-agent header from a request matches any of the values in the list, any PingAccess-issued cookie is set with no `SameSite` attribute if `SameSite=None` would otherwise have been applied. The default value is:
>
>   ```
>   ^.\\(iP.+; CPU .*OS 12[_\\d].\\) AppleWebKit\\/.$,\
>   ^.Macintosh;.*Mac OS X 10_14.*Version.*Safari.$,\
>   ^.(Chromium|Chrome)\\/(5[1-9]|6[0-6])\\.(\\d+)(?:\\.(\\d+)|)(?:\\.(\\d+)|).$,\
>   ^.UCBrowser\\/[0-9][0-1]?.(\\d+)\\.(\\d+)[\\.\\d].$,\
>   ^.*UCBrowser\\/12.[0-9][0-2]?.(\\d+)[\\.\\d].$,\
>   ^.*UCBrowser\\/12.13.[0-2][\\.\\d].*$
>   ```
>
> * pa.default.session.cookie.attributes.partitioned
>
>   When enabled, adds the `Partitioned` attribute to cookies set by PingAccess. This ensures that cross-site cookies continue to be readable within the same context that they're created in. Learn more in the [PingAccess 8.1 release notes](../release_notes/pa_release_notes.html#previous-releases).
>
>   The default value is `false`. If you edit this value, restart PingAccess to make your changes take effect.
>
> * pa.default.cookie.attributes.partitioned.excludedUserAgentPatterns
>
>   If `pa.default.session.cookie.attributes.partitioned` is enabled, or if you've selected **Partitioned Cookie** on a [web session](../pingaccess_user_interface_reference_guide/pa_advanced_web_session_settings.html) or the [admin web session](../pingaccess_user_interface_reference_guide/pa_configuring_session_properties.html), you can define a comma-separated list of regex to declare any user-agents that don't support the `Partitioned` attribute. If the user-agent header from a request matches any of the values in the list, PingAccess excludes the `Partitioned` attribute from any related cookies that it sets.
>
>   For example:
>
>   ```
>   pa.default.cookie.attributes.partitioned.excludedUserAgentPatterns= ^.\\(iP.+; CPU .*OS 12[\\d].\\) AppleWebKit\\/.$,\
>
>   ^.Macintosh;.*Mac OS X 10_14.*Version.*Safari.$,\
>
>   ^.(Chromium|Chrome)\\/(5[1-9]|6[0-6])\\.(\\d+)(?:\\.(\\d+)|)(?:\\.(\\d+)|).$,\
>
>   ^.UCBrowser\\/[0-9][0-1]?.(\\d+)\\.(\\d+)[\\.\\d].$,\
>
>   ^.*UCBrowser\\/12.[0-9][0-2]?.(\\d+)[\\.\\d].$,\
>
>   ^.*UCBrowser\\/12.13.[0-2][\\.\\d].$,\
>
>   ^.\\(Macintosh;.Mac OS X 10_14[\\d].\\) AppleWebKit\\/[\\.\\d]+ \\(KHTML. like Gecko\\)$,\
>
>   Box.\\/.+Darwin\\/10.14.$,\
>
>   ^.*PAN GlobalProtect.*Mac OS X 10.*14.$
>   ```
>
>   By default, this property doesn't have a value. If you edit this value, restart PingAccess to make your changes take effect.
>
> * pa.uri.strict
>
>   When enabled, this setting requires that the raw input Uniform Resource Identifier (URI) *(tooltip: \<div class="paragraph">
>   \<p>Identifies a web resource with a string of characters conforming to a specified format.\</p>
>   \</div>)* be in strict compliance with the URI spec implemented by `java.net.URI` when generating URIs. The default value is `false`.
>
> * pa.uri.canonicalize
>
>   When enabled, PingAccess normalizes empty and dot path segments that contain URL-encoded forward slashes (`/`, encoded as `%2f`) or periods (encoded as `%2e`). When this setting has a value of `false`, PingAccess doesn't normalize empty and dot path segments that contain URL-encoded forward slashes or periods. The default value is `true`.
>
> > **Collapse: Learn more**
> >
> > * Learn more about cluster configuration in the [Clustering Reference Guide](pa_clustering_ref_guide.html).
> >
> > * Learn more about how some SSL properties are overridden in FIPS mode in [Managing Federal Information Processing Standards (FIPS) mode](../configuring_and_customizing_pingaccess/pa_fips_mode.html).

## Agent properties

> **Collapse: Click to expand or collapse**
>
> * agent.http.port
>
>   Defines the TCP port on which the engine listens for agent requests. The default value is `3030`.
>
> * agent.http.bindAddress
>
>   Defines the address from which an engine listens for agent requests. The default value is `0.0.0.0`.
>
> * agent.http.acceptors
>
>   Defines the number of acceptor threads used to establish agent connections. The default value is `1`.
>
> * agent.http.secure
>
>   Defines whether the engine is using HTTPS for agent requests. The default value is `true`.
>
> * agent.http.backlog
>
>   Defines the maximum queue length for incoming agent connection indications. The default value is `512`.
>
> * agent.http.enabled
>
>   Defines whether the engine node (either `STANDALONE` or `CLUSTERED_ENGINE`, if you're running PingAccess in a cluster) listens for agent requests on the port defined by the `agent.http.port` setting. The default value is `true`.
>
> * agent.http.reuseAddress
>
>   When enabled, allows a process to bind to a port which remains in a `TIME_WAIT` state for the agent transport. The default value is `true`.
>
> * agent.ssl.protocols
>
>   Defines the protocols used for communication with agent HTTPS ports. The default value is `${tls.default.protocols}`, which uses the protocols specified by the `tls.default.protocols` property.
>
> * agent.ssl.ciphers
>
>   Defines the type of cryptographic ciphers available for use with agent HTTPS ports. The default value is `${tls.default.cipherSuites}`, which uses the ciphers specified by the `tls.default.cipherSuites` property.
>
> * agent.httptransport.coreThreadPoolSize
>
>   Defines the number of threads to keep in the agent transport pool, even if they are idle. The default value is `5`.
>
> * agent.httptransport.maxThreadPoolSize
>
>   Defines the maximum number of threads for the agent transport pool. The default value is `-1`, which denotes no limit.
>
> * agent.httptransport.socketTimeout
>
>   Defines, in milliseconds, the agent socket timeout. The default value is `30000`.
>
> * agent.httptransport.ioThreads
>
>   Defines the number of I/O threads for the agent host. The default value is `0`, which denotes that PingAccess should automatically calculate the appropriate number of I/O threads for the host.
>
> * agent.authz.header.required
>
>   Defines whether PingAccess server should authenticate agent requests using agent name and shared secret in the vnd-pi-authz header. The default value is `true`. Setting this to `false` is useful for POCs and/or debugging.
>
> * agent.default.token.cache.ttl
>
>   Defines, in seconds, the time to live for cached agent tokens. The default value is `60`.
>
> > **Collapse: Learn more**
> >
> > * Learn more about agent settings in [PingAccess User Interface Reference Guide](../pingaccess_user_interface_reference_guide/pa_ui_ref_guide.html).
> >
> > * Learn more about agent installation and management for Apache (RHEL) in [PingAccess Agent for Apache (RHEL)](../agents_and_integrations/pa_agent_for_apache_rhel.html).
> >
> > * Learn more about agent installation and management for Apache (SLES) in [PingAccess Agent for Apache (SLES)](../agents_and_integrations/pa_agent_for_apache_sles.html).
> >
> > * Learn more about agent installation and management for Apache (Windows) in [PingAccess Agent for Apache (Windows)](../agents_and_integrations/pa_agent_for_apache_windows.html).
> >
> > * Learn more about agent installation and management for IIS in [PingAccess Agent for IIS](../agents_and_integrations/pa_agent_for_iis.html).
> >
> > * Learn more about agent installation and management foe NGINX in [PingAccess Agent for NGINX](../agents_and_integrations/pa_agent_for_nginx.html).
> >
> > * Learn more about how some SSL properties are overridden in FIPS mode in [Managing Federal Information Processing Standards (FIPS) mode](../configuring_and_customizing_pingaccess/pa_fips_mode.html).

## Sideband properties

> **Collapse: Click to expand or collapse the whole section**
>
> * sideband.http.port
>
>   Defines the TCP port on which the engine listens for sideband requests. The default value is `3020`.
>
> * sideband.http.bindAddress
>
>   Defines the address from which an engine listens for sideband requests. The default value is `0.0.0.0`.
>
> * sideband.http.acceptors
>
>   Defines the number of acceptor threads used to establish sideband connections. The default value is `1`.
>
> * sideband.http.secure
>
>   Defines whether the engine is using HTTPS for sideband requests. The default value is `true`.
>
> * sideband.http.backlog
>
>   Defines the maximum queue length for incoming sideband connection indications. The default value is `512`.
>
> * sideband.http.enabled
>
>   Defines whether the engine node (either `STANDALONE` or `CLUSTERED_ENGINE`, if you're running PingAccess in a cluster) listens for sideband requests on the port defined by the `sideband.http.port` setting. The default value is `false`.
>
> * sideband.http.reuseAddress
>
>   When enabled, allows a process to bind to a port which remains in a `TIME_WAIT` state for the sideband transport. The default value is `true`.
>
> * sideband.ssl.protocols
>
>   Defines the protocols used for communication with sideband HTTPS ports. The default value is `${tls.default.protocols}`, which uses the protocols specified by the `tls.default.protocols` property.
>
> * sideband.ssl.ciphers
>
>   Defines the type of cryptographic ciphers available for use with sideband HTTPS ports. The default value is `${tls.default.cipherSuites}`, which uses the ciphers specified by the `tls.default.cipherSuites` property.
>
> * sideband.httptransport.coreThreadPoolSize
>
>   Defines the number of threads to keep in the sideband transport pool, even if they are idle. The default value is `5`.
>
> * sideband.httptransport.maxThreadPoolSize
>
>   Defines the maximum number of threads for the sideband transport pool. The default value is `-1`, which denotes no limit.
>
> * sideband.httptransport.socketTimeout
>
>   Defines, in milliseconds, the sideband socket timeout. The default value is `30000`.
>
> * sideband.httptransport.ioThreads
>
>   Defines the number of I/O threads for the sideband host. The default value is `0`, which denotes that PingAccess should automatically calculate the appropriate number of I/O threads for the host.
>
> > **Collapse: Learn more**
> >
> > * Learn more about how to configure a sideband client in the user interface in [Sideband Clients](../pingaccess_user_interface_reference_guide/pa_sideband_clients.html).
> >
> > * Learn more about how some SSL properties are overwritten in FIPS mode in [Managing Federal Information Processing Standards (FIPS) mode](../configuring_and_customizing_pingaccess/pa_fips_mode.html).

## URL filtering settings

> **Collapse: Click to expand or collapse the whole section**
>
> * pa.interceptors.relativepath.strict
>
>   When this property is set to `true`, the incoming URL is matched with the allow list pattern defined in `pa.interceptors.relativepath.decode.regex`. All other request URLs are rejected. The default value is `false`.
>
> * pa.interceptors.relativepath.decode.count
>
>   Defines the number of times the URL is decoded to check for path traversal characters. The default value is `3`.
>
> * pa.interceptors.relativepath.decode.regex
>
>   Defines the regular expression to use when checking for a valid path in an incoming request. The default value is:
>
>   ```
>   [\\p{Po}\\p{N}\\p{Z}\\p{L}\\p{M}\\p{Zs}\\./_\\-\\\\~()\\{\\}\\[\\]]*
>   ```
>
>   |   |                                                                                       |
>   | - | ------------------------------------------------------------------------------------- |
>   |   | This value is double-escaped as required by the `java.util.regex.Pattern` Java class. |
>
> > **Collapse: Learn more**
> >
> > * You can find more information about URL filtering in [Adding rewrite URL rules](../pingaccess_user_interface_reference_guide/pa_adding_rewrite_url_rules.html).

## Monitoring

> **Collapse: Click to expand or collapse the whole section**
>
> * pa.mbean.site.connection.pool.enable
>
>   When set to `true`, enables Java Management Extensions (JMX) *(tooltip: \<div class="paragraph">
>   \<p>Java technology that provides tools for managing and monitoring applications, devices, system objects, and service-oriented networks.\</p>
>   \</div>)* read-only access to backend connection pools. This can be useful when troubleshooting latency issues because it provides information about requests that are waiting for a connection to targets in a site when `maxConnections` isn't unlimited. The default value is `false`.
>
> * enable.detailed.heartbeat.response
>
>   When enabled, this setting enables a customizable heartbeat response to be returned. When disabled, the heartbeat endpoint returns a `200 OK` response. The default value is `false`.
>
> * pa.statistics.window\.seconds
>
>   If the `enable.detailed.heartbeat.response` property is set to `true`, this property sets the number of seconds back to collect response statistics. A value less than `1` disables collection. The default value is `0`.
>
> > **Collapse: Learn more**
> >
> > * You can find more information about monitoring in the [PingAccess Monitoring Guide](../pingaccess_monitoring_guide/pa_monitoring_guide.html).

## TLS/SSL

> **Collapse: Click to expand or collapse the whole section**
>
> * tls.default.protocols
>
>   Defines the default protocols used for HTTPS communication. The default value is `TLSv1.1, TLSv1.2, TLSv1.3`.
>
> * tls.default.cipherSuites
>
>   Defines the default set of ciphers used for HTTPS communication. The default value is:
>
>   ```
>   TLS_CHACHA20_POLY1305_SHA256,\
>   TLS_AES_256_GCM_SHA384,\
>   TLS_AES_128_GCM_SHA256,\
>   TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,\
>   TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,\
>   TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256,\
>   TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256,\
>   TLS_RSA_WITH_AES_128_GCM_SHA256,\
>   TLS_RSA_WITH_AES_128_CBC_SHA256,\
>   TLS_DHE_RSA_WITH_AES_128_GCM_SHA256,\
>   TLS_EMPTY_RENEGOTIATION_INFO_SCSV
>   ```
>
>   |   |                                                                                                                                                                                                                                                                                                                              |
>   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | Legacy browsers might require the addition of SHA1-based ciphers to negotiate a cipher suite with the server. In this case, add the following ciphers to the `run.properties` file and restart PingAccess:- `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`
>
>   - `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`
>
>   - `TLS_RSA_WITH_AES_128_CBC_SHA` |
>
> * clusterconfig.ssl.protocols
>
>   Defines the protocols used for communication with HTTPS ports in a clustered configuration. The default value is `$\{tls.default.protocols}`, which uses the protocols specified by the `tls.default.protocols` property.
>
> * clusterconfig.ssl.ciphers
>
>   Defines the type of cryptographic ciphers available for use with HTTPS ports in a clustered configuration. The default value is `$\{tls.default.cipherSuites}`, which uses the ciphers specified by the `tls.default.cipherSuites` property.
>
> * site.ssl.protocols
>
>   Defines the protocols used for communication with site HTTPS ports. There is no default value. When not specified, PingAccess uses the protocols defined in the Java Development Kit (JDK) *(tooltip: \<div class="paragraph">
>   \<p>A development environment for building applications and components using Java.\</p>
>   \</div>)*.
>
> * site.ssl.ciphers
>
>   Defines the type of cryptographic ciphers available for use with site HTTPS ports. There is no default value. When not specified, PingAccess uses the protocols defined in the JDK.
>
> * pf.ssl.protocols
>
>   Defines the protocols used for communication with PingFederate HTTPS ports. There is no default value. When not specified, PingAccess uses the protocols defined in the JDK.
>
> * pf.ssl.ciphers
>
>   Defines the type of cryptographic ciphers available for use with PingFederate HTTPS ports. There is no default value. When not specified, PingAccess uses the protocols defined in the JDK.
>
> * provider.ssl.protocols
>
>   Defines the protocols used for communication with provider HTTPS ports. There is no default value. When not specified, PingAccess uses the protocols defined in the JDK.
>
> * provider.ssl.ciphers
>
>   Defines the type of cryptographic ciphers available for use with provider HTTPS ports. There is no default value. When not specified, PingAccess uses the protocols defined in the JDK.
>
> * as.ssl.protocols
>
>   Defines the protocols used for communication with authorization server HTTPS ports. There is no default value. When not specified, PingAccess uses the protocols defined in the JDK.
>
> * as.ssl.ciphers
>
>   Defines the type of cryptographic ciphers available for use with authorization server HTTPS ports. There is no default value. When not specified, PingAccess uses the protocols defined in the JDK.
>
> * p14c.ssl.protocols
>
>   Defines the protocols used for communication with PingOne. There is no default value. When not specified, PingAccess uses the protocols defined in the JDK.
>
> * p14c.ssl.ciphers
>
>   Defines the type of cryptographic ciphers available for use with PingOne. There is no default value. When not specified, PingAccess uses the protocols defined in the JDK.
>
> * thirdpartyservice.ssl.protocols
>
>   Defines the protocols used for communication with third-party services. There is no default value. When not specified, PingAccess uses the protocols defined in the JDK.
>
> * thirdpartyservice.ssl.ciphers
>
>   Defines the type of cryptographic ciphers available for use with third-party services. There is no default value. When not specified, PingAccess uses the protocols defined in the JDK.
>
> > **Collapse: Learn more**
> >
> > * You can find more information about the use of TLS/SSL settings for security in the [PingAccess Hardening Guide](https://support.pingidentity.com/s/article/PingAccess-Security-Hardening-Guide).
> >
> > * Learn more about how some TLS properties are overwritten in FIPS mode in [Managing Federal Information Processing Standards (FIPS) mode](../configuring_and_customizing_pingaccess/pa_fips_mode.html).

## POST preservation properties

> **Collapse: Click to expand or collapse the whole section**
>
> * pa.oidc.post.preservation.encrypt
>
>   When enabled, PingAccess preserves POST data through a redirection to PingFederate for authentication is encrypted on the client to be used after the authentication is successful. The default value is `false`.
>
> * pa.oidc.post.preservation.maxRequestBodySize
>
>   Defines, in bytes, the maximum size of the request body for POST preservation. The default value is `8192`.
>
> * pa.oidc.post.preservation.paramsAttributeName
>
>   Used to store the encoded or encrypted POST payload in the browser session storage during POST preservation. The default value is `postParams`.
>
> > **Collapse: Learn more**
> >
> > * Learn more about the use of POST preservation in system templates meant to provide information to the end user in [User-facing page customization reference](../configuring_and_customizing_pingaccess/pa_user_facing_page_customization_ref.html).
> >
> > * Learn more about the use of POST preservation in system templates meant to provide localized versions of user-facing status messages generated by PingAccess in [User-facing page localization reference](../configuring_and_customizing_pingaccess/pa_user_facing_page_localization_ref.html).
> >
> > * Learn more about the use of POST preservation in web sessions in the [PingAccess User Interface Reference Guide](../pingaccess_user_interface_reference_guide/pa_ui_ref_guide.html).

## Configuration database and key store settings

> **Collapse: Click to expand or collapse the whole section**
>
> * derby.language.statementCacheSize
>
>   Defines the number of statements that are stored in memory. The default value is `500`.
>
> * derby.storage.pageCacheSize
>
>   Defines the number of pages cached in memory. The default value is `1000`.
>
> * pa.trust.keystore.type
>
>   Defines the truststore type for the `$JAVA_HOME/lib/security/cacerts` keystore. The default value is `JKS`.
>
>   |   |                                                                                     |
>   | - | ----------------------------------------------------------------------------------- |
>   |   | PKCS#12 isn't supported if you're using FIPS mode, because it isn't FIPS-compliant. |
>
> * pa.trust.keystore.path
>
>   Defines the path for the `$JAVA_HOME/lib/security/cacerts` keystore. The default value is `${java.home}/lib/security/cacerts`.
>
> * pa.keystore.pw
>
>   Defines the password for the truststore configured in the `pa.trust.keystore.path` property. The value is encrypted.
>
> > **Collapse: Learn more**
> >
> > * Learn more about the initial database settings in [Installing and Uninstalling PingAccess](../installing_and_uninstalling_pingaccess/pa_installing_and_uninstalling_pa.html).
> >
> > * Learn more about adjusting PingAccess settings for specific environments in the [Performance Tuning Reference Guide](pa_performance_tuning.html).
> >
> > * Learn more about how the native Apache Derby properties are used in the [Apache Derby: Documentation](https://db.apache.org/derby/manuals/) in the Apache documentation.

## PingFederate administration integration properties

> **Collapse: Click to expand or collapse the whole section**
>
> * pf.api.maxRetries
>
>   Defines the maximum number of retries PingAccess attempts to make to the PingFederate server before declaring the server unavailable. The default value is `0`.
>
> * pf.api.socketTimeout
>
>   Defines, in milliseconds, the socket timeout for the PingFederate API endpoint. The default value is `5000`.
>
> * pf.api.maxConnections
>
>   Defines the maximum number of connections PingAccess will establish to the PingFederate API endpoint. The default value is `-1`, which means there is no limit.
>
> * pf.api.keepAliveTimeout
>
>   Defines, in milliseconds, the keep alive timeout for the PingFederate API. The default value is `30000`.
>
> * pf.api.readTimeout
>
>   Defines, in milliseconds, how long the API will wait for responses from PingFederate when making calls to the PingFederate administrative API. The default value is `-1`, which means there is no limit.
>
> > **Collapse: Learn more**
> >
> > You can find more information about using PingAccess with PingFederate in:
> >
> > * [Configure PingFederate as the token provider for PingAccess](../token_providers/pa_configure_pf_as_the_token_provider_for_pa.html).
> >
> > * [PingAccess User Interface Reference Guide](../pingaccess_user_interface_reference_guide/pa_ui_ref_guide.html).

## Administrative console settings

> **Collapse: Click to expand or collapse the whole section**
>
> * pa.backup.filesToKeep
>
>   Defines the number of backup files to preserve when the administrator authenticates to PingAccess. The default value is `25`. A value of `0` disables the creation of backup files.
>
>   |   |                                                                                                                                                                                                                   |
>   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | Disabling the creation of backup files can speed up the sign-on process in large environments. If you disable the creation of backup files, use the administrative API backup endpoint to create regular backups. |
>
> * pa.admin.user.password.regex
>
>   Defines the regex that controls password complexity for the administrative console. The default value is:
>
>   ```
>   ((?=.\\d)(?=.[a-z])(?=.*[A-Z]).{8,20})
>   ```
>
> * pa.admin.user.password.error.message
>
>   Defines the message returned when password complexity isn't satisfied. The default value is `Password must be at least 8 characters in length, contain one upper-case letter, one lower-case letter and one digit`.
>
> * pa.admin.test.connections
>
>   A boolean property that allows the PingAccess administrative console to make HTTP calls to validate that it can reach PingFederate and sites when the user configures them. The default value is `true`.
>
> * account.locking.max.consecutive.failures
>
>   Defines the maximum number of failed sign-on attempts before locking the account when using basic authentication in the administrative console or administrative REST APIs. The default value is `3`.
>
> * account.locking.max.lockout.period
>
>   Defines, in minutes, the amount of time to lock an account out from the administrative interfaces after exceeding the `account.locking.max.consecutive.failures`. The default value is `1`.
>
> > **Collapse: Learn more**
> >
> > * You can find more information about PingAccess administration in the [PingAccess User Interface Reference Guide](../pingaccess_user_interface_reference_guide/pa_ui_ref_guide.html).

## EHCache configuration properties

> **Collapse: Click to expand or collapse the whole section**
>
> * pa.ehcache.PingFederateReferenceTokenCache.maxEntriesLocalHeap
>
>   Defines the maximum number of entries in the local heap for OAuth *(tooltip: \<div class="paragraph">
>   \<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
>   \</div>)* tokens. The default value is `10000`.
>
> * pa.ehcache.PingFederateReferenceTokenCache.timeToIdleSeconds
>
>   Defines, in seconds, the time an entry in the OAuth token cache can be idle before it is expired. The default value is `0`.
>
> * pa.ehcache.PingFederateReferenceTokenCache.timeToLiveSeconds
>
>   Defines, in seconds, the maximum time an entry can be in the OAuth token cache. The default value is `0`.
>
> * pa.ehcache.ServiceTokenCache.maxEntriesLocalHeap
>
>   Defines the maximum number of entries in the local heap for token mediation. The default value is `10000`.
>
> * pa.ehcache.ServiceTokenCache.timeToIdleSeconds
>
>   Defines, in seconds, the time an entry in the token mediation cache can be idle before it is expired. The default value is `1800`.
>
> * pa.ehcache.ServiceTokenCache.timeToLiveSeconds
>
>   Defines, in seconds, the maximum time an entry can be in the token mediation cache. The default value is `14400`.
>
> * pa.ehcache.PATokenValidationCache.maxEntriesLocalHeap
>
>   Defines the maximum number of entries in the local heap for decryption of signed or encrypted PingAccess tokens. The default value is `10000`.
>
> * pa.ehcache.PATokenValidationCache.timeToIdleSeconds
>
>   Defines, in seconds, the time an entry in the token validation cache can be idle before it is expired. The default value is `120`.
>
> * pa.ehcache.PATokenValidationCache.timeToLiveSeconds
>
>   Defines, in seconds, the maximum time an entry can be in the token validation cache. The default value is `300`.
>
> * pa.ehcache.PFSessionValidationCache.maxEntriesLocalHeap
>
>   Defines the maximum number of entries in the local heap for the session validation cache. The default value is `10000`.
>
> * pa.ehcache.PFSessionValidationCache.timeToIdleSeconds
>
>   Defines, in seconds, the time an entry in the session validation cache can be idle before it expires. The default value is `120`.
>
> * pa.ehcache.PFSessionValidationCache.timeToLiveSeconds
>
>   Defines, in seconds, the maximum time an entry can be in the session validation cache. The default value is `300`.
>
> * pa.ehcache.PAWamUserAttributesCache.maxEntriesLocalHeap
>
>   Defines the maximum number of entries in the local heap for the PingAccess Web Access Management (WAM) user attribute cache. The default value is `10000`.
>
> * pa.ehcache.PAWamUserAttributesCache.timeToIdleSeconds
>
>   Defines, in seconds, the time an entry in the PingAccess WAM user attribute cache can be idle before it is expired. The default value is `120` seconds.
>
> * pa.ehcache.PAWamUserAttributesCache.timeToLiveSeconds
>
>   Defines, in seconds, the maximum time an entry can be in the PingAccess WAM user attribute cache. The default value is `300` seconds.
>
> * pa.ehcache.AuthTokenCache.maxEntriesLocalHeap
>
>   Defines the maximum size of the JSON Web Token (JWT) *(tooltip: \<div class="paragraph">
>   \<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>
>   \</div>)* identity mapping token cache used when sending tokens to a protected site. The default value is `10000`.
>
> * pa.ehcache.SessionStateCache.maxEntriesLocalHeap
>
>   Defines the maximum size of the identity attribute entry cache when the user's attributes are stored on the server rather than as a cookie. The default value is `10000`.
>
> * pa.ehcache.AzureGroupNameCache.maxEntriesLocalHeap
>
>   Defines the maximum number of entries in the local heap for the Azure group name cache. The default value is `10000`.
>
> > **Collapse: Learn more**
> >
> > * You can find more information about EHCache configuration in the [Clustering Reference Guide](pa_clustering_ref_guide.html).

## Security headers properties

> **Collapse: Click to expand or collapse the whole section**
>
> * admin.headers
>
>   Additional headers added to responses from the PingAccess administrative console and the administrative API interface. Define header values using the `admin.header` prefix. The default value is:
>
>   ```
>   X-Frame-Options,X-XSS-Protection,X-Content-Type-Options,Strict-Transport-Security,Content-Security-Policy
>   ```
>
>   |   |                                                                                                                                                                                                                                             |
>   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | `Content-Security-Policy` might be omitted if PingAccess was upgraded with template customizations. To enable for this case, add the `Content-Security-Policy` value to this property and uncomment `admin.header.Content-Security-Policy`. |
>
> * admin.header.X-Frame-Options
>
>   Sets the parameters for the `X-Frame-Options` HTTP response header sent to the browser when an admin is interacting with the administrative console. The default value is `DENY`.
>
>   Learn more about this header and its potential values in [x-frame-options](https://html.spec.whatwg.org/multipage/document-lifecycle.html#x-frame-options).
>
> * admin.header.X-XSS-Protection
>
>   Sets the parameters for the `X-XSS-Protection` HTTP response header sent to the browser when an admin is interacting with the administrative console. The default value is `1; mode=block`.
>
> * admin.header.X-Content-Type-Options
>
>   Sets the parameters for the `X-Content-Type-Options` response header sent to the browser when an admin is interacting with the administrative console. The default value is `nosniff`.
>
> * admin.header.Content-Security-Policy
>
>   Sets the parameters for the `Content-Security-Policy` response header sent by PingAccess in response to API calls. The default value is:
>
>   ```
>   default-src 'self'; style-src 'self' \$\\{cspNonce\\}; \
>     script-src 'self' \$\\{cspNonce\\}; font-src 'self' data:; img-src 'self' data:; object-src 'none'; base-uri 'self';
>   ```
>
>   |   |                                                                                               |
>   | - | --------------------------------------------------------------------------------------------- |
>   |   | This property might be commented out if PingAccess was upgraded with template customizations. |
>
> * admin.header.Strict-Transport-Security
>
>   Sets the parameters for the `Strict-Transport-Security` response header sent to the browser when an administrator is interacting with the administrative console. This property is commented out by default and should be enabled only if the admin and engine use different host names. The default value is `max-age=31536000; includeSubDomains`.
>
> * agent.assets.headers
>
>   Additional headers added to responses from PingAccess agents. Header values are defined using the `agent.assets.header` prefix. The default value is `X-Frame-Options`.
>
> * agent.assets.header.X-Frame-Options
>
>   Sets the parameters for the `X-Frame-Options` HTTP response header sent to the browser using the agent when responding to a request for an asset used by a PingAccess template. The default value is `DENY`.
>
>   Learn more about this header and its potential values in [x-frame-options](https://html.spec.whatwg.org/multipage/document-lifecycle.html#x-frame-options).
>
> * agent.error.headers
>
>   Additional headers added to error responses from PingAccess agents. Header values are defined using the `agent.error.header` prefix. The default value is `X-Frame-Options, Content-Security-Policy`.
>
>   |   |                                                                                                                                                                                                                                                   |
>   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | `Content-Security-Policy` might be omitted if PingAccess was upgraded with template customizations. To enable for this case, add the `Content-Security-Policy` value to this property and uncomment `agent.error.header.Content-Security-Policy`. |
>
> * agent.error.header.Content-Security-Policy
>
>   Sets the parameters for the `Content-Security-Policy` HTTP response header sent to the browser using the agent when responding with a PingAccess error template. The default value is:
>
>   ```
>   default-src 'self'; style-src 'self' \$\\{cspNonce\\}; \
>     script-src 'self' \$\\{cspNonce\\}; font-src 'self' data:; object-src 'none'; base-uri 'self';
>   ```
>
>   |   |                                                                                               |
>   | - | --------------------------------------------------------------------------------------------- |
>   |   | This property might be commented out if PingAccess was upgraded with template customizations. |
>
> * agent.error.header.X-Frame-Options
>
>   Sets the parameters for the `X-Frame-Options` HTTP response header sent to the browser using the agent when responding with a PingAccess error template. The default value is `DENY`.
>
>   Learn more about this header and its potential values in [x-frame-options](https://html.spec.whatwg.org/multipage/document-lifecycle.html#x-frame-options).
>
> * engine.assets.headers
>
>   Additional headers added to responses from the PingAccess engine. Header values are defined using the `engine.assets.header` prefix. The default value is `X-Frame-Options`.
>
> * engine.assets.header.X-Frame-Options
>
>   Sets the parameters for the `X-Frame-Options` HTTP response header sent to the browser using the engine when responding to a request for an asset used by a PingAccess template. The default value is `DENY`.
>
>   Learn more about this header and its potential values in [x-frame-options](https://html.spec.whatwg.org/multipage/document-lifecycle.html#x-frame-options).
>
> * engine.error.headers
>
>   Additional headers added to error responses from the PingAccess engine. Define header values using the `engine.error.header` prefix. The default value is `X-Frame-Options, Content-Security-Policy`.
>
>   |   |                                                                                                                                                                                                                                                                |
>   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | `Content-Security-Policy` might be omitted if PingAccess was upgraded with template customizations. If you want to enable for this case, add the `Content-Security-Policy` value to this property and uncomment `engine.error.header.Content-Security-Policy`. |
>
> * engine.error.header.Content-Security-Policy
>
>   Sets the parameters for the `Content-Security-Policy` HTTP response header sent to the browser using the engine when responding with a PingAccess error template. The default value is:
>
>   ```
>   default-src 'self'; style-src 'self' \$\\{cspNonce\\}; \
>     script-src 'self' \$\\{cspNonce\\}; font-src 'self' data:; object-src 'none'; base-uri 'self';
>   ```
>
>   |   |                                                                                               |
>   | - | --------------------------------------------------------------------------------------------- |
>   |   | This property might be commented out if PingAccess was upgraded with template customizations. |
>
> * engine.error.header.X-Frame-Options
>
>   Sets the parameters for the `X-Frame-Options` HTTP response header sent to the browser using the engine when responding with a PingAccess error template. The default value is `DENY`.
>
>   Learn more about this header and its potential values in [x-frame-options](https://html.spec.whatwg.org/multipage/document-lifecycle.html#x-frame-options).
>
> * sideband.assets.headers
>
>   Additional headers added to responses from PingAccess sideband clients. Define header values using the `sideband.assets.header` prefix. The default value is `X-Frame-Options`.
>
> * sideband.assets.header.X-Frame-Options
>
>   Sets the parameters for the `X-Frame-Options` HTTP response header sent to the browser using the sideband client when responding to a request for an asset used by a PingAccess template. The default value is `DENY`.
>
>   Learn more about this header and its potential values in [x-frame-options](https://html.spec.whatwg.org/multipage/document-lifecycle.html#x-frame-options).
>
> * sideband.error.header.Content-Security-Policy
>
>   Sets the parameters for the `Content-Security-Policy` HTTP response header sent to the browser using the sideband client when responding with a PingAccess error template. The default value is:
>
>   ```
>   default-src 'self'; style-src 'self' \$\\{cspNonce\\}; \
>     script-src 'self' \$\\{cspNonce\\}; font-src 'self' data:; object-src 'none'; base-uri 'self';
>   ```
>
>   |   |                                                                                               |
>   | - | --------------------------------------------------------------------------------------------- |
>   |   | This property might be commented out if PingAccess was upgraded with template customizations. |
>
> * sideband.error.headers
>
>   Additional headers added to error responses from PingAccess sideband clients. Define header values using the `sideband.error.header` prefix. The default value is `X-Frame-Options,Content-Security-Policy`.
>
>   |   |                                                                                                                                                                                                                                                      |
>   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | `Content-Security-Policy` might be omitted if PingAccess was upgraded with template customizations. To enable for this case, add the `Content-Security-Policy` value to this property and uncomment `sideband.error.header.Content-Security-Policy`. |
>
> * sideband.error.header.X-Frame-Options
>
>   Sets the parameters for the `X-Frame-Options` HTTP response header sent to the browser using the sideband client when responding with a PingAccess error template. The default value is `DENY`.
>
>   Learn more about this header and its potential values in [x-frame-options](https://html.spec.whatwg.org/multipage/document-lifecycle.html#x-frame-options).
>
> * pf.redirect.use.default.csp
>
>   Determines whether PingAccess uses the default CSP for HTML authentication challenge responses (ACRs) for web apps. The default value is `true`.
>
>   If you set the `pf.redirect.use.default.csp` property to `false`, you can use the `pf.redirect.headers` to set the CSP that PingAccess uses.
>
>   |   |                                                                                                                                                               |
>   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | Make sure to use the `pf.redirect.headers` to configure a value if you set `pf.redirect.use.default.csp` to `false`. Otherwise, PingAccess won't use any CSP. |
>
> * pf.redirect.headers
>
>   Additional headers added to the redirection response that sends the client to PingFederate for authentication.
>
>   These headers are added when using the **SPA Support Disabled** authentication challenge policy (ACP), the global PingFederate Redirect Headers Appender challenge response filter, or an application that's configured without an ACP and has SPA support disabled.
>
>   Define header values using the `pf.redirect.header` prefix. The default value is `X-Frame-Options,Content-Security-Policy`.
>
>   |   |                                                                                                                                                                                                                                                               |
>   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | `Content-Security-Policy` might be omitted if PingAccess was upgraded with template customizations. If you want to enable for this case, add the `Content-Security-Policy` value to this property and uncomment `pf.redirect.header.Content-Security-Policy`. |
>
> * pf.redirect.header.Content-Security-Policy
>
>   Sets the parameters for the `Content-Security-Policy` HTTP response header sent when the user is redirected to PingFederate to authenticate. The default value is:
>
>   ```
>   default-src 'self'; style-src 'self' \$\\{cspNonce\\}; \
>     script-src 'self' \$\\{cspNonce\\}; font-src 'self' data:; object-src 'none'; base-uri 'self';
>   ```
>
>   |   |                                                                                               |
>   | - | --------------------------------------------------------------------------------------------- |
>   |   | This property might be commented out if PingAccess was upgraded with template customizations. |
>
> * pf.redirect.header.X-Frame-Options
>
>   Sets the parameters for the `X-Frame-Options` value sent when the user is redirected to PingFederate to authenticate. The default value is `DENY`.
>
>   Learn more about this header and its potential values in [x-frame-options](https://html.spec.whatwg.org/multipage/document-lifecycle.html#x-frame-options).
>
> * rule.error.headers
>
>   Additional headers added to responses that result from policy rule results. Define header values using the `rule.error.header` prefix. The default value is `Content-Security-Policy`.
>
>   |   |                                                                                                                                                                                                                                                  |
>   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
>   |   | `Content-Security-Policy` might be omitted if PingAccess was upgraded with template customizations. To enable for this case, add the `Content-Security-Policy` value to this property and uncomment `rule.error.header.Content-Security-Policy`. |
>
> * rule.error.header.Content-Security-Policy
>
>   Sets the parameters for the `Content-Security-Policy` HTTP response header sent to the browser when the response is generated by a rule failure. The default value is:
>
>   ```
>   default-src 'self'; style-src 'self' \$\\{cspNonce\\}; \
>     script-src 'self' \$\\{cspNonce\\}; font-src 'self' data:; object-src 'none'; base-uri 'self';
>   ```
>
>   |   |                                                                                               |
>   | - | --------------------------------------------------------------------------------------------- |
>   |   | This property might be commented out if PingAccess was upgraded with template customizations. |
>
> * oauth.error.headers
>
>   Additional headers added to responses that result from requests made to a protected API application that lack a valid OAuth Bearer token. Define header values using the `oauth.error.header` prefix. The default value is `Content-Security-Policy`.
>
>   |   |                                                                                                                                                                                                                                                   |
>   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | `Content-Security-Policy` might be omitted if PingAccess was upgraded with template customizations. To enable for this case, add the `Content-Security-Policy` value to this property and uncomment `oauth.error.header.Content-Security-Policy`. |
>
> * oauth.error.header.Content-Security-Policy
>
>   Sets the parameters for the `Content-Security-Policy` HTTP response header sent to the browser when PingAccess receives a request made to a protected API application that doesn't contain a valid OAuth Bearer token. The default value is:
>
>   ```
>   default-src 'self'; style-src 'self' \$\\{cspNonce\\}; \
>     script-src 'self' \$\\{cspNonce\\}; font-src 'self' data:; object-src 'none'; base-uri 'self';
>   ```
>
>   |   |                                                                                               |
>   | - | --------------------------------------------------------------------------------------------- |
>   |   | This property might be commented out if PingAccess was upgraded with template customizations. |
>
> > **Collapse: Learn more**
> >
> > * Learn more about security headers and the behavior of the administrative API in [PingAccess API endpoints](pa_api_endpoints.html).
> >
> > * Learn more about security headers and administrative console settings in the [PingAccess User Interface Reference Guide](../pingaccess_user_interface_reference_guide/pa_ui_ref_guide.html).
> >
> > * Learn more about security headers and measures to ensure security in the [PingAccess Hardening Guide](https://support.pingidentity.com/s/article/PingAccess-Security-Hardening-Guide).

## Localization settings

> **Collapse: Click to expand or collapse the whole section**
>
> * pa.localization.resource.bundle.cache.enable
>
>   When set to `false`, allows language files in `/conf/localization` to be added or modified. When `true`, enables caching of language files and properties. The default value is `true`.
>
> * pa.localization.missing.message.placeholder
>
>   Defines the message used when an error message is unresolvable. There is no default value.
>
> * pa.enable.distributed.tracing
>
>   Enables instrumentation to produce tracing data for requests that pass through PingAccess. PingAccess will also pass current tracing information to supported external systems like PingFederate. The default value is `false`.
>
>   |   |                                                                                                                                                                                                                                                     |
>   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | If you're [running PingAccess as a Windows service](../installing_and_uninstalling_pingaccess/pa_managing_pa_as_a_windows_service.html), you must reinstall the service for changes to the `pa.enable.distributed.tracing` property to take effect. |
>
> > **Collapse: Learn more**
> >
> > * Learn more about localization and customizing PingAccess page templates in [User-facing page customization reference](../configuring_and_customizing_pingaccess/pa_user_facing_page_customization_ref.html). You can also find more information about the differences between customizable templates and system templates.
> >
> > * Learn more about localizing user-facing system status messages in [User-facing page localization reference](../configuring_and_customizing_pingaccess/pa_user_facing_page_localization_ref.html).
> >
> > * You can find more information on distributed tracing in [Distributed tracing](../troubleshooting/pa_distributed_tracing.html).

## Cert rotation

> **Collapse: Click to expand or collapse the whole section**
>
> * cert.rotation.transition.window\.ttl.seconds
>
>   Defines, in seconds, how long the config query certificate rotation window stays open. The default value is `300`. While the config query certificate rotation window is open, you can't assign another key pair to the config query listener.
>
>   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
>   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | The config query certificate rotation window closes when all registered PingAccess engines have confirmed the new cert fingerprint or the amount of time specified by the `cert.rotation.transition.window.ttl.seconds` property elapses, whichever comes first. The window doesn't close if the admin restarts the console.- If the primary console goes offline mid-rotation, the replica admin can continue to serve both certificates.
>
>   - If an engine node is offline for the entire rotation window or doesn't complete rotating the cert before the TTL elapses, you must update the `bootstrap.properties` file manually, then restart the node, as described in steps 8 - 9 in [Configuring engine nodes](../pingaccess_user_interface_reference_guide/pa_configuring_engine_nodes.html). |
>
> > **Collapse: Learn more**
> >
> > * Learn more in [Automatic key rotation for config query listeners](../pingaccess_user_interface_reference_guide/pa_assigning_key_pairs.html#autorotation).

---

---
title: Configuring a PingAccess cluster
description: Install and configure PingAccess on each node in a cluster, including the administrative node, a replica administrative node, and one or more engine nodes.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_configuring_a_pa_cluster
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_configuring_a_pa_cluster.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 26, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Configuring a PingAccess cluster

Install and configure PingAccess on each node in a cluster, including the administrative node, a replica administrative node, and one or more engine nodes.

## About this task

The initial node you configure becomes the administrative node, which you will use to configure the rest of the cluster.

|   |                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Setting the `pa.operational.mode` property on each node is part of the configuration process. Do not modify this property until directed to do so. |

## Steps

1. Install PingAccess on each cluster node.

2. Configure the administrative node:

   1. Open the `conf/run.properties` file in a text editor and change the `pa.operational.mode` value to `CLUSTERED_CONSOLE`.

      This property is case-sensitive.

   2. Start PingAccess.

   3. Follow steps 1-14 of [Generating new key pairs](../pingaccess_user_interface_reference_guide/pa_generating_new_key_pairs.html) to create a new key pair for the CONFIG QUERY listener. Make the following adjustments to steps 4-5:

      1. To complete step 4, enter the DNS name of the administrative node in the **Common Name** field.

      2. To complete step 5, enter both the DNS name of the replica administrative node and the DNS name of the administrative node in the **Subject Alternative Names** field. Alternately, configure the **Subject Alternative Names** field as a wildcard certificate.

         |   |                                                                                                                                                                                                                                                                                                                                                                                                          |
         | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
         |   | You can use an Internet Protocol (IP) *(tooltip: \<div class="paragraph">&#xA;\<p>The method by which data is sent across the internet from the source host to the destination host.\</p>&#xA;\</div>)* address as the common name or in the **Subject Alternative Names** field, as long as those values are used in the administrative node fields on the **Administrative Nodes** configuration page. |

         |   |                                                                                      |
         | - | ------------------------------------------------------------------------------------ |
         |   | You will need this key pair in step 3a to set up the replica administrative console. |

   4. Follow steps 1-4 of [Assigning key pairs to HTTPS listeners](../pingaccess_user_interface_reference_guide/pa_assigning_key_pairs_to_https_listeners.html) to assign the key pair you just created to the CONFIG QUERY listener.

   5. Follow steps 1-6 in [Configuring administrative nodes](../pingaccess_user_interface_reference_guide/pa_configuring_admin_nodes.html) to configure the administrative node settings, then review the *What to do next* section. Make the following adjustment to step 2:

      1. To complete step 2, define the primary administrative node as a `host:port` pair in the **Host** field.

         |   |                                                                                                                                                                                                                     |
         | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
         |   | The host you specify must be a resolvable DNS name for the node or the node's IP address. The port must be the TCP port that PingAccess listens to for the administrative interface. By default, this port is 9090. |

   6. Follow steps 1-14 of [Generating new key pairs](../pingaccess_user_interface_reference_guide/pa_generating_new_key_pairs.html) to create a new key pair for the ADMIN listener. Make the following adjustments to steps 4-5:

      1. To complete step 4, enter the DNS name of the administrative node in the **Common Name** field.

      2. To complete step 5, enter both the DNS name of the replica administrative node and the DNS name of the administrative node in the **Subject Alternative Names** field. Alternately, configure the **Subject Alternative Names** field as a wildcard certificate.

         |   |                                                                                                                                                                                                                   |
         | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
         |   | You can use an IP address as the common name or in the **Subject Alternative Names** field as long as those values are used in the administrative node fields on the **Administrative Nodes** configuration page. |

   7. Follow steps 1-4 of [Assigning key pairs to HTTPS listeners](../pingaccess_user_interface_reference_guide/pa_assigning_key_pairs_to_https_listeners.html) to assign the key pair you just created to the ADMIN listener.

   8. Restart PingAccess.

3. Configure the replica administrative node.

   |   |                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you add a replica administrative node after you deploy the cluster, you must update the configuration for each engine node. |

   1. Complete steps 1-11 of [Configuring replica administrative nodes](../pingaccess_user_interface_reference_guide/pa_configuring_replica_administrative_nodes.html). Make the following adjustments to step 2 and step 5:

      1. To complete step 2, the host you specify must be a resolvable DNS name for the node or the node's IP address. The port must be the TCP port that PingAccess listens to for the administrative interface. By default, this port is 9090.

      2. To complete step 5, select the key pair that you created for the CONFIG QUERY listener in step 2c of this topic as the **Replica Administrative Node Trusted Certificate**.

4. Configure the engine nodes in the cluster one at a time. For each engine node:

   1. Complete steps 1-10 of [Configuring engine nodes](../pingaccess_user_interface_reference_guide/pa_configuring_engine_nodes.html).

   2. On the engine node, open the `conf/run.properties` file in a text editor and change the `pa.operational.mode` value to `CLUSTERED_ENGINE`.

   3. Complete step 11 of [Configuring engine nodes](../pingaccess_user_interface_reference_guide/pa_configuring_engine_nodes.html).

      If you specified a proxy for the engine node, see the *What to do next* section also.

   |   |                                                                                                                                                                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Alternately, you can configure each engine node with an auto-registration file. For more information, see [Configuring engine nodes using an auto-registration file](../pingaccess_user_interface_reference_guide/pa_configuring_engine_nodes_using_an_auto_registration_file.html). |

## Next steps

1. Go to **Settings → System → Clustering** to check your cluster's status. If everything is configured properly, the cluster engine nodes and the replica administrative node should display a green status icon, indicating that the cluster is operational. For more information about status icons, see [Clustering in PingAccess](pa_clustering_ref_guide.html).

2. Optionally, you can configure each node in the cluster to run PingAccess as a service. This set-up prompts PingAccess to run automatically when you start a node. For more information, see [Running PingAccess as a service](../installing_and_uninstalling_pingaccess/pa_running_pa_as_a_service.html) in *Installing and Uninstalling PingAccess*.

---

---
title: Configuring acceptor threads
description: Configure the pool of acceptor threads based on your environment.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_configuring_acceptor_threads
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_configuring_acceptor_threads.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring acceptor threads

Configure the pool of acceptor threads based on your environment.

## About this task

PingAccess uses a pool of threads to respond to HTTP/S requests made to the TCP ports in use. This applies to both administrative and runtime engine listening ports. Acceptor threads read user requests from the administrative or runtime port and pass the requests to worker threads for processing. For performance, only one acceptor thread need be used in most situations. On larger multiple CPU core machines, more acceptors can be used.

To modify the pool of acceptor threads:

## Steps

1. Open the `run.properties` file located in the `conf` directory of your PingAccess deployment.

2. Specify the number of acceptors you want to use on the following lines, where *\<N>* represents the number of acceptor threads:

   * `admin.acceptors=<N>`

   * `engine.http.acceptors=<N>`

   * `agent.http.acceptors=<N>`

---

---
title: Configuring JVM crash log in Java startup
description: Enable or disable the Java Virtual Machine (JVM) crash log.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_configuring_jvm_crash_log_in_java_startup
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_configuring_jvm_crash_log_in_java_startup.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Configuring JVM crash log in Java startup

Enable or disable the Java Virtual Machine (JVM) crash log.

## About this task

The Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">
\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>
\</div>)* crash log is enabled by default. On Windows, the `run.bat` file specifies the JVM crash log location, and on Linux, the `run.sh` file specifies the JVM crash log location.

## Steps

* Edit the `<PA_HOME>/bin/run.bat` file on Windows, or the `<PA_HOME>/bin/run.sh` file on Linux.

  ### Choose from:

  * To disable JVM crash log reporting, comment out the line that specifies the JVM crash log location. For example:

    ```
    #ERROR_FILE="-XX:ErrorFile=$PA_HOME/log/java_error%p.log"
    ```

  * To enable JVM crash log reporting, remove the comment tag and make the line active. For example:

    ```
    ERROR_FILE="-XX:ErrorFile=$PA_HOME/log/java_error%p.log"
    ```

---

---
title: Configuring memory dumps in Java startup
description: You can enable or disable Java Virtual Machine (JVM) memory dump, or change the memory dump's storage location.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_configuring_memory_dumps_in_java_startup
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_configuring_memory_dumps_in_java_startup.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Configuring memory dumps in Java startup

You can enable or disable Java Virtual Machine (JVM) memory dump, or change the memory dump's storage location.

## About this task

The Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">
\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>
\</div>)* memory dump is disabled by default. On Windows, the `run.bat` file specifies the memory dump location, and on Linux, the `run.sh` file specifies the memory dump location.

## Steps

* Edit `<PA_HOME>/bin/run.bat` on Windows, or `<PA_HOME>/bin/run.sh` on Linux.

  ### Choose from:

  * To enable JVM memory dump, remove the comment tag on the line that specifies the JVM memory dump location. For example:

    ```
    HEAP_DUMP="-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=$PA_HOME/log"
    ```

  * To disable JVM memory dump, comment out the line. For example:

    ```
    #HEAP_DUMP="-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=$PA_HOME/log"
    ```