---
title: Adding device postures to your authentication policy
description: Create an authentication policy to pass the Workspace ONE device ID from the X.509 Certificate Adapter instance to the Workspace ONE IdP Adapter instance.
component: workspaceone-uem
page_id: workspaceone-uem:setup:pf_workspaceone_uem_ik_create_an_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/workspaceone-uem/setup/pf_workspaceone_uem_ik_create_an_authentication_policy.html
revdate: July 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device postures to your authentication policy

Create an authentication policy to pass the Workspace ONE device ID from the X.509 Certificate Adapter instance to the Workspace ONE IdP Adapter instance.

## About this task

These steps are designed to help you add to an existing authentication policy. You can find general information about configuring authentication policies in [PingFederate Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

## Steps

1. In the PingFederate admin console, go to the **Policies** tab.

   * For PingFederate 10.1 or later, go to **Authentication > Policies > Policies**.

   * For PingFederate 10.0 or earlier, go to **Identity Provider > Authentication Policies > Policies**.

2. Select the **IdP Authentication Policies** checkbox.

3. Open an existing authentication policy, or click **Add Policy**.

   You can find help in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

4. In the **Policy** area, in the **Select** list, select the X.509 Certificate Adapter instance that you created in [Create an X.509 Certificate Adapter instance](pf_workspaceone_uem_ik_create_an_x509_certificate_adapter_instance.html).

5. In the X.509 **Fail** section, configure the failure result.

6. In the X.509 **Success** section, select the Workspace ONE IdP Adapter instance that you created in [Configuring a Workspace ONE IdP Adapter instance](pf_workspaceone_uem_ik_configuring_a_workspace_one_idp_adapter_instance.html). Click **Options**.

7. On the **Incoming User ID** modal, in the **Source** list, select the X.509 Certificate Adapter instance.

8. In the **Attribute** list, select the attribute that you added to the extended contract of the X.509 Certificate Adapter instance. Click **Done**.

9. In the Workspace ONE IdP Adapter **Fail** section, configure the failure result.

10. In the Workspace ONE IdP Adapter **Success** section, select the policy contract that you created in [Create a policy contract](pf_workspaceone_uem_ik_create_a_policy_contract.html).

11. Click **Contract Mapping**.

12. On the **Contract Fulfillment** tab, in the **Source** list, select the X.509 Certificate Adapter instance.

13. In the **Value** list, select the attribute that contains the Workspace ONE device ID.

14. Click **Done**. In the **Policies** window, click **Save**.

---

---
title: Changelog
description: The following is the change history for the Workspace ONE UEM Integration Kit.
component: workspaceone-uem
page_id: workspaceone-uem:release_notes:pf_workspaceone_uem_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/workspaceone-uem/release_notes/pf_workspaceone_uem_ik_changelog.html
revdate: July 10, 2025
section_ids:
  workspace-one-uem-integration-kit-1-0-4-november-2021: Workspace ONE UEM Integration Kit 1.0.4 – November 2021
  airwatch-integration-kit-1-0-3-september-2020: AirWatch Integration Kit 1.0.3 – September 2020
  airwatch-integration-kit-1-0-2-march-2019: AirWatch Integration Kit 1.0.2 – March 2019
  airwatch-integration-kit-1-0-1-april-2018: AirWatch Integration Kit 1.0.1 – April 2018
  airwatch-integration-kit-1-0-april-2017: AirWatch Integration Kit 1.0 – April 2017
---

# Changelog

The following is the change history for the Workspace ONE UEM Integration Kit.

## Workspace ONE UEM Integration Kit 1.0.4 – November 2021

* Updated the product name from AirWatch Integration Kit to Workspace ONE UEM Integration Kit.

* Changed to a standardized `.zip` file structure to make automated deployments easier.

## AirWatch Integration Kit 1.0.3 – September 2020

* Improved security by masking the API key in the admin console.

* Fixed an issue that prevented the adapter from correctly returning a `FAIL` result to the PingFederate authentication policy after receiving an error from the AirWatch API.

## AirWatch Integration Kit 1.0.2 – March 2019

* Fixed an issue that prevented connections from being released for some AirWatch API responses.

## AirWatch Integration Kit 1.0.1 – April 2018

* Updated the adapter to use the latest Airwatch API version.

## AirWatch Integration Kit 1.0 – April 2017

* Initial release.

---

---
title: Configure the SP connection to use the policy contract
description: You can find more information in SP connection management in the PingFederate documentation.
component: workspaceone-uem
page_id: workspaceone-uem:setup:pf_workspaceone_uem_ik_configure_the_sp_connection_to_use_the_policy_contract
canonical_url: https://docs.pingidentity.com/integrations/workspaceone-uem/setup/pf_workspaceone_uem_ik_configure_the_sp_connection_to_use_the_policy_contract.html
revdate: July 10, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure the SP connection to use the policy contract

## About this task

You can find more information in [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html) in the PingFederate documentation.

## Steps

1. In the PingFederate admin console, create a new SP connection:

   * For PingFederate 10.1 or later, go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier, go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. On the **Connection Template** tab, select **Do not use a template for this connection**.

3. On the **Connection Type** tab, select **Browser SSO Profiles**. Click **Next**.

4. On the **Connection Options** tab, click **Next**.

5. On the **Import Metadata** tab, select **None**. Click **Next**.

6. On the **General Info** tab, enter the entity ID and choose a name for the connection. Click **Next**.

7. On the **SAML Profiles** tab, select **IdP-Initiated SSO** and any other profiles you need.

8. On the **Assertion Lifetime** tab, click **Next**.

9. On the **Assertion Creation** tab, configure the assertion creation. Click **Next**.

   1. On the **Authentication Source Mapping** tab, click **Map New Authentication Policy**.

   2. On the **Authentication Policy Contract** tab, in the **Authentication Policy Contract** list, select the policy contract that you created in [Create a policy contract](pf_workspaceone_uem_ik_create_a_policy_contract.html). Click **Next**.

   3. On the **Attribute Contract Fulfillment** tab, in the **Source** list, select **Authentication Policy Contract**.

   4. In the **Value** list, select the attribute that contains the Workspace ONE device ID. Click **Next**.

   Learn more in [Configuring SSO token creation](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spbrowserssotasklet_assertioncreationstate.html) in the PingFederate documentation.

10. On the **Assertion Creation** tab, click **Next**.

11. On the **Protocol Settings** tab, configure the protocol settings. Click **Next**.

    Learn more in [Configuring protocol settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spbrowserssotasklet_spprotocolsettingsstate.html) in the PingFederate documentation.

12. On the **Protocol Settings** tab, click **Next**.

13. On the **Summary** tab, click **Done**.

14. On the **Browser SSO** tab, click **Next**.

15. On the **Credentials** tab, configure the connection credentials as shown in [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation. Click **Next**.

16. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

---

---
title: Configuring a Workspace ONE IdP Adapter instance
description: Configure the Workspace ONE IdP Adapter to determine how PingFederate communicates with the Workspace ONE API.
component: workspaceone-uem
page_id: workspaceone-uem:setup:pf_workspaceone_uem_ik_configuring_a_workspace_one_idp_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/workspaceone-uem/setup/pf_workspaceone_uem_ik_configuring_a_workspace_one_idp_adapter_instance.html
revdate: July 10, 2025
section_ids:
  steps: Steps
---

# Configuring a Workspace ONE IdP Adapter instance

Configure the Workspace ONE IdP Adapter to determine how PingFederate communicates with the Workspace ONE API.

## Steps

1. In the PingFederate admin console, create a new IdP adapter instance:

   * For PingFederate 10.1 or later, go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

   * For PingFederate 10.0 or earlier, go to **Identity Provider > Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **Workspace ONE IdP Adapter**. Click **Next**.

3. On the **IdP Adapter** tab, configure the adapter instance with information from your Workspace ONE configuration. Click **Next**.

   |   |                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For Workspace ONE version 9.1.0.301, the API key is in **Groups & Settings > All Settings > System > Advanced > API > REST API**. We recommend that you create a new API key. |

4. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

5. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation.

   1. (Optional) [Restrict device access based on criteria](pf_workspaceone_uem_ik_restrict_device_access_based_on_criteria.html).

   2. Click **Next**.

6. On the **Summary** tab, check and save your configuration:

   * For PingFederate 10.1 or later, click **Save**.

   * For PingFederate 10.0 or earlier, click **Done**. On the **Manage IdP Adapter Instances** tab, click **Save**.

---

---
title: Create a policy contract
description: Create a policy contract that you will use in the authentication policy.
component: workspaceone-uem
page_id: workspaceone-uem:setup:pf_workspaceone_uem_ik_create_a_policy_contract
canonical_url: https://docs.pingidentity.com/integrations/workspaceone-uem/setup/pf_workspaceone_uem_ik_create_a_policy_contract.html
revdate: July 10, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Create a policy contract

Create a policy contract that you will use in the authentication policy.

## About this task

You can find help with these steps in [Policy contracts](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_policy_contracts.html) in the PingFederate documentation.

## Steps

1. On the **Identity Provider > Policy Contracts** tab, click **Create New Contract**.

2. On the **Contract Info** tab, in the **Contract Name** field, enter a unique name. Click **Next**.

3. On the **Contract Attributes** tab, click **Next**.

4. On the **Summary** tab, click **Done**.

5. On the **Authentication Policy Contract** tab, click **Save**.

---

---
title: Create an X.509 Certificate Adapter instance
description: Pass the Workspace ONE device ID to PingFederate through an X.509 certificate.
component: workspaceone-uem
page_id: workspaceone-uem:setup:pf_workspaceone_uem_ik_create_an_x509_certificate_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/workspaceone-uem/setup/pf_workspaceone_uem_ik_create_an_x509_certificate_adapter_instance.html
revdate: July 10, 2025
section_ids:
  steps: Steps
---

# Create an X.509 Certificate Adapter instance

Pass the Workspace ONE device ID to PingFederate through an X.509 certificate.

## Steps

1. In Workspace ONE, configure the X.509 certificate template to include the Workspace ONE device ID as an attribute in the SAN extension.

   You can find help in the Workspace ONE UEM documentation.

2. In PingFederate, set up the X.509 Certificate Integration Kit and [create an X.509 Certificate Adapter instance](../../x509/x509_certificate_integration_kit/pf_x509_certificate_ik_configuring_an_adapter_instance.html).

   1. In the adapter instance configuration, on the **IdP Adapter** tab, click **Show Advanced Fields**, then select **Include subject alternative name (SAN)**.

   2. On the **Extended Contract** tab, add the SAN attribute from the X.509 certificate that contains the Workspace ONE device ID.

   You can find the complete documentation in [X.509 Certificate Integration Kit](../../x509/x509_certificate_integration_kit/pf_x509_certificate_ik.html).

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Workspace ONE UEM Integration Kit files to your PingFederate directory.
component: workspaceone-uem
page_id: workspaceone-uem:setup:pf_workspaceone_uem_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/workspaceone-uem/setup/pf_workspaceone_uem_ik_deploying_the_integration_files.html
revdate: July 10, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Workspace ONE UEM Integration Kit files to your PingFederate directory.

## About this task

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | If you operate PingFederate in a cluster, the following steps refer to the console node. |

## Steps

1. Download the Workspace ONE UEM Integration Kit `.zip` archive from the [Add-ons tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/vmware-workspace-one-uem-airwatch-integration).

2. Stop PingFederate.

3. If you're upgrading an existing deployment, delete the `pf-airwatch-adapter-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. Start PingFederate.

6. If you operate PingFederate in a cluster, repeat steps 2 - 5 for each engine node.

---

---
title: Download manifest
description: The following files are included in the Workspace ONE UEM Integration Kit .zip archive.
component: workspaceone-uem
page_id: workspaceone-uem:release_notes:pf_workspaceone_uem_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/workspaceone-uem/release_notes/pf_workspaceone_uem_ik_download_manifest.html
revdate: July 10, 2025
---

# Download manifest

The following files are included in the Workspace ONE UEM Integration Kit `.zip` archive.

* `Legal.pdf`: Copyright and license information.

* `dist/pingfederate/server/default`: Contains the integration files.

  * `deploy`: Contains the Java libraries.

    * `pf-airwatch-adapter-<version>.jar`: The Workspace ONE IdP Adapter.

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the Workspace ONE UEM Integration Kit.
component: workspaceone-uem
page_id: workspaceone-uem:release_notes:pf_workspaceone_uem_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/workspaceone-uem/release_notes/pf_workspaceone_uem_ik_known_issues_and_limitations.html
revdate: July 10, 2025
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the Workspace ONE UEM Integration Kit.

## Known issues

There are no known issues.

## Known limitations

* Because of a limitation in how mobile devices handle X.509 certificates, iOS clients must use Safari, and Android clients must use Chrome.

---

---
title: Overview of the SSO flow
description: The following figure shows a basic SSO scenario in which a PingFederate server authenticates users to an SP application using the Workspace ONE IdP Adapter and PingFederate X.509 Certificate Adapter.
component: workspaceone-uem
page_id: workspaceone-uem::pf_workspaceone_uem_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/workspaceone-uem/pf_workspaceone_uem_ik_overview_of_the_sso_flow.html
revdate: July 17, 2025
section_ids:
  description: Description
---

# Overview of the SSO flow

The following figure shows a basic SSO scenario in which a PingFederate server authenticates users to an SP application using the Workspace ONE IdP Adapter and PingFederate X.509 Certificate Adapter.

![Diagram showing the authentication flow using the Workspace ONE IdP Adapter.](_images/workspace_sso_flow_diagram.png)

## Description

1. A user with a device enrolled in Workspace ONE requests access to an SP resource. The request is redirected to PingFederate to perform X.509 authentication.

2. The browser requests the user's X.509 certificate. The PingFederate X.509 Certificate Adapter validates the certificate against a list of issuers. If there aren't any issuers specified in the X.509 Certificate Adapter configuration, the adapter uses the server's list of trusted CAs instead.

3. PingFederate validates the certificate, then passes the device ID from the certificate to the Workspace ONE IdP Adapter.

4. PingFederate contacts the Workspace ONE API and provides the device ID to get information about the device's security posture.

5. PingFederate returns the authentication result. If authentication was successful, the user is redirected to the requested resource.

---

---
title: Restrict device access based on criteria
description: You can specify criteria to restrict which devices can access resources.
component: workspaceone-uem
page_id: workspaceone-uem:setup:pf_workspaceone_uem_ik_restrict_device_access_based_on_criteria
canonical_url: https://docs.pingidentity.com/integrations/workspaceone-uem/setup/pf_workspaceone_uem_ik_restrict_device_access_based_on_criteria.html
revdate: July 10, 2025
section_ids:
  steps: Steps
---

# Restrict device access based on criteria

You can specify criteria to restrict which devices can access resources.

## Steps

1. On the **Issuance Criteria** tab, in the **Source** list, select **Adapter**.

2. (Optional) Restrict access based on device ownership:

   1. In the **Attribute Name** list, select **Ownership**.

   2. In the **Condition** list, select **not equal to**.

   3. In the **Value** field, enter one of the following letters:

      * `C`: For corporate-owned devices.

      * `S`: For corporate shared devices.

      * `E`: For employee-owned devices.

   4. Click **Add**, and then click **Done**.

3. (Optional) Restrict access based on device operating system:

   1. In the **Attribute Name** list, select **OperatingSystem**.

   2. In the **Condition** list, select **not equal to**.

   3. In the **Value** field, enter one of the following:

      * `Apple`

      * `Android`

   4. Click **Add**, then **Done**.

4. (Optional) Restrict access based on device MDM policy compliance:

   1. In the **Attribute Name** list, select **ComplianceStatus**.

   2. In the **Condition** list, select **equal to (case insensitive)**.

   3. In the **Value** field, enter **Compliant**.

   4. Click **Add**, then **Done**.

5. (Optional) Restrict access for compromised devices:

   1. In the **Attribute Name** list, select **CompromisedStatus**.

   2. In the **Condition** list, select **not equal to**.

   3. In the **Value** field, enter **True**.

   4. Click **Add**, then **Done**.

6. Click **Done**, then **Next**.

---

---
title: Supported attributes reference
description: The Workspace ONE IdP Adapter retrieves the following attributes:
component: workspaceone-uem
page_id: workspaceone-uem::pf_workspaceone_uem_ik_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/workspaceone-uem/pf_workspaceone_uem_ik_supported_attributes_reference.html
revdate: July 10, 2025
---

# Supported attributes reference

The Workspace ONE IdP Adapter retrieves the following attributes:

| Attribute                   | Description                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------- |
| `AcLineStatus`              |                                                                                             |
| `AssetNumber`               |                                                                                             |
| `ComplianceStatus`          | Returns as `true` if the status is compliant with MDM policies. Otherwise, returns `false`. |
| `CompromisedStatus`         | Returns as `true` if the device is compromised. Otherwise, returns `false`.                 |
| `DataEncryptionYN`          | Returns as `true` if data protection is enabled. Otherwise, returns `false`.                |
| `DeviceFriendlyName`        | The concatenated name used to identify the user and device combination.                     |
| `EasId`                     |                                                                                             |
| `EnrollmentStatus`          | Returns as `true` if the MDM value is `false`.                                              |
| `Imei`                      | The IMEI number of the device.                                                              |
| `IsRemoteManagementEnabled` |                                                                                             |
| `IsSupervised`              |                                                                                             |
| `LastComplianceCheckOn`     | The refresh date and timestamp of the last status reported.                                 |
| `LastCompromisedCheckOn`    | The refresh date and timestamp of the last status reported.                                 |
| `LastEnrolledOn`            |                                                                                             |
| `LastSeen`                  | The date and time that the device last made successful contact with the MDM.                |
| `LocationGroupName`         | The MDM location group configuration value.                                                 |
| `MacAddress`                | The Wi-Fi MAC address.                                                                      |
| `Model`                     | The model, which the device automatically reports during registration.                      |
| `OperatingSystem`           | The OS version.                                                                             |
| `Ownership`                 | Possible values:- `C`

  Corporate.

- `E`

  Employee.

- `S`

  Shared.                   |
| `PhoneNumber`               | The phone number entered during registration.                                               |
| `Platform`                  | The platform specified during registration.                                                 |
| `SerialNumber`              | The device's serial number.                                                                 |
| `UserEmailAddress`          | The e-mail address of the device user.                                                      |
| `UserName`                  | The name of the device user.                                                                |
| `VirtualMemory`             |                                                                                             |

---

---
title: Test the integration
description: Test your configuration by adding a profile for your device and assigning it to a group.
component: workspaceone-uem
page_id: workspaceone-uem:setup:pf_workspaceone_uem_ik_test_the_integration
canonical_url: https://docs.pingidentity.com/integrations/workspaceone-uem/setup/pf_workspaceone_uem_ik_test_the_integration.html
revdate: July 10, 2025
section_ids:
  steps: Steps
---

# Test the integration

Test your configuration by adding a profile for your device and assigning it to a group.

## Steps

1. Set up PingFederate to run the service provider (SP) application according to instructions in the Workspace ONE admin documentation.

2. In the Workspace ONE admin console, on the **Devices > Profiles & Resources > Profiles** page, click **Add > Add Profile**.

3. In the device type list, select the type that the profile applies to, then complete the profile form.

4. In the **Assigned Groups** field, assign the profile to the group that includes your test device.

5. On the **Credentials** tab of the profile, click **Configure**. Select your credential source, verify the data is correct, then click **Save & Publish**.

6. Install the profile on the device:

   1. On the **Profiles & Resources** page, on the profile that you created, click **Not Installed**.

   2. Click **Install Profile**.

   3. Turn on the test device.

   4. On the device, open the agent app to force a sync between the device and the Workspace ONE server.

7. On the test device, on the **Devices > List View > Select your device > Certificates** page, check that the certificate appears on the list of certificates installed on the device.

8. On the test device, in a browser, go to a protected resource.

9. When asked for X.509 authentication, select the certificate installed by the profile. If the certificate isn't available, add it manually to the browser certificate store and try again.

   The browser redirects to PingFederate for X.509 validation and the device should redirect to the protected resource.

---

---
title: Workspace ONE UEM Integration Kit
description: The Workspace ONE UEM Integration Kit allows PingFederate to integrate with Workspace ONE (formerly known as AirWatch).
component: workspaceone-uem
page_id: workspaceone-uem::pf_workspaceone_uem_ik
canonical_url: https://docs.pingidentity.com/integrations/workspaceone-uem/pf_workspaceone_uem_ik.html
revdate: July 9, 2025
section_ids:
  features: Features
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Workspace ONE UEM Integration Kit

The Workspace ONE UEM Integration Kit allows PingFederate to integrate with Workspace ONE (formerly known as AirWatch).

## Features

* Make policy decisions based on the security posture of employees' devices.

* Mitigate the risks that come with allowing employees' mobile and desktop devices to access corporate resources.

## Components

* Workspace ONE IdP Adapter

  Allows PingFederate to communicate with the Workspace ONE API.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following resources:

* The following sections of the PingFederate documentation:

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

  * [Policy contracts](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_policy_contracts.html)

  * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

* If you want to use Workspace ONE to manage the PingID app on devices, refer to [Configure Workspace ONE UEM for PingID](https://docs.pingidentity.com/pingid/pingid_service_management/pid_configuring_workspace_one_uem.html) in the PingID documentation.

## System requirements

* PingFederate 9.0 or later.

* The X.509 Certificate Integration Kit, deployed in PingFederate.

* An on-premise or cloud deployment of the Workspace ONE platform.

* The Workspace ONE certificate authority (CA) root certificate, installed in the PingFederate trust store.

  You can find help in [Manage trusted certificate authorities](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_trustedcas_certmanagementstate.html) in the PingFederate documentation.

* A device enrolled with Workspace ONE that you can use to test your configuration.

* The following mobile single sign-on requirements:

  * A web controller, to allow the application to read the certificate from the device:

    * Android

      Chrome 45 or later and Chrome Custom Tabs.

    * Apple

      iOS9 or later and Safari View Controller.

  * AppAuth, to share sessions between supported mobile apps.