---
title: Changelog
description: The following is the change history for the ForgeRock Intelligent Access Integration Kit.
component: forgerock-intelligent-access
page_id: forgerock-intelligent-access:release_notes:pf_forgerock_intelligent_access_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/release_notes/pf_forgerock_intelligent_access_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2024
section_ids:
  forgerock-intelligent-access-integration-kit-1-0-february-2024: ForgeRock Intelligent Access Integration Kit 1.0 – February 2024
---

# Changelog

The following is the change history for the ForgeRock Intelligent Access Integration Kit.

## ForgeRock Intelligent Access Integration Kit 1.0 – February 2024

* Initial release

---

---
title: Configuring an adapter instance
description: Configure the ForgeRock Intelligent Access IdP Adapter to determine how PingFederate communicates with ForgeRock Intelligent Access.
component: forgerock-intelligent-access
page_id: forgerock-intelligent-access:setup:pf_forgerock_intelligent_access_ik_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/setup/pf_forgerock_intelligent_access_ik_configuring_an_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Configuring an adapter instance

Configure the ForgeRock Intelligent Access IdP Adapter to determine how PingFederate communicates with ForgeRock Intelligent Access.

## About this task

To begin the integration, deploy the ForgeRock Intelligent Access Integration Kit files to your PingFederate directory.

## Steps

1. In the PingFederate administrative console, go to **Authentication > Integration > IdP Adapters** and click **Create New Instance**.

2. On the Type tab, set the basic adapter instance attributes:

   1. In the Instance Name field, enter a name for the adapter instance.

   2. In the Instance ID field, enter a unique identifier for the adapter instance.

   3. From the Type list, select ForgeRock Intelligent Access IdP Adapter. Click Next.

3. **Optional:** On the **IdP Adapter** tab, in the **Response Mappings** section, map attributes from the ForgeRock Intelligent Access response to the attribute contract:

   1. In the **Local Attribute** field, enter a name of your choosing for an attribute.

   2. In the **Action** column, click **Update**.

   3. To add more attributes, repeat steps a-b.

      ### Result:

      These attributes become available in your PingFederate authentication policy.

4. On the IdP Adapter tab, configure the adapter instance by referring to [ForgeRock Intelligent Access IdP Adapter settings reference](pf_forgerock_intelligent_access_ik_forgerock_intelligent_access_idp_adapter_settings_reference.html). Click Next.

5. On the Extended Contract tab, add any attributes that you included in the ForgeRock Intelligent Access Response Mappings section of the IdP Adapter tab. Click Next.

6. On the Adapter Attributes tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click Next.

7. On the Adapter Contract Mapping tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click Next.

8. On the **Summary** tab, review your configuration. Click **Save**.

## Next steps

Review [Using ForgeRock Intelligent Access Journey](pf_forgerock_intelligent_access_ik_using_forgerock_intelligent_access_journey.html).

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the ForgeRock Intelligent Access Integration Kit files to your PingFederate directory.
component: forgerock-intelligent-access
page_id: forgerock-intelligent-access:setup:pf_forgerock_intelligent_access_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/setup/pf_forgerock_intelligent_access_ik_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  next-steps: Next steps
---

# Deploying the integration files

To get started with the integration, deploy the ForgeRock Intelligent Access Integration Kit files to your PingFederate directory.

## Before you begin

You must sign up for a ForgeRock Intelligent Access account.

## Steps

1. Download the ForgeRock Intelligent Access Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

2. Stop PingFederate.

3. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Start PingFederate.

5. If you operate PingFederate in a cluster, repeat steps 2-4 for each engine node.

## Next steps

[Configure an adapter instance](pf_forgerock_intelligent_access_ik_configuring_an_adapter_instance.html).

---

---
title: Download manifest
description: The following files are included in the ForgeRock Intelligent Access Integration Kit .zip archive.
component: forgerock-intelligent-access
page_id: forgerock-intelligent-access:release_notes:pf_forgerock_intelligent_access_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/release_notes/pf_forgerock_intelligent_access_ik_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2024
---

# Download manifest

The following files are included in the ForgeRock Intelligent Access Integration Kit `.zip` archive.

* `Legal.pdf` – copyright and license information

* `dist/pingfederate/server/default` – contains the integration files

  * `deploy` – contains the Java libraries

    * `pf-forgerock-intelligent-access-integration-kit-<version>.jar` – The ForgeRock Intelligent Access IdP Adapter

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for PingFederate, the ForgeRock Intelligent Access IdP Adapter, or both.
component: forgerock-intelligent-access
page_id: forgerock-intelligent-access:troubleshooting:pf_forgerock_intelligent_access_ik_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/troubleshooting/pf_forgerock_intelligent_access_ik_enabling_debug_logging.html
llms_txt: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for PingFederate, the ForgeRock Intelligent Access IdP Adapter, or both.

