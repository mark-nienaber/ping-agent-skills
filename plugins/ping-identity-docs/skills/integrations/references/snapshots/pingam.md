---
title: Changelog
description: The following is the change history for the PingAM Integration Kit.
component: pingam
page_id: pingam:release_notes:pf_pingam_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/pingam/release_notes/pf_pingam_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 21, 2026
section_ids:
  pingam-integration-kit-1-4-may-2026: PingAM Integration Kit 1.4 - May 2026
  pingam-integration-kit-1-3-1-november-2025: PingAM Integration Kit 1.3.1 - November 2025
  pingam-integration-kit-1-3-october-2025: PingAM Integration Kit 1.3 - October 2025
  pingam-integration-kit-1-2-february-2025: PingAM Integration Kit 1.2 - February 2025
  pingam-integration-kit-1-1-november-2024: PingAM Integration Kit 1.1 – November 2024
  pingam-integration-kit-1-0-august-2024: PingAM Integration Kit 1.0 – August 2024
---

# Changelog

The following is the change history for the PingAM Integration Kit.

## PingAM Integration Kit 1.4 - May 2026

* Added the ability to indicate that an attribute in the Journey Response Mappings is multi-valued.\
  Learn more in step 5d of [Configuring an adapter instance](../setup/pf_pingam_ik_configuring_an_adapter_instance.html).

* Added the **Always Authenticate User** option to authenticate the user with a PingAM Journey.

## PingAM Integration Kit 1.3.1 - November 2025

* Fixed an issue that caused PingFederate to not send a username value to PingAM when using backchannel authentication.

  A new tracked HTTP request parameter called `username` is now available. Entering `login_hint` as the **Source Parameter** in step 4d of [Configuring an adapter instance](../setup/pf_pingam_ik_configuring_an_adapter_instance.html) prompts PingFederate to send the username value to PingAM as a string.

## PingAM Integration Kit 1.3 - October 2025

* Username validation only occurs once now. If validation fails, the adapter encounters an error.

* The `redirect_uri` no longer includes any additional parameters. Learn more in [Known issues and limitations](pf_pingam_ik_known_issues_and_limitations.html).

## PingAM Integration Kit 1.2 - February 2025

* Added the ability to use backchannel communication with PingAM to pass data from PingFederate to PingAM securely.

  To send PingFederate parameters to PingAM, you must create an OAuth client in PingAM and update the PingAM IdP Adapter configuration with the associated **Client ID** and **Client Secret**.

  Learn more in step 6 of [Preparing to use a PingAM journey](../setup/pf_pingam_ik_using_pingam_journey.html) and refer to the **Client ID** and **Client Secret** table entries in [PingAM IdP Adapter settings reference](../setup/pf_pingam_ik_pingam_idp_adapter_settings_reference.html).

* Added the ability to configure whether the PingAM session should be deleted after a user signs off from the protected application.

  Learn more in the **Logout Mode** table entry in the [PingAM IdP Adapter settings reference](../setup/pf_pingam_ik_pingam_idp_adapter_settings_reference.html).

## PingAM Integration Kit 1.1 – November 2024

* Added the ability to track PingFederate and PingAM transactions using a unique request ID that's set by the adapter. This enhances the application log debugging experience. You can find configuration instructions in [Tracking transactions between PingFederate and PingAM](../troubleshooting/pf_pingam_ik_tracking_transactions.html).

* Added the ability to perform username validation. To do so, configure the [Username Path](../setup/pf_pingam_ik_pingam_idp_adapter_settings_reference.html) between the username that the adapter receives from the authentication policy and a value in the PingAM session info payload.

* Fixed an issue that caused an infinite loop between PingFederate and PingAM if the PingAM and adapter cookie name values didn't match. The adapter now fails if it doesn't receive the expected cookie name from PingAM.

## PingAM Integration Kit 1.0 – August 2024

* Initial release

---

---
title: Collecting session data from PingAM
description: Get session data from a PingAM journey (tree) to use in PingFederate.
component: pingam
page_id: pingam:setup:pf_pingam_ik_collecting_session_data_from_pingam
canonical_url: https://docs.pingidentity.com/integrations/pingam/setup/pf_pingam_ik_collecting_session_data_from_pingam.html
llms_txt: https://docs.pingidentity.com/integrations/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 2, 2024
section_ids:
  steps: Steps
---

# Collecting session data from PingAM

