---
title: Adding Duo Security to your authentication policy
description: By modifying your PingFederate authentication policy to include the Duo Security IdP Adapter, you can challenge users to complete a multi-factor authentication (MFA) step.
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_22:pf_duo_security_ik_22_adding_duo_security_to_your_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_22/pf_duo_security_ik_22_adding_duo_security_to_your_authentication_policy.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Adding Duo Security to your authentication policy

By modifying your PingFederate authentication policy to include the Duo Security IdP Adapter, you can challenge users to complete a multi-factor authentication (MFA) step.

## About this task

These steps are designed to help you add to an existing authentication policy. You can find general information about configuring authentication policies in [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html) in the PingFederate documentation.

## Steps

1. In the PingFederate administrative console, go to the **Policies** tab.

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Authentication > Policies > Policies**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > Authentication Policies > Policies**.

2. Select the **IdP Authentication Policies** check box.

3. Open an existing authentication policy, or click **Add Policy**. Learn more in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

4. In the **Policy** area, from the **Select** list, select a Duo Security IdP Adapter instance.

5. Map the Duo Security user ID or username into the Duo Security IdP Adapter instance.

   1. Under the Duo Security IdP Adapter instance, click **Options**.

   2. On the **Options** dialog, from the **Source** list, select a previous authentication source that collects the Duo Security user ID or username.

   3. From the **Attribute** list, select the user ID. Click **Done**.

6. Configure each of the authentication paths.

   ![puc1579651708651](../_images/puc1579651708651.jpg)

7. Click **Done**.

8. In the **Policies** window, click **Save**.

---

---
title: Adding Duo Security to your authentication policy
description: By modifying your PingFederate authentication policy to include the Duo Security IdP Adapter, you can challenge users to complete a multi-factor authentication (MFA) step.
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_3x:pf_duo_security_ik_adding_duo_security_to_your_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_3x/pf_duo_security_ik_adding_duo_security_to_your_authentication_policy.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Adding Duo Security to your authentication policy

By modifying your PingFederate authentication policy to include the Duo Security IdP Adapter, you can challenge users to complete a multi-factor authentication (MFA) step.

## About this task

These steps are designed to help you add to an existing authentication policy. You can find general information about configuring authentication policies in [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html) in the PingFederate documentation.

## Steps

1. In the PingFederate administrative console, go to the **Policies** tab.

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Authentication > Policies > Policies**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > Authentication Policies > Policies**.

2. Select the **IdP Authentication Policies** check box.

3. Open an existing authentication policy, or click **Add Policy**. Learn more in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

4. In the **Policy** area, from the **Select** list, select a Duo Security IdP Adapter instance.

5. Map the Duo Security user ID or username into the Duo Security IdP Adapter instance.

   1. Under the Duo Security IdP Adapter instance, click **Options**.

   2. On the **Options** dialog, from the **Source** list, select a previous authentication source that collects the Duo Security user ID or username.

   3. From the **Attribute** list, select the user ID. Click **Done**.

6. Configure each of the authentication paths.

   ![puc1579651708651](../_images/puc1579651708651.jpg)

7. Click **Done**.

8. In the **Policies** window, click **Save**.

---

---
title: Authentication API support
description: You can use the PingFederate authentication API to integrate the Duo Security IdP Adapter into your application.
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_3x:pf_duo_security_ik_authentication_api_support
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_3x/pf_duo_security_ik_authentication_api_support.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
---

# Authentication API support

You can use the PingFederate authentication API to integrate the Duo Security IdP Adapter into your application.

