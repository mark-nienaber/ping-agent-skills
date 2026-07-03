---
title: Adding an API Proxy in Apigee
description: Configure the API Proxy where you want to reach a target endpoint.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_adding_an_api_proxy_in_apigee
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_adding_an_api_proxy_in_apigee.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 28, 2025
section_ids:
  steps: Steps
---

# Adding an API Proxy in Apigee

Configure the API Proxy where you want to reach a target endpoint.

## Steps

1. Go to **API Proxies > Create Proxy** and click the **Reverse Proxy** tab.

2. In the **Name** field, enter a name for the API proxy.

3. In the **Base Path** field, enter the base path of the API.

4. In the **Target (existing API)** field, enter the Uniform Resource Locator (URL) *(tooltip: \<div class="paragraph">
   \<p>Identifies a resource according to its internet location.\</p>
   \</div>)* of the service invoked by the proxy.

5. Click **Next**.

6. In the **Common Policies** section, select **Pass through (no authorization)**.

7. Click **Next**.

8. In the **Optional Deployment** section, select the deployment environment.

9. Click **Create and Deploy**.

---

---
title: Agent for Apache (SLES) Release Notes
description: These release notes summarize the changes in current and previous PingAccess agent for Apache (SLES) updates. Updated April 18, 2025.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_apache_sles_rn
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_apache_sles_rn.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2025
section_ids:
  pingaccess-agent-for-apache-sles-3-0-april-2025: PingAccess Agent for Apache (SLES) 3.0 (April 2025)
  agent-sdk-for-c-compatibility: Agent SDK for C compatibility
  authenticate-the-pingaccess-agent-for-apache-sles-with-a-bearer-token: Authenticate the PingAccess agent for Apache (SLES) with a bearer token
  pingaccess-agent-for-apache-sles-1-6-july-2024: PingAccess Agent for Apache (SLES) 1.6 (July 2024)
  agent-sdk-for-c-compatibility-2: Agent SDK for C compatibility
  cache-multiple-token-types-for-web-api-applications: Cache multiple token-types for Web + API applications
  block-bad-characters-in-apache-and-iis-agent-deployments: Block bad characters in Apache and IIS agent deployments
  pingaccess-agent-for-apache-sles-1-5-2-september-2021: PingAccess Agent for Apache (SLES) 1.5.2 (September 2021)
  agent-sdk-for-c-version-compatibility: Agent SDK for C version compatibility
  override-default-x-forwarded-host-header: Override default X-Forwarded-Host header
  pingaccess-agent-for-apache-sles-1-5-1-april-2021: PingAccess Agent for Apache (SLES) 1.5.1 (April 2021)
  agent-sdk-for-c-compatibility-3: Agent SDK for C compatibility
  fixed-post-preservation-corruption: Fixed POST preservation corruption
  pingaccess-agent-for-apache-sles-1-5-july-2020: PingAccess Agent for Apache (SLES) 1.5 (July 2020)
  agent-sdk-for-c-compatibility-4: Agent SDK for C compatibility
  added-ability-to-send-agent-inventory-information-topingaccess: Added ability to send agent inventory information toPingAccess
  pingaccess-agent-for-apache-sles-1-4-1-february-2020: PingAccess Agent for Apache (SLES) 1.4.1 (February 2020)
  agent-sdk-for-c-compatibility-5: Agent SDK for C compatibility
  fixed-a-potential-security-issue: Fixed a potential security issue
  pingaccess-agent-for-apache-sles-1-4-june-2019: PingAccess Agent for Apache (SLES) 1.4 (June 2019)
  agent-sdk-for-c-compatibility-6: Agent SDK for C compatibility
  use-paa-enabled-inside-a-directory-or-location-container: Use PAA Enabled inside a directory or location container
  set-the-policy-caching-mechanism-in-agent-properties: Set the policy caching mechanism in agent.properties
  manage-agent-processing-for-a-request-based-on-the-note-field: Manage agent processing for a request based on the note field
  fixed-a-potential-security-issue-2: Fixed a potential security issue
  pingaccess-agent-for-apache-sles-1-3-2-november-2018: PingAccess Agent for Apache (SLES) 1.3.2 (November 2018)
  fixed-a-potential-security-issue-3: Fixed a potential security issue
  pingaccess-agent-for-apache-sles-1-3-march-2017: PingAccess Agent for Apache (SLES) 1.3 (March 2017)
  initial-release: Initial release
---

# Agent for Apache (SLES) Release Notes

These release notes summarize the changes in current and previous PingAccess agent for Apache (SLES) updates. Updated April 18, 2025.

|   |                          |
| - | ------------------------ |
|   | Removed SLES 12 support. |

## PingAccess Agent for Apache (SLES) 3.0 (April 2025)

### Agent SDK for C compatibility

Info

Compatible with the Agent SDK for C version 3.0.

### Authenticate the PingAccess agent for Apache (SLES) with a bearer token

New PASDKC-198

Authenticate PingAccess agents to the engine nodes with a stronger authentication method.

|   |                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------- |
|   | To use this feature, you must upgrade to PingAccess 8.2 or later and the PingAccess agent for Apache (SLES) 3.0 or later. |

