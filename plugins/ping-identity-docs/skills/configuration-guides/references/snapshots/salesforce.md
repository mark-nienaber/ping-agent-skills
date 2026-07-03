---
title: Configure direct Salesforce sign on using PingOne (SP-initiated login) plus SLO
description: You must first enable identity provider (IdP)-initiated sign-on.
component: configuration_guides
page_id: configuration_guides:salesforce:config_signon_slo_salesforce_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/salesforce/config_signon_slo_salesforce_p1.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  enable-pingone-authentication-in-salesforce: Enable PingOne authentication in Salesforce
  test-the-pingone-sp-initiated-sso-integration: Test the PingOne SP-initiated SSO integration
---

# Configure direct Salesforce sign on using PingOne (SP-initiated login) plus SLO

## Before you begin

* You must first enable identity provider (IdP)-initiated sign-on.

## Enable PingOne authentication in Salesforce

1. Sign on to your Salesforce domain as an administrator.

2. Click the **Gear** icon, then go to **Setup → Company Settings → My Domain**.

   ![Screen capture of the Salesforce Settings menu with the My Domain tab highlighted.](_images/icd1619220366566.png)

3. Make a note of your domain name, for example, `https://your-company.my.salesforce.com`

4. In the **Authentication Configuration** section, click **Edit**.

   ![Screen capture of the Salesforce Authentication Configuration page with the Edit button highlighted in red.](_images/kka1619220392349.png)

5. In the **Authentication Service** list, select **PingOne**. Click **Save**.

   ![Screen capture of the Salesforce Authentication Configuration fields with the Save button and the Authentication Service pingone check box highlighted in red](_images/uci1619220428580.png)

   |   |                                                                       |
   | - | --------------------------------------------------------------------- |
   |   | This entry was created as a result of the IdP-initiated sign-on task. |

   Configuration is complete.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Salesforce will now redirect to PingOne for authentication of all new sessions. You should also select the **Login Form** check box during the testing phase in case of authentication issues.Testers will be offered the option of the standard Salesforce login form or PingOne authentication.After you've successfully tested authentication, you can clear the **Login Form** check box so that authentication automatically defaults to PingOne. |

## Test the PingOne SP-initiated SSO integration

1. Go to your Salesforce domain.

   |   |                                                                                                                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the **Login Form** check box is still selected, the Salesforce sign-on screen still displays, and you're offered a choice of Salesforce sign on or PingOne sign, select PingOne.If you've cleared the **Login Form** check box, you're not offered a choice. |

2. When you are redirected to PingOne, enter your PingOne username and password.

   After successful authentication, you're redirected back to Salesforce.

   ![Screen capture of the Salesforce domain home page.](_images/isr1619220460753.png)

---

---
title: Configure direct Salesforce sign-on using PingFederate (SP-initiated sign-on) plus single logout (SLO)
description: You must first enable IdP-initiated sign-on.
component: configuration_guides
page_id: configuration_guides:salesforce:config_signon_slo_salesforce_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/salesforce/config_signon_slo_salesforce_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  enable-pingfederate-authentication-in-salesforce: Enable PingFederate authentication in Salesforce
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configure direct Salesforce sign-on using PingFederate (SP-initiated sign-on) plus single logout (SLO)

## Before you begin

* You must first enable IdP-initiated sign-on.

## Enable PingFederate authentication in Salesforce

1. Sign on to your Salesforce domain as an administrator.

2. Click the **Gear** icon, then go to **Setup → Company Settings → My Domain**.

   ![Screen capture of the Salesforce Settings menu with the My Domain tab highlighted.](_images/huz1619218618296.png)

3. Make a note of your domain name, such as `https://your-company.my.salesforce.com`.

4. In the **Authentication Configuration** section, click **Edit**.

   ![Screen capture of the Salesforce Authentication Configuration page with the Edit button highlighted in red.](_images/zvc1619218660632.png)

5. In the **Authentication Service** list, select **YourPingFederate**. Click **Save**.

   ![Screen capture of the Salesforce Authentication Configuration page with the Save and YourPingFederate check box highlighted in red.](_images/abf1619218701705.png)

   |   |                                                                                              |
   | - | -------------------------------------------------------------------------------------------- |
   |   | The "YourPingFederate" entry was created as a result of the IdP-initiated login tasks above. |

   Configuration is complete.

