---
title: Adding device profiling to an authentication page
description: Instead of using the iovation IdP Adapter to gather the device profile, you can speed up the sign-on process by adding the device profiling scripts to an existing authentication adapter.
component: iovation
page_id: iovation:setup:pf_iovation_ik_adding_device_profiling_to_an_authentication_page
canonical_url: https://docs.pingidentity.com/integrations/iovation/setup/pf_iovation_ik_adding_device_profiling_to_an_authentication_page.html
llms_txt: https://docs.pingidentity.com/integrations/iovation/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 30, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to an authentication page

Instead of using the iovation IdP Adapter to gather the device profile, you can speed up the sign-on process by adding the device profiling scripts to an existing authentication adapter.

## About this task

These steps describe how to add the device-profiling scripts to the HTML Form Adapter that's bundled with PingFederate. You can adapt these instructions for any page that meets the criteria listed in [Device profiling method](../pf_iovation_ik_device_profiling_method.html).

The authentication page you modify must appear earlier in the sign-on flow than the iovation IdP Adapter.

## Steps

1. Embed the JavaScript files in the page.

   1. Open the `<pf_install>/pingfederate/server/default/conf/template/html.form.login.template.html` file for editing.

   2. At the end of the file, above the \</body> tag, add the following external script references:

      ```
      <script language="javascript" src="../assets/scripts/iovation_adapter_custom.js"></script>
      <script language="javascript" src="../assets/scripts/iovation_device_profiling.js"></script>
      ```

   3. Save the file.

2. (Optional) Customize the name prefix for the blackbox cookie to suit your environment:

   1. Open the `<pf_install>/pingfederate/server/default/conf/assets/scripts/iovation_adapter_custom.js` file for editing.

   2. On the following line, change `iovation_bb` to a name prefix of your choosing:

      ```
      var bbCookieNamePrefix = "iovation_bb";
      ```

      |   |                                                                                                                                                                                                                                                                                                                                       |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you customize the name prefix, you must enter the new prefix value in the **Blackbox Cookie Name Prefix** field in [Configuring an adapter instance](pf_iovation_ik_configuring_an_adapter_instance.html). Additionally, you must set the **Device Profiling Method** to **Captured by a previous adapter**. Learn more in step 5. |

   3. Save the file.

3. (Optional) Increase the client header buffer size setting on your proxy server.

   It must be able to accommodate the blackbox HTTP cookies (up to 8 KB) as well as any other cookies in your sign-on flow.

4. Configure your proxy server to pass the user's IP address to PingFederate through HTTP headers:

   1. In your reverse proxy server configuration, specify a header to store the IP address associated with the request, such as *\<X-Forwarded-For>*.

   2. In the PingFederate admin console, go to **Security > System Integration > Incoming Proxy Settings**.

   3. In the **HTTP Header For Client IP Addresses** field, enter the header you specified in step 4a.

      You can find more details in [Configure incoming proxy settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_systemoptionstasklet_systemoptionsstate.html) in the PingFederate documentation.

5. When [Configuring an adapter instance](pf_iovation_ik_configuring_an_adapter_instance.html), configure the **Device Profiling Method** and **Blackbox Cookie Name Prefix** fields as shown in [iovation IdP Adapter settings reference](pf_iovation_ik_iovation_idp_adapter_settings_reference.html).

---

---
title: Adding risk results to your authentication policy
description: By modifying your authentication policy to include risk results, you can dynamically change authentication requirements for higher-risk users.
component: iovation
page_id: iovation:setup:pf_iovation_ik_adding_risk_results_to_your_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/iovation/setup/pf_iovation_ik_adding_risk_results_to_your_authentication_policy.html
llms_txt: https://docs.pingidentity.com/integrations/iovation/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 30, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding risk results to your authentication policy

By modifying your authentication policy to include risk results, you can dynamically change authentication requirements for higher-risk users.

## About this task

These steps are designed to help you add to an existing authentication policy. You can find general information about configuring authentication policies in [Policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/qmq1564002987890.html) in the PingFederate documentation.

## Steps

1. Sign on to the PingFederate administrative console.

2. Go to **Authentication > Policies** and either open an existing authentication policy, or create a new one.

   Learn more in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

3. In the **Policy** section, in the **Select** list, select an iovation IdP Adapter instance.

   ![Screen capture of example adapter instance selection options.](_images/Success_path.jpg)

4. Map the user ID into the iovation IdP Adapter instance:

   ![Screen capture of the Incoming User ID section with the HTML form adapter as the source and username as the attribute.](_images/Incoming_user_id.jpg)

   1. Under the iovation IdP Adapter instance, click **Options**.

   2. On the **Options** modal, in the **Source** list, select a previous authentication source that collects the user ID.

   3. In the **Attribute** list, select the user ID. Click **Done**.

