---
title: Authentication API Support
description: You can use the PingFederate authentication API to integrate the PingOne Credentials IdP Adapter into your application.
component: pingone-credentials
page_id: pingone-credentials:setup:pf_p1_credentials_ik_authentication_api_support
canonical_url: https://docs.pingidentity.com/integrations/pingone-credentials/setup/pf_p1_credentials_ik_authentication_api_support.html
revdate: August 27, 2024
---

# Authentication API Support

You can use the PingFederate authentication API to integrate the PingOne Credentials IdP Adapter into your application.

The PingFederate Authentication API provides access to the current state of the authentication flow as a user steps through the PingFederate authentication policy. Learn more in [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

To integrate the PingOne Credentials IdP Adapter into your authentication flow, configure your application based on the information in this section.

|   |                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can also explore the process using the PingFederate Authentication API Explorer. Learn more in [Exploring the Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_exploring_authentication_api.html) in the PingFederate documentation. |

---

---
title: Changelog
description: The following is the change history for the PingOne Credentials Integration Kit.
component: pingone-credentials
page_id: pingone-credentials:release_notes:pf_p1_credentials_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/pingone-credentials/release_notes/pf_p1_credentials_ik_changelog.html
revdate: August 27, 2024
section_ids:
  pingone-credentials-integration-kit-1-0-august-2024: PingOne Credentials Integration Kit 1.0 - August 2024
---

# Changelog

The following is the change history for the PingOne Credentials Integration Kit.

## PingOne Credentials Integration Kit 1.0 - August 2024

* Initial release.

* Added the ability to verify user credentials as part of a sign-on flow.

* Added the ability to control which message pages (templates) are shown to the user.

* Added the ability to customize template messages using a language pack file.

* Added settings to control how the adapter handles sign-on attempts when errors occur.

* Added support for the platform connection to PingOne introduced in PingFederate 10.2.

* Added support for the PingFederate authentication API.

* Added support for the JavaScript Widget for the PingFederate Authentication API.

* Added settings for API connection and request timeouts.

---

---
title: Configuring an adapter instance
description: Configure the PingOne Credentials IdP Adapter to determine how PingFederate communicates with PingOne Credentials.
component: pingone-credentials
page_id: pingone-credentials:setup:pf_p1_credentials_ik_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/pingone-credentials/setup/pf_p1_credentials_ik_configuring_an_adapter_instance.html
revdate: September 3, 2024
section_ids:
  steps: Steps
  example: Example:
  example-2: Example:
  example-3: Example:
  next-steps: Next steps
---

# Configuring an adapter instance

Configure the PingOne Credentials IdP Adapter to determine how PingFederate communicates with PingOne Credentials.

## Steps

1. In the PingFederate administrative console, go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. From the **Type** list, select **PingOne Credentials IdP Adapter**. Click **Next**.

3. On the **IdP Adapter** tab, in the **Credential Types and Attributes** section, define the credential types and attributes that you want users to present for verification.

   1. Click **Add a new row to 'Credential Types and Attributes'**.

   2. In the **Credential Type** list, select a credential type that you want users to present for verification.

      ### Example:

      `verifiedEmployee`

   3. In the corresponding **Credential Attribute** field, enter any attributes that you want users to present for verification.

      Separate the attribute values with commas.

      ### Example:

      `firstName, lastName`

   4. In the **Action** column, click **Update**.

   5. To add more credential types and attributes, repeat steps a-d.

   Because the credential issuer and credential verifier can be in different environments, the **Credential Type** list doesn't auto-populate credential types for the selected environment. Use the following issuer filters, **Requested Issuer(s) by Environment ID** and **Requested Issuer(s) by Decentralized Identifiers (DID)** to filter through environments and find the credential types that you want to include in the credential presentation request.

4. **Optional:** In the **Requested Issuer(s) by Environment ID** section, enter the PingOne environment ID of a trusted issuer.

   1. Click **Add a new row to 'Requested Issuer(s) by Environment ID'**.

   2. In the **Issuer by Environment ID** field, enter the environment ID of the issuer.

   3. In the **Action** column, click **Update**.

   4. To add more issuers, repeat steps a-d.

5. **Optional:** In the **Requested Issuer(s) by Decentralized Identifiers (DID)** section, enter the decentralized identifier of a trusted issuer.

   1. Click **Add a new row to 'Requested Issuer(s) by Decentralized Identifiers (DID)'**.

   2. In the **Issuer by Decentralized Identifier** field, enter the decentralized identifier of the issuer.

   3. In the **Action** column, click **Update**.

   4. To add more issuers, repeat steps a-d.

6. On the **IdP Adapter** tab, configure the adapter instance by referring to [PingOne Credentials IdP Adapter settings reference](pf_p1_credentials_ik_p1_credentials_idp_adapter_settings_reference.html). Click **Next**.

7. On the **Extended Contract** tab, add all of the attributes that you defined in the **Credential Types and Attributes** table. Then click **Next**.

   Using the following format, define each attribute separately:

   ```
   <credentialType>.<credentialAttribute>
   ```

   ### Example:

   For a `verifiedEmployee` credential type that has two attributes, entered in the **Credential Attribute** field as `firstName, lastName`, add the `firstName` attribute first:

   ```
   verifiedEmployee.firstName
   ```

   Then add the `lastName` attribute:

   ```
   verifiedEmployee.lastName
   ```

8. On the **Adapter Attributes** tab, for **subject**, select the **Pseudonym** check box. Click **Next**.

9. On the **Adapter Contract Mapping** tab, click **Configure Adapter Contract** and fill out the configuration as necessary. Click **Done**, then **Next**.

   |   |                                                                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Make sure to click **Configure Adapter Contract** and complete a configuration, even if it's just **Configure Adapter Contract > Next > Next > Next > Done > Next**. Otherwise, the adapter contract fulfillment isn't mapped to the adapter. |

10. On the **Summary** tab, review your configuration. Click **Save**.

## Next steps

Complete the [Extending the contract](pf_p1_credentials_ik_configuring_the_extended_contract.html) procedure.

---

---
title: Connecting PingFederate 10.1 or earlier
description: In PingOne, create a set of credentials for PingFederate. For PingFederate 10.1 and earlier, you must enter these credentials in each PingFederate component that communicates with PingOne.
component: pingone-credentials
page_id: pingone-credentials:setup:pf_p1_credentials_ik_connecting_pf_101_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/pingone-credentials/setup/pf_p1_credentials_ik_connecting_pf_101_or_earlier.html
revdate: August 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Connecting PingFederate 10.1 or earlier

## About this task

In PingOne, create a set of credentials for PingFederate. For PingFederate 10.1 and earlier, you must enter these credentials in each PingFederate component that communicates with PingOne.

## Steps

1. On the PingOne administrative console, go to **Applications > Applications** and click the **[icon: plus, set=fa]**icon.

2. On the **Add Application** window, enter a unique **Application Name**.

3. In the **Application Type** list, select **Worker**, then **Save**.

4. On the **Roles** tab, click **Grant Roles**, then select the **Identity Data Administrator** checkbox for the environment.

5. On the **Overview** or **Configuration** tab, note the **Client ID**, **Client Secret**, and **Environment ID**.

   You'll use these credentials in [Configuring an adapter instance](pf_p1_credentials_ik_configuring_an_adapter_instance.html).

6. Click the toggle at the top of the application to activate it.

---

---
title: Connecting PingFederate 10.2 or later
description: Create a connection between PingFederate and PingOne. In PingFederate 10.2 and later, you can use this connection for all PingFederate components that communicate with PingOne.
component: pingone-credentials
page_id: pingone-credentials:setup:pf_p1_credentials_ik_connecting_pf_102_or_later
canonical_url: https://docs.pingidentity.com/integrations/pingone-credentials/setup/pf_p1_credentials_ik_connecting_pf_102_or_later.html
revdate: August 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Connecting PingFederate 10.2 or later

## About this task

Create a connection between PingFederate and PingOne. In PingFederate 10.2 and later, you can use this connection for all PingFederate components that communicate with PingOne.

|   |                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you already have a connection from PingOne to PingFederate, ensure that the **Identity admin** and **Environment admin** roles are enabled. Skip the steps below. |

## Steps

1. Create credentials in PingOne:

   1. On the PingOne administrative console, go to **Integrations > PingFederate** and click the **[icon: plus, set=fa]**icon.

   2. On the **Create Connection Profile** window, enter a connection name, then click **Save**.

   3. After the **New Credential Created** window opens, click **Copy To Clipboard**, then **Done**.

2. Use the credentials to create a connection in PingFederate:

   1. On the PingFederate administrative console, go to **System > External Systems > PingOne Connections** and click **[icon: plus, set=fa]Add Connection**.

   2. On the **Add Connection** window, paste the credential information in the **Paste The Credential Here** field.

   3. In the **Connection Name** field, enter a unique name and click **Save**.

---

---
title: Connecting PingFederate to PingOne
description: To allow PingFederate to communicate with PingOne, create a connection.
component: pingone-credentials
page_id: pingone-credentials:setup:pf_p1_credentials_ik_connecting_pf_to_p1
canonical_url: https://docs.pingidentity.com/integrations/pingone-credentials/setup/pf_p1_credentials_ik_connecting_pf_to_p1.html
revdate: August 27, 2024
section_ids:
  connecting-pingfederate-10-2-or-later: Connecting PingFederate 10.2 or later
  about-this-task: About this task
  steps: Steps
  connecting-pingfederate-10-1-or-earlier: Connecting PingFederate 10.1 or earlier
  about-this-task-2: About this task
  steps-2: Steps
---

# Connecting PingFederate to PingOne

To allow PingFederate to communicate with PingOne, create a connection.

* PingFederate 10.2 or later

* PingFederate 10.1 or earlier

## Connecting PingFederate 10.2 or later

### About this task

Create a connection between PingFederate and PingOne. In PingFederate 10.2 and later, you can use this connection for all PingFederate components that communicate with PingOne.

|   |                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you already have a connection from PingOne to PingFederate, ensure that the **Identity admin** and **Environment admin** roles are enabled. Skip the steps below. |

### Steps

1. Create credentials in PingOne:

   1. On the PingOne administrative console, go to **Integrations > PingFederate** and click the **[icon: plus, set=fa]**icon.

   2. On the **Create Connection Profile** window, enter a connection name, then click **Save**.

   3. After the **New Credential Created** window opens, click **Copy To Clipboard**, then **Done**.

2. Use the credentials to create a connection in PingFederate:

   1. On the PingFederate administrative console, go to **System > External Systems > PingOne Connections** and click **[icon: plus, set=fa]Add Connection**.

   2. On the **Add Connection** window, paste the credential information in the **Paste The Credential Here** field.

   3. In the **Connection Name** field, enter a unique name and click **Save**.

## Connecting PingFederate 10.1 or earlier

### About this task

In PingOne, create a set of credentials for PingFederate. For PingFederate 10.1 and earlier, you must enter these credentials in each PingFederate component that communicates with PingOne.

### Steps

1. On the PingOne administrative console, go to **Applications > Applications** and click the **[icon: plus, set=fa]**icon.

2. On the **Add Application** window, enter a unique **Application Name**.

3. In the **Application Type** list, select **Worker**, then **Save**.

4. On the **Roles** tab, click **Grant Roles**, then select the **Identity Data Administrator** checkbox for the environment.

5. On the **Overview** or **Configuration** tab, note the **Client ID**, **Client Secret**, and **Environment ID**.

   You'll use these credentials in [Configuring an adapter instance](pf_p1_credentials_ik_configuring_an_adapter_instance.html).

6. Click the toggle at the top of the application to activate it.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the PingOne Credentials Integration Kit files to your PingFederate directory.
component: pingone-credentials
page_id: pingone-credentials:setup:pf_p1_credentials_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/pingone-credentials/setup/pf_p1_credentials_ik_deploying_the_integration_files.html
revdate: August 29, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the PingOne Credentials Integration Kit files to your PingFederate directory.

## Steps

1. Download the PingOne Credentials Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/pingone-credentials-integration-kit).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, back up your customizations and delete earlier versions of the integration files:

   1. Back up any PingOne Credentials Integration Kit files that you customized in the `<pf_install>/pingfederate/server/default/conf/` directory.

   2. Delete the `pf-pingone-credentials-adapter-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. If there is more than one version of the `pf-authn-api-sdk-<version>.jar` file in your `<pf_install>/pingfederate/server/default/lib` directory, delete all but the latest version of the file.

6. If you backed up any customized files, modify the new files with your customizations.

7. Start PingFederate.

8. If you operate PingFederate in a cluster, repeat steps 2-7 for each engine node.

---

---
title: Download manifest
description: The following files are included in the PingOne Credentials Integration Kit .zip archive:
component: pingone-credentials
page_id: pingone-credentials:release_notes:pf_p1_credentials_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/pingone-credentials/release_notes/pf_p1_credentials_ik_download_manifest.html
revdate: August 27, 2024
---

# Download manifest

The following files are included in the PingOne Credentials Integration Kit `.zip` archive:

* `ReadMeFirst.pdf` – contains links to this online documentation

* `Legal.pdf` – copyright and license information

* `dist/pingfederate/server/default` – contains the integration files

  * `deploy` – contains the Java libraries

    * `pf-pingone-credentials-adapter-<version>.jar` – JAR file that contains the PingOne Credentials IdP Adapter.

  * `conf` – contains the HTML template that presents the PingOne sign-on form.

    * `language-packs` – contains files with customizable user-facing messages

      * `pingone-credentials-messages.properties` – a variable file that customizes the messages that appear on the template file.

    * `template` – contains user-facing HTML template files

      * `pingone-credentials-completed.html` – a sample template that indicates the presentation session completed successfully.

      * `pingone-credentials-failed.html` – a sample template that indicates that the user failed the presentation session.

      * `pingone-credentials-required.html` – a sample template that asks the user to complete the presentation session.

      * `pingone-credentials-timed-out.html` – a sample template that indicates that the presentation session took too long.

      - `assets` – contains functional scripts and files used by the template

        * `css` – contains CSS files for the templates.

          * `pingone-credentials.css` – a CSS file that customizes the appearance of the template files.

          * `end-user/<version>/end-user.css` – a CSS file that customizes the appearance of the template files.

        * `fonts/end-user` – contains template fonts and icons

          * `icons` – contains template icons

        * `images` – contains template image files

          * `ping-logo.svg` – an image file with company branding

          * `spinner.svg` – an image file used in a spinner animation

        * `scripts` – contains script files used to collect and send information

          * `jquery-<version>.min.js` – a JavaScript file that contains the jQuery library.

  * `lib/pf-authn-api-sdk-<version>.jar` – a JAR file that contains the PingFederate Authentication API SDK

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.
component: pingone-credentials
page_id: pingone-credentials:troubleshooting:pf_p1_credentials_ik_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/pingone-credentials/troubleshooting/pf_p1_credentials_ik_enabling_debug_logging.html
revdate: August 27, 2024
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

3. If you want to log activity just for the PingOne Credentials IdP Adapter, add the following line.

   ```html
   <Logger name="com.pingidentity.adapters.pingone.credentials" level="DEBUG"/>
   ```

4. Save the file.

---

---
title: Extending the contract
description: Apply the same extended contract changes to the policy contract and OpenToken SP adapter. Map the policy contract to the authentication policy's IdP adapter success step and the browser SSO of the SP and IdP connections.
component: pingone-credentials
page_id: pingone-credentials:setup:pf_p1_credentials_ik_configuring_the_extended_contract
canonical_url: https://docs.pingidentity.com/integrations/pingone-credentials/setup/pf_p1_credentials_ik_configuring_the_extended_contract.html
revdate: September 3, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Extending the contract

Apply the same extended contract changes to the policy contract and OpenToken SP adapter. Map the policy contract to the authentication policy's IdP adapter success step and the browser SSO of the SP and IdP connections.

## Before you begin

This procedure assumes that you've created:

1. An OpenToken SP adapter. Learn more in [Configuring an OpenToken SP adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_opentoken_sp_adapt_instance.html).

2. The authentication policy that you want to use the PingOne Credentials IdP Adapter in. Learn more in [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html).

3. An SP connection for the OpenToken SP adapter and an IdP connection for the PingOne Credentials IdP Adapter. Learn more in [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html) and [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html).

## About this task

Complete this procedure to finish configuring the PingOne Credentials IdP Adapter and successfully use the [same device or different device SSO flow](../pf_p1_credentials_ik_overview_of_the_sso_flow.html) to collect the credential attribute values presented from the user's digital wallet. Chained adapters can then use the collected attribute values later in the configured PingFederate authentication policy flow.

Credential attributes can't be added to the core attribute contract because administrators might require different credential types and attributes for verification. Unlike with the PingOne Verify integration kit, administrators must configure the PingOne Credentials IdP Adapter credential fields manually, then extend the attribute contract to match.

## Steps

1. Create the same extended contract from the [Configuring an adapter instance](pf_p1_credentials_ik_configuring_an_adapter_instance.html) procedure in a PingFederate policy contract:

   Learn more in [Policy contracts](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_policy_contracts.html).

   |   |                                                         |
   | - | ------------------------------------------------------- |
   |   | You will use this policy contract in steps 2, 4, and 5. |

   1. Go to **Authentication > Policies > Policy Contracts** and click **Create New Contract**.

   2. On the **Contract Info** tab, in the **Contract Name** field, enter a unique value, then click **Next**.

      For example, `PingOne Credentials contract`.

   3. On the **Contract Attributes** tab, add the same attributes that you added to the extended contract in step 7 of the [Configuring an adapter instance](pf_p1_credentials_ik_configuring_an_adapter_instance.html) procedure. Click **Save**, then click **Next**.

      For example, `verifiedEmployee.firstName` and `verifiedEmployee.lastName`.

   4. On the **Summary** tab, click **Save**.

2. Map the policy contract that you created in step 2 to the PingOne Credentials IdP Adapter contract on the adapter's success step in the authentication policy:

   Learn more in [Applying policy contracts or identity profiles to authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_apply_policy_contract_or_ident_profile_to_auth_policies.html).

   1. Go to **Authentication > Policies > Policies** and edit the authentication policy that you've included the PingOne Credentials IdP Adapter in.

   2. In the **Policy** section, expand the **Success** step containing the PingOne Credentials IdP Adapter, and click **Contract Mapping** under the adapter's **Success** step.

   3. On the **Contract Fulfillment** tab, add the same attributes that you added to the extended contract in step 7 of the [Configuring an adapter instance](pf_p1_credentials_ik_configuring_an_adapter_instance.html) procedure.

      For each attribute, select the adapter as the **Source** and add the attribute as the **Value**.

   4. On the **Contract Fulfillment** tab, click **Done**, then click **Next**.

   5. On the **Summary** tab, click **Done**.

3. Create the same extended contract from the [Configuring an adapter instance](pf_p1_credentials_ik_configuring_an_adapter_instance.html) procedure in your OpenToken SP adapter instance:

   Learn more in [Extending an SP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_sessioncreationadaptertasklet_createadaptercontractstate.html).

   1. Go to **Applications > SP Adapters** and open your OpenToken SP adapter configuration.

   2. On the **Extended Contract** tab, add the same attributes that you added to the extended contract in step 7 of the [Configuring an adapter instance](pf_p1_credentials_ik_configuring_an_adapter_instance.html) procedure. Click **Save**, then click **Next**.

   3. On the **Summary** tab, click **Save**.

4. Map the policy contract that you created in step 2 to the **Browser SSO** section of the SP connection:

   Learn more in [Configuring SP browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_idpconnectionconfigtasklet_idpbrowserssostate.html).

   1. Go to **Applications > SP Connections** and open the connection that you used for your SP adapter.

   2. On the **Browser SSO** tab, click **Configure Browser SSO**, go to the **Assertion Creation** tab, click **Configure Assertion Creation**, and then go to the **Attribute Contract** tab.

   3. In the **Extend the Contract** section, add the same attributes that you added to the extended contract in step 7 of the [Configuring an adapter instance](pf_p1_credentials_ik_configuring_an_adapter_instance.html) procedure. Click **Save**, then **Next**.

      For each attribute, use `urn:oasis:names:tc:SAML:2.0:attrname-format:basic` as the **Attribute Name Format**.

   4. On the **Authentication Source Mapping** tab, confirm that your PingOne Credentials policy contract is mapped in the **Authentication Policy Contract Name** section.

   5. Open the authentication policy mapping, go to the **Attribute Contract Fulfillment** tab, and add the same attributes that you added to the extended contract in step 7 of the [Configuring an adapter instance](pf_p1_credentials_ik_configuring_an_adapter_instance.html) procedure.

      For each attribute, use **Authentication Policy Contract** as the **Source** and the attribute as the **Value**.

   6. Click **Save**, then **Done**.

5. Map the policy contract that you created in step 2 to the **Browser SSO** section of the IdP connection:

   Learn more in [Configuring IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html).

   1. Go to **Authentication > IdP Connections** and open the connection associated with the PingOne Credentials IdP Adapter.

   2. On the **Browser SSO** tab, click **Configure Browser SSO**, go to the **User-Session Creation** tab, click **Configure User-Session Creation**, and then go to the **Attribute Contract** tab.

   3. In the **Extend the Contract** section, add the same attributes that you added to the extended contract in step 7 of the [Configuring an adapter instance](pf_p1_credentials_ik_configuring_an_adapter_instance.html) procedure. Click **Save**, then **Next**.

   4. On the **Target Session Mapping** tab, confirm that your PingOne Credentials IdP Adapter is mapped in the **Adapter Instance Name** section.

   5. Open the adapter instance mapping, go to the **Adapter Contract Fulfillment** tab, and add the same attributes that you added to the extended contract in step 7 of the [Configuring an adapter instance](pf_p1_credentials_ik_configuring_an_adapter_instance.html) procedure.

      For each attribute, use **Assertion** as the **Source** and the attribute as the **Value**.

   6. Click **Save**, then **Done**.

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the PingOne Credentials Integration Kit.
component: pingone-credentials
page_id: pingone-credentials:release_notes:pf_p1_credentials_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/pingone-credentials/release_notes/pf_p1_credentials_ik_known_issues_and_limitations.html
revdate: August 27, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the PingOne Credentials Integration Kit.

## Known issues

There are no known issues.

## Known limitations

There are no known limitations.

---

---
title: Models, attributes, and error codes
description: When using the PingOne Credentials IdP Adapter through the PingFederate authentication API, the adapter uses the following state models, action models, objects, and error codes.
component: pingone-credentials
page_id: pingone-credentials:setup:pf_p1_credentials_ik__models_objects_and_error_codes
canonical_url: https://docs.pingidentity.com/integrations/pingone-credentials/setup/pf_p1_credentials_ik__models_objects_and_error_codes.html
revdate: September 3, 2024
section_ids:
  state-models: State models
  action-models: Action models
---

# Models, attributes, and error codes

When using the PingOne Credentials IdP Adapter through the PingFederate authentication API, the adapter uses the following state models, action models, objects, and error codes.

## State models

| Status                              | Response Model                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Action                               | Description                                                    |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | -------------------------------------------------------------- |
| `CREDENTIAL_VERIFICATION_REQUIRED`  | * `sessionID (string)`: The ID that can be used to check the status of the credential verification request.

* `sessionStatus (SessionStatus)`: The status of the credential verification request.

* `qUrl (string)`: The URL that can be used to get the QR code. Used in the different device SSO flow to open the wallet app.

* `appOpenUrl (string)`: The URL that can be used to open the wallet app.

* `redirect (boolean)`: Used in the same device SSO flow to open the wallet app after the user clicks **Open Wallet**. Uses the `appOpenUrl`.

* `errorDetails (List<CustomAuthnErrorDetail>)`: A list of the errors that caused the credential verification request to fail. | - `poll`

- `cancel`

- `sameDevice` | Indicates that credential verification is required.            |
| `CREDENTIAL_VERIFICATION_COMPLETED` | No model                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | * `continue`                         | Indicates that credential verification completed successfully. |
| `CREDENTIAL_VERIFICATION_FAILED`    | - `sessionID (string)`: The ID that can be used to check the status of the credential verification request.

- `sessionStatus (SessionStatus)`: The status of the credential verification request.

- `errorDetails (List<CustomAuthnErrorDetail>)`: A list of the errors that caused the credential verification request to fail.                                                                                                                                                                                                                                                                                                                                                          | * `cancel`                           | Indicates that credential verification failed.                 |
| `CREDENTIAL_VERIFICATION_TIMED_OUT` | No model                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | - `retryVerification`

- `cancel`    | Indicates that credential verification timed out.              |

## Action models

| Action              | Request Model | Errors | Description                                                                                                                                                                   |
| ------------------- | ------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cancel`            | No model      | None   | Cancels the verification flow.                                                                                                                                                |
| `continue`          | No model      | None   | Continues the verification flow.                                                                                                                                              |
| `poll`              | No model      | None   | Gets the current presentation session status.                                                                                                                                 |
| `retryVerification` | No model      | None   | Retries verification after time out or failure.                                                                                                                               |
| `sameDevice`        | No model      | None   | Indicates that the user prefers to complete verification on the same device. Learn more in [Overview of the SSO flow](../pf_p1_credentials_ik_overview_of_the_sso_flow.html). |