Salesforce will now redirect to PingFederate for authentication of all new sessions.

You should also select the **Login Form** check box during the testing phase in case of authentication issues. Testers will be offered the option of the standard Salesforce login form or PingFederate authentication. After you've successfully tested authentication against PingFederate, you can clear the **Login Form** check box so that authentication automatically defaults to PingFederate.

## Test the PingFederate SP-initiated SSO integration

1. Go to your Salesforce domain.

   |   |                                                                                                                                                                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the **Login Form** check box is still selected, the Salesforce sign on screen still displays, and you're offered a choice of Salesforce sign on or PingFederate sign on, select **PingFederate**.If you've cleared the **Login Form** check box, you're not offered a choice. |

2. When you are redirected to PingFederate, enter your PingFederate username and password.

   After successful authentication, you're redirected back to Salesforce.

   ![Screen capture of the Salesforce home page.](_images/dra1619218741821.png)

---

---
title: Configuring SAML SSO with Salesforce and PingFederate
description: Enable Salesforce sign-on from a PingFederate URL (IdP-initiated sign-on) plus single logout (SLO).
component: configuration_guides
page_id: configuration_guides:salesforce:config_saml_salesforce_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/salesforce/config_saml_salesforce_pf.html
revdate: February 10, 2022
section_ids:
  before-you-begin: Before you begin
  create-a-pingfederate-sp-connection-for-salesforce: Create a PingFederate SP connection for Salesforce
  add-the-pingfederate-idp-connection-to-salesforce: Add the PingFederate IDP Connection to Salesforce
  import-the-salesforce-certificate-into-pingfederate: Import the Salesforce certificate into PingFederate
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  configure-direct-salesforce-sign-on-using-pingfederate-sp-initiated-sign-on-plus-single-logout-slo: Configure direct Salesforce sign-on using PingFederate (SP-initiated sign-on) plus single logout (SLO)
  before-you-begin-2: Before you begin
  enable-pingfederate-authentication-in-salesforce: Enable PingFederate authentication in Salesforce
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with Salesforce and PingFederate

Enable Salesforce sign-on from a PingFederate URL (IdP-initiated sign-on) plus single logout (SLO).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users requiring application access.

* Populate Salesforce with at least one user to test access.

* You must have administrative access to PingFederate and Salesforce.

## Create a PingFederate SP connection for Salesforce

1. Sign on to the PingFederate administrative console.

2. Create an SP connection for Salesforce in PingFederate:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Set **Partner's Entity ID** to **Entity ID**.

      * Enable the following SAML Profiles:

      * **IDP-Initiated SSO**

      * **SP Initiated SSO**

      * **IDP-Initiated SLO**

      * **SP Initiated SLO**

   3. In **Assertion Creation → Authentication Source Mapping → Attribute Contract Fulfillment**, map the **SAML\_SUBJECT** to the attribute containing the Salesforce username.

   4. In **Protocol Settings → Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to **ACS URL**.

   5. In **Protocol Settings → SLO Service URLs**, set **Binding** to **POST** and set **Endpoint URL** to **SLO URL**.

   6. In **Protocol Settings → Allowable SAML Bindings**, enable **POST**.

   7. In **Credentials → Digital Signature Settings**, select the **PingFederate Signing Certificate**.

   8. In **Credentials → Signature Verification**, set **Trust Model** to **Unanchored**.

   9. In **Credentials → Signature Verification → Signature Verification Certificate**, select the **PingFederate Signing Certificate**.

      |   |                                                                                       |
      | - | ------------------------------------------------------------------------------------- |
      |   | This certificate is a placeholder and will be replaced with a Salesforce certificate. |

3. Export the metadata for the newly created Salesforce SP connection.

4. Export the signing certificate.

## Add the PingFederate IDP Connection to Salesforce

1. Sign on to your Salesforce domain as an administrator.

2. Click the **Gear** icon, then go to **Setup → Identity → Single Sign-On Settings**.

   ![Screen capture of the Salesforce Single Sign-On Settings.](_images/qxq1619216915118.png)

