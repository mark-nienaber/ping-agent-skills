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

---

---
title: Configure forgotten username retrieval
description: Configure forgotten username retrieval to allow users to recover their usernames using email, security questions, or browser display in PingAM
component: pingam
version: 8.1
page_id: pingam:user-self-service:configuring-forgotten-username
canonical_url: https://docs.pingidentity.com/pingam/8.1/user-self-service/configuring-forgotten-username.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Self-Service"]
page_aliases: ["user-self-service-guide:configuring-forgotten-username.adoc"]
---

# Configure forgotten username retrieval

The forgotten username feature allows existing users to retrieve their usernames when they cannot remember them.

1. In the AM admin UI, go to Realms > *realm name* > Services and select User Self-Service.

2. Select the Forgotten Username tab.

3. Enable Forgotten Username.

4. Enable Captcha to turn on the Google reCAPTCHA plugin. Make sure you configured the plugin as described in [Configure the Google reCAPTCHA plugin](configuring-recaptcha.html).

5. Enable Security Questions to display security questions to the user during the forgotten password reset process. The user must have security questions defined in their profile, and must correctly answer the presented questions to be able to reset passwords.

6. Enable Email Username for the user to receive the retrieved username by email.

7. Enable Show Username for the user to see their retrieved username on the browser.

8. In the Token LifeTime (seconds) field, enter an appropriate number of seconds for the token lifetime. If the token lifetime expires before the user resets their password, then the user will need to restart the forgotten password process over again.

   Default: `300` seconds.

9. To customize the forgotten username outgoing email, perform the following steps:

   * In the Outgoing Email Subject field, enter the subject line of the email.

     The syntax is `lang|subject-text`, where `lang` is the ISO 639 language code, such as `en` for English, `fr` for French, and others. For example, the subject line value could be: `en|Forgotten username email`.

   * In the Outgoing Email Body field, enter the text of the email.

     The syntax is `lang|email-text`, where `lang` is the ISO 639 language code. Note that email body text must be all on one line and can contain any HTML tags within the body of the text.

     For example, the email body text could be: `en|Thank you for your inquiry! Your username is %username%.`

10. Save your changes.

---

---
title: Configure knowledge-based security questions
description: Configure knowledge-based authentication security questions to verify user identity during registration, password reset, and username recovery processes
component: pingam
version: 8.1
page_id: pingam:user-self-service:configuring-kba
canonical_url: https://docs.pingidentity.com/pingam/8.1/user-self-service/configuring-kba.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Self-Service", "Registration", "KBA"]
page_aliases: ["user-self-service-guide:configuring-kba.adoc"]
---

# Configure knowledge-based security questions

Knowledge-based authentication (KBA) is an authentication mechanism in which the user must correctly answer a number of pre-configured security questions that are set during the initial registration setup. If successful, the user is granted the privilege to carry out an action, such as registering an account, resetting a password, or retrieving a username. The security questions are presented in a random order to the user during the User Self-Registration, forgotten password reset, and forgotten username processes.

AM provides a default set of security questions and easily allows AM administrators and users to add their own custom questions.

Security questions must be set in order for users to reset their password.

If the user enters an invalid username, email, or first name/surname pair as part of a recovery flow, AM presents them with a random KBA question before failing the flow. This is to protect the service against account enumeration attacks. If both the security questions and the confirmation emails are enabled for a given flow, AM presents the user with a message similar to `An email has been sent to the address you entered. Click the link in that email to proceed`, but does not actually send an email.

1. In the AM admin UI, go to Realms > *realm name* > Services and select the User Self-Service service.

2. Select the General Configuration tab.

3. In the Security Questions field, several questions are available by default.

   Enter your own questions as required. The syntax is `OrderNum|ISO-3166-2 Country Code|Security Question`. For example, `5|en|What is your dog's name?`. Make sure that order numbers are unique.

   |   |                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------ |
   |   | You should never remove any security questions as a user may have reference to a given question. |

4. In the Minimum Answers to Define field, enter the number of security questions that will be presented to the user during the registration process.

5. In the Minimum Answers to Verify field, enter the number of security questions that must be answered during the Forgotten Password and Forgotten Username services.

6. Save your changes.

7. Ensure that the `kbainfo` attribute is set in the profile attribute allowlist.

The profile attribute allowlist controls the information returned to non-administrative users when they access `json/user` endpoints. For example, the allowlist controls the attributes shown in the user profile page.

Common profile attributes are allowlisted by default. You must add any custom attributes that you want non-administrative users to see.

The allowlist can be set globally, or per realm, in the user self-service service. To modify the list:

* **Globally**: Go to Configure > Global Services > User Self-Service > Profile Management, and edit the Self readable attributes field.

* **By realm**: Go to Realms > *realm name* > Services > User Self-Service > Profile Management, and edit the Self readable attributes field.

  You must add the user self-service service to the realm if you've not done so already but you don't need to configure anything other than the allowlist.

---

---
title: Configure the email service
description: Configure PingAM to send user registration and password reset emails using SMTP or Microsoft Graph API email transport
component: pingam
version: 8.1
page_id: pingam:user-self-service:configuring-email-service
canonical_url: https://docs.pingidentity.com/pingam/8.1/user-self-service/configuring-email-service.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Self-Service", "Registration", "Email"]
page_aliases: ["user-self-service-guide:configuring-email-service.adoc"]
section_ids:
  mail-msgraph-api: Microsoft Graph API
  mail-smtp-basic: SMTP
---

# Configure the email service

The user self-service feature lets you send confirmation emails to users who are registering on your site or resetting forgotten passwords. Mails are sent using AM's SMTP or OAuth 2.0 REST-based email service. You can configure the email service by realm or globally.

Each user must have a unique email address to use the email features of user self-service.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * If a user enters an *invalid* first or last name, username, or email address during the username or password reset flows, AM *doesn't* send an email but still presents the user with a message similar to:

  `An email has been sent to the address you entered. Click the link in that email to proceed.`

