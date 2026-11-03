---
title: Administrative API endpoints
description: PingAccess ships with interactive documentation for both developers and non-developers to explore the PingAccess application programming interface (API) endpoints, view a reference of the metadata for each API, and experiment with API calls.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_admin_api_endpoints
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_admin_api_endpoints.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 20, 2026
section_ids:
  admin-api-documentation-swagger-ui-specifications: Admin API documentation Swagger-UI specifications
---

# Administrative API endpoints

PingAccess ships with interactive documentation for both developers and non-developers to explore the PingAccess application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* endpoints, view a reference of the metadata for each API, and experiment with API calls.

PingAccess APIs are REST APIs that provide complete administrative capabilities of the product. They can be called from custom applications or from command line tools, such as cURL.

These endpoints are only available on the `admin.port` defined in the `/pa-admin-api/v3/api-docs/<PA_HOME>/conf/run.properties` file. For example, https\://*\<PA_HOME>*:*\<PORT>*/pa-admin-api/v3/api-docs/.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you selected the **Use context root as reserved resource base path** checkbox in your PingAccess application, this feature creates an instance of any reserved PingAccess resources under the application's context root. As such, the context root of the application needs to prepend the reserved context application root (`/pa` by default) in any file paths that reference it. For example, if the context root of your application is `myApp`, the file path would start with `/myApp/pa`. |

|   |                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | For enhanced API security, you must include `X-XSRF-Header: PingAccess` in all requests and use the `application/json` content type for `PUT` and `POST` requests. |

## Admin API documentation Swagger-UI specifications

The Swagger-UI component that displays the PingAccess admin API documentation uses OpenAPI specification (OAS) 2.0.

|   |                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The specification that the PingAccess admin API docs used previously, Swagger 1.2, has been deprecated. The Swagger 1.2 specification is still available at https\://*\<PA_HOME>*:*\<PORT>*/pa-admin-api/v3/api-docs/pa/api-docs.json but might be removed from future versions of PingAccess. |

You can find the PingAccess admin API's OAS 2.0 specifications at either of the following:

* https\://*\<PA_HOME>*:*\<PORT>*/pa-admin-api/v3/api-docs/pa/api-docs-v2.json

* https\://*\<PA_HOME>*:*\<PORT>*/pa-admin-api/v3/api-docs/pa/api-docs-v2.yaml

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
title: Increasing file descriptor limits (systemd)
description: Increase file descriptor limits in a systemd environment to enable PingAccess to handle a high volume of concurrent requests.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_increasing_file_descriptor_limits_systemd
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_increasing_file_descriptor_limits_systemd.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
section_ids:
  steps: Steps
---

# Increasing file descriptor limits (systemd)

Increase file descriptor limits in a systemd environment to enable PingAccess to handle a high volume of concurrent requests.

## Steps

1. Edit the `/etc/systemd/system/pingaccess.service` file.

2. Modify the following line under the `[Service]` section:

   ```
   LimitNOFILE=<value>
   ```

   *\<value>* is the new value. The default value of 65536 (64K) should be sufficient for most environments.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The number of open file descriptors is limited by the physical memory available to the host. You can determine this limit with the following command:```
   cat /proc/sys/fs/file-max
   ```If the file-max value is significantly higher than the 65536 limit, consider increasing the file descriptor limit to between 10% and 15% of the system-wide file descriptor limit. For example, if the file-max value is 810752, you can set the file descriptor limit to 100000. If the file-max value is lower than 65536, the host is likely not sized appropriately for PingAccess. |

3. Run the following command as root:

   ```
   systemctl daemon-reload
   ```

4. Restart the PingAccess service.

---

---
title: Increasing file descriptor limits (systemv)
description: Increase file descriptor limits in a systemv environment to enable PingAccess to handle a high volume of concurrent requests.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_increasing_file_descriptor_limits_systemv
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_increasing_file_descriptor_limits_systemv.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
section_ids:
  steps: Steps
---

# Increasing file descriptor limits (systemv)

Increase file descriptor limits in a systemv environment to enable PingAccess to handle a high volume of concurrent requests.

## Steps

1. Edit the `/etc/security/limits.conf` file.

