---
title: Adjusting the OIDC policy configuration
description: Adjust the OIDC policy configuration to include the access token manager (ATM) and attributes you've configured.
component: microsoft-eam
page_id: microsoft-eam:setup:pf_ms_eam_adjusting_the_oidc_policy_configuration
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/setup/pf_ms_eam_adjusting_the_oidc_policy_configuration.html
revdate: September 17, 2025
section_ids:
  steps: Steps
---

# Adjusting the OIDC policy configuration

Adjust the OIDC policy configuration to include the access token manager (ATM) and attributes you've configured.

You can find more information in the [Configuring OpenID Connect policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_oidc_policies.html) section of the PingFederate documentation.

## Steps

1. Go to **Applications > OpenID Connect Policy Management** and open the policy configuration you plan to use.

2. On the **Manage Policy** tab:

   1. Make sure that you've configured a unique **Policy ID** and **Name**.

   2. In the **Access Token Manager** list, select the ATM you configured in [Configuring an access token manager](pf_ms_eam_configuring_an_atm.html).

   3. Select the **Include x.509 Thumbprint Header in ID token** checkbox.

      This configures the OIDC policy to expose the X5T header when PingFederate issues the `id_token` for Microsoft Entra ID.

   You can find more configuration information in [configuring policy and ID token settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_policymanagementtasklet_policymanagementstate.html) in the PingFederate documentation.

3. On the **Attribute Contract** tab, make sure that the attribute contract includes `acr`, `amr`, and any optional attributes you configured into the issued id\_token:

   1. In the **Extend the Contract** section, enter `acr`.

   2. In the **Action** column, click **Add**.

   3. Repeat this process for `amr` and any optional attributes that you extended the contract for in step 4 of [Configuring an adapter instance](pf_ms_eam_configuring_an_adapter_instance.html).

   4. Click **Next**.

   You can find more information about configuration options in [Configuring the policy attribute contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_policymanagementtasklet_createpolicycontractstate.html) in the PingFederate documentation.

4. On the **Attribute Scopes** tab, make sure that the `acr` and `amr` attributes, plus any optional attributes, are returned with the `openid` scope:

   1. In the **Scope** list, select **openid**.

   2. In the **Attributes** section, select the checkboxes for `acr`, `amr`, and any optional attributes that you configured.

   3. In the **Action** column, click **Add**.

   4. Click **Next**.

   You can find more information about configuration options in [Configuring attribute scopes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_policymanagementtasklet_attributescopesstate.html) in the PingFederate documentation.

5. On the **Attribute Sources & User Lookup** tab, click **Next**.

6. On the **Contract Fulfillment** tab, fulfill the attribute contract for `acr`, `amr`, `sub`, and any optional attributes that you configured.

   For example, to configure contract fulfillment for the `acr` attribute:

   1. In the **Source** list, select **Access Token**.

   2. In the **Value** list, select **acr**.

   3. Repeat for `amr`, `sub`, and any optional attributes that you extended the contract for in step 4 of [Configuring an adapter instance](pf_ms_eam_configuring_an_adapter_instance.html).

      * For the `amr` attribute, in the **Source** list, select **Access Token**, and in the **Value** list, select **amr**.

      * For the `sub` attribute, in the **Source** list, select **Persistent Grant**, and in the **Value** list, select `USER_KEY`.

   4. Click **Next**.

   You can find more information about configuration options in [Configuring ID token fulfillment](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_policymanagementtasklet_policycontractmappingstate.html) in the PingFederate documentation.

7. (Optional) On the **Issuance Criteria** tab, configure the criteria for use with this OIDC policy.

   You can find more information about configuration options in [Defining issuance criteria for policy mapping](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_policymanagementtasklet_policyissuancecriteriastate.html) in the PingFederate documentation.

8. On the **Summary** tab, click **Save**.

---