5. Define policy paths based on risk results:

   ![Screen capture of the Rules section that shows three policy paths with transactionRiskResults as the Attribute Name.](_images/Rules.jpg)

   1. Under the iovation IdP Adapter instance, click **Rules**.

   2. On the **Rules** modal, in the **Attribute Name** list, select **transactionRiskResult**.

   3. In the **Condition** list, select **equal to**.

   4. In the **Value** field, enter `allow`, `review`, or `deny`.

   5. In the **Result** field, enter a name.

      This appears as a new policy path that branches from the authentication source.

   6. To add more authentication paths, click **Add** and repeat steps a - d.

   7. Clear the **Default to success** checkbox.

   8. Click **Done**.

6. Configure each of the authentication paths, including **Fail**, **Success**, and the paths that you defined in the **Rules** modal.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | In case the iovation API is unreachable or returns an error, you can allow users to continue to sign on by satisfying stricter authentication requirements.You can do this in your authentication policy by setting the **Fail** outcome of the iovation IdP Adapter instance to point to a second authentication factor, as shown in the following example.Alternately, you can do this in your iovation IdP Adapter instance by setting the **Failure Mode** as shown in [Configuring an adapter instance](pf_iovation_ik_configuring_an_adapter_instance.html). |

   ![Screen capture showing authentication paths for Fail, Allow, and Review, the three policy paths configured based on risk results in step 6.](_images/Review.jpg)

7. Click **Done**.

8. On the **Policies** page, click **Save**.

---

---
title: Changelog
description: This list describes the changes made in each version of the iovation Integration Kit.
component: iovation
page_id: iovation:release_notes:pf_iovation_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/iovation/release_notes/pf_iovation_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/iovation/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2025
section_ids:
  iovation-integration-kit-2-0-august-2025: iovation Integration Kit 2.0 - August 2025
  iovation-integration-kit-1-0-1-may-2022: iovation Integration Kit 1.0.1 - May 2022
  iovation-integration-kit-1-0-october-2019: iovation Integration Kit 1.0 - October 2019
---

# Changelog

This list describes the changes made in each version of the iovation Integration Kit.

## iovation Integration Kit 2.0 - August 2025

* Added mutual TLS (mTLS) support to communicate with iovation APIs. Learn more in [Known issues and limitations](pf_iovation_ik_known_issues_and_limitations.html) and [iovation IdP Adapter settings reference](../setup/pf_iovation_ik_iovation_idp_adapter_settings_reference.html).

## iovation Integration Kit 1.0.1 - May 2022

* Standardized the directory file structure.

## iovation Integration Kit 1.0 - October 2019

* Initial release.

* Added support for iovation FraudForce.

* Added support for sending device profiles and transaction data to the iovation API.

* Added support for retrieving risk assessment results and transaction data from the iovation API.

* Added the ability to include device profiling in any browser-based authentication source.

* Added the **Iovation API Base URL** field to direct requests to the production or pre-production iovation API.

* Added the **Failure Mode** and **Fallback Risk Result Value** fields to handle failed risk result requests.

* Added the **API Request Timeout** and **Connection Timeout** fields.

* Added the **Proxy Settings**, **Custom Proxy Host**, and **Custom Proxy Port** fields to override PingFederate system-default proxy settings.

* Added the **Verify HTTPS Hostname** field to skip hostname verification.

---

---
title: Configuring an adapter instance
description: Configure the iovation IdP Adapter to determine how PingFederate communicates with the iovation API.
component: iovation
page_id: iovation:setup:pf_iovation_ik_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/iovation/setup/pf_iovation_ik_configuring_an_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/iovation/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 30, 2025
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Configure the iovation IdP Adapter to determine how PingFederate communicates with the iovation API.

## Steps

1. Sign on to the PingFederate administrative console.

2. Go to **Authentication > IdP Adapters** and click **Create New Instance**.

3. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **iovation IdP Adapter**. Click **Next**.

4. (Optional) On the **IdP Adapter** tab, in the **Optional Transaction Insight Parameters** section, configure additional transaction data to send to iovation with the device profile.

   You can find an overview in [Transaction insight parameters](pf_iovation_ik_transaction_insight_parameters.html).

   1. Click **Add a new row to 'Transaction Insight Parameters'**.

   2. In the **Incoming Attribute Name** field, enter the name of an attribute from any authentication source that appears earlier in your PingFederate authentication policy than the iovation IdP Adapter.

   3. In the **iovation API Attribute Parameter** field, enter the transaction insight parameter, such as `billingCountry` or `eventId`.

   4. In the **Action** column, click **Update**.

   5. To map another transaction insight parameter, repeat steps a - d.

