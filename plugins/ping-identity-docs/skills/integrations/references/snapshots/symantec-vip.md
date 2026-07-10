---
title: Adding credentials as a user
description: The Symantec VIP IdP adapter allows users to add credentials as a self-service by default.
component: symantec-vip
page_id: symantec-vip:user_credential_management:pf_symantec_vip_ik_adding_credentials_as_a_user
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/user_credential_management/pf_symantec_vip_ik_adding_credentials_as_a_user.html
llms_txt: https://docs.pingidentity.com/integrations/symantec-vip/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 24, 2025
section_ids:
  steps: Steps
---

# Adding credentials as a user

The Symantec VIP IdP adapter allows users to add credentials as a self-service by default.

## Steps

1. Open the VIP Access app on your mobile device.

2. Start the PingFederate authentication flow by signing on to the first-factor authentication adapter.

   For example, this could be an HTML Form Adapter or OpenToken Adapter instance.

3. On the Symantec VIP IdP adapter, sign on with the same username and password.

4. Click **Add Credential**.

   ![The Symantec VIP Adapter Add Credential button](_images/addCredentialButton.png)

5. On the **Add Credentials** page, enter the credential ID and security code shown on your VIP Access mobile app, or on your physical VIP security token or card. Click **Submit**.

6. On the sign-on screen, select **Security Code**, and enter the next security code that appears on your device. Click **Submit**.

   ![The Symantec VIP Adapter sign on page](../_images/symantecVIPsignon.jpg)

---

---
title: Adding credentials as an administrator
description: As an administrator, you can manually add credentials to a user's account. This allows them to sign on with Symantec VIP using another device or authentication method.
component: symantec-vip
page_id: symantec-vip:user_credential_management:pf_symantec_vip_ik_adding_credentials_as_an_administrator
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/user_credential_management/pf_symantec_vip_ik_adding_credentials_as_an_administrator.html
llms_txt: https://docs.pingidentity.com/integrations/symantec-vip/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 24, 2025
section_ids:
  steps: Steps
---

# Adding credentials as an administrator

As an administrator, you can manually add credentials to a user's account. This allows them to sign on with Symantec VIP using another device or authentication method.

## Steps

