---
title: Adding review statuses to your authentication policy
description: By modifying your PingFederate authentication policy to include the review status from ThreatMetrix, you can dynamically change authentication requirements based on security risk level.
component: threatmetrix
page_id: threatmetrix:setup:pf_threatmetrix_ik_adding_review_statuses_to_your_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/setup/pf_threatmetrix_ik_adding_review_statuses_to_your_authentication_policy.html
revdate: October 30, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding review statuses to your authentication policy

By modifying your PingFederate authentication policy to include the review status from ThreatMetrix, you can dynamically change authentication requirements based on security risk level.

## About this task

These steps are designed to help you add to an existing authentication policy. You can find general information about configuring authentication policies in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

|   |                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | ThreatMetrix automatically tunes its rules and policies based on user behavior. To accommodate an initial training period, we recommend allowing all transactions to succeed for a period of time, regardless of review status. |

## Steps

1. In the PingFederate admin console, go to **Authentication > Policies > Policies** and select the **IdP Authentication Policies** checkbox.

2. Open an existing authentication policy.

3. In the **Policy** section, select your ThreatMetrix IdP Adapter instance.

   ![Adding the adapter to the authentication policy.](_images/pf-threatmetrix-ik-adding-adapter-to-authn-policy.jpg)

4. Map the user ID into the ThreatMetrix IdP Adapter instance:

   ![A screenshot that shows the Incoming User ID modal with the user identifier selected.](_images/pf-threatmetrix-ik-incoming-user-id.jpg)

   1. Under the ThreatMetrix IdP Adapter instance, click **Options**.

   2. On the **Options** modal, in the **Source** list, select a previous authentication source that collects the user ID.

   3. In the **Attribute** list, select the user ID.

   4. Select the **User ID Authenticated** checkbox.

   5. Click **Done**.

5. Define policy paths based on the information provided by ThreatMetrix:

   ![Branching the authentication policy based on details from ThreatMetrix.](_images/pf-threatmetrix-ik-branching-authn-policy.jpg)

   1. Under the ThreatMetrix IdP Adapter instance, click **Rules**.

   2. On the **Rules** modal, in the **Attribute Name** list, select **reviewStatus**.

   3. In the **Condition** list, do one of the following:

      * For **reviewStatus**, select **equal to**.

      * For **reasonCode**, select **multi-value contains**.

   4. In the **Value** field, do one of the following:

      * For **reviewStatus**, enter `pass`, `review`, `challenge`, or `reject`.

      * For **reasonCode**, enter a ThreatMetrix reason code.

        |   |                                                                                                                                                                                                          |
        | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | Reason codes reflect the policy or policies that ThreatMetrix used to determine the review status. In the ThreatMetrix admin console, set meaningful names for your policies and enter those names here. |

   5. In the **Result** field, enter a name.

      This appears as a new policy path that branches from the ThreatMetrix IdP Adapter.

   6. If you want to add more authentication paths, click **Add** and repeat steps b - e.

   7. (Optional) Clear the **Default to success** checkbox.

   8. Click **Done**.

6. Configure each of the authentication paths.

   |   |                                                                                                                                                                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If ThreatMetrix is unreachable or returns an error, the **Failure mode** advanced setting assigns a default review status. As a result, the **Fail** outcome of the ThreatMetrix IdP Adapter instance isn't used.Learn more in [ThreatMetrix IdP Adapter settings reference](pf_threatmetrix_ik_threatmetrix_idp_adapter_settings_reference.html). |

   ![The complete authentication policy.](_images/pf-threatmetrix-ik-complete-authn-policy.jpg)

7. Click **Done**. On the **Policies** page, click **Save**.

---

---
title: Authentication API Support
description: You can use the PingFederate authentication API to integrate the ThreatMetrix IdP Adapter into your application.
component: threatmetrix
page_id: threatmetrix::pf_threatmetrix_ik_authentication_api_support
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/pf_threatmetrix_ik_authentication_api_support.html
revdate: October 28, 2025
---

# Authentication API Support

You can use the PingFederate authentication API to integrate the ThreatMetrix IdP Adapter into your application.

