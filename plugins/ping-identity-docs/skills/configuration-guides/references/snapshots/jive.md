---
title: Configuring SAML SSO with Jive and PingFederate
description: Learn how to configure SAML SSO with Jive and PingFederate.
component: configuration_guides
page_id: configuration_guides:jive:config_saml_jive_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/jive/config_saml_jive_pf.html
revdate: May 15, 2024
section_ids:
  about-this-task: About this task
  create-the-pingfederate-sp-connection-for-jive: Create the PingFederate SP Connection for Jive
  configure-the-pingfederate-idp-connection-for-jive: Configure the PingFederate IdP connection for Jive
---

# Configuring SAML SSO with Jive and PingFederate

Learn how to configure SAML SSO with Jive and PingFederate.

## About this task

The following table details the references that are used within this guide that are environment specific. Replace these with the suitable value for your environment.

| Reference      | Description                              |
| -------------- | ---------------------------------------- |
| *jiveinstance* | The host and port for the Jive instance. |

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | The following configuration is untested and is provided as an example. Additional steps might be required. |

## Create the PingFederate SP Connection for Jive

1. Sign on to the Jive Admin Console and enable single sign-on:

   1. Go to **People → Settings → Single Sign-On → SAML**.

   2. Check **Enabled**.

   3. Click **Save**.

   4. Restart Jive.

      |   |                                                                                                                                   |
      | - | --------------------------------------------------------------------------------------------------------------------------------- |
      |   | Until SAML configuration is complete, you'll need to sign on by going directly to the admin console, `http://jiveinstance/admin`. |

2. Download the Jive metadata from `http://jiveinstance/saml/metadata`.

3. Sign on to the PingFederate administrative console.

4. Using the metadata that you downloaded, create an SP connection in Ping Federate:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Enable the following **SAML Profiles**:

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   3. In **Assertion Creation: Attribute Contract**, set the **Subject Name Format** to `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified`.

   4. In the **Assertion Creation: Attribute Contract Fulfilment**, map the attribute **SAML\_SUBJECT** to the attribute `username`.

   5. Add any additional attributes required into the attribute contract and contract fulfillment.

   6. In **Protocol Settings: Allowable SAML Bindings**, enable **POST**, and **Redirect**.

5. Export the metadata for the newly-created SP connection.

6. Export the signing certificate public key.

## Configure the PingFederate IdP connection for Jive

1. Sign on to the Jive Admin Console and go to **People → Settings → Single Sign-On → SAML**.

2. On the **IdP Metadata** tab, copy the contents of the metadata file into the metadata field.

3. Click **Save All SAML Settings**.

4. On the **User Attribute Mapping** tab, map the user attributes in the Jive profile to the attributes that you configured in PingFederate.

5. **Optional:** Select **Group Mapping Enabled** if you want to assign users to groups with a group attribute passed in the assertion.

6. Click **Save Settings**.

---

---
title: Configuring SAML SSO with Jive and PingOne for Enterprise
description: Learn how to configure SAML SSO with Jive and PingOne for Enterprise.
component: configuration_guides
page_id: configuration_guides:jive:config_saml_jive_p14e
canonical_url: https://docs.pingidentity.com/configuration_guides/jive/config_saml_jive_p14e.html
revdate: December 7, 2021
section_ids:
  about-this-task: About this task
  create-a-pingone-for-enterprise-application-for-jive: Create a PingOne for Enterprise Application for Jive
  configure-the-pingone-for-enterprise-idp-connection-for-jive: Configure the PingOne for Enterprise IdP connection for Jive
---

# Configuring SAML SSO with Jive and PingOne for Enterprise

Learn how to configure SAML SSO with Jive and PingOne for Enterprise.

## About this task

The following table details the references that are used within this guide that are environment specific. Replace these with the suitable value for your environment.

