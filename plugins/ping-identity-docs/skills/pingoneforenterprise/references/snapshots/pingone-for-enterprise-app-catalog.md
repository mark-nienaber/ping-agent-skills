---
title: Achievers Attribute Mapping
description: PingOne will automatically populate required SAML attributes.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_achievers_attribute
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_achievers_attribute.html
revdate: July 17, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  next-steps: Next steps
---

# Achievers Attribute Mapping

## About this task

PingOne will automatically populate required SAML attributes.

For Achievers, the required attribute is `SAML_SUBJECT`.

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
title: Achievers Customization
description: To change the application icon, click Select image and upload a local image file.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_achievers_customization
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_achievers_customization.html
revdate: July 17, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Achievers Customization

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
title: Achievers Group Access
description: The Group Access tab shows every user group that you have created.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_achievers_groups
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_achievers_groups.html
revdate: July 17, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Achievers Group Access

## About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

## Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

## Next steps

On the **Review Setup** tab, review your configuration, and click **Finish** to add the application to your PingOne Dock.

---

---
title: Adding Achievers to Your PingOne for Enterprise Dock
description: Add the Achievers application your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_achievers
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_achievers.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  achievers-connection-configuration: Achievers Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  achievers-attribute-mapping: Achievers Attribute Mapping
  about-this-task: About this task
  steps-3: Steps
  choose-from-3: Choose from:
  next-steps-3: Next steps
  achievers-customization: Achievers Customization
  steps-4: Steps
  next-steps-4: Next steps
  achievers-group-access: Achievers Group Access
  about-this-task-2: About this task
  steps-5: Steps
  next-steps-5: Next steps
---

# Adding Achievers to Your PingOne for Enterprise Dock

Add the Achievers application your PingOne for Enterprise dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Achievers** application line to expand it and click **Setup**.

4. On the **SSO Instructions** tab, click **Download** to download the signing certificate.

5. Send an email to your Achievers client success manager with the following information:

   * The signing certificate file you downloaded in step 2, attached to the email.

   * The entity ID, which is the **Issuer** URL.

   * The sign-on page URL, which is <https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=>*\<your IdP ID>*, where *\<your Idp ID>* is your **IdP ID** number.

## Next steps

After your client success manager responds with the necessary information, click **Continue to Next Step**.

## Achievers Connection Configuration

### Steps

1. Import the metadata for Achievers:

   #### Choose from:

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

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

11. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

12. Select the **Use Custom URL** checkbox to enter a customer URL to launch Achievers from the dock.

### Next steps

Click **Continue to Next Step**.

## Achievers Attribute Mapping

### About this task

PingOne will automatically populate required SAML attributes.

For Achievers, the required attribute is `SAML_SUBJECT`.

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

## Achievers Customization

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

## Achievers Group Access

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
title: Adding ADP Workforce Now to Your PingOne for Enterprise Dock
description: Add the ADP Workforce Now application your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_adp_workforce
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_adp_workforce.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  adp-workforce-now-connection-configuration: ADP Workforce Now Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  next-steps-2: Next steps
  adp-workforce-now-attribute-mapping: ADP Workforce Now Attribute Mapping
  about-this-task: About this task
  steps-3: Steps
  choose-from-2: Choose from:
  next-steps-3: Next steps
  adp-workforce-now-customization: ADP Workforce Now Customization
  steps-4: Steps
  next-steps-4: Next steps
  adp-workforce-now-group-access: ADP Workforce Now Group Access
  about-this-task-2: About this task
  steps-5: Steps
  adp-workforce-now-saml-connection: ADP Workforce Now SAML Connection
  steps-6: Steps
---

# Adding ADP Workforce Now to Your PingOne for Enterprise Dock

Add the ADP Workforce Now application your PingOne for Enterprise dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click on the **ADP Workforce Now** application line to expand it and click **Setup**.

## Next steps

On the **SSO Instructions** tab, click **Continue to Next Step**.

## ADP Workforce Now Connection Configuration

### Steps

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

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

11. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

12. Select the **Use Custom URL**checkbox to enter a customer URL to launch ADP Workforce Now from the dock.

### Next steps

Click **Continue to Next Step**.

## ADP Workforce Now Attribute Mapping

### About this task

PingOne will automatically add required SAML attributes.

For ADP Workforce Now, the required attributes are:

* `SAML_SUBJECT`. The identity bridge attribute is mapped by default.

* `PersonImmutableID`. Map the identity bridge attribute representing your employee ID.

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

## ADP Workforce Now Customization

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

## ADP Workforce Now Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

## ADP Workforce Now SAML Connection

### Steps

1. On the **Review Setup** tab, go to the **SAML Metadata** line and click **Download** to download the PingOne metadata.

2. Click **Finish** to complete your configuration and add ADP Workforce Now to your PingOne Dock.

3. Go to <https://adpfedsso.adp.com> and sign on using your ADP account credentials.

4. Follow the steps on the ADP site to upload the metadata file.

5. After your metadata has been uploaded, your ADP account representative will confirm that the setup is complete in the live environment and to advise on next steps.

---

---
title: Adding Amazon Web Services to Your PingOne for Enterprise Dock
description: Add the Amazon Web Services (AWS) application to your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_aws
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_aws.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  amazon-web-services-connection-configuration: Amazon Web Services Connection Configuration
  about-this-task: About this task
  steps-2: Steps
  choose-from: Choose from:
  next-steps-2: Next steps
  amazon-web-services-provisioning: Amazon Web Services Provisioning
  about-this-task-2: About this task
  steps-3: Steps
  next-steps-3: Next steps
  amazon-web-services-attribute-mapping: Amazon Web Services Attribute Mapping
  about-this-task-3: About this task
  steps-4: Steps
  choose-from-2: Choose from:
  next-steps-4: Next steps
  amazon-web-services-customization: Amazon Web Services Customization
  steps-5: Steps
  next-steps-5: Next steps
  amazon-web-services-group-access: Amazon Web Services Group Access
  about-this-task-4: About this task
  steps-6: Steps
  next-steps-6: Next steps
  amazon-web-services-saml-connection: Amazon Web Services SAML connection
  about-this-task-5: About this task
  steps-7: Steps
  next-steps-7: Next steps
---

# Adding Amazon Web Services to Your PingOne for Enterprise Dock

Add the Amazon Web Services (AWS) application to your PingOne for Enterprise dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the Amazon Web Services application line to expand it and then click **Setup**.

4. Sign on to your AWS administration account and go to the **Management Console**.

5. Click your user name, click**My Security Credentials**, and click to expand **Access Keys**.

6. Copy the **Access Key ID** and the **Access Key Secret** values.

   For more information about your access key ID and access key secret, see the related [AWS documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSGettingStartedGuide/AWSCredentials.html).

## Next steps

In PingOne for Enterprise, click **Continue to Next Step**.

## Amazon Web Services Connection Configuration

### About this task

The **ACS URL** and **Entity ID** fields are populated with the correct values for Amazon Web Services (AWS).

All other fields are optional.

### Steps

1. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

2. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

3. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

4. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from Achiever.

5. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses in case the primary certificate fails.

6. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

7. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

8. On the **Signing** line:

   #### Choose from:

   * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

   * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

9. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

10. Select the **Use Custom URL**checkbox to enter a customer URL to launch AWS from the dock.