Get session data from a PingAM journey (tree) to use in PingFederate.

## Steps

1. Create a script to collect the desired session data from the PingAM journey that you specified in the [adapter settings](pf_pingam_ik_pingam_idp_adapter_settings_reference.html):

   1. In the PingAM administrative console, go to the realm that the journey is in, then go to **Scripts** and click **[icon: plus, set=fa]New Script**.

   2. In the **Name** field, give the script a meaningful name.

   3. In the **Description** field, give the script a meaningful description.

   4. In the **Script Type** list, select **Decision node script for authentication trees**.

   5. In the **Language** section, select **JavaScript**.

   6. In the **Evaluator Version** section, confirm that the value is **Legacy**.

   7. In the **Script** field, enter the following sample code.

      |   |                                                                                                                                                                                                                                       |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The following script sets the username, email and telephone number attributes that PingAM stores as part of authentication. Use this script as a starting point for the session data that you want to make available to PingFederate. |

      ```javascript
      /*
      - Data made available by nodes that have already executed are available in the sharedState variable.
      - The script should set outcome to either "true" or "false".
      - Note: This script is not fault-tolerant. It is simply meant to give an idea of how script nodes may be used.
      */

      var fr = JavaImporter(org.forgerock.openam.auth.node.api.Action);

      var userId = nodeState.get("username").asString();

      // lookup attributes by LDAP attribute name
      var mail = idRepository.getAttribute(userId, "mail").iterator().next();
      var telephoneNumber = idRepository.getAttribute(userId, "telephoneNumber").iterator().next();

      // for each attribute, add the 'putSessionProperty' method
      action = fr.Action.goTo("true").putSessionProperty("am.protected.sessionUsername", userId)
      .putSessionProperty("am.protected.mail", mail)
      .putSessionProperty("am.protected.telephoneNumber", telephoneNumber)
      .build();

      outcome = "true";
      ```

   8. Click **Validate**.

2. Use the script in the authentication journey:

   |   |                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------- |
   |   | This procedure assumes that the mail, username, and telephone number attributes are available from a previous node in the journey. |

   1. Go to **Authentication > Trees** and open the journey that's being used in the adapter.

   2. Drag the **Scripted Decision** node onto the journey.

   3. Select the **Scripted Decision** node and give the node a meaningful name.

   4. In the **Script** list, select the script that you created in the previous step.

   5. In the **Outcomes** field, enter `true`. Press Enter.

   6. Connect the `True` outcome of the **DataStore Decision** node to the **Scripted Decision** node.

   7. Connect the `True` outcome of the **Scripted Decision** node to the **Success** node.

   8. Click **Save**.

3. Add the properties that the script sets in the session to the allow list:

   1. In the PingAM administrative console, go to **Services**.

   2. Add or edit the **Session Property Whitelist Service**. To add this service:

      1. Click **[icon: plus, set=fa]Add a Service**.

      2. In the **Choose a service type** list, search for `Session Property Whitelist Service` and select it in the list.

   3. On the **Session Property Whitelist Service** page, in the **Allowlisted Session Property Names** field, add the following properties:

      * `am.protected.sessionUsername`

      * `am.protected.mail`

      * `am.protected.telephoneNumber`

   4. Click **Save Changes**.

4. Map the user attributes that you set in the script to their session attribute equivalents:

   1. Go to **Authentication > Settings** and click the **Post Authentication Processing Settings** tab.

   2. In the **User Attribute Mapping to Session Attribute** field, add the following attribute mappings:

      * `mail|mail`

      * `username|sessionUsername`

      * `telephoneNumber|telephoneNumber`

   3. Click **Save Changes**.

5. Test the user journey.

---

---
title: Configuring an adapter instance
description: Configure the PingAM IdP Adapter to determine how PingFederate communicates with PingAM.
component: pingam
page_id: pingam:setup:pf_pingam_ik_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/pingam/setup/pf_pingam_ik_configuring_an_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 21, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Configuring an adapter instance

Configure the PingAM IdP Adapter to determine how PingFederate communicates with PingAM.

## About this task

To begin the integration, deploy the PingAM Integration Kit files to your PingFederate directory.

## Steps

1. In the PingFederate administrative console, go to **Authentication > Integration > IdP Adapters** and click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **PingAM IdP Adapter**. Click **Next**.

