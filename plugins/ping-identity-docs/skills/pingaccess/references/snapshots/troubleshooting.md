---
title: Administrative SSO lockout
description: If you misconfigure administrative single sign-on (SSO) and are locked out of the PingAccess administrative console, you can disable SSO and sign on using the native sign-on.
component: pingaccess
version: 9.1
page_id: pingaccess:troubleshooting:pa_admin_sso_lockout
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/troubleshooting/pa_admin_sso_lockout.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2023
---

# Administrative SSO lockout

If you misconfigure administrative single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* and are locked out of the PingAccess administrative console, you can disable SSO and sign on using the native sign-on.

Choose one of the following methods to disable SSO:

* If you can start the PingAccess server or the administrative node in a cluster, refer to [Editing `run.properties` to disable SSO](pa_editing_run_properties_to_disable_sso.html).

* If you didn't disable basic authorization, refer to [Using the administrative API to disable SSO](pa_using_the_admin_api_to_disable_sso.html).

* If basic authorization is disabled, but administrative API OAuth *(tooltip: \<div class="paragraph">
  \<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
  \</div>)* is enabled, refer to [Using the administrative API and a new token to disable SSO](pa_using_the_admin_api_and_a_new_token_to_disable_sso.html).

---

---
title: Collecting support data
description: When troubleshooting, Ping Identity Support might ask you to use the collect support data tool to compile information about your PingAccess installation.
component: pingaccess
version: 9.1
page_id: pingaccess:troubleshooting:pa_collecting_support_data
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/troubleshooting/pa_collecting_support_data.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Collecting support data

When troubleshooting, Ping Identity Support might ask you to use the collect support data tool to compile information about your PingAccess installation.

## About this task

By default, the tool collects information from:

* `<PA_Home>/bin`

* `<PA_Home>/log` (the most recent files of each type within a size limit)

* `<PA_Home>/conf` (configuration files)

Information the tool collects includes:

* Environment details, such as:

  * Files present and their sizes

  * Certificate data

  * Version data

  * Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">
    \<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>
    \</div>)* details

* System details, such as:

  * Crontab

  * Ifconfig

  * Netstat

  * Uname

|   |                                                                    |
| - | ------------------------------------------------------------------ |
|   | Sytem details vary depending on the operating system you're using. |

The tool consists of the following files in the PingAccess home directory:

* `bin/collect-support-data.bat`

* `bin/collect-support-data.sh`

* `tools/csd/csd_configuration.yaml`

* `tools/csd/csd-1.1.jar`

|   |                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If Ping Identity Support needs more information about the PingAccess installation than the default configuration provides, Support might ask you to add a data collector to the tool by modifying its `csd_configuration.yaml` file. |

To collect support data with the tool:

## Steps

1. Using your PingAccess administrator account and a terminal, go to the `<PA_Home>/bin` directory.

