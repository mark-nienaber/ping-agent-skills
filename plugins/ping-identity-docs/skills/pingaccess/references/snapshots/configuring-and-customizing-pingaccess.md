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

---

---
title: Appending log messages to syslog and the console
description: Enable additional output destinations, called appenders.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_appending_log_messages_to_syslog_and_the_console
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_appending_log_messages_to_syslog_and_the_console.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Appending log messages to syslog and the console

Enable additional output destinations, called appenders.

## About this task

Console and syslog appenders are pre-configured in `log4j2.xml`, but they're commented out by default.

To enable additional appenders:

## Steps

1. Open the `conf/log4j2.xml` file in a text editor.

2. Locate the following lines in the `<Loggers>` element:

   ```
   <AsyncLogger name="com.pingidentity" level="DEBUG" additivity="false" includeLocation="false">
       <AppenderRef ref="File"/>
       <!--<AppenderRef ref="CONSOLE" />-->
       <!--<AppenderRef ref="SYSLOG" />-->
   </AsyncLogger>
   ```

   |   |                                                                                                                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you have customized logging to enable logging for additional classes, locate the `<AsyncLogger>` element that's relevant to the class in question. This class is defined in the `<AsyncLogger>``name` attribute. |

3. Uncomment the `<AppenderRef>` element that applies to the appender that you want to enable.

   |   |                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------ |
   |   | PingAccess will rescan the logging configuration within 30 seconds and make the change active automatically. |

4. Save the file.

---

---
title: Configure logging in PingAccess
description: Common tasks to configure and manage logging in PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_configure_logging_lp
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_configure_logging_lp.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 9, 2023
---

# Configure logging in PingAccess

Common tasks to configure and manage logging in PingAccess.

* For information on how to make your log entries more or less detailed, see [Configuring log levels](pa_configuring_log_levels.html).

* For information on enabling cookie logging, see [Enabling cookie logging](pa_enabling_cookie_logging.html).

* For information on enabling additional log output destinations, see [Appending log messages to syslog and the console](pa_appending_log_messages_to_syslog_and_the_console.html).

---

---
title: Configuring and Customizing PingAccess
description: This section contains information on how to configure and customize your PingAccess environment.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_configuring_and_customizing_pa_landing_topic
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_configuring_and_customizing_pa_landing_topic.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 10, 2023
---

# Configuring and Customizing PingAccess

This section contains information on how to configure and customize your PingAccess environment.

* For information on configuring PingAccess for server-side session management, see [Session management configuration](pa_session_management_config.html).

* For information on the types of PingAccess logs and how to configure them, see [Log configuration](pa_logging_configuration.html).

* For information on customizing PingAccess templates or localizing user-facing documentation and system status messages, see [Customize and Localize PingAccess](pa_customize_localize_landing_topic.html).

* For information on enabling or disabling Federal Information Processing Standards (FIPS) mode, see [Managing Federal Information Processing Standards (FIPS) mode](pa_fips_mode.html).

* If you're using Amazon Web Services (AWS), see [Configuring PingAccess to use Amazon Key Management Services](pa_config_amazon_kms.html).

* For information on formatting environment variables, see [Use environment variables to override configuration settings](pa_environment_variables_config_override.html).

---

---
title: Configuring log levels
description: Define log levels for specific package or class names in the log4j2.xml file to get more or less detailed logging from a class or group of classes.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_configuring_log_levels
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_configuring_log_levels.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 9, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  example-2: Example:
  result: Result
---

# Configuring log levels

Define log levels for specific package or class names in the `log4j2.xml` file to get more or less detailed logging from a class or group of classes.

## About this task

Class or package loggers are defined in the `<AsyncLogger>``name` attribute. For example, the following line enables cookie logging:

```
<AsyncLogger name="com.pingidentity.pa.core.interceptor.CookieLoggingInterceptor" level="TRACE" additivity="false" includeLocation="false">
    <AppenderRef ref="File"/>
</AsyncLogger>
```

|   |                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------- |
|   | If you don't specify a log level for a particular package or class, it inherits the settings for the root logger. |

For information on how to configure log levels in the administrative console instead, see [Log settings](../pingaccess_user_interface_reference_guide/pa_log_settings.html).

To configure the log level for a class or package in the `log4j2.xml` file:

## Steps

1. Open `conf/log4j2.xml` in a text editor.

2. Locate the `<AsyncLogger>` element for the package or class you want to adjust the logging level for.

   ### Example:

   ```
   <AsyncLogger name="com.pingidentity" level="DEBUG" additivity="false" includeLocation="false">
   ```

3. Set the `level` value in the `<AsyncLogger>` element to one of the following values:

   `OFF`, `FATAL`, `ERROR`, `WARN`, `INFO`, `DEBUG`, and `TRACE`.

   ### Example:

   To apply `TRACE` level logging for the `com.pingidentity` package, locate the following line:

   ```
   <AsyncLogger name="com.pingidentity" level="DEBUG" additivity="false" includeLocation="false">
   ```

   Change it to:

   ```
   <AsyncLogger name="com.pingidentity" level="TRACE" additivity="false" includeLocation="false">
   ```

