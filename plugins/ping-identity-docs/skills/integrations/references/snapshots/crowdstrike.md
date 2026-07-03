---
title: Changelog
description: The following is the change history for the CrowdStrike Integration Kit.
component: crowdstrike
page_id: crowdstrike:release_notes:pf_crowdstrike_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/crowdstrike/release_notes/pf_crowdstrike_ik_changelog.html
revdate: September 22, 2025
section_ids:
  crowdstrike-integration-kit-1-0-1-september-2025: CrowdStrike Integration Kit 1.0.1 - September 2025
  crowdstrike-integration-kit-1-0-february-2024: CrowdStrike Integration Kit 1.0 – February 2024
---

# Changelog

The following is the change history for the CrowdStrike Integration Kit.

## CrowdStrike Integration Kit 1.0.1 - September 2025

* Updated the dependencies that the CrowdStrike Integration Kit uses.

## CrowdStrike Integration Kit 1.0 – February 2024

* Initial release

---

---
title: Configuring an adapter instance
description: Configure the CrowdStrike IdP Adapter to determine how PingFederate communicates with CrowdStrike.
component: crowdstrike
page_id: crowdstrike:setup:pf_crowdstrike_ik_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/crowdstrike/setup/pf_crowdstrike_ik_configuring_an_adapter_instance.html
revdate: June 10, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  example: Example:
  result: Result:
  next-steps: Next steps
---

# Configuring an adapter instance

Configure the CrowdStrike IdP Adapter to determine how PingFederate communicates with CrowdStrike.

## Before you begin

Deploy the CrowdStrike Integration Kit files to your PingFederate directory.

## Steps

1. In the PingFederate administrative console, go to **Authentication > Integration > IdP Adapters** and click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. From the **Type** list, select **CrowdStrike IdP Adapter**. Click **Next**.

3. On the **IdP Adapter** tab, in the **CrowdStrike Service API Response Mappings** section, map the attributes from the CrowdStrike Service API response to the attribute contract:

   1. Click **Add a new row to 'CrowdStrike Service API Response Mappings'**.

   2. In the **Local Attribute** field, enter a name for an attribute.

   3. In the **CrowdStrike Service API Response Mapping** field, enter the JSON Pointer syntax for the source Google Verified Access API attributes, as shown in [JSON Pointer syntax reference](pf_crowdstrike_ik_json_pointer_syntax_reference.html).

      ### Example:

      For example, the JSON pointer `/resource/0/system_serial_number` will return the system serial number.

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a-d.

      ### Result:

      These attributes are now available in your PingFederate authentication policy.

4. On the **IdP Adapter** tab, configure the adapter instance by referring to [CrowdStrike IdP Adapter settings reference](pf_crowdstrike_ik_crowdstrike_idp_adapter_settings_reference.html). Click **Next**.

5. On the **Actions** tab, test your connection to the CrowdStrike service by fetching the API access token. Resolve any issues that are reported, and then click **Next**.

6. On the **Extended Contract** tab, add any attributes that you included in the **CrowdStrike Service API Response Mappings** section of the **IdP Adapter** tab. Click **Next**.

7. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

8. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

9. On the **Summary** tab, review your configuration. Click **Save**.

## Next steps

Review [Using CrowdStrike Risk Level](pf_crowdstrike_ik_using_crowdstrike_risk_level.html).

---

---
title: CrowdStrike IdP Adapter settings reference
description: Field descriptions for the CrowdStrike IdP Adapter configuration screen.
component: crowdstrike
page_id: crowdstrike:setup:pf_crowdstrike_ik_crowdstrike_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/crowdstrike/setup/pf_crowdstrike_ik_crowdstrike_idp_adapter_settings_reference.html
revdate: June 10, 2024
---

# CrowdStrike IdP Adapter settings reference

Field descriptions for the CrowdStrike IdP Adapter configuration screen.

**Standard fields**

