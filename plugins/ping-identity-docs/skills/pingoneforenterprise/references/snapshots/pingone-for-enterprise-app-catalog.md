---
title: Achievers Connection Configuration
description: Import the metadata for Achievers:
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_achievers_connection
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_achievers_connection.html
revdate: July 17, 2023
section_ids:
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps: Next steps
---

# Achievers Connection Configuration

## Steps

1. Import the metadata for Achievers:

   ### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** and **Entity ID** fields, replace the *${programName}* and *${serverName}* variables with the information provided by your client success manager.

3. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

4. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

5. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

6. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from Achiever.

7. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

8. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an activeSSO session.

9. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

10. On the **Signing** line:

    ### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

11. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

12. Select the **Use Custom URL** checkbox to enter a customer URL to launch Achievers from the dock.

## Next steps

Click **Continue to Next Step**.

---

---
title: Adding CylancePROTECT to Your PingOne for Enterprise Dock
description: Add the CylancePROTECT application your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_cylanceprotect
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_cylanceprotect.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  cylanceprotect-connection-configuration: CylancePROTECT Connection Configuration
  about-this-task: About this task
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  cylanceprotect-attribute-mapping: CylancePROTECT Attribute Mapping
  about-this-task-2: About this task
  steps-3: Steps
  choose-from-3: Choose from:
  next-steps-3: Next steps
  cylanceprotect-customization: CylancePROTECT Customization
  steps-4: Steps
  next-steps-4: Next steps
  cylanceprotect-group-access: CylancePROTECT Group Access
  about-this-task-3: About this task
  steps-5: Steps
  next-steps-5: Next steps
---

# Adding CylancePROTECT to Your PingOne for Enterprise Dock

Add the CylancePROTECT application your PingOne for Enterprise dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **CylancePROTECT** application line for your region to expand it and then click **Setup**.

4. On the **Signing Certificate** line, click **Download**.

5. In a separate tab or window, sign on to the CylancePROTECT console.

6. In CylancePROTECT, Go to **Settings > Application**.

7. From the **Provider** list, select **PingOne**.

8. Open the signing certificate file you downloaded in step 4 in a plain text editor.

9. Copy the contents of the signing certificate and, in CylancePROTECT, paste the contents into the **X.509 Certificate** field.

10. In the **Login URL** field, enter `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=<IdP ID>`, where *\<IdP ID>* is the value of the **IdP ID** line on the PingOne **SSO Instructions** tab.

## Next steps

In PingOne for Enterprise, click **Continue to Next Step**.

## CylancePROTECT Connection Configuration

### About this task

The pre-populated values for the **ACS URL**, **Entity ID**, and **Target Resource** fields will work for most configurations.

All other fields are optional.

### Steps

1. Import the metadata for CylancePROTECT:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** and **Entity ID** fields, replace the *${programName}* and *${serverName}* variables with the information provided by your client success manager.

3. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

4. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

5. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

6. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from CylancePROTECT.

7. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

8. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

9. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

10. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

11. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

12. Select the **Use Custom URL** checkbox to enter a customer URL to launch CylancePROTECT from the dock.

### Next steps

Click **Continue to Next Step**.

## CylancePROTECT Attribute Mapping

### About this task

PingOne will automatically populate the required SAML attributes.

For CylancePROTECT, the required attribute is `SAML_SUBJECT`, which you should map to `Email (Work)`.

### Steps

1. To add an additional optional attribute, click **Add new attribute**.

2. In the **Application Attribute** field, enter the attribute name as it appears in the application.

3. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   #### Choose from:

   * To map to the application attribute: Enter or select a directory attribute.

   * To assign to the application attribute: Select **As Literal**, then enter a literal value.

4. To create advanced attribute mappings, click **Advanced**.

   Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

### Next steps

Click **Continue to Next Step**.

## CylancePROTECT Customization

### Steps

* To change the application icon, click **Select image** and upload a local image file.

  The image file must be:

  * PNG, GIF, or JPG format

  * 312 x 52 pixels maximum

  * 2 MB maximum file size

    |   |                                                  |
    | - | ------------------------------------------------ |
    |   | Images are scaled to 64 x 64 pixels for display. |

* To change the name of the application displayed on the dock, in the **Name** field, enter a new name.

* To change the description of the application, in the **Description** field, enter the new description text.

* To change the category to which the application is assigned on the dock, in the **Category** list, select a category.

  Learn more in [Creating a custom application category](../pingone_for_enterprise/p14e_creating_custom_application_category.html).

### Next steps

Click **Continue to Next Step**.

## CylancePROTECT Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

On the **Review Setup** tab, review your configuration, and click **Finish** to add the application to your PingOne Dock.

---

---
title: Adding PagerDuty to Your PingOne for Enterprise Dock
description: Add the PagerDuty application your PingOne for Enterprise Dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_pagerduty
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_pagerduty.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  pagerduty-connection-configuration: PagerDuty Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  pagerduty-attribute-mapping: PagerDuty Attribute Mapping
  about-this-task: About this task
  steps-3: Steps
  choose-from-3: Choose from:
  next-steps-3: Next steps
  pagerduty-customization: PagerDuty Customization
  steps-4: Steps
  next-steps-4: Next steps
  pagerduty-group-access: PagerDuty Group Access
  about-this-task-2: About this task
  steps-5: Steps
  next-steps-5: Next steps
---

# Adding PagerDuty to Your PingOne for Enterprise Dock

Add the PagerDuty application your PingOne for Enterprise Dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **PagerDuty** application line to expand it and click **Setup**.

4. On the **SSO Instructions** tab, click **Download** to download the signing certificate.

5. In a separate tab or window, sign on to PagerDuty as the account owner.

6. In PagerDuty, go to **Account Settings > Single Sign-on**.

7. Enter the signing certificate:

   1. In a plain text editor, open the signing certificate you downloaded in step 4.

   2. Copy the contents of the certificate.

   3. In PagerDuty, in the **X.509 Certificate** field, paste the certificate contents, including the `Begin Certificate` and `End Certificate` lines.

8. In the **Login URL** field, enter `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=<IdP ID>`, replacing *\<IdP ID>* with the **IdP ID** value from PingOne for Enterprise.

9. Select the **Turn on single sign-on** checkbox.

10. Select the **Allow username/password login** checkbox.

    Enable this option while testing your single sign-on (SSO) connection. After a successful test, you can disable it.

11. Click **Save Changes**.

12. Sign out of PagerDuty.

13. On the PagerDuty sign on page, click **Sign in with your Identity Provider**.

## Next steps

In PingOne for Enterprise, click **Continue to Next Step**.

## PagerDuty Connection Configuration

### Steps

1. Import the metadata for PagerDuty:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** and **Entity ID** fields, replace *${accountid}* with your PagerDuty account ID.

3. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated SSO.

4. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

5. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

6. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from PagerDuty.

7. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

8. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

9. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

10. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

11. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

12. Select the **Use Custom URL** checkbox to enter a customer URL to launch PagerDuty from the dock.

### Next steps

Click **Continue to Next Step**.

## PagerDuty Attribute Mapping

### About this task

PingOne for Enterprise will automatically populate required SAML attributes.

For PagerDuty, the required attribute is `SAML_SUBJECT`.

### Steps

1. To add an additional optional attribute, click **Add new attribute**.

2. In the **Application Attribute** field, enter the attribute name as it appears in the application.

3. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   #### Choose from:

   * To map to the application attribute: Enter or select a directory attribute.

   * To assign to the application attribute: Select **As Literal**, then enter a literal value.

4. To create advanced attribute mappings, click **Advanced**.

   Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

### Next steps

Click **Continue to Next Step**.

## PagerDuty Customization

### Steps

* To change the application icon, click **Select image** and upload a local image file.

  The image file must be:

  * PNG, GIF, or JPG format

  * 312 x 52 pixels maximum

  * 2 MB maximum file size

    |   |                                                  |
    | - | ------------------------------------------------ |
    |   | Images are scaled to 64 x 64 pixels for display. |

* To change the name of the application displayed on the dock, in the **Name** field, enter a new name.

* To change the description of the application, in the **Description** field, enter the new description text.

* To change the category to which the application is assigned on the dock, in the **Category** list, select a category.

  Learn more in [Creating a custom application category](../pingone_for_enterprise/p14e_creating_custom_application_category.html).

### Next steps

Click **Continue to Next Step**.

## PagerDuty Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

On the **Review Setup** tab, review your configuration, and click **Finish** to add the application to your PingOne Dock.

---

---
title: Adding Salesforce to Your PingOne for Enterprise Dock
description: Add the Salesforce application your PingOne for Enterprise Dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_salesforce
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_salesforce.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  salesforce-connection-configuration: Salesforce Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  salesforce-provisioning: Salesforce Provisioning
  before-you-begin: Before you begin
  about-this-task: About this task
  steps-3: Steps
  choose-from-3: Choose from:
  example: Example:
  choose-from-4: Choose from:
  result: Result:
  next-steps-3: Next steps
  salesforce-attribute-mapping: Salesforce Attribute Mapping
  about-this-task-2: About this task
  steps-4: Steps
  choose-from-5: Choose from:
  next-steps-4: Next steps
  salesforce-customization: Salesforce Customization
  steps-5: Steps
  next-steps-5: Next steps
  salesforce-group-access: Salesforce Group Access
  about-this-task-3: About this task
  steps-6: Steps
  next-steps-6: Next steps
---

# Adding Salesforce to Your PingOne for Enterprise Dock

Add the Salesforce application your PingOne for Enterprise Dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Salesforce** application line to expand it, and then and click **Setup**.

4. On the **SSO Instructions** tab, click **Download** to download the signing certificate.

5. In a separate tab or window, sign on to the Salesforce admin portal.

6. In Salesforce, go to **Setup > Administer > Security Controls > Single Sign-On Settings**.

7. Select the **SAML Enabled** checkbox.