4. Save the modified file.

## Result

PingAccess automatically makes the changes effective within 30 seconds.

---

---
title: Configuring PingAccess for server-side session management
description: Configure PingAccess to enable server-side session management.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_configuring_pa_for_server_side_session_management
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_configuring_pa_for_server_side_session_management.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 27, 2024
section_ids:
  steps: Steps
---

# Configuring PingAccess for server-side session management

Configure PingAccess to enable server-side session management.

## Steps

1. Sign on to the PingAccess administrative console.

2. Click **Access**, then go to **Web Sessions > Web Sessions**.

3. Click either [Create a new web session](../pingaccess_user_interface_reference_guide/pa_creating_web_sessions.html) or [Edit an existing web session](../pingaccess_user_interface_reference_guide/pa_editing_web_sessions.html).

4. Enter a unique **Name** for the web session, up to 64 characters, including special characters and spaces.

5. Specify the **Audience** that the PingAccess token is applicable to, represented as a short, unique identifier between 1 and 32 characters.

   Requests are rejected that contain a PingAccess token with an audience that differs from what is configured in the web session associated with the target application. Changing this setting might affect existing ongoing sessions, forcing the user to re-authenticate to access protected resources.

6. In the **Client ID** field, enter the Client ID defined in PingFederate.

7. In the **Client Credentials Type** section, select **Secret**, and then enter the **Client Secret** associated with the specified Client ID.

8. Click **Show Advanced**.

9. To enable the server-side session management feature, select **Validate Session**.

10. Click **Save**.

---

---
title: Configuring PingAccess to use Amazon Key Management Services
description: During initial startup, PingAccess automatically generates a randomized master key, which by default is not encrypted. If you are running in Amazon Web Services (AWS), you can configure PingAccess to use Amazon Key Management Services (KMS) to encrypt the master key.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_config_amazon_kms
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_config_amazon_kms.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  example: Example:
---

# Configuring PingAccess to use Amazon Key Management Services

During initial startup, PingAccess automatically generates a randomized master key, which by default is not encrypted. If you are running in Amazon Web Services (AWS) *(tooltip: \<div class="paragraph">
\<p>An Amazon subsidiary providing cloud computing platforms.\</p>
\</div>)*, you can configure PingAccess to use Amazon Key Management Services (KMS) to encrypt the master key.

## Before you begin

* Make sure that you have an active connection to AWS.

* Use AWS KMS to generate a key to use for the PingAccess master key encryption.

|   |                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For more information about managing access rights to your keys using key policies or AWS Identity and Access Management (IAM), see [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html). |

## About this task

To configure the encryption of the PingAccess master key, modify the `pa.jwk.properties` file found in `<PA_HOME>/conf`.

## Steps

1. Stop PingAccess.

2. In a text editor, open `<PA_HOME>/conf/pa.jwk.properties`.

3. Locate the `pa.hostkey.masterKeyEncryptor` property .

4. Enable master key encryption.

   1. Change `com.pingidentity.pa.crypto.NoOpMasterKeyEncryptor` to the AWS KMS master key encryptor class name `com.pingidentity.pingcommons.aws.key.AwsKmsMasterKeyEncryptor`.

   2. Locate the ID for the key that you generated using AWS KMS.

   3. If this is not the first time starting PingAccess, prefix the key ID with `"ENCRYPT:"`.

      ### Example:

      After making changes, the properties file should look similar to the following:

      ```
      pa.hostkey.masterKeyEncryptor=com.pingidentity.pingcommons.aws.key.AwsKmsMasterKeyEncryptor
       pa.hostkey.keyId=ENCRYPT:d4e6adab-e20c-4339-ba76-e4cb1348713f
      ```

5. Save and close the updated `pa.jwk.properties` file.

6. Restart PingAccess.

   The PingAccess master file `pa.jwk` is encrypted using Amazon KMS.

---

---
title: Configuring PingFederate for session management
description: Configure PingFederate to revoke PingAccess session cookies.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_configuring_pf_for_session_management
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_configuring_pf_for_session_management.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Configuring PingFederate for session management

Configure PingFederate to revoke PingAccess session cookies.

## Steps

1. Sign on to the PingFederate Administrative Console

2. If you are using PingFederate 10.0 or earlier, go to **Server Configuration → Server → Protocol settings → Roles & Protocols** and ensure that **Enable OAuth 2.0 Authorization Server (AS) role** and **OpenID Connect** are enabled.

3. Go to **System → OAuth Settings → Authorization Server Settings** and configure the authorization server settings.

4. Go to the client management section.

   ### Choose from:

   * If you are using PingFederate 10.0 or earlier, go to **System → OAuth Settings → Client Management**.

   * If you are using PingFederate 10.1 or later, go to **Applications → OAuth → Clients**.

5. Create or modify an existing client.

6. Ensure that **Client Secret** is enabled, and then enter a client secret to be used by PingAccess for authentication.

