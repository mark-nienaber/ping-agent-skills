---
title: Configuring a Twilio notification publisher instance
description: You can configure one of the Twilio notification publishers to allow PingFederate to send one-time passcodes (OTPs) using email, SMS message, or voice call.
component: otp
page_id: otp:setup:pf_otp_ik_configuring_a_twilio_notification_publisher_instance
canonical_url: https://docs.pingidentity.com/integrations/otp/setup/pf_otp_ik_configuring_a_twilio_notification_publisher_instance.html
revdate: January 14, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a Twilio notification publisher instance

You can configure one of the Twilio notification publishers to allow PingFederate to send one-time passcodes (OTPs) using email, SMS message, or voice call.

## About this task

|   |                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Instead of using a Twilio notification publisher, you can send email notifications directly from PingFederate by completing the steps in [Configuring an SMTP Notification Publisher instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_notificationsendermanagementstate_configureauthnadapterstate_smtp.html) in the PingFederate documentation. |

## Steps

1. Complete the steps in [Getting your Twilio API credentials](pf_otp_ik_getting_your_twilio_api_credentials.html).

2. Sign on to the PingFederate administrative console.

3. On the **System > External Systems > Notification Publishers** tab, click **Create New Instance**.

4. On the **Type** tab, set the basic notification publisher instance attributes.

   1. In the **Instance Name** field, enter a name for the notification publisher instance.

   2. In the **Instance ID** field, enter a unique identifier for the notification publisher instance.

   3. In the **Type** list, select **Twilio Verify API Notification Publisher** or **Twilio Programmable API Notification Publisher**. Click **Next**.

5. Configure the notification publisher by referring to [Twilio Programmable API Notification Publisher settings reference](pf_otp_ik_twilio_programmable_api_notification_publisher_settings_reference.html) or [Twilio Verify API Notification Publisher settings reference](pf_otp_ik_twilio_verify_api_notification_publisher_settings_reference.html). Click **Next**.

6. On the **Actions** tab, click **Test**. Resolve any issues that are reported, and then click **Next**.

7. On the **Summary** tab, check that the configuration is correct. Click **Done**.

8. On the **Notification Publishers** tab, click **Save**.

---

---
title: Configuring an adapter instance
description: Configure the One-Time Passcode IdP Adapter to allow PingFederate to use notification publishers to send one-time passcodes (OTPs) to users during sign-on.
component: otp
page_id: otp:setup:pf_otp_ik_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/otp/setup/pf_otp_ik_configuring_an_adapter_instance.html
revdate: October 6, 2025
section_ids:
  steps: Steps
  example: Example:
---

# Configuring an adapter instance

Configure the One-Time Passcode IdP Adapter to allow PingFederate to use notification publishers to send one-time passcodes (OTPs) to users during sign-on.

## Steps

1. Sign on to the PingFederate admin console.

2. On the **Identity Provider > Adapters** tab, click **Create New Instance**.

3. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **One-Time Passcode IdP Adapter**. Click **Next**.

4. On the **IdP Adapter** tab, in the **Notification Delivery Methods** section, configure a list of delivery methods by assigning contact information and message templates to your notification publishers.

   1. Click **Add a new row to 'Notification Delivery Methods'**.

   2. In the **Notification Publisher** list, select the notification publisher that you want to use.

   3. In the **Contact Attribute** list, enter the attribute that contains the user's contact information for this delivery method. For example, `email`, or `phone`.

   4. In the **Language Properties and Templates Key** field, enter a key. You can find an explanation of keys in [Language property and template keys](pf_otp_ik_language_property_and_template_keys.html).

   5. In the **Action** column, click **Update**.

   6. To add more delivery methods, repeat steps a - e.

   7. Change the order of the delivery methods to define the sequence that the adapter attempts the deliveries when **Device Selection** is set to **Automatic**.

5. On the **IdP Adapter** tab, in the **User Attribute Mapping** section, configure user data mapping from the chained attribute to the target attribute.

   1. Click **Add a new row to 'User Attribute Mapping'**.

   2. In the **Source User Attribute** field, enter the name of the source attribute that contains the user information.

   3. In the **Target User Attribute** field, enter the name of the target attribute to use in the `otp.adapter*` templates and authentication API responses.

   4. In the **Action** column, click **Update**.

   5. To add more user information attributes, repeat steps a - d.

      ### Example:

      | Chained Attribute | Target Attribute |
      | ----------------- | ---------------- |
      | firstName         | first\_name      |
      | lastName          | last\_name       |
      | title             | title            |

      If the chained attributes contain acceptable values for the `firstName`, `lastName`, and `title` attributes, the One-Time Passcode IdP Adapter assigns the values to `first_name`, `last_name`, and `title`.

      In the `otp.adapter*` templates, these attributes are accessible using the following velocity template variables:

      * `$userData.first_name`

      * `$userData.last_name`

      * `$userData.title`

      In the Authentication API `DEVICE_SELECTION_REQUIRED` and `OTP_REQUIRED` response model states, the `userData` object contains the mapped attributes.

      |   |                                                                                                                                                                                                                                                                                                                                        |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The attributes you add with this table are available for reference and use only within the four user-facing browser templates that are directly rendered by the adapter. You can find a list of these `otp.adapter*` templates and more information about using them in [Customizing templates](pf_otp_ik_customizing_templates.html). |

6. Configure the adapter instance by referring to [One-Time Passcode IdP Adapter settings reference](pf_otp_ik_one_time_passcode_idp_adapter_settings_reference.html). Click **Next**.

7. On the **Actions** tab, test your connection to the database. Resolve any issues that are reported, and then click **Next**.

8. On the **Extended Contract** tab, add any attributes that you expect to retrieve in addition to the core contract attributes. Click **Next**.

9. Complete the adapter configuration.

10. On the **Summary** tab, check that the configuration is correct. Click **Done**.

11. On the **Manage IdP Adapter Instances** tab, click **Save**.

12. Modify your PingFederate authentication policy to include your One-Time Passcode IdP Adapter instance. Position it after a first-factor authentication step, such as the HTML Form IdP Adapter.

    You can find general information about configuring authentication policies in [Policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/qmq1564002987890.html) in the PingFederate documentation.

---