---

---
title: Overview of the SSO flow
description: With the PingOne Credentials Integration Kit, PingFederate includes PingOne Credentials in the sign-on flow.
component: pingone-credentials
page_id: pingone-credentials::pf_p1_credentials_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/pingone-credentials/pf_p1_credentials_ik_overview_of_the_sso_flow.html
revdate: August 28, 2024
section_ids:
  different-device-sso-flow-description: Different device SSO flow description
  same-device-sso-flow-description: Same device SSO flow description
---

# Overview of the SSO flow

With the PingOne Credentials Integration Kit, PingFederate includes PingOne Credentials in the sign-on flow.

## Different device SSO flow description

1. The user initiates SSO with PingFederate on their first device. For example, a laptop. They complete the first authentication step, which might be provided by an HTML Form Adapter instance, for example.

2. The PingOne Credentials IdP Adapter contacts PingOne Credentials to initiate the credential verification process.

3. PingOne Credentials provides a QR code image URL and a **Open Wallet** button URL to the adapter.

4. The PingOne Credentials IdP Adapter presents an HTML page that shows the QR code and **Open Wallet** button to the user on their first device.

5. The user scans the QR code through their wallet app on a second device.

6. The wallet app on the user's second device presents a consent prompt to the user to confirm whether the requested credentials can be presented for verification.