7. Grant access to the Session Revocation API.

   ### Choose from:

   * If you are using PingFederate 10.0 or earlier, in the **OpenID Connect** section of the client's configuration page, enable **Grant Access to Session Revocation API**.

   * If you are using PingFederate 10.1 or later, beside **Session API Endpoints**, select **Allow Access to Session Revocation API**.

     |   |                                                                                                           |
     | - | --------------------------------------------------------------------------------------------------------- |
     |   | This setting is the main setting that enables the server-side session management feature in PingFederate. |

8. Click **Save** to save your changes.

---

---
title: Configuring PingFederate for user-initiated single logout
description: Configure PingFederate to provide PingAccess with access to the PingFederate-managed session.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_configuring_pf_for_user_initiated_slo
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_configuring_pf_for_user_initiated_slo.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 6, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Configuring PingFederate for user-initiated single logout

Configure PingFederate to provide PingAccess with access to the PingFederate-managed session.

## Steps

1. Sign on to the PingFederate administrative console.

2. Go to **System → OAuth Settings → Authorization Server Settings**.

3. Select **Track User Sessions for Logout**.

4. Click **Save**.

5. Select an OpenID Connect policy.

   ### Choose from:

   * If you are using PingFederate 10.0 or earlier, go to **System → OAuth Settings → OpenID Connect Policy Management** and click an existing policy.

   * If you are using PingFederate 10.1 or later, go to **Applications → OAuth → OpenID Connect Policy Management** and click an existing policy.

6. On the **Manage Policy** tab, select **Include Session Identifier in ID Token**.

   For more information about configuring an OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
   \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
   \</div>)* Policy, see [Configuring OpenID Connect Policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_oidc_policies.html) in the PingFederate Administrator's Manual.

7. Click **Save**.

8. Select the client to be used by PingAccess.

   ### Choose from:

   * If you are using PingFederate 10.0 or earlier, go to **System → OAuth Settings → Client Management** and select the client to be used by PingAccess.

   * If you are using PingFederate 10.1 or later, go to **Applications → OAuth → Clients** and select the client to be used by PingAccess.

9. In the **OpenID Connect** section of the client's configuration page, select **PingAccess Logout Capable**.

   |   |                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------- |
   |   | If this option is not available, ensure that the **Track User Sessions for Logout** setting change made in step 3 was saved. |

10. Click **Save**.

---

---
title: Customize and localize PingAccess
description: This section contains information on how to customize PingAccess templates and localize user-facing messages.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_customize_localize_landing_topic
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_customize_localize_landing_topic.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 11, 2023
---

# Customize and localize PingAccess

This section contains information on how to customize PingAccess templates and localize user-facing messages.

* For information on customizing PingAccess page templates and on the difference between customizable templates and system templates, see [User-facing page customization reference](pa_user_facing_page_customization_ref.html).

* For information on localizing user-facing system status messages, see [User-facing page localization reference](pa_user_facing_page_localization_ref.html).

---

---
title: Enabling agent traffic logging
description: Enable agent audit logging, including requests and responses.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_enabling_agent_traffic_logging
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_enabling_agent_traffic_logging.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2023
section_ids:
  steps: Steps
  example: Example:
  example-2: Example:
  result: Result
---

# Enabling agent traffic logging

Enable agent audit logging, including requests and responses.

## Steps

1. Edit the `<PA_HOME>/conf/log4j2.xml` file.

2. In the Logger section, uncomment the `AppenderRef` element for the agent audit log HAR file.

   ### Example:

   ```
          <!-- Audit Log Configuration-->
           ...
           <Logger name="agentaudit" level="INFO" additivity="false">
               <AppenderRef ref="AgentAuditLog-File"/>
               <!--<AppenderRef ref="AgentAuditLog-Database-Failover"/>-->
               <!--<AppenderRef ref="AgentAuditLog-SQLServer-Database-Failover"/>-->
               <!--<AppenderRef ref="AgentAuditLog-PostgreSQL"/>-->
               <!--<AppenderRef ref="AgentAudit2Splunk"/>-->
               <AppenderRef ref="AgentAuditLog-HarFile"/>
           </Logger>
   ```

3. In the Appenders section, uncomment the `RollingFile` element for the engine audit log HAR file.

   ### Example:

   ```
       <Appenders>
           ...
           <RollingFile name="AgentAuditLog-HarFile"
                               fileName="${sys:pa.home}/log/pingaccess_agent_audit_har.log"
                               filePattern="${sys:pa.home}/log/pingaccess_agent_audit_har.%d{yyyy-MM-dd}.log"
                               ignoreExceptions="false">
               <StatusCodeRegExFilter regex=".*"/>
               <HarLogLayout>
                   <KeyValuePair key="AUDIT.metadata" value="true"/>
                   <KeyValuePair key="AUDIT.http-client" value="true"/>
                   <KeyValuePair key="AUDIT.http-app" value="true"/>
               </HarLogLayout>
               <Policies>
                   <TimeBasedTriggeringPolicy />
               </Policies>
           </RollingFile>
       </Appenders>
   ```

