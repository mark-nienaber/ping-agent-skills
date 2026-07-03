---
title: Access the Password Manager
description: After configuring PingFederate and deploying the application, users can access the Google Apps Password Manager using the URL below. You can find additional parameters in System-service endpoints in the PingFederate Administrator's Manual.
component: google
page_id: google:google_workspace_provisioner:pf_google_workforce_connector_access_the_password_manager
canonical_url: https://docs.pingidentity.com/integrations/google/google_workspace_provisioner/pf_google_workforce_connector_access_the_password_manager.html
revdate: June 24, 2024
---

# Access the Password Manager

After configuring PingFederate and deploying the application, users can access the Google Apps Password Manager using the URL below. You can find additional parameters in [System-service endpoints](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_sys_services_endpoints.html) in the PingFederate Administrator's Manual.

|   |                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you have configured more than one IdP-to-SP adapter mapping, you must specify the SP-adapter instance ID as the value for the query parameter `SpSessionAuthnAdapterId`. |

`http[s]://<pf_host>:<port>/pf/adapter2adapter.ping?TargetResource=http[s]://<g_apps_pm_host>:<port>/gapps-password-manager/ResetPassword`

where:

* `<pf_host>:<port>` is the PingFederate host server name or IP address and port number.

* `<g_apps_pm_host>:<port>` is the host server name or IP address and port number where the Password Manager is deployed (may be the same as for PingFederate).

---

---
title: Available user attributes reference
description: The Google IdP Adapter can retrieve the following user attributes from Google.
component: google
page_id: google:google_login_integration_kit:pf_google_cic_available_user_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/google/google_login_integration_kit/pf_google_cic_available_user_attributes_reference.html
revdate: June 24, 2024
---

# Available user attributes reference

The Google IdP Adapter can retrieve the following user attributes from Google.

To retrieve a specific attribute, configure the Google IdP Adapter instance in two places:

* On the **IdP Adapter** screen, select the **Attribute Retrieval** option for the attribute.

* On the **Extended Contract** screen, add the attribute.

The `email` attribute is always available.