3. (Optional) On the **IdP Adapter** tab, in the **Simple Parameter Mappings** section, select pre-defined parameters to send from PingFederate to PingAM.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | * If you have [configured an OAuth client in PingAM](pf_pingam_ik_using_pingam_journey.html) and provided the [**Client ID** and **Client Secret**](pf_pingam_ik_pingam_idp_adapter_settings_reference.html), the adapter sends your **Simple Parameter Mappings** and **Advanced Parameter Mappings** to PingAM.

     In PingAM, you can access these parameters by configuring your flow's input schema to expect the **Parameter Name** values you define in steps 3b and 4b.

   * You can find more information about other input parameter options in the [Parameter reference](https://download.pingidentity.com/public/documentation/pingfederate/11.0/sdkdoc/index.html?com/pingidentity/sdk/IdpAuthenticationAdapterV2.html) in the PingFederate SDK documentation and [Extended properties](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_extended_properti.html) in the PingFederate documentation. |

   1. Click **Add a new row to 'Simple Parameter Mappings (optional)'**.

   2. In the **Parameter Name** field, enter a key name to use when sending the parameter to PingAM.

      For example, `appName`.

   3. In the **Source** list, select the pre-defined parameter you want to send.

      For example, **Application Name**.

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a - d.

4. (Optional) On the **IdP Adapter** tab, in the **Advanced Parameter Mappings** section, define custom parameters to send from PingFederate to PingAM.

   1. Click **Add a new row to 'Advanced Parameter Mappings (optional)'**.

   2. In the **Parameter Name** field, enter a key name to use when sending the parameter to PingAM.

      For example, `trackedParameters`.

   3. In the **Source Type** list, select the type of parameter you want to send.

      For example, **Tracked HTTP Request Parameters**.

      The following options are available:

      * Chained attributes

        The attributes that are made available by the other adapters and selectors in your PingFederate authentication policy.

      * Extended properties

        These parameters store additional information about connections, OAuth clients, or both. You can find more detail in [Extended properties](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_extended_properti.html) in the PingFederate documentation.

      * Request claims

        The claims PingFederate received within an OAuth/OpenID Connect Request Object or the parameters of a pushed authorization request.

      * Tracked HTTP request parameters

        The tracked HTTP request parameters that were included in the initial HTTP request of the current transaction.

   4. In the **Source Parameter** field, enter the exact name of the parameter that you want to send to PingAM. The parameter must be available to the adapter from the **Source Type** that you selected.

      Leave this field empty to send all parameters of the **Source Type**.

   5. In the **Action** column, click **Update**.

   6. To add more attributes, repeat steps a - e.

5. (Optional) On the **IdP Adapter** tab, in the **Journey Response Mappings** section, map attributes from the PingAM response to the attribute contract:

   1. Click **Add a new row to 'Journey Response Mappings (optional)'**.

   2. In the **Local Attribute** field, enter a name of your choosing for an attribute.

   3. In the **Journey Attribute Mapping** field, map the local attribute to a remote attribute using JSON pointer syntax.

      Learn more about JSON pointer syntax in [RFC 6901](https://datatracker.ietf.org/doc/html/rfc6901).

   4. If the attribute is multi-valued, select the **Multi-Valued Attribute** check box.

   5. In the **Action** column, click **Update**.

   6. To add more attributes, repeat steps a - e.

      These attributes become available in your PingFederate authentication policy.

6. On the **IdP Adapter** tab, configure the adapter instance by referring to [PingAM IdP Adapter settings reference](pf_pingam_ik_pingam_idp_adapter_settings_reference.html). Click **Next**.

7. On the **Extended Contract** tab, add any attributes that you included in the **PingAM Response Mappings** section of the **IdP Adapter** tab. Click **Next**.

8. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

9. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

10. On the **Summary** tab, review your configuration. Click **Save**.

## Next steps

Review [Preparing to use a PingAM journey](pf_pingam_ik_using_pingam_journey.html).

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the PingAM Integration Kit files to your PingFederate directory.
component: pingam
page_id: pingam:setup:pf_pingam_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/pingam/setup/pf_pingam_ik_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  next-steps: Next steps
---

# Deploying the integration files

To get started with the integration, deploy the PingAM Integration Kit files to your PingFederate directory.

## Before you begin

You must sign up for a PingAM account.

## Steps

1. Download the PingAM Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/pingam-integration-kit).

2. Stop PingFederate, if it's running.

3. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Start PingFederate.

5. If you operate PingFederate in a cluster, repeat steps 2 - 4 for each engine node.

## Next steps

[Configure an adapter instance](pf_pingam_ik_configuring_an_adapter_instance.html).

---

---
title: Download manifest
description: The following files are included in the PingAM Integration Kit .zip archive.
component: pingam
page_id: pingam:release_notes:pf_pingam_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/pingam/release_notes/pf_pingam_ik_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2024
---

# Download manifest

The following files are included in the PingAM Integration Kit `.zip` archive.

* `Legal.pdf` – Copyright and license information

* `dist/pingfederate/server/default` – Contains the integration files

  * `deploy` – Contains the Java libraries

    * `pf-pingam-integration-kit-<version>.jar` – The PingAM IdP Adapter

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for PingFederate, the PingAM IdP Adapter, or both.
component: pingam
page_id: pingam:troubleshooting:pf_pingam_ik_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/pingam/troubleshooting/pf_pingam_ik_enabling_debug_logging.html
llms_txt: https://docs.pingidentity.com/integrations/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for PingFederate, the PingAM IdP Adapter, or both.

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

3. To log activity relating to the PingAM IdP Adapter:

   ### Choose from:

   * To log activity for the PingAM IdP Adapter as well as its HTTPS and component activity, add the following line:

     ```html
     <Logger name="com.pingidentity.adapters.pingam" level="DEBUG"/>
     ```

   * To log activity for the adapter's HTTPS activity and other components but not for the adapter itself, add the following line:

     ```html
     <Logger name="com.pingidentity.adapters.pingam.shade" level="DEBUG"/>
     ```

   * To log activity for the PingAM IdP Adapter but not its HTTPS or component activity, add the following lines:

     ```html
     <Logger name="com.pingidentity.adapters.pingam" level="DEBUG"/>
     <Logger name="com.pingidentity.adapters.pingam.shade" level="INFO"/>
     ```

4. Save the file.

---

---
title: Extracting data from PingFederate
description: Extract data collected from PingFederate through the simple and advanced parameter mappings to use in a PingAM journey (tree).
component: pingam
page_id: pingam:setup:pf_pingam_ik_extracting_data_from_pf
canonical_url: https://docs.pingidentity.com/integrations/pingam/setup/pf_pingam_ik_extracting_data_from_pf.html
llms_txt: https://docs.pingidentity.com/integrations/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 12, 2025
section_ids:
  steps: Steps
---

# Extracting data from PingFederate

Extract data collected from PingFederate through the [simple and advanced parameter mappings](pf_pingam_ik_configuring_an_adapter_instance.html) to use in a PingAM journey (tree).

## Steps

1. Create a script to extract data coming from PingFederate into the PingAM journey that you specified in the [adapter settings](pf_pingam_ik_pingam_idp_adapter_settings_reference.html):

   1. In the PingAM administrative console, go to the realm that the journey is in, then go to **Scripts** and click **[icon: plus, set=fa]New Script**.

   2. In the **Name** field, give the script a meaningful name.

   3. In the **Description** field, give the script a meaningful description.

   4. In the **Script Type** list, select **Decision node script for authentication trees**.

   5. In the **Language** section, select **JavaScript**.

   6. In the **Evaluator Version** section, confirm that the value is **Legacy**.

   7. In the **Script** field, enter the following sample code.

      |   |                                                                                                                                            |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | Use this script as a starting point. In this example, the data sent from PingFederate is configured with the **Parameter Name** `appName`. |

      ```javascript
      /*
      - Data made available by nodes that have already executed are available in the sharedState variable.
      - The script should set outcome to either "true" or "false".
      */

      var fr = JavaImporter(org.forgerock.openam.auth.node.api.Action);

      var pfApplicationName = nodeState.get("appName").asString();

      logger.error("The PingFederate application name passed in is {}", pfApplicationName);

      //for each attribute, add the 'putSessionProperty' method
      action = fr.Action.goTo("true").putSessionProperty("am.pf.appName", pfApplicationName)
      .build();

      outcome = "true";
      ```

   8. Click **Validate**.

2. Use the script in the authentication journey:

   1. Go to **Authentication > Trees** and open the journey that's being used in the adapter.

   2. Drag the **Scripted Decision** node onto the journey.

   3. Select the **Scripted Decision** node and give the node a meaningful name.

   4. In the **Script** list, select the script that you created in the previous step.

   5. In the **Outcomes** field, enter `true`. Press Enter.

   6. Connect the `True` outcome of the **DataStore Decision** node to the **Scripted Decision** node.

   7. Connect the `True` outcome of the **Scripted Decision** node to the **Success** node.

   8. Click **Save**.

3. Add the properties that the script sets in the session to the allow list:

   1. In the PingAM administrative console, go to **Services**.

   2. Add or edit the **Session Property Whitelist Service**. To add this service:

      1. Click **[icon: plus, set=fa]Add a Service**.

      2. In the **Choose a service type** list, search for `Session Property Whitelist Service` and select it in the list.

   3. On the **Session Property Whitelist Service** page, in the **Allowlisted Session Property Names** field, add the properties that you set in the script:

      For example:

      * `am.pf.appName`

   4. Click **Save Changes**.

4. Test the user journey.

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the PingAM Integration Kit.
component: pingam
page_id: pingam:release_notes:pf_pingam_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/pingam/release_notes/pf_pingam_ik_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 21, 2026
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the PingAM Integration Kit.

## Known issues

There aren't any known issues.

## Known limitations

* The adapter doesn't support the PingFederate authentication API because it isn't feasible to generate verified access challenge response values externally.

* PingAM Integration Kit 1.2 and later require PingAM 8.0.

* As of PingAM Integration Kit 1.2, the adapter uses an OAuth client to do backchannel authentication. Learn more in [Changelog](pf_pingam_ik_changelog.html).

* As of PingAM Integration Kit 1.3, if you haven't configured OAuth credentials, the adapter encounters an error if you try to configure simple or advanced parameters.

* As of PingAM Integration Kit 1.4, the **Always Authenticate User** option is not supported when OAuth credentials are enabled.

---

---
title: Overview of the SSO flow
description: The following figure illustrates an example single sign-on (SSO) process flow.
component: pingam
page_id: pingam::pf_pingam_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/pingam/pf_pingam_ik_overview_of_the_sso_flow.html
llms_txt: https://docs.pingidentity.com/integrations/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 12, 2025
---

# Overview of the SSO flow

The following figure illustrates an example single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* process flow.

![A diagram illustrating a typical sign on process leveraging the integration kit.](_images/PingAM_SSO_Flow.png)

In summary:

1. A user initiates the sign-on process by requesting access to a protected resource.

2. If PingFederate detects that the PingAM cookie is not present, it gets an access token using the OAuth credentials, then initializes a backchannel authentication using the access token, and uses the redirect URI returned to send the user to orchestrate authentication. It also appends a PingFederate URL as a request parameter to resume the flow post-login.

   If a session cookie is present, PingFederate makes a backchannel request to get session information from PingAM.

3. On a success, PingFederate extracts session information from the JSON response provided by PingAM and generates a SAML assertion.

4. PingFederate redirects the user to the protected resource and configures the SAML assertion. The user is granted access.

---

---
title: PingAM IdP Adapter settings reference
description: Field descriptions for the PingAM IdP Adapter configuration screen.
component: pingam
page_id: pingam:setup:pf_pingam_ik_pingam_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/pingam/setup/pf_pingam_ik_pingam_idp_adapter_settings_reference.html
llms_txt: https://docs.pingidentity.com/integrations/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 21, 2026
---

# PingAM IdP Adapter settings reference

Field descriptions for the PingAM IdP Adapter configuration screen.

> **Collapse: Standard Fields**
>
> | Field             | Description                                                                                                                                                                                                                                                                                                                                                                              |
> | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Base URL**      | The PingAM base URL, including context for the sign-on redirect. For example:`https://am.example.com/am`                                                                                                                                                                                                                                                                                 |
> | **Realm**         | The PingAM Realm to call. For example:`alpha`                                                                                                                                                                                                                                                                                                                                            |
> | **Journey**       | The PingAM Journey or Tree to call. For example:`Login`                                                                                                                                                                                                                                                                                                                                  |
> | **Cookie Name**   | The PingAM session cookie name. For example:`iPlanetDirectoryPro`                                                                                                                                                                                                                                                                                                                        |
> | **Client ID**     | The `Client ID` defined in PingAM for backchannel authentication.If this field is left blank, the adapter uses the PingAM Integration Kit 1.1 authentication mechanism and logs a warning in the PingFederate server log.	This field is required, if you want to use backchannel communication to send PingFederate data to PingAM.                                                      |
> | **Client Secret** | The `Client Secret` defined in PingAM for backchannel authentication.If this field is left blank, the adapter uses the PingAM Integration Kit 1.1 authentication mechanism and logs a warning in the PingFederate server log.	This field is required if you want to use backchannel communication to send PingFederate data to PingAM.                                                   |
> | **Logout Mode**   | Define handling for application sign off. Select one of the following options:- PingAM
>
>   PingFederate sends a sign-off request to PingAM after a user signs off from the protected application. This deletes the PingAM session.
>
> - None
>
>   PingFederate doesn't send a sign-off request to PingAM after a user signs off from the protected application.The default value is `PingAM`. |

> **Collapse: Advanced Fields**
>
> | Field                        | Description                                                                                                                                                                                                                                                                           |
> | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Username Path**            | The JSON Pointer path that indicates the location of the username in the payload that PingAM returns. If you set a **Username Path**, the adapter validates this value against the incoming user ID that it receives from the authentication policy.The default value is `/username`. |
> | **API Request Timeout**      | The amount of time in milliseconds that PingFederate waits for PingAM to respond to requests and connection establishment. A value of `0` disables the timeout.The default value is `5000`.                                                                                           |
> | **Always Authenticate User** | Enable this option to authenticate the user with PingAM Journey.                                                                                                                                                                                                                      |
> | **Proxy Settings**           | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                                                                           |
> | **Custom Proxy Host**        | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                        |
> | **Custom Proxy Port**        | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                             |

---

---
title: PingAM Integration Kit
description: The PingAM Integration Kit allows PingFederate to communicate with PingAM and provide a rich sign-on orchestration experience.
component: pingam
page_id: pingam::pf_pingam_ik
canonical_url: https://docs.pingidentity.com/integrations/pingam/pf_pingam_ik.html
llms_txt: https://docs.pingidentity.com/integrations/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 23, 2025
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# PingAM Integration Kit

The PingAM Integration Kit allows PingFederate to communicate with PingAM and provide a rich sign-on orchestration experience.

|   |                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The ForgeRock Intelligent Access Integration Kit and the PingAM Integration Kit use different adapters, so it isn't possible to upgrade from one to the other. Going forward, enhancements will only be added to the PingAM Integration Kit. |

PingAM can deploy at scale and across any platform. It's a software as a service (SaaS) application with self-managed options for:

* Public cloud deployment

* Private cloud deployment

* On-premises virtual machine deployment

* Bare metal server deployment

PingFederate outsources user sign-on experience to PingAM.

## Components

* PingAM IdP Adapter

  * When a user signs on through PingFederate, the adapter validates whether there's a valid session cookie and whether it needs to create a new session with PingAM.

## Intended audience

This document is intended for PingFederate administrators. If you need help during the setup process, learn more in the following resources:

* [Step 3. Deploy AM](https://docs.pingidentity.com/pingam/latest/evaluation/step-3-deploy-am.html) in the PingAM documentation.

## System requirements

* PingFederate 11.3 or later.

* PingAM Integration Kit 1.2 or later (requires PingAM 8.0 or later).

* You must deploy PingFederate and PingAM on the same cookie domain because the current implementation relies on the presence and validation of a PingAM single sign-on (SSO) *(tooltip: \<div class="paragraph">
  \<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
  \</div>)* cookie.

---

---
title: Preparing to use a PingAM journey
description: To use a PingAM journey, you must install PingAM and perform the additional configuration steps described in this document.
component: pingam
page_id: pingam:setup:pf_pingam_ik_using_pingam_journey
canonical_url: https://docs.pingidentity.com/integrations/pingam/setup/pf_pingam_ik_using_pingam_journey.html
llms_txt: https://docs.pingidentity.com/integrations/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 23, 2025
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  example: Example:
---

# Preparing to use a PingAM journey

To use a PingAM journey, you must install PingAM and perform the additional configuration steps described in this document.

## Before you begin

Complete the steps in the PingAM installation [guide](https://docs.pingidentity.com/pingam/latest/installation/preface.html).

## About this task

In the PingAM admin console:

## Steps

1. If you don't have an alpha realm in your environment yet:

   1. Go to **Realms** and click **New Realm**.

   2. In the **Name** field, enter `alpha`.

   3. Click **Use Client-Side Sessions**.

   4. Click **Create** to save your configuration.

      |   |                                                                                                                                                                                                                                                                                    |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You should have an alpha realm because it's best practice to reserve the root realm for administrative operations. Learn more about configuring a realm in [create a new realm](https://docs.pingidentity.com/pingam/latest/setup/configure-realms-console.html#create-new-realm). |

2. Configure client-side sessions by completing the steps in the [configure client-side sessions](https://docs.pingidentity.com/pingam/latest/am-sessions/impl-client-based-sessions.html) procedure.

3. Enable goto and redirects for the validation service.

   By default, PingAM denies all goto and redirects after the sign on flow is complete.

   1. In the alpha realm, go to **Services**.

   2. If the **Validation Service** is not in the list of services, click **Add a Service** and in the **Choose a service type** list, select **Validation Service.**

   3. In the **Valid goto URL Resources** field, enter one or more valid URL patterns to allow.

      ### Example:

      * `https://<my_ping_federate_url>:*/*`

      * `https://<my_ping_federate_url>:*/*?*`

4. Configure push authentication journeys by completing the steps in the [push authentication journeys guide](https://docs.pingidentity.com/pingam/latest/am-authentication/authn-mfa-trees-push.html).

5. (Optional) To adjust authentication session lifetimes:

   1. In the alpha realm, go to **Services**, click **Session**, then click **Create**.

   2. On the **Dynamic Attributes** tab, enter the desired values in the **Maximum Session Time** and **Maximum Idle Time** fields.

   3. Click **Save Changes**.

      Learn more in [Configure authenticated session timeout settings](https://docs.pingidentity.com/pingam/latest/am-sessions/session-state-session-termination.html#auth-session-termination-config).

6. If you're using PingAM Integration Kit 1.2 or later, create an OAuth client as described in [Create a client profile](https://docs.pingidentity.com/pingam/latest/am-oauth2/oauth2-register-client.html#configure-oauth2-client-profile) in the PingAM documentation.

   1. In the **Core** section, make sure to set the `write` and `back_channel_authentication` scopes.

   2. In the **Advanced** section, make sure to configure the [`Client Credentials`](https://docs.pingidentity.com/pingam/latest/am-oauth2/oauth2-client-cred-grant.html) grant type, and that the **Token Endpoint Authentication Method** is using `client_secret_basic`.

---

---
title: Tracking transactions between PingFederate and PingAM
description: To help with application log debugging, you can track PingFederate and PingAM transactions using a unique request ID that's set by the adapter.
component: pingam
page_id: pingam:troubleshooting:pf_pingam_ik_tracking_transactions
canonical_url: https://docs.pingidentity.com/integrations/pingam/troubleshooting/pf_pingam_ik_tracking_transactions.html
llms_txt: https://docs.pingidentity.com/integrations/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Tracking transactions between PingFederate and PingAM

To help with application log debugging, you can track PingFederate and PingAM transactions using a unique request ID that's set by the adapter.

## About this task

PingFederate and PingAM both have methods to keep track of transactions across multiple applications:

* In PingFederate, the `httprequestid` can be used to track transactions that come from outside PingFederate.

* In PingAM, the [`X-ForgeRock-TransactionId` header](https://docs.pingidentity.com/pingam/latest/am-rest/rest-intro.html#x_forgerock_transactionid) tracks related requests throughout the ForgeRock platform.

To track transactions between PingFederate and PingAM, the PingAM IdP Adapter injects the `X-ForgeRock-TransactionId` header with the `httprequestid` value in all API calls to PingAM.

Complete the following procedure to finish the setup in PingAM and see the unique request ID in the audit logs:

## Steps

1. To see the value set for `httprequestid` in the `X-ForgeRock-TransactionId` header, configure PingFederate to log the `httprequestid`:

   1. In the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file, go to the `SecurityAudit2File` RollingFile and add the **httprequestid** field in the **Pattern** section.

      Learn more in [PingFederate security audit logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_security_audit_logging.html) and the [PingFederate log files](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_pf_log_files.html) section of the PingFederate documentation.

   2. Save the file.

2. Configure PingAM to accept the `X-ForgeRock-TransactionId` header:

   1. In the PingAM admin UI, go to **Configure > Server Defaults > Advanced** and go to the bottom of the list.

   2. In the **Property Name** column, enter `org.forgerock.http.TrustTransactionHeader`.

   3. In the corresponding **Property Value** column, enter `true`.

   4. To add the property and save your work, click the **+** icon.

### Result

You can now track the unique request ID between PingFederate and PingAM in the PingFederate security audit log and the PingAM access audit log.