4. **Optional:** To filter the entries to add to the log file, edit the value of the `StatusCodeRegExFilter` element.

5. **Optional:** To specify what information to log, add or edit the values in the `HarLogLayout` section of the `RollingFile` element.

   You can add or edit metadata, client response, and app response values. For more information, see [Traffic logging reference](pa_traffic_logging_ref.html).

## Result

Logging begins when the configuration reloads. The configuration reloads at regular intervals according to the `monitorInterval` value.

---

---
title: Enabling API audit traffic logging
description: Enable API audit logging including request and responses.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_enabling_api_audit_traffic_logging
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_enabling_api_audit_traffic_logging.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2023
section_ids:
  steps: Steps
  example: Example:
  example-2: Example:
  result: Result
---

# Enabling API audit traffic logging

Enable API audit logging including request and responses.

## Steps

1. Edit the `<PA_HOME>/conf/log4j2.xml` file.

2. In the Logger section, uncomment the `AppenderRef` element for the API audit log HAR file.

   ### Example:

   ```
          <!-- Audit Log Configuration-->
           <Logger name="apiaudit" level="INFO" additivity="false">
               <AppenderRef ref="APIAuditLog-File"/>
               <!--<AppenderRef ref="ApiAuditLog-Database-Failover"/>-->
               <!--<AppenderRef ref="ApiAuditLog-SQLServer-Database-Failover"/>-->
               <!--<AppenderRef ref="ApiAuditLog-PostgreSQL"/>-->
               <!--<AppenderRef ref="ApiAudit2Splunk"/>-->
               <AppenderRef ref="ApiAuditLog-HarFile"/>
           </Logger>
   ```

3. In the Appenders section, uncomment the `RollingFile`.

   ### Example:

   ```
       <Appenders>
           ...
           <RollingFile name="ApiAuditLog-HarFile"
                               fileName="${sys:pa.home}/log/pingaccess_api_audit_har.log"
                               filePattern="${sys:pa.home}/log/pingaccess_api_audit_har.%d{yyyy-MM-dd}.log"
                               ignoreExceptions="false">
               <StatusCodeRegExFilter regex=".*"/>
               <HarLogLayout>
                   <KeyValuePair key="AUDIT.metadata" value="true"/>
                   <KeyValuePair key="AUDIT.http-client" value="true"/>
               </HarLogLayout>
               <Policies>
                   <TimeBasedTriggeringPolicy />
               </Policies>
           </RollingFile>
   ```

4. **Optional:** To filter the entries to add to the log file, edit the value of the `StatusCodeRegExFilter` element.

5. **Optional:** To specify what information to log, add or edit the values in the `HarLogLayout` section of the `RollingFile` element.

   You can add or edit metadata and client response values. For more information, see [Traffic logging reference](pa_traffic_logging_ref.html).

## Result

Logging begins when the configuration reloads. The configuration reloads at regular intervals according to the `monitorInterval` value.

---

---
title: Enabling cookie logging
description: Enable cookie logging, which is an optional feature in the TRACE log level.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_enabling_cookie_logging
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_enabling_cookie_logging.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2023
section_ids:
  steps: Steps
---

# Enabling cookie logging

Enable cookie logging, which is an optional feature in the `TRACE` log level.

## Steps

1. Edit the `conf/log4j2.xml` file and uncomment the following section:

   ```
   <AsyncLogger name="com.pingidentity.pa.core.interceptor.CookieLoggingInterceptor" level="TRACE" additivity="false" includeLocation="false">
        <AppenderRef ref="File"/>
   </AsyncLogger>
   ```

2. Save the file.

---

---
title: Enabling engine traffic logging
description: Enable engine audit logging, including requests and responses.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_enabling_engine_traffic_logging
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_enabling_engine_traffic_logging.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2023
section_ids:
  steps: Steps
  example: Example:
  example-2: Example:
  result: Result
---

# Enabling engine traffic logging

Enable engine audit logging, including requests and responses.

## Steps

1. Edit the `<PA_HOME>/conf/log4j2.xml` file.

2. In the Logger section, uncomment the `AppenderRef` element for the engine audit log HAR file.

   ### Example:

   ```
          <!-- Audit Log Configuration-->
           ...
           <Logger name="engineaudit" level="INFO" additivity="false">
               <AppenderRef ref="EngineAuditLog-File"/>
               <!--<AppenderRef ref="EngineAuditLog-Database-Failover"/>-->
               <!--<AppenderRef ref="EngineAuditLog-SQLServer-Database-Failover"/>-->
               <!--<AppenderRef ref="EngineAuditLog-PostgreSQL"/>-->
               <!--<AppenderRef ref="EngineAudit2Splunk"/>-->
               <AppenderRef ref="EngineAuditLog-HarFile"/>
           </Logger>
   ```