## About this task

You can use logging for troubleshooting and analytics.

Learn more about logging in [Enabling debug messages and console logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html) in the PingFederate documentation.

## Steps

1. Open the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file for editing.

2. To log activity for PingFederate and all adapters:

   1. Find the following section:

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   2. Change `INFO` to `DEBUG`:

      ```html
      <AsyncRoot level="DEBUG" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   3. **Optional:** To see the adapter activity in the console, remove the comment tags that surround the `CONSOLE` line:

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<AppenderRef ref="CONSOLE" />
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

3. To log activity relating to the ForgeRock Intelligent Access IdP Adapter:

   ### Choose from:

   * To log activity for the ForgeRock Intelligent Access IdP Adapter as well as its HTTPS and component activity, add the following line:

     ```
     <Logger name="com.pingidentity.adapters.forgerock" level="DEBUG"/>
     ```

   * To log activity for the adapter's HTTPS activity and other components but not for the adapter itself, add the following line:

     ```
     <Logger name="com.pingidentity.adapters.forgerock.shade" level="DEBUG"/>
     ```

   * To log activity for the ForgeRock Intelligent Access IdP Adapter but not its HTTPS or component activity, add the following lines:

     ```
     <Logger name="com.pingidentity.adapters.forgerock" level="DEBUG"/>
     <Logger name="com.pingidentity.adapters.forgerock.shade" level="INFO"/>
     ```

4. Save the file.

---

---
title: ForgeRock Intelligent Access IdP Adapter settings reference
description: Field descriptions for the ForgeRock Intelligent Access IdP Adapter configuration screen.
component: forgerock-intelligent-access
page_id: forgerock-intelligent-access:setup:pf_forgerock_intelligent_access_ik_forgerock_intelligent_access_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/setup/pf_forgerock_intelligent_access_ik_forgerock_intelligent_access_idp_adapter_settings_reference.html
llms_txt: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2024
---

# ForgeRock Intelligent Access IdP Adapter settings reference

Field descriptions for the ForgeRock Intelligent Access IdP Adapter configuration screen.

**Standard fields**

| Field                  | Description                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------- |
| **ForgeRock Base URL** | The ForgeRock Intelligent Access base URL, including context for the sign-on redirect. |
| **Realm**              | The ForgeRock Realm to call.                                                           |
| **Journey**            | The ForgeRock Journey or Tree to call.                                                 |
| **Cookie Name**        | The ForgeRock session cookie name.                                                     |

**Advanced fields**

| Field                   | Description                                                                                                                                                                                                                                   |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **API Request Timeout** | The amount of time in milliseconds that PingFederate allows when establishing a connection with the ForgeRock Intelligent Access API or waiting for a response to a request. A value of `0` disables the timeout.The default value is `5000`. |
| **Proxy Settings**      | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                                   |
| **Custom Proxy Host**   | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                |
| **Custom Proxy Port**   | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                     |

---

---
title: ForgeRock Intelligent Access Integration Kit
description: The ForgeRock Intelligent Access Integration Kit allows PingFederate to communicate with ForgeRock Intelligent Access and provide a rich sign-on orchestration experience.
component: forgerock-intelligent-access
page_id: forgerock-intelligent-access::pf_forgerock_intelligent_access_ik
canonical_url: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/pf_forgerock_intelligent_access_ik.html
llms_txt: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2024
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# ForgeRock Intelligent Access Integration Kit

The ForgeRock Intelligent Access Integration Kit allows PingFederate to communicate with ForgeRock Intelligent Access and provide a rich sign-on orchestration experience.

ForgeRock Intelligent Access can deploy at scale and across any platform. It's a software as a service (SaaS) application with self-managed options for:

* Public cloud deployment

* Private cloud deployment

* On-premises virtual machine deployment

* Bare metal server deployment

PingFederate outsources user sign-on experience to ForgeRock Intelligent Access.

## Components

* ForgeRock Intelligent Access IdP Adapter

  When a user signs on through PingFederate, the adapter validates whether there's a valid session cookie and whether it needs to create a new session with ForgeRock Intelligent Access.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following resources:

* <https://backstage.forgerock.com/docs/am/7.4/eval-guide/step-2-deploy-am.html>

## System requirements

* PingFederate 10.3 or later.

* You must deploy PingFederate and ForgeRock Intelligent Access on the same cookie domain because the current implementation relies on the presence and validation of a ForgeRock Intelligent Access single sign-on (SSO) *(tooltip: \<div class="paragraph">
  \<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
  \</div>)* cookie.

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the ForgeRock Intelligent Access Integration Kit.
component: forgerock-intelligent-access
page_id: forgerock-intelligent-access:release_notes:pf_forgerock_intelligent_access_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/release_notes/pf_forgerock_intelligent_access_ik_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2024
section_ids:
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the ForgeRock Intelligent Access Integration Kit.

## Known limitations

* The adapter does not implement support for the PingFederate Authentication API, as it isn't feasible to externally generate verified access challenge response values.

* The adapter does not yet provide the ability to map simple and advanced attributes from PingFederate to send to ForgeRock. This was included in version 1.0 of the integration kit but was removed before the release because of security concerns that will be addressed in the next release.

---

---
title: Overview of the SSO flow
description: The following figure illustrates an example SSO process flow.
component: forgerock-intelligent-access
page_id: forgerock-intelligent-access::pf_forgerock_intelligent_access_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/pf_forgerock_intelligent_access_ik_overview_of_the_sso_flow.html
llms_txt: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2024
---

# Overview of the SSO flow

The following figure illustrates an example SSO process flow.

![A diagram illustrating a typical sign on process leveraging the ForgeRock Intelligent Access Integration Kit.](_images/pcw1708036183304.png)

1. A user initiates the sign-on process by requesting access to a protected resource.

2. If PingFederate detects that the ForgeRock Intelligent Access cookie is not present, it redirects to a configurable Intelligent Access journey to orchestrate authentication. It also appends a PingFederate URL as a request parameter to resume the flow post-login.

   If a session cookie is present, the ForgeRock solution checks the session cookie against ForgeRock Intelligent Access to ensure its validity.

---

---
title: Using ForgeRock Intelligent Access Journey
description: To use a ForgeRock Intelligent Access Journey, you must install ForgeRock Access Management and perform the additional configuration steps described in this document.
component: forgerock-intelligent-access
page_id: forgerock-intelligent-access:setup:pf_forgerock_intelligent_access_ik_using_forgerock_intelligent_access_journey
canonical_url: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/setup/pf_forgerock_intelligent_access_ik_using_forgerock_intelligent_access_journey.html
llms_txt: https://docs.pingidentity.com/integrations/forgerock-intelligent-access/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  example: Example:
---

# Using ForgeRock Intelligent Access Journey

To use a ForgeRock Intelligent Access Journey, you must install ForgeRock Access Management and perform the additional configuration steps described in this document.

## Before you begin

Complete the steps in the ForgeRock Access Management (ForgeRock AM) installation [guide](https://backstage.forgerock.com/docs/am/7.4/install-guide/preface.html).

## About this task

Perform the following configuration steps in the ForgeRock Access Management admin console:

## Steps

1. If you do not have an alpha realm in your environment yet:

   1. Go to **Realms** and click **New Realm**.

   2. In the **Name** field, enter `alpha`.

   3. Click **Use Client-Side Sessions**.

   4. Click **Create** to save your configuration.

      |   |                                                                                                                                                                                                                                                                                       |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You should have an alpha realm because it's best practice to reserve the root realm for administrative operations. Learn more about configuring a realm in [Create a new realm](https://docs.pingidentity.com/pingam/7.5/setup-guide/configure-realms-console.html#create-new-realm). |

2. Enable goto and redirects for the validation service.

   By default, ForgeRock AM denies all goto and redirects after the sign on flow is complete.

   1. In the alpha realm, go to **Services**.

   2. If the **Validation Service** is not in the list of services, click **Add a Service** and in the **Choose a service type** drop-down list, select **Validation Service.**

   3. In the **Valid goto URL Resources** field, enter one or more valid URL patterns to allow.

      ### Example:

      * https\://*\<my-ping\_url>*:\*/\*

      * https\://*\<my-ping\_url>*:\*/**?**

3. Configure push authentication journeys by completing the steps in the [push authentication journeys guide](https://backstage.forgerock.com/docs/am/7.4/authentication-guide/authn-mfa-trees-push.html).

4. **Optional:** To adjust authentication session lifetimes:

   1. In the alpha realm, go to **Services**, click **Session**, then click **Create**.

   2. On the **Dynamic Attributes** tab, enter the desired values in the **Maximum Session Time** and **Maximum Idle Time** fields.

   3. Click **Save Changes**.