The PingFederate Authentication API provides access to the current state of the authentication flow as a user steps through the PingFederate authentication policy. Learn more in [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

To integrate the Duo Security IdP Adapter into your authentication flow, configure your application based on the states, actions, and models available in the PingFederate Authentication API Explorer. Learn more in [Exploring the Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_exploring_authentication_api.html) in the PingFederate documentation.

---

---
title: Changelog
description: The following is the change history for the Duo Security Integration Kit 2.2.
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_22:pf_duo_security_ik_22_changelog
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_22/pf_duo_security_ik_22_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
section_ids:
  duo-security-integration-kit-2-2-2-january-2020: Duo Security Integration Kit 2.2.2 - January 2020
  duo-security-integration-kit-2-2-1-july-2017: Duo Security Integration Kit 2.2.1 - July 2017
  duo-security-integration-kit-2-2-september-2016: Duo Security Integration Kit 2.2 - September 2016
  duo-security-integration-kit-2-1-april-2016: Duo Security Integration Kit 2.1 - April 2016
  duo-security-integration-kit-2-0-september-2015: Duo Security Integration Kit 2.0 - September 2015
---

# Changelog

The following is the change history for the Duo Security Integration Kit 2.2.

|   |                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This documentation is for Duo Security Integration Kit 2.2 and earlier. You can find later versions of the integration kit in the latest [Duo Security Integrations](../pf_is_overview_of_duo_security_integrations.html) documentation. |

## Duo Security Integration Kit 2.2.2 - January 2020

* Resolved an issue that allowed sessions to exceed the `max_age` parameter in the authentication request.

* Improved input validation for the **Session Timeout** field in the adapter configuration.

* Defect fixes to resolve a potential security vulnerability.

## Duo Security Integration Kit 2.2.1 - July 2017

* Resolved issue using the Duo adapter with **Failmode** set to **safe**.

* Upgraded to v2 of the Duo Web SDK.

## Duo Security Integration Kit 2.2 - September 2016

* Added **Failmode** option, allowing users to bypass second factor authentication in the event that the Duo service is down.

## Duo Security Integration Kit 2.1 - April 2016

* Added clustering support without the use of sticky sessions.

* Added option to configure login template for each adapter instance.

## Duo Security Integration Kit 2.0 - September 2015

* Initial release.

* Added support for SSO.

---

---
title: Changelog
description: The following is the change history for the Duo Security Integration Kit.
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_3x:pf_duo_security_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_3x/pf_duo_security_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
section_ids:
  duo-security-integration-kit-3-1-2-may-2024: Duo Security Integration Kit 3.1.2 - May 2024
  duo-security-integration-kit-3-1-1-july-2023: Duo Security Integration Kit 3.1.1 - July 2023
  duo-security-integration-kit-3-1-may-2023: Duo Security Integration Kit 3.1 - May 2023
  duo-security-integration-kit-3-0-3-december-2022: Duo Security Integration Kit 3.0.3 - December 2022
  duo-security-integration-kit-3-0-2-september-2021: Duo Security Integration Kit 3.0.2 - September 2021
  duo-security-integration-kit-3-0-1-march-2021: Duo Security Integration Kit 3.0.1 - March 2021
  duo-security-integration-kit-3-0-october-2020: Duo Security Integration Kit 3.0 - October 2020
  duo-security-integration-kit-2-2-2-january-2020: Duo Security Integration Kit 2.2.2 - January 2020
  duo-security-integration-kit-2-2-1-july-2017: Duo Security Integration Kit 2.2.1 - July 2017
  duo-security-integration-kit-2-2-september-2016: Duo Security Integration Kit 2.2 - September 2016
  duo-security-integration-kit-2-1-april-2016: Duo Security Integration Kit 2.1 - April 2016
  duo-security-integration-kit-2-0-september-2015: Duo Security Integration Kit 2.0 - September 2015
---

# Changelog

The following is the change history for the Duo Security Integration Kit.

## Duo Security Integration Kit 3.1.2 - May 2024

* Fixed a issue that caused the adapter to throw an error instead of making an authentication request to Duo if an OIDC call preceded the adapter call.

## Duo Security Integration Kit 3.1.1 - July 2023

* Fixed an issue with how the adapter collects the application name configured in the SP connection and sends it to Duo for use in mobile push notifications.

* Added the ability to select whether to send application names to Duo for use in push notifications. When the **Send Application Name** [check box](pf_duo_security_ik_duo_security_idp_adapter_settings_reference.html) is selected, the adapter sends Duo the application's name if it's configured in the SP connection.

  |   |                                                                                                                                                                                                               |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This check box is selected by default. If you haven't set an application name or if you clear the **Send Application Name** check box, push notifications use the application name configured in Duo instead. |

## Duo Security Integration Kit 3.1 - May 2023

* Added the ability for the adapter to send the application name to Duo where it can be displayed in the Push notification in the Duo mobile application. This provides the user more context for which application is requesting a push notification.

## Duo Security Integration Kit 3.0.3 - December 2022

* Fixed a defect in adapter when PingFederate is deployed under non-default context path.

## Duo Security Integration Kit 3.0.2 - September 2021

* Verified that the Duo Security IdP Adapter is compliant with US Federal Information Processing Standards (FIPS). For usage, see [Integrating with Bouncy Castle FIPS provider](https://docs.pingidentity.com/pingfederate/latest/getting_started_with_pingfederate/pf_integra_bouncy_castl_fips_provider.html) in the PingFederate documentation.

## Duo Security Integration Kit 3.0.1 - March 2021

* Fixed an issue that caused transactions to fail when many users were signing into Duo Security at the same time.

## Duo Security Integration Kit 3.0 - October 2020

* Added support for the new Duo Universal Prompt multi-factor authentication (MFA) flow, including:

  * OpenID Connect authentication protocol

  * Duo Universal Prompt

  * New endpoints for checking API availability, authorizing users, and getting authentication results

* Added the ability to map any Duo Universal Prompt API response attribute to an attribute in the PingFederate authentication policy.

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

* Added a setting for API connection and request timeout.

* Added settings to override the PingFederate system-default proxy settings.

* Improved security by disabling device registration during password reset flows.

* Removed the template and JavaScript files that were needed in previous versions.

## Duo Security Integration Kit 2.2.2 - January 2020

* Fixed an issue that allowed sessions to exceed the `max_age` parameter in the authentication request.

* Improved input validation for the **Session Timeout** field in the adapter configuration.

## Duo Security Integration Kit 2.2.1 - July 2017

* Fixed an issue using the Duo adapter with **Failmode** set to **safe**.

* Upgraded to v2 of the Duo Web SDK.

## Duo Security Integration Kit 2.2 - September 2016

* Added **Failmode** option, allowing users to bypass second factor authentication in the event that the Duo service is down.

## Duo Security Integration Kit 2.1 - April 2016

* Added clustering support without the use of sticky sessions.

* Added option to configure login template for each adapter instance.

## Duo Security Integration Kit 2.0 - September 2015

* Initial release.

* Added support for SSO.

---

---
title: Configuring an adapter instance
description: Configure the Duo Security IdP Adapter to determine how PingFederate communicates with Duo Security.
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_22:pf_duo_security_ik_22_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_22/pf_duo_security_ik_22_configuring_an_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Configuring an adapter instance

Configure the Duo Security IdP Adapter to determine how PingFederate communicates with Duo Security.

## Steps

1. In the PingFederate administrative console, create a new IdP adapter instance:

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. From the **Type** list, select **Duo Security IdP Adapter**. Click **Next**.

3. On the **IdP Adapter** tab, configure the adapter instance by referring to [Duo Security Adapter settings reference](pf_duo_security_ik_22_duo_security_adapter_settings_reference.html). Click **Next**.

4. On the **Actions** tab, test your connection to Duo Security. Resolve any issues that are reported, and then click **Next**.

5. On the **Extended Contract** tab, add any attributes that you want to include in the contract. Click **Next**.

6. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

7. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

8. On the **Summary** tab, check and save your configuration:

   ### Choose from:

   * For PingFederate 10.1 or later: click **Save**.

   * For PingFederate 10.0 or earlier: click **Done**. On the **Manage IdP Adapter Instances** tab, click **Save**.

---

---
title: Configuring an adapter instance
description: Configure the Duo Security IdP Adapter to determine how PingFederate communicates with Duo Universal Prompt.
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_3x:pf_duo_security_ik_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_3x/pf_duo_security_ik_configuring_an_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Configuring an adapter instance

Configure the Duo Security IdP Adapter to determine how PingFederate communicates with Duo Universal Prompt.

## Steps

1. In the PingFederate administrative console, create a new IdP adapter instance:

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. From the **Type** list, select **Duo Security IdP Adapter**. Click **Next**.

3. **Optional:** On the **IdP Adapter** tab, in the **Duo API Response Mappings** section, map attributes from the Duo Universal Prompt response to the attribute contract. These attributes become available in your PingFederate authentication policy.

   1. Click **Add a new row to 'Duo API Response Mappings'**.

   2. In the **Local Attribute** field, enter a name of your choosing for an attribute.

   3. In the **Duo API Attribute Mapping** field, enter the JSON Pointer syntax for the value of the matching Duo Security attributes as shown in [JSON Pointer syntax reference](pf_duo_security_ik_json_pointer_syntax_reference.html).

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a - d.

4. On the **IdP Adapter** tab, configure the adapter instance by referring to [Duo Security IdP Adapter settings reference](pf_duo_security_ik_duo_security_idp_adapter_settings_reference.html).

5. On the **Extended Contract** tab, add any attributes that you want to include in the contract. Click **Next**.

6. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

7. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

8. On the **Summary** tab, check and save your configuration:

   ### Choose from:

   * For PingFederate 10.1 or later: click **Save**.

   * For PingFederate 10.0 or earlier: click **Done**. On the **Manage IdP Adapter Instances** tab, click **Save**.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Duo Security Integration Kit files to your PingFederate directory.
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_22:pf_duo_security_ik_22_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_22/pf_duo_security_ik_22_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Duo Security Integration Kit files to your PingFederate directory.

## About this task

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | If you operate PingFederate in a cluster, the following steps refer to the console node. |

## Steps

1. Download the Duo Security Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/home).

2. Stop PingFederate.

3. If you are upgrading an existing deployment, delete `pf-duo-security-adapter-<version>.jar` from `<pf_install>/pingfederate/server/default/deploy`.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. Start PingFederate.

6. If you operate PingFederate in a cluster, repeat steps 2 - 5 for each engine node.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Duo Security Integration Kit files to your PingFederate directory.
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_3x:pf_duo_security_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_3x/pf_duo_security_ik_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Deploying the integration files

To get started with the integration, deploy the Duo Security Integration Kit files to your PingFederate directory.

## Steps

1. Download the Duo Security Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/duo-security-integration-kit).