3. In the Appenders section, uncomment the `RollingFile` element for the engine audit log HAR file.

   ### Example:

   ```
       <Appenders>
           ...
           <RollingFile name="EngineAuditLog-HarFile"
                               fileName="${sys:pa.home}/log/pingaccess_engine_audit_har.log"
                               filePattern="${sys:pa.home}/log/pingaccess_engine_audit_har.%d{yyyy-MM-dd}.log"
                               ignoreExceptions="false">
               <StatusCodeRegExFilter regex=".*"/>
               <HarLogLayout>
                   <KeyValuePair key="AUDIT.metadata" value="true"/>
                   <KeyValuePair key="AUDIT.http-client" value="true"/>
                   <KeyValuePair key="AUDIT.http-app" value="true"/>
               </HarLogLayout>
               <Policies>
                   <TimeBasedTriggeringPolicy />
               </Policies>
           </RollingFile>
   ```

4. **Optional:** To filter the entries to add to the log file, edit the value of the `StatusCodeRegExFilter` element.

5. **Optional:** To specify what information to log, add or edit the values in the `HarLogLayout` section of the `RollingFile` element.

   You can add or edit metadata, client response, and app response values. For more information, see [Traffic logging reference](pa_traffic_logging_ref.html).

## Result

Logging begins when the configuration reloads. The configuration reloads at regular intervals according to the `monitorInterval` value.

---

---
title: Enabling sideband client traffic logging
description: Enable sideband client audit logging, including transactions sent to or from the sideband client integration.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_enabling_sideband_client_traffic_logging
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_enabling_sideband_client_traffic_logging.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2023
section_ids:
  steps: Steps
  example: Example:
  example-2: Example:
  result: Result
---

# Enabling sideband client traffic logging

Enable sideband client audit logging, including transactions sent to or from the sideband client integration.

## Steps

1. Edit the `<PA_HOME>/conf/log4j2.xml` file.

2. In the Logger section, uncomment the `AppenderRef` element for the sideband client audit log HAR file.

   ### Example:

   ```
          <!-- Audit Log Configuration-->
           ...
           <Logger name="sidebandclientaudit" level="INFO" additivity="false">
               <AppenderRef ref="SidebandClientAuditLog-File"/>
               <!--<AppenderRef ref="SidebandClientAuditLog-Database-Failover"/>-->
               <!--<AppenderRef ref="SidebandClientAuditLog-SQLServer-Database-Failover"/>-->
               <!--<AppenderRef ref="SidebandClientAuditLog-PostgreSQL"/>-->
               <!--<AppenderRef ref="SidebandClientAudit2Splunk"/>-->
               <AppenderRef ref="SidebandClientAuditLog-HarFile"/>
           </Logger>
   ```

3. In the Appenders section, uncomment the `RollingFile` element for the engine audit log HAR file.

   ### Example:

   ```
       <Appenders>
           ...
           <RollingFile name="SidebandClientAuditLog-HarFile"
                        fileName="${sys:pa.home}/log/pingaccess_sideband_client_audit_har.log"
                        filePattern="${sys:pa.home}/log/pingaccess_sideband_client_audit_har.%d{yyyy-MM-dd}.log"
                        ignoreExceptions="false">
               <StatusCodeRegExFilter regex="5.."/>
               <HarLogLayout clientBodySizeLimit="16384" appBodySizeLimit="16384">
                   <KeyValuePair key="AUDIT.metadata" value="true"/>
                   <KeyValuePair key="AUDIT.http-client" value="true"/>
                   <KeyValuePair key="AUDIT.http-app" value="true"/>
               </HarLogLayout>
               <Policies>
                   <TimeBasedTriggeringPolicy />
               </Policies>
           </RollingFile>
           ...
       </Appenders>
   ```

4. **Optional:** To filter the entries to add to the log file, edit the value of the `StatusCodeRegExFilter` element.

5. **Optional:** To specify what information to log, add or edit the values in the `HarLogLayout` section of the `RollingFile` element.

   You can add or edit metadata, client response, and app response values. For more information, see [Traffic logging reference](pa_traffic_logging_ref.html).

## Result

Logging begins when the configuration reloads. The configuration reloads at regular intervals according to the `monitorInterval` value.

---

---
title: Enabling sideband traffic logging
description: Enable sideband audit logging, including end-user transactions captured by the sideband client request.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_enabling_sideband_traffic_logging
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_enabling_sideband_traffic_logging.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2023
section_ids:
  steps: Steps
  example: Example:
  example-2: Example:
  result: Result
---

# Enabling sideband traffic logging

Enable sideband audit logging, including end-user transactions captured by the sideband client request.

## Steps

1. Edit the `<PA_HOME>/conf/log4j2.xml` file.

