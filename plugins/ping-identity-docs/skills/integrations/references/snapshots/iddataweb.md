---
title: Adding device profiling to a web application
description: If you have a web application that uses the PingFederate authentication API and cannot accommodate HTTP cookies, modify your web application to run the device profiling script.
component: iddataweb
page_id: iddataweb:setup:pf_iddataweb_ik_adding_device_profiling_to_a_web_application
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/setup/pf_iddataweb_ik_adding_device_profiling_to_a_web_application.html
revdate: June 24, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to a web application

If you have a web application that uses the PingFederate authentication API and cannot accommodate HTTP cookies, modify your web application to run the device profiling script.

## About this task

Learn more in [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

## Steps

1. Add the following code to the sign-on page:

   ```
   <script type="text/javascript"
   src="<device profiling URL>"></script>
   ```

   For each sign-on event, insert the device profiling URL from PingFederate.

2. Configure your application to complete the following actions in sequence:

   1. Get the device profiling URL from PingFederate. This is an attribute of the `DEVICE_PROFILE_REQUIRED` state.

   2. Run the device profiling script by including it in the page.

   3. POST `continueAuthentication` to the authentication API.

3. When you complete the steps in [Configuring an adapter instance](pf_iddataweb_ik_configuring_an_adapter_instance.html), set the **Device profiling method** to **Captured by this adapter**.

---

---
title: Adding device profiling to an authentication page
description: Instead of using the ID DataWeb IdP Adapter to collect the device profile, you can capture the device profile using an existing sign-on page. This can reduce perceived wait times for the user.
component: iddataweb
page_id: iddataweb:setup:pf_iddataweb_ik_adding_device_profiling_to_an_authentication_page
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/setup/pf_iddataweb_ik_adding_device_profiling_to_an_authentication_page.html
revdate: July 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to an authentication page

Instead of using the ID DataWeb IdP Adapter to collect the device profile, you can capture the device profile using an existing sign-on page. This can reduce perceived wait times for the user.

## About this task

You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in [Device profiling methods](../pf_iddataweb_ik_device_profiling_methods.html).

## Steps

1. Embed the JavaScript files in the page.

   1. If you're modifying an external web application, copy the `id_dataweb_device_profiling.js` file from the integration `.zip` archive to a location that your page can access.

   2. Add the following to the sign-on page and adjust the path to the script file:

      ```
      <script type="text/javascript" src="id_dataweb_device_profiling.js"></script>
      ```

      |   |                                                                                                                  |
      | - | ---------------------------------------------------------------------------------------------------------------- |
      |   | If you're modifying a PingFederate template, the script path is `assets/scripts/id_dataweb_device_profiling.js`. |

   3. Save the file.

2. (Optional) In the script file, customize the name prefix for the device profile cookie to suit your environment.

   ```
   var cookieName = "idwUUID";
   ```

3. When you complete the steps in [Configuring an adapter instance](pf_iddataweb_ik_configuring_an_adapter_instance.html):

   1. Set the **Device profiling method** to **Captured by a previous adapter**.

   2. Update the **Cookie name** field if you customized it in step 2.

---

---
title: Adding ID DataWeb policy decisions to your authentication policy
description: By modifying your PingFederate authentication policy to include the policy decision (approve, obligation, or deny) from the ID DataWeb API, you can change authentication requirements dynamically based on security risk level.
component: iddataweb
page_id: iddataweb:setup:pf_iddataweb_ik_adding_id_dataweb_policy_decisions_to_your_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/setup/pf_iddataweb_ik_adding_id_dataweb_policy_decisions_to_your_authentication_policy.html
revdate: June 24, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding ID DataWeb policy decisions to your authentication policy

By modifying your PingFederate authentication policy to include the policy decision (`approve`, `obligation`, or `deny`) from the ID DataWeb API, you can change authentication requirements dynamically based on security risk level.

## About this task

These steps are designed to help you add to an existing authentication policy. You can find general information about configuring authentication policies in [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html) in the PingFederate documentation.

## Steps

1. In the PingFederate administrative console, go to **Authentication > Policies > Policies**.

2. Select the **IdP Authentication Policies** checkbox.

3. Open an existing authentication policy, or click **Add Policy**.

   Learn more in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

4. In the **Policy** area, in the **Select** list, select an ID DataWeb IdP Adapter instance.

   ![policy success path](_images/policy_success_path.jpg)

5. Map the user ID into the ID DataWeb IdP Adapter instance:

   ![incoming user id](_images/incoming_user_id.jpg)

   1. Under the ID DataWeb IdP Adapter instance, click **Options**.

   2. On the **Options** dialog, in the **Source** list, select a previous authentication source that collects the user ID.

   3. In the **Attribute** list, select the user ID. Click **Done**.

6. Define policy paths based on risk results:

   ![policy decision equal to rules](_images/policy_decision_equal_to_rules.jpg)

   1. Under the ID DataWeb IdP Adapter instance, click **Rules**.

   2. On the **Rules** dialog, in the **Attribute Name** list, select **policyDecision**.

   3. In the **Condition** list, select **equal to**.

   4. In the **Value** field, enter `approve`, `obligation`, or `deny`.

   5. In the **Result** field, enter a name. This appears as a new policy path that branches from the authentication source.

   6. If you want to add more authentication paths, click **Add** and repeat steps a-e.

   7. Click **Done**.

7. Configure each of the authentication paths, including **Fail**, **Success**, and the paths that you defined in the **Rules** dialog.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | In case the ID DataWeb API is unreachable or returns an error, we recommend that you allow users to continue to sign on by satisfying stricter authentication requirements.You can do this in your authentication policy by setting the **Fail** outcome of the ID DataWeb IdP Adapter instance to point to a second authentication factor, as shown in the following example.Alternately, you can do this in your ID DataWeb IdP Adapter instance by setting the **Failure mode** as shown in [Configuring an adapter instance](pf_iddataweb_ik_configuring_an_adapter_instance.html). |

   ![id dataweb authn policy](_images/id_dataweb_authn_policy.jpg)

8. Click **Done**.

9. In the **Policies** window, click **Save**.

---

---
title: Changelog
description: The following is the change history for the ID DataWeb Integration Kit.
component: iddataweb
page_id: iddataweb:release_notes:pf_iddataweb_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/release_notes/pf_iddataweb_ik_changelog.html
revdate: February 19, 2026
section_ids:
  version-1-3-january-2026: Version 1.3 - January 2026
  version-1-2-1-september-2025: Version 1.2.1 - September 2025
  version-1-2-november-2023: Version 1.2 - November 2023
  version-1-1-2-june-2022: Version 1.1.2 - June 2022
  version-1-1-1-may-2022: Version 1.1.1 - May 2022
  version-1-1-august-2020: Version 1.1 - August 2020
  version-1-0-january-2020: Version 1.0 - January 2020
---

# Changelog

The following is the change history for the ID DataWeb Integration Kit.

## Version 1.3 - January 2026

* Added the ability to configure a dynamic App ID in API requests. Learn more in the **Application Name Attribute** row of the [ID DataWeb IdP Adapter settings reference](../setup/pf_iddataweb_ik_id_dataweb_idp_adapter_settings_reference.html).

## Version 1.2.1 - September 2025

* Updated the dependencies that the ID DataWeb Integration Kit uses.

## Version 1.2 - November 2023

* Added the ability for API calls to send an App ID based on the [**Application Name**](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_sessioncreationadaptertasklet_inheritabletargetapplicationinfostate.html) from the [**SP Connection**](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html) in PingFederate.

* Added a new configuration setting that enables end-users to mark their device as private to the trust device API.

## Version 1.1.2 - June 2022

* Updated the Authentication API `.JAR` file version.

## Version 1.1.1 - May 2022

* Removed third-party fonts.

* Standardized the archive file structure.

## Version 1.1 - August 2020

* Improved the appearance of the device profiling template.

* Added support for the flat JSON payload structure from ID DataWeb.

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

## Version 1.0 - January 2020

* Initial release.

* Added support for sending user attributes and ThreatMetrix device profiles to the ID DataWeb API.

* Added support for retrieving attributes and risk policy decisions from the ID DataWeb API.

* Added the ability to add device profiling into any browser-based authentication source.

* Added the **Base URL** setting to direct requests to the production or pre-production ID DataWeb API.

* Added the **Failure Mode** and **Fallback Risk Result Value** settings to handle failed risk result requests.

* Added the **API Request Timeout** and **Connection Timeout** settings.

* Added the **Proxy Settings**, **Custom Proxy Host**, and **Custom Proxy Port** settings to override PingFederate default proxy settings.

* Added the **Verify HTTPS Hostname** setting to skip hostname verification.

---

---
title: Configuring an adapter instance
description: Configure the ID DataWeb IdP Adapter to determine how PingFederate communicates with the ID DataWeb API.
component: iddataweb
page_id: iddataweb:setup:pf_iddataweb_ik_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/setup/pf_iddataweb_ik_configuring_an_adapter_instance.html
revdate: June 24, 2024
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Configure the ID DataWeb IdP Adapter to determine how PingFederate communicates with the ID DataWeb API.

## Steps

1. In the PingFederate administrative console, create a new IdP adapter instance:

   1. Go to **Authentication > Integration > IdP Adapters** and click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **ID DataWeb IdP Adapter**. Click **Next**.

3. (Optional) On the **IdP Adapter** tab, in the **Additional Verification Attributes** section, configure additional attributes to send to ID DataWeb with the user data:

   1. Click **Add a new row to 'Additional Verification Attributes'**.

   2. In the **Incoming Attribute Name** field, enter the name of an attribute from any authentication source that appears earlier in your PingFederate authentication policy than the ID DataWeb IdP Adapter.

   3. In the **ID DataWeb User Attribute** list, select the ID DataWeb attribute that you want to populate.

      |   |                                                                                                                                                                                                                                                                                                                                                            |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The ID DataWeb IdP Adapter allows you to pass custom attributes to ID DataWeb. The name and value of the attribute are determined by the **Local Attribute** column.For example, if you enter `officeName` in the **Local Attribute** column, ID DataWeb receives an attribute with the following name and value format: `{…​officeName: headquarters…​}`. |

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a - d.

4. (Optional) On the **IdP Adapter** tab, in the **ID DataWeb Response Mappings (optional)** section, map attributes from the ID DataWeb response to the attribute contract:

   1. Click **Add a new row to 'ID DataWeb Response Mappings (optional)'**.

   2. In the **Local Attribute** field, enter a name of your choosing for an attribute.

   3. In the **ID DataWeb API Attribute Mapping** field, enter the JSON Pointer syntax for the value of the matching ID DataWeb attributes as shown in [JSON Pointer syntax reference](pf_iddataweb_ik_json_pointer_syntax_reference.html).

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a-d.

5. On the **IdP Adapter** tab, configure the adapter instance by referring to [ID DataWeb IdP Adapter settings reference](pf_iddataweb_ik_id_dataweb_idp_adapter_settings_reference.html). Click **Next**.

6. On the **Actions** tab, test your connection to the ID DataWeb API. Resolve any issues that are reported, and then click **Next**.

7. On the **Extended Contract** tab, add any attributes that you included in the **ID DataWeb Response Mappings (optional)** section of the **IdP Adapter** tab.

8. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

9. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

10. On the **Summary** tab, check your configuration and then click **Save**.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the ID DataWeb Integration Kit files to your PingFederate directory.
component: iddataweb
page_id: iddataweb:setup:pf_iddataweb_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/setup/pf_iddataweb_ik_deploying_the_integration_files.html
revdate: June 24, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the ID DataWeb Integration Kit files to your PingFederate directory.

## About this task

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | If you operate PingFederate in a cluster, the following steps refer to the console node. |

## Steps

1. Download the ID DataWeb Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/id-dataweb-integration-kit).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, back up your customizations and delete earlier versions of the integration files:

   1. Back up any ID DataWeb Integration Kit files that you customized in the `<pf_install>/pingfederate/server/default/conf/` directory.

   2. Delete the `pf-id-dataweb-adapter-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. If there is more than one version of the `pf-authn-api-sdk-<version>.jar` file in your `<pf_install>/pingfederate/server/default/lib` directory, delete all but the latest version of the file.

6. If you backed up any customized files, modify the new files with your customizations.

7. Start PingFederate.

8. If you operate PingFederate in a cluster, repeat steps 2 - 8 for each engine node.

---

---
title: Device profiling methods
description: To include ThreatMetrix when producing a policy decision for a sign-on event, ID DataWeb requires information about the device as well as the user. There are different methods for collecting the device profile depending on your preferences and whether users are authenticating directly through PingFederate or through the PingFederate authentication API.
component: iddataweb
page_id: iddataweb::pf_iddataweb_ik_device_profiling_methods
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/pf_iddataweb_ik_device_profiling_methods.html
revdate: June 24, 2024
section_ids:
  direct-authentication-mode-captured-by-the-id-dataweb-idp-adapter: Direct authentication mode - Captured by the ID DataWeb IdP Adapter
  direct-authentication-mode-captured-by-a-previous-adapter: Direct authentication mode - Captured by a previous adapter
  authentication-api-mode-captured-by-the-id-dataweb-idp-adapter: Authentication API mode - Captured by the ID DataWeb IdP Adapter
  authentication-api-mode-captured-by-your-web-application-first-factor-sign-on-page: Authentication API mode - Captured by your web application first-factor sign-on page
---

# Device profiling methods

To include ThreatMetrix when producing a policy decision for a sign-on event, ID DataWeb requires information about the device as well as the user. There are different methods for collecting the device profile depending on your preferences and whether users are authenticating directly through PingFederate or through the PingFederate authentication API.

## Direct authentication mode - Captured by the ID DataWeb IdP Adapter

When the ID DataWeb IdP Adapter is triggered in the sign-on flow, it inserts a page that runs the device profiling script.

This method does not require modifications to any other pages, but adds a wait time to the sign-on process. The length of the wait depends on your environment.

Sequence:

1. The user arrives at the first-factor sign-on page and enters their credentials.

2. The ID DataWeb IdP Adapter is triggered by the PingFederate authentication policy. It presents a spinner animation page that runs the device profiling script. The script sends the device profile to the ID DataWeb API with a unique session ID.

3. The ID DataWeb IdP Adapter requests a policy decision by sending the session ID and any user attributes to the ID DataWeb API.

## Direct authentication mode - Captured by a previous adapter

To reduce perceived wait times for the user, you can run the device profiling script on a page that already requires user interaction.

Sequence:

1. The user arrives at a page presented by a PingFederate adapter, such as the HTML Form Adapter.

2. While the user interacts with the page (for example, entering their username and password), the device profiling script sends the device profile to the ID DataWeb API with a unique session ID. The script also stores the session ID in an HTTP cookie.

3. The ID DataWeb IdP Adapter is triggered by the PingFederate authentication policy. It gets the session ID from the HTTP cookie.

4. The ID DataWeb IdP Adapter requests a policy decision by sending the session ID and any user attributes to the ID DataWeb API.

You can integrate the device profiling script into any page that meets the following criteria:

* The page appears before the ID DataWeb IdP Adapter in your PingFederate authentication policy.

* The page is hosted in the same domain as your PingFederate server. This is required to accommodate the HTTP cookies. You might be able to work around this requirement by consolidating your domains with a reverse proxy server.

## Authentication API mode - Captured by the ID DataWeb IdP Adapter

If you have a web application that uses the PingFederate authentication API, you can add the device profiling script to your existing sign-on page.

Sequence:

1. The user arrives at the sign-on page and enters their credentials.

2. The ID DataWeb IdP Adapter is triggered by the PingFederate authentication policy.

3. The web application gets a device profiling URL from the authentication API. The script creates the device profile and associated it with the session ID in the URL.

4. The web application tells PingFederate to continue the authentication flow.

5. The ID DataWeb IdP Adapter requests a policy decision by sending the session ID and any user attributes to the ID DataWeb API.

This method is recommended if you have a web application and cannot accommodate HTTP cookies.

## Authentication API mode - Captured by your web application first-factor sign-on page

If your web application can accommodate HTTP cookies, you can reduce perceived wait times by running the device profiling script while the user interacts with your sign-on page.

Sequence:

1. The user arrives at a first-factor sign-on page presented by your web application.

2. While the user interacts with the page (for example, entering their username and password), the device profiling script sends the device profile to the ID DataWeb API with a unique session ID. The script also stores the session ID in an HTTP cookie.

3. The ID DataWeb IdP Adapter gets the session ID from the HTTP cookie.

4. The ID DataWeb IdP Adapter sends the session ID and any user attributes to the ID DataWeb API and requests the policy decision.

You can integrate the device profiling script into your web application if it meets the following criteria:

* The user sees your sign-on page before the ID DataWeb IdP Adapter is triggered in your PingFederate authentication policy.

* The page is hosted in the same domain as your PingFederate server. This is required to accommodate the HTTP cookies. You might be able to work around this requirement by consolidating your domains with a reverse proxy server.

---

---
title: Download manifest
description: The following files are included in the ID DataWeb Integration Kit .zip archive:
component: iddataweb
page_id: iddataweb:release_notes:pf_iddataweb_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/release_notes/pf_iddataweb_ik_download_manifest.html
revdate: June 24, 2024
---

# Download manifest

The following files are included in the ID DataWeb Integration Kit `.zip` archive:

* `Legal.pdf`: Copyright and license information

* `dist/pingfederate/server/default`: Contains the integration files

  * `deploy`: Contains the Java libraries

    * `pf-id-dataweb-adapter-<version>.jar`: `.jar` file that contains the ID DataWeb IdP Adapter.

  * `conf`: Contains the HTML template and script that send device data to the ID DataWeb API.

    * `language-packs/id-dataweb-messages.properties`: A variable file that customizes the messages that appear on the template file.

    * `template`: Contains user-facing HTML template files

      * `id-dataweb.adapter.template.html`: A sign-on redirect page used with the "captured by this adapter" device profiling method. Runs scripts to show a spinner animation and create the device profile.

      * `assets`: Contains functional scripts and files used by the template

        * `css/id-dataweb.css`: A CSS file that customizes the appearance of the template file.

        * `images`: Contains template image files

          * `ping-logo.svg`: An image file with company branding

          * `spinner.svg`: An image file used in a spinner animation

        * `scripts`: Contains script files used to collect and send information

          * `id_dataweb_device_profiling.js`: A JavaScript script that retrieves and runs the ThreatMetrix device profiling script and prepares a cookie with the device profile identifier. Used with the "captured by a previous adapter" device profiling method.

  * `lib/pf-authn-api-sdk-<version>.jar`: A `.jar` file that contains the PingFederate Authentication API SDK

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.
component: iddataweb
page_id: iddataweb:troubleshooting:pf_iddataweb_ik_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/troubleshooting/pf_iddataweb_ik_enabling_debug_logging.html
revdate: June 24, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.

## About this task

These steps are optional.

Learn more about logging in [Enabling debug messages and console logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html) in the PingFederate documentation.

## Steps

1. Open the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file for editing.

2. If you want to log activity for PingFederate and all adapters, do the following:

   1. Find the following section:

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   2. Change `INFO` to `DEBUG`.

      ```html
      <AsyncRoot level="DEBUG" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   3. If you want to see the adapter activity in the console, remove the comment tags.

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<AppenderRef ref="CONSOLE" />
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