2. Stop PingFederate.

3. If you are upgrading an existing deployment, delete earlier versions of the integration files.

   ### Choose from:

   * For upgrades from Duo Security Integration Kit 3.0 or later: delete `pf-duo-security-integration-kit-<version>.jar` from `<pf_install>/pingfederate/server/default/deploy`.

   * For upgrades from Duo Security Integration Kit 2.2 or earlier:

     1. Delete the `duo.adapter.template.html` file from `<pf_install>/pingfederate/server/default/conf/template`.

     2. Delete the following files from `<pf_install>/pingfederate/server/default/deploy`:

        * `pf-duo-security-adapter-<version>.jar`

        * `duo-web/js/Duo-Web-v2.min.js`

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. If there is more than one version of the `pf-authn-api-sdk-<version>.jar` file in your `<pf_install>/pingfederate/server/default/lib` directory, delete all but the latest version of the file.

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 2 - 6 for each engine node.

---

---
title: Download manifest
description: The following files are included in the Duo Security Integration Kit .zip archive:
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_22:pf_duo_security_ik_22_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_22/pf_duo_security_ik_22_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
---

# Download manifest

The following files are included in the Duo Security Integration Kit `.zip` archive:

* `ReadMeFirst.pdf` – contains links to this online documentation.

* `legal` – a directory that contains this document:

  * `Legal.pdf` – copyright and license information.