---
title: Customizing templates
description: The One-Time Passcode Integration Kit includes templates that can present one-time passcode (OTP) authentication challenges and other messages.
component: otp
page_id: otp:setup:pf_otp_ik_customizing_templates
canonical_url: https://docs.pingidentity.com/integrations/otp/setup/pf_otp_ik_customizing_templates.html
revdate: April 22, 2025
---

# Customizing templates

The One-Time Passcode Integration Kit includes templates that can present one-time passcode (OTP) *(tooltip: \<div class="paragraph">
\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
\</div>)* authentication challenges and other messages.

* You can customize the HTML portions of these templates to suit your organization's branding and presentation needs.

* You can use the **HTML Prefix Field** to configure adapter instance-specific templates. Learn more in the [One-Time Passcode IdP Adapter settings reference](pf_otp_ik_one_time_passcode_idp_adapter_settings_reference.html).

* You can access the user information attributes configured in the **User Attribute Mapping** table during the [Configuring an adapter instance](pf_otp_ik_configuring_an_adapter_instance.html) procedure in the templates using the `$userData.<target_attribute_name>` velocity variable.

The following table lists the available templates and their uses. You can find more information about templates in [Customizable user-facing pages](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_custom_user_facing_pages.html) in the PingFederate documentation.

**Template files included in the One-Time Passcode Integration Kit**

| Template file                                | Description                                                                                           |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `otp.adapter.device.selection.template.html` | Presents the user with a form to select a device on which to receive the OTP.                         |
| `otp.adapter.mfa.failed.template.html`       | Presents the user with a form to indicate failed verification of the OTP they entered previously.     |
| `otp.adapter.otp.required.template.html`     | Presents the user with a form to input the OTP.                                                       |
| `otp.adapter.otp.verified.template.html`     | Presents the user with a form to indicate successful verification of the OTP they entered previously. |

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the One-Time Passcode Integration Kit files to your PingFederate directory.
component: otp
page_id: otp:setup:pf_otp_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/otp/setup/pf_otp_ik_deploying_the_integration_files.html
revdate: October 6, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the One-Time Passcode Integration Kit files to your PingFederate directory.

## Before you begin

Download the integration kit `.zip` archive from the [**Add-ons** tab on the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/onetime-passcode-integration-kit).

## Steps

1. Stop PingFederate, if it's running.

2. If you're upgrading from a previous deployment, do the following:

   1. Back up any One-Time Passcode Integration Kit files you customized in `<pf_install>/pingfederate/server/default/conf/`.

   2. Delete `pf-one-time-passcode-adapter-<version>.jar` from `<pf_install>/pingfederate/server/default/deploy`.

   3. Delete `pf-authn-api-sdk-<version>.jar` from `<pf_install>/pingfederate/server/default/lib` if it's older than the version in the integration files.

3. Extract the `.zip` archive and copy the contents of the `dist` directory to `<pf_install>`.

4. If you want to use the SMTP Notification Publisher, merge the contents of the `pingfederate-smtp-otp-messages.properties` file into the `<pf_install>/pingfederate/server/default/conf/language-packs/pingfederate-email-messages.properties` file.

5. If you backed up templates or messages from a previous deployment, modify the new files with your customizations.

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 1 - 6 for each instance of PingFederate.

---

---
title: Download manifest
description: The following files are included in the One-Time Passcode Integration Kit:
component: otp
page_id: otp:release_notes:pf_otp_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/otp/release_notes/pf_otp_ik_download_manifest.html
revdate: January 6, 2026
---

# Download manifest

The following files are included in the One-Time Passcode Integration Kit:

* `ReadMeFirst.pdf`: Contains links to this online documentation.

* `legal`: A directory that contains this document:

  * `Legal.pdf`: Copyright and license information.

* `dist`: A directory that contains integration files.

  * `conf`: A directory that contains configuration files.

    * `language-packs`: A directory that contains language template files.

      * `pingfederate-otp-adapter-messages.properties`: A variable file that customizes the messages that appear in template files.

      * `pingfederate-smtp-otp-messages.properties`: A variable file that customizes the messages that appear on the SMTP template file.

      * `twilio-programmable-api-publisher-messages.properties`: A variable file that customizes the messages that appear on the Twilio SMS template file.

    * `template`: A directory that contains language template files.

      * `assets`: A directory that contains style, font, and image files for the template files.

        * `css/otp-adapter.css`: A CSS file that customizes the appearance of the template file.

        * `fonts/end-user`: Contains fonts and icons used in the template file.

          * `icons`: Contains an icon font used in the template file.

        * `images`: Contains sample logos and delivery method icons used in the template file.

      * `mail-notifications`: A directory that contains email template files.

        * `pingfederate.smtp.otp.adapter.template.html`: A sample template file that the SMTP Notification Publisher can use to send a one-time passcode in an email.

      * `otp.adapter.device.selection.template.html`: A sample template file that allows the user to select a delivery method for the passcode.

      * `otp.adapter.mfa.failed.template.html`: A sample template file that shows a message when the passcode fails.

      * `otp.adapter.otp.required.template.html`: A sample template file that allows a user to enter a passcode.

      * `otp.adapter.otp.verified.template.html`: A sample template file that shows a message when the passcode succeeds.

      * `twilio.sms.otp.adapter.template.html`: A sample template file that the Twilio Programmable API Notification Publisher can use to send a one-time passcode in an SMS message.

      * `twilio.voice.otp.adapter.template.html`: A sample template file that the Twilio Programmable API Notification Publisher can use to send a one-time passcode in a voice message.

  * `deploy`: A directory that contains the Java libraries needed to run the adapter and Twilio notification publishers.

    * `pf-one-time-passcode-adapter-<version>.jar`: A JAR file that contains the One-Time Passcode IdP Adapter.

    * `twilio-programmable-api-notification-plugin-<version>.jar`: A JAR file that contains the Twilio Programmable API Notification Publisher.

    * `twilio-verify-api-notification-plugin-<version>.jar`: A JAR file that contains the Twilio Verify API Notification Publisher.

  * `lib`: A directory that contains PingFederate core library files.

    * `pf-authn-api-sdk-<version>.jar`: A JAR file that contains the PingFederate Authentication API SDK.

---