2. Add or modify the following lines:

   ```
   <pingAccessAccount>  soft nofile  <value>
   <pingAccessAccount>  hard nofile  <value>
   ```

   `<pingAccessAccount>` is the user account used to run the PingAccess java process, or `*` for all users, and *\<value>* is the new value. A value of 65536 (64K) should be sufficient for most environments.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The number of open file descriptors is limited by the physical memory available to the host. You can determine this limit with the following command:```
   cat /proc/sys/fs/file-max
   ```If the file-max value is significantly higher than the 65536 limit, consider increasing the file descriptor limit to between 10% and 15% of the system-wide file descriptor limit. For example, if the file-max value is 810752, you could set the file descriptor limit to 100000. If the file-max value is lower than 65536, the host is likely not sized appropriately for PingAccess. |

---

---
title: Increasing the number of available ephemeral ports
description: Increase the number of available ephemeral ports to prevent deployment issues, particularly in high capacity environments.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_increasing_the_number_of_available_ephemeral_ports
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_increasing_the_number_of_available_ephemeral_ports.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Increasing the number of available ephemeral ports

Increase the number of available ephemeral ports to prevent deployment issues, particularly in high capacity environments.

## About this task

This setting increases the performance and capacity of network, specifically the TCP socket, connectivity, enabling PingAccess to handle a high volume of concurrent requests.

## Steps

1. View the ephemeral ports with the `netsh int ipv4 show dynamicportrange tcp` command.

2. Increase the ephemeral ports with the `netsh int ipv4 set dynamicport tcp start=1025 num=64510` command.

3. Reboot the machine.

4. View and confirm the updated port range with the `netsh int ipv4 show dynamicportrange tcp` command.

---

---
title: Java tuning
description: One of the most important tuning options you can apply to the Java Virtual Machine (JVM) is to configure how much heap (memory for runtime objects) to use.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_java_tuning
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_java_tuning.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
---

# Java tuning

One of the most important tuning options you can apply to the Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">
\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>
\</div>)* is to configure how much heap (memory for runtime objects) to use.

The JVM grows the heap from a specified minimum to a specified maximum. If you have sufficient memory, fix the size of the heap by setting minimum and maximum to the same value. This allows the JVM to reserve its entire heap at startup, optimizing organization and eliminating potentially expensive resizing.

By default, PingAccess fixes the Java heap at 512 megabytes (MB). This is a fairly small footprint and not optimal for supporting higher concurrent user loads over extended periods of activity. If you expect your deployment of PingAccess to serve more than 50 concurrent users, per PingAccess node, if deploying a cluster, increase the heap size.

For more information, see the following topics:

* [Configuring JVM crash log in Java startup](pa_configuring_jvm_crash_log_in_java_startup.html)

* [Configuring memory dumps in Java startup](pa_configuring_memory_dumps_in_java_startup.html)

* [Modifying the Java heap size](pa_modifying_the_java_heap_size.html)

---

---
title: JsonNode object reference
description: The JsonNode object represents the attributes of an identity.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_jsonnode_object_ref
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_jsonnode_object_ref.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  groovy-sample: Groovy sample
  method-summary: Method summary
  remarks: Remarks
---

# JsonNode object reference

The JsonNode object represents the attributes of an identity.

## Groovy sample

```
// Only allow access if the user is in the group "staff"
def groups = exc?.identity?.attributes?.get("groups")

foundGroup = falseif (groups) {
  for (group in groups) {
    if ("staff".equals(group.asText())) {
      foundGroup = truebreak
    }
  }
}

if (foundGroup) {
  pass()
} else {
  fail()
}
```

## Method summary

| Method                                    | Description                                                                                                                                                                                                                                                                                           |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `JsonNode get(String fieldName)`          | Gets the JsonNode representing a field of this JsonNode. This method will return null if no field exists with the specified name.                                                                                                                                                                     |
| `boolean has(String fieldName)`           | Returns true if this JsonNode has a field with the specified name.                                                                                                                                                                                                                                    |
| `java.util.Iterator<String> fieldNames()` | Returns an java.util.Iterator providing access to the names of all the fields of this JsonNode.                                                                                                                                                                                                       |
| `boolean isTextual()`                     | Returns true if this JsonNode represents a string value.                                                                                                                                                                                                                                              |
| `String asText()`                         | Returns a string representation of this JsonNode. If this JsonNode is an array or object, this will return an empty string.                                                                                                                                                                           |
| `int intValue()`                          | Returns an integer representation of this JsonNode. If this JsonNode does not represent a number, 0 is returned.                                                                                                                                                                                      |
| `boolean isArray()`                       | Returns true if this JsonNode is an array.                                                                                                                                                                                                                                                            |
| `boolean isObject()`                      | Returns true if this JsonNode is an object.                                                                                                                                                                                                                                                           |
| `int size()`                              | For an array JsonNode, returns the number of elements in the array. For an object JsonNode, returns the number of fields in the object. 0 otherwise.                                                                                                                                                  |
| `java.util.Iterator<JsonNode>iterator()`  | Returns an java.util.Iterator over all JsonNode objects contained in this JsonNode. For an array JsonNode, the returned java.util.Iterator will iterate over all the elements in the array. For an object JsonNode, the returned java.util.Iterator will iterate over all field values in the object. |

