---
title: Configure forgotten password reset
description: Configure PingAM to allow existing users to reset forgotten passwords using email verification, optional security questions, and customizable notifications
component: pingam
version: 8.1
page_id: pingam:user-self-service:configuring-forgotten-password
canonical_url: https://docs.pingidentity.com/pingam/8.1/user-self-service/configuring-forgotten-password.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Self-Service", "Password Reset"]
page_aliases: ["user-self-service-guide:configuring-forgotten-password.adoc"]
---

# Configure forgotten password reset

The forgotten password feature allows existing users to reset their passwords when they cannot remember them.

1. In the AM admin UI, go to Realms > *realm name* > Services and select the User Self-Service service.

2. Select the Forgotten Password tab.

3. Enable Forgotten Password.

4. Enable Captcha to turn on the Google reCAPTCHA plugin. Make sure you configured the plugin as described in [Configure the Google reCAPTCHA plugin](configuring-recaptcha.html).

5. Enable Email Verification to turn on the email verification service. You should keep this enabled.

   Note that the recovery link AM emails to the user contains a code that can only be used once.

6. Enable Security Questions to display security questions to the user during the forgotten password reset process. The user must have security questions defined in their profile, and must correctly answer the presented questions to be able to reset passwords.

   You can also configure AM to lock an account if the user fails to answer their security questions a number of times. To enable this feature, perform the following steps:

   * Enable Enforce password reset lockout.

   * In the Lock Out After number of attempts field, set the number of questions the user must fail to answer for AM to lock their account.

7. In the Token LifeTime (seconds) field, enter an appropriate number of seconds for the token lifetime. If the token lifetime expires before the user resets their password, then the user will need to restart the forgotten password process over again.

   Default: `300` seconds.

8. To customize the forgotten password outgoing email, perform the following steps:

   * In the Outgoing Email Subject field, enter the subject line of the email.

     The syntax is `lang|subject-text`, where `lang` is the ISO-639 language code, such as `en` for English, `fr` for French, and others. For example, the subject line value could be: `en|Forgotten Password Email`.

   * In the Outgoing Email Body field, enter the text of the email.

     The syntax is `lang|email-text`, where `lang` is the ISO-639 language code. Note that email body text must be all on one line and can contain any HTML tags within the body of the text.

     For example, the email body text could be:

     ```
     en|Thank you for request! Click <a href="%link%">here<;/a> to reset your password.
     ```

9. Save your changes.

10. Under the Advanced Configuration tab, change the default Forgotten Password Confirmation Email URL for your deployment. The default is: `https://am.example.com:8443/am/XUI/?realm=${realm}#passwordReset/`.

11. Save your changes.
