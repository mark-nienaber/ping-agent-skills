---
title: Configuring SAML SSO with Tableau and PingFederate
description: Learn how to enable Tableau SSO in PingFederate (IdP and SP-initiated).
component: configuration_guides
page_id: configuration_guides:tableau:config_saml_tableau_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/tableau/config_saml_tableau_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  export-the-metadata-from-tableau: Export the metadata from Tableau
  create-a-tableau-sp-connection: Create a Tableau SP Connection
  import-the-metadata-in-tableau: Import the metadata in Tableau
  test-the-idp-initiated-sso-integration: Test the IdP-initiated SSO integration
  test-the-sp-initiated-sso-integration: Test the SP-initiated SSO integration
---

# Configuring SAML SSO with Tableau and PingFederate

Learn how to enable Tableau SSO in PingFederate (IdP and SP-initiated).

## Before you begin

* Configure PingFederate to authenticate against an identity repository containing the users requiring application access.

* An Email Attribute is required in the assertion, either the SAML Subject or another SAML attribute per the SAML configuration. The value of the Email Attribute must be a valid email address. This attribute is used to uniquely identify the user in the organization.

## Export the metadata from Tableau

1. Sign on to Tableau with an administration account.

2. Go to **Settings → Authentication**.

3. Select the **Enable an additional authentication method** check box.

4. Select the SAML authentication method.

5. Expand the **Edit Connection** section.

6. Click **Export Metadata**.

   ![Screen capture of Tableau Authentication types page.](_images/lrk1640220985403.png)

## Create a Tableau SP Connection

1. In PingFederate, create a service provider (SP) connection for Tableau.

2. Configure using **Browser SSO** profile **SAML 2.0**.

3. Upload the metadata file from Tableau.

4. Enable the following SAML profiles.

   * **IdP-Initiated SSO**

   * **SP-Initiated SSO**

5. Configure the assertion:

   * Select the source mappings.

   * Define the contract fulfillment.

     ![Screen capture of PingFederate mapping mathod and attribute contract fulfillment sections.](_images/ank1640221175322.png)

6. In **protocol settings: Allowable SAML Bindings**, enable **POST**.

7. Go to `https://PingFederate-url/pf/federation_metadata.ping?PartnerSpId=Tableau-EntityId` and download the metadata file from PingFederate.

## Import the metadata in Tableau

1. Upload the PingFederate metadata file and click **Apply**.

2. Confirm that the IdP entityID and SSO service URL are correct.

3. Test the connection.

4. Match the Tableau attributes to the assertion attributes and click **Apply**.

   ![Screen capture of Tableau Online Attribute page with Email and Display Name attributes shown.](_images/eej1640221622163.png)

## Test the IdP-initiated SSO integration

1. Go to the PingFederate SSO application endpoint for Tableau, `https://PingFederate-url/idp/startSSO.ping?PartnerSpId=Tableau-EntityId`.

   `https://127.0.0.1:9031/idp/startSSO.ping?PartnerSpId=https://sso.online.tableau.com/public/sp/metadata/5c142f94-8889-491a-816c-e61ae6dc84cb`

2. Authenticate with PingFederate.

   You're redirected to Tableau.

## Test the SP-initiated SSO integration

1. Go to the Tableau sign on page.

2. Enter the email address that will redirect to PingFederate.

3. Authenticate with PingFederate.

   You're redirected back to Tableau.

---

---
title: Configuring SAML SSO with Tableau and PingOne
description: Learn how to enable Tableau SSO in PingOne (IdP and SP-initiated).
component: configuration_guides
page_id: configuration_guides:tableau:config_saml_tableau_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/tableau/config_saml_tableau_p1.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  export-the-metadata-from-tableau: Export the metadata from Tableau
  create-the-tableau-sp-connection: Create the Tableau SP connection
  import-the-metadata-in-tableau: Import the metadata in Tableau
  test-the-idp-initiated-sso-integration: Test the IdP-initiated SSO integration
  test-the-sp-initiated-sso-integration: Test the SP-initiated SSO integration
---

# Configuring SAML SSO with Tableau and PingOne

Learn how to enable Tableau SSO in PingOne (IdP and SP-initiated).

## Before you begin

* Configure PingOne to authenticate against an identity repository containing the users requiring application access.

* An Email Attribute is required in the assertion, either the SAML Subject or another SAML attribute per the SAML configuration. The value of the Email Attribute must be a valid email address. This attribute is used to uniquely identify the user in the organization.

## Export the metadata from Tableau

1. Sign on to Tableau with an administration account.

2. Go to **Settings → Authentication**.

3. Select the **Enable an additional authentication method** check box.

4. Select the SAML authentication method.

5. Expand the **Edit Connection** section.

6. Click **Export Metadata**.

   ![Screen capture of Tableau Authentication types page.](_images/lrk1640220985403.png)

## Create the Tableau SP connection