2. In the Logger section, uncomment the `AppenderRef` element for the sideband audit log HAR file.

   ### Example:

   ```
          <!-- Audit Log Configuration-->
           ...
           <Logger name="sidebandaudit" level="INFO" additivity="false">
               <AppenderRef ref="SidebandAuditLog-File"/>
               <!--<AppenderRef ref="SidebandAuditLog-Database-Failover"/>-->
               <!--<AppenderRef ref="SidebandAuditLog-SQLServer-Database-Failover"/>-->
               <!--<AppenderRef ref="SidebandAuditLog-PostgreSQL"/>-->
               <!--<AppenderRef ref="SidebandAudit2Splunk"/>-->
               <AppenderRef ref="SidebandAuditLog-HarFile"/>
           </Logger>
   ```

3. In the Appenders section, uncomment the `RollingFile` element for the engine audit log HAR file.

   ### Example:

   ```
       <Appenders>
           ...
           <RollingFile name="SidebandAuditLog-HarFile"
                        fileName="${sys:pa.home}/log/pingaccess_sideband_audit_har.log"
                        filePattern="${sys:pa.home}/log/pingaccess_sideband_audit_har.%d{yyyy-MM-dd}.log"
                        ignoreExceptions="false">
               <StatusCodeRegExFilter regex="5.."/>
               <HarLogLayout clientBodySizeLimit="16384" appBodySizeLimit="16384">
                   <KeyValuePair key="AUDIT.metadata" value="true"/>
                   <KeyValuePair key="AUDIT.http-client" value="true"/>
                   <KeyValuePair key="AUDIT.http-app" value="true"/>
               </HarLogLayout>
               <Policies>
                   <TimeBasedTriggeringPolicy />
               </Policies>
           </RollingFile>
           ...
       </Appenders>
   ```

4. **Optional:** To filter the entries to add to the log file, edit the value of the `StatusCodeRegExFilter` element.

5. **Optional:** To specify what information to log, add or edit the values in the `HarLogLayout` section of the `RollingFile` element.

   You can add or edit metadata, client response, and app response values. For more information, see [Traffic logging reference](pa_traffic_logging_ref.html).

## Result

Logging begins when the configuration reloads. The configuration reloads at regular intervals according to the `monitorInterval` value.

---

---
title: Enabling the CEF format file
description: Uncomment the CEF file appender references in the apiaudit, engineaudit, agentaudit, sidebandclientaudit, and sidebandaudit logger configurations.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_enabling_the_cef_format_file
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_enabling_the_cef_format_file.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 5, 2024
section_ids:
  steps: Steps
  example: Example:
  example-2: Example:
---

# Enabling the CEF format file

## Steps

1. Uncomment the CEF file appender references in the `apiaudit`, `engineaudit`, `agentaudit`, `sidebandclientaudit`, and `sidebandaudit` logger configurations.

   ### Example:

   In the `Audit log configuration` section of the `log4j2.xml` file, go to the `apiaudit` logger configuration and uncomment the `ApiAuditLogToCEF-FILE` appender reference:

   > **Collapse: Code**
   >
   > ```
   > <!-- ======================= -->
   > <!-- Audit log configuration -->
   > <!-- ======================= -->
   > <Logger name="apiaudit" level="${sys:pa.log.level.apiaudit:-INFO}" additivity="false">
   >    <AppenderRef ref="APIAuditLog-File"/>
   >    <!--<AppenderRef ref="ApiAuditLog-Database-Failover"/>-->
   >    <!--<AppenderRef ref="ApiAuditLog-SQLServer-Database-Failover"/>-->
   >    <!--<AppenderRef ref="ApiAuditLog-PostgreSQL"/>-->
   >    <!--<AppenderRef ref="ApiAudit2Splunk"/>-->
   >    <!--<AppenderRef ref="ApiAuditLog-HarFile"/>-->
   >     <AppenderRef ref="ApiAuditLogToCEF-File"/>
   >    <!--<AppenderRef ref="ApiAuditLogToCEF-Syslog-Failover"/>-->
   > </Logger>
   > ```

   Repeat this with the `EngineAuditLogToCEF-FILE`, `AgentAuditLogToCEF-FILE`, `SidebandClientAuditLogToCEF-FILE`, and `SidebandAuditLogToCEF-FILE` appender references.

2. Uncomment the `RollingFile` preset appender configurations in the `Api Audit log : CEF format file`, `Engine Audit log : CEF format file`, `Agent Audit log : CEF format file`, `SidebandClient Audit log : CEF format file`, and `Sideband Audit log : CEF format file` sections.

   ### Example:

   In the `Api Audit log : CEF format file` section, uncomment the `ApiAuditLogToCEF-FILE` `RollingFile` preset appender configuration:

   > **Collapse: Code**
   >
   > ```
   > <RollingFile name="ApiAuditLogToCEF-File"
   >              fileName="${sys:pa.home}/log/pingaccess_api_audit_cef.log"
   >              filePattern="${sys:pa.home}/log/pingaccess_api_audit_cef.%d{yyyy-MM-dd}.log" >
   >    <PatternLayout>
   >       <pattern>%escape{CEF}{CEF:0|Ping Identity|PingAccess|%X{AUDIT.paVersion}|%X{exchangeId}|API_AccessEvent|0|rt=%d{ISO8601} msg=%X{AUDIT.responseCode} duid=%X{AUDIT.subject} src=%X{AUDIT.client} requestMethod=%X{AUDIT.method} request=%X{AUDIT.requestUri} cs1Label=AuthenticationMechanism cs1=%X{AUDIT.authMech} cs2Label=RoundTripMS cs2=%X{AUDIT.roundTripMS} externalId=%X{AUDIT.trackingId} %n}</pattern>
   >    </PatternLayout>
   >    <Policies>
   > <TimeBasedTriggeringPolicy />
   >    </Policies>
   > </RollingFile>
   > ```

   Repeat this with the `EngineAuditLogToCEF-FILE`, `AgentAuditLogToCEF-FILE`, `SidebandClientAuditLogToCEF-FILE`, and `SidebandAuditLogToCEF-FILE` appender configurations.