* `dist` – a directory that contains the Java libraries needed to run the adapter:

  * `pf-duo-security-adapter-<version>.jar` – JAR file that contains the Duo Security Adapter.

  * `duo-web/js` – a directory that contains a script that works with the Duo Security authentication page.

    * `Duo-Web-v2.min.js` – a script that communicates with the Duo Security API.

* `conf/template` – a directory that contains the HTML template and script that send device data to the Duo Security API.

  * `duo.adapter.template.html` – a page that presents the Duo Security authentication options during sign on.

---

---
title: Download manifest
description: The following files are included in the Duo Security Integration Kit .zip archive:
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_3x:pf_duo_security_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_3x/pf_duo_security_ik_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
---

# Download manifest

The following files are included in the Duo Security Integration Kit `.zip` archive:

* `Legal.pdf` – copyright and license information

* `dist/pingfederate/server/default` – contains the integration files

  * `deploy` – contains the Java libraries

* `lib/pf-authn-api-sdk-<version>.jar` – a JAR file that contains the PingFederate Authentication API SDK

---

---
title: Duo Security Adapter settings reference
description: Field descriptions for the Duo Security IdP Adapter configuration screen.
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_22:pf_duo_security_ik_22_duo_security_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_22/pf_duo_security_ik_22_duo_security_adapter_settings_reference.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
---

