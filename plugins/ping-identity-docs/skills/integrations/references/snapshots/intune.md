---
title: Adding Intune security posture results to your authentication policy
description: By modifying your PingFederate authentication policy to include the isManaged and isCompliant results from Intune, you can control access to resources based on the device's security posture.
component: intune
page_id: intune:setup:pf_intune_ik_adding_intune_security_posture_results_to_your_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/intune/setup/pf_intune_ik_adding_intune_security_posture_results_to_your_authentication_policy.html
revdate: March 5, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding Intune security posture results to your authentication policy

By modifying your PingFederate authentication policy to include the `isManaged` and `isCompliant` results from Intune, you can control access to resources based on the device's security posture.

## About this task

These steps are designed to help you add to an existing authentication policy. Learn more about configuring authentication policies in [Policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/qmq1564002987890.html) in the PingFederate documentation.

## Steps

1. Sign on to the PingFederate administrative console.

2. On the **Identity Provider** page, under **Authentication Policies**, click **Policies**.

3. Open an existing authentication policy, or create a new one. Learn more in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

4. In the **Policy** area, in the **Select** list, select an Intune IdP Adapter instance.

   ![A screen capture of the fail and success paths for the HTML Form Adapter.](_images/jmc1588867003421.jpg)

5. Map the `deviceId` (shown as **CN**) or `userPrincipalName` from your X.509 Adapter instance into the Intune IdP Adapter instance.

   ![Screen capture of the Incoming User ID page, showing the userPrincipalName attribute mapped to X.509 adapter.](_images/syn1588867161010.jpg)

   1. Under the Intune IdP Adapter instance, click **Options**.

   2. On the **Options** dialog, from the **Source** list, select your X.509 Adapter instance.

   3. From the **Attribute** list, select **CN** or **userPrincipalName**. Click **Done**.

6. Define policy paths based on the two security posture attributes, `isCompliant` and `isManaged`.

   ![Screen capture of the Rules area. If the isCompliant attribute is equal to false, the result is notCompliant. If the isManaged attribute is equal to false, the result is notManaged.](_images/nlc1588867246179.jpg)

   1. Under the Intune IdP Adapter instance, click **Rules**.

   2. On the **Rules** dialog, in the **Attribute Name** list, select **isCompliant**.

   3. In the **Condition** list, select **equal to**.

   4. In the **Value** field, enter `true` or `false`.

   5. In the **Result** field, enter a name. This appears as a new policy path that branches from the authentication source.

   6. Repeat steps b - e for **isManaged**.

   7. Click **Done**.

7. Configure each of the authentication paths, including **Fail**, **Success**, and the paths that you defined in the **Rules** dialog.

   ![Screen capture of the Fail and Success paths for the HTML Form Adapter.](_images/atl1588867472580.jpg)

8. Click **Done**.

9. In the **Policies** window, click **Save**.

---

---
title: Changelog
description: The following is the change history for the Intune Integration Kit.
component: intune
page_id: intune:release_notes:pf_intune_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/intune/release_notes/pf_intune_ik_changelog.html
revdate: March 5, 2025
---

# Changelog

The following is the change history for the Intune Integration Kit.

**Intune Integration Kit 1.1 – May 2020**

* Added the ability to get the security posture for all of the current user's devices or only the current device.

**Intune Integration Kit 1.0 – December 2017**

* Initial release

---

---
title: Configuring an adapter instance
description: Configure the Intune IdP Adapter to allow PingFederate to get the security posture for sign-on devices.
component: intune
page_id: intune:setup:pf_intune_ik_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/intune/setup/pf_intune_ik_configuring_an_adapter_instance.html
revdate: March 5, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Configuring an adapter instance

Configure the Intune IdP Adapter to allow PingFederate to get the security posture for sign-on devices.

## Before you begin

Make sure that you've configured the X.509 Certificate Integration Kit. Learn more in [Deploying and configuring the X.509 Certificate Integration Kit](pf_intune_ik_deploying_and_configuring_the_x509_certificate_i.html).

## Steps

1. Sign on to the PingFederate administrative console.

2. On the **Identity Provider > Adapters** tab, click **Create New Instance**.

3. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **Intune Adapter**, then click **Next**.

4. On the **IdP Adapter** tab, configure the adapter instance by referring to [Intune IdP Adapter settings reference](pf_intune_ik_intune_idp_adapter_settings_reference.html), then click **Next**.

5. On the **Extended Contract** tab, add any attributes that you expect to retrieve in addition to the core contract attributes, then click **Next**.

   |   |                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Aside from the core contract attributes, the Intune IdP adapter can only provide the following two attributes:- `isCompliant`

   - `isManaged` |