## Remarks

A JsonNode implements java.lang.Iterable*\<JsonNode>* so a for loop can be used to iterate over all the elements in an array JsonNode or the field values in an object JsonNode.

---

---
title: Linux tuning
description: This section describes tuning recommendations for the Linux operating system environment.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_linux_tuning
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_linux_tuning.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# Linux tuning

This section describes tuning recommendations for the Linux operating system environment.

Implement these recommendations to prevent deployment issues, particularly in high capacity environments. The following settings will increase the performance and capacity of the networking, particularly TCP, stack, and file descriptor usage, respectively, enabling PingAccess to handle a high volume of concurrent requests.

For more information, see the following topics:

* [Tuning network and TCP settings](pa_tuning_network_and_tcp_settings.html)

* [Increasing file descriptor limits (systemv)](pa_increasing_file_descriptor_limits_systemv.html)

* [Increasing file descriptor limits (systemd)](pa_increasing_file_descriptor_limits_systemd.html)

---

---
title: Logger object reference
description: This object accesses the Logger object.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_logger_object_ref
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_logger_object_ref.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  configuration: Configuration
  method-summary: Method summary
---

# Logger object reference

This object accesses the Logger object.

## Configuration

PingAccess must be configured to accept logging from Groovy rules.

In the `conf/log4j2.xml` file, uncomment or add the following line to enable debug-level logging from Groovy rules.

```
<AsyncLogger name="GroovyRule" level="DEBUG"/>
```

Uncomment or add the following line to enable info-level logging from the *\<RuleName>* Groovy rule.

```
<AsyncLogger name="GroovyRule.<RuleName>" level="INFO"/>
```

## Method summary

| Method                                          | Description                                                                |
| ----------------------------------------------- | -------------------------------------------------------------------------- |
| `void trace(String format, Object…​ arguments)` | Logs a `TRACE` level message based on the specified format and arguments.  |
| `void debug(String format, Object…​ arguments)` | Logs a `DEBUG` level message based on the specified format and arguments.  |
| `void info(String format, Object…​ arguments)`  | Logs an `INFO` level message based on the specified format and arguments.  |
| `void warn(String format, Object…​ arguments)`  | Logs a `WARN` level message based on the specified format and arguments.   |
| `void error(String format, Object…​ arguments)` | Logs an `ERROR` level message based on the specified format and arguments. |
| `boolean isTraceEnabled()`                      | Checks if the logger instance is enabled for the `TRACE` level.            |
| `boolean isDebugEnabled()`                      | Checks if the logger instance is enabled for the `DEBUG` level.            |
| `boolean isInfoEnabled()`                       | Checks if the logger instance is enabled for the `INFO` level.             |
| `boolean isWarnEnabled()`                       | Checks if the logger instance is enabled for the `WARN` level.             |
| `boolean isErrorEnabled()`                      | Checks if the logger instance is enabled for the `ERROR` level.            |

---

---
title: Logging and Auditing
description: PingAccess uses a high performance, asynchronous logging framework to provide logging and auditing services with the lowest possible impact to overall application performance.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_logging_and_auditing
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_logging_and_auditing.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 16, 2024
section_ids:
  logging: Logging
  auditing: Auditing
---

# Logging and Auditing

PingAccess uses a high performance, asynchronous logging framework to provide logging and auditing services with the lowest possible impact to overall application performance.

## Logging

Modify your logging settings to increase performance.

