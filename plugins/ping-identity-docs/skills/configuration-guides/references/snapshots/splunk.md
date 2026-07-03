---
title: Configuring SAML SSO with Splunk Cloud and PingFederate
description: Learn how to configure SAML SSO with Splunk Cloud and PingFederate.
component: configuration_guides
page_id: configuration_guides:splunk:config_saml_splunk_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/splunk/config_saml_splunk_pf.html
revdate: May 15, 2024
section_ids:
  about-this-task: About this task
  create-a-pingfederate-sp-connection-for-splunk-cloud: Create a PingFederate SP connection for Splunk Cloud
  configure-the-pingfederate-idp-connection-for-splunk-cloud: Configure the PingFederate IdP-connection for Splunk Cloud
---

# Configuring SAML SSO with Splunk Cloud and PingFederate

Learn how to configure SAML SSO with Splunk Cloud and PingFederate.

## About this task

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | An error in configuration could cause users and administrators to be unable to sign on to Splunk Cloud.The following **Direct Login** link can be used for local authentication:`https://tenant.splunkcloud.com/en-US/account/login?loginType=splunk`. |

The following table details the required and optional attributes to be configured in the assertion attribute contract.

| Attribute Name | Description                                                                                         | Required / Optional |
| -------------- | --------------------------------------------------------------------------------------------------- | ------------------- |
| `SAML_SUBJECT` |                                                                                                     | Required            |
| `Role`         | User role as per SAML Groups. Attribute name is configurable in SAML configuration for application. | Required            |
| `Email`        | User Email address. Attribute name is configurable in SAML configuration for application.           | Optional            |
| `RealName`     | User display name. Attribute name is configurable in SAML configuration for application.            | Optional            |

The following table details the references that are used within this guide that are environment-specific. Replace these with the suitable value for your environment.

| Reference | Description                                    |
| --------- | ---------------------------------------------- |
| `tenant`  | The instance name for the Splunk Cloud tenant. |

|   |                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------- |
|   | The following configuration is untested, and is provided as an example. Additional steps might be required. |

## Create a PingFederate SP connection for Splunk Cloud

1. Download the Splunk Cloud metadata from `https://tenant.splunkcloud.com/en-US/saml/spmetadata`.

2. Sign on to the PingFederate administrative console.

3. Using the metadata that you downloaded, create an SP connection in PingFederate:

   1. Configure using **Browser SSO profile SAML 2.0**.

   2. Enable the following **SAML Profiles**:

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

      * **IdP-Initiated SLO**

      * **SP-Initiated SLO**

   3. In **Assertion Creation: Attribute Contract**, set the **Subject Name Format** to **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

   4. Extend the contract:

      * **Attribute**: `Role`

      * **Format**: `urn:oasis:names:tc:SAML:2.0:attrname-format-basic`

   5. In the **Assertion Creation: Attribute Contract Fulfilment**, map attribute **SAML\_SUBJECT** to the attribute **mail** and map attribute **Role** to the LDAP attribute containing the Splunk role.

   6. In **Protocol Settings: Allowable SAML Bindings**, enable **Redirect** and **POST**.

4. Export the metadata for the newly-created SP connection.

5. Export the signing certificate public key.

   ![Screen capture illustrating the completed PingFederate SP connection for Splunk Cloud.](_images/wmf1621282668902.png)

## Configure the PingFederate IdP-connection for Splunk Cloud

1. Sign on to Splunk Cloud as an administrator.

2. In the top navigation bar, click **Settings**.

3. Click **Authentication Methods**.

   ![Screen capture illustrating the menu navigation bar in Splunk Cloud, with the Authentication Methods section highlighted in red.](_images/ixd1621282803424.png)

4. Click **SAML**, and then click **Configure Splunk to use SAML**.

   ![Screen capture illustrating the Authentication Methods section of Splunk Cloud, with the option to Configure Splunk to use SAML highlighted in red.](_images/wjw1621283009168.png)

5. On the **SAML Configuration** window, note the warning and save the **Direct Login** URL so that you can use it in the event of integration errors.

6. In the **Metadata XML File** field, click **Select File**, and select the PingFederate metadata file that you exported.

   ![Screen capture illustrating the SAML Configuration warning message notifying users that an error in configuring SAML could result in users and admins being locked out of Splunk Cloud.](_images/oqx1621283170873.png)

7. Review the configuration loaded from the metadata.

8. Set the **Entity ID** to the one that you configured in PingFederate when creating the SP configuration, such as `splunkEntityId`.

9. Set the **Role** alias to the value that you configured in PingFederate for the attribute contract, such as `Role`.

10. Set the **Name ID Format** to **Email Address**.

    ![Screen capture of the SAML Configuration window in Splunk Cloud with the Entity ID field, the Role alias field, the Name Id Format field, and the Fully qualified domain name or IP of the load balancer field highlighted in red.](_images/hnj1621283569750.png)

11. Ensure the fully qualified domain name parameter and port parameter match that of your Splunk Cloud instance.

    For example:

    * **Fully Qualified Domain Name**: `https://tenant.splunkcloud.com`

    * **Port**: 443

12. Click **Save**.

13. Go to **Settings → Authentication Methods → SAML Settings**.

14. Click **New Group** and configure the following settings.

    | Setting  | Value                                                                                                                |
    | -------- | -------------------------------------------------------------------------------------------------------------------- |
    | **Name** | `samluser`&#xA;&#xA;This value should match the role you are passing from PingFederate in the SSO Attribute Mapping. |
    | **Role** | `user`                                                                                                               |

    ![Screen capture of the SAML Groups window in Splunk Cloud with the New Group button highlighted in red.](_images/wmu1621284056009.png)

15. Click **Save**.

16. Create additional groups as required to meet requirements.

    ![Screen capture illustrating the Create New SAML Group window with the Group Name field and the selected Splunk Role of user highlighted in red. The Save button is highlighted in red.](_images/ucz1621284253583.png)

The configuration is complete.
