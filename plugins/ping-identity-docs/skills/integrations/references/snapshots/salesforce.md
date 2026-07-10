---
title: Add an SSO link in Salesforce (example)
description: Create a dynamic single sign-on (SSO) link and add it to your Salesforce page.
component: salesforce
page_id: salesforce:salesforce_login_integration_kit:pf_salesforce_cic_add_an_sso_link_in_salesforce_example
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_login_integration_kit/pf_salesforce_cic_add_an_sso_link_in_salesforce_example.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Add an SSO link in Salesforce (example)

Create a dynamic single sign-on (SSO) link and add it to your Salesforce page.

## Steps

1. In the Salesforce administrative console, go to **Setup > Customize > Home > Custom Links**.

2. On the **Home** page, in the **Custom Links** section, click **New**.

3. Complete the **Label**, **Name**, and **Description** fields.

4. In the **Content Source** list, select **URL**.

5. In the text area, enter one of the following URLs:

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can insert `{!API.Session_ID}` and `{!API.Partner_Server_URL_200}` or equivalent by selecting **$Api** from the **Select Field Type** list and then selecting the variable you want from the **Insert Field** list.Salesforce dynamically populates these variables when the user clicks the link. Learn more about [Global Variables](https://help.salesforce.com/articleView?id=sf.dev_understanding_global_variables.htm) in the Salesforce documentation. |

   ### **Choose from:**

   * For SSO through an SP-partner connection in PingFederate:

     ```shell
     https://pf_host:pf_port/idp/startSSO.ping?
     sid={!API.Session_ID}&apiendpoint={!API.Partner_Server_URL_200}&
     TargetResource=destination_URL&
     PartnerSpId=connection_ID
     ```

     Replace the variables as follows:

     * *pf\_host*: The host name or IP address of the PingFederate server.

     * *pf\_port*: The port number of the PingFederate server.

     * *destination\_URL*: The fully-qualified URL of the target application or other protected resource.

     * *connection\_ID*: The **Partner's Entity ID (Connection ID)** of the service provider (SP) connection that you configured.

       Example URL:

       ```shell
       https://pingfederate.example.com:9031/idp/startSSO.ping?sid={!API.Session_ID}&apiendpoint={!API.Partner_Server_URL_200}&TargetResource=https://portal.example.com/welcome&PartnerSpId=SFConnection1
       ```

   * For SSO through IdP-to-SP adapter mapping in PingFederate:

     ```shell
     https://pf_host:pf_port/pf/adapter2adapter.ping?
     sid={!API.Session_ID}&apiendpoint={!API.Partner_Server_URL_200}&
     TargetResource=destination_URL&
     IdpAdapterId=adapter_ID
     ```

     Replace the variables as follows:

     * *pf\_host*: The host name or IP address of the PingFederate server.

     * *pf\_port*: The port number of the PingFederate server.

     * *destination\_URL*: The fully-qualified URL of the target application or other protected resource.

     * *adapter\_ID*: The **Instance ID** of the Salesforce IdP Adapter that you configured.

       Example URL:

       ```shell
       https://pingfederate.example.com:9031/pf/adapter2adapter.ping?sid={!API.Session_ID}&apiendpoint={!API.Partner_Server_URL_200}&TargetResource=https://portal.example.com/welcome&IdpAdapterId=SFAdapter1
       ```

6. Click **Save**.

7. Go to **Setup > Customize > Home Page Components**.

8. Add a new link component using the custom link that you created.

9. Go to **Setup > Customize > Home Page Layout**.

10. Edit your existing layout or create a new layout to include the new link component.

11. Check that the user profile is configured to use the page layout that you modified.

---

---
title: Changelog
description: The following is the change history for the Salesforce Contacts Provisioner.
component: salesforce
page_id: salesforce:salesforce_contacts_provisioner:pf_salesforce_contacts_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_contacts_provisioner/pf_salesforce_contacts_connector_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Changelog

The following is the change history for the Salesforce Contacts Provisioner.

**Salesforce Connector 1.0 – September 2020**

* Initial release.

* Added the ability to manage Leads and Contacts in Salesforce.

* Added the ability to enable the create, update, and disable capabilities independently.

---

---
title: Changelog
description: Salesforce Cloud Identity Connector 1.0 – January 2011
component: salesforce
page_id: salesforce:salesforce_login_integration_kit:pf_salesforce_cic_changelog
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_login_integration_kit/pf_salesforce_cic_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Changelog

**Salesforce Cloud Identity Connector 1.0 – January 2011**

Initial Release

---

---
title: Changelog
description: The following is the change history for the Salesforce Provisioner.
component: salesforce
page_id: salesforce:salesforce_provisioner:pf_salesforce_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_provisioner/pf_salesforce_connector_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  salesforce-connector-7-0-1-april-2020: Salesforce Connector 7.0.1 – April 2020
  salesforce-connector-7-0-september-2019: Salesforce Connector 7.0 – September 2019
  salesforce-connector-6-1-july-2017: Salesforce Connector 6.1 – July 2017
  salesforce-connector-6-0-october-2016: Salesforce Connector 6.0 – October 2016
  salesforce-connector-5-1-1-november-2015: Salesforce Connector 5.1.1 – November 2015
  salesforce-connector-5-1-august-2015: Salesforce Connector 5.1 – August 2015
  salesforce-connector-5-0-october-2014: Salesforce Connector 5.0 – October 2014
  salesforce-connector-4-1-june-2011: Salesforce Connector 4.1 - June 2011
  salesforce-connector-4-0-1-november-2010: Salesforce Connector 4.0.1 - November 2010
  salesforce-connector-4-0-november-2010: Salesforce Connector 4.0 - November 2010
  salesforce-connector-3-3-may-2009: Salesforce Connector 3.3 - May 2009
  salesforce-connector-3-2-january-2009: Salesforce Connector 3.2 - January 2009
  salesforce-connector-3-1-september-2008: Salesforce Connector 3.1 - September 2008
  salesforce-com-integration-kit-3-0-may-2008: Salesforce.com Integration Kit 3.0 - May 2008
  salesforce-com-integration-kit-2-0-july-2007: Salesforce.com Integration Kit 2.0 - July 2007
  salesforce-com-integration-kit-1-1-november-2006: Salesforce.com Integration Kit 1.1 - November 2006
  salesforce-com-integration-kit-1-0-june-2006: Salesforce.com Integration Kit 1.0 - June 2006
---

# Changelog

The following is the change history for the Salesforce Provisioner.

## Salesforce Connector 7.0.1 – April 2020

* Fixed an issue that caused the connection check to return a success when the wrong subdomain was entered.

## Salesforce Connector 7.0 – September 2019

* Added support for provisioning to Salesforce Community Cloud, which includes customer, partner, and custom communities.

* Added the ability to create connections to custom Salesforce domains.

* Added support for version `46.0` of the Salesforce REST API.

* Added configuring options to manage permission sets by merging or overwriting.

* Added support for additional Salesforce attributes.

* Added the ability to create multiple Salesforce connections in one PingFederate instance.

* Added default attribute mappings for channels that use PingDirectory and Oracle Directory Server datastores.

* Improved error handling and reporting for cases where users in the target application do not have an ID.

* Improved error handling and reporting for cases where groups are updated or deleted but don't exist in the target application.

* Fixed an issue that prevented users with certain special characters from being provisioned to Salesforce.

* Fixed an issue that caused a user to be updated in Salesforce when the user was being disabled and the **Update Users** option was turned off.

## Salesforce Connector 6.1 – July 2017

* Added support for disabling user without updating any user attributes.

* Added configuration control of provisioning disabled users.

* Added custom attribute support.

* Removed non-mappable attributes from attribute mapping page.

## Salesforce Connector 6.0 – October 2016

* Added support for additional user attributes.

* Added support for group provisioning.

* Added support for adding users to groups.

* Added configuration options for CRUD capabilities.

* Improved exception handling and reporting.

* Added support for Salesforce REST `v37.0` API.

* Added support for the OAuth Authentication with the OAuth Configuration Service (OCS).

* Removed support for Delegated Authentication in favor of SAML (deprecated).

* Removed support for outbound provisioning to partner and customer portals (deprecated).

## Salesforce Connector 5.1.1 – November 2015

* Added support for Salesforce API endpoint change (January 1, 2016).

## Salesforce Connector 5.1 – August 2015

* Added support for SSO to Veeva iRep mobile clients through delegated authentication with Salesforce.

* Fixed quick-connection UI performance issues.

* Added support for the ability to freeze user accounts instead of deactivating them through the provisioner.

* Added support for overriding the provisioning target environment endpoint.

* Enhanced support for SP-Initiated SSO through deep linking and SP-initiated SLO by adding a Salesforce Login URL and a **Single Logout Landing Page** field.

## Salesforce Connector 5.0 – October 2014

* Added ability to have one LDAP user mapped to two different Salesforce administrator accounts.

* Salesforce API was updated from version `20` to version `31`.

* Added `Permission Set` attribute to SP Connection, which enables mapping of permission sets in Salesforce to an LDAP field.

* Added support for proxy authentication.

## Salesforce Connector 4.1 - June 2011

* Added support for Salesforce Chatter and Chatter Free user provisioning.

## Salesforce Connector 4.0.1 - November 2010

* Corrected compatibility issue with PingFederate `6.4`.

## Salesforce Connector 4.0 - November 2010

* Added quick-connection SSO template and enabled SaaS provisioning to the Salesforce Customer Portal.

* Added quick-connection SSO template and enabled SaaS provisioning to the Salesforce Partner Portal.

* Added quick-connection SSO template to support Salesforce CRM SAML capabilities including metadata export from Salesforce and import into PingFederate, plus optional SaaS provisioning.

## Salesforce Connector 3.3 - May 2009

* Added support for Salesforce "Connect for Microsoft Outlook" version `3.2.513`.

* Added an option to remove the email domain from the Salesforce Username for OpenToken authentication by the Authentication Web Service.

## Salesforce Connector 3.2 - January 2009

* Added a quick-connection plug-in component for automated SSO configuration and SaaS provisioning support for use with PingFederate `5.3`.

* Added support for Mutual Transport Layer Security (TLS) between Salesforce and the PingFederate Authentication Service.

* Added an option to remove the email domain from the Salesforce User Name for authentication to a LDAP directory.

* Added support for delegated authentication to Salesforce through Salesforce Mobile Clients.

* Combined the former Salesforce User Guide into the Salesforce Quick Connection Guide.

## Salesforce Connector 3.1 - September 2008

* Support for URL deep linking.

* Obfuscated LDAP password in the configuration file.

* Enabled Single Logout from Salesforce.

* Included Salesforce Quick Connection Guide for PingFederate `5.2`.

* Changed the product name to Salesforce Connector.

## Salesforce.com Integration Kit 3.0 - May 2008

* Support for Salesforce "Connect for Microsoft Outlook" plug-in through a new Desktop Proxy Service that allows the use of corporate credentials for access to Salesforce.

* Uses OpenToken for the encrypted token format rather than PFTOKEN.

## Salesforce.com Integration Kit 2.0 - July 2007

* Provisioning (new user creation on the Salesforce side).

* PingFederate `v4` administrative console Salesforce configuration for optional provisioning and direct Salesforce login.

* Salesforce Web Service user-validation changes.

* Certification on Salesforce AppExchange.

## Salesforce.com Integration Kit 1.1 - November 2006

Use of the PingFederate Standard Adapter, eliminating the Salesforce.com Adapter that was specific to this Integration Kit.

## Salesforce.com Integration Kit 1.0 - June 2006

Initial release.

---

---
title: Configure the IdP adapter
description: For this configuration, you need to know your Salesforce.com Organization ID. You can use more than one ID as needed. Organization IDs are listed under Company Information in your Salesforce Administration Setup.
component: salesforce
page_id: salesforce:salesforce_login_integration_kit:pf_salesforce_cic_configure_the_idp_adapter
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_login_integration_kit/pf_salesforce_cic_configure_the_idp_adapter.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure the IdP adapter

## About this task

|   |                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | For this configuration, you need to know your Salesforce.com Organization ID. You can use more than one ID as needed. Organization IDs are listed under **Company Information** in your Salesforce Administration Setup. |

## Steps

1. Sign on to the PingFederate administrative console and click **Adapters** under **My IdP Configuration** on the Main Menu.

2. On the **Manage IdP Adapter Instances** page, click **Create New Instance**.

3. On the **Type** page, enter an **Instance Name** and **Instance ID**.

   The **Instance Name** is any name you choose for identifying this adapter instance. The **Instance ID** is used internally and must be alphanumeric without any spaces.

   |   |                                              |
   | - | -------------------------------------------- |
   |   | Make a note of the adapter ID for later use. |

4. Select **Salesforce.com Adapter** from the **Type** list and click **Next**.

5. On the **IdP Adapter** page, under **Allowed Organization(s)**:

   1. Click **Add a new row to 'Allowed Organization(s)'**.

   2. Enter your Salesforce Org ID.

   3. Click **Update**.

   4. Repeat these steps for any other Salesforce IDs at your site as needed.

6. (Optional) If SSO to a target application requires the user's organizational role and profile, select the associated checkbox.

   Note that this selection marginally increases processing time for the SSO transaction.

7. Click **Next.**

8. On the **Adapter Attributes** page, select the checkbox next to subject under **Pseudonym**.

   *Pseudonyms* are opaque subject identifiers used for SAML account linking and might not be applicable in the context of cloud-identity deployments. To ensure correct PingFederate performance under all circumstances, however, a selection is required. Learn more about account linking in the [PingFederate Administrator's Manual](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_administrators_reference_guide.html) or click **Help** on this page.

9. On the **Summary** page, verify that the information is correct and click **Done**.

10. On the **Manage IdP Adapter Instances** page, click **Save**.

---

---
title: Contact record attributes reference
description: The following table lists the core attributes that can be mapped for Contact records in Salesforce. Learn more in Contact in the Salesforce documentation.
component: salesforce
page_id: salesforce:salesforce_contacts_provisioner:pf_salesforce_contacts_connector_contact_record_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_contacts_provisioner/pf_salesforce_contacts_connector_contact_record_attributes_reference.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Contact record attributes reference

The following table lists the core attributes that can be mapped for Contact records in Salesforce. Learn more in [Contact](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_contact.htm) in the Salesforce documentation.

| Attribute                   | Description                                                                                                                                                                        |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Email                       | The Contact's email address.This attribute is required.                                                                                                                            |
| Last name                   | The Contact's last name.This attribute is required.                                                                                                                                |
| Assistant's Name            | The Contact's assistant's name.                                                                                                                                                    |
| Birthdate                   | The Contact's birthdate.                                                                                                                                                           |
| Clean Status                | Indicates the record's clean status compared with Data.com.Values include: `Matched`, `Different`, `Acknowledged`, `NotFound`, `Inactive`, `Pending`, `SelectMatch`, or `Skipped`. |
| Contact Description         | A description of the Contact.                                                                                                                                                      |
| Data.com Key                | The Contact's Contact ID in Data.com.                                                                                                                                              |
| Department                  | The Contact's department.                                                                                                                                                          |
| EmailBouncedDate            | The date and time that an email bounced. Applies when bounce management is activated and when an email sent to the Contact bounced.                                                |
| EmailBouncedReason          | The reason that an email bounced. Applies when bounce management is activated and when an email sent to the Contact bounced.                                                       |
| Fax                         | The Contact's fax number.                                                                                                                                                          |
| First name                  | The Contact's first name.                                                                                                                                                          |
| Home Phone                  | The Contact's home phone number.                                                                                                                                                   |
| Individual ID               | ID of the data privacy record associated with this Contact.This field is available when Data Protection and Privacy are enabled in Salesforce.                                     |
| Industry                    | The Contact's industry.                                                                                                                                                            |
| Lead Source                 | The Contact's source, such as web, phone inquiry, partner referral, purchased list, other.                                                                                         |
| Mailing City                | The Contact's mailing city.                                                                                                                                                        |
| Mailing Country Code        | The Contact's mailing country code.                                                                                                                                                |
| Mailing Country             | The Contact's mailing country.                                                                                                                                                     |
| Mailing Geocode Accuracy    | Accuracy level of the geocode for the mailing address.                                                                                                                             |
| Mailing Latitude            | Used with Longitude to specify the precise geolocation of an address.Acceptable values are numbers between `–90` and `90` up to `15` decimal places.                               |
| Mailing Longitude           | Used with Latitude to specify the precise geolocation of an address.Acceptable values are numbers between `–180` and `180` up to `15` decimal places.                              |
| Mailing Phone               | The Contact's mailing phone number.                                                                                                                                                |
| Mailing State/Province Code | The Contact's mailing state or province code.                                                                                                                                      |
| Mailing State/Province      | The Contact's mailing state or province.                                                                                                                                           |
| Mailing Street              | The Contact's mailing street.                                                                                                                                                      |
| Mailing Zip/Postal Code     | The Contact's mailing ZIP or postal code.                                                                                                                                          |
| Mobile Phone                | The Contact's mobile phone number.                                                                                                                                                 |
| Other City                  | The Contact's "other" city.                                                                                                                                                        |
| Other Country Code          | The Contact's "other" country code.                                                                                                                                                |
| Other Country               | The Contact's "other" country.                                                                                                                                                     |
| Other Geocode Accuracy      | Accuracy level of the geocode for the "other" address.                                                                                                                             |
| Other Latitude              | Used with Longitude to specify the precise geolocation of an address.Acceptable values are numbers between `–90` and `90` up to `15` decimal places.                               |
| Other Longitude             | Used with Latitude to specify the precise geolocation of an address.Acceptable values are numbers between `–180` and `180` up to `15` decimal places.                              |
| Other Phone                 | The Contact's "other" phone number.                                                                                                                                                |
| Other State/Province Code   | The Contact's "other" state or province code.                                                                                                                                      |
| Other State/Province        | The Contact's "other" state or province.                                                                                                                                           |
| Other Street                | The Contact's "other" street.                                                                                                                                                      |
| Other Zip/Postal Code       | The Contact's "other" ZIP or postal code.                                                                                                                                          |
| Owner ID                    | The ID of the Contact's owner.                                                                                                                                                     |
| Phone                       | The Contact's phone number.                                                                                                                                                        |
| Reports to ID               | The ID of the person that the Contact reports to.                                                                                                                                  |
| Salutation                  | The Contact's salutation.                                                                                                                                                          |
| Title                       | The Contact's job title.                                                                                                                                                           |

---

---
title: Creating a connection
description: To allow PingFederate to act as an identity provider and manage users in Salesforce, create a service provider (SP) connection:
component: salesforce
page_id: salesforce:salesforce_provisioner:pf_salesforce_connector_creating_a_connection
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_provisioner/pf_salesforce_connector_creating_a_connection.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  steps: Steps
---

# Creating a connection

To allow PingFederate to act as an identity provider and manage users in Salesforce, create a service provider (SP) connection:

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   **Choose from:**

   * For PingFederate 10.1 or later: Go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: Go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details with the Salesforce quick connection template:

   1. On the **Connection Template** tab, select **Use a template for this connection**.

   2. In the **Connection Template** list, select **Salesforce Provisioner**.

   3. On the **Metadata File** row, upload the SAMLSP-xxxxxxxxxxxxxxx.xml file that you saved in [Registering PingFederate as an SSO provider in Salesforce](pf_salesforce_connector_registering_pf_as_an_sso_provider_in_salesforce.html). Click **Next**.

   4. On the **Connection Type** tab, select **Browser SSO Profiles** and **Outbound Provisioning**. Click **Next**.

   5. On the **Connection Options** tab, click **Next**.

   6. On the **General Info** tab, if you configured a custom entity ID in the **Issuer** field in [Registering PingFederate as an SSO provider in Salesforce](pf_salesforce_connector_registering_pf_as_an_sso_provider_in_salesforce.html), enter the name in the **Virtual Server IDs** field and then click **Add**.

   7. In the **Connection Name** field, enter a name that you choose. Click **Next**.

3. On the **Browser SSO** page, configure browser SSO with the following details.

   You can find more information in [Configuring IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) and [Configuring SSO token creation](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spbrowserssotasklet_assertioncreationstate.html) in the PingFederate documentation.

   If you want to integrate with Salesforce Communities, set your Salesforce Communities URL as the default for SSO:

   1. On the **Browser SSO > Protocol Settings > Assertion Consumer Service URL** tab, find your Salesforce Communities URL.

   2. In the **Actions** column, click **Edit**.

   3. In the **Default** column, select the checkbox. Click **Update**.

4. On the **Credentials** page, configure the digital signature settings with the following details:

   1. On the **Digital Signature Settings** page, in the **Signing Certificate** list, select your certificate.

   2. Select **Include the certificate in the signature \<keyinfo> element**. Click **Done**.

      Learn more about [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation.

5. On the **Outbound Provisioning** page, configure provisioning with the following details:

   Learn more about [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

   1. On the **Target** tab, in the **Client ID** field, enter the **Consumer Key** that you noted in [Registering PingFederate as a connected app in Salesforce](pf_salesforce_connector_registering_pf_as_a_connected_app_in_salesforce.html).

   2. In the **Client Secret** field, enter the **Consumer Secret** that you noted in [Registering PingFederate as a connected app in Salesforce](pf_salesforce_connector_registering_pf_as_a_connected_app_in_salesforce.html).

   3. In the **OAuth Access Token** field, enter the **Access Token** that you noted in [Getting an API access token from Salesforce](pf_salesforce_connector_getting_an_api_access_token_from_salesforce.html).

   4. In the **OAuth Refresh Token** field, enter the **Refresh Token** that you noted in [Getting an API access token from Salesforce](pf_salesforce_connector_getting_an_api_access_token_from_salesforce.html).

   5. If you want to provision to Salesforce Communities, select **Enable Communities**.

   6. Under **Provisioning Options**, customize the provisioning connector behavior. Click **Next**.

      Learn more about [Provisioning options reference](pf_salesforce_connector_provisioning_options_reference.html).

   7. On the **Manage Channels > Attribute Mapping** tab, at the bottom of the attribute list, click **Refresh Fields** to get fields and specifications from your Salesforce site. Complete the attribute mappings by referring to [Supported attributes reference](pf_salesforce_connector_supported_attributes_reference.html).

      You can learn more in [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation.

      |   |                                                                                                                                                                       |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you're provisioning to Salesforce Communities, you must map attributes for any Salesforce fields that are required, including custom fields in users and contacts. |

6. On the **Activation and Summary** page, above the **Summary** section, note the **SSO Application Endpoint**.

   Use this value for the **Identity Provider Login URL** of the provider that you configured in [Registering PingFederate as an SSO provider in Salesforce](pf_salesforce_connector_registering_pf_as_an_sso_provider_in_salesforce.html).

7. Turn on the connection and then click **Save**.

---

---
title: Creating a provisioning connection
description: To allow PingFederate to manage users in Salesforce, configure a service provider (SP) connection.
component: salesforce
page_id: salesforce:salesforce_contacts_provisioner:pf_salesforce_contacts_connector_creating_a_provisioning_connection
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_contacts_provisioner/pf_salesforce_contacts_connector_creating_a_provisioning_connection.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating a provisioning connection

To allow PingFederate to manage users in Salesforce, configure a service provider (SP) connection.

## About this task

Configure PingFederate to provision users and groups to Salesforce and enable single sign-on (SSO). You can find more general information in [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | You can complete the following steps to create a new SP connection or you can modify an existing connection. |

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   **Choose from:**

   * For PingFederate 10.1 or later: Go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: Go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. On the **Connection Template** tab, select **Do not use a template for this connection**. Click **Next**.

3. On the **Connection Type** tab, select only **Outbound Provisioning**. In the **Type** list, select **Salesforce Contacts Provisioner**. Click **Next**.

4. On the **General Info** tab, configure the basic connection information.

   1. In the **Entity ID** field, enter any value. This field is not used for this integration.

   2. In the **Connection Name** field, enter a name that you choose. Click **Next**.

5. On the **Outbound Provisioning** tab, configure provisioning with the following details:

   You can find more information in [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation:

   1. On the **Target** tab, in the **Client ID** field, enter the **Consumer Key** that you noted in [Registering PingFederate as a connected app in Salesforce](pf_salesforce_contacts_connector_registering_pf_as_a_connected_app_in_salesforce.html).

   2. In the **Client Secret** field, enter the **Consumer Secret** that you noted in [Registering PingFederate as a connected app in Salesforce](pf_salesforce_contacts_connector_registering_pf_as_a_connected_app_in_salesforce.html).

   3. In the **OAuth Access Token** field, enter the **Access Token** that you noted in [Getting an API access token from Salesforce](pf_salesforce_contacts_connector_getting_an_api_access_token_from_salesforce.html).

   4. In the **OAuth Refresh Token** field, enter the **Refresh Token** that you noted in [Getting an API access token from Salesforce](pf_salesforce_contacts_connector_getting_an_api_access_token_from_salesforce.html).

   5. In the **Salesforce Domain** field, enter the domain of your Salesforce site. For example, `mycompany.my.salesforce.com` in the URL https\://mycompany.my.salesforce.com.

   6. In the **Salesforce Record Type** list, select the type of record you want to create in Salesforce.

      |   |                                                                                                                                                                                                                                         |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You can find more information about [Contacts](https://help.salesforce.com/articleView?id=contacts_overview.htm\&type=5) and [Leads](https://help.salesforce.com/articleView?id=leads_def.htm\&type=5) in the Salesforce documentation. |

      |   |                                                                                                                                                                                                 |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Although you can change this setting after creating the connection, it requires that you refresh and remap all attributes. Instead, you can create a new connection with the other record type. |

   7. Under **Provisioning Options**, customize the provisioning connector behavior by referring to [Provisioning options reference](pf_salesforce_contacts_connector_provisioning_options_reference.html).

   8. On the **Manage Channels > Attribute Mapping** tab, at the bottom of the attribute list, click **Refresh Fields** to get fields and specifications from your Salesforce site. Complete the attribute mappings by referring to [Supported attributes reference](pf_salesforce_contacts_connector_supported_attributes_reference.html).

      You can find more information in [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation.

6. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: Define the SSO URL in Salesforce
description: In your Salesforce administrative web interface, add a custom link to initiate single sign-on (SSO) where needed for your Salesforce deployment. The content of the link depends on the PingFederate configuration.
component: salesforce
page_id: salesforce:salesforce_login_integration_kit:pf_salesforce_cic_define_the_sso_url_in_salesforce
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_login_integration_kit/pf_salesforce_cic_define_the_sso_url_in_salesforce.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Define the SSO URL in Salesforce

In your Salesforce administrative web interface, add a custom link to initiate single sign-on (SSO) where needed for your Salesforce deployment. The content of the link depends on the PingFederate configuration.

|   |                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Salesforce navigational details and identification of pages and selections in these steps are subject to change. Only the configuration options directly relevant to the PingFederate Connector are described. Some configuration steps are summarized and different configurations may be possible. Ensure you consult the Salesforce documentation for complete and up-to-date information as needed. |

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Salesforce Contacts Provisioner files to your PingFederate directory.
component: salesforce
page_id: salesforce:salesforce_contacts_provisioner:pf_salesforce_contacts_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_contacts_provisioner/pf_salesforce_contacts_connector_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Salesforce Contacts Provisioner files to your PingFederate directory.

## Steps

1. Download the Salesforce Contacts Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/salesforce-leads-and-contacts-provisioner).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete `pf-salesforce-contacts-quickconnection-<version>.jar` from `<pf_install>/pingfederate/server/default/deploy`.

4. In the `.zip` archive, copy the contents of `dist` to `<pf_install>/pingfederate/server/default`.

5. Enable the PingFederate provisioning engine.

   1. In `<pf_install>/pingfederate/bin`, open `run.properties` for editing.

   2. Change `pf.provisioner.mode` to `STANDALONE`. Save the file.

      |   |                                                                                                                                                                                                                                                       |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Learn more about how to configure `FAILOVER` mode instead in [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate Server Clustering Guide. |

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 2 - 6 for each engine node.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Salesforce Provisioner files to your PingFederate directory.
component: salesforce
page_id: salesforce:salesforce_provisioner:pf_salesforce_connector_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_provisioner/pf_salesforce_connector_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Salesforce Provisioner files to your PingFederate directory.

## Steps

1. Download the Salesforce Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/salesforce-single-signon-integration).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the `pf-salesforce-quickconnection-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate/server/default/deploy` directory.

5. Enable the PingFederate provisioning engine:

   1. Open your `<pf_install>/pingfederate/bin/run.properties` file.

   2. Change `pf.provisioner.mode` to `STANDALONE`.

   3. Save the file.

      |   |                                                                                                                                                                                                                                                            |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Learn more about how you can configure `FAILOVER` mode instead in [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate Server Clustering Guide. |

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 2 - 4 and step 6 for each engine node.

---

---
title: Download manifest
description: The following files are included in the Salesforce .zip archive:
component: salesforce
page_id: salesforce:salesforce_contacts_provisioner:pf_salesforce_contacts_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_contacts_provisioner/pf_salesforce_contacts_connector_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Download manifest

The following files are included in the Salesforce `.zip` archive:

* `ReadMeFirst.pdf`: Contains links to this online documentation

* `legal`: A directory that contains the legal document

  * `Legal.pdf`: Copyright and license information

* `dist`: Contains the integration files

  * `deploy`: Contains the Java libraries

    * `pf-salesforce-contacts-quickconnection-<version>.jar`: The Salesforce Contacts Provisioner quick connection template

---

---
title: Download manifest
description: The distribution .zip archive for the connector contains the following:
component: salesforce
page_id: salesforce:salesforce_login_integration_kit:pf_salesforce_cic_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_login_integration_kit/pf_salesforce_cic_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Download manifest

The distribution `.zip` archive for the connector contains the following:

* `/docs`: Contains this documentation:

  * `Salesforce_Cloud_Identity_Connector_Qualification_Statement.pdf`: Testing and platform information

  * `Salesforce_Cloud_Identity_Connector_User_Guide.pdf`: This document

* `/dist`: Contains libraries needed for the adapter:

  * `pf-salesforce-idp-adapter-1.0.jar`: Salesforce Adapter `.jar` file

  * `salesforce-partner-api-20.jar `: Salesforce application programming interface (API)

---

---
title: Download manifest
description: The following files are included in the Salesforce Provisioner .zip archive:
component: salesforce
page_id: salesforce:salesforce_provisioner:pf_salesforce_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_provisioner/pf_salesforce_connector_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2024
---

# Download manifest

The following files are included in the Salesforce Provisioner `.zip` archive:

* `legal`: A directory that contains the legal document

  * `Legal.pdf`: Copyright and license information

* `dist`: Contains the integration files

  * `pf-salesforce-quickconnection-<version>.jar`: The Salesforce Provisioner quick connection template

---

---
title: Enabling provisioning and single sign-on (SSO) in PingFederate
description: To use PingFederate for provisioning and SSO, configure an external datastore and set a SAML entity ID.
component: salesforce
page_id: salesforce:salesforce_provisioner:pf_salesforce_connector_enabling_provisioning_and_single_sign_on_in_pf
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_provisioner/pf_salesforce_connector_enabling_provisioning_and_single_sign_on_in_pf.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  enabling-provisioning-and-sso-in-pingfederate-10-1-or-later: Enabling provisioning and SSO in PingFederate 10.1 or later
  steps: Steps
  enabling-provisioning-and-sso-in-pingfederate-10-0-or-earlier: Enabling provisioning and SSO in PingFederate 10.0 or earlier
  steps-2: Steps
---

# Enabling provisioning and single sign-on (SSO) in PingFederate

To use PingFederate for provisioning and SSO, configure an external datastore and set a SAML entity ID.

## About this task

Your external datastore acts as the source of data for provisioning. PingFederate also uses an internal datastore to store the state of synchronization between the source datastore and the target datastore.

Learn more about [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) and [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

## Enabling provisioning and SSO in PingFederate 10.1 or later

### Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   Learn more about [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Server > Protocol Settings > Federation Info**.

3. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use when identifying itself to SAML partners.

4. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   Learn more about [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

## Enabling provisioning and SSO in PingFederate 10.0 or earlier

### Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   Learn more about [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Protocol Settings > Roles & Protocols**.

3. Select the **Enable Identity Provider IdP Role and Support the Following** checkbox.

4. Select the **SAML 2.0** and **Outbound Provisioning** checkboxes. Click **Next**.

5. Click the **Federation Info** tab.

6. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

7. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   Learn more about [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Enabling provisioning and SSO in PingFederate 10.0 or earlier
description: In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.
component: salesforce
page_id: salesforce:salesforce_provisioner:pf_salesforce_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_provisioner/pf_salesforce_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  steps: Steps
---

# Enabling provisioning and SSO in PingFederate 10.0 or earlier

## Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   Learn more about [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Protocol Settings > Roles & Protocols**.

3. Select the **Enable Identity Provider IdP Role and Support the Following** checkbox.

4. Select the **SAML 2.0** and **Outbound Provisioning** checkboxes. Click **Next**.

5. Click the **Federation Info** tab.

6. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

7. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   Learn more about [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Enabling provisioning and SSO in PingFederate 10.1 or later
description: In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.
component: salesforce
page_id: salesforce:salesforce_provisioner:pf_salesforce_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_provisioner/pf_salesforce_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  steps: Steps
---

# Enabling provisioning and SSO in PingFederate 10.1 or later

## Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   Learn more about [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Server > Protocol Settings > Federation Info**.

3. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use when identifying itself to SAML partners.

4. On the **Outbound Provisioning** tab, in the **Provisioner Data Store** list, select the internal database that will store the synchronization state. Click **Save**.

   Learn more about [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Enabling provisioning in PingFederate
description: To use PingFederate for provisioning, configure an external datastore and enable outbound provisioning.
component: salesforce
page_id: salesforce:salesforce_contacts_provisioner:pf_salesforce_contacts_connector_enabling_provisioning_in_pf
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_contacts_provisioner/pf_salesforce_contacts_connector_enabling_provisioning_in_pf.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Enabling provisioning in PingFederate

To use PingFederate for provisioning, configure an external datastore and enable outbound provisioning.

## About this task

Your external datastore acts as the source of data for provisioning. PingFederate also uses an internal datastore to store the state of synchronization between the source datastore and the target datastore.

Learn more in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) and [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

## Steps

1. Configure the external datastore that PingFederate will use as the source of user data. You can find instructions in [Adding a new datastore](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_datasourcetasklet_selectdatasourcetypestate.html) in the PingFederate documentation.

   |   |                                                                                                                                                                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When targeting users and groups for provisioning, exclude the user account that you will use to administer users in your connection to Salesforce. This prevents the PingFederate provisioning engine from interfering with the account that provisions users and groups. |

2. Do one of the following:

   ### **Choose from:**

   * For PingFederate 10.1 or later: Go to **System > Server > Protocol Settings**.

   * For PingFederate 10.0 or earlier:

     1. Go to **System > Protocol Settings > Roles & Protocols**.

     2. Select **Enable Identity Provider IdP Role and Support the Following**.

     3. Select **Outbound Provisioning**. Click **Next**.

3. On the **Outbound Provisioning** tab, select the PingFederate internal datastore. Click **Save**.

   You can find more information in [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Getting an API access token from Salesforce
description: PingFederate needs an access token to manage users and groups using the Salesforce API. You can use your consumer key and secret with the Ping Identity OAuth Configuration Service (OCS) tool to get your Salesforce access token.
component: salesforce
page_id: salesforce:salesforce_contacts_provisioner:pf_salesforce_contacts_connector_getting_an_api_access_token_from_salesforce
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_contacts_provisioner/pf_salesforce_contacts_connector_getting_an_api_access_token_from_salesforce.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Getting an API access token from Salesforce

## About this task

PingFederate needs an access token to manage users and groups using the Salesforce API. You can use your consumer key and secret with the Ping Identity OAuth Configuration Service (OCS) tool to get your Salesforce access token.

## Steps

1. In a browser, open Ping Identity's [OAuth Configuration Service](https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oasrequestform) (OCS).

2. In the service list, select **Salesforce Connector**.

3. In the **Client ID** field, enter the **Consumer Key** that you noted in [Registering PingFederate as a connected app in Salesforce](pf_salesforce_contacts_connector_registering_pf_as_a_connected_app_in_salesforce.html).

4. In the **Client Secret** field, enter your **Consumer Secret**.

5. Click **Connect**.

   ![oud1567794788952](../_images/oud1567794788952.png)

6. Authorize the request through Salesforce.

   1. If you receive a message asking you to sign on to Salesforce, enter your Salesforce administrator credentials and then click **Log In**.

   2. On the Salesforce **Allow Access** dialog, click **Allow**.

7. On the **Service Response** dialog, note the **Access Token** and **Refresh Token**.

   You will use these tokens in [Creating a provisioning connection](pf_salesforce_contacts_connector_creating_a_provisioning_connection.html).

   ![vik1567794897114](../_images/vik1567794897114.png)

---

---
title: Getting an API access token from Salesforce
description: PingFederate and PingOne need an access token to manage users and groups using the Salesforce API. You can use your consumer key and secret with the Ping Identity OAuth Configuration Service (OCS) tool to get your Salesforce access token.
component: salesforce
page_id: salesforce:salesforce_provisioner:pf_salesforce_connector_getting_an_api_access_token_from_salesforce
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_provisioner/pf_salesforce_connector_getting_an_api_access_token_from_salesforce.html
llms_txt: https://docs.pingidentity.com/integrations/salesforce/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Getting an API access token from Salesforce

## About this task

PingFederate and PingOne need an access token to manage users and groups using the Salesforce API. You can use your consumer key and secret with the Ping Identity OAuth Configuration Service (OCS) tool to get your Salesforce access token.

## Steps

1. In a browser, open Ping Identity's [OAuth Configuration Service](https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oasrequestform) (OCS).

2. In the service list, select **Salesforce Connector**.

3. In the **Client ID** field, enter the **Consumer Key** that you noted in [Registering PingFederate as a connected app in Salesforce](pf_salesforce_connector_registering_pf_as_a_connected_app_in_salesforce.html).

4. In the **Client Secret** field, enter your **Consumer Secret**.

5. Click **Connect**.

   ![oud1567794788952](../_images/oud1567794788952.png)

6. Authorize the request through Salesforce:

   1. If you receive a message asking you to sign on to Salesforce, enter your Salesforce administrator credentials and then click **Log In**.

   2. On the Salesforce **Allow Access** dialog, click **Allow**.

7. On the **Service Response** dialog, note the **Access Token** and **Refresh Token**.

   You will use these tokens in [Creating a connection](pf_salesforce_connector_creating_a_connection.html)

   ![vik1567794897114](../_images/vik1567794897114.png)