3. If you want to log activity just for the ID DataWeb IdP Adapter, add the following line.

   ```html
   <Logger name="com.pingidentity.adapters.id-dataweb" level="DEBUG"/>
   ```

4. If you want to log all HTTP requests and responses with ID DataWeb API, add the following line.

   |   |                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can use this information with a third-party log analysis tool to monitor for important events, such as when a sign-on event has a high-risk policy decision. |

   ```html
   <Logger name="org.shaded.id-dataweb" level="INFO"/>
   ```

5. Save the file.

---

---
title: ID DataWeb IdP Adapter settings reference
description: Field descriptions for the ID DataWeb IdP Adapter configuration screen.
component: iddataweb
page_id: iddataweb:setup:pf_iddataweb_ik_id_dataweb_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/setup/pf_iddataweb_ik_id_dataweb_idp_adapter_settings_reference.html
revdate: January 7, 2026
---

# ID DataWeb IdP Adapter settings reference

Field descriptions for the ID DataWeb IdP Adapter configuration screen.

> **Collapse: Standard fields**
>
> | Field                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Client ID**                              | The client ID provided to you by ID DataWeb.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
> | **Client Secret**                          | The client secret provided to you by ID DataWeb.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
> | **ID DataWeb API Base URL**                | The URL of the ID DataWeb API.- Production: `https://api.iddataweb.com/`
>
> - Pre-production: `https://api.preprod.iddataweb.com/`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
> | **Update Device Trust**                    | When enabled, users can receive a boost to their trust score for subsequent sign on attempts with a given device.When a user signs on successfully after being challenged with an "obligation" result from ID DataWeb, PingFederate contacts the ID DataWeb API to mark the device as "trusted." You can configure the amount and duration of the trust score boost in the ID DataWeb admin console. The boost affects the device, not the user account.This checkbox is cleared by default.                                                                                                                                                                                                                                                                                                   |
> | **Update Device Trust Using User Consent** | When the user selects **This is my device** in a previous adapter, such as the HTML Form Adapter, PingFederate contacts the ID DataWeb API after the user signs on to mark the device as "trusted" for subsequent sign on attempts.This setting works in conjunction with the **Update Device Trust** setting. If you do not select **Update Device Trust**, **Update Device Trust Using User Consent** will not mark the device as trusted.This checkbox is cleared by default.                                                                                                                                                                                                                                                                                                               |
> | **Update Device Trust API Key**            | The API key that PingFederate uses to communicate with the ID DataWeb API when marking a device as "trusted". Applies only when **Update Device Trust** is enabled.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
> | **Device Profiling Method**                | Determines how the adapter handles session IDs and device profiling:- Captured by this adapter
>
>   The ID DataWeb IdP Adapter creates a session ID. In authentication API mode, it provides the device profiling URL (including session ID) to the external web application. In direct authentication mode, it runs the device profiling script.
>
> - Captured by a previous adapter
>
>   The ID DataWeb IdP Adapter looks for an existing session ID in an HTTP cookie. Learn more in [Device profiling methods](../pf_iddataweb_ik_device_profiling_methods.html).&#xA;&#xA;If you completed the steps in Adding device profiling to an authentication page, select Captured by a previous adapter. Otherwise, select Captured by this adapter.The default value is **Captured by this adapter**. |

