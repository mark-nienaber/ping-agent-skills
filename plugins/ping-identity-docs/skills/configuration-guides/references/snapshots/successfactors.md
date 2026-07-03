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

---

---
title: Configuring SAML SSO with SuccessFactors and PingOne for Enterprise
description: Learn how to enable SuccessFactors sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct SuccessFactors sign-on using PingOne for Enterprise (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:successfactors:config_saml_successfactors_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/successfactors/config_saml_successfactors_p1.html
revdate: May 20, 2024
section_ids:
  before-you-begin: Before you begin
  obtain-the-pingone-for-enterprise-values-for-the-successfactors-application: Obtain the PingOne for Enterprise values for the SuccessFactors application
  add-the-pingone-for-enterprise-idp-connection-to-successfactors: Add the PingOne for Enterprise IdP connection to SuccessFactors
  complete-the-successfactors-setup-in-pingone-for-enterprise: Complete the SuccessFactors setup in PingOne for Enterprise
  test-the-pingone-for-enterprise-idp-initiated-sso-integration: Test the PingOne for Enterprise IdP-initiated SSO integration
  test-the-pingone-sp-initiated-sso-integration: Test the PingOne SP-initiated SSO integration
---

# Configuring SAML SSO with SuccessFactors and PingOne for Enterprise

Learn how to enable SuccessFactors sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct SuccessFactors sign-on using PingOne for Enterprise (SP-initiated sign-on).

## Before you begin

* Link PingOne for Enterprise to an identity repository containing the users requiring application access.

* Populate SuccessFactors with at least one user to test access.

* You must have administrative access to PingOne for Enterprise.

* You must have access to either SuccessFactors Customer Support or the SuccessFactors Provisioning tool.

## Obtain the PingOne for Enterprise values for the SuccessFactors application

1. Sign on to PingOne for Enterprise and go to **Applications → Application Catalog**.

2. Search for `SuccessFactors`.

   ![Screen capture of Application Catalog with SuccessFactors entered in the search bar and the expansion arrow for the result highlighted in red.](_images/tzy1621954660187.png)

3. Expand the SuccessFactors entry and click the **Setup** icon.

4. Copy the **Issuer** and **IdP ID** values.

5. Download the signing certificate.

   ![Screen capture of SSO Instructions with the Signing Certificate Download hyperlink, IdP ID field, and Issuer field all highlighted in red.](_images/rvm1621954861081.png)

## Add the PingOne for Enterprise IdP connection to SuccessFactors

1. Sign on to the SuccessFactors Provisioning application.

   |   |                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------- |
   |   | If you do not have access to this application, you will need to contact SuccessFactors' Customer Support. |

2. Search for your company and click its name link.

   ![Screen capture of SuccessFactors Companies List with Your Company highlighted in red.](_images/xie1621955047666.png)

3. Click **Single Sign-On (SSO) Settings**.

   ![Screen capture of SuccessFactors Edit Company Settings with Single Sign-On (SSO) Settings highlighted in red.](_images/nhh1621955183823.png)

4. In the **For SAML based SSO** section, click **SAML v2 SSO**.

5. In the **SAML Asserting Parties (IdP)** list, select **Add a SAML Asserting Party**, and enter the following.

   | Field                                            | Value                                                          |
   | ------------------------------------------------ | -------------------------------------------------------------- |
   | **SAML Asserting Party Name**                    | PingOne for Enterprise                                         |
   | **SAML Issuer**                                  | The PingOne for Enterprise **Issuer** value.                   |
   | **Require Mandatory Signature**                  | **Assertion**                                                  |
   | **Enable SAML Flag**                             | **Enabled**                                                    |
   | **Login Request Signature (SF Generated/SP/RP)** | Select **No.**                                                 |
   | **SAML Profile**                                 | **Browser/Post Profile**                                       |
   | **SAML Verifying Certificate**                   | Paste the PingOne for Enterprise signing certificate contents. |

   ![Screen capture of SuccessFactors SAML settings with SAML v2 SSO checked and highlighted in red. Below, Add a SAML Asserting Party is highlighted in red, as well as the fields for SAML Asserting Party Name, SAML Issuer, Require Mandatory Signature, Enable SAML Flag, Login Request Signature(SF Generate/SP/RP), SAML Profiled, and SAML Verifying Certificate.](_images/rgy1621955570180.png)

6. In the **SAML v2: SP-initiated login** section, enter the following.

   | Field                                                                | Value                                                                       |
   | -------------------------------------------------------------------- | --------------------------------------------------------------------------- |
   | **Enable sp initiated login (AuthnRequest)**                         | Select **Yes**.                                                             |
   | **Default Issuer**                                                   | Selected.                                                                   |
   | **single sign on redirect service location (to be provided by idp)** | `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=IdP-ID-value` |
   | **Send request as Company-Wide issuer**                              | Select **Yes**.                                                             |

   ![Screen capture of SuccessFactors SAML v2 : SP-initiated login section with all its applicable fields highlighted in red.](_images/xni1621956065976.png)

7. Click **Add an asserting party** to save the configuration.

   ![Screen capture of SuccessFactors SAML Asserting Parties(IdP) section with Add an asserting party highlighted in red.](_images/hop1621956214007.png)

8. In the **SAML Asserting Parties (IdP)** list, select the asserting party that you created.

   ![Screen capture of SuccessFactors SAML Asserting Parties(IdP) dropdown menu with test highlighted in red.](_images/lsz1621956298053.png)

9. In the **Single Sign On Features** section, enter any text value in the **Reset Token** field.

   A value is required only to switch on SSO.

10. Click **Save Token**.

    ![Screen capture of SuccessFactors Single Sign On Features section with the Reset Token field and Save Token field highlighted In red. Token is required for all SSO is also noted in red.](_images/sux1621956541928.png)

11. Record the SuccessFactors **Assertion Consumer Service URL** value containing your SuccessFactors **Hostname** and **Company ID**.

    (\`https\://*your-hostname*.successfactors.com/saml2/SAMLAssertionConsumer?company=*your-company-ID*)

## Complete the SuccessFactors setup in PingOne for Enterprise

1. Continue editing the SuccessFactors entry in PingOne for Enterprise for Enterprise.

   |   |                                                                                              |
   | - | -------------------------------------------------------------------------------------------- |
   |   | If the session has timed out, complete the initial steps to the point of clicking **Setup**. |

2. Click **Continue to Next Step**.

3. Set the **ACS URL** to be the SuccessFactors **Assertion Consumer Service URL** value.

   (`https://your-hostname.successfactors.com/saml2/SAMLAssertionConsumer?company=your-company-ID`)

4. Leave the preset **Entity ID**.

5. In the **Target Resource** field, replace `${sfdatacenter}` with the hostname from the **ACS URL** value.

   ![Screen capture of SSO attribute values with the fields for ACS URL, Entity ID, and Target Resource all highlighted in red.](_images/oqc1621958803227.png)

6. Click **Continue to Next Step**.

7. Map the **SAML\_SUBJECT** attribute to the similar attribute names in your environment and click **Advanced**.

   ![Screen capture of Attribute Mapping section. In the SAML\_SUBJECT\* row and Identity Bridge Attribute or Literal Value column, SAML\_SUBJECT and Advanced are highlighted in red.](_images/bie1621959006376.png)

8. Set the **Name ID Format to send to SP** to **urn:oasis:names:tc:SAML:2.0:nameid-format:persistent**. Click **Save**.

   ![Screen capture of Advanced Attribute Options with the field for Name ID Format to send to SP highlighted in red, as well as the Save button at the bottom of the screen.](_images/qjz1621959244085.png)

9. Click **Continue to Next Step** twice.

10. Click **Add** for all user groups that should have access to SuccessFactors.

    ![Screen capture of Group Access page with option to remove/add Users@directory and Domain Administrators@directory.](_images/mqh1621959361157.png)

11. Click **Continue to Next Step**.

12. Click **Finish**.

## Test the PingOne for Enterprise IdP-initiated SSO integration

1. Go to your Ping desktop as a user with SuccessFactors access.

   |   |                                                                                               |
   | - | --------------------------------------------------------------------------------------------- |
   |   | To find the Ping desktop URL in the Admin console, go to **Setup → Dock → PingOne Dock URL**. |

2. Complete the PingOne for Enterprise authentication.

   You're redirected to your SuccessFactors account.

   ![Screen capture of login screen.](_images/dtb1621959941529.png)

## Test the PingOne SP-initiated SSO integration

1. Go to your SuccessFactors URL.

2. When you're redirected to PingOne for Enterprise, enter your PingOne username and password.

   ![Screen capture of login screen.](_images/ekx1621960032886.png)

   You're redirected back to SuccessFactors.