3. On the **Single Sign-On Settings** page, click **Edit**.

   ![Screen capture of the Salesforce Single Sign-On Settings with the Edit button highlighted in red.](_images/ood1619216957673.png)

4. Select the **SAML Enabled** check box to enable the use of SAML single sign-on. Click **Save**.

   ![Screen capture of the Salesforce Single Sign-On Settings with the SAML enabled checkbox and the Save button highlighted in red.](_images/kpc1619216998431.png)

5. Click **New From Metadata File**.

   ![Screen capture of the Salesforce SAML Single Sign-On Settings section with the New from Metadata File button highlighted in red.](_images/rji1619217026354.png)

6. Click **Choose File**, select the metadata that you downloaded from PingFederate, and click **Create**.

   ![Screen capture of the Salesforce SAML Single Sign-On Settings with the Choose File and the Create buttons highlighted in red.](_images/oje1619217061693.png)

   The summary screen opens.

7. In the **Identity Provider Certificate** section, click **Choose file** and select the signing certificate that you downloaded from PingFederate.

8. Clear the **Single Logout Enabled** check box if you don't require single logout.

   The summary page opens.

   ![Screen capture of the SAML Single Sign-On Settings with the Save button highlighted in red.](_images/rfg1619217108763.png)

9. Click **Save**.

10. On the summary page for the configuration that you saved in the previous step, click **Edit**.

    ![Screen capture of the SAML Single Sign-On Settings with the Edit button highlighted in red.](_images/ecr1619217157176.png)

11. Click the link on the **Request Signing Certificate** line.

    ![Screen capture of the Identity Provider Certificate, the Request Signing Certificate, and the Request Signature Method fields with the Request Signing Certificate field highlighted in red.](_images/bnn1619217208047.png)

12. Click **Download Certificate**.

    ![Screen capture of the Certificates section with the Download Certificate button highlighted in red.](_images/yxt1619217291556.png)

## Import the Salesforce certificate into PingFederate

1. Sign on to the PingFederate administrative console.

2. Open the Salesforce SP connection and click **Signature Verification Certificate**.

3. Delete the placeholder certificate and upload the certificate that you downloaded from Salesforce.

4. Save the configuration.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO application endpoint for the Salesforce SP connection.

2. Complete PingFederate authentication.

   You're redirected to your Salesforce domain.

   ![Screen capture of the Salesforce doman home page.](_images/sep1619217350076.png)

## Configure direct Salesforce sign-on using PingFederate (SP-initiated sign-on) plus single logout (SLO)

### Before you begin

* You must first enable IdP-initiated sign-on.

### Enable PingFederate authentication in Salesforce

1. Sign on to your Salesforce domain as an administrator.

2. Click the **Gear** icon, then go to **Setup → Company Settings → My Domain**.

   ![Screen capture of the Salesforce Settings menu with the My Domain tab highlighted.](_images/huz1619218618296.png)

3. Make a note of your domain name, such as `https://your-company.my.salesforce.com`.

4. In the **Authentication Configuration** section, click **Edit**.

   ![Screen capture of the Salesforce Authentication Configuration page with the Edit button highlighted in red.](_images/zvc1619218660632.png)

5. In the **Authentication Service** list, select **YourPingFederate**. Click **Save**.

   ![Screen capture of the Salesforce Authentication Configuration page with the Save and YourPingFederate check box highlighted in red.](_images/abf1619218701705.png)

   |   |                                                                                              |
   | - | -------------------------------------------------------------------------------------------- |
   |   | The "YourPingFederate" entry was created as a result of the IdP-initiated login tasks above. |

   Configuration is complete.

Salesforce will now redirect to PingFederate for authentication of all new sessions.

You should also select the **Login Form** check box during the testing phase in case of authentication issues. Testers will be offered the option of the standard Salesforce login form or PingFederate authentication. After you've successfully tested authentication against PingFederate, you can clear the **Login Form** check box so that authentication automatically defaults to PingFederate.

### Test the PingFederate SP-initiated SSO integration

1. Go to your Salesforce domain.

   |   |                                                                                                                                                                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the **Login Form** check box is still selected, the Salesforce sign on screen still displays, and you're offered a choice of Salesforce sign on or PingFederate sign on, select **PingFederate**.If you've cleared the **Login Form** check box, you're not offered a choice. |

