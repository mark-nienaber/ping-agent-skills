---
title: Adding Jamf security posture results to your authentication policy
description: By modifying your PingFederate authentication policy to include the isManaged or isMDMCapable results from Jamf Pro, you can control access to resources dynamically based on the device's security posture.
component: jamf
page_id: jamf:setup:pf_jamf_ik_adding_jamf_security_posture_results_to_your_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/jamf/setup/pf_jamf_ik_adding_jamf_security_posture_results_to_your_authentication_policy.html
revdate: November 4, 2025
section_ids:
  steps: Steps
---

# Adding Jamf security posture results to your authentication policy

By modifying your PingFederate authentication policy to include the `isManaged` or `isMDMCapable` results from Jamf Pro, you can control access to resources dynamically based on the device's security posture.

These steps are intended to help you add to an existing authentication policy. You can find general information about configuring authentication policies in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

## Steps

1. In the PingFederate admin console, go to **Authentication > Policies > Policies**.

2. Select the **IdP Authentication Policies** checkbox.

3. Open an existing authentication policy.

4. In the **Policy** area, in the **Select** list, select a Jamf IdP Adapter instance.

   ![Adding the Jamf IdP Adapter to the authentication policy.](_images/pf-jamf-ik-adding-the-adapter-to-the-authn-policy.jpg)

5. Map the attribute that contains the device identifier (shown here as **SerialNumber**) from your X.509 Certificate IdP Adapter instance into the Jamf IdP Adapter instance.

   ![Passing the user ID from the first-factor authentication adapter.](_images/pf-jamf-ik-passing-the-user-id.jpg)

   1. Under the Jamf IdP Adapter instance, click **Options**.

   2. On the **Options** modal, in the **Source** list, select your X.509 Certificate IdP Adapter instance.

   3. In the **Attribute** list, select an attribute that matches the **Device Identifier** you selected in your adapter configuration. Click **Done**.