Learn more in the [PingAccess 8.2 release notes](https://docs.pingidentity.com/pingaccess/8.3/release_notes/pa_release_notes.html#configure-pingaccess-to-allow-agents-to-authenticate-with-a-bearer-token). You can find setup instructions in [Configuring PingAccess agents to use bearer token authentication](../pingaccess_user_interface_reference_guide/pa_configuring_pa_agents_to_use_bearer_token_authn.html) and [Agent SDK for C 3.0 (April 2025)](pa_sdk_for_c_rn.html#sdk-for-c-30).

## PingAccess Agent for Apache (SLES) 1.6 (July 2024)

### Agent SDK for C compatibility

Info

Compatible with the Agent SDK for C version 1.4.

### Cache multiple token-types for **Web + API** applications

New PA-15516

If you use a **Web + API** application, the `vnd-pi-resource-cache` PingAccess agent protocol (PAAP) header now contains an additional path so **Web + API** applications can cache both cookie and authorization header token-types. For more information, see the **Cache multiple token-types for Web + API applications** entry in the PingAccess 8.1 release notes, and the `agent.cache.defaultTokenType` property on the SLES agent configuration page.

|   |                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Existing agent environments ignore the new `vnd-pi-token-cache-oauth-ttl` header and additional paths in the `vnd-pi-resource-cache` header.To see the performance boost, upgrade to PingAccess 8.1 and upgrade to the latest version of the SLES agent. Otherwise, continue to use an earlier agent version. |

### Block bad characters in Apache and IIS agent deployments

New PAA-251

Configure a PingAccess Apache agent or the PingAccess agent for IIS to block requests that contain bad characters in the URI, query parameters, form parameters, or request body without having to reach out to PingAccess for a decision.

Added eight new properties to each agent:

1. `agent.request.block.xss.characters`

2. `agent.request.block.uri.characters`

3. `agent.request.block.query.characters`

4. `agent.request.block.form.characters`

5. `agent.request.block.xss.http.status`

6. `agent.request.block.uri.http.status`

7. `agent.request.block.query.http.status`

8. `agent.request.block.form.http.status`

Learn more in the configuration page for your agent:

* [RHEL agent configuration](pa_apache_rhel_configuration.html)

* [SLES agent configuration](pa_apache_sles_configuration.html)

* [Windows agent configuration](pa_apache_windows_configuration.html)

* [IIS agent configuration](pa_iis_configuration.html)

|   |                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------- |
|   | For large scale or more complex blocking decisions, it's best practice for the agent to reach out to PingAccess for a decision. |

## PingAccess Agent for Apache (SLES) 1.5.2 (September 2021)

### Agent SDK for C version compatibility

Info

Compatible with Agent SDK for C version 1.3.

### Override default `X-Forwarded-Host` header

New PAA-255

Added an option to override the default `X-Forwarded-Host` header with a specified header.

## PingAccess Agent for Apache (SLES) 1.5.1 (April 2021)

### Agent SDK for C compatibility

Info

Compatible with Agent SDK for C version 1.3.

### Fixed POST preservation corruption

Fixed PAA-220

Fixed an issue that caused large bodies sent through POST preservation in an agent deployment to be corrupted.

## PingAccess Agent for Apache (SLES) 1.5 (July 2020)

### Agent SDK for C compatibility

Info

Compatible with Agent SDK for C version 1.3.

### Added ability to send agent inventory information toPingAccess

New PAA-178

Added agent inventory callback API.

## PingAccess Agent for Apache (SLES) 1.4.1 (February 2020)

### Agent SDK for C compatibility

Info

Compatible with Agent SDK for C version 1.2.1.

### Fixed a potential security issue

Security

Fixed a potential security issue.

## PingAccess Agent for Apache (SLES) 1.4 (June 2019)

### Agent SDK for C compatibility

Info

Compatible with Agent SDK for C version 1.2.0.

### Use **PAA Enabled** inside a directory or location container

Improved PAA-57

You can now use the **PAA Enabled** directive inside a directory or location container.

### Set the policy caching mechanism in `agent.properties`

New PAA-75

Added ability to set policy caching mechanism using a property in the `agent.properties` file.

### Manage agent processing for a request based on the note field

New PAA-90

Added ability to enable or disable agent processing for a request based on a note field.

### Fixed a potential security issue

Security

Fixed a potential security issue.

## PingAccess Agent for Apache (SLES) 1.3.2 (November 2018)

### Fixed a potential security issue

Security

Fixed a potential security issue.

## PingAccess Agent for Apache (SLES) 1.3 (March 2017)

### Initial release

Info

Initial release for Apache 2.2 on SUSE Linux Enterprise Server (SLES) 11 and Apache 2.4 on SLES 12.

|   |                                                             |
| - | ----------------------------------------------------------- |
|   | Version is aligned with PingAccess agent for Apache (RHEL). |

---

---
title: Agent SDK directory structure
description: The PingAccess Agent SDK for Java directory contains the following directories:
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_agent_sdk_for_java_directory_structure
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_agent_sdk_for_java_directory_structure.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 18, 2025
---

# Agent SDK directory structure

The PingAccess Agent SDK for Java directory contains the following directories:

* `/apidocs`

  The Javadocs for the Java Agent API. Open `index.html` in this directory to access the Javadocs content.

* `/dist`

  The directory containing `pingaccess-agent-java-api-<version_number>.jar`

* `/sample`

  A directory containing `src` and `target` directories for building a Java Servlet Filter. This filter uses the Java Agent API, an `agent.properties` configuration exported from PingAccess, and the `init-params` from the web application `web.xml` file to enforce resource policy decisions configured in PingAccess.

---

---
title: Agent SDK for C directory structure
description: The PingAccess Agent SDK for C directory contains these subdirectories.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_sdk_for_c_directory_structure
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_sdk_for_c_directory_structure.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# Agent SDK for C directory structure

The PingAccess Agent SDK for C directory contains these subdirectories.

* `/`

  This directory contains the Agent Software Development Kit (SDK) *(tooltip: \<div class="paragraph">
  \<p>A set of tools that allows a developer to build a custom application that integrates with or connects to a platform or service.\</p>
  \</div>)* for C `README.md`, which contains information developers need to develop agents using the SDK. It also contains `ReadMeFirst.pdf` and `Legal.pdf`, which contain general information about the kit and third-party licenses used by components of the SDK.

* `/apidocs`

  API documentation for the SDK. Open `index.html` to access the API documentation content.

* `/include`

  Agent SDK header files.

* `/lib`

  32-bit and 64-bit libraries for Red Hat Enterprise Linux 7 and 8, and Windows, including third-party dependencies required by the SDK.

* `/sample`

  Sample source code for an agent for Apache. This sample agent uses the SDK and includes a sample configuration file for Apache to use the sample agent to enforce authentication and access control policies.

---

---
title: Agent SDK for C sample code
description: The Agent SDK for C sample code is available both in the SDK distribution and on GitHub at https://github.com/pingidentity/pa-agent-c-sdk-sample-apache.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_sdk_for_c_sample_code
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_sdk_for_c_sample_code.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# Agent SDK for C sample code

The Agent SDK for C sample code is available both in the SDK distribution and on GitHub at <https://github.com/pingidentity/pa-agent-c-sdk-sample-apache>.

Before building the sample code, ensure you have the PingAccess Agent SDK for C archive, the GNU `make` utility and associated compiler utilities installed with your compiler, and Apache and its development libraries.

The sample uses Apache and assumes that the PingAccess Agent SDK for C can be referenced as a dependency. For more details about specific dependencies and requirements, as well as instructions on how to build the sample code, see `<AGENT_SDK_C_HOME>/sample/readme.md`.

---

---
title: Agent SDK prerequisites
description: Verify that your system meets these prerequisites before installing the PingAccess Agent SDK for Java.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_agent_sdk_for_java_prereqs
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_agent_sdk_for_java_prereqs.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 19, 2025
---

# Agent SDK prerequisites

Verify that your system meets these prerequisites before installing the PingAccess Agent SDK for Java.

Before you start, ensure you have the Java SDK, [Apache Maven](https://maven.apache.org) and an application server, such as Apache Tomcat, installed. The sample uses Apache Maven and assumes that the Java Agent API can be referenced as a dependency. It references Ping Identity's public Maven repository, located at

```
http://maven.pingidentity.com/release
```

If internet access is unavailable, there are two other ways to reference the Java Agent API. First, after Apache Maven is installed, install the Java Agent API into your local dependency repository by executing the following command.

```
mvn install:install-file -Dfile=<AGENT_SDK_JAVA_HOME>/dist/pingaccess-agent-java-api-<version_number>.jar -DgroupId=com.pingidentity -DartifactId=pingaccess-agent-java-api -Dversion=<version_number> -Dpackaging=jar
```

Alternatively, update the dependency in your `pom.xml` to point to the local installation.

```
<dependency>
        <groupId>com.pingidentity</groupId>
        <artifactId>pingaccess-agent-java-api</artifactId>
        <version><version_number></version>
        <scope>system</scope>
        <systemPath><AGENT_SDK_JAVA_HOME>/dist/pingaccess-agent-java-api-<version_number>.jar</systemPath>
</dependency>
```

With either of these options, replace *\<AGENT\_SDK\_JAVA\_HOME>* with the absolute path to the extracted `pingaccess-agent-java-sdk-<version_number>` directory.

To download the SDK, go to the [PingAccess downloads site](https://www.pingidentity.com/en/resources/downloads/pingaccess.html) and click the **Add-ons** tab.

---

---
title: Agents and Integrations
description: PingAccess is supported by agents that can be installed in an agent deployment, and integrations that help PingAccess work with other tools.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_agents_and_integrations
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_agents_and_integrations.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  agents: Agents
  integrations: Integrations
---

# Agents and Integrations

PingAccess is supported by agents that can be installed in an agent deployment, and integrations that help PingAccess work with other tools.

## Agents

In an agent deployment, agents are installed on each web server. You can use an existing agent or create your own using the SDKs.

* [PingAccess Agent for Apache (RHEL)](pa_agent_for_apache_rhel.html)

* [PingAccess Agent for Apache (SLES)](pa_agent_for_apache_sles.html)

* [PingAccess Agent for Apache (Windows)](pa_agent_for_apache_windows.html)

* [PingAccess Agent for IIS](pa_agent_for_iis.html)

* [PingAccess Agent for NGINX](pa_agent_for_nginx.html)

* [PingAccess agent protocol](pa_agent_protocol.html)

* [PingAccess Agent SDK for C](pa_agent_sdk_for_c.html)

* [PingAccess Agent SDK for Java](pa_agent_sdk_for_java.html)

## Integrations

You can create integrations for PingAccess using the Add-on Software Development Kit (SDK) *(tooltip: \<div class="paragraph">
\<p>A set of tools that allows a developer to build a custom application that integrates with or connects to a platform or service.\</p>
\</div>)*, or use existing integrations with products used in your environment.

* [PingAccess Add-on SDK for Java](pa_add_on_sdk_for_java.html)

* [iovation Device Risk integration](pa_iovation_device_risk_integration.html)

* [IWA Integration](pa_iwa_integration.html)

* [Kong API Gateway Integration](pa_kong_api_gateway_integration.html)

* [Apigee API Gateway integration](pa_apigee_api_gateway_integration.html)

* [PingOne Protect integration](pa_p1risk_policy_eval_integration.html)

---

---
title: Apache (SLES) agent system requirements
description: The PingAccess agent for Apache (SLES) is supported on the following platforms:
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_apache_sles_system_requirements
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_apache_sles_system_requirements.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 18, 2025
---

# Apache (SLES) agent system requirements

The PingAccess agent for Apache (SLES) is supported on the following platforms:

* Apache HTTP Server 2.4 running on SUSE Linux Enterprise Server 15 (x86\_64). Use the latest supported SP from SUSE.

|   |                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | As with any system that is reachable from the Internet, the server should be properly hardened. The PingAccess agent for Apache includes an SELinux profile, and you should deploy SELinux on the server. |

---

---
title: Apache (Windows) agent system requirements
description: The PingAccess agent for Apache (Windows) is supported on these platforms.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_apache_windows_system_reqs
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_apache_windows_system_reqs.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 8, 2023
---

# Apache (Windows) agent system requirements

The PingAccess agent for Apache (Windows) is supported on these platforms.

* Apache HTTP Server 2.4 64-bit running on Microsoft Windows Server 2016, VC14 or later

* Apache HTTP Server 2.4 64-bit running on Microsoft Windows Server 2019, VC14 or later

* Apache HTTP Server 2.4 64-bit running on Microsoft Windows Server 2022, VC14 or later

As with any system that is reachable from the internet, the server should be properly hardened.

---

---
title: Apigee API Gateway integration
description: Ping Identity's shared flow for Apigee extends Apigee's authorization capabilities through an external authorization policy runtime service.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_apigee_api_gateway_integration
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_apigee_api_gateway_integration.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 28, 2025
section_ids:
  before-you-begin: Before you begin
---

# Apigee API Gateway integration

Ping Identity's shared flow for Apigee extends Apigee's authorization capabilities through an external authorization policy runtime service.

Integration with Apigee allows identity and access management (IAM) administrators to centrally manage access control and application protection in PingAccess, while enforcement is delegated to Apigee.

Use this guide to install and configure the shared flow in Apigee. After installation and configuration, you can manage access control rules, identity mappings, and other application protection features in PingAccess.

The following diagram shows how traffic flows through Apigee and PingAccess.

![Diagram showing interactions between API clients, an Apigee API Gateway, , and an API target. The following list explains the interactions.](_images/hix1654893804903.png)

1. The API client makes a request to the application programming interface (API) *(tooltip: \<div class="paragraph">
   \<p>A specification of interactions available for building software to access an application or service.\</p>
   \</div>)* gateway.

2. The shared flow extracts fields from the API client's request and sends them to PingAccess for authorization.

3. PingAccess evaluates the request, validates the authorization, then responds to Apigee. The response could be an authentication or authorization error that should be immediately sent back to the client, or it could be a modified request that Apigee will send to the API target.

4. If authorized to proceed, Apigee passes the original or modified API request to the API target.

5. The API service responds with the requested resource or with the result of the operation.

6. The shared flow extracts fields from the API target's response and sends them to PingAccess for processing.

7. PingAccess responds to the processing request. The API response can be modified by the web session configuration and processing rules in PingAccess.

8. Apigee responds to the API client with the original API response received from the API target or the modified response received from PingAccess.

## Before you begin

The Ping Identity shared flow for Apigee supports Apigee Edge, Apigee Private Cloud, and Apigee X. Before you begin, ensure that you have the following:

* A supported Apigee environment

* PingAccess installed and started

* The PingAuth shared flow bundle `.zip` file (`sharedflowbundle.zip`), which is available to download from either the **Add-ons** tab of the [PingAccess downloads page](https://www.pingidentity.com/en/resources/downloads/pingaccess.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/external-authorization-for-apigee-api-management)

---

---
title: Attaching the PingAuth shared flow to API proxies in Apigee
description: Configure the PingAuth shared flow on the API proxies where you want to use PingAccess as the external authorization policy runtime service.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_attaching_pingauth_shared_flow_to_api_proxies_in_apigee
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_attaching_pingauth_shared_flow_to_api_proxies_in_apigee.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 28, 2025
section_ids:
  steps: Steps
---

# Attaching the PingAuth shared flow to API proxies in Apigee

Configure the PingAuth shared flow on the API proxies where you want to use PingAccess as the external authorization policy runtime service.

## Steps

1. Add a **Flow Callout Policy**:

   1. In **Develop > API Proxies**, go to one of your APIs and click the **Develop** tab. Make sure you're on the latest revision of the proxy.

   2. In the **Policies** section of the **Navigator**, click **[icon: plus, set=fa]**to add a policy.

   3. Add a **Flow Callout Policy**, and in the **Shared Flow** list, select **PingAuth**.

   4. Click **Save**.

   ![This screen capture shows the completed Flow Callout Policy on the Flow Callout tab of the Add Policy window.](_images/pfj1654898020704.png)

2. Attach the **Flow Callout Policy** to **Flows**.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When PingAccess is integrated as the external authorization policy runtime service for Apigee, it should be integrated in the preflow of the request to the proxy endpoint, because the authentication and authorization function provided by PingAccess should occur before most other policies execute.You can consider other ways to integrate PingAccess by reading about flows at [Controlling API proxies with flows](https://cloud.google.com/apigee/docs/api-platform/fundamentals/what-are-flows). |

   1. In the **Proxy Endpoint** section of the **Navigator**, click **PreFlow**, then click **[icon: plus, set=fa]Step** to add a flow step to the request.

      ![This screen capture shows the included PreFlow step. PreFlow is highlighted.](_images/ehp1654898291582.png)

   2. On the **Existing** tab, select the flow callout policy that you created, then click **Add**.

      ![This screen capture shows the Add Step window for the Flow Callout Policy.](_images/tuc1654898763377.png)

   3. In the **Target Endpoint** section of the **Navigator**, select **PreFlow**, then add the flow callout policy as a **Step** to the **Response** flow.

      This gives PingAccess an early opportunity to process the API response from the target API before it's processed by Apigee.

      ![This screen capture shows the completed PingAuth policy.](_images/egd1654898970796.png)

3. Save and deploy the updated proxy.

---

---
title: com.pingidentity.pa.sdk.http
description: The body interface now requires an explicit read of data before invoking methods to collect that data. Previously, methods to collect the data would result in an implicit read of the data. The following code examples illustrate this change in semantics.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_sdk_http
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_sdk_http.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 19, 2025
section_ids:
  com-pingidentity-pa-sdk-http-body: com.pingidentity.pa.sdk.http.Body
  com-pingidentity-pa-sdk-http-bodyfactory: com.pingidentity.pa.sdk.http.BodyFactory
  com-pingidentity-pa-sdk-http-constants: com.pingidentity.pa.sdk.http.Constants
  com-pingidentity-pa-sdk-http-exchange: com.pingidentity.pa.sdk.http.Exchange
  com-pingidentity-pa-sdk-http-header: com.pingidentity.pa.sdk.http.Header
  com-pingidentity-pa-sdk-http-headerfield: com.pingidentity.pa.sdk.http.HeaderField
  com-pingidentity-pa-sdk-http-headers: com.pingidentity.pa.sdk.http.Headers
  com-pingidentity-pa-sdk-http-headersfactory: com.pingidentity.pa.sdk.http.HeadersFactory
  com-pingidentity-pa-sdk-http-httpstatus: com.pingidentity.pa.sdk.http.HttpStatus
  com-pingidentity-pa-sdk-http-mimetype: com.pingidentity.pa.sdk.http.MimeType
  com-pingidentity-pa-sdk-http-mediatype: com.pingidentity.pa.sdk.http.MediaType
  com-pingidentity-pa-sdk-http-message: com.pingidentity.pa.sdk.http.Message
  com-pingidentity-pa-sdk-http-method: com.pingidentity.pa.sdk.http.Method
  com-pingidentity-pa-sdk-http-request: com.pingidentity.pa.sdk.http.Request
  com-pingidentity-pa-sdk-http-responsebuilder: com.pingidentity.pa.sdk.http.ResponseBuilder
  com-pingidentity-pa-sdk-http-response: com.pingidentity.pa.sdk.http.Response
---

# com.pingidentity.pa.sdk.http

The body interface now requires an explicit read of data before invoking methods to collect that data. Previously, methods to collect the data would result in an implicit read of the data. The following code examples illustrate this change in semantics.

## com.pingidentity.pa.sdk.http.Body

As the updated Javadocs for the body interface indicates, plugins should avoid interrogating a body object unless absolutely necessary because reading a body object's data into memory can impact the scalability of PingAccess. As the plugin code is updated, evaluate whether the body object needs to be used by the plugin.

* Using the Body#read method

  Before PingAccess 5.0:

  ```
  private void invokeRead(Body body) throws IOException
  {
      body.read();
  }
  ```

  After PingAccess 5.0:

  ```
  private void invokeRead(Body body) throws AccessException
  {
      try
      {
          body.read();
      }
      catch (IOException e)
      {
          throw new AccessException("Failed to read body content",
                                    HttpStatus.BAD_GATEWAY,
                                    e);
      }
  }
  ```

* Using the Body#getContent method

  Before PingAccess 5.0:

  ```
  private void invokeGetContent(Body body) throws IOException
  {
      byte[] content = body.getContent();
  }
  ```

  After PingAccess 5.0:

  ```
  private void invokeGetContent(Body body) throws AccessException
  {
      invokeRead(body); // see the Body#read code example for this method
      byte[] content = body.getContent();
  }
  ```

* Using the Body#getBodyAsStream method

  Before PingAccess 5.0:

  ```
  private void invokeGetBodyAsStream(Body body) throws IOException
  {
      InputStream stream = body.getBodyAsStream();
  }
  ```

  After PingAccess 5.0:

  ```
  private void invokeGetBodyAsStream(Body body) throws AccessException
  {
      invokeRead(body); // see the Body#read code example for this method
      InputStream stream = body.newInputStream();
  }
  ```

  |   |                                                                    |
  | - | ------------------------------------------------------------------ |
  |   | The method was renamed from `getBodyAsStream` to `newInputStream`. |

* Using the Body#write method

  Before PingAccess 5.0:

  ```
  private void invokeWrite(Body body, BodyTransferrer bodyTransferrer) throws IOException
  {
      body.write(bodyTransferrer);
  }
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. To get the content of the Body, read the content into memory using the Body#read method and then invoke `Body#getContent` or `Body#newInputStream`.

* Using the Body#getLength method

  Before PingAccess 5.0:

  ```
  private void invokeGetLength(Body body) throws IOException
  {
      int length = body.getLength();
  }
  ```

  After PingAccess 5.0:

  ```
  private void invokeGetLength(Body body) throws AccessException
  {
      invokeRead(body); // see the Body#read code example for this method
      int length = body.getLength();
  }
  ```

* Using the Body#getRaw method

  Before PingAccess 5.0:

  ```
  private void invokeGetRaw(Body body) throws IOException
  {
      byte[] rawBody = body.getRaw();
  }
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. This method used to provide access to the content as it appeared on the wire, which required complicated handling if the body content used a chunked Transfer-Encoding. Use Body#getContent instead.

## com.pingidentity.pa.sdk.http.BodyFactory

* Using the BodyFactory#continuousBody method

  Before PingAccess 5.0:

  ```
  private void invokeContinuousBody(BodyFactory bodyFactory, byte[] content)
  {
      Body body = bodyFactory.continuousBody(content);
  }
  ```

  After PingAccess 5.0:

  ```
  private void invokeContinuousBody(BodyFactory bodyFactory, byte[] content)
  {
      Body body = bodyFactory.createInMemoryBody(content);
  }
  ```

  Before PingAccess 5.0:

  ```
  private void invokeContinuousBody(BodyFactory bodyFactory, InputStream in)
  {
      Body body = bodyFactory.continuousBody(in);
  }
  ```

  After PingAccess 5.0:

  A Body instance can no longer be created from an InputStream using the BodyFactory class. Instead, a plugin should read the contents of the InputStream into a byte array and provide the byte array to BodyFactory#createInMemoryBody.

## com.pingidentity.pa.sdk.http.Constants

The constants available from this class have been removed from the SDK. Plugins using these constants should maintain their own constants with the needed values.

## com.pingidentity.pa.sdk.http.Exchange

A handful of methods have been removed from the Exchange.

Further, the mechanism for storing data on the exchange through properties has been enhanced to make it easier to write type-safe code when working with Exchange properties.

* Using the Exchange#getCreationTime method

  Before PingAccess 5.0:

  ```
  Calendar creationTime = exchange.getCreationTime();
  ```

  After PingAccess 5.0:

  ```
  Calendar creationTime = Calendar.getInstance();
  creationTime.setTime(Date.from(exchange.getCreationTime()));
  ```

  |   |                                                                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If a Calendar object is not required, consider using the Instant object returned from the `getCreationTime` method directly instead of converting it into a Calendar object. |

* Using the Exchange#getDestinations method

  Before PingAccess 5.0:

  ```
  List<String> destinations = exchange.getDestinations();
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. Consider using the Exchange#getTargetHosts method to get similar information from the Exchange.

* Using the Exchange#getOriginalHostHeader method

  Before PingAccess 5.0:

  ```
  String originalHostHeader = exchange.getOriginalHostHeader();
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. Consider using the Exchange#getUserAgentHost method to get similar information from the Exchange. The getUserAgentHost method leverages the PingAccess HTTP requests configuration to determine the Host header value sent by the user agent.

* Using the Exchange#getOriginalHostHeaderHost method

  Before PingAccess 5.0:

  ```
  String host = exchange.getOriginalHostHeaderHost();
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. Consider using the Exchange#getUserAgentHost method to get similar information from the Exchange. The getUserAgentHost method leverages the PingAccess HTTP requests configuration to determine the Host header value sent by the user agent.

* Using the Exchange#getOriginalHostHeaderPort method

  Before PingAccess 5.0:

  ```
  String port = exchange.getOriginalHostHeaderPort();
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. Consider using the Exchange#getUserAgentHost method to get similar information from the Exchange. The getUserAgentHost method leverages the PingAccess HTTP requests configuration to determine the Host header value sent by the user agent.

* Using the Exchange#getOriginalRequestBaseUri method

  Before PingAccess 5.0:

  ```
  String originalRequestBaseUri = exchange.getOriginalRequestBaseUri();
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. A possible replacement is as follows:

  ```
  String originalRequestBaseUri = exchange.getUserAgentProtocol() +
                                  "://" +
                                  exchange.getUserAgentHost();
  ```

* Using the Exchange#getProperties method

  Before PingAccess 5.0:

  ```
  Map<String, String> properties = exchange.getProperties();
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. Properties should be obtained individually from the Exchange.

* Using the Exchange#getRequestBaseUri method

  Before PingAccess 5.0:

  ```
  String requestBaseUri = exchange.getRequestBaseUri();
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. A possible replacement is as follows.

  ```
  String requestBaseUri = exchange.getUserAgentProtocol() +
                          "://" +
                          exchange.getUserAgentHost();
  ```

* Using the Exchange#getRequestScheme method

  Before PingAccess 5.0:

  ```
  String requestScheme = exchange.getRequestScheme();
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. A possible replacement is as follows.

  ```
  String requestScheme = exchange.getUserAgentProtocol() + "://";
  ```

* Using the Exchange#getUser method

  Before PingAccess 5.0:

  ```
  private void invokeSetUser(Exchange exchange, User user)
  {
      exchange.setUser(user);
  }
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. The identity associated with an Exchange cannot be replaced.

* Using the Exchange#setUser method

  Before PingAccess 5.0:

  ```
  private void invokeSetUser(Exchange exchange, User user)
  {
      exchange.setUser(user);
  }
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. The identity associated with an Exchange cannot be replaced.

* Using the Exchange#setSourceIp method

  Before PingAccess 5.0:

  ```
  private void invokeSetSourceIp(Exchange exchange, String sourceIp)
  {
      exchange.setSourceIp(sourceIp);
  }
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. This value cannot be changed.

* Using the Exchange#setProperty method

  Before PingAccess 5.0:

  ```
  private void invokeSetProperty(Exchange exchange, String propertyKey, String value)
  {
      exchange.setProperty(propertyKey, value);
  }
  ```

  After PingAccess 5.0:

  ```
  private void invokeSetProperty(Exchange exchange,
                                 ExchangeProperty<String> propertyKey,
                                 String value)
  {
      exchange.setProperty(propertyKey, value);
  }
  ```

  See the Javadocs for ExchangeProperty for instructions on creating an ExchangeProperty object.

* Using the Exchange#getProperty method

  Before PingAccess 5.0:

  ```
  private void invokeGetProperty(Exchange exchange, String propertyKey)
  {
      Object propertyValueObj = exchange.getProperty(propertyKey);
      if (propertyValueObj instanceof String)
      {
          String propertyValue = (String) propertyValueObj;
      }
  }
  ```

  After PingAccess 5.0:

  ```
  private void invokeGetProperty(Exchange exchange, ExchangeProperty<String> propertyKey)
  {
      String propertyValue = exchange.getProperty(propertyKey).orElse(null);
  }
  ```

  |   |                                                                                       |
  | - | ------------------------------------------------------------------------------------- |
  |   | `Exchange#getProperty` now returns an Optional object instead of the Object directly. |

## com.pingidentity.pa.sdk.http.Header

This deprecated class has been replaced by the Headers interface. A Headers object can be created using a HeadersFactory obtained from the `ServiceFactory#headersFactory` method. The majority of methods on Header have counterparts on the Headers interface. See the Javadocs for the Headers interface for more information.

## com.pingidentity.pa.sdk.http.HeaderField

This class is now final and cannot be extended.

* Constructing a HeaderField

  Before PingAccess 5.0:

  ```
  private HeaderField createHeaderField(String line)
  {
      return new HeaderField(line);
  }
  ```

  After PingAccess 5.0:

  ```
  private HeaderField createHeaderField(String line)
  {
      String name = line.substring(0, line.indexOf(':'));
      String value = (line.substring(line.indexOf(":") + 1)).trim();

      return new HeaderField(name, value);
  }
  ```

  |   |                                                                                                                                        |
  | - | -------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Parsing an HTTP header field line can be error-prone. Consider whether the plugin can avoid having to parse an HTTP header field line. |

* Using the HeaderField#setHeaderName method

  Before PingAccess 5.0:

  ```
  private void invokeSetHeaderName(HeaderField field)
  {
      field.setHeaderName(new HeaderName("X-Custom"));
  }
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. A HeaderField's name is set upon construction and cannot be changed.

* Using the HeaderField#getApproximateSize method

  Before PingAccess 5.0:

  ```
  int approximateSize = field.getApproximateSize();
  ```

  After PingAccess 5.0:

  This method has been removed. The value returned by the method can still be computed:

  ```
  int approximateSize = 2 * (4 +
                             field.getHeaderName().toString().length() +
                             field.getValue().length());
  ```

## com.pingidentity.pa.sdk.http.Headers

A few methods on the Headers interface have been updated to use the instant class, instead of date.

* Using the Headers#getDate method

  Before PingAccess 5.0:

  ```
  Date date = headers.getDate();
  ```

  After PingAccess 5.0:

  ```
  Date date = Date.from(headers.getDate());
  ```

* Using the Headers#setDate method

  Before PingAccess 5.0:

  ```
  private void invokeSetDate(Headers headers, Date date)
  {
      headers.setDate(date);
  }
  ```

  After PingAccess 5.0:

  ```
  private void invokeSetDate(Headers headers, Date date)
  {
      headers.setDate(date.toInstant());
  }
  ```

* Using the Headers#getLastModified method

  Before PingAccess 5.0:

  ```
  SimpleDateFormat format = new SimpleDateFormat("E, dd MMM yyyy HH:mm:ss z",
                                                 Locale.ENGLISH);

  String lastModified = headers.getLastModified();
  if (lastModified != null)
  {
      Date lastModifiedDate = format.parse(lastModified);
  }
  ```

  After PingAccess 5.0:

  ```
  Date lastModifiedDate = Date.from(headers.getLastModified());
  ```

* Using the Headers#setLastModified method

  Before PingAccess 5.0:

  ```
  private void invokeSetLastModified(Headers headers, Date date)
  {
      SimpleDateFormat format = new SimpleDateFormat("E, dd MMM yyyy HH:mm:ss z",
                                                     Locale.ENGLISH);

      headers.setLastModified(format.format(date));
  }
  ```

  After PingAccess 5.0:

  ```
  private void invokeSetLastModified(Headers headers, Date date)
  {
      headers.setLastModified(date.toInstant());
  }
  ```

## com.pingidentity.pa.sdk.http.HeadersFactory

* Using the HeadersFactory#createFromRawHeaderFields method

  Before PingAccess 5.0:

  ```
  private void invokeCreateFromRawHeaderFields(HeadersFactory factory,
                                               List<String> fields) throws ParseException
  {
      Headers headers = factory.createFromRawHeaderFields(fields);
  }
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. Consider if the plugin can create HeaderFields directly and utilize the HeadersFactory#create method.

## com.pingidentity.pa.sdk.http.HttpStatus

The HttpStatus enum was converted to a final class. Common HttpStatus instances are defined as constants on HttpStatus.

* Using the HttpStatus#getLocalizationKey method

  Before PingAccess 5.0:

  ```
  String localizationKey = status.getLocalizationKey();
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. Instead, a HttpStatus contains a LocalizedMessage instance that encapsulates the localization of the status message for use in error templates.

## com.pingidentity.pa.sdk.http.MimeType

The constants available in this class are now available as constant MediaType instances in the class `com.pingidentity.pa.sdk.http.CommonMediaTypes`.

## com.pingidentity.pa.sdk.http.MediaType

This class is now final and cannot be extended.

* Constructing a MediaType

  Before PingAccess 5.0:

  ```
  private void createMediaType(String mediaTypeString)
  {
      MediaType mediaType = new MediaType(mediaTypeString);
  }
  ```

  After PingAccess 5.0:

  ```
  private void createMediaType(String mediaTypeString)
  {
      MediaType mediaType = MediaType.parse(mediaTypeString);
  }
  ```

## com.pingidentity.pa.sdk.http.Message

A number of methods have been removed from the Message interface.

* Using the Message#getBodyAsStream method

  Before PingAccess 5.0:

  ```
  InputStream bodyStream = message.getBodyAsStream();
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. However, the following code snippet can be used to maintain semantics of the old method.

  ```
  Body body = message.getBody();
  try
  {
      body.read();
  }
  catch (IOException | AccessException e)
  {
      throw new RuntimeException("Could not get body as stream", e);
  }

  InputStream bodyStream = body.newInputStream();
  ```

While this snippet maintains semantics, enable a plugin to propagate errors as an AccessException instead of as a RuntimeException.

* Using the Message#getCharset method

  Before PingAccess 5.0:

  ```
  Charset charset = message.getCharset();
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. However, the following code snippet can be used to maintain the semantics of the old method.

  ```
  Charset charset = message.getHeaders().getCharset();
  if (charset == null)
  {
      charset = StandardCharsets.UTF_8;
  }
  ```

  While this snippet maintains semantics, a plugin should consider how to handle the case where a Charset is not specified by a Message's header fields. Assuming a Charset of UTF-8 might lead to issues in some cases.

* Using the Message#getHeader method

  Before PingAccess 5.0:

  ```
  Header header = message.getHeader();
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. Instead, use Message#getHeaders and the Headers interface instead of Header.

* Using the Message#setHeader method

  Before PingAccess 5.0:

  ```
  private void invokeSetHeader(Message message, Header header)
  {
      message.setHeader(header);
  }
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. Instead, use Message#setHeaders and the Headers interface instead of Header.

* Using the Message#isDeflate method

  Before PingAccess 5.0:

  ```
  boolean deflate = message.isDeflate();
  ```

  After PingAccess 5.0:

  This method has been removed. However, the value can still be computed with the following code snippet.

  ```
  List<String> contentEncodingValues = message.getHeaders().getContentEncoding();
  boolean deflate = contentEncodingValues.stream().anyMatch(v -> v.equalsIgnoreCase("deflate"))
                    && contentEncodingValues.size() == 1;
  ```

* Using the Message#isGzip method

  Before PingAccess 5.0:

  ```
  boolean gzip = message.isGzip();
  ```

  After PingAccess 5.0:

  This method has been removed. However, the value can still be computed with the following code snippet.

  ```
  List<String> contentEncodingValues = message.getHeaders().getContentEncoding();
  boolean gzip = contentEncodingValues.stream().anyMatch(v -> v.equalsIgnoreCase("gzip"))
                 && contentEncodingValues.size() == 1;
  ```

* Using the Message#isHTTP10 method

  Before PingAccess 5.0:

  ```
  boolean http10 = message.isHTTP10();
  ```

  After PingAccess 5.0:

  This method has been removed. However, the value can still be computed with the following code snippet.

  ```
  boolean http10 = message.getVersion().equals("1.0");
  ```

* Using the Message#isHTTP11 method

  Before PingAccess 5.0:

  ```
  boolean http11 = message.isHTTP11();
  ```

  After PingAccess 5.0:

  The method has been removed. However, the value can still be computed with the following code snippet.

  ```
  boolean http11 = message.getVersion().equals("1.1");
  ```

* Using the Message#read method

  Before PingAccess 5.0:

  ```
  private void invokeRead(Message message,
                          InputStream inputStream,
                          boolean createBody) throws IOException
  {
      message.read(inputStream, createBody);
  }
  ```

  After PingAccess 5.0: This functionality is no longer supported. A request attached to an exchange can no longer be completely replaced, but individual components can be replaced, such as the method, Uniform Resource Identifier (URI) *(tooltip: \<div class="paragraph">
  \<p>Identifies a web resource with a string of characters conforming to a specified format.\</p>
  \</div>)*, headers and body. A response attached to an exchange can be replaced by using Exchange#setResponse.

* Using the Message#setVersion method

  Before PingAccess 5.0:

  ```
  private void invokeSetVersion(Message message, String version)
  {
      message.setVersion(version);
  }
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. The version of a message cannot be changed.

* Using the Message#write method

  Before PingAccess 5.0:

  ```
  private void invokeWrite(Message message,
                           OutputStream output) throws IOException
  {
      message.write(output);
  }
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. However, the following code snippet can be used to perform the equivalent operation.

  ```
  private void invokeWrite(Message message,
                           OutputStream output) throws IOException, AccessException
  {
      Body body = message.getBody();
      body.read();

      output.write(message.getStartLine().getBytes(StandardCharsets.ISO_8859_1));
      output.write(message.getHeaders().toString().getBytes(StandardCharsets.ISO_8859_1));
      output.write("\r\n".getBytes(StandardCharsets.ISO_8859_1));
      output.write(body.getContent());
      output.flush();
  }
  ```

## com.pingidentity.pa.sdk.http.Method

The method interface has been converted to a final class. Additionally, the related methods enum has been merged into the method class. The method class provides common method instances as class-level constants.

* Getting a common Method instance

  Before PingAccess 5.0:

  ```
  Method get = Methods.GET
  ```

  After PingAccess 5.0:

  ```
  Method get = Method.GET;
  ```

* Using the Method#getMethodName method

  Before PingAccess 5.0:

  ```
  String methodName = method.getMethodName();
  ```

  After PingAccess 5.0:

  ```
  String methodName = method.getName();
  ```

## com.pingidentity.pa.sdk.http.Request

A few methods have been removed from the request interface.

* Using the Request#getPostParams method

  Before PingAccess 5.0:

  ```
  private void invokeGetPostParams(Request request) throws IOException
  {
      Map<String, String[]> postParams = request.getPostParams();
  }
  ```

  After PingAccess 5.0:

  ```
  private void invokeGetPostParams(Request request) throws AccessException
  {
      Body body = request.getBody();
      try
      {
          body.read();
      }
      catch (IOException e)
      {
          throw new AccessException("Failed to read body content",
                                    HttpStatus.BAD_GATEWAY,
                                    e);
      }

      Map<String, String[]> postParams = body.parseFormParams();
  }
  ```

* Using the Request#isMultipartFormPost method

  Before PingAccess 5.0:

  ```
  boolean multipartFormPost = request.isMultipartFormPost();
  ```

  After PingAccess 5.0:

  This method has been removed from the Request interface. However, the value can still be calculated using the following code snippet.

  ```
  Headers headers = request.getHeaders();

  boolean multipartFormPost =
          request.getMethod() == Method.POST
          && headers.getContentType() != null
          && headers.getContentType().getBaseType().equals("multipart/form-data")
          && headers.getContentType().getParameter("boundary") != null;
  ```

## com.pingidentity.pa.sdk.http.ResponseBuilder

A handful of methods were removed from ResponseBuilder. Additionally, a handful of methods changed their semantics, particularly those that included an HTML message payload. See the updated Javadocs for ResponseBuilder for more info.

* Using the ResponseBuilder#badRequestText method

  Before PingAccess 5.0:

  ```
  Response response = ResponseBuilder.badRequestText(message).build();
  ```

  After PingAccess 5.0:

  ```
  Response response = ResponseBuilder.newInstance(HttpStatus.BAD_REQUEST)
                                     .contentType(CommonMediaTypes.TEXT_PLAIN)
                                     .body(message)
                                     .build();
  ```

  |   |                                                                                                    |
  | - | -------------------------------------------------------------------------------------------------- |
  |   | This approach doesn't localize the response body. Using a TemplateRenderer is recommended instead. |

* Using the ResponseBuilder#contentLength method

  Before PingAccess 5.0:

  ```
  Response response = ResponseBuilder.newInstance().contentLength(length).build();
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. Consider using one of the ResponseBuilder#body methods instead of explicitly setting the content length. This ensures that the body content of the Response aligns with the Content-Length header field.

* Using the ResponseBuilder#continue100 method

  Before PingAccess 5.0:

  ```
  Response response = ResponseBuilder.continue100().build();
  ```

  After PingAccess 5.0:

  ```
  Response response = ResponseBuilder.newInstance(HttpStatus.CONTINUE).build();
  ```

* Using the ResponseBuilder#forbiddenText method

  Before PingAccess 5.0:

  ```
  Response response = ResponseBuilder.forbiddenText().build();
  ```

  After PingAccess 5.0:

  ```
  Response response = ResponseBuilder.newInstance(HttpStatus.FORBIDDEN)
                                     .contentType(CommonMediaTypes.TEXT_PLAIN)
                                     .body(HttpStatus.FORBIDDEN.getMessage())
                                     .build();
  ```

  |   |                                                                                   |
  | - | --------------------------------------------------------------------------------- |
  |   | This approach doesn't localize the response body. Use a TemplateRenderer instead. |

* Using the ResponseBuilder#forbiddenWithoutBody method

  Before PingAccess 5.0:

  ```
  Response response = ResponseBuilder.forbiddenWithoutBody().build();
  ```

  After PingAccess 5.0:

  ```
  Response response = ResponseBuilder.newInstance(HttpStatus.FORBIDDEN).build();
  ```

  Before PingAccess 5.0:

  ```
  Response response = ResponseBuilder.forbiddenWithoutBody(message).build();
  ```

  After PingAccess 5.0:

  ```
  Response response = ResponseBuilder.newInstance(HttpStatus.FORBIDDEN).build();
  ```

  |   |                                                                    |
  | - | ------------------------------------------------------------------ |
  |   | In the original method, the string message parameter was not used. |

* Using the ResponseBuilder#htmlMessage method

  Before PingAccess 5.0:

  ```
  String message = ResponseBuilder.htmlMessage(caption, text);
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. Plugins that used this method will need to construct the HTML message without this method. Consider using the TemplateRenderer utility class in place of this method.

* Using the ResponseBuilder#internalServerError method

  Before PingAccess 5.0:

  ```
  Response response = ResponseBuilder.internalServerError(message).build();
  ```

  After PingAccess 5.0:

  ```
  Response response = ResponseBuilder.internalServerError().body(message).build();
  ```

  |   |                                                                                   |
  | - | --------------------------------------------------------------------------------- |
  |   | This approach doesn't localize the response body. Use a TemplateRenderer instead. |

* Using the ResponseBuilder#internalServerErrorWithoutBody method

  Before PingAccess 5.0:

  ```
  Response response = ResponseBuilder.internalServerErrorWithoutBody().build();
  ```

  After PingAccess 5.0:

  ```
  Response response = ResponseBuilder.internalServerError().build();
  ```

* Using the ResponseBuilder#newInstance method

  The no-arg newInstance method has been removed. A HttpStatus is required to create an instance of ResponseBuilder, and the required HttpStatus object should be passed to the newInstance method that accepts a HttpStatus.Before PingAccess 5.0:

  ```
  Response response = ResponseBuilder.newInstance().build()
  ```

  After PingAccess 5.0:

  ```
  Response response = ResponseBuilder.newInstance(HttpStatus.INTERNAL_SERVER_ERROR).build();
  ```

* Using the ResponseBuilder#noContent method

  Before PingAccess 5.0:

  ```
  Response response = ResponseBuilder.noContent().build();
  ```

  After PingAccess 5.0:

  ```
  Response response = ResponseBuilder.newInstance(HttpStatus.NO_CONTENT).build();
  ```

* Using the ResponseBuilder#notFoundWithoutBody method

  Before PingAccess 5.0:

  ```
  Response response = ResponseBuilder.notFoundWithoutBody().build();
  ```

  After PingAccess 5.0:

  ```
  Response response = ResponseBuilder.notFound().build();
  ```

* Using the ResponseBuilder#serverUnavailable method

  Before PingAccess 5.0:

  ```
  Response response = ResponseBuilder.serverUnavailable(message).build();
  ```

  After PingAccess 5.0:

  ```
  Response response = ResponseBuilder.serviceUnavailable().body(message).build();
  ```

  |   |                                                                                    |
  | - | ---------------------------------------------------------------------------------- |
  |   | This approach does not localize the response body. Use a TemplateRenderer instead. |

* Using the ResponseBuilder#serviceUnavailableWithoutBody method

  Before PingAccess 5.0:

  ```
  Response response = ResponseBuilder.serverUnavailableWithoutBody().build();
  ```

  After PingAccess 5.0:

  ```
  Response response = ResponseBuilder.serviceUnavailable().build();
  ```

* Using the ResponseBuilder#status method

  The status methods have been removed. Instead the status should be specified to the newInstance method as it is now required.Before PingAccess 5.0:

  ```
  Response response = ResponseBuilder.newInstance().status(HttpStatus.OK).build();
  ```

  After PingAccess 5.0:

  ```
  Response response = ResponseBuilder.newInstance(HttpStatus.OK).build();
  ```

* Using the ResponseBuilder#unauthorizedWithoutBody method

  Before PingAccess 5.0:

  ```
  Response response = ResponseBuilder.unauthorizedWithoutBody().build();
  ```

  After PingAccess 5.0:

  ```
  Response response = ResponseBuilder.unauthorized().build();
  ```

## com.pingidentity.pa.sdk.http.Response

A few methods were removed from the response interface.

* Using the Response#isRedirect method

  Before PingAccess 5.0:

  ```
  boolean redirect = response.isRedirect();
  ```

  After PingAccess 5.0:

  ```
  boolean redirect = response.getStatusCode() >= 300
                     && response.getStatusCode() < 400;
  ```

* Using the Response#setStatusCode method

  Before PingAccess 5.0:

  ```
  response.setStatusCode(HttpStatus.OK.getCode());
  ```

  After PingAccess 5.0:

  ```
  response.setStatus(HttpStatus.OK);
  ```

* Using the Response#setStatusMessage method

  Before PingAccess 5.0:

  ```
  response.setStatusMessage(HttpStatus.OK.getMessage());
  ```

  After PingAccess 5.0:

  ```
  response.setStatus(HttpStatus.OK);
  ```

---

---
title: com.pingidentity.pa.sdk.identity
description: The getTokenExpiration method was updated to use an instant instead of date.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_sdk_identity
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_sdk_identity.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  com-pingidentity-pa-sdk-identity-identity: com.pingidentity.pa.sdk.identity.Identity
  com-pingidentity-pa-sdk-identity-oauthtokenmetadata: com.pingidentity.pa.sdk.identity.OAuthTokenMetadata
---

# com.pingidentity.pa.sdk.identity

## com.pingidentity.pa.sdk.identity.Identity

The getTokenExpiration method was updated to use an instant instead of date.

* Using the Identity#getTokenExpiration method

  Before PingAccess 5.0:

  ```
  Date expiration = identity.getTokenExpiration();
  ```

  After PingAccess 5.0:

  ```
  Date expiration = Date.from(identity.getTokenExpiration());
  ```

## com.pingidentity.pa.sdk.identity.OAuthTokenMetadata

The OAuthTokenMetadata methods now use an instant instead of a date.

* Using the OAuthTokenMetadata#getExpiresAt method

  Before PingAccess 5.0:

  ```
  Date expiresAt = metadata.getExpiresAt();
  ```

  After PingAccess 5.0:

  ```
  Date expiresAt = Date.from(metadata.getExpiresAt());
  ```

* Using the OAuthTokenMetadata#getRetrievedAt method

  Before PingAccess 5.0:

  ```
  Date retrievedAt = metadata.getRetrievedAt();
  ```

  After PingAccess 5.0:

  ```
  Date retrievedAt = Date.from(metadata.getRetrievedAt());
  ```

---

---
title: com.pingidentity.pa.sdk.identitymapping.header
description: ClientCertificateMapping has been removed from the SDK, as it was not required to create an IdentityMappingPlugin implementation.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_sdk_identity_mapping_header
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_sdk_identity_mapping_header.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# com.pingidentity.pa.sdk.identitymapping.header

ClientCertificateMapping has been removed from the SDK, as it was not required to create an IdentityMappingPlugin implementation.

Plugins utilizing this class should create their own version of this class.

---

---
title: com.pingidentity.pa.sdk.policy
description: The nested Builder class has been removed from AccessExceptionContext and instead AccessExceptionContext is a builder that can be initially created with the new AccessExceptionContext#create method.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_sdk_policy
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_sdk_policy.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  com-pingidentity-pa-sdk-policy-accessexceptioncontext: com.pingidentity.pa.sdk.policy.AccessExceptionContext
  com-pingidentity-pa-sdk-policy-accessexception: com.pingidentity.pa.sdk.policy.AccessException
  com-pingidentity-pa-sdk-policy-ruleinterceptor: com.pingidentity.pa.sdk.policy.RuleInterceptor
  com-pingidentity-pa-sdk-policy-error-internalservererrorcallback: com.pingidentity.pa.sdk.policy.error.InternalServerErrorCallback
---

# com.pingidentity.pa.sdk.policy

## com.pingidentity.pa.sdk.policy.AccessExceptionContext

The nested Builder class has been removed from AccessExceptionContext and instead AccessExceptionContext is a builder that can be initially created with the new AccessExceptionContext#create method.

The LocalizedMessage interface has been introduced to simplify the configuration of a localized message for use in an error template. A LocalizedMessage has three implementations provided in the SDK: FixedMessage, BasicLocalizedMessage and ParameterizedLocalizedMessage. See the following code examples for more information on using these new classes.

* Constructing an AccessExceptionContext

  Before PingAccess 5.0:

  ```
  private AccessExceptionContext createAccessExceptionContext(HttpStatus httpStatus,
                                                              Throwable cause)

  {
      return AccessExceptionContext.builder()
                                   .cause(cause)
                                   .httpStatus(httpStatus)
                                   .exceptionMessage(httpStatus.getMessage())
                                   .errorDescription(httpStatus.getLocalizationKey())
                                   .errorDescriptionIsKey(true)
                                   .errorDescriptionSubstitutions(new String[0])
                                   .build();
  }
  ```

  After PingAccess 5.0:

  ```
  private AccessExceptionContext createAccessExceptionContext(HttpStatus httpStatus,
                                                              Throwable cause)
  {
      return AccessExceptionContext.create(httpStatus)
                                   .cause(cause)
                                   .exceptionMessage(httpStatus.getMessage())
                                   .errorDescription(httpStatus.getLocalizedMessage());
  }
  ```

  Before PingAccess 5.0:

  ```
  private AccessExceptionContext createAccessExceptionContext(HttpStatus httpStatus,
                                                              String localizationKey,
                                                              String[] substitutions)
  {
      return AccessExceptionContext.builder()
                                   .httpStatus(httpStatus)
                                   .errorDescription(localizationKey)
                                   .errorDescriptionIsKey(true)
                                   .errorDescriptionSubstitutions(substitutions)
                                   .build();
  }
  ```

  After PingAccess 5.0:

  ```
  private AccessExceptionContext createAccessExceptionContext(HttpStatus httpStatus,
                                                              String localizationKey,
                                                              String[] substitutions)
  {
      LocalizedMessage localizedMessage =
              new ParameterizedLocalizedMessage(localizationKey, substitutions);

      return AccessExceptionContext.create(httpStatus)
                                   .errorDescription(localizedMessage);
  }
  ```

  Before PingAccess 5.0:

  ```
  private AccessExceptionContext createAccessExceptionContext(HttpStatus httpStatus,
                                                              String localizationKey)
  {
      return AccessExceptionContext.builder()
                                   .httpStatus(httpStatus)
                                   .errorDescription(localizationKey)
                                   .errorDescriptionIsKey(true)
                                   .build();
  }
  ```

  After PingAccess 5.0:

  ```
  private AccessExceptionContext createAccessExceptionContext(HttpStatus httpStatus,
                                                              String localizationKey)
  {
      LocalizedMessage localizedMessage = new BasicLocalizedMessage(localizationKey);
      return AccessExceptionContext.create(httpStatus)
                                   .errorDescription(localizedMessage);
  }
  ```

  Before PingAccess 5.0:

  ```
  private AccessExceptionContext createAccessExceptionContext(HttpStatus httpStatus)
  {
      return AccessExceptionContext.builder()
                                   .from(httpStatus)
                                   .httpStatusDescription(httpStatus.getLocalizationKey())
                                   .httpStatusDescriptionIsKey(true)
                                   .templateFile("template.html")
                                   .contentType("text/html");
  }
  ```

  After PingAccess 5.0:

  ```
  private AccessExceptionContext createAccessExceptionContext(HttpStatus httpStatus)
  {
      return AccessExceptionContext.create(httpStatus)
                                   .errorDescription(httpStatus.getLocalizedMessage());
  }
  ```

  |   |                                                                                                                                                                                                                                                                                                        |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | This example demonstrates that it is no longer possible to set a template file and its associated content type on an AccessExceptionContext. To generate an error response from a template file, use the TemplateRenderer class. See the Javadocs for the TemplateRenderer class for more information. |

## com.pingidentity.pa.sdk.policy.AccessException

The changes to AccessExceptionContext apply to the creation of AccessException because the creation of an AccessException requires an AccessExceptionContext.

In addition to these changes, obtaining information from AccessException has also changed. See the code examples below for more information.

Finally, AccessException no longer derives from IOException and derives directly from Exception instead.

* Constructing an AccessException

  Before PingAccess 5.0:

  ```
  private void throwAccessException(String errorDescription,
                                    Throwable throwable) throws AccessException
  {
      throw new AccessException(errorDescription, throwable);
  }
  ```

  After PingAccess 5.0:

  ```
  private void throwAccessException(String errorDescription,
                                    Throwable throwable) throws AccessException
  {
      LocalizedMessage templateMessaage = new FixedMessage(errorDescription);
      throw new AccessException(AccessExceptionContext.create(HttpStatus.INTERNAL_SERVER_ERROR)
                                                      .exceptionMessage(errorDescription)
                                                      .cause(throwable)
                                                      .errorDescription(templateMessaage));
  }
  ```

  Before PingAccess 5.0:

  ```
  private void throwAccessException(String errorDescription) throws AccessException
  {
      throw new AccessException(errorDescription);
  }
  ```

  After PingAccess 5.0:

  ```
  private void throwAccessException(String errorDescription) throws AccessException
  {
      LocalizedMessage templateMessage = new FixedMessage(errorDescription);
      throw new AccessException(AccessExceptionContext.create(HttpStatus.INTERNAL_SERVER_ERROR)
                                                      .exceptionMessage(errorDescription)
                                                      .errorDescription(templateMessage));
  }
  ```

  Before PingAccess 5.0:

  ```
  private void createAccessException(int statusCode,
                                     String statusMessage,
                                     String errorDescription) throws AccessException
  {
      throw new AccessException(statusCode, statusMessage, errorDescription);
  }
  ```

  After PingAccess 5.0:

  ```
  private void createAccessException(int statusCode,
                                     String statusMessage,
                                     String errorDescription) throws AccessException
  {
      HttpStatus httpStatus = new HttpStatus(statusCode, statusMessage);
      LocalizedMessage templateMessage = new FixedMessage(errorDescription);
      throw new AccessException(AccessExceptionContext.create(httpStatus)
                                                      .exceptionMessage(errorDescription)
                                                      .errorDescription(templateMessage));
  }
  ```

  Before PingAccess 5.0:

  ```
  private void throwAccessException(int statusCode,
                                    String statusMessage,
                                    String errorDescription,
                                    Throwable throwable) throws AccessException
  {
      throw new AccessException(statusCode, statusMessage, errorDescription, throwable);
  }
  ```

  After PingAccess 5.0:

  ```
  private void throwAccessException(int statusCode,
                                    String statusMessage,
                                    String errorDescription,
                                    Throwable throwable) throws AccessException
  {
      HttpStatus httpStatus = new HttpStatus(statusCode, statusMessage);
      LocalizedMessage templateMessage = new FixedMessage(errorDescription);
      throw new AccessException(AccessExceptionContext.create(httpStatus)
                                                      .exceptionMessage(errorDescription)
                                                      .errorDescription(templateMessage)
                                                      .cause(throwable));
  }
  ```

  Before PingAccess 5.0:

  ```
  private void throwAccessException() throws AccessException
  {
      throw new AccessException(AccessExceptionContext.builder()
                                                      .httpStatusCode(403)
                                                      .httpStatusMessage("Forbidden")
                                                      .build());
  }
  ```

  After PingAccess 5.0:

  ```
  private void throwAccessException() throws AccessException
  {
      throw new AccessException(AccessExceptionContext.create(HttpStatus.FORBIDDEN));
  }
  ```

* Using the AccessException#getExceptionContext method

  Before PingAccess 5.0:

  ```
  AccessExceptionContext context = accessException.getExceptionContext();
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. The information that used to be provided by the AccessExceptionContext is now provided directly by an AccessException.

* Using the AccessException#getHttpStatusCode method

  Before PingAccess 5.0:

  ```
  int statusCode = accessException.getHttpStatusCode();
  ```

  After PingAccess 5.0:

  ```
  int statusCode = accessException.getErrorStatus().getCode();
  ```

* Using the AccessException#getHttpStatusMessage method

  Before PingAccess 5.0:

  ```
  String statusMessage = accessException.getHttpStatusMessage();
  ```

  After PingAccess 5.0:

  ```
  String statusMessage = accessException.getErrorStatus().getMessage();
  ```

* Using the AccessException#setHttpStatusCode method

  Before PingAccess 5.0:

  ```
  accessException.setHttpStatusCode(statusCode);
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. The status code associated with an AccessException is fixed once it is constructed.

* Using the AccessException#setHttpStatusMessage method

  Before PingAccess 5.0:

  ```
  accessException.setHttpStatusMessage(statusMessage);
  ```

  After PingAccess 5.0:

  This functionality is no longer supported. The status message associated with an AccessException is fixed once it is constructed.

## com.pingidentity.pa.sdk.policy.RuleInterceptor

The handleRequest and handleResponse methods on a RuleInterceptor no longer throw an IOException. Instead, they throw an AccessException, which no longer derives from IOException.

* Accounting for the RuleInterceptor#handleRequest method signature change

  Before PingAccess 5.0:

  ```
  @Override
  public Outcome handleRequest(Exchange exchange) throws IOException
  {
      Outcome outcome = applyPolicy(exchange);

      return outcome;
  }
  ```

  After PingAccess 5.0:

  ```
  @Override
  public Outcome handleRequest(Exchange exchange) throws AccessException
  {
      Outcome outcome = applyPolicy(exchange);

      return outcome;
  }
  ```

* Account for the RuleInterceptor#handleResponse method signature change

  Before PingAccess 5.0:

  ```
  @Override
  public void handleResponse(Exchange exchange) throws IOException
  {
      applyPolicyToResponse(exchange.getResponse());
  }
  ```

  After PingAccess 5.0:

  ```
  @Override
  public void handleResponse(Exchange exchange) throws AccessException
  {
      applyPolicyToResponse(exchange.getResponse());
  }
  ```

## com.pingidentity.pa.sdk.policy.error.InternalServerErrorCallback

This class has been removed. Use LocalizedInternalServerErrorCallback instead.

---

---
title: com.pingidentity.pa.sdk.services
description: This class is now final and cannot be extended.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_sdk_services
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_sdk_services.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  com-pingidentity-pa-sdk-services-servicefactory: com.pingidentity.pa.sdk.services.ServiceFactory
---

# com.pingidentity.pa.sdk.services

## com.pingidentity.pa.sdk.services.ServiceFactory

This class is now final and cannot be extended.

---

---
title: com.pingidentity.pa.sdk.siteauthenticator
description: This interface is no longer a RequestInterceptor or ResponseInterceptor, but it still defines the handleRequest and handleResponse methods.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_sdk_site_authenticator
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_sdk_site_authenticator.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  com-pingidentity-pa-sdk-siteauthenticator-siteauthenticatorinterceptor: com.pingidentity.pa.sdk.siteauthenticator.SiteAuthenticatorInterceptor
---

# com.pingidentity.pa.sdk.siteauthenticator

## com.pingidentity.pa.sdk.siteauthenticator.SiteAuthenticatorInterceptor

This interface is no longer a RequestInterceptor or ResponseInterceptor, but it still defines the handleRequest and handleResponse methods.

```
public interface SiteAuthenticatorInterceptor<T extends PluginConfiguration>
        extends DescribesUIConfigurable, ConfigurablePlugin<T>
{
    void handleRequest(Exchange exchange) throws AccessException;
    void handleResponse(Exchange exchange) throws AccessException;
}
```

Additionally, these methods now only throw an AccessException instead of an IOException or InterruptedException.

* Accounting for the SiteAuthenticatorInterceptor#handleRequest method signature change

  Before PingAccess 5.0:

  ```
  @Override
  public Outcome handleRequest(Exchange exc)
          throws RuntimeException, IOException, InterruptedException
  {
      // Site authenticator implementation //

      return Outcome.CONTINUE;
  }
  ```

  After PingAccess 5.0:

  ```
  @Override
  public void handleRequest(Exchange exc) throws AccessException
  {
      // Site authenticator implementation //
  }
  ```

* Accounting for the SiteAuthenticatorInterceptor#handleResponse method signature chang

  Before PingAccess 5.0:

  ```
  @Override
  public void handleResponse(Exchange exc) throws IOException
  {
      // Site authenticator response implementation //
  }
  ```

  After PingAccess 5.0:

  ```
  @Override
  public void handleResponse(Exchange exc) throws AccessException
  {
      // Site authenticator response implementation //
  }
  ```

---

---
title: com.pingidentity.pa.sdk.ui
description: The deprecated PRIVATEKEY enum value has been removed. Use a ConfigurationType of ConfigurationType#SELECT and specify the PrivateKeyAccessor.class instance to ConfigurationBuilder#dynamicOptions or UIElement#modelAccessor.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_sdk_ui
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_sdk_ui.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  com-pingidentity-pa-sdk-ui-configurationtype: com.pingidentity.pa.sdk.ui.ConfigurationType
---

# com.pingidentity.pa.sdk.ui

## com.pingidentity.pa.sdk.ui.ConfigurationType

The deprecated PRIVATEKEY enum value has been removed. Use a ConfigurationType of ConfigurationType#SELECT and specify the PrivateKeyAccessor.class instance to ConfigurationBuilder#dynamicOptions or UIElement#modelAccessor.

---

---
title: com.pingidentity.pa.sdk.user
description: This class has been removed from the SDK. Use the identity interface instead. An instance of identity can be retrieved from the exchange, similar to the user interface.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_sdk_user
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_sdk_user.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  com-pingidentity-pa-sdk-user-user: com.pingidentity.pa.sdk.user.User
---

# com.pingidentity.pa.sdk.user

## com.pingidentity.pa.sdk.user.User

This class has been removed from the SDK. Use the identity interface instead. An instance of identity can be retrieved from the exchange, similar to the user interface.

---

---
title: com.pingidentity.pa.sdk.util
description: The semantics of the renderResponse method have changed so it produces a response and does not have any side-effects on the specified parameters.
component: pingaccess
version: 9.1
page_id: pingaccess:agents_and_integrations:pa_sdk_util
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/pa_sdk_util.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  com-pingidentity-pa-sdk-util-templaterenderer: com.pingidentity.pa.sdk.util.TemplateRenderer
---

# com.pingidentity.pa.sdk.util

## com.pingidentity.pa.sdk.util.TemplateRenderer

The semantics of the renderResponse method have changed so it produces a response and does not have any side-effects on the specified parameters.

* Before PingAccess 5.0

  ```
  private void invokeRenderResponse(TemplateRenderer templateRenderer,
                                    Map<String, String> context,
                                    String templateName,
                                    Exchange exchange,
                                    ResponseBuilder builder)
  {
      templateRenderer.renderResponse(context, templateName, exchange, builder);
  }
  ```

* After PingAccess 5.0

  ```
  private void invokeRenderResponse(TemplateRenderer templateRenderer,
                                    Map<String, String> context,
                                    String templateName,
                                    Exchange exchange,8
                                    ResponseBuilder builder)
  {
      Response response = templateRenderer.renderResponse(exchange,
                                                          context,
                                                          templateName,
                                                          builder);
      exchange.setResponse(response);
  }
  ```