Although logging is handled by a high performance, asynchronous logging framework, it is more efficient for the system overall to log the minimum amount of information required. Review the [logging section of the documentation](../configuring_and_customizing_pingaccess/pa_logging_configuration.html) and adjust the logging level to the lowest level that suits your needs.

## Auditing

Modify your environment's auditing settings based on your security and performance needs.

As with logging, auditing is provided by the same high performance, asynchronous logging framework. Auditing messages can be written to a database instead of flat files, decreasing file I/O.

If you do not require auditing for interactions with a resource or between PingAccess and PingFederate, it is more efficient to disable audit logging. However, if you do require auditing services and have access to a Relational Database Management System (RDBMS), audit to a database. You will see a decrease in disk I/O, which might result in increased performance, depending on database resources.

---

---
title: Manually promoting the replica administrative node
description: To promote the replica admin manually:
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_manually_promoting_the_replica_admin_node
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_manually_promoting_the_replica_admin_node.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Manually promoting the replica administrative node

## About this task

To promote the replica admin manually:

## Steps

1. Open the `<PA_HOME>/conf/run.properties` file in a text editor.

2. Locate the `pa.operational.mode` line and change the value from `CLUSTERED_CONSOLE_REPLICA` to `CLUSTERED_CONSOLE`.

   These properties are case-sensitive.

   |   |                                                                                                                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Do not restart the replica node during the promotion process. PingAccess can detect and apply this change without a restart, and restarting the node during its promotion can cause file corruption or failure to promote correctly. |

## Next steps

Complete [Reinstating a replica administrative node after failing over](pa_reinstating_a_replica_admin_node_after_failing_over.html).

---

---
title: Matcher usage reference
description: Groovy script rules and OAuth Groovy script rules must end execution with a matcher instance. Matchers provide a framework for establishing declarative rule matching objects.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_matcher_usage_ref
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_matcher_usage_ref.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 26, 2023
section_ids:
  pingaccess-matchers: PingAccess matchers
---

# Matcher usage reference

Groovy script rules and OAuth Groovy script rules must end execution with a matcher instance. Matchers provide a framework for establishing declarative rule matching objects.

