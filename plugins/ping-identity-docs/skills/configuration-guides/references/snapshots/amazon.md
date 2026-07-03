---
title: Assigning Amazon Managed Grafana administrators
description: During authentication to Amazon Managed Grafana, you can optionally assign the Grafana Admin role to users by defining an admin role attribute and populating a PingOne SAML assertion attribute with the expected agreed-upon value.
component: configuration_guides
page_id: configuration_guides:amazon:config_saml_amazonmanagedgrafana_p1_assigning_administrators
canonical_url: https://docs.pingidentity.com/configuration_guides/amazon/config_saml_amazonmanagedgrafana_p1_assigning_administrators.html
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Assigning Amazon Managed Grafana administrators

## About this task

During authentication to Amazon Managed Grafana, you can optionally assign the Grafana Admin role to users by defining an admin role attribute and populating a PingOne SAML assertion attribute with the expected agreed-upon value.

For the example configuration, in PingOne, the **memberOf** attribute is mapped to the SAML assertion **groups** attribute. In Amazon Managed Grafana, the SAML assertion **groups** attribute is mapped to the Grafana admin role value, as shown in the following image.

![Screen capture of Grafana Assertion mapping section.](_images/tsh1638830072661.png)

## Steps

1. In your Amazon Managed Grafana workspace, go to **SAML Configuration**.

2. In the **Assertion mapping** section, in the **Assertion attribute role** field, enter `groups`.

3. Set the **Admin role values**to the PingOne group for Grafana admins.

   |   |                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------- |
   |   | The example in step 7 uses GrafanaAdmins\@directory. The @directory is appended to any PingOne group name. |

4. **Optional:** Set the **Assertion attribute groups**to the **groups** and **Editor role values**to the PingOne group for Grafana editors.

5. Click **Save SAML configuration**.

6. In PingOne, go to **Amazon Managed Grafana application Attribute Mapping**.

7. Map PingOne's **memberOf** attribute to the SAML assertion **groups** attribute.

   ![Screen capture of SSO Attribute Mapping section.](_images/ytt1638830176983.png)

   ### Result:

   Users in the PingOne **GrafanaAdmins** group are Just-In-Time provisioned during authentication as Grafana admins, and users in the PingOne **GrafanaEditors**group are Just-In-Time provisioned during authentication as Grafana editors.

---

---
title: Assigning Amazon Managed Grafana group access
description: The Group Access tab shows every user group that you've created.
component: configuration_guides
page_id: configuration_guides:amazon:config_saml_amazonmanagedgrafana_p1_assigning_group_access
canonical_url: https://docs.pingidentity.com/configuration_guides/amazon/config_saml_amazonmanagedgrafana_p1_assigning_group_access.html
revdate: December 15, 2021
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Assigning Amazon Managed Grafana group access

## About this task

The **Group Access** tab shows every user group that you've created.

## Steps

1. To add a group's access to Amazon Managed Grafana, on the row for that group, click **Add**.

2. To remove a group's access, on the row for that group, click **Remove**.

3. After you finish assigning groups, click **Continue to Next Step**.

---

---
title: Configuring Amazon Managed Grafana SAML
description: In PingOne, on the Review Setup tab, either:
component: configuration_guides
page_id: configuration_guides:amazon:config_saml_amazonmanagedgrafana_p1_configuring_saml
canonical_url: https://docs.pingidentity.com/configuration_guides/amazon/config_saml_amazonmanagedgrafana_p1_configuring_saml.html
revdate: May 6, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Configuring Amazon Managed Grafana SAML

## Steps

1. In PingOne, on the **Review Setup** tab, either:

   ### Choose from:

   * Click **Download** to download the SAML metadata file

   * Copy the PingOne SAML Metadata URL.

2. Click **Finish** to add Amazon Managed Grafana to your PingOne dock.

3. In the AWS Console, go to the Amazon Managed Grafana console.

