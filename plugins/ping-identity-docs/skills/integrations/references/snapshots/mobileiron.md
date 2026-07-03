---
title: Configuration examples
description: The following examples use the adapter's issuance criteria to put restrictions on authorizing users to access protected resources.
component: mobileiron
page_id: mobileiron:setup:pf_mobileiron_ik_configuration_examples
canonical_url: https://docs.pingidentity.com/integrations/mobileiron/setup/pf_mobileiron_ik_configuration_examples.html
revdate: November 5, 2025
section_ids:
  restrict-users-based-on-device-ownership: Restrict users based on device ownership
  restrict-users-based-on-device-operating-system: Restrict users based on device operating system
---

# Configuration examples

The following examples use the adapter's issuance criteria to put restrictions on authorizing users to access protected resources.

You can find more information about adapter contract mapping in [Defining the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation.

## Restrict users based on device ownership

1. In the PingFederate admin console, go to **Authentication > Integration > IdP Adapters**. Open the MobileIron adapter you configured.

2. Click **Adapter Contract Mapping**, then click **Configure Adapter Contract** to access the adapter's attribute mapping summary page. Go to the **Issuance Criteria** section.

3. In the **Source** list, select `adapter`.

4. In the **Attribute Name** list, select `Ownership`.

5. In the **Condition** list, select `not equal to`.

6. The MobileIron Device API returns one of three values for ownership:

   * `COMPANY` for Corporate-owned devices

   * `EMPLOYEE` for Employee-owned devices

   * `UNKNOWN`

   Select the device ownership type that complies with your business practices.

7. Click **Add**, click **Done** twice, then click **Save**.

## Restrict users based on device operating system

1. In the PingFederate admin console, go to **Authentication > Integration > IdP Adapters**. Open the MobileIron adapter you configured.

2. Click **Adapter Contract Mapping**, then click **Configure Adapter Contract** to access the adapter's attribute mapping summary page. Go to the **Issuance Criteria** section.

3. In the **Source** list, select `adapter`.

4. In the **Attribute Name** list, select `os`.

5. In the **Condition** list, select `not equal to`.

6. The MobileIron Device API returns different values for device operating systems.

   * `IOS`

   * `ANDROID`

   Select the device operating system type that complies with your business practices.

7. Click **Add**, click **Done** twice, then click **Save**.

---

---
title: Configuring a MobileIron Adapter instance
description: Configure the MobileIron Adapter to determine how PingFederate communicates with MobileIron.
component: mobileiron
page_id: mobileiron:setup:pf_mobileiron_ik_creating_a_mobileiron_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/mobileiron/setup/pf_mobileiron_ik_creating_a_mobileiron_adapter_instance.html
revdate: April 14, 2026
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Configuring a MobileIron Adapter instance

Configure the MobileIron Adapter to determine how PingFederate communicates with MobileIron.

## Steps

1. In the PingFederate admin console, go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

      The instance ID must contain only alphanumeric characters.

   3. In the **Type** list, select **MobileIron Adapter *\<version>***. Click **Next**.

3. On the **IdP Adapter** tab, configure the adapter instance:

   1. In the **Hostname** field, enter the hostname for your MobileIron instance.

   2. In the **API User Username** field, enter your API user's username.

   3. In the **API User Password** field, enter your API user's password for querying the CPS API.

   4. Click **Next**.

4. On the **Extended Contract** tab, configure any other attributes that you expect to receive. Click **Next**.

   |   |                                                                                                                                                                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The **Extended Contract** tab lists all the available attributes MobileIron can manage for devices. These are the attributes that can be used to make authentication decisions for your users. Learn more in [Supported attributes reference](pf_mobileiron_ik_supported_attributes_reference.html). |

5. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

6. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation.

   You can also find some contract fulfillment examples in [Configuration examples](pf_mobileiron_ik_configuration_examples.html).

7. On the **Summary** tab, check your configuration, and then click **Save**.

## Next steps

1. Go to **Authentication > Integration > IdP Adapters** and open the configured X509 Adapter for editing.

2. On the **IdP Adapter** tab, click **Show Advanced Fields** and select the **Include Subject Alternative Name (SAN)** checkbox.

3. On the **Extended Contract** tab, edit the configuration to include the name of the subject alternative name key.

4. Save the X509 Adapter configuration.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the MobileIron Integration Kit files to your PingFederate directory.
component: mobileiron
page_id: mobileiron:setup:pf_mobileiron_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/mobileiron/setup/pf_mobileiron_ik_deploying_the_integration_files.html
revdate: April 14, 2026
section_ids:
  download-manifest: Download manifest
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the MobileIron Integration Kit files to your PingFederate directory.

## Download manifest

The following files are included in the MobileIron Integration Kit `.zip` archive.

> **Collapse: Included files**
>
> * `Legal.pdf`: Contains the licenses for the dependencies used in the project.
>
> * `dist/pingfederate/server/default`: Contains the integration files.
>
>   * `pf-mobileiron-integration-kit-<version>.jar`: The MobileIron Adapter `.jar` file.

## Steps

1. Download the MobileIron Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/mobileiron-integration-kit).