You can use a matcher from the list of PingAccess matchers or from the [Hamcrest library](http://hamcrest.org/JavaHamcrest/javadoc/1.3/org/hamcrest/CoreMatchers.html).

* For more information on Hamcrest, see the [Hamcrest Tutorial](http://code.google.com/p/hamcrest/wiki/Tutorial).

* For more information on creating and troubleshooting Groovy scripts, and examples of how you might use Hamcrest matchers instead of PingAccess matchers, see [Groovy Scripts](pa_groovy_scripts.html).

* For more information on PingAccess matchers, review the following examples and tables.

|   |                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Matcher string evaluation is case sensitive unless otherwise specified. In the PingAccess matchers table, case insensitivity is called out in a matcher's description when applicable. |

> **Collapse: Examples**
>
> In the following example, the Groovy script rule inserts a custom HTTP header *(tooltip: \<div class="paragraph">
> \<p>A section of an HTTP request or response that conveys additional information relevant to the client or server in the transaction.\</p>
> \</div>)* and the script ends with a call to the `pass()` matcher. The `pass()` matcher signals that the rule has passed.
>
> ```
> test = "let's get Groovy!"
> exc?.response?.header?.add("X-Groovy", "$test")
> pass()
> ```
>
> In the following example, the OAuth *(tooltip: \<div class="paragraph">
> \<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
> \</div>)* Groovy script rule checks the HTTP method and confirms the OAuth scope, and a matcher is evaluated at the end of each line of execution. The first matcher is the `hasScope()` matcher, which confirms whether the OAuth access token has the `WRITE` scope. If it does, the rule passes.
>
> ```
> //Get the HTTP method name
> def methodName = exc?.request?.method?.methodName()
> if (methodName == "POST") {
>     hasScope("WRITE")
> } else {
>     fail()
> }
> ```
>
> The `fail()` matcher combination is only evaluated when the `methodName` does not equal `POST`. This matcher combination evaluates to false.

## PingAccess matchers

The following table lists the PingAccess matchers available for the [Groovy script rule](../pingaccess_user_interface_reference_guide/pa_adding_groovy_script_rules.html) and the [OAuth Groovy script rule](../pingaccess_user_interface_reference_guide/pa_adding_oauth_groovy_script_rules.html).

> **Collapse: Groovy and OAuth Groovy script rule matchers**
>
> | Matcher                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `pass()`                                                                                                                                              | Signals that the rule has passed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | `fail()`                                                                                                                                              | Signals that the rule has failed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | `inIpRange(String cidr)`                                                                                                                              | Validates the source Internet Protocol (IP) *(tooltip: \<div class="paragraph">&#xA;\<p>The method by which data is sent across the internet from the source host to the destination host.\</p>&#xA;\</div>)* address of the request against the `cidr` string parameter in CIDR notation. When source IP headers defined in the [HTTP Requests](../pingaccess_user_interface_reference_guide/pa_http_requests.html) page are found, the source IP address determined from those headers is used as the source address.For agents, this value is potentially controlled by the override options on the agent settings.**Example:** `inIpRange("127.0.0.1/8")`                                                                                                                                                        |
> | `inIpRange(java.net.InetAddress ipAddress, int prefixSize)`                                                                                           | Validates the source IP address against the `ipAddress` and the `prefixSize` parameters specified individually. When source IP headers defined in the [HTTP Requests](../pingaccess_user_interface_reference_guide/pa_http_requests.html) page are found, the source IP address determined from those headers is used as the source address.For agents, this value is potentially controlled by the override options on the agent settings.**Example:** `inIpRange(InetAddress.getByName("127.0.0.1"),8)`is equivalent to  `inIpRange("127.0.0.1/8")`                                                                                                                                                                                                                                                                |
> | `inIpRange(String cidr, String listValueLocation, boolean fallBackToLastHopIp, String…​ headerNames)`                                                 | Validates the source IP address in the first of the specified `headerNames` using the `cidr` value. Can be specified as part of a Groovy script as a means of overriding the configuration stored in PingAccess for a specific Groovy script rule.Valid values for the `listValueLocation` parameter are `FIRST`, `LAST`, and `ANY`. This parameter controls where, in a multivalued list of source IP addresses, the last source should be taken from. If `ANY` is used, if any of the source IP addresses in a matching header match the CIDR value, the matcher evaluates to `true`.**Example:** `inIpRange("127.0.0.1/8", "LAST", true, "X-Forwarded-For", "Custom-Source-IP")`                                                                                                                                  |
> | `inIpRange(java.net.InetAddress address, int prefixSize, String listValueLocation, boolean fallBackToLastHopIp, String…​ headerName)`                 | Validates the source IP address in the first of the specified `headerNames` using the `address` and `prefixSize` values. In all other respects, this matcher behaves the same as the version that uses a `cidr` value for comparison.**Example:** `inIpRange(InetAddress.getByName("127.0.0.1"), 8, "LAST", true, "X-Forwarded-For", "Custom-Source-IP")`                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | `requestXPathMatches(String xPathString, String xPathValue)`                                                                                          | Validates that the value returned by the `xPathString` parameter is equal to the `xPathValue` parameter.**Example:** `requestXPathMatches("//header[@name='Host']/text()","localhost:3000")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
> | `inTimeRange(String startTime, String endTime)`                                                                                                       | Validates that the current server time is between the `startTime` and `endTime` parameters.**Example:** `inTimeRange("9:00 am","5:00 pm")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
> | `inTimeRange24(String startTime, String endTime)`                                                                                                     | Validates that the current server time is between the specified 24-hour formatted time range between the `startTime` and `endTime` parameters.**Example:** `inTimeRange24("09:00","17:00")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | `requestHeaderContains(String field, String value)`                                                                                                   | Validates that the HTTP header field value is equal to the `value` parameter.**Example:** `requestHeaderContains("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
> | `requestHeaderContains(Map<String, String> fieldValuesMap, boolean caseSensitive)`&#xA;&#xA;This matcher can be case sensitive or case insensitive.   | Validates that all of the HTTP header fields map to the associated value. The first `fieldValuesMap` string contains the HTTP header name, and the second string contains the value to compare the incoming request header value with.The `caseSensitive` parameter determines whether a case-sensitive comparison is performed on the value.The second string in the `fieldValuesMap` supports Java regular expressions.If multiple pairs of strings are present in the `fieldValuesMap` parameter, then all conditions must be met in order for the matcher to pass.**Example:** `requestHeaderContains(['User-Agent':'Mozilla/5.0', 'Cookie':'JSESSIONID'], false)`                                                                                                                                               |
> | `requestPostFormContains(Map<String, String> fieldValuesMap, boolean caseSensitive)`&#xA;&#xA;This matcher can be case sensitive or case insensitive. | Validates that all of the HTTP form fields maps to the associated value. The first `fieldValuesMap` string contains the form header name, and the second string contains the value to compare the incoming request header value with.The `caseSensitive` parameter determines whether a case-sensitive comparison is performed on the value.&#xA;&#xA;This matcher determines whether to use fields passed in the URL or forms with a content-type header of application/x-www-form-urlencoded.The second string in the `fieldValuesMap` supports Java regular expressions.If multiple pairs of strings are present in the `fieldValuesMap` parameter, then all conditions must be met in order for the matcher to pass.**Example:** `requestPostFormContains(['email':'@example.com', 'phonenumber':'720'], false)` |
> | `requestHeaderDoesntContain(String field, String value)`                                                                                              | Validates that the HTTP header field value is not equal to the `value` parameter.**Example:** `requestHeaderDoesntContain("User-Agent", "InternetExplorer")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
> | `requestBodyContains(String value)`                                                                                                                   | Validates that the HTTP body contains the `value` parameter.**Example:** `requestBodyContains("production")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
> | `requestBodyDoesntContain(String value)`                                                                                                              | Validates that the HTTP body does not contain the value parameter.**Example:** `requestBodyDoesntContain("test")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | `containsWebSessionAttribute(String attributeName, String attributeValue)`                                                                            | Validates that the PingAccess token contains the attribute name and value.**Example:** `containsWebSessionAttribute("sub", "sarah")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
> | `containsACRValues(String value)`                                                                                                                     | Validates that the PingAccess token contains a matching ACR value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

The following table lists the PingAccess matchers available to only the [OAuth Groovy script rule](../pingaccess_user_interface_reference_guide/pa_adding_oauth_groovy_script_rules.html).

> **Collapse: OAuth Groovy script rule matchers**
>
> | Matcher                                                                                                                                  | Description                                                                                                         |
> | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
> | `hasScope(String scope)`                                                                                                                 | Validates that the OAuth access token contains the `scope` parameter.**Example:** `hasScope("access")`              |
> | `hasScopes(String…​ scopes)`                                                                                                             | Validates that the OAuth access token contains the list of scopes.**Example:** `hasScopes("access","portfolio")`    |
> | `hasAttribute(String attributeName, String attributeValue)`&#xA;&#xA;This matcher is case insensitive and cannot be made case sensitive. | Checks for an attribute value within the current OAuth2 policy context.**Example:** `hasAttribute("account","joe")` |

---

---
title: MediaType object reference
description: Access the MediaType object.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_mediatype_object_ref
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_mediatype_object_ref.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  method-summary: Method summary
---

# MediaType object reference

Access the MediaType object.

## Method summary

| Method                        | Description                                                     |
| ----------------------------- | --------------------------------------------------------------- |
| `Map getParameters()`         | Returns a list of parameters.                                   |
| `String getBaseType()`        | Returns the media base type.                                    |
| `String getSubType()`         | Returns the media sub type.                                     |
| `String getParameter(String)` | Returns a string containing the value of the request parameter. |
| `String getPrimaryType()`     | Returns the primary media type.                                 |

---

---
title: Method object reference
description: Access the Method object in Groovy exc?.request?.method.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_method_object_ref
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_method_object_ref.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  purpose: Purpose
  groovy-sample: Groovy sample
  method-summary: Method summary
---

# Method object reference

Access the Method object in Groovy `exc?.request?.method`.

## Purpose

The Method object contains the HTTP method name from the request made to an application. The HTTP method is sent on to the site after the rules are evaluated.

## Groovy sample

```
//Retrieve the HTTP Method name and make different decisions based on the method name
def method = exc?.request?.method?.methodName
switch (method) {
     case "GET":
         println("GET")
         break;
     case "POST":
         println("POST")
         break;
     case "PUT":
         println("PUT")
         break;
     case "DELETE":
         println("DELETE")
         break;
default:
     println("DEFAULT")
     pass()
}
```

## Method summary

| Method                 | Description                                                        |
| ---------------------- | ------------------------------------------------------------------ |
| String getMethodName() | Returns the name of the HTTP method, GET, PUT, POST, DELETE, HEAD. |