---
title: Changelog
description: The following is the change history for the Microsoft EAM Integration Kit.
component: microsoft-eam
page_id: microsoft-eam:release_notes:pf_ms_eam_changelog
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/release_notes/pf_ms_eam_changelog.html
revdate: August 27, 2025
section_ids:
  microsoft-eam-integration-kit-1-1-september-2025: Microsoft EAM Integration Kit 1.1 – September 2025
  microsoft-eam-integration-kit-1-0-october-2024: Microsoft EAM Integration Kit 1.0 – October 2024
---

# Changelog

The following is the change history for the Microsoft EAM Integration Kit.

## Microsoft EAM Integration Kit 1.1 – September 2025

* Added advanced configuration fields to specify Issuer URI and JWKS URI values that were previously hardcoded. Learn more in [Microsoft EAM IdP Adapter settings reference](../setup/pf_ms_eam_adapter_settings_ref.html).

## Microsoft EAM Integration Kit 1.0 – October 2024

* Initial release

---

---
title: Configuring a PingFederate authentication policy
description: Configure a PingFederate authentication policy using the Microsoft EAM IdP Adapter and a downstream MFA adapter such as PingID.
component: microsoft-eam
page_id: microsoft-eam:setup:pf_ms_eam_configuring_a_pf_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/setup/pf_ms_eam_configuring_a_pf_authentication_policy.html
revdate: August 27, 2025
section_ids:
  steps: Steps
---

# Configuring a PingFederate authentication policy

Configure a PingFederate authentication policy using the Microsoft EAM IdP Adapter and a downstream MFA adapter such as PingID.

Learn more in the [Policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/qmq1564002987890.html) section of the PingFederate documentation.

## Steps

1. Go to **Authentication > Policies** and click **Add Policy**.

2. In the **Name** field, give the policy a unique name.

3. Configure the Microsoft EAM IdP Adapter as the first step and the PingID adapter as the second step in the policy:

   1. In the **Policy** list, select **IdP Adapters**, then select the EAM adapter instance you configured in [Configuring an adapter instance](pf_ms_eam_configuring_an_adapter_instance.html).

   2. In the **Fail** section, click **Done**.

   3. In the **Success** list, select **IdP Adapters**, then select the PingID adapter instance you configured.

4. Configure the PingID adapter step:

   1. In the **Fail** section, click **Done**.

   2. In the **Success** list, select **Policy Contracts**, then select a policy contract you've configured.

      Learn more in [Applying policy contracts or identity profiles to authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_apply_policy_contract_or_ident_profile_to_auth_policies.html) in the PingFederate documentation.

5. If the PingID adapter follows the Microsoft EAM IdP Adapter in the authentication policy, set the Microsoft EAM IdP Adapter's `sub` attribute as the `User ID Authenticated` for PingID:

   1. On the PingID adapter step, click **Options**.

   2. In the **Source** list, select the Microsoft EAM IdP Adapter.

   3. In the **Attribute list**, select `sub`.

   4. Select the **User ID Authenticated** checkbox.

   5. Click **Done**.

6. If the PingID adapter follows the Microsoft EAM IdP Adapter in the authentication policy and the flow ends in a policy contract, select PingID's `amr` attribute as the **Source** for the **Contract Mapping**:

   1. On the policy contract step, click **Contract Mapping**.

   2. On the **Attribute Sources & User Lookup** tab, click **Next**.

   3. On the **Contract Fulfillment** tab:

      1. For the `acr` attribute, in the **Source** list, select the EAM adapter instance. In the **Value** list, select `acr`.

      2. For the `amr` attribute, in the **Source** list, select the PingID adapter instance. In the **Value** list, select `amr`.

      3. For the `subject` attribute, in the **Source** list, select the EAM adapter instance. In the **Value** list, select `sub`.

   4. On the **Issuance Criteria** tab, click **Next**.

   5. On the **Summary** tab, click **Done**.

   Learn more in [configuring contract mapping](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_contract_mapping.html).

7. Check your configuration, then click **Done**.

---

