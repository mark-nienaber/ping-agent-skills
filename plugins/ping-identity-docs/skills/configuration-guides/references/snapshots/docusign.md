---
title: Configuring SAML SSO using DocuSign and PingFederate
description: Learn how to enable DocuSign sign on from a PingFederate URL (IdP-initiated sign-on) and direct DocuSign sign on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:docusign:config_saml_docusign_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/docusign/config_saml_docusign_pf.html
revdate: May 16, 2024
section_ids:
  before-you-begin: Before you begin
  create-a-pingfederate-sp-connection-for-docusign: Create a PingFederate SP Connection for DocuSign
  add-the-pingfederate-connection-to-docusign: Add the PingFederate connection to DocuSign
  update-the-entityid-and-acs-url-values-in-pingfederate: Update the EntityID and ACS URL values in PingFederate
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO using DocuSign and PingFederate

Learn how to enable DocuSign sign on from a PingFederate URL (IdP-initiated sign-on) and direct DocuSign sign on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users requiring application access.

* Make sure DocuSign has a valid domain, an organisation created, and is populated with at least one user to test access.

* You must have administrative access to PingFederate and DocuSign.

## Create a PingFederate SP Connection for DocuSign

1. Sign on to PingFederate administration console.

2. Create an SP connection for DocuSign in PingFederate:

   * Configure using **Browser SSO** profile **SAML 2.0**.

   * Set **Partner's Entity ID** to `Placeholder`.

     You will update this value later.

   * Enable the following **SAML Profiles**:

     * **IdP-Initiated SSO**

     * **SP-Initiated SSO**

   * In **Assertion Creation: Attribute Contract**, extend the contract to add attributes named `SAML_NAME_FORMAT`, `surname`, `givenname` and `emailaddress`.

   * In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfillment**, map **SAML\_SUBJECT**, **surname**, **givenname** and **emailaddress** and map **SAML\_NAME\_FORMAT** to `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`.

   * In **Protocol Settings: Assertion Consumer Service URL**, set **binding** to **POST**, and set **Endpoint URL** to `http://placeholder`.

     You will update the placeholder value later.

   * In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

   * In **Credentials: Digital Signature Settings**, select the PingFederate signing certificate.

3. Save the configuration.

4. Export the signing certificate.

5. Export and then open the metadata file, and copy the value of these properties:

   * `entityID`

   * `Location entry` (`https://your value/idp/SSO.saml2`)

## Add the PingFederate connection to DocuSign

1. Sign on to your DocuSign domain as an administrator.

2. In the left navigation pane, select **Identity Providers**, and then click **Add Identity Provider**.

   ![Screen capture of the Docusign Admin portal open to the Identity Providers window with the Add Identity Provider button highlighted in red.](_images/njv1621287978925.png)

3. Configure the following fields.

   | Field                             | Value                                                                               |
   | --------------------------------- | ----------------------------------------------------------------------------------- |
   | **Name**                          | A name for the identity provider.                                                   |
   | **Identity Provider Issuer**      | Enter the **Issue** value from PingID.                                              |
   | **Identity Provider Login URL**   | `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=PingOne IdP ID value` |
   | **Send AuthN Request by**         | Click **POST**.                                                                     |
   | **Select Send Logout Request by** | Click **POST**.                                                                     |

   ![Screen capture of the Add Identity Provider fields for SSO Protocol: SAML 2.0. The Name, Identity Provider Issuer, and Identity Provider Login URL fields are required.](_images/psh1621288267240.png)

4. In the **Custom Attribute Mapping** section, click **Add New Mapping**, and then:

   * In the **Field** list, select **surname**, then enter `surname` in the **Attribute** field.

   * In the **Field** list, select **givenname**, then enter `givenname` in the **Attribute** field.

   * In the **Field** list, select **emailaddress**, then enter `emailaddress` in the **Attribute** field.

5. Click **Save**.

6. Click **Add New Certificate**.

   ![Screen capture of the PingOne identity provider with no current valid certificate. The Add New Certificate button is highlighted in red.](_images/ruf1621288498690.png)

7. Click **Add Certificate**.

   ![Screen capture of the Identity Provider Certificates field with the Add Certificate button highlighted in red.](_images/ogj1621288643739.png)

8. Select the signing certificate that downloaded from PingFederate. Click **Save**.

9. In the **Actions** list for the identity provider that you created, select **Endpoints**.

   ![Screen capture of the Identity Providers list with the PingOne identity provider Actions menu expanded. The Endpoints option is highlighted in red.](_images/pkv1621288741728.png)

