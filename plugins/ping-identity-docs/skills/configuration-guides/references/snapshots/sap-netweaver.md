---
title: Configuring SAML SSO with SAP Netweaver and PingFederate
description: Learn how to configure SAML SSO with SAP Netweaver and PingFederate.
component: configuration_guides
page_id: configuration_guides:sap_netweaver:config_saml_sapnetweaver_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/sap_netweaver/config_saml_sapnetweaver_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  create-a-pingfederate-sp-connection-for-sap-netweaver: Create a PingFederate SP connection for SAP Netweaver
  configure-the-pingfederate-idp-connection-for-sap-netweaver: Configure the PingFederate IdP connection for SAP Netweaver
---

# Configuring SAML SSO with SAP Netweaver and PingFederate

Learn how to configure SAML SSO with SAP Netweaver and PingFederate.

## Before you begin

Refer to the vendor documentation and complete the following:

1. Ensure that HTTPS is enabled for your SAP system.

2. Activate Secure Session Management.

3. Enable SAML 2.0 support:

   1. Create a local provider.

   2. Export metadata for local provider.

## About this task

The following table details the required and optional attributes to be configured in the assertion attribute contract.

| Attribute Name    | Description | Required / Optional |
| ----------------- | ----------- | ------------------- |
| **SAML\_SUBJECT** | Username    | Required            |

## Create a PingFederate SP connection for SAP Netweaver

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | The following configuration is untested and is provided as an example. Additional steps might be required. |

1. Sign on to the PingFederate administrative console.

2. Using the details retrieved from SAP Netweaver:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Enable the following **SAML Profiles**:

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   3. In **Assertion Creation: Attribute Contract**, set the Subject Name Format to **urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified**.

   4. In **Assertion Creation: Attribute Contract Fulfilment**, map the attribute **SAML\_SUBJECT** to the attribute **username**.

      This should match the username for the user in SAP Netweaver.

   5. In **Protocol Settings: Allowable SAML Bindings**, enable **Post** and **Redirect**.

3. Export the metadata for the newly-created SP connection.

4. Export the signing certificate public key.

## Configure the PingFederate IdP connection for SAP Netweaver

1. Sign on to SAP Netweaver as an administrator.

2. Go to **Trusted Partners** and select **Identity Providers**.

3. Click **Add**.

4. Click **Upload Metadata File**, select the file that you downloaded from PingFederate, and click **Next**.

5. On the **Provider Name** page, verify the data populated. Click **Next**.

6. On the **Signature and Encryption** page, verify the data populated. Click **Next**.

7. On the **Single Sign-On Endpoints** page, verify the data populated. Click **Next**.

8. On the **Single Logout Endpoints** screen, verify the data populated. Click **Next**.

9. Select **Binding** as **HTTP POST**. Click **Finish**.

10. Enable the provider.

11. Configuration is completed.

After testing, you can enable SP-initiated SSO for SAP Netweaver by editing the configuration in `sap/opu/odata/iwfnd/catalogservice`.

---

---
title: Configuring SAML SSO with SAP Netweaver and PingOne for Enterprise
description: Learn how to configure SAML SSO with SAP Netweaver and PingOne for Enterprise.
component: configuration_guides
page_id: configuration_guides:sap_netweaver:config_saml_sapnetweaver_p14e
canonical_url: https://docs.pingidentity.com/configuration_guides/sap_netweaver/config_saml_sapnetweaver_p14e.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  create-a-pingone-for-enterprise-application-for-sap-netweaver: Create a PingOne for Enterprise application for SAP Netweaver
  configure-the-pingone-for-enterprise-idp-connection-for-sap-netweaver: Configure the PingOne for Enterprise IdP connection for SAP Netweaver
---

# Configuring SAML SSO with SAP Netweaver and PingOne for Enterprise

Learn how to configure SAML SSO with SAP Netweaver and PingOne for Enterprise.

## Before you begin

Refer to the vendor documentation and complete the following:

1. Ensure that HTTPS is enabled for your SAP system.