8. In the **Name** field, enter a name for the connection to PingOne.

9. In the **Issuer** field, enter the **Issuer** value from PingOne.

10. On the **Identity Provider Certificate** line, click **Browse** to upload the signing certificate you downloaded in step 4.

11. From the **SAML Identity Type** list, select **Assertion contains User's salesforce.com username**.

12. From the **SAML Identity Location** list, select **Identity is in the NameIdentifier element of the Subject Statement**.

13. In the **API Name** field, enter a unique name for the API.

14. In the **Entity ID** field, enter `https://saml.salesforce.com`

    If you have a Salesforce.com My Domain URL, you can enter it into this field instead.

15. **Optional:** In the **Identity Provier Login URL**, enter `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=<IdP ID>`, replacing *\<IdP ID>* with the **IdP ID** value from PingOne.

16. **Optional:** In the **Identity provider Logout URL** field, enter `https://sso.connect.pingidentity.com/sso/terminatesession.aspx?page=https://www.salesforce.com`.

17. **Optional:** In the **Custom Error URL**, enter a URL to redirect users to when an error occurs.

    If your identity bridge is AD Connect with IIS, you can enter `https://<AD Connect IIS Server URL>/ADconnect/error.aspx`.

18. Click **Save**.

    |   |                                                                                   |
    | - | --------------------------------------------------------------------------------- |
    |   | Keep the Salesforce tab open, as you will need values from it for the next steps. |

## Next steps

In PingOne for Enterprise, click **Continue to Next Step**.

## Salesforce Connection Configuration

### Steps

1. Import the metadata for Salesforce:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** field, enter the **Salesforce Login URL** value from Salesforce.

3. In the **Entity ID** field, enter the **Entity ID** value from Salesforce.

4. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

5. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

6. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

7. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from Salesforce.

8. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

9. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

10. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

11. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

12. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

13. Select the **Use Custom URL** checkbox to enter a customer URL to launch Salesforce from the dock.

14. Select the **Set Up Provisioning** checkbox to configure user provisioning to Salesforce.

### Next steps

Click **Continue to Next Step**.

## Salesforce Provisioning

### Before you begin

Ensure that popups are permitted in your browser.

### About this task

|   |                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------ |
|   | If you don't need to set up user provisioning, proceed to [Salesforce Attribute Mapping](p14eapps_salesforce_attributes.html). |

If you selected **Set Up Provisioning** on the **Connection configuration** tab:

### Steps

1. In PingOne, click **Continue to Next Step** to proceed to the **Application Configuration** tab.

2. Chose how Salesforce will deprovision:

   #### Choose from:

   * Select the **FREEZE\_USER\_FLAG** checkbox to freeze a deprovisioned user account.

   * Leave the checkbox clear to deactivate a deprovisioned user account.

3. In the **SUBDOMAIN** field, your Salesforce subdomain

   #### Example:

   If your Salesforce URL is `example.my.salesforce.com`, your subdomain is `example.my`.

4. From the **PERMISSION\_SET\_MANAGEMENT** list, select how to handle permission sets provisioned from PingOne to Salesforce:

   #### Choose from:

   * Select **Merge with permission sets in Salesforce** to add provisioned PingOne user permissions to existing permission sets in Salesforce.

   * Select **Overwrite permission sets in Salesforce** to overwrite permissions in Salesforce with the provisioned permissions from PingOne.

5. Click **Continue to Next Step**.

6. On the **Connection Configuration** tab, click **Activate**.

   #### Result:

   PingOne opens the Salesforce sign-on page in a pop-up window.

7. Sign on to Salesforce as an administrative user.

8. Click **Allow**.

### Next steps

In PingOne, click **Continue to Next Step**.

## Salesforce Attribute Mapping

### About this task

PingOne for Enterprise will automatically populate required SAML attributes.

For Salesforce, the required attribute is `SAML_SUBJECT`.

### Steps

1. To add an additional optional attribute, click **Add new attribute**.

2. In the **Application Attribute** field, enter the attribute name as it appears in the application.

3. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   #### Choose from:

   * To map to the application attribute: Enter or select a directory attribute.

   * To assign to the application attribute: Select **As Literal**, then enter a literal value.

4. To create advanced attribute mappings, click **Advanced**.

   Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

### Next steps

Click **Continue to Next Step**.

## Salesforce Customization

### Steps

* To change the application icon, click **Select image** and upload a local image file.

  The image file must be:

  * PNG, GIF, or JPG format

  * 312 x 52 pixels maximum

  * 2 MB maximum file size

    |   |                                                  |
    | - | ------------------------------------------------ |
    |   | Images are scaled to 64 x 64 pixels for display. |

* To change the name of the application displayed on the dock, in the **Name** field, enter a new name.

* To change the description of the application, in the **Description** field, enter the new description text.

* To change the category to which the application is assigned on the dock, in the **Category** list, select a category.

  Learn more in [Creating a custom application category](../pingone_for_enterprise/p14e_creating_custom_application_category.html).

### Next steps

Click **Continue to Next Step**.

## Salesforce Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

On the **Review Setup** tab, review your configuration, and click **Finish** to add the application to your PingOne Dock.

---

---
title: Adding ServiceNow to Your PingOne for Enterprise Dock
description: Add the ServiceNow application to your PingOne for Enterprise Dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_servicenow
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_servicenow.html
revdate: October 4, 2023
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  next-steps: Next steps
  servicenow-connection-configuration: ServiceNow Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  servicenow-provisioning: ServiceNow Provisioning
  before-you-begin-2: Before you begin
  about-this-task: About this task
  steps-3: Steps
  examplehttpsyourinstance-servicenow-com: Example:https://<yourinstance>.servicenow.com
  next-steps-3: Next steps
  servicenow-attribute-mapping: ServiceNow Attribute Mapping
  about-this-task-2: About this task
  steps-4: Steps
  choose-from-3: Choose from:
  next-steps-4: Next steps
  servicenow-customization: ServiceNow Customization
  steps-5: Steps
  next-steps-5: Next steps
  servicenow-group-access: ServiceNow Group Access
  about-this-task-3: About this task
  steps-6: Steps
  next-steps-6: Next steps
  servicenow-saml-connection: ServiceNow SAML Connection
  steps-7: Steps
---

# Adding ServiceNow to Your PingOne for Enterprise Dock

Add the ServiceNow application to your PingOne for Enterprise Dock from the application catalog.

## Before you begin

To configure single sign-on (SSO) for ServiceNow, you must have the SAML 2.0 Single Sign-On plugin installed in your ServiceNow account. If this plugin is not yet installed, contact ServiceNow customer support.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **ServiceNow** application line to expand it and click **Setup**.

4. In a separate tab or window, sign on to your ServiceNow account as an administrative user.

5. In ServiceNow, go to **SAML 2.0 Single Sign-On > Properties**.

6. On the **Enable External Authentication** line, click **Yes**.

7. In the **Identity Provider URL which will issue the SAML2 Security token with user info** field, enter the **Issuer** value from PingOne for Enterprise.

8. In the **The base URL to the Identity Provider's AuthnRequest service. The AuthnRequest will be posted to this URL as the SAMLRequest parameter** field, enter `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=<IdP ID>`, replacing *\<IdP ID>* with the **IdP ID** value from PingOne for Enterprise.

## Next steps

In PingOne for Enterprise, click **Continue to Next Step**.

## ServiceNow Connection Configuration

### Steps

1. Import the metadata for ServiceNow:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** field, enter the **The URL to the ServiceNow instance homepage** value from ServiceNow.

3. In the **Entity ID** field, enter the **The entity identification, or the issuer** value from ServiceNow.

4. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single SSO.

5. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

6. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

7. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from ServiceNow.

8. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

9. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

10. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

11. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

12. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

13. Select the **Use Custom URL** checkbox to enter a customer URL to launch ServiceNow from the dock.

14. Select the **Set Up Provisioning** checkbox to configure user provisioning to ServiceNow.

### Next steps

In PingOne, click **Continue to Next Step**.

## ServiceNow Provisioning

### Before you begin

Ensure that popups are permitted in your browser.

### About this task

|   |                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------ |
|   | If you don't need to set up user provisioning, proceed to [ServiceNow Attribute Mapping](p14eapps_servicenow_attributes.html). |

If you selected **Set Up Provisioning** on the **Connection configuration** tab:

### Steps

1. In PingOne, click**Continue to Next Step** to proceed to the **Application Configuration** tab.

