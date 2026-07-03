---
title: Configuring SAML SSO with SuccessFactors and PingFederate
description: Learn how to enable SuccessFactors sign-on from a PingFederate URL (IdP-initiated sign-on) and direct SuccessFactors sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:successfactors:config_saml_successfactors_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/successfactors/config_saml_successfactors_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  create-a-pingfederate-sp-connection-for-successfactors: Create a PingFederate SP connection for SuccessFactors
  add-the-pingfederate-idp-connection-to-successfactors: Add the PingFederate IdP Connection to SuccessFactors
  update-the-acs-url-values-in-pingfederate: Update the ACS URL values in PingFederate
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
---

# Configuring SAML SSO with SuccessFactors and PingFederate

Learn how to enable SuccessFactors sign-on from a PingFederate URL (IdP-initiated sign-on) and direct SuccessFactors sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users requiring application access.

* Populate SuccessFactors with at least one user to test access.

* You must have administrative access to PingFederate.

* You must have access to either SuccessFactors Customer Support or the SuccessFactors Provisioning tool.

## Create a PingFederate SP connection for SuccessFactors

1. Sign on to the PingFederate administrative console.

2. Create an SP connection for SuccessFactors in PingFederate:

   1. Configure using**Browser SSO** profile **SAML 2.0**.

   2. Set **Partner's Entity ID** to `https://www.successfactors.com`.

   3. Enable the following **SAML Profiles**:

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   4. In **Assertion Creation: Attribute Contract**, extend the contract to add an attribute named **SAML\_NAME\_FORMAT**.

   5. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfillment**, map **SAML\_SUBJECT** and map **SAML\_NAME\_FORMAT** to `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`.

   6. In **Protocol Settings: Assertion Consumer Service URL**, set **binding** to **POST**, and set **Endpoint URL** to `http://placeholder`.

      You will update this value later.

   7. In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

   8. In **Credentials: Digital Signature Settings**, select the PingFederate signing certificate.

3. Save the configuration.

4. Export the signing certificate.

5. Export and then open the metadata file, and copy the following values:

   * The entityID

   * The Location entry (`https://your-value/idp/SSO.saml2`)

## Add the PingFederate IdP Connection to SuccessFactors

1. Sign on to the SuccessFactors Provisioning application.

   |   |                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------- |
   |   | If you do not have access to this application, you will need to contact SuccessFactors' Customer Support. |

2. Search for your company and click its name link.

   ![Screen capture of SuccessFactors Companies page with Your Company hyperlink highlighted in red.](_images/mbk1622048337046.png)

3. Click **Single Sign-On (SSO) Settings**.

   ![Screen capture of SuccessFactors Edit Company Settings section with the Single Sign-On (SSO) Settings hyperlink highlighted in red.](_images/wwd1622048425777.png)

4. In the **For SAML based SSO** section, click **SAML v2 SSO**.

5. In the **SAML Asserting Parties (IdP)** list, select **Add a SAML Asserting Party**, and enter the following values:

   | Field                                              | Value                                                |
   | -------------------------------------------------- | ---------------------------------------------------- |
   | **SAML Asserting Party Name**                      | PingFederate                                         |
   | **SAML Issuer**                                    | The PingFederate **Issuer** value                    |
   | **Require Mandatory Signature**                    | **Assertion**                                        |
   | **Enable SAML Flag**                               | **Enabled**                                          |
   | **Login Requested Signature (SF Generated/SP/RP)** | Select **No**.                                       |
   | **SAML Profile**                                   | **Browser/Post Profile**                             |
   | **SAML Verifying Certificate**                     | Paste the PingFederate signing certificate contents. |

   ![Screen capture of SuccessFactors SAML based SSO settings with SAML v2 SSO selected and highlighted in red. The fields for Add a SAML Asserting Party, SAML Asserting Party Name, SAML Issuer, Require Mandatory Signature, Enable SAML Flag, Login Request Signature, SAML Profile, and SAML Verifying Certificate are also highlighted in red.](_images/vof1622048790228.png)

6. In the **SAML v2: SP-initiated login** section, enter the following values:

   | Field                                                                | Value                                                                       |
   | -------------------------------------------------------------------- | --------------------------------------------------------------------------- |
   | **Enable sp initiated login (AuthnRequest)**                         | Select **Yes**.                                                             |
   | **Default issuer**                                                   | Selected.                                                                   |
   | **single sign on redirect service location (to be provided by idp)** | `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=IdP-ID-value` |
   | **Send request as Company-Wide issuer**                              | Select **Yes**.                                                             |

   ![Screen capture of SuccessFactors SAML v2 : SP-initiated login section with all fields highlighted in red.](_images/vze1622049158112.png)

7. Click **Add an asserting party** to save the configuration.

   ![Screen capture of SuccessFactors SAML Asserting Parties(IdP) section with Add an asserting party highlighted in red.](_images/ubt1622049263265.png)

8. In the **SAML Asserting Parties (IdP)** list, select the asserting party that you created.

   ![Screen capture of SuccessFactors SAML Asserting Parties(IdP) dropdown menu with test selected and highlighted in red.](_images/qxn1622049536222.png)

9. Go to **Single Sign On Features**.

10. In the **Single Sign On Features** section, enter any text value in the **Reset Token** field.

    A value is required only to switch on SSO.

11. Click **Save Token**.

    ![Screen capture of SuccessFactors Single Sign On Features section with the Reset Token field and Save Token hyperlink both highlighted in red. Token is required for all SSO also appears as red text.](_images/udp1622049586404.png)

12. Record the SuccessFactors **Assertion Consumer Service URL** value containing your SuccessFactors **Hostname** and **Company ID**.

    (`https://your-hostname.successfactors.com/saml2/SAMLAssertionConsumer?company=your-company-ID`)

## Update the ACS URL values in PingFederate

1. Sign on to the PingFederate administrative console.

2. Edit the SP connection for SuccessFactors.

3. Set **Assertion Consumer Service URL → Endpoint URL** to the SuccessFactors **Assertion Consumer Service URL** value.

   (`https://your-hostname.successfactors.com/saml2/SAMLAssertionConsumer?company=your-company-ID`)

4. Save the changes.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO Application Endpoint for the SuccessFactors SP connection.

2. Complete PingFederate authentication.

   You're redirected to your SuccessFactors domain.
