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
