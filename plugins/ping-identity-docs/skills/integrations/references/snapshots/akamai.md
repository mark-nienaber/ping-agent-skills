---
title: Akamai Account Protector IdP Adapter settings reference
description: Descriptions of standard and advanced fields that you can configure for the Akamai Account Protector IdP Adapter.
component: akamai
page_id: akamai:setup:pf-akamai-p7-adapter-settings-ref
canonical_url: https://docs.pingidentity.com/integrations/akamai/setup/pf-akamai-p7-adapter-settings-ref.html
llms_txt: https://docs.pingidentity.com/integrations/akamai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 30, 2026
---

# Akamai Account Protector IdP Adapter settings reference

Field descriptions for the Akamai Account Protector IdP Adapter configuration page.

> **Collapse: Standard fields**
>
> | Field Name             | Description                                                                                                                                                                                                                                                                                                                                                                                                                              |
> | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Medium Limit**       | Scores less than or equal to the configured **Medium Limit** value are classified as `LOW` risk. For requests with a low risk score, the `level` core contract attribute is set to `low`.The default value is `25`.                                                                                                                                                                                                                      |
> | **High Limit**         | Scores greater than the configured **Medium Limit** and less than or equal to the configured **High Limit** value are classified as `MEDIUM` risk. For requests with a medium risk score, the `level` core contract attribute is set to `medium`.Scores exceeding the **High Limit** are classified as `HIGH` risk. For requests with a high risk score, the `level` core contract attribute is set to `high`.The default value is `50`. |
> | **Save Akamai Header** | If you select this checkbox, the adapter exposes any additional key and value pairs it parses from the Akamai Account Protector header as adapter attributes.&#xA;&#xA;The adapter provides the score and level core contract attributes regardless of whether this checkbox is selected.This checkbox is cleared by default.                                                                                                            |

> **Collapse: Advanced fields**
>
> | Field Name                               | Description                                                                                |
> | ---------------------------------------- | ------------------------------------------------------------------------------------------ |
> | **Akamai Account Protector Header Name** | The Akamai Account Protector HTTP header to parse.The default value is `Akamai-User-Risk`. |

---

---
title: Akamai Account Protector Integration Kit
description: Overview of the components, requirements, and benefits of integrating the Akamai Account Protector Integration Kit with PingFederate.
component: akamai
page_id: akamai::pf-akamai-p1-homepage
canonical_url: https://docs.pingidentity.com/integrations/akamai/pf-akamai-p1-homepage.html
llms_txt: https://docs.pingidentity.com/integrations/akamai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 30, 2026
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Akamai Account Protector Integration Kit

The Akamai Account Protector Integration Kit enables PingFederate to access the Akamai Account Protector header and use the associated risk score to inform authentication and authorization decisions.

|   |                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The default request header the adapter looks for is `Akamai-User-Risk`. To change this value, configure the **Akamai Account Protector Header Name** advanced field as described in [Akamai Account Protector IdP Adapter settings reference](setup/pf-akamai-p7-adapter-settings-ref.html). |

## Components

* Akamai Account Protector IdP Adapter

  When a user signs on through PingFederate, the adapter:

  * Examines the incoming request and collects the Akamai Account Protector header.

  * Extracts the risk score value from the header.

  * Assigns appropriate risk level and score values based on thresholds you configure for authentication policy decisions.

## Intended audience

This document is intended for PingFederate administrators. If you need help during the setup process, you can find more information in the following resources:

* [Account Protector](https://techdocs.akamai.com/account-protector/docs/welcome-to-account-protector) (requires sign-on) in the Akamai TechDocs.

* The following sections of the PingFederate documentation:

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

## System requirements

* PingFederate 11.3 or later

---

---
title: Configuring an adapter instance
description: Learn how to create an Akamai Account Protector IdP Adapter instance.
component: akamai
page_id: akamai:setup:pf-akamai-p6-configuring-an-adapter-instance
canonical_url: https://docs.pingidentity.com/integrations/akamai/setup/pf-akamai-p6-configuring-an-adapter-instance.html
llms_txt: https://docs.pingidentity.com/integrations/akamai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 30, 2026
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Configuring an adapter instance

Configure the Akamai Account Protector IdP Adapter to determine how PingFederate handles the incoming Akamai Account Protector header.

## Steps

1. In the PingFederate admin console, go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **Akamai Account Protector IdP Adapter**. Click **Next**.

3. On the **IdP Adapter** tab, configure the adapter instance by referring to [Akamai Account Protector IdP Adapter settings reference](pf-akamai-p7-adapter-settings-ref.html). Click **Next**.

4. On the **Extended Contract** tab, add any attributes exposed with the **Save Akamai Header** adapter configuration for use in authentication.

   You can find more information in the **Save Akamai Header** standard field description in [Akamai Account Protector IdP Adapter settings reference](pf-akamai-p7-adapter-settings-ref.html).

5. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

6. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in the [Defining the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

7. On the **Summary** tab, check and save your configuration. Click **Save**.

## Next steps

[Use risk score in the PingFederate authentication policy](pf-akamai-p8-using-score.html).

---

---
title: Deploying the integration files
description: Download the Akamai Account Protector Integration Kit [.filepath]``.zip`` file and deploy it to your PingFederate directory.
component: akamai
page_id: akamai:setup:pf-akamai-p5-deploying-the-integration-files
canonical_url: https://docs.pingidentity.com/integrations/akamai/setup/pf-akamai-p5-deploying-the-integration-files.html
llms_txt: https://docs.pingidentity.com/integrations/akamai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 30, 2026
section_ids:
  download-manifest: Download manifest
  steps: Steps
  next-steps: Next steps
---

# Deploying the integration files

To get started with the integration, deploy the Akamai Account Protector Integration Kit files to your PingFederate directory.

## Download manifest

The following files are included in the Akamai Account Protector Integration Kit `.zip` archive.

> **Collapse: Included files**
>
> * `Legal.pdf`: Copyright and license information.
>
> * `dist/pingfederate/server/default`: Contains the integration files.
>
>   * `deploy`: Contains the Java libraries.
>
>     * `pf-akamai-account-protector-adapter-<version>.jar`: A `.jar` file containing the Akamai Account Protector IdP Adapter.

## Steps

1. Download the Akamai Account Protector Integration Kit `.zip` archive from the **Add-ons** tab of the [PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

2. Stop PingFederate if it's running.

3. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Start PingFederate.

5. If you operate PingFederate in a cluster, repeat steps 1 - 4 for each engine node.

## Next steps

[Configure an adapter instance](pf-akamai-p6-configuring-an-adapter-instance.html).

---

---
title: Enabling debug logging
description: Configure activity logging to troubleshoot how your Akamai Account Protector IdP Adapter instance integrates with PingFederate.
component: akamai
page_id: akamai:troubleshooting:pf-akamai-p9-enabling-debug-logging
canonical_url: https://docs.pingidentity.com/integrations/akamai/troubleshooting/pf-akamai-p9-enabling-debug-logging.html
llms_txt: https://docs.pingidentity.com/integrations/akamai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 30, 2026
section_ids:
  steps: Steps
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for PingFederate, the Akamai Account Protector IdP Adapter, or both. You can also use logging for analytics.

|   |                        |
| - | ---------------------- |
|   | This task is optional. |

You can find general information about logging in [Enabling debug messages and console logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html) in the PingFederate documentation.

## Steps

1. Open the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file for editing.

2. To log activity for PingFederate and all adapters:

   1. Go to the following section in the `log4j2.xml` file:

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

   3. (Optional) To see the adapter activity in the console as well as the log file, remove the comment tags surrounding the CONSOLE line:

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<AppenderRef ref="CONSOLE" />
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

3. To log activity relating to the Akamai Account Protector IdP Adapter only, add the following line:

   ```html
   <Logger name ="com.pingidentity.adapters.akamai.account.protector" level="DEBUG"/>
   ```

4. Save the file.

---

---
title: Overview of the SSO flow
description: Description of the SSO flow when using the Akamai Account Protector Integration Kit.
component: akamai
page_id: akamai::pf-akamai-p2-sso-flow-overview
canonical_url: https://docs.pingidentity.com/integrations/akamai/pf-akamai-p2-sso-flow-overview.html
llms_txt: https://docs.pingidentity.com/integrations/akamai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 30, 2026
---

# Overview of the SSO flow

The following description covers the typical sign-on process when using the Akamai Account Protector Integration Kit.

1. A user initiates the sign-on process by requesting access to a protected resource.

2. The Akamai Account Protector IdP Adapter collects and parses the Akamai Account Protector header from the incoming request.

   |   |                                                                                                                                                                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The default request header the adapter looks for is `Akamai-User-Risk`. To change this value, configure the **Akamai Account Protector Header Name** advanced field as described in [Akamai Account Protector IdP Adapter settings reference](setup/pf-akamai-p7-adapter-settings-ref.html). |

3. Based on the threshold values you [configure in the adapter instance](setup/pf-akamai-p6-configuring-an-adapter-instance.html), the adapter evaluates the request and determines a risk level.

   You can then use the resulting risk level and corresponding score to drive authentication policy decisions. Learn more in [Using risk score in the PingFederate authentication policy](setup/pf-akamai-p8-using-score.html).

4. If you select the [**Save Akamai Header**](setup/pf-akamai-p7-adapter-settings-ref.html) checkbox in the adapter configuration, the adapter exposes individually retrieved values as core contract attributes, making them available to use within PingFederate authentication policies.

---

---
title: Release notes
description: Release notes for the Akamai Account Protector Integration Kit.
component: akamai
page_id: akamai::pf-akamai-p3-rn
canonical_url: https://docs.pingidentity.com/integrations/akamai/pf-akamai-p3-rn.html
llms_txt: https://docs.pingidentity.com/integrations/akamai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 30, 2026
section_ids:
  version-1-0: Version 1.0
  initial-release: Initial release
  known-limitations: Known limitations
---

# Release notes

The change history for the Akamai Account Protector Integration Kit.

## Version 1.0

Released in March 2026.

### Initial release

New IK-3834

* Learn more about how the Akamai Account Protector Integration Kit works in [Akamai Account Protector Integration Kit](pf-akamai-p1-homepage.html) and [Overview of the SSO flow](pf-akamai-p2-sso-flow-overview.html).

* You can find more information about how to configure the IK in [Setup](setup/pf-akamai-p4-setup.html) and about troubleshooting in [Enabling debug logging](troubleshooting/pf-akamai-p9-enabling-debug-logging.html).

## Known limitations

* The adapter doesn't support using the PingFederate Authentication API because it isn't applicable.

---

---
title: Setup
description: Setup tasks for the Akamai Account Protector Integration Kit.
component: akamai
page_id: akamai:setup:pf-akamai-p4-setup
canonical_url: https://docs.pingidentity.com/integrations/akamai/setup/pf-akamai-p4-setup.html
llms_txt: https://docs.pingidentity.com/integrations/akamai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 30, 2026
---

# Setup

To configure the Akamai Account Protector Integration Kit, complete the following steps in order:

1. [Deploy the integration files](pf-akamai-p5-deploying-the-integration-files.html).

2. [Configure an adapter instance](pf-akamai-p6-configuring-an-adapter-instance.html), using the [Akamai Account Protector IdP Adapter settings reference](pf-akamai-p7-adapter-settings-ref.html) to complete specific fields.

3. [Use score in the PingFederate authentication policy](pf-akamai-p8-using-score.html).

You can find troubleshooting information in [Enabling debug logging](../troubleshooting/pf-akamai-p9-enabling-debug-logging.html).

---

---
title: Using risk score in the PingFederate authentication policy
description: Guidance on how to configure a branching PingFederate authentication policy based on an assigned risk score.
component: akamai
page_id: akamai:setup:pf-akamai-p8-using-score
canonical_url: https://docs.pingidentity.com/integrations/akamai/setup/pf-akamai-p8-using-score.html
llms_txt: https://docs.pingidentity.com/integrations/akamai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 30, 2026
section_ids:
  how-the-adapter-handles-requests-with-or-without-the-specified-request-header: How the adapter handles requests with or without the specified request header
  configuring-the-pingfederate-authentication-policy: Configuring the PingFederate authentication policy
---

# Using risk score in the PingFederate authentication policy

After receiving a request, the Akamai Account Protector IdP Adapter examines it to determine if the Akamai Account Protector header is present. If the header is present, the adapter parses its value as described in the following sections.

|   |                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The default request header the adapter looks for is `Akamai-User-Risk`. To change this value, configure the **Akamai Account Protector Header Name** advanced field as described in [Akamai Account Protector IdP Adapter settings reference](pf-akamai-p7-adapter-settings-ref.html). |

## How the adapter handles requests with or without the specified request header

Based on the threshold values configured in the adapter instance, the adapter evaluates the incoming request and determines a risk level. You can then use the resulting risk level and corresponding score to drive authentication policy decisions.

* Learn more about configuring threshold values in the **Medium Limit** and **High Limit** fields described in [Akamai Account Protector IdP Adapter settings reference](pf-akamai-p7-adapter-settings-ref.html).

* Learn more about using the risk score in the authentication policy in the Authentication policy configuration section.

If the Akamai Account Protector header isn't present in the incoming request:

* The adapter exits, setting the `status` to `SUCCESS` and the `level` core contract attribute to `noscore`.

* The adapter doesn't fulfill the `score` contract attribute.

## Configuring the PingFederate authentication policy

1. In the PingFederate admin console, go to **Authentication > Policies > Policies** and make sure the **IdP Authentication Policies** checkbox is selected.

2. Open an existing policy or click **Add Policy**.

   You can find more information in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

3. In the **Policy** area, in the **Select** list, select a Akamai Account Protector IdP Adapter adapter instance.

4. In the **Rules** modal, create paths for the possible outcomes of the `level` core contract attribute.

   You can find more information in [Configuring rules in authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_rules_auth_policies.html) in the PingFederate documentation.

   1. Under the Akamai Account Protector IdP Adapter adapter instance, click **Rules**.

   2. In the **Authentication Source** list, select the adapter instance.

   3. In the **Attribute Name** list, select the `level` core contract attribute.

   4. In the **Condition** list, select **equal to**.

   5. In the **Value** field, enter `low`, `medium`, `high`, `no_score`, or `client_error`.

      |   |                                                                                                                                                                                                                                                                                                                    |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | `client_error` is a value the adapter sets if it received the Akamai Account Protector header but encountered a runtime error when reading the `score` value. For example, if the value isn't an integer, the adapter can't determine where it falls as far as the configured **Medium Limit** and **High Limit**. |

   6. In the **Result** field, enter a name.

      This appears as a new policy path that branches from the authentication source.

   7. To add more policy paths, click **Add** and repeat steps a - e.

   8. (Optional) Clear the **Default to success** checkbox.

   9. Click **Done**.

   For example:

   ![Screen capture of an example rules configuration for the Akamai Account Protector IdP Adapter.](_images/akamai-authn-policy.png)

5. Configure each of the authentication policy paths you created based on the output of the `level` core contract attribute.

6. Click **Done**.

7. In the **Policies** window, click **Save**.