3. Save and close the file.

---

---
title: Enabling the CEF formatted syslog appender
description: Uncomment the syslog failover appender references in the apiaudit, engineaudit, agentaudit, sidebandclientaudit, and sidebandaudit sections.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_enabling_the_cef_formatted_syslog_appender
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_enabling_the_cef_formatted_syslog_appender.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 5, 2024
section_ids:
  steps: Steps
  example: Example:
  example-2: Example:
---

# Enabling the CEF formatted syslog appender

## Steps

1. Uncomment the syslog failover appender references in the `apiaudit`, `engineaudit`, `agentaudit`, `sidebandclientaudit`, and `sidebandaudit` sections.

   ### Example:

   In the `Audit log configuration` section of the `log4j2.xml` file, go to the `apiaudit` logger configuration and uncomment the `<AppenderRef ref="ApiAuditLogToCEF-Syslog-Failover"/>` appender reference:

   > **Collapse: Code**
   >
   > ```
   > <!-- ======================= -->
   > <!-- Audit log configuration -->
   > <!-- ======================= -->
   > <Logger name="apiaudit" level="${sys:pa.log.level.apiaudit:-INFO}" additivity="false">
   >    <AppenderRef ref="APIAuditLog-File"/>
   >    <!--<AppenderRef ref="ApiAuditLog-Database-Failover"/>-->
   >    <!--<AppenderRef ref="ApiAuditLog-SQLServer-Database-Failover"/>-->
   >    <!--<AppenderRef ref="ApiAuditLog-PostgreSQL"/>-->
   >    <!--<AppenderRef ref="ApiAudit2Splunk"/>-->
   >    <!--<AppenderRef ref="ApiAuditLog-HarFile"/>-->
   >    <!--<AppenderRef ref="ApiAuditLogToCEF-File"/>-->
   >     <AppenderRef ref="ApiAuditLogToCEF-Syslog-Failover"/>
   > </Logger>
   > ```

   Repeat this with the `<AppenderRef ref="EngineAuditLogToCEF-Syslog-Failover"/>`, `<AppenderRef ref="AgentAuditLogToCEF-Syslog-Failover"/>`, `<AppenderRef ref="SidebandClientAuditLogToCEF-Syslog-Failover"/>`, and `<AppenderRef ref="SidebandAuditLogToCEF-Syslog-Failover"/>` appender references.

