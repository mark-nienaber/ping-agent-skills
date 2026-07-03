---
title: Configuring SAML SSO with GitHub Cloud and PingFederate
description: Learn how to enable GitHub sign-on from a PingFederate URL (IdP-initiated sign-on) and direct GitHub sign on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:github:config_saml_githubcloud_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/github/config_saml_githubcloud_pf.html
revdate: May 16, 2024
section_ids:
  before-you-begin: Before you begin
  create-a-pingfederate-sp-connection-for-github: Create a PingFederate SP connection for GitHub
  add-the-pingfederate-idp-connection-to-github: Add the PingFederate IdP connection to GitHub
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with GitHub Cloud and PingFederate

Learn how to enable GitHub sign-on from a PingFederate URL (IdP-initiated sign-on) and direct GitHub sign on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users requiring application access.

* Populate GitHub with at least one user to test access.

* You must have administrative access to PingFederate and GitHub.

## Create a PingFederate SP connection for GitHub

1. Sign on to the PingFederate administrative console.

2. Create an SP connection for GitHub in Ping Federate UI:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Set **Partner's Entity ID** to `https://github.com/orgs/your-tenant`.

   3. Enable the following SAML Profiles:

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   4. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfillment**, map **SAML\_SUBJECT** to an attribute containing the user's email address.

   5. In **Protocol Settings: Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to `https://github.com/orgs/your-tenant/saml/consume`.

   6. In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

   7. In **Credentials: Digital Signature Settings**, select the **PingFederate Signing Certificate**.

3. Save the configuration.

4. Export the signing certificate.

5. Export and then open the metadata file.

   Copy the value of the entityID and the Location entry (`https://your-value/idp/SSO.saml2`).

## Add the PingFederate IdP connection to GitHub

1. Sign on to GitHub as an administrator.

2. Select your GitHub organization.

3. Click **Organization settings**, then click **Security**.

4. Under **SAML single sign-on**, select **Enable SAML authentication**.

   |   |                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The assertion consumer service URL displayed on this screen should match the value that you entered into the PingFederate **Endpoint URL** field. |

   ![Screen capture of GitHub settings with the Enable checkbox, assertion consumer service URL, Sign on URL, Issuer URL, and Public certificate fields highlighted in red.](_images/rin1625253520648.png)

5. Set the following values.

   | Field                  | Value                                                                |
   | ---------------------- | -------------------------------------------------------------------- |
   | **Sign on URL**        | The PingFederate Location value (`https://your-value/idp/SSO.saml2`) |
   | **Issuer**             | The PingFederate entityID value.                                     |
   | **Public certificate** | Paste in the contents of the PingFederate signing certificate.       |

6. Click **Save**.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate **SSO Application Endpoint** for the GitHub SP connection.

2. Complete the PingFederate authentication.

   You're redirected to your GitHub domain.

## Test the PingFederate SP-initiated SSO integration

1. Go to `https://github.com/orgs/your-tenant/sso`

2. After you're redirected to PingFederate, enter your PingFederate username and password.

   You're redirected back to GitHub.

---