2. When you are redirected to PingFederate, enter your PingFederate username and password.

   After successful authentication, you're redirected back to Salesforce.

   ![Screen capture of the Salesforce home page.](_images/dra1619218741821.png)

---

---
title: Configuring SAML SSO with Salesforce and PingOne for Enterprise
description: Enable Salesforce sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) plus single logout (SLO).
component: configuration_guides
page_id: configuration_guides:salesforce:config_saml_salesforce_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/salesforce/config_saml_salesforce_p1.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  extract-the-pingone-for-enterprise-metadata-for-salesforce: Extract the PingOne for Enterprise metadata for Salesforce
  add-the-pingone-for-enterprise-idp-connection-to-salesforce: Add the PingOne for Enterprise IdP Connection to Salesforce
  import-the-salesforce-metadata-into-pingone: Import the Salesforce metadata into PingOne.
  test-the-pingone-for-enterprise-idp-initiated-sso-integration: Test the PingOne for Enterprise IdP-initiated SSO integration
  configure-direct-salesforce-sign-on-using-pingone-sp-initiated-login-plus-slo: Configure direct Salesforce sign on using PingOne (SP-initiated login) plus SLO
  before-you-begin-2: Before you begin
  enable-pingone-authentication-in-salesforce: Enable PingOne authentication in Salesforce
  test-the-pingone-sp-initiated-sso-integration: Test the PingOne SP-initiated SSO integration
---

# Configuring SAML SSO with Salesforce and PingOne for Enterprise

Enable Salesforce sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) plus single logout (SLO).

## Before you begin

* Link PingOne for Enterprise to an identity repository containing the users requiring application access.

* Populate Salesforce with at least one user to test access.

* You must have administrative access to PingOne for Enterprise and Salesforce.

## Extract the PingOne for Enterprise metadata for Salesforce

1. Sign on to PingOne for Enterprise and go to **Applications → Application Catalog**.

2. Search for `Salesforce`.

   ![Screen capture of the PingOne for Enterprise Application Catalog with various Salesforce applications displayed.](_images/ggx1619219319740.png)

3. Expand the Salesforce entry and click the **Setup** icon.

4. Click **Continue to Next Step** until you're on the **Group Access** page.

   |   |                                                                   |
   | - | ----------------------------------------------------------------- |
   |   | You'll configure the application settings later through metadata. |

5. Click **Add** for each user group that should have access to Salesforce.

   ![Screen capture of the Group Access section with the Group search bar and the available Group Names displaying.](_images/glp1619219372679.png)

6. Click **Continue to Next Step**.

7. Download the PingOne for Enterprise signing certificate and SAML metadata.

8. Click **Finish**.

   ![Screen capture of the Single Logout Response Endpoint section with the Signing Certificate and SAML Metadata Download buttons highlighted in red.](_images/kab1619219407787.png)

## Add the PingOne for Enterprise IdP Connection to Salesforce

1. Sign on to your Salesforce domain as an administrator.

2. Click the **Gear** icon ([icon: gear, set=fa]), then go to **Setup → Identity → Single Sign-On Settings**.

   ![Screen capture of the Salesforce Single Sign-On Settings page.](_images/ymz1619219443121.png)

3. On the **Single Sign-On Settings** page, click **Edit**.

   ![Screen capture of the Salesforce Single Sign-On Settings Setup page with the Edit button highlighted in red.](_images/bbf1619219484774.png)

4. Select the **SAML Enabled** check box to enable the use of SAML SSO. Click **Save**.

   ![Screen capture of the Salesforce Signle Sign-On Settings page with the SAML Enabled check box and the Save button highlighted in red.](_images/gyv1619219637121.png)

5. Click **New From Metadata File**.

   ![Screen capture of the Samle Single Sign-On Settings page with the New from Metadata File button highlighted in red.](_images/sih1619219553530.png)

6. Click **Choose File**, select the SAML metadata file that you downloaded from PingOne for Enterprise, and click **Create**.

   ![Screen capture of the SAML Single Sign-On Settings page with the Choose Metadata File and Create buttons highlighted in red.](_images/big1619219699886.png)

   The summary screen opens.

