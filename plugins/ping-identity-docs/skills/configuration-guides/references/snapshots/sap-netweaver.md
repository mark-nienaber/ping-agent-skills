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