1. Sign on to the [Symantec VIP Manager](https://manager.vip.symantec.com/) portal as an administrator.

2. On the **Users** tab, go to the user that you want to modify and click **Edit Details**.

3. In the **Credentials** section, click **Add Another**.

4. In the **Type** list, select the desired authentication method.

5. In the **Credential ID** field, enter the user's credential ID.

   You can find the ID on the user's VIP Access mobile app, or on their physical VIP security token or card.

6. (Optional) If the **Extension** field appears, enter a phone extension.

   The extension can include hashtags, commas, asterisks, periods, and the letter `x`, but only if numbers precede these characters.

7. In the **Name** field, enter a name, then click **Save**.

---

---
title: Changelog
description: The following is the change history for the Symantec VIP integration kit.
component: symantec-vip
page_id: symantec-vip:release_notes:pf_symantec_vip_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/release_notes/pf_symantec_vip_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/symantec-vip/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 205
section_ids:
  symantec-vip-integration-kit-2-0-july-2025: Symantec VIP integration kit 2.0 - July 2025
  symantec-vip-integration-kit-1-8-1-february-2024: Symantec VIP integration kit 1.8.1 – February 2024
  symantec-vip-integration-kit-1-8-july-2023: Symantec VIP integration kit 1.8 – July 2023
  symantec-vip-integration-kit-1-7-1-march-2023: Symantec VIP integration kit 1.7.1 – March 2023
  symantec-vip-integration-kit-1-7-july-2022: Symantec VIP integration kit 1.7 – July 2022
  symantec-vip-integration-kit-1-6-september-2021: Symantec VIP integration kit 1.6 – September 2021
  symantec-vip-integration-kit-1-5-may-2020: Symantec VIP integration kit 1.5 – May 2020
  symantec-vip-integration-kit-1-4-january-2018: Symantec VIP integration kit 1.4 – January 2018
  symantec-vip-integration-kit-1-3-october-2016: Symantec VIP integration kit 1.3 – October 2016
  symantec-vip-integration-kit-1-2-august-2015: Symantec VIP integration kit 1.2 – August 2015
  symantec-vip-integration-kit-1-1-may-2014: Symantec VIP integration kit 1.1 – May 2014
  symantec-vip-integration-kit-1-0-1-july-2011: Symantec VIP integration kit 1.0.1 – July 2011
  symantec-vip-integration-kit-1-0-january-2011: Symantec VIP integration kit 1.0 – January 2011
---

# Changelog

The following is the change history for the Symantec VIP integration kit.

## Symantec VIP integration kit 2.0 - July 2025

* Added the ability to obscure personally identifiable information (PII) in displayed user credentials. Learn more in the **Visible Leading Characters Length** and **Visible Trailing Characters Length** table entries in [Symantec VIP IdP adapter settings reference](../setup/pf_symantec_vip_ik_symantec_vip_adapter_settings_reference.html).

* Added the ability to create users automatically. Learn more in the **Create User** table entry in [Symantec VIP IdP adapter settings reference](../setup/pf_symantec_vip_ik_symantec_vip_adapter_settings_reference.html).

* Added support for number challenges in push notification authentication. Learn more in the **Enable Number Matching in Push Notifications** table entry in [Symantec VIP IdP adapter settings reference](../setup/pf_symantec_vip_ik_symantec_vip_adapter_settings_reference.html).

* Added the ability for users to configure and authenticate with SMS, voice, and email credentials. Learn more in the **Enable Adding SMS Credential** - **Enable Adding Email Credential** table entries in [Symantec VIP IdP adapter settings reference](../setup/pf_symantec_vip_ik_symantec_vip_adapter_settings_reference.html).

* Added documentation for the PingFederate authentication API. Learn more in [PingFederate Authentication API support](../pf_symantec_vip_ik_pf_authn_api_support.html).

* Removed legacy web application authentication and added support for template-based authentication. Learn more in [Customizing templates](../setup/pf_symantec_vip_ik_customizing_templates.html).

  |   |                                                                                                                                                                                                                                                           |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The `vip-adapter-security-code-challenge.war` directory is no longer in use. If you created a `.war` file to make customizations to this directory previously, you can re-implement your changes with the new HTML templates after upgrading the adapter. |

* Fixed an issue that allowed users without any configured credentials to attempt to authenticate, leading to a dead end in the authentication flow.

  |   |                                                                                                                  |
  | - | ---------------------------------------------------------------------------------------------------------------- |
  |   | This issue was applicable if the **Suppress Add Credential** checkbox was selected in the adapter configuration. |

## Symantec VIP integration kit 1.8.1 – February 2024

* Fixed an issue that caused failures if a temporary code was used.

## Symantec VIP integration kit 1.8 – July 2023

* Added two new exposed attributes in the adapter contract, `credential_type` and `credential_id`. You can use these attributes to do branching logic in PingFederate authentication policies.

  * `credential_type` specifies the type of credential used to sign on to Symantec VIP.

  * `credential_id` specifies the credential ID used to sign on to Symantec VIP.

## Symantec VIP integration kit 1.7.1 – March 2023

* Fixed an issue that caused some sensitive information to display in the JSP.

## Symantec VIP integration kit 1.7 – July 2022

* Removed adapter-based session management.

* Added the ability to retrieve the targeted application's [Application Name](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_identifying_target_application.html) from the [SP Connection](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html) in PingFederate when a push notification is triggered for an account.

## Symantec VIP integration kit 1.6 – September 2021

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

## Symantec VIP integration kit 1.5 – May 2020

* Added support for the PingFederate localization framework.

* Added the ability to select a default authentication method or allow users to choose.

* Added the ability to skip the authentication prompt when a one-time password is provided.

## Symantec VIP integration kit 1.4 – January 2018

* SMS and voice are now supported for one–time passcode delivery.

* Added ability to configure the maximum number of retry attempts for the one–time passcode.

* Bug fixes.

## Symantec VIP integration kit 1.3 – October 2016

* Added support for VIP's Access Push feature, which replaces the need for the user to manually enter a security code, by sending a push verification to the registered mobile device upon sign–in.

* Validated solution against VIP's latest API changes (SHA–1 to SHA–2 migration).

* Updated html templates with the latest UI theme.

## Symantec VIP integration kit 1.2 – August 2015

* Added support to suppress the register credentials workflow.

## Symantec VIP integration kit 1.1 – May 2014

* Added the ability to override default VIP endpoint URLs.

* Added support to register credentials.

* Added support to reset credentials after two consecutive failed authentication attempts.

* Added support for Symantec VIP API 1.1

## Symantec VIP integration kit 1.0.1 – July 2011

* Corrected malformed HTML which would prevent the Submit button from rendering on Internet Explorer 8 and Firefox 5 browsers

## Symantec VIP integration kit 1.0 – January 2011

* Initial release

---

---
title: Configuring an adapter instance
description: Configure the Symantec VIP IdP adapter to allow PingFederate to use Symantec VIP as an authentication factor.
component: symantec-vip
page_id: symantec-vip:setup:pf_symantec_vip_ik_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/setup/pf_symantec_vip_ik_configuring_an_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/symantec-vip/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 24, 2025
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Configure the Symantec VIP IdP adapter to allow PingFederate to use Symantec VIP as an authentication factor.

## Steps

1. Sign on to the PingFederate administrative console.

2. On the **Identity Provider > Adapters** tab, click **Create New Instance**.

3. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **Symantec VIP Adapter**. Click **Next**.

4. On the **IdP Adapter** tab, configure the adapter instance by referring to [Symantec VIP IdP adapter settings reference](pf_symantec_vip_ik_symantec_vip_adapter_settings_reference.html). Click **Next**.

5. On the **Extended Contract** tab, add any attributes that you expect to retrieve in addition to the core contract attributes. Click **Next**.

6. Complete the adapter configuration.

7. On the **Summary** tab, check that the configuration is correct. Click **Done**.

8. On the **Manage IdP Adapter Instances** tab, click **Save**.

9. Modify your PingFederate authentication policy to pass attributes to your Symantec VIP IdP adapter instance from earlier in the authentication flow.

   The adapter expects the `username` attribute and accepts the optional security code attribute you defined in the **Security Code Attribute Name** field.

   Learn more about configuring authentication policies in [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html) in the PingFederate documentation.

---

---
title: Customizing templates
description: The Symantec VIP integration kit includes templates that can display Symantec VIP authentication challenges and other messages. You can customize the HTML portions of these templates to suit your organization's branding and presentation needs.
component: symantec-vip
page_id: symantec-vip:setup:pf_symantec_vip_ik_customizing_templates
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/setup/pf_symantec_vip_ik_customizing_templates.html
llms_txt: https://docs.pingidentity.com/integrations/symantec-vip/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 24, 2025
---

# Customizing templates

The Symantec VIP integration kit includes templates that can display Symantec VIP authentication challenges and other messages. You can customize the HTML portions of these templates to suit your organization's branding and presentation needs.

The following table lists the available templates and their uses. You can find more information about the templates in [Customizable user-facing pages](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_custom_user_facing_pages.html) in the PingFederate documentation.

> **Collapse: Template files**
>
> | Attribute                          | Description                                                                                                                                                                                                                       |
> | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `vip.enrollment.html`              | Initial form presented to the user. Offers the option to add a new credential (if configured) or proceed with authentication using an existing credential.                                                                        |
> | `vip.security_code_challenge.html` | Form presented to the user to enter a security code for authentication. Offers the option to choose alternative credential types if those methods are available to the user.For example, push notification, SMS, voice, or email. |
> | `vip.security_code_reset.html`     | Form presented to the user when they begin the reset credential flow.                                                                                                                                                             |
> | `vip.add_voice_credential.html`    | Form presented to the user when they add a new voice credential.                                                                                                                                                                  |
> | `vip.add_email_credential.html`    | Form presented to the user when they add a new email credential.                                                                                                                                                                  |
> | `vip.add_sms_credential.html`      | Form presented to the user when they add a new SMS credential.                                                                                                                                                                    |
> | `vip.add_credential.html`          | Form presented to the user when they verify ownership of a new credential using a security code they received.                                                                                                                    |

The `vip-messages.properties` file contains configurable properties that allow administrators to customize the messages displayed in the previous templates for various scenarios. The properties file has inline comments providing more context. Keys are self-descriptive.

---

---
title: Customizing user messages
description: The Symantec VIP integration kit allows you to customize or translate the messages shown to the user on the authentication prompt.
component: symantec-vip
page_id: symantec-vip:setup:pf_symantec_vip_ik_customizing_user_messages
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/setup/pf_symantec_vip_ik_customizing_user_messages.html
llms_txt: https://docs.pingidentity.com/integrations/symantec-vip/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 24, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Customizing user messages

The Symantec VIP integration kit allows you to customize or translate the messages shown to the user on the authentication prompt.

## About this task

Learn more about localization in PingFederate in [Localizing messages for end users](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_local_message_end_users.html).

## Steps

1. In the `<pf_install>/pingfederate/server/default/conf/language-packs` directory, open the `vip-messages.properties` file for editing.

2. Translate or modify the messages.

3. Save the file with a suffix to indicate the language, such as `vip-messages.properties_fr` for French.

4. Restart PingFederate.

5. If you operate PingFederate in a cluster, repeat steps 1 - 3 for each instance of PingFederate.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Symantec VIP integration kit files to your PingFederate directory.
component: symantec-vip
page_id: symantec-vip:setup:pf_symantec_vip_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/setup/pf_symantec_vip_ik_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/symantec-vip/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 6, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Symantec VIP integration kit files to your PingFederate directory.

## Before you begin

Download the Symantec VIP integration kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

## Steps

1. Stop PingFederate, if it's running.

2. If you're upgrading an existing deployment, back up your customizations and delete previous versions of the integration files:

   1. Back up any Symantec VIP integration kit files that you customized in `<pf_install>/pingfederate/server/default/conf/`.

   2. Delete the `pf-vip-idp-adapter-<version>.jar` file from `<pf_install>/pingfederate/server/default/deploy`.

3. Extract the `.zip` archive and copy the contents of the `dist` directory to `<pf_install>`.

4. If there is more than one version of the `pf-authn-api-sdk-<version>.jar` file in your `<pf_install>/pingfederate/server/default/lib` directory, delete all but the latest version of the file.

5. If you backed up any customized files, modify the new files with your customizations.

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 2 - 7 for each engine node.

---

---
title: Download manifest
description: The following items are included in the Symantec VIP integration kit:
component: symantec-vip
page_id: symantec-vip:release_notes:pf_symantec_vip_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/release_notes/pf_symantec_vip_ik_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/symantec-vip/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2025
---

# Download manifest

The following items are included in the Symantec VIP integration kit:

* `Legal.pdf`: A file that contains copyright and license information.

* `dist/pingfederate/server/default`: A directory that contains the Java libraries needed to run the adapter.

  * `deploy`: A directory that contains the integration files.

    * `pf-vip-idp-adapter-<version>.jar`: A JAR file that contains the Symantec VIP IdP adapter.

  * `lib`: Contains common JAR files.

    * `pf-authn-api-sdk-<version>.jar`: A JAR file that contains the PingFederate Authentication API SDK.

  * `conf`: A directory that contains language template files.

    * `language-packs/vip-messages.properties`: A variable file that customizes the messages that appear on the template file.

    * `template`: A directory that contains language template files.

      * `assets`: A directory that contains style, font, and image files for the template files.

        * `css/vip.css`: A CSS file that customizes the appearance of the template file.

        * `end-user/<version>/end-user.css`: A CSS file that customizes the appearance of the template files.

        * `fonts/end-user/icons`: Contains template icons.

        * `images`: Contains template image files.

          * `logo.png`: An image file with company branding.

          * `ping-logo-horizontal.png`: An image file with company branding.

          * `ping-logo.svg`: An image file with company branding.

          * `product.png`: An image file with company branding.

          * `spinner.svg`: An image file used in a spinner animation.

          * `VIP_logo_RGB.png`: An image file with company branding.

        * `scripts`: Contains script files used to collect and send information.

          * `jquery-<version>.min.js`: A JavaScript file that contains the jQuery library.

          * `vip.js`: A JavaScript file that contains common functions used by templates.

      * `vip.add_credential.html`: Template displayed to the user during verification of a new credential using the received security code.

      * `vip.add_email_credential.html`: Template displayed to the user when the add email credential process is initiated.

      * `vip.add_sms_credential.html`: Template displayed to the user when the add SMS credential process is initiated.

      * `vip.add_voice_credential.html`: Template displayed to the user when the add voice credential process is initiated.

      * `vip.enrollment.html`: Template displayed to the user to add a new credential (if configured on the adapter) or proceed with authentication using preexisting credentials.

      * `vip.security_code_challenge.html`: Template displayed to the user for entering a security code for authentication, with the option to choose alternative credential types such as Push Notification, SMS, Voice, or Email if those methods are available to the user.

      * `vip.security_code_reset.html`: Template displayed to the user when the user goes through the reset credential flow.

---

---
title: Importing the Symantec certificate into PingFederate
description: To allow PingFederate and Symantec VIP to communicate securely, import the Symantec signing certificate into PingFederate.
component: symantec-vip
page_id: symantec-vip:setup:pf_symantec_vip_ik_importing_the_symantec_certificate_into_pf
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/setup/pf_symantec_vip_ik_importing_the_symantec_certificate_into_pf.html
llms_txt: https://docs.pingidentity.com/integrations/symantec-vip/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 24, 2025
section_ids:
  steps: Steps
---

# Importing the Symantec certificate into PingFederate

To allow PingFederate and Symantec VIP to communicate securely, import the Symantec signing certificate into PingFederate.

## Steps

1. In the [Symantec VIP Manager](https://manager.vip.symantec.com/vipmgr/signin.v) portal, export your SSL client certificate in the PKCS#12 format.

   To do so, complete the steps in [Managing VIP Certificates](https://manager.vip.symantec.com/vipmgr/helpcontentvipenrollcert.v) in the Symantec VIP Manager documentation.

2. In PingFederate, go to the certificate import page:

   1. Go to **Security > Certificate & Key Management > SSL Client Keys & Certificates**.

   2. On the **SSL Client Keys & Certificates** window, click **Import**.

3. On the **Import Certificate** tab, select your Symantec certificate and enter the password. Click **Next**.

4. On the **Summary** tab, click **Save**.

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the Symantec VIP integration kit:
component: symantec-vip
page_id: symantec-vip:release_notes:pf_symantec_vip_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/release_notes/pf_symantec_vip_ik_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/symantec-vip/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2025
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the Symantec VIP integration kit:

## Known issues

There aren't any known issues.

## Known limitations

There aren't any known limitations.

---

---
title: Overview of the SSO flow
description: With the Symantec VIP integration kit, PingFederate includes the Symantec VIP service in the authentication flow.
component: symantec-vip
page_id: symantec-vip::pf_symantec_vip_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/pf_symantec_vip_ik_overview_of_the_sso_flow.html
llms_txt: https://docs.pingidentity.com/integrations/symantec-vip/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 24, 2025
section_ids:
  description: Description
---

# Overview of the SSO flow

With the Symantec VIP integration kit, PingFederate includes the Symantec VIP service in the authentication flow.

![Diagram showing how PingFederate includes Symantec VIP in the authentication flow.](_images/SSOFlowOverview.jpg)

## Description

1. The user initiates single sign-on (SSO) *(tooltip: \<div class="paragraph">
   \<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
   \</div>)* from an service provider (SP) *(tooltip: \<div class="paragraph">
   \<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
   \</div>)* application through a PingFederate SP server.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This SP-initiated scenario represents the optimal use case, one in which both the identity provider (IdP) *(tooltip: \<div class="paragraph">&#xA;\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>&#xA;\</div>)* and SP are using PingFederate. However, PingFederate accepts any valid Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">&#xA;\<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>&#xA;\</div>)* authentication request from an SP.In addition, you can enable IdP-initiated SSO *(tooltip: \<div class="paragraph">&#xA;\<p>An identity federation transaction in which the SSO operation is initiated on the IdP. For example, the user is signed on to the IdP and signs off, triggering an SSO operation on the IdP. The IdP sends the SSO information to the SP.\</p>&#xA;\</div>)*. In this case, the user attempts SSO to an SP application from the IdP site, and the processing sequence would not include the following step. |

2. The PingFederate SP server generates a SAML AuthnRequest to the PingFederate IdP server.

3. If not already signed on at the IdP (using a first-factor adapter such as Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
   \<p>An open, cross platform protocol used for interacting with directory services.\</p>
   \</div>)* or Integrated Windows authentication (IWA) *(tooltip: \<div class="paragraph">
   \<p>Internet Information Services (IIS) authentication protocol for authenticated connections between IIS and other Microsoft services.\</p>
   \</div>)*), the user is challenged to authenticate.

4. The PingFederate IdP server obtains user-session information via the first-factor adapter.

5. The Symantec VIP IdP adapter requests a one-time passcode (OTP) *(tooltip: \<div class="paragraph">
   \<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
   \</div>)* from the user.

6. The Symantec VIP IdP adapter uses the username obtained by the first-factor adapter and the OTP to verify the user and the code via the Symantec VIP application programming interface (API) *(tooltip: \<div class="paragraph">
   \<p>A specification of interactions available for building software to access an application or service.\</p>
   \</div>)*.

7. If the validation succeeds, the PingFederate IdP server generates a SAML assertion with the username as the Subject and passes it to the PingFederate SP server.

8. (Not shown) The user is signed on to the SP target application.

---

---
title: PingFederate Authentication API support
description: You can use the PingFederate Authentication API to integrate the Symantec VIP IdP adapter into your application.
component: symantec-vip
page_id: symantec-vip::pf_symantec_vip_ik_pf_authn_api_support
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/pf_symantec_vip_ik_pf_authn_api_support.html
llms_txt: https://docs.pingidentity.com/integrations/symantec-vip/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 24, 2025
section_ids:
  models-objects-and-error-codes: Models, objects, and error codes
  objects: Objects
  error-codes: Error codes
---

# PingFederate Authentication API support

You can use the PingFederate Authentication API to integrate the Symantec VIP IdP adapter into your application.

The PingFederate Authentication API provides access to the current state of the authentication flow as a user steps through the PingFederate authentication policy. Learn more in [PingFederate Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

To integrate the Symantec VIP IdP adapter into your authentication flow, configure your application based on the information in this section.

|   |                                                                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can also explore integrating the Symantec VIP IdP adapter into your application using the PingFederate Authentication API Explorer. Learn more in [Exploring the Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_exploring_authentication_api.html) in the PingFederate documentation. |

## Models, objects, and error codes

When using the Symantec VIP integration kit through the PingFederate Authentication API, the adapter uses the following state models, action models, objects, and error codes:

> **Collapse: State models**
>
> | Status                                       | Request model                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Action                                                                                       | Description                                                                               |
> | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
> | `VIP_AUTHENTICATION_REQUIRED`                | * `username`
>
>   The authenticating user's username.
>
> * `pushNotificationInfo`
>
>   An object with data required to complete push notification.
>
>   If number matching is enabled, the user must enter the number displayed on their device.
>
> * `VIPCredentialInfo`
>
>   An object with details about the VIP credential.                                                                                                                                                                                                                                    | - `initiatePushAuthentication`
>
> - `selectVIPCredential`
>
> - `checkSecurityCode`
>
> - `continue` | To continue, the user must authenticate with a credential or approve a push notification. |
> | `VIP_CREDENTIAL_REQUIRED`                    | * `username`
>
>   The authenticating user's username.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | - `submitVIPCredential`
>
> - `continue`                                                        | The user must submit a credential to complete the enrollment process.                     |
> | `VIP_CREDENTIAL_RESET_REQUIRED`              | * `username`
>
>   The authenticating user's username.
>
> * `resettableVipCredentials`
>
>   A list of `VIP Credential Info` objects with details about the resettable credentials.                                                                                                                                                                                                                                                                                                                                                                            | - `resetVIPCredential`
>
> - `continue`                                                         | The user must reset their credential to continue.                                         |
> | `VIP_EMAIL_CREDENTIAL_REQUIRED`              | * `username`
>
>   The authenticating user's username.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | - `submitEmailCredential`
>
> - `continue`                                                      | The user must submit an email credential to complete the enrollment process.              |
> | `VIP_EMAIL_CREDENTIAL_VERIFICATION_REQUIRED` | * `username`
>
>   The authenticating user's username.
>
> * `credentialId`
>
>   The email credential ID.
>
> * `credentialType`
>
>   The type of credential that's currently going through verification. This can be `SMS`, `Email`, or `Voice`.
>
> * `errorMessage`
>
>   An optional error message indicating the error encountered during validation, if applicable.
>
> * `informationMessage`
>
>   An optional message containing additional information about the error encountered during validation.
>
> * `friendlyName`
>
>   The friendly name of the added credential. | - `validateSecurityCode`
>
> - `continue`                                                       | The user must verify their email credential to complete the enrollment process.           |
> | `VIP_ENROLLMENT`                             | * `username`
>
>   The authenticating user's username.
>
> * `vipCredentials`
>
>   A list of `VIP Credential Info` objects with details about the credential.
>
> * `suppressAddCredentials`
>
>   Indicates whether the user can add credentials.
>
> * `enableAddingSMSCredential`
>
>   Indicates whether the user can add an SMS credential.
>
> * `enableAddingVoiceCredential`
>
>   Indicates whether the user can add a voice credential.
>
> * `enableAddingEmailCredential`
>
>   Indicates whether the user can add an email credential.                                    | - `addVIPCredential`
>
> - `continue`
>
> - `cancel`                                               | The user can either add a credential or continue to the authentication process.           |
> | `VIP_SMS_CREDENTIAL_REQUIRED`                | * `username`
>
>   The authenticating user's username.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | - `submitSMSCredential`
>
> - `continue`                                                        | The user must submit an SMS credential to complete the enrollment process.                |
> | `VIP_SMS_CREDENTIAL_VERIFICATION_REQUIRED`   | * `username`
>
>   The authenticating user's username.
>
> * `credentialId`
>
>   The SMS credential ID.
>
> * `credentialType`
>
>   The type of credential that's currently going through verification. This can be `SMS`, `Email`, or `Voice`.
>
> * `errorMessage`
>
>   An optional error message indicating the error encountered during validation, if applicable.
>
> * `informationMessage`
>
>   An optional message containing additional information about the error encountered during validation.
>
> * `friendlyName`
>
>   The friendly name of the added credential.   | - `validateSecurityCode`
>
> - `continue`                                                       | The user must verify their SMS credential to complete the enrollment process.             |
> | `VIP_VOICE_CREDENTIAL_REQUIRED`              | * `username`
>
>   The authenticating user's username.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | - `submitVoiceCredential`
>
> - `continue`                                                      | The user must submit a voice credential to complete the enrollment process.               |
> | `VIP_VOICE_CREDENTIAL_VERIFICATION_REQUIRED` | * `username`
>
>   The authenticating user's username.
>
> * `credentialId`
>
>   The voice credential ID.
>
> * `credentialType`
>
>   The type of credential that's currently going through verification. This can be `SMS`, `Email`, or `Voice`.
>
> * `errorMessage`
>
>   An optional error message indicating the error encountered during validation, if applicable.
>
> * `informationMessage`
>
>   An optional message containing additional information about the error encountered during validation.
>
> * `friendlyName`
>
>   The friendly name of the added credential. | - `validateSecurityCode`
>
> - `continue`                                                       | The user must verify their voice credential to complete the enrollment process.           |

> **Collapse: Action models**
>
> | Status                       | Request model                                                                                                                                                                                                               | Action                                                                                                                                                                                | Description                                                                                                                                                                                             |
> | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `initiatePushAuthentication` | This action has no model.                                                                                                                                                                                                   | This action has no errors.                                                                                                                                                            | Initiates push notification authentication.                                                                                                                                                             |
> | `selectVIPCredential`        | * `vipCredentialId`
>
>   The credential ID to use.
>
> * `type`
>
>   The credential type. Possible values are `STANDARD_OTP`, `SMS_OTP`, `EMAIL_OTP`, AND `VOICE_OTP`.                                                             | - Error: `VALIDATION_ERROR`
>
>   ErrorDetail: `INVALID_VIP_CREDENTIAL_ID`: Credential ID isn't valid.
>
>   `AUTHENTICATION_FAILED`: Authentication failed.                                | Select the credential to use for authentication.                                                                                                                                                        |
> | `checkSecurityCode`          | * `securityCode`
>
>   The security code.
>
> * `type`
>
>   The credential type. Possible values are `STANDARD_OTP`, `SMS_OTP`, `EMAIL_OTP`, AND `VOICE_OTP`.                                                                       | - Error: `VALIDATION_ERROR`
>
>   ErrorDetail: `AUTHENTICATION_FAILED`: Failed to authenticate successfully with the given security code.                                                | Validates the entered security code.                                                                                                                                                                    |
> | `cancel`                     | This action has no model.                                                                                                                                                                                                   | This action has no errors.                                                                                                                                                            | Cancels the current authentication step.                                                                                                                                                                |
> | `submitVIPCredential`        | * `vipCredentialId`
>
>   The credential ID.
>
> * `securityCode`
>
>   The security code.                                                                                                                                           | - Error: `VALIDATION_ERROR`
>
>   ErrorDetail: `SUBMIT_VIP_CREDENTIAL_ERROR`: Error adding credential because of an incorrect security code.                                             | Submit a security code to complete the enrollment process of the VIP credential type.                                                                                                                   |
> | `resetVIPCredential`         | * `vipCredentialId`
>
>   The credential ID of the credential to be reset.
>
> * `securityCode`
>
>   A security code from the credential to be reset.
>
> * `nextSecurityCode`
>
>   The next security code from the credential to reset. | - Error: `VALIDATION_ERROR`
>
>   ErrorDetail: `INVALID_VIP_CREDENTIAL_ID`: Invalid credential ID was provided.
>
>   `RESET_VIP_CREDENTIAL_ERROR`: Error encountered resetting credential. | Process with two consecutive security codes to reset the credential.                                                                                                                                    |
> | `submitEmailCredential`      | * `credentialId`
>
>   The new credential ID (email address) to add.
>
> * `friendlyName`
>
>   The friendly name of the email credential.                                                                                           | - Error: `VALIDATION_ERROR`
>
>   ErrorDetail: `SUBMIT_EMAIL_CREDENTIAL_ERROR`: Error adding email credential.                                                                           | Enter your email credentials. An OTP will be sent to the provided email address.When the OTP is presented back for verification, this completes the credential addition process.                        |
> | `validateSecurityCode`       | * `securityCode`
>
>   A security code received by the new credential.                                                                                                                                                         | - Error: `VALIDATION_ERROR`
>
>   ErrorDetail: `AUTHENTICATION_FAILED`: Authentication failed.                                                                                           | Validate the received security code to prove device ownership and complete the credential addition process.                                                                                             |
> | `addVIPCredential`           | * `type`
>
>   The credential type. Acceptable values are `VIP Credential`, `SMS`, `VOICE`, and `Email`.
>
>   If not specified, `VIP Credential` will be used as the default value.                                              | - Error: `VALIDATION_ERROR`                                                                                                                                                           | Initiate credential enrollment process.                                                                                                                                                                 |
> | `continue`                   | This action has no model.                                                                                                                                                                                                   | This action has no errors.                                                                                                                                                            | Continues the current authentication flow.                                                                                                                                                              |
> | `submitSMSCredential`        | * `credentialId`
>
>   The new credential ID (SMS mobile device number) to add.
>
> * `friendlyName`
>
>   The friendly name of the SMS credential.                                                                                  | - Error: `VALIDATION_ERROR`
>
>   ErrorDetail: `SUBMIT_SMS_CREDENTIAL_ERROR`: Error adding SMS credential.                                                                               | Enter your mobile device number. An OTP will be sent to the provided SMS address.When the OTP is presented back for verification, this completes the credential addition process.                       |
> | `submitVoiceCredential`      | * `credentialId`
>
>   The new credential ID (voice mobile device number) to add.
>
> * `friendlyName`
>
>   The friendly name of the voice credential.                                                                              | - Error: `VALIDATION_ERROR`
>
>   ErrorDetail: `SUBMIT_VOICE_CREDENTIAL_ERROR`: Error adding voice credential.                                                                           | Enter your mobile device number. An OTP will be sent to the provided phone number through a voice call.When the OTP is presented back for verification, this completes the credential addition process. |

### Objects

> **Collapse: object**
>
> | Parameter Name           | Type   | Description                                                                      |
> | ------------------------ | ------ | -------------------------------------------------------------------------------- |
> | **numberChallengeValue** | String | If number matching is enabled, this is the number you must enter on the VIP app. |
> | **statusCode**           | String | The status code of the push notification request.                                |
> | **statusMessage**        | String | The status message of the push notification request.                             |

> **Collapse: object**
>
> | Parameter Name            | Type    | Description                                                                                                                                                                                                                                                                                                                                            |
> | ------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> | **id**                    | String  | The credential ID.                                                                                                                                                                                                                                                                                                                                     |
> | **maskedCredentialId**    | String  | The masked credential ID for display purposes.                                                                                                                                                                                                                                                                                                         |
> | **friendlyName**          | String  | The credential's friendly name.                                                                                                                                                                                                                                                                                                                        |
> | **type**                  | String  | The credential type. Possible values are:- `STANDARD_OTP`
>
> - `SMS_OTP`
>
> - `EMAIL_OTP`
>
> - `VOICE_OTP`                                                                                                                                                                                                                                                   |
> | **authenticationInvoked** | Boolean | Indicates whether authentication with associated credentials has been initiated:- For SMS, voice, and email credentials this means Symantec VIP sent a security code using the respective channel.
>
> - For `STANDARD_OTP` credentials, use the code displayed within the app or approve the push notification if push was initiated for authentication. |
> | **pushEnabled**           | Boolean | Indicates whether the credential is push-enabled.                                                                                                                                                                                                                                                                                                      |

### Error codes

If the call flow state hasn't reached a dead end and the user can still authenticate with a device the PingFederate Authentication API returns an error code.

> **Collapse: Top level error codes**
>
> | Error code          | Message                                                                           | HTTP status |
> | ------------------- | --------------------------------------------------------------------------------- | ----------- |
> | `VALIDATION_ERROR`  | One or more validation errors occurred.                                           | `400`       |
> | `INVALID_ACTION_ID` | A push notification was initiated with no underlying support from the credential. | `400`       |

> **Collapse: Detail level error codes**
>
> | Error code                      | Message                                                                | userMessageKey                                                         | Parent code        |
> | ------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------ |
> | `INVALID_VIP_CREDENTIAL_ID`     | Credential ID isn't valid.                                             | `vip.message.invalid.security.code`                                    | `VALIDATION_ERROR` |
> | `AUTHENTICATION_FAILED`         | Message varies based on the error status code returned by the VIP API. | Various message properties associated with `vip.status.message.*` keys | `VALIDATION_ERROR` |
> | `SUBMIT_EMAIL_CREDENTIAL_ERROR` | Error adding an email credential.                                      |                                                                        | `VALIDATION_ERROR` |
> | `SUBMIT_VIP_CREDENTIAL_ERROR`   | Error adding a credential.                                             |                                                                        | `VALIDATION_ERROR` |
> | `RESET_VIP_CREDENTIAL_ERROR`    | Error resetting a credential.                                          |                                                                        | `VALIDATION_ERROR` |
> | `SUBMIT_SMS_CREDENTIAL_ERROR`   | Error adding an SMS credential.                                        |                                                                        | `VALIDATION_ERROR` |
> | `SUBMIT_VOICE_CREDENTIAL_ERROR` | Error adding a voice credential.                                       |                                                                        | `VALIDATION_ERROR` |

---

---
title: Resetting credentials as a user
description: Users can reset their own credentials after failing to authenticate twice in a row.
component: symantec-vip
page_id: symantec-vip:user_credential_management:pf_symantec_vip_ik_resetting_credentials_as_a_user
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/user_credential_management/pf_symantec_vip_ik_resetting_credentials_as_a_user.html
llms_txt: https://docs.pingidentity.com/integrations/symantec-vip/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 24, 2025
section_ids:
  steps: Steps
---

# Resetting credentials as a user

Users can reset their own credentials after failing to authenticate twice in a row.

## Steps

1. Open the VIP Access app on your mobile device.

2. Start the PingFederate authentication flow by signing on to the first-factor authentication adapter.

   For example, this could be an HTML Form Adapter or OpenToken Adapter instance.

3. On the Symantec VIP IdP adapter, sign on with the same username and password.

4. On the **Reset your VIP credential** page, in the **First Security Code** field, enter the security code shown on your VIP Access mobile app or physical VIP security token or card.

   ![The Symantec VIP Adapter credential reset page](_images/credentialResetPage.png)

5. In the **Second Security Code** field, enter the next security code that appears. Click **Submit**.

---

---
title: Symantec VIP IdP adapter settings reference
description: The following tables show field descriptions for the Symantec VIP Adapter configuration page.
component: symantec-vip
page_id: symantec-vip:setup:pf_symantec_vip_ik_symantec_vip_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/setup/pf_symantec_vip_ik_symantec_vip_adapter_settings_reference.html
llms_txt: https://docs.pingidentity.com/integrations/symantec-vip/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2025
---

# Symantec VIP IdP adapter settings reference

The following tables show field descriptions for the **Symantec VIP Adapter** configuration page.

> **Collapse: Standard fields**
>
> | Field                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
> | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Client Certificate**     | Select the VIP Manager certificate that you downloaded and imported into PingFederate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
> | **VIP Configuration Type** | Selection options are:- **Pilot**
>
>   The adapter tests the connection to the VIP application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)*, which is used to verify user-token authentication.
>
> - **Production**
>
>   The adapter runs as normal.&#xA;&#xA;The standard one-time passcode (OTP) security-code generators for VIP are usable only for production. They don't provide valid codes for a pilot configuration. Instead, you must obtain the VIP Test Drive OTP generator for pilot testing.If you have a specific URL to use for the API, enter it in the **Advanced Fields** section. |

> **Collapse: Advanced fields**
>
> | Field                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
> | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Default Authentication Method**                | Determines whether the adapter defaults to push, SMS, or voice, or prompts the user to select an authentication method for the current session. The selection options are:- **None** (default)
>
>   The adapter prompts the user to choose an authentication method or enter a Symantec VIP security code. This is the default selection.
>
> - **Security Code**
>
>   The adapter prompts the user to enter a Symantec VIP security code.
>
> - **Push Notification**
>
>   The adapter sends a push notification to the Symantec VIP app on the user's mobile device.
>
> - **SMS** and **Voice Call**
>
>   The adapter sends a text or voice authentication message to the user's phone number.
>
> - **Email**
>
>   The adapter sends a security code to the user's email address.&#xA;&#xA;If the default method isn't valid for a user, the adapter prompts the user to select another authentication method. |
> | **Override Default Authentication Method**       | When enabled, the adapter checks the **Security Code Attribute Name** defined in the following row.- If the user has a security code in the data store, the adapter passes it to Symantec VIP, allowing the user to skip any prompts.
>
> - If the user does not have a security code in the data store, the adapter falls back to the default authentication method.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
> | **Security Code Attribute Name**                 | The name of the attribute in your data store that contains a user's Symantec VIP security code.&#xA;&#xA;The adapter checks this attribute when Override Default Authentication Method is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
> | **Create User**                                  | Select this checkbox to automatically create a new user in Symantec VIP if the user doesn't already exist.The adapter uses the incoming `User ID` value as the user ID for the new account.This checkbox is cleared by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
> | **Suppress Add Credential**                      | When selected, users aren't shown the interface to register new credentials, such as phone numbers or email addresses.&#xA;&#xA;If you are using this adapter instance in a password reset flow, select this checkbox. This prevents users from bypassing authentication by adding credentials during the password reset flow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
> | **Enable Adding SMS Credential**                 | Select this checkbox to allow users to add **SMS** credentials.This checkbox is cleared by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | **Enable Adding Voice Credential**               | Select this checkbox to allow users to add **Voice Call** credentials.This checkbox is cleared by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
> | **Enable Adding Email Credential**               | Select this checkbox to allow users to add **Email** credentials.This checkbox is cleared by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
> | **Enable Number Matching in Push Notifications** | Select this checkbox to allow users to enter a number to match the number displayed in the push notification.This checkbox is cleared by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | **Visible Leading Characters Length**            | The number of leading characters to display in the credential ID.The default value is `3`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
> | **Visible Trailing Characters Length**           | The number of trailing characters to display in the credential ID.The default value is `3`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
> | **Push Request Timeout**                         | The timeout for push requests, in seconds.The default value is `60`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
> | **Challenge Retries**                            | The maximum number of times that a user can try to authenticate before authentication fails.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
> | **API URL Override**                             | Overrides the API URL defined by the selected **VIP Configuration Type**.Use a URL override to connect to the API service if you have a non-standard pilot or production instance of Symantec VIP.By default, the adapter uses the following URL for a production configuration: https\://userservices-auth.vip.symantec.com/vipuserservices/AuthenticationService\_1\_6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
> | **Management API URL Override**                  | Overrides the Management API URL defined by the selected **VIP Configuration Type**.Use a URL override to connect to the Management API service if you have a non-standard pilot or production instance of Symantec VIP.By default, the adapter uses the following URL for a production configuration: https\://userservices-auth.vip.symantec.com/vipuserservices/ManagementService\_1\_6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
> | **Query API URL Override**                       | Overrides the Query API URL defined by the selected **VIP Configuration Type**.Use a URL override to connect to the Query API service if you have a non-standard pilot or production instance of Symantec VIP.By default, the adapter uses the following URL for a production configuration: https\://userservices-auth.vip.symantec.com/vipuserservices/QueryService\_1\_6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
> | **VIP API URL Override**                         | Overrides the VIP API URL defined by the selected **VIP Configuration Type**.Use a URL override to connect to the VIP API service if you have a non-standard pilot or production instance of Symantec VIP.By default, the adapter uses the following URL for a production configuration: https\://services-auth.vip.symantec.com/mgmt/soap                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
> | **HTML Template Prefix**                         | Identifies the set of HTML templates the adapter users during authentication. You can find a description of the template files in [Download manifest](../release_notes/pf_symantec_vip_ik_download_manifest.html).If you customize the file names of the templates in the `/server/default/conf/template` directory, enter the new prefix in this field.The default value is `vip`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

> **Collapse: Contract attributes**
>
> The adapter contract returns the following attributes when you make a call to it:
>
> | Attribute                              | Description                                                       |
> | -------------------------------------- | ----------------------------------------------------------------- |
> | `subject` (core attribute)             | Specifies the username obtained by the first-factor adapter.      |
> | `credential_id` (non-core attribute)   | Specifies the credential ID used to sign on to Symantec VIP.      |
> | `credential_type` (non-core attribute) | Specifies the type of credential used to sign on to Symantec VIP. |

---

---
title: Symantec VIP Integration Kit
description: The Symantec VIP integration kit allows PingFederate to use Symantec VIP as a second authentication factor for single sign-on (SSO).
component: symantec-vip
page_id: symantec-vip::pf_symantec_vip_ik
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/pf_symantec_vip_ik.html
llms_txt: https://docs.pingidentity.com/integrations/symantec-vip/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 24, 2025
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Symantec VIP Integration Kit

The Symantec VIP integration kit allows PingFederate to use Symantec VIP as a second authentication factor for single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*.

## Components

* Symantec VIP IdP adapter

  * Allows PingFederate to contact the Symantec VIP application programming interface (API) *(tooltip: \<div class="paragraph">
    \<p>A specification of interactions available for building software to access an application or service.\</p>
    \</div>)*, which triggers a multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
    \<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
    \</div>)* request for the user.

  * Accepts a security code from earlier in the authentication flow to allow users to sign on without a prompt.

  * Allows users to add and reset authentication credentials.

* Security code prompt page

  * Allows users to enter a security code from Symantec VIP manually or choose an authentication method.

* Language pack

  * Allows you to customize or localize the messages shown to the user during authentication.

## Intended audience

This document is intended for PingFederate administrators.

Before starting, you should familiarize yourself with the following:

* [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html) in the PingFederate documentation

* [Authentication Policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html) in the PingFederate documentation

## System requirements

* PingFederate 11.3 or later

* A Symantec VIP account

---

---
title: Troubleshooting
description: The following solutions address common situations you might encounter with the Symantec VIP integration kit:
component: symantec-vip
page_id: symantec-vip::pf_symantec_vip_ik_troubleshooting
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/pf_symantec_vip_ik_troubleshooting.html
llms_txt: https://docs.pingidentity.com/integrations/symantec-vip/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 24, 2025
---

# Troubleshooting

The following solutions address common situations you might encounter with the Symantec VIP integration kit:

| Situation                                                                                                               | Recommendation                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| You receive an error in the `server.log` file that says **Operation not allowed in current user status**.               | The user is disabled. Enable the user account in Symantec VIP and try again.                                                                           |
| You receive an error in the `server.log` file that says **No credentials available for reset, failing authentication**. | The user doesn't have any standard credentials available. Have the user install the Symantec VIP mobile app or use an SMS or voice credential instead. |

---

---
title: User credential management
description: Users sign on to their Symantec VIP IdP adapter account using a credential that's associated with their Symantec VIP account.
component: symantec-vip
page_id: symantec-vip:user_credential_management:pf_symantec_vip_ik_user_credential_management
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/user_credential_management/pf_symantec_vip_ik_user_credential_management.html
llms_txt: https://docs.pingidentity.com/integrations/symantec-vip/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 24, 2025
section_ids:
  adding-credentials: Adding credentials
  resetting-credentials: Resetting credentials
---

# User credential management

Users sign on to their Symantec VIP IdP adapter account using a credential that's associated with their Symantec VIP account.

In Symantec VIP, a credential is an authentication method (such as voice or SMS) that is paired with a unique credential ID. The credential ID is shown on the user's VIP Access mobile app, or on their physical VIP security token or card.

## Adding credentials

When you create a user account in Symantec VIP, you must add at least one credential for the user. Additional credentials let the user sign on with different devices or authentication methods.

You can add additional credentials on behalf of a user, or allow users to add their own credentials through the Symantec VIP IdP adapter sign-on page. Learn more in:

* [Adding credentials as an administrator](pf_symantec_vip_ik_adding_credentials_as_an_administrator.html)

* [Adding credentials as a user](pf_symantec_vip_ik_adding_credentials_as_a_user.html)

The **Suppress Add Credentials** setting in the Symantec VIP IdP adapter instance configuration determines whether users are allowed to add credentials.

## Resetting credentials

If a user fails to authenticate twice in a row, the Symantec VIP IdP adapter prompts the user to reset their credentials, as shown in [Resetting credentials as a user](pf_symantec_vip_ik_resetting_credentials_as_a_user.html). This self-service prevents users from locking their accounts and reduces the workload for administrators.