---
title: Configuring SAML SSO with Box and PingFederate
description: Learn how to configure SAML SSO with Box and PingFederate.
component: configuration_guides
page_id: configuration_guides:box:config_saml_box_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/box/config_saml_box_pf.html
revdate: May 16, 2024
section_ids:
  about-this-task: About this task
  create-a-pingfederate-sp-connection-for-box: Create a PingFederate SP connection for Box
  configure-the-pingfederate-idp-connection-for-box: Configure the PingFederate IdP connection for Box
---

# Configuring SAML SSO with Box and PingFederate

Learn how to configure SAML SSO with Box and PingFederate.

## About this task

The following table details the required and optional attributes to be configured in the assertion attribute contract.

| Attribute Name | Description | Required / Optional |
| -------------- | ----------- | ------------------- |
| `SAML_SUBJECT` | Email       | Required            |
| `givenName`    | First Name  | Optional            |
| `sn`           | Last Name   | Optional            |
| `memberOf`     | Groups      | Optional            |

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | The following configuration is untested and is provided as an example. Additional steps might be required. |

## Create a PingFederate SP connection for Box

1. Download the Box metadata from <https://cloud.app.box.com/s/9y0zm1sqgvkxe8ha2qa3dfhwoivpoyy4>.

2. Sign on to the PingFederate administrative console.

3. Using the metadata that you downloaded, create an SP connection in PingFederate:

   1. Configure using **Browser SSO profile SAML 2.0**.

   2. Enable the following **SAML Profiles**:

      * **IdP-Initiated SO**

      * **SP-Initiated SSO**

      * **IdP-Initiated SLO**

      * **SP-Initiated SLO**

   3. In **Assertion Creation: Attribute Contract**, set the **Subject Name Format** to **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

   4. Extend the contract with the following attributes:

      * **givenName**

      * **memberOf**

      * **Sn**

   5. In the **Assertion Creation: Attribute Contract Fulfillment** section:

      * Map the attribute **SAML\_SUBJECT** to the attribute **mail**.

      * Map the optional attribute **givenName** to the attribute for the user's first name.

      * Map the optional attribute **memberOf** to the attribute for the user's Box roles.

      * Map the optional attribute **Sn** to the attribute for the user's surname or family name.

   6. In **Protocol Settings**:

      * In **Assertion Consumer Service URL**, delete **Artifact** and **PAOS Bindings**.

      * In **SLO Service URLs**, delete **Artifact** and **SOAP** bindings.

      * In **Allowable SAML Bindings**, enable **Redirect** and **POST**.

4. Export the metadata for the newly-created SP connection.

5. Export the signing certificate public key.

   ![Screen capture of PingFederate SP Connections page.](_images/omb1625087491743.png)

## Configure the PingFederate IdP connection for Box

1. Sign on to the Box Admin Console as an administrator.

   ![Screen capture of the Box Admin Console with the Settings icon on the lefthand sidebar highlighted in red.](_images/tfw1625087801073.png)

2. Click **Enterprise Settings**.

3. Click the **User Settings** tab.

4. In the **Configure Single Sign On (SSO) for All Users** section, click **Configure**.

   ![Screen capture of the Box User Settings tab highlighted in red and the Configure button for Configure Single Sign On (SSO) for All Users highlighted in red.](_images/hpv1625087938902.png)

5. Click **'I don't see my provider, or don't have a metadata file.'**

6. Complete the **Box SSO Setup Support Form**:

   1. Review the request form and the **For faster service please read** section.

   2. Complete the required fields:

      * For **Who is your Identity Provider?**, select **Other with Metadata**.

      * For **What is the attribute for the user's email?**, select **SAML\_SUBJECT**.

      * For **What is the attribute for groups?**, select **memberOf**.

      * For **What is the attribute for the user's first name?**, select **givenName**.

      * For **What is the attribute for the user's last name?**, select **Sn**.

      * Attach the metadata that you downloaded from the PingFederate configuration.

7. Click **Submit**.

   ![Screen capture of the Box SSO Setup Support Form.](_images/kdp1625088309558.png)

8. After the Box support team completes the configuration, follow any provided instructions and test the integration.
