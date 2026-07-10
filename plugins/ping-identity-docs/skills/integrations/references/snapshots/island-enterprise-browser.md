---
title: Changelog
description: Change history for the Island Enterprise Browser Device Trust Integration Kit:
component: island-enterprise-browser
page_id: island-enterprise-browser:release_notes:pf_island_browser_changelog
canonical_url: https://docs.pingidentity.com/integrations/island-enterprise-browser/release_notes/pf_island_browser_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/island-enterprise-browser/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 6, 2025
section_ids:
  island-enterprise-browser-device-trust-integration-kit-1-0-august-2025: Island Enterprise Browser Device Trust Integration Kit 1.0 – August 2025
---

# Changelog

Change history for the Island Enterprise Browser Device Trust Integration Kit:

## Island Enterprise Browser Device Trust Integration Kit 1.0 – August 2025

* Initial release.

---

---
title: Configuring an adapter instance
description: Configure the Island Enterprise Browser Device Trust IdP Adapter to determine how PingFederate communicates with Island Enterprise.
component: island-enterprise-browser
page_id: island-enterprise-browser:setup:pf_island_browser_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/island-enterprise-browser/setup/pf_island_browser_configuring_an_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/island-enterprise-browser/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 6, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  next-steps: Next steps
---

# Configuring an adapter instance

Configure the Island Enterprise Browser Device Trust IdP Adapter to determine how PingFederate communicates with Island Enterprise.

## About this task