2. Install the Ping Identity Provisioning Solution application.

   For more information, see [Adding the Ping Identity provisioning role in ServiceNow](https://docs.pingidentity.com/bundle/integrations/page/pzq1563995052451.html).

3. Create a provisioning user.

   Learn more in [Creating a provisioning user in ServiceNow](https://docs.pingidentity.com//integrations/servicenow/setup/pf_servicenow_connector_creating_a_provisioning_user_in_servicenow.html).

4. In PingOne, in the **Administrator\_Username** field, enter the username for the provisioning user.

5. In the **Administrator\_Password** field, enter the password for the provisioning user.

6. In the **ServiceNow\_URL** field, enter the full URL of your ServiceNow instance.

   #### Example:`https://<yourinstance>.servicenow.com`

### Next steps

Click **Continue to Next Step**.

## ServiceNow Attribute Mapping

### About this task

PingOne will automatically populate required SAML attributes.

For ServiceNow, the required attribute is `SAML_SUBJECT`.

If you enabled provisioning, the required provisioning attribute is `Username`. All other provisioning attributes are optional.

### Steps

1. To add an additional optional attribute, click **Add new attribute**.

2. In the **Application Attribute** field, enter the attribute name as it appears in the application.

3. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   #### Choose from:

   * To map to the application attribute: Enter or select a directory attribute.

   * To assign to the application attribute: Select **As Literal**, then enter a literal value.

4. To create advanced attribute mappings, click **Advanced**.

   Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

### Next steps

Click **Continue to Next Step**.

## ServiceNow Customization

### Steps

* To change the application icon, click **Select image** and upload a local image file.

  The image file must be:

  * PNG, GIF, or JPG format

  * 312 x 52 pixels maximum

  * 2 MB maximum file size

    |   |                                                  |
    | - | ------------------------------------------------ |
    |   | Images are scaled to 64 x 64 pixels for display. |

* To change the name of the application displayed on the dock, in the **Name** field, enter a new name.

* To change the description of the application, in the **Description** field, enter the new description text.

* To change the category to which the application is assigned on the dock, in the **Category** list, select a category.

  Learn more in [Creating a custom application category](../pingone_for_enterprise/p14e_creating_custom_application_category.html).

### Next steps

Click **Continue to Next Step**.

## ServiceNow Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

On the **Review Setup** tab, review your configuration, and click **Finish** to add the application to your PingOne Dock.

## ServiceNow SAML Connection

### Steps

1. On the **Review Setup** tab, go to the **SAML Metadata** line and click **Download** to download the PingOne metadata.

2. Click **Finish** to complete your configuration and add ServiceNow to your PingOne Dock.

3. In ServiceNow, go to **SAML 2.0 Single Sign-On > Certificate**.

4. In the **Name** field, enter or select **SAML 2.0**.

5. From the **Format** list, select **PEM**.

6. In a plain text editor, open the PingOne metadata file.

7. Copy the contents of the metadata file and paste them into the **PEM Certificate** field.

8. Click **Save**.

---

---
title: Adding ShareFile to Your PingOne for Enterprise Dock
description: Add the ShareFile application to your PingOne for Enterprise Dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_sharefile
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_sharefile.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  sharefile-connection-configuration: ShareFile Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  sharefile-attribute-mapping: ShareFile Attribute Mapping
  about-this-task: About this task
  steps-3: Steps
  choose-from-3: Choose from:
  next-steps-3: Next steps
  sharefile-customization: ShareFile Customization
  steps-4: Steps
  next-steps-4: Next steps
  sharefile-group-access: ShareFile Group Access
  about-this-task-2: About this task
  steps-5: Steps
  next-steps-5: Next steps
---

# Adding ShareFile to Your PingOne for Enterprise Dock

Add the ShareFile application to your PingOne for Enterprise Dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **ShareFile** application line to expand it and click **Setup**.

4. On the **SSO Instructions** tab, click **Download** to download the signing certificate.

5. In a separate tab or window, sign on to ShareFile as an administrative user.

6. In ShareFile, go to **Admin > Configure Single Sign-On**.

7. Select the **Enable SAML** checkbox.

8. In the **Your Issuer/Entity ID** field, enter the **Issuer** value from PingOne for Enterprise.

9. In the **Sharefile Issuer/Entity ID** field, enter `https//<subdomain>.sharefile.com/saml/info`, replacing *\<subdomain>* with your Sharefile subdomain.

10. In a plain text editor, open the signing certificate you downloaded in step 4.

11. Copy the contents of the certificate, and paste them into the **X.509 Certificate** field.

12. In the **Login URL** field, enter the **Initiate Single Sign-On URL** value from PingOne for Enterprise.

13. In the **Logout URL** field, enter a URL to redirect users to when they sign off from ShareFile.

    Consider the **PingOne Dock URL**, which you can find at **Setup > Dock**.

14. Click **Save**.

## Next steps

In PingOne for Enterprise, click **Continue to Next Step**.

## ShareFile Connection Configuration

### Steps

1. Import the metadata for ShareFile:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** and **Entity ID** fields, replace *${mydomain}* with your ShareFile subdomain.

3. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

4. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

5. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

6. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from ShareFile.

7. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

8. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

9. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

10. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

11. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

12. Select the **Use Custom URL** checkbox to enter a customer URL to launch ShareFile from the dock.

### Next steps

Click **Continue to Next Step**.

## ShareFile Attribute Mapping

### About this task

PingOne for Enterprise will automatically populate required SAML attributes.

For ShareFile, the required attribute is `SAML_SUBJECT`.

### Steps

1. To add an additional optional attribute, click **Add new attribute**.

2. In the **Application Attribute** field, enter the attribute name as it appears in the application.

3. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   #### Choose from:

   * To map to the application attribute: Enter or select a directory attribute.

   * To assign to the application attribute: Select **As Literal**, then enter a literal value.

4. To create advanced attribute mappings, click **Advanced**.

   Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

### Next steps

Click **Continue to Next Step**.

## ShareFile Customization

### Steps

* To change the application icon, click **Select image** and upload a local image file.

  The image file must be:

  * PNG, GIF, or JPG format

  * 312 x 52 pixels maximum

  * 2 MB maximum file size

    |   |                                                  |
    | - | ------------------------------------------------ |
    |   | Images are scaled to 64 x 64 pixels for display. |

* To change the name of the application displayed on the dock, in the **Name** field, enter a new name.

* To change the description of the application, in the **Description** field, enter the new description text.

* To change the category to which the application is assigned on the dock, in the **Category** list, select a category.

  Learn more in [Creating a custom application category](../pingone_for_enterprise/p14e_creating_custom_application_category.html).

### Next steps

Click **Continue to Next Step**.

## ShareFile Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

On the **Review Setup** tab, review your configuration, and click **Finish** to add the application to your PingOne Dock.

---

---
title: Adding Slack to Your PingOne for Enterprise Dock
description: Add the Slack application to your PingOne for Enterprise Dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_slack
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_slack.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  choose-from: Choose from:
  result: Result
  next-steps: Next steps
  slack-connection-configuration: Slack Connection Configuration
  steps-2: Steps
  choose-from-2: Choose from:
  choose-from-3: Choose from:
  next-steps-2: Next steps
  slack-provisioning: Slack Provisioning
  before-you-begin: Before you begin
  about-this-task: About this task
  steps-3: Steps
  result-2: Result:
  next-steps-3: Next steps
  slack-attribute-mapping: Slack Attribute Mapping
  about-this-task-2: About this task
  steps-4: Steps
  choose-from-4: Choose from:
  next-steps-4: Next steps
  slack-customization: Slack Customization
  steps-5: Steps
  next-steps-5: Next steps
  slack-group-access: Slack Group Access
  about-this-task-3: About this task
  steps-6: Steps
  next-steps-6: Next steps
---

# Adding Slack to Your PingOne for Enterprise Dock

Add the Slack application to your PingOne for Enterprise Dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Slack** application line to expand it, and then click **Setup**.

4. On the **SSO Instructions** tab, click **Download** to download the signing certificate.

5. In a separate tab or window, go to [slack.com/admin](https://www.slack.com/admin) and sign on to your Slack account as a team owner.

6. In Slack, go to **Menu > Authentication > SAML authentication > Configure**.

7. From the **SAML provider** list, select **Custom SAML 2.0**.

8. In the **SAML SSO URL** field, enter `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=<IdP ID>`, replacing *\<IdP ID>* with the **IdP ID** field from PingOne.

9. Enter the PingOne for Enterprise signing certificate:

   1. In a plain text editor, open the PingOne for Enterprise signing certificate you downloaded in step 4.

   2. Copy the contents of the certificate.

   3. In Slack, paste the copied certificate contents into the **X.509 Certificate** field.

10. On the **Settings** line, click the button to set single sign-on (SSO) requirements.

    ### Choose from:

    * **Required**

    * **Partially Required**

    * **Optional**

    If your users include restricted or single-channel guest accounts, select **Partially Required**.

11. Click **Save Configuration**.

## Result

Slack will send a confirmation email to all users, prompting them to connect their Slack accounts to their single sign-on (SSO) accounts. After they confirm, they will be able to SSO into Slack.

## Next steps

In PingOne, click **Continue to Next Step**.

## Slack Connection Configuration

### Steps

1. Import the metadata for Slack:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** field, replace the *${teamname}* variable with your Slack subdomain.

3. In the **Entity ID** field, enter the entity ID.

   The default value of `https://slack.com` should work for most configurations.

4. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated SSO.

5. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

6. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

7. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from Slack.

8. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

9. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

10. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

11. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

12. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

13. Select the **Use Custom URL** checkbox to enter a customer URL to launch Slack from the dock.

14. Select the **Set Up Provisioning** checkbox to configure user provisioning to Slack.

### Next steps

Click **Continue to Next Step**.

## Slack Provisioning

### Before you begin

Ensure that popups are permitted in your browser.

### About this task

|   |                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------- |
|   | If you don't need to set up user provisioning, proceed to [Slack Attribute Mapping](p14eapps_slack_attributes.html). |

If you selected **Set Up Provisioning** on the **Connection configuration** tab:

### Steps

1. In PingOne, click**Continue to Next Step**.

2. Click **Activate**.

   #### Result:

   The **Customer Log In** page appears in a pop-up window.

3. On the **Customer Log In**, page, enter your team name and sign on to the Slack admin console.

4. Click **Authorize**.

### Next steps

In PingOne, click **Continue to Next Step**.

## Slack Attribute Mapping

### About this task

PingOne will automatically populate required SAML attributes.

For Slack, the required attribute is `SAML_SUBJECT`. Map it to your email attribute. Click **Advanced** and from the **Name ID Format to send to SP** list, select **urn:oasis:names:tc:SAML:1.1:nameid-format:persistent**.

### Steps

1. To add an additional optional attribute, click **Add new attribute**.

2. In the **Application Attribute** field, enter the attribute name as it appears in the application.

3. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   #### Choose from:

   * To map to the application attribute: Enter or select a directory attribute.

   * To assign to the application attribute: Select **As Literal**, then enter a literal value.

4. To create advanced attribute mappings, click **Advanced**.

   Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

### Next steps

Click **Continue to Next Step**.

## Slack Customization

### Steps

* To change the application icon, click **Select image** and upload a local image file.

  The image file must be:

  * PNG, GIF, or JPG format

  * 312 x 52 pixels maximum

  * 2 MB maximum file size

    |   |                                                  |
    | - | ------------------------------------------------ |
    |   | Images are scaled to 64 x 64 pixels for display. |

* To change the name of the application displayed on the dock, in the **Name** field, enter a new name.

* To change the description of the application, in the **Description** field, enter the new description text.

* To change the category to which the application is assigned on the dock, in the **Category** list, select a category.

  Learn more in [Creating a custom application category](../pingone_for_enterprise/p14e_creating_custom_application_category.html).

### Next steps

Click **Continue to Next Step**.

## Slack Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

On the **Review Setup** tab, review your configuration, and click **Finish** to add the application to your PingOne Dock.

---

---
title: Adding Smartsheet to Your PingOne for Enterprise Dock
description: Add the Smartsheet application your PingOne for Enterprise Dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_smartsheet
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_smartsheet.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  smartsheet-connection-configuration: Smartsheet Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  smartsheet-attribute-mapping: Smartsheet Attribute Mapping
  about-this-task: About this task
  steps-3: Steps
  choose-from-3: Choose from:
  next-steps-3: Next steps
  smartsheet-customization: Smartsheet Customization
  steps-4: Steps
  next-steps-4: Next steps
  smartsheet-group-access: Smartsheet Group Access
  about-this-task-2: About this task
  steps-5: Steps
  next-steps-5: Next steps
  smartsheet-saml-connection: Smartsheet SAML Connection
  before-you-begin: Before you begin
  steps-6: Steps
  result: Result:
  result-2: Result:
---

# Adding Smartsheet to Your PingOne for Enterprise Dock

Add the Smartsheet application your PingOne for Enterprise Dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Smartsheet** application line to expand it, and then click **Setup**.

## Next steps

On the **SSO Instruction** tab, click **Continue to Next Step**.

## Smartsheet Connection Configuration

### Steps

1. Import the metadata for Smartsheet:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

   Find your Smartsheet metadata URL at [What You Need to Set Up Smartsheet with Your Identity Provider](https://help.smartsheet.com/articles/2476141-configure-saml-sso) in the Smartsheet documentation.

2. In the **ACS URL** field, enter the Smartsheet ACS URL.

   The pre-populated value for this field should work for most configurations.

3. In the **Entity ID** field, enter the Smartsheet entity ID.

   The pre-populated value for this field should work for most configurations.

4. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

5. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

6. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

7. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from Smartsheet.

8. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

9. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

10. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

11. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

12. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

13. Select the **Use Custom URL** checkbox to enter a customer URL to launch Smartsheet from the dock.

### Next steps

Click **Continue to Next Step**.

## Smartsheet Attribute Mapping

### About this task

PingOne will automatically populate required SAML attributes.

Smartsheet requires two attributes:

* `SAML_SUBJECT`. Map to an attribute that matches user email address. Click **Advanced** and from the **Name ID Format to send to SP** list, select **urn:oasis:names:tc:SAML:1.1:nameid-format:persistent**.

* `emailaddress`. Map to email. Click **Advanced** and in the **NameFormat** field, enter `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`.

### Steps

1. To add an additional optional attribute, click **Add new attribute**.

2. In the **Application Attribute** field, enter the attribute name as it appears in the application.

3. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   #### Choose from:

   * To map to the application attribute: Enter or select a directory attribute.

   * To assign to the application attribute: Select **As Literal**, then enter a literal value.

4. To create advanced attribute mappings, click **Advanced**.

   Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

### Next steps

Click **Continue to Next Step**.

## Smartsheet Customization

### Steps

* To change the application icon, click **Select image** and upload a local image file.

  The image file must be:

  * PNG, GIF, or JPG format

  * 312 x 52 pixels maximum

  * 2 MB maximum file size

    |   |                                                  |
    | - | ------------------------------------------------ |
    |   | Images are scaled to 64 x 64 pixels for display. |

* To change the name of the application displayed on the dock, in the **Name** field, enter a new name.

* To change the description of the application, in the **Description** field, enter the new description text.

* To change the category to which the application is assigned on the dock, in the **Category** list, select a category.

  Learn more in [Creating a custom application category](../pingone_for_enterprise/p14e_creating_custom_application_category.html).

### Next steps

Click **Continue to Next Step**.

## Smartsheet Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

Click **Continue to Next Step**.

## Smartsheet SAML Connection

### Before you begin

Ensure that your Smartsheet account is an enterprise account.

### Steps

1. On the **Review Setup** tab, go to the **SAML Metadata** line and click **Download** to download the PingOne metadata.

2. Click **Finish** to complete your configuration and add Smartsheet to your PingOne Dock.

3. In a separate tab or window, sign on to your Smartsheet account as an administrative user.

4. In Smartsheet, go to **Account > Account Admin > Security Controls**.

5. Under the **Authentication** heading, click **Edit**.

6. Click **Not Configured**.

   #### Result:

   Smartsheet opens the **SAML Administration** form.

7. Click **Add IdP**.

8. In the **IdP Nickname** field, enter a name for the connection.

9. Enter the PingOne metadata.

   1. In a plain text editor, open the PingOne metadata file you downloaded in step 1.

   2. Copy the contents of the file.

   3. In Smartsheet, paste the file contents into the **IdP Metadata** field.

10. Click **Save**.

11. Click **Activate**.

    #### Result:

    The **IdP Status** will change from **Inactive** to **Active, Default**

12. In the **Authentication** form, select the **SAML** checkbox to enable the SAML connection.

13. Click **Save**.

---

---
title: Adding SuccessFactors to Your PingOne for Enterprise Dock
description: Add the SuccessFactors application your PingOne for Enterprise Dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_successfactors
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_successfactors.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  successfactors-connection-configuration: SuccessFactors Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  successfactors-attribute-mapping: SuccessFactors Attribute Mapping
  about-this-task: About this task
  steps-3: Steps
  choose-from-3: Choose from:
  next-steps-3: Next steps
  successfactors-customization: SuccessFactors Customization
  steps-4: Steps
  next-steps-4: Next steps
  successfactors-group-access: SuccessFactors Group Access
  about-this-task-2: About this task
  steps-5: Steps
  next-steps-5: Next steps
---

# Adding SuccessFactors to Your PingOne for Enterprise Dock

Add the SuccessFactors application your PingOne for Enterprise Dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **SuccessFactors** application line to expand it, and then click **Setup**.

4. On the **SSO Instructions** tab, click **Download** to download the signing certificate.

5. Email your SuccessFactors representative requesting a single sign-on (SSO) connection. Include the following information in the email:

   * The **Issuer** value.

   * The SAML version you want to use. In most cases this is SAML 2.0.

   * The PingOne signing certificate you downloaded in step 4, attached to the email.

   In the email, request the following information from your SuccessFactors representative:

   * The assertion consumer service (ACS) URL

   * The target resource value

## Next steps

After your SuccessFactors representative replies with the requested information, click **Continue to Next Step**.

## SuccessFactors Connection Configuration

### Steps

1. Import the metadata for SuccessFactors:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** field, enter ACS URL value supplied by your SuccessFactors representative.

3. In the **Entity ID** field, enter the entity ID.

   The pre-populated value for this field should work for most configurations.

4. In the **Target Resource** field, enter the target resource value supplied by your SuccessFactors representative.

5. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

6. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

7. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from Achiever.

8. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

9. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

10. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

11. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

12. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

13. Select the **Use Custom URL** checkbox to enter a customer URL to launch SuccessFactors from the dock.

### Next steps

Click **Continue to Next Step**.

## SuccessFactors Attribute Mapping

### About this task

PingOne for Enterprise will automatically populate required SAML attributes.

For SuccessFactors, the required attribute is `SAML_SUBJECT`.

### Steps

1. To add an additional optional attribute, click **Add new attribute**.

2. In the **Application Attribute** field, enter the attribute name as it appears in the application.

3. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   #### Choose from:

   * To map to the application attribute: Enter or select a directory attribute.

   * To assign to the application attribute: Select **As Literal**, then enter a literal value.

4. To create advanced attribute mappings, click **Advanced**.

   Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

### Next steps

Click **Continue to Next Step**.

## SuccessFactors Customization

### Steps

* To change the application icon, click **Select image** and upload a local image file.

  The image file must be:

  * PNG, GIF, or JPG format

  * 312 x 52 pixels maximum

  * 2 MB maximum file size

    |   |                                                  |
    | - | ------------------------------------------------ |
    |   | Images are scaled to 64 x 64 pixels for display. |

* To change the name of the application displayed on the dock, in the **Name** field, enter a new name.

* To change the description of the application, in the **Description** field, enter the new description text.

* To change the category to which the application is assigned on the dock, in the **Category** list, select a category.

  Learn more in [Creating a custom application category](../pingone_for_enterprise/p14e_creating_custom_application_category.html).

### Next steps

Click **Continue to Next Step**.

## SuccessFactors Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

On the **Review Setup** tab, review your configuration, and click **Finish** to add the application to your PingOne Dock.

---

---
title: Adding Ultimate Software to Your PingOne for Enterprise Dock
description: Add UltiPro your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_ultimate_software
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_ultimate_software.html
revdate: August 5, 2024
section_ids:
  steps: Steps
  result: Result:
  next-steps: Next steps
  ultimate-software-connection-configuration: Ultimate Software Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  ultimate-software-provisioning: Ultimate Software Provisioning
  about-this-task: About this task
  steps-3: Steps
  next-steps-3: Next steps
  ultimate-software-attribute-mapping: Ultimate Software Attribute Mapping
  about-this-task-2: About this task
  steps-4: Steps
  choose-from-3: Choose from:
  next-steps-4: Next steps
  ultimate-software-customization: Ultimate Software Customization
  steps-5: Steps
  next-steps-5: Next steps
  ultimate-software-group-access: Ultimate Software Group Access
  about-this-task-3: About this task
  steps-6: Steps
  next-steps-6: Next steps
  ultimate-software-saml-connection: Ultimate Software SAML Connection
  steps-7: Steps
  result-2: Result:
---

# Adding Ultimate Software to Your PingOne for Enterprise Dock

Add UltiPro your PingOne for Enterprise dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Ultimate Software** application line to expand it , and then click **Setup**.

4. On the **SSO Instructions** tab, click **Download** to download the PingOne for Enterprise signing certificate.

5. Email <Setupmanagement@ultimatesoftware.com> with your company name to request a single sign-on (SSO) connection.

   ### Result:

   Ultimate Software will respond with the **ACS URL** and **Entity ID** values you will need in following steps.

## Next steps

In PingOne for Enterprise, click **Continue to Next Step**

## Ultimate Software Connection Configuration

### Steps

1. Import the metadata for Ultimate Software:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** and **Entity ID** fields, replace *$\\{ultipro provided host}* with the values supplied by your Ultimate Software representative.

3. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated SSO.

4. In the **Single Logout Endpoint** field, enter a URL for PingOne for Enterprise to send single logout (SLO) requests to.

5. In the **Single Logout Response Endpoint** field, enter a URL for PingOne for Enterprise to send SLO responses to.

6. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from Ultimate Software.

7. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

8. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

9. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

10. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne for Enterprise sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne for Enterprise sign responses to incoming SAML assertions.

11. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

12. Select the **Use Custom URL** checkbox to enter a customer URL to launch Achievers from the dock.

13. Select the **Set Up Provisioning** checkbox to configure user provisioning to Ultimate Software.

### Next steps

Click **Continue to Next Step**.

## Ultimate Software Provisioning

### About this task

|   |                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you don't need to set up user provisioning, proceed to [Ultimate Software Attribute Mapping](p14eapps_ultimate_software_attributes.html). |

If you selected **Set Up Provisioning** on the **Connection configuration** tab:

### Steps

1. Email your Ultimate Software representative and ask them to configure provisioning for your account.

2. After your representative confirms the provisioning configuration, click**Continue to Next Step**.

3. In a separate tab or window, sign on to your Ultimate Software account.

4. In Ultimate Software, go to **System Admin > Web Services**.

5. In PingOne, enter the following information:

   1. In the **Username** field, enter the username for your Ultimate Software account.

   2. In the **Password** and **Repeat Password** fields, enter your Ultimate Software account password.

   3. In the **User API Key**, **Client API Key**, and **Login Service Endpoint**, enter the corresponding values from the Ultimate Software **Web Services** page.

### Next steps

Click **Continue to Next Step**.

## Ultimate Software Attribute Mapping

### About this task

PingOne for Enterprise will automatically populate required SAML attributes.

For Ultimate Software, the required attribute is `SAML_SUBJECT`.

### Steps

1. To add an additional optional attribute, click **Add new attribute**.

2. In the **Application Attribute** field, enter the attribute name as it appears in the application.

3. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   #### Choose from:

   * To map to the application attribute: Enter or select a directory attribute.

   * To assign to the application attribute: Select **As Literal**, then enter a literal value.

4. To create advanced attribute mappings, click **Advanced**.

   Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

### Next steps

Click **Continue to Next Step**.

## Ultimate Software Customization

### Steps

* To change the application icon, click **Select image** and upload a local image file.

  The image file must be:

  * PNG, GIF, or JPG format

  * 312 x 52 pixels maximum

  * 2 MB maximum file size

    |   |                                                  |
    | - | ------------------------------------------------ |
    |   | Images are scaled to 64 x 64 pixels for display. |

* To change the name of the application displayed on the dock, in the **Name** field, enter a new name.

* To change the description of the application, in the **Description** field, enter the new description text.

* To change the category to which the application is assigned on the dock, in the **Category** list, select a category.

  Learn more in [Creating a custom application category](../pingone_for_enterprise/p14e_creating_custom_application_category.html).

### Next steps

Click **Continue to Next Step**.

## Ultimate Software Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

Click **Continue to Next Step**.

## Ultimate Software SAML Connection

### Steps

1. On the **Review Setup** tab, click **Download** to download the PingOne SAML metadata file.

2. Email your Ultimate Software representative with the following information:

   * The **IdP ID** value.

   * The PingOne SAML metadata file you downloaded in step 1, attached to the email.

     #### Result:

     Your Ultimate Software representative will respond with your SSO URL.

3. In PingOne, click **Finish** to add Ultimate Software to your PingOne Dock.

---

---
title: Adding WebEx to Your PingOne for Enterprise Dock
description: Add the WebEx application your PingOne for Enterprise Dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_webex
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_webex.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  webex-connection-configuration: WebEx Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  webex-provisioning: WebEx Provisioning
  about-this-task: About this task
  steps-3: Steps
  next-steps-3: Next steps
  webex-attribute-mapping: WebEx Attribute Mapping
  about-this-task-2: About this task
  steps-4: Steps
  choose-from-3: Choose from:
  next-steps-4: Next steps
  webex-customization: WebEx Customization
  steps-5: Steps
  next-steps-5: Next steps
  webex-group-access: WebEx Group Access
  about-this-task-3: About this task
  steps-6: Steps
  next-steps-6: Next steps
---

# Adding WebEx to Your PingOne for Enterprise Dock

Add the WebEx application your PingOne for Enterprise Dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **WebEx** application line to expand it, and then click **Setup**.

4. On the **SSO Instructions** tab, click **Download** to download the signing certificate.

5. In a separate tab or window, sign on to your WebEx account as an administrative user.

6. In WebEx, go to **Site Administration > SSO Configuration**.

7. Click **Organization Certificate Management** and upload the PingOne for Enterprise signing certificate you downloaded in step 4.

8. In the single sign-on (SSO) configuration form, enter the following information.

   | Field                                                 | Action                                                                                                                                                |
   | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Federation Protocol**                               | **SAML 2.0**                                                                                                                                          |
   | **WebEx SAML Issuer (SP ID)**                         | `https://webex.com`                                                                                                                                   |
   | **Issuer for SAML (IdP ID)**                          | Enter the **IdP ID** from PingOne                                                                                                                     |
   | **Customer SSO Service Login URL**                    | `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=<IdP ID>`, replacing *\<IdP ID>* with the **IdP ID** value from PingOne for Enterprise. |
   | **Default WebEx Target Page URL**                     | Leave blank                                                                                                                                           |
   | **Customer SSO Error URL**                            | Leave blank                                                                                                                                           |
   | **NameID Format**                                     | `Unspecified`                                                                                                                                         |
   | **AuthnContextClassRef**                              | `urn:oasis:names:tc:SAML:2.0:ac:classes:unspecified`                                                                                                  |
   | **SSO Profile**                                       | `SP Initiated`                                                                                                                                        |
   | **Single Logout**                                     | Leave checkbox clear                                                                                                                                  |
   | **AuthnRequest Signed**                               | Leave checkbox clear                                                                                                                                  |
   | **Auto Account Update**                               | Leave checkbox clear                                                                                                                                  |
   | **Remove uid Domain Suffix for Active Directory UPN** | Leave checkbox clear                                                                                                                                  |

## Next steps

In PingOne for Enterprise, click **Continue to Next Step**.

## WebEx Connection Configuration

### Steps

1. Import the metadata for WebEx:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** field, replace *${parameter}* with your WebEx subdomain.

3. In the **Entity ID** field, enter your entity ID.

   The pre-populated value for this field should work for most configurations.

4. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated SSO.

5. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

6. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

7. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from WebEx.

8. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

9. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

10. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

11. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

12. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

13. Select the **Use Custom URL** checkbox to enter a customer URL to launch WebEx from the dock.

14. Select the **Set Up Provisioning** checkbox to configure user provisioning to WebEx.

### Next steps

Click **Continue to Next Step**.

## WebEx Provisioning

### About this task

|   |                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------- |
|   | If you don't need to set up user provisioning, proceed to [WebEx Attribute Mapping](p14eapps_webex_attributes.html). |

If you selected **Set Up Provisioning** on the **Connection configuration** tab:

### Steps

1. In PingOne, click**Continue to Next Step**.

2. On the **Application Configuration** tab, enter the following information.

   1. In the **webexid** field, enter your WebEx administrator user name

   2. In the **password** field, enter the WebEx administrator user password.

   3. In the **siteName** field, enter your WebEx subdomain.

   4. **Optional:** In the **siteid** field, enter your WebEx **Account Site ID** value.

      You can find this value on the WebEx Administration Tool page.

   5. In the **partnerId** field, enter your WebEx **Account Partner ID** value.

   You can find this value on the WebEx Administration Tool page.

### Next steps

In PingOne, click **Continue to Next Step**.

## WebEx Attribute Mapping

### About this task

PingOne for Enterprise will automatically populate required SAML attributes.

For WebEx, the following attributes are required for SSO:

* `SAML_SUBJECT`. Map to the username attribute. Email address is preferred.

* `SAML_AUTHN_CTX`. Select the **As Literal** checkbox. Enter a value of `urn:oasis:names:tc:SAML:2.0:ac:classes:unspecified`.

If you enabled provisioning, the following provisioning attributes are required:

* `firstname`

* `lastname`

* `password`

* `email`

All other provisioning attributes are optional.

### Steps

1. To add an additional optional attribute, click **Add new attribute**.

2. In the **Application Attribute** field, enter the attribute name as it appears in the application.

3. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   #### Choose from:

   * To map to the application attribute: Enter or select a directory attribute.

   * To assign to the application attribute: Select **As Literal**, then enter a literal value.

4. To create advanced attribute mappings, click **Advanced**.

   Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

### Next steps

Click **Continue to Next Step**.

## WebEx Customization

### Steps

* To change the application icon, click **Select image** and upload a local image file.

  The image file must be:

  * PNG, GIF, or JPG format

  * 312 x 52 pixels maximum

  * 2 MB maximum file size

    |   |                                                  |
    | - | ------------------------------------------------ |
    |   | Images are scaled to 64 x 64 pixels for display. |

* To change the name of the application displayed on the dock, in the **Name** field, enter a new name.

* To change the description of the application, in the **Description** field, enter the new description text.

* To change the category to which the application is assigned on the dock, in the **Category** list, select a category.

  Learn more in [Creating a custom application category](../pingone_for_enterprise/p14e_creating_custom_application_category.html).

### Next steps

Click **Continue to Next Step**.

## WebEx Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

On the **Review Setup** tab, review your configuration, and click **Finish** to add the application to your PingOne Dock.

---

---
title: Adding Workday to Your PingOne for Enterprise Dock
description: Add the Workday application to your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_workday
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_workday.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  workday-connection-configuration: Workday Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  workday-attribute-mapping: Workday Attribute Mapping
  about-this-task: About this task
  steps-3: Steps
  choose-from-3: Choose from:
  next-steps-3: Next steps
  workday-customization: Workday Customization
  steps-4: Steps
  next-steps-4: Next steps
  workday-group-access: Workday Group Access
  about-this-task-2: About this task
  steps-5: Steps
  next-steps-5: Next steps
---

# Adding Workday to Your PingOne for Enterprise Dock

Add the Workday application to your PingOne for Enterprise dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Workday** application line to expand it, and then click **Setup**.

4. On the **SSO Instructions** tab, click **Download** to download the PingOne for Enterprise signing certificate.

5. Copy the **IdP ID** value.

6. Send an email to your Workday partner representative with the following information.

   | Property                   | Description                                                                                                                                                                                                                                                                                                                                                                               |
   | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Certificate                | Attach the signing certificate you downloaded in step 4.                                                                                                                                                                                                                                                                                                                                  |
   | Certificate validity range | The issued date and the expiration date of the certificate.                                                                                                                                                                                                                                                                                                                               |
   | Redirect URL               | Include the following URL with your PingOne for Enterprise account information filled in.`https://sso.connect.pingidentity.com/sso/sp/initsso?saasid=e003a904-a9d8-4d2e-a3e8-74dac7879938&idpid=<Enter idpid here>&appurl=https%3A%2F%2Fwww.myworkday.com%2<Enter Workday tenant here>%2Flogin.flex`&#xA;&#xA;The Redirect URL isn't required if you plan to use the Target Resource URL. |
   | Logout URL                 | Specify where to redirect users when they sign out of Workday.                                                                                                                                                                                                                                                                                                                            |
   | Identity Provider ID       | The **IdP ID** value from above.                                                                                                                                                                                                                                                                                                                                                          |

## Next steps

In PingOne for Enterprise, click **Continue to Next Step**.

## Workday Connection Configuration

### Steps

1. Import the metadata for Workday:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** field, replace the *${tenant}* variable with the your Workday account name.

3. Leave the default **Entity ID** value.

4. **Optional:** In the **Target Resource** field, replace the *${tenant}* variable with the your Workday account name.

   |   |                                                                                              |
   | - | -------------------------------------------------------------------------------------------- |
   |   | Enter this information only if you're using a target resource URL instead of a redirect URL. |

5. In the **Single Logout Endpoint** field, enter a URL for PingOne for Enterprise to send single logout (SLO) requests to.

6. In the **Single Logout Response Endpoint** field, enter a URL for PingOne for Enterprise to send SLO responses to.

7. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from Zendesk.

8. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

9. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

10. Select **Pass-Thru RequestedAuthnContext to IdP** if you want PingOne for Enterprise to pass the `RequestedAuthnContext` request to the IdP for your account.

    This option is available only if you upload a primary verification certificate.

11. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

12. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne for Enterprise sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne for Enterprise sign responses to incoming SAML assertions.

13. In the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

14. Select the **Use Custom URL** checkbox to enter a customer URL to launch Workday from the dock.

### Next steps

Click **Continue to Next Step**.

## Workday Attribute Mapping

### About this task

PingOne for Enterprise will automatically populate required SAML attributes.

For Workday, the required attribute is `SAML_SUBJECT`.

### Steps

1. To add an additional optional attribute, click **Add new attribute**.

2. In the **Application Attribute** field, enter the attribute name as it appears in the application.

3. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   #### Choose from:

   * To map to the application attribute: Enter or select a directory attribute.

   * To assign to the application attribute: Select **As Literal**, then enter a literal value.

4. To create advanced attribute mappings, click **Advanced**.

   Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

### Next steps

Click **Continue to Next Step**.

## Workday Customization

### Steps

* To change the application icon, click **Select image** and upload a local image file.

  The image file must be:

  * PNG, GIF, or JPG format

  * 312 x 52 pixels maximum

  * 2 MB maximum file size

    |   |                                                  |
    | - | ------------------------------------------------ |
    |   | Images are scaled to 64 x 64 pixels for display. |

* To change the name of the application displayed on the dock, in the **Name** field, enter a new name.

* To change the description of the application, in the **Description** field, enter the new description text.

* To change the category to which the application is assigned on the dock, in the **Category** list, select a category.

  Learn more in [Creating a custom application category](../pingone_for_enterprise/p14e_creating_custom_application_category.html).

### Next steps

Click **Continue to Next Step**.

## Workday Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

On the **Review Setup** tab, review your configuration, and click **Finish** to add the application to your PingOne for Enterprise dock.

---

---
title: Adding Workplace by Facebook to Your PingOne for Enterprise Dock
description: Add the Workplace by Facebook application your PingOne for Enterprise Dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_facebook
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_facebook.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  workplace-by-facebook-connection-configuration: Workplace by Facebook Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  workplace-by-facebook-attribute-mapping: Workplace by Facebook Attribute Mapping
  about-this-task: About this task
  steps-3: Steps
  choose-from-3: Choose from:
  next-steps-3: Next steps
  workplace-by-facebook-customization: Workplace by Facebook Customization
  steps-4: Steps
  next-steps-4: Next steps
  workplace-by-facebook-group-access: Workplace by Facebook Group Access
  about-this-task-2: About this task
  steps-5: Steps
  next-steps-5: Next steps
---

# Adding Workplace by Facebook to Your PingOne for Enterprise Dock

Add the Workplace by Facebook application your PingOne for Enterprise Dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Workplace by Facebook** application line to expand it and click **Setup**.

4. On the **Signing Certificate** line, click **Download**.

5. In a separate tab or window, sign on to Workplace by Facebook as an administrator.

6. From the dashboard, go to **Settings > SSO Settings**.

7. From the **Allow users to login via** list, select **SSO only**.

8. In the **SAML URL** field, enter `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=<IdP ID>`, where *\<IdP ID>* is the value of the **IdP ID** line on the PingOne for Enterprise **SSO Instructions** tab.

9. In the **SAML Issuer URI** field, enter the **Issuer** value from the PingOne for Enterprise **SSO Instructions** tab.

10. Using a text editor, open the PingOne for Enterprise signing certificate you downloaded in step 4.

11. Copy the contents of the certificate and paste them into the **SAML Certificate** field in Workplace by Facebook.

12. Click **Test SSO** to confirm that the SSO connection is successful.

13. Click **Save**.

## Next steps

In PingOne for Enterprise, click **Continue to Next Step**.

## Workplace by Facebook Connection Configuration

### Steps

1. Import the metadata for Workplace by Facebook:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** field, replace *${company\_subdomain}* with your company subdomain.

3. In the **Entity ID** field, replace *${companyid}* with your company ID.

4. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

5. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

6. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

7. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from Achiever.

8. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

9. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

10. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

11. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

12. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

13. Select the **Use Custom URL** checkbox to enter a customer URL to launch Workplace by Facebook from the dock.

### Next steps

Click **Continue to Next Step**.

## Workplace by Facebook Attribute Mapping

### About this task

PingOne for Enterprise will automatically populate required SAML attributes.

For Workplace by Facebook, the required attribute is `SAML_SUBJECT`. Map it to an attribute that matches the `userName` attribute. Click **Advanced** and from the **Name ID Format to send to SP** list, select **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

### Steps

1. To add an additional optional attribute, click **Add new attribute**.

2. In the **Application Attribute** field, enter the attribute name as it appears in the application.

3. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   #### Choose from:

   * To map to the application attribute: Enter or select a directory attribute.

   * To assign to the application attribute: Select **As Literal**, then enter a literal value.

4. To create advanced attribute mappings, click **Advanced**.

   Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

### Next steps

Click **Continue to Next Step**.

## Workplace by Facebook Customization

### Steps

* To change the application icon, click **Select image** and upload a local image file.

  The image file must be:

  * PNG, GIF, or JPG format

  * 312 x 52 pixels maximum

  * 2 MB maximum file size

    |   |                                                  |
    | - | ------------------------------------------------ |
    |   | Images are scaled to 64 x 64 pixels for display. |

* To change the name of the application displayed on the dock, in the **Name** field, enter a new name.

* To change the description of the application, in the **Description** field, enter the new description text.

* To change the category to which the application is assigned on the dock, in the **Category** list, select a category.

  Learn more in [Creating a custom application category](../pingone_for_enterprise/p14e_creating_custom_application_category.html).

### Next steps

Click **Continue to Next Step**.

## Workplace by Facebook Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

On the **Review Setup** tab, review your configuration, and click **Finish** to add the application to your PingOne Dock.

---

---
title: Adding Zendesk to Your PingOne for Enterprise Dock
description: Add the Zendesk application to your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_zendesk
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_zendesk.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  zendesk-connection-configuration: Zendesk Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  zendesk-attribute-mapping: Zendesk Attribute Mapping
  about-this-task: About this task
  steps-3: Steps
  choose-from-3: Choose from:
  next-steps-3: Next steps
  zendesk-customization: Zendesk Customization
  steps-4: Steps
  next-steps-4: Next steps
  zendesk-group-access: Zendesk Group Access
  about-this-task-2: About this task
  steps-5: Steps
  next-steps-5: Next steps
---

# Adding Zendesk to Your PingOne for Enterprise Dock

Add the Zendesk application to your PingOne for Enterprise dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Zendesk** application line to expand it, and then click **Setup**.

4. On the **SSO Instructions** tab, click **Download** to download the PingOne for Enterprise signing certificate.

5. In the Zendesk admin console, click the **Zendesk Products** icon, then click **Admin Center**.

6. Click the **Security** icon, then click the **Single sign-on** tab.

7. Click **Configure**.

8. In the single sign-on (SSO) configuration form, enter the following information.

   | Field                                  | Action                                                                                                                                                                                                                                                                                                            |
   | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **SAML SSO URL** (Required)            | `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=<your IdP ID value>`                                                                                                                                                                                                                                |
   | **Certificate fingerprint** (Required) | Enter the certificate fingerprint for your signing certificate.&#xA;&#xA;To obtain the certificate fingerprint, in PingOne for Enterprise, go to Setup > Certificates, and expand the line for your signing certificate. PingOne for Enterprise displays both the SHA1 Fingerprint and SHA256 Fingerprint values. |
   | **Remote logout URL** (Optional)       | `https://sso.connect.pingidentity.com/sso/terminatesession?page=https://<URL to redirect users to>`                                                                                                                                                                                                               |
   | **IP Ranges** (Optional)               | Enter a range of IP addresses to restrict SSO to those locations. Users requesting sign on from outside those locations will be redirected to the Zendesk sign-on page.Leave this field blank to allow SSO from any location.                                                                                     |

9. Click **Enabled**

10. Click **Save**.

## Next steps

In PingOne for Enterprise, click **Continue to Next Step**.

## Zendesk Connection Configuration

### Steps

1. Import the metadata for Zendesk:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** and **Entity ID** fields, replace the *${accountname}* variables with the your Zendesk account name.

3. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

4. In the **Single Logout Endpoint** field, enter a URL for PingOne for Enterprise to send single logout (SLO) requests to.

5. In the **Single Logout Response Endpoint** field, enter a URL for PingOne for Enterprise to send SLO responses to.

6. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from Zendesk.

7. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

8. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

9. Select **Pass-Thru RequestedAuthnContext to IdP** if you want PingOne for Enterprise to pass the `RequestedAuthnContext` request to the IdP for your account.

   This option is available only if you upload a primary verification certificate.

10. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

11. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne for Enterprise sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne for Enterprise sign responses to incoming SAML assertions.

12. In the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

13. Select the **Use Custom URL** checkbox to enter a customer URL to launch Zendesk from the dock.

### Next steps

Click **Continue to Next Step**.

## Zendesk Attribute Mapping

### About this task

PingOne for Enterprise will automatically populate required SAML attributes.

For Zendesk, the required attribute is `SAML_SUBJECT`.

### Steps

1. To add an additional optional attribute, click **Add new attribute**.

2. In the **Application Attribute** field, enter the attribute name as it appears in the application.

3. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   #### Choose from:

   * To map to the application attribute: Enter or select a directory attribute.

   * To assign to the application attribute: Select **As Literal**, then enter a literal value.

4. To create advanced attribute mappings, click **Advanced**.

   Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

### Next steps

Click **Continue to Next Step**.

## Zendesk Customization

### Steps

* To change the application icon, click **Select image** and upload a local image file.

  The image file must be:

  * PNG, GIF, or JPG format

  * 312 x 52 pixels maximum

  * 2 MB maximum file size

    |   |                                                  |
    | - | ------------------------------------------------ |
    |   | Images are scaled to 64 x 64 pixels for display. |

* To change the name of the application displayed on the dock, in the **Name** field, enter a new name.

* To change the description of the application, in the **Description** field, enter the new description text.

* To change the category to which the application is assigned on the dock, in the **Category** list, select a category.

  Learn more in [Creating a custom application category](../pingone_for_enterprise/p14e_creating_custom_application_category.html).

### Next steps

Click **Continue to Next Step**.

## Zendesk Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

On the **Review Setup** tab, review your configuration, and click **Finish** to add the application to your PingOne for Enterprise dock.

---

---
title: Adding Zoom to Your PingOne for Enterprise Dock
description: Add the Zoom application to your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_zoom
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_zoom.html
revdate: October 4, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
  zoom-connection-configuration: Zoom Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  zoom-provisioning: Zoom Provisioning
  about-this-task-2: About this task
  steps-3: Steps
  zoom-attribute-mapping: Zoom Attribute Mapping
  about-this-task-3: About this task
  steps-4: Steps
  choose-from-3: Choose from:
  next-steps-3: Next steps
  zoom-customization: Zoom Customization
  steps-5: Steps
  next-steps-4: Next steps
  zoom-group-access: Zoom Group Access
  about-this-task-4: About this task
  steps-6: Steps
  next-steps-5: Next steps
  zoom-saml-connection: Zoom SAML Connection
  steps-7: Steps
  examplehttpssso-connect-pingidentity-comssoidpsso-saml2idpididpid-value: Example:https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=<idpid value>
---

# Adding Zoom to Your PingOne for Enterprise Dock

Add the Zoom application to your PingOne for Enterprise dock from the application catalog.

## About this task

|   |                                                                                        |
| - | -------------------------------------------------------------------------------------- |
|   | Single sign-on (SSO) is only available to paid business and educational Zoom accounts. |

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Zoom** application line to expand it and click **Setup**.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | As of June 2023, Zoom no longer allows the creation of new JSON Web Token (JWT) *(tooltip: \<div class="paragraph">&#xA;\<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>&#xA;\</div>)* applications.If you want to enable user provisioning for Zoom, select the **Zoom - OAuth** application in the PingOne for Enterprise Application Catalog.Learn more in [JWT App Type Deprecation](https://developers.zoom.us/changelog/platform/jwt-app-type-deprecation/) in the Zoom documentation. |

4. In a separate tab, go to <https://www.zoom.us/signin> and sign on to your account as an administrative user.

5. In the Zoom admin console, click **Single Sign-On**.

6. On the **Vanity URL** line, click **Apply**.

7. In the **Vanity URL** field, enter a vanity URL for your organization and click **Apply**.

   For more information, see [Guidelines for Vanity URL requests](https://support.zoom.us/hc/en-us/articles/215062646-Guidelines-for-Vanity-URL-Requests) in the Zoom documentation.

   |   |                                                              |
   | - | ------------------------------------------------------------ |
   |   | Zoom takes 1-2 business days to process vanity URL requests. |

## Next steps

After Zoom approves your vanity URL request, return to the Zoom app catalog application and click **Continue to Next Step**.

## Zoom Connection Configuration

### Steps

1. Import the metadata for Zoom:

   #### Choose from:

   * To upload the metadata file: Click **Select File**.

   * To enter the URL of the metadata: Click **Or use URL**.

     |   |                                                                                                                                                                                                                                                                                                         |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you upload a metadata file, the **Entity ID** field is automatically populated to include the `https` prefix. Leaving this prefix intact can cause configuration errors.After you upload the metadata file, you should verify that the **Entity ID** value is in the format `<vanity name>.zoom.us`. |

2. **Required:** In the **ACS URL** and **Entity ID** fields, replace the *${vanity}* variables with your Zoom vanity URL.

3. In the **Target Resource** field, enter a URL to redirect the user to after identity provider (IdP)-initiated SSO.

4. In the **Single Logout Endpoint** field, enter a URL for PingOne for Enterprise to send single logout (SLO) requests to.

   |   |                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you enter a value in the **Single Logout Endpoint** field, it should be in the format `https://<vanity name>.zoom.us/saml/SingleLogout`. |

5. In the **Single Logout Response Endpoint** field, enter a URL for PingOne for Enterprise to send SLO responses to.

   |   |                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Using the https\://*\<your vanity URL>*.zoom.us/saml/singlelogout SLO endpoint for both **Single Logout Endpoint** and **Single Logout Response Endpoint** improves your security by ending the user session in the application when the user's SSO session ends. |

6. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from Zoom.

7. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

8. To require your identity bridge to re-authenticate users with an active SSO session, select the **Force Re-authentication** checkbox .

9. If you want PingOne for Enterprise to pass the `RequestedAuthnContext` request to the IdP for your account, select **Pass-Thru RequestedAuthnContext to IdP**.

   |   |                                                                                 |
   | - | ------------------------------------------------------------------------------- |
   |   | This option is available only if you upload a primary verification certificate. |

10. To encrypt outgoing SAML assertions, select the **Encrypt Assertion** checkbox.

11. On the **Signing** line:

    #### Choose from:

    * To have PingOne for Enterprise sign outgoing SAML assertions: Click **Sign Assertion**. This is the default option.

    * To have PingOne for Enterprise sign responses to incoming SAML assertions: Click **Sign Response**.

12. In the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

13. To enter a custom URL to launch Zoom from the dock, select the **Use Custom URL** checkbox.

14. To enable user provisioning, select the **Set Up Provisioning** checkbox.

### Next steps

Click **Continue to Next Step**.

## Zoom Provisioning

### About this task

|   |                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------ |
|   | If you don't need to set up user provisioning, proceed to [Zoom Attribute Mapping](p14eapps_zoom_attributes.html). |

### Steps

1. Sign on to the [Zoom App Marketplace](https://marketplace.zoom.us/) as an administrator.

2. Click **Develop > Build App**.

3. On the **Choose your app type** page, in the **Server-to-Server OAuth** tile, click **Create**.

4. In the **App Name** field, enter a name for your application and click **Create**.

5. On the **App credentials** tab, copy the **Account ID**, **Client ID**, and **Client Secret** values, then click **Continue**.

You will enter these values into PingOne for Enterprise later.

1. On the **Information** tab, complete the following information:

   1. In the **Short description** field, enter a description for the application.

   2. In the **Company Name** field, enter the name of your organization.

   3. In the **Name**, enter the name of the contact for your Zoom account administrator.

   4. In the **Email address** field, enter to company email address of your Zoom account administrator.

      |   |                                                                               |
      | - | ----------------------------------------------------------------------------- |
      |   | The information on this tab is required for you to activate your application. |

2. On the **Features** tab, click **Continue**.

3. On the **Scopes** tab:

   1. Click **Add Scopes**.

   2. On the **Add Scopes** dialog, select the checkboxes to add the following scopes:

      * **User**

        * **View and manage sub account's user information** (user:master)

        * **View all user information** (user:read:admin)

        * **View users information and manage users** (user:write:admin)

      * **Account**

        * **View and manage sub accounts** (account:master)

        * **View account info** (account:read:admin)

        * **View and manage account info** (account:write:admin)

      * **SCIM2**

        * **Call Zoom SCIM2 API** (scim2)

   3. Click **Done** to add the selected scopes.

4. On the **Activation** tab, click **Activate**.

5. In PingOne for Enterprise, click **Continue to Next Step** until you see the **Application Configuration** tab.

6. On the **Application Configuration** tab, configure your Zoom connection.

   1. Review the values for the **SCIM\_URL** and **OAUTH\_TOKEN\_URL** fields, and change if necessary.

      |   |                                                  |
      | - | ------------------------------------------------ |
      |   | The default values will work for most customers. |

   2. In the **OAUTH\_ACCOUNT\_ID** field, enter your Zoom account ID.

   3. In the **OAUTH\_CLIENT\_ID** field, enter your Zoom client ID

   4. In the **OAUTH\_CLIENT\_SECRET** field, enter your Zoom client secret.

   5. From the **REMOVE\_ACTION** list, select one of the following options:

      * If you select **Disable**, a user you disable or delete in PingOne for Enterprise will be disabled in Zoom.

      * If you select **Delete**, a user you disable or delete in PingOne for Enterprise will be deleted in Zoom.

   6. Click **Continue to Next Step**.

## Zoom Attribute Mapping

### About this task

PingOne for Enterprise automatically populates required SAML attributes.

For Zoom, the required attribute is `SAML_SUBJECT`. Map this to the attribute of the user's email address, usually `SAML_SUBJECT` or `email`.

### Steps

1. To add an additional optional attribute, click **Add new attribute**.

2. In the **Application Attribute** field, enter the attribute name as it appears in the application.

3. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   #### Choose from:

   * To map to the application attribute: Enter or select a directory attribute.

   * To assign to the application attribute: Select **As Literal**, then enter a literal value.

4. To create advanced attribute mappings, click **Advanced**.

   Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

### Next steps

Click **Continue to Next Step**.

## Zoom Customization

### Steps

* To change the application icon, click **Select image** and upload a local image file.

  The image file must be:

  * PNG, GIF, or JPG format

  * 312 x 52 pixels maximum

  * 2 MB maximum file size

    |   |                                                  |
    | - | ------------------------------------------------ |
    |   | Images are scaled to 64 x 64 pixels for display. |

* To change the name of the application displayed on the dock, in the **Name** field, enter a new name.

* To change the description of the application, in the **Description** field, enter the new description text.

* To change the category to which the application is assigned on the dock, in the **Category** list, select a category.

  Learn more in [Creating a custom application category](../pingone_for_enterprise/p14e_creating_custom_application_category.html).

### Next steps

Click **Continue to Next Step**.

## Zoom Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

On the **Review Setup** tab, review your configuration, and click **Finish** to add the application to your PingOne for Enterprise Dock.

## Zoom SAML Connection

### Steps

1. On the **Review Setup** tab:

   1. On the **Signing Certificate** line, click **Download** to download the signing certificate.

   2. On the **SAML Metadata** line, click **Download** to download the metadata file.

2. In a separate tab, sign on to the Zoom admin console and go to the **Single Sign-On** tab.

3. In Zoom, set the **Sign-in Page URL** value:

   1. Open the metadata file in a text editor.

   2. Copy the `SingleSignOnService` `Location` value.

      #### Example:`https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=<idpid value>`

   3. In the Zoom admin console, paste the `Location` value into the **Sign-in Page URL** field.

4. **Optional:** In the **Sign-Out page URL** field, enter `https://<vanity name>.zoom.us/saml/SingleLogout`.

   |   |                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------- |
   |   | An SLO URL improves security by ending a user session in Zoom when the user's SSO session ends. |

5. In the **Service Provider (SP) Entity ID** list, select the non-HTTPS option.

6. In the **Enter Issuer** field, paste the *entityID* value from the metadata file.

7. Enter the **Identity provider certificate** value:

   1. Open the signing certificate file in a text editor.

   2. Copy the contents of the signing certificate file, excluding the `BEGIN CERTIFICATE` and `END CERTIFICATE` lines.

   3. In the Zoom admin console, paste the certificate contents into the **Identity provider certificate** field.

8. On the **Binding** line, click either **HTTP-POST** or **HTTP-Redirect**.

   |   |                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------ |
   |   | **HTTP-POST** is the more secure option, because it doesn't expose the SAML token as a query parameter in the URL. |

9. On the **Signature Hash Algorithm** line, click **SHA-256**.

10. On the **Security** line, select the checkboxes of the security policies to implement.

    |   |                                                                                                           |
    | - | --------------------------------------------------------------------------------------------------------- |
    |   | Improve your security by selecting **Sign SAML request** and **Save SAML response logs on user sign-in**. |

11. Click **Save Changes**.

---

---
title: ADP Workforce Now Attribute Mapping
description: PingOne will automatically add required SAML attributes.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_adp_workforce_attributes
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_adp_workforce_attributes.html
revdate: July 17, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  next-steps: Next steps
---

# ADP Workforce Now Attribute Mapping

## About this task

PingOne will automatically add required SAML attributes.

For ADP Workforce Now, the required attributes are:

* `SAML_SUBJECT`. The identity bridge attribute is mapped by default.

* `PersonImmutableID`. Map the identity bridge attribute representing your employee ID.

## Steps

1. To add an additional optional attribute, click **Add new attribute**.

2. In the **Application Attribute** field, enter the attribute name as it appears in the application.

3. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   ### Choose from:

   * To map to the application attribute: Enter or select a directory attribute.

   * To assign to the application attribute: Select **As Literal**, then enter a literal value.

4. To create advanced attribute mappings, click **Advanced**.

   Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

## Next steps

Click **Continue to Next Step**.

---

---
title: ADP Workforce Now Connection Configuration
description: In the ACS URL field, enter the assertion consumer service (ACS) URL.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_adp_workforce_connection
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_adp_workforce_connection.html
revdate: July 17, 2023
section_ids:
  steps: Steps
  choose-from: Choose from:
  next-steps: Next steps
---

# ADP Workforce Now Connection Configuration

## Steps

1. In the **ACS URL** field, enter the assertion consumer service (ACS) URL.

   |   |                                                                                               |
   | - | --------------------------------------------------------------------------------------------- |
   |   | The default ACS URL is pre-populated, and should work for most ADP Workforce Now connections. |

2. In the **Entity ID** field, enter the Entity ID.

   The default Entity ID is pre-populated, and should work for most ADP Workforce Now connections.

3. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

   The default URL is pre-populated, and should work for most ADP Workforce Now connections.

4. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

5. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

6. On the **Primary Verification Certificate** line, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses.

7. On the **Secondary Verification Certificate** line, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

8. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

9. Select the **Encrypt Assertion** box to encrypt outgoing SAML assertions.

10. On the **Signing** line:

    ### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

11. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

12. Select the **Use Custom URL**checkbox to enter a customer URL to launch ADP Workforce Now from the dock.

## Next steps

Click **Continue to Next Step**.

---

---
title: ADP Workforce Now Customization
description: To change the application icon, click Select image and upload a local image file.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_adp_workforce_customization
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_adp_workforce_customization.html
revdate: July 17, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
---

# ADP Workforce Now Customization

## Steps

* To change the application icon, click **Select image** and upload a local image file.

  The image file must be:

  * PNG, GIF, or JPG format

  * 312 x 52 pixels maximum

  * 2 MB maximum file size

    |   |                                                  |
    | - | ------------------------------------------------ |
    |   | Images are scaled to 64 x 64 pixels for display. |

* To change the name of the application displayed on the dock, in the **Name** field, enter a new name.

* To change the description of the application, in the **Description** field, enter the new description text.

* To change the category to which the application is assigned on the dock, in the **Category** list, select a category.

  Learn more in [Creating a custom application category](../pingone_for_enterprise/p14e_creating_custom_application_category.html).

## Next steps

Click **Continue to Next Step**.

---

---
title: ADP Workforce Now Group Access
description: The Group Access tab shows every user group that you have created.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_adp_workforce_groups
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_adp_workforce_groups.html
revdate: July 17, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# ADP Workforce Now Group Access

## About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

## Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

---

---
title: ADP Workforce Now SAML Connection
description: On the Review Setup tab, go to the SAML Metadata line and click Download to download the PingOne metadata.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_adp_workforce_saml
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_adp_workforce_saml.html
revdate: July 17, 2023
section_ids:
  steps: Steps
---

# ADP Workforce Now SAML Connection

## Steps

1. On the **Review Setup** tab, go to the **SAML Metadata** line and click **Download** to download the PingOne metadata.

2. Click **Finish** to complete your configuration and add ADP Workforce Now to your PingOne Dock.

3. Go to <https://adpfedsso.adp.com> and sign on using your ADP account credentials.

4. Follow the steps on the ADP site to upload the metadata file.

5. After your metadata has been uploaded, your ADP account representative will confirm that the setup is complete in the live environment and to advise on next steps.