| Field                              | Description                                                                                                                                                                                                                                       |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CrowdStrike Region**             | The CrowdStrike API region and API base URL to use.                                                                                                                                                                                               |
| **Client ID**                      | The client ID generated by CrowdStrike for access to the API.                                                                                                                                                                                     |
| **Client Secret**                  | The client secret generated by CrowdStrike for access to the API.                                                                                                                                                                                 |
| **CrowdStrike Service**            | The CrowdStrike service to use. The CrowdStrike adapter will only call one of the following CrowdStrike services. Supported services are:- **Incident Score of Device**

- **Zero Trust Assessment of Device**

- **Environment Wide CrowdScore** |
| **CrowdStrike Agent ID Attribute** | The incoming chained attribute that provides the value of the **CrowdStrike Agent ID**. The default attribute name that the adapter looks for is `crowdStrikeAgentId`.                                                                            |

**Advanced fields**

| Field                                 | Description                                                                                                                                                                                                                           |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Crowd Score Service Records Limit** | The maximum number of score records to return when the **CrowdStrike Service** is **Environment Wide CrowdScore**.The default value is `20`.                                                                                          |
| **High Score Threshold**              | If the CrowdStrike score is higher than this value, the adapter returns a `High` result.                                                                                                                                              |
| **Medium Score Threshold**            | If the CrowdStrike score is higher than this value but lower than or equal to the **High Score Threshold**, the adapter returns a `Medium` result.                                                                                    |
| **Low Score Threshold**               | If the CrowdStrike score is higher than this value but lower than or equal to the **Medium Score Threshold**, the adapter returns a `Low` result.                                                                                     |
| **API Request Timeout**               | The amount of time in milliseconds thatPingFederateallows when establishing a connection with the Google Verified Access API or waiting for a response to a request. A value of `0` disables the timeout.The default value is `5000`. |
| **Proxy Settings**                    | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                           |
| **Custom Proxy Host**                 | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                        |
| **Custom Proxy Port**                 | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                             |

---

---
title: CrowdStrike Integration Kit
description: When paired with the Google Chrome Enterprise Integration Kit in PingFederate, the CrowdStrike Integration Kit enables organizations to balance security and user experience.
component: crowdstrike
page_id: crowdstrike::pf_crowdstrike_ik
canonical_url: https://docs.pingidentity.com/integrations/crowdstrike/pf_crowdstrike_ik.html
revdate: September 22, 2025
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# CrowdStrike Integration Kit

When paired with the [Google Chrome Enterprise Integration Kit](../google/google_chrome_enterprise_integration_kit/pf_google_chrome_enterprise_ik.html) in PingFederate, the CrowdStrike Integration Kit enables organizations to balance security and user experience.

## Components

* CrowdStrike IdP Adapter

  When a user signs on through PingFederate, the adapter provides security posture for use in authentication policy decisions based on CrowdStrike signals received within the authentication flow. The CrowdStrike signals come from the [Google Chrome Enterprise Device Trust IdP Adapter](../google/google_chrome_enterprise_integration_kit/pf_google_chrome_enterprise_ik.html).

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following resources:

* The following sections of the PingFederate documentation:

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication Policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