---
title: Getting your Twilio API credentials
description: To use the Twilio notification publishers, configure your Twilio account and note your credentials.
component: otp
page_id: otp:setup:pf_otp_ik_getting_your_twilio_api_credentials
canonical_url: https://docs.pingidentity.com/integrations/otp/setup/pf_otp_ik_getting_your_twilio_api_credentials.html
revdate: April 21, 2025
section_ids:
  steps: Steps
---

# Getting your Twilio API credentials

To use the Twilio notification publishers, configure your Twilio account and note your credentials.

## Steps

1. Sign on to the [Twilio Console](https://www.twilio.com/console).

2. Create an account as described in [View and Create New Accounts in Twilio Console](https://help.twilio.com/articles/27256720639899-View-and-Create-New-Accounts-in-Twilio-Console) in the Twilio documentation.

3. Note the **Account SID** and **Auth Token**.

   Learn more in [Auth Tokens and How to Change Them](https://support.twilio.com/hc/en-us/articles/223136027-Auth-Tokens-and-How-to-Change-Them) in the Twilio documentation.

4. If you want to use the Twilio Verify API Notification Publisher, do the following:

   1. On the [Twilio Verify Services](https://www.twilio.com/console/verify/services) page in the Twilio Console, create a service.

   2. Note the **Service ID**.

   3. In the **Code Customization** section, enable **Custom Code**.

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the One-Time Passcode Integration Kit.
component: otp
page_id: otp:release_notes:pf_otp_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/otp/release_notes/pf_otp_ik_known_issues_and_limitations.html
revdate: April 14, 2025
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the One-Time Passcode Integration Kit.

## Known issues

There are no known issues.

## Known limitations

* When PingFederate is operating in standalone mode, changes you make to an existing notification publisher configuration don't take effect until you save the corresponding adapter instance again.

* Passcodes are associated with a particular PingFederate session, which causes the following known limitations:

  * The one-time passcode (OTP) timeout value cannot be controlled. The OTP won't expire as long as it isn't used or the PingFederate session isn't expired.

  * You can't refresh the OTP value using resend request.

* This integration kit is intentionally designed as a simpler version of multi-factor authentication (MFA) without full features and will not add any new feature in the future.

  * For full-featured MFA operation, PingOne MFA or PingID is recommended.

---

---
title: Language property and template keys
description: The Language Property and Template Keys that you define in the One-Time Passcode IdP Adapter instance configuration affect the messages and prompts shown to end users.
component: otp
page_id: otp:setup:pf_otp_ik_language_property_and_template_keys
canonical_url: https://docs.pingidentity.com/integrations/otp/setup/pf_otp_ik_language_property_and_template_keys.html
revdate: April 28, 2025
section_ids:
  using-the-pingfederate-authentication-api: Using the PingFederate authentication API
  user-interface: User interface
  smtp-notification-publisher: SMTP Notification Publisher
  twilio-programmable-api-notification-publisher: Twilio Programmable API Notification Publisher
---

# Language property and template keys

The **Language Property and Template Keys** that you define in the One-Time Passcode IdP Adapter instance configuration affect the messages and prompts shown to end users.

The adapter uses these keys in different ways depending on how the adapter is accessed and which notification publisher it interacts with.

## Using the PingFederate authentication API

When the PingFederate authentication API provides your web application with a list of notification delivery methods, it includes the **Language Property and Template Keys** value as the device type.

By having your web application read the device type, you can set different icons or formatting for each delivery method.

In the example below, the authentication API is prompting the web application to select a delivery method. The methods are defined with these three keys: `VOICE`, `SMS`, and `EMAIL`.

![The Notification Delivery Methods table](_images/NotificationDeliveryMethods.jpg)

```json
{
  "id": "G1j8b",
  "pluginTypeId": "7r5wldvoQS8iEJEpdMYqmA",
  "status": "DEVICE_SELECTION_REQUIRED",
  "devices": [
    {
      "id": "7337a6ac-98b2-4c02-9afd-82aa9f6b55c7",
      "type": "VOICE",
      "target": "+155*\**55"
    },
    {
      "id": "2ac3e6a8-5b3e-4247-b7d8-4d12cec8b9da",
      "type": "SMS",
      "target": "+155**\*55"
    },
    {
      "id": "b6cbaeff-bea2-4cfd-a0fd-3ffe6907df39",
      "type": "EMAIL",
      "target": "an****@example.com"
    }
  ],
  "user": {
    "username": "anonymous"
  },
  "_links": {
    "cancelAuthentication": {
      "href": "https://pf-host:9031/pf-ws/authn/flows/G1j8b"
    },
    "selectDevice": {
      "href": "https://pf-host:9031/pf-ws/authn/flows/G1j8b"
    },
    "self": {
      "href": "https://pf-host:9031/pf-ws/authn/flows/G1j8b"
    }
  }
}
```

## User interface

The template files included in the integration kit show information about your OTP delivery methods. To do this, they use lines from the `pingfederate-otp-adapter-messages.properties` file that begin with the **Language Properties and Templates Key** that you define for each delivery method.

For example, you configure a delivery method with a **Language Properties and Templates Key** value of `sms` . When asking the user to enter a passcode for that delivery method, the adapter uses the following lines to generate the page:

```
sms.otp.adapter.otp.required.template.header=SMS Authentication
sms.otp.adapter.otp.required.template.message=Enter the passcode you received to continue.
sms.otp.adapter.otp.required.template.otp.sent.text=SMS sent to:
sms.otp.adapter.otp.required.template.resend.button.title=Resend
```

By default, the `pingfederate-otp-adapter-messages.properties` file has messages defined for the following keys:

* `email`

* `sms`

* `voice`

You can modify the existing messages, or add your own using a new prefix.

|   |                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When using the SMTP Notification Publisher or the Twilio Programmable API Notification Publisher, the key determines the template file that forms the message body.`.otp.adapter.template.html` is a file name suffix appended to the prefix key you configured in the **Language Properties and Templates Key** field. |

## SMTP Notification Publisher

When using the SMTP Notification Publisher, the key determines the template file that forms the body of the email message.

For example, if you enter `pingfederate.smtp` in the **Language Properties and Templates Key** field, the adapter will use the `<pf_install>/pingfederate/server/default/conf/template/mail-notifications/pingfederate.smtp.otp.adapter.template.html` file as the body of the email message.

If you are also using the user interface, the adapter will check the `pingfederate-otp-adapter-messages.properties` file for message lines that begin with `pingfederate.smtp`. Modify the file accordingly.

## Twilio Programmable API Notification Publisher

When using the Twilio Programmable API Notification Publisher, the key determines the template file that forms the body of the notification SMS or voice call.

For example, if you enter `twilio.sms` in the **Language Properties and Templates Key** field, the adapter will use the `<pf_install>/pingfederate/server/default/conf/template/twilio.sms.otp.adapter.template.html` file as the body of the SMS message.

If you are also using the user interface, the adapter will check the `pingfederate-otp-adapter-messages.properties` file for message lines that begin with `twilio.sms`. Modify the file accordingly.

---

---
title: One-Time Passcode IdP Adapter settings reference
description: Field descriptions for the One-Time Passcode IdP Adapter configuration page.
component: otp
page_id: otp:setup:pf_otp_ik_one_time_passcode_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/otp/setup/pf_otp_ik_one_time_passcode_idp_adapter_settings_reference.html
revdate: April 22, 2025
---

# One-Time Passcode IdP Adapter settings reference

Field descriptions for the **One-Time Passcode IdP Adapter** configuration page.

> **Collapse: Standard fields**
>
> | Field                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
> | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Device Selection**                    | * Automatic
>
>   The adapter uses the method from the **Preferred Delivery Method Attribute** or uses the first delivery method that it matches in the **Notification Delivery Methods** list.
>
> * User Choice
>
>   The adapter prompts the user to choose the delivery method.                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | **Preferred Delivery Method Attribute** | The source attribute that contains the user's preferred one-time passcode (OTP) delivery method.If the user has a valid preferred delivery method attribute, it overrides the **Automatic** and **User choice** options above.For example, you enter `OTPPreference` in this field. You also create a user attribute called `OTPPreference` in your datastore or pass it to this adapter as a chained attribute.When Alice signs on, the adapter checks her `OTPPreference` attribute. The value is `sms`, which matches one of the **Language Properties and Template Key** entries in the **Notification Delivery Methods** table. The adapter automatically sends the OTP to Alice by SMS message. |
> | **Attribute Source**                    | The source of the attribute in the **Preferred Delivery Method Attribute** field and the attributes listed in the **Contact Attribute** column of the **Notification Delivery Methods** table.Select a datastore, or select **Chained Attributes** if the adapter receives the attributes from earlier in the authentication flow.                                                                                                                                                                                                                                                                                                                                                                    |
> | **Search String**                       | The string that the adapter uses to search the datastore to find the user.* For JDBC, enter a "select" statement. For example, `select email, phone from <db.table> where username=${userid}`.
>
> * For LDAP, enter an LDAP filter. For example, `sAMAccountName=${userid}`.
>
> * For a PingOne datastore, enter the attribute. For example, `username=${userid}` or `id=${userid}`s.
>
> * For REST API datastores, enter the resource path appended to the base URL of the REST API datastore. For example, `/users?uid=${userid}`.The `${userid}` variable contains the user ID. Your adapter instance receives this from earlier in your PingFederate authentication flow.                               |
> | **Base DN**                             | The base DN that the adapter uses when connecting to an LDAP datastore.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
> | **Test User ID**                        | The user ID used to test the configuration on the **Actions** tab.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | **Failure Mode**                        | This setting determines whether the adapter should block the user's sign-on attempt or bypass the OTP requirement when the adapter can't find the user or contact information in the datastore or chained attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

> **Collapse: Advanced fields**
>
> | Field                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> | **HTML Template Prefix**               | A file prefix identifying the customizable HTML templates that the adapter instance uses. The default value is:`otp.adapter.`&#xA;&#xA;You must keep the following files in the \<pf\_home>/server/default/conf/template folder:&#xA;&#xA;\<HTML Template Prefix>device.selection.template.html&#xA;&#xA;\<HTML Template Prefix>otp.verified.template.html&#xA;&#xA;\<HTML Template Prefix>otp.required.template.html&#xA;&#xA;\<HTML Template Prefix>mfa.failed.template.html |
> | **Visible Leading Characters Length**  | The length of the leading characters to display for email and phone number formats that don't pass the built-in validation check.                                                                                                                                                                                                                                                                                                                                              |
> | **Visible Trailing Characters Length** | The length of the trailing characters to display for email and phone number formats that don't pass the built-in validation check.                                                                                                                                                                                                                                                                                                                                             |
> | **OTP Length**                         | Length of the OTP generated by the adapter.The default value is `6`.                                                                                                                                                                                                                                                                                                                                                                                                           |
> | **Max OTP Attempts**                   | The maximum number of times the user is allowed to try entering the OTP before authentication fails.The default value is `3`.                                                                                                                                                                                                                                                                                                                                                  |
> | **Max OTP Resends**                    | The maximum number of times the user is allowed to request a specific OTP to be sent. After reaching this limit, the `Resend` button on the passcode entry prompt no longer resends the passcode.The default value is `15`.                                                                                                                                                                                                                                                    |
> | **Show Success Screens**               | Determines whether the adapter shows an authentication success screen to the user.This checkbox is selected by default.                                                                                                                                                                                                                                                                                                                                                        |
> | **Show Error Screens**                 | Determines whether the adapter shows an authentication error screen to the user.This checkbox is selected by default.                                                                                                                                                                                                                                                                                                                                                          |
> | **OTP Generator Field**                | A read-only value used by the adapter.	Do not edit this field.This field is hidden in PingFederate 10.0 and later.                                                                                                                                                                                                                                                                                                                                                             |
> | **LDAP Search Scope**                  | When the attribute source is an LDAP datastore, this setting determines the scope of the user search.- Single Level
>
>   Searches the immediate children of the base object, but excludes the base object itself.
>
> - Include Subtree (default)
>
>   Searches all child objects as well as the base object.                                                                                                                                                                         |

---

---
title: One-Time Passcode Integration Kit
description: The One-Time Passcode Integration Kit allows PingFederate to send one-time passcodes (OTPs) through a variety of notification publishers. The OTPs can be used as a second authentication factor for single sign-on.
component: otp
page_id: otp::pf_otp_ik
canonical_url: https://docs.pingidentity.com/integrations/otp/pf_otp_ik.html
revdate: April 21, 2025
section_ids:
  features: Features
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# One-Time Passcode Integration Kit

The One-Time Passcode Integration Kit allows PingFederate to send one-time passcodes (OTPs) through a variety of notification publishers. The OTPs can be used as a second authentication factor for single sign-on.

## Features

* Includes a customizable user interface that allows users to select an OTP delivery method and enter a passcode.

* Supports the PingFederate Authentication API, allowing you to integrate it into your existing web-based sign-on application.

* Supports existing PingFederate notification publishers.

## Components

* One-Time Passcode IdP Adapter

  * Allows PingFederate to trigger a notification publisher to send an OTP to a user during sign-on.

  * Accesses user contact information from data store attributes or from earlier in the authentication flow.

  * Validates passcodes entered by users.

* Language packs

  * Allow you to customize the messages shown to the user during authentication.

* Templates

  * Allow you to modify the appearance of pages shown to the user during authentication.

* Twilio Programmable API Notification Publisher

  * Allows you to send OTP messages through SMS and voice with a customizable message body.

* Twilio Verify API Notification Publisher

  * Allows you to send OTP messages through SMS, voice, and email (with the SendGrid addon). This option supports localization but not customizable messages.

## Intended audience

This document is intended for PingFederate administrators.

Before starting, you should familiarize yourself with the following sections of the PingFederate documentation:

* [Authentication applications and the authentication API](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_applications_authentication_api.html)

* [Managing notification publisher instances](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_notificationsendertasklet_notificationsendermanagementstate.html)

* [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

* [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

## System requirements

* PingFederate 11.3 or later

---

---
title: One-Time Passcode Integration Kit changelog
description: The following is the change history for the One-Time Passcode Integration Kit.
component: otp
page_id: otp:release_notes:pf_otp_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/otp/release_notes/pf_otp_ik_changelog.html
revdate: March 30, 2026
section_ids:
  version-1-1-3: Version 1.1.3
  version-1-1-2: Version 1.1.2
  version-1-1-1: Version 1.1.1
  version-1-1: Version 1.1
  version-1-0-2: Version 1.0.2
  version-1-0-1: Version 1.0.1
  version-1-0: Version 1.0
---

# One-Time Passcode Integration Kit changelog

The following is the change history for the One-Time Passcode Integration Kit.

## Version 1.1.3

Released in March 2026.

* Fixed an issue with authentication handling. Learn more in security bulletin [SECADV053](https://support.pingidentity.com/s/article/SECADV053-PingFederate-OTP-Integration-Kit-authentication-bypass) (requires sign-on).

## Version 1.1.2

Released in January 2026.

* Removed third-party fonts.

## Version 1.1.1

Released in October 2025.

* Fixed an issue with authentication handling. Learn more in security bulletin [SECADV051](https://support.pingidentity.com/s/article/SECADV051-PingFederate-OTP-Integration-Kit-authentication-bypass) (requires sign-on).

## Version 1.1

Released in April 2025.

* Added a default masking mechanism for arbitrary emails and phone number formats that fail the built-in validation.

  Learn more in the **Visible Leading Characters Length** and **Visible Trailing Characters Length** table entries in the [One-Time Passcode IdP Adapter settings reference](../setup/pf_otp_ik_one_time_passcode_idp_adapter_settings_reference.html).

* Added the ability to customize velocity templates for specific adapter instances.

  Learn more in the **HTML Template Prefix** table entry in the [One-Time Passcode IdP Adapter settings reference](../setup/pf_otp_ik_one_time_passcode_idp_adapter_settings_reference.html).

* Added the ability to pass dynamic user information to velocity templates.

  Learn more in step 5 of the [Configuring an adapter instance](../setup/pf_otp_ik_configuring_an_adapter_instance.html) procedure.

* Added the ability to use a **Messaging Service SID** with the Twilio Programmable API Notification Publisher.

  Learn more in the **Messaging Service SID** table entry in the [Twilio Programmable API Notification Publisher settings reference](../setup/pf_otp_ik_twilio_programmable_api_notification_publisher_settings_reference.html).

* Upgraded the Twilio SDK jar used in the Twilio Programmable API Notification Publisher and the Twilio Verify API Notification Publisher.

## Version 1.0.2

Released in August 2023.

* Fixed an issue that prevented the One-Time Passcode IdP Adapter from creating LDAPS datastore connections.

* Fixed an issue with an invalid URL in the adapter CSS.

* Upgraded the Apache Commons Text library to version 1.10.0 to follow best practices for [CVE-2022-42889](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42889).

  |   |                                                                     |
  | - | ------------------------------------------------------------------- |
  |   | The One-Time Passcode IdP Adapter was not vulnerable to this issue. |

## Version 1.0.1

Released in June 2021.

* Fixed an issue that caused an error when a PingFederate node loaded the adapter while a user was authenticating.

## Version 1.0

Released in June 2020.

* Initial release.

* Added the ability to use the adapter with a UI or through the PingFederate authentication API.

* Added the ability to look up user device details in a data store attached to PingFederate.

* Added the ability to use chained attributes from earlier in the authentication flow.

* Added the ability to allow users to choose their delivery method.

* Added the ability to stop or continue authentication when the data store lookup fails.

* Added the ability to send one-time passcodes through PingFederate notification publishers.

* Added the Twilio Verify API Notification Publisher.

* Added the Twilio Programmable API Notification Publisher.

---

---
title: Overview of one-time passcodes
description: The One-Time Passcode Integration Kit generates passcodes that the user must enter to complete the authentication flow.
component: otp
page_id: otp::pf_otp_ik_overview_of_one_time_passcodes
canonical_url: https://docs.pingidentity.com/integrations/otp/pf_otp_ik_overview_of_one_time_passcodes.html
revdate: April 14, 2025
section_ids:
  passcode-storage: Passcode storage
  passcode-duration: Passcode duration
---

# Overview of one-time passcodes

The One-Time Passcode Integration Kit generates passcodes that the user must enter to complete the authentication flow.

## Passcode storage

PingFederate does not store one-time passcodes (OTPs) at any time. Instead, passcodes are generated based on several components that are stored in memory, including a nonce value, a transaction ID, and a secret value associated with the adapter instance.

## Passcode duration

Passcodes are associated with a particular PingFederate session. Although the passcodes themselves do not expire, they can only be used once and only for the associated session and authentication flow. When the authentication flow ends, the passcode is no longer valid.

---

---
title: Overview of the SSO flow
description: With the One-Time Passcode Integration Kit, PingFederate sends a one-time passcode (OTP) to the user as part of the sign-on flow.
component: otp
page_id: otp::pf_otp_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/otp/pf_otp_ik_overview_of_the_sso_flow.html
revdate: April 14, 2025
section_ids:
  description: Description
---

# Overview of the SSO flow

With the One-Time Passcode Integration Kit, PingFederate sends a one-time passcode (OTP) *(tooltip: \<div class="paragraph">
\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
\</div>)* to the user as part of the sign-on flow.

The following figure shows how the One-Time Passcode IdP Adapter integrates with the sign-on process:

![The PingFederate sign-on flow including the One-Time Passcode IdP Adapter](_images/SSO_flow_diagram.jpg)

## Description

1. The user initiates single sign-on (SSO) with PingFederate and completes the first-factor authentication step, such as an HTML Form Adapter instance.

2. If the adapter is configured to allow user selection:

   1. The adapter presents a list of OTP delivery methods to the user.

   2. The user selects an OTP delivery method.

3. The adapter gets the user's contact information from a datastore or an attribute passed from earlier in the authentication flow.

4. The adapter sends the user an OTP in an email, SMS message, or automated voice call.

5. The user enters the OTP in the browser.

6. The adapter validates the OTP.

7. PingFederate grants access to the requested resource.

---

---
title: Overview of the Twilio notification publishers
description: The One-Time Passcode Integration Kit includes two Twilio-based notification publishers. They use two Twilio APIs that offer different features and behavior.
component: otp
page_id: otp::pf_otp_ik_overview_of_the_twilio_notification_publishers
canonical_url: https://docs.pingidentity.com/integrations/otp/pf_otp_ik_overview_of_the_twilio_notification_publishers.html
revdate: April 14, 2025
section_ids:
  twilio-programmable-api-notification-publisher: Twilio Programmable API Notification Publisher
  twilio-verify-api-notification-publisher: Twilio Verify API Notification Publisher
---

# Overview of the Twilio notification publishers

The One-Time Passcode Integration Kit includes two Twilio-based notification publishers. They use two Twilio APIs that offer different features and behavior.

## Twilio Programmable API Notification Publisher

* Uses the Twilio Programmable API, a generic messaging API.

* Supports SMS messages and voice calls. Learn more in [Programmable SMS](https://www.twilio.com/sms) and [Programmable Voice](https://www.twilio.com/voice) in the Twilio documentation.

* Allows you to manually customize or localize messages using the templates and message files included in this integration.

* Allows you to redact the last four digits of phone numbers that appear in the Twilio administrator console. Learn more in [Message Redaction Supports Phone Number and Content Privacy for Sensitive Applications](https://www.twilio.com/blog/protect-customer-privacy-with-redaction) in the Twilio blog and the Twilio [Message Redaction](https://ahoy.twilio.com/message-redaction) request form.

## Twilio Verify API Notification Publisher

* Uses the newer Twilio Verify API, which is designed to send one-time passcodes (OTPs). Learn more in [Verify](https://www.twilio.com/verify) in the Twilio documentation.

* Supports SMS messages, voice calls, and email.

* SMS and voice calls do not support message customization, but they do support automatic localization of the default messages.

* Email support is provided through an integration between Twilio and SendGrid. It allows some customization. Learn more in [Send Serverless Emails using SendGrid and Twilio Functions](https://www.twilio.com/blog/send-serverless-emails-sendgrid-twilio-functions) in the Twilio documentation.

* Shows phone numbers in clear text in the Twilio administrator console for 30 days after each transaction. Phone numbers are encrypted in the backend server at all times.

---

---
title: PingFederate Authentication API support
description: The PingFederate Authentication API provides access to the current state of the authentication flow as a user steps through the PingFederate authentication policy. You can use the PingFederate Authentication API to integrate the One-Time Passcode IdP Adapter into your application.
component: otp
page_id: otp::pf_otp_ik_authentication_api_support
canonical_url: https://docs.pingidentity.com/integrations/otp/pf_otp_ik_authentication_api_support.html
revdate: October 6, 2025
section_ids:
  models-objects-and-error-codes: Models, objects, and error codes
  objects: Objects
  error-codes: Error codes
---

# PingFederate Authentication API support

The PingFederate Authentication API provides access to the current state of the authentication flow as a user steps through the PingFederate authentication policy. You can use the PingFederate Authentication API to integrate the One-Time Passcode IdP Adapter into your application.

You can also explore the process using the PingFederate Authentication API Explorer. Learn more in the following sections of the PingFederate documentation:

* [PingFederate Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html)

* [Exploring the Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_exploring_authentication_api.html)

|   |                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | HTTP method contract:* `GET /pf-ws/authn/flows/{flowId}` always returns the current state. The response never changes state, regardless of query parameters.

* All state transitions are `POST`-only actions. A `POST` request that's invalid for the current state returns an `INVALID_ACTION_ID` `400` error. |

To integrate the One-Time Passcode IdP Adapter into your authentication flow, configure your application based on the information in this section.

## Models, objects, and error codes

When using the One-Time Passcode Integration Kit through the PingFederate Authentication API, the adapter uses the following state models, action models, objects, and error codes.

> **Collapse: State models**
>
> | Status                      | Request model                                                                                                                                                                                         | Action                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                  |
> | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `DEVICE_SELECTION_REQUIRED` | * `devices`
>
>   The list of devices associated with the user.
>
> * `user`
>
>   The authenticating user's username.
>
> * `userData`
>
>   The user info object.                                                  | - `selectDevice`
>
> - `cancelAuthentication`                              | Indicates that device selection is required because the user might have more than one device.To continue, the user must select a device for multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">&#xA;\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>&#xA;\</div>)*.  |
> | `OTP_REQUIRED`              | * `devices`
>
>   The list of devices associated with the user.
>
> * `user`
>
>   The authenticating user's username.
>
> * `selectedDeviceRef`
>
>   The device identifier.
>
> * `userData`
>
>   The user info object. | - `checkOtp`
>
> - `cancelAuthentication`
>
> - `selectDevice`
>
> - `resendOtp` | Indicates that a one-time passcode (OTP) *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)* is required.To continue, the user must enter the OTP sent to them through either SMS, voice call, or email. |
> | `OTP_VERIFIED`              | This state has no model.                                                                                                                                                                              | * `continueAuthentication`                                              | Indicates that the user has completed MFA using an OTP.                                                                                                                                                                                                                                                                                                                                      |
> | `MFA_FAILED`                | - `code`
>
>   The error code.
>
> - `message`
>
>   The developer-facing error message.
>
> - `userMessage`
>
>   The user-facing error message.                                                                    | * `cancelAuthentication`                                                | Indicates a dead end in the authentication flow\.The API client can proceed in the flow by calling `cancelAuthentication`. The adapter returns a `FAILURE` status.                                                                                                                                                                                                                           |

> **Collapse: Action models**
>
> | Status                   | Request model                                      | Action                                                       | Description                                                                                                                         |
> | ------------------------ | -------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
> | `selectDevice`           | * `deviceRef` (required)
>
>   The device identifier. | - Error: `VALIDATION_ERROR`
>
>   ErrorDetail: `INVALID_DEVICE` | Starts an authentication flow with the specified `deviceId`.For example:```
> {
>   "deviceRef":
>   {
>      "id":
> "<device ID>"
>   }
> }
> ``` |
> | `checkOtp`               | * `otp`
>
>   The OTP submitted by the user.          | - Error: `VALIDATION_ERROR`
>
>   ErrorDetail: `INVALID_OTP`    | Validates the submitted OTP.                                                                                                        |
> | `resendOtp`              | This action has no model.                          | * Error: `REQUEST_FAILED`
>
>   ErrorDetail: `OTP_RESEND_LIMIT` | Re-sends an OTP to the previously selected device.                                                                                  |
> | `continueAuthentication` | This action has no model.                          | This action has no errors.                                   | This action continues the current authentication flow.                                                                              |
> | `cancelAuthentication`   | This action has no model.                          | This action has no errors.                                   | This action cancels the current authentication step.                                                                                |

### Objects

> **Collapse: Device object**
>
> | Parameter Name | Type   | Description                                                                             |
> | -------------- | ------ | --------------------------------------------------------------------------------------- |
> | **id**         | String | The unique identifier for this object.                                                  |
> | **type**       | String | The device delivery method type. The available options are `SMS`, `VOICE`, and `EMAIL`. |
> | **target**     | String | The device's masked email address or phone number.                                      |

> **Collapse: User object**
>
> | Parameter Name | Type   | Description                                           |
> | -------------- | ------ | ----------------------------------------------------- |
> | **username**   | String | The user's username that was mapped into the adapter. |

* userData object

  Object with dynamic data populated based on adapter configuration.

> **Collapse: Resource reference (ResourceRef) object**
>
> | Parameter Name | Type   | Description                |
> | -------------- | ------ | -------------------------- |
> | **id**         | String | The resource's identifier. |

### Error codes

An error code is returned if the call flow state hasn't reached a dead end and the user can still authenticate with a device. In cases where a flow reaches a dead end, the `MFA_FAILED` state is returned with a corresponding code.

> **Collapse: Top level error codes**
>
> | Error code         | Message                                                                       | HTTP status |
> | ------------------ | ----------------------------------------------------------------------------- | ----------- |
> | `VALIDATION_ERROR` | One or more validation errors occurred.                                       | `400`       |
> | `REQUEST_FAILED`   | The request couldn't be completed. There was an issue processing the request. | `400`       |

> **Collapse: Detail level error codes**
>
> | Error code                                                                        | Message                                               | userMessageKey               | Parent code        |
> | --------------------------------------------------------------------------------- | ----------------------------------------------------- | ---------------------------- | ------------------ |
> | `INVALID_OTP`                                                                     | An invalid or expired OTP was provided.               | `authn.api.invalid.otp`      | `VALIDATION_ERROR` |
> | `OTP_RESEND_LIMIT`	This error code can also be returned by the MFA\_FAILED state. | The OTP has been re-sent the maximum number of times. | `authn.api.otp.resend.limit` | `REQUEST_FAILED`   |
> | `INVALID_DEVICE`                                                                  | An invalid device was provided.                       |                              | `VALIDATION_ERROR` |

> **Collapse: codes**
>
> | Error code                                                                                                                                                                      | Message                                               | userMessageKey               |
> | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ---------------------------- |
> | `OTP_RESEND_LIMIT`	This error code can also be returned if the call flow state hasn't reached a dead end. To learn more, refer to the previous table, Detail level error codes. | The OTP has been re-sent the maximum number of times. | `authn.api.otp.resend.limit` |
> | `INVALID_DEVICE`                                                                                                                                                                | An invalid device was provided.                       |                              |

---

---
title: Twilio Programmable API Notification Publisher settings reference
description: Field descriptions for the Twilio Programmable API Notification Publisher configuration page.
component: otp
page_id: otp:setup:pf_otp_ik_twilio_programmable_api_notification_publisher_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/otp/setup/pf_otp_ik_twilio_programmable_api_notification_publisher_settings_reference.html
revdate: April 22, 2025
---

# Twilio Programmable API Notification Publisher settings reference

Field descriptions for the **Twilio Programmable API Notification Publisher** configuration page.

> **Collapse: Standard fields**
>
> | Field                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                              |
> | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Account SID**                                                                    | The **Account SID** that you noted in [Getting your Twilio API credentials](pf_otp_ik_getting_your_twilio_api_credentials.html).                                                                                                                                                                                                                                                                                                                         |
> | **Auth Token**                                                                     | The **Auth Token** that you noted in [Getting your Twilio API credentials](pf_otp_ik_getting_your_twilio_api_credentials.html).                                                                                                                                                                                                                                                                                                                          |
> | **From Number**	This field is required if you select Voice as the Delivery Method. | The Twilio phone number, sender ID, or Wireless SIM that sends the message to the user.This value appears as the sender. Phone numbers must be in E.164 format. Learn more in [E.164](https://www.twilio.com/docs/glossary/what-e164) in the Twilio documentation.	Alphanumeric sender IDs are not available in all countries. You can find a list of supported countries in International support for Alphanumeric Sender ID in the Twilio Help Center. |
> | **Messaging Service ID**                                                           | The Twilio Messaging Service SID.                                                                                                                                                                                                                                                                                                                                                                                                                        |
> | **Delivery Method**                                                                | The method used to send the one-time passcode (OTP).The default value is **SMS**.&#xA;&#xA;If the Delivery Method is SMS, you must configure a value for at least one of the following fields:&#xA;&#xA;From Number&#xA;&#xA;Messaging Service ID                                                                                                                                                                                                        |
> | **Block VoIP Numbers**                                                             | When selected, the Twilio Lookup API is used to ensure SMS messages are not sent to VoIP phone numbers.This is a paid service. Learn more in [Lookup](https://www.twilio.com/lookup) in the Twilio documentation.This checkbox is cleared by default.                                                                                                                                                                                                    |
> | **Blocked Numbers**                                                                | OTPs are not sent to phone numbers that match these values.Separate multiple values with a comma.The default values are the following toll-free numbers: `+1800,+1888,+1877,+1866,+1855,+1844,+1833`.                                                                                                                                                                                                                                                    |
> | **Test Phone**                                                                     | The phone number used to test the configuration on the **Actions** tab.                                                                                                                                                                                                                                                                                                                                                                                  |

> **Collapse: Advanced fields**
>
> | Field                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Messages File**       | The name of the messages file to use for notifications.The adapter uses the corresponding `.properties` file in `<pf_install>/pingfederate/server/default/conf/language-packs`.The default value is `twilio-programmable-api-publisher-messages`.                                                                                                                                                                                                    |
> | **Voice Option**        | The Twilio voice to use for voice calls. Select Twilio's basic **Man** or **Woman** voice, or select **Other** to specify one of the more advanced voices.You can find a list of languages and locales supported by each voice in [What Languages can the \<Say> TwiML Verb Speak?](https://support.twilio.com/hc/en-us/articles/223132827-What-Languages-can-the-Say-TwiML-Verb-Speak-) in the Twilio Help Center.The default setting is **Woman**. |
> | **Other Voice Option**  | If you selected a **Voice Option** of **Other**, specify the specific voice to use. For example, `alice` or `Polly.Joanna`.You can find a list of voice names in [What Languages can the \<Say> TwiML Verb Speak?](https://support.twilio.com/hc/en-us/articles/223132827-What-Languages-can-the-Say-TwiML-Verb-Speak-) in the Twilio Help Center.This field is blank by default.                                                                    |
> | **API Request Timeout** | The amount of time in milliseconds that PingFederate allows when establishing a connection with the Twilio API or waiting for a response to a request. A value of `0` disables the timeout.The default value is `5000`.                                                                                                                                                                                                                              |
> | **Connection Timeout**  | The amount of time in milliseconds that PingFederate allows to establish a connection with the Twilio API. A value of `0` disables the timeout.The default value is `5000`.                                                                                                                                                                                                                                                                          |
> | **Proxy Settings**      | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                                                                                                                                                                                                                                          |
> | **Custom Proxy Host**   | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                       |
> | **Custom Proxy Port**   | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                            |

---

---
title: Twilio Verify API Notification Publisher settings reference
description: Field descriptions for the Twilio Verify API Notification Publisher configuration page.
component: otp
page_id: otp:setup:pf_otp_ik_twilio_verify_api_notification_publisher_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/otp/setup/pf_otp_ik_twilio_verify_api_notification_publisher_settings_reference.html
revdate: April 14, 2025
---

# Twilio Verify API Notification Publisher settings reference

Field descriptions for the **Twilio Verify API Notification Publisher** configuration page.

> **Collapse: Standard fields**
>
> | Field                  | Description                                                                                                                                                                                                                                           |
> | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Account SID**        | The **Account SID** that you noted in [Getting your Twilio API credentials](pf_otp_ik_getting_your_twilio_api_credentials.html).                                                                                                                      |
> | **Auth Token**         | The **Auth Token** that you noted in [Getting your Twilio API credentials](pf_otp_ik_getting_your_twilio_api_credentials.html).                                                                                                                       |
> | **Service ID**         | The **Service ID** that you noted in [Getting your Twilio API credentials](pf_otp_ik_getting_your_twilio_api_credentials.html).                                                                                                                       |
> | **Delivery Method**    | The method used to send the one-time passcode (OTP).                                                                                                                                                                                                  |
> | **Block VoIP Numbers** | When selected, the Twilio Lookup API is used to ensure SMS messages are not sent to VoIP phone numbers.This is a paid service. Learn more in [Lookup](https://www.twilio.com/lookup) in the Twilio documentation.This checkbox is cleared by default. |
> | **Blocked Numbers**    | OTPs are not sent to phone numbers that match these values.Separate multiple values with a comma.The default values are the following toll-free numbers: `+1800,+1888,+1877,+1866,+1855,+1844,+1833`.                                                 |
> | **Test Mail**          | The email address used to test the configuration on the **Actions** tab.                                                                                                                                                                              |
> | **Test Phone**         | The phone number used to test the configuration on the **Actions** tab.                                                                                                                                                                               |

> **Collapse: Advanced fields**
>
> | Field                   | Description                                                                                                                                                                                                                         |
> | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **API Request Timeout** | The amount of time in milliseconds that PingFederate waits for the Twilio API to respond to requests. A value of `0` disables the timeout. A negative value uses the PingFederate system defaults.The default value is `5000`.      |
> | **Connection Timeout**  | The amount of time in milliseconds that PingFederate allows to establish a connection with the Twilio API. A value of `0` disables the timeout. A negative value uses the PingFederate system defaults.The default value is `5000`. |
> | **Proxy Settings**      | The proxy settings to use for outbound HTTP requests originating from the notification publisher. This setting allows you to override the PingFederate system-default proxy settings.The default selection is **System Defaults**.  |
> | **Customer Proxy Host** | The proxy server hostname to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                       |
> | **Custom Proxy Port**   | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                           |