7. The user confirms or cancels the request.

8. If the user confirms that the requested credentials may be shared, the wallet app presents the requested credentials to PingOne Credentials for verification, following the configured **[Presentation Protocol](setup/pf_p1_credentials_ik_p1_credentials_idp_adapter_settings_reference.html)**.

9. The PingOne Credentials IdP Adapter polls PingOne Credentials while it waits for the result of the credential verification process.

10. PingOne Credentials provides the adapter with the result of the verification process.

11. (Optional) The PingOne Credentials IdP Adapter presents an HTML page on the user's first device that shows the success or failure message, depending on the verification result.

12. If the user completed the verification process successfully, PingFederate provides access to the requested resource on the user's first device.

## Same device SSO flow description

1. The user initiates SSO with PingFederate on the same device that their wallet app is on. For example, a cellphone. They complete the first authentication step, which might be provided by an HTML Form Adapter instance, for example.

2. The PingOne Credentials IdP Adapter contacts PingOne Credentials to initiate the credential verification process.

3. PingOne Credentials provides a QR code image URL and a **Open Wallet** button URL to the adapter.

4. The PingOne Credentials IdP Adapter presents an HTML page that shows the QR code and **Open Wallet** button to the user on the same device.

5. The user clicks **Open Wallet** and is redirected to the wallet app on the same device.