---
title: Configuring SAML SSO with GitHub Cloud and PingOne for Enterprise
description: Learn how to enable GitHub sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct GitHub sign-on using PingOne for Enterprise (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:github:config_saml_githubcloud_p14e
canonical_url: https://docs.pingidentity.com/configuration_guides/github/config_saml_githubcloud_p14e.html
revdate: May 16, 2024
section_ids:
  before-you-begin: Before you begin
  set-up-the-supplied-github-application-in-pingone-for-enterprise: Set up the supplied GitHub application in PingOne for Enterprise
  add-the-pingone-for-enterprise-idp-connection-to-github: Add the PingOne for Enterprise IdP connection to GitHub
  test-the-pingone-for-enterprise-idp-initiated-sso-integration: Test the PingOne for Enterprise IdP-initiated SSO integration
  test-the-pingone-for-enterprise-sp-initiated-sso-integration: Test the PingOne for Enterprise SP-initiated SSO integration
---

# Configuring SAML SSO with GitHub Cloud and PingOne for Enterprise

Learn how to enable GitHub sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct GitHub sign-on using PingOne for Enterprise (SP-initiated sign-on).

## Before you begin

* Link PingOne for Enterprise to an identity repository containing the users requiring application access.

* Populate GitHub with at least one user to test access.

* You must have administrative access to PingOne for Enterprise and GitHub.

## Set up the supplied GitHub application in PingOne for Enterprise

1. Sign on to PingOne for Enterprise for and go to **Applications → Application Catalog**.

2. Search for `GitHub`.

3. Expand the GitHub entry and click the **Setup** icon.

   ![Screen capture of PingOne for Enterprise Application Catalog with GitHub displayed as the search result and the expansion arrow highlighted in red.](_images/smv1625254124267.png)

4. Copy the **Issuer** and **IdP ID** values.

5. Download the signing certificate.

   ![Screen capture of PingOne for Enterprise SSO Instructions with the Signing Certificate Download hyperlink, IdP ID, and Issuer value highlighted in red.](_images/ola1625254236990.png)

6. Click **Continue to Next Step**.

7. Set **ACS URL** to `https://github.com/orgs/your-tenant/saml/consume`.

   Set **Entity ID** to `https://github.com/orgs/your-tenant`.

8. Click **Continue to Next Step**.

9. Ensure that **SAML\_SUBJECT** is mapped to the field containing a user's email address.

10. Click **Continue to Next Step** twice.

11. Click **Add** for all user groups that should have access to GitHub.

    ![Screen capture of PingOne for Enterprise Group Access page.](_images/qgs1625254380304.png)

12. Click **Continue to Next Step**.

13. Click **Finish**.

## Add the PingOne for Enterprise IdP connection to GitHub

1. Sign on to GitHub as an administrator.

2. Select your GitHub organization.

3. Click **Organization settings**, then click **Security**.

4. Under **SAML single sign-on**, select **Enable SAML authentication**.

   |   |                                                                                                                                                                                                                                                                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The assertion consumer service URL displayed on this screen should match the value that you entered into the PingOne for Enterprise **ACS URL** field.![Screen capture of GitHub SAML settings with the Enable SAML authentication checkbox, assertion consumer service URL, Sign on URL, Issuer URL, and Public certificate highlighted in red.](_images/tup1625254603157.png) |

5. Set the following values.

   | Field                  | Value                                                                               |
   | ---------------------- | ----------------------------------------------------------------------------------- |
   | **Sign on URL**        | `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=PingOne-IdP-ID-value` |
   | **Issuer**             | PingOne for Enterprise **Issuer** value                                             |
   | **Public certificate** | Paste in the contents of the PingOne for Enterprise signing certificate.            |

6. Click **Save**.

## Test the PingOne for Enterprise IdP-initiated SSO integration

1. Go to your Ping desktop as a user with GitHub access.

   |   |                                                                                    |
   | - | ---------------------------------------------------------------------------------- |
   |   | To find the Ping desktop URL in the Admin console, go to **Setup → PingOne Dock**. |

2. Complete the PingOne for Enterprise authentication.

   You're redirected to your GitHub domain.

   ![Screen capture of PingOne for Enterprise sign on screen.](_images/jbo1625254892038.png)

## Test the PingOne for Enterprise SP-initiated SSO integration

1. Go to `https://github.com/orgs/your-tenant/sso`.

2. After you're redirected to PingOne for Enterprise, enter your PingOne for Enterprise username and password.

   ![Screen capture of PingOne for Enterprise sign on screen.](_images/jbo1625254892038.png)

   You're redirected back to GitHub.

---

---
title: Configuring SAML SSO with GitHub Enterprise Server and PingFederate
description: Learn how to enable GitHub sign-on from a PingFederate URL (IdP-initiated sign-on) and direct GitHub sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:github:config_saml_githubenterpriseserver_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/github/config_saml_githubenterpriseserver_pf.html
revdate: May 16, 2024
section_ids:
  before-you-begin: Before you begin
  download-the-github-metadata: Download the GitHub metadata
  create-a-pingfederate-sp-connection-for-github: Create a PingFederate SP connection for GitHub
  add-the-pingfederate-idp-connection-to-github: Add the PingFederate IdP Connection to GitHub
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with GitHub Enterprise Server and PingFederate

Learn how to enable GitHub sign-on from a PingFederate URL (IdP-initiated sign-on) and direct GitHub sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users requiring application access.

* Populate GitHub with at least one user to test access.

* You must have administrative access to PingFederate and GitHub.

## Download the GitHub metadata

1. Go to where your GitHub server publishes its metadata (`https://GitHub-hostname/saml/metadata`).

2. Save the metadata as an XML file.

## Create a PingFederate SP connection for GitHub

1. Sign on to the PingFederate administrative console.

2. Create an SP connection for GitHub in PingFederate using the GitHub metadata file:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Enable the following **SAML Profiles**:

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   3. In **Assertion Creation: Attribute Contract**, if you want to have these values populated in GitHub, extend the contract to add attributes called **username** and **full\_name.**

   4. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfillment**, map **SAML\_SUBJECT** to an attribute containing the user's email address.

      If added, map **username** and **full\_name** to appropriate attributes.

   5. In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

   6. In **Credentials: Digital Signature Settings**, select the **PingFederate Signing Certificate**.

3. Save the configuration.

4. Export the signing certificate.

5. Export and then open the metadata file.

   Copy the value of the entityID and the Location entry (`https://your-value/idp/SSO.saml2`).

## Add the PingFederate IdP Connection to GitHub

1. Sign on to GitHub Enterprise Server as an administrator.

2. Click the **Rocket** icon.

3. Click **Management Console**.

   ![Screen capture of GitHub Site admin controls with Management console highlighted in red.](_images/hjm1625257408895.png)

4. Click **Authentication**.

   ![Screen capture of GitHub Authentication option highlighted in red.](_images/ian1625256331790.png)

5. Click **SAML** and select the **idP initiated SSO (disables AuthnRequest)** check box.

   ![Screen capture of GitHub Authentication settings with SAML checked and idP initiated SSO highlighted in red.](_images/thh1625256392431.png)

6. In the **Single sign-on URL** field, enter the PingFederate Location value (`https://your-value/idp/SSO.saml2`).

   ![Screen capture of GitHub Single sign-on URL field highlighted in red.](_images/xge1625256484285.png)

7. In the **Issuer** field, enter the PingFederate **entityID** value.

   ![Screen capture of GitHub Issuer field highlighted in red.](_images/rfj1625256540616.png)

8. Click **Choose File** for the **Verification Certificate** and upload the PingFederate signing certificate that you downloaded

9. Click **Save Settings**.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate **SSO Application Endpoint** for the GitHub SP connection.

2. Complete the PingFederate authentication.

   You're redirected to your GitHub domain.

## Test the PingFederate SP-initiated SSO integration

1. Go to your GitHub server.

2. After you're redirected to PingFederate, enter your PingFederate username and password.

   You're redirected back to GitHub.

---

---
title: Configuring SAML SSO with GitHub Enterprise Server and PingOne for Enterprise
description: Learn how to enable GitHub sign on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct GitHub sign on using PingOne for Enterprise (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:github:config_saml_githubenterpriseserver_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/github/config_saml_githubenterpriseserver_p1.html
revdate: May 20, 2024
section_ids:
  before-you-begin: Before you begin
  download-the-github-metadata: Download the GitHub metadata
  set-up-the-github-application-in-pingone-for-enterprise: Set up the GitHub application in PingOne for Enterprise
  add-the-pingone-for-enterprise-idp-connection-to-github: Add the PingOne for Enterprise IdP Connection to GitHub
  test-the-pingone-for-enterprise-idp-initiated-sso-integration: Test the PingOne for Enterprise IdP-initiated SSO integration
  test-the-pingone-sp-initiated-sso-integration: Test the PingOne SP-initiated SSO integration
---

# Configuring SAML SSO with GitHub Enterprise Server and PingOne for Enterprise

Learn how to enable GitHub sign on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct GitHub sign on using PingOne for Enterprise (SP-initiated sign-on).

## Before you begin

* Link PingOne for Enterprise to an identity repository containing the users requiring application access.

* Populate GitHub with at least one user to test access.

* You must have administrative access to PingOne for Enterprise and GitHub.

## Download the GitHub metadata

1. Go to where your GitHub server publishes its metadata (`https://GitHub-hostname/saml/metadata`).

2. Save the metadata as an XML file.

## Set up the GitHub application in PingOne for Enterprise

1. Sign on to PingOne for Enterprise for Enterprise and go to **Applications → Application Catalog**.

2. On the **SAML** tab, click **Add Application**.

   ![Screen capture of My Applications tab with the Add Application drop down opened and New SAML Application selected.](_images/opj1625255243572.png)

3. Enter **GitHub** as the application name.

4. Enter a suitable description.

5. Select **Collaboration** as the category.

6. Click **Continue to Next Step**.

7. In the **Upload Metadata** row, click **Select File** and upload the metadata file that you saved from GitHub.

   ![Screen capture of Application Configuration section with the Select File button next to Upload Metadata highlighted in red.](_images/tjn1625255382381.png)

   The following values should now be populated:

   * **ACS URL**: `https://github.com/orgs/your-tenant/saml/consume`

   * **Entity ID**: `https://github.com/orgs/your-tenant`

8. Click **Continue to Next Step**.

9. Click **Add new attribute** and map **SAML\_SUBJECT** to the attribute containing the user's email address.

   ![Screen capture of SSO Attribute Mapping section with the Add new attribute button highlighted in red.](_images/jvj1625255607747.png)

   ![Screen capture of SSO Attribute mapping section with the Application Attribute table displaying SAML\_SUBJECT as the first row entry.](_images/jeh1625255725920.png)

10. **Optional:** Add the **username** and **full\_name** attributes, then map these to appropriate attributes.

    This populates these values in GitHub when a new user signs on.

11. Click **Continue to Next Step**.

12. Click **Add** for all user groups that should have access to GitHub.

    ![Screen capture of Group Access section.](_images/und1625255913186.png)

13. Click **Continue to Next Step**.

14. Copy the **Issuer** and **idpid** values.

    ![Screen capture of Issuer and idpid values redacted and highlighted in red.](_images/wcx1625256134508.png)

15. Download the signing certificate.

    ![Screen capture of Signing Certificate Download hyperlink highlighted in red.](_images/zwu1625256184986.png)

16. Click **Finish**.

## Add the PingOne for Enterprise IdP Connection to GitHub

1. Sign on to GitHub Enterprise Server as an administrator.

2. Click the **Rocket** icon.

3. Click **Management Console**.

   ![Screen capture of GitHub Site admin controls with Management console highlighted in red.](_images/iig1625256280294.png)

4. Click **Authentication**.

   ![Screen capture of GitHub Authentication option highlighted in red.](_images/ian1625256331790.png)

5. Click **SAML** and select the **idP initiated SSO (disables AuthnRequest)** check box.

   ![Screen capture of GitHub Authentication settings with SAML checked and idP initiated SSO highlighted in red.](_images/thh1625256392431.png)

6. In the **Single sign-on URL** field, enter `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=idpid-value-from-PingOne`.

   ![Screen capture of GitHub Single sign-on URL field highlighted in red.](_images/xge1625256484285.png)

7. In the **Issuer** field, enter the PingOne for Enterprise **Issuer** value.

   ![Screen capture of GitHub Issuer field highlighted in red.](_images/rfj1625256540616.png)

8. Click **Choose File** for the **Verification Certificate** and upload the PingOne signing certificate that you downloaded.

9. Click **Save Settings**.

## Test the PingOne for Enterprise IdP-initiated SSO integration

1. Go to your Ping desktop as a user with GitHub access.

   |   |                                                                                               |
   | - | --------------------------------------------------------------------------------------------- |
   |   | To find the Ping desktop URL in the Admin console, go to **Setup → Dock → PingOne Dock URL**. |

2. Complete the PingOne for Enterprise authentication.

   You're redirected to your GitHub server.

   ![Screen capture of sign on screen.](_images/llr1625256687377.png)

## Test the PingOne SP-initiated SSO integration

1. Go to your GitHub server.

2. After you're redirected to PingOne for Enterprise, enter your PingOne username and password.

   ![Screen capture of sign on screen.](_images/llr1625256687377.png)

   You're redirected back to GitHub.