2. Stop PingFederate, if it's running.

3. If you're upgrading an existing deployment, delete `pf-mobileiron-integration-kit-<version>.jar` from `<pf_install>/pingfederate/server/default/deploy`.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. Start PingFederate.

6. If you operate PingFederate in a cluster, repeat steps 2 - 5 for each engine node.

---

---
title: MobileIron Integration Kit
description: The MobileIron Integration Kit includes an identity provider (IdP) adapter to integrate PingFederate with any instance of the MobileIron platform.
component: mobileiron
page_id: mobileiron::pf_mobileiron_ik
canonical_url: https://docs.pingidentity.com/integrations/mobileiron/pf_mobileiron_ik.html
revdate: April 14, 2026
section_ids:
  example-use-cases: Example use cases
  intended-audience: Intended audience
  system-requirements: System requirements
---

# MobileIron Integration Kit

The MobileIron Integration Kit includes an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* adapter to integrate PingFederate with any instance of the MobileIron platform.

This integration enables customers to make policy decisions based on the employee's device posture, which mitigates the risk of accessing corporate resources from employees' mobile and desktop devices.

## Example use cases

You can use the MobileIron Integration Kit to:

* Allow access for devices running on the iOS platform. Learn more about how to set up this use case in [Configuration examples](setup/pf_mobileiron_ik_configuration_examples.html).

* Deny access for devices that aren't managed by MobileIron.

* Allow access for devices that comply with company policy.

* Deny access for compromised or rooted devices.

## Intended audience

This document is intended for PingFederate administrators. If you need help during the setup process, you can find more information in the following resources:

* The following sections of the PingFederate documentation:

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