6. The wallet app presents a consent prompt to the user to confirm whether the requested credentials can be presented for verification.

7. If the user confirms that the requested credentials may be shared, the wallet app shares the requested credentials with PingOne Credentials, following the selected **[Presentation Protocol](setup/pf_p1_credentials_ik_p1_credentials_idp_adapter_settings_reference.html)**.

8. The PingOne Credentials IdP Adapter polls PingOne Credentials while it waits for the result of the verification process.

9. PingOne Credentials provides the adapter with the result of the credential verification process.

10. (Optional) The PingOne Credentials IdP Adapter presents an HTML page on the user's device that shows the success or failure message, depending on the verification result.

11. If the user completed the verification process successfully, PingFederate provides access to the requested resource on the same device.

---

---
title: PingOne Credentials IdP Adapter settings reference
description: Field descriptions for the PingOne Credentials IdP Adapter configuration screen.
component: pingone-credentials
page_id: pingone-credentials:setup:pf_p1_credentials_ik_p1_credentials_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/pingone-credentials/setup/pf_p1_credentials_ik_p1_credentials_idp_adapter_settings_reference.html
revdate: September 3, 2024
---

# PingOne Credentials IdP Adapter settings reference

Field descriptions for the PingOne Credentials IdP Adapter configuration screen.