|   |                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------- |
|   | To sign up for the CrowdStrike Falcon platform, contact [CrowdStrike](https://www.crowdstrike.com/products/). |

## System requirements

* PingFederate 11.3 or later

* To allow PingFederate to make outbound HTTPS connections, you might need to allow one of the following host names in your firewall:

  * <https://api.crowdstrike.com/>

  * <https://api.us-2.crowdstrike.com/>

  * <https://api.eu-1.crowdstrike.com>

  * <https://api.laggar.gcw.crowdstrike.com>

|   |                                                                             |
| - | --------------------------------------------------------------------------- |
|   | The host name to allow depends on the CrowdStrike API region configuration. |

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the CrowdStrike Integration Kit files to your PingFederate directory.
component: crowdstrike
page_id: crowdstrike:setup:pf_crowdstrike_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/crowdstrike/setup/pf_crowdstrike_ik_deploying_the_integration_files.html
revdate: June 10, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  next-steps: Next steps
---

# Deploying the integration files

To get started with the integration, deploy the CrowdStrike Integration Kit files to your PingFederate directory.

## Before you begin

1. Contact [CrowdStrike](https://www.crowdstrike.com/products/) to sign up for the CrowdStrike Falcon platform.

2. Configure the [Google Chrome Enterprise Device Trust IdP Adapter](../../google/google_chrome_enterprise_integration_kit/pf_google_chrome_enterprise_ik.html).

   |   |                                                                                                                                                                                                                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | As noted in [Using CrowdStrike Risk Level](pf_crowdstrike_ik_using_crowdstrike_risk_level.html), you must configure the Google Chrome Enterprise Device Trust IdP adapter or configure some other way to have the **CrowdStrike Agent ID** value sent to the CrowdStrike IdP Adapter for the CrowdStrike adapter flow to work. |

## Steps

1. Download the CrowdStrike Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/crowdstrike-integration-kit).

2. Stop PingFederate.

3. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Start PingFederate.

5. If you operate PingFederate in a cluster, repeat steps 2-4 for each engine node.

## Next steps

[Configure an adapter instance](pf_crowdstrike_ik_configuring_an_adapter_instance.html).

---

---
title: Download manifest
description: The following files are included in the CrowdStrike Integration Kit .zip archive.
component: crowdstrike
page_id: crowdstrike:release_notes:pf_crowdstrike_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/crowdstrike/release_notes/pf_crowdstrike_ik_download_manifest.html
revdate: June 10, 2024
---

# Download manifest

The following files are included in the CrowdStrike Integration Kit `.zip` archive.

* `Legal.pdf` – copyright and license information

* `dist/pingfederate/server/default` – contains the integration files

  * `deploy` – contains the Java libraries

    * `pf-crowdstrike-adapter-<version>.jar` – The CrowdStrike IdP Adapter

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for PingFederate, the CrowdStrike IdP Adapter, or both.
component: crowdstrike
page_id: crowdstrike:troubleshooting:pf_crowdstrike_ik_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/crowdstrike/troubleshooting/pf_crowdstrike_ik_enabling_debug_logging.html
revdate: June 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for PingFederate, the CrowdStrike IdP Adapter, or both.

## About this task

You can use logging for both troubleshooting and analytics.

For general information about logging, see [Enabling debug messages and console logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html) in the PingFederate documentation.

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

3. To log activity relating to the CrowdStrike IdP Adapter:

   ### Choose from:

   * To log activity for the CrowdStrike IdP Adapter as well as its HTTPS and component activity, add the following line:

     ```
     <Logger name="com.pingidentity.adapters.crowdstrike" level="DEBUG"/>
     ```

   * To log activity for the adapter's HTTPS activity and other components but not for the adapter itself, add the following line:

     ```
     <Logger name="com.pingidentity.adapters.crowdstrike.shade"  level="DEBUG"/>
     ```

   * To log activity for the CrowdStrike IdP Adapter but not its HTTPS or component activity, add the following lines:

     ```
     <Logger name="com.pingidentity.adapters.crowdstrike" level="DEBUG"/>
     <Logger name="com.pingidentity.adapters.crowdstrike.shade" level="INFO"/>
     ```

4. Save the file.

---

---
title: JSON Pointer syntax reference
description: JavaScript Object Notation (JSON) Pointer defines a syntax for identifying a specific value within a JSON payload. Using the sample payload and JSON Pointer examples below, identify the attributes that you want to use to populate your attribute contract.
component: crowdstrike
page_id: crowdstrike:setup:pf_crowdstrike_ik_json_pointer_syntax_reference
canonical_url: https://docs.pingidentity.com/integrations/crowdstrike/setup/pf_crowdstrike_ik_json_pointer_syntax_reference.html
revdate: June 10, 2024
section_ids:
  example-crowdstrike-incident-service-api-response-json-payload: Example CrowdStrike Incident service API response JSON payload
  json-pointer-syntax: JSON Pointer syntax
---

# JSON Pointer syntax reference

JavaScript Object Notation (JSON) Pointer defines a syntax for identifying a specific value within a JSON payload. Using the sample payload and JSON Pointer examples below, identify the attributes that you want to use to populate your attribute contract.

For a complete technical description of JSON Pointer syntax, see [JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901) on ietf.org.

## Example CrowdStrike Incident service API response JSON payload

```json
{
   "meta": {
      "query_time": 0.004738113,
       "powered_by": "incident-api",
       "trace_id": "b495ee9e-43e6-48bd-b0ac-19178ae304b1"
   },
   "resources": [
      {
         "incident_id": "inc:8389af03dfa04bac876ce5baf4a2dbbc:3d37a9f8c19b49b18bda301114c0861f",
         "incident_type": 1,
         "cid": "d1438ce1781d470aa639bb3374848448",
         "host_ids": [
             "8389af03dfa04bac876ce5baf4a2dbbc"
         ],
         "hosts": [
            {
               "device_id": "8389af03dfa04bac876ce5baf4a2dbbc",
               "cid": "d1438ce1781d470aa639bb3374848448",
               "agent_load_flags": "0",
               "agent_local_time": "2023-12-22T23:41:46.652Z",
               "agent_version": "6.42.15610.0",
               "bios_manufacturer": "Amazon EC2",
               "bios_version": "1.0",
               "config_id_base": "65994763",
               "config_id_build": "15610",
               "config_id_platform": "3",
               "external_ip": "34.219.249.45",
               "hostname": "EC2AMAZ-8FF6F2B",
               "first_seen": "2023-12-22T23:31:18Z",
               "last_login_timestamp": "2023-12-22T23:33:58Z",
               "last_login_user": "Administrator",
               "last_seen": "2024-01-17T22:19:59Z",
               "local_ip": "10.101.24.96",
               "mac_address": "06-66-9c-b8-bf-89",
               "machine_domain": "pfikteam.ping-eng.com",
               "major_version": "10",
               "minor_version": "0",
               "os_version": "Windows Server 2019",
               "ou": [
                   "Domain Controllers"
               ],
               "platform_id": "0",
               "platform_name": "Windows",
               "product_type": "2",
               "product_type_desc": "Domain Controller",
               "site_name": "Default-First-Site-Name",
               "status": "normal",
               "system_manufacturer": "Amazon EC2",
               "system_product_name": "t3.xlarge",
               "modified_timestamp": "2024-01-17T22:21:46Z",
               "instance_id": "i-00b24ead0c2e2bf27",
               "service_provider": "AWS_EC2_V2",
               "service_provider_account_id": "728729496554"
            }
         ],
         "created": "2024-01-17T22:38:30Z",
         "start": "2024-01-17T22:38:30Z",
         "end": "2024-01-17T22:39:04Z",
         "state": "open",
         "email_state": "START",
         "status": 20,
         "tactics": [
            "Falcon Overwatch"
         ],
         "techniques": [
         "Malicious Activity"
         ],
         "objectives": [
         "Falcon Detection Method"
         ],
         "modified_timestamp": "2024-01-17T22:39:09Z",
         "fine_score": 13
      }
   ],
   "errors": []
}
```

## JSON Pointer syntax

| Description                      | JSON Pointer                    | Example value     |
| -------------------------------- | ------------------------------- | ----------------- |
| Score of first incident detected | `/resources/0/final_sscore`     | `13`              |
| Host name of first incident      | `/resources/0/hosts/0/hostname` | `EC2AMAZ-8FF6F2B` |

|   |                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------- |
|   | To populate an attribute with the entire JSON response, leave the **CrowdStrike Service API Response Mappings** field blank. |

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the CrowdStrike Integration Kit.
component: crowdstrike
page_id: crowdstrike:release_notes:pf_crowdstrike_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/crowdstrike/release_notes/pf_crowdstrike_ik_known_issues_and_limitations.html
revdate: June 10, 2024
section_ids:
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the CrowdStrike Integration Kit.

## Known limitations

* The adapter does not implement support for the PingFederate Authentication API because it is not applicable in the CrowdStrike IdP Adapter flow. The adapter determines the score and risk level for the **CrowdStrike Agent ID** it receives from the [Google Chrome Enterprise Device Trust IdP Adapter](../../google/google_chrome_enterprise_integration_kit/pf_google_chrome_enterprise_ik.html) and according to the configured CrowdStrike service, and these determinations are immediately used in authentication policy decisions.

---

---
title: Overview of the SSO flow
description: The following figure illustrates an example SSO process flow.
component: crowdstrike
page_id: crowdstrike::pf_crowdstrike_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/crowdstrike/pf_crowdstrike_ik_overview_of_the_sso_flow.html
revdate: June 10, 2024
---

# Overview of the SSO flow

The following figure illustrates an example SSO process flow.

![A diagram illustrating a typical sign-on process leveraging the CrowdStrike Integration Kit.](_images/ojg1707777369202.png)

1. A user initiates the sign-on process by requesting access to a protected resource.

2. The [Google Chrome Enterprise Device Trust IdP Adapter](../google/google_chrome_enterprise_integration_kit/pf_google_chrome_enterprise_ik.html) determines if the incoming request is from the Google Chrome Enterprise browser. If so, the authentication request goes through the adapter flow, which fulfills core contract attributes, such as the **CrowdStrike Agent ID**.

3. The **CrowdStrike Agent ID** is made available to the CrowdStrike IdP Adapter.

4. The adapter invokes the configured CrowdStrike Service API for the agent ID that it received.

5. If the CrowdStrike incident returns with a score, the risk level value is fulfilled based on the threshold level scores configured in the adapter. Learn more in [CrowdStrike IdP Adapter settings reference](setup/pf_crowdstrike_ik_crowdstrike_idp_adapter_settings_reference.html).

6. The authentication policy can use the risk level value in subsequent decision making.

---

---
title: Using CrowdStrike Risk Level
description: Because the CrowdStrike IdP Adapter relies on the CrowdStrike Agent ID that is automatically detected and returned by the Google Chrome Enterprise Device Trust IdP Adapter, the CrowdStrike IdP Adapter is designed to work with the Google Chrome Enterprise Device Trust IdP Adapter flow.
component: crowdstrike
page_id: crowdstrike:setup:pf_crowdstrike_ik_using_crowdstrike_risk_level
canonical_url: https://docs.pingidentity.com/integrations/crowdstrike/setup/pf_crowdstrike_ik_using_crowdstrike_risk_level.html
revdate: June 10, 2024
---

# Using CrowdStrike Risk Level

Because the CrowdStrike IdP Adapter relies on the **CrowdStrike Agent ID** that is automatically detected and returned by the [Google Chrome Enterprise Device Trust IdP Adapter](../../google/google_chrome_enterprise_integration_kit/pf_google_chrome_enterprise_ik.html), the CrowdStrike IdP Adapter is designed to work with the Google Chrome Enterprise Device Trust IdP Adapter flow.

|   |                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you can make the **CrowdStrike Agent ID** of the authenticating user available to the CrowdStrike IdP Adapter without using the Google Chrome Enterprise Device Trust IdP adapter, then you don't need to configure the Google Chrome Enterprise Device Trust IdP adapter in the PingFederate authentication policy. |

The CrowdStrike IdP Adapter fulfills the `riskLevel` core contract attribute value based on the response it receives from the Google Chrome Enterprise Device Trust IdP Adapter and the threshold adapter's configuration. For example:

* If there are no incidents, or the returned score is less than the **Low Score Threshold** adapter configuration value, the `riskLevel` contract value is set to the value `zero_incidents`.

* If an incident is detected with a risk score in the range of the **High Score Threshold**, **Medium Score Threshold**, or **Low Score Threshold** field values as described in the [CrowdStrike IdP Adapter settings reference](pf_crowdstrike_ik_crowdstrike_idp_adapter_settings_reference.html), the `riskLevel` contract value is set to a value of `high`, `medium`, or `low` accordingly.

The following policy configuration shows a typical use case where a request coming from a trusted device goes through the Google Chrome Enterprise Device Trust IdP adapter and reaches the CrowdStrike IdP Adapter. The authentication policy is subsequently configured to handle and branch out based on different risk level scores.

![](_images/rsh1707838428768.png)