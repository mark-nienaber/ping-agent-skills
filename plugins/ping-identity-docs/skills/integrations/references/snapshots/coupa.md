---
title: Attribute index
description: The following table lists the user attributes that you can map for provisioning.
component: coupa
page_id: coupa:setup:pf_coupa_connector_attribute_index
canonical_url: https://docs.pingidentity.com/integrations/coupa/setup/pf_coupa_connector_attribute_index.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 14, 2024
---

# Attribute index

The following table lists the user attributes that you can map for provisioning.

| Attribute                                       | Description                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `login`                                         | Login name for the user.&#xA;&#xA;This value must be unique.                                                                                                                                                                                                                                                                                                        |
| `email`                                         | User's email address.&#xA;&#xA;This value must be unique.                                                                                                                                                                                                                                                                                                           |
| `firstName`                                     | User's first name.                                                                                                                                                                                                                                                                                                                                                  |
| `lastName`                                      | User's last name.                                                                                                                                                                                                                                                                                                                                                   |
| `employee-number`                               | User's Employee Number.&#xA;&#xA;This value must be unique.                                                                                                                                                                                                                                                                                                         |
| `authentication-method`                         | The method of authentication for the user. Acceptable values include `coupa-credentials` (default), `saml`, and `ldap`.When setting a user's authentication-method to `saml` or `ldap`, you must configure the security settings of your Coupa account.                                                                                                             |
| `role`                                          | The names of roles the user is a member of. If you don't set a role, users will be assigned to the `User` role by default.The roles must exist already in Coupa before you can add a user to them.&#xA;&#xA;User roles can't be cleared directly by the Coupa Connector. However, you can set the role to User, the default user role.                              |
| `password`                                      | The User's Coupa password.This value is ignored when `generate-password-and-notify` is set to `true`.                                                                                                                                                                                                                                                               |
| `generate-password-and-notify`                  | When creating or updating users with this field set to `true`, an email is sent to the `email` set for the user allowing the user to reset their own password. Acceptable values are `true` and `false`.If you want to set the password for a user using the `password` attribute, `generate-password-and-notify` must be set to `false`.                           |
| `SSO-identifier`                                | User's Single Sign-on ID (SSO ID).&#xA;&#xA;This value must be unique.                                                                                                                                                                                                                                                                                              |
| `phone-mobile`                                  | User's mobile phone number, such as `1 222-333-4444 ext. 12345`.&#xA;&#xA;Coupa only accepts certain formats for phone numbers. If you have difficulty correctly formatting numbers, you can reach Coupa support:&#xA;&#xA;Online at https\://support.coupa.com.&#xA;&#xA;By email at support\@coupa.com.&#xA;&#xA;Through your Coupa Implementation Administrator. |
| `phone-work`                                    | User's work phone number, such as `1 222-333-4444 ext. 12345`.&#xA;&#xA;Coupa only accepts certain formats for phone numbers. If you have difficulty correctly formatting numbers, you can reach Coupa support:- Online at <https://support.coupa.com>.

- By email at <support@coupa.com>.