**Standard fields**

| Field                                     | Description                                                                                                                                                                                                                              |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PingOne Environment**                   | For PingFederate 10.2 and later.Select the PingOne connection that you created in [Connecting PingFederate to PingOne](pf_p1_credentials_ik_connecting_pf_to_p1.html).This field is blank by default.                                    |
| **Environment ID**                        | For PingFederate 10.1 and earlier.The environment ID that you noted in [Connecting PingFederate to PingOne](pf_p1_credentials_ik_connecting_pf_to_p1.html).This field is blank by default.                                               |
| **Region**                                | For PingFederate 10.1 and earlier.Determines the PingOne API that the adapter communicates with.Select the region that appears on **Settings > Environment > Properties** in PingOne.                                                    |
| **PingFederate Connection Client ID**     | For PingFederate 10.1 and earlier.The client ID that you noted in [Connecting PingFederate to PingOne](pf_p1_credentials_ik_connecting_pf_to_p1.html). This is required for automatic device pairing.This field is blank by default.     |
| **PingFederate Connection Client Secret** | For PingFederate 10.1 and earlier.The client secret that you noted in [Connecting PingFederate to PingOne](pf_p1_credentials_ik_connecting_pf_to_p1.html). This is required for automatic device pairing.This field is blank by default. |
| **Digital Wallet Application**            | The name of the application that captures the mobile application attributes for the wallet. This list is populated when you select a **PingOne Environment**.                                                                            |
| **App Consent Prompt**                    | The message prompt that's shown to the user in the app before they consent to the presentation request.The default value is `Please accept`.                                                                                             |
| **Presentation Protocol**                 | The presentation protocol that the app should use to complete the presentation request. Available options are:- Ping Native