The PingFederate Authentication API provides access to the current state of the authentication flow as a user steps through the PingFederate authentication policy. Learn more in [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

To integrate the ThreatMetrix IdP Adapter into your authentication flow, configure your application based on the states, actions, and models available in the PingFederate Authentication API Explorer. You can find more information in [Exploring the Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_exploring_authentication_api.html) in the PingFederate documentation.

---

---
title: Changelog
description: The following is the change history for the ThreatMetrix Integration Kit.
component: threatmetrix
page_id: threatmetrix:release_notes:pf_threatmetrix_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/release_notes/pf_threatmetrix_ik_changelog.html
revdate: October 29, 2025
section_ids:
  threatmetrix-integration-kit-1-4-2-may-2026: ThreatMetrix Integration Kit 1.4.2 - May 2026
  threatmetrix-integration-kit-1-4-1-november-2025: ThreatMetrix Integration Kit 1.4.1 - November 2025
  threatmetrix-integration-kit-1-4-september-2021: ThreatMetrix Integration Kit 1.4 - September 2021
  threatmetrix-integration-kit-1-3-june-2021: ThreatMetrix Integration Kit 1.3 - June 2021
  threatmetrix-integration-kit-1-2-may-2021: ThreatMetrix Integration Kit 1.2 - May 2021
  threatmetrix-integration-kit-1-1-october-2020: ThreatMetrix Integration Kit 1.1 - October 2020
  threatmetrix-integration-kit-1-0-july-2020: ThreatMetrix Integration Kit 1.0 - July 2020
---

# Changelog

The following is the change history for the ThreatMetrix Integration Kit.

## ThreatMetrix Integration Kit 1.4.2 - May 2026

* Fixed an issue that caused HTTP calls to time out in some scenarios.

## ThreatMetrix Integration Kit 1.4.1 - November 2025

* Updated Apache Commons Text library version to address a potential security vulnerability.

## ThreatMetrix Integration Kit 1.4 - September 2021

* Added the ability to configure how unknown sessions are handled.

* Added the ability to disable update API calls to ThreatMetrix.

## ThreatMetrix Integration Kit 1.3 - June 2021

* Updated the `tmx_sdk_profiling.js` script to use the latest code from ThreatMetrix.

* Fixed an issue that, after upgrading the adapter, caused an error when using the administrative API to bulk import an earlier version of the adapter.

## ThreatMetrix Integration Kit 1.2 - May 2021

* Added support for the transaction failure callback added in PingFederate 10.2. PingFederate can now signal ThreatMetrix when a transaction fails, which can affect future risk evaluations.

* Added support for ThreatMetrix reason codes. After a transaction, the reason codes provided by ThreatMetrix are now available in the PingFederate authentication policy in the `reasonCode` attribute.

* Added support for authentication using mobile and native apps. Learn more in [Device profiling methods](../pf_threatmetrix_ik_device_profiling_methods.html).

* Updated the **Device Profiling** setting labels for clarity and to accommodate mobile and native apps.

  | 1.1 Device Profiling Settings      | 1.2 Device Profiling Settings            |
  | ---------------------------------- | ---------------------------------------- |
  | **Captured by this adapter**       | **Create new device profile**            |
  | **Captured by a previous adapter** | **Use existing ThreatMetrix session ID** |

* Fixed an issue that caused an error when an attribute in the **Additional User Attributes** table had no value. Attributes with empty values are now ignored.

## ThreatMetrix Integration Kit 1.1 - October 2020

* Changed the adapter to retrieve a JSON-encoded (instead of URL-encoded) response from ThreatMetrix. The adapter can now make the entire response available in a single attribute in the PingFederate authentication policy.

* Combined the API connection and request timeout settings.

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

## ThreatMetrix Integration Kit 1.0 - July 2020

* Initial release.

* Added support for getting risk assessments and additional data from ThreatMetrix.

* Added support for the ThreatMetrix Web and SDK device profiling scripts.

* Added the ability to add device profiling into any browser-based authentication source or web application.

* Added the ability to send user attributes to ThreatMetrix.

* Added the ability to map any ThreatMetrix API response attribute to an attribute in the PingFederate authentication policy.

* Added support for the PingFederate authentication API.

* Added a setting to handle failed risk assessment requests.

* Added settings for API connection and request timeouts.

* Added settings to override the PingFederate system-default proxy settings.

---

---
title: Configuring an adapter instance
description: Configure the ThreatMetrix IdP Adapter to determine how PingFederate communicates with ThreatMetrix.
component: threatmetrix
page_id: threatmetrix:setup:pf_threatmetrix_ik_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/setup/pf_threatmetrix_ik_configuring_an_adapter_instance.html
revdate: October 30, 2025
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Configure the ThreatMetrix IdP Adapter to determine how PingFederate communicates with ThreatMetrix.

## Steps

1. In the PingFederate admin console, go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **ThreatMetrix IdP Adapter**. Click **Next**.

3. (Optional) On the **IdP Adapter** tab, in the **Additional User Attributes** section, configure user attributes to send to ThreatMetrix.

   |   |                                                                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can find a list of user attributes that ThreatMetrix can collect in [Session Query API](https://portal.threatmetrix.com/kb/index.htm#t=implementation%2Fapis%2Fsession_query_api.htm) (requires sign-on) in the ThreatMetrix documentation. |

   1. Click **Add a new row to 'Additional User Attributes'**.

   2. In the **Incoming Attribute Name** field, enter the name of an attribute from any authentication source that appears earlier in your PingFederate authentication policy than the ThreatMetrix IdP Adapter.

   3. In the **ThreatMetrix Attribute** list, select the ThreatMetrix attribute you want to populate.

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a - d.

4. (Optional) On the **IdP Adapter** tab, in the **ThreatMetrix API Response Mappings** section, map attributes and sign-on event data from the ThreatMetrix response to the attribute contract.

   These attributes become available in your PingFederate authentication policy.

   1. Click **Add a new row to 'ThreatMetrix API Response Mappings'**.

   2. In the **Local Attribute** field, enter a name of your choosing for an attribute.

   3. In the **ThreatMetrix API Attribute Mapping** field, enter the JSON Pointer syntax for the value of the matching ThreatMetrix attributes.

      Alternately, leave the field blank to include the entire response as the value.

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a - d.

5. On the **IdP Adapter** tab, configure the adapter instance by referring to [ThreatMetrix IdP Adapter settings reference](pf_threatmetrix_ik_threatmetrix_idp_adapter_settings_reference.html). Click **Next**.

6. On the **Extended Contract** tab, add any attributes that you included in the **ThreatMetrix API Response Mappings** section of the **IdP Adapter** tab. Click **Next**.

7. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

8. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

9. On the **Summary** tab, click **Save**.

---

---
title: Configuring ThreatMetrix
description: To complete the integration, you'll need your ThreatMetrix organization ID, API key, and optional device profiling domain.
component: threatmetrix
page_id: threatmetrix:setup:pf_threatmetrix_ik_configuring_threatmetrix
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/setup/pf_threatmetrix_ik_configuring_threatmetrix.html
revdate: October 30, 2025
section_ids:
  steps: Steps
---

# Configuring ThreatMetrix

To complete the integration, you'll need your ThreatMetrix organization ID, API key, and optional device profiling domain.

You can find more information about these values in the following sections of the ThreatMetrix documentation:

* [Organization ID](https://portal.threatmetrix.com/kb/index.htm#t=implementation%2Fimplementation_overview%2Forgid.htm) (requires sign-on)

* [API Key](https://portal.threatmetrix.com/kb/index.htm#t=implementation%2Fimplementation_overview%2Fapi_key.htm) (requires sign-on)

* [Enhanced Profiling via Hosted SSL](https://portal.threatmetrix.com/kb/index.htm#t=implementation%2Fprofiling%2Fprofiling%20introduction%20and%20integration%2Fenhanced_profiling_via_hosted_ssl.htm) (requires sign-on)

## Steps

1. Sign on to the [ThreatMetrix Portal](https://portal.threatmetrix.com) as an administrator.

2. Get your organization ID:

   1. In the upper-right corner, click your user avatar.

   2. Note the **Org ID**.

   You'll use this value in [Integrating device profiling](pf_threatmetrix_ik_integrating_device_profiling.html) and [Configuring an adapter instance](pf_threatmetrix_ik_configuring_an_adapter_instance.html).

   ![The organization ID shown on the Portal.](_images/pf-threatmetrix-ik-organization-id.jpg)

3. Get your API key:

   1. Go to **Admin > API Keys**.

   2. If you want a new API key, click **Create New API Key**. On the **Create New API Key** modal, click **Save**.

   3. Note the **API Key**.

      You'll use this value in [Configuring an adapter instance](pf_threatmetrix_ik_configuring_an_adapter_instance.html).

4. (Optional) Request a custom device profiling domain to make ThreatMetrix requests appear to come from your domain:

   1. Follow the [Enhanced Profiling via Hosted SSL](https://portal.threatmetrix.com/kb/index.htm#t=implementation%2Fprofiling%2Fprofiling%20introduction%20and%20integration%2Fenhanced_profiling_via_hosted_ssl.htm) (requires sign-on) guide in the ThreatMetrix documentation.

   2. Note your device profiling domain.

      You'll use this value in [Integrating device profiling](pf_threatmetrix_ik_integrating_device_profiling.html) and [Configuring an adapter instance](pf_threatmetrix_ik_configuring_an_adapter_instance.html).

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the ThreatMetrix Integration Kit files to your PingFederate directory.
component: threatmetrix
page_id: threatmetrix:setup:pf_threatmetrix_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/setup/pf_threatmetrix_ik_deploying_the_integration_files.html
revdate: October 30, 2025
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the ThreatMetrix Integration Kit files to your PingFederate directory.

## Steps

1. Download the ThreatMetrix Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

2. Stop PingFederate, if it's running.

3. If you're upgrading an existing deployment, back up your customizations and delete earlier versions of the integration files:

   1. Back up any ThreatMetrix Integration Kit files that you customized in the `<pf_install>/pingfederate/server/default/conf/` directory.

   2. Delete the `pf-threatmetrix-adapter-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. If there's more than one version of the `pf-authn-api-sdk-<version>.jar` file in your `<pf_install>/pingfederate/server/default/lib` directory, delete all but the latest version of the file.

6. If you backed up any customized files, modify the new files with your customizations.

7. Start PingFederate.

8. If you operate PingFederate in a cluster, repeat steps 2 - 8 for each engine node.

---

---
title: Device profiling methods
description: ThreatMetrix requires a device profile to determine a review status. There are several methods for capturing the device profile and sending it to ThreatMetrix.
component: threatmetrix
page_id: threatmetrix::pf_threatmetrix_ik_device_profiling_methods
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/pf_threatmetrix_ik_device_profiling_methods.html
revdate: October 28, 2025
section_ids:
  choosing-a-device-profiling-method: Choosing a device profiling method
  built-in-basic-method: Built-in (basic method)
  web-app-basic-method: Web app (basic method)
  web-app-enhanced-method: Web app (enhanced method)
  mobile-or-native-app-enhanced-method: Mobile or native app (enhanced method)
---

# Device profiling methods

ThreatMetrix requires a device profile to determine a review status. There are several methods for capturing the device profile and sending it to ThreatMetrix.

Device profiling methods determine:

* Where users sign on, such as:

  * A PingFederate adapter template, such as the HTML Form Adapter or ThreatMetrix IdP Adapter

  * A web, mobile, or native app that uses the PingFederate authentication API

* Whether you're able to modify the sign-on page or app to:

  * Run a device profiling script

  * Pass a session ID to the ThreatMetrix IdP Adapter through an HTTP cookie or the PingFederate authentication API

## Choosing a device profiling method

Compare the device profiling methods in the following table and descriptions to decide which is the best fit for your environment.

* *Basic* methods are simpler to set up, but the user must wait during the device profiling process.

* *Enhanced* methods have more complex setup requirements, but device profiling happens in the background before the PingFederate Authentication API triggers the ThreatMetrix IdP Adapter. This eliminates the perceived wait time for users.

* With all device profiling methods, the ThreatMetrix IdP Adapter uses a session ID to pass additional (optional) attributes to ThreatMetrix.

You can find detailed configuration instructions for each method in [Integrating device profiling](setup/pf_threatmetrix_ik_integrating_device_profiling.html).

> **Collapse: Comparison of device profiling methods**
>
> | Method                          | Authentication mode                         | Session ID created by    | Profile captured by      | Profile submitted by     | Device Profiling Setting        | Notes                                                     |
> | ------------------------------- | ------------------------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------------- | --------------------------------------------------------- |
> | Built-in (basic)                | PingFederate template                       | ThreatMetrix IdP Adapter | ThreatMetrix IdP Adapter | ThreatMetrix IdP Adapter | **Create a new device profile** | User waits during device profiling                        |
> | Web app (basic)                 | Authentication API                          | ThreatMetrix IdP Adapter | Web app                  | Web app                  | **Create a new device profile** | User waits during device profilingRequires script setup   |
> | Web app (enhanced)              | PingFederate template or Authentication API | Web app                  | Web app                  | Web app                  | **Use existing session ID**     | Requires script setupPasses session ID in a cookie        |
> | Mobile or native app (enhanced) | Authentication API                          | Mobile or native app     | Mobile or native app     | Mobile or native app     | **Use existing session ID**     | Requires ThreatMetrix SDKPasses session ID in an API call |

## Built-in (basic method)

When the ThreatMetrix IdP Adapter is triggered in the sign-on flow, it inserts a page that runs the device profiling script.

|   |                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This method doesn't require modifications to any other pages, but users must wait while the device profile is captured. The length of the wait depends on your environment. |

> **Collapse: Sequence**
>
> 1. The user arrives at the first-factor sign-on page and enters their credentials.
>
> 2. The ThreatMetrix IdP Adapter is triggered by the PingFederate authentication policy and presents a spinner animation page that runs the device profiling script. The script sends the device profile to ThreatMetrix with a unique session ID.
>
> 3. The ThreatMetrix IdP Adapter requests a review status by sending the session ID and any user attributes to ThreatMetrix.

## Web app (basic method)

If you have a web app that uses the PingFederate authentication API, you can add the device profiling script to your existing sign-on page.

|   |                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * This method requires you to add a device profiling script to your existing page, and users must wait while the device profile is captured. The length of the wait depends on your environment.

* This method is recommended if you have a web app and can't accommodate HTTP cookies. |

> **Collapse: Sequence**
>
> 1. The user arrives at the sign-on page and enters their credentials.
>
> 2. The ThreatMetrix IdP Adapter is triggered by the PingFederate authentication policy.
>
> 3. The web app gets the session ID from the authentication API and runs the device profiling script. The script sends the device profile to ThreatMetrix with the session ID.
>
> 4. The web app tells PingFederate to continue the authentication flow.
>
> 5. The ThreatMetrix IdP Adapter requests a review status by sending the session ID and any user attributes to ThreatMetrix.

## Web app (enhanced method)

To reduce perceived wait times for the user, you can run the device profiling script while the user interacts with a web page that's already part of the sign-on flow.

> **Collapse: Requirements**
>
> You can integrate the device profiling script into any web page that meets the following criteria:
>
> * The user sees your sign-on page before the ThreatMetrix IdP Adapter is triggered in your PingFederate authentication policy.
>
> * The page is hosted in the same domain as your PingFederate server.
>
>   This is required to accommodate the HTTP cookies that pass the ThreatMetrix session ID to the ThreatMetrix IdP Adapter. You might be able to work around this requirement by consolidating your domains with a reverse proxy server.
>
> For example, you can use this method with:
>
> * The HTML Form Adapter, or another PingFederate adapter that presents a web page.
>
> * A web app that uses the PingFederate authentication API.

> **Collapse: Sequence**
>
> 1. The user arrives at a first-factor sign-on page presented by the HTML Form Adapter or your web app.
>
> 2. While the user interacts with the page (for example, entering their username and password), the device profiling script sends the device profile to ThreatMetrix with a unique session ID. The script also stores the session ID in an HTTP cookie.
>
> 3. The ThreatMetrix IdP Adapter gets the session ID from the HTTP cookie.
>
> 4. The ThreatMetrix IdP Adapter sends the session ID and any user attributes to ThreatMetrix and requests the review status.

## Mobile or native app (enhanced method)

If your users authenticate through a mobile or native app, you can use the ThreatMetrix SDK to capture the device profile. Your app can then provide the ThreatMetrix session ID to PingFederate to continue the authentication flow.

ThreatMetrix provides SDKs for Android, iOS, OSX, Windows, and Java. Learn more in [Introduction to ThreatMetrix SDK and FAQ](https://portal.threatmetrix.com/kb/index.htm#t=threatmetrix%20sdk%2Fintroduction_to_threatmetrix_sdk_and_faq.htm\&rhsearch=ThreatMetrix%20SDK) (requires sign-on) in the ThreatMetrix documentation.

> **Collapse: Sequence**
>
> 1. The user starts the authentication process in your mobile or native app.
>
> 2. While the user interacts with the app (for example, entering their username and password), the ThreatMetrix SDK captures the device profile and sends it to ThreatMetrix. The app then sends the ThreatMetrix session ID to PingFederate.
>
> 3. The ThreatMetrix IdP Adapter sends the session ID and any user attributes to ThreatMetrix and requests the review status.

---

---
title: Download manifest
description: The following files are included in the ThreatMetrix Integration Kit .zip archive.
component: threatmetrix
page_id: threatmetrix:release_notes:pf_threatmetrix_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/release_notes/pf_threatmetrix_ik_download_manifest.html
revdate: October 29, 2025
---

# Download manifest

The following files are included in the ThreatMetrix Integration Kit `.zip` archive.

* `Legal.pdf`: Copyright and license information.

* `dist/pingfederate/server/default`: Contains the integration files.

  * `deploy`: Contains the Java libraries.

    * `pf-threatmetrix-adapter-<version>.jar`: A JAR file that contains the ThreatMetrix IdP Adapter.

  * `conf`: Contains the HTML template that presents the ThreatMetrix sign-on form.

    * `language-packs/threatmetrix-messages.properties`: A variable file that customizes the messages that appear on the template file.

    * `template`: Contains user-facing HTML template file.s

      * `threatmetrix.adapter.template.html`: A sign-on redirect page used with the **Captured by This Adapter** device profiling method. Runs scripts to show a spinner animation and create the device profile.

      * `assets`: Contains functional scripts and files used by the template.

        * `css`: Contains CSS files for the templates.

          * `threatmetrix.css`: A CSS file that customizes the appearance of the template files.

          * `end-user/<version>/end-user.css`: A CSS file that customizes the appearance of the template files.

        * `fonts/end-user/icons`: Contains template icons.

        * `images`: Contains template image files.

          * `ping-logo.svg`: An image file with company branding.

          * `spinner.svg`: An image file used in a spinner animation.

        * `scripts`: Contains script files used to collect and send information.

          * `tmx_sdk_profiling.js`: A JavaScript script that can be embedded in any authentication page. Initiates the ThreatMetrix SDK device profiling script and stores the device profile in a cookie. Used with the **Captured by This Adapter** device profiling method.

          * `tmx_web_profiling.js`: A JavaScript script that can be embedded in any authentication page. Initiates the ThreatMetrix Web device profiling script and stores the device profile in a cookie. Used with the **Captured by This Adapter** device profiling method.

  * `lib/pf-authn-api-sdk-<version>.jar`: A JAR file that contains the PingFederate Authentication API SDK.

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for PingFederate, the ThreatMetrix IdP Adapter, or both.
component: threatmetrix
page_id: threatmetrix:troubleshooting:pf_threatmetrix_ik_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/troubleshooting/pf_threatmetrix_ik_enabling_debug_logging.html
revdate: October 28, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for PingFederate, the ThreatMetrix IdP Adapter, or both.

## About this task

This task is optional. You can use logging for troubleshooting or analytics.

You can find general information about logging in [Enabling debug messages and console logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html) in the PingFederate documentation.

## Steps

1. Open the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file for editing.

2. To log activity for PingFederate and all adapters:

   1. Find the following section in the file:

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   2. Change `INFO` to `DEBUG`:

      The following code snippet shows `DEBUG` in bold for visibility.

      ```html
      <AsyncRoot level="DEBUG" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   3. (Optional) To see the adapter activity in the console as well as the log file, remove the comment tags (`<!--` and `-→`) that surround the `CONSOLE` line.

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<AppenderRef ref="CONSOLE" />
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

3. To log activity relating to the ThreatMetrix IdP Adapter, do one of the following.

   ### Choose from:

   * To log activity for the ThreatMetrix IdP Adapter as well as its HTTPS and component activity, add the following line:

     ```html
     <Logger name="com.pingidentity.adapters.threatmetrix" level="DEBUG"/>
     ```

   * To log activity for the adapter's HTTPS activity and other components but not the adapter itself, add the following line:

     ```
     <Logger name="{logging-class}.shade" level="DEBUG"/>
     ```

   * To log activity for the ThreatMetrix IdP Adapter but not its HTTPS or component activity, add the following lines:

     ```html
     <Logger name="com.pingidentity.adapters.threatmetrix" level="DEBUG"/>
     <Logger name="com.pingidentity.adapters.threatmetrix.shade" level="INFO"/>
     ```

   |   |                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can use this information with a third-party log analysis tool to monitor for important events, such as when a sign-on event has a high-risk review status. |

4. Save the file.

---

---
title: Integrating device profiling
description: Depending on your authentication mode and preferences, complete one of the following steps to capture the device profile. You can find a description of each method in Device profiling methods.
component: threatmetrix
page_id: threatmetrix:setup:pf_threatmetrix_ik_integrating_device_profiling
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/setup/pf_threatmetrix_ik_integrating_device_profiling.html
revdate: October 30, 2025
section_ids:
  steps: Steps
---

# Integrating device profiling

Depending on your authentication mode and preferences, complete one of the following steps to capture the device profile. You can find a description of each method in [Device profiling methods](../pf_threatmetrix_ik_device_profiling_methods.html).

## Steps

1. Do one of the following:

   | Method                          | Steps                                                                                                                                                                       |
   | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Built-in (basic)                | No extra steps are necessary. Continue to [Configuring an adapter instance](pf_threatmetrix_ik_configuring_an_adapter_instance.html).                                       |
   | Web app (basic)                 | Complete the steps in [Integrating device profiling - Web app (basic)](pf_threatmetrix_ik_integrating_device_profiling_web_app_basic.html).                                 |
   | Web app (enhanced)              | Complete the steps in [Integrating device profiling - Web app (enhanced)](pf_threatmetrix_ik_integrating_device_profiling_web_app_enhanced.html).                           |
   | Mobile or native app (enhanced) | Complete the steps in [Integrating device profiling - Mobile or native app (enhanced)](pf_threatmetrix_ik_integrating_device_profiling_mobile_or_native_app_enhanced.html). |

---

---
title: Integrating device profiling - Mobile or native app (enhanced)
description: Instead of using the ThreatMetrix IdP Adapter to collect the device profile, you can capture the device profile using your mobile or native app.
component: threatmetrix
page_id: threatmetrix:setup:pf_threatmetrix_ik_integrating_device_profiling_mobile_or_native_app_enhanced
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/setup/pf_threatmetrix_ik_integrating_device_profiling_mobile_or_native_app_enhanced.html
revdate: October 30, 2025
section_ids:
  steps: Steps
  example: Example:
---

# Integrating device profiling - Mobile or native app (enhanced)

Instead of using the ThreatMetrix IdP Adapter to collect the device profile, you can capture the device profile using your mobile or native app.

## Steps

1. Integrate the ThreatMetrix SDK device profiling functionality into your mobile app.

   ThreatMetrix provides SDKs for Android, iOS, OSX, Windows, and Java. You can find details in [Introduction to ThreatMetrix SDK and FAQ](https://portal.threatmetrix.com/kb/index.htm#t=threatmetrix%20sdk%2Fintroduction_to_threatmetrix_sdk_and_faq.htm\&rhsearch=ThreatMetrix%20SDK) (requires sign-on) in the ThreatMetrix documentation.

2. Configure your mobile app to communicate with PingFederate via the authentication API.

   Learn more in [Authentication API Support](../pf_threatmetrix_ik_authentication_api_support.html).

3. Configure your mobile app to provide the ThreatMetrix session ID when the authentication API reaches the `DEVICE_PROFILE_SESSION_ID_REQUIRED` state.

   ### Example:

   ```
   submitDeviceProfileSessionId{
       "sessionId":"8de77938-65bf-4578-9d1d-cd14a2f87042"
   }
   ```

4. When you complete the steps in [Configuring an adapter instance](pf_threatmetrix_ik_configuring_an_adapter_instance.html), set **Device Profiling** to **Use existing ThreatMetrix session ID**.

---

---
title: Integrating device profiling - Web app (basic)
description: If you have a web application that uses the PingFederate authentication API and can't accommodate HTTP cookies, modify your web application to run the device profiling script.
component: threatmetrix
page_id: threatmetrix:setup:pf_threatmetrix_ik_integrating_device_profiling_web_app_basic
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/setup/pf_threatmetrix_ik_integrating_device_profiling_web_app_basic.html
revdate: October 30, 2025
section_ids:
  steps: Steps
---

# Integrating device profiling - Web app (basic)

If you have a web application that uses the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) and can't accommodate HTTP cookies, modify your web application to run the device profiling script.

There are two device profiling scripts to choose from, the *SDK* and *Web* scripts. You can find a description of the differences in [Introduction to Profiling](https://portal.threatmetrix.com/kb/index.htm#t=implementation%2Fprofiling%2Fprofiling_introduction.htm\&rhsearch=session%20query%20api\&ux=search) (requires sign-on) in the ThreatMetrix documentation.

## Steps

1. If you want to use the ThreatMetrix SDK script, do the following:

   > **Collapse: Details**
   >
   > 1. Copy the `tmx_sdk_profiling.js` file from the integration `.zip` archive to a location that your web application page can access.
   >
   > 2. Add the following code to the sign-on page.
   >
   >    ```
   >    <script type="text/javascript" src="tmx_sdk_profiling.js"></script>
   >    <script type="text/javascript">pinghelper.run_sid_provided("https://h-api.online-metrix.net", "<orgId>", "<sessionId>");</script>
   >    ```
   >
   >    * Substitute your organization ID and adjust the path to the script file:
   >
   >    * If you requested a custom device profiling domain in [Configuring ThreatMetrix](pf_threatmetrix_ik_configuring_threatmetrix.html), substitute it here.
   >
   >    * For each sign-on event, insert the session ID provided by PingFederate.

2. If you want to use the ThreatMetrix Web script, add the following code to the sign-on page:

   > **Collapse: Details**
   >
   > ```
   > <script type="text/javascript"
   > src="https://h-api.online-metrix.net/fp/tags.js?org_id=<orgId>&session_id=<sessionId>"></script>
   > ```
   >
   > * Substitute your organization ID.
   >
   > * If you requested a custom device profiling domain in [Configuring ThreatMetrix](pf_threatmetrix_ik_configuring_threatmetrix.html), substitute it here.
   >
   > * For each sign-on event, insert the session ID from PingFederate.

3. Configure your application to complete the following actions in sequence:

   1. Get the session ID from PingFederate.

      This is an attribute of the `DEVICE_PROFILE_REQUIRED` state.

   2. Run the device profiling script with the session ID.

   3. POST `continueAuthentication` to the authentication API.

4. When you complete the steps in [Configuring an adapter instance](pf_threatmetrix_ik_configuring_an_adapter_instance.html), set **Device Profiling** to **Create new device profile**.

---

---
title: Integrating device profiling - Web app (enhanced)
description: Instead of using the ThreatMetrix IdP Adapter to collect the device profile, you can capture the device profile using an existing sign-on page. This can reduce perceived wait times for the user.
component: threatmetrix
page_id: threatmetrix:setup:pf_threatmetrix_ik_integrating_device_profiling_web_app_enhanced
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/setup/pf_threatmetrix_ik_integrating_device_profiling_web_app_enhanced.html
revdate: October 30, 2025
section_ids:
  steps: Steps
---

# Integrating device profiling - Web app (enhanced)

Instead of using the ThreatMetrix IdP Adapter to collect the device profile, you can capture the device profile using an existing sign-on page. This can reduce perceived wait times for the user.

You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your external web app. The page must meet the criteria listed in [Device profiling methods](../pf_threatmetrix_ik_device_profiling_methods.html).

There are two device profiling scripts to choose from, the SDK and Web scripts. You can find a description of the differences in [Introduction to Profiling](https://portal.threatmetrix.com/kb/index.htm#t=implementation%2Fprofiling%2Fprofiling_introduction.htm\&rhsearch=session%20query%20api\&ux=search) (requires sign-on) in the ThreatMetrix documentation.

## Steps

1. If you want to use the ThreatMetrix SDK script, do the following:

   > **Collapse: Details**
   >
   > 1. If you're modifying an external web application, copy the `tmx_sdk_profiling.js` file from the integration `.zip` archive to a location that your page can access.
   >
   > 2. Add the following code to the sign-on page:
   >
   >    ```
   >    <script type="text/javascript" src="tmx_sdk_profiling.js"></script>
   >    <script type="text/javascript">pinghelper.run("https://h-api.online-metrix.net", "<orgId>");</script>
   >    ```
   >
   >    Substitute your organization ID and adjust the path to the script file.
   >
   >    |   |                                                                                                           |
   >    | - | --------------------------------------------------------------------------------------------------------- |
   >    |   | If you're modifying a PingFederate template, the script path is `../assets/scripts/tmx_sdk_profiling.js`. |
   >
   >    If you requested a custom device profiling domain in [Configuring ThreatMetrix](pf_threatmetrix_ik_configuring_threatmetrix.html), substitute it here.

2. If you want to use the ThreatMetrix Web script, do the following:

   > **Collapse: Details**
   >
   > 1. If you're modifying an external web application, copy the `tmx_web_profiling.js` file from the integration `.zip` archive to a location that your page can access.
   >
   > 2. In the `tmx_web_profiling.js` file, substitute your organization ID:
   >
   >    ```
   >    var deviceProfilingDomain = "h.online-metrix.net";
   >    var orgId = "orgId";
   >    ```
   >
   >    If you requested a custom device profiling domain in [Configuring ThreatMetrix](pf_threatmetrix_ik_configuring_threatmetrix.html), substitute it here.
   >
   > 3. Add the following to the sign-on page and adjust the path to the script file:
   >
   >    ```
   >    <script type="text/javascript" src="tmx_web_profiling.js"></script>
   >    ```
   >
   >    |   |                                                                                                               |
   >    | - | ------------------------------------------------------------------------------------------------------------- |
   >    |   | If you're modifying a PingFederate template, use `../assets/scripts/tmx_web_profiling.js` as the script path. |

3. (Optional) In the script file, customize the name prefix for the device profile cookie to suit your environment.

   ```
   var cookieNamePrefix = "tmxSessionID";
   ```

4. When you complete the steps in [Configuring an adapter instance](pf_threatmetrix_ik_configuring_an_adapter_instance.html), do the following:

   1. Set **Device Profiling** to **Use existing ThreatMetrix session ID**.

   2. Update the **Cookie Name Prefix** field if you customized it previously.

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the ThreatMetrix Integration Kit.
component: threatmetrix
page_id: threatmetrix:release_notes:pf_threatmetrix_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/release_notes/pf_threatmetrix_ik_known_issues_and_limitations.html
revdate: October 29, 2025
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the ThreatMetrix Integration Kit.

## Known issues

There are no known issues.

## Known limitations

* When a user completes authentication after receiving a review status of `review`, the ThreatMetrix IdP Adapter reports a success to the ThreatMetrix Update API. However, when the user fails to authenticate, the ThreatMetrix IdP Adapter isn't able to send a failure report.

---

---
title: Overview of the SSO flow
description: With the ThreatMetrix Integration Kit, PingFederate includes ThreatMetrix in the sign-on flow.
component: threatmetrix
page_id: threatmetrix::pf_threatmetrix_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/pf_threatmetrix_ik_overview_of_the_sso_flow.html
revdate: October 28, 2025
section_ids:
  description: Description
---

# Overview of the SSO flow

With the ThreatMetrix Integration Kit, PingFederate includes ThreatMetrix in the sign-on flow.

The following figure shows how ThreatMetrix is integrated into the sign-on process:

![A sign-on flow diagram including the ThreatMetrix IdP Adapter.](_images/threatmetrix-ik-sso-flow-overview-diagram.jpg)

## Description

1. A user initiates the sign-on process by requesting access to a protected resource.

2. Depending on the device profiling method, the ThreatMetrix IdP Adapter or a previous authentication adapter collects the device profile and sends it back to ThreatMetrix with a session ID.

   |   |                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------- |
   |   | If using the **Captured by a Previous Adapter** device profiling method, this step takes place at the same time as step 1. |

3. The ThreatMetrix IdP Adapter sends the session ID and any optional user attributes to ThreatMetrix.

4. ThreatMetrix responds with the review status (`pass`, `review`, `challenge`, or `reject`) as well as additional attributes and sign-on event data.

5. The ThreatMetrix IdP Adapter makes the review status, attributes, and sign-on event data available in the PingFederate authentication policy.

6. PingFederate continues executing the authentication policy, which branches based on the review status provided by the adapter.

7. If the user authenticates successfully, PingFederate returns the resource that the user requested.

8. (Optional) If the review status was `review` and authentication ultimately succeeded, the adapter notifies ThreatMetrix.

   This allows ThreatMetrix to train models and tune policies for future sign-on attempts.

---

---
title: Overview of ThreatMetrix
description: ThreatMetrix evaluates the level of security risk for a user sign-on event based on a device profile and user attributes.
component: threatmetrix
page_id: threatmetrix::pf_threatmetrix_ik_overview_of_threatmetrix
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/pf_threatmetrix_ik_overview_of_threatmetrix.html
revdate: October 28, 2025
section_ids:
  device-profile: Device profile
  session-id: Session ID
  user-attributes: User attributes
  review-statuses: Review statuses
  attributes-and-sign-on-event-data: Attributes and sign-on event data
---

# Overview of ThreatMetrix

ThreatMetrix evaluates the level of security risk for a user sign-on event based on a device profile and user attributes.

## Device profile

The device profile is collected by a JavaScript script that runs during the sign-on flow. There are various ways to collect the device profile, as described in [Device profiling methods](pf_threatmetrix_ik_device_profiling_methods.html).

ThreatMetrix also provides two script options. The ThreatMetrix SDK script runs locally, and the ThreatMetrix Web script fetches the latest device profiling script from ThreatMetrix each time. You can find more information in [Introduction to Profiling](https://portal.threatmetrix.com/kb/index.htm#t=implementation%2Fprofiling%2Fprofiling_introduction.htm\&rhsearch=session%20query%20api\&ux=search) (requires sign-on) in the ThreatMetrix documentation.

## Session ID

ThreatMetrix assigns a session ID to every authentication session. This session ID is associated with the device profile, and can be used to send in additional (optional) user attributes from the ThreatMetrix IdP Adapter. The session ID also allows the adapter to get the resulting review status and reason code from the risk assessment.

In some device profiling methods, the session ID is passed to or from the ThreatMetrix IdP Adapter to coordinate sending information to ThreatMetrix from multiple sources for the same authentication session.

## User attributes

When sending the device profile to ThreatMetrix, you can also provide user attributes such as `name`, `address`, and `email`. Use these in your ThreatMetrix policies to affect risk assessments.

|   |                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can find a list of attributes that ThreatMetrix can collect in [Session Query API](https://portal.threatmetrix.com/kb/index.htm#t=implementation%2Fapis%2Fsession_query_api.htm) (requires sign-on) in the ThreatMetrix documentation. |

## Review statuses

ThreatMetrix evaluates risk for a sign-on event by using configurable policies. The result is a *review status* value of `pass`, `review`, `challenge`, or `reject`.

You can configure your PingFederate authentication policy to determine how each of the `pass`, `review`, `challenge`, and `reject` results affects a user's ability to sign on. For example, you can prompt a user for a second authentication factor if their review status is `review`.

## Attributes and sign-on event data

The response from ThreatMetrix also contains attributes and sign-on event data.

In your ThreatMetrix IdP Adapter instance configuration, you can capture this information and make it available to other adapters and contracts in the PingFederate authentication policy.

---

---
title: ThreatMetrix IdP Adapter settings reference
description: The following are setting descriptions for the ThreatMetrix IdP Adapter.
component: threatmetrix
page_id: threatmetrix:setup:pf_threatmetrix_ik_threatmetrix_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/setup/pf_threatmetrix_ik_threatmetrix_idp_adapter_settings_reference.html
revdate: October 30, 2025
---

# ThreatMetrix IdP Adapter settings reference

The following are setting descriptions for the ThreatMetrix IdP Adapter.

> **Collapse: Standard fields**
>
> | Field                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
> | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Org ID**                                                                                                  | The org ID that you noted in [Configuring ThreatMetrix](pf_threatmetrix_ik_configuring_threatmetrix.html).This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
> | **API Key**                                                                                                 | The API key that you noted in [Configuring ThreatMetrix](pf_threatmetrix_ik_configuring_threatmetrix.html).This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | **Policy Name**                                                                                             | The name of the policy to use when requesting a review status.The default value is `default`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
> | **ThreatMetrix Base URL**                                                                                   | The ThreatMetrix API URL.&#xA;&#xA;If ThreatMetrix changes this URL, enter the new URL.The default value is `https://h-api.online-metrix.net`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> | **Device Profiling**                                                                                        | Determines whether the adapter creates a new ThreatMetrix session ID or receives one from another source.Your selection depends on which [device profiling method](../pf_threatmetrix_ik_device_profiling_methods.html) you set up.- **Create new device profile**
>
>   Select this option if you used one of the basic device profiling methods.
>
>   * The ThreatMetrix IdP Adapter creates a new ThreatMetrix session ID.
>
>   * In authentication API mode, the adapter provides a session ID to your web app.
>
>   * Otherwise, the adapter shows the built-in device profiling page that runs the device profiling script.
>
> - **Use existing ThreatMetrix session ID**
>
>   Select this option if you used one of the enhanced device profiling methods.
>
>   * In authentication API mode, the adapter looks for a session ID provided in response to the `SESSION_ID_REQUIRED`.
>
>   * Otherwise, the adapter looks for a session ID provided in an HTTP cookie.The default value is **Create new device profile**. |
> | **Device Profiling Script Source**&#xA;&#xA;Applies only with the Built-in (basic) device profiling method. | Determines the script used to create the device profile.The ThreatMetrix SDK script runs locally, and the ThreatMetrix Web script fetches the latest device profiling script from ThreatMetrix each time. Learn more in [Introduction to Profiling](https://portal.threatmetrix.com/kb/index.htm#t=implementation%2Fprofiling%2Fprofiling_introduction.htm) (requires sign-on) in the ThreatMetrix documentation.The default value is **ThreatMetrix Web**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

> **Collapse: Advanced fields**
>
> | Field                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> | **Device Profiling Domain**&#xA;&#xA;Applies when Device Profiling is set to Create new device profile.     | The domain used for device profiling.If you requested a custom device profiling domain in [Configuring ThreatMetrix](pf_threatmetrix_ik_configuring_threatmetrix.html), enter it here.The default value is `h.online-metrix.net`.                                                                                                                                                                                              |
> | **Device Profiling Timeout**&#xA;&#xA;Applies when Device Profiling is set to Create new device profile.    | The amount of time in milliseconds that PingFederate waits for the device profiling script to collect device details.The minimum value is `3000`. The default value is `5000`.                                                                                                                                                                                                                                                 |
> | **Cookie Name**&#xA;&#xA;Applies only when Device Profiling is set to Use existing ThreatMetrix session ID. | The name of the cookie that contains the device profile.If you customized the name for the cookie in the optional [Integrating device profiling - Web app (enhanced)](pf_threatmetrix_ik_integrating_device_profiling_web_app_enhanced.html) steps, enter the same name in this field.The default value is `tmxSessionID`.                                                                                                     |
> | **Service Type**                                                                                            | Determines the attributes and sign-on event data that ThreatMetrix provides in the response. Learn more in the `service_type` parameter in [Session Query Parameters](https://portal.threatmetrix.com/kb/index.htm#t=implementation%2Fapis%2Fsession_query_api.htm\&rhsearch=session%20query\&rhhlterm=session%20query\&ux=search) (requires sign-on) in the ThreatMetrix documentation.The default value is `session-policy`. |
> | **Failure Mode**                                                                                            | When ThreatMetrix is unavailable or an error occurs, this setting determines the default review status.To allow users to continue to sign on by satisfying stricter authentication requirements, select **review**.&#xA;&#xA;Setting this field to pass isn't recommended outside a test environment.                                                                                                                          |
> | **Unknown Session Mode**                                                                                    | When ThreatMetrix returns an unknown session, this setting determines the review status used.&#xA;&#xA;Setting this field to pass isn't recommended outside a test environment.                                                                                                                                                                                                                                                |
> | **Session Query API Endpoint**                                                                              | The ThreatMetrix Session Query API endpoint.&#xA;&#xA;If ThreatMetrix changes this endpoint, enter the new endpoint.The default value is `/api/session-query`.                                                                                                                                                                                                                                                                 |
> | **Update API Endpoint**                                                                                     | The ThreatMetrix Update API endpoint.&#xA;&#xA;If ThreatMetrix changes this endpoint, enter the new endpoint.The default value is `/api/update`.                                                                                                                                                                                                                                                                               |
> | **Update API Enabled**                                                                                      | After a user with a `review` status moves through the PingFederate authentication policy, the adapter informs ThreatMetrix whether authentication succeeded. This helps improve future risk assessments.If your authentication policy doesn't require users with a `review` status to pass any other authentication challenges, clear this checkbox to skip the update step.This checkbox is selected by default.              |
> | **API Request Timeout**                                                                                     | The amount of time in milliseconds that PingFederate allows when establishing a connection with ThreatMetrix or waiting for a response to a request. A value of `0` disables the timeout.The default value is `2000`.                                                                                                                                                                                                          |
> | **Proxy Settings**                                                                                          | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                                                                                                                                                                                                                    |
> | **Custom Proxy Host**                                                                                       | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                 |
> | **Custom Proxy Port**                                                                                       | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                      |

---

---
title: ThreatMetrix Integration Kit
description: The ThreatMetrix Integration Kit allows PingFederate to communicate with ThreatMetrix for risk-based authentication.
component: threatmetrix
page_id: threatmetrix::pf_threatmetrix_ik
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/pf_threatmetrix_ik.html
revdate: October 28, 2025
section_ids:
  features: Features
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# ThreatMetrix Integration Kit

The ThreatMetrix Integration Kit allows PingFederate to communicate with ThreatMetrix for risk-based authentication.

By sending a device profile (and, optionally, user attributes) to ThreatMetrix when a user signs on, PingFederate can get a security risk assessment for the sign-on event. You can use this assessment to adjust authentication requirements dynamically each time a user signs on. For example, by configuring policies in PingFederate and ThreatMetrix, you could require multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* when a user signs on with a new device.

## Features

* Supports ThreatMetrix's *Web* and *SDK* device profiling scripts. You can find more information in [Introduction to Profiling](https://portal.threatmetrix.com/kb/index.htm#t=implementation%2Fprofiling%2Fprofiling_introduction.htm) (requires sign-on) in the ThreatMetrix documentation.

* Supports device profiling in any browser-based authentication source or web application. Learn more in [Device profiling methods](pf_threatmetrix_ik_device_profiling_methods.html).

* Supports the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Supports the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

## Components

* Template and script files

  * When a user signs on through PingFederate, these files create the device profile and send it to ThreatMetrix. There are several files to accommodate a variety of device profiling methods.

* ThreatMetrix IdP Adapter

  * When a user signs on through PingFederate, the adapter sends the user attributes to ThreatMetrix.

  * The adapter receives the result of the risk assessment as well as other attributes and sign-on event data. The adapter makes this information available in the PingFederate authentication policy.

## Intended audience

This document is intended for PingFederate administrators. If you need help during the setup process, see the following resources:

* The following sections of the PingFederate documentation:

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

* The following sections of the ThreatMetrix documentation:

  * [Introduction to ThreatMetrix Platform](https://portal.threatmetrix.com/kb/index.htm#t=introduction_to_threatmetrix%2Fintroduction_threatmetrix_platform.htm) (requires sign-on)

  * [Architecture Overview](https://portal.threatmetrix.com/kb/index.htm#t=implementation%2Fimplementation_overview%2Farchitecture_overview.htm) (requires sign-on)

  * [Implementation Resources](https://portal.threatmetrix.com/kb/index.htm#t=implementation%2Fimplementation_overview%2Fimplementation_resources.htm) (requires sign-on)

  * [Implementation Steps](https://portal.threatmetrix.com/kb/index.htm#t=implementation%2Fimplementation_overview%2Fimplementation_steps.htm) (requires sign-on)

## System requirements

* PingFederate 11.3 or later

* A ThreatMetrix account