4. To import the SAML metadata into Amazon Managed Grafana, either:

   ### Choose from:

   * Use the PingOne **SAML Metadata URL** on the Amazon Managed Grafana connection summary page in PingOne.

   * Upload the SAML metadata file.

   ![Screen capture of the Amazon Managed Grafana SAML page with URL selected as the metadata import method.](_images/ljd1638829896395.png)

---

---
title: Configuring an Amazon Managed Grafana connection
description: Set up the Amazon Managed Grafana application in PingOne:
component: configuration_guides
page_id: configuration_guides:amazon:config_saml_amazonmanagedgrafana_p1_configuring_connection
canonical_url: https://docs.pingidentity.com/configuration_guides/amazon/config_saml_amazonmanagedgrafana_p1_configuring_connection.html
revdate: May 6, 2024
section_ids:
  steps: Steps
---

# Configuring an Amazon Managed Grafana connection

## Steps

1. Set up the Amazon Managed Grafana application in PingOne:

   1. Go to **Applications → Application Catalog**.

   2. In the **Application Catalog**, search for `Grafana`.

   3. Expand the **Amazon Managed Grafana** entry and click **Setup**.

   4. Review the instructions to configure SAML with the Amazon Managed Grafana console.

   5. Click **Continue to Next Step**.

2. In the **ACS URL**field, replace the `${namespace}` and `${region}` variables with your Grafana namespace and your AWS region.

3. In the **Entity ID** field, replace the `${namespace}` and `${region}` variables with your Grafana namespace and your AWS region.

4. Click **Continue to Next Step**.

---

---
title: Configuring SAML SSO with Amazon Managed Grafana and PingOne
description: Learn how to configure SAML SSO for Amazon Managed Grafana and PingOne.
component: configuration_guides
page_id: configuration_guides:amazon:config_saml_amazonmanagedgrafana_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/amazon/config_saml_amazonmanagedgrafana_p1.html
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  configuring-an-amazon-managed-grafana-connection: Configuring an Amazon Managed Grafana connection
  steps: Steps
  mapping-amazon-managed-grafana-attributes: Mapping Amazon Managed Grafana attributes
  about-this-task-2: About this task
  steps-2: Steps
  choose-from: Choose from:
  customizing-amazon-managed-grafana-boxes: Customizing Amazon Managed Grafana boxes
  steps-3: Steps
  assigning-amazon-managed-grafana-group-access: Assigning Amazon Managed Grafana group access
  about-this-task-3: About this task
  steps-4: Steps
  configuring-amazon-managed-grafana-saml: Configuring Amazon Managed Grafana SAML
  steps-5: Steps
  choose-from-2: Choose from:
  choose-from-3: Choose from:
  assigning-amazon-managed-grafana-administrators: Assigning Amazon Managed Grafana administrators
  about-this-task-4: About this task
  steps-6: Steps
  result: Result:
---

# Configuring SAML SSO with Amazon Managed Grafana and PingOne

Learn how to configure SAML SSO for Amazon Managed Grafana and PingOne.

## About this task

|   |                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------- |
|   | Amazon Managed Grafana only supports SP-initiated SSO that is initiated from the Grafana Workspace URL. |

## Configuring an Amazon Managed Grafana connection

### Steps

1. Set up the Amazon Managed Grafana application in PingOne:

   1. Go to **Applications → Application Catalog**.

   2. In the **Application Catalog**, search for `Grafana`.

   3. Expand the **Amazon Managed Grafana** entry and click **Setup**.

   4. Review the instructions to configure SAML with the Amazon Managed Grafana console.

   5. Click **Continue to Next Step**.

2. In the **ACS URL**field, replace the `${namespace}` and `${region}` variables with your Grafana namespace and your AWS region.

3. In the **Entity ID** field, replace the `${namespace}` and `${region}` variables with your Grafana namespace and your AWS region.

4. Click **Continue to Next Step**.

## Mapping Amazon Managed Grafana attributes

### About this task

PingOne will automatically populate required SAML attributes.

For Amazon Managed Grafana, the required attributes are:

* `SAML_SUBJECT`