6. Complete the adapter configuration.

7. On the **Summary** tab, check that the configuration is correct, then click **Done**.

8. On the **Manage IdP Adapter Instances** tab, click **Save**.

---

---
title: Creating certificate profiles in Intune
description: To complete the configuration, import the certificate authority (CA) root certificate into PingFederate, and configure trusted certificate and SCEP profiles in Intune.
component: intune
page_id: intune:setup:pf_intune_ik_creating_certificate_profiles_in_intune
canonical_url: https://docs.pingidentity.com/integrations/intune/setup/pf_intune_ik_creating_certificate_profiles_in_intune.html
revdate: March 5, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating certificate profiles in Intune

To complete the configuration, import the certificate authority (CA) root certificate into PingFederate, and configure trusted certificate and SCEP profiles in Intune.

## About this task

Learn more about certificate profiles in Intune in the following sections of the Microsoft documentation:

* [Use certificates for authentication in Microsoft Intune](https://learn.microsoft.com/en-us/mem/intune-service/protect/certificates-configure)

* [Create a device profile in Microsoft Intune](https://learn.microsoft.com/en-us/mem/intune-service/configuration/device-profile-create)

## Steps

1. In PingFederate, import the root certificate from your CA into the global trust list. Learn more in [Manage trusted certificate authorities](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_trustedcas_certmanagementstate.html) in the PingFederate documentation.

2. Sign on to [Microsoft Azure](https://portal.azure.com/#home) as an administrator.

3. Follow the steps in [Create trusted certificate profiles](https://learn.microsoft.com/en-us/mem/intune-service/protect/certificates-configure//) in the Microsoft documentation.

4. Follow the steps in [Create and assign SCEP certificate profiles in Intune](https://learn.microsoft.com/en-us/mem/intune-service/protect/certificates-profile-scep) in the Microsoft documentation, with the following details:

   1. On the **Configuration settings** tab, in the **Certificate type** list, select **User**.

   2. To get the security posture for all of the user's devices, from the **Subject name format** list, select **Common name**. From the **Subject alternative name** list, select **User principal name (UPN)**.

   3. To get the security posture for the user's current device only, from the **Subject name format** list, select **Custom**. In the **Custom** field, modify the value to include `CN={{AAD_Device_ID}}}`.

---

---
title: Deploying and configuring the X.509 Certificate Integration Kit
description: The Intune Integration Kit requires the X.509 Certificate Adapter to parse information out of the user's client certificate.
component: intune
page_id: intune:setup:pf_intune_ik_deploying_and_configuring_the_x509_certificate_i
canonical_url: https://docs.pingidentity.com/integrations/intune/setup/pf_intune_ik_deploying_and_configuring_the_x509_certificate_i.html
revdate: March 5, 2025
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Deploying and configuring the X.509 Certificate Integration Kit

The Intune Integration Kit requires the X.509 Certificate Adapter to parse information out of the user's client certificate.

## Steps

1. Follow the steps in [Deploying the integration files](../../x509/x509_certificate_integration_kit/pf_x509_certificate_ik_deploying_the_integration_files.html) in the X.509 Certificate Integration Kit documentation.

2. Follow the steps in [Configuring an adapter instance](../../x509/x509_certificate_integration_kit/pf_x509_certificate_ik_configuring_an_adapter_instance.html) in the X.509 Certificate Integration Kit documentation with one of the following modifications:

   ### Choose from:

   * If you want to base security posture results on the user's current device using the `deviceId` attribute, on the **Extended Contract** tab, add the CN attributes to parse from the SubjectDN certificate.

   * If you want to base security posture results on all of a user's devices using the `userPrincipalName` attribute, do the following:

     1. On the **IdP Adapter** tab, in the **Advanced Fields** section, select the **Include Subject Alternative Name (SAN)** checkbox.

     2. On the **Extended Contract** tab, add the `deviceId` or `userPrincipalName` attribute. The attribute that you add determines the type of security posture result you get from Intune. Learn more in **Device Lookup Attribute** in the [Intune IdP Adapter settings reference](pf_intune_ik_intune_idp_adapter_settings_reference.html).

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Intune Integration Kit files to your PingFederate directory.
component: intune
page_id: intune:setup:pf_intune_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/intune/setup/pf_intune_ik_deploying_the_integration_files.html
revdate: March 5, 2025
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Intune Integration Kit files to your PingFederate directory.

## Steps

1. Download the integration kit `.zip` archive from the [Ping Identity Integration Directory](https://support.pingidentity.com/s/marketplace-integration-home-page).

2. Stop PingFederate.

3. If you are upgrading from an earlier version of the adapter, delete `pf-intune-adapter-<version>.jar` from `<pf_install>/pingfederate/server/default/deploy`.

4. From the `.zip` archive, copy the contents of `dist` to `<pf_install>/pingfederate/server/default/deploy`.

5. Start PingFederate.

6. If you operate PingFederate in a cluster, repeat steps 2 - 5 for each instance of PingFederate.

---

---
title: Download manifest
description: The following files are included in the Intune Integration Kit:
component: intune
page_id: intune:release_notes:pf_intune_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/intune/release_notes/pf_intune_ik_download_manifest.html
revdate: March 5, 2025
---

# Download manifest

The following files are included in the Intune Integration Kit:

* `ReadMeFirst.pdf`: Contains links to this online documentation.

* `legal`: A directory that contains this document.

  * `Legal.pdf`: Contains copyright and license information.

* `dist`: A directory that contains the Java libraries needed to run the adapter.

  * `pf-intune-idp-adapter-<version>.jar`: A JAR file that contains the Intune IdP Adapter.

---

---
title: Intune IdP Adapter settings reference
description: Field descriptions for the Intune IdP Adapter configuration page.
component: intune
page_id: intune:setup:pf_intune_ik_intune_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/intune/setup/pf_intune_ik_intune_idp_adapter_settings_reference.html
revdate: March 5, 2025
---

# Intune IdP Adapter settings reference

Field descriptions for the Intune IdP Adapter configuration page.

**Standard fields**

| Field                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tenant ID**               | The ID for your Intune tenant.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Application ID**          | The ID for your application in Intune.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Application Secret**      | The password for your application in Intune.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Device Lookup Attribute** | **Device ID**: Gets the security posture for the current device by querying the `deviceId` attribute. The `deviceId` must be embedded in the Subject Alternative Name (SAN) in the client certificate. Learn more in [Configure infrastructure to support SCEP with Intune](https://learn.microsoft.com/en-us/mem/intune-service/protect/certificates-scep-configure) in the Microsoft documentation.**User Principal Name**: Gets the security posture for all devices associated with the user by querying the `userPrincipalName` attribute. |

---

---
title: Intune Integration Kit
description: The Intune Integration Kit allows PingFederate to integrate with the Microsoft Intune platform.
component: intune
page_id: intune::pf_intune_ik
canonical_url: https://docs.pingidentity.com/integrations/intune/pf_intune_ik.html
revdate: Mar 5, 2025
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Intune Integration Kit

The Intune Integration Kit allows PingFederate to integrate with the Microsoft Intune platform.

This integration allows you to get the security posture of the device that an employee is using to authenticate. Including the security posture in your PingFederate authentication policy allows you to dynamically allow or deny access to resources for each user that signs on. For example, you can:

* Deny access for users who have devices that are not managed by Intune.

* Allow access for users that only have devices that are in compliance.

* Deny access to a user whose current device has been compromised or rooted.

This mitigates the risk of corporate resources being accessed from employees' mobile and desktop devices.

|   |                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can learn how to use Microsoft Intune to manage the PingID app on mobile devices in [Configuring Microsoft Intune for PingID](https://docs.pingidentity.com/pingid/pingid_service_management/pid_configuring_microsoft_intune.html) in the PingID documentation. |

## Components

Intune IdP Adapter

* Allows you to retrieve the security posture for the authenticating user's current device, or all devices associated with that user.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, you can find more information in the following:

* The following sections of the PingFederate documentation:

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

* The [X.509 Certificate Integration Kit](../x509/x509_certificate_integration_kit/pf_x509_certificate_ik.html) documentation

* The following sections of the Microsoft documentation:

  * [Enroll devices in Microsoft Intune](https://learn.microsoft.com/en-us/mem/intune-service/fundamentals/deployment-guide-enroll)

  * [Configure the certification authority](https://learn.microsoft.com/en-us/mem/intune-service/protect/certificates-scep-configure#configure-the-certification-authority)

  * [Set up NDES](https://learn.microsoft.com/en-us/mem/intune-service/protect/certificates-scep-configure/#set-up-ndes)

  * [Configure infrastructure to support SCEP with Intune](https://learn.microsoft.com/en-us/mem/intune-service/protect/certificates-scep-configure)

## System requirements

* PingFederate 9.0 or later.

* A Microsoft Intune tenant.

* A Windows 2012 R2 (or later) server configured as a Certificate Authority (CA) server.

* A Windows 2012 R2 (or later) server configured with the Network Device Enrollment Service (NDES) server role and Simple Certificate Enrollment Protocol (SCEP).

* Mobile application support requires the following:

  * A Web Controller to allow the application to read the certificate from the device. For Android, Chrome 45+ & Chrome Custom Tabs. For Apple, iOS9+ & Safari View Controller.

  * AppAuth is required for shared sessions between supported mobile applications.

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the Intune Integration Kit.
component: intune
page_id: intune:release_notes:pf_intune_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/intune/release_notes/pf_intune_ik_known_issues_and_limitations.html
revdate: March 5, 2025
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the Intune Integration Kit.

## Known issues

There are no known issues.

## Known limitations

There are no known limitations.

---

---
title: Overview of the SSO flow
description: With the Intune Integration Kit, PingFederate parses the user's deviceId or userPrincipalName attribute from an X.509 certificate and uses it to get the device's security posture from Microsoft Intune.
component: intune
page_id: intune::pf_intune_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/intune/pf_intune_ik_overview_of_the_sso_flow.html
revdate: March 5, 2025
section_ids:
  description: Description
---

# Overview of the SSO flow

With the Intune Integration Kit, PingFederate parses the user's `deviceId` or `userPrincipalName` attribute from an X.509 certificate and uses it to get the device's security posture from Microsoft Intune.

![Diagram showing the SSO flow.](_images/zfp1563995414518.png)

## Description

1. A user requests access to a resource by using a device that is enrolled with Intune.

2. The service provider (SP) redirects the request to PingFederate. The browser requests the user's X.509 certificate.

3. The PingFederate X.509 Certificate Adapter validates the certificate against a specified list of issuers or the the server's list of trusted certificate authorities. Depending on your configuration, the X.509 Certificate Adapter passes the `deviceId` or `userPrincipalName` (UPN) attribute to the Intune IdP Adapter.

4. The Intune IdP Adapter contacts the Microsoft Graph API to look up the user's security posture information. Intune provides one of the following results depending on the Intune IdP Adapter instance configuration:

   * The security posture for the current device based on the `deviceId`.

   * An aggregate security posture for all of the current user's devices based on the `userPrincipalName`.

5. The PingFederate authentication policy uses the result from Intune to determine whether the user is redirected to the resource they requested.

---

---
title: Registering PingFederate as an application in Azure Active Directory
description: To allow PingFederate to access Intune through the Microsoft Graph API, add an application in Azure Active Directory with the necessary permissions.
component: intune
page_id: intune:setup:pf_intune_ik_registering_pf_as_an_application_in_azure_active_directory
canonical_url: https://docs.pingidentity.com/integrations/intune/setup/pf_intune_ik_registering_pf_as_an_application_in_azure_active_directory.html
revdate: March 5, 2025
section_ids:
  steps: Steps
---

# Registering PingFederate as an application in Azure Active Directory

To allow PingFederate to access Intune through the Microsoft Graph API, add an application in Azure Active Directory with the necessary permissions.

## Steps

1. In Azure Active Directory, follow the steps in [Quickstart: Register an application in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) in the Microsoft documentation.

2. Add the `DeviceManagementManagedDevices.Read.All` application permission from the Microsoft Graft API to your application by following the steps in [Configure app permissions for a web API](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-access-web-apis) in the Microsoft documentation.

3. Note your Tenant ID, Application ID, and Application Secret. You will use these in [Configuring an adapter instance](pf_intune_ik_configuring_an_adapter_instance.html).

---

---
title: Testing the integration
description: After you have completed the setup, you can test your Intune integration.
component: intune
page_id: intune:setup:pf_intune_ik_testing_the_integration
canonical_url: https://docs.pingidentity.com/integrations/intune/setup/pf_intune_ik_testing_the_integration.html
revdate: March 5, 2025
section_ids:
  steps: Steps
---

# Testing the integration

After you have completed the setup, you can test your Intune integration.

## Steps

1. On a testing device, install the Intune Company Portal app. Follow the prompts to set up the device.

2. On the **Intune > Devices > All devices** page, select your test device. Click **Sync**.

3. Wait 3 - 5 minutes for the device to communicate with Microsoft Intune and for Microsoft Intune to communicate with the NDES server. You might need to follow prompts on the device to complete the process.

4. On the **Intune > Device configuration > Assignment status** page, check the profiles that you created to see if the device registration succeeded.

5. Test your configuration:

   1. In a browser on your test device, go to the PingFederate login URL for your adapter, such as `https://pf_host:pf_port/idp/startSSO.ping?PartnerSpId=YourConnectionID`.

   2. If you are prompted to select a certificate from the device's certificate store, select the certificate that is issued from your CA that shows either your device ID or username (depending on your configuration from [Creating certificate profiles in Intune](pf_intune_ik_creating_certificate_profiles_in_intune.html)). After confirming your certificate selection, you should be redirected to your SP application.