For more information about these attributes, see [Users](https://developers.google.com/admin-sdk/directory/v1/reference/users#resource) in the Google documentation.

**Attribute Retrieval: Email**

| Attribute Name | Description                                                                             |
| -------------- | --------------------------------------------------------------------------------------- |
| `sub`          | The subject identifier of the authenticated user.                                       |
| `email`        | The email address of the authenticated user. This value is retrieved from the ID token. |

**Attribute Retrieval: Basic Profile**

| Attribute Name   | Description                                                                                                                               |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `sub`            | The subject identifier of the authenticated user.                                                                                         |
| `email`          | The email address of the authenticated user. This value is retrieved from the ID token.                                                   |
| `name`           | The user's full name.                                                                                                                     |
| `given_name`     | The user's first name.                                                                                                                    |
| `family_name`    | The user's last name.                                                                                                                     |
| `locale`         | The user's preferred locale.                                                                                                              |
| `hd`             | The hosted domain name of the user's G Suite account, such as `example.com`.                                                              |
| `email_verified` | A boolean flag that indicates the verification status of the user's email address. A value of `true` means the email address is verified. |

**Attribute Retrieval: Extended Profile**

| Attribute Name | Description                                                                             |
| -------------- | --------------------------------------------------------------------------------------- |
| `email`        | The email address of the authenticated user. This value is retrieved from the ID token. |
| `kind`         | Identifies this resource as a person in OpenID Connect format.                          |
| `id`           | The user's unique ID.                                                                   |
| `givenName`    | The user's first name.                                                                  |
| `familyName`   | The user's last name.                                                                   |
| `fullName`     | The user's full name.                                                                   |
| `externalIds`  | The raw JSON string.                                                                    |
| `groups`       | A multi-value list of groups that the user is a member of.                              |

---

---
title: Changelog
description: The following is the change history for the Google Chrome Enterprise Integration Kit.
component: google
page_id: google:google_chrome_enterprise_integration_kit:pf_google_chrome_enterprise_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/google/google_chrome_enterprise_integration_kit/pf_google_chrome_enterprise_ik_changelog.html
revdate: April 8, 2026
section_ids:
  version-1-0-2: Version 1.0.2
  version-1-0-1: Version 1.0.1
  version-1-0: Version 1.0
---

# Changelog

The following is the change history for the Google Chrome Enterprise Integration Kit.

## Version 1.0.2

Released in April 2026.

* Updated the Jackson Core library to address a potential security vulnerability.

## Version 1.0.1

Released in September 2025.

* Updated the dependencies that the Google Chrome Enterprise Integration Kit uses.

## Version 1.0

Released in December 2023.

* Initial release

---

---
title: Changelog
description: The following is the change history for the Google Login Integration Kit.
component: google
page_id: google:google_login_integration_kit:pf_google_cic_changelog
canonical_url: https://docs.pingidentity.com/integrations/google/google_login_integration_kit/pf_google_cic_changelog.html
revdate: February 19, 2026
section_ids:
  version-1-5-3-january-2026: Version 1.5.3 - January 2026
  version-1-5-2-march-2025: Version 1.5.2 - March 2025
  version-1-5-1-november-2022: Version 1.5.1 - November 2022
  version-1-5-september-2020: Version 1.5 - September 2020
  version-1-4-1-june-2019: Version 1.4.1 - June 2019
  version-1-4-may-2019: Version 1.4 - May 2019
  version-1-3-february-2019: Version 1.3 - February 2019
  version-1-2-august-2018: Version 1.2 - August 2018
  version-1-1-1-june-2016: Version 1.1.1 - June 2016
  version-1-1-april-2015: Version 1.1 - April 2015
  version-1-0-1-may-2015: Version 1.0.1 - May 2015
  version-1-0-may-2014: Version 1.0 - May 2014
---

# Changelog

The following is the change history for the Google Login Integration Kit.

## Version 1.5.3 - January 2026

* Removed third-party fonts and the `authn-api-messages.properties` file.

## Version 1.5.2 - March 2025

* Fixed a vulnerability where unconsumed non-`200` HTTP responses could impact Jetty thread availability, potentially leading to service disruption or Denial of Service. Users should upgrade to mitigate any potential risks.

## Version 1.5.1 - November 2022

* Fixed an issue that caused the Google IdP adapter to not encode spaces in scopes.

* Fixed an issues that caused an error when configuring the Google login adapter with custom proxy and host settings.

## Version 1.5 - September 2020

* Added the ability to show the Google sign-on prompt in a pop-up window for environments that block the automatic redirect.

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Added settings for retrying failed requests.

* Added settings for API connection and request timeouts.

* Added settings to override the PingFederate system-default proxy settings.

## Version 1.4.1 - June 2019

* Fixed an issue that caused an error in upgrade scenarios.

## Version 1.4 - May 2019

* Added support for retrieving group memberships in the adapter configuration and extended contract.

* Added the ability to override the system-default proxy settings in the adapter configuration.

* Added the ability to configure timeout durations in the adapter configuration.

* Added support for virtual host names. In the adapter configuration, **PingFederate Base URL** is now an optional override field. Learn more in [Virtual host names](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_virtual_host_names.html) in the PingFederate documentation.

## Version 1.3 - February 2019

* Updated the adapter to use a different user data source in preparation for the shutdown of the Google+ API.

## Version 1.2 - August 2018

* Resolved an iframe issue with SLO.

* Added support to periodically retry a failed request with increasing delays between retries.

* Improved logging for error scenarios.

* Removed the bundled OAuth CIC helper as Ping Identity's OAuth Configuration Service replaces the functionality.

## Version 1.1.1 - June 2016

* Resolved an issue with using the Google IdP Adapter within a Composite Adapter.

## Version 1.1 - April 2015

* Upgraded the adapter interface to V2 of the PingFederate SDK (IdpAuthenticationAdapterV2).

* Added username attribute to the Basic and Extended Profile schemas.

* Added support for additional attributes to the Extended Profile schema.

* Added mitigation for Google API throttling through the use of the quotaUser parameter.

* Minor bug fixes.

## Version 1.0.1 - May 2015

* Added support for openid\_id parameter.

* Security enhancements.

## Version 1.0 - May 2014

* Initial release.

---

---
title: Complete setup of SAML SSO to Google Apps
description: In order to setup your Google Apps account for SSO you will need to do the following.
component: google
page_id: google:google_workspace_provisioner:pf_google_workforce_connector_complete_setup_of_saml_sso_to_google_apps
canonical_url: https://docs.pingidentity.com/integrations/google/google_workspace_provisioner/pf_google_workforce_connector_complete_setup_of_saml_sso_to_google_apps.html
revdate: June 24, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Complete setup of SAML SSO to Google Apps

## About this task

In order to setup your Google Apps account for SSO you will need to do the following.

|   |                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This section requires the exported certificate used to sign the SAML assertion configured in step 5 of [Creating a connection](pf_google_workforce_connector_creating_a_connection.html). |

## Steps

1. Go to `https://admin.google.com/<domain_name>/` and sign in with your Administrator credentials.

2. Go to **Security** to view the **Set up single sign-on (SSO)** section.

3. Select **Setup SSO with third party identity provider**.

4. Enter the PingFederate SSO SAML endpoint in the **Sign-in page URL** field.

   ```
   https://<pf_host>:<pf_port>/idp/SSO.saml2
   ```

5. (Optional) Enter the PingFederate SLO SAML endpoint in the **Sign-out page URL** field.

   ```
   https://<pf_host>:<pf_port>/idp/SLO.saml2
   ```

6. (Optional) Enter the Password Manager URL in the **Change password URL** field.

   ```
   http[s]://<pf_host>:<port>/pf/adapter2adapter.ping?TargetResource=http[s]://<g_apps_pm_host>:<port>/gapps-password-manager/ResetPassword
   ```

7. Upload the signing certificate exported from PingFederate in the **Verification certificate** field.

8. Select **Use a domain specific issuer** if applicable.

   ![iul1563995381411](_images/iul1563995381411.png)

9. Click **Save** to complete Google Apps SSO Setup.

   |   |                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Learn more about Google Apps SSO setup in [Set up SSO via a third-party Identity provider](https://support.google.com/a/answer/60224?hl=en\&ref_topic=6348126) in the Google Workspace Admin Help. |

---

---
title: Configure and Deploy the Password Manager
description: Copy gapps-password-manager.war from the dist/gapps-password-manager directory to either:
component: google
page_id: google:google_workspace_provisioner:pf_google_workforce_connector_configure_and_deploy_the_password_manager
canonical_url: https://docs.pingidentity.com/integrations/google/google_workspace_provisioner/pf_google_workforce_connector_configure_and_deploy_the_password_manager.html
revdate: June 24, 2024
section_ids:
  steps: Steps
---

# Configure and Deploy the Password Manager

## Steps

1. Copy `gapps-password-manager.war` from the `dist/gapps-password-manager` directory to either:

   `<pf_install>/pingfederate/server/default/deploy/`

   Or the application-deployment directory in a different Web-servlet container of your choice.

2. In the directory `gapps-password-manager.war/WEB-INF/classes`, edit the file `gapps-password-manager-config.props`, to provide valid client id, client secret, and oauth tokens for Google Apps.

   Follow the instructions in [Obtain an application name, client ID, and secret](pf_google_workforce_connector_obtain_an_application_name,_client_id,_and_secret.html) section of this guide to obtain the client id and secret. Refer to [Generate authorized OAuth 2.0 tokens](pf_google_workforce_connector_generate_authorized_oauth_20_tokens.html) for instructions on obtaining the token values.

   |   |                                                                                                                                                                                                                                                                                                                                                |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can use the `obfuscate.bat\|sh` utility to mask the client secret, access token and refresh token value in the configuration file (recommended). The utility is located in the `<pf-install>/pingfederate/bin` directory. Make sure to run the obfuscate utility with `-l` flag.Example: `obfuscate.[bat\|sh] -l <Value to be obfuscated>` |

   As an option in this file, you may also change the default specifications (usable characters and length) for the randomly generated reset passwords that users will receive from the Password Manager.

3. Copy the `agent-config.txt` file, which was exported during the SP adapter, configuration, into the same directory. Learn more in [SP Adapter Setup](pf_google_workforce_connector_sp_adapter_setup.html).

   `../gapps-password-manager.war/WEB-INF/classes/`

4. Start or restart PingFederate, or the servlet container in which the Manager is installed.

---

---
title: Configuring an adapter instance
description: Configure the Google Chrome Enterprise Device Trust IdP Adapter to determine how PingFederate communicates with Google Chrome Enterprise.
component: google
page_id: google:google_chrome_enterprise_integration_kit:pf_google_chrome_enterprise_ik_configuring_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/google/google_chrome_enterprise_integration_kit/pf_google_chrome_enterprise_ik_configuring_adapter_instance.html
revdate: June 24, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  result: Result:
---

# Configuring an adapter instance

Configure the Google Chrome Enterprise Device Trust IdP Adapter to determine how PingFederate communicates with Google Chrome Enterprise.

## About this task

To get started with the integration, deploy the Google Chrome Enterprise Integration Kit files to your PingFederate directory.

## Steps

1. In the PingFederate administrative console, go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. From the **Type** list, select **Google Chrome Enterprise Device Trust IdP Adapter**. Click **Next**.

3. On the **IdP Adapter** tab, in the **Google Verified Access API Response Mappings** section, map attributes from the Google Verified Access API response to the attribute contract:

   1. Click **Add a new row to 'Google Verified Access API Response Mappings'**.

   2. In the **Local Attribute** field, enter a name for an attribute.

   3. In the **Google Verified Access API Response Mapping** field, enter the JSON Pointer syntax for the source Google Verified Access API attributes as shown in [JSON Pointer syntax reference](pf_google_chrome_enterprise_ik_json_syntax_reference.html).

      ### Example:

      The JSON pointer `/deviceSignals/displayName` returns the machine display name.

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a - d.

      ### Result:

      These attributes become available in your PingFederate authentication policy.

4. On the **IdP Adapter** tab, configure the adapter instance by referring to [Google Chrome Enterprise Device Trust IdP Adapter settings reference](pf_google_chrome_enterprise_ik_adapter_settings.html). Click **Next**.

5. On the **Actions** tab, test your connection to Google Chrome Enterprise. Resolve any issues that are reported, and then click **Next**.

6. On the **Extended Contract** tab, add any attributes that you included in the **Google Verified Access API Response Mappings** section of the **IdP Adapter** tab. Click **Next**.

7. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

8. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

9. On the **Summary** tab, review your configuration and then click **Save**.

---

---
title: Configuring an adapter instance
description: Configure the Google IdP Adapter to determine how PingFederate communicates with the Google API.
component: google
page_id: google:google_login_integration_kit:pf_google_cic_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/google/google_login_integration_kit/pf_google_cic_configuring_an_adapter_instance.html
revdate: January 6, 2026
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Configure the Google IdP Adapter to determine how PingFederate communicates with the Google API.

## Steps

1. In the PingFederate admin console, go to **Authentication > Integration > IdP Adapters** and click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **Google IdP Adapter**. Click **Next**.

3. On the **IdP Adapter** tab, configure the adapter instance by referring to [Google IdP Adapter settings reference](pf_google_cic_google_idp_adapter_settings_reference.html). Click **Next**.

4. On the **Extended Contract** tab, add any attributes that you want to include in the contract. Click **Next**.

   1. Add each attribute associated with the **Attribute Retrieval** setting you selected.

      For a list of attributes associated with each **Attribute Retrieval** setting, see [Available user attributes reference](pf_google_cic_available_user_attributes_reference.html).

   2. If you changed the **Authentication URL** to expose the `openid_id` parameter, add `openid_id`.

5. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

6. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

7. On the **Summary** tab, check your configuration, then click **Save**.

---

---
title: Configuring SSO to an application within the PingFederate domain
description: To enable SSO to an application within the PingFederate domain, configure an adapter-to-adapter mapping.
component: google
page_id: google:google_login_integration_kit:pf_google_cic_configuring_sso_to_an_application_within_the_pf_domain
canonical_url: https://docs.pingidentity.com/integrations/google/google_login_integration_kit/pf_google_cic_configuring_sso_to_an_application_within_the_pf_domain.html
revdate: June 24, 2024
section_ids:
  steps: Steps
---

# Configuring SSO to an application within the PingFederate domain

To enable SSO to an application within the PingFederate domain, configure an adapter-to-adapter mapping.

## Steps

1. On the PingFederate administrative console, create an SP adapter instance to integrate with your web application.

   For an overview of SP adapters, see [Managing SP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_adaptermanagementtasklet_spadaptermanagementstate.html) in the PingFederate documentation. For most use cases, we recommend the Reference ID Adapter included in the [Agentless Integration Kit](../../agentless/pf_agentless_ik.html).

2. Map the attributes from your Google IdP Adapter instance to the SP adapter instance by creating an adapter-to-adapter mapping. For instructions, see [Adapter-to-adapter mappings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_adaptertoadapter_mappings.html) in the PingFederate documentation.

3. In your web application, add sign-on hyperlink based on the following URL:

   ```
   https://pf_host:pf_port/pf/adapter2adapter.ping?IdpAdapterId=IdpAdapterId&SpSessionAuthnAdapterId=SpAdapterId
   ```

   |                |                                                         |
   | -------------- | ------------------------------------------------------- |
   | *pf\_host*     | The host name or IP address of the PingFederate server. |
   | *pf\_port*     | The port number of the PingFederate server.             |
   | *IdpAdapterId* | The instance ID of the IdP adapter instance.            |
   | *SpAdapterId*  | The instance ID of the SP adapter instance.             |

---

---
title: Configuring SSO to an SP outside the PingFederate domain
description: To enable SSO to a service provider (SP) outside the PingFederate domain, configure an SP connection and add a sign-on link to the SP application.
component: google
page_id: google:google_login_integration_kit:pf_google_cic_configuring_sso_to_an_sp_outside_the_pf_domain
canonical_url: https://docs.pingidentity.com/integrations/google/google_login_integration_kit/pf_google_cic_configuring_sso_to_an_sp_outside_the_pf_domain.html
revdate: June 24, 2024
section_ids:
  steps: Steps
---

# Configuring SSO to an SP outside the PingFederate domain

To enable SSO to a service provider (SP) outside the PingFederate domain, configure an SP connection and add a sign-on link to the SP application.

## Steps

1. Create an SP connection and select your Google IdP Adapter instance on the **Authentication Source Mapping** tab.

   For detailed instructions, see [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html) in the PingFederate documentation.

2. In your web application, add sign-on hyperlink based on the following URL:

   ```
   https://pf_host:pf_port/idp/startSSO.ping?PartnerSpId=ConnectionId
   ```

   |                |                                                         |
   | -------------- | ------------------------------------------------------- |
   | *pf\_host*     | The host name or IP address of the PingFederate server. |
   | *pf\_port*     | The port number of the PingFederate server.             |
   | *ConnectionId* | The ID of the SP connection.                            |

---

---
title: Creating a connection
description: To allow PingFederate to act as an identity provider and manage users in Google Workspace, create a service provider (SP) connection.
component: google
page_id: google:google_workspace_provisioner:pf_google_workforce_connector_creating_a_connection
canonical_url: https://docs.pingidentity.com/integrations/google/google_workspace_provisioner/pf_google_workforce_connector_creating_a_connection.html
revdate: July 23, 2024
section_ids:
  steps: Steps
---

# Creating a connection

To allow PingFederate to act as an identity provider and manage users in Google Workspace, create a service provider (SP) connection.

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details with the Google Workspace quick connection template.

   1. On the **Connection Template** tab, select **Use a template for this connection**.

   2. From the **Connection Template** list, select **Google Workspace Provisioner**.

   3. In the **Google Domain** field, the Google Domain used by your organization for SSO access to Google Apps.

      |   |                                                                                                                                                                                                                                                                                                |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If your Google Apps administrative implementation supports more than one domain, select the **USE A DOMAIN SPECIFIC ISSUER** checkbox under the Google Domain. Checking this box allows you to configure additional SP connections for other domains at your site registered with Google Apps. |

   4. On the **Connection Type** tab select **Browser SSO Profiles** and **Outbound Provisioning**. Click **Next**.

   5. On the **Connection Options** tab, click **Next**.

   6. On the **General Info** tab, in the **Connection Name** field, enter a name of your choosing. Click **Next**.

3. On the **Browser SSO** tab, configure browser SSO.

   For more information, see [Configuring IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation.

   1. On the **Browser SSO > SAML Profiles** tab, select only **SP-Initiated SSO**.

   2. On the **Browser SSO > Protocol Settings > Allowable SAML Bindings** tab, select only **Redirect**.

4. On the **Browser SSO > Protocol Settings > Signature Policy** tab, select the **Always sign the SAML Assertion** check box. Click **Next**.

5. On the **Credentials** tab, configure the connection credentials as shown in [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation. Click **Next**.

6. On the **Outbound Provisioning** tab, configure provisioning with the following details.

   For help, see [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

   1. On the **Target** tab, complete the fields as follows.

      | Field Name                   | Description                                                                                                                                                                                                                                                                                                                                                                |
      | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | **Application Name**         | The Application Name for the application created in Google Apps.For more information on obtaining an application name, client Id and secret, see [Obtain an application name, client ID, and secret](pf_google_workforce_connector_obtain_an_application_name,_client_id,_and_secret.html).                                                                                |
      | **Domain**                   | The Domain for the Google Apps account.                                                                                                                                                                                                                                                                                                                                    |
      | **OAuth Access Token**       | The OAuth Access Token generated by the OAuth Configuration Service.For more information on obtaining authorized OAuth tokens, see the [Generate authorized OAuth 2.0 tokens](pf_google_workforce_connector_generate_authorized_oauth_20_tokens.html).                                                                                                                     |
      | **Oauth Client ID**          | The Oauth client ID for the application created in Google Apps.For more information on obtaining an application name, client Id and secret, see [Obtain an application name, client ID, and secret](pf_google_workforce_connector_obtain_an_application_name,_client_id,_and_secret.html).                                                                                 |
      | **Oauth Client Secret**      | The Oauth client secret generated during application creation for Google Apps.                                                                                                                                                                                                                                                                                             |
      | **OAuth Refresh Token**      | The OAuth refresh token generated by the OAuth Configuration Service.                                                                                                                                                                                                                                                                                                      |
      | **User Create**              | **Selected** (default) – PingFederate creates users in Google Apps.**Cleared** - PingFederate does not create users in Google Apps.                                                                                                                                                                                                                                        |
      | **User Update**              | **Selected** (default) – PingFederate updates existing users in Google Apps.**Cleared** - PingFederate does not update existing users in Google Apps.                                                                                                                                                                                                                      |
      | **User Disable/Delete**      | **Selected** (default) – PingFederate disables or deletes users in Google Apps.&#xA;&#xA;PingFederate can only re-enable a user if User Update is selected.**Cleared** – PingFederate does not disable or delete users in Google Apps.                                                                                                                                     |
      | **Provision Disabled Users** | This option applies when:- the **User Create** option is selected, and

      - the provisioning engine targets a user in the data store that has a "disabled" status.**Selected** (default) – PingFederate creates the user in Google Apps with a "disabled" status.**Cleared** – PingFederate does not create the user in Google Apps.                                         |
      | **Remove User Action**       | This option applies when:- **User Disable/Delete** is selected, and

      - a previously-provisioned user no longer meets the condition set on the **Source Location** screen, or

      - a user has been disabled or deleted from the data store.**Disable** (default) – PingFederate disables the user in Google Apps.**Delete** – PingFederate deletes the user from Google Apps. |

7. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: Deploying the Application
description: The Password Manager is located in the Google Workspace Provisioner distribution package in the form of an extracted Web archive (WAR). The WAR directory can be installed and deployed either within PingFederate or inside a separate Web servlet container.
component: google
page_id: google:google_workspace_provisioner:pf_google_workforce_connector_deploying_the_application
canonical_url: https://docs.pingidentity.com/integrations/google/google_workspace_provisioner/pf_google_workforce_connector_deploying_the_application.html
revdate: June 24, 2024
---

# Deploying the Application

The Password Manager is located in the Google Workspace Provisioner distribution package in the form of an extracted Web archive (WAR). The WAR directory can be installed and deployed either within PingFederate or inside a separate Web servlet container.

After the WAR is installed, one configuration file must be modified. An additional SP-adapter configuration file must be added before the application can be deployed. Learn more in [Creating a connection](pf_google_workforce_connector_creating_a_connection.html).

* [Configure and Deploy the Password Manager](pf_google_workforce_connector_configure_and_deploy_the_password_manager.html)

* [Access the Password Manager](pf_google_workforce_connector_access_the_password_manager.html)

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Google Chrome Enterprise Integration Kit files to your PingFederate directory.
component: google
page_id: google:google_chrome_enterprise_integration_kit:pf_google_chrome_enterprise_ik_deploying_integration_files
canonical_url: https://docs.pingidentity.com/integrations/google/google_chrome_enterprise_integration_kit/pf_google_chrome_enterprise_ik_deploying_integration_files.html
revdate: June 24, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Google Chrome Enterprise Integration Kit files to your PingFederate directory.

## Before you begin

Sign up for Chrome Browser Cloud Management and enroll cloud-managed Chrome browsers. For more information, see [Chrome Browser Cloud Management](https://support.google.com/chrome/a/answer/9116814?sjid=16357975367494130609-NC).

## Steps

1. Download the Google Chrome Enterprise Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/google-chrome-enterprise-integration).

2. Stop PingFederate.

3. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Start PingFederate.

5. If you operate PingFederate in a cluster, repeat steps 2-4 for each engine node.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Google Workspace Provisioner files to your PingFederate directory.
component: google
page_id: google:google_workspace_provisioner:pf_google_workforce_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/google/google_workspace_provisioner/pf_google_workforce_connector_deploying_the_integration_files.html
revdate: June 24, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deploying the integration files

## About this task

To get started with the integration, deploy the Google Workspace Provisioner files to your PingFederate directory.

## Steps

1. Download the Google Workspace Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/google-workspace-provisioner).

2. Stop the PingFederate server if it is running.

3. Remove any existing Google Workspace Provisioner files from the directory:

   `<PF_install>/pingfederate/server/default/deploy`

4. Unzip the distribution file and copy the contents of the `/dist` directory to the PingFederate directory:

   `<PF_install>/pingfederate/server/default/deploy`

5. Edit the `run.properties` file located in `<pf_install>/pingfederate/bin`, changing the property `pf.provisioner.mode` to the value shown here:

   `pf.provisioner.mode=STANDALONE`

   The property is located near the end of the file.

   For information about using the `FAILOVER` setting for runtime deployment, see the PingFederate [Server Clustering Guide](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_server_clustering_guide.html).

6. Start or restart the PingFederate server.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Google Login Integration Kit files to your PingFederate directory.
component: google
page_id: google:google_login_integration_kit:pf_google_cic_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/google/google_login_integration_kit/pf_google_cic_deploying_the_integration_files.html
revdate: June 24, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Google Login Integration Kit files to your PingFederate directory.

## About this task

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | If you operate PingFederate in a cluster, the following steps refer to the console node. |

## Steps

1. Download the Google Login Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/google-login-integration-kit).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, back up your customizations and delete earlier versions of the integration files:

   1. Back up any Google Login Integration Kit files that you customized in the `<pf_install>/pingfederate/server/default/conf/` directory.

   2. Delete the `pf-google-adapter-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. If there is more than one version of the `pf-authn-api-sdk-<version>.jar` file in your `<pf_install>/pingfederate/server/default/lib` directory, delete all but the latest version of the file.

6. If you backed up any customized files, modify the new files with your customizations.

7. Start PingFederate.

8. If you operate PingFederate in a cluster, repeat steps 2-8 for each engine node.

---

---
title: Download manifest
description: The following files are included in the Google Chrome Enterprise Integration Kit .zip archive.
component: google
page_id: google:google_chrome_enterprise_integration_kit:pf_google_chrome_enterprise_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/google/google_chrome_enterprise_integration_kit/pf_google_chrome_enterprise_ik_download_manifest.html
revdate: June 24, 2024
---

# Download manifest

The following files are included in the Google Chrome Enterprise Integration Kit `.zip` archive.

* `Legal.pdf` – copyright and license information

* `dist/pingfederate/server/default` – contains the integration files

  * `deploy` – contains the Java libraries

    * `pf-google-chrome-enterprise-adapter-<version>.jar` – The Google Chrome Enterprise Device Trust IdP Adapter

---

---
title: Download manifest
description: The distribution .zip archive for the Google Workspace Provisioner contains the following:
component: google
page_id: google:google_workspace_provisioner:pf_google_workforce_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/google/google_workspace_provisioner/pf_google_workforce_connector_download_manifest.html
revdate: June 24, 2024
---

# Download manifest

The distribution `.zip` archive for the Google Workspace Provisioner contains the following:

* `dist` – contains the integration files

  * `gapps-password-manager.war` – The Google Password Manager Application

  * `pf-google-quickconnection-<version>.jar`– PingFederate Google Workspace Provisioner

* `legal/Legal.pdf` – copyright and license information.

---

---
title: Download manifest
description: The following files are included in the Google Login Integration Kit .zip archive:
component: google
page_id: google:google_login_integration_kit:pf_google_cic_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/google/google_login_integration_kit/pf_google_cic_download_manifest.html
revdate: January 21, 2026
---

# Download manifest

The following files are included in the Google Login Integration Kit `.zip` archive:

* `ReadMeFirst.pdf` – contains links to this online documentation

* `Legal.pdf` – copyright and license information

* `dist` – contains the integration files

  * `deploy` – contains the Java libraries

    * `pf-google-adapter-<version>.jar` – JAR file that contains the Google IdP Adapter.

  * `conf` – contains the HTML template that presents the Google sign-on form.

    * `language-packs` – contains files with customizable user-facing messages

      * `google-messages.properties` – a variable file that customizes the messages that appear on the template file.

    * `template` – contains user-facing HTML template files

      * `google-pop-up-template.html` – a page that presents the Google sign-on window in the **Pop-up window** sign-on presentation mode.

      * `google-post-auth-template.html` – a page that signals the main template or authentication widget to continue the authentication flow in the **Pop-up window** sign-on presentation mode.

      * `assets` – contains functional scripts and files used by the template

        * `css/google.css` – a CSS file that customizes the appearance of the template file.

        * `fonts/end-user` - contains template fonts and icons

          * `icons` - contains template icons

        * `images` – contains template image files

          * `ping-logo.svg` – an image file with company branding

  * `lib/pf-authn-api-sdk-<version>.jar` – a JAR file that contains the PingFederate Authentication API SDK

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can optionally turn on activity logging for PingFederate, the Google Chrome Enterprise Device Trust IdP Adapter, or both.
component: google
page_id: google:google_chrome_enterprise_integration_kit:pf_google_chrome_enterprise_ik_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/google/google_chrome_enterprise_integration_kit/pf_google_chrome_enterprise_ik_enabling_debug_logging.html
revdate: June 24, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can optionally turn on activity logging for PingFederate, the Google Chrome Enterprise Device Trust IdP Adapter, or both.

## About this task

You can use logging for troubleshooting or analytics.

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

3. To log activity relating to the Google Chrome Enterprise Device Trust IdP Adapter:

   ### Choose from:

   * To log activity for the Google Chrome Enterprise Device Trust IdP Adapter as well as its HTTPS and component activity, add the following line:

     ```
     <Logger name="com.pingidentity.adapters.google.chrome.enterprise.device.trust" level="DEBUG"/>
     ```

   * To log activity for the adapter's HTTPS activity and other components but not for the adapter itself, add the following line:

     ```
     <Logger name="com.pingidentity.adapters.google.chrome.enterprise.device.trust.shade" level="DEBUG"/>
     ```

   * To log activity for the Google Chrome Enterprise Device Trust IdP Adapter but not its HTTPS or component activity, add the following lines:

     ```
     <Logger name="com.pingidentity.adapters.google.chrome.enterprise.device.trust" level="DEBUG"/>
     <Logger name="com.pingidentity.adapters.google.chrome.enterprise.device.trust.shade" level="INFO"/>
     ```

4. Save the file.

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.
component: google
page_id: google:google_login_integration_kit:pf_google_cic_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/google/google_login_integration_kit/pf_google_cic_enabling_debug_logging.html
revdate: June 24, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.

## About this task

These steps are optional. For general information about logging, see [Enabling debug messages and console logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html)in the PingFederate documentation.

## Steps

1. Open the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file for editing.

2. If you want to log activity for PingFederate and all adapters, do the following.

   1. Find the following section.

      ```xml
      <AsyncRoot level="INFO" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   2. Change `INFO` to `DEBUG`.

      ```xml
      <AsyncRoot level="DEBUG" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   3. If you want to see the adapter activity in the console, remove the comment tags.

      ```xml
      <AsyncRoot level="INFO" includeLocation="false">
      	<AppenderRef ref="CONSOLE" />
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

3. If you want to log activity just for the Google IdP Adapter, add the following line.

   ```
   <Logger name="com.pingidentity.adapters.idp.google" level="DEBUG"/>
   ```

4. If you want to log all HTTP requests and responses with the Google API, add the following line.

   ```
   <Logger name="org.shaded.googlecic.apache.wire" level="DEBUG"/>
   ```

5. Save the file.