10. Copy the **Service Provider Issuer URL** and **Service Provider Assertion Consumer Service URL** values.

    ![Screen capture of the Service Provider Issuer URL and Service Provider Assertion Consumer Service URL fields highlighted in red.](_images/cmz1621288870338.png)

    The DocuSign connection configuration is complete.

    |   |                                                                                                           |
    | - | --------------------------------------------------------------------------------------------------------- |
    |   | After testing, you can set the domain to require IP authentication to remove the DocuSign sign-on screen. |

## Update the EntityID and ACS URL values in PingFederate

1. Sign on to the PingFederate administrative console.

2. Edit the SP connection for DocuSign.

3. Set **Partner's Entity ID** to the DocuSign **Service Provider Issuer URL** value.

4. Set **Assertion Consumer Service URL Endpoint URL** to the **DocuSign Service Provider Assertion Consumer Service URL** value.

5. Save the changes.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO application endpoint for the DocuSign SP connection.

2. Complete PingFederate authentication.

   You're redirected to your DocuSign domain.

   ![Screen capture of the DocuSign domain.](_images/arw1621290347104.png)

## Test the PingFederate SP-initiated SSO integration

1. Go to <https://account.docusign.com>.

2. Enter your email address.

3. Click **Use Company Login**.

4. After you're redirected to PingFederate, enter your PingFederate username and password.

   After successful authentication, you're redirected back to DocuSign.

   ![Screen capture of the DocuSign domain.](_images/arw1621290347104.png)

---

---
title: Configuring SAML SSO with DocuSign and PingOne for Enterprise
description: Learn how to enable DocuSign sign on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct DocuSign sign on using PingOne for Enterprise (SP initiated sign on).
component: configuration_guides
page_id: configuration_guides:docusign:config_saml_docusign_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/docusign/config_saml_docusign_p1.html
revdate: May 20, 2024
section_ids:
  before-you-begin: Before you begin
  copy-pingone-values-for-the-supplied-docusign-application: Copy PingOne values for the Supplied DocuSign Application
  add-the-pingone-for-enterprise-idp-connection-to-docusign: Add the PingOne for Enterprise IdP Connection to DocuSign
  complete-the-docusign-setup-in-pingone-for-enterprise: Complete the DocuSign setup in PingOne for Enterprise
  test-the-pingone-for-enterprise-idp-initiated-sso-integration: Test the PingOne for Enterprise IdP-initiated SSO integration
  test-the-pingone-for-enterprise-sp-initiated-sso-integration: Test the PingOne for Enterprise SP-initiated SSO integration
---

# Configuring SAML SSO with DocuSign and PingOne for Enterprise

Learn how to enable DocuSign sign on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct DocuSign sign on using PingOne for Enterprise (SP initiated sign on).

## Before you begin

* Link PingOne for Enterprise to an identity repository containing the users requiring application access.

* Make sure DocuSign has a valid domain, an organization created, and is populated with at least one user to test access.

* You must have administrative access to PingOne for Enterprise and DocuSign.

## Copy PingOne values for the Supplied DocuSign Application