- OpenID4VP                                                                                                 |

**Advanced fields**

| Field                                     | Description                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Refresh Interval**                      | The interval, in milliseconds, at which the adapter checks if the credential has been shared.The default value is `5000`.                                                                                                                                                                                                                                  |
| **Cookie Signing Key**                    | The key that the adapter uses to sign application instance ID cookies. This value can't exceed 1000 characters.The default value is `some-secret-key`.                                                                                                                                                                                                     |
| **HTML Template Prefix**                  | Identifies the set of HTML templates that the adapter uses.If you customize the template file names in the `/server/default/conf/template` directory, enter the new prefix here.The default value is `pingone-credentials`.For a description of the template files, see [Download manifest](../release_notes/pf_p1_credentials_ik_download_manifest.html). |
| **Messages Files**                        | Identifies the customizable language-pack file that the adapter uses to show messages on the templates.If you customize the `pingone-credentials-messages.properties` file name in the `/server/default/conf/language-packs` directory, enter the new name here.The default value is `pingone-credentials-messages`.                                       |
| **Error Message Key Prefix**              | Identifies the error messages in the language-pack file that the adapter uses to show messages on the templates.If you customize the error message names in `/server/default/conf/language-packs/pingone-credentials-messages.properties`, enter the new prefix here.The default value is `pingone.credentials.error.`.                                    |
| **Allow Credential Verification Retries** | When credential verification fails, this setting determines whether to start a new session.This check box is cleared by default.                                                                                                                                                                                                                           |
| **Service Unavailable Failure Mode**      | When the adapter is unable to access PingOne, this setting determines whether the adapter should block the user's sign-on attempt or bypass authentication.The default selection is `Bypass authentication`.                                                                                                                                               |
| **Show Success Screens**                  | When the presentation session is successful, this setting determines whether the adapter shows a success page.This check box is selected by default.                                                                                                                                                                                                       |
| **Show Failed Screens**                   | When the presentation session fails, this setting determines whether the adapter shows a failure page.This check box is selected by default.                                                                                                                                                                                                               |
| **Show Timeout Screens**                  | When a presentation session times out, this setting determines whether the adapter shows a timeout page.This check box is selected by default.                                                                                                                                                                                                             |
| **State Timeout**                         | The amount of time in seconds that the adapter will stay in the same presentation session state before the adapter times out.The default value is `300`.The minimum value is `60`.                                                                                                                                                                         |
| **API Request Timeout**                   | The amount of time in milliseconds that PingFederate allows when establishing a connection with PingOne Credentials or waiting for a response to a request. A value of 0 disables the timeout.The default value is `5000`.                                                                                                                                 |
| **Proxy Settings**                        | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                                                                                                                                                |
| **Custom Proxy Host**                     | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                             |
| **Custom Proxy Port**                     | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                  |