* `mail`

* `givenName`

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | You must set `SAML_SUBJECT` to Name ID format: `urn:oasis:names:tc:SAML:2.0:nameid-format:transient` |

### Steps

1. In the **Application Attribute** field, enter the attribute name as it appears in the application.

2. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following.

   #### Choose from:

   * Enter or select a directory attribute to map to the application attribute.

   * Select **As Literal**, then enter a literal value to assign to the application attribute.

3. **Optional:** To create advanced attribute mappings, click **Advanced**.

   ![Screen capture of PingOne SSO Attribute Mapping section with SAML\_SUBJECT, mail, and displayName listed as Application Attributes.](_images/qmw1638829973125.png)

4. Click **Continue to Next Step**.

## Customizing Amazon Managed Grafana boxes

### Steps

1. To change the application icon, click **Select Image** and upload a local image file.

   The image file must be:

   * PNG, GIF, or JPG format

   * 312 x 52 pixels maximum

   * 2 MB maximum file size

     |   |                                                  |
     | - | ------------------------------------------------ |
     |   | Images are scaled to 64 X 64 pixels for display. |

2. To change the name of the application displayed on the dock, in the **Name** field, enter a new name.

3. To change the description of the application, in the **Description** field, enter the new description.

4. To change the category the application is assigned on the dock, in the **Category** list, select a category.

5. Click **Continue to Next Step**.

## Assigning Amazon Managed Grafana group access

### About this task

The **Group Access** tab shows every user group that you've created.

### Steps

1. To add a group's access to Amazon Managed Grafana, on the row for that group, click **Add**.

2. To remove a group's access, on the row for that group, click **Remove**.

3. After you finish assigning groups, click **Continue to Next Step**.

## Configuring Amazon Managed Grafana SAML

### Steps

1. In PingOne, on the **Review Setup** tab, either:

   #### Choose from:

   * Click **Download** to download the SAML metadata file

   * Copy the PingOne SAML Metadata URL.

2. Click **Finish** to add Amazon Managed Grafana to your PingOne dock.

3. In the AWS Console, go to the Amazon Managed Grafana console.

4. To import the SAML metadata into Amazon Managed Grafana, either:

   #### Choose from:

   * Use the PingOne **SAML Metadata URL** on the Amazon Managed Grafana connection summary page in PingOne.

   * Upload the SAML metadata file.

   ![Screen capture of the Amazon Managed Grafana SAML page with URL selected as the metadata import method.](_images/ljd1638829896395.png)

## Assigning Amazon Managed Grafana administrators

### About this task

During authentication to Amazon Managed Grafana, you can optionally assign the Grafana Admin role to users by defining an admin role attribute and populating a PingOne SAML assertion attribute with the expected agreed-upon value.

For the example configuration, in PingOne, the **memberOf** attribute is mapped to the SAML assertion **groups** attribute. In Amazon Managed Grafana, the SAML assertion **groups** attribute is mapped to the Grafana admin role value, as shown in the following image.

![Screen capture of Grafana Assertion mapping section.](_images/tsh1638830072661.png)

### Steps

1. In your Amazon Managed Grafana workspace, go to **SAML Configuration**.

2. In the **Assertion mapping** section, in the **Assertion attribute role** field, enter `groups`.

3. Set the **Admin role values**to the PingOne group for Grafana admins.

   |   |                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------- |
   |   | The example in step 7 uses GrafanaAdmins\@directory. The @directory is appended to any PingOne group name. |

4. **Optional:** Set the **Assertion attribute groups**to the **groups** and **Editor role values**to the PingOne group for Grafana editors.

5. Click **Save SAML configuration**.

6. In PingOne, go to **Amazon Managed Grafana application Attribute Mapping**.

7. Map PingOne's **memberOf** attribute to the SAML assertion **groups** attribute.

   ![Screen capture of SSO Attribute Mapping section.](_images/ytt1638830176983.png)

   #### Result:

   Users in the PingOne **GrafanaAdmins** group are Just-In-Time provisioned during authentication as Grafana admins, and users in the PingOne **GrafanaEditors**group are Just-In-Time provisioned during authentication as Grafana editors.