1. Sign on to PingOne for Enterprise, go to **Applications → Application Catalog**, and search for DocuSign.

   ![Screen capture of the Application Catalog in PingOne for Enterprisewith a completed search for DocuSign in the Search Field. In the list of applications, the DocuSign 2.0 Production application name's expand button is highlighted in red.](_images/pyx1621287515283.png)

2. Expand the **DocuSign 2.0 - Production** entry and click the **Setup** icon.

3. Copy the **Issuer** and **IdP ID** values.

4. Download the **Signing Certificate**.

   ![Screen capture of the SSO Instructions Signing Certificate field with the download button highlighted in red, and the IdP ID and Issuer configuration parameter fields higlighted in red.](_images/bki1621287826678.png)

## Add the PingOne for Enterprise IdP Connection to DocuSign

1. Sign on to your DocuSign Admin organization as an administrator.

2. In the left navigation pane, select **Identity Providers**, and then click **Add Identity Provider**.

   ![Screen capture of the DocuSign Admin portal open to the Identity Providers window with the Add Identity Provider button highlighted in red.](_images/njv1621287978925.png)

3. Configure the following fields

   | Field                             | Value                                                                                              |
   | --------------------------------- | -------------------------------------------------------------------------------------------------- |
   | **Name**                          | A name for the identity provider                                                                   |
   | **Identity Provider Issuer**      | The **Issue** value from PingID                                                                    |
   | **Identity Provider Login URL**   | `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=PingOne for Enterprise IdP ID value` |
   | **Send AuthN Request by**         | **POST**                                                                                           |
   | **Select Send Logout Request by** | **POST**                                                                                           |

   ![Screen capture of the Add Identity Provider fields for SSO Protocol: SAML 2.0.. The Name, Identity Provider Issuer, and Identity Provider Login URL fields are required.](_images/psh1621288267240.png)

4. In the **Custom Attribute Mapping** section, click **Add New Mapping**, and then:

   * In the **Field** list, select **surname**, then enter `surname` in the **Attribute** field.

   * In the **Field** list, select **givenname**, then enter `givenname` in the **Attribute** field.

   * In the Field list, select **emailaddress**, then enter `emailaddress` in the **Attribute** field.

5. Click **Save**.

6. Click **Add New Certificate**.

   ![Screen capture of the PingOne for Enterprise identity provider with no current valid certificate. The Add New Certificate button is highlighted in red.](_images/ruf1621288498690.png)

7. Click **Add Certificate**.

   ![Screen capture of the Identity Provider Certificates field with the Add Certificate button highlighted in red.](_images/ogj1621288643739.png)

8. Select the signing certificate that you downloaded from PingOne for Enterprise. Click **Save**.

9. In the **Actions** list for the IdP that you created, select **Endpoints**.

   ![Screen capture of the Identity Providers list with the PingOne for Enterprise identity provider Actions menu expanded. The Endpoints option is highlighted in red.](_images/pkv1621288741728.png)

10. Copy the **Service Provider Issuer URL** and**Service Provider Assertion Consumer Service URL** values.

    ![Screen capture of the Service Provider Issuer URL and Service Provider Assertion Consumer Service URL fields highlighted in red.](_images/cmz1621288870338.png)

    The DocuSign connection configuration is complete.

    |   |                                                                                                           |
    | - | --------------------------------------------------------------------------------------------------------- |
    |   | After testing, you can set the domain to require IP authentication to remove the DocuSign sign-on screen. |

## Complete the DocuSign setup in PingOne for Enterprise

1. Continue editing the DocuSign entry in PingOne for Enterprise.

   |   |                                                                                              |
   | - | -------------------------------------------------------------------------------------------- |
   |   | If the session has timed out, complete the initial steps to the point of clicking **Setup**. |

2. Click **Continue to Next Step**.

3. Set the **ACS URL** to the **DocuSign Service Provider Assertion Consumer Service URL** value.

4. Set the **Entity ID** to the **DocuSign Service Provider Issuer URL** value.

   ![Screen capture of the Connection Configuration section with the ACS URL and Entity ID fields filled in.](_images/zkm1621289831380.png)

   |   |                                         |
   | - | --------------------------------------- |
   |   | Do not just update the organization ID. |

5. Click **Continue to Next Step**.

6. Map the required attributes to the corresponding attribute names in your environment.

   |   |                                                                |
   | - | -------------------------------------------------------------- |
   |   | The corresponding attribute names might not be an exact match. |

   ![Screen capture of the Attribute Mapping section with the Identity Bridge Attribute or Literal Value fields highlighted in red for the SAML\_SUBJECT, emailaddress, givenname, and surname application attributes.](_images/eku1621289988318.png)

7. On the **SAML\_SUBJECT** line, click **Advanced**, and change the name format you're sending to DocuSign to `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`.

8. Click **Continue to Next Step** twice.

9. Click **Add** for all user groups that should have access to DocuSign.

   ![Screen capture of the Group Access section with the list of user groups that should have access to the Docusign application.](_images/gnm1621290134509.png)

10. Click **Continue to Next Step**.

11. Click **Finish**.

    PingOne for Enterprise configuration is complete.

## Test the PingOne for Enterprise IdP-initiated SSO integration

1. Go to your Ping desktop as a user with DocuSign access.

   |   |                                                                                               |
   | - | --------------------------------------------------------------------------------------------- |
   |   | To find the Ping desktop URL in the Admin console, go to **Setup → Dock → PingOne Dock URL**. |

2. Complete the PingOne for Enterprise authentication.

   You're redirected to your DocuSign domain.

   ![Screen capture of the DocuSign domain.](_images/arw1621290347104.png)

## Test the PingOne for Enterprise SP-initiated SSO integration

1. Go to <https://account.docusign.com>.

2. Enter your email address.

3. Click **Use Company Login**.

4. When you're redirected to PingOne for Enterprise, enter your PingOne username and password.

   ![Screen capture of the PingOne for Enterprise sign-on page.](_images/scs1621290470051.png)

   After successful authentication, you're redirected back to DocuSign.

   ![Screen capture of the DocuSign domain.](_images/mds1621290533443.png)