> **Collapse: Advanced fields**
>
> | Field                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
> | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Application Name Attribute**     | You can map the application name to an attribute that's passed to this adapter instance as a chained attribute in the authentication policy. To do so, enter the name of the desired attribute in the **Application Name Attribute** field.&#xA;&#xA;If no attribute is mapped or retrieved, the adapter uses the application name defined in the SP connection instead.                                                                                                                                                                                                                                                                                                                                                                                                                  |
> | **Device Profiling Script URL**    | The URL of the ID DataWeb script that collects the device profile during sign on. Applies only when **Device Profiling Method** is set to **Captured by this adapter**.Applies only with the "Direct authentication mode - Captured by this adapter" device profiling method.The default value is: `https://content.maxconnector.com/fp/tags.js?org_id=716kkpe1&api_key=bvrbl1ev61nw7zq7&pageid=verify&session_id=${sessionId}`                                                                                                                                                                                                                                                                                                                                                           |
> | **Device Profiling Timeout**       | The amount of time, in milliseconds, that PingFederate waits for the device profiling script to collect device details. Applies only when **Device Profiling Method** is set to **Captured by this adapter**.The minimum value is `3000`.The default value is `5000`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
> | **Cookie Name**                    | The name of the cookie that contains the identifier for the ThreatMetrix device profile. Applies only when **Device Profiling Method** is set to **Captured by a previous adapter**.If you customized the name for the cookie in the optional [Adding device profiling to an authentication page](pf_iddataweb_ik_adding_device_profiling_to_an_authentication_page.html) steps, enter the same name in this field.The default value is `idwUUID`.                                                                                                                                                                                                                                                                                                                                        |
> | **Failure Mode**                   | When ID DataWeb is unavailable or an error occurs, this setting determines whether the user's sign-on attempt should fail or continue with a pre-determined policy decision.For cases where the ID DataWeb API is unavailable or returns an error, we recommend that you allow users to continue to sign on by satisfying stricter authentication requirements. You can do this in your adapter configuration by setting the **Failure mode** to return the `obligation` result. Alternately, you can do this in your authentication policy by setting the **Fail** outcome of the ID DataWeb IdP Adapter instance as shown in [Adding ID DataWeb policy decisions to your authentication policy](pf_iddataweb_ik_adding_id_dataweb_policy_decisions_to_your_authentication_policy.html). |
> | **Fallback Policy Decision Value** | The risk result (for example, `obligation`, `deny`, or `unknown`) to use in the authentication policy when ID DataWeb is unavailable or an error occurs, and **Failure Mode** is set to **Continue with fallback risk result**.The default value is `deny`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
> | **Token API Endpoint**             | The ID DataWeb endpoint that issues access tokens.The default value is `/v1/token`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
> | **Verify API Endpoint**            | The ID DataWeb endpoint that performs one-time user verification.The default value is `/v1/flat/slverify`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> | **Trust Device API Endpoint**      | The ID DataWeb endpoint that PingFederate contacts after a user successfully signs on. Applies only when **Update Device Trust** is enabled.The default value is `/v1/trustdevice`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
> | **API Request Timeout**            | The amount of time in milliseconds that PingFederate waits for the ID DataWeb API to respond to requests. A value of `0` disables the timeout.&#xA;&#xA;Some ID DataWeb verification services have longer response times than others. Test your specific configuration and adjust this value based on the range of response times that you receive.The default value is `2000`.                                                                                                                                                                                                                                                                                                                                                                                                           |
> | **Connection Timeout**             | The amount of time in milliseconds that PingFederate allows to establish a connection with the ID DataWeb API. A value of `0` disables the timeout.The default value is `2000`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
> | **Proxy Settings**                 | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
> | **Custom Proxy Host**              | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | **Custom Proxy Port**              | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
> | **Verify HTTPS Hostname**          | When a connection is established with the ID DataWeb API, PingFederate matches the target host name against the names stored inside the server's X.509 certificate. This security measure ensures that PingFederate is connecting to the correct server.This checkbox is selected by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