2. Use one of the following commands to run the collect support data tool, depending on your operating system:

   ### Choose from:

   * On a Windows operating system, use `./collect-support-data.bat`.

   * On a Unix-based operating system, use `./collect-support-data.sh`.

     |   |                                                                                                                                                                                                                                                                                                                                                             |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If Ping Identity Support directs you to do so, you can use additional options with these commands. For example, you can run the command with the `--help` option.For more information, see the [PingFederate and PingAccess Support Data Collector](https://support.pingidentity.com/s/article/PingFederate-Support-Data-Collector) knowledge base article. |

   As the tool collects data, it displays its progress and any errors it detects. When it finishes collecting data, the tool places the data in a `.zip` file in the current directory. The format of the file's name is `support-data-ping-$<hostname>-r-$<timestamp>.zip`.

3. Review any errors that the tool brought up during the collection process, and any errors that've been added to the `support-data-ping-$<hostname>-r.log` log file.

   If necessary, resolve the errors and run the tool again.

4. Send the support data `.zip` file to Ping Identity Support.

---

---
title: Distributed tracing
description: Learn more about how PingAccess supports distributed tracing.
component: pingaccess
version: 9.1
page_id: pingaccess:troubleshooting:pa_distributed_tracing
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/troubleshooting/pa_distributed_tracing.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 17, 2026
section_ids:
  what-is-distributed-tracing: What is distributed tracing?
  supported-request-types: Supported request types
  distributed-tracing-components: Distributed tracing components
  visualizing-traces: Visualizing traces
  configuring-distributed-tracing: Configuring distributed tracing
  configure-distributed-tracing-with-property-files: Configure distributed tracing with property files
  steps: Steps
  example: Example:
  configure-distributed-tracing-with-environment-variables: Configure distributed tracing with environment variables
  steps-2: Steps
  example-2: Example:
---

# Distributed tracing

Distributed tracing provides visibility into the full path a request takes in a distributed system, helping to instrument, collect, and export telemetry data. Telemetry data can make it easier to identify the root cause of performance issues or errors, especially when investigating backchannel calls.

Ping Identity supports the [OpenTelemetry framework (OTEL)](https://opentelemetry.io/docs/what-is-opentelemetry/) for collecting distributed tracing data. PingAccess uses [OpenTelemetry Protocol (OTLP)](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.51.0/oteps/0035-opentelemetry-protocol.md) to send distributed traces to a backend service such as [Jaeger](https://www.jaegertracing.io/) for collection, storage, and visualization.

|   |                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   | Distributed tracing is an evolving feature in PingAccess. It's subject to change without notice, even in a minor or maintenance release. |

## What is distributed tracing?

In a distributed system, requests pass through multiple services hosted on multiple servers. Distributed tracing shows you how an incoming request was processed across all servers and services, including:

* Which servers and services the request went through.

* How much time each service took to process its part of the request.

* How the services are connected.

* What the failure point was in case of a request failure.

## Supported request types

PingAccess supports distributed tracing for the following request types:

* Incoming HTTP requests

* Outgoing HTTP requests

* Internal Java database connectivity (JDBC) requests

## Distributed tracing components

* Traces

  A trace represents the path of a request through an application. A trace is made up of one or more spans. Learn more about traces in the [OpenTelemetry documentation](https://opentelemetry.io/docs/concepts/signals/traces/).

* Spans

  A span is a segment of a request journey. It represents a unit of work or an operation within a service. Each span includes the following elements:

  * `traceId` represents the trace that the span is a part of.

  * `spanId` is a unique ID for the span.

  * `parentSpanId` is the ID of the originating request.

* Root span

  The root span indicates the start and end of an entire operation. The `parentSpanId` of the root span is null because the root span isn't part of an existing trace. Subsequent spans in the trace have their own unique `spanId`. Their `traceId` is the same as that of the root span, and their `parentSpanId` matches the `spanId` of the root span.

* OpenTelemetry

  OpenTelemetry is an open-source observability framework for instrumenting, generating, collecting, and exporting telemetry data. It provides a standardized way to capture distributed traces across different services and platforms. It doesn't provide a backend for storing or analyzing telemetry data. Learn more in the [OpenTelemetry documentation](https://opentelemetry.io/docs/what-is-opentelemetry/).

## Visualizing traces

PingAccess can push traces to an [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otel/protocol/) endpoint over HTTP. Any backend that supports OTLP and HTTP can be used to collect and visualize the traces.

|   |                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Try the [Jaeger tracing All-in-one Docker image](https://www.jaegertracing.io/docs/2.11/getting-started/) to capture exported spans. By default, Jaeger stores the spans in memory, but you can configure Jaeger to send the spans to various persistent datastores external to the Docker image. |

PingAccess includes an `exchangeId` tag on each operation it performs. You can use this tag to compare a specific span with a corresponding entry in the PingAccess log. Debug log level entries can provide additional insight after you use a tool like Jaeger to identify where the problem might lie.

## Configuring distributed tracing

Enable distributed tracing and configure relevant OpenTelemetry settings using one of the following methods:

* Edit the `run.properties` and `opentelemetry.properties` files directly.

* Use environment variables to set the properties in the `run.properties` and `opentelemetry.properties` files.

  Properties set by environment variables take precedence over any property values specified in the `opentelemetry.properties` file.

|   |                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you're [running PingAccess as a Windows service](../installing_and_uninstalling_pingaccess/pa_managing_pa_as_a_windows_service.html), you must reinstall the service for changes to the `pa.enable.distributed.tracing` property to take effect. This limitation applies regardless of the configuration method you use. |

* With the property files

* With environment variables

## Configure distributed tracing with property files

### Steps

1. Enable distributed tracing:

   1. Open the `<PA_HOME>/conf/run.properties` file in a text editor.

   2. Set the `pa.enable.distributed.tracing` property to `true`.

      #### Example:

      `pa.enable.distributed.tracing=true`

2. To configure OpenTelemetry properties, open the `<PA_HOME>/conf/opentelemetry.properties` file in a text editor.

   |   |                                                                                                                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The following table lists the default properties in `opentelemetry.properties`. You can find the full list of configurable OpenTelemetry properties in the [OpenTelemetry SDK documentation](https://opentelemetry.io/docs/languages/java/configuration/). |

   > **Collapse: Default OpenTelemetry properties**
   >
   > | Property                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   > | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | `otel.service.name` (required)                                                                               | Specify the name of your application or service. The default value is PingAccess.&#xA;&#xA;If running PingAccess in a clustered environment, it might be helpful to give each node a different otel.service.name so you can tell them apart if one is having latency issues.                                                                                                                                                                                                                                                                                                              |
   > | `otel.exporter.otlp.endpoint` (required)                                                                     | Specify the endpoint for your OpenTelemetry collector or backend:- If using OTLP or gRPC, use port 4317.
   >
   >   For example, `http://localhost:4317`.
   >
   > - If using either OTLP or HTTP with protobuf, use port 4318.The default value is `http://localhost:4318`.                                                                                                                                                                                                                                                                                                                              |
   > | `otel.exporter.otlp.protocol` (required)                                                                     | Specify the OTLP transport protocol to use for all telemetry data. Valid values include:- `http/protobuf` (default)
   >
   >   PingAccess recommends using this setting for its simplicity and compatibility with firewalls.
   >
   >   If using `http/protobuf`, make sure `otel.exporter.otlp.endpoint` is set to port 4318.
   >
   > - `grpc` to use OTLP or gRPC.
   >
   >   If using `grpc`, make sure `otel.exporter.otlp.endpoint` is set to port 4317.
   >
   > - `http/json` to use either OTLP or HTTP with JSON.
   >
   >   Review your backend OTEL consumer documentation for recommendations on which port to use for JSON. |
   > | `otel.resource.attributes` (optional)&#xA;&#xA;This property is commented out by default.                    | Optionally define static environment metadata for all telemetry data. Use the `key1=val,key2=val` format.For example, to add the environment, deployment zone, and host role, set `otel.resource.attributes=environment=dev,deployment.zone=us-east-1a,host.role=web-server`.                                                                                                                                                                                                                                                                                                             |
   > | `otel.instrumentation.<instrumentation_name>` (optional)&#xA;&#xA;This property is commented out by default. | You can use this property to disable specific instrumentation modules if they cause noise or conflicts.&#xA;&#xA;The value after otel.instrumentation must match the instrumentation name.&#xA;&#xA;For example, to disable JDBC instrumentation, set otel.instrumentation.jdbc.enabled=false.                                                                                                                                                                                                                                                                                            |
   > | `otel.javaagent.logging` (required)                                                                          | You can use this property to control OpenTelemetry agent logging. The default value is `application`.&#xA;&#xA;Ping Identity recommends using the default value because it integrates with the PingAccess Log4j2 implementation smoothly.                                                                                                                                                                                                                                                                                                                                                 |

   |   |                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | PingAccess doesn't support the following OpenTelemetry properties:- `otel.logs.exporter`

   - `otel.metrics.exporter`

   - `otel.instrumentation.netty.ssl.telemetry.enabled`

   - `otel.instrumentation.netty.connection-telemetry.enabled`While these properties are included in the file, they are disabled by default. It is not recommended to alter these values. |

3. Repeat these steps for each node in the cluster.

4. Start or restart PingAccess.

## Configure distributed tracing with environment variables

To set your environment variables, use a deployment tool of your choice, such as [Kubernetes](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/) or [Docker Compose](https://docs.docker.com/compose/environment-variables/set-environment-variables/).

### Steps

1. To enable distributed tracing, set the environment variable `PA_RUN_PA_ENABLE_DISTRIBUTED_TRACING=true`.

   You can find more information about PingAccess environment variables in [Use environment variables to override configuration settings](../configuring_and_customizing_pingaccess/pa_environment_variables_config_override.html).

2. Review the default properties available for configuration in the default OpenTelemetry properties table. To convert an OpenTelemetry property to an environment variable:

   1. Convert the name to uppercase.

   2. Replace all dot (`.`) and hyphen (`-`) characters with underscores (`_`).

      #### Example:

      The `otel.exporter.otlp.endpoint` property is equivalent to the `OTEL_EXPORTER_OTLP_ENDPOINT` environment variable.

      |   |                                                                                                                                                                                                                                                                                                                                                   |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | These environment variables are native to the OpenTelemetry library and are distinct from PingAccess's standard environment variable format (PA\_*\<FILENAME>*\_*\<PROPERTY>*).Don't use the PingAccess "PA\_" prefix to set OpenTelemetry environment variables. Use the standard "OTEL\_" prefix as defined in the OpenTelemetry specification. |

      The following table lists the default properties in `opentelemetry.properties`. You can find the full list of configurable OpenTelemetry properties in the [OpenTelemetry SDK documentation](https://opentelemetry.io/docs/languages/java/configuration/).

      > **Collapse: Default OpenTelemetry properties**
      >
      > | Property                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
      > | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      > | `otel.service.name` (required)                                                                               | Specify the name of your application or service. The default value is PingAccess.&#xA;&#xA;If running PingAccess in a clustered environment, it might be helpful to give each node a different otel.service.name so you can tell them apart if one is having latency issues.                                                                                                                                                                                                                                                                                                              |
      > | `otel.exporter.otlp.endpoint` (required)                                                                     | Specify the endpoint for your OpenTelemetry collector or backend:- If using OTLP or gRPC, use port 4317.
      >
      >   For example, `http://localhost:4317`.
      >
      > - If using either OTLP or HTTP with protobuf, use port 4318.The default value is `http://localhost:4318`.                                                                                                                                                                                                                                                                                                                              |
      > | `otel.exporter.otlp.protocol` (required)                                                                     | Specify the OTLP transport protocol to use for all telemetry data. Valid values include:- `http/protobuf` (default)
      >
      >   PingAccess recommends using this setting for its simplicity and compatibility with firewalls.
      >
      >   If using `http/protobuf`, make sure `otel.exporter.otlp.endpoint` is set to port 4318.
      >
      > - `grpc` to use OTLP or gRPC.
      >
      >   If using `grpc`, make sure `otel.exporter.otlp.endpoint` is set to port 4317.
      >
      > - `http/json` to use either OTLP or HTTP with JSON.
      >
      >   Review your backend OTEL consumer documentation for recommendations on which port to use for JSON. |
      > | `otel.resource.attributes` (optional)&#xA;&#xA;This property is commented out by default.                    | Optionally define static environment metadata for all telemetry data. Use the `key1=val,key2=val` format.For example, to add the environment, deployment zone, and host role, set `otel.resource.attributes=environment=dev,deployment.zone=us-east-1a,host.role=web-server`.                                                                                                                                                                                                                                                                                                             |
      > | `otel.instrumentation.<instrumentation_name>` (optional)&#xA;&#xA;This property is commented out by default. | You can use this property to disable specific instrumentation modules if they cause noise or conflicts.&#xA;&#xA;The value after otel.instrumentation must match the instrumentation name.&#xA;&#xA;For example, to disable JDBC instrumentation, set otel.instrumentation.jdbc.enabled=false.                                                                                                                                                                                                                                                                                            |
      > | `otel.javaagent.logging` (required)                                                                          | You can use this property to control OpenTelemetry agent logging. The default value is `application`.&#xA;&#xA;Ping Identity recommends using the default value because it integrates with the PingAccess Log4j2 implementation smoothly.                                                                                                                                                                                                                                                                                                                                                 |

      |   |                                                                                                                                                                                                                                                                                                                                                                   |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | PingAccess doesn't support the following OpenTelemetry properties:- `otel.logs.exporter`

      - `otel.metrics.exporter`

      - `otel.instrumentation.netty.ssl.telemetry.enabled`

      - `otel.instrumentation.netty.connection-telemetry.enabled`While these properties are included in the file, they are disabled by default. It is not recommended to alter these values. |

3. Repeat these steps for each node in the cluster.

4. Start or restart PingAccess.

---

---
title: "Editing <code class=\"filepath\">run.properties</code> to disable SSO"
description: If you cannot sign on to the PingAccess administrative console, but you can start the PingAccess server or the administrative node in a cluster, you can edit the run.properties file to disable single sign-on (SSO).
component: pingaccess
version: 9.1
page_id: pingaccess:troubleshooting:pa_editing_run_properties_to_disable_sso
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/troubleshooting/pa_editing_run_properties_to_disable_sso.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 22, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  result: Result
  next-steps: Next steps
---

# Editing `run.properties` to disable SSO

If you cannot [sign on to the PingAccess administrative console](../installing_and_uninstalling_pingaccess/pa_accessing_the_admin_console.html), but you can [start the PingAccess server](../installing_and_uninstalling_pingaccess/pa_starting_pa.html) or the administrative node in a [cluster](../reference_guides/pa_clustering_ref_guide.html), you can edit the `run.properties` file to disable single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*.

## About this task

If you are locked out of the administrative console because of an SSO misconfiguration, switching to basic (native) authentication makes it easier to sign on and reconfigure SSO.

## Steps

1. Start the local PingAccess server.

   Learn more in [Starting PingAccess](../installing_and_uninstalling_pingaccess/pa_starting_pa.html).

2. Open the `run.properties` file for editing.

3. Change the `admin.auth` value from `default` to `native`.

   ### Example:

   ```
   admin.auth=native
   ```

4. Save your changes and restart PingAccess.

## Result

You can sign on to the administrative console normally.

## Next steps

Go to **Settings > Admin UI Authentication > Authentication Method** to reconfigure SSO.

---

---
title: Minimizing the PingAccess cookie size
description: Reduce the size of the PingAccess cookie if it causes problems in your environment.
component: pingaccess
version: 9.1
page_id: pingaccess:troubleshooting:pa_minimizing_the_pa_cookie_size
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/troubleshooting/pa_minimizing_the_pa_cookie_size.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 1, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Minimizing the PingAccess cookie size

Reduce the size of the PingAccess cookie if it causes problems in your environment.

## About this task

Each of the following options can reduce the PingAccess cookie size. The exact reduction amount can't be precisely quantified because it's environment-dependent.

## Steps

* When configuring the site, clear the **Send Token** checkbox. This minimizes the amount of information forwarded to the site itself. Learn more in [Adding sites](../pingaccess_user_interface_reference_guide/pa_adding_sites.html), [Editing sites](../pingaccess_user_interface_reference_guide/pa_editing_sites.html), and [Site field descriptions](../pingaccess_user_interface_reference_guide/pa_site_field_descriptions_ref.html).

* When configuring the web session, select the **Cache User Attributes** checkbox. This caches user information for use in policy decisions instead of including it in the cookie. Learn more in [Creating web sessions](../pingaccess_user_interface_reference_guide/pa_creating_web_sessions.html) and [Editing and deleting web sessions](../pingaccess_user_interface_reference_guide/pa_editing_web_sessions.html).

* When [Configuring web session management settings](../pingaccess_user_interface_reference_guide/pa_configuring_web_session_management_settings.html), select the simplest algorithms: `ECDSA using P-256 Curve` for the **Signing Algorithm** and `AES 128 with CBC and HMAC SHA 256` for the **Encryption Algorithm**.

  |   |                                                                                                                               |
  | - | ----------------------------------------------------------------------------------------------------------------------------- |
  |   | This option isn't as impactful as the other options and might not be possible depending on your environment's security needs. |

* When [Configuring admin UI SSO authentication](../pingaccess_user_interface_reference_guide/pa_configuring_admin_ui_sso_authn_task.html), clear the **Include id\_token\_hint in SLO** checkbox.

  |   |                                                                                                                                                                                                                                                                                                                      |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If your token provider requires the `id_token_hint` parameter to complete single logout (SLO) *(tooltip: \<div class="paragraph">&#xA;\<p>The process of signing a user out of multiple sites where the user has started a SSO session.\</p>&#xA;\</div>)*, explore the other options to reduce cookie size instead. |

* When [Configuring OpenID Connect token providers](../pingaccess_user_interface_reference_guide/pa_configuring_oidc.html), clear the **Track token\_id** checkbox.

  |   |                                                                                                                                                                |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you want to use the `id_token` attribute in an identity mapping, rule, or virtual logout resource, explore the other options to reduce cookie size instead. |

* When [Configuring PingOne Advanced Identity Cloud or PingAM as the token provider](../pingaccess_user_interface_reference_guide/pa_configuring_p1aic_or_pingam_as_the_token_provider.html), clear the **Track token\_id** checkbox.

  |   |                                                                                                                                                                |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you want to use the `id_token` attribute in an identity mapping, rule, or virtual logout resource, explore the other options to reduce cookie size instead. |

---

---
title: Troubleshooting
description: This section covers troubleshooting for common issues with PingAccess:
component: pingaccess
version: 9.1
page_id: pingaccess:troubleshooting:pa_troubleshooting
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/troubleshooting/pa_troubleshooting.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 16, 2026
---

# Troubleshooting

This section covers troubleshooting for common issues with PingAccess:

* You can find more information about how to proceed if you're locked out of the administrative console in [Administrative SSO lockout](pa_admin_sso_lockout.html).

* Learn more about how to use the collect support data tool in [Collecting support data](pa_collecting_support_data.html).

* Learn more about settings that affect the size of the PingAccess cookie in [Minimizing the PingAccess cookie size](pa_minimizing_the_pa_cookie_size.html).

* You can find more information about distributed tracing and OpenTelemetry in [Distributed tracing](pa_distributed_tracing.html).

---

---
title: Using the administrative API and a new token to disable SSO
description: If basic authorization is disabled but administrative application programming interface (API) OAuth is enabled, you can also use the administrative API to disable single sign-on (SSO).
component: pingaccess
version: 9.1
page_id: pingaccess:troubleshooting:pa_using_the_admin_api_and_a_new_token_to_disable_sso
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/troubleshooting/pa_using_the_admin_api_and_a_new_token_to_disable_sso.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2023
section_ids:
  steps: Steps
  result: Result
---

# Using the administrative API and a new token to disable SSO

If basic authorization is disabled but administrative application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)* is enabled, you can also use the administrative API to disable single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*.

## Steps

1. Retrieve a valid token for admin API OAuth from your token provider.

2. Submit a PUT request to `https://<pa-host>/pa-admin-api/<api version>/auth/oidc` with the valid access token, where *\<pa-host>* is the `hostname:port` for the PingAccess admin node and *\<api-version>* is the API version (`v3` on PingAccess 5.0 or later, and `v2` on 4.X).

   The request body must contain:

   ```json
   {
    "enabled": false,
   }
   ```

## Result

You can sign on normally and reconfigure the SSO from **Settings → Admin UI Authentication → Authentication Method**.

---

---
title: Using the administrative API to disable SSO
description: If basic authorization wasn't disabled, use the admin application programming interface (API) to disable single sign-on (SSO).
component: pingaccess
version: 9.1
page_id: pingaccess:troubleshooting:pa_using_the_admin_api_to_disable_sso
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/troubleshooting/pa_using_the_admin_api_to_disable_sso.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2023
section_ids:
  steps: Steps
  example: Example:
  result: Result
---

# Using the administrative API to disable SSO

If basic authorization wasn't disabled, use the admin application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* to disable single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*.

## Steps

1. Sign on to the local PingAccess system and start a non-Internet Explorer (IE) browser.

2. Sign on to the API doc page at https\://*\<host>*:*\<admin-port>*/pa-admin-api/v3/api-docs/.

   ### Example:

   https\://localhost:9000/pa-admin-api/v3/api-docs/

   Use the normal administrator username, `Administrator`, and your password.

3. Click and expand the **Auth** section, then expand **PUT /auth/oidc**.

4. Enter the following code:

   ```json
   {
   "enabled": false
   }
   ```

5. Click **Try it Out**.

## Result

You can sign on normally and reconfigure SSO for the admin API from **Settings → Admin UI Authentication → Authentication Method**.