2. Activate Secure Session Management.

3. Enable SAML 2.0 support:

   1. Create a local provider.

   2. Export metadata for local provider.

## About this task

The following table details the required and optional attributes to be configured in the assertion attribute contract.

| Attribute Name    | Description | Required / Optional |
| ----------------- | ----------- | ------------------- |
| **SAML\_SUBJECT** | Username    | Required            |

## Create a PingOne for Enterprise application for SAP Netweaver

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | The following configuration is untested and is provided as an example. Additional steps might be required. |

1. Sign on to PingOne for Enterprise and click **Applications**.

2. On the **SAML** tab, click **Add Application**.

   ![Screen capture of PingOne for Enterprise SAML Application tab with the Add Application dropdown menu opened and New SAML Application highlighted in red.](_images/axb1622052381893.png)

3. Enter the following:

   * A suitable **Application Name**, such as `SAP Netweaver`.

   * A suitable **Application Description**.

   * A suitable **Category**, such as `Information Technology`.

   * (Optional) Upload an icon to be used in the PingOne for Enterprise dock.

   ![Screen capture of the PingOne for Enterprise Application details page with SAP Netweaver entered as the Application Name and Application Description.](_images/arw1622052553105.png)

4. Click **Continue to Next Step**.

5. Select **I have the SAML configuration**.

6. In the **Signing Certificate list**, select a suitable signing certificate.

7. For **Protocol Version**, click **SAML v.2.0**.

   ![Screen capture of PingOne for Enterprise SAML Application Settings with a signing certificate selected in the Signing Certificate dropdown menu and SAML v.2.0 selected as the Protocol Version.](_images/wps1622052704168.png)

8. Upload the metadata from your SAP Netweaver local provider configuration.

9. Click **Continue to Next Step**.

10. In the **SSO Attribute Mapping** section, add the following mapping for the **SAML\_SUBJECT**:

    * For **Identity Bridge Attribute or Literal Value**, select the appropriate attribute. This should match the username for the user in SAP Netweaver.

    * Select the **Required** check box.

    ![Screen capture of PingOne for Enterprise SSO Attribute Mapping section with SAML\_SUBJECT entered as both the Application Attribute and the Identity Bridge Attribute or Literal Value and the Required box checked.](_images/ivd1622052909642.png)

11. Click **Continue to Next Step**.

12. Add the user groups for the application.

    ![Screen capture of PingOne for Enterprise Group Access section with Domain Administrators@directory and Users@directory listed in the Group Name column.](_images/rue1622053045315.png)

13. Click **Continue to Next Step**.

14. Review the settings.

    ![Screen capture of PingOne for Enterprise Review Setup section to test the connection to SAP Netweaver.](_images/pcp1622053155280.png)

15. Copy the **Single Sign-On (SSO) URL** value to a temporary location.

    This is the IdP-initiated SSO URL that you can use for testing.

16. Note the **idpid** and **Issuer** values.

17. On the **Signing Certificate** line, click **Download**.

    You'll use this for the application configuration.

18. On the **SAML Metadata** line, click **Download**.

    You'll use this for the application configuration.

19. Click **Finish**.

## Configure the PingOne for Enterprise IdP connection for SAP Netweaver

1. Sign on to SAP Netweaver as an administrator.

2. Go to **Trusted Partners** and select **Identity Providers**.

3. Click **Add**.

4. Click **Upload Metdata File**, select the file that you downloaded from PingOne for Enterprise, and click **Next**.

5. On the **Provider Name** page, verify the data populated. Click **Next**.

6. On the **Signature and Encryption** page, verify the data populated. Click **Next**.

7. On the **Single Sign-On Enpoints** page, verify the data populated. Click **Next**.

8. On the **Single Logout Endpoints** page, verify the data populated. Click **Next**.

9. Select **Binding** as **HTTP POST**. Click **Finish**.

10. Enable the provider.

After testing, you can enable SP-initiated SSO for SAP Netweaver by editing the configuration in `sap/opu/odata/iwfnd/catalogservice`.