11. Select the **Set Up Provisioning** checkbox to configure user provisioning to AWS.

### Next steps

Click **Continue to Next Step**.

## Amazon Web Services Provisioning

### About this task

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | If you don't need to set up user provisioning, proceed to [Amazon Web Services Attribute Mapping](p14eapps_aws_attributes.html). |

If you selected **Set Up Provisioning** on the **Connection configuration** tab:

### Steps

1. In the AWS Management Console, go to **My Security Credentials**.

2. Expand the **Access keys** tab and click **Create New Access Key**.

3. When prompted, click **Show Access Key**.

4. Copy the **Access Key ID** and **Access Key Secret**.

5. In PingOne, click **Continue to Next Step** to open the **Application Configuration** tab.

6. On the **Application Configuration** tab, enter the credentials you copied in step 4 in the **accessKey** and **accessKeySecret** fields.

### Next steps

Click **Continue to Next Step**.

## Amazon Web Services Attribute Mapping

### About this task

PingOne will automatically populate required SAML attributes.

For Amazon Web Services, the required attributes are:

* `SAML_SUBJECT`

* `https://aws.amazon.com/SAML/Attributes/Role`

* If you selected **Set Up Provisioning**, `UserName(provisioning)`

### Steps

1. For `SAML_SUBJECT`:

   1. In the **Identity Bridge Attribute or Literal Value** field, enter or select **Username**.

   2. Click **Advanced**.

   3. In the **Name ID Format to send to SP** field, enter or select **urn:oasis:names:tc:SAML:2.0:nameid-format:persistent**.

   4. Click **Save**

2. For `https://aws.amazon.com/SAML/Attributes/Role`

   1. In the **Identity Bridge Attribute or Literal Value** field, select the attribute that matches `Role`.

   2. Click **Advanced**.

   3. In the **NameFormat** field, select **urn:oasis:names:tc:SAML:2.0:attrname-format:uri**.

   4. Click **Save**

   The expected format for this attribute is

   \+

   ```
   arn:aws:iam::<account-number>:role/<role-name>,arn:aws:iam::<account-number>:saml-provider/<provider-name>
   ```

3. To add an additional optional attribute, click **Add new attribute**.

4. In the **Application Attribute** field, enter the attribute name as it appears in the application.

5. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   #### Choose from:

   * Enter or select a directory attribute to map to the application attribute.

   * Select **As Literal**, then enter a literal value to assign to the application attribute.

6. To create advanced attribute mappings, click **Advanced**.

Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

### Next steps

Click **Continue to Next Step**.

## Amazon Web Services Customization

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

## Amazon Web Services Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

Click **Continue to Next Step**.

## Amazon Web Services SAML connection

### About this task

After completing the Amazon Web Services configuration in the PingOne for Enterprise admin portal, you must authorize PingOne for Enterprise as a SAML provider in the AWS console.

### Steps

1. In the PingOne for Enterprise admin console, on the **Review Setup** tab, click **Download** to download the **SAML Metadata** file.

2. Click **Finish** to add Amazon Web Services to your PingOne for Enterprise Dock.

3. In the AWS console, create a SAML provider.

   For information about creating a SAML provider in AWS, see [Create a SAML identity provider in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html) in the AWS documentation.