---

---
title: Configuring SAML SSO with AWS Client VPN and PingOne
description: Learn to configure SAML single sign-on (SSO) using AWS Client VPN and PingOne.
component: configuration_guides
page_id: configuration_guides:amazon:config_saml_awsclientvpn_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/amazon/config_saml_awsclientvpn_p1.html
revdate: May 6, 2024
section_ids:
  before-you-begin: Before you begin
  create-the-aws-client-vpn-application-in-pingone: Create the AWS Client VPN application in PingOne
  result: Result:
  add-pingone-as-your-idp-in-the-aws-management-console: Add PingOne as your IdP in the AWS Management Console
  create-an-aws-client-vpn-endpoint: Create an AWS Client VPN endpoint
  configure-the-aws-client-vpn-endpoint-association: Configure the AWS Client VPN Endpoint association
  set-up-saml-group-specific-authorization: Set up SAML group-specific authorization
  connect-to-the-client-vpn: Connect to the Client VPN
  test-your-connection: Test your connection
---

# Configuring SAML SSO with AWS Client VPN and PingOne

Learn to configure SAML single sign-on (SSO) using AWS Client VPN and PingOne.

## Before you begin

Make sure you have:

* An [Amazon Web Services (AWS) account](https://aws.amazon.com/account/)

* An [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-getting-started.html) with an [EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)

  |   |                                                                                                            |
  | - | ---------------------------------------------------------------------------------------------------------- |
  |   | In the instance **Security Group**, allow ICMP traffic from the VPC CIDR range. You need this for testing. |

* A private certificate imported into [AWS Certificate Manager (ACM)](https://aws.amazon.com/certificate-manager/)

* PingOne user and group information

* A desktop (Windows or macOS) running the latest AWS Client VPN software

  |   |                                                                                        |
  | - | -------------------------------------------------------------------------------------- |
  |   | You can download the software [here](https://aws.amazon.com/vpn/client-vpn-download/). |

## Create the AWS Client VPN application in PingOne

1. In the PingOne admin portal, go to **Connections → Add Application**.

   ![Screen capture of PingOne Applications page with the plus icon outlined in red.](../_images/wos1637005186329.jpg)

2. Click **Advanced Configuration**.

3. In the **Choose Connection Type** menu, next to **SAML**, click **Configure**.

   ![Screen capture of PingOne Advanced Application Configuration section.](_images/edl1647966006621.png)

4. On the **Create App Profile** page, enter an **Application Name**, **Description**, and **Icon** for your application. Click **Next**.

   ![Screen capture of PingOne Create App Profile page with fields filled out pertaining to the AWS Client VPN.](_images/vmv1647966116023.png)

5. For **Configure SAML Connection**, select **Manually Enter** and configure the following:

   * For **ACS URLs**, enter `http://127.0.0.1:35001`.

   * Select **Sign Assertion & Response**.

   * Select **RSA\_SHA256** as the algorithm for **Signing the response**.

   * For **Entity ID**, enter `urn:amazon:webservices:clientvpn`.

   * For **Subject nameID format**, enter `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`.

   * For **Assertion Validity Duraction (in seconds)**, enter `300`.

   * For **SLO** options, leave the default settings.

6. After configuring the above values, leave the default settings and click **Save and Continue**.

   ![Screen capture of PingOne Configure SAML Connection page.](_images/xtx1647969677760.png)

7. Configure **Attribute Mapping** by adding the following **PingOne Attributes**:

   | PingOne User Attribute | Application Attribute |
   | ---------------------- | --------------------- |
   | **Username**           | `saml_subject`        |
   | **Given Name**         | `FirstName`           |
   | **Family Name**        | `LastName`            |
   | **Group Names**        | `memberOf`            |

   ### Result:

   The new application is shown in the **Applications** list.

8. Expand the application details and on the **Policies** tab, click the **Pencil** icon to edit the **Authentication Policy**.

9. Expand the application details and on the **Configuration** tab, download the metadata file.

   ![ewt1647976318504](_images/ewt1647976318504.png)

   |   |                                                    |
   | - | -------------------------------------------------- |
   |   | You'll upload this metadata file in the next step. |

## Add PingOne as your IdP in the AWS Management Console

|   |                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | AWS Client VPN is a separate app and requires a unique IdP definition in AWS. You cannot reuse an IdP already defined for another app, even if it's from the same vendor. |

1. In the AWS Management Console, open the **IAM** console and in the **Access management** section, click **Identity providers**.

2. Click **Add Provider**.

3. For **Provider type**, select **SAML**.

4. For **Provider name**, enter a unique name.

5. For **Metadata document**, click **Choose file** and upload the metadata file that you downloaded from PingOne.

   ![Screen capture of AWS IAM console SAML configuration settings.](_images/wip1647980007823.png)

## Create an AWS Client VPN endpoint

1. In the **Amazon VPC** console, in the **Virtual Private Network (VPN)** section, click **Client VPN Endpoints**.

2. Click **Create Client VPN Endpoint**.

3. Enter your desired **Name Tag** and **Description**.

4. For **Client IPv4 CIDR**, enter `your-IP-range/22`.

   |   |                                                                   |
   | - | ----------------------------------------------------------------- |
   |   | This is the IP range that will be allocated to your remote users. |

5. For **Server certificate ARN**, select the certificate you created as a prerequisite.

6. For **Authentication Options**, select **Use user-based authentication** and **Federated authentication**.

7. In the **SAML provider ARN** list, select the PingOne IdP you configured earlier.

   ![Screen capture of Amazon VPC Create Client VPN Endpoint section.](_images/qws1647983631458.png)

8. In the **Other optional parameters** section, select **Enable split-tunnel** and leave the rest of the default values.

   |   |                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------ |
   |   | Enabling split-tunnel makes sure that only traffic to the VPC IP range is forwarded via the VPN. |

9. Configure the other options according to your environment requirements.

10. Click **Create Client VPN Endpoint** to complete the setup.

## Configure the **AWS Client VPN Endpoint** association

1. In the **Amazon VPC** console, in the **Virtual Private Network (VPN)** section, click **Client VPN Endpoints**.

2. Select the VPN you created in the last step.

   It should be in the **Pending** state.

3. Go to **Options → Associations** and click **Associate**.

4. In the **Associations** list, select the target VPC and subnet with which you want to associate your endpoint.

5. **Optional:** Repeat the previous steps to associate your Client VPN endpoint to another subnet for high availability.

## Set up SAML group-specific authorization

1. In the **Amazon VPC** console, in the **Virtual Private Network (VPN)** section, click **Authorization**.

2. Click **Authorize Ingress**.

3. For **Destination network to enable**, specify the IP address of your EC2 instance that you created as a prerequisite.

4. In the **Grant access to** section, select **Allow access to users in a specific access group**.

5. In the **Access group ID** field, enter the name of the group that you want to allow access to the EC2 instance.

6. Provide an optional description and click **Add authorization rule**.

## Connect to the Client VPN

1. In the **Amazon VPC** console, in the **Virtual Private Network (VPN)** section, click **Client VPN Endpoints**.

2. Select the VPN that you created.

   It should be in the **Available** state.

3. To download the configuration profile to your desktop, click **Download Client Configuration**.

4. Open the **AWS Client VPN** desktop application.

5. Go to **File → Manage Profiles**.

6. Click **Add Profile**, choose the configuration profile that you downloaded, and give it a **Display Name** of your choice.

   Your profile appears in the AWS Client VPN profile list.

7. Select your profile and click **Connect**.

   You're redirected to PingOne for authentication.

8. Sign on to PingOne as a user with access to your EC2 instance.

   After successful authentication, you should be able to reach the EC2 instance in the target VPC.

## Test your connection

1. To test your connection, send an ICMP ping to the IP of the instance from your command line terminal.

2. In your browser, use a plugin, such as SAML-tracer, to confirm that the IdP is sending the correct details in the SAML assertion.

---

---
title: Configuring SAML SSO with AWS IAM and PingFederate
description: Enable Amazon Web Services (AWS) sign-on from a PingFederate URL (IdP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:amazon:config_saml_aws_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/amazon/config_saml_aws_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  create-the-pingfederate-sp-connection-for-aws: Create the PingFederate SP Connection for AWS
  add-the-pingfederate-idp-connection-to-aws: Add the PingFederate IdP connection to AWS
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration:
---

# Configuring SAML SSO with AWS IAM and PingFederate

Enable Amazon Web Services (AWS) sign-on from a PingFederate URL (IdP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an identity provider (IdP) or datastore containing the users requiring application access.

* Populate AWS with at least one user to test access.

* You must have administrative access to PingFederate and AWS.

## Create the PingFederate SP Connection for AWS

1. Sign on to the PingFederate administrative console.

2. Configure using **Browser SSO** profile **SAML 2.0**.

3. Set **Partner's Entity ID** to `urn:amazon:webservices`.

4. Enable the **IdP-Initiated SSO** SAML profile.

5. Enable the **SP Initiated SSO** SAML profile.

6. In **Assertion Creation → Attribute Contract**:

   * Extend the contract to add the attributes `SAML_NAME_FORMAT` and `https://aws.amazon.com/SAML/Attributes/Role`.

   * Set **https\://aws.amazon.com/SAML/Attributes/Role** to have an **Attribute Name Format** of `urn:oasis:names:tc:SAML:2.0:attrname-format:uri`.

7. In **Assertion Creation → Authentication Source Mapping → Attribute Contract Fulfillment**:

   * Map **SAML\_SUBJECT** to an attribute containing the `username` value.

   * Map **SAML\_NAME\_FORMAT** to a text value of `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`.

   * Map **https\://aws.amazon.com/SAML/Attributes/Role** to a fixed value or your attribute holding the user's AWS role name.

   * In **Protocol Settings → Assertion Consumer Service URL**, set **Binding** to **Post** and set **Endpoint URL** to `https://signin.aws.amazon.com/saml`.

     * In **Protocol Settings → Allowable SAML Bindings**, enable **POST**.

     * In **Credentials → Digital Signature Settings**, select the **PingFederate Signing Certificate**.

8. Save the configuration.

9. Export the signing certificate.

10. Export the metadata file, open it in a text editor, and copy the value of the **entityID** and the **Location** entry (https\://*your value*/idp/SSO.saml2).

## Add the PingFederate IdP connection to AWS

1. Sign on to your AWS console as an administrator.

2. In the **Security, Identity, & Compliance** section, select the **IAM** service.

   ![Screen capture of the AWS console with the IAM link highlighted in red in the Security, Identity, and Compliance section.](_images/lfb1619229721205.png)

3. Go to **Access Management → Identity Providers**.

4. Click **Add Provider**.

   ![Screen capture of the AWS console with the Identity providers section highlighted in red in the Access management menu.](_images/xwb1619229772253.png)

5. Set the following:

   |                       |                                                                           |
   | --------------------- | ------------------------------------------------------------------------- |
   | **Provider Type**     | SAML                                                                      |
   | **Provider Name**     | PingFederate                                                              |
   | **Metadata Document** | Select the PingFederate metadata download file you downloaded previously. |

6. Continue through to the final page and click **Create**.

7. Copy the **ARN** value of the provider.

   ![Screen capture of the AWS console open to the Identity providers page under the Access Management menu. The ARN value is highlighted in red.](_images/doo1619229815784.png)

8. In the side menu, select **Roles**.

9. Select the role that PingFederate SSO should have access to and then click the **Trust relationships** tab.

10. Click **Edit Trust Relationship**.

    ![Screen capture of the AWS console with the Roles page open under the Access management menu. The Edit trust relationship button is highlighted in red on the Trust relationships tab.](_images/zbc1619229841082.png)

11. Add the provider ARN value you copied previously to the policy for this role.

    ![Screen capture of the AWS console with the Trust relationships tab open.](_images/rbt1619229875203.png)

## Test the PingFederate IdP-initiated SSO integration:

1. Go to the PingFederate SSO Application Endpoint for the AWS SP connection.

2. Complete the PingFederate authentication.

   You are redirected to your AWS domain.

   ![Screen capture of the AWS console open to the AWS Management Console page.](_images/kqk1619229904875.png)

---

---
title: Configuring SAML SSO with AWS IAM and PingOne for Enterprise
description: Enable AWS sign-on from the PingOne for Enterprise console (IdP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:amazon:config_saml_aws_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/amazon/config_saml_aws_p1.html
revdate: May 20, 2024
section_ids:
  before-you-begin: Before you begin
  set-up-the-aws-application-in-pingone-for-enterprise-and-extract-the-metadata: Set up the AWS Application in PingOne for Enterprise and extract the metadata
  add-the-pingone-for-enterprise-idp-connection-to-aws: Add the PingOne for Enterprise IdP connection to AWS
  test-pingone-for-enterprise-idp-initiated-sso: Test PingOne for Enterprise IdP-initiated SSO
---

# Configuring SAML SSO with AWS IAM and PingOne for Enterprise

Enable AWS sign-on from the PingOne for Enterprise console (IdP-initiated sign-on).

## Before you begin

* Link PingOne for Enterprise to an identity repository containing the users that require application access.

* Populate AWS with at least one user to test application access.

* You must have administrative access to PingOne for Enterprise and AWS.

## Set up the AWS Application in PingOne for Enterprise and extract the metadata

1. Sign on to PingOne for Enterprise and go to **Applications → Application Catalog**.

2. In the **Application Catalog**, search for `Amazon Web Services`.

3. Click the right arrow to expand the **Amazon Web Services** entry and then click **Setup**.

   ![PingOne Application catalog showing the results of a search for Amazon Web Services. The right arrow is highlighted.](_images/wfb1617988989973.png)

4. Click **Continue to Next Step** twice.

5. Map **SAML\_SUBJECT** to the attribute containing the username value.

   ![The AWS console showing the Attribute Mapping step. SAML\_SUBJECT and the Advanced button are highlighted in red.](_images/uqq1617989274270.png)

6. Click **Advanced**.

7. Set **Name ID Format to sent to SP** to `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`.

   ![The AWS console showing the Advanced Attribute Options. The Name ID Format to send to SP value is highlighted in red.](_images/hnz1619502415218.png)

8. Click **Save**.

9. Map the **AWS Role** attribute to a fixed value or your attribute holding the user's AWS role name.

   ![The AWS console showing the Attribute Mapping step. MyRole and the Advanced button are highlighted in red.](_images/ihv1619502545618.png)

10. Click **Advanced**.

11. Set **NameFormat** to `urn:oasis:names:tc:SAML:2.0:attrname-format:uri`.

    ![The AWS Advanced Attribute Options menu. The NameFormat value is highlighted in red.](_images/bii1619502605011.png)

12. Click **Save**.

13. Click **Continue to Next Step** twice.

14. Click **Add** for each user group that you want to have access to AWS.

    ![The Group Access page showing group names.](_images/dnh1619502683691.png)

15. Download the metadata.

    ![The Single Logout Response Endpoint section with the Download link outlined in red.](_images/eqr1619502738999.png)

16. Click **Finish**.

## Add the PingOne for Enterprise IdP connection to AWS

1. Sign on to your AWS console as an administrator.

2. Select the IAM service.

   ![The AWS console showing service options. IAM is highlighted in red.](_images/inz1619502811583.png)

3. Go to **Access Management → Identity Providers** and click **Add Provider**.

   ![The IAM menu in AWS. In the sidebar, Identity providers is outlined in red.](_images/rgl1619502907798.png)

4. Set the following:

   * **Provider Type**: SAML

   * **Provider Name**: PingOne for Enterprise

   * **Metadata Document**: Select the PingOne for Enterprise metadata download file

5. Continue through to the final screen and click **Create**.

6. Copy the **ARN** value of the provider.

   ![The IAM menu in AWS. The ARN value is outlined in red.](_images/ryz1619502980624.png)

7. Select **Roles** from the side menu, and then select the role that you want PingOne for Enterprise SSO to have access to.

8. Click the **Trust Relationship** tab.

9. Click **Edit Trust Relationship**.

   ![The IAM Roles section in AWS showing the Trust relationships tab on the Summary page. The Edit trust relationship button is outlined in red.](_images/xep1619503151526.png)

10. Add the provider ARN value that you copied previously to the policy for the role.

    ![The Trust relationships tab in AWS.](_images/koz1619503263641.png)

## Test PingOne for Enterprise IdP-initiated SSO

1. Go to your Ping desktop as a user with AWS access.

   |   |                                                                                               |
   | - | --------------------------------------------------------------------------------------------- |
   |   | You can find the Ping desktop URL in the Admin console at **Setup → Dock → PingOne Dock URL** |

2. Authenticate with PingOne for Enterprise.

   ![PingOne sign on page.](_images/reg1619503321292.png)

   You're redirected to your AWS domain.

   ![The AWS console.](_images/lgc1619503389418.png)

---

---
title: Customizing Amazon Managed Grafana boxes
description: To change the application icon, click Select Image and upload a local image file.
component: configuration_guides
page_id: configuration_guides:amazon:config_saml_amazonmanagedgrafana_p1_customizing_boxes
canonical_url: https://docs.pingidentity.com/configuration_guides/amazon/config_saml_amazonmanagedgrafana_p1_customizing_boxes.html
revdate: December 15, 2021
section_ids:
  steps: Steps
---

# Customizing Amazon Managed Grafana boxes

## Steps

1. To change the application icon, click **Select Image** and upload a local image file.

   The image file must be:

   * PNG, GIF, or JPG format

   * 312 x 52 pixels maximum

   * 2 MB maximum file size

     |   |                                                  |
     | - | ------------------------------------------------ |
     |   | Images are scaled to 64 X 64 pixels for display. |

2. To change the name of the application displayed on the dock, in the **Name** field, enter a new name.

3. To change the description of the application, in the **Description** field, enter the new description.

4. To change the category the application is assigned on the dock, in the **Category** list, select a category.

5. Click **Continue to Next Step**.

---

---
title: Mapping Amazon Managed Grafana attributes
description: PingOne will automatically populate required SAML attributes.
component: configuration_guides
page_id: configuration_guides:amazon:config_saml_amazonmanagedgrafana_p1_mapping_attributes
canonical_url: https://docs.pingidentity.com/configuration_guides/amazon/config_saml_amazonmanagedgrafana_p1_mapping_attributes.html
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Mapping Amazon Managed Grafana attributes

## About this task

PingOne will automatically populate required SAML attributes.

For Amazon Managed Grafana, the required attributes are:

* `SAML_SUBJECT`

* `mail`

* `givenName`

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | You must set `SAML_SUBJECT` to Name ID format: `urn:oasis:names:tc:SAML:2.0:nameid-format:transient` |

## Steps

1. In the **Application Attribute** field, enter the attribute name as it appears in the application.

2. In the **Identity Bridge Attribute or Literal Value** field, choose one of the following.

   ### Choose from:

   * Enter or select a directory attribute to map to the application attribute.

   * Select **As Literal**, then enter a literal value to assign to the application attribute.

3. **Optional:** To create advanced attribute mappings, click **Advanced**.

   ![Screen capture of PingOne SSO Attribute Mapping section with SAML\_SUBJECT, mail, and displayName listed as Application Attributes.](_images/qmw1638829973125.png)

4. Click **Continue to Next Step**.