7. On the **Identity Provider Certificate** line, click **Choose File** and select the signing certificate that you downloaded from PingOne for Enterprise.

8. Set **Service Provider Initiated Request Binding** to **HTTP POST**.

9. Set **Single Logout Request Binding** to **HTTP POST**.

10. Clear the **Single Logout Enabled** check box if you don't require single logout.

    The summary screen will resemble the following:

    ![Screen capture of the SAML Single Sign-On Settings summary page with metadata file warnings highlighted in red.](_images/xon1619219855807.png)

11. Ignore the metadata file warnings and click **Save**.

12. Click **Download Metadata** to save the Salesforce metadata.

    ![Screen capture of the Endpoints section of the Salesforce metadata summary page with the Download Metadata button highlighted in red.](_images/qwu1619219992372.png)

## Import the Salesforce metadata into PingOne.

1. Sign on to PingOne for Enterprise and go to **Applications → My Applications**.

2. Expand the Salesforce entry and click **Edit**.

3. Click **Continue to Next Step**.

4. Click **Select File** and select the metadata file that you downloaded from Salesforce.

   ![Screen capture of the Upload Metadata field with the Select File button highlighted in red.](_images/iis1619220121654.png)

   The **ACS URL**, **Entity ID**, **Single Logout Endpoint**, and **Primary Verification Certificate** fields should now be populated.

   ![Screen capture of the populated Connection Configuration fields.](_images/nil1619220160144.png)

5. Click **Continue to Next Step** on the remaining pages then click **Finish**.

   |   |                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This step assumes that your usernames in Salesforce match the ones in PingOne for Enterprise. If this is not the case, then you must map the expected Salesforce username value on the third page. |

## Test the PingOne for Enterprise IdP-initiated SSO integration

1. Go to your Ping desktop as a user with Salesforce access.

   |   |                                                                                               |
   | - | --------------------------------------------------------------------------------------------- |
   |   | To find the Ping desktop URL in the Admin console, go to **Setup → Dock → PingOne Dock URL**. |

2. Complete PingOne for Enterprise authentication.

   You're redirected to your Salesforce domain.

   ![Screen capture of the Salesforce domain home page..](_images/dev1619220239684.png)

## Configure direct Salesforce sign on using PingOne (SP-initiated login) plus SLO

### Before you begin

* You must first enable identity provider (IdP)-initiated sign-on.

### Enable PingOne authentication in Salesforce

1. Sign on to your Salesforce domain as an administrator.

2. Click the **Gear** icon, then go to **Setup → Company Settings → My Domain**.

   ![Screen capture of the Salesforce Settings menu with the My Domain tab highlighted.](_images/icd1619220366566.png)

3. Make a note of your domain name, for example, `https://your-company.my.salesforce.com`

4. In the **Authentication Configuration** section, click **Edit**.

   ![Screen capture of the Salesforce Authentication Configuration page with the Edit button highlighted in red.](_images/kka1619220392349.png)

5. In the **Authentication Service** list, select **PingOne**. Click **Save**.

   ![Screen capture of the Salesforce Authentication Configuration fields with the Save button and the Authentication Service pingone check box highlighted in red](_images/uci1619220428580.png)

   |   |                                                                       |
   | - | --------------------------------------------------------------------- |
   |   | This entry was created as a result of the IdP-initiated sign-on task. |

   Configuration is complete.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Salesforce will now redirect to PingOne for authentication of all new sessions. You should also select the **Login Form** check box during the testing phase in case of authentication issues.Testers will be offered the option of the standard Salesforce login form or PingOne authentication.After you've successfully tested authentication, you can clear the **Login Form** check box so that authentication automatically defaults to PingOne. |

### Test the PingOne SP-initiated SSO integration

1. Go to your Salesforce domain.

   |   |                                                                                                                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the **Login Form** check box is still selected, the Salesforce sign-on screen still displays, and you're offered a choice of Salesforce sign on or PingOne sign, select PingOne.If you've cleared the **Login Form** check box, you're not offered a choice. |

2. When you are redirected to PingOne, enter your PingOne username and password.

   After successful authentication, you're redirected back to Salesforce.

   ![Screen capture of the Salesforce domain home page.](_images/isr1619220460753.png)