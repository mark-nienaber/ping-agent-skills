---
title: Authenticating with social media providers
description: You can authenticate using social media providers as an external identity provider (IdP) using PingOne and PingFederate.
component: solution-guides
page_id: solution-guides:customer_use_cases:htg_authn_with_social_media
canonical_url: https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_authn_with_social_media.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2025
page_aliases: ["customer_use_cases:htg_authn_with_social_media_p1.adoc", "customer_use_cases:htg_authn_with_social_media_pf.adoc"]
section_ids:
  authenticating-with-social-media-providers-using-pingone: Authenticating with social media providers using PingOne
  authenticating-with-social-media-providers-using-pingfederate: Authenticating with social media providers using PingFederate
  component: Component
  additional-information: Additional information
---

# Authenticating with social media providers

You can authenticate using social media providers as an external identity provider (IdP) using PingOne and PingFederate.

## Authenticating with social media providers using PingOne

Using an external IdP allows linked users to authenticate using the credentials provided by the external IdP. Learn more about using external IdPs with PingOne in [Identity providers](https://docs.pingidentity.com/pingone/integrations/p1_external_idps.html).

Learn more about how to add the following social media providers as an external IdP using PingOne:

* [Amazon](https://docs.pingidentity.com/pingone/integrations/p1_add_idp_amazon_overview.html)

* [Apple](https://docs.pingidentity.com/pingone/integrations/p1_add_idp_apple_prereqs.html)

* [Facebook](https://docs.pingidentity.com/pingone/integrations/p1_addidentityproviderfacebook.html)

* [Google](https://docs.pingidentity.com/pingone/integrations/p1_addidentityprovidergoogle.html)

* [LinkedIn](https://docs.pingidentity.com/pingone/integrations/p1_add_idp_linkedin_prereqs.html)

* [Twitter](https://docs.pingidentity.com/pingone/integrations/p1_add_idp_twitter_prereqs.html)

* [Yahoo](https://docs.pingidentity.com/pingone/integrations/p1_add_idp_yahoo_prereqs.html)

## Authenticating with social media providers using PingFederate

Ping Identity provides several login integration kits that allow PingFederate to coordinate single sign-on (SSO) by using third-party services as IdPs.

### Component

PingFederate 10.3

### Additional information

Learn more in the following topics:

* [Amazon Login Integration Kit](https://docs.pingidentity.com/integrations/amazon/amazon_login_integration_kit/pf_amazon_cic.html)

* [Apple Login Integration Kit](https://docs.pingidentity.com/integrations/apple/pf_apple_cic.html)

* [Facebook Login Integration Kit](https://docs.pingidentity.com/integrations/facebook/facebook_login_integration_kit/pf_facebook_cic.html)

* [Google Login Integration Kit](https://docs.pingidentity.com/integrations/google/google_login_integration_kit/pf_google_cic.html)

* [LinkedIn Login Integration Kit](https://docs.pingidentity.com/integrations/linkedin/pf_linkedin_cic.html)

* [Twitter Login Integration Kit](https://docs.pingidentity.com/integrations/twitter/pf_twitter_cic.html)

---

---
title: Customer Use Cases
description: Authenticating with social media providers
component: solution-guides
page_id: solution-guides:customer_use_cases:htg_customer
canonical_url: https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_customer.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 19, 2024
---

# Customer Use Cases

| Use case                                                                                               | Description                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Authenticating with social media providers](htg_authn_with_social_media.html)                         | You can authenticate using social media providers as an external identity provider (IdP) using PingOne and PingFederate                                                                                                           |
| [Customizing SSO user sign-on windows in PingFederate](htg_customize_sso_user_sign_on_windows_pf.html) | You can customize the default single sign-on (SSO) end user sign-on window for PingFederate.                                                                                                                                      |
| [Enabling MFA for your application](htg_enable_mfa_for_app.html)                                       | Enable an authentication policy that includes multi-factor authentication (MFA) for your applications in PingOne.                                                                                                                 |
| [Obtaining logging data from PingOne](htg_obtain_logging_data_p1.html)                                 | Learn how to obtain logging data from PingOne.                                                                                                                                                                                    |
| [Setting up an agent in PingAccess](htg_agent_setup_pa.html)                                           | Learn how to set up an agent integration for PingAccess applications.                                                                                                                                                             |
| [Setting up an OIDC application in PingFederate](htg_oidc_app_setup_pf.html)                           | Create a new OAuth or OpenID Connect (OIDC) application in PingFederate.                                                                                                                                                          |
| [Setting up and customizing sign-on windows in PingOne](htg_sign_on_window_setup_p1.html)              | Customize the sign-on window in PingOne to match your company's desired branding and themes.                                                                                                                                      |
| [Setting up password recovery in PingOne](htg_password_recovery_setup_p1.html)                         | Learn how to set up password recovery for an application using PingOne.                                                                                                                                                           |
| [Setting up password reset in PingOne](htg_password_reset_setup_p1.html)                               | Learn how to customize the user's sign-on experience by enabling self-service management, such as change password and password reset, in the PingFederate administrative console when using the company's HTML Form sign-on page. |
| [Setting up PingDataSync between Active Directory and PingOne](htg_pds_setup_between_ad_and_p1.html)   | Learn how to configure PingDataSync for Microsoft Active Directory (AD) to PingOne in a Windows environment.                                                                                                                      |
| [Setting up PingDataSync between PingDirectory and PingOne](htg_pds_setup_between_pd_and_p1.html)      | Learn how to set up PingDataSync between PingDirectory and PingOne using installation commands for Linux.                                                                                                                         |

---

---
title: Customizing SSO user sign-on windows in PingFederate
description: You can customize the default single sign-on (SSO) end user sign-on window for PingFederate. Learn more about customizable user-facing pages in IdP user-facing pages in the PingFederate documentation.
component: solution-guides
page_id: solution-guides:customer_use_cases:htg_customize_sso_user_sign_on_windows_pf
canonical_url: https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_customize_sso_user_sign_on_windows_pf.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2025
page_aliases: ["customer_use_cases:htg_customize_sso_user_sign_on_windows_pf_default_template.adoc", "customer_use_cases:htg_customize_sso_user_sign_on_windows_pf_custom_css.adoc", "customer_use_cases:htg_customize_sso_user_sign_on_windows_pf_custom_background.adoc"]
section_ids:
  component: Component
  configuration-instructions: Configuration instructions
  formatting-the-default-sign-on-window-template: Formatting the default sign-on window template
  steps: Steps
  using-css-to-customize-sso-user-sign-on-windows-in-pingfederate: Using CSS to customize SSO user sign-on windows in PingFederate
  about-this-task: About this task
  steps-2: Steps
  example: Example:
  setting-up-a-custom-background-for-the-sso-user-sign-on-window-in-pingfederate: Setting up a custom background for the SSO user sign-on window in PingFederate
  about-this-task-2: About this task
  steps-3: Steps
  example-2: Example:
  result: Result:
---

# Customizing SSO user sign-on windows in PingFederate

You can customize the default single sign-on (SSO) end user sign-on window for PingFederate. Learn more about customizable user-facing pages in [IdP user-facing pages](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_idp_user_facing_pages.html) in the PingFederate documentation.

## Component

PingFederate 10.1 and later

## Configuration instructions

Read the following sections for instructions specific to the configuration you are performing.

## Formatting the default sign-on window template

### Steps

1. To view the various HTML files that PingFederate presents to the end user, in your PingFederate server open the `<pf_install>/pingfederate/server/default/conf/template` folder.

2. Format the default sign-on window template.

   1. Open the `html.form.login.template.html`.

      This document contains the default sign-on window.

   2. Customize the content of the sign-on window.

      |   |                                                                                                                                                                                                  |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | The `html.form.login.template.html` file contains information in comments to assist you in customizing the content of the web page.Remember to save a backup or copy of the file before editing. |

3. Save the `html.form.login.template.html` file.

4. If you changed the name of the `html.form.login.template.html` file, you must update it in the PingFederate administrative console.

   1. In the PingFederate administrative console, go to **Authentication > Integration > IdP Adapters**.

   2. Click the adapter that you want to modify.

   3. On the **IdP Adapter** tab, scroll to the bottom and click **Show Advanced Fields**.

   4. In the **Login Template** field, enter the updated `html` login template.

   5. Save your changes.

## Using CSS to customize SSO user sign-on windows in PingFederate

Edit the CSS in the `main.css` directory file to set up a custom background for your single sign-on (SSO) end user sign-on window in PingFederate.

### About this task

If you are familiar with CSS, you can edit the `main.css` directory file to customize the background of your PingFederate SSO sign-on window as desired.

If you are running PingFederate in a cluster, you must make these changes on each runtime node.

### Steps

1. Open the `<pf_install>/pingfederate/server/default/conf/template/css/main.css` file.

2. Edit the `main.css` file.

   |   |                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------- |
   |   | Remember to create a copy or backup of the `main.css` file in case you need to revert to the default settings. |

   1. To locate the `html` rule set, open the file and search for `html {`.

      #### Example:

      ```css
      html {
        height: 100%;
        background-color: #f7f7f7;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-color: #3d454d;
        background-color: rgba(61, 69, 77, 0.9) \9;
        /*IE9 hack */
        background-image: radial-gradient(40% 40%, circle cover, rgba(61, 69, 77, 0.9) 30%, #3d454d 80%);
        background-image: -o-radial-gradient(40% 40%, circle cover, rgba(61, 69, 77, 0.9) 30%, #3d454d 80%);
        background-image: -ms-radial-gradient(40% 40%, circle cover, rgba(61, 69, 77, 0.9) 30%, #3d454d 80%);
        background-image: -moz-radial-gradient(40% 40%, circle cover, rgba(61, 69, 77, 0.9) 30%, #3d454d 80%);
        background-image: -webkit-radial-gradient(40% 40%, circle cover, rgba(61, 69, 77, 0.9) 30%, #3d454d 80%);
        -webkit-background-size: cover;
        -moz-background-size: cover;
        -o-background-size: cover;
        background-size: cover;
      }
      ```

   2. Edit the CSS as desired.

3. Save the `main.css` file.

## Setting up a custom background for the SSO user sign-on window in PingFederate

Edit the `main.css` directory file to set up a custom background for your single sign-on (SSO) end user sign-on window in PingFederate.

### About this task

This procedure is applicable for PingFederate 8.4.x and later.

If you are unfamiliar with CSS, you can use this workaround to edit the `main.css` file in the PingFederate directory server. Perform the following changes to specify the desired PingFederate server image file for your custom background.

If you are running PingFederate in a cluster, you must make these changes on each runtime node.

### Steps

1. Select the image you want to use as a custom background and save it as `<pf_install>/pingfederate/server/default/conf/template/images/custombackground.png`.

   |   |                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------- |
   |   | To update the image later, repeat step 1 or update the filepath in the `main.css` file to point to a different image. |

2. Open the `<pf_install>/pingfederate/server/default/conf/template/assets/css/main.css` file.

3. Edit the `main.css` file.

   |   |                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------- |
   |   | Remember to create a copy or backup of the `main.css` file in case you need to revert to the default settings. |

   1. To locate the `html` rule set, open the file and search for `html {`.

      #### Example:

      ```css
      html {
        height: 100%;
        background-color: #f7f7f7;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-color: #3d454d;
        background-color: rgba(61, 69, 77, 0.9) \9;
        /*IE9 hack */
        background-image: radial-gradient(40% 40%, circle cover, rgba(61, 69, 77, 0.9) 30%, #3d454d 80%);
        background-image: -o-radial-gradient(40% 40%, circle cover, rgba(61, 69, 77, 0.9) 30%, #3d454d 80%);
        background-image: -ms-radial-gradient(40% 40%, circle cover, rgba(61, 69, 77, 0.9) 30%, #3d454d 80%);
        background-image: -moz-radial-gradient(40% 40%, circle cover, rgba(61, 69, 77, 0.9) 30%, #3d454d 80%);
        background-image: -webkit-radial-gradient(40% 40%, circle cover, rgba(61, 69, 77, 0.9) 30%, #3d454d 80%);
        -webkit-background-size: cover;
        -moz-background-size: cover;
        -o-background-size: cover;
        background-size: cover;
      }
      ```

   2. Replace the declaration block for the `html` rule set with the following declaration block.

      ```css
      html {
        height: 100%;
        background-color: #f7f7f7;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-image: url(../images/custombackground.png);
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        background-size: cover;
      }
      ```

4. Save the `main.css` file.

   ### Result:

   The background image points to the `<pf_install>/pingfederate/server/default/conf/template/images/custombackground.png` file.

---

---
title: Enabling MFA for your application
description: Enable an authentication policy that includes multi-factor authentication (MFA) for your applications in PingOne.
component: solution-guides
page_id: solution-guides:customer_use_cases:htg_enable_mfa_for_app
canonical_url: https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_enable_mfa_for_app.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Enabling MFA for your application

Enable an authentication policy that includes multi-factor authentication (MFA) for your applications in PingOne.

## Before you begin

* Register for a PingOne tenant.

* To use a custom application for MFA, the application must already be configured.

* Configure an application connection.

## Steps

1. In the PingOne dashboard, click **Settings**.

2. Go to **Authentication > Policies**, and then click **+Add Policy**.

3. Select an option for the first **Step Type**.

   There are multiple options depending on how you would like your user experience to be. For this example, **Login** was selected.

   ![Screen capture showing Login chosen as the first step type.](_images/iax1600197124996.png)

4. Click **+Add Step**, and then select **Multi-factor Authentication**.

5. Select the methods you want to enable for your users.

   If you have created a mobile application for MFA, you will have an option to select the appropriate application to associate to this login logic.

6. Select pertinent rules to be evaluated when a user is processed through this policy.

   Learn more about these options in [Adding a multi-factor authentication step](https://docs.pingidentity.com/pingone/authentication/p1_add_mfa_step.html).

7. Review your selections, and then click **Save**.

8. Click **Connections**.

9. Select the desired connection you want to add your new policy to and click the **Pencil** ([icon: pencil, set=fa]) icon.

   ![Screen capture of the Applications window with an application selected and the Pencil icon highlighted.](_images/fbc1600197671444.png)

10. Click the **Policies** tab.

11. Drag and drop your policy from the **All Policies** list to the **Applied Policies** list.

    ![Screen capture of the Policies tab with the All Policies and Applied Policies lists displayed. One policy, shown in dark blue gray, has already been dragged to the Applied Policies list.](_images/int1600197337483.png)

12. Click **Save**.

---

---
title: Obtaining logging data from PingOne
description: Sign on to PingOne and select your environment.
component: solution-guides
page_id: solution-guides:customer_use_cases:htg_obtain_logging_data_p1
canonical_url: https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_obtain_logging_data_p1.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2025
page_aliases: ["customer_use_cases:htg_obtain_logging_data_p1_audit_params.adoc"]
section_ids:
  steps: Steps
  result: Result:
  example: Example
  next-steps: Next steps
  audit-parameter-fields: Audit parameter fields
---

# Obtaining logging data from PingOne

## Steps

1. Sign on to PingOne and select your environment.

   ![Screen capture of the PingOne Your Environments page showing a list of available environments.](_images/oxv1621447315044.png)

2. In the left navigation pane, click **Audit**.

   ![Screen capture of the PingOne Overview page in the Dashboard navigation pane with the Audit section circled in white.](_images/ndk1621447392544.png)

3. In the **Audit Parameters** section, adjust the audit parameters fields as needed.

   ![Screen capture of the Audit Parameters section in PingOne, with the Time Range, Within, Filter Type, Selected Fields, Time Zone, and Secondary Filter Type fields.](_images/zuu1621447468128.png)

4. To update the report, click **Run**.

   ### Result:

   The audit report is created.

   ![Screen capture of a sample audit report showing the Timestamp, Event Type, Description, Client, Population, and Details columns in the audit report from PingOne.](_images/zzd1621275866349.png)

   |   |                                                                                        |
   | - | -------------------------------------------------------------------------------------- |
   |   | If no fields are selected, the audit report only contains an empty **Details** column. |

## Example

The **Details** column contains a **View** link showing the JSON representation of the audit entry, as shown in the following example.

|   |                                                                   |
| - | ----------------------------------------------------------------- |
|   | All unique identifiers in this example are intentionally blocked. |

```json
{
 "_links": {
   "self": {
     "href": "https://api.pingone.com/v1/environments/429f5783-0f16-432f-b726-88223c380ab0/activities/979c1096-a693-4920-a2c6-62e34ff74dfe"
   }
 },
 "id": "9*******-a***-4***-a***-6**********",
 "recordedAt": "2021-04-06T16:27:34.783Z",
 "createdAt": "2021-04-06T16:27:34.803Z",
 "correlationId": "f******-2***-4***-9***-6***********",
 "actors": {
   "client": {
     "id": "b*******-4***-4***-9***-0************",
     "name": "PingOne Admin Console",
     "environment": {
       "id": "4*******-0***-4***-b***-8***********"
     },
     "href": "https://api.pingone.com/v1/environments/4*******-4*******-0***-4***-b***-8***********/applications/b*******-4***-4***-9***-0***********",
     "type": "CLIENT"
   },
   "user": {
     "id": "7*******-5***-4***-9***-d***********",
     "name": "m******p********@pingidentity.com",
     "environment": {
       "id": "4*******-0***-4***-b***-8***********"
     },
     "population": {
       "id": "4*******-0***-4***-b***-8***********"
     },
     "href": "https://api.pingone.com/v1/environments/4*******-0***-4***-b***-8***********/users/7*******-5***-4***-9***-d***********",
     "type": "USER"
   }
 },
 "action": {
   "type": "USER.ACCESS_ALLOWED",
   "description": "User Access Allowed"
 },
 "resources": [
   {
     "type": "USER",
     "id": "7*******-5***-4***-9***-d***********",
     "name": "matthewpollicove@pingidentity.com",
     "environment": {
       "id": "4*******-0***-4***-b***-8***********"
     },
     "population": {
       "id": "4*******-0***-4***-b***-8***********"
     },
     "href": "https://api.pingone.com/v1/environments/4*******-0***-4***-b***-8***********/users/7*******-5***-4***-9***-d***********"
   }
 ],
 "result": {
   "status": "SUCCESS",

   "description": "Passed role access control"
 }
}
```

## Next steps

If you need to connect the audit data to an external application, such as Splunk, learn more in [Monitoring activity with Splunk](https://docs.pingidentity.com/pingone/developer_tools/p1_monitor_activity_splunk.html).

## Audit parameter fields

The following table describes the fields and options available in the **Audit Parameters** section of PingOne.

| Field                                                                                                  | Option                  | Description                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------ | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Time Range**                                                                                         | **Specific**            | Set the time range to a specific date range.                                                                                                                                                                                                                     |
|                                                                                                        | **Relative**            | Set the time range to a period relative to the current time.                                                                                                                                                                                                     |
| **Filter Type**&#xA;&#xA;You must select a Filter Type before the Secondary Filter field is available. | **Resource ID**         | Find activities by resource ID.                                                                                                                                                                                                                                  |
|                                                                                                        | **Correlation ID**      | Find activities by correlation ID. When an HTTP request is received by PingOne, it is assigned a correlation ID. You can use the correlation ID to associate HTTP responses with messages in the event log.                                                      |
|                                                                                                        | **Event type**          | Find activities by event type.Select an event type. If **Risk** is enabled, the following parameters are available:- **Risk Evaluation Created**

- **Risk Evaluation Updated**

- **Risk Policy Created**

- **Risk Policy Deleted**

- **Risk Policy Updated** |
|                                                                                                        | **User ID (Actor)**     | Find activities that were performed by a particular user by user ID.                                                                                                                                                                                             |
|                                                                                                        | **Username (Actor)**    | Find activities that were performed by a particular user by username.                                                                                                                                                                                            |
|                                                                                                        | **Client (Actor)**      | Select a client to find activities that were performed by that client.The list of clients can vary depending on your configuration.                                                                                                                              |
|                                                                                                        | **Resource population** | Select a population to find activities that were performed in resources within a particular population.                                                                                                                                                          |
|                                                                                                        | **Resource type**       | Select a resource to find activities that were performed on a particular type of resource.                                                                                                                                                                       |
|                                                                                                        | **Population**          | Find activities that were performed on a particular population.                                                                                                                                                                                                  |
|                                                                                                        | **User**                | Find activities that were performed on a particular user.                                                                                                                                                                                                        |
|                                                                                                        | **Application**         | Find activities that were performed by a particular client application.                                                                                                                                                                                          |
| **Selected Fields**                                                                                    | **Timestamp**           | The date and time of the event.The format is: MM/DD/YYYY HH:mm:ss.                                                                                                                                                                                               |
|                                                                                                        | **Event name**          | A unique identifier for the event.                                                                                                                                                                                                                               |
|                                                                                                        | **Description**         | A brief description of the event.                                                                                                                                                                                                                                |
|                                                                                                        | **Client**              | The client that performed the event.                                                                                                                                                                                                                             |
|                                                                                                        | **User identity**       | The user for which the event was performed.                                                                                                                                                                                                                      |
|                                                                                                        | **Population**          | The population in which the event was performed.                                                                                                                                                                                                                 |
|                                                                                                        | **Resource type**       | The type of resource for which the event was performed.                                                                                                                                                                                                          |

---

---
title: Resetting a password through a text or SMS message
description: Configure an SMS provider in an HTML Form Adapter instance in PingFederate for users to receive a text message notification with a one-time passcode (OTP) to reset their password.
component: solution-guides
page_id: solution-guides:customer_use_cases:htg_password_reset_p1_method_message
canonical_url: https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_password_reset_p1_method_message.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 29, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
---

# Resetting a password through a text or SMS message

Configure an SMS provider in an HTML Form Adapter instance in PingFederate for users to receive a text message notification with a one-time passcode (OTP) to reset their password.

## Before you begin

* Make sure **Password Reset Type** is set to **Text Message** in your HTML Form Adapter instance configuration.

## Steps

1. Go to **Authentication****IdP Adapters** and, in the **Instance Name** list, select the adapter instance that you want to use.

2. Go to the **IdP Adapter** tab and click **Manage SMS Provider Settings**.

![A screen capture of the IdP Adapters instance configuration in . On the IdP Adapter tab, the user can modify various instance settings by clicking Manage Password Credential Validators, Mange SMS provider Settings, Mange Local Identity Profiles, Manage Notification Publishers, Manage CAPTCHA Settings, or Manage Policy Contracts, as well as Show Advanced Fields to display more configuration settings. To open and edit the SMS Provider configuration, the user clicks Manage SMS Provider Settings. To finalize, edit, or undo any changes, the user clicks Save, Next, Previous, or Cancel.](_images/ghy1605660160622.png)

1. In the **Manage SMS Provider Settings** page, edit the **Account SID**, **Auth Token**, **From Number** fields to match your service account. Click **Save**.

![A screen capture of the Manage SMS Provider Settings window configuration in to connect to an SMS Provider. The user can edit the Account SID, Auth Token, and From Number fields to match their service account. The user can click Save to save their changes or Cancel to undo any new changes.](_images/spc1605660341199.png)

\+

### Result:

\+ You're returned to the **Create Adapter Instance** page.

1. On the **Summary** tab, click **Save**.

2. Go to the **Sign On** page and click the **Trouble Signing On?** link. ![A screen capture of the Sign On page. The Sign On page has the username and password fields and Sign On button. If the user is having issues signing on, the Change Password and Trouble Signing On links are provided.](_images/lkb1605644195117.jpg)

   ### Result:

   A text message notification with an OTP is sent to your mobile phone.

3. In the **Account Recovery** page, in the **Enter Security Code** field, enter the OTP. Click **Validate**.

   ### Result:

   You're directed to the **Reset Your Password** page.

4. Enter a new password in the **New Password** and the **Confirm New Password** fields. Click **Reset**.

![A screen capture of the Reset Your Password page. The page displays the New Password and Confirm New Password fields, requesting the user to enter and reenter their password change. The user can click Reset to confirm and save the password changes or Cancel to stop the password changing process.](_images/oso1605568287541.jpg)

---

---
title: Resetting a password through the HTML Form sign on page
description: Change your password through the HTML Form sign-on page.
component: solution-guides
page_id: solution-guides:customer_use_cases:htg_password_reset_p1_method_html_form
canonical_url: https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_password_reset_p1_method_html_form.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 29, 2024
section_ids:
  steps: Steps
---

# Resetting a password through the HTML Form sign on page

Change your password through the HTML Form sign-on page.

## Steps

1. Go to the **Sign On** page and click the **Trouble Signing On?** link. ![A screen capture showing the Sign On dialog.](_images/lkb1605644195117.jpg)

2. On the **Account Recovery** page, in the **Username** field, enter the username associated with your account. Click **Send Request**. ![A screen capture of the Account Recovery page. The page displays a username field, requesting the entry to an enable password reset request. The user has the option to click Send Request to progress or Cancel to stop the password reset process.](_images/fab1605644111256.jpg)

3. On the **Reset Your Password** page, enter a new password in the **New Password** and **Confirm New Password** fields. Click **Reset**.

![A screen capture of the Reset Your Password page. The page displays the New Password and Confirm New Password fields, requesting the user to enter and reenter their password change. The user can click Reset to confirm and save the password changes or Cancel to stop the password changing process.](_images/oso1605568287541.jpg)

---

---
title: Resetting a password using a link through email
description: Reset a password using a one-time link sent to a user's email account.
component: solution-guides
page_id: solution-guides:customer_use_cases:htg_password_reset_p1_method_email
canonical_url: https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_password_reset_p1_method_email.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 29, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  result-4: Result:
  result-5: Result:
  choose-from: Choose from:
  result-6: Result:
  result-7: Result:
---

# Resetting a password using a link through email

Reset a password using a one-time link sent to a user's email account.

## Before you begin

* Make sure **Password Reset Type** is set to **Email One-Time Link** in your HTML Form Adapter instance configuration.

## About this task

For resetting a password using an email link, you must set up an SMTP mail server.

## Steps

1. Go to **Authentication****IdP Adapters** and, in the **Instance Name** list, select the adapter instance that you want to use.

2. **Optional:** Create a local identity profile (LIP).

   |   |                                                                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Do this step if you want to allow self-service registration using their local identity profile, such as managing a password reset or forgot password scenario. If not, you can skip this step and go to step 3. |

   1. On the **IdP Adapter** tab, click **Manage Local Identity Profiles**.

      ### Result:

      The **Local Identity Profiles** page opens.

   2. Reuse an existing Local Identity Profile or click **Create New Profile** to create a new profile.

      ### Result:

      The **Local Identity Profile** page opens.

   3. On the **Profile Info** tab, select the **Enable Registration** checkbox to show the **Email Verification** tab and email configuration settings for this identity profile. Click **Next**.

   4. On the **Email Verification** tab, select the **Enable Email Ownership Verification** checkbox to show additional email verification settings. Click **Next**.

   5. On the **Summary** tab, click **Done**.

      ### Result:

      You're returned to the **Create Adapter Instance** page.

3. On the **IdP Adapter** tab, click **Manage Notification Publishers**.

   ### Result:

   The **Notification Publishers** page opens.

4. Reuse an existing instance or click **Create New Instance** to create a new one.

   ### Result:

   The **Create Notification Publisher Instance** page opens.

5. On the **Type** tab, in the **Type**list, select **SMTP Notification Publisher**. Click **Next**.

6. On the **Instance Configuration** tab, in the **Email Server** field, enter one of the following:

   ### Choose from:

   * a mailtrap.io

   * a gmail smtp server

   ![A screen capture of the Instance Configuration tab within the Create Notification Publisher Instance configuration window. There are settings to configure the server to communicate with your organization's SMTP mail server. The user can edit the From Address, Email Server, SMTP Port, Encryption Method, SMTPS Port, Verify Hostname, and UTF-8 Message Header Support settings. In this screen capture the SMTP Port field has 25 entered, the Encryption Method drop-down has None selected, the SMTPS Port has 465 entered, and the Verify Hostname checkbox is selected.](_images/joa1606333432434.png)

7. Click **Next**.

8. On the **Summary** tab, click **Save**.

9. Go to the user **Sign On** page and click the **Trouble Signing On?** link.

   ![A screen capture of the Sign On page. The page displays the username and password fields as well as the Sign On button. If the user is having issues signing on the Change Password and Trouble Signing On links are provided.](_images/lkb1605644195117.jpg)

   ### Result:

   An email containing a one-time password reset link is sent to your email.

10. In your email inbox, open the password reset email from PingFederate. Click on the link provided to reset your password.

    ### Result:

    You're directed to the **Reset Your Password** page.

11. In the **Reset Your Password** page, enter a new password in the **New Password** and **Confirm New Password** fields. Click **Reset**.

![A screen capture of the Reset Your Password page. The page displays the New Password and Confirm New Password fields, requesting the user to enter and reenter their password change. The user can click Reset to confirm and save the password changes or Cancel to stop the password changing process.](_images/oso1605568287541.jpg)

---

---
title: Resetting a password using a one-time passcode through email
description: Reset a password through a user's email account using a one-time passcode (OTP) .
component: solution-guides
page_id: solution-guides:customer_use_cases:htg_password_reset_p1_method_otp
canonical_url: https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_password_reset_p1_method_otp.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 29, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  result-4: Result:
  result-5: Result:
  choose-from: Choose from:
  result-6: Result:
  result-7: Result:
  result-8: Result:
---

# Resetting a password using a one-time passcode through email

Reset a password through a user's email account using a one-time passcode (OTP) .

## Before you begin

* Make sure **Password Reset Type** is set to **Email One-Time Password** in your HTML Form Adapter instance configuration.

## About this task

For resetting a password with a one-time passcode through email, you must setup a SMTP mail server in PingFederate.

## Steps

1. Go to **Authentication****IdP Adapters** and, in the **Instance Name** list, select the adapter instance that you want to use.

2. **Optional:** Create a local identity profile (LIP).

   |   |                                                                                                                                                                                                                      |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Perform this step if you want to allow the user to manage self-service registration using their LIP, such as managing a password reset or forgot password scenario. If not, you can skip this step and go to step 3. |

   1. On the **IdP Adapter** tab, click **Manage Local Identity Profiles**.

      ### Result:

      The **Local Identity Profiles** page opens.

   2. Reuse an existing Local Identity Profile or click **Create New Profile** to create a new profile.

      ### Result:

      The **Local Identity Profile** page opens.

   3. On the **Profile Info** tab, select the **Enable Registration** checkbox to show the **Email Verification** tab and configuration settings for this identity profile. Click **Next**.

   4. On the **Email Verification** tab, select the **Enable Email Ownership Verification** checkbox to show additional email verification settings. Click **Next**.

   5. On the **Summary** tab, click **Done**.

      ### Result:

      You're returned to the **Create Adapter Instance** window.

3. On the **IdP Adapter** tab, click **Manage Notification Publishers**.

   ### Result:

   The **Notification Publishers** page opens.

4. Click **Create New Instance**.

   ### Result:

   The **Create Notification Publisher Instance** page opens.

5. On the **Type** tab, from the **Type** list, select **SMTP Notification Publisher**. Click **Next**.

6. On the **Instance Configuration** tab, in the **Email Server** field, enter one of the following:

   ### Choose from:

   * a mailtrap.io

   * a gmail smtp server

   ![A screen capture of the Instance Configuration tab in the Create Notification Publisher Instance configuration window. There are settings to configure the server to communicate with your organization's SMTP mail server. The user can edit the From Address, Email Server, SMTP Port, Encryption Method, SMTPS Port, Verify Hostname, and UTF-8 Message Header Support settings. In this screen capture the SMTP Port field has 25 entered, the Encryption Method drop-down has None selected, the SMTPS Port has 465 entered, and the Verify Hostname checkbox is selected.](_images/joa1606333432434.png)

7. Click **Next**.

8. On the **Summary** tab, click **Save**.

9. Go to the **Sign On** page and click the **Trouble Signing On?** link.

   ![A screen capture of the Sign On page. The page displays the username and password fields as well as the Sign On button. If the user has issues signing on, the Change Password and Trouble Signing On links are provided.](_images/lkb1605644195117.jpg)

   ### Result:

   A password reset notification email containing an OTP is sent to your inbox.

10. In your email inbox, open the password reset email from PingFederate and copy the OTP.

    ### Result:

    You're directed to the **Account Recovery** page.

11. In the **Account Recovery** page, in the **Enter Security Code** field, paste the OTP. Click **Validate**.

![A screen capture of the Account Recovery page. There is the Enter Security Code field, which is requesting the one-time passcode sent to the user's email, and the Validate and Cancel buttons. The user can click Validate to progress or Cancel to stop the password reset process.](_images/sbx1605897984078.jpg)

\+

### Result:

\+ You're directed to the **Reset Your Password** page.

1. Enter a new password in the **New Password** and **Confirm New Password** fields. Click **Reset**.

![A screen capture of the Reset Your Password page. The page displays the New Password and Confirm New Password fields, requesting the user to enter and reenter their password change. The user can click Reset to confirm and save the password changes or Cancel to stop the password changes.](_images/oso1605568287541.jpg)

---

---
title: Setting up an agent in PingAccess
description: Learn how to set up an agent integration for PingAccess applications.
component: solution-guides
page_id: solution-guides:customer_use_cases:htg_agent_setup_pa
canonical_url: https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_agent_setup_pa.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 14, 2025
page_aliases: ["customer_use_cases:htg_agent_setup_pa_config_agent.adoc", "customer_use_cases:htg_agent_setup_pa_config_token_provider.adoc", "customer_use_cases:htg_agent_setup_pa_install_agent.adoc"]
section_ids:
  component: Component
  configuring-an-agent-for-pingaccess: Configuring an agent for PingAccess
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
  example: Example:
  result-2: Result:
  configuring-a-token-provider: Configuring a token provider
  steps-2: Steps
  example-2: Example:
  installing-the-agent: Installing the agent
  steps-3: Steps
---

# Setting up an agent in PingAccess

Learn how to set up an agent integration for PingAccess applications.

## Component

* PingAccess 8.2

* PingAccess 6.3

## Configuring an agent for PingAccess

### Before you begin

* Install PingAccess with either a PingFederate, PingOne, or OpenID Connect (OIDC) token provider configured.

### Steps

1. Sign on to the PingAccess admin console.

2. Go to **Applications > Agents** and click **[icon: plus, set=fa]Add Agents**:

   1. In the **Name** field, enter a name for the agent.

   2. In the **PingAccess Host** field, enter a host name and port number.

   3. To retrieve the `agent.properties` file to use during the agent installation process, click **Save & Download**.

      |   |                                                                                                                                                                                                                                |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | In most deployments the host name and port must match the `agent.http.port` value in the PingAccess `run.properties` file (default `3030`).The host name and port of the PingAccess server is where this agent sends requests. |

3. Go to **Applications > Applications**.

4. To connect the newly created agent with a PingAccess application, click **[icon: plus, set=fa]Add Application**:

   1. In the **Name** field, enter an application name.

   2. In the **Context Root** field, enter an appropriate value.

   3. In the **Virtual Host(s)** section, click **[icon: plus, set=fa]Create**.

   4. Create a virtual host that matches the agent server's host and port values that users will access, then click **Save**.

5. In the `Web Session` section, click **[icon: plus, set=fa]Create** to create a new web session:

   1. In the **Name** field, enter a name for the web session.

   2. In the **Audience** field, enter the names of the applications using this web session.

   3. In the **Client ID** and **Client Secret** fields, enter the OIDC Login Type values from the PingAccess token provider.

   4. Click **Save**.

      #### Result:

      You return to the **New Application** page.

6. In the **Web Identity Mapping** section, click **[icon: plus, set=fa]Create** to create a new mapping:

   1. In the **Name** field enter an identity mapping name.

   2. In the **Type** list, select **Header Identity Mapping**.

   3. In the **Attributes** section, click **Exclusion List**.

   4. In the **Header Name Prefix** field, enter a prefix pattern the agent application will expect.

      #### Example:

      If your user was Ping, your prefix header for the username field would be "ping-" and then it would say ping-username.

   5. In the **Attribute to Header Mapping** section, click **[icon: plus, set=fa]Add Row**.

   6. In the **Subject Attribute Name** list, select the attribute that corresponds to the user's subject value.

   7. In the **Header Name** field, enter a header name.

   8. Click **Save**.

      #### Result:

      You return to the **New Application** configuration page.

7. In the **Destination** list, select **Agent**.

8. In the **Agent** list, select the agent you created earlier.

9. Select the **Enabled** checkbox and click **Save**.

## Configuring a token provider

### Steps

* For the PingAccess token provider that you're using, add the virtual host's redirect URI to the OAuth client selected for the web session of the created application.

  #### Example:

  https\://*\<virtualhostname>*:*\<virtualhostnameport>*/pa/oidc/cb

## Installing the agent

### Steps

1. Download the appropriate agent installation file from the PingAccess [Add-Ons Downloads](https://www.pingidentity.com/en/resources/downloads/pingaccess.html) page.

2. Configure the PingAccess agent installation.

   You can find installation instructions for each agent type in PingAccess [Agents and Integrations](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=362) (page 362).

3. Copy the `agent.properties` file that you downloaded previously into the PingAccess agent installation directory.

   |   |                                                       |
   | - | ----------------------------------------------------- |
   |   | The properties file must be named `agent.properties`. |

4. To deploy the new PingAccess agent configuration to the desired resources, restart the web or API service that you just installed the agent on.

---

---
title: Setting up an OIDC application in PingFederate
description: Create a new OAuth or OpenID Connect (OIDC) application in PingFederate.
component: solution-guides
page_id: solution-guides:customer_use_cases:htg_oidc_app_setup_pf
canonical_url: https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_oidc_app_setup_pf.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  choose-from-3: Choose from:
---

# Setting up an OIDC application in PingFederate

Create a new OAuth or OpenID Connect (OIDC) application in PingFederate.

## Before you begin

**Component**

* PingFederate 10.1

Do the following:

* [Install PingFederate](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=108).

* [Configure an access token manager](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=550) (page 550).

* [Configure an OIDC policy](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=572) (page 572).

* [Map authentication sources to persistent grants](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=528) (page 528).

* [Map persistent grants to access token attribute contract](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=549) (page 549).

## Steps

1. In the PingFederate administrative console, go to **Applications > OAuth > Clients**, and click **Add Client**.

2. In the **Client ID** field, provide a client ID.

   The client ID is a unique identifier and cannot have the same ID as another OAuth client.

   |   |                                                |
   | - | ---------------------------------------------- |
   |   | You cannot change a client ID after it is set. |

3. In the **Name** field, enter a name for the client.

   The name value is a descriptive name displayed for end users that indicates the purpose of the client.

4. In the **Description** field, provide a description that gives additional detail on the use of the client.

5. Select a **Client Authentication** method:

   ### Choose from:

   * **None**

   * **Client TLS Certificate**

     1. In the **Issuer** list, select the certificate for a trusted issuer if the client should expect certificates from a specific issuer. If certificates from any issuer should be allowed, select **Trust Any**.

     2. In the **Subject DN** field, enter the subject DN for the certificate or extract it from a file by clicking **Choose File**, selecting an appropriate certificate, and then clicking **Extract**.

   * **Private Key JWT**

     1. Select the **Replay Prevention** checkbox if the client should require a unique JSON web token (JWT) for each request.

     2. From the **Signing Algorithm** list, select the specific algorithm for the incoming JWT, or to allow any supported signing algorithm to be used, select **Allow Any**.

   * **Client Secret**

     |   |                                                                                                                                                              |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     |   | If selected as the authentication method, you must provide a client secret. If you select another method for authentication, you don't need a client secret. |

     1. Select the **Change Secret** checkbox.

     2. In the **Client Secret** field, enter a client secret, or to have a random value provided, click **Generate** secret. Make a copy of this value because it won't be visible after the client is saved.

        ![Screen capture showing the different Client Authentication options. The options are None, Client Secret, Client TLS Certificate, and Private Key JWT. Each option has a radio button next to it. After the Client Authentication section is the Client Secret section. The field says, 'No Secret Defined', and to the right of the field is the Generate Secret button. After the field is the Change Secret checkbox.](_images/zlx1600203062226.png)

6. If the client requires all requests to be signed, select the **Require Signed Requests** checkbox.

7. If you selected **Require Signed Requests** checkbox, select the expected signing algorithm or select **Allow Any**.

8. If you selected **Private Key JWT** as the authentication method, or if you selected the **Require Signed Requests** checkbox, complete either the **JWKS URL** or **JWKS** fields:

   1. To use a JSON web key set (JWKS) URL, enter the URL of the JWKS.

   2. To provide the JWKS directly, copy and paste the contents of the JWKS in the **JWKS** field.

9. If the client will be configured to support the OAuth authorization code or implicit flows, in the **Redirection URI** section, enter at least one URI.

   The redirection URI values specify the valid redirection locations that an application might request post authorization. The redirection URI value must be a fully qualified URL. Wildcards can be used to allow redirection into any sub-path. Make redirection URIs as restrictive as possible.

   1. In the **Redirection URI** field, enter a value.

   2. Click **Add**.

   3. Repeat steps 9a and 9b for each valid redirection URI.

10. In the **Logo URL** field, enter a fully qualified URL.

    This is the URL for the logo image that displays on the **User Grant Authorization** and **Revocation** pages.

11. If the client will use the PingFederate authentication API for authentication and will require an experience that doesn't use HTTP redirections, select the **Allow Authentication API OAuth Initiation** checkbox.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | * The **Bypass Authorization Approval** checkbox is automatically selected and can't be changed because this flow doesn't support the user-facing grant consent page.

    * The **Restrict Common Scopes** checkbox is automatically selected and can't be changed because this flow doesn't support the user-facing grant consent page.

    * Any configured **Common Scopes** and the default openID scope is displayed and can be selected as valid scopes for the client. |

    ![Screen capture showing the Allow Authentication API OAuth Initiation, Bypass Authorization Approval, and Restrict Common Scopes options. Each option as a checkbox. All three checkboxes are selected. The Bypass and Restrict checkboxes are grayed out to show that they are selected by default and cannot be changed.](_images/ybr1600203703328.png)

12. If any exclusive scopes are defined and the client should be allowed to use them, select the **Exclusive Scopes** checkbox.

    Any defined exclusive scopes are displayed and can be selected as available to this client.

13. In the **Allowed Grant Types** list, select at least one option.

    ![Screen capture showing the options for Allowed Grant Types. Each option has a checkbox next to it. The options are Authorization Code, Implicit, Refresh Token, Client Credentials, Device Authorization Grant, CIBA, Token Exchange, Resource Owner Password Credentials, Assertion Grants, Access Token Validation (Client is a Resource Server).](_images/dpr1600203885485.png)

    Learn more about each grant type in [Grant types](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=76).

14. If the client should restrict the available response types requested by the application, select the **Restrict Response Types** checkbox.

    1. In the list of available response types, select at least one option.

       ![Screen capture the Restrict Response Types option with the checkbox for Restrict selected. After this checkbox is a list of options and checkboxes for response types to restrict. The options are code, code id\_token, code id\_token token, code token, id\_token, id\_token token, token.](_images/xtr1600204154232.png)

15. In the **Default Access Token Manager** list, select the default access token manager (ATM) for this client.

    The Default ATM can either be the default ATM configured in **Access Token Mappings** or a specific ATM.

16. **Optional:** For resource server clients that won't receive a specific request for an ATM, select the **Validate Against All Eligible Access Token Managers** checkbox to instruct PingFederate to validate access tokens against all available ATMs.

17. If the client should require PKCE, select the **Require Proof Key for Code Exchange (PKCE)** checkbox.

    |   |                                                                                                        |
    | - | ------------------------------------------------------------------------------------------------------ |
    |   | This checkbox isn't displayed unless **Authorization Code** is selected under **Allowed Grant Types**. |

18. Override the global setting for the **Persistent Grants Max Lifetime** set in **System > OAuth Settings > Authorization Server Settings**:

    ### Choose from:

    * To use the global setting (default), click **Use Global Setting**.

    * For grants that should not have an expiration, click **Grants Do Not Expire**.

    * To enter a custom duration for this client's grants, click the radio button below **Grants Do Not Expire**.

19. Override the global setting for the **Refresh Token Rolling Policy** set in **System > OAuth Settings > Authorization Server Settings**.

    The client can override the global setting.

    ### Choose from:

    * To use the global setting (default), click **Use Global Setting**.

    * To tell the client to never roll the refresh token, click **Don't Roll**.

    * To tell the client to roll the refresh token, click **Roll**.

20. Change the default option for the token signing algorithm by selecting a different value in the **ID Token Signing Algorithm**list.

21. If the content of the ID token should be encrypted, then in the **ID Token Key Management Encryption Algorithm** list, select the algorithm that will be used to encrypt the content encryption key.

22. (Optional) If an **ID Token Key Management Encryption Algorithm** is selected, then in the **ID Token Content Encryption Algorithm** list, select the value of the encryption algorithm used to encrypt the plaintext content of the ID token.

23. To have the client use a specific OIDC policy, in the **Policy** list, select a specific value.

    By default, the client uses the OIDC policy configured as default in **Applications > OAuth > OpenID Connect Policy Management**.

24. To enable pairwise pseudonymous identifiers for open banking support, select the **Use Pairwise Identifier** checkbox.

    * In the **Sector Identifier URI** field, enter a single HTTPS URI.

25. To send logout requests to an OIDC endpoint in PingAccess as part of the logout process, select the **PingAccess Logout Capable** checkbox.

    |   |                                                                                                                                                          |
    | - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | This checkbox only displays if the **Track User Sessions for Logout** option is selected in **System > OAuth Settings > Authorization Server Settings**. |

26. Enter a fully qualified URI in the **Logout URIs** field and click **Add** for each endpoint desired.

    |   |                                                                                                                                                                          |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | The **Logout URIs** field is displayed only if the **Track User Sessions for Logout** option is selected in **System > OAuth Settings > Authorization Server Settings**. |

    PingFederate sends logout requests to each relying party listed.

    ![Screen capture of the OpenID Connect section and the fields for ID Token Signing Algorithm, ID Token Key Management Encryption Algorithm, Policy, and Logout URIs. The ID Token Signing Algorithm field is set to Default. The ID Token Key Management Encryption Algorithm field is set to No Encryption. The Policy field is set to Default. After the Policy field are two checkboxes. One checkbox is for the Use Pairwise Identifier option. One checkbox is for the Logout Capable option. The Logout URIs field is blank. To the right of this field is an Add button.](_images/gdc1600204848615.png)

27. To allow the client to use the back-channel session revocation API, select the **Allow Access to Session Revocation API** checkbox.

28. To allow the client to use the session management API, select the **Allow Access to Session Management API** checkbox.

29. Override the global values set by clicking **Override** in **System > OAuth Settings > Authorization Server Settings**.

    |   |                                                                                                                                                 |
    | - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | The **Device Authorization Grant** settings section is only displayed If **Device Authorization Grant** is selected in **Allowed Grant Types**. |

    1. To allow the client to override the global value for the user authorization URL, in the **User Authorization URL** field, enter a fully qualified URL.

    2. To allow the client to override the global value for an activation code, in the **Pending Authorization Timeout (seconds)** field, specify a timeout value.

    3. To allow the client to override the global value for the device's polling interval to the PingFederate token endpoint, in the **Device Polling Interval (seconds)** field, enter an interval value.

    4. To allow the client to override the global setting for bypassing the confirmation of an activation code, select the Bypass **Activation Code Confirmation** checkbox.

       ![Screen capture of the Device Authorization Grant section. The section starts with radio buttons for the Use Global Settings and Override options. After the radio buttons are the User Authorization URL, Pending Authorization Time (seconds), and Device Polling Interval (seconds)fields. After the fields is the Bypass Activation Code Confirmation checkbox.](_images/smd1600205123422.png)

30. Configure the following CIBA settings:

    |   |                                                                                            |
    | - | ------------------------------------------------------------------------------------------ |
    |   | The **CIBA** section is displayed only if **CIBA** is selected in **Allowed Grant Types**. |

    1. In the **Token Delivery Method** field, specify token delivery method for the client:

       * If the client can check authorization results at the token endpoint, select **Poll**.

       * If the client expects a callback when authorization results are available, select **Ping**.

    2. If you selected **Ping**, in the **Notification Endpoint** field that displays, enter the client notification endpoint for PingFederate to provide call back messages for this client.

    3. If you selected **Poll**, to override the default polling interval, in the **Polling Interval** field, specify a value..

       The default polling interval for **Poll** clients is 3 seconds.

    4. To override the default CIBA request policy configured in **Applications > OAuth > CIBA > Request Policies**, in the **Policy** list, select a different request policy.

    5. To enable support for the user code in the client, select the **User Code Support** checkbox.

    6. To require CIBA signed requests, select the **Require CIBA Signed Requests**checkboxx.

    7. To select a specific algorithm, in the **CIBA Request Object Signing Algorithm** list, select a specific value.

       By default, the client supports any signing algorithm for the CIBA request object.

       ![Screen capture of the CIBA section and the corresponding fields. The section starts with Poll and Ping radio button options for Token Delivery Mode. After the radio buttons is the Polling Interval (seconds) field. Next is the Policy list with checkboxes below for User Code Support and Require CIBA Signed Requests. Finally is the CIBA Request Object Signing Algorithm list.](_images/lfl1600205386208.png)

31. To override the default processor policy configured in **Applications > Processor Policies**, in the **Processor Policy** list, select a specific process policy.

    If **Token Exchange**is selected in **Allowed Grant Types**, the **Token Exchange** section is displayed.

32. If any extended properties are defined in **System > Extended Properties**, click **Next** to continue to the **Extended Properties** options for the client.

33. Click **Save**.

---

---
title: Setting up and customizing sign-on windows in PingOne
description: Customize the sign-on window in PingOne to match your company's desired branding and themes.
component: solution-guides
page_id: solution-guides:customer_use_cases:htg_sign_on_window_setup_p1
canonical_url: https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_sign_on_window_setup_p1.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2025
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Setting up and customizing sign-on windows in PingOne

Customize the sign-on window in PingOne to match your company's desired branding and themes.

## Before you begin

Collect any logos, background images, and specific color Hex values to match your company branding.

## About this task

The **Branding & Themes** window provides the ability to customize logos, colors, and layout of all end user-facing pages.

![Screen capture illustrating the Branding & Themes window in the PingOne for Customers web console.](_images/dht1600281334986.png)

## Steps

1. In the PingOne admin console, go to **Settings > Customization**.

2. In the **Company Name** field, enter a company name.

3. Upload a desired image for your logo.

   If there is already a default logo, click **Remove Image** before uploading a new logo.

   1. In the **Default Logo** field, click the **Plus** ([icon: plus, set=fa]) icon to select an image file.

   2. Select the desired image and click **Open**.

      The max size is 2.0 MB. Your image file must be a JPEG, JPG, GIF, or PNG.

4. For additional customization, change the theme.

   1. In the **My Themes** section, click the **Plus** ([icon: plus, set=fa]) icon.

   2. Click to select the desired theme from the available options.

   3. Use the editor to further customize the appearance.

      |   |                                                     |
      | - | --------------------------------------------------- |
      |   | All customization changes will appear in real-time. |

5. To open the editor and customize the theme, click the desired theme.

   ### Choose from:

   * In the **Name** field, enter a new name.

   * From the **Preview** list, select a different preview display.

   * In the **Theme Colors** field, select a new color for the theme.

   * In the **Logo** field, remove or add a new image logo.

   * In the **Background Image** field, remove, update, or change the color of the background image.

   * In the **Footer** field, enter a footer.

     ![Screen capture illustrating the Customize window for PingOne themes editor.](_images/qdz1600282684026.png)

6. To toggle between the desktop and mobile view, click the **Desktop** ([icon: desktop, set=fa]) or **Mobile** ([icon: mobile, set=fa]) icon.

   ![Screen capture illustrating the Name field and Preview list with the Desktop and Mobile icons, surrounded by a rectangle outline for highlight purposes, between them for the Branding & Themes window in PingOne. The Desktop icon is selected.](_images/wbe1600202692135.png)

7. To confirm your changes, click **Save Changes**.

   |   |                                |
   | - | ------------------------------ |
   |   | Add multiple themes as needed. |

8. To activate a theme, click the **Star** ([icon: star, set=fa]) icon.

   ![Screen capture illustrating the active Focus theme in PingOne's branding and themes with the active Star icon highlighted.](_images/jwj1600202599505.png)

---

---
title: Setting up password recovery in PingOne
description: Learn how to set up password recovery for an application using PingOne.
component: solution-guides
page_id: solution-guides:customer_use_cases:htg_password_recovery_setup_p1
canonical_url: https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_password_recovery_setup_p1.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
  choose-from: Choose from:
---

# Setting up password recovery in PingOne

Learn how to set up password recovery for an application using PingOne.

## About this task

Set up account recovery by modifying an application's **Single\_Factor** policy in the PingOne administrative console or Unified Product Administrator.

## Steps

1. Sign on to PingOne and go to **Experiences > Authentication Policies**.

   ![Screen capture of the PingOne navigation menu. The menu has Experiences selected with sub-menu options for Authentication Policies, Auth Method Policies, Password Policies, and Risk Policies. The Authentication Policies option is selected.](_images/eic1627403251642.png)

   ### Result:

   The **Policies** page lists your default **Single\_Factor** and **Multi\_Factor** policies.

   ![Screen capture of the Policies page with a list of all existing policies in your PingOne configuration.](_images/lta1626204946617.jpg)

2. To modify the **Single\_Factor** policy, click the **Expand** icon and then click the **Pencil** ([icon: pencil, set=fa]) icon.

   ![Screen capture of the expanded Single\_Factor authentication policy with a summary of its login, recovery and registration, required when, and presented identity providers configuration details.](_images/jmo1626205305899.jpg)

3. In the **Recovery & Registration** section, select the **Enable account recovery** checkbox. Click **Save**.

   ![Screen capture of the edit page for the Single\_Factor policy. There are modifiable configurations for Login, Recovery & Registration, Requested When, and Presented Identity Providers. The Recovery & Registration section has checkboxes for Enable account recovery and Enable registration. The Enable account recovery checkbox is selected.](_images/xaq1626205429170.jpg)

4. To view the connection policies of an application, go to **Connections > Applications**.

   ![Screen capture of the PingOne navigation menu. The menu has Connections icon selected with sub-menu options for Application, External IDPs, PingFederate, and Provisioning. The Applications option is selected.](_images/zrw1627404943029.jpg)

   ### Result:

   The **Applications** page lists all of your existing applications.

5. Locate the application that contains the connection policy you want to modify, and click the **Expand** icon.

6. To modify the application's policies, click the **Policies** tab and then click the **Pencil** ([icon: pencil, set=fa]) icon.

   ![Screen capture of a expanded application. There are tabs for Profile, Configuration, Access, Policies, Attribute Mappings, and Roles. The Policies tab is selected.](_images/akb1626205809699.jpg)

7. To add the **Single\_Factor** policy to **Applied Policies**, choose one of the following ways:

   ### Choose from:

   * Drag the **Single\_Factor** policy from **All Policies** to **Applied Policies**.

   * Click the **[icon: plus, set=fa]**icon in the **Single\_Factor** policy.

     ![Screen capture of the Policies tab with existing policies for All Policies and Applied Policies. The All Policies section has Multi\_Factor and Single\_Factor listed.](_images/xbb1626209941584.jpg)

8. Click **Save**.

   ![Screen capture of a dragged Single\_Factor policy from the All Policies section to the Applied Policies section. The Single\_Factor policy is highlighted waiting for the changes to be saved. There are buttons for Save and Discard Changes.](_images/zir1626209614329.jpg)

---

---
title: Setting up password reset in PingOne
description: Learn how to customize the user's sign-on experience by enabling self-service management, such as change password and password reset, in the PingFederate administrative console when using the company's HTML Form sign-on page.
component: solution-guides
page_id: solution-guides:customer_use_cases:htg_password_reset_setup_p1
canonical_url: https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_password_reset_setup_p1.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2025
page_aliases: ["customer_use_cases:htg_password_reset_p1_pf_ldaps.adoc", "customer_use_cases:htg_password_reset_p1_pf_html_form.adoc", "customer_use_cases:htg_password_reset_p1_methods.adoc"]
section_ids:
  components: Components
  overview-of-changing-and-resetting-passwords: Overview of changing and resetting passwords
  before-you-begin: Before you begin
  set-up-ldaps-datastore-connection-pf: Setting up an LDAPS datastore connection in PingFederate
  about-this-task: About this task
  steps: Steps
  configuring-an-html-form-adapter-instance-for-password-reset: Configuring an HTML Form Adapter instance for password reset
  before-you-begin-2: Before you begin
  about-this-task-2: About this task
  steps-2: Steps
  choose-from: Choose from:
  result: Result
  resetting-a-password-using-various-methods: Resetting a password using various methods
---

# Setting up password reset in PingOne

Learn how to customize the user's sign-on experience by enabling self-service management, such as change password and password reset, in the PingFederate administrative console when using the company's HTML Form sign-on page.

## Components

* PingOne

* PingFederate 10.1

## Overview of changing and resetting passwords

The change password capability is helpful when a user knows their password and wants to change it. The password reset capability is helpful when a user forgets their password and wants to use another factor, such as PingDirectory, to authenticate and change their password. This guide covers how to successfully configure password reset and enable change password in the HTML Form Adapter and password credential validator (PCV) framework in PingFederate. PingFederate provides the following password reset methods for self-service password reset:

* Email one-time link

* Email one-time passcode

* Text message

* PingID

Each method requires additional configuration.

|   |                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Self-service password reset using the authentication policy method in PingFederate isn't covered in this topic. Learn more about the authentication policy method and configuration steps in [Configuring self-service account recovery](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#pingfed=643) (page 643) in the PingFederate Server documentation. |

## Before you begin

1. Create an LDAP datastore source connection in PingFederate using LDAPS.

2. Create a service provider (SP) connection in PingFederate.

3. Add PingFederate as an identity provider (IdP) to PingOne and configure PingID.

4. Create an HTML Form Adapter and PingID IdP adapter in PingFederate.

5. Create a PCV in PingFederate.

## Setting up an LDAPS datastore connection in PingFederate

### About this task

The self-service password reset capability relies on the LDAP connection to your directory server and the Username PCV to query the required attributes for the chosen reset method.

PingFederate supports the following datastores:

* PingDirectory

* Microsoft Active Directory

* Oracle Unified Directory

* Oracle Directory Server out-of-the-box

|   |                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This task covers specific configuration settings for this use case. Learn more in [Configuring an LDAP Connection](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=871) (page 871). |

### Steps

1. Go to **System > Data & Credential Stores > Data Stores**, and click **Add New Data Store**.

2. On the **Data Store Type** tab, in the **Data Store Name** field, enter a name for the datastore.

3. In the **Type** list, select **Directory (LDAP)**. Click **Next**.

   |   |                                                                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For an Active Directory (AD) datastore, you must issue a certificate from your internal certificate authority (CA) and import it. Follow these substeps to complete the process: |

   1. For an AD datastore, go to **Security > Trusted CAs**, and click **Import**.

   2. On the **Import Certificate** tab, click **Choose File** and upload the relevant file. Click **Next.**

   3. On the **Summary** tab, click **Save**.

4. Go to the **LDAP Configuration** tab:

   1. Select the **Use LDAPS** checkbox.

      |   |                                                                                                                                                                                                                                    |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | PingFederate assumes port 389 when the **Use LDAPS** checkbox is cleared and assumes port 636 when this checkbox is selected. If you are using the default port of 636, you don't have to specify it in the **Hostname(s)** field. |

      ![Screen capture of the Data Store window and on the LDAP Configuration tab. There are configuration settings for Data Store Name which as AD entered, Hostname(s) which has EC2AMAZ-IV4ESP3.pingdemo.org entered, a Use LDAPS checkbox which is selected to enable, a Use DNS SRV Record checkbox to enable, Load Type which has Active Directory set, a Bind Anonymously checkbox to enable, User DN which has ADAdmin entered, Password which has a protected entry, and a Mask Values in Log checkbox to enable.](_images/fjk1605555084221.jpg)

   2. Enter the user attributes in the **User DN** and **Password** fields.

      |   |                                                                                                                                                                                                                                                                                                                                                                                 |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | * If the **Password Reset Type** is **PingID** , the user attribute that passes to PingID/> during password reset must be the attribute that is associated with the PingID/> account in PingOne.

      * For an AD datastore, the default user attribute is `sAMAccountName`. This does not have to be the attribute you enter into the username field on the account recovery page. |

   3. Enter the attributes you want to use to query in the **Search Filter** field.

      The **Search Filter** field, commonly used for Office 365 connections, allows you to enter `sAMAccountName` or `userPrincipleName`.

      For example, `(|(sAMAccountName=${username})(userPrincipalName=${username}))`.

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | If the **Password Reset Type** is **PingID**, use a search filter that searches with multiple attributes. You can enter either attribute into the fields, and it passes the username attribute you set in your PCV.To view or modify this user attribute:1) Go to **System > Data & Credential Store > Password Credential Validators >** **Password Credential Validators**, and select the relevant PCV instance.

      2) On the **Instance Configuration** tab, edit the **PingID Username Attribute** field.This is the attribute used for a PingID password reset type. |

      ![Screen capture the LDAP configuration tab settings. There are settings for Search Filter which has (\\|(sAMAccountName=${username})(userPrincipalName=${username})) entered, Scope of Search which has two options of One Level and Subtree and Subtree is clicked, a Case-Sensitive Matching checkbox which is selected, Display Name Attribute which has displayName entered, Mail Attribute which has mail entered, SMS Attribute, PingID Username Attribute which has userPrincipalName entered, Mail Search Filter which has mail=$(mail) entered, and Username Attribute which has sAMAccountName entered.](_images/qud1605562002361.jpg)

5. Click **Next**.

6. Configure the remaining LDAP settings as needed.

   Learn more about the settings in [Configuring an LDAP connection](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=871) (page 871) and [Setting advanced LDAP options](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=874) (page 874).

7. On the **Summary** tab, click **Save**.

## Configuring an HTML Form Adapter instance for password reset

### Before you begin

Make sure you have configured an LDAP datastore connection in PingFederate to connect to your application to enable self-service password reset.

This task covers specific configuration steps. You can find comprehensive instructions in [Setting up an LDAP connection in PingFederate](#set-up-ldaps-datastore-connection-pf).

### About this task

An HTML Form Adapter instance is used to validate a user authentication session with a PCV and an LDAP datastore connection. This authentication mechanism allows you to customize a user's sign-on experience, such as:

* Enabling self-service password reset

* Account unlock

* Notifying users with password expiration information

* Localizable template files

To create or modify an HTML Form Adapter instance with a password credential validator (PCV) and an LDAP datastore connection for self-service password management:

### Steps

1. Go to **Identity Provider > IdP Adapters** and choose an HTML Form Adapter:

   #### Choose from:

   * In the **Instance Name** list, reuse an existing HTML Form Adapter.

   * Click **Create New Instance** to create one.

2. Go to the **IdP Adapter** tab:

   1. Click **Add New Row to 'Credential Validators'** and add the PCV that's linked to your LDAP connection. Click **Update**.

   2. Select the **Allow Password Changes** checkbox.

      |   |                                                                                                                                                  |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | You must select the **Allow Password Changes** checkbox to enable password reset. If you don't enable this setting, your changes can't be saved. |

   3. **Optional:** To send the user an email when their password is changed, select the **Change Password Email Notification** checkbox.

   4. **Optional:** To alert the user with an approaching password expiry message at sign on, select the **Show Password Expiring Warning** checkbox.

   5. In the **Password Reset Type** row, click the password reset method that you want to use.

      ![Screen capture of the IdP Adapter tab configuration. There are checkboxes for the Change Password Email Notification and Show Password Expiring Warning settings. Only the Show Password Expiring Warning checkbox is selected. In the Password Reset Type section, the user has the following method options to select for self-service password reset type: Authentication Policy, Email One-Time Link, Email One-Time Password, PingID, Text Message, or None as radio buttons. The PingID reset type is clicked.](_images/cuj1605217589715.jpg)

   6. To allow a user with a locked account to unlock the account using the password reset function, select the **Account Unlock** checkbox.

3. To edit the templates for the HTML pages for password reset:

   1. Click **Show Advanced Fields**.

   2. Edit the relevant template fields as needed with the appropriate HTML template.

      |   |                                                                                                       |
      | - | ----------------------------------------------------------------------------------------------------- |
      |   | If you modify and rename a template, make sure to update the template name of that specific template. |

      ![Screen capture of the IdP Adapter tab configuration. There are settings for the HTML templates that support the password reset function. The user can edit the Password Reset Username Template, Password Reset Code Template, Password Reset Template, Password Reset Error Template, Password Reset Success Template, and Account Unlock Template. The fields have the following entries: Password Reset Username Template has forgot-password.html entered, Password Reset Code Template has forgot-password-resume.html entered, Password Reset Template has forgot-password-change.html, Password Reset Error Template has forgot-password-error.html, Password Reset Success Template has forgot-password-success.html, and Account Unlock Template has account-unlock.html entered.](_images/buh1605218856943.jpg)

4. For the **PingID** password reset type, in the **PingID Properties** field, import your PingID properties file from PingOne.

   This is the same file you used to setup your PingID adapter in PingFederate.

5. Configure the remaining settings as needed. Click **Next**.

   You can find more information about the settings in [Configuring an HTML Form Adapter instance](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=288) (page 288) and [HTML Form Adapter advanced fields](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=298) (page 298).

6. On the **Summary** tab, click **Save**.

### Result

You have successfully created an instance of the HTML Form Adapter with the self-service password reset capability. When a user signs on through this adapter instance, the sign-on page displays the **Change Password?** and **Trouble Signing On?** options.

## Resetting a password using various methods

You can use several methods to configure password reset. Click the following tabs to see instructions for each method.

---

---
title: Setting up PingDataSync between Active Directory and PingOne
description: Learn how to configure PingDataSync for Microsoft Active Directory (AD) to PingOne in a Windows environment.
component: solution-guides
page_id: solution-guides:customer_use_cases:htg_pds_setup_between_ad_and_p1
canonical_url: https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_pds_setup_between_ad_and_p1.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 25, 2025
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Setting up PingDataSync between Active Directory and PingOne

Learn how to configure PingDataSync for Microsoft Active Directory (AD) to PingOne in a Windows environment.

## Before you begin

**Components**

* PingOne

* PingDataSync

You must:

* [Install PingDataSync](https://docs.pingidentity.com/pingdirectory/latest/installing_the_pingdirectory_suite_of_products/pd_sync_installing_pds.html).

* Have the hostname for the AD instance.

* Have the port for the AD instance.

  With AD, this is 389 or 636. If you're not planning to work with passwords, you should keep everything on 389. Steps for working with SSL over port 636 are not a part of this guide.

* Have the AD Admin ID (For example, cn=administrator, cn=users, dc=mydomain, dc=com).

* Have your PingOne Environment ID, Client ID, and Client Secret from your designated PingOne Worker App.

  |   |                                                                                                                                                                                                                                                                                                          |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Use the Client ID and Client Secret from the PingOne Worker App that will manage the operation. Learn more about creating and maintaining Worker Apps in [Adding an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html) in the PingOne documentation. |

## About this task

Setting this configuration primarily uses the `dsconfig.bat` tool.

|   |                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Although the steps for this configuration are shown in a Windows environment, you can configure this in Linux or Docker with the correct networking configuration in place. |

This task uses the following naming conventions:

* PingDataSync Server references: "server" + Application.

  For example, `serverAD` or `` serverP1` ``.

* PingDataSync objects: object name + source + "to" + destination.

  For example, `mapADtoP1`, `pipeADtoP1`.

## Steps

1. To create an external server in PingDataSync, open a terminal window and run the following command.

   |   |                                                                                        |
   | - | -------------------------------------------------------------------------------------- |
   |   | Make sure to replace the bracketed fields with the values for the administrative user. |

   ```shell
   C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
   create-external-server ^
   --server-name serverAD ^
   --type active-directory ^
   --set server-host-name:<hostname or IP>  ^
   --set server-port:389 ^
   --set bind-dn:<your bind DN> ^
   --set password:<password> ^
   --set connection-security:none ^
   --set key-manager-provider:null ^
   --trustAll ^
   --no-prompt
   ```

   This step defines the connection from PingDataSync to the AD server.

   |   |                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `--trustAll` and `--no-prompt` parameters bypass any potential certificate issues and suppress prompts or inputs from executing `dsconfig`. |

2. To create the sync source, specify the starting point for the synchronization process with the following command.

   ```shell
   C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
   create-sync-source ^
   --source-name sourceAD ^
   --type active-directory ^
   --set base-dn:<your base DN> ^
   --set server:serverAD ^
   --trustAll ^
   --no-prompt
   ```

3. To create the sync destination, run the following command.

   ```shell
   C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
   create-sync-destination ^
   --destination-name destinationP1 ^
   --type ping-one-customer ^
   --set api-url:https://api.pingone.com/v1 ^
   --set auth-url:https://auth.pingone.com/<your environment ID>/as/token ^
   --set environment-id:<your environment ID> ^
   --set oauth-client-id:<your OAuth client ID> ^
   --set oauth-client-secret:<your client secret> ^
   --trustAll ^
   --no-prompt
   ```

   |   |                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Because you're using PingOne as a destination, you don't need to create an external server reference. Everything is done through the API. |

4. Create the attribute map:

   1. Create the map object with the following command.

      ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-attribute-map ^
      --map-name mapADtoP1 ^
      --trustAll ^
      --no-prompt
      ```

      There are three types of mappings that you can make after you define a map:

      * Direct

        All the contents from the source attribute are mapped to the destination attribute with no changes, for example,`mail` to `email`.

      * Constructed

        The value of the destination attribute is constructed by various means with the simplest use case being a user defined string, for example, `resourceType` to `"user"`.

      * JSON Attribute mapping

        JSON mappings hold a JSON representation of a complex attribute. PingOne specifically uses JSON representation for concepts, such as addresses and name information. These attributes in PingOne are case-sensitive. For example, `Address.street` doesn't work, but `address.streetAddress` does.

        |   |                                                                                                             |
        | - | ----------------------------------------------------------------------------------------------------------- |
        |   | The following mappings are suggestions for what works. Your installations might require different mappings. |

   2. Create the direct attribute mappings.

      | Mapping                             | Command                                                                                                                                                                                                                  |
      | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      | `sAMAccountName` to `accountID`     | ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-attribute-mapping ^
      --map-name mapADtoP1 ^
      --mapping-name accountID ^
      --type direct ^
      --set from-attribute:samaccountname ^
      --trustAll ^
      --no-prompt
      ```     |
      | `mobile` to `mobilePhone`           | ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-attribute-mapping ^
      --map-name mapADtoP1 ^
      --mapping-name mobilePhone ^
      --type direct ^
      --set from-attribute:mobile ^
      --trustAll ^
      --no-prompt
      ```           |
      | `mail` to `email`                   | ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-attribute-mapping ^
      --map-name mapADtoP1 ^
      --mapping-name email ^
      --type direct ^
      --set from-attribute:mail ^
      --trustAll ^
      --no-prompt
      ```                   |
      | `telephoneNumber` to `primaryPhone` | ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-attribute-mapping ^
      --map-name mapADtoP1 ^
      --mapping-name primaryPhone ^
      --type direct ^
      --set from-attribute:telephoneNumber ^
      --trustAll ^
      --no-prompt
      ``` |
      | `title` to `title`                  | ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-attribute-mapping ^
      --map-name mapADtoP1 ^
      --mapping-name title ^
      --type direct ^
      --set from-attribute:title ^
      --trustAll ^
      --no-prompt
      ```                  |
      | `employeeNumber` to `externalID`    | ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-attribute-mapping ^
      --map-name mapADtoP1 ^
      --mapping-name externalID ^
      --type direct ^
      --set from-attribute:employeeNumber ^
      --trustAll ^
      --no-prompt
      ```    |
      | `sAMAccountName` to `username`      | ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-attribute-mapping ^
      --map-name mapADtoP1 ^
      --mapping-name username ^
      --type direct ^
      --set from-attribute:samaccountname ^
      --trustAll ^
      --no-prompt
      ```      |

   3. Create constructed attribute mappings.

      | Mapping        | Command                                                                                                                                                                                                                          |
      | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | `population`   | ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-attribute-mapping ^
      --map-name mapADtoP1 ^
      --mapping-name population ^
      --type constructed ^
      --set value-pattern:{{"P1People":"name"}} ^
      --trustAll ^
      --no-prompt
      ``` |
      | `resourceType` | ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-attribute-mapping ^
      --map-name mapADtoP1 ^
      --mapping-name resourceType ^
      --type constructed ^
      --set value-pattern:user ^
      --trustAll ^
      --no-prompt
      ```                |

   4. Create JSON attribute maps:

      * To create the `name` attribute, run the following command.

        ```shell
        C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
        create-attribute-mapping ^
        --map-namemapADtoP1 ^
        --mapping-name name ^
        --type json ^
        --trustAll ^
        --no-prompt
        ```

        |   |                                                                                                                               |
        | - | ----------------------------------------------------------------------------------------------------------------------------- |
        |   | The PingOne name attribute holds information about the identity's name — first name, last name, and formatted (display name). |

      * To create the `address` attribute, run the following command.

        ```shell
        C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
        create-attribute-mapping ^
        --map-name mapADtoP1 ^
        --mapping-name address ^
        --type json ^
        --trustAll ^
        --no-prompt
        ```

        |   |                                                                                                   |
        | - | ------------------------------------------------------------------------------------------------- |
        |   | The PingOne address attribute holds address information and maps to a number of different fields. |

   5. Create JSON attribute mappings.

      | Mapping                              | Command                                                                                                                                                                                                                                                      |
      | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      | `sn` to `name.family`                | ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-json-attribute-mapping-field ^
      --map-name mapADtoP1 ^
      --mapping-name name ^
      --field-name family ^
      --set json-type:string ^
      --set from-attribute:sn ^
      --trustAll ^
      --no-prompt
      ```                |
      | `givenName` to `name.given`          | ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-json-attribute-mapping-field ^
      --map-name mapADtoP1 ^
      --mapping-name name ^
      --field-name given ^
      --set json-type:string ^
      --set from-attribute:givenName ^
      --trustAll ^
      --no-prompt
      ```          |
      | `cn` to `name.formatted`             | ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-json-attribute-mapping-field ^
      --map-name mapADtoP1 ^
      --mapping-name name ^
      --field-name formatted ^
      --set json-type:string ^
      --set from-attribute:cn ^
      --trustAll ^
      --no-prompt
      ```             |
      | `l` to `address.locality`            | ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-json-attribute-mapping-field ^
      --map-name mapADtoP1 ^
      --mapping-name address ^
      --field-name locality ^
      --set json-type:string ^
      --set from-attribute:l ^
      --trustAll ^
      --no-prompt
      ```            |
      | `postalCode` to `address.postalCode` | ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-json-attribute-mapping-field ^
      --map-name mapADtoP1 ^
      --mapping-name address ^
      --field-name postalCode ^
      --set json-type:string ^
      --set from-attribute:postalCode ^
      --trustAll ^
      --no-prompt
      ``` |
      | `st` to `address.region`             | ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-json-attribute-mapping-field ^
      --map-name mapADtoP1 ^
      --mapping-name address ^
      --field-name region ^
      --set json-type:string ^
      --set from-attribute:st ^
      --trustAll ^
      --no-prompt
      ```             |
      | `street` to `address.streetAddress`  | ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-json-attribute-mapping-field ^
      --map-name mapADtoP1 ^
      --mapping-name address ^
      --field-name streetAddress ^
      --set json-type:string ^
      --set from-attribute:street ^
      --trustAll ^
      --no-prompt
      ```  |
      | `c` to `address.countryCode`         | ```shell
      C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
      create-json-attribute-mapping-field ^
      --map-name mapADtoP1 ^
      --mapping-name address ^
      --field-name countryCode ^
      --set json-type:string ^
      --set from-attribute:c ^
      --trustAll ^
      --no-prompt
      ```         |

5. Create the sync pipe with the following command.

   ```shell
   C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
   create-sync-pipe ^
   --pipe-name pipeADtoP1 ^
   --set started:true ^
   --set sync-source:sourceAD ^
   --set sync-destination:destinationP1 ^
   --trustAll ^
   --no-prompt
   ```

   Creating the sync pipe provides the object that is directly used by PingDataSync and continues to bring the PingDataSync objects together.

6. Create the sync class with the following command.

   ```shell
   C:\<Ping>\<PingDataSync>\bat\dsconfig.bat ^
   create-sync-class ^
   --pipe-name pipeADtoP1 ^
   --class-name classADtoP1 ^
   --set attribute-map:mapADtoP1 ^
   --set "include-filter:(objectClass=user)" ^
   --set auto-mapped-source-attribute:-none- ^
   --set destination-correlation-attributes:username ^
   --set replace-all-attr-values:true ^
   --set creates-as-modifies:true ^
   --trustAll ^
   --no-prompt
   ```

   The sync class brings the remaining objects together and is directly linked to the sync pipe.

7. To test the PingDataSync connection between AD and PingOne, run the `resync -p pipeADtoP1` command.

   |   |                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------- |
   |   | If the sync encounters any errors, examine the `C:\<Ping>\<PingDataSync>\logs\tools\re-sync-failed-DNs.log` file. |

---

---
title: Setting up PingDataSync between PingDirectory and PingOne
description: Learn how to set up PingDataSync between PingDirectory and PingOne using installation commands for Linux.
component: solution-guides
page_id: solution-guides:customer_use_cases:htg_pds_setup_between_pd_and_p1
canonical_url: https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_pds_setup_between_pd_and_p1.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 25, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Setting up PingDataSync between PingDirectory and PingOne

Learn how to set up PingDataSync between PingDirectory and PingOne using installation commands for Linux.

## Before you begin

You must have:

* PingDataSync

* PingDirectory

* PingOne

You must:

* [Install PingDataSync](https://docs.pingidentity.com/pingdirectory/latest/installing_the_pingdirectory_suite_of_products/pd_sync_installing_pds.html).

* (Optional) Note the following values in a plain text file for easy copy and paste to the command line:

  * Implementation suffix

  * Host name for the PingDirectory instance

  * PingDirectory port

  * PingDirectory starting point

  * PingDirectory filter

  * PingDirectory Admin ID

  * PingDirectory Admin password

  * PingOne Population ID

  * PingOne Environment ID

  * WorkerApp Client ID

  * WorkerApp Client Secret

    |   |                                                                                                                                                                                                                                                                                                               |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Use the Client ID and Client Secret from the PingOne Worker App that will be managing the operation. Learn more about creating and maintaining Worker Apps in [Adding an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html) in the PingOne documentation. |

* (Optional) [Set up SSO access from the PingOne admin console](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_set_up_sso_pd.html).

  This allows administrative users to single sign-on (SSO) *(tooltip: \<div class="paragraph">
  \<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
  \</div>)* to the PingData admin console from PingOne.

## Steps

1. To create an external server, run the following command:

   ```
   /opt/<PingDataSync>/bin/dsconfig create-external-server --server-name serverPD_PDtest --type ping-identity-ds --set server-host-name:localhost --set server-port:11389 --set bind-dn:<your bind DN>  --set password:<your password>  --set connection-security:none --set key-manager-provider:null --trustAll --no-prompt
   ```

   |   |                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------ |
   |   | The `--type` parameter is different if you're using Active Directory or another Directory Server type. |

2. To create a sync source, run the following command:

   ```
   /opt/<PingDataSync>/bin/dsconfig create-sync-source --source-name sourcePD_PDtest --type ping-identity --set base-dn:ou=test,dc=p1,dc=lab --set server:serverPD_PDtest --trustAll --no-prompt
   ```

   |   |                                                                                        |
   | - | -------------------------------------------------------------------------------------- |
   |   | Make sure that your `base-dn` indicates where you want to start in the directory tree. |

3. To create a sync destination, run the following command:

   ```
   /opt/<PingDataSync>/bin/dsconfig create-sync-destination --destination-name destinationPD-P1_PDtest --trustAll --no-prompt --type ping-one-customer --set api-url:https://api.pingone.com/v1 --set auth-url:https://auth.pingone.com/<your PingOne environment ID>/as/token --set environment-id:<your PingOne environment ID>  --set oauth-client-id:<your worker app client ID>  --set oauth-client-secret:<your worker app client secret>  --set default-population-id:<your PingOne population ID>
   ```

   |   |                                                                                                |
   | - | ---------------------------------------------------------------------------------------------- |
   |   | Setting the population ID here avoids having to configure it in the attribute mapping section. |

4. To create an attribute map, run the following command:

   ```
   /opt/<PingDataSync>/bin/dsconfig create-attribute-map --map-name mapPDtoP1_PDtest --trustAll --no-prompt
   ```

   There are three types of mappings that you can make after you define a map:

   * Direct

     All the contents from the source attribute are mapped to the destination attribute with no changes, such as `mail` to `email`.

   * Constructed

     The value of the destination attribute is constructed by various means, with the simplest use case being a user defined string, such as `resourceType` to `"user"`.

   * JSON Attribute mapping

     JSON mappings hold a JSON representation of a complex attribute. PingOne specifically uses JSON representation for concepts, such as addresses and name information. These attributes in PingOne are case-sensitive. For example, `Address.street` doesn't work, but `address.streetAddress` does.

     |   |                                                                                                                     |
     | - | ------------------------------------------------------------------------------------------------------------------- |
     |   | The following mappings are suggestions for what works. Your installations will possibly require different mappings. |

     1. Create direct mappings.

        |   |                                              |
        | - | -------------------------------------------- |
        |   | This is easier to run as a `dsconfig` batch. |

        1. Create a `<PingDataSync>/directMapping.dsconfig` text file.

        2. Place the following commands into your `directMapping` file:

           ```
           dsconfig create-attribute-mapping --map-name mapPDtoP1_PDtest --mapping-name accountID --type direct --set from-attribute:uid --trustAll --no-prompt
           dsconfig create-attribute-mapping --map-name mapPDtoP1_PDtest --mapping-name mobilePhone --type direct --set from-attribute:mobile --trustAll --no-prompt
           dsconfig create-attribute-mapping --map-name mapPDtoP1_PDtest --mapping-name email --type direct --set from-attribute:mail --trustAll --no-prompt
           dsconfig create-attribute-mapping --map-name mapPDtoP1_PDtest --mapping-name primaryPhone --type direct --set from-attribute:telephoneNumber --trustAll --no-prompt
           dsconfig create-attribute-mapping --map-name mapPDtoP1_PDtest --mapping-name title --type direct --set from-attribute:title --trustAll --no-prompt
           dsconfig create-attribute-mapping --map-name mapPDtoP1_PDtest --mapping-name externalID --type direct --set from-attribute:employeeNumber --trustAll --no-prompt
           dsconfig create-attribute-mapping --map-name mapPDtoP1_PDtest --mapping-name username --type direct --set from-attribute:uid --trustAll --no-prompt
           ```

        3. Run the batch with the following command:

           ```
           /opt/<PingDataSync>/bin/dsconfig --trustAll --no-prompt --batch-file /opt/<Your directMapping file name>.dsconfig
           ```

     2. Create constructed attribute mappings with the following command:

        ```
        /opt/<PingDataSync>/bin/dsconfig create-attribute-mapping --map-name mapPDtoP1_PDtest --mapping-name resourceType --trustAll --no-prompt --type constructed --set value-pattern:user
        ```

     3. Create JSON attribute maps.

        |   |                                                                                                                                                                             |
        | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | This is easier to run as a `dsconfig` batch. The JSON maps are created as a subset of the attribute map that was just constructed and are populated in the following steps. |

        1. Create a `<PingDataSync>/jsonMap.dsconfig` text file.

        2. Place the following commands in your `jsonMap` file:

           ```
           dsconfig create-attribute-mapping --map-name mapPDtoP1_PDtest --mapping-name name --type json --trustAll --no-prompt
           dsconfig create-attribute-mapping --map-name mapPDtoP1_PDtest --mapping-name address --type json --trustAll --no-prompt
           ```

        3. Run the batch with the following command:

           ```
           /opt/<PingDataSync>/bin/dsconfig --trustAll --no-prompt --batch-file /opt/jsonMap.dsconfig
           ```

     4. Create JSON attribute mappings.

        |   |                                              |
        | - | -------------------------------------------- |
        |   | This is easier to run as a `dsconfig` batch. |

        1. Create a `<PingDataSync>/jsonMapping.dsconfig` text file.

        2. Place the following commands in your `jsonMapping` file:

           ```
           dsconfig create-json-attribute-mapping-field --map-name mapPDtoP1_PDtest --mapping-name name --field-name family --set json-type:string --set from-attribute:sn --trustAll --no-prompt
           dsconfig create-json-attribute-mapping-field --map-name mapPDtoP1_PDtest --mapping-name name --field-name given --set json-type:string --set from-attribute:givenName --trustAll --no-prompt
           dsconfig create-json-attribute-mapping-field --map-name mapPDtoP1_PDtest --mapping-name name --field-name formatted --set json-type:string --set from-attribute:cn --trustAll --no-prompt
           dsconfig create-json-attribute-mapping-field --map-name mapPDtoP1_PDtest --mapping-name address --field-name locality --set json-type:string --set from-attribute:l --trustAll --no-prompt
           dsconfig create-json-attribute-mapping-field --map-name mapPDtoP1_PDtest --mapping-name address --field-name postalCode --set json-type:string --set from-attribute:postalCode --trustAll --no-prompt
           dsconfig create-json-attribute-mapping-field --map-name mapPDtoP1_PDtest --mapping-name address --field-name region --set json-type:string --set from-attribute:st --trustAll --no-prompt
           dsconfig create-json-attribute-mapping-field --map-name mapPDtoP1_PDtest --mapping-name address --field-name streetAddress --set json-type:string --set from-attribute:street --trustAll --no-prompt
           ```

        3. Run the batch with the following command:

           ```
           /opt/<PingDataSync>/bin/dsconfig --trustAll --no-prompt --batch-file /opt/jsonMapping.dsconfig
           ```

5. To create a SyncPipe, run the following command:

   ```
   /opt/<PingDataSync>/bin/dsconfig create-sync-pipe --pipe-name  pipePDtoP1_PDtest --set started:true --set sync-source:sourcePD_PDtest --set sync-destination:destinationPD-P1_PDtest --trustAll --no-prompt
   ```

6. To create a sync class, run the following command:

   ```
   /opt/<PingDataSync>/bin/dsconfig  create-sync-class --pipe-name pipePDtoP1_PDtest --class-name classPDtoP1_PDtest --set attribute-map:mapPDtoP1_PDtest --set "include-filter:(objectClass=inetOrgPerson)" --set auto-mapped-source-attribute:-none- --set destination-correlation-attributes:username --set replace-all-attr-values:true --set creates-as-modifies:true --trustAll --no-prompt
   ```

7. Test the sync:

   1. Run the sync with the following command:

      ```
      /opt/<PingDataSync>/bin/resync -p pipePDtoP1_PDtest
      ```

   2. (Optional) If the sync results in any errors, examine the `/Ping/<PingDataSync>/logs/tools/re-sync-failed-DNs.log`.

   3. (Optional) If you receive an error that includes `Cannot connect because: The connection to server localhost:11389 was closed while waiting for a response to a bind request SimpleBindRequest(dn='cn=dmanager').`:

      1. In the PingDataSync admin console, go to **Configuration > External Servers > ServerPD\_PDtest**.

      2. Update your password.