* If you want to use MobileIron to manage the PingID® app on devices, refer to [Configuring MobileIron for PingID](https://docs.pingidentity.com/pingid/pingid_service_management/pid_configuring_mobileiron_for_pid.html) in the PingID documentation.

## System requirements

* PingFederate 11.3 or later

* [PingFederate X.509 Certificate Integration Kit](../x509/x509_certificate_integration_kit/pf_x509_certificate_ik.html) 1.2.1 or later

* A MobileIron Cloud, Core, or Connected Core deployment (on-premise or cloud)

* A device registered with MobileIron (for testing)

---

---
title: Overview of the SSO flow
description: The following figure shows a basic single sign-on (SSO) scenario in which a PingFederate server authenticates users to an service provider (SP) application using the MobileIron Adapter and X.509 Adapter.
component: mobileiron
page_id: mobileiron::pf_mobileiron_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/mobileiron/pf_mobileiron_ik_overview_of_the_sso_flow.html
revdate: April 14, 2026
section_ids:
  description: Description
---

# Overview of the SSO flow

The following figure shows a basic single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* scenario in which a PingFederate server authenticates users to an service provider (SP) *(tooltip: \<div class="paragraph">
\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
\</div>)* application using the MobileIron Adapter and X.509 Adapter.

![Diagram showing the SSO flow using the MobileIron Adapter.](_images/mobileiron-ik-sso-flow-overview-diagram.png)

## Description

1. A user requests access to an SP resource through a device enrolled with MobileIron. The request is redirected to PingFederate to perform X.509 authentication.

2. The browser requests the user's X.509 certificate. The PingFederate X.509 Certificate Adapter validates that certificate against a list of issuers.

   If you didn't specify any issuers during the adapter setup, the adapter uses the server's list of trusted certificate authorities instead.

3. During validation, the X.509 Certificate Adapter parses the device identifier from the certificate and passes it to the MobileIron Adapter.

4. The MobileIron Adapter uses the device identifier to contact the MobileIron Device API to retrieve the device's posture.

5. The API returns the result of the authentication. If authentication was successful, the user is redirected to the requested resource.

---

---
title: Release notes
description: The change history for the MobileIron Integration Kit.
component: mobileiron
page_id: mobileiron::pf_mobileiron_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/mobileiron/pf_mobileiron_ik_changelog.html
revdate: April 14, 2026
section_ids:
  version-1-0: Version 1.0
  initial-release: Initial release
  known-limitations: Known limitations
---

# Release notes

The change history for the MobileIron Integration Kit.

## Version 1.0

Released in March 2018.

### Initial release

New

* Learn more about how the MobileIron Integration Kit works in [MobileIron Integration Kit](pf_mobileiron_ik.html) and [Overview of the SSO flow](pf_mobileiron_ik_overview_of_the_sso_flow.html).

* You can find more information about how to configure the IK in [Setup](setup/pf_mobileiron_ik_setup.html).

## Known limitations

None.

---

---
title: Setup
description: To configure the MobileIron Integration Kit, complete the following steps in order:
component: mobileiron
page_id: mobileiron:setup:pf_mobileiron_ik_setup
canonical_url: https://docs.pingidentity.com/integrations/mobileiron/setup/pf_mobileiron_ik_setup.html
revdate: April 14, 2026
---

# Setup

To configure the MobileIron Integration Kit, complete the following steps in order:

1. [Deploy the integration files](pf_mobileiron_ik_deploying_the_integration_files.html).

2. [Configure an adapter instance](pf_mobileiron_ik_creating_a_mobileiron_adapter_instance.html), using [Supported attributes reference](pf_mobileiron_ik_supported_attributes_reference.html) and [Configuration examples](pf_mobileiron_ik_configuration_examples.html) as references for steps 4 and 6 respectively.

3. [Test the adapter](pf_mobileiron_ik_testing_the_adapter.html).

---

---
title: Supported attributes reference
description: The MobileIron Adapter retrieves the following attributes. You can apply policy decisions against any of these attributes.
component: mobileiron
page_id: mobileiron:setup:pf_mobileiron_ik_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/mobileiron/setup/pf_mobileiron_ik_supported_attributes_reference.html
revdate: November 5, 2025
---

# Supported attributes reference

The MobileIron Adapter retrieves the following attributes. You can apply policy decisions against any of these attributes.

| Attribute          | Description                                                                                                    |
| ------------------ | -------------------------------------------------------------------------------------------------------------- |
| `blocked`          |                                                                                                                |
| `compliant`        | True if the device is in compliance with its MDM security policies; false otherwise.                           |
| `compromised`      | True if the device is compromised; false otherwise.                                                            |
| `identifier`       |                                                                                                                |
| `imei`             | The IMEI number of the device.                                                                                 |
| `iosUdid`          | Unique device identifier.                                                                                      |
| `lastCheckInTime`  |                                                                                                                |
| `macAddress`       | The Wi-Fi MAC address.                                                                                         |
| `manufacturer`     | The device reports the manufacturer automatically during registration.                                         |
| `model`            | The device reports the model automatically during registration.                                                |
| `os`               | The operating system.                                                                                          |
| `osVersion`        | The operating system version.                                                                                  |
| `ownership`        | A value of `COMPANY` signifies that the device is corporate-owned. Other values are: `EMPLOYEE` and `UNKNOWN`. |
| `phoneNumber`      | The phone number.                                                                                              |
| `quarantined`      | True if the device is quarantined by the MDN; false otherwise.                                                 |
| `registrationTime` |                                                                                                                |
| `serialNumber`     | The serial number.                                                                                             |
| `status`           |                                                                                                                |
| `userId`           | The User ID.                                                                                                   |
| `userUdid`         |                                                                                                                |

---

---
title: Testing the adapter
description: Test the X509 Adapter and MobileIron Adapter's connection to MobileIron.
component: mobileiron
page_id: mobileiron:setup:pf_mobileiron_ik_testing_the_adapter
canonical_url: https://docs.pingidentity.com/integrations/mobileiron/setup/pf_mobileiron_ik_testing_the_adapter.html
revdate: November 6, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
---

# Testing the adapter

Test the X509 Adapter and MobileIron Adapter's connection to MobileIron.

## Before you begin

* Install the MobileIron agent on your device and configure it with your MobileIron instance.

  |   |                                                                                                    |
  | - | -------------------------------------------------------------------------------------------------- |
  |   | An X.509 certificate will be provisioned to your device for authentication with the X.509 Adapter. |

* Import the certificate authority (CA) *(tooltip: \<div class="paragraph">
  \<p>An entity that issues digital certificates.\</p>
  \</div>)* root certificate into the PingFederate trusted store.

  You can find more information in [Manage trusted certificate authorities](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_trustedcas_certmanagementstate.html) in the PingFederate documentation.

* Configure PingFederate to run the SP Application according to instructions in [SP application integration settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_applicat_integra_settings.html) in the PingFederate documentation.

## Steps

1. Go to your MobileIron instance, sign on, and go to **Configurations > Add > Identity Certificate**.

   1. Enter a name for the certificate.

   2. In the **Certificate Distribution** list, select **Dynamically Generated**.

   3. In the **Source** list, select your certificate authority.

   4. In the **Subject** field, enter the desired subject name.

      For example, `CN=${userCN}`.

2. In the **Subject Alternative Name Type**, click **Add**, select a key, and then enter `${deviceMdmDeviceIdentifier}` as the value.

   |   |                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The X.509 Adapter 1.3 and later support parsing the URI, RFC 822 name, and user principal name out-of-the-box.If you enter a different key in this field, you must use an OGNL script to extract the value. |

3. Click **Test Configuration**, then click **Continue**.

4. Select your inclusion and exclusion criteria for provisioning the certificate to the devices enrolled in MobileIron. Click **Done**.

   Ping Identity recommends selecting **Custom** and choosing your test device selectively.

5. On your test device, open the MobileIron Go app and sync your device.

   |   |                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The certificate can take some time to provision. You might need to open the agent app and force a check-in between the device and the MobileIron instance. |

6. After the profile is installed on the device, verify that a certificate from your credential source is available:

   1. Go to **Devices > Select your device > Certificates**.

   2. Review the list of installed certificates and confirm that a certificate from your configuration was provisioned to the device.

7. Using the device with the installed configuration, open a browser on the device and go to a resource protected by the adapter.

8. When prompted for X.509 authentication, select the certificate installed by the profile.

   |   |                                                                                                                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Depending on the device, the certificate might not be readily available in the browser for authentication. You might need to import the certificate into the browser's certificate store before you can use the certificate to authenticate a user. |

   ### Result:

   The browser redirects to PingFederate for X.509 validation. The device should be redirected to the protected resource.