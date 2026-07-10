---
title: Changelog
description: Users are no longer required to provide the WebEx Site ID or Partner ID to configure outbound provisioning.
component: webex
page_id: webex:release_notes:pf_webex_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/webex/release_notes/pf_webex_connector_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/webex/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  webex-provisioner-2-3-june-2023-current-release: Webex Provisioner 2.3 – June 2023 (current release)
  webex-provisioner-2-1-july-2019: Webex Provisioner 2.1 – July 2019
  webex-provisioner-2-0-2-march-2017: Webex Provisioner 2.0.2 – March 2017
  webex-provisioner-2-0-1-february-2017: Webex Provisioner 2.0.1 – February 2017
  webex-provisioner-2-0-may-2016: Webex Provisioner 2.0 – May 2016
  webex-provisioner-1-0-1-february-2014: Webex Provisioner 1.0.1 – February 2014
  webex-provisioner-1-0-may-2010: Webex Provisioner 1.0 – May 2010
---

# Changelog

## Webex Provisioner 2.3 – June 2023 (current release)

Users are no longer required to provide the WebEx **Site ID** or **Partner ID** to configure outbound provisioning.

## Webex Provisioner 2.1 – July 2019

* Fixed an issue that prevented users with special characters from being provisioned to Webex.

* Improved error handling and reporting for cases where users in the target application do not have an ID.

* Improved error logging security.

* Added [provisioning options](../setup/pf_webex_connector_provisioning_options.html) to control the "create", "update", and "disable" functions individually.

## Webex Provisioner 2.0.2 – March 2017

* Fixed synchronization on update of users, that were previously created with "User Create Enabled" set to false in configurable options.

## Webex Provisioner 2.0.1 – February 2017

* Fixed handling of timezones not listed in Webex's 'Timezone encoding list' .

## Webex Provisioner 2.0 – May 2016

* Added support for additional user attributes.

* Added configuration options for CRUD capabilities.

* Added support for Webex API 10.0 SP3.

* Improved exception handling and reporting.

## Webex Provisioner 1.0.1 – February 2014

* Updated Webex API to use XMLBeans 2.6.0 to be compatible with PingFederate 7.x.

## Webex Provisioner 1.0 – May 2010

* Initial Release.

* Added Support for User Provisioning.

---

---
title: Configuring provisioning and single sign-on
description: You can follow these steps to create a new service provider (SP) connection, or you can modify an existing connection.
component: webex
page_id: webex:setup:pf_webex_connector_configuring_provisioning_and_single_sign_on
canonical_url: https://docs.pingidentity.com/integrations/webex/setup/pf_webex_connector_configuring_provisioning_and_single_sign_on.html
llms_txt: https://docs.pingidentity.com/integrations/webex/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring provisioning and single sign-on

## About this task

|   |                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------- |
|   | You can follow these steps to create a new service provider (SP) connection, or you can modify an existing connection. |

## Steps

1. In the PingFederate administrator console, configure the datastore that PingFederate will use as the source of user data.

   For instructions, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html) in the PingFederate documentation.

   |   |                                                                                                                                                                                                                                                                      |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When targeting users and groups for provisioning, exclude the user account that you will use to administer users in your connection to Webex. This prevents the PingFederate provisioning engine from interfering with the account that provisions users and groups. |

2. Enable provisioning:

   1. Go to **System > Protocol Settings > Roles & Protocols** and select **Enable Identity Provider IdP Role and Support the Following**.

   2. Select **Outbound Provisioning**. Click **Save**.

3. Create an SP connection with the Webex quick connection template:

   1. Follow the steps in [Downloading your Webex SAML metadata file](pf_webex_connector_downloading_your_webex_saml_metadata_file.html).

   2. On the PingFederate **Identity Provider** tab, in the **SP Connections** section, click **Create new**.

   3. On the **Connection Template** tab, select **Use a template for this connection**.

   4. In the **Connection Template** list, select **Webex Connector**.

   5. Click **Choose File**, select the Webex metadata file that you downloaded, and then click **Open**. Click **Next**.

4. On the **Connection Type** tab, select **Browser SSO Profiles** and **Outbound Provisioning**.