| Reference      | Description                              |
| -------------- | ---------------------------------------- |
| *jiveinstance* | The host and port for the Jive instance. |

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | The following configuration is untested and is provided as an example. Additional steps might be required. |

## Create a PingOne for Enterprise Application for Jive

1. Sign on to the Jive Admin Console and enable single sign-on:

   1. Go to **People → Settings → Single Sign-On → SAML**.

   2. Check **Enabled**.

   3. Click **Save**.

   4. Restart Jive.

      |   |                                                                                                                                   |
      | - | --------------------------------------------------------------------------------------------------------------------------------- |
      |   | Until SAML configuration is complete, you'll need to sign on by going directly to the admin console, `http://jiveinstance/admin`. |

2. Download the Jive Metadata from `http://jiveinstance/saml/metadata`.

3. Sign on to PingOne for Enterprise and click **Applications**.

4. On the SAML tab, click **Add Application**.

   ![Screen capture of PingOne for Enterprise My Applications page with the Add Application drop down list selected.](_images/bxd1625246814612.png)

5. Click **Search Application Catalog** and search for `Jive`.

6. Click the **Jive - Production** row or click **Jive – UAT** for a non-production environment.

   ![Screen capture of PingOne for Enterprise Application Catalog with Jive - Production and Jive - UAT displayed as search results for "jive".](_images/pxb1625246939739.png)

7. Click **Setup**.

8. Select the appropriate signing certificate from the list.

9. Review the steps, and note the **PingOne for Enterprise SaaS ID**, **IdP ID**, **Single Sign-on URL**, and **Issuer** values.

10. Click **Continue to Next Step**.

11. On the **Upload Metadata** row, click **Select File**, and upload the Jive metadata file that you previously downloaded.

    ![Screen capture of PingOne for Enterprise Connection Configuration settings with the fields for ACS URL, Entity ID, and Primary Verification Certificate redacted.](_images/gjr1625247086269.png)

12. Click **Continue to Next Step**.

13. In the **Attribute Mapping** section, complete the attribute mappings as required.

    ![Screen capture of PingOne for Enterprise Attribute Mapping section with sAMAccountName, givenName, sn, mail, and objectGUID listed as application attributes.](_images/rlm1625247189643.png)

14. Click **Continue to Next Step**.

15. Update the **Name**, **Description**, and **Category** fields as required.

    ![Screen capture of PingOne for Enterprise App Customization settings for Jive - Production.](_images/fre1625247291926.png)

16. Click **Continue to Next Step**.

17. Add suitable user groups for the application.

    ![Screen capture of PingOne for Enterprise Application Group Access section.](_images/rqi1625247352076.png)

18. Click **Continue to Next Step**.

19. Review the settings.

    ![Screen capture of PingOne for Enterprise Review Setup section with all fields customized for the Jive - Production app.](_images/jvg1625247410226.png)

    ![Continuing from the last screen capture, the PingOne for Enterprise Review Setup section displaying SSO and SAML connection information as well as the Application Attribute table for review.](_images/bth1625247452899.png)

20. Copy the **Single Sign-On (SSO) URL** value to a temporary location.

    This is the IdP-initiated SSO URL that you can use for testing.

21. On the **Signing Certificate** row, click **Download**. You'll use this for the Jive configuration.

22. On the **SAML Metadata** row, click **Download**. You'll use this the Jive configuration.

23. Click **Finish**.

## Configure the PingOne for Enterprise IdP connection for Jive

1. Sign on to the Jive Admin Console and go to **People → Settings → Single Sign-On → SAML**.

2. On the **IdP Metadata** tab, copy the contents of the metadata file into the metadata field.

3. Click **Save All SAML Settings**.

4. On the **User Attribute Mapping** tab, map the user attributes in the Jive profile to the attributes configured in PingOne for Enterprise.

5. **Optional:** Select **Group Mapping Enabled** if you want to assign users to groups using a group attribute passed in the assertion.

6. Click **Save Settings**.