* If a user enters an *existing* username while registering, AM sends an email with a registration link to the address that the user entered and presents the user with a message similar to:

  `An email has been sent to the address you entered. Click the link in that email to proceed.`

  Clicking that link redirects the user to the registration page, and AM shows a message similar to:

  `One or more user account values are invalid.`This behavior protects the service against account enumeration attacks. |

Follow these steps to configure the email service:

1. In the AM admin UI, go to Realms > *realm name* > Services.

2. Select Add a Service and choose Email Service from the list of available services.

3. In the Email From Address field, enter the email address from which to send email notifications; for example, `no-reply@example.com`.

   For Microsoft Graph API transport configurations, this address *must exist* in the Microsoft Exchange administration center.

   |   |                                                                               |
   | - | ----------------------------------------------------------------------------- |
   |   | You can't select anything in the Transport Type drop-down menu at this stage. |

4. Click Create.

5. Configure the generic attributes that apply to both types of email service, such as the profile attribute for the user's email address, the subject, and content for notification messages.

   Learn more about the different configuration properties in [Email service](../setup/services-configuration.html#global-email).

   |   |                                                                               |
   | - | ----------------------------------------------------------------------------- |
   |   | You can't select anything in the Transport Type drop-down menu at this stage. |

6. Save your changes.

7. On the Secondary Configurations tab, click Add a Secondary Configuration.

8. Select one of the following:

   * [Microsoft Graph API](#mail-msgraph-api) to configure an OAuth 2.0 REST-based transport type email service.

   * [SMTP](#mail-smtp-basic) to configure an SMTP basic authentication transport type email service.

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | You can configure different realms to use different email transport configuration types. |

## Microsoft Graph API

1. Refer to your Microsoft account to complete the following settings on the New microsoftRestTransports configuration screen:

   | Property                  | Value                                                               | Notes                                                                                                                                                                                               |
   | ------------------------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Name                      | A unique name for this MS Graph API service.                        | The name must include alphanumeric characters only.You'll use this name later to map the client secret in the secret store.                                                                         |
   | Email Rest Endpoint URL   | The REST endpoint URL for sending emails through the MS Graph API.  | The format of this URL is `https://graph.microsoft.com/v1.0/users/user ID/sendMail`, for example: `https://graph.microsoft.com/v1.0/users/bjensen@xftq8.onmicrosoft.com/sendMail`.                  |
   | OAuth2 Token Endpoint URL | The OAuth 2.0 authentication endpoint.                              | The format of this URL is `https://login.microsoftonline.com/tenant ID/oauth2/v2.0/token`, for example: `https://login.microsoftonline.com/d258d3da-98a2-492b-875e-059a6abfbdf9/oauth2/v2.0/token`. |
   | OAuth2 Client Id          | The ID for the OAuth 2.0 client.                                    | This is the client ID or application ID provided by the Microsoft Application Registration portal.                                                                                                  |
   | OAuth2 Scopes             | The scopes to be requested as part of the OAuth 2.0 authentication. | The only value supported by the Microsoft Graph API is `https://graph.microsoft.com/.default`.                                                                                                      |

2. Click Create.

3. Obtain the client secret from the Microsoft Application Registration portal and map it to a secret label in the secret store.

   Use one of the following methods:

   1. Dynamic secret label (all secret stores):

      1. Set a value in the Secret Label Identifier field.

         AM uses this identifier to generate a specific secret label for this email service.

         The secret label has the format `am.services.mail.microsoftrest.identifier.clientsecret` where identifier is the value of the Secret Label Identifier field.

         The Secret Label Identifier can only contain characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

      2. Store the client secret obtained from the Microsoft Application Registration portal in a secret in a secret store.

      3. [Map the secret](../security/secret-mapping.html) to the generated secret label.

      4. For improved security, rotate this secret periodically.

   2. Secret label based on a filename (file system secret stores only):

      1. [Create a file system secret volume](../security/secret-stores.html#create-file-system-secret-volumes) if one doesn't exist.

      2. Create a file named `am.services.email.microsoftrest.service-name.clientsecret`; for example, if you named this MS Graph API service `msrest`, create a file named `am.services.email.microsoftrest.msrest.clientsecret.txt`.

         The filename must use alphanumeric characters only.

      3. Add the client secret obtained from the Microsoft Application Registration portal to the file and save.

      4. [Map the secret label](../security/secret-mapping.html#creating-mappings-FS) `am.services.email.microsoftrest.service-name.clientsecret` to the file system secret you created in the previous step.

|   |                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you set a Secret Label Identifier, the secret mapped to the generated secret label takes precedence over the secret mapped to `am.services.mail.microsoftrest.service-name.clientsecret`. |

## SMTP

|   |                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------- |
|   | SMTP Basic authentication is deprecated. Where possible, use the OAuth 2.0 REST-based Microsoft Graph API transport type instead. |

1. On the New smtpTransports configuration screen, complete the following settings:

   | Property                            | Value                                                                               | Notes                                                                                                                                                                                                                                                                                                                                                         |
   | ----------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Name                                | A name for the SMTP transport secondary configuration.                              |                                                                                                                                                                                                                                                                                                                                                               |
   | Mail Server Host Name               | The hostname of the mail server.                                                    | If you're using the Google SMTP server, configure the Google Mail settings to enable access for less secure applications.                                                                                                                                                                                                                                     |
   | Mail Server Authentication Username | The username to authenticate to the mail server.                                    | If you're testing with a Google account, you can enter a known Gmail address.                                                                                                                                                                                                                                                                                 |
   | Mail Server Authentication Password | The password of the username who authenticates to the mail server.                  | 	For improved security, set a Secret Label Identifier to store the password in the secret store instead. If you set a Secret Label Identifier and AM finds a matching secret in the secret store, it ignores this password field.                                                                                                                             |
   | Secret Label Identifier             | AM uses this identifier to generate a specific secret label for this email service. | The secret label has the format `am.services.email.smtp.identifier.secret` where identifier is the value of Secret Label Identifier.The Secret Label Identifier can only contain characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.If you set a value in this field, AM ignores the Mail Server Authentication Password. |

2. Click Create.

3. [Map a secret](../security/secret-mapping.html) in the secret store to the generated secret label.

---

---
title: Configure the Google reCAPTCHA plugin
description: Configure the Google reCAPTCHA plugin to protect user self-service pages from software bots
component: pingam
version: 8.1
page_id: pingam:user-self-service:configuring-recaptcha
canonical_url: https://docs.pingidentity.com/pingam/8.1/user-self-service/configuring-recaptcha.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Self-Service", "Password Reset", "Registration"]
page_aliases: ["user-self-service-guide:configuring-recaptcha.adoc"]
---

# Configure the Google reCAPTCHA plugin

The user self-service feature supports the Google reCAPTCHA plugin, which can be placed on the Register Your Account, Reset Your Password, and Retrieve Your Username pages. The Google reCAPTCHA plugin protects your user self-service implementation from software bots.

Google reCAPTCHA is the only supported plugin for user self-service. AM works with Google reCAPTCHA v2. Any other Captcha service will require a custom plugin.

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To configure JVM properties for proxy support, see [Configure AM for outbound communication](../security/reverse-proxy.html#outbound-communication). |

1. Register your website at a Captcha provider, such as [Google reCAPTCHA](https://www.google.com/recaptcha/intro/index.html), to get your site and secret key.

   When you register your site for Google reCAPTCHA, you only need to obtain the site and secret key, which you enter in the User Self-Service configuration page in the AM admin UI. You do not have to do anything with client-side integration and server-side integration. The Google reCAPTCHA plugin appears automatically on the Register Your Account, Reset Your Password, and Retrieve Your Username pages after you configure it in the AM admin UI.

   ![AM supports the Google reCAPTCHA plugin to protect against software bots.](_images/google-recaptcha.png)Figure 1. Google reCAPTCHA Page

2. In the AM admin UI, go to Realms > *realm name* > Services and select the User Self-Service service.

3. Select the General Configuration tab.

4. In the Google reCAPTCHA Site Key field, enter the site key that you obtained from the Google reCAPTCHA site.

5. In the Google reCAPTCHA Secret Key field, enter the secret key that you obtained from the Google reCAPTCHA site.

6. In the Google reCAPTCHA Verification URL field, leave the URL by default.

7. Save your changes.

8. Enable Google reCAPTCHA for the user self-service features.

   For more information see:

   * [Configure user registration](configuring-user-self-registration.html)

   * [Configure forgotten password reset](configuring-forgotten-password.html)

   * [Configure forgotten username retrieval](configuring-forgotten-username.html)

---

---
title: Configure user registration
description: Enable user self-registration in PingAM with email verification, captcha, and security questions to let end users create their own accounts
component: pingam
version: 8.1
page_id: pingam:user-self-service:configuring-user-self-registration
canonical_url: https://docs.pingidentity.com/pingam/8.1/user-self-service/configuring-user-self-registration.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Self-Service", "Registration", "Configuration &amp; Setup"]
page_aliases: ["user-self-service-guide:configuring-user-self-registration.adoc"]
section_ids:
  configure-user-self-registration: Configure AM for user self-registration
  user-mgmt-pwd-sec-questions: User management of passwords and security questions
---

# Configure user registration

User self-registration lets end users create their own accounts in AM.

## Configure AM for user self-registration

Although you can configure user self-registration without any additional security mechanisms, such as email verification or KBA security questions, you *should* configure the email verification service with user self-registration at a minimum.

1. In the AM admin UI, [configure the email service](configuring-email-service.html).

2. Go to Realms > *realm name* > Services and select User Self-Service.

3. On the User Registration tab, enable User Registration.

4. Enable Captcha to turn on the Google reCAPTCHA plugin. Make sure you have configured the plugin, as described in [Configure the Google reCAPTCHA plugin](configuring-recaptcha.html).

5. Enable Email Verification to turn on the email verification service. You should leave Email Verification enabled, so users who self-register *must* perform email address verification.

6. Enable Verify Email before User Detail to verify the user's email address before requesting the user details.

   By default, the user self-registration flow validates the email address after the user has provided their details.

7. Enable Security Questions to display security questions during the self-registration process.

   If you enable security questions, the user is presented with the configured questions during the forgotten password and forgotten username flows. The user must answer these questions in order to reset their passwords or retrieve their usernames.

8. In the Token LifeTime field, set an appropriate number of seconds for the token lifetime. If the token lifetime expires before the user self-registers, they'll need to restart the registration process.

   Default: `300` seconds.

9. To customize the user registration outgoing email, follow these steps:

   * In the Outgoing Email Subject field, enter the subject line of the email.

     The syntax is `lang|subject-text`, where `lang` is the ISO-639 language code, such as `en` for English, or `fr` for French. For example, the subject line values could be: `en|Registration Email` and `fr|E-mail d'inscription`.

   * In the Outgoing Email Body field, enter the text of the email.

     The syntax is `lang|email-text`, where `lang` is the ISO-639 language code. The email body text must be all on one line, and can contain any HTML tags within the body of the text.

     For example:

     ```
     en|Thank you for registering with example.com! Click <a href="%link%">here</a> to register.`
     ```

10. In the Valid Creation Attributes field, enter the attributes the user can set during registration.

    These attributes are based on the AM identity store.

11. For Destination After Successful Registration, select one of the following options:

    * **auto-login**. User is automatically logged in and sent to the appropriate page within the system.

    * **default**. User is sent to a success page without being logged in. In this case, AM displays a "You have successfully registered" page. The user can then click the Login link to log in to AM. This is the default selection.

    * **login**. User is sent to the login page to authenticate.

12. Save your changes.

13. On the Advanced Configuration tab, configure the User Registration Confirmation Email URL for your deployment. The default is: `https://am.example.com:8443/am/XUI/?realm=${realm}#register/`.

14. Save your changes.

## User management of passwords and security questions

Once the user has self-registered to your system, they can change their password and security questions at any time on the user profile page. The user profile page provides tabs to carry out these functions.

![The User Profile page supports the ability to change the user's password on the Password tab.](_images/user-profile-page-pwd-tab.png)Figure 1. User Profile Page Password Tab![The User Profile page supports the ability to change the user's security questions on the Security Questions tab.](_images/user-profile-page-sec-questions-tab.png)Figure 2. User Profile Page Security Questions Tab

---

---
title: Configure user self-service
description: Set up user self-service instances with encryption keys, security methods, and features like registration, password reset, and username recovery
component: pingam
version: 8.1
page_id: pingam:user-self-service:configuring-uss
canonical_url: https://docs.pingidentity.com/pingam/8.1/user-self-service/configuring-uss.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Self-Service", "Registration", "Configuration &amp; Setup"]
page_aliases: ["user-self-service-guide:configuring-uss.adoc"]
section_ids:
  create-uss-service: Create a user self-service instance
---

# Configure user self-service

The following table summarizes the high-level tasks required to configure the user self-service features:

| Task                                                                                                                                                                                                                                                                                                                                                                                                                      | Resources                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Create encryption and signing keys**The user self-service features require a key pair for encryption and a signing secret key. Create one of each for each instance of user self-service you plan to configure.                                                                                                                                                                                                         | * [Create self-service key aliases](../security/configuring-keys.html#changing-uss-keys)                                                                                                                                               |
| **Configure a user self-service instance**Each realm requires its own instance.                                                                                                                                                                                                                                                                                                                                           | - [Create a user self-service instance](#create-uss-service)                                                                                                                                                                           |
| **Configure user self-service security**Configure at least one security method for each feature:- Configure the email service to send an email to users who are registering, resetting their passwords, or users who have forgotten their username.

- Configure knowledge-based questions that users must answer to reset their passwords.

- Configure Google reCAPCHA to protect user self-service features from bots. | * [Configure the email service](configuring-email-service.html)

* [Configure the Google reCAPTCHA plugin](configuring-recaptcha.html)

* [Configure knowledge-based security questions](configuring-kba.html)                         |
| **Configure user self-service features**Configure the features that your environment requires.                                                                                                                                                                                                                                                                                                                            | - [Configure user registration](configuring-user-self-registration.html)

- [Configure forgotten password reset](configuring-forgotten-password.html)

- [Configure forgotten username retrieval](configuring-forgotten-username.html) |

## Create a user self-service instance

1. In the AM admin UI, go to Realms > *realm name* > Services and select Add a Service.

2. Select User Self-Service from the list of possible services.

3. Specify the secrets used to sign and encrypt the JWT token AM uses to track end users during user self-service operations. Do one of the following:

   * Enable the Use Secret Store property and configure the following secret IDs in the secret store:

     * `am.services.selfservice.token.encryption`

     * `am.services.selfservice.token.signing`

   * Populate the values of the Encryption Key Pair Alias and the Signing Secret Key Alias properties.

     For example, if you're using the demo keys in the default `keystore.jceks` file, set the properties as follows:

     * Encryption Key Pair Alias to `selfserviceenctest`.

     * Signing Secret Key Alias to `selfservicesigntest`.

     |   |                                                                                                                                                                                                                                                                                                                                      |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     |   | - By default, the name of the demo keys displays in grey. This doesn't mean the fields are filled in.

     - The demo key aliases are for test or evaluation purposes. Don't use them in production environments. Read [Create self-service key aliases](../security/configuring-keys.html#changing-uss-keys) to create new key aliases. |

4. Enable each of the user self-service features you require.

5. Select Create.

6. On the User Self-Service page, configure each feature as described in the sections that follow.

---

---
title: Register a user
description: Enable users to register themselves through the PingAM UI or REST API with optional security methods like email validation and reCAPTCHA
component: pingam
version: 8.1
page_id: pingam:user-self-service:uss-registering-users
canonical_url: https://docs.pingidentity.com/pingam/8.1/user-self-service/uss-registering-users.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Self-Service", "Registration", "REST API"]
page_aliases: ["user-self-service-guide:uss-registering-users.adoc"]
section_ids:
  register-user-rest: Register a user over REST
  register-user-rest-backwards-compatible: Register a user over REST (backwards-compatible mode)
---

# Register a user

The AM UI includes pages for users to register themselves. You can also create a RESTful application that uses the user self-service features.

![AM's User Self-Registration basic flow with optional features disabled.](_images/user-self-registration-basic-flow.png)Figure 1. User self-registration basic flow (UI)

> **Collapse: User self-registration flow with options (UI)**
>
> ![AM's user self-registration supports various user flows, depending on how you configure your options.](_images/user-self-registration-flow.png)

When performing user self-service functions, you can enable one or more security methods, such as email validation, Google reCAPTCHA, knowledge-based authentication, or custom plugins. Each configured security method requires requests to be sent from AM to the client, and completed responses returned to AM to verify.

A unique token is provided in the second request to the client that must be used in any subsequent responses, so that AM can maintain the state of the user self-service process.

By default, the user self-registration flow validates the email address after the user has provided their details.

## Register a user over REST

Before performing the steps in this procedure, ensure that Verify Email before User Detail (Realms > *realm name* > Services > User Self-Service > User Registration) is *disabled*.

1. Create a GET request to the `/selfservice/userRegistration` endpoint.

   Notice that the request does not require any form of authentication:

   ```bash
   $ curl \
   --header "Accept-API-Version: resource=1.0, protocol=1.0" \
   "https://am.example.com:8443/am/json/realms/root/selfservice/userRegistration"
   {
      "requirements": {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "New user details",
        "properties": {
           "user": {
               "description": "User details",
               "type": "object"
           }
        },
        "required": [
           "user"
        ],
        "type": "object"
      },
      "tag": "initial",
      "type": "userDetails"
   }
   ```

   AM sends a request to complete the user details. The `required` array defines the data that must be returned to AM to progress past this step of the registration. In the example, the required type is a `user` object that contains the user details.

2. Create a POST response back to the `/selfservice/userRegistration` endpoint with a query string containing `_action=submitRequirements`. In the POST data, include an `input` element in the JSON structure, which should contain values for each element in the `required` array of the request.

   In this example, AM requests an object named `user`. Ths object should contain values for the `username`, `givenName`, `sn`, `mail`, `userPassword`, and `inetUserStatus` properties:

   ```bash
   $ curl \
   --header "Accept-API-Version: resource=1.0, protocol=1.0" \
   --request POST \
   --header "Content-Type: application/json" \
   --data \
   '{
       "input": {
          "user": {
            "username": "bjensen",
            "givenName": "Babs",
            "sn": "Jensen",
            "mail":"bjensen@example.com",
            "userPassword": "Ch4ng31t",
            "inetUserStatus": "Active"
          }
       }
   }' \
   "https://am.example.com:8443/am/json/realms/root/selfservice/userRegistration?_action=submitRequirements"
   {
       "requirements": {
         "$schema": "http://json-schema.org/draft-04/schema#",
         "description": "Verify emailed code",
         "properties": {
            "code": {
                "description": "Enter code emailed",
                "type": "string"
            }
         },
         "required": [
             "code"
         ],
         "type": "object"
       },
       "tag": "validateCode",
       "token": "eyJ0eXAiOiJKV…​..QiLCJjmqrlqUfQ",
       "type": "emailValidation"
   }
   ```

   If the response is accepted, AM continues with the registration process and sends the next request for information.

   The value of the `token` element should be included in this and any subsequent responses to AM for this registration; AM uses this information to track which stage of the registration process is being completed.

   Note that the request for information is of the type `emailValidation`. Other possible types include:

   * `captcha`, if the Google reCAPTCHA plugin is enabled

   * `kbaSecurityAnswerDefinitionStage`, if knowledge-based security questions are required

   For an example of Google reCAPTCHA validation, see [Retrieve forgotten usernames](uss-forgotten-username.html).

3. Return the information required by the next step of the registration, along with the `token` element.

   In this example, the user information was accepted and a code was emailed to the email address. AM requires this code in the response in an element named `code` before continuing:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --header "Accept-API-Version: resource=1.0, protocol=1.0" \
   --data \
   '{
       "input": {
           "code": "cf53fcb6-3bf2-44eb-a437-885296899699"
       },
       "token": "eyJ0eXAiOiJKV…​..QiLCJjmqrlqUfQ"
   }' \
   "https://am.example.com:8443/am/json/realms/root/selfservice/userRegistration?_action=submitRequirements"
   {
       "type": "selfRegistration",
       "tag": "end",
       "status": {
           "success": true
       },
       "additions": {}
   }
   ```

   When the process is complete, the response from AM has a `tag` property with value of `end`. If the `success` property in the `status` object has a value of `true`, then self-registration is complete and the user account was created.

   In the example, AM only required email verification to register a new user. In flows containing Google reCAPTCHA validation or knowledge-based security questions, you would continue returning POST data to AM containing the requested information until the process is complete.

## Register a user over REST (backwards-compatible mode)

Before performing the steps in this procedure, ensure that Verify Email before User Detail (Realms > *realm name* > Services > User Self-Service > User Registration) is *enabled*.

1. Create a GET request to the `/selfservice/userRegistration` endpoint.

   Notice that the request does not require any form of authentication:

   ```bash
   $ curl \
   --header "Accept-API-Version: resource=1.0, protocol=1.0" \
   "https://am.example.com:8443/am/json/realms/root/selfservice/userRegistration"
   {
      "type":"emailValidation",
      "tag":"initial",
      "requirements":{
         "$schema":"http://json-schema.org/draft-04/schema#",
         "description":"Verify your email address",
         "type":"object",
         "required":[
            "mail"
         ],
         "properties":{
            "mail":{
               "description":"Email address",
               "type":"string"
            }
         }
      }
   }
   ```

   AM sends the first request for security information. In this example, the first request is of type `emailValidation`, but other types include `captcha`, if the Google reCAPTCHA plugin is enabled, and `kbaSecurityAnswerDefinitionStage`, if knowledge-based authentication is required.

   The `required` array defines the data that must be returned to AM to progress past this step of the registration.

   The `properties` element contains additional information about the required response, such as a description of the required field, or the site key required to generate a reCAPTCHA challenge.

2. Create a POST response back to the `/selfservice/userRegistration` endpoint with a query string containing `_action=submitRequirements`. In the POST data, include an `input` element in the JSON structure, which should contain values for each element in the `required` array of the request.

   In this example, a `mail` value was requested:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --header "Accept-API-Version: resource=1.0, protocol=1.0" \
   --data \
   '{
       "input": {
           "mail": "bjensen@example.com"
       }
   }' \
   "https://am.example.com:8443/am/json/selfservice/userRegistration?_action=submitRequirements"
   {
      "type":"emailValidation",
      "tag":"validateCode",
      "requirements":{
         "$schema":"http://json-schema.org/draft-04/schema#",
         "description":"Verify emailed code",
         "type":"object",
         "required":[
            "code"
         ],
         "properties":{
            "code":{
               "description":"Enter code emailed",
               "type":"string"
            }
         }
      },
      "token":"eyAicHis…​PIF-lN4s"
   }
   ```

   If the response was accepted, AM continues with the registration process and sends the next request for information. In this example, the email address was accepted and a code was emailed to the address, which AM requires in the response in an element named `code` before continuing.

   The value of the `token` element should be included in this and any subsequent responses to AM for this registration.

3. Continue returning POST data to AM containing the requested information, in the format specified in the request. Also return the `token` value in the POST data, so that AM can track which stage of the registration process is being completed:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --header "Accept-API-Version: resource=1.0, protocol=1.0" \
   --data \
   '{
       "input": {
           "code": "cf53fcb6-3bf2-44eb-a437-885296899699"
       },
       "token": "eyAicHis…​PIF-lN4s"
   }' \
   "https://am.example.com:8443/am/json/selfservice/userRegistration?_action=submitRequirements"
   {
      "type":"userDetails",
      "tag":"initial",
      "requirements":{
         "$schema":"http://json-schema.org/draft-04/schema#",
         "description":"New user details",
         "type":"object",
         "required":[
            "user"
         ],
         "properties":{
            "user":{
               "description":"User details",
               "type":"object"
            }
         }
      },
      "token":"eyAicHis…​PIF-lN4s"
   }
   ```

4. When requested—when the `type` value in the request is `userDetails`—supply the details of the new user as an object in the POST data:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --header "Accept-API-Version: resource=1.0, protocol=1.0" \
   --data \
   '{
       "input": {
           "user": {
               "username": "bjensen",
               "givenName": "Babs",
               "sn": "Jensen",
               "userPassword": "Ch4ng31t",
               "inetUserStatus": "Active"
           }
       },
       "token": "eyAicHis…​PIF-lN4s"
   }' \
   "https://am.example.com:8443/am/json/selfservice/userRegistration?_action=submitRequirements"
   {
        "type": "selfRegistration",
        "tag": "end",
        "status": {
        "success": true
        },
        "additions": {}
   }
   ```

   When the process is complete, the `tag` element has a value of `end`. If the `success` element in the `status` element has a value of `true`, then self-registration is complete and the user account was created.

The user self-service feature provides options to set the user's destination after a successful self-registration. These options include redirecting the user to a 'successful registration' page, to the login page, or automaticatically logging the user into the system. Use the `Destination After Successful Self-Registration` property to set the option (on the console: *Realm Name* > Services > User Self-Service > User Registration). When you select `User sent to 'successful registration' page` or `User sent to login page`, the JSON response after a successful registration is as follows:

```json
{
   "type": "selfRegistration",
   "tag": "end",
   "status": {
       "success": true
   },
   "additions": {}
}
```

If you select `User is automatically logged in`, the JSON response is:

```json
{
    "type": "autoLoginStage",
    "tag": "end",
    "status": {
        "success": true
    },
    "additions": {
        "tokenId": "AQIC5…​MQAA*",
        "successUrl": "/am/console"
    }
}
```

---

---
title: Reset forgotten passwords
description: Enable users to reset forgotten passwords through the PingAM UI or a custom RESTful application using security methods like email validation, reCAPTCHA, and knowledge-based authentication
component: pingam
version: 8.1
page_id: pingam:user-self-service:uss-forgotten-password
canonical_url: https://docs.pingidentity.com/pingam/8.1/user-self-service/uss-forgotten-password.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Self-Service", "Password Reset"]
page_aliases: ["user-self-service-guide:uss-forgotten-password.adoc"]
---

# Reset forgotten passwords

The AM UI includes pages for users to reset their forgotten passwords. You can, however, create a RESTful application to leverage the user self-service features.

Forgotten password flow in the UI

![The forgotten password feature supports multiple user flows, depending on how it is configured.](_images/forgotten-password-flow.png)

When performing user self-service functions, you can enable one or more security methods such as email validation, Google reCAPTCHA, knowledge-based authentication, or custom plugins.

Each configured security method requires particular security data that AM requests from the client for verification.

A unique token is provided in the second response to the client that must be used in any subsequent requests, so that AM can maintain the state of the user self-service process.

1. Send a GET request to the `/selfservice/forgottenPassword` endpoint.

   Notice that the request does not require any form of authentication:

   ```bash
   $ curl \
   --header "Accept-API-Version: resource=1.0" \
   "https://am.example.com:8443/am/json/realms/root/selfservice/forgottenPassword"
   {
     "type": "captcha",
     "tag": "initial",
     "requirements": {
       "$schema": "http://json-schema.org/draft-04/schema#",
       "description": "Captcha stage",
       "type": "object",
       "required": [
         "response"
       ],
       "properties": {
         "response": {
           "recaptchaSiteKey": "6Lfr1…​cIqbd",
           "description": "Captcha response",
           "type": "string"
         }
       }
     }
   }
   ```

   In this example, the Google reCAPTCHA plugin is enabled, so the first required item of security data is of the `captcha` type.

2. Send a POST request to the `/selfservice/forgottenPassword` endpoint with a query string containing `_action=submitRequirements`. In the POST data, include an `input` element in the JSON structure, which should contain values for each element in the `required` array of the response.

   In this example, the `response` value required is the user input provided after completing the Google reCAPTCHA challenge:

   ```bash
   $ curl \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   --header "Content-Type: application/json" \
   --data \
   '{
       "input": {
           "response": "03AHJ…​qiE1x4"
       }
   }' \
   "https://am.example.com:8443/am/json/realms/root/selfservice/forgottenPassword?_action=submitRequirements"
   {
       "type": "userQuery",
       "tag": "initial",
       "requirements": {
           "$schema": "http://json-schema.org/draft-04/schema#",
           "description": "Find your account",
           "type": "object",
           "required": [
               "queryFilter"
           ],
           "properties": {
               "queryFilter": {
                   "description": "filter string to find account",
                   "type": "string"
               }
           }
       },
       "token": "eyAicHis…​PIF-lN4s"
   }
   ```

   If the input value was accepted, AM continues with the password reset process and specifies the information required next. In this example, the Google reCAPTCHA was verified and AM is requesting details about the account for the password reset, which must be provided in a `queryFilter` element.

   The value of the `token` element should be included in this and all subsequent requests to AM for this reset process.

3. Send a POST request to AM with a `queryFilter` value in the POST data containing the username of the subject with the password to replace.

   For more information on query filters, see [Query](../am-rest/rest-intro.html#about-crest-query).

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --data \
   '{
       "input": {
           "queryFilter": "uid eq \"bjensen\""
       },
       "token": "eyAicHis…​PIF-lN4s"
   }' \
   "https://am.example.com:8443/am/json/realms/root/selfservice/forgottenPassword?_action=submitRequirements"
   {
       "type": "kbaSecurityAnswerVerificationStage",
       "tag": "initial",
       "requirements": {
           "$schema": "http://json-schema.org/draft-04/schema#",
           "description": "Answer security questions",
           "type": "object",
           "required": [
               "answer1"
           ],
           "properties": {
               "answer1": {
                   "systemQuestion": {
                       "en": "What was the model of your first car?"
                   },
                   "type": "string"
               }
           }
       },
       "token": "eyAicHis…​PIF-lN4s"
   }
   ```

   If a single subject is located that matches the provided query filter, the password reset process continues.

   If a subject is not found, an HTTP 400 Bad Request status is returned, along with an error message in the JSON data:

   ```json
   {
       "code": 400,
       "reason": "Bad Request",
       "message": "Unable to find account"
   }
   ```

4. Continue sending POST data to AM containing the requested information, in the format specified in the response.

   Also return the `token` value in the POST data, so that AM can track the stages of the password reset process.

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --data \
   '{
       "input": {
           "answer1": "Mustang"
       },
       "token": "eyAicHis…​PIF-lN4s"
   }' \
   "https://am.example.com:8443/am/json/realms/root/selfservice/forgottenPassword?_action=submitRequirements"
   {
       "type": "resetStage",
       "tag": "initial",
       "requirements": {
           "$schema": "http://json-schema.org/draft-04/schema#",
           "description": "Reset password",
           "type": "object",
           "required": [
               "password"
           ],
           "properties": {
               "password": {
                   "description": "Password",
                   "type": "string"
               }
           }
           "code": "cf88bb63-b59c-4792-8fdf-2bcc00b0ab06"
       },
       "token": "eyAicHis…​PIF-lN4s"
   }
   ```

5. When AM has received all the requested information, it sets `type` to `resetStage` and returns a unique `code` value in the response. You can now specify a new password in the POST data, along with both the `code` and `token` values:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --data \
   '{
       "input": {
           "password": "5tr0ng~P4s5worD!"
       },
       "code": "cf88bb63-b59c-4792-8fdf-2bcc00b0ab06",
       "token": "eyAicHis…​PIF-lN4s"
   }' \
   "https://am.example.com:8443/am/json/realms/root/selfservice/forgottenPassword?_action=submitRequirements"
   {
       "type": "activityAuditStage",
       "tag": "end",
       "status": {
           "success": true
       },
       "additions": {}
   }
   ```

   When the process is complete, the `tag` element has a value of `end`. If the `success` element in `status` has a value of `true`, the password reset is complete and the new password is now active.

   If the password is not accepted, an HTTP 400 Bad Request status is returned along with an error message:

   ```json
   {
       "code": 400,
       "reason": "Bad Request",
       "message": "Minimum password length is 8."
   }
   ```

---

---
title: Retrieve forgotten usernames
description: Use the user self-service API to retrieve forgotten usernames with configurable security methods including email validation, reCAPTCHA, and knowledge-based authentication
component: pingam
version: 8.1
page_id: pingam:user-self-service:uss-forgotten-username
canonical_url: https://docs.pingidentity.com/pingam/8.1/user-self-service/uss-forgotten-username.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Self-Service"]
page_aliases: ["user-self-service-guide:uss-forgotten-username.adoc"]
---

# Retrieve forgotten usernames

The AM UI includes pages for users to recover their forgotten usernames. You can, however, create a RESTful application to leverage the user self-service features.

![AM's Forgotten Username supports multiple user flows, depending on how you configure your options.](_images/forgotten-username-flow.png)Figure 1. Forgotten Username Flow (UI)

When performing user self-service functions, you can enable one or more security methods, such as email validation, Google reCAPTCHA, knowledge-based authentication, or custom plugins. Each configured security method requires requests to be sent from AM to the client, and completed responses returned to AM to verify.

A unique token is provided in the second request to the client that must be used in any subsequent responses, so that AM can maintain the state of the user self-service process.

1. Create a GET request to the `/selfservice/forgottenUsername` endpoint.

   Notice that the request does not require any form of authentication.

   ```bash
   $ curl \
   --header "Accept-API-Version: resource=1.0" \
   https://am.example.com:8443/am/json/realms/root/selfservice/forgottenUsername
   {
     "type": "captcha",
     "tag": "initial",
     "requirements": {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Captcha stage",
        "type": "object",
        "required": [
          "response"
        ],
        "properties": {
          "response": {
            "recaptchaSiteKey": "6Lfr1…​cIqbd",
            "description": "Captcha response",
            "type": "string"
          }
         }
     }
   }
   ```

   In this example, the Google reCAPTCHA plugin is enabled, so the first request is of the `captcha` type.

2. Create a POST response back to the `/selfservice/forgottenUsername` endpoint with a query string containing `_action=submitRequirements`. In the POST data, include an `input` element in the JSON structure, which should contain values for each element in the `required` array of the request.

   In this example, a `response` value was requested, which should be the user input as provided after completing the Google reCAPTCHA challenge.

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --header "Accept-API-Version: resource=1.0" \
   --data \
   '{
       "input": {
           "response": "03AHJ…​qiE1x4"
       }
   }' \
   https://am.example.com:8443/am/json/realms/root/selfservice/forgottenUsername?_action=submitRequirements
   {
       "type": "userQuery",
       "tag": "initial",
       "requirements": {
           "$schema": "http://json-schema.org/draft-04/schema#",
           "description": "Find your account",
           "type": "object",
           "required": [
               "queryFilter"
           ],
           "properties": {
               "queryFilter": {
                   "description": "filter string to find account",
                   "type": "string"
               }
           }
       },
       "token": "eyAicHis…​PIF-lN4s"
   }
   ```

   If the response was accepted, AM continues with the username retrieval process and sends the next request for information. In this example, the Google reCAPTCHA was verified and AM is requesting details about the account name to retrieve, which must be provided in a `queryFilter` element.

   The value of the `token` element should be included in this and all subsequent responses to AM for this retrieval process.

3. Create a POST response to AM with a `queryFilter` value in the POST data containing the user's email address associated with their account:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --data \
   '{
       "input": {
           "queryFilter": "mail eq \"bjensen@example.com\""
       },
       "token": "eyAicHis…​PIF-lN4s"
   }' \
   https://am.example.com:8443/am/json/realms/root/selfservice/forgottenUsername?_action=submitRequirements
   {
       "type": "kbaSecurityAnswerVerificationStage",
       "tag": "initial",
       "requirements": {
           "$schema": "http://json-schema.org/draft-04/schema#",
           "description": "Answer security questions",
           "type": "object",
           "required": [
               "answer1"
           ],
           "properties": {
               "answer1": {
                   "systemQuestion": {
                       "en": "What was the model of your first car?"
                   },
                   "type": "string"
               }
           }
       },
       "token": "eyAicHis…​PIF-lN4s"
   }
   ```

   If a single subject is located that matches the provided query filter, the retrieval process continues.

   If KBA is enabled, AM requests answers to the configured number of KBA questions, as in this example.

   For more information on query filters, see [Query](../am-rest/rest-intro.html#about-crest-query).

   If a subject is not found, an HTTP 400 Bad Request status is returned, and an error message in the JSON data:

   ```
   {
       "code": 400,
       "reason": "Bad Request",
       "message": "Unable to find account"
   }
   ```

4. Return a POST response with the answers as values of the elements specified in the `required` array, in this example `answer1`. Ensure the same `token` value is sent with each response.

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --data \
   '{
       "input": {
           "answer1": "Mustang"
       },
       "token": "eyAicHis…​PIF-lN4s"
   }' \
   https://am.example.com:8443/am/json/realms/root/selfservice/forgottenUsername?_action=submitRequirements
   {
       "type": "retrieveUsername",
       "tag": "end",
       "status": {
           "success": true
       },
       "additions": {
           "userName": "bjensen"
       }
   }
   ```

   When the process is complete, the `tag` element has a value of `end`. If the `success` element in the `status` element has a value of `true`, then username retrieval is complete and the username is emailed to the registered address.

   If the Show Username option is enabled for username retrieval, the username retrieved is also returned in the JSON response as the value of the `userName` element, as in the example above.

---

---
title: User self-service
description: "PingAM's user self-service capabilities enable end users to self-register, reset forgotten passwords, and retrieve usernames while reducing help desk costs and strengthening customer loyalty"
component: pingam
version: 8.1
page_id: pingam:user-self-service:about-uss
canonical_url: https://docs.pingidentity.com/pingam/8.1/user-self-service/about-uss.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Self-Service", "Password Reset", "Registration", "KBA"]
page_aliases: ["user-self-service-guide:about-uss.adoc"]
---

# User self-service

User self-service lets end users self-register on your website, securely reset forgotten passwords and retrieve their usernames.

AM's user self-service capabilities greatly reduce help desk costs and provide a rich online experience that strengthens customer loyalty.

Features

* User self-registration

  Lets non-authenticated users register on your site. You can add security features like email verification, knowledge-based authentication (KBA) security questions, Google reCAPTCHA, and custom plugins to augment the self-registration process.

* Knowledge-based authentication security questions

  When enabled, AM requests answers to pre-configured or custom security questions during the registration process. During the forgotten password or forgotten username process, end users are presented with the security questions, and must answer them correctly to continue the process.

|   |                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------- |
|   | Security questions are presented to the end user in a random order during forgotten password and forgotten username flows. |

* Forgotten password reset

  Lets registered users reset their passwords. The default password policy is set in the underlying directory server and requires a minimum password length of eight characters by default. If security questions are enabled, users must also correctly answer their pre-configured security questions before resetting their passwords.

* Forgotten username support

  Lets users retrieve their forgotten usernames. If security questions are enabled, users must also correctly answer their pre-configured security questions before retrieving their usernames.

* Google reCAPTCHA plugin

  Supports the ability to add a Google reCAPTCHA plugin to the registration page. This plugin protects against software bots that can be used against your site.

* Configurable plugins

  Supports the ability to add plugins to customize the user services process flow. You can develop your custom code and drop the `.jar` file into your container.

* Customizable confirmation emails

  Supports the ability to customize or localize confirmation emails in plain text or HTML.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The [OTP Email Sender node](https://docs.pingidentity.com/auth-node-ref/8.1/otp-email-sender.html) supports plain text notifications only. You can't include HTML-rich notifications that use information from shared or transient state. If you need to support HTML notifications, use a Groovy script with a private HTTP client that makes the REST API calls and place the output in a Scripted Decision node. |

* Password policy configuration

  Password policy is enforced by the underlying DS server and manually aligned with frontend UI templates. The default password policy requires a password with a minimum length of eight characters.

* Self-registration user attribute allowlist

  Attribute allowlisting lets you specify which attributes can be set by the user during account creation.

User self-registration supports a number of different user flows, depending on the security options you configure. For example, email verification, security questions, Google reCAPTCHA, and custom plugins.

Forgotten username retrieval and forgotten password reset also support various user flows, depending on your configured security options.

---

---
title: User self-service
description: Configure PingAM user self-service for self-registration, password reset, and username retrieval
component: pingam
version: 8.1
page_id: pingam:user-self-service:preface
canonical_url: https://docs.pingidentity.com/pingam/8.1/user-self-service/preface.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Self-Service", "Password Reset", "Registration"]
page_aliases: ["index.adoc", "user-self-service-guide:preface.adoc"]
---

# User self-service

These topics show you how to configure, maintain, and troubleshoot the user self-service feature provided by PingAM, which automates account registration and account name retrieval, and forgotten password reset.

[icon: book, set=fad, size=3x]

#### [User self-service](about-uss.html)

Enable self-registration, password reset, and username retrieval.

[icon: id-card, set=fad, size=3x]

#### [Configure user registration](configuring-user-self-registration.html)

Let end users register their own accounts.

[icon: edit, set=fad, size=3x]

#### [Configure password reset](configuring-forgotten-password.html)

Allow existing users to reset their *password*.

[icon: question-circle, set=fad, size=3x]

#### [Configure username retrieval](configuring-forgotten-username.html)

Allow existing users to retrieve their *username*.