4. In the AWS console, create a SAML role.

   For more information about creating a SAML role in AWS, see [Create a role for a third-party identity provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the AWS documentation.

### Next steps

To configure AWS for multiple roles and accounts, see [Configure Amazon Web Services SSO for multiple roles and accounts](https://support.pingidentity.com/s/article/Configure-Amazon-Web-Services-SSO-for-multiple-roles-and-accounts) in the Ping Identity Knowledge Base.

---

---
title: Adding Aquera to Your PingOne for Enterprise Dock
description: Add the Aquera application your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_aquera
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_aquera.html
revdate: October 4, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
  aquera-connection-configuration: Aquera Connection Configuration
  steps-2: Steps
  next-steps-2: Next steps
  aquera-application-configuration: Aquera Application Configuration
  before-you-begin: Before you begin
  steps-3: Steps
  choose-from: Choose from:
  next-steps-3: Next steps
  aquera-attribute-mapping: Aquera Attribute Mapping
  about-this-task-2: About this task
  steps-4: Steps
  choose-from-2: Choose from:
  next-steps-4: Next steps
  aquera-customization: Aquera Customization
  steps-5: Steps
  next-steps-5: Next steps
  aquera-group-access: Aquera Group Access
  about-this-task-3: About this task
  steps-6: Steps
  next-steps-6: Next steps
---

# Adding Aquera to Your PingOne for Enterprise Dock

Add the Aquera application your PingOne for Enterprise dock from the application catalog.

## About this task

This application enables outbound provisioning to various services through Aquera. It can also be used to configure SSO to the target service. See the configuration documentation for the target service for more information.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Aquera** application line to expand it and then click **Setup**.

## Next steps

Click **Continue to Next Step**.

## Aquera Connection Configuration

### Steps

1. On the **Connection Configuration** form, select the **Set Up Provisioning** checkbox.

### Next steps

Click **Continue to Next Step**.

## Aquera Application Configuration

### Before you begin

Before configuring the **Application Configuration** form, sign on to the Aquera admin console in a separate browser window.

### Steps

1. In the Aquera admin console, go to **Applications**.

2. Click the application that you want to provision.

3. Copy the URL in the **Copy this URL** field.

4. In PingOne for Enterprise, paste the URL into the **SCIM\_URL** field.

5. In Aquera, from the **Authorization** field, copy the bearer token.

6. In PingOne for Enterprise, paste the bearer token into the **ACCESS\_TOKEN** field.

7. **Optional:** In the **BASIC\_AUTH\_USER** and **BASIC\_AUTH\_PASSWORD** fields, enter the credentials for the administrator account of the service you're provisioning.

   |   |                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you enter and save both the access token and the basic authorization credentials, only the access token is saved and used to authenticate. |

8. From the **REMOVE\_ACTION** list, select the action you want Aquera to take when you delete or disable a user in PingOne for Enterprise.

   #### Choose from:

   * Select **Disable** to have Aquera disable a user that you've disabled or deleted in PingOne for Enterprise.

   * Select **Delete** to have Aquera delete a user that you've disabled deleted in PingOne for Enterprise.

### Next steps

Click **Continue to Next Step**.

## Aquera Attribute Mapping

### About this task

For Aquera, the required attributes are `SAML_SUBJECT` and `userName`.

If you want to add additional attributes, Aquera supports provisioning for standard System for Cross-domain Identity Management (SCIM) attributes. For a list of SCIM attributes, see [Supported attributes reference](https://docs.pingidentity.com/integrations/aquera/setup/pf_aquera_connector_supported_attributes_reference.html).

Aquera also supports custom provisioning attributes. When creating a custom attribute, use the `IANUser` prefix. For example, if you want to create a custom attribute for office location, call it `IANUser:officeLocation` and map it to `IANUser:officeLocation`.

### Steps

1. To add an additional optional attribute, click **Add new attribute**.

2. In the **Application Attribute** field, enter the attribute name as it appears in the application.

3. For custom attributes, select the **Provisioning** checkbox.

4. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   #### Choose from:

   * Enter or select a directory attribute to map to the application attribute.

   * Select **As Literal**, then enter a literal value to assign to the application attribute.

5. To create advanced attribute mappings, click **Advanced**.

   Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

### Next steps

Click **Continue to Next Step**.

## Aquera Customization

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

## Aquera Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

On the **Review Setup** tab, review your configuration, and click **Finish** to add the application to your PingOne for Enterprise Dock.

---

---
title: Adding Arena BOMControl to Your PingOne for Enterprise Dock
description: Add the Arena BOMControl application your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_arena_bomcontrol
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_arena_bomcontrol.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  arena-bomcontrol-connection-configuration: Arena BOMControl Connection Configuration
  about-this-task: About this task
  steps-2: Steps
  next-steps-2: Next steps
  arena-bomcontrol-attribute-mapping: Arena BOMControl Attribute Mapping
  about-this-task-2: About this task
  steps-3: Steps
  choose-from: Choose from:
  next-steps-3: Next steps
  arena-bomcontrol-customization: Arena BOMControl Customization
  steps-4: Steps
  next-steps-4: Next steps
  arena-bomcontrol-group-access: Arena BOMControl Group Access
  about-this-task-3: About this task
  steps-5: Steps
  next-steps-5: Next steps
---

# Adding Arena BOMControl to Your PingOne for Enterprise Dock

Add the Arena BOMControl application your PingOne for Enterprise dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Arena BOMControl** application line to expand it and then click **Setup**.

4. To enable cloud single sign-on (SSO), email [Arena Sales.](mailto:sales@arenasolutions.com)

   |   |                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------- |
   |   | You can continue configuring this application for PingOne before your sales representative activates SSO. |

## Next steps

Click **Continue to Next Step**.

## Arena BOMControl Connection Configuration

### About this task

Your Arena representative will configure your application connection based on your specific requirements.

### Steps

* Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active single sign-on (SSO) session when they start this application.

### Next steps

Click **Continue to Next Step**.

## Arena BOMControl Attribute Mapping

### About this task

For Arena BOMControl, the required attribute is `subject`.

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

## Arena BOMControl Customization

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

## Arena BOMControl Group Access

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
title: Adding Ariba to Your PingOne for Enterprise Dock
description: Add the Ariba application your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_ariba
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_ariba.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  ariba-connection-configuration: Ariba Connection Configuration
  about-this-task: About this task
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  ariba-attribute-mapping: Ariba Attribute Mapping
  about-this-task-2: About this task
  steps-3: Steps
  choose-from-3: Choose from:
  next-steps-3: Next steps
  ariba-customization: Ariba Customization
  steps-4: Steps
  next-steps-4: Next steps
  ariba-group-access: Ariba Group Access
  about-this-task-3: About this task
  steps-5: Steps
  next-steps-5: Next steps
---

# Adding Ariba to Your PingOne for Enterprise Dock

Add the Ariba application your PingOne for Enterprise dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Ariba** application line to expand it and then click **Setup**.

4. On the **SSO Instructions** tab, click **Download** to download the signing certificate.

5. Send an email to your Ariba representative with the following information:

   * The signing certificate file you downloaded in step 3, attached to the email

   * The **Issuer** URL

   * The sign-on page URL, which is <https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=>*\<your IdP ID>*, where *\<your Idp ID>* is your **IdP ID** number.

   * The logout URL where you would like to redirect users after they sign off of Ariba.

## Next steps

After your client success manager responds with the necessary information, click **Continue to Next Step**.

## Ariba Connection Configuration

### About this task

Your Ariba representative will provide you with connection parameters for the **ACS URL** and **Entity ID** fields.

All other fields are optional.

### Steps

1. Import the metadata for Ariba:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** and **Entity ID** fields, replace the *${parameter}* variables with the information provided by your Ariba representative.

3. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

4. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

5. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

6. On the **Primary Verification Certificate** line, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses.

7. On the **Secondary Verification Certificate** line, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

8. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

9. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

10. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

11. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

12. Select the **Use Custom URL** checkbox to enter a customer URL to launch Ariba from the dock.

### Next steps

Click **Continue to Next Step**.

## Ariba Attribute Mapping

### About this task

PingOne for Enterprise will automatically populate required SAML attributes.

For Ariba, the required attribute is `SAML_SUBJECT`.

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

## Ariba Customization

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

## Ariba Group Access

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
title: Adding Atlassian Cloud to Your PingOne for Enterprise Dock
description: Add the Atlassian Cloud application to your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_atlassian_cloud
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_atlassian_cloud.html
revdate: June 5, 2024
section_ids:
  steps: Steps
  next-steps: Next steps
  atlassian-cloud-connection-configuration: Atlassian Cloud Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  atlassian-cloud-provisioning: Atlassian Cloud Provisioning
  about-this-task: About this task
  steps-3: Steps
  choose-from-3: Choose from:
  next-steps-3: Next steps
  atlassian-cloud-attribute-mapping: Atlassian Cloud Attribute Mapping
  about-this-task-2: About this task
  steps-4: Steps
  choose-from-4: Choose from:
  next-steps-4: Next steps
  atlassian-cloud-customization: Atlassian Cloud Customization
  steps-5: Steps
  next-steps-5: Next steps
  atlassian-cloud-group-access: Atlassian Cloud Group Access
  about-this-task-3: About this task
  steps-6: Steps
  atlassian-cloud-saml-connection: Atlassian Cloud SAML connection
  steps-7: Steps
---

# Adding Atlassian Cloud to Your PingOne for Enterprise Dock

Add the Atlassian Cloud application to your PingOne for Enterprise dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Atlassian Cloud** application line to expand it and click **Setup**.

4. On the **SSO Instructions** tab, click **Download** to download the signing certificate.

5. Sign on to Atlassian Cloud as an administrator

6. Go to **Security > SAML Single Sign-On**

7. Copy the **ACS URL** and **Entity ID** values.

## Next steps

In PingOne for Enterprise, click **Continue to Next Step**.

## Atlassian Cloud Connection Configuration

### Steps

1. Import the metadata for Atlassian Cloud,

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** field, enter the assertion consumer service (ACS) URL.

3. In the **Entity ID** field, enter the Entity ID.

4. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

   The default URL is pre-populated, and should work for most Atlassian Cloud connections.

5. In the **Single Logout Endpoint** field, enter a URL for PingOne for Enterprise to send single logout (SLO) requests to.

6. In the **Single Logout Response Endpoint** field, enter a URL for PingOne for Enterprise to send SLO responses to.

7. On the **Primary Verification Certificate** line, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses.

8. On the **Secondary Verification Certificate** line, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

9. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

10. Select the **Encrypt Assertion** box to encrypt outgoing SAML assertions.

11. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne for Enterprise sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne for Enterprise sign responses to incoming SAML assertions.

12. In the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

13. Select the **Use Custom URL**checkbox to enter a customer URL to launch Atlassian Cloud from the dock.

14. Select the **Set Up Provisioning** checkbox to configure provisioning to Atlassian Cloud.

### Next steps

Click **Continue to Next Step**.

## Atlassian Cloud Provisioning

### About this task

|   |                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you don't need to set up user provisioning, proceed to [Atlassian Cloud Attribute Mapping](p14eapps_atlassian_attribute_mapping.html). |

If you selected **Set Up Provisioning** on the **Connection configuration** tab:

### Steps

{In Atlassian Cloud}

1. In Atlassian Cloud, go to **Directory > User Provisioning**.

2. Click **Create a Directory**.

3. In the **Directory** field, enter a name for your directory.

4. Copy your **Directory Base URL** and **API Key**.

{In PingOne for Enterprise}

1. Click **Continue to Next Step**.

2. In the **DIRECTORY\_BASE\_URL** field, enter the directory base URL.

3. In the **API\_KEY** field, enter your API key.

4. In the **REMOVE\_ACTION** list, select one of the following options:

   #### Choose from:

   * If you select **Disable**, a user you disable or delete in PingOne for Enterprise will be disabled in Atlassian Cloud.

   * If you select **Delete**, a user you disable or delete in PingOne for Enterprise will be deleted in Atlassian Cloud.

### Next steps

Click **Continue to Next Step**.

## Atlassian Cloud Attribute Mapping

### About this task

For Atlassian Cloud, the required attribute is `SAML_SUBJECT`.

If you want to add additional attributes, Atlassian Cloud supports provisioning for standard System for Cross-domain Identity Management (SCIM) attributes. For a list of SCIM attributes, see [Supported attributes reference](https://docs.pingidentity.com/integrations/atlassian/atlassian_cloud_provisioner/pf_atlassian_cloud_connector_supported_attributes_reference.html).

### Steps

1. To add an additional optional attribute, click **Add new attribute**.

2. In the **Application Attribute** field, enter the attribute name as it appears in the application.

3. For custom attributes, select the **Provisioning** checkbox.

4. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following:

   #### Choose from:

   * Enter or select a directory attribute to map to the application attribute.

   * Select **As Literal**, then enter a literal value to assign to the application attribute.

5. To create advanced attribute mappings, click **Advanced**.

   Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html).

### Next steps

Click **Continue to Next Step**.

## Atlassian Cloud Customization

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

## Atlassian Cloud Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

## Atlassian Cloud SAML connection

### Steps

1. In PingOne for Enterprise, on the **Review Setup** tab, click **Download** to download the signing certificate.

2. Copy the **Issuer** and **idpid** values.

3. Click **Finish** to add Atlassian Cloud to your PingOne for Enterprise Dock.

4. In Atlassian Cloud, go to **Security > Identity providers** and select your PingOne for Enterprise **Directory**.

5. Click **Set up SAML single sign-on**.

6. Enter your configuration information.

   1. In the **Identity provider Entity ID** field, enter the **Issuer** value.

   2. In the **Identity provider SSO URL** field, enter `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=<your idpid>`, where *\<your idpid>* is the **idpid** value.

   3. In the **Public x509 Certificate** field, paste the text of the signing certificate you downloaded, including the `----BEGIN CERTIFICATE----` line.

7. Click **Save SAML configuration** to activate the connection to PingOne for Enterprise.

---

---
title: Adding Bomgar to Your PingOne for Enterprise Dock
description: Add the Bomgar application your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_bomgar
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_bomgar.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  bomgar-connection-configuration: Bomgar Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  bomgar-attribute-mapping: Bomgar Attribute Mapping
  about-this-task: About this task
  steps-3: Steps
  choose-from-3: Choose from:
  next-steps-3: Next steps
  bomgar-customization: Bomgar Customization
  steps-4: Steps
  next-steps-4: Next steps
  bomgar-group-access: Bomgar Group Access
  about-this-task-2: About this task
  steps-5: Steps
  bomgar-saml-connection: Bomgar SAML connection
  steps-6: Steps
---

# Adding Bomgar to Your PingOne for Enterprise Dock

Add the Bomgar application your PingOne for Enterprise dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Bomgar** application line to expand it and then click **Setup**.

4. On the **SSO Instructions** tab, click **Download** to download the signing certificate.

5. In the Bomgar admin interface, go to **Users & Security > Security Providers > Add a SAML Provider**.

6. In the **Bomgar admin interface**:

   1. In the **Name** field, enter a name for the connection.

   2. Select the **Enabled** checkbox to activate the connection.

   3. In the **Entity ID** field, enter the **Issuer** value from the **SSO Instructions** tab in PingOne.

   4. In the **Single Sign-On Service URL** field, enter the **Initiate Single Sign-On URL** value from the **SSO Instructions** tab in PingOne.

   5. In the **Certificate** section, click **Choose File** and upload the signing certificate you downloaded previously.

7. In the Bomgar admin interface, click **Download Service Provider Metadata**.

## Next steps

In PingOne for Enterprise, click **Continue to Next Step**.

## Bomgar Connection Configuration

### Steps

1. In PingOne for Enterprise, import the metadata for Bomgar:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** field, enter the value from the **Assertion Consumer Service URL** field in the Bomgar admin interface.

3. In the **Entity ID** field, enter the value from the **Entity ID** field in the Bomgar admin interface.

4. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

5. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

6. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

7. On the **Primary Verification Certificate** line, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses.

8. On the **Secondary Verification Certificate** line, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

9. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an activeSSO session.

10. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

11. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

12. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

13. Select the **Use Custom URL** checkbox to enter a customer URL to launch Bomgar from the dock.

### Next steps

Click **Continue to Next Step**.

## Bomgar Attribute Mapping

### About this task

PingOne for Enterprise will automatically populate requested SAML attributes.

For Bomgar, the populated attributes are:

* `SAML_SUBJECT`. Maps to a unique value.

  1. Click **Advanced**.

  2. From the **Name ID Format to send to SP** list, select **urn:oasis:names:tc:SAML:2.0:nameid-format:persistent**.

  3. Click **Save** to apply this format.

* `Username`. Map to `Email`.

* `Email`. Map to `Email`.

* `FirstName`. Map to `FirstName`.

* `LastName`. Map to `Last Name`.

* `Groups`. Map to `memberOf`.

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

## Bomgar Customization

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

## Bomgar Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

## Bomgar SAML connection

### Steps

1. In PingOne for Enterprise, on the **Review Setup** tab, click **Download** to download the SAML metadata file.

2. Click **Finish** to add Bomgar to your PingOne Dock.

3. In the **Bomgar admin interface**, on the **Identity Provider Settings** tab, click **Choose File** and upload the PingOne metadata file.

4. Click **Save Changes** to activate the connection to PingOne.

---

---
title: Adding Box to Your PingOne for Enterprise Dock
description: Add the Box application your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_box
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_box.html
revdate: October 4, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
  box-connection-configuration: Box Connection Configuration
  about-this-task-2: About this task
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  box-provisioning: Box Provisioning
  before-you-begin: Before you begin
  about-this-task-3: About this task
  steps-3: Steps
  result: Result:
  result-2: Result:
  next-steps-3: Next steps
  box-attribute-mapping: Box Attribute Mapping
  about-this-task-4: About this task
  steps-4: Steps
  choose-from-3: Choose from:
  next-steps-4: Next steps
  box-customization: Box Customization
  steps-5: Steps
  next-steps-5: Next steps
  box-group-access: Box Group Access
  about-this-task-5: About this task
  steps-6: Steps
  box-saml-connection: Box SAML connection
  about-this-task-6: About this task
  steps-7: Steps
---

# Adding Box to Your PingOne for Enterprise Dock

Add the Box application your PingOne for Enterprise dock from the application catalog.

## About this task

After you configure the Box application for the PingOne for Enterprise dock, you must email your Box representative with configuration and connection information.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Box** application line to expand it and click **Setup**.

## Next steps

Click **Continue to Next Step**.

## Box Connection Configuration

### About this task

PingOne for Enterprise automatically populates the values for the **ACS URL** and **Entity ID** fields. All other fields are optional.

For most configurations, the values on this tab should not change.

### Steps

1. Import the metadata for Box:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** field, the value should be `https://sso.services.box.net/sp/ACS.saml2`.

3. In the **Entity ID** field, the value should be `box.net`.

4. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

5. In the **Single Logout Endpoint** field, enter a URL for PingOne for Enterprise to send single logout (SLO) requests to.

6. In the **Single Logout Response Endpoint** field, enter a URL for PingOne for Enterprise to send SLO responses to.

7. On the **Primary Verification Certificate** line, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses.

8. On the **Secondary Verification Certificate** line, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

9. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

10. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

11. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne for Enterprise sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne for Enterprise sign responses to incoming SAML assertions.

12. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

13. Select the **Use Custom URL** checkbox to enter a customer URL to launch Achievers from the dock.

14. Select the **Set Up Provisioning** checkbox to configure user provisioning to Box.

### Next steps

Click **Continue to Next Step**.

## Box Provisioning

### Before you begin

Ensure that popups are permitted in your browser.

### About this task

|   |                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------- |
|   | If you don't need to set up user provisioning, proceed to [Box Attribute Mapping](p14eapps_box_attributes.html). |

If you selected **Set Up Provisioning** on the **Connection configuration** tab:

### Steps

1. On the **Provisioning Instructions** tab, click **Continue to Next Step**.

2. **Optional:** On the **Application Configuration** tab, complete the following steps.

   1. Select the **CREATE\_PERSONAL\_FOLDERS** checkbox to create a new Box folder when a new user is created.

   2. In the **PARENT\_FOLDER\_ID** field, enter the ID of the folder where the new user folders will be created.

      |   |                                                                                                                                                                                                                                             |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Find the ID of the desired parent folder by navigating to the Box web portal and copying the string at the end of the URL. For the folder located at <https://myconnector.app.box.com/folder/1234567890>, the folder ID would be 123456789. |

The administrator account used to obtain the **Client ID** and **Client Secret** must be the owner of this folder.

1. From the **PERSONAL\_FOLDER\_PERMISSION\_LEVELS** list, select the ownership and access permissions to apply to new user folders.

2. From the **REMOVE\_ACTION** list, select the action to take when you disable or delete a user account in PingOne.

   * Select **Suspend** to suspend a deleted user's Box account.

   * Select **Delete** to delete a deleted user's Box account.

3. In the **DELETED\_CONTENT\_ACCOUNT** field, enter the email address to which the content of a deleted user's account will be transferred.

4. From the **FORCE\_DELETE** list, select whether to delete users who own content.

   * **False** is the default option. Attempts to delete users who own content will fail.

   * **True** allows users who own content to be deleted.

     1. Click **Continue to Next Step**.

     2. Click **Activate**.

        #### Result:

        The **Customer Log In** page appears in a pop-up window.

     3. Enter your Box credentials and click **Authorize**.

     4. Click **Grant Access to Box**.

        #### Result:

        You will be redirected to PingOne. The **Activate** button should now read **Activated**.

### Next steps

Click **Continue to Next Step**.

## Box Attribute Mapping

### About this task

PingOne will automatically populate required SAML attributes.

For Box, the required attribute is `SAML_SUBJECT`.

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

## Box Customization

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

## Box Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

## Box SAML connection

### About this task

### Steps

1. In PingOne, on the **Review Setup** tab, click **Download** to download the SAML metadata file.

2. Click **Finish** to add Box to your PingOne Dock.

3. Send an email to inform your Box representative that you want to enable SSO. Include the following information.

   * The SAML metadata file you downloaded, attached to the email.

   * Which SSO mode you want.

     * SSO Enabled allows users to sign on to Box using either their Box credentials or SAML SSO.

     * SSO Required requires users to sign on to Box using SSO.

---

---
title: Adding Concur to Your PingOne for Enterprise Dock
description: Add the Concur application your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_concur
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_concur.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  concur-connection-configuration: Concur Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  concur-provisioning: Concur Provisioning
  before-you-begin: Before you begin
  about-this-task: About this task
  steps-3: Steps
  result: Result:
  result-2: Result:
  next-steps-3: Next steps
  concur-attribute-mapping: Concur Attribute Mapping
  about-this-task-2: About this task
  steps-4: Steps
  choose-from-3: Choose from:
  next-steps-4: Next steps
  concur-customization: Concur Customization
  steps-5: Steps
  next-steps-5: Next steps
  concur-group-access: Concur Group Access
  about-this-task-3: About this task
  steps-6: Steps
  next-steps-6: Next steps
---

# Adding Concur to Your PingOne for Enterprise Dock

Add the Concur application your PingOne for Enterprise dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Concur** application line to expand it and then click **Setup**.

4. On the **SSO Instructions** tab, click **Download** to download the PingOne signing certificate.

5. Email Ping Identity at <concursso@pingidentity.com>. Include the following information in the email.

   * The signing certificate you downloaded, attached to the email.

   * The **Issuer** value.

   * The email address of your employee who is the primary point of contact for the Concur configuration.

   * A logout URL to direct users to when they log out of Concur.

## Next steps

Click **Continue to Next Step**.

## Concur Connection Configuration

### Steps

1. Import the metadata for Concur:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** field, replace *$\\{www or implementation}* with the information supplied by Ping.

   The **Entity ID** field is automatically populated. You should not need to change it. All other fields are optional.

3. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

4. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

5. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

6. On the **Primary Verification Certificate** line, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses.

7. On the **Secondary Verification Certificate** line, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

8. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an activeSSO session.

9. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

10. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

11. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

12. Select the **Use Custom URL** checkbox to enter a customer URL to launch Concur from the dock.

13. Select the **Set Up Provisioning** checkbox to configure user provisioning to Concur.

### Next steps

Click **Continue to Next Step**.

## Concur Provisioning

### Before you begin

Ensure that popups are permitted in your browser.

### About this task

|   |                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------- |
|   | If you don't need to set up user provisioning, proceed to [Concur Attribute Mapping](p14eapps_concur_attributes.html). |

If you selected **Set Up Provisioning** on the **Connection configuration** tab:

### Steps

1. Sign on to Concur as a Web Services Administrator.

2. Go to **Administration > Web Services**.

3. Click **Enable Partner Application**.

4. Select **PingOne Provisioning** and click **Enable**.

5. In PingOne, click**Continue to Next Step**.

6. Click **Activate**.

   #### Result:

   The **Customer Log In** page appears in a pop-up window.

7. Enter your Concur credentials and click **Authorize**.

8. Click **Grant Access to Concur**.

   #### Result:

   You will be redirected to PingOne. The **Activate** button should now read **Activated**.

### Next steps

Click **Continue to Next Step**.

## Concur Attribute Mapping

### About this task

PingOne will automatically populate required SAML attributes.

For Concur, the required attribute is `SAML_SUBJECT`.

Enabling user provisioning creates additional required attributes, which are designated with asterisks (`\*`). We recommend literal mapping for these attributes.

|   |                                                                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `EmpID` attribute is unique to Concur and is required to complete user provisioning for this application. It is mapped to `Email` by default, but we recommend changing it.Click **Advanced**, and from the **Function** list, select **PickByFieldsFromJsonList**. In the **Expression** field, enter `\{"primary":true,"type":"work","targetField":"employeeID"}` |

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

## Concur Customization

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

## Concur Group Access

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
title: Adding Cornerstone to Your PingOne for Enterprise Dock
description: Add the Cornerstone application your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_cornerstone
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_cornerstone.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  cornerstone-connection-configuration: Cornerstone Connection Configuration
  about-this-task: About this task
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  cornerstone-attribute-mapping: Cornerstone Attribute Mapping
  about-this-task-2: About this task
  steps-3: Steps
  choose-from-3: Choose from:
  next-steps-3: Next steps
  cornerstone-customization: Cornerstone Customization
  steps-4: Steps
  next-steps-4: Next steps
  cornerstone-group-access: Cornerstone Group Access
  about-this-task-3: About this task
  steps-5: Steps
  next-steps-5: Next steps
---

# Adding Cornerstone to Your PingOne for Enterprise Dock

Add the Cornerstone application your PingOne for Enterprise dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Cornerstone** application line to expand it and then click **Setup**.

4. On the **SSO Instructions** tab, click **Download** to download the signing certificate.

5. Send an email to your Cornerstone representative with the following information:

   * The signing certificate file you downloaded in step 2, attached to the email.

   * The entity ID, which is the **Issuer** URL.

## Next steps

After your client success manager responds with the necessary information, click **Continue to Next Step**.

## Cornerstone Connection Configuration

### About this task

Your Cornerstone representative will respond with your host name, which you will enter into the **ACS URL** and **Entity ID** fields. All other fields on this tab are optional.

### Steps

1. Import the metadata for Cornerstone.

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** and **Entity ID** fields, replace the *${host}* variables with the host name provided by your Cornerstone representative.

3. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

4. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

5. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

6. On the **Primary Verification Certificate** line, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses.

7. On the **Secondary Verification Certificate** line, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

8. Select the **Force Re-authentication**checkbox to require your identity bridge to re-authenticate users with an active SSO session.

9. Select the **Encrypt Assertion** box to encrypt outgoing SAML assertions.

10. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

11. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

12. Select the **Use Custom URL** box to enter a customer URL to launch Achievers from the dock.

### Next steps

Click **Continue to Next Step**.

## Cornerstone Attribute Mapping

### About this task

PingOne for Enterprise will automatically populate required SAML attributes.

For Cornerstone, the required attribute is `SAML_SUBJECT`.

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

## Cornerstone Customization

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

## Cornerstone Group Access

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
title: Adding Coupa to Your PingOne for Enterprise Dock
description: Add the Coupa application your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_coupa
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_coupa.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  next-steps: Next steps
  coupa-connection-configuration: Coupa Connection Configuration
  about-this-task: About this task
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  coupa-provisioning: Coupa Provisioning
  about-this-task-2: About this task
  steps-3: Steps
  example: Example:
  next-steps-3: Next steps
  coupa-attribute-mapping: Coupa Attribute Mapping
  about-this-task-3: About this task
  steps-4: Steps
  choose-from-3: Choose from:
  next-steps-4: Next steps
  coupa-customization: Coupa Customization
  steps-5: Steps
  next-steps-5: Next steps
  coupa-group-access: Coupa Group Access
  about-this-task-4: About this task
  steps-6: Steps
  next-steps-6: Next steps
  coupa-saml-connection: Coupa SAML Connection
  steps-7: Steps
---

# Adding Coupa to Your PingOne for Enterprise Dock

Add the Coupa application your PingOne for Enterprise dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Coupa** application line to expand it and click **Setup**.

4. On the **SSO Instructions** page, click the **Download** link to download the PingOne for Enterprise signing certificate.

## Next steps

Click **Continue to Next Step**.

## Coupa Connection Configuration

### About this task

PingOne for Enterprise automatically populates the values for the **ACS URL** and **Entity ID** fields. All other fields are optional.

### Steps

1. Import the metadata for Coupa:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** field, make sure the value is `https://prdsso40.coupahost.com/sp/ACS.saml2`.

3. In the **Entity ID** field, make sure the value is `prdsso40.coupahost.com`.

4. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

5. In the **Single Logout Endpoint** field, enter a URL for PingOne for Enterprise to send single logout (SLO) requests to.

6. In the **Single Logout Response Endpoint** field, enter a URL for PingOne for Enterprise to send SLO responses to.

7. On the **Primary Verification Certificate** line, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses.

8. On the **Secondary Verification Certificate** line, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

9. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

10. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

11. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne for Enterprise sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne for Enterprise sign responses to incoming SAML assertions.

12. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

13. Select the **Use Custom URL** checkbox to enter a customer URL to launch Coupa from the dock.

14. Select the **Set Up Provisioning** checkbox to configure user provisioning to Coupa.

### Next steps

Click **Continue to Next Step**.

## Coupa Provisioning

### About this task

|   |                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------- |
|   | If you don't need to set up user provisioning, proceed to [Coupa Attribute Mapping](p14eapps_coupa_attributes.html). |

If you selected **Set Up Provisioning** on the **Connection Configuration** tab:

### Steps

1. On the **Provisioning Instructions** tab, click **Continue to Next Step** to proceed to the **Application Configuration** tab.

2. In the **COUPA\_SUBDOMAIN** field, enter your Coupa subdomain.

   Your Coupa subdomain is the subdomain in the URL for your Coupa login.

   #### Example:

   https\://*\<subdomain>*.coupacloud.com

3. In the **API\_KEY** field, enter the API key used to authenticate provisioning requests.

   To obtain your API key:

   1. Sign on to your Coupa account as an administrative user.

   2. Go to **Setup > API Keys**.

   3. Click **Create**.

   4. Complete the creation form and click **Create**.

   5. Copy the API key value and paste into the **API\_KEY** field.

### Next steps

Click **Continue to Next Step**.

## Coupa Attribute Mapping

### About this task

PingOne will automatically populate required SAML attributes.

For Coupa, the required attribute is `SAML_SUBJECT`.

If you enabled provisioning, the required provisioning attributes are:

* `login`

* `email`

* `firstname`

* `lastname`

Provisioning creates and populates a number of optional attributes. Clear the **Identity Bridge Attribute** field for any attribute you don't intend to use.

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

## Coupa Customization

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

## Coupa Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

Click **Continue to Next Step**.

## Coupa SAML Connection

### Steps

1. On the **Review Setup** tab, on the **SAML Metadata** line, click **Download** to download the metadata file.

2. Click **Finish** to add Coupa to your PingOne Dock.

3. Send an email to inform your Coupa representative that you want to enable SSO. Include the following information.

   * The SAML metadata file you downloaded, attached to the email.

   * A login URL. The login URL should be in the following format.

     ```
     https://prdsso40.coupahost.com/sp/startSSO.ping?PartnerIdpId=<Issuer>&TARGET=https://<your_site>.coupahost.com/sessions/saml_post
     ```

     * Replace *\<Issuer>* with the **Issuer** value on the **Review Setup** tab.

     * Replace *\<your\_site>* with the complete URL of your site as registered at Coupa.

   * A logout page URL. Consider using the PingOne dashboard URL, which you can find in the **Configure Single Sign-on** box on your PingOne Dashboard.

   * Test user. Coupa needs a test user name and password to test SSO functionality.

4. Sign on to Coupa.

5. Go to **Setup > Company Setup > Security Controls**.

   1. Check the **Log in using SAML** checkbox.

   2. In the **Login Page URL** field, enter the login URL that you emailed to your Coupa representative.

   3. In the **Logout Page URL** field, enter the logout page URL that you emailed to your Coupa representative.

   4. In the **Timeout URL**, enter the same URL as the **Logout Page URL**.

   5. In the **Certificate** field, upload the signing certificate that you downloaded in [Adding Coupa to Your PingOne for Enterprise Dock](p14eapps_coupa.html).

6. Save your configuration in Coupa.

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
title: Adding DocuSign to Your PingOne for Enterprise Dock
description: Add the DocuSign application your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_docusign
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_docusign.html
revdate: October 4, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
  docusign-connection-configuration: Docusign Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  docusign-attribute-mapping: DocuSign Attribute Mapping
  about-this-task-2: About this task
  steps-3: Steps
  choose-from-3: Choose from:
  next-steps-3: Next steps
  docusign-customization: DocuSign Customization
  steps-4: Steps
  next-steps-4: Next steps
  docusign-group-access: DocuSign Group Access
  about-this-task-3: About this task
  steps-5: Steps
  next-steps-5: Next steps
  docusign-saml-connection: DocuSign SAML connection
  about-this-task-4: About this task
  steps-6: Steps
---

# Adding DocuSign to Your PingOne for Enterprise Dock

Add the DocuSign application your PingOne for Enterprise dock from the application catalog.

## About this task

For more information about configuring an identity provider for DocuSign, see [Set Up an Identity Provider](https://support.docusign.com/en/guides/org-admin-guide-identity-providers) in the DocuSign documentation.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **DocuSign 2.0 - Production** application line to expand it and then click **Setup**.

## Next steps

Click **Continue to Next Step**.

## Docusign Connection Configuration

### Steps

1. Import the metadata for DocuSign:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. **Required:** In the **ACS URL** and **Entity ID** fields, replace the *${customer-organization-ID-goes-here}* variable with the value in your DocuSign account.

3. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

4. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

5. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

6. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from DocuSign.

7. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

8. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

9. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

10. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

11. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

12. Select the **Use Custom URL** checkbox to enter a customer URL to launch DocuSign from the dock.

### Next steps

Click **Continue to Next Step**.

## DocuSign Attribute Mapping

### About this task

For DocuSign, the required attributes are:

* `SAML_SUBJECT`: Map to your username attribute.

  |   |                                                                                                                                                                                 |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | On the **SAML\_SUBJECT** line, click **Advanced**.In the **Name ID Format to send to SP** list, select **urn:oasis:names:tc:SAML:2.0:nameid-format:persistent**.Click **Save**. |

* `emailaddress`: Map to your email attribute. This can be the same as your username attribute.

* `givenname`: Map to your first name attribute.

* `surname`: Map to your last name attribute.

DocuSign also creates two optional attributes.

* `accountid`: Map to your account ID attribute.

* `permissionprofileid`: Map to your permission profile id, for example `memberof`.

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

## DocuSign Customization

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

## DocuSign Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

On the **Review Setup** tab, review your configuration, and click **Finish** to add the application to your PingOne Dock.

## DocuSign SAML connection

### About this task

Keep the PingOne for Enterprise **Review Setup** tab open. You will need values from the **Review Setup** tab to complete your configuration in DocuSign.

### Steps

1. In a separate tab or window, sign on to the DocuSign administrative console.

2. From the DocuSign dashboard, click **Identity Providers**, then click **Add Identity Provider**.

3. In the **Identity Provider Settings** form, enter the following information:

   | Field                                         | Value                                                                                                              |
   | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
   | **Name**                                      | Enter a name for this connection.                                                                                  |
   | **Identity Provider Issuer**                  | **Issuer**                                                                                                         |
   | **Identity Provider Login URL**               | `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=<idpid>`Replace *\<idpid>* with the **idpid** value. |
   | (Optional) **Identity Provider Logout URL**   | **Single Logout Endpoint**                                                                                         |
   | (Optional) **Identity Provider Metadata URL** | **SAML Metadata URL**                                                                                              |

4. In PingOne for Enterprise, click **Download** to download the **Signing Certificate**.

5. In DocuSign, click **Add Certificate** and upload the PingOne for Enterprise signing certificate you downloaded.

6. Click **Save**.

---

---
title: Adding Dropbox to Your PingOne for Enterprise Dock
description: Add the Dropbox application to your PingOne for Enterprise dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_dropbox
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_dropbox.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  choose-from: Choose from:
  next-steps: Next steps
  dropbox-connection-configuration: Dropbox Connection Configuration
  about-this-task: About this task
  steps-2: Steps
  choose-from-2: Choose from:
  choose-from-3: Choose from:
  next-steps-2: Next steps
  dropbox-provisioning: Dropbox Provisioning
  before-you-begin: Before you begin
  about-this-task-2: About this task
  steps-3: Steps
  result: Result:
  next-steps-3: Next steps
  dropbox-attribute-mapping: Dropbox Attribute Mapping
  about-this-task-3: About this task
  steps-4: Steps
  choose-from-4: Choose from:
  next-steps-4: Next steps
  dropbox-customization: Dropbox Customization
  steps-5: Steps
  next-steps-5: Next steps
  dropbox-group-access: Dropbox Group Access
  about-this-task-4: About this task
  steps-6: Steps
  next-steps-6: Next steps
---

# Adding Dropbox to Your PingOne for Enterprise Dock

Add the Dropbox application to your PingOne for Enterprise dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Dropbox** application line to expand it and then click **Setup**.

4. On the **SSO Instructions** tab, click **Download** to download the PingOne for Enterprise signing certificate.

5. In a new tab or window, sign on to the Dropbox admin console.

6. Go to **Settings > Single Sign-On** and select the **Enable single sign-on** checkbox.

7. From the **Single sign-on** list, select one of the following:

   ### Choose from:

   * **Optional** allows users to authenticate using either their single sign-on (SSO) credentials or their Dropbox account.

   * **Required** forces users to authenticate using SSO.

8. On the **Identity provider sign-in URL** line, enter `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=<IdP ID>`, where *\<IdP ID>* is the **IdP ID** value on the **SSO Instructions** in PingOne.

9. **Optional:** On the **Identity provider sign-out URL** line, enter `https://sso.connect.pingidentity.com/sso/SLO.saml2`.

10. On the **X.509 certificate** line, upload the PingOne for Enterprise signing certificate that you downloaded in step 4.

## Next steps

In PingOne for Enterprise, click **Continue to Next Step**.

## Dropbox Connection Configuration

### About this task

PingOne automatically populates the values for the required **ACS URL** and **Entity ID** fields.

All other fields are optional.

### Steps

1. Import the metadata for Dropbox:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** field, enter the ACS URL.

   The pre-populated value for this field should work for most configurations.

3. In the **Entity ID** field, enter an entity ID.

   The pre-populated value for this field should work for most configurations.

4. In the **Target Resource** field, enter a URL to redirect the user to after IdP-initiated single sign-on (SSO).

5. In the **Single Logout Endpoint** field, enter a URL for PingOne to send single logout (SLO) requests to.

6. In the **Single Logout Response Endpoint** field, enter a URL for PingOne to send SLO responses to.

7. To add a **Primary Verification Certificate**, click **Browse** to locate and upload a local certificate file used to verify SLO requests and responses coming from Dropbox.

8. To add a **Secondary Verification Certificate**, click **Browse** to locate and upload a local certificate used to verify SLO requests and responses if the primary certificate fails.

9. Select the **Force Re-authentication** checkbox to require your identity bridge to re-authenticate users with an active SSO session.

10. Select the **Encrypt Assertion** checkbox to encrypt outgoing SAML assertions.

11. On the **Signing** line:

    #### Choose from:

    * Click **Sign Assertion** to have PingOne sign outgoing SAML assertions. This is the default option.

    * Click **Sign Response** to have PingOne sign responses to incoming SAML assertions.

12. From the **Signing Algorithm** list, select an algorithm with which to sign SAML assertions.

13. Select the **Use Custom URL** checkbox to enter a customer URL to launch Dropbox from the dock.

14. Select the **Set Up Provisioning** checkbox to configure user provisioning to Dropbox.

### Next steps

Click **Continue to Next Step**.

## Dropbox Provisioning

### Before you begin

Ensure that popups are permitted in your browser.

### About this task

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | If you don't need to set up user provisioning, proceed to [Dropbox Attribute Mapping](p14eapps_dropbox_attributes.html). |

If you selected **Set Up Provisioning** on the **Connection configuration** tab:

### Steps

1. In PingOne, click**Continue to Next Step**.

2. Click **Activate**.

   #### Result:

   The **Customer Log In** page appears in a pop-up window.

3. Sign on to the Dropbox admin console.

4. Click **Allow**.

### Next steps

Click **Continue to Next Step**.

## Dropbox Attribute Mapping

### About this task

PingOne will automatically populate the required SAML attributes.

For Dropbox, the required attribute is `SAML_SUBJECT`. Map it to an attribute that matches the Dropbox username. Click **Advanced** and from the **Name ID Format to send to SP** list, select **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

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

## Dropbox Customization

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

## Dropbox Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

On the **Review Setup** tab, review your configuration, and click **Finish** to add the application to your PingOne dock.

---

---
title: Adding Egnyte to Your PingOne for Enterprise Dock
description: Add the Egnyte application your PingOne for Enterprise Dock from the application catalog.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_app_catalog:p14eapps_egnyte
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/p14eapps_egnyte.html
revdate: October 4, 2023
section_ids:
  steps: Steps
  result: Result:
  next-steps: Next steps
  egnyte-connection-configuration: Egnyte Connection Configuration
  steps-2: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  next-steps-2: Next steps
  egnyte-provisioning: Egnyte Provisioning
  before-you-begin: Before you begin
  about-this-task: About this task
  steps-3: Steps
  result-2: Result:
  next-steps-3: Next steps
  egnyte-attribute-mapping: Egnyte Attribute Mapping
  about-this-task-2: About this task
  steps-4: Steps
  choose-from-3: Choose from:
  next-steps-4: Next steps
  egnyte-customization: Egnyte Customization
  steps-5: Steps
  next-steps-5: Next steps
  egnyte-group-access: Egnyte Group Access
  about-this-task-3: About this task
  steps-6: Steps
  next-steps-6: Next steps
---

# Adding Egnyte to Your PingOne for Enterprise Dock

Add the Egnyte application your PingOne for Enterprise Dock from the application catalog.

## Steps

1. In the PingOne for Enterprise admin console, go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for the application.

3. Click the **Egnyte** application line to expand it and click **Setup**.

4. On the **SSO Instructions** tab, click **Download** to download the signing certificate.

5. In a separate tab or window, sign on to your Egnyte domain.

6. In Egnyte, go to **Settings > External Authentication > SAML (SSO)**.

7. Select the **Enable SAML (SSO)** checkbox.

   ### Result:

   Egnyte presents a SAML connection form.

8. From the **IdP Name** list, select **PingIdentity**.

9. In the **IdP Account Name** field, enter your Egnyte account name.

   Do not include the ".egnyte.com" part of your account name.

10. In the **IdP Target URL** field, enter `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=<IdP ID>`, where *\<IdP ID>* is the **IdP ID** value from the **SSO Instructions** tab in PingOne.

11. In the **IdP Issuer URL** field, enter the **Issuer** value from the **SSO Instructions** tab in PingOne.

12. In the **SAML Certificate** field, enter the signing certificate information.

    1. In a plain text editor, open the signing certificate you downloaded in step 4.

    2. Copy the text of the certificate.

    Do not copy theBegin CertificateorEnd Certificatelines.

    1. Paste the text into the **SAML Certificate** field.

13. From the **Default User Mapping** list, select **Email address**.

14. Click **Save**.

## Next steps

In PingOne for Enterprise, click **Continue to Next Step**.

## Egnyte Connection Configuration

### Steps

1. Import the metadata for Egnyte:

   #### Choose from:

   * Click **Select File** to upload the metadata file.

   * Click **Or use URL** to enter the URL of the metadata.

2. In the **ACS URL** field, replace *$\\{your Egnyte domain}* with your Egnyte subdomain.

3. In the **Entity ID** field, enter the Egnyte entity ID.

   The pre-populated value for this field should work for most configurations.

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

13. Select the **Use Custom URL** checkbox to enter a customer URL to launch Egnyte from the dock.

14. Select the **Set Up Provisioning** checkbox to configure user provisioning to Egnyte.

### Next steps

Click **Continue to Next Step**.

## Egnyte Provisioning

### Before you begin

Ensure that popups are permitted in your browser.

### About this task

|   |                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------- |
|   | If you don't need to set up user provisioning, proceed to [Egnyte Attribute Mapping](p14eapps_egnyte_attributes.html). |

If you selected **Set Up Provisioning** on the **Connection configuration** tab:

### Steps

1. In PingOne, click **Continue to Next Step**.

2. In the **Subdomain** field, enter your Egnyte subdomain.

3. Click **Continue to Next Step**.

4. Click **Activate**.

   #### Result:

   The **Customer Log In** page appears in a pop-up window.

5. Sign on to the Egnyte admin console.

6. Click **Authorize**.

### Next steps

Click **Continue to Next Step**.

## Egnyte Attribute Mapping

### About this task

PingOne will automatically populate required SAML attributes.

For Egnyte, the required attribute is `SAML_SUBJECT`.

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

## Egnyte Customization

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

## Egnyte Group Access

### About this task

The **Group Access** tab shows every user group that you have created.

Learn more in [Adding user groups](../pingone_for_enterprise/p14e_add_groups.html).

### Steps

* To add a group's access to the application, on the line for that group, click **Add**.

* To remove a group's access, on the line for that group, click **Remove**.

* When you're finished assigning groups, click **Continue to Next Step**.

### Next steps

On the **Review Setup** tab, review your configuration, and click **Finish** to add the application to your PingOne for Enterprise Dock.