# Duo Security Adapter settings reference

Field descriptions for the Duo Security IdP Adapter configuration screen.

| Field               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Integration Key** | The integration key that you noted in [Getting your Duo Security keys and API hostname](pf_duo_security_ik_22_getting_your_duo_security_keys_and_api_hostname.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Secret Key**      | The secret key that you noted in [Getting your Duo Security keys and API hostname](pf_duo_security_ik_22_getting_your_duo_security_keys_and_api_hostname.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **API Host**        | The API hostname that you noted in [Getting your Duo Security keys and API hostname](pf_duo_security_ik_22_getting_your_duo_security_keys_and_api_hostname.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Session State**   | Determines whether this Duo Security Adapter instance maintains adapter sessions and shares adapter sessions with other Duo Security Adapter instances.- Globally

  Adapter sessions from this Duo Security Adapter instance are shared among other Duo Security Adapter instances that have **Session State** set to **Globally**.

- None

  This Duo Security Adapter does not maintain adapter sessions for this Duo Security Adapter instance.&#xA;&#xA;If you intend to enable PingFederate authentication sessions globally or individually for this adapter instance, select None. You can find more information about PingFederate authentication sessions in Sessions in the PingFederate documentation.The default selection is **None**. |
| **Session Timeout** | The amount of time in minutes of inactivity that a session is valid. A value of 0 disables the timeout. Applies only when **Session State** is set to **Globally**.The default value is 60.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Login Template**  | The filename of the Duo Security login template. You can use this to replace the provided template with your own.The custom template must be in `<pf_install>/pingfederate/default/conf/template`.The default value is `duo.form.login.template.html`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Failmode**        | When Duo Security is unavailable or an error occurs, this setting determines whether the user's sign-on attempt should fail or continue.Select **secure** to deny all sign-on attempts when Duo Security is unavailable.Select **safe** to allow all sign-on attempts when Duo Security is unavailable.The default selection is **secure**.                                                                                                                                                                                                                                                                                                                                                                                                           |

---

---
title: Duo Security IdP Adapter settings reference
description: Field descriptions for the Duo Security IdP Adapter configuration screen.
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_3x:pf_duo_security_ik_duo_security_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_3x/pf_duo_security_ik_duo_security_idp_adapter_settings_reference.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
---

# Duo Security IdP Adapter settings reference

Field descriptions for the Duo Security IdP Adapter configuration screen.

**Standard fields**

| Field             | Description                                                                                                                                                                                                                                                                                                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Client ID**     | The client ID that you noted in [Getting your Duo Security keys and API hostname](pf_duo_security_ik_getting_your_duo_security_keys_and_api_hostname.html).This field is blank by default.                                                                                                                                                                                |
| **Client Secret** | The client secret that you noted in [Getting your Duo Security keys and API hostname](pf_duo_security_ik_getting_your_duo_security_keys_and_api_hostname.html).This field is blank by default.                                                                                                                                                                            |
| **API Hostname**  | The API hostname that you noted in [Getting your Duo Security keys and API hostname](pf_duo_security_ik_getting_your_duo_security_keys_and_api_hostname.html).This field is blank by default.                                                                                                                                                                             |
| **Failure Mode**  | When Duo Universal Prompt is unavailable or an error occurs, this setting determines whether the user's sign-on attempt should fail or continue.- Select **secure** to deny all sign-on attempts when Duo Universal Prompt is unavailable.

- Select **safe** to allow all sign-on attempts when Duo Universal Prompt is unavailable.The default selection is **secure**. |

**Advanced fields**

| Field                          | Description                                                                                                                                                                                                                 |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Duo Health Check Endpoint**  | The endpoint used to check the availability of the Duo Universal Prompt API.The default value is `/oauth/v1/health_check`.                                                                                                  |
| **Duo Authorization Endpoint** | The endpoint used to perform second-factor authentication to Duo Universal Prompt.The default value is `/oauth/v1/authorize`.                                                                                               |
| **Duo Access Token Endpoint**  | The endpoint used to get an access token from Duo Universal Prompt.The default value is `/oauth/v1/token`.                                                                                                                  |
| **API Request Timeout**        | The amount of time in milliseconds that PingFederate allows when establishing a connection with Duo Universal Prompt or waiting for a response to a request. A value of 0 disables the timeout.The default value is `5000`. |
| **Send Application Name**      | Send Duo the application name configured in the SP connection for use in push notifications.This check box is selected by default.                                                                                          |
| **Proxy Settings**             | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                 |
| **Custom Proxy Host**          | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                              |
| **Custom Proxy Port**          | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                   |

---

---
title: Duo Security Integration Kit 2.2
description: The Duo Security Integration Kit allows PingFederate to use the Duo Security service for multi-factor authentication (MFA). This sign-on experience uses an iFrame and works with the Duo Auth API.
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_22:pf_duo_security_ik_22
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_22/pf_duo_security_ik_22.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Duo Security Integration Kit 2.2

The Duo Security Integration Kit allows PingFederate to use the Duo Security service for multi-factor authentication (MFA). This sign-on experience uses an iFrame and works with the Duo Auth API.

|   |                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This documentation is for Duo Security Integration Kit 2.2 and earlier. For later versions of the integration kit, see the latest [Duo Security Integration Kit 3.x](../duo_security_integration_kit_3x/pf_duo_security_ik.html) documentation. |

## Components

* Duo Security IdP Adapter

  * Allows PingFederate to trigger a multi-factor authentication (MFA) challenge during sign on.

  * Allows for MFA when single sign-on (SSO) is intiated at the identity provider (IdP) or service provider (SP).

* Template and script files

  * When a user signs on through PingFederate and the authentication policy triggers the Duo Security Adapter, these files present the Duo Security authentication page.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following resources:

* [PingFederate](https://duo.com/docs/pingfederate) in the Duo Security documentation

* The following sections of the PingFederate documentation:

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

## System requirements

* PingFederate 8.0 or later

* A Duo Security administrator account

---

---
title: Duo Security Integration Kit 3.x
description: The Duo Security Integration Kit allows PingFederate to use Duo Universal Prompt for multi-factor authentication (MFA). This sign-on experience uses OpenID Connect standards and does not require or support iFrames.
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_3x:pf_duo_security_ik
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_3x/pf_duo_security_ik.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
section_ids:
  upgrade-considerations: Upgrade considerations
  features: Features
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Duo Security Integration Kit 3.x

The Duo Security Integration Kit allows PingFederate to use Duo Universal Prompt for multi-factor authentication (MFA). This sign-on experience uses OpenID Connect standards and does not require or support iFrames.

|   |                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This documentation is for Duo Security Integration Kit 3.0 and later. For earlier versions of the integration kit, see the [Duo Security Integration Kit 2.2](../duo_security_integration_kit_22/pf_duo_security_ik_22.html) documentation. |

## Upgrade considerations

The Duo Security Integration Kit 3.0 and later no longer support the [session state](../duo_security_integration_kit_22/pf_duo_security_ik_22_duo_security_adapter_settings_reference.html) feature or the adapter session feature. If you were using the adapter session feature previously, you can configure [Authentication sessions](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sessions.html) instead.

|   |                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The authentication sessions feature doesn't have complete feature parity with the adapter session feature. For example, the authentication sessions feature doesn't support session sharing between composite adapters. To use authentication sessions with the Duo Security Integration Kit 3.0 and later, remove any interfering composite adapters. |

## Features

* Supports Duo's Standard Editions and [Federal Editions](https://duo.com/docs/duo-federal-guide)

* Supports Duo's OpenID Connect-enabled APIs.

* Supports the [Duo Universal Prompt](https://help.duo.com/s/article/6340) authentication experience.

* Supports the PingFederate [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Supports the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

## Components

The Duo Security IdP Adapter:

* Allows PingFederate to redirect users to Duo Universal Prompt for a multi-factor authentication (MFA) challenge during sign on.

* Allows for MFA when single sign-on (SSO) is initiated at the identity provider (IdP) or service provider (SP).

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following resources:

* The following sections of the Duo Universal Prompt documentation:

  * [Getting Started with Duo Security](https://duo.com/docs/getting-started)

  * [What is the Duo Universal Prompt?](https://help.duo.com/s/article/6340)

  * [Application Options - Universal Prompt](https://duo.com/docs/protecting-applications//)

  * [Duo Universal Prompt Update Guide](https://duo.com/docs/universal-prompt-update-guide)

  * [Troubleshooting - Universal Prompt Update Progress](https://duo.com/docs/administration//)

  * [PingFederate](https://duo.com/docs/pingfederate)

* The following sections of the PingFederate documentation:

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

## System requirements

* PingFederate 10.3 or later

* A Duo Universal Prompt administrator account

---

---
title: Duo Security integrations
description: The latest Duo Security Integration Kit allows PingFederate to use Duo Universal Prompt for multi-factor authentication (MFA). This sign-on experience uses OpenID Connect standards and does not require iFrames.
component: duosecurity
page_id: duosecurity::pf_is_overview_of_duo_security_integrations
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/pf_is_overview_of_duo_security_integrations.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
section_ids:
  duo-security-integration-kit-latest: Duo Security Integration Kit (latest)
  duo-security-integration-kit-2-2: Duo Security Integration Kit 2.2
---

# Duo Security integrations

## Duo Security Integration Kit (latest)

The latest Duo Security Integration Kit allows PingFederate to use [Duo Universal Prompt](https://help.duo.com/s/article/6340) for multi-factor authentication (MFA). This sign-on experience uses OpenID Connect standards and does not require iFrames.

## Duo Security Integration Kit 2.2

This documentation is available for customers with existing deployments of Duo Security Integration Kit 2.2 and earlier. This sign-on experience uses an iFrame and works with the Duo Auth API.

This version of the Duo Security Integration Kit integrated with Duo MFA using a PingFederate-based template.

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_22:pf_duo_security_ik_22_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_22/pf_duo_security_ik_22_enabling_debug_logging.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.

## About this task

These steps are optional. For general information about logging, see [Enabling debug messages and console logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html) in the PingFederate documentation.

## Steps

1. Open the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file for editing.

2. If you want to log activity for PingFederate and all adapters, do the following.

   1. Find the following section.

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

3. If you want to log activity just for the Duo Security IdP Adapter, add the following line.

   ```html
   <Logger name="com.pingidentity.clientservices.product.integrationkit.duo" level="DEBUG"/>
   ```

4. Save the file.

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_3x:pf_duo_security_ik_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_3x/pf_duo_security_ik_enabling_debug_logging.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.

## About this task

These steps are optional. For general information about logging, see [Enabling debug messages and console logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html) in the PingFederate documentation.

## Steps

1. Open the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file for editing.

2. If you want to log activity for PingFederate and all adapters, do the following.

   1. Find the following section.

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

3. If you want to log activity just for the Duo Security IdP Adapter, add the following line.

   ```html
   <Logger name="com.pingidentity.clientservices.product.integrationkit.duo" level="DEBUG"/>
   ```

4. Save the file.

---

---
title: Getting your Duo Security keys and API hostname
description: To allow PingFederate to communicate with Duo Security, add it as a protected application.
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_22:pf_duo_security_ik_22_getting_your_duo_security_keys_and_api_hostname
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_22/pf_duo_security_ik_22_getting_your_duo_security_keys_and_api_hostname.html
llms_txt: https://docs.pingidentity.com/integrations/duosecurity/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
section_ids:
  steps: Steps
---

# Getting your Duo Security keys and API hostname

To allow PingFederate to communicate with Duo Security, add it as a protected application.

## Steps

1. Log into Duo Security as an administrator.

2. Go to **Applications > Protect an Application**. For **PingFederate**, click **Protect this Application.**

3. Note the **Client ID**, **Client Secret**, and **API hostname**. You will use these in [Configuring an adapter instance](pf_duo_security_ik_22_configuring_an_adapter_instance.html).

   ![Screen capture showing the positioning of the Client ID, Client Secret, and API hostname fields on the PingFederate page.](../_images/lzr1579652693781.jpg)