2. Uncomment the `Socket` appender configurations in the `Api Audit log : CEF Formatted syslog appender`, `Engine Audit log : CEF Formatted syslog appender`, `Agent Audit log : CEF Formatted syslog appender`, `SidebandClient Audit log : CEF Formatted syslog appender`, and `Sideband Audit log : CEF Formatted syslog appender` sections.

   |   |                                                                                                                                                                                                                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Each `Socket` appender is followed by two related appenders, `RollingFile` and `PingFailover`. Together, they create a running `audit-cef-syslog-failover.log` file in the *\<PA\_HOME>*/log/pingaccess.log directory if CEF logging fails for any reason. If you uncomment the `Socket` appenders, make sure to uncomment the related appenders also. |

   ### Example:

   In the `Api Audit log : CEF Formatted syslog appender` section, uncomment the `ApiAuditLogToCEF-Syslog` `Socket` appender configuration:

   > **Collapse: Code**
   >
   > ```
   > <!--
   > <Socket name="ApiAuditLogToCEF-Syslog" host="{syslog.host}" port="{syslog.port}" protocol="{syslog.protocol}" ignoreExceptions="false">
   >    <PingSyslogLayout>
   >       <PatternLayout>
   >          <pattern>%escape{CEF}{CEF:0|Ping Identity|PingAccess|%X{AUDIT.paVersion}|%X{exchangeId}|API_AccessEvent|0|rt=%d{ISO8601} msg=%X{AUDIT.responseCode} duid=%X{AUDIT.subject} src=%X{AUDIT.client} requestMethod=%X{AUDIT.method} request=%X{AUDIT.requestUri} cs1Label=AuthenticationMechanism cs1=%X{AUDIT.authMech} cs2Label=RoundTripMS cs2=%X{AUDIT.roundTripMS} externalId=%X{AUDIT.trackingId} %n}</pattern>
   >       </PatternLayout>
   >    </PingSyslogLayout>
   > </Socket>
   >
   > <RollingFile name="ApiAuditLogToCEF-Syslog-FILE"
   > fileName="${sys:pa.home}/log/pingaccess_api_audit_cef_syslog_failover.log"
   > filePattern="${sys:pa.home}/log/pingaccess_api_audit_cef_syslog_failover.%d{yyyy-MM-dd}.log"
   > ignoreExceptions="false">
   >    <PatternLayout>
   >       <pattern>%escape{CEF}{CEF:0|Ping Identity|PingAccess|%X{AUDIT.paVersion}|%X{exchangeId}|API_AccessEvent|0|rt=%d{ISO8601} msg=%X{AUDIT.responseCode} duid=%X{AUDIT.subject} src=%X{AUDIT.client} requestMethod=%X{AUDIT.method} request=%X{AUDIT.requestUri} cs1Label=AuthenticationMechanism cs1=%X{AUDIT.authMech} cs2Label=RoundTripMS cs2=%X{AUDIT.roundTripMS} externalId=%X{AUDIT.trackingId} %n}</pattern>
   >    </PatternLayout>
   >    <Policies>
   >       <TimeBasedTriggeringPolicy />
   >    </Policies>
   > </RollingFile>
   >
   > <PingAccessFailover name="ApiAuditLogToCEF-Syslog-Failover" primary="ApiAuditLogToCEF-Syslog" error="File">
   >    <Failovers>
   >       <AppenderRef ref="ApiAuditLogToCEF-Syslog-FILE" />
   >    </Failovers>
   > </PingAccessFailover>
   > -->
   > ```

   Repeat this with the `EngineAuditLogToCEF-Syslog`, `AgentAuditLogToCEF-Syslog`, `SidebandClientAuditLogToCEF-Syslog`, and `SidebandAuditLogToCEF-Syslog` appenders.

3. In the `ApiAuditToCEF-Syslog`, `EngineAuditToCEF-Syslog`, `AgentAuditToCEF-Syslog`, `SidebandClientAuditToCEF-Syslog`, and `SidebandAuditToCEF-Syslog` `Socket` appenders, replace the following placeholder parameter values:

   * syslog.host

     The URL of your syslog host server.

   * syslog.port

     The port that your syslog host server uses.

   * syslog.protocol

     The protocol that your syslog host server uses. Valid values are UDP or TCP.

     |   |                                          |
     | - | ---------------------------------------- |
     |   | Only the TCP protocol supports failover. |

4. Save and close the file.

---

---
title: Garbage collection logging
description: By default, PingAccess logs Java garbage collection data.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_garbage_collection_logging
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_garbage_collection_logging.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2023
---

# Garbage collection logging

By default, PingAccess logs Java garbage collection data.

The garbage collection log includes details related to each occurrence of garbage collection. For example, the log might record a timestamp and the change in heap memory.

Edit the following properties in the `<PA_HOME>/bin/run.sh` file on Linux systems or the `<PA_HOME>\bin\run.bat` file on Windows systems to configure garbage collection properties.

| Property                     | Description                                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `GC_FILE=`*"\<filename>"*    | Specifies the location of the garbage collection log. Comment out this line to disable garbage collection logging. |
| `GC_FILE_COUNT=`*"\<count>"* | Specifies the number of garbage collection files to retain before rotating.                                        |
| `GC_FILE_SIZE=`*"\<size>"*   | Specifies the maximum size for garbage collection files.                                                           |

---

---
title: Log configuration
description: This document describes the types of logging performed by PingAccess and provides instructions for configuring PingAccess logging.
component: pingaccess
version: 9.1
page_id: pingaccess:configuring_and_customizing_pingaccess:pa_logging_configuration
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/pa_logging_configuration.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 13, 2024
---

# Log configuration

This document describes the types of logging performed by PingAccess and provides instructions for configuring PingAccess logging.

* You can find information on types of logging in [Types of Logging](pa_types_of_logging.html).

  * You can find information on logging in the context of monitoring in [Logging, reporting, and troubleshooting](../pingaccess_monitoring_guide/pa_logging_reporting_and_troubleshooting.html).

  * You can find information on logging and auditing in the context of performance tuning in [Logging and Auditing](../reference_guides/pa_logging_and_auditing.html).

* You can find information on configuring and managing logging in [Configure logging in PingAccess](pa_configure_logging_lp.html).

  * You can find information on configuring log levels in the administrative console in [Log settings](../pingaccess_user_interface_reference_guide/pa_log_settings.html) also.

* You can find information on logging in the context of troubleshooting specific issues in [Log traffic for troubleshooting](pa_log_traffic_for_troubleshooting.html).

* You can find information on Common Event Format (CEF) *(tooltip: \<div class="paragraph">
  \<p>A logging and auditing file format that supports multiple device types.\</p>
  \</div>)*, JSON format, or logging formats usable by Splunk or a database in [Other logging formats](pa_other_logging_formats.html).