---
title: Configuring an access token manager
description: Configure an access token manager (ATM).
component: microsoft-eam
page_id: microsoft-eam:setup:pf_ms_eam_configuring_an_atm
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/setup/pf_ms_eam_configuring_an_atm.html
revdate: August 28, 2025
section_ids:
  steps: Steps
  creating-access-token-mappings: Creating access token mappings
  steps-2: Steps
---

# Configuring an access token manager

Configure an access token manager (ATM).

Learn more in the [Access token management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_access_token_management.html) section of the PingFederate documentation.

## Steps

1. Go to **Applications > Access Token Management** and open an existing ATM configuration or click **Create New Instance**.

2. On the **Type** tab:

   1. Enter a unique **Instance Name** and **Instance ID**.

   2. In the **Type** list, select **JSON Web Tokens**.

   3. Click **Next**.

3. On the **Instance Configuration** tab:

   1. In the **JWS Algorithm** list, select the RSA key type that you configured in [Enabling signing keys](pf_ms_eam_enabling_signing_keys.html).

   2. Select the **Use Centralized Signing Key** checkbox or, in the **Active Signing Certificate Key ID** list, select the **Active Signing Certificate** that you configured in [Enabling signing keys](pf_ms_eam_enabling_signing_keys.html).

   You can find more information about instance configuration options on the JSON token management tab in [Configuring an access token management instance](https://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/pf_configuring_access_token_management_instance.html) in the PingFederate documentation.

4. (Optional) On the **Session Validation** tab, define a session validation policy. Click **Next**.

   You can find more information about configuration options in [Managing session validation settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_beareraccesstokenmgmtplugintasklet_sessionvalidationstate.html) in the PingFederate documentation.

5. On the **Access Token Attribute Contract** tab:

   1. In the **Extend the Contract** field, enter `acr`.

   2. In the **Action** column, click **Add**.

   3. Repeat this process for `amr` and any optional attributes that you extended the contract for in step 4 of [Configuring an adapter instance](pf_ms_eam_configuring_an_adapter_instance.html).

   4. Click **Next**.

6. (Optional) On the **Resource URIs** tab, enter a list of base resource URIs that can be used to select this access token management instance. Click **Next**.

   You can find more information in [Managing resource URIs](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_beareraccesstokenmgmtplugintasklet_atmselectionsettingsstate.html) in the PingFederate documentation.

7. (Optional) On the **Access Control** tab, select whether to restrict allowed clients. Click **Next**.

   You can find more information in [Defining access control](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_beareraccesstokenmgmtplugintasklet_atmaccesscontrolsettingsstate.html).

8. On the **Summary** tab, click **Save**.

## Creating access token mappings

Configure the access token mappings for the ATM you configured in the previous procedure.

You can find more information about configuration options in [Managing access token mappings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_accesstokenmappingtasklet_oauthuserkey2accesstokenmappingstate.html) and [Configuring access token mapping](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configure_access_token_mapping.html) in the PingFederate documentation.

### Steps

1. On the **Access Token Mappings** page:

   1. In the **Context** menu, select the desired authentication policy contract.

   2. In the **Access Token Manager** menu, select the JWT ATM that you configured in the previous procedure.

   3. Click **Add Mapping**.

2. On the **Attribute Sources & User Lookup** tab, click **Next**.

3. On the **Contract Fulfillment** tab, select a **Source** and **Value** to map into the `acr` and `amr` attributes in the **Contract** list:

   For example, to configure contract fulfillment for the `acr` attribute:

   1. In the **Source** list, select **Authentication Policy Contract**.

   2. In the **Value** list, select **acr**.

   3. Repeat for `amr` and any optional attributes that you extended the contract for in step 4 of [Configuring an adapter instance](pf_ms_eam_configuring_an_adapter_instance.html).

      * For the `amr` attribute, in the **Source** list, select **Authentication Policy Contract**, and in the **Value** list, select **amr**.

   4. Click **Next**.

   You can find more configuration information in [Configuring access token fulfillment](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_oauthuserkey2accesstokenmappingtasklet_oauthsource2targetmappingstate.html) in the PingFederate documentation.

4. (Optional) On the **Issuance Criteria** tab, configure the criteria for use with this token authorization:

   You can find more configuration information in [Defining issuance criteria for access token mapping](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_oauthuserkey2accesstokenmappingtasklet_oauthsource2targetissuancecriteriastate.html) in the PingFederate documentation.

5. On the **Summary** tab, click **Save**.

---

---
title: Configuring an adapter instance
description: Configure the Microsoft EAM IdP Adapter to determine how PingFederate communicates with Microsoft Entra ID.
component: microsoft-eam
page_id: microsoft-eam:setup:pf_ms_eam_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/setup/pf_ms_eam_configuring_an_adapter_instance.html
revdate: February 25, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Configuring an adapter instance

Configure the Microsoft EAM IdP Adapter to determine how PingFederate communicates with Microsoft Entra ID.

## About this task

To begin the integration, deploy the Microsoft EAM Integration Kit files to your PingFederate directory.

## Steps

1. In the PingFederate administrative console, go to **Authentication > Integration > IdP Adapters** and click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **Microsoft EAM IdP Adapter**.

   4. Click **Next**.

3. On the **IdP Adapter** tab, configure the adapter instance:

   1. In the **Entra Tenant ID** field, enter the Azure (Microsoft Entra ID) Tenant ID.

   2. In the **Entra App ID** field, enter the application ID of the protected resource in Microsoft Entra ID.

      |   |                                                                                              |
      | - | -------------------------------------------------------------------------------------------- |
      |   | By default, you don't need to update the **Location of ACR** and **Location of AMR** fields. |

   3. Click **Next**.

   Learn more about these settings in [Microsoft EAM IdP Adapter settings reference](pf_ms_eam_adapter_settings_ref.html).

4. (Optional) On the **Extended Contract** tab, add any attributes you want to extract out of the **id\_token\_hint**.

   > **Collapse: Show or hide substeps**
   >
   > 1. In the **Extend the Contract** field, enter the name of an attribute.
   >
   > 2. In the **Action** column, click **Add**.
   >
   > 3. Repeat for any additional attributes.
   >
   > 4. Click **Next**.

5. On the **Adapter Attributes** tab, select the **Pseudonym** checkbox for `acr`, `amr`, and `sub`. Click **Next**.

   Learn more about these settings in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation.

6. On the **Adapter Contract Mapping** tab, select **Adapter** for `acr`, `amr`, and `sub`. Click **Next**.

   > **Collapse: Show or hide substeps**
   >
   > You can find more information about these settings in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation.
   >
   > 1. On the **Adapter Contract Mapping** tab, click **Configure Adapter Contract**.
   >
   > 2. On the **Attribute Sources & User Lookup** tab, click **Next**.
   >
   > 3. On the **Adapter Contract Fulfillment** tab, confirm that in the **Source** list, **Adapter** is selected for `acr`, `amr`, and `sub`. Click **Next**.
   >
   > 4. On the **Issuance Criteria** tab, click **Next**.
   >
   > 5. On the **Summary** tab, click **Done**.

7. On the **Summary** tab, review your configuration. Click **Save**.

## Next steps

1. [Configure the downstream adapter to export amr as an additional attribute](pf_ms_eam_exporting_amr_as_an_additional_attribute.html).

2. [Configure PingFederate to use the Microsoft EAM IdP Adapter](pf_ms_eam_configuring_pf_to_use_the_ms_eam_idp_adapter.html)

---

---
title: Configuring PingFederate to use the Microsoft EAM IdP Adapter
description: Enable static signing keys in the OAuth and OpenID Connect (OIDC) key configuration.
component: microsoft-eam
page_id: microsoft-eam:setup:pf_ms_eam_configuring_pf_to_use_the_ms_eam_idp_adapter
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/setup/pf_ms_eam_configuring_pf_to_use_the_ms_eam_idp_adapter.html
revdate: August 28, 2025
section_ids:
  steps: Steps
---

# Configuring PingFederate to use the Microsoft EAM IdP Adapter

## Steps

1. [Enable static signing keys in the OAuth and OpenID Connect (OIDC) key configuration](pf_ms_eam_enabling_signing_keys.html).

2. [Configure an access token manager (ATM) and create access token mappings](pf_ms_eam_configuring_an_atm.html).

3. [Adjust the OIDC policy configuration](pf_ms_eam_adjusting_the_oidc_policy_configuration.html).

4. [Register an OAuth Client for Microsoft Entra ID in PingFederate](pf_ms_eam_registering_an_oauth_client_for_ms_entra_id.html).

5. [Use the Microsoft EAM IdP Adapter and a downstream MFA adapter, such as PingID, in the PingFederate authentication policy](pf_ms_eam_configuring_a_pf_authentication_policy.html).

6. [Track HTTP request parameters in the PingFederate authentication policy](pf_ms_eam_tracking_http_request_parameters.html).

---

---
title: Configuring the downstream adapter to export <code>amr</code> as an additional attribute
description: Configure the downstream adapter you're planning to use as the MFA factor to export amr as an additional attribute.
component: microsoft-eam
page_id: microsoft-eam:setup:pf_ms_eam_exporting_amr_as_an_additional_attribute
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/setup/pf_ms_eam_exporting_amr_as_an_additional_attribute.html
revdate: February 26, 2024
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Configuring the downstream adapter to export `amr` as an additional attribute

Configure the downstream adapter you're planning to use as the MFA factor to export `amr` as an additional attribute.

In the following example, the PingID adapter is the downstream adapter.

## Steps

1. In the PingFederate administrative console, open the PingID adapter configuration and go to the **Extended Contract** tab.

2. In the **Extend the Contract** field, enter `amr`. Click **Add**.

3. Go to the **Adapter Contract Mapping** tab and click **Configure Adapter Contract**.

4. Convert PingID-specific `amr` values into Microsoft Entra ID-specific `amr` values:

   1. Go to the **Adapter Contract Fulfillment** tab.

   2. Find `amr` in the **Contract** column.

   3. In the corresponding **Source** list, select **Expression**.

   4. In the corresponding **Value** field, enter the following OGNL expression:

      ```
      #xref = #{
      "FIDO2":"fido",
      "FIDO2_BIOMETRICS":"fido",
      "BYPASS":"bypass",
      "MOBILE_APP_BIOMETRICS":"bio",
      "MOBILE_APP_SWIPE":"swk",
      "NUMBER_MATCHING":"swk",
      "MOBILE_APP_OTP":"otp",
      "POLICY_APPROVE":"pop",
      "EMAIL":"otp",
      "SMS":"sms",
      "VOICE":"tel",
      "YUBIKEY":"hwk",
      "OATH_TOKEN":"hwk",
      "AUTHENTICATOR_APP":"otp",
      "DESKTOP_OTP":"otp",
      "SECURITY_KEY":"fido" },
      #action = #this.get("pingid.authentication.type").toString(),
      #result = (#action != null) && (#xref[#action] != null) ? #xref[#action] : "no_mapping",
      #result
      ```

5. Click **Done**.

## Next steps

[Configure PingFederate to use the Microsoft EAM IdP Adapter](pf_ms_eam_configuring_pf_to_use_the_ms_eam_idp_adapter.html).

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Microsoft EAM Integration Kit files to your PingFederate directory.
component: microsoft-eam
page_id: microsoft-eam:setup:pf_ms_eam_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/setup/pf_ms_eam_deploying_the_integration_files.html
revdate: October 24, 2024
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Deploying the integration files

To get started with the integration, deploy the Microsoft EAM Integration Kit files to your PingFederate directory.

## Steps

1. Download the Microsoft EAM Integration Kit `.zip` archive from the **Add-ons** tab of the [PingFederate Downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/microsoft-eam-integration-kit).

2. Stop PingFederate, if it's running.

3. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Start PingFederate

5. If you operate PingFederate in a cluster, repeat steps 2 - 4 for each engine node.

## Next steps

[Configure an adapter instance](pf_ms_eam_configuring_an_adapter_instance.html).

---

---
title: Download manifest
description: The following files are included in the Microsoft EAM Integration Kit .zip archive:
component: microsoft-eam
page_id: microsoft-eam:release_notes:pf_ms_eam_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/release_notes/pf_ms_eam_download_manifest.html
revdate: July 29, 2024
---

# Download manifest

The following files are included in the Microsoft EAM Integration Kit `.zip` archive:

* `Legal.pdf`: copyright and license information.

* `dist/pingfederate/server/default`: contains the integration files.

  * `deploy`: contains the java libraries.

    * `pf-microsoft-eam-idp-adapter-<version>.jar`: The Microsoft EAM IdP Adapter.

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for PingFederate, the Microsoft EAM IdP Adapter, or both.
component: microsoft-eam
page_id: microsoft-eam:troubleshooting:pf_ms_eam_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/troubleshooting/pf_ms_eam_enabling_debug_logging.html
revdate: October 25, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for PingFederate, the Microsoft EAM IdP Adapter, or both.

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

3. To log activity relating to the Microsoft EAM IdP Adapter:

   ### Choose from:

   * To log activity for the Microsoft EAM IdP Adapter as well as its HTTPS and component activity, add the following line:

     ```html
     <Logger name="com.pingidentity.adapters.microsoft.eam" level="DEBUG"/>
     ```

   * To log activity for the adapter's HTTPS activity and other components but not for the adapter itself, add the following line:

     ```html
     <Logger name="com.pingidentity.adapters.microsoft.eam.shade" level="DEBUG"/>
     ```

   * To log activity for the Microsoft EAM IdP Adapter but not its HTTPS or component activity, add the following lines:

     ```html
     <Logger name="com.pingidentity.adapters.microsoft.eam" level="DEBUG"/>
     <Logger name="com.pingidentity.adapters.microsoft.eam.shade" level="INFO"/>
     ```

4. Save the file.

---

---
title: Enabling signing keys
description: Enable static signing keys in the OAuth and OpenID Connect (OIDC) key configuration.
component: microsoft-eam
page_id: microsoft-eam:setup:pf_ms_eam_enabling_signing_keys
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/setup/pf_ms_eam_enabling_signing_keys.html
revdate: September 17, 2025
section_ids:
  steps: Steps
---

# Enabling signing keys

Enable static signing keys in the OAuth and OpenID Connect (OIDC) key configuration.

## Steps

1. In the PingFederate admin console, go to **Security > Certificate & Key Management > OAuth & OpenID Connect keys**.

2. Select **Enable Static Keys**.

3. In the **Signing Keys** section, go to the RSA **Key Type**, select an **Active** signing key, and select the **Publish Certificate** checkbox.

4. Click **Save**.

Learn more in [Configuring static signing keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_static_signing_keys.html) in the PingFederate documentation.

---

---
title: Known issues and limitations
description: The following are known issues or limitations with the Microsoft EAM Integration Kit.
component: microsoft-eam
page_id: microsoft-eam:release_notes:pf_ms_eam_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/release_notes/pf_ms_eam_known_issues_and_limitations.html
revdate: August 27, 2025
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations with the Microsoft EAM Integration Kit.

## Known issues

There are no known issues.

## Known limitations

* Authentication API

  The adapter doesn't support the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

---

---
title: Microsoft EAM IdP Adapter settings reference
description: Field descriptions for the Microsoft EAM IdP Adapter configuration, accessible on the IdP Adapter tab in the PingFederate admin console.
component: microsoft-eam
page_id: microsoft-eam:setup:pf_ms_eam_adapter_settings_ref
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/setup/pf_ms_eam_adapter_settings_ref.html
revdate: August 27, 2025
---

# Microsoft EAM IdP Adapter settings reference

Field descriptions for the Microsoft EAM IdP Adapter configuration, accessible on the **IdP Adapter** tab in the PingFederate admin console.

> **Collapse: Standard fields**
>
> | Field               | Description                                                                                                                   |
> | ------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
> | **Entra Tenant ID** | The Azure (Microsoft Entra ID) Tenant ID.                                                                                     |
> | **Entra App ID**    | The application ID of the protected resource in Microsoft Entra ID.                                                           |
> | **Location of ACR** | The JSON Pointer location of the `acr` options within the **claims** parameter.The default value is `/id_token/acr/values/0`. |
> | **Location of AMR** | The JSON Pointer location of the `amr` options within the **claims** parameter.The default value is `/id_token/amr/values`.   |

> **Collapse: Advanced fields**
>
> | Field          | Description                                                                                                                                                                                                                            |
> | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Issuer URI** | The Issuer URI used to validate the **id\_token\_hint**.The default value is `https://login.microsoftonline.com/<tenant-id>/v2.0` where *\<tenant-id>* is the value configured for the **Entra Tenant ID** field.                      |
> | **JWKS URI**   | The JWKS URI that identifies the keys used to sign the tokens.The default value is `https://login.microsoftonline.com/<tenant-id>/discovery/v2.0/keys` where *\<tenant-id>* is the value configured for the **Entra Tenant ID** field. |

---

---
title: Microsoft EAM Integration Kit
description: This integration kit enables PingFederate, together with a downstream multi-factor authentication (MFA) adapter, to serve as a Microsoft External Authentication Method (EAM) provider.
component: microsoft-eam
page_id: microsoft-eam::pf_ms_eam_ik
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/pf_ms_eam_ik.html
revdate: August 27, 2025
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Microsoft EAM Integration Kit

This integration kit enables PingFederate, together with a downstream multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* adapter, to serve as a Microsoft External Authentication Method (EAM) provider.

The Microsoft EAM Integration Kit processes the **id\_token\_hint** and **claims** parameters sent by Microsoft Entra ID's external authentication mechanism.

The integration kit extracts the `acr` and `amr` values from the **claims** parameter and sets them as input for downstream adapters in the PingFederate authentication policy. Typically, a downstream adapter like PingID uses these values to perform MFA.

## Components

* Microsoft EAM IdP Adapter

  When PingFederate receives an OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
  \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
  \</div>)* request from Microsoft Entra ID, the adapter validates the **id\_token\_hint** and extracts the `acr` and `amr` values from the **claims** parameter. You can export additional claims out of the **id\_token\_hint** as necessary.