5. In the **Type** list, select **Webex Connector**. Click **Next**.

6. On the **Connection Options** tab, click **Next**.

7. On the **General Info** tab, the basic connection information is populated by the metadata XML file. Click **Next**.

8. On the **Browser SSO** tab, configure single sign-on (SSO) settings. Click **Next**.

   Follow the steps in [Configure IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation, with the following specifics:

   1. Go to **Browser SSO > SAML Profiles** and select **IdP-initiated SSO** and **SP-initiated SSO**.

   2. **Optional:** Go to **Browser SSO > Assertion Creation > Attribute Contract** and extend the contract. Webex supports the following formats:

      * Unspecified

      * Email address

      * X509 subject name

      * Entity identifier

      * Persistent identifier

   3. **Optional:** Add the special `SAML_AUTHN_CTX` attribute.

   This indicates to the SP the type of credentials used to authenticate to the identity provider (IdP) application.

   1. Go to **Browser SSO > Assertion Creation > Authentication Source Mapping** to configure your authentication source mappings:

      * If you added the special `SAML_AUTHN_CTX` attribute, on the **Attribute Contract Fulfillment** tab, map the attribute to a text value, such as `urn:oasis:names:tc:SAML:2.0:ac:classes:unspecified`.

   2. Go to **Browser SSO > Protocol Settings > Allowable SAML Bindings** and select **Post** and **Redirect**. Clear **Artifact** and **SOAP**.

   3. If you want to enable SP-initiated SSO, go to **Browser SSO > Protocol Settings > Signature Policy** and select **Require authn requests to be signed when received via the POST or Redirect bindings**.

9. On the **Credentials** tab, configure your credentials. Click **Next**.

   See [Configure credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation.

   1. Click **Configure Credentials**.

   2. Go to **Credentials > Digital Signature Settings** and in the **Signing Certificate** list, select a certificate to use to sign SAML assertions.

10. On the **Outbound Provisioning** tab, configure the provisioning target and channel. Click **Next**.

    See [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

    1. Click **Configure Provisioning**.

    2. On the **Target** tab, complete the fields as follows.

       | Field          | Description                                                                                                                                       |
       | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
       | **Webex ID**   | Your Webex administrator username.                                                                                                                |
       | **Password**   | Your Webex administrator password.                                                                                                                |
       | **Site name**  | The subdomain of the **Site Brand Name(s)** listed on your Webex administration **Site Information** tab, such as *example* in example.webex.com. |
       | **Site ID**    | **Optional**:The **Site ID** listed on your Webex administration **Site Information** tab.                                                        |
       | **Partner ID** | **Optional**:The **Partner ID** listed on your Webex administration **Site Information** tab.                                                     |

       |   |                                                                                        |
       | - | -------------------------------------------------------------------------------------- |
       |   | PingFederate verifies the credentials when you activate the channel and SP connection. |

    3. Customize the provisioning connector actions. Click **Next**.

       See [Provisioning options](pf_webex_connector_provisioning_options.html).

    4. On the **Manage Channels** tab, create a channel. Click **Done**.

    See [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation.

11. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: Configuring single sign-on in Webex
description: Use the following minimum required settings to configure single sign-on (SSO) for Webex.
component: webex
page_id: webex:setup:pf_webex_connector_configuring_single_sign_on_in_webex
canonical_url: https://docs.pingidentity.com/integrations/webex/setup/pf_webex_connector_configuring_single_sign_on_in_webex.html
llms_txt: https://docs.pingidentity.com/integrations/webex/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring single sign-on in Webex

Use the following minimum required settings to configure single sign-on (SSO) for Webex.

## About this task

For more information on how to setup SSO for Webex, see [Configure Single Sign-On for Cisco Webex Site](https://help.webex.com/docs/DOC-1067) on the Webex site.

|   |                                                                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can customize your Webex configuration beyond the basics described here. However, the SP connection created by the connector template does not support the Webex Account Creation/Update options. These SAML assertion-based provisioning options conflict with the connector's outbound provisioning methodology. |

## Steps

1. Download your PingFederate SAML metadata file.

   For more information, see [Metadata export](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_metadata_export.html) in the PingFederate documentation.

2. Sign on to your Webex administrator site.

3. In the upper-right corner, click your account, and then click **Webex Administration.**

4. Go to **Configuration > Common Site Settings > SSO Configuration** and in the **Federation Protocol** list, select **SAML 2.0**.

5. Click **Import SAML Metadata**, select the PingFederate metadata file that you downloaded, and then click **Open**.

   |   |                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------- |
   |   | If you receive a message asking whether you want to overwrite an existing certificate, click **Yes**. |

6. Configure the fields based on the following table.

   |   |                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | At a minimum, you must change the Webex default AuthnContextClassRef value, as specified in the table. This setting is not contained in the SAML metadata. |

   | Field                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **SSO Profile**                    | If you want to enable both identity provider (IdP)- and service provider (SP)-initiated SSO, select **SP Initiated**.&#xA;&#xA;Use this if you only want pre-authenticated users to be able to access Webex directly through another site, such as a company portal.If you want to enable only IdP-initiated SSO, select **IdP Initiated**.&#xA;&#xA;Use this if you want the SP-initiated behavior and also want users to be able to authenticate by clicking a link in Webex. |
   | **Webex SAML Issuer (SP ID)**      | If you are configuring a second (or greater) Webex Site for SSO, change this ID to match the Connection ID defined for the corresponding PingFederate SP connection.The default value is http\://www\.webex.com.                                                                                                                                                                                                                                                                |
   | **Issuer for SAML (IdP ID)**       | The Entity ID for SAML 2.0 at your site, as shown on the PingFederate administrative console **Federation Info** tab.                                                                                                                                                                                                                                                                                                                                                           |
   | **Customer SSO Service Login URL** | Your site's PingFederate SAML 2.0 endpoint in the format:`https://<pf_host>:<pf_port>/idp/SSO.saml2`                                                                                                                                                                                                                                                                                                                                                                            |
   | **AuthnContextClassRef**           | * If you customized the SAML\_AUTHN\_CTX value in [Configuring provisioning and single sign-on](pf_webex_connector_configuring_provisioning_and_single_sign_on.html), enter your custom value in this field.

   * Otherwise, enter the following: `urn:oasis:names:tc:SAML:2.0:ac:classes:Password`                                                                                                                                                                               |
   | **Default Webex Target page URL**  | The fully-qualified URL for your Webex site. For example, https\://subdomain.webex.com.                                                                                                                                                                                                                                                                                                                                                                                         |

7. **Optional:** If you selected **SP Initiated SSO**, select **AuthnRequest Signed**.

8. **Optional:** In the **Destination URL** field, paste the value from the **Customer SSO Service Login URL** field.

9. Click **Update**.

---

---
title: Deploy the provisioning connector
description: Download the integration .zip archive from the Add-ons tab of the PingFederate downloads page or the Ping Identity Marketplace.
component: webex
page_id: webex:setup:pf_webex_connector_deploy_the_provisioning_connector
canonical_url: https://docs.pingidentity.com/integrations/webex/setup/pf_webex_connector_deploy_the_provisioning_connector.html
llms_txt: https://docs.pingidentity.com/integrations/webex/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Deploy the provisioning connector

## Steps

1. Download the integration `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/webex-sso-integration).

2. Stop PingFederate.

3. Delete any existing Webex Connector files in the PingFederate directory:

   1. In the `<pf_install>/pingfederate/server/default/deploy` directory, delete the following files:

      * `pf-webex-quickconnection-<version>.jar`

      * `webex-api-4.8.1.jar`

4. Deploy the provisioning connector:

   1. Extract the Webex Connector distribution file, and then go to the `dist` folder.

   2. Copy the `pf-webex-quickconnection-<version>.jar` file to the `<pf_install>` `/pingfederate/server/default/deploy` directory.

5. Enable the PingFederate provisioning engine:

   1. In the `<pf_install>/pingfederate/bin` direcotry, open the `run.properties` file for editing.

   2. Change `pf.provisioner.mode` to `STANDALONE`. Save the file.

      |   |                                                                                                                                                                                                                                          |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | To configure the `FAILOVER` mode instead, see [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html) in the PingFederate *Server Clustering Guide*. |

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 1-5 for each instance of PingFederate.

---

---
title: Download manifest
description: The distribution archive contains the following files.
component: webex
page_id: webex:release_notes:pf_webex_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/webex/release_notes/pf_webex_connector_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/webex/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Download manifest

The distribution archive contains the following files.

* `ReadMeFirst.pdf` – contains a link to the [Ping Identity Support Home](https://support.pingidentity.com/s/).

* `/legal`:

  * `Legal.pdf` – copyright and license information.

* `/dist` – contains libraries needed for the provisioning connector:

  * `pf-webex-quickconnection-<version>.jar` – Webex Connector

---

---
title: Downloading your Webex SAML metadata file
description: You can use a Webex SAML metadata file to automatically configure some of your PingFederate connection settings.
component: webex
page_id: webex:setup:pf_webex_connector_downloading_your_webex_saml_metadata_file
canonical_url: https://docs.pingidentity.com/integrations/webex/setup/pf_webex_connector_downloading_your_webex_saml_metadata_file.html
llms_txt: https://docs.pingidentity.com/integrations/webex/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Downloading your Webex SAML metadata file

## About this task

You can use a Webex SAML metadata file to automatically configure some of your PingFederate connection settings.

To download SAML 2.0 Metadata for Webex:

## Steps

1. Sign on to your Webex administrator site.

2. In the upper-right corner, click your account, and then click **Webex Administration.**

3. Go to **Configuration > Common Site Settings > SSO Configuration** and in the **Federation Protocol** list, select **SAML 2.0**.

4. Click **Export**, and then save the `saml-metadata.xml` file.

5. Leave the **SSO Configuration** tab empty for now.

---

---
title: Known issues and limitations
description: The following are known issues and limitations of the Webex Connector integration.
component: webex
page_id: webex:release_notes:pf_webex_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/webex/release_notes/pf_webex_connector_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/webex/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues and limitations of the Webex Connector integration.

## Known issues

There are no known issues.

## Known limitations

* Updates made to users that are disabled in WebEx will not be visible in WebEx until they are reenabled.

* Because of a limitation with PingFederate 8.1 and earlier versions, when configuring two service provider (SP) connections with the same provisioner, the second connection built might be pre-populated with the channel from the first connection. To avoid conflicts, delete this pre-populated channel and create a unique channel for each connection.

* User attributes cannot be cleared when set.

* When an LDAP user is deleted in a targeted group distinguished name (DN), the provisioning connector does not propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled.

  For solutions, see [SaaS provisioner does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Knowledge Base.

* The Webex API does not allow a user to be created in a disabled state. Webex activates all users after creation.

* The connector cannot re-enable user meeting types that have been disabled through the Webex administration console. If the connector tries to update the user's meeting types in this scenario, it can cause all meeting types for that user to be disabled.

---

---
title: Provisioning options
description: User Create
component: webex
page_id: webex:setup:pf_webex_connector_provisioning_options
canonical_url: https://docs.pingidentity.com/integrations/webex/setup/pf_webex_connector_provisioning_options.html
llms_txt: https://docs.pingidentity.com/integrations/webex/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Provisioning options

| Option                                                                                                                                                        | Description                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **User Create**                                                                                                                                               | * Selected (default) — PingFederate creates users in Webex.

* Cleared — PingFederate does not create users in Webex.                   |
| **User Update**                                                                                                                                               | - Selected (default) – PingFederate updates existing users in Webex.

- Cleared – PingFederate does not update existing users in Webex. |
| **User Disable**                                                                                                                                              | * Selected (default) – PingFederate disables users in Webex.

* Cleared – PingFederate does not disable users in Webex.                 |
| &#xA;&#xA;If any of the above options are cleared, PingFederate logs a warning in the user workflow section of provisioner.log when the related action fails. |                                                                                                                                         |

---

---
title: Supported attributes reference
description: The following table lists the attributes that can be mapped for user provisioning.
component: webex
page_id: webex:setup:pf_webex_connector_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/webex/setup/pf_webex_connector_supported_attributes_reference.html
llms_txt: https://docs.pingidentity.com/integrations/webex/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Supported attributes reference

The following table lists the attributes that can be mapped for user provisioning.

|   |                                                                                               |
| - | --------------------------------------------------------------------------------------------- |
|   | Make sure you send all user attributes that are required by your Webex account configuration. |

| Attribute      | Description                                                                                                                                                                                                                                                                                                                      |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Email`        | The user's email address. Must be a valid email address.                                                                                                                                                                                                                                                                         |
| `Webex ID`     | A reference to the Webex user account.                                                                                                                                                                                                                                                                                           |
| `First Name`   | The user's first name.                                                                                                                                                                                                                                                                                                           |
| `Last Name`    | The user's last name.                                                                                                                                                                                                                                                                                                            |
| `Password`     | The user's password. A user password is validated against the password security options configured in the Webex Site Administration tool. If any of the security rules are violated, an exception occurs.                                                                                                                        |
| `Address 1`    | The first line of the user's street address.                                                                                                                                                                                                                                                                                     |
| `Address 2`    | The second line of the user's street address.                                                                                                                                                                                                                                                                                    |
| `City`         | The user's city.                                                                                                                                                                                                                                                                                                                 |
| `Company`      | The user's company name.                                                                                                                                                                                                                                                                                                         |
| `Country`      | The user's country. Must be a valid Country name. See [Elements in WebEx XML Schema Definitions for the User Service](https://developer.cisco.com/docs/webex-xml-api-reference-guide/?origin_team=T02JF3TTN#!elements-in-webex-xml-schema-definitions-for-the-user-service) in the Webex Meeting XML API Reference Guide.        |
| `Fax`          | The user's fax number.                                                                                                                                                                                                                                                                                                           |
| `Language`     | The user's preferred language. Must be a valid language. See [Elements in WebEx XML Schema Definitions for the User Service](https://developer.cisco.com/docs/webex-xml-api-reference-guide/?origin_team=T02JF3TTN#!elements-in-webex-xml-schema-definitions-for-the-user-service) in the Webex Meeting XML API Reference Guide. |
| `Meeting Type` | The user's meeting type IDs.                                                                                                                                                                                                                                                                                                     |
| `Mobile Phone` | The user's mobile phone number.                                                                                                                                                                                                                                                                                                  |
| `Pager`        | The user's pager number.                                                                                                                                                                                                                                                                                                         |
| `Phone`        | The user's phone number.                                                                                                                                                                                                                                                                                                         |
| `Pin`          | The user's PIN number. Secondary level of authentication for PCN and when host is using the phone and inviting additional attendees. Single number values and simple sequences, like 1111 or 1234, are not allowed.                                                                                                              |
| `State`        | The user's state.                                                                                                                                                                                                                                                                                                                |
| `Timezone`     | The user's time zone. Must be a valid timezone. See [Elements in WebEx XML Schema Definitions for the User Service](https://developer.cisco.com/docs/webex-xml-api-reference-guide/?origin_team=T02JF3TTN#!elements-in-webex-xml-schema-definitions-for-the-user-service) in the Webex Meeting XML API Reference Guide.          |
| `Title`        | The user's title.                                                                                                                                                                                                                                                                                                                |
| `Zip Code`     | The user's zip code (postal code).                                                                                                                                                                                                                                                                                               |

---

---
title: Upgrade an existing connector
description: If you're upgrading from a previous version of the Webex Connector, copy your current configuration to a new connection.
component: webex
page_id: webex:setup:pf_webex_connector_upgrade_an_existing_connector
canonical_url: https://docs.pingidentity.com/integrations/webex/setup/pf_webex_connector_upgrade_an_existing_connector.html
llms_txt: https://docs.pingidentity.com/integrations/webex/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Upgrade an existing connector

## About this task

If you're upgrading from a previous version of the Webex Connector, copy your current configuration to a new connection.

## Steps

1. Note the attribute mapping configuration from your existing Webex provisioning connection:

   1. On the PingFederate administrator console, on the **Identity Provider** tab, in the **SP Connections** section, click the name of your existing provisioning connection.

   2. On the **Outbound Provisioning** tab, click **Configure Provisioning**.

   3. On the **Manage Channels** tab, click your existing channel configuration.

   4. On the **Attribute Mapping** tab, note your existing attribute mappings.

2. Disable and delete your existing provisioning connection:

   1. On the **Identity Provider** tab, in the **SP Connections** area, click **Manage All**.

   2. For your existing provisioning connection, disable the connection.

   3. Click **Select Action**, and then click **Delete**.

   4. Click **Save**.

3. Complete the steps in [Deploy the provisioning connector](pf_webex_connector_deploy_the_provisioning_connector.html).

4. Complete the steps in [Configuring provisioning and single sign-on](pf_webex_connector_configuring_provisioning_and_single_sign_on.html) to configure a new SP connection.

5. Go to **Outbound Provisioning > Manage Channels > Attribute Mapping** and configure the attribute mappings based on the information you noted in step 1.

---

---
title: User management
description: The Webex Connector synchronizes users from your datastore to Webex. The following describes the behavior of each provisioning capability.
component: webex
page_id: webex::pf_webex_connector_user_management
canonical_url: https://docs.pingidentity.com/integrations/webex/pf_webex_connector_user_management.html
llms_txt: https://docs.pingidentity.com/integrations/webex/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  synchronizing-existing-users: Synchronizing existing users
  user-provisioning: User provisioning
  user-updates: User updates
  user-deprovisioning: User deprovisioning
---

# User management

The Webex Connector synchronizes users from your datastore to Webex. The following describes the behavior of each provisioning capability.

|   |                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can configure the following capabilities and specify which users to provision when you get to the [Configuring provisioning and single sign-on](setup/pf_webex_connector_configuring_provisioning_and_single_sign_on.html) part of the setup process. |

## Synchronizing existing users

PingFederate synchronizes users based on the `email` attribute in Webex. If a user already exists in your datastore and Webex, mapping this attribute correctly links the two records together.

For example:

* In Webex, Janet's `email` is `jsmith@example.com`.

* In your datastore, Janet's `mail` is `jsmith@example.com`.

* On the **Attribute Mapping** tab of your provisioning connection configuration, map the `email` attribute to `mail`.

* When the provisioning connector runs, the datastore user is provisioned with a `email` of `jsmith@example.com`. That matches Janet's existing `email` in Webex, so her information in the datastore is synchronized to her Webex account.

## User provisioning

PingFederate provisions users when any of the following happens:

* A user is added to the datastore group or filter that is targeted by the provisioning connector.

* A user with `disabled` status is added to the datastore group or filter that is targeted by the provisioning connector, and the**Provision disabled users** provisioning option is enabled. This feature is not available in all provisioning connectors.

|   |                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can define which users PingFederate targets for provisioning on the **Source Location** tab of your provisioning connection configuration. |

## User updates

PingFederate updates users when a user attribute changes in your datastore.

|   |                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can define which attributes PingFederate monitors for changes on the **Attribute Mapping** tab of your provisioning connection configuration. |

## User deprovisioning

PingFederate deprovisions users when any of the following happens:

* A user is deleted from the user store.

* A user is disabled in the user store.

* A user is removed from the datastore group or filter that is targeted by the provisioning connector.

---

---
title: Webex Provisioner
description: The Webex Provisioner allows PingFederate to integrate with Webex for provisioning and single sign-on (SSO).
component: webex
page_id: webex::pf_webex_connector
canonical_url: https://docs.pingidentity.com/integrations/webex/pf_webex_connector.html
llms_txt: https://docs.pingidentity.com/integrations/webex/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  provisioning-connector: Provisioning connector
  sso-support: SSO support
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Webex Provisioner

The Webex Provisioner allows PingFederate to integrate with Webex for provisioning and single sign-on (SSO).

The distribution file includes a quick connection template to help you get started.

## Provisioning connector

Allows PingFederate to manage users in Webex based on changes in an external user datastore.

You can enable the create, update, and delete capabilities independently.

## SSO support

Allows you to create a connection between PingFederate and Webex to support browser-based, IdP- and SP-initiated SSO.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following resources:

* The following sections of the PingFederate documentation:

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html)

  * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

  * [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

  * [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

## System requirements

* PingFederate 8.x or later.

* To allow PingFederate to make outbound connections to Webex, you might need to whitelist the following endpoints in your firewall:

  * https\://*\<subdomain>*.webex.com