5. (Optional) On the **IdP Adapter** tab, in the **Optional iovation Attributes** section, configure additional attributes to include in the attribute contract from the iovation payload.

   |   |                                                                                            |
   | - | ------------------------------------------------------------------------------------------ |
   |   | The `transactionRiskResult`(`/result`) attribute is already included in the core contract. |

   1. Click **Add a new row to 'Optional iovation Attributes'**.

   2. In the **Local Attribute** field, enter a name of your choosing for an attribute.

   3. In the **iovation API Attribute Mapping** field, enter the JSON Pointer syntax for the value of the matching iovation attributes as shown in [JSON Pointer syntax reference](pf_iovation_ik_json_pointer_syntax_reference.html).

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a - d.

6. On the **IdP Adapter** tab, configure the adapter instance by referring to [iovation IdP Adapter settings reference](pf_iovation_ik_iovation_idp_adapter_settings_reference.html). Click **Next**.

7. On the **Actions** tab, test your connection to the iovation API. Resolve any issues that are reported, and then click **Next**.

8. On the **Extended Contract** tab, add any attributes that you included in the **Optional iovation Attributes** section of the **IdP Adapter** tab.

9. Complete the adapter configuration.

10. On the **Summary** tab, check that the configuration is correct. Click **Done**.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the iovation Integration Kit files to your PingFederate directory.
component: iovation
page_id: iovation:setup:pf_iovation_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/iovation/setup/pf_iovation_ik_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/iovation/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 30, 2025
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the iovation Integration Kit files to your PingFederate directory.

## Steps

1. Download the integration kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/iovation-integration-kit).

2. Stop PingFederate.

3. If upgrading from a previous version of the adapter, delete the `pf-iovation-adapter-<version>.jar` file from the `<pf_install>/pingfederate/server/default/deploy` directory.

4. In the `.zip` archive, copy the integration kit files to the PingFederate directory.

   1. Copy the contents of `dist` to `<pf_install>/pingfederate/server/default/deploy`.

   2. Copy the contents of `conf` to `<pf_install>/pingfederate/server/default/conf`.

5. Start PingFederate.

6. If you operate PingFederate in a cluster, repeat steps 2 - 5 for each instance of PingFederate.

---

---
title: Device profiling method
description: To produce a risk assessment for a sign-on event, FraudForce requires information about the user's device. You can collect this information using the iovation IdP Adapter or by attaching the scripts to another adapter in your sign-on flow.
component: iovation
page_id: iovation::pf_iovation_ik_device_profiling_method
canonical_url: https://docs.pingidentity.com/integrations/iovation/pf_iovation_ik_device_profiling_method.html
llms_txt: https://docs.pingidentity.com/integrations/iovation/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 22, 2025
section_ids:
  captured-by-the-iovation-idp-adapter: Captured by the iovation IdP Adapter
  captured-by-a-previous-adapter: Captured by a previous adapter
---

# Device profiling method

To produce a risk assessment for a sign-on event, FraudForce requires information about the user's device. You can collect this information using the iovation IdP Adapter or by attaching the scripts to another adapter in your sign-on flow.

## Captured by the iovation IdP Adapter

The iovation IdP Adapter inserts a page into the sign-on flow that shows a spinner animation while the device profiling process runs. The page typically appears after the first-factor authentication page, as determined by your authentication policy.

|   |                                                            |
| - | ---------------------------------------------------------- |
|   | This method adds a short wait time to the sign-on process. |

## Captured by a previous adapter

Scripts are added to a page presented by another adapter in your authentication policy. This page must appear earlier in the sign-on flow than the iovation IdP Adapter, such as the first-factor authentication page.

This method reduces wait times by allowing the iovation JavaScript to prepare the device profile blackbox while the user types in their credentials.

The iovation IdP Adapter is still responsible for sending data back to the iovation API, so the script uses HTTP cookies to pass the device profile blackbox from the first-factor authentication page to the iovation IdP Adapter.

You can integrate the iovation script into any page that meets the following criteria:

* The page appears before the iovation IdP Adapter in the sign-on flow.

* The page is hosted in the same domain as your PingFederate server. This allows you to use HTTP cookies to pass the blackbox to the iovation IdP Adapter.

  |   |                                                                                                              |
  | - | ------------------------------------------------------------------------------------------------------------ |
  |   | You might be able to work around this requirement by consolidating your domains with a reverse proxy server. |

* You have access to add JavaScript to the page's HTML code.

You can find instructions in [Adding device profiling to an authentication page](setup/pf_iovation_ik_adding_device_profiling_to_an_authentication_page.html) after you finish [Deploying the integration files](setup/pf_iovation_ik_deploying_the_integration_files.html).

---

---
title: Download manifest
description: The following files are included in the iovation Integration Kit .zip archive:
component: iovation
page_id: iovation:release_notes:pf_iovation_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/iovation/release_notes/pf_iovation_ik_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/iovation/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 22, 2025
---

# Download manifest

The following files are included in the iovation Integration Kit `.zip` archive:

* `Legal.pdf`: Copyright and license information.

* `dist/pingfederate/server/default`: Contains the integration files.

  * `deploy`: Contains the Java libraries.

    * `pf-iovation-adapter-<version>.jar`: A JAR file that contains the iovation IdP Adapter.

  * `conf`: A directory that contains the HTML template and script that send device data to the iovation API.

    * `language-packs`: Contains files with customizable user-facing messages.

      * `iovation-messages.properties`: A variable file that customizes the messages that appear on the template file.

    * `template`: Contains user-facing HTML template files.

      * `iovation.adapter.template.html`: A sign-on redirect page that triggers the script file.

      * `assets`: Contains functional scripts and files used by the template.

        * `css`: Contains the template file style sheets.

          * `iovation.css`: A CSS file that customizes the appearance of the template file.

        * `scripts`: Contains script files used to collect and send information.

          * `iovation_device_profiling.js`: A JavaScript script that fetches the latest iovation JavaScript and collects device data.

          * `iovation_adapter_default.js`: A JavaScript script that configures the iovation device profiling script. Used with the default device profiling method.

          * `iovation_adapter_custom.js`: A JavaScript script that configures the iovation device profiling script and prepares blackbox cookies. Used with the custom device profiling method.

          * `iovation_spinner.js`: A JavaScript script that presents a spinner animation while user data is processed and sent to the iovation API.

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.
component: iovation
page_id: iovation:troubleshooting:pf_iovation_ik_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/iovation/troubleshooting/pf_iovation_ik_enabling_debug_logging.html
llms_txt: https://docs.pingidentity.com/integrations/iovation/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 20, 2025
section_ids:
  steps: Steps
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.

|   |                        |
| - | ---------------------- |
|   | This task is optional. |