## Intended audience

This document is intended for PingFederate administrators.

Use the following resources to find help during the setup process:

* You can find more information about configuring PingFederate in the following sections of the PingFederate documentation:

  * [Access token management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_access_token_management.html)

  * [OIDC Policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_oidc_policies.html)

  * [Configuring OAuth clients](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_oauth_clients.html)

  * [Authentication Policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

* If you plan to use the bundled PingID adapter as the downstream adapter, you can find configuration instructions and context in:

  * The [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html) section of the PingFederate documentation.

  * The [Integrate with PingID for PingFederate SSO](https://docs.pingidentity.com/pingid/pingid_integrations/pid_integrate_pf_sso.html) section of the PingID documentation.

## System requirements

* PingFederate 11.3 or later.

* A Microsoft Entra ID account with [external authentication method](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-external-method-manage) enabled.

---

---
title: Overview of the SSO flow
description: The following figure demonstrates an example single sign-on (SSO) process flow.
component: microsoft-eam
page_id: microsoft-eam::pf_ms_eam_sso_flow_overview
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/pf_ms_eam_sso_flow_overview.html
revdate: September 17, 2024
section_ids:
  description: Description
---

# Overview of the SSO flow

The following figure demonstrates an example single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* process flow.

![A diagram illustrating a typical sign on process leveraging the integration kit.](_images/MS_EAM_SSO_Flow.png)

## Description

1. A user initiates the sign-on process by requesting access to an application that's protected by Microsoft Entra ID.

2. The user authenticates with Microsoft Entra ID using a primary authentication method.

3. Microsoft Entra ID makes an OpenID Connect (OIDC) request to PingFederate for secondary authentication.

4. PingFederate validates the OIDC request, then sets the **id\_token\_hint** and **claims** provided by Microsoft Entra ID as tracked parameters.

5. The Microsoft EAM IdP Adapter picks up the **id\_token\_hint** and **claims**, validates the **id\_token\_hint**, and then sets the `sub`, `acr`, and `amr` values for downstream adapters like PingID.

6. The downstream adapter requests a second authentication factor from the user.

7. The user authenticates with the downstream adapter using a secondary authentication method.

8. The downstream adapter shares the used `amr` and `acr` values with PingFederate.

9. PingFederate sends a response to Microsoft Entra ID with the id\_token, including the `sub`, `acr`, and `amr` claims required by Microsoft Entra ID.

10. Microsoft Entra ID validates the id\_token, signature, and claims.

11. Microsoft Entra ID grants the user access to the protected application.

---

---
title: Registering an OAuth client for Microsoft Entra ID
description: Register an OAuth Client for Microsoft Entra ID in PingFederate.
component: microsoft-eam
page_id: microsoft-eam:setup:pf_ms_eam_registering_an_oauth_client_for_ms_entra_id
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/setup/pf_ms_eam_registering_an_oauth_client_for_ms_entra_id.html
revdate: August 28, 2025
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Registering an OAuth client for Microsoft Entra ID

Register an OAuth Client for Microsoft Entra ID in PingFederate.

Learn more in [configuring OAuth clients](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_oauth_clients.html).

## Steps

1. Go to **Applications > OAuth Clients**.

2. In the **Client Authentication** section, select **None**.

3. In the **Redirect URIs** section, in the **Redirection URIs** field, enter `https://login.microsoftonline.com/common/federation/externalauthprovider` and click **Add**.

4. Select the **Bypass Authorization Approval** checkbox.

5. In the **Allowed Grant Types** section, select `Implicit`.

   |   |                                                                   |
   | - | ----------------------------------------------------------------- |
   |   | `Implicit` is the only supported grant type for this integration. |

6. Confirm that `id_token` is a valid response type.

7. In the **Default Access Token Manager** list, select the ATM that you configured in [Configuring an access token manager](pf_ms_eam_configuring_an_atm.html).

8. In the **OpenID Connect** section, in the **Policy** list, select the OIDC policy that you configured in [Adjusting the OIDC policy configuration](pf_ms_eam_adjusting_the_oidc_policy_configuration.html).

## Next steps

When configuring the OAuth Client details in Microsoft Entra ID, you must configure a redirect\_uri. Use PingFederate's authorization endpoint URL: `https://{pingfederate}/as/authorization.oauth2`.

---

---
title: Tracking HTTP request parameters
description: Configure tracked HTTP parameters in the PingFederate authentication policy for the Microsoft EAM IdP Adapter to reference.
component: microsoft-eam
page_id: microsoft-eam:setup:pf_ms_eam_tracking_http_request_parameters
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/setup/pf_ms_eam_tracking_http_request_parameters.html
revdate: August 28, 2025
section_ids:
  steps: Steps
---

# Tracking HTTP request parameters

Configure tracked HTTP parameters in the PingFederate authentication policy for the Microsoft EAM IdP Adapter to reference.

Learn more about tracked HTTP parameters in [defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html).

## Steps

1. In the PingFederate admin console, go to **Authentication > Policies** and click the **Tracked HTTP Parameters** tab.

2. In the **Parameter Name** field, enter **id\_token\_hint** and **claims**. Click **Add**.

3. Click **Save**.