- Through your Coupa Implementation Administrator.                     |
| `manager`                                       | The `login` attribute value of the user's manager.The manager must exist already on the Coupa account before it can be added as a manager of another user.                                                                                                                                                                                                          |
| `Requisition Approval Limit Amount`             | User's approval limit, such as `1000.00`.                                                                                                                                                                                                                                                                                                                           |
| `Requisition Approval Limit Currency`           | User's requisition approval limit currency code, such as `CAD`.The list of valid currency codes available for your use can be found on your Coupa accounts currencies list at https\://*Your\_Subdomain*.coupacloud.com/currencies.                                                                                                                                 |
| `Invoice Approval Limit Amount`                 | User's approval limit, such as `1000.00`.                                                                                                                                                                                                                                                                                                                           |
| `Invoice Approval Limit Currency`               | User's invoice approval limit currency code, such as`CAD`.The list of valid currency codes available for your use can be found on your Coupa accounts currencies list at https\://*Your\_Subdomain*.coupacloud.com/currencies.                                                                                                                                      |
| `Content-Groups`                                | The names of content groups the user is a member of.The content groups must exist already in Coupa before you can add a user to them.&#xA;&#xA;Content groups can't be cleared directly by the Coupa Connector. However, you can remove a user from all content groups through the Coupa admin console.                                                             |
| `Requisition Self-Approval Limit Amount`        | User's self-Approval limit, such as `1000.00`.                                                                                                                                                                                                                                                                                                                      |
| `Requisition Self-Approval Limit Currency Code` | User's requisition self-approval limit currency code, such as `CAD`.The list of valid currency codes available for your use can be found on your Coupa accounts currencies list at https\://*Your\_Subdomain*.coupacloud.com/currencies.                                                                                                                            |
| `Approval Groups`                               | The names of approval groups the user is a member of.The approval groups must exist already in Coupa before you can add a user to them.&#xA;&#xA;Approval groups can't be cleared directly by the Coupa Connector. However, you can remove a user from all approval groups through the Coupa admin console.                                                         |
| `Default Currency`                              | User's Default Currency Code, such as `CAD`.The list of valid currency codes available for your use can be found on your Coupa accounts currencies list at https\://*Your\_Subdomain*.coupacloud.com/currencies.                                                                                                                                                    |
| `Departments`                                   | The names of departments the user is a member of.The departments must exist already in Coupa before you can add a user to them.                                                                                                                                                                                                                                     |

---

---
title: Changelog
description: The following changes have been implemented for the Coupa Connector:
component: coupa
page_id: coupa:release_notes:pf_coupa_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/coupa/release_notes/pf_coupa_connector_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 14, 2024
section_ids:
  coupa-connector-1-0-february-2015-current-release: Coupa Connector 1.0 — February 2015 (Current Release)
---

# Changelog

The following changes have been implemented for the Coupa Connector:

## Coupa Connector 1.0 — February 2015 (Current Release)

* Initial release.

* Added support for user provisioning.

* Added support for browser-based single sign-on (SSO).

---

---
title: Completing setup of SAML SSO to Coupa
description: The following steps outline how to complete the configuration of your Coupa account and service provider (SP) connection to enable identity provider (IdP) or SP-initiated SAML single sign-on (SSO).
component: coupa
page_id: coupa:setup:pf_coupa_connector_complete_setup_of_saml_sso_to_coupa
canonical_url: https://docs.pingidentity.com/integrations/coupa/setup/pf_coupa_connector_complete_setup_of_saml_sso_to_coupa.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 14, 2024
---

# Completing setup of SAML SSO to Coupa

The following steps outline how to complete the configuration of your Coupa account and service provider (SP) connection to enable identity provider (IdP) or SP-initiated SAML single sign-on (SSO).

|   |                                                                                            |
| - | ------------------------------------------------------------------------------------------ |
|   | Coupa supports either SP or IdP-initiated SAML SSO on a given Coupa account, but not both. |