1. In the PingOne admin portal, go to **Connections → Applications**.

2. Create an SP connection for Tableau by selecting **Add application**.

3. When you're prompted to select an application type, select **WEB APP** and then click **Configure** next to **SAML** for the chosen connection type.

4. Enter a unique name for the application.

5. Import the Tableau metadata.

6. Select the signing certificate.

7. Confirm that the **EntityID** and endpoints are correct.

8. Enter a suitable value for **Assertion Validity Duration (in seconds)**. A value of 300 seconds is typical.

9. Click **Save and Continue**.

10. Define the Tableau assertion requirements.

    ![Screen capture of Tableau application attribute mapping.](_images/pcc1640222397705.png)

11. Click the toggle to enable the application.

12. On the **Configuration** tab for the Tableau application, on the **Download Metadata** line, click **Download**.

    ![Screen capture of Tableau Configuration tab with download metadata button.](_images/cva1640222494748.png)

## Import the metadata in Tableau

1. Upload the PingOne metadata file and click **Apply**.

2. Confirm that the IdP, entityID, and SSO service URL are correct.

3. Test the connection.

4. Match the Tableau attributes to the assertion attributes and click **Apply**.

   ![Screen capture of Tableau Online Attribute page with Email and Display Name attributes shown.](_images/eej1640221622163.png)

## Test the IdP-initiated SSO integration

1. Go to the PingOne Application Portal and sign on with a user account.

   |   |                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------ |
   |   | In the Admin console, go to **Dashboard → Environment Properties** to find the **PingOne Application Portal URL**. |

2. Click the Tableau icon.

   You're redirected to the Tableau website and logged in with SSO.

## Test the SP-initiated SSO integration

1. Go to the Tableau sign on page and enter the email address that will redirect to PingOne.

2. In the PingOne sign-on prompt, enter your PingOne username and password.

   You're redirected back to Tableau and signed on with SSO.

---

---
title: Configuring SCIM 2.0 provisioning with Tableau and PingFederate
description: Learn how to enable Tableau SCIM 2.0 Provisioning in PingFederate.
component: configuration_guides
page_id: configuration_guides:tableau:config_scim_tableau_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/tableau/config_scim_tableau_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  enable-scim-provisioning-in-tableau: Enable SCIM provisioning in Tableau
  enable-scim-provisioning-in-the-sp-connection: Enable SCIM provisioning in the SP connection
---

# Configuring SCIM 2.0 provisioning with Tableau and PingFederate

Learn how to enable Tableau SCIM 2.0 Provisioning in PingFederate.

## Before you begin

* Configure PingFederate to authenticate against an LDAP identity repository containing the users requiring application access.

* Configure PingFederate with the SCIM provisioning connector to support the SCIM 2.0 protocol.

* Configure PingFederate with the Tableau SP connection.

* Configure the PingFederate `run.properties` file to support provisioning.

## Enable SCIM provisioning in Tableau

1. Sign on to Tableau with an administration account.

2. Go to **Settings → Authentication**.

3. In the **Automatic Provisioning and Group Synchronisation (SCIM)** section, select the **Enable SCIM** check box.

4. Click **Generate New Secret**.

   This will generate a new API secret that PingFederate will use to authenticate to the Tableau SCIM endpoint.

   ![Screen capture of Tableau automatic provisioning and group synchronization section to generate a new secret.](_images/bfo1640220001145.png)

## Enable SCIM provisioning in the SP connection

1. In the PingFederate administrative console, select the Tableau SP connector.

2. On the **Connection Type** tab, select the **Outbound Provisioning** check box and in the **Type** list, select **SCIM Connector**.

   ![Screen capture of PingFederate SP Connections page with SCIM Connector selected as the connection type with Outbound Provisioning and Browser SSO Profiles also selected.](_images/qqy1640220118360.png)

3. On the **Outbound Provisioning** tab, select **Configure Provisioning**.

4. On the **Target** tab, in the **SCIM Version** list, select 2.0 and enter the **SCIM URL** and **OAuth 2 Bearer Token** obtained from Tableau.

   ![Screen capture of PingFederate SP Connection channel configuration.](_images/vyd1640220262324.png)

5. Define a channel to obtain the user details:

   1. Add the LDAP source and source location according to your user data source.

      ![Screen capture of PingFederate SP Connection channel configuration with PingDirectory selected as the active LDAP data store.](_images/odq1640220402622.png)![Screen capture of PingFederate SP Connection channel data store source settings.](_images/ndo1640220471464.png)![Screen capture of PingFederate channel configuration with source location settings.](_images/zhj1640220552222.png)

   2. Configure attribute mappings.

      |   |                                                                                                                                                                                                      |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The SCIM **userName** field must map to an email address.+ image::ixz1640220648501.png\[alt="Screen capture of PingFederate SP Connection channel attribute mapping page.",role="border-no-padding"] |

   3. Enable the channel.