You must have permission to configure integrations in the Island management console (`fulladmin`, `system admin`). Learn more in [Configure Verified Device Access Integration in Island](https://documentation.island.io/v2/docs/configure-and-manage-verified-device-access-integration-for-ping-identity-1#configure-verified-device-access-integration-in-island) (requires sign-on).

While enabling permissions, identify the advanced settings criteria that align with your organization's requirements. Keep these criteria in mind when configuring a Island Enterprise Browser Device Trust IdP Adapter adapter instance.

## Steps

1. In the PingFederate admin console, go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a descriptive name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **Island Enterprise Browser Device Trust IdP Adapter**. Click **Next**.

3. (Optional) On the **IdP Adapter** tab, in the **Island Device Trust API Response Mappings** section, map attributes from the response issued by the Island Verify Challenge Response API endpoint to the attribute contract:

   1. Click **Add a new row to 'Island Device Trust API Response Mappings'**.

   2. In the **Local Attribute** field, enter a name of your choice for an attribute.

   3. In the **Verify Challenge Response Attribute Mapping** field, enter the JSON Pointer syntax for the source Island Device Trust API attributes as described in [JSON Pointer syntax](pf_island_browser_json_pointer_syntax_ref.html).

      ### Example:

      The JSON pointer `/deviceSignals/displayName` returns the machine display name.

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a - d.

4. On the **IdP Adapter** tab, configure the adapter instance by referring to [Island Enterprise Browser Device Trust IdP Adapter settings reference](pf_island_browser_idp_adapter_settings_ref.html). Click **Next**.

5. On the **Actions** tab, test your connection to the Island Generate Challenge API endpoint. Resolve any reported issues, then click **Next**.

6. On the **Extended Contract** tab, add any attributes you included in the **Island Device Trust API Response Mappings** section of the **IdP Adapter** tab. Click **Next**.

7. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

8. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

9. On the **Summary** tab, check and save your configuration. Click **Save**.

## Next steps

[Use Island Device Signals](pf_island_browser_using_island_device_signals.html).

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Island Enterprise Browser Device Trust Integration Kit files to your PingFederate directory.
component: island-enterprise-browser
page_id: island-enterprise-browser:setup:pf_island_browser_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/island-enterprise-browser/setup/pf_island_browser_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/island-enterprise-browser/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 6, 2025
section_ids:
  next-steps: Next steps
---

# Deploying the integration files

To get started with the integration, deploy the Island Enterprise Browser Device Trust Integration Kit files to your PingFederate directory.

1. Download the Island Enterprise Browser Device Trust Integration Kit `.zip` archive from the **Add-ons** tab of the [PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

2. Stop PingFederate if it's running.

3. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Start PingFederate.

5. If you operate PingFederate in a cluster, repeat steps 2 - 5 for each engine node.

## Next steps

[Configure an adapter instance](pf_island_browser_configuring_an_adapter_instance.html).

---

---
title: Download manifest
description: The following files are included in the Island Enterprise Browser Device Trust Integration Kit .zip archive:
component: island-enterprise-browser
page_id: island-enterprise-browser:release_notes:pf_island_browser_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/island-enterprise-browser/release_notes/pf_island_browser_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/island-enterprise-browser/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 6, 2025
---

# Download manifest

The following files are included in the Island Enterprise Browser Device Trust Integration Kit `.zip` archive:

* `legal/Legal.pdf`: Copyright and license information.

* `dist/pingfederate/server/default`: Contains the integration files.

  * `deploy`: Contains the Java libraries.

    * `pf-island-enterprise-browser-device-trust-adapter-<version>.jar`: A JAR file that contains the Island Enterprise Browser Device Trust IdP Adapter.

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for PingFederate, the Island Enterprise Browser Device Trust IdP Adapter, or both. You can also use logging for analytics.
component: island-enterprise-browser
page_id: island-enterprise-browser:troubleshooting:pf_island_browser_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/island-enterprise-browser/troubleshooting/pf_island_browser_enabling_debug_logging.html
llms_txt: https://docs.pingidentity.com/integrations/island-enterprise-browser/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 6, 2025
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for PingFederate, the Island Enterprise Browser Device Trust IdP Adapter, or both. You can also use logging for analytics.

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

3. To log only activity relating to the Island Enterprise Browser Device Trust IdP Adapter, do one of the following:

   ### Choose from:

   * To log activity for the Island Enterprise Browser Device Trust IdP Adapter as well as its HTTPS and component activity, add the following line:

     ```html
     <Logger name ="com.pingidentity.adapters.island.device.trust" level="DEBUG"/>
     ```

   * To log activity for the adapter's HTTPS activity and other components, but not the adapter itself, add the following line:

     ```html
     <Logger name ="com.pingidentity.adapters.island.device.trust.shade" level="DEBUG"/>
     ```

   * To log activity for the Island Enterprise Browser Device Trust IdP Adapter but not its HTTPS or component activity, add the following lines:

     ```html
     <Logger name ="com.pingidentity.adapters.island.device.trust" level="DEBUG"/>
     <Logger name ="com.pingidentity.adapters.island.device.trust.shade" level="INFO"/>
     ```

4. Save the file.

---

---
title: Island Enterprise Browser Device Trust IdP Adapter settings reference
description: Field descriptions for the Island Enterprise Browser Device Trust IdP Adapter configuration page:
component: island-enterprise-browser
page_id: island-enterprise-browser:setup:pf_island_browser_idp_adapter_settings_ref
canonical_url: https://docs.pingidentity.com/integrations/island-enterprise-browser/setup/pf_island_browser_idp_adapter_settings_ref.html
llms_txt: https://docs.pingidentity.com/integrations/island-enterprise-browser/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 6, 2025
---

# Island Enterprise Browser Device Trust IdP Adapter settings reference

Field descriptions for the **Island Enterprise Browser Device Trust IdP Adapter** configuration page:

> **Collapse: Standard fields**
>
> | Field Name  | Description                                                        |
> | ----------- | ------------------------------------------------------------------ |
> | **API Key** | The API key created in the Island platform.This field is required. |

> **Collapse: Advanced fields**
>
> | Field Name                             | Description                                                                                                                                                                                                                      |
> | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Island Device Trust API Base URL**   | The base URL for the Island Device Trust API.The default endpoint is `https://api.island.io.services/devices/api/v1/verified-device-access`.                                                                                     |
> | **Generate Challenge Endpoint**        | The endpoint used to generate a new challenge. This is generated based on the **Island Device Trust API Base URL** and **API Key** configured previously.The default endpoint is `/challenge/generate`.                          |
> | **Verify Challenge Response Endpoint** | The endpoint used to verify challenge responses. This is generated based on the **Island Device Trust API Base URL** and **API Key** configured previously.The default endpoint is `/challenge/verify`.                          |
> | **API Request Timeout**                | The amount of time in milliseconds that PingFederate allows when establishing a connection with Island Device Trust API or waiting for a response to a request. A value of `0` disables the timeout.The default value is `5000`. |
> | **Proxy Settings**                     | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                      |
> | **Custom Proxy Host**                  | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                   |
> | **Custom Proxy Port**                  | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                        |

---

---
title: Island Enterprise Browser Device Trust Integration Kit
description: Retrieve Island browser device posture information to use in authentication and authorization decisions.
component: island-enterprise-browser
page_id: island-enterprise-browser::pf_island_browser_ik
canonical_url: https://docs.pingidentity.com/integrations/island-enterprise-browser/pf_island_browser_ik.html
llms_txt: https://docs.pingidentity.com/integrations/island-enterprise-browser/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 21, 2025
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Island Enterprise Browser Device Trust Integration Kit

The Island Enterprise Browser Device Trust Integration Kit allows PingFederate to retrieve Island browser device posture information to use in authentication and authorization decisions.

## Components

* Island Enterprise Browser Device Trust IdP Adapter

  When a user signs on through PingFederate, the adapter validates if the request is from a verified and trusted device running Island browser, then retrieves the device signal information for use in authentication policy decisions.

## Intended audience

This document is intended for PingFederate admins. If you need help during the setup process, you can find more information in the following resources:

* The following sections of the Island Enterprise documentation (requires sign-on):

  * [Configure Verified Device Access Integration in Island](https://documentation.island.io/v2/docs/configure-and-manage-verified-device-access-integration-for-ping-identity-1#configure-verified-device-access-integration-in-island)

  * [Configure Verified Device Access Integration in Ping Identity](https://documentation.island.io/v2/docs/configure-and-manage-verified-device-access-integration-for-ping-identity-1#configure-verified-device-access-integration-in-ping-identity)

  * [Configure Verified Device Access Integration in Island (continued)](https://documentation.island.io/v2/docs/configure-and-manage-verified-device-access-integration-for-ping-identity-1#configure-verified-device-access-integration-in-island-continued)

  * [Verify the Verified Device Access Integration in Island](https://documentation.island.io/v2/docs/configure-and-manage-verified-device-access-integration-for-ping-identity-1#verify-the-verified-device-access-integration-in-island)

* The following sections of the PingFederate documentation:

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

## System requirements

* PingFederate 11.3 or later.

  * To allow PingFederate to make outbound HTTPS connections, you might need to allow the following host name in your firewall: https\://api.island.io/.

* Permission to configure integrations in the Island management console (`fulladmin`, `system admin`). Learn more in [Configure Verified Device Access Integration in Island](https://documentation.island.io/v2/docs/configure-and-manage-verified-device-access-integration-for-ping-identity-1#configure-verified-device-access-integration-in-island) (requires sign-on).

* To learn more about supported platforms, [contact the Island support team](https://www.island.io/lets-talk).

---

---
title: JSON Pointer syntax
description: JSON Pointer defines a syntax for identifying a specific value within a JSON payload. Using the following sample payload and JSON Pointer examples, identify the attributes you want to use to populate your attribute contract.
component: island-enterprise-browser
page_id: island-enterprise-browser:setup:pf_island_browser_json_pointer_syntax_ref
canonical_url: https://docs.pingidentity.com/integrations/island-enterprise-browser/setup/pf_island_browser_json_pointer_syntax_ref.html
llms_txt: https://docs.pingidentity.com/integrations/island-enterprise-browser/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 6, 2025
section_ids:
  example-island-browser-verify-challenge-response-api-json-payload: Example Island Browser Verify Challenge Response API JSON payload
---

# JSON Pointer syntax

JSON Pointer defines a syntax for identifying a specific value within a JSON payload. Using the following sample payload and JSON Pointer examples, identify the attributes you want to use to populate your attribute contract.

You can find a complete technical description of JSON Pointer syntax in [IETF RFC 6901 - JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901).

## Example Island Browser Verify Challenge Response API JSON payload

```json
{
    "devicePermanentId": "Q1M9T7X2KD",
    "virtualDeviceId": "Q1M9T7X2KD",
    "customerId": "ping-device-trust-integration",
    "signedPublicKeyAndChallenge": "",
    "deviceSignals": {
        "deviceManufacturer": "Apple Inc.",
        "deviceModel": "Mac14,5",
        "operatingSystem": "MAC_OS_X",
        "osVersion": "14.7.0",
        "displayName": "mac-24XXRFQW",
        "diskEncryption": "DISK_ENCRYPTION_ENABLED",
        "serialNumber": "Q1M9T7X2KD",
        "osFirewall": "OS_FIREWALL_ENABLED",
        "systemDnsServers": [
            "75.153.171.124:53",
            "8.8.8.8:53",
            "192.168.1.254:53"
        ],
        "macAddresses": [
            "da:1b:43:67:db:20",
            "b9:5b:77:ad:4c:b5"
        ],
        "screenLockSecured": "SCREEN_LOCK_ENABLED",
        "secureBootMode": "SECURE_BOOT_UNKNOWN",
        "browserVersion": "138.1.70.26",
        "deviceAffiliationIds": [],
        "profileAffiliationIds": [],
        "builtInDnsClientEnabled": true,
        "chromeRemoteDesktopAppBlocked": false,
        "safeBrowsingProtectionLevel": "STANDARD",
        "siteIsolationEnabled": true,
        "passwordProtectionWarningTrigger": "POLICY_UNSET",
        "realtimeUrlCheckMode": "REALTIME_URL_CHECK_MODE_UNSPECIFIED",
        "thirdPartyBlockingEnabled": false,
        "trigger": "TRIGGER_BROWSER_NAVIGATION"
    },
    "keyTrustLevel": "ISLAND_BROWSER_HW_KEY",
    "profileCustomerId": "ping-device-trust-integration",
    "virtualProfileId": "Q1M9T7X2KD",
    "profileKeyTrustLevel": "ISLAND_BROWSER_HW_KEY"
}
```

**JSON Pointer Syntax**

| Description       | JSON Pointer                  | Example value                               |
| ----------------- | ----------------------------- | ------------------------------------------- |
| `Browser version` | `/deviceSignals/browser`      | `138.1.70.26`                               |
| `Mac Addresses`   | `/deviceSignals/macAddresses` | `["da:1b:43:67:db:20","b9:5b:77:ad:4c:b5"]` |

|   |                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To populate an attribute with the entire JSON response, leave the **Verify Challenge Response Attribute Mapping** field blank in step 3c of [Configuring an adapter instance](pf_island_browser_configuring_an_adapter_instance.html). |

---

---
title: Known issues and limitations
description: Known issues or limitations for the Island Enterprise Browser Device Trust Integration Kit:
component: island-enterprise-browser
page_id: island-enterprise-browser:release_notes:pf_island_browser_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/island-enterprise-browser/release_notes/pf_island_browser_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/island-enterprise-browser/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 6, 2025
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

Known issues or limitations for the Island Enterprise Browser Device Trust Integration Kit:

## Known issues

There are no known issues.

## Known limitations

* PingFederate Authentication API support

  The Island Enterprise Browser Device Trust IdP Adapter doesn't support the PingFederate Authentication API because it's not feasible to generate the challenge response value externally. The challenge response is built into the Island Enterprise browser engine and only works with redirects.

---

---
title: Overview of the SSO flow
description: The following figure illustrates a single sign-on (SSO) scenario in which PingFederate authenticates users to a protected resource using the Island Enterprise Browser Device Trust IdP Adapter.
component: island-enterprise-browser
page_id: island-enterprise-browser::pf_island_browser_sso_flow_overview
canonical_url: https://docs.pingidentity.com/integrations/island-enterprise-browser/pf_island_browser_sso_flow_overview.html
llms_txt: https://docs.pingidentity.com/integrations/island-enterprise-browser/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 6, 2025
section_ids:
  description: Description
---

# Overview of the SSO flow

The following figure illustrates a single sign-on (SSO) scenario in which PingFederate authenticates users to a protected resource using the Island Enterprise Browser Device Trust IdP Adapter.

![A diagram illustrating a typical sign-on process leveraging the Island Enterprise Browser Device Trust Integration Kit.](_images/island_browser_sso_flow_diagram.png)

## Description

1. A user initiates the sign-on process by requesting access to a protected resource.

2. The Island Enterprise Browser Device Trust IdP Adapter determines if the incoming request is from the Island Enterprise browser.

   You can find more information about what happens with requests originating from any source in [Using Island Device Signals](setup/pf_island_browser_using_island_device_signals.html).

3. If Island Enterprise manages the user's browser, the adapter makes a backend call to the Island Enterprise challenge API endpoint to generate a challenge.

4. The adapter sends a `302` redirect to the PingFederate resume path with the challenge set in the response header.

5. The Island Enterprise browser processes the challenge and sets the response in the resume path request header.

6. The adapter finds the challenge response set by the browser and makes a backend call to the Island Enterprise verify challenge response API endpoint.

7. The Island Enterprise verify challenge response API endpoint verifies the response.

8. After successful verification, the adapter has access to the device signals from the browser.

9. The adapter uses the decoded device signals to fulfill the core contract for the authentication policy for subsequent decision-making.

---

---
title: Using Island Device Signals
description: The Island Enterprise Browser Device Trust IdP Adapter looks for a specific request header to determine where the request originates from.
component: island-enterprise-browser
page_id: island-enterprise-browser:setup:pf_island_browser_using_island_device_signals
canonical_url: https://docs.pingidentity.com/integrations/island-enterprise-browser/setup/pf_island_browser_using_island_device_signals.html
llms_txt: https://docs.pingidentity.com/integrations/island-enterprise-browser/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 7, 2025
section_ids:
  requests-from-verified-island-enterprise-browsers: Requests from verified Island Enterprise browsers
  requests-from-non-island-browsers-or-unverified-and-unmanaged-island-browsers: Requests from non-Island browsers or unverified and unmanaged Island browsers
  authentication-policy-configuration: Authentication policy configuration
---

# Using Island Device Signals

The Island Enterprise Browser Device Trust IdP Adapter looks for a specific request header to determine where the request originates from.

## Requests from verified Island Enterprise browsers

For requests originating from verified Island Enterprise browsers, the adapter initiates its flow as described in [Overview of the SSO flow](../pf_island_browser_sso_flow_overview.html) to retrieve device signals.

The adapter completes the flow successfully if the request originates from a managed browser and the adapter is able to retrieve device signals for the browser that are configured to work with the Island Enterprise platform. Depending on the availability of the attribute in the device signals, the adapter fulfills several core contract attributes, such as:

* `browserVersion`

* `displayName`

* `hostname`

* `macAddresses`

* `operatingSystem`

The `deviceTrustEnabled` core contract attribute is always set to a value of `true` after a flow completes successfully.

## Requests from non-Island browsers or unverified and unmanaged Island browsers

For requests originating from non-Island browsers or unverified Island browsers that aren't managed, the adapter immediately returns a `SUCCESS` status and only one core contract attribute, `deviceTrustEnabled`, set to a value of `false`.

## Authentication policy configuration

The authentication policy should typically use the `deviceTrustEnabled` contract attribute to make decisions related to stepping authentication flow with multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)*.

The adapter fails the authentication flow for the following cases:

* When a request originates from an unverified browser, causing the adapter to not retrieve device signals.

* When a runtime error occurs, such as a network error invoking the Island APIs. This can result in timeouts and other unexpected errors.

The authentication policy should be configured to handle these cases. For example, the following policy configuration describes a typical use case where:

* A request coming from a trusted device goes through HTML form adapter authentication only.

* A request coming from an untrustworthy device goes through HTML form adapter authentication as the first factor followed by MFA authentication as the second factor.

(Click the image to enlarge it.)

![Screen capture of an example policy configuration.](_images/island_browser_authn_policy.png)