You can find general information about logging in [Enabling debug messages and console logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html) in the PingFederate documentation.

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

   2. Change `INFO` to `DEBUG`:

      ```html
      <AsyncRoot level="DEBUG" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   3. If you want to see the adapter activity in the console, remove the comment tags:

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<AppenderRef ref="CONSOLE" />
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

3. If you want to log only activity relating to the iovation IdP Adapter, add the following line:

   ```html
   <Logger name="com.pingidentity.adapters.iovation" level="DEBUG"/>
   ```

4. Save the file.

---

---
title: iovation IdP Adapter settings reference
description: Field descriptions for the iovation IdP Adapter configuration page:
component: iovation
page_id: iovation:setup:pf_iovation_ik_iovation_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/iovation/setup/pf_iovation_ik_iovation_idp_adapter_settings_reference.html
llms_txt: https://docs.pingidentity.com/integrations/iovation/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2025
---

# iovation IdP Adapter settings reference

Field descriptions for the iovation IdP Adapter configuration page:

> **Collapse: Standard fields**
>
> | Field                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                      |
> | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Subscriber ID**              | The subscriber ID iovation provides you.                                                                                                                                                                                                                                                                                                                                                                                         |
> | **Subscriber Account**         | The subscriber account iovation provides you. This is typically `OLTP`.                                                                                                                                                                                                                                                                                                                                                          |
> | **Subscriber Passcode**        | The subscriber passcode iovation provides you.                                                                                                                                                                                                                                                                                                                                                                                   |
> | **Client Certificate**         | The client certificate used to authenticate to the iovation service.&#xA;&#xA;You can find more information on adding a client certificate in Manage SSL client keys and certificates in the PingFederate docs.                                                                                                                                                                                                                  |
> | **Iovation Integration Point** | The name of the integration point you configured in the iovation Intelligence Center in [Setup](pf_iovation_ik_setup.html).                                                                                                                                                                                                                                                                                                      |
> | **Iovation API Base URL**      | The URL of the iovation API.- Production
>
>   https\://mtls-api.iovation.com
>
> - Pre-production
>
>   https\://mtls-ci-api.iovation.com                                                                                                                                                                                                                                                                                                |
> | **Device Profiling Method**    | The stage of authentication that device details are collected in. You can find a more detailed description in [Device profiling method](../pf_iovation_ik_device_profiling_method.html).&#xA;&#xA;If you completed the optional steps in Adding device profiling to an authentication page, select Captured by a previous adapter. Otherwise, select Captured by this adapter.The default value is **Captured by this adapter**. |

> **Collapse: Advanced fields**
>
> | Field                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
> | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Device Profiling Timeout**    | The amount of time, in milliseconds, that PingFederate waits for the iovation scripts to collect device details.&#xA;&#xA;Applies only when Device Profiling Method is Captured by this adapter.The default value is `2000`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
> | **Blackbox Cookie Name Prefix** | The prefix of the cookies that contain the iovation blackbox captured by a previous adapter.&#xA;&#xA;Applies only when Device Profiling Method is Captured by a previous adapter.If you customized the name prefix for the blackbox cookie in [Adding device profiling to an authentication page](pf_iovation_ik_adding_device_profiling_to_an_authentication_page.html), enter the same name in this field.The default value is `iovation_bb`.                                                                                                                                                                                                                                                                                                                                 |
> | **Fraud Check API Endpoint**    | The iovation REST Fraud Check API endpoint that assesses risk for transactions based on the device and transaction details.The default value is `/fraud/v1/subs/${subscriberId}/checks`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
> | **Failure Mode**                | When iovation is unavailable or an error occurs, this setting determines whether the user's sign-on attempt should fail or continue with a pre-determined risk result.For cases where the iovation API is unavailable or returns an error, you can allow users to continue to sign on by satisfying stricter authentication requirements. You can configure this either:- In your adapter configuration by setting the **Failure Mode** to return the `review` result.
>
> - In your authentication policy by setting the **Fail** outcome of the iovation IdP Adapter instance as shown in [Adding risk results to your authentication policy](pf_iovation_ik_adding_risk_results_to_your_authentication_policy.html).The default value is **Continue with fallback risk result**. |
> | **Fallback Risk Result Value**  | The risk result (for example, `review`, `deny`, or `unknown`) to use in the authentication policy when iovation is unavailable or an error occurs, and **Failure Mode** is **Continue with fallback risk result**.The default value is `review`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
> | **API Request Timeout**         | The amount of time, in milliseconds, that PingFederate waits for the API to respond to requests. A value of `0` disables the timeout.The default value is `2000`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> | **Connection Timeout**          | The amount of time, in milliseconds, that PingFederate allows to establish a connection with the API. A value of `0` disables the timeout.The default value is `2000`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
> | **Proxy Settings**              | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
> | **Custom Proxy Host**           | The proxy server hostname to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | **Custom Proxy Port**           | The proxy server port to use when **Proxy Settings** is **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
> | **Verify HTTPS Hostname**       | When a connection is established with iovation, PingFederate matches the target hostname against the names stored inside the server's X.509 certificate. This security measure ensures that PingFederate is connecting to the correct server.This checkbox is selected by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

---

---
title: iovation Integration Kit
description: The iovation Integration Kit allows PingFederate to communicate with iovation Device Risk.
component: iovation
page_id: iovation::pf_iovation_ik
canonical_url: https://docs.pingidentity.com/integrations/iovation/pf_iovation_ik.html
llms_txt: https://docs.pingidentity.com/integrations/iovation/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2025
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# iovation Integration Kit

The iovation Integration Kit allows PingFederate to communicate with iovation Device Risk.

By sending a device profile to iovation when a user signs on, PingFederate can get a security risk assessment for the sign-on event. The risk assessment results allow you to adjust authentication requirements based on your authentication policies.

## Components

* iovation IdP Adapter

  * When a user signs on through PingFederate, the adapter sends the device profile to the iovation API, and retrieves a risk result.

* Template and script files

  * When a user signs on through PingFederate, these files retrieve the latest JavaScript from iovation in order to build a profile of the device.

## Intended audience

This document is intended for PingFederate administrators. Before starting, familiarize yourself with the following resources:

* [PingFederate and iovation](https://support.pingidentity.com/servlet/servlet.FileDownload?file=00P1W00001PXcEuUAL) \[PDF] solution brief

* [Configuring Integration Points](https://help.iovation.com/Managing_Business_Rules_with_the_Business_Rule_Editor/Configuring_Integration_Points) in the iovation Help Center (sign-on required)

* [Defining and Managing Business Rules](https://help.iovation.com/Managing_Business_Rules_with_the_Business_Rule_Editor/Defining_and_Managing_Business_Rules) in the iovation Help Center (sign-on required)

* [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html) in the PingFederate documentation

## System requirements

* PingFederate 11.3 or later

* An iovation cloud service account

* [iovation Intelligence Center](https://admin.iovation.com/login.html) login credentials (provided by iovation):

  * Account

  * Login

  * Password

* iovation Device Risk credentials (provided by iovation):

  * Subscriber ID

  * Subscriber account

  * Passcode

  * Client certificate (for mTLS)

---

---
title: JSON Pointer syntax reference
description: JavaScript Object Notation (JSON) Pointer defines a syntax for identifying a specific value within a JSON payload. Using the sample payload and JSON Pointer examples below, identify the attributes that you want to use to populate your attribute contract.
component: iovation
page_id: iovation:setup:pf_iovation_ik_json_pointer_syntax_reference
canonical_url: https://docs.pingidentity.com/integrations/iovation/setup/pf_iovation_ik_json_pointer_syntax_reference.html
llms_txt: https://docs.pingidentity.com/integrations/iovation/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 15, 2025
section_ids:
  example-json-payload: Example JSON payload
---

# JSON Pointer syntax reference

JavaScript Object Notation (JSON) Pointer defines a syntax for identifying a specific value within a JSON payload. Using the sample payload and JSON Pointer examples below, identify the attributes that you want to use to populate your attribute contract.

You can find a complete technical description of JSON Pointer syntax in the [IETF RFC 6901 - JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901).

You can find more information about the iovation payload structure in [Transaction REST API Response Attributes](https://help.iovation.com/Programming_References/API_Reference_Documentation/Transaction_REST_API_Response_Attributes) in the iovation Help Center (sign-on required).

## Example JSON payload

```json
{
    "id": "4a5cc146-9a48-4663-b93e-cdc3fa4517ba",
    "result": "R",
    "reason": "Accounts Per Device- 3 Max",
    "statedIp": "127.0.0.1",
    "accountCode": "sampleAccountCode",
    "trackingNumber": 877301938420090395,
    "details": {
        "device": {
            "alias": 113919332761383848,
            "blackboxMetadata": {
                "age": 937853,
                "timestamp": "2019-10-10T23:42:03Z"
            },
            "browser": {
                "cookiesEnabled": true,
                "configuredLanguage": "EN-CA,EN-US;Q=0.7,EN;Q=0.3",
                "language": "EN-CA",
                "type": "FIREFOX",
                "timezone": "480",
                "version": "70.0"
            },
            "firstSeen": "2019-10-01T23:48:46.393Z",
            "isNew": false,
            "os": "INTEL MAC OS X 10.14",
            "screen": "1440X3440",
            "type": "MAC"
        },
        "statedIp": {
            "address": "127.0.0.1",
            "source": "subscriber"
        },
        "realIp": {
            "address": "8.8.8.8",
            "isp": "INTERNET NOW",
            "ipLocation": {
                "city": "MANASSAS",
                "country": "UNITED STATES",
                "countryCode": "US",
                "latitude": 38.74622,
                "longitude": -77.48911,
                "region": "VIRGINIA"
            },
            "parentOrganization": "INTERNET NOW",
            "source": "iovation"
        },
        "ruleResults": {
            "score": -1,
            "rulesMatched": 1,
            "rules": [
                {
                    "type": "Accounts Per Device",
                    "reason": "Accounts Per Device- 3 Max",
                    "score": -1
                }
            ]
        }
    }
}
```

**JSON Pointer syntax**

| Description                                                                                    | JSON Pointer                         | Example value   |
| ---------------------------------------------------------------------------------------------- | ------------------------------------ | --------------- |
| Result of the transaction risk assessment.- `A`

  `allow`

- `R`

  `review`

- `D`

  `deny` | `/result`                            | `R`             |
| The numeric score that determines the risk result.                                             | `/details/ruleResults/score`         | `-1`            |
| The country that the device is signing in from.                                                | `/details/realIp/ipLocation/country` | `UNITED STATES` |

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the iovation Integration Kit.
component: iovation
page_id: iovation:release_notes:pf_iovation_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/iovation/release_notes/pf_iovation_ik_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/iovation/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 20, 2025
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the iovation Integration Kit.

## Known issues

There are no known issues.

## Known limitations

* iovation Integration Kit 2.0 requires mTLS

  iovation Integration Kit 2.0 requires mTLS to communicate with the iovation APIs. You must acquire a certificate, import it into PingFederate, and add it to any new or existing adapter instance configurations.

  |   |                                                                                                                                                                                                                                                                                       |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | You can find more information on adding a client certificate in [Manage SSL client keys and certificates](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_sslcertauth_certmanagementstate.html) in the PingFederate docs. |

---

---
title: Overview of iovation Device Risk
description: iovation Device Risk collects a device profile and other transaction data and uses a series of rules to evaluate the level of security risk for a transaction. The type of transaction is flexible, but in the context of PingFederate, it's usually a user sign-on event.
component: iovation
page_id: iovation::pf_iovation_ik_overview_of_iovation_device_risk
canonical_url: https://docs.pingidentity.com/integrations/iovation/pf_iovation_ik_overview_of_iovation_device_risk.html
llms_txt: https://docs.pingidentity.com/integrations/iovation/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 15, 2025
section_ids:
  device-profile-blackbox-and-transaction-insight-parameters: Device profile, blackbox, and transaction insight parameters
  integration-points: Integration points
  rule-sets-and-business-rules: Rule sets and business rules
  risk-results: Risk results
---

# Overview of iovation Device Risk

iovation Device Risk collects a device profile and other transaction data and uses a series of rules to evaluate the level of security risk for a transaction. The type of transaction is flexible, but in the context of PingFederate, it's usually a user sign-on event.

## Device profile, blackbox, and transaction insight parameters

When a user signs on, iovation JavaScript collects hundreds of data elements associated with the device, including the device type, geolocation information, information about the browser, and system settings such as language settings. Together, this data is called the device profile.

The iovation JavaScript encrypts the device profile in a package called a *blackbox*.

In addition to the device profile data, you can take attributes from previous authentication sources and send them to iovation as transaction insight parameters.

The iovation IdP Adapter sends the blackbox and transaction insight parameters to iovation for analysis.

## Integration points

Each iovation IdP Adapter instance communicates with the iovation API through a specific integration point. Each integration point typically represents one type of interaction, such as sign-on or password change.

You can find guidance on integration point design in [Planning and Designing Integration Points](https://help.iovation.com/Managing_Business_Rules_with_the_Business_Rule_Editor/Configuring_Integration_Points/01_Planning_and_Designing_Integration_Points) in the iovation Help Center (sign-on required).

## Rule sets and business rules

Each integration point is associated with one rule set, which is a collection of business rules and rule groups.

Each business rule has a numeric weight assigned to it. When the conditions of the rule are met by the device profile or transaction data, the weight affects the total risk score for a transaction.

You can find a list of business rule categories in [About iovation Device Risk](https://help.iovation.com/001_FraudForce/01_Getting_Started_with_FraudForce/02_FraudForce_Basics/01_About_FraudForce) and an example business rule scenario in [Business Rule Basics](https://help.iovation.com/001_FraudForce/01_Getting_Started_with_FraudForce/02_FraudForce_Basics/02_How_Business_Rules_Catch_Suspicious_Behavior) in the iovation Help Center (sign-on required).

## Risk results

After processing the device profile through the rule set, Device Risk matches the resulting risk score to one of three risk results: `allow`, `review`, or `deny`. The rule set determines the numeric threshold associated with each of the results.

You can find more details about result thresholds in [About Rule Weights and Thresholds](https://help.iovation.com/001_FraudForce/01_Getting_Started_with_FraudForce/02_FraudForce_Basics/02_How_Business_Rules_Catch_Suspicious_Behavior//) in the iovation Help Center (sign-on required).

The iovation API provides the risk result and other data in a response to PingFederate. By including the risk result in your authentication policy, you decide how each of the `allow`, `review`, and `deny` results affects a user's ability to sign on in your environment.

---

---
title: Overview of the SSO flow
description: With the iovation Integration Kit, PingFederate includes the iovation API in the sign-on flow as follows.
component: iovation
page_id: iovation::pf_iovation_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/iovation/pf_iovation_ik_overview_of_the_sso_flow.html
llms_txt: https://docs.pingidentity.com/integrations/iovation/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 30, 2025
section_ids:
  description: Description
---

# Overview of the SSO flow

With the iovation Integration Kit, PingFederate includes the iovation API in the sign-on flow as follows.

![Diagram showing how the iovation API is integrated in the sign-on process.](_images/SSO_flow.png)

## Description

1. A user initiates the sign-on process by requesting access to a protected resource.

2. Depending on the device profiling method, the iovation IdP Adapter or a previous authentication adapter retrieves the latest JavaScript from iovation.

   |   |                                                                               |
   | - | ----------------------------------------------------------------------------- |
   |   | For the previous adapter method, this takes place at the same time as step 1. |

3. Depending on the device profiling method, the iovation IdP Adapter or a previous authentication adapter runs the iovation JavaScript, which builds the device profile and packages it in an encrypted blackbox.

4. The iovation IdP Adapter sends the blackbox and transaction insight parameters to the iovation API and requests the risk result for the transaction.

5. The iovation API returns a JSON payload with the risk result and other attributes to the iovation IdP Adapter.

6. The iovation IdP Adapter makes the risk result and contract attributes available in the authentication policy.

7. PingFederate executes the authentication policy, which branches based on the risk result reported by the iovation IdP Adapter.

8. PingFederate returns the resource that the user requested.

---

---
title: Setup
description: To use the iovation Integration Kit with PingFederate, set up a reverse proxy server, configure iovation, then set up the integration on your PingFederate server.
component: iovation
page_id: iovation:setup:pf_iovation_ik_setup
canonical_url: https://docs.pingidentity.com/integrations/iovation/setup/pf_iovation_ik_setup.html
llms_txt: https://docs.pingidentity.com/integrations/iovation/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 15, 2025
section_ids:
  steps: Steps
---

# Setup

To use the iovation Integration Kit with PingFederate, set up a reverse proxy server, configure iovation, then set up the integration on your PingFederate server.

## Steps

1. Set up a reverse proxy server as shown in [Retrieving & Serving Dynamic iovation JavaScript](https://help.iovation.com/001_FraudForce/04_Integrating_FraudForce/02_Integrating_with_Websites/02_Retrieving_First-Party_Dynamic_JavaScript) in the iovation Help Center (sign-on required).

   By positioning PingFederate behind the reverse proxy server, you allow it to retrieve and run the latest iovation device-profiling JavaScript when a user signs on.

2. In the [iovation Intelligence Center](https://admin.iovation.com/login.html), create business rules and an integration point.

   This determines how risk results are determined for sign-on transactions through your iovation IdP Adapter instance. For configuration guidance and instructions, explore the relevant topics in the iovation Help Center, such as [Defining and Managing Business Rules](https://help.iovation.com/Managing_Business_Rules_with_the_Business_Rule_Editor/Defining_and_Managing_Business_Rules) and [Configuring Integration Points](https://help.iovation.com/Managing_Business_Rules_with_the_Business_Rule_Editor/Configuring_Integration_Points) (sign-on required). The iovation customer success team can help you plan business rules to suit your needs.

3. Deploy the integration files to your PingFederate server as shown in [Deploying the integration files](pf_iovation_ik_deploying_the_integration_files.html).

4. (Optional) Reduce user sign-on times by [Adding device profiling to an authentication page](pf_iovation_ik_adding_device_profiling_to_an_authentication_page.html).

5. Configure the iovation IdP Adapter as shown in [Configuring an adapter instance](pf_iovation_ik_configuring_an_adapter_instance.html).

6. Integrate iovation risk results into your authentication policy as shown in [Adding risk results to your authentication policy](pf_iovation_ik_adding_risk_results_to_your_authentication_policy.html).

---

---
title: Transaction insight parameters
description: When a user signs on, iovation can collect optional transaction data along with the device profile. In the iovation Intelligence Center, you can use these transaction insight parameters in business rules to affect risk results.
component: iovation
page_id: iovation:setup:pf_iovation_ik_transaction_insight_parameters
canonical_url: https://docs.pingidentity.com/integrations/iovation/setup/pf_iovation_ik_transaction_insight_parameters.html
llms_txt: https://docs.pingidentity.com/integrations/iovation/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 15, 2025
---

# Transaction insight parameters

When a user signs on, iovation can collect optional transaction data along with the device profile. In the iovation Intelligence Center, you can use these transaction insight parameters in business rules to affect risk results.

The iovation IdP Adapter allows you to take attributes from previous authentication sources in your PingFederate authentication policy and send them to iovation as transaction insight parameters.

For example, on the first-factor authentication page, you collect the user's security PIN type. Then, in your iovation IdP Adapter instance, you map the PIN type attribute to the iovation `securityPinType` parameter. This allows you to create a business rule that considers certain PIN types to be higher risk.

You can find a complete list of transaction insight parameters you can populate in [Transaction Insight Fields](https://help.iovation.com/Programming_References/API_Reference_Documentation/002_iovation_Data_Dictionary/Transaction_Insight_Fields) in the iovation Help Center (sign-on required).

---

---
title: Troubleshooting information
description: The following information addresses technical situations you might encounter after setting up the iovation Integration Kit:
component: iovation
page_id: iovation:troubleshooting:pf_iovation_ik_troubleshooting_info
canonical_url: https://docs.pingidentity.com/integrations/iovation/troubleshooting/pf_iovation_ik_troubleshooting_info.html
llms_txt: https://docs.pingidentity.com/integrations/iovation/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 15, 2025
---

# Troubleshooting information

The following information addresses technical situations you might encounter after setting up the iovation Integration Kit:

| Situation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Recommendation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Using iovation with PingFederate 11.3 results in the following error:`iovation_device_profiling.js:5 Refused to load the script 'https://mpsnare.iesnare.com/general5/xz1wcI_mlev7ZyvfJj94rYhbKk9av1rsH3sDg5_JGsQ/wdp.js?loaderVer=5.2.2&compat=false&tp=true&tp_split=false&fp_static=true&fp_dyn=true&flash=false' because it violates the following Content Security Policy directive: "script-src 'self' 'nonce-6Uzh6NlXESurUeLj'". Note that 'script-src-elem' was not explicitly set, so 'script-src' is used as a fallback.` | Update the HTML form template in `$PF_HOME/server/default/conf/templates`.HTML pages implementing ContentSecurityPolicy restrictions might require updates to the `script-src` and `image-src` CSP settings when adding the `iovation_device_profiling` JavaScript file to the page. Update `script-src` and `img-src` to include the `https://mpsnare.iesnare.com` host name.For example, PingFederate 11.3 has default templates with strict CSP settings. To use the `iovation_device_profiling` JavaScript file with the default templates, update the following line in the template's CSP settings:```
<meta http-equiv="Content-Security-Policy" content="script-src 'self' 'nonce-$CSPNonce'; style-src 'self'; img-src 'self'; font-src 'self';" />
```Updated line:```
<meta http-equiv="Content-Security-Policy" content="script-src 'self' 'unsafe-inline' https://mpsnare.iesnare.com; style-src 'self'; img-src 'self' https://mpsnare.iesnare.com; font-src 'self';" />
``` |