|   |                                                                                              |
| - | -------------------------------------------------------------------------------------------- |
|   | You can find more information in the [Coupa documentation](https://coupa-external.okta.com). |

---

---
title: Configuring Coupa for SAML SSO
description: For assistance configuring Coupa for SAML single sign-on (SSO), Coupa recommends you send your prepared idp-metadata.xml to their support team or your Coupa Implementation Administrator along with:
component: coupa
page_id: coupa:setup:pf_coupa_connector_configuring_coupa_for_saml_sso
canonical_url: https://docs.pingidentity.com/integrations/coupa/setup/pf_coupa_connector_configuring_coupa_for_saml_sso.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 14, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Configuring Coupa for SAML SSO

## About this task

|   |                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For assistance configuring Coupa for SAML single sign-on (SSO), Coupa recommends you send your prepared `idp-metadata.xml` to their support team or your Coupa Implementation Administrator along with:- Login page URL

- Logout page URL

- Timeout URL

- A test user that exists in your identity provider (IdP) |

## Steps

1. Sign on to your Coupa account as an administrative user.

2. Click the **Setup** tab.

3. In the **Company Setup** section, click **Security controls**.

4. Import the `idp-metadata.xml` that you prepared above into the **Upload IdP metadata** field.

   |   |                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | During development and testing of the Coupa connector, Ping Identity was unable to upload the `idp-metadata.xml` into Coupa without receiving errors. Coupa Support assisted with this configuration. |

5. Select the **Advanced Options** checkbox.

6. In the **Login page URL** field, enter the Login page URL:

   ### Choose from:

   * SP-initiated SSO: Enter `https://prdsso40.cloudcoupa.com/sp/startSSO.ping?PartnerIdpId=YOUR_PF_ENTITY_ID&TARGET=https://YOUR_COUPA_SUBDOMAIN.cloudcoupa.com/sessions/saml_post`

   * IdP-Initiated SSO: Points to the login page of your IdP.

7. In the **Logout page URL** field, enter the Logout page URL.

   The **Logout page URL** is set to where your users should be directed when they sign off of Coupa.

8. In the **Timeout URL** field, enter the Timeout URL.

   The **Timeout URL** is set to where your users should be directed if their session times out before they sign on.

9. Click **Save**.

---

---
title: Configuring your SP connection for IdP-initiated SSO
description: This task is only required if you want to enable identity provider (IdP)-initiated single sign-in (SSO).
component: coupa
page_id: coupa:setup:pf_coupa_connector_configuring_your_sp_connection_for_idp_initiated_sso
canonical_url: https://docs.pingidentity.com/integrations/coupa/setup/pf_coupa_connector_configuring_your_sp_connection_for_idp_initiated_sso.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 14, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring your SP connection for IdP-initiated SSO

## About this task

|   |                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------- |
|   | This task is only required if you want to enable identity provider (IdP)-initiated single sign-in (SSO). |

To successfully configure your SP connection for IdP-initiated SSO, you must add a `RelayState` parameter to your SP connection's Assertion Consumer Service (ACS) URL.

## Steps

1. In the PingFederate admin console, click your Coupa SP connection to edit it.

2. In the **Protocol Settings** section, click the **Assertion Consumer Service URL** link.

3. Click **Edit** for the endpoint URL you're using in your SP connection.

4. Enter the following endpoint URL, which contains the `RelayState` parameter:

   ```none
    /sp/ACS.saml2?RelayState=https://YourSubDomain.coupacloud.com/sessions/saml_post
   ```

   The *YourSubDomain* variable is your Coupa subdomain, which you obtained in [Obtaining required information](pf_coupa_connector_obtain_required_information.html).

5. Click **Update**.

6. Click **Done**, **Done** and **Save**.

---

---
title: Coupa Provisioner
description: The PingFederate Provisioner for Coupa enables an enterprise to provision its users to Coupa. This Coupa Provisioner includes a quick connection template to easily set up a single sign-on (SSO) connection requiring Coupa provisioning.
component: coupa
page_id: coupa::pf_coupa_connector
canonical_url: https://docs.pingidentity.com/integrations/coupa/pf_coupa_connector.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 14, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Coupa Provisioner

The PingFederate Provisioner for Coupa enables an enterprise to provision its users to Coupa. This Coupa Provisioner includes a quick connection template to easily set up a single sign-on (SSO) connection requiring Coupa provisioning.

## Features

* Outbound user provisioning

* Browser-based SAML SSO

## Intended audience

This document is intended for PingFederate administrators.

## System requirements

* PingFederate 7.2.1 or later

* Common Provisioning Layer (CPL) 2.0.1 or later (`prov-cpl-2.0.1.jar`)

---

---
title: Creating a connection
description: To allow PingFederate to act as an identity provider (IdP) and manage users in Coupa, create a service provider (SP) connection.
component: coupa
page_id: coupa:setup:pf_coupa_connector_creating_a_connection
canonical_url: https://docs.pingidentity.com/integrations/coupa/setup/pf_coupa_connector_creating_a_connection.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 14, 2024
section_ids:
  steps: Steps
---

# Creating a connection

To allow PingFederate to act as an identity provider (IdP) and manage users in Coupa, create a service provider (SP) connection.

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   **Choose from:**

   * For PingFederate 10.1 or later: Go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: Go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details with the Coupa quick connection template:

   1. On the **Connection Template** tab, click **Use a template for this connection**.

   2. In the **Connection Template** list, select **Coupa Provisioner**.

   3. On the **Metadata File** row, upload the `idp-metadata.xml` file that you saved in [Obtaining your Coupa (SP) metadata file](pf_coupa_connector_obtaining_your_coupa_sp_metadata_file.html). Click **Next**.

   4. On the **Connection Type** tab select the **Browser SSO Profiles** and **Outbound Provisioning** checkboxes. Click **Next**.

   5. On the **Connection Options** tab, click **Next**.

   6. On the **General Info** tab, in the **Connection Name** field, enter a name of your choosing. Click **Next**.

3. On the **Browser SSO** tab, configure your assertion creation settings and customize the defaults set by the metadata file.

   You can find more information in [Configuring IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation.

4. On the **Credentials** tab, configure the connection credentials as shown in [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation. Click **Next**.

5. On the **Outbound Provisioning** tab, configure provisioning with the following details.

   Learn more in [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

   1. On the **Target** tab, enter the API key and subdomain you noted in [Obtaining required information](pf_coupa_connector_obtain_required_information.html).

   2. (Optional) In the **Provisioning Options** section, customize the provisioning connector behavior. Click **Next**.

   3. Go to **Manage Channels > Attribute Mapping** tab and at the bottom of the attribute list, click **Refresh Fields** to get fields and specifications from your Coupa site.

   4. Complete the attribute mappings by referring to the [Attribute index](pf_coupa_connector_attribute_index.html).

      For help, reference [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation.

6. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: Download manifest
description: The distribution .zip archive for the connector contains the following files:
component: coupa
page_id: coupa:release_notes:pf_coupa_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/coupa/release_notes/pf_coupa_connector_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 14, 2024
---

# Download manifest

The distribution `.zip` archive for the connector contains the following files:

* `ReadMeFirst.pdf`: Contains links to this online documentation

* `idp-metadata.xml`: The metadata used for browser single sign-on (SSO)

* `/legal`:

  * `Legal.pdf`: Copyright and license information

* `/dist`: Contains libraries needed for the connector:

  * `pf-coupa-quickconnection-1.0.jar`: PingFederate Coupa Connector

  * `prov-cpl-2.0.1.jar`: PingFederate Common Provisioning Layer

---

---
title: Enabling provisioning and single sign-on (SSO) in PingFederate
description: To use PingFederate for provisioning and single sign-on, configure an external datastore and set a SAML entity ID.
component: coupa
page_id: coupa:setup:pf_coupa_connector_enabling_provisioning_and_single_sign_on_in_pf
canonical_url: https://docs.pingidentity.com/integrations/coupa/setup/pf_coupa_connector_enabling_provisioning_and_single_sign_on_in_pf.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 14, 2024
section_ids:
  about-this-task: About this task
  enabling-provisioning-and-single-sign-on-sso-in-pingfederate-10-1-or-later: Enabling provisioning and single sign-on (SSO) in PingFederate 10.1 or later
  steps: Steps
  enabling-provisioning-and-single-sign-on-sso-in-pingfederate-10-0-or-earlier: Enabling provisioning and single sign-on (SSO) in PingFederate 10.0 or earlier
  steps-2: Steps
---

# Enabling provisioning and single sign-on (SSO) in PingFederate

To use PingFederate for provisioning and single sign-on, configure an external datastore and set a SAML entity ID.

## About this task

Your external datastore acts as the source of data for provisioning. PingFederate also uses an internal datastore to store the state of synchronization between the source datastore and the target datastore.

You can find more information in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) and [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

## Enabling provisioning and single sign-on (SSO) in PingFederate 10.1 or later

### Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   Learn more about [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Server > Protocol Settings > Federation Info**.

3. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use when identifying itself to SAML partners.

4. On the **Outbound Provisioning** tab, in the **Provisioner Datastore** list, select the internal database that will store the synchronization state. Click **Save**.

   Learn more in [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

## Enabling provisioning and single sign-on (SSO) in PingFederate 10.0 or earlier

### Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   Learn more in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Protocol Settings > Roles & Protocols**.

3. Select the **Enable Identity Provider IdP Role and Support the Following** checkbox.

4. Select the **SAML 2.0** and **Outbound Provisioning** checkboxes. Click **Next**.

5. Click the **Federation Info** tab.

6. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

7. On the **Outbound Provisioning** tab, in the **Provisioner Datastore** list, select the internal database that will store the synchronization state. Click **Save**.

   Learn more in [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Enabling provisioning and single sign-on (SSO) in PingFederate 10.0 or earlier
description: In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.
component: coupa
page_id: coupa:setup:pf_coupa_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/coupa/setup/pf_coupa_connector_enabling_provisioning_and_single_sign_on_in_pf_100_or_earlier.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Enabling provisioning and single sign-on (SSO) in PingFederate 10.0 or earlier

## Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   Learn more in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Protocol Settings > Roles & Protocols**.

3. Select the **Enable Identity Provider IdP Role and Support the Following** checkbox.

4. Select the **SAML 2.0** and **Outbound Provisioning** checkboxes. Click **Next**.

5. Click the **Federation Info** tab.

6. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

7. On the **Outbound Provisioning** tab, in the **Provisioner Datastore** list, select the internal database that will store the synchronization state. Click **Save**.

   Learn more in [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Enabling provisioning and single sign-on (SSO) in PingFederate 10.1 or later
description: In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.
component: coupa
page_id: coupa:setup:pf_coupa_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/coupa/setup/pf_coupa_connector_enabling_provisioning_and_single_sign_on_in_pf_101_or_later.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Enabling provisioning and single sign-on (SSO) in PingFederate 10.1 or later

## Steps

1. In the PingFederate administrative console, configure the datastore for PingFederate to use as the source of user data.

   Learn more about [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html) in the PingFederate documentation.

2. Go to **System > Server > Protocol Settings > Federation Info**.

3. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use when identifying itself to SAML partners.

4. On the **Outbound Provisioning** tab, in the **Provisioner Datastore** list, select the internal database that will store the synchronization state. Click **Save**.

   Learn more in [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) in the PingFederate documentation.

---

---
title: Known issues and limitations
description: The following are known issues and limitations of the Coupa Connector integration:
component: coupa
page_id: coupa:release_notes:pf_coupa_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/coupa/release_notes/pf_coupa_connector_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 14, 2024
---

# Known issues and limitations

The following are known issues and limitations of the Coupa Connector integration:

* Because of a limitation in PingFederate 8.1 and earlier versions, when configuring two service provider (SP) connections with the same provisioner, the second connection built might be pre-populated with the channel from the first connection. To avoid conflicts, delete this pre-populated channel and create a unique channel for each connection.

* Single logout (SLO) is not supported.

* Group (department) provisioning is not supported.

* User attributes cannot be cleared when set.

* Failed requests to update a user might remove the user from their roles, approval groups, content groups or departments until the update request is successfully retried.

* Managers must exist in Coupa before they can be added as the manager of another user. Not doing so results in a failure.

* Values set for the `phone-mobile` or `phone-work` attributes must adhere to how the service provider validates phone numbers. Not doing so results in a failure.

* Currency values are expected as a number with two decimals, for example `1000.00`. Not providing the value in the correct format might result in the value being stored as something different than what you sent, for example, `1,000.00` is stored as `1.00`.

---

---
title: Obtaining required information
description: Before you can configure this connector, you must complete the following steps:
component: coupa
page_id: coupa:setup:pf_coupa_connector_obtain_required_information
canonical_url: https://docs.pingidentity.com/integrations/coupa/setup/pf_coupa_connector_obtain_required_information.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 14, 2024
---

# Obtaining required information

Before you can configure this connector, you must complete the following steps:

* [Obtaining your Coupa subdomain](pf_coupa_connector_obtain_your_coupa_subdomain.html)

* [Obtaining your Coupa API key](pf_coupa_connector_obtaining_your_coupa_api_key.html)

* [Obtaining your Coupa (SP) metadata file](pf_coupa_connector_obtaining_your_coupa_sp_metadata_file.html)

* [Synchronizing existing Coupa users](pf_coupa_connector_synchronize_existing_coupa_users.html)

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some of these steps result in information that you'll need for subsequent tasks. You should copy this information to a secure location. |

---

---
title: Obtaining the EntityDescriptor's ID from your SP connection
description: Export your service provider (SP) connection's metadata.xml file:
component: coupa
page_id: coupa:setup:pf_coupa_connector_obtaining_the_entitydescriptors_id_from_your_sp_connection
canonical_url: https://docs.pingidentity.com/integrations/coupa/setup/pf_coupa_connector_obtaining_the_entitydescriptors_id_from_your_sp_connection.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  steps: Steps
  example: Example:
---

# Obtaining the EntityDescriptor's ID from your SP connection

## Steps

1. Export your service provider (SP) connection's `metadata.xml` file:

   1. In the PingFederate admin console, in the **SP Connection** section, click **Manage All SP**.

   2. Click **Export Metadata** for your Coupa SP connection.

   3. Select the signing certificate you used in that SP connection and click **Next**.

   4. Click the **Export** button to download the metadata file.

   5. Click **Done** and then click **Save**.

2. After you have the metadata from your SP connection, view the metadata file that you exported and record the ID value of the `EntityDescriptor` tag at the top of the file.

   ### Example:

   The following SP connection metadata file example shows the `EntityDescriptor` ID value at the top of the file, in this case `"R6HV.w-pHhv_pacAMTH7D-nFe3W"`.

   ![Screen capture of a sample SP connection metadata file with the EntityDescriptor ID value highlighted in blue.](_images/edm1563995238524.jpg)

---

---
title: Obtaining your Coupa (SP) metadata file
description: This connector's quick-connection template uses a metadata XML file to assist in configuring many settings in the service provider (SP) connection.
component: coupa
page_id: coupa:setup:pf_coupa_connector_obtaining_your_coupa_sp_metadata_file
canonical_url: https://docs.pingidentity.com/integrations/coupa/setup/pf_coupa_connector_obtaining_your_coupa_sp_metadata_file.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 14, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Obtaining your Coupa (SP) metadata file

This connector's quick-connection template uses a metadata XML file to assist in configuring many settings in the service provider (SP) connection.

## About this task

Before configuring your SP connection, you must download the `idp-metadata.xml` from Coupa.

|   |                                                                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To enable single sign-on (SSO), you must follow the steps outlined in the [Completing setup of SAML SSO to Coupa](pf_coupa_connector_complete_setup_of_saml_sso_to_coupa.html) section of this guide after you have completed the [Creating a connection](pf_coupa_connector_creating_a_connection.html) section. |

## Steps

1. Sign on to Coupa as an administrative user.

2. Click the **Setup** tab.

3. In the **Company Setup** section, select the **Security controls** checkbox.

4. Click the **Coupa SP metadata** link labeled **Download and import SP metadata**.

---

---
title: Obtaining your Coupa API key
description: The Coupa Connector's outbound provisioning functionality is built using Coupa's REST API, which requires an API key for authentication.
component: coupa
page_id: coupa:setup:pf_coupa_connector_obtaining_your_coupa_api_key
canonical_url: https://docs.pingidentity.com/integrations/coupa/setup/pf_coupa_connector_obtaining_your_coupa_api_key.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 14, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Obtaining your Coupa API key

The Coupa Connector's outbound provisioning functionality is built using Coupa's REST API, which requires an API key for authentication.

## About this task

To create and obtain the Coupa API key:

## Steps

1. Sign on to your Coupa account as an administrative user.

2. Click the **Setup** tab.

3. In the **Company Setup** section, select the **API Keys** checkbox.

4. Click the **Create** button.

5. Complete the form and click the **Create** button.

---

---
title: Obtaining your Coupa subdomain
description: This connector requires your Coupa subdomain to access your Coupa account for single sign-on (SSO) and outbound provisioning.
component: coupa
page_id: coupa:setup:pf_coupa_connector_obtain_your_coupa_subdomain
canonical_url: https://docs.pingidentity.com/integrations/coupa/setup/pf_coupa_connector_obtain_your_coupa_subdomain.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 14, 2024
---

# Obtaining your Coupa subdomain

This connector requires your Coupa subdomain to access your Coupa account for single sign-on (SSO) and outbound provisioning.

Your Coupa subdomain is the subdomain portion of the URL you visit to access your Coupa account, for example, https\://*YourSubDomain*.Coupa.com.

---

---
title: "Preparing the <code class=\"filepath\">idp-metadata.xml</code> file"
description: Edit the idp-metadata.xml file that is packaged with the Coupa connector in a text editor.
component: coupa
page_id: coupa:setup:pf_coupa_connector_preparing_the_idp_metadata_xml_file
canonical_url: https://docs.pingidentity.com/integrations/coupa/setup/pf_coupa_connector_preparing_the_idp_metadata_xml_file.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Preparing the `idp-metadata.xml` file

## Steps

1. Edit the `idp-metadata.xml` file that is packaged with the Coupa connector in a text editor.

2. Replace `<YOUR_ENTITY_DESCRIPTOR_ID>` with the ID you obtained in [Obtaining the EntityDescriptor's ID from your SP connection](pf_coupa_connector_obtaining_the_entitydescriptors_id_from_your_sp_connection.html).

3. Replace `<YOUR_PF_ENTITY_ID>` with the PingFederate Entity ID you obtained in [Enabling provisioning and single sign-on (SSO) in PingFederate](pf_coupa_connector_enabling_provisioning_and_single_sign_on_in_pf.html).

4. Replace `<YOUR_PF_BASE_URL>` with the PingFederate base URL you obtained in [Enabling provisioning and single sign-on (SSO) in PingFederate](pf_coupa_connector_enabling_provisioning_and_single_sign_on_in_pf.html).

5. Save your changes.

---

---
title: Synchronizing existing Coupa users
description: If your Coupa account already has users you want to provision with the Coupa Connector, this is possible by completing the following steps.
component: coupa
page_id: coupa:setup:pf_coupa_connector_synchronize_existing_coupa_users
canonical_url: https://docs.pingidentity.com/integrations/coupa/setup/pf_coupa_connector_synchronize_existing_coupa_users.html
llms_txt: https://docs.pingidentity.com/integrations/coupa/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 14, 2024
---

# Synchronizing existing Coupa users

|   |                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If your Coupa account already has users you want to provision with the Coupa Connector, this is possible by completing the following steps. |

Ensure that the value mapped to the `email` attribute, when configuring the connector matches the existing Coupa users email address exactly as it appears in Coupa.

For example, on the **Attribute Mapping** tab, the user's **email** attribute on Coupa is mapped to the user's `mail` attribute in your LDAP. This synchronizes a user that already exists on Coupa with an `email` address in Coupa of john.smith\@mydomain.com. In this case, the user's **mail** attribute in LDAP would also have to be john.smith\@mydomain.com.

When the Coupa connector provisions for the first time, this address is used to synchronize the user in your LDAP datastore with the user in Coupa.