---

---
title: PingOne Credentials Integration Kit
description: The PingOne Credentials Integration Kit allows PingFederate to verify and return requested credentials through a credential verification presentation session.
component: pingone-credentials
page_id: pingone-credentials::pf_p1_credentials_ik
canonical_url: https://docs.pingidentity.com/integrations/pingone-credentials/pf_p1_credentials_ik.html
revdate: August 27, 2024
section_ids:
  features: Features
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# PingOne Credentials Integration Kit

The PingOne Credentials Integration Kit allows PingFederate to verify and return requested credentials through a credential verification presentation session.

## Features

* Initiate a credential verification process as part of a user sign-on flow.

* Supports the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Supports the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

## Components

PingOne Credentials IdP Adapter

* Allows PingFederate to use PingOne Credentials to trigger a credential verification challenge as part of the PingFederate authentication policy.

Templates

* Allow the adapter to show the status of the credential verification process.

* Allow you to modify the appearance of pages shown to the user during authentication.

Language packs

* Allow you to customize or localize the messages returned by the PingFederate authentication application programming interface (API) and shown on the templates during authentication. Learn more in [Localizing messages for end users](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_local_message_end_users.html) in the PingFederate documentation.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following resources:

* [PingOne Credentials](https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_start.html) in the PingOne documentation

* The following sections of the PingFederate documentation:

  * [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html)

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

## System requirements

* PingFederate 11.2 or later

* To allow PingFederate to make outbound HTTPS connections, you might need to allow the following host names in your firewall:

  * https\://api.pingone.com, https\://api.pingone.asia, https\://api.pingone.com.au/, or https\://api.pingone.eu

  * https\://auth.pingone.com, https\://auth.pingone.asia, https\://auth.pingone.com.au/, or https\://auth.pingone.eu