---

---
title: ID DataWeb Integration Kit
description: The ID DataWeb Integration Kit allows PingFederate to communicate with ID DataWeb for risk-based authentication using ThreatMetrix.
component: iddataweb
page_id: iddataweb::pf_iddataweb_ik
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/pf_iddataweb_ik.html
revdate: September 18, 2025
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# ID DataWeb Integration Kit

The ID DataWeb Integration Kit allows PingFederate to communicate with ID DataWeb for risk-based authentication using ThreatMetrix.

By sending a ThreatMetrix device profile and optional user attributes to ID DataWeb when a user signs on, PingFederate can get a security risk assessment for the sign-on event. Including the risk assessment in your PingFederate authentication policy allows you to adjust the user's authentication requirements dynamically each time they sign on.

## Components

* Template and script files

  * When a user signs on through PingFederate, these files retrieve the JavaScript that collects a profile of the user's device. This allows you to use ThreatMetrix as a verification service in ID DataWeb.

* ID DataWeb IdP Adapter

  * When a user signs on through PingFederate, the adapter sends the device profile and user attributes to the ID DataWeb API, then retrieves a policy decision `approve`, `obligation`, or `deny`) from ID DataWeb.

## Intended audience

This document is intended for PingFederate administrators. Before starting, we recommend that you familiarize yourself with the following:

* The [ID DataWeb documentation](https://docs.iddataweb.com/docs/getting-started)

* [ThreatMetrix Overview](https://docs.iddataweb.com/docs/threatmetrix-1) in the ID DataWeb documentation

* [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html) in the PingFederate documentation

## System requirements

* PingFederate 11.3 or later

* An ID DataWeb service administrator account

---

---
title: Integrating device profiling
description: Depending on your authentication mode and preferences, complete one of the following steps to capture the device profile.
component: iddataweb
page_id: iddataweb:setup:pf_iddataweb_ik_integrating_device_profiling
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/setup/pf_iddataweb_ik_integrating_device_profiling.html
revdate: June 24, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Integrating device profiling

Depending on your authentication mode and preferences, complete one of the following steps to capture the device profile.

## About this task

You can find detailed descriptions of each method in [Device profiling methods](../pf_iddataweb_ik_device_profiling_methods.html).

## Steps

* Do one of the following:

  | Method                                                                                         | Steps                                                                                                                                                                               |
  | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | **Direct authentication mode - Captured by the ID DataWeb IdP Adapter**                        | No extra steps are necessary. Continue to [Configuring an adapter instance](pf_iddataweb_ik_configuring_an_adapter_instance.html).                                                  |
  | **Direct authentication mode - Captured by a previous adapter, such as the HTML Form Adapter** | Modify the adapter template by completing the steps in [Adding device profiling to an authentication page](pf_iddataweb_ik_adding_device_profiling_to_an_authentication_page.html). |
  | **Authentication API mode - Captured by the ID DataWeb IdP Adapter**                           | Modify your web application by completing the steps in [Adding device profiling to a web application](pf_iddataweb_ik_adding_device_profiling_to_a_web_application.html).           |
  | **Authentication API mode - Captured by your web application first-factor sign-on page**       | Modify your web application by completing the steps in [Adding device profiling to an authentication page](pf_iddataweb_ik_adding_device_profiling_to_an_authentication_page.html). |

---

---
title: JSON Pointer syntax reference
description: JavaScript Object Notation (JSON) Pointer defines a syntax for identifying a specific value within a JSON payload. Using the sample payload and JSON Pointer examples below, identify the attributes that you want to use to populate your attribute contract.
component: iddataweb
page_id: iddataweb:setup:pf_iddataweb_ik_json_pointer_syntax_reference
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/setup/pf_iddataweb_ik_json_pointer_syntax_reference.html
revdate: June 24, 2024
section_ids:
  example-json-payload: Example JSON payload
---

# JSON Pointer syntax reference

JavaScript Object Notation (JSON) Pointer defines a syntax for identifying a specific value within a JSON payload. Using the sample payload and JSON Pointer examples below, identify the attributes that you want to use to populate your attribute contract.

You can find a complete technical description of JSON Pointer syntax in [JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901) on ietf.org.

You can find more information about the ID DataWeb attributes and payload structure in the [Attribute list](https://docs.iddataweb.com/docs/attribute-list) and [Attribute dictionary](https://docs.iddataweb.com/reference#test-input) in the ID DataWeb documentation.

## Example JSON payload

```json
{
   "endpoint$transaction$serialVersionUID":"3437946115680492319",
   "endpoint$transaction$errorCode":"",
   "endpoint$transaction$errorDescription":"",
   "endpoint$transaction$mbun":"5d87fd39-af76-9732-3435-7fa1d0bc8148",
   "endpoint$transaction$transaction_id":"0375fc22-3321-4108-b0b9-69660ef19bf4",
   "endpoint$transaction$forwardApiKey":"e16774cfb79941b9",
   "endpoint$transaction$policyObligation":"true",
   "endpoint$transaction$policyDecision":"obligation",
   "userAttributes$APSessionID$apSessionId":"875efc0d-f6e3-4ca7-9c09-4b0c79446359",
   "userAttributes$FullName$fname":"Janet",
   "userAttributes$FullName$lname":"Smith",
   "userAttributes$FullName$mname":"middleName",
   "userAttributes$FullName$suffix":"null",
   "userAttributes$InternationalAddress$country":"US",
   "userAttributes$InternationalAddress$sublocality":"null",
   "userAttributes$InternationalAddress$locality":"Denver",
   "userAttributes$InternationalAddress$subpremise":"null",
   "userAttributes$InternationalAddress$sublocality_level_2":"null",
   "userAttributes$InternationalAddress$route":"Main Street",
   "userAttributes$InternationalAddress$administrative_area_level_2":"null",
   "userAttributes$InternationalAddress$premise":"null",
   "userAttributes$InternationalAddress$sublocality_level_5":"null",
   "userAttributes$InternationalAddress$administrative_area_level_3":"null",
   "userAttributes$InternationalAddress$sublocality_level_4":"null",
   "userAttributes$InternationalAddress$sublocality_level_3":"null",
   "userAttributes$InternationalAddress$administrative_area_level_1":"VA",
   "userAttributes$InternationalAddress$street_number":"18",
   "userAttributes$InternationalAddress$neighborhood":"null",
   "userAttributes$InternationalAddress$postal_code":"23225",
   "userAttributes$CustomAttribute1$name":"customAttribute1Val",
   "userAttributes$CustomAttribute1$value":"myCustomAttribute1Value",
   "acquiredAttributes$EquifaxScore$equifaxScore":"7",
   "acquiredAttributes$SmartIDBrowserstringPersonaAgeMonths$smartIDBrowserStringPersonaAge":"0",
   "acquiredAttributes$NEATPersonaAgeMonths$NEATPersonaAge":"0",
   "acquiredAttributes$DigitalID$digitalID":"0e12aa408fb114c3b0c7d780c3a69c91",
   "acquiredAttributes$DigitalIDConfidence$digitalIDConfidence":"6022",
   "acquiredAttributes$FuzzyDeviceIDConfidence$fuzzyDeviceIDConfidence":"100.00",
   "acquiredAttributes$TrueIP$trueIP":"127.0.0.1",
   "acquiredAttributes$TrueIPGeoCountry$trueIPGeoCountry":"CA",
   "acquiredAttributes$Platform$platform":"browser_computer",
   "acquiredAttributes$FuzzyDeviceID$fuzzyDeviceID":"7d9eeb9464784039bc427e97b3184da2",
   "acquiredAttributes$ExactIDIPPersonaAgeMonths$exactIDIPPersonaAge":"0",
   "acquiredAttributes$TMXScore$tmxScore":"1",
   "acquiredAttributes$RawAssertionScore$rawAssertionScore":"4",
   "acquiredAttributes$AssertionScore$assertionScore":"80",
   "acquiredAttributes$IDWScore$idwScore":"85",
   "userAssertionList$Equifax Identity Fraud Service$link.fullName_address":"pass",
   "userAssertionList$Equifax Identity Fraud Service$link.lastName_address":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$blacklist.ofacIP":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$blacklist.device":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$detect.browserAnomaly":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$test.lte3ProxyToday":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$test.trustedDevice":"fail",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$test.lte3CredentialsDevice7d":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$link.timeZone_TrueGeo":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$test.credentialLTE500mi1hr":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$test.exactIDAgeGTE7d":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$detect.vpn":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$test.trueIPLTE500miInputIP":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$detect.proxyAnonymous":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$blacklist.ip":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$test.expectedLanguage":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$link.proxyOrg_TrueOrg":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$detect.malware":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$detect.aggregator":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$test.smartIDAgeGTE7d":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$detect.proxyOpenTransparent":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$detect.unusualActivity":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$detect.proxyHidden":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$link.proxyISP_TrueISP":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$detect.tor":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$detect.torNode":"pass",
   "userAssertionList$Threatmetrix Session Query Low Location Accuracy$link.proxyGeo_TrueGeo":"pass"
}
```

**Table 1. JSON Pointer syntax**

| Description                   | JSON Pointer                           | Resulting value |
| ----------------------------- | -------------------------------------- | --------------- |
| Result of the risk assessment | `/endpoint$transaction$policyDecision` | `obligation`    |
| The user's first name         | `/userAttributes$FullName$fname`       | `Janet`         |

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the ID DataWeb Integration Kit.
component: iddataweb
page_id: iddataweb:release_notes:pf_iddataweb_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/release_notes/pf_iddataweb_ik_known_issues_and_limitations.html
revdate: June 24, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the ID DataWeb Integration Kit.

## Known issues

There are no known issues.

## Known limitations

There are no known limitations.

---

---
title: Overview of ID DataWeb
description: ID DataWeb evaluates the level of security risk for a user sign-on event based on user attributes and a device profile.
component: iddataweb
page_id: iddataweb::pf_iddataweb_ik_overview_of_id_dataweb
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/pf_iddataweb_ik_overview_of_id_dataweb.html
revdate: June 24, 2024
section_ids:
  device-profile-and-user-attributes: Device profile and user attributes
  verification-services: Verification services
  policy-decisions: Policy decisions
  attributes-in-the-response-from-id-dataweb: Attributes in the response from ID DataWeb
---

# Overview of ID DataWeb

ID DataWeb evaluates the level of security risk for a user sign-on event based on user attributes and a device profile.

## Device profile and user attributes

ID DataWeb uses a device profile to determine a "trust score" for each user sign-on event. The device profile is collected by a ThreatMetrix JavaScript script that runs during the sign-on flow.

You can opt to provide user attributes, such as name, address, and email, to ThreatMetrix or other verification services that are offered by ID DataWeb. You can populate these attributes from other sources in your PingFederate authentication policy. You can find a complete list of attributes that ID DataWeb can collect in [Attribute List](https://docs.iddataweb.com/docs/attribute-list) in the ID DataWeb documentation.

The ID DataWeb IdP Adapter is responsible for sending the device profile and user attributes to ID DataWeb as part of the sign-on flow.

## Verification services

The ID DataWeb service supports a network of more than 70 identity verification services. ID DataWeb combines the results from all of these services into a unified trust score.

As an ID DataWeb administrator, you can choose the verification services that you want to involve in user sign on events as shown in [Managing Verification Services](https://docs.iddataweb.com/docs/managing-verification-services) in the ID DataWeb documentation.

The ID DataWeb Integration Kit is designed to use the ThreatMetrix verification service, which allows you to build risk-based authentication into your PingFederate authentication policy. Learn more in [ThreatMetrix](https://docs.iddataweb.com/docs/threatmetrix-1) in the ID DataWeb documentation.

## Policy decisions

ID DataWeb processes the sign-on event information through the rules and identity verification services that you configure in the ID DataWeb dashboard. It then matches the resulting trust score to one of three policy decisions: `approve`, `obligation`, or `deny`.

The ID DataWeb API provides the policy decision in a response to PingFederate. By including the ID DataWeb policy decision in your PingFederate authentication policy, you decide how each of the `approve`, `obligation`, and `deny` results affects a user's ability to sign on in your environment. For example, you can configure the `obligation` result to require a second authentication factor.

## Attributes in the response from ID DataWeb

The response from ID DataWeb also contains user attributes and sign-on event data from the various ID DataWeb verification services.

In your ID DataWeb IdP Adapter instance configuration, you can capture attributes from the response. This makes them available in other adapters and contracts in the PingFederate authentication policy.

---

---
title: Overview of the SSO flow
description: With the ID DataWeb Integration Kit, PingFederate includes the ID DataWeb API in the sign-on flow.
component: iddataweb
page_id: iddataweb::pf_iddataweb_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/pf_iddataweb_ik_overview_of_the_sso_flow.html
revdate: June 24, 2024
section_ids:
  description: Description
---

# Overview of the SSO flow

With the ID DataWeb Integration Kit, PingFederate includes the ID DataWeb API in the sign-on flow.

The following figure shows how the ID DataWeb API integrates into the sign-on process:

![id dataweb sso flow overview](_images/id_dataweb_sso_flow_overview.png)

## Description

1. A user initiates the sign-on process by requesting access to a protected resource.

2. Depending on the device profiling method, the ID DataWeb IdP Adapter or a previous authentication adapter retrieves the latest JavaScript from ThreatMetrix, which collects the device profile and sends it back to ThreatMetrix. The adapter can also collect user attributes. For the "previous adapter" method, this takes place at the same time as step 1.

3. The ID DataWeb IdP Adapter sends the device profile identifier and any user attributes to the ID DataWeb API and requests the policy decision (`approve`, `obligation`, or `deny`).

4. The ID DataWeb API returns a JSON payload with the policy decision and other attributes to the ID DataWeb IdP Adapter.

5. The ID DataWeb IdP Adapter makes the policy decision and contract attributes available in the PingFederate authentication policy.

6. PingFederate executes the authentication policy, which branches based on the policy decision provided by the ID DataWeb IdP Adapter.

7. PingFederate returns the resource that the user requested.

8. If **Update Device Trust** is enabled in the adapter instance configuration, the ID DataWeb IdP Adapter notifies ID DataWeb that the device is trustworthy. This gives the device a better trust score for subsequent sign on attempts.

   If **Update Device Trust Using User Consent** is enabled in the adapter configuration and the user selects **This is my device** in the HTML form adapter when authenticating, the ID DataWeb IdP Adapter notifies ID DataWeb that the device is trustworthy.

---

---
title: Setup
description: To use the ID DataWeb Integration Kit with PingFederate, configure ID DataWeb, deploy the integration files, and then set up the integration on your PingFederate server.
component: iddataweb
page_id: iddataweb:setup:pf_iddataweb_ik_setup
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/setup/pf_iddataweb_ik_setup.html
revdate: June 24, 2024
section_ids:
  steps: Steps
---

# Setup

To use the ID DataWeb Integration Kit with PingFederate, configure ID DataWeb, deploy the integration files, and then set up the integration on your PingFederate server.

## Steps

1. In the ID DataWeb admin console, add the verification services that you want to use, such as ThreatMetrix.

   You can find instructions in [Managing Verification Services](https://docs.iddataweb.com/docs/managing-verification-services) in the ID DataWeb documentation.

2. In the ID DataWeb admin console, in the **Relying Parties** section, add PingFederate as a relying party.

3. Complete the steps in [Deploying the integration files](pf_iddataweb_ik_deploying_the_integration_files.html).

4. (Optional) Complete the steps in [Adding device profiling to an authentication page](pf_iddataweb_ik_adding_device_profiling_to_an_authentication_page.html).

5. Complete the steps in [Configuring an adapter instance](pf_iddataweb_ik_configuring_an_adapter_instance.html).

6. Complete the steps in [Adding ID DataWeb policy decisions to your authentication policy](pf_iddataweb_ik_adding_id_dataweb_policy_decisions_to_your_authentication_policy.html).

---

---
title: Troubleshooting information
description: The following information addresses technical situations that you might encounter after setting up the ID DataWeb Integration Kit.
component: iddataweb
page_id: iddataweb:troubleshooting:pf_iddataweb_ik_troubleshooting_information
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/troubleshooting/pf_iddataweb_ik_troubleshooting_information.html
revdate: June 24, 2024
---

# Troubleshooting information

The following information addresses technical situations that you might encounter after setting up the ID DataWeb Integration Kit.

| Situation                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Using ID DataWeb with PingFederate 11.3 results in the following error:`Refused to load the script 'https://content.maxconnector.com/fp/tags.js?org_id=716kkpe1&api_key=bvrbl1ev61nw7zq7&pageid=verify&session_id=577fa681-da3d-45e0-b982-6fa0841cc2bd' because it violates the following Content Security Policy directive: "script-src 'self' 'nonce-sJyOa0AjeQgjsZDh'". Note that 'script-src-elem' was not explicitly set, so 'script-src' is used as a fallback.` | Update the HTML form template in `$PF_HOME/server/default/conf/templates`.HTML pages implementing ContentSecurityPolicy restrictions might require updating the `script-src` and `image-src` CSP settings when adding the `id_dataweb_device_profiling` JavaScript file to the page. Update `script-src` and `img-src` to include the `https://content.maxconnector.com` and `*.online-metrix.net` host names.For example, PingFederate 11.3 has updated default templates with strict CSP settings. To use the `id_dataweb_device_profiling` JavaScript file with PingFederate 11.3 default templates, update the following line in the template's CSP settings:```
<meta http-equiv="Content-Security-Policy" content="script-src 'self' 'nonce-$CSPNonce'; style-src 'self'; img-src 'self'; font-src 'self';" />
```Updated line:```
<meta http-equiv="Content-Security-Policy" content="script-src 'self' 'unsafe-inline' https://content.maxconnector.com *.online-metrix.net; style-src 'self'; img-src 'self' https://content.maxconnector.com *.online-metrix.net; font-src 'self';" />
``` |