6. Define policy paths based on the security posture attribute `isCompliant`.

   ![Branching the authentication policy based on the device's security posture.](_images/pf-jamf-ik-branching-the-authn-policy.jpg)

   1. Under the Jamf IdP Adapter instance, click **Rules**.

   2. On the **Rules** modal, in the **Attribute Name** list, select `isCompliant`.

   3. In the **Condition** list, select **equal to**.

   4. In the **Value** field, enter `true` or `false`.

   5. In the **Result** field, enter a name.

      This appears as a new policy path that branches from the authentication source.

   6. (Optional) Repeat steps a - e for `isMDMCapable` or any attributes that you mapped in the **Jamf API Attribute Mappings** table in the adapter configuration.

   7. (Optional) Clear the **Default to success** checkbox to ensure the authentication flow follows one of the paths you defined.

   8. Click **Done**.

7. Configure each of the authentication paths.

   ![The complete authentication policy.](_images/pf-jamf-ik-example-authn-policy.jpg)

8. Click **Done**.

9. In the **Policies** window, click **Save**.

---

---
title: Authentication API Support
description: You can use the PingFederate authentication API to integrate the Jamf IdP Adapter into your application.
component: jamf
page_id: jamf::pf_jamf_ik_authentication_api_support
canonical_url: https://docs.pingidentity.com/integrations/jamf/pf_jamf_ik_authentication_api_support.html
revdate: November 4, 2025
---

# Authentication API Support

You can use the PingFederate authentication API to integrate the Jamf IdP Adapter into your application.

The PingFederate Authentication API provides access to the current state of the authentication flow as a user steps through the PingFederate authentication policy. You can find more information in [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

To integrate the Jamf IdP Adapter into your authentication flow, configure your application based on the states, actions, and models available in the PingFederate Authentication API Explorer. Learn more in [Exploring the Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_exploring_authentication_api.html) in the PingFederate documentation.

---

---
title: Certificate requirements
description: For PingFederate to get a device's security posture, each device must provide a device identifier. One way to accomplish this is by configuring SSL certificates on each device.
component: jamf
page_id: jamf:setup:pf_jamf_ik_certificate_requirements
canonical_url: https://docs.pingidentity.com/integrations/jamf/setup/pf_jamf_ik_certificate_requirements.html
revdate: November 4, 2025
section_ids:
  device-identifier-and-device-type-attributes: Device identifier and device type attributes
  example-certificate-contents: Example certificate contents
  certificate-selection: Certificate selection
---

# Certificate requirements

For PingFederate to get a device's security posture, each device must provide a device identifier. One way to accomplish this is by configuring SSL certificates on each device.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Jamf IdP Adapter requires a device identifier attribute (such as `deviceId`). The adapter uses this attribute to request the device's security posture from Jamf Pro.If you can make the device identifier attribute available in the PingFederate authentication policy without using certificates, skip this topic and [Setting up the X.509 Certificate Integration Kit](pf_jamf_ik_setting_up_the_x509_certificate_i.html). |

As described in [Overview of the SSO flow](../pf_jamf_ik_overview_of_the_sso_flow.html), the PingFederate X.509 Certificate IdP Adapter reads information from a user certificate provided through the browser.

Based on the specifics of your environment, you must determine a process for generating certificates and making them available on the enrolled devices.

The following sections describe the information that needs to be included in the certificate.

## Device identifier and device type attributes

To use the Jamf Integration Kit, each device must have a certificate that includes one of the following unique device identifiers:

* `deviceId`

* `serialnumber`

* `macaddress`

* `udid`

Optionally, you can also include a `device` attribute with a value of `computers` or `mobiledevices`. This identifies the type of device, and helps the Jamf IdP Adapter determine which Jamf Pro API to query. If the device type isn't available, the adapter queries both APIs.

The X.509 Certificate IdP Adapter checks for the device identifier and device type attributes within Subject Alternative Name portion of the certificate. Specifically, the `otherName` part of `subjectAltName`.

## Example certificate contents

When generating a certificate, you might use a `.cnf` file, such as the one in the following example, as a source:

```
[ req ]
default_bits       = 2048
distinguished_name = req_distinguished_name
req_extensions     = req_ext
[ req_distinguished_name ]
countryName                = Country Name (2 letter code)
stateOrProvinceName        = State or Province Name (full name)
localityName               = Locality Name (eg, city)
organizationName           = Organization Name (eg, company)
commonName                 = Common Name (e.g. server FQDN or YOUR name)
[ req_ext ]
subjectAltName = @alt_names
[alt_names]
otherName.1=2.16.76.1.3.4;UTF8:deviceId=18
otherName.2=2.16.76.1.3.4;UTF8:device=computers
```

|   |                                                                  |
| - | ---------------------------------------------------------------- |
|   | The last two lines define the device identifier and device type. |

## Certificate selection

After you finish setting up the Jamf Integration Kit, your users might be prompted to select the appropriate certificate during sign on. For the best user experience, we recommend that you configure automatic certificate selection. The approach you must use depends on your environment, devices, and browsers.

---

---
title: Changelog
description: The following is the change history for the Jamf Integration Kit.
component: jamf
page_id: jamf:release_notes:pf_jamf_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/jamf/release_notes/pf_jamf_ik_changelog.html
revdate: November 4, 2025
section_ids:
  jamf-integration-kit-2-0-2-november-2025: Jamf Integration Kit 2.0.2 - November 2025
  jamf-integration-kit-2-0-1-june-2022: Jamf Integration Kit 2.0.1 – June 2022
  jamf-integration-kit-2-0-april-2022: Jamf Integration Kit 2.0 – April 2022
  jamf-integration-kit-1-0-march-2021: Jamf Integration Kit 1.0 – March 2021
---

# Changelog

The following is the change history for the Jamf Integration Kit.

## Jamf Integration Kit 2.0.2 - November 2025

* Updated library dependencies to address potential security vulnerabilities.

## Jamf Integration Kit 2.0.1 – June 2022

* Updated the PingFederate Authentication API `.jar` file version.

## Jamf Integration Kit 2.0 – April 2022

* Added support for using bearer tokens to authenticate API calls to Jamf. Removed support for Basic Authentication.

* Added the `User-Agent` header to all API requests.

## Jamf Integration Kit 1.0 – March 2021

* Initial release.

* Added the ability to query Jamf Pro for a device's security posture.

* Added the ability to get the device identifier and device type from chained attributes in the PingFederate authentication policy.

* Added the ability to map any Jamf API response attribute to an attribute in the PingFederate authentication policy.

* Added the ability to control how the adapter handles sign-on attempts when errors occur.

* Added the ability to test the connection to Jamf Pro.

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Added settings for API connection and request timeouts.

* Added settings to override the PingFederate system-default proxy settings.

---

---
title: Configuring an adapter instance
description: Configure the Jamf IdP Adapter to determine how PingFederate communicates with Jamf Pro.
component: jamf
page_id: jamf:setup:pf_jamf_ik_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/jamf/setup/pf_jamf_ik_configuring_an_adapter_instance.html
revdate: November 4, 2025
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Configure the Jamf IdP Adapter to determine how PingFederate communicates with Jamf Pro.

## Steps

1. In the PingFederate admin console, go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **Jamf IdP Adapter**. Click **Next**.

3. (Optional) On the **IdP Adapter** tab, in the **Jamf API Response Mappings** section, map attributes from the Jamf Pro response to the attribute contract.

   These attributes become available in your PingFederate authentication policy.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * The `isManaged` and `isMDMCapable` attributes are already included in the core contract.

   * If you use [Computer Extension Attributes](https://docs.jamf.com/10.27.0/jamf-pro/administrator-guide/Computer_Extension_Attributes.html) or [Mobile Device Extension Attributes](https://docs.jamf.com/10.27.0/jamf-pro/administrator-guide/Mobile_Device_Extension_Attributes.html) in Jamf Pro, use this table to include your extension attributes in the PingFederate attribute contract. |

   1. Click **Add a new row to 'Jamf API Response Mappings'**.

   2. In the **Local Attribute** field, enter a name for the new attribute.

   3. In the **Jamf API Response Mapping** field, enter the JSON Pointer syntax for the value of the matching Jamf Pro attribute.

      You can find help in [JSON Pointer syntax reference](pf_jamf_ik_json_pointer_syntax_reference.html).

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a - d.

4. On the **IdP Adapter** tab, configure the adapter instance by referring to [Jamf IdP Adapter settings reference](pf_jamf_ik_jamf_idp_adapter_settings_reference.html). Click **Next**.

5. On the **Actions** tab, test your connection to Jamf Pro. Resolve any issues that are reported, and then click **Next**.

6. On the **Extended Contract** tab, add any local attributes that mapped in the **Jamf API Attribute Mappings** section. Click **Next**.

7. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

8. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

9. On the **Summary** tab, check your configuration, then click **Save**.

---

---
title: Creating API credentials in Jamf Pro
description: To allow PingFederate to communicate with Jamf Pro, create a user account with READ privileges.
component: jamf
page_id: jamf:setup:pf_jamf_ik_creating_api_credentials_in_jamf_pro
canonical_url: https://docs.pingidentity.com/integrations/jamf/setup/pf_jamf_ik_creating_api_credentials_in_jamf_pro.html
revdate: November 4, 2025
section_ids:
  steps: Steps
---

# Creating API credentials in Jamf Pro

To allow PingFederate to communicate with Jamf Pro, create a user account with `READ` privileges.

## Steps

1. Sign on to Jamf Pro as an administrator.

2. Go to **Settings > System Settings > Jamf Pro user Accounts & Groups**.

3. Click **New**.

4. Select **Create Standard Account**. Click **Next**.

5. On the **Account** tab, enter a username and password.

   |   |                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------- |
   |   | You will use these values in [Configuring an adapter instance](pf_jamf_ik_configuring_an_adapter_instance.html). |

6. In the **Privilege Set** list, select **Custom**.

7. In the **Access Status** list, select **Enabled**.

8. On the **Privileges** tab, in the **Jamf Pro Server Objects** section, select `READ` for the following:

   * **Advanced Computer Searches**

   * **Advanced Mobile Device Searches**

   * **Computers**

   * **Mobile Devices**

9. Click **Save**.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Jamf Integration Kit files to your PingFederate directory.
component: jamf
page_id: jamf:setup:pf_jamf_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/jamf/setup/pf_jamf_ik_deploying_the_integration_files.html
revdate: November 4, 2025
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Jamf Integration Kit files to your PingFederate directory.

## Steps

1. Download the Jamf Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/jamf-pro-integration-kit).

2. Stop PingFederate, if it's running.

3. If you're upgrading an existing deployment, delete `pf-jamf-adapter-<version>.jar` from `<pf_install>/pingfederate/server/default/deploy`.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. Start PingFederate.

6. If you operate PingFederate in a cluster, repeat steps 2 - 5 for each engine node.

---

---
title: Download manifest
description: The following files are included in the Jamf Integration Kit .zip archive:
component: jamf
page_id: jamf:release_notes:pf_jamf_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/jamf/release_notes/pf_jamf_ik_download_manifest.html
revdate: November 4, 2025
---

# Download manifest

The following files are included in the Jamf Integration Kit `.zip` archive:

* `Legal.pdf`: Copyright and license information.

* `dist`: Contains the integration files.

  * `pf-jamf-adapter-<version>.jar`: A `.jar` file containing the Jamf IdP Adapter.

---

---
title: Jamf IdP Adapter settings reference
description: Field descriptions for the Jamf IdP Adapter configuration page.
component: jamf
page_id: jamf:setup:pf_jamf_ik_jamf_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/jamf/setup/pf_jamf_ik_jamf_idp_adapter_settings_reference.html
revdate: November 4, 2025
---

# Jamf IdP Adapter settings reference

Field descriptions for the Jamf IdP Adapter configuration page.

> **Collapse: Standard fields**
>
> | Field                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
> | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> | **API Username**          | The username you created in [Creating API credentials in Jamf Pro](pf_jamf_ik_creating_api_credentials_in_jamf_pro.html).                                                                                                                                                                                                                                                                                                                                    |
> | **API Password**          | The password you created in [Creating API credentials in Jamf Pro](pf_jamf_ik_creating_api_credentials_in_jamf_pro.html).                                                                                                                                                                                                                                                                                                                                    |
> | **API Hostname**          | The hostname for the Jamf Pro server.For example:- company-name.jamfcloud.com
>
> - jamf-pro.companyname.com:8443                                                                                                                                                                                                                                                                                                                                               |
> | **Device Identifier**     | The attribute used to uniquely identify the user's authentication device.&#xA;&#xA;The adapter gets this attribute from the device's X.509 certificate and uses it to query the Jamf Pro for the device's security posture.&#xA;&#xA;This attribute must be available in the core or extended of your X.509 Certificate IdP Adapter instance.The default selection is **Serial Number**.                                                                     |
> | **Device Type Attribute** | The attribute that identifies whether the device is a computer or mobile device.&#xA;&#xA;The adapter gets this attribute from the device's X.509 certificate and uses it to determine which Jamf Pro API to query.&#xA;&#xA;The value of the attribute must be computers or mobiledevices.&#xA;&#xA;If the device type is provided in this attribute, the value overrides the Possible Device Types setting.The default value is `deviceType`.              |
> | **Possible Device Types** | Determines which Jamf Pro API the adapter queries for a device's security posture.Jamf Pro provides two separate APIs, one for computers and the other for mobile devices. This setting allows you to eliminate unecessary calls to one API if your users all use the same device type (either computers or mobile devices).&#xA;&#xA;If a valid Device Type Attribute is available, that value overrides this setting.The default selection is `Computers`. |
> | **Failure Mode**          | Determines whether the adapter blocks the user's sign-on attempt when it can't find the device or the connection to Jamf Pro fails.The default selection is `Bypass authentication`.                                                                                                                                                                                                                                                                         |
> | **API Request Timeout**   | The amount of time, in milliseconds, that PingFederate allows when establishing a connection with Jamf Pro or waiting for a response to a request. A value of `0` disables the timeout.The default value is `5000`.                                                                                                                                                                                                                                          |
> | **Proxy Settings**        | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                                                                                                                                                                                                                                                  |
> | **Custom Proxy Host**     | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                               |
> | **Custom Proxy Port**     | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                    |

---

---
title: Jamf Integration Kit
description: The Jamf Integration Kit allows PingFederate to integrate with Jamf Pro for secure device management. This allows you to make dynamic policy decisions based on the security posture of a user's Apple device.
component: jamf
page_id: jamf::pf_jamf_ik
canonical_url: https://docs.pingidentity.com/integrations/jamf/pf_jamf_ik.html
revdate: November 4, 2025
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Jamf Integration Kit

The Jamf Integration Kit allows PingFederate to integrate with Jamf Pro for secure device management. This allows you to make dynamic policy decisions based on the security posture of a user's Apple device.

For example, you can:

* Deny access for users who have devices that aren't managed by Jamf Pro.

* Deny access to a user whose current device has been compromised or rooted.

* Allow access only for users who have compliant devices.

* Branch your authentication policy based on device attributes, such as operating system.

## Components

* Jamf IdP Adapter

  Allows PingFederate to get the security posture for the authenticating user's current device.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following resources:

* The [X.509 Certificate Integration Kit](../x509/x509_certificate_integration_kit/pf_x509_certificate_ik.html) documentation

* The following sections of the Jamf documentation:

  * [Managing Mobile Devices](https://docs.jamf.com/10.27.0/jamf-pro/administrator-guide/Managing_Mobile_Devices.html)

  * [Managing Computers](https://docs.jamf.com/10.27.0/jamf-pro/administrator-guide/Managing_Computers.html)

* The following sections of the PingFederate documentation:

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

## System requirements

* PingFederate 11.3 or later

* A Jamf Pro account (cloud or on-premises)

* An Apple mobile device managed by Jamf Pro, such as an Apple computer, iPhone, iPad, or Apple TV

---

---
title: JSON Pointer syntax reference
description: JavaScript Object Notation (JSON) Pointer defines a syntax for identifying a specific value within a JSON payload. Using the sample payload and JSON Pointer examples below, identify the attributes that you want to use to populate your attribute contract.
component: jamf
page_id: jamf:setup:pf_jamf_ik_json_pointer_syntax_reference
canonical_url: https://docs.pingidentity.com/integrations/jamf/setup/pf_jamf_ik_json_pointer_syntax_reference.html
revdate: November 4, 2025
section_ids:
  example-jamf-pro-json-payload-for-computers: Example Jamf Pro JSON payload for computers
  example-jamf-pro-json-payload-for-mobile-devices: Example Jamf Pro JSON payload for mobile devices
---

# JSON Pointer syntax reference

JavaScript Object Notation (JSON) Pointer defines a syntax for identifying a specific value within a JSON payload. Using the sample payload and JSON Pointer examples below, identify the attributes that you want to use to populate your attribute contract.

You can find a technical description of JSON Pointer syntax in [JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901) on ietf.org.

## Example Jamf Pro JSON payload for computers

|   |                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Portions of the following payload have been removed for brevity. You can find a complete example in [Find computers by ID](https://developer.jamf.com/jamf-pro/reference/findcomputersbyid) in the Jamf Pro API documentation. |

```json
{
    "computer": {
        "general": {
            "id": 1,
            "name": "Admins iMac",
            "ip_address": "10.1.1.1",
            "last_reported_ip": "192.0.0.1",
            "udid": "55900BDC-347C-58B1-D249-F32244B11D30",
            "jamf_version": "9.99.0-t1494340586",
            "platform": "Mac",
            "remote_management": {
                "managed": true,
                "management_username": "casperadmin"
            },
            "mdm_capable": true,
            "mdm_capable_users": {
                "mdm_capable_user": "string"
            },
            "management_status": {
                "enrolled_via_dep": true,
                "user_approved_enrollment": true,
                "user_approved_mdm": true
            },
            "site": {
                "id": 0,
                "name": "None"
            }
        },
        "location": {
            "username": "JBetty",
            "realname": "Betty Jackson",
            "real_name": "Betty Jackson",
            "email_address": "jbetty@company.com",
            "position": "Systems Engineer",
            "phone": "123-555-6789",
            "phone_number": "123-555-6789",
            "department": "Sales Staff",
            "building": "New York Office",
            "room": 1159
        },
        "groups_accounts": {
            "computer_group_memberships": [
                {
                    "group": "All Managed Clients"
                }
            ],
            "local_accounts": [
                {
                    "user": {
                        "name": "_amavisd",
                        "realname": "AMaViS Daemon",
                        "uid": 83,
                        "home": "/var/virusmails",
                        "home_size": "-1MB",
                        "home_size_mb": -1,
                        "administrator": false,
                        "filevault_enabled": false
                    }
                }
            ]
        },
        "configuration_profiles": [
            {
                "size": 1,
                "configuration_profile": {
                    "id": 1,
                    "name": "string",
                    "uuid": "string",
                    "is_removable": false
                }
            }
        ]
    }
}
```

**JSON Pointer syntax**

| Description                 | JSON Pointer                                                    | Example value     |
| --------------------------- | --------------------------------------------------------------- | ----------------- |
| Device IP address           | `/computer/general/ip_address`                                  | `10.1.1.1`        |
| User's name                 | `/computer/location/realname`                                   | `Betty Jackson`   |
| User's location             | `/computer/location/building`                                   | `New York Office` |
| User's administrator status | `/computer/groups_accounts/local_accounts/0/user/administrator` | `false`           |

|   |                                                                                                  |
| - | ------------------------------------------------------------------------------------------------ |
|   | To populate an attribute with the entire JSON response, leave the attribute mapping field blank. |

## Example Jamf Pro JSON payload for mobile devices

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Portions of the following payload have been removed for brevity. You can find a complete example in [Find mobile devices by ID](https://developer.jamf.com/jamf-pro/reference/findmobiledevicesbyid) in the Jamf Pro API documentation.```json
{
    "mobile_device": {
        "general": {
            "id": 1,
            "display_name": "Tinas iPad",
            "device_name": "Tinas iPad",
            "name": "Tinas iPad",
            "os_type": "iOS",
            "udid": "270aae10800b6e61a2ee2bbc285eb967050b5984",
            "phone_number": "123-555-6789",
            "ip_address": "192.0.0.1",
            "managed": true,
            "supervised": true
        },
        "location": {
            "username": "JBetty",
            "realname": "Betty Jackson",
            "real_name": "Betty Jackson",
            "email_address": "jbetty@company.com",
            "position": "Systems Engineer",
            "phone": "123-555-6789",
            "phone_number": "123-555-6789",
            "department": "Sales Staff",
            "building": "New York Office",
            "room": 1159
        },
        "security": {
            "data_protection": true,
            "block_level_encryption_capable": true,
            "file_level_encryption_capable": true,
            "passcode_present": true,
            "passcode_compliant": true,
            "passcode_compliant_with_profile": true,
            "passcode_lock_grace_period_enforced": "Not Available",
            "hardware_encryption": "string",
            "activation_lock_enabled": true,
            "jailbreak_detected": "Normal"
        },
        "network": {
            "home_carrier_network": "Verizon",
            "phone_number": 5555555555
        },
        "mobile_device_groups": [
            {
                "size": 1,
                "mobile_device_group": {
                    "id": 1,
                    "name": "string"
                }
            }
        ]
    }
}
``` |

**JSON Pointer syntax**

| Description             | JSON Pointer                                 | Example value     |
| ----------------------- | -------------------------------------------- | ----------------- |
| Device IP address       | `/mobile_device/general/ip_address`          | `192.0.0.1`       |
| User's name             | `/mobile_device/location/realname`           | `Betty Jackson`   |
| User's location         | `/mobile_device/location/building`           | `New York Office` |
| Device jailbreak status | `/mobile_device/security/jailbreak_detected` | `Normal`          |

|   |                                                                                                  |
| - | ------------------------------------------------------------------------------------------------ |
|   | To populate an attribute with the entire JSON response, leave the attribute mapping field blank. |

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the Jamf Integration Kit.
component: jamf
page_id: jamf:release_notes:pf_jamf_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/jamf/release_notes/pf_jamf_ik_known_issues_and_limitations.html
revdate: November 4, 2025
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the Jamf Integration Kit.

## Known issues

There are no known issues.

## Known limitations

* Advanced searches

  The Jamf IdP Adapter queries Jamf Pro with a unique device identifier (such as serial number) as described in [Simple Mobile Device Searches](https://docs.jamf.com/10.26.0/jamf-pro/administrator-guide/Simple_Mobile_Device_Searches.html) and [Simple Computer Searches](https://docs.jamf.com/10.26.0/jamf-pro/administrator-guide/Simple_Computer_Searches.html) in the Jamf Pro documentation. However, the adapter doesn't support advanced searches using criteria and operators.

---

---
title: Overview of the SSO flow
description: With the Jamf Integration Kit, PingFederate parses identifying attributes from the X.509 certificate on the user's Apple device. The Jamf IdP Adapter uses these attributes to get the device's security posture from Jamf Pro.
component: jamf
page_id: jamf::pf_jamf_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/jamf/pf_jamf_ik_overview_of_the_sso_flow.html
revdate: June 21, 2024
section_ids:
  description: Description
---

# Overview of the SSO flow

With the Jamf Integration Kit, PingFederate parses identifying attributes from the X.509 certificate on the user's Apple device. The Jamf IdP Adapter uses these attributes to get the device's security posture from Jamf Pro.

The following figure illustrates a single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* scenario in which PingFederate retrieves the security posture of a user's device during authentication.

![A diagram showing the authentication flow using the X.509 and Jamf integration kits.](_images/jamf-ik-sso-flow-overview-diagram.png)

## Description

1. The user initiates sign on with the service provider (SP) *(tooltip: \<div class="paragraph">
   \<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
   \</div>)* using a device enrolled with Jamf Pro.

2. The SP redirects the request to PingFederate. The browser provides the user's X.509 certificate.

3. The PingFederate X.509 Certificate identity provider (IdP) *(tooltip: \<div class="paragraph">
   \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
   \</div>)* Adapter validates the certificate against a specified list of issuers or the server's list of trusted certificate authorities, then parses the device information from the certificate.

4. The X.509 Certificate IdP Adapter provides the device type (mobile device or computer) and device identifier to the Jamf IdP Adapter.

5. The Jamf IdP Adapter provides the device identifier to Jamf Pro and requests the device's security posture.

6. Jamf Pro returns the device's security posture and a collection of other attributes.

7. PingFederate completes the sign-on flow or branches the authentication policy to a different result depending on the security posture result.

---

---
title: Setting up the X.509 Certificate Integration Kit
description: The Jamf Integration Kit requires the X.509 Certificate IdP Adapter to get device information from the device's client certificate.
component: jamf
page_id: jamf:setup:pf_jamf_ik_setting_up_the_x509_certificate_i
canonical_url: https://docs.pingidentity.com/integrations/jamf/setup/pf_jamf_ik_setting_up_the_x509_certificate_i.html
revdate: November 4, 2025
section_ids:
  steps: Steps
---

# Setting up the X.509 Certificate Integration Kit

The Jamf Integration Kit requires the X.509 Certificate IdP Adapter to get device information from the device's client certificate.

## Steps

1. Follow the steps in [Deploying the integration files](../../x509/x509_certificate_integration_kit/pf_x509_certificate_ik_deploying_the_integration_files.html) in the X.509 Certificate Integration Kit documentation.

2. Configure an adapter instance as shown in [Configuring an adapter instance](../../x509/x509_certificate_integration_kit/pf_x509_certificate_ik_configuring_an_adapter_instance.html) in the X.509 Certificate Integration Kit. Use the following details:

   1. On the **IdP Adapter** tab, in the **Advanced Fields** section, select the **Include Subject Alternative Name (SAN)** checkbox.

   2. On the **Extended Contract** tab, check that the device identifier and device type are available in either the core or extended contract.

      In the Jamf IdP Adapter configuration, you can specify that the device identifier is contained in one of the following attributes:

      * `deviceId`

      * `macAddress`

      * `serialNumber`

      * `udid`

      Depending on your certificate configuration, you might need to add one of these attributes to the extended contract.

      Optionally, you can also include an attribute that contains the device type. The value must be `computers` or `mobiledevices`.