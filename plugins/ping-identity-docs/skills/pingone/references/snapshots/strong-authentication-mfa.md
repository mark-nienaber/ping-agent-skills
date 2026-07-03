---
title: (Customer Only) Configuring WhatsApp authentication
description: Enable and configure WhatsApp authentication to allow your users to receive a one-time passcode (OTP) by WhatsApp.
component: pingone
page_id: pingone:strong_authentication_mfa:p1-strong-auth_whatsapp
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1-strong-auth_whatsapp.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
---

# (Customer Only) Configuring WhatsApp authentication

Enable and configure WhatsApp authentication to allow your users to receive a one-time passcode (OTP) by WhatsApp.

![WhatsApp message showing a one-time passcode. The message includes a security message, and the copy code button.](_images/whatsapp-message-example.png)

## Before you begin

To enable WhatsApp authentication, make sure you have a WhatsApp Business account that includes one or more WhatsApp messaging templates. You can find more details in [Configuring a custom WhatsApp sender account](../settings/p1-using-a-custom-whatsapp-sender-account.html).

## About this task

To configure WhatsApp authentication:

1. Add your WhatsApp Business account as a Sender in PingOne. Learn more in [Configuring a custom WhatsApp sender account](../settings/p1-using-a-custom-whatsapp-sender-account.html).

2. For each language you want to support, link a WhatsApp messaging template to the relevant PingOne Notification templates. Learn more in [Notification Templates](../user_experience/p1_edit_notification.html).

3. In the PingOne **MFA policy** enable WhatsApp as an authentication method. Learn more in [Configuring an MFA policy for strong authentication](p1_creating_an_mfa_policy_for_strong_auth.html).

4. (Optional) Configure a notification policy to limit the number of WhatsApp messages that can be sent per day or to limit their target locations. Learn more in [Notification Polices](../user_experience/p1_creating_a_notification_policy.html).
