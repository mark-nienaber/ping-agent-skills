---
title: Adding SSO to a connection
description: To enable single sign-on (SSO) to Workplace from Facebook, modify the provisioning connection that you created in Creating a provisioning connection.
component: facebook
page_id: facebook:workplace_from_facebook_provisioner:pf_workplace_connector_adding_sso_to_a_connection
canonical_url: https://docs.pingidentity.com/integrations/facebook/workplace_from_facebook_provisioner/pf_workplace_connector_adding_sso_to_a_connection.html
revdate: June 11, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Adding SSO to a connection

To enable single sign-on (SSO) to Workplace from Facebook, modify the provisioning connection that you created in [Creating a provisioning connection](pf_workplace_connector_creating_a_provisioning_connection.html).

## Steps

1. On the PingFederate administrator console, open your existing SP connection.

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Select your connection.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Select your connection.

2. On the **Connection Type** tab select **Browser SSO Profiles**. Click **Next**.

3. On the **Browser SSO** tab, configure your SSO settings.

   1. Go to **Browser SSO > SAML Profiles** and select only **IdP-Initiated SSO** and **SP-Initiated SSO**.

   2. Go to **Browser SSO > Assertion Creation > Attribute Contract**. For **SAML\_SUBJECT**, select **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

   3. On the **Authentication Policy Mapping** tab, select or create an authentication source that maps `SAML_SUBJECT` to an email attribute that matches the email addresses used in Workplace from Facebook.

   For configuration help, see [Configuring IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation.

4. On the **Credentials** tab, configure the connection credentials as shown in [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation.

   * On the **Digital Signature Settings** tab, from the **Signing Certificate** list, select the certificate that you want to use with Workplace from Facebook.

5. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: App secret proof feature
description: "The \"app secret proof\" feature can protect your integration from being compromised or misused."
component: facebook
page_id: facebook:workplace_from_facebook_provisioner:pf_workplace_connector_app_secret_proof_feature
canonical_url: https://docs.pingidentity.com/integrations/facebook/workplace_from_facebook_provisioner/pf_workplace_connector_app_secret_proof_feature.html
revdate: June 11, 2024
---

# App secret proof feature

The "app secret proof" feature can protect your integration from being compromised or misused.

The provisioning connector uses an access token to communicate with Workplace from Facebook. Because access tokens are portable, they can be stolen by malicious software on a person's computer or by using a "man in the middle" attack. That access token can then be used from an unauthorized third party to generate spam or steal data.

To ensure that API calls are only ever made from authorized server-side code, Workplace from Facebook recommends that you set your custom integration to require an "app secret proof".

When the feature is enabled and configured in PingFederate, the provisioning connector uses the app secret to send a short-lived app secret proof along with the access token when making API calls to Workplace from Facebook. This can have a minor effect on performance.

For official documentation on this feature, see [App Secret Proof](https://developers.facebook.com/docs/workplace/reference/permissions/#appsecretproof) and [Securing Graph API Requests](https://developers.facebook.com/docs/graph-api/securing-requests/) in the Workplace from Facebook documentation.

---

---
title: Changelog
description: The following is the change history for the Facebook Login Integration Kit.
component: facebook
page_id: facebook:facebook_login_integration_kit:pf_facebook_cic_changelog
canonical_url: https://docs.pingidentity.com/integrations/facebook/facebook_login_integration_kit/pf_facebook_cic_changelog.html
revdate: February 19, 2026
section_ids:
  version-2-1-1-january-2026: Version 2.1.1 - January 2026
  version-2-1-august-2020: Version 2.1 – August 2020
  version-2-0-1-november-2018: Version 2.0.1 – November 2018
  version-2-0-february-2018: Version 2.0 – February 2018
  version-1-3-2-march-2017: Version 1.3.2 – March 2017
  version-1-3-march-2015: Version 1.3 – March 2015
  version-1-2-2-july-2013: Version 1.2.2 – July 2013
  version-1-2-1-may-2013: Version 1.2.1 – May 2013
  version-1-2-february-2013: Version 1.2 – February 2013
  version-1-1-march-2011: Version 1.1 – March 2011
  version-1-0-december-2010: Version 1.0 – December 2010
---

# Changelog

The following is the change history for the Facebook Login Integration Kit.

## Version 2.1.1 - January 2026

* Removed third-party fonts and the `authn-api-messages.properties` file.

## Version 2.1 – August 2020

* Fixed an error that could happen when permissions were added to a new adapter instance.

* Fixed an issue that prevented single logout from completing correctly.

* Updated the core contract attributes to accommodate changes in the Facebook API.

* Added support for the Facebook **Require App Secret** option.

* Added the ability to show the Facebook sign-on prompt in a pop-up window for environments that block the automatic redirect. Learn more in the [Facebook IdP Adapter settings reference](pf_facebook_cic_facebook_idp_adapter_settings_reference.html).

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Added settings for retrying failed requests.

* Added settings for API connection and request timeouts.

* Added settings to override the PingFederate system-default proxy settings.

## Version 2.0.1 – November 2018

* Improved HTTP client package names to avoid class-loading collisions with other add-ons, such as the CoreBlox Integration Kit.

## Version 2.0 – February 2018

* Improved user experience for adding additional scope permissions and attributes.

* Added support for multivalued attributes, which are returned from the adapter as a JSON string.

* Improved error handling for a canceled sign-on request.

* Bug fixes.

## Version 1.3.2 – March 2017

* Upgraded to v2.3 of the Facebook Graph API. The Facebook IdP Adapter also supports v2.8.

* Resolved SLO issue when running the Facebook IdP Adapter behind a load balancer.

## Version 1.3 – March 2015

* Upgraded to v2.2 of the Facebook Graph API.

* URL query parameters can now be included in the **Facebook User Data URL** field. For example:

  `https://graph.facebook.com/v2.2/me?fields=id,birthday,email,first_name,gender,last_name,name,picture`

## Version 1.2.2 – July 2013

* Added masking to the **Application ID** and **Application Secret** fields. Learn more in the [Facebook IdP Adapter settings reference](pf_facebook_cic_facebook_idp_adapter_settings_reference.html).

* Removed access token, **Application ID**, and **Application Secret** from being displayed in the `server.log` when the log level is set to debug.

## Version 1.2.1 – May 2013

* Addressed potential security vulnerabilities found since version 1.2.

## Version 1.2 – February 2013

* Added the **Logout URL** field to the **IdP Adapter** tab. Learn more in the [Facebook IdP Adapter settings reference](pf_facebook_cic_facebook_idp_adapter_settings_reference.html).

## Version 1.1 – March 2011

* Modified error handling capabilities.

* Added configurable Facebook API endpoints to the **IdP Adapter** tab, in the **Advanced Fields** section. Learn more in the [Facebook IdP Adapter settings reference](pf_facebook_cic_facebook_idp_adapter_settings_reference.html).

## Version 1.0 – December 2010

* Initial Release.

---

---
title: Changelog
description: The following is the change history for the Workplace from Facebook Provisioner.
component: facebook
page_id: facebook:workplace_from_facebook_provisioner:pf_workplace_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/facebook/workplace_from_facebook_provisioner/pf_workplace_connector_changelog.html
revdate: June 11, 2024
section_ids:
  workplace-from-facebook-provisioner-1-10-october-2022: Workplace from Facebook Provisioner 1.10 - October 2022
  workplace-from-facebook-provisioner-1-8-1-january-2021: Workplace from Facebook Provisioner 1.8.1 - January 2021
  workplace-from-facebook-provisioner-1-8-1-march-2020: Workplace from Facebook Provisioner 1.8.1 - March 2020
  workplace-from-facebook-provisioner-1-8-january-2020: Workplace from Facebook Provisioner 1.8 - January 2020
  workplace-from-facebook-provisioner-1-7-1-september-2018: Workplace from Facebook Provisioner 1.7.1 - September 2018
  workplace-from-facebook-provisioner-1-7-february-2018: Workplace from Facebook Provisioner 1.7 - February 2018
  workplace-from-facebook-provisioner-1-6-2-october-2017: Workplace from Facebook Provisioner 1.6.2 - October 2017
  workplace-from-facebook-provisioner-1-6-1-july-2017: Workplace from Facebook Provisioner 1.6.1 - July 2017
  workplace-from-facebook-provisioner-1-6-june-2017: Workplace from Facebook Provisioner 1.6 - June 2017
  workplace-from-facebook-provisioner-1-5-june-2017: Workplace from Facebook Provisioner 1.5 - June 2017
  workplace-from-facebook-provisioner-1-4-1-march-2017: Workplace from Facebook Provisioner 1.4.1 - March 2017
  workplace-from-facebook-provisioner-1-4-october-2016: Workplace from Facebook Provisioner 1.4 - October 2016
  workplace-from-facebook-provisioner-1-3-august-2016: Workplace from Facebook Provisioner 1.3 - August 2016
  workplace-from-facebook-provisioner-1-2-june-2016: Workplace from Facebook Provisioner 1.2 - June 2016
  workplace-from-facebook-provisioner-1-1-january-2016: Workplace from Facebook Provisioner 1.1 - January 2016
  workplace-from-facebook-provisioner-1-0-march-2015: Workplace from Facebook Provisioner 1.0 - March 2015
---

# Changelog

The following is the change history for the Workplace from Facebook Provisioner.

## Workplace from Facebook Provisioner 1.10 - October 2022

* Added support for SCIM 2.0.

* Changed the default SCIM URL to https\://scim.workplace.com/.

## Workplace from Facebook Provisioner 1.8.1 - January 2021

* Rebranded to new name (formerly known as Workplace by Facebook).

## Workplace from Facebook Provisioner 1.8.1 - March 2020

* Changed the default SCIM URL to https\://www\.facebook.com/scim/v1/.

## Workplace from Facebook Provisioner 1.8 - January 2020

* Added support for the app secret security feature.

* Added the following attributes: `employeeNumber`, `costCenter`, `organization`, `division`.

* Fixed an issue that caused a JSON error when updating users that were awarded a badge or added to a People Set or Work Team.

## Workplace from Facebook Provisioner 1.7.1 - September 2018

* Improved error handling and reporting when workplace users contain no ID.

* Improved check connection call by not retrieving a list of users.

## Workplace from Facebook Provisioner 1.7 - February 2018

* Added support for `formattedName` attribute.

## Workplace from Facebook Provisioner 1.6.2 - October 2017

* Fixed LDAP lookup issue when multiple SP connections use different LDAP data stores.

## Workplace from Facebook Provisioner 1.6.1 - July 2017

* Fixed LDAP lookup issue when multiple SSO connections exist along side provisioning connections.

## Workplace from Facebook Provisioner 1.6 - June 2017

* Improved Manager attribute lookup by connecting to the LDAP directory to determine manager's email address for an optimized Workplace query.

## Workplace from Facebook Provisioner 1.5 - June 2017

* Support added for the profileUrl attribute

* Added a "disable" configuration option for CRUD capabilities

* Added configuration options for provisioning disabled users

* Fixed attributes being cleared in Facebook when attributes are unmapped in PingFederate

* Fixed disabling a user after initial synchronization when the user was not created via the provisioner

## Workplace from Facebook Provisioner 1.4.1 - March 2017

* Fixed synchronization on update of users, that were previously created with "User Create Enabled" set to false in configurable options

## Workplace from Facebook Provisioner 1.4 - October 2016

* Rebranded to new name (formerly known as Facebook At Work)

* Removed suppressEmail attribute

## Workplace from Facebook Provisioner 1.3 - August 2016

* Added configuration options for CRUD capabilities

* Improved exception handling and reporting

## Workplace from Facebook Provisioner 1.2 - June 2016

* Added support for the Manager attribute.

## Workplace from Facebook Provisioner 1.1 - January 2016

* Added support for provisioning additional user attributes

* Minor bug fixes

* Added support for user provisioning

## Workplace from Facebook Provisioner 1.0 - March 2015

* Initial release

---

---
title: Configuring an adapter instance
description: Configure the Facebook IdP Adapter to determine how PingFederate communicates with the Facebook API.
component: facebook
page_id: facebook:facebook_login_integration_kit:pf_facebook_cic_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/facebook/facebook_login_integration_kit/pf_facebook_cic_configuring_an_adapter_instance.html
revdate: January 20, 2026
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Configure the Facebook IdP Adapter to determine how PingFederate communicates with the Facebook API.

## Steps

1. In the PingFederate admin console, go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **Facebook IdP Adapter**. Click **Next**.

3. (Optional) On the **IdP Adapter** tab, in the **Scope Permissions** section, add any additional Facebook scopes you want to request.

   Learn more in [Facebook permissions](pf_facebook_cic_facebook_permissions.html).

   1. Click **Add a new row to 'Scope Permissions'**.

   2. In the **Additional Facebook Scope Permissions** field, enter the name of a scope.

   3. In the **Action** column, click **Update**.

   4. To add more scopes, repeat steps a - c.

4. On the **IdP Adapter** tab, configure the adapter instance by referring to [Facebook IdP Adapter settings reference](pf_facebook_cic_facebook_idp_adapter_settings_reference.html). Click **Next**.

5. On the **Extended Contract** tab, add any attributes that you want to include in the contract. Click **Next**.

6. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

7. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

8. On the **Summary** tab, check your configuration, then click **Save**.

---

---
title: Configuring provisioning
description: To allow PingFederate to manage users in Workplace from Facebook, configure SAML in Workplace from Facebook, and then create a connection in PingFederate.
component: facebook
page_id: facebook:workplace_from_facebook_provisioner:pf_workplace_connector_configuring_provisioning
canonical_url: https://docs.pingidentity.com/integrations/facebook/workplace_from_facebook_provisioner/pf_workplace_connector_configuring_provisioning.html
revdate: June 11, 2024
section_ids:
  steps: Steps
---

# Configuring provisioning

To allow PingFederate to manage users in Workplace from Facebook, configure SAML in Workplace from Facebook, and then create a connection in PingFederate.

## Steps

1. Complete the steps in [Creating a custom integration and access token in Workplace](pf_workplace_connector_creating_a_custom_integration_and_access_token_in_workplace.html).

2. Complete the steps in [Creating a provisioning connection](pf_workplace_connector_creating_a_provisioning_connection.html).

---

---
title: Configuring single sign-on
description: To allow PingFederate to act as an identity provider for Workplace from Facebook, exchange signing certificates and create a connection.
component: facebook
page_id: facebook:workplace_from_facebook_provisioner:pf_workplace_connector_configuring_single_sign_on
canonical_url: https://docs.pingidentity.com/integrations/facebook/workplace_from_facebook_provisioner/pf_workplace_connector_configuring_single_sign_on.html
revdate: August 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring single sign-on

To allow PingFederate to act as an identity provider for Workplace from Facebook, exchange signing certificates and create a connection.

## About this task

|   |                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Single sign-on (SSO) is not required for provisioning. If you only want to use the Workplace from Facebook Provisioner for provisioning, skip these steps. |

## Steps

1. Complete the steps in [Adding SSO to a connection](pf_workplace_connector_adding_sso_to_a_connection.html).

2. Complete the steps in [Registering PingFederate as an identity provider in Workplace](pf_workplace_connector_registering_pf_as_an_identity_provider_in_workplace.html).

---

---
title: Configuring SSO to an application within the PingFederate domain
description: To enable SSO to an application within the PingFederate domain, configure an adapter-to-adapter mapping.
component: facebook
page_id: facebook:facebook_login_integration_kit:pf_facebook_cic_configuring_sso_to_an_application_within_the_pf_domain
canonical_url: https://docs.pingidentity.com/integrations/facebook/facebook_login_integration_kit/pf_facebook_cic_configuring_sso_to_an_application_within_the_pf_domain.html
revdate: June 11, 2024
section_ids:
  steps: Steps
---

# Configuring SSO to an application within the PingFederate domain

To enable SSO to an application within the PingFederate domain, configure an adapter-to-adapter mapping.

## Steps

1. On the PingFederate administrative console, create an SP adapter instance to integrate with your web application.

   For an overview of SP adapters, see [Managing SP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_adaptermanagementtasklet_spadaptermanagementstate.html) in the PingFederate documentation. For most use cases, we recommend the Reference ID Adapter included in the [Agentless Integration Kit](../../agentless/pf_agentless_ik.html).

2. Map the attributes from your Facebook IdP Adapter instance to the SP adapter instance by creating an adapter-to-adapter mapping.

   For instructions, see [Adapter-to-adapter mappings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_adaptertoadapter_mappings.html) in the PingFederate documentation.

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
component: facebook
page_id: facebook:facebook_login_integration_kit:pf_facebook_cic_configuring_sso_to_an_sp_outside_the_pf_domain
canonical_url: https://docs.pingidentity.com/integrations/facebook/facebook_login_integration_kit/pf_facebook_cic_configuring_sso_to_an_sp_outside_the_pf_domain.html
revdate: June 11, 2024
section_ids:
  steps: Steps
---

# Configuring SSO to an SP outside the PingFederate domain

To enable SSO to a service provider (SP) outside the PingFederate domain, configure an SP connection and add a sign-on link to the SP application.

## Steps

1. Create an SP connection and select your Facebook IdP Adapter instance on the **Authentication Source Mapping** tab.

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
title: Core contract attributes reference
description: The Facebook IdP Adapter has a set of core contract attributes. The core contract attributes have changed across versions to accommodate changes in the Facebook API.
component: facebook
page_id: facebook:facebook_login_integration_kit:pf_facebook_cic_core_contract_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/facebook/facebook_login_integration_kit/pf_facebook_cic_core_contract_attributes_reference.html
revdate: June 11, 2024
---

# Core contract attributes reference

The Facebook IdP Adapter has a set of core contract attributes. The core contract attributes have changed across versions to accommodate changes in the Facebook API.

**Core contract attributes in the Facebook IdP Adapter**

| Version 1.3                                       | Version 2.0    | Version 2.1    |
| ------------------------------------------------- | -------------- | -------------- |
| about                                             |                |                |
| access\_token                                     | access\_token  | access\_token  |
|                                                   | age\_range     |                |
| bio\[[1](#_footnotedef_1 "View footnote.")]       |                |                |
| birthday\[[1](#_footnotedef_1 "View footnote.")]  |                |                |
|                                                   | cover          |                |
| education\[[1](#_footnotedef_1 "View footnote.")] |                |                |
| first\_name                                       | first\_name    | first\_name    |
| gender                                            | gender         |                |
| hometown\[[1](#_footnotedef_1 "View footnote.")]  |                |                |
| id                                                | id             | id             |
| last\_name                                        | last\_name     | last\_name     |
| link                                              | link           |                |
| locale                                            | locale         |                |
| location\[[1](#_footnotedef_1 "View footnote.")]  |                |                |
|                                                   |                | middle\_name   |
| name                                              | name           | name           |
|                                                   |                | name\_format   |
|                                                   | picture        | picture        |
| quotes\[[1](#_footnotedef_1 "View footnote.")]    |                |                |
|                                                   |                | short\_name    |
| timezone                                          | timezone       |                |
| token\_expires                                    | token\_expires | token\_expires |
| updated\_time                                     | updated\_time  |                |
| verified                                          | verified       |                |
| work\[[1](#_footnotedef_1 "View footnote.")]      |                |                |

***

[1](#_footnoteref_1). Attribute requires additional permissions. If configured in 1.3, it will need to be added as an extended attribute after the upgrade.

---

---
title: Creating a custom integration and access token in Workplace
description: To allow PingFederate to access the Workplace from Facebook API, create a custom integration in Workplace from Facebook that will allow you to generate an access token.
component: facebook
page_id: facebook:workplace_from_facebook_provisioner:pf_workplace_connector_creating_a_custom_integration_and_access_token_in_workplace
canonical_url: https://docs.pingidentity.com/integrations/facebook/workplace_from_facebook_provisioner/pf_workplace_connector_creating_a_custom_integration_and_access_token_in_workplace.html
revdate: June 11, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating a custom integration and access token in Workplace

To allow PingFederate to access the Workplace from Facebook API, create a custom integration in Workplace from Facebook that will allow you to generate an access token.

## About this task

By creating a custom integration to represent PingFederate in Workplace from Facebook, you can generate an access token.

|   |                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Workplace from Facebook automatically deactivates custom integrations that have not been active for 60 days. For details, see [Custom integration deactivation policy](https://developers.facebook.com/docs/workplace/custom-integrations-new/deactivation-policy) in the Workplace documentation. |

## Steps

1. Sign on to Workplace as an administrator.

2. From the **Admin Panel**, go to **Integrations**.

   ![Screen capture of the administration menu with Integrations highlighted.](_images/foa1575671382207.jpg)

3. Click **Create Custom Integration**.

4. On the **Create Custom Integration** dialog, enter a name and description of your choosing. Click **Create**.

5. Click **Create Access Token**.

6. On the **New Token Created** dialog, note the access token value. You will use this in [Configuring provisioning](pf_workplace_connector_configuring_provisioning.html).

   ![Screen shot of the New Token Created dialog.](_images/pey1563995329327.png)

7. Select **I understand**, and then click **Done**.

8. On the **Integration Details** window, in the **Integration Permissions** section, select **Manage accounts**.

9. **Optional:** Select **Automatically invite people to Workplace as soon as they're added using this integration**.

10. **Optional:** Enable the [App secret proof feature](pf_workplace_connector_app_secret_proof_feature.html).

    1. In the **Integration Details** section, note the **App Secret** value.

       You will use this in [Configuring provisioning](pf_workplace_connector_configuring_provisioning.html).

    2. In the **Security Settings** section, turn on **Require App Secret Proof**.

11. Click **Save**.

---

---
title: Creating a provisioning connection
description: To allow PingFederate to manage users in Workplace from Facebook, create a service provider (SP) connection.
component: facebook
page_id: facebook:workplace_from_facebook_provisioner:pf_workplace_connector_creating_a_provisioning_connection
canonical_url: https://docs.pingidentity.com/integrations/facebook/workplace_from_facebook_provisioner/pf_workplace_connector_creating_a_provisioning_connection.html
revdate: June 11, 2024
section_ids:
  steps: Steps
---

# Creating a provisioning connection

To allow PingFederate to manage users in Workplace from Facebook, create a service provider (SP) connection.

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   **Choose from:**

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details with the Workplace from Facebook quick connection template.

   1. On the **Connection Template** tab, select **Use a template for this connection**.

   2. From the **Connection Template** list, select **Workplace from Facebook Provisioner**.

   3. On the **Metadata File** row, upload the workplacebyfacebook-saml-metadata.xml file that you saved in [Getting SAML details from Workplace](pf_workplace_connector_getting_saml_details_from_workplace.html). Click **Next**.

   4. On the **Connection Type** tab select **Outbound Provisioning**. Click **Next**.

   5. On the **Connection Options** tab, click **Next**.

   6. On the **General Info** tab, in the **Connection Name** field, enter a name of your choosing. Click **Next**.

3. On the **Outbound Provisioning** tab, configure provisioning with the following details.

   For help, see [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

   1. On the **Target** screen, enter the **OAuth Access Token** value that you noted in [Creating a custom integration and access token in Workplace](pf_workplace_connector_creating_a_custom_integration_and_access_token_in_workplace.html).

      |   |                                                                                         |
      | - | --------------------------------------------------------------------------------------- |
      |   | PingFederate verifies the access token when you activate the channel and SP connection. |

   2. If you want to enable the [App secret proof feature](pf_workplace_connector_app_secret_proof_feature.html), enter the **App Secret** value that you noted in [Creating a custom integration and access token in Workplace](pf_workplace_connector_creating_a_custom_integration_and_access_token_in_workplace.html).

   3. In the **SCIM URL** field, update the pre-populated value with the one of the following URLs depending on which version of SCIM you are using:

      * For SCIM 1.1 (Provisioner JAR 1.8.1 or earlier) use `https://www.facebook.com/scim/v1/`.

      * For SCIM 2.0 (Provisioner JAR 1.10 and later) use `https://scim.workplace.com/`.

   4. Under **Provisioning Options**, customize the provisioning connector behavior by referring to the [Provisioning options reference](pf_workplace_connector_provisioning_options_reference.html). Click **Next**.

   5. From the **UserName Attribute Mapping** list, select the attribute that you want to use to synchronize users between the datastore and Workplace from Facebook. For details, see [User management](pf_workplace_connector_user_management.html).

   6. On the **Manage Channels** tab, create a channel as shown.

      For help, see [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation.

      |   |                                                                                                                                                                      |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you changed the **UserName Attribute Mapping** in **Provisioning Options**, make the same change in **Manage Channels > Channel > Attribute Mapping > userName**. |

      |   |                                                                                                                                                                                      |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | For more information about the attributes available in your channel configuration, see [Supported attributes reference](pf_workplace_connector_supported_attributes_reference.html). |

4. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: Creating an app in Facebook
description: To allow PingFederate to process sign-on requests using Facebook, add PingFederate as a sign-on provider in Facebook.
component: facebook
page_id: facebook:facebook_login_integration_kit:pf_facebook_cic_creating_an_app_in_facebook
canonical_url: https://docs.pingidentity.com/integrations/facebook/facebook_login_integration_kit/pf_facebook_cic_creating_an_app_in_facebook.html
revdate: June 11, 2024
section_ids:
  steps: Steps
---

# Creating an app in Facebook

To allow PingFederate to process sign-on requests using Facebook, add PingFederate as a sign-on provider in Facebook.

## Steps

1. Sign on to the [Facebook developer apps](https://developers.facebook.com/apps) page.

2. Create the app.

   1. Click **Create App**.

   2. On the **Select an app type** modal, in the **Which products, permissions and features does your app need?** section, select **Consumer**.

   3. Configure the basic app details. Click **Create App**.

   4. Confirm your password. Click **Submit**.

3. On the **Add a Product** page, for **Facebook Login**, click **Set Up**.

4. Click **Web**.

5. On the **Web** tab, in the **Tell Us about Your Website** section, in the **Site URL** field, enter your PingFederate Facebook authentication URL based on the following. Click **Save**. Click **Continue**.

   ```
   https://pf_host:pf_port/ext/facebook-authn/
   ```

6. Disregard the remaining sections on this page, your settings are saved automatically.

7. Go to **Products > Facebook Login > Settings**.

   ![A screenshot that shows the navigation path for the Facebook Login settings.](_images/onn1623869418596.jpg)

8. In the **Valid OAuth Redirect URIs** field, enter the same PingFederate URL.

   ![A screenshot that shows the Valid OAuth Redirect URIs field.](_images/mqn1623869449689.jpg)

9. Click **Save Changes**.

10. Go to **Settings > Basic**. Note your **App ID** and **App Secret**.

    ![A screenshot that shows the navigation path for the basic app settings.](_images/nxk1623869706000.jpg)

    You will use these in [Configuring an adapter instance](pf_facebook_cic_configuring_an_adapter_instance.html).

11. **Optional:** Go to **Settings > Advanced**. In the **Security** section, turn on **Require App Secret**. Click **Save Changes**.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Facebook Login Integration Kit files to your PingFederate directory.
component: facebook
page_id: facebook:facebook_login_integration_kit:pf_facebook_cic_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/facebook/facebook_login_integration_kit/pf_facebook_cic_deploying_the_integration_files.html
revdate: June 11, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Facebook Login Integration Kit files to your PingFederate directory.

## Steps

1. Download the Facebook Login Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/facebook-login-integration-kit).

2. Stop PingFederate.

3. If you are upgrading from a previous deployment, back up your customizations and delete older versions of the integration files.

   1. Back up any Facebook Login Integration Kit files that you customized in `<pf_install>/pingfederate/server/default/conf/`.

   2. Delete the following files from `<pf_install>/pingfederate/server/default/deploy`:

      * `pf-facebook-adapter-<version>.jar`

      * `json-simple-<version>.jar`

4. Delete `pf-authn-api-sdk-<version>.jar` from `<pf_install>/pingfederate/server/default/lib` if it is older than the version in the integration files.

5. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

6. If you backed up any customized files, modify the new files with your customizations.

7. Start PingFederate.

8. If you operate PingFederate in a cluster, repeat steps 2-7 for each engine node.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Workplace from Facebook Provisioner files to your PingFederate directory.
component: facebook
page_id: facebook:workplace_from_facebook_provisioner:pf_workplace_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/facebook/workplace_from_facebook_provisioner/pf_workplace_connector_deploying_the_integration_files.html
revdate: June 11, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Workplace from Facebook Provisioner files to your PingFederate directory.

## Steps

1. Download the Workplace from Facebook Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/workplace-from-facebook-single-signon-integration).

2. Stop PingFederate.

3. If you are upgrading from an earlier version of the integration, delete the following files from `<pf_install>/pingfederate/server/default/deploy`:

   * `pf-workplacebyfacebook-quickconnection-<version>.jar`

   * `pf-workplacebyfacebook-quickconnect-<version>.jar`

4. From the `.zip` archive, copy the contents of `dist` to `<pf_install>/pingfederate/server/default/deploy`.

5. Enable the PingFederate provisioning engine.

   1. In `<pf_install>/pingfederate/bin`, open `run.properties` for editing.

   2. Change `pf.provisioner.mode` to `STANDALONE`. Save the file.

      |   |                                                                                                                                                                                                                                        |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | To configure the `FAILOVER` mode instead, see [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate server clustering guide. |

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 2-6 for each engine node.

---

---
title: Download manifest
description: The following files are included in the Facebook Login Integration Kit .zip archive:
component: facebook
page_id: facebook:facebook_login_integration_kit:pf_facebook_cic_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/facebook/facebook_login_integration_kit/pf_facebook_cic_download_manifest.html
revdate: January 21, 2026
---

# Download manifest

The following files are included in the Facebook Login Integration Kit `.zip` archive:

* `ReadMeFirst.pdf`: Contains links to this online documentation.

* `Legal.pdf`: Copyright and license information.

* `dist`: Contains the integration files.

  * `deploy`: Contains the Java libraries.

    * `pf-facebook-adapter-<version>.jar`: JAR file that contains the Facebook IdP Adapter.

  * `conf`: Contains the HTML template that presents the Facebook sign-on form.

    * `language-packs`: Contains files with customizable user-facing messages.

      * `facebook-messages.properties`: A variable file that customizes the messages that appear on the template file.

    * `template`: Contains user-facing HTML template files.

      * `facebook.template.html`: A page that presents the Facebook sign-on window in the **Pop-up window** sign-on presentation mode.

      * `facebook.post.auth.template.html`: A page that signals the main template or authentication widget to continue the authentication flow in the **Pop-up window** sign-on presentation mode.

      * `assets`: Contains functional scripts and files used by the template.

        * `css/facebook.css`: A CSS file that customizes the appearance of the template file.

        * `fonts/end-user`: Contains template fonts and icons.

          * `icons`: Contains template icons.

        * `images`: Contains template image files.

          * `ping-logo.svg`: An image file with company branding.

  * `lib/pf-authn-api-sdk-<version>.jar`: A JAR file that contains the PingFederate Authentication API SDK.

---

---
title: Download manifest
description: The following files are included in the Workplace from Facebook Provisioner .zip archive:
component: facebook
page_id: facebook:workplace_from_facebook_provisioner:pf_workplace_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/facebook/workplace_from_facebook_provisioner/pf_workplace_connector_download_manifest.html
revdate: June 11, 2024
---

# Download manifest

The following files are included in the Workplace from Facebook Provisioner `.zip` archive:

* `legal/Legal.pdf` – copyright and license information.

* `dist`: Contains the integration files.

  * `pf-workplacebyfacebook-quickconnection-<version>.jar` – The Workplace from Facebook Provisioner quick connection template.

* `workplacebyfacebook-saml-metadata.xml` – a modifiable metadata file used to create the connection.

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.
component: facebook
page_id: facebook:facebook_login_integration_kit:pf_facebook_cic_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/facebook/facebook_login_integration_kit/pf_facebook_cic_enabling_debug_logging.html
revdate: June 11, 2024
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

3. If you want to log activity just for the Facebook IdP Adapter, add the following line.

   ```html
   <Logger name="com.pingidentity.adapters.idp.facebook" level="DEBUG"/>
   ```

4. Save the file.

---

---
title: Enabling provisioning and single sign-on in PingFederate
description: To use PingFederate for provisioning and single sign-on, configure an external datastore and set a SAML entity ID.
component: facebook
page_id: facebook:workplace_from_facebook_provisioner:pf_workplace_connector_enabling_provisioning_and_single_sign_on_in_pf
canonical_url: https://docs.pingidentity.com/integrations/facebook/workplace_from_facebook_provisioner/pf_workplace_connector_enabling_provisioning_and_single_sign_on_in_pf.html
revdate: June 11, 2024
section_ids:
  about-this-task: About this task
  enabling-provisioning-and-single-sign-on-in-pingfederate-10-1-or-later: Enabling provisioning and single sign-on in PingFederate 10.1 or later
  steps: Steps
  enabling-provisioning-and-single-sign-on-in-pingfederate-10-0-or-earlier: Enabling provisioning and single sign-on in PingFederate 10.0 or earlier
  steps-2: Steps
---

# Enabling provisioning and single sign-on in PingFederate

To use PingFederate for provisioning and single sign-on, configure an external datastore and set a SAML entity ID.

## About this task

Your external datastore acts as the source of data for provisioning. PingFederate also uses an internal datastore to store the state of synchronization between the source datastore and the target datastore.

For more information, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) and [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

## Enabling provisioning and single sign-on in PingFederate 10.1 or later

### Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   For help, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Server > Protocol Settings > Federation Info**.

3. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use when identifying itself to SAML partners.

4. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   For more information, see [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

## Enabling provisioning and single sign-on in PingFederate 10.0 or earlier

### Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   For help, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Protocol Settings > Roles & Protocols**.

3. Select the **Enable Identity Provider IdP Role and Support the Following** check box.

4. Select the **SAML 2.0** and **Outbound Provisioning** check boxes. Click **Next**.

5. Click the **Federation Info** tab.

6. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

7. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   For more information, see [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Enabling provisioning and single sign-on in PingFederate 10.0 or earlier
description: In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.
component: facebook
page_id: facebook:workplace_from_facebook_provisioner:pf_workplace_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/facebook/workplace_from_facebook_provisioner/pf_workplace_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier.html
revdate: August 12, 2024
section_ids:
  steps: Steps
---

# Enabling provisioning and single sign-on in PingFederate 10.0 or earlier

## Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   For help, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Protocol Settings > Roles & Protocols**.

3. Select the **Enable Identity Provider IdP Role and Support the Following** check box.

4. Select the **SAML 2.0** and **Outbound Provisioning** check boxes. Click **Next**.

5. Click the **Federation Info** tab.

6. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

7. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   For more information, see [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.