---
title: About Healthcare flow pack
description: Learn about the purpose and configuration of the Healthcare flow pack.
component: pingone-solutions
page_id: pingone-solutions:healthcare:index
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/index.html
revdate: January 15, 2026
---

# About Healthcare flow pack

The Healthcare flow pack lets you provide end users (your patients) with a secure way to register an account and sign on, and provides customer service representatives with a way to manage user healthcare accounts, all using a simple getting started experience and pre-built PingOne DaVinci flows.

This flow pack enables robust threat detection against bots, disposable email, and Adversary-in-the-Middle (AITM) attacks. It also analyzes risk signals to detect high, medium, and low threats to reduce the risk of account takeovers.

The flow pack uses three main flows to handle separate portions of the process:

* **Healthcare - Registration with Threat Detection and ID Verification - Main Flow** lets users register an account, including performing a threat assessment and verifying the user's identity.

* **Healthcare - Progressive Verification during Authentication - Main Flow** lets users sign on.

* **Healthcare - CSR Help Desk - Main Flow** lets customer service representatives assist users with account management tasks such as enabling an account or resetting a password.

You can view additional information about the solution, including download links, in the Ping Identity Marketplace. Learn more at [Healthcare flow pack on the Marketplace](https://marketplace.pingone.com/item/healthcare-patient-experience-flow-pack).

Preparing the Healthcare flow pack solution involves configuration steps in PingOne and DaVinci:

* In PingOne, perform basic configuration to prepare the flows to be launched and enable features such as multi-factor authentication (MFA) and PingOne notifications.

* In DaVinci, configure variables and flow settings to customize the flow behavior for your environment and customers.

* Clone the flows for use in your production environment.

The Healthcare flow pack solution offers many of the available DaVinci capabilities. However, the solution limits the pre-built components to common use cases and selected best practices.

The solution includes a variety of authentication methods, such as email magic link, email and SMS OTP, FIDO2, voice, mobile applications, and Time-based One-Time Passwords (TOTPs).

|   |                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Healthcare flow pack solution offers pre-built flow templates and configurations. Review these components with your Ping Identity account representative to understand the limitations and risks associated with this solution. Your account representative can also help you customize the pre-built flow templates to satisfy any compliance or regulatory requirements that relate to your business. |

This solution uses PingOne and DaVinci. Learn more about managing users and other PingOne tasks in the [PingOne documentation](https://docs.pingidentity.com/pingone/p1_cloud__platform_main_landing_page.html). Learn more about customizing flows in the [DaVinci documentation](https://docs.pingidentity.com/davinci/davinci_landing_page.html).

---

---
title: Best Practices
description: Learn about how to effectively use the Healthcare flow pack.
component: pingone-solutions
page_id: pingone-solutions:healthcare:healthcare-best-practices
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/healthcare-best-practices.html
revdate: January 9, 2025
section_ids:
  select-an-appropriate-flow-timeout: Select an appropriate flow timeout
  clone-your-flows-before-using-or-customizing-them: Clone your flows before using or customizing them
  use-caution-when-customizing-flows: Use caution when customizing flows
---

# Best Practices

These guidelines help you make effective use of the Healthcare flow pack solution in your environment.

## Select an appropriate flow timeout

When you're configuring your DaVinci flows, you can set a timeout value for the flow as a whole. Because the user's account could be updated later by anyone with access to the device, a flow with a very long or indefinite timeout could be a security risk. Set a value that minimizes that risk.

## Clone your flows before using or customizing them

Flows with the original name can be updated by PingOne when we publish flow updates. These updates are not applied automatically, but they add a new latest version to each flow.

By cloning the flows before you apply any customization or use them with customers, you prevent any of your changes or customizations from being overwritten accidentally.

## Use caution when customizing flows

If you want to customize the flows in the Healthcare flow pack solution, do so carefully.

Clone the flows before making customizations so that:

* You can revert to the earlier versions if you encounter breaking changes.

* If you download an updated version of the solution, you don't overwrite your customizations.

Test your customizations in a test environment before importing them into your production environment. Because any additional nodes or flows you add are not part of the standard solution, you must test them to make sure that they're working as you intend.

---

---
title: Configuring flows in DaVinci
description: Learn about how to configure flows in DaVinci as part of the Healthcare flow pack.
component: pingone-solutions
page_id: pingone-solutions:healthcare:getting-started/healthcare-configuring-flows-in-davinci
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/getting-started/healthcare-configuring-flows-in-davinci.html
revdate: September 6, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
  result: Result:
  result-2: Result:
  choose-from-2: Choose from:
---

# Configuring flows in DaVinci

After you configure PingOne and test the solution using the wizard, perform additional configuration in PingOne DaVinci to enable all features and make the flows available to end users.

## Steps

1. Import the solution into your initial environment:

   1. In your production DaVinci environment, click **Flows**.

   2. Click **Add Flow > Import from JSON**.

   3. Select the JSON file containing the flows.

   4. Click **Import**.

2. Enter or verify the values for each company variable that's used in the Healthcare flow pack solution.

   These variables determine whether some processes and subflows are included or excluded.

   |   |                                                                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you plan to invoke the flow using the widget, you can pass in parameter values that override some of these variables. These parameters are described [later in this procedure](#parameters-anchor). |

   1. Click the **Variables** tab.

   2. Locate a variable and click the **Pencil** icon.

   3. In the **Value** field, verify that the value is correct or enter a new value for the variable.

   4. Click **Update**.

   5. Repeat steps b - d for each remaining variable.

      > **Collapse: Company variables**
      >
      > | Variable                       | Description                                                                                                                                                                                                                                                                                                                                                                            |
      > | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      > | `ciam_sessionLengthInMinute`   | The maximum allowed session length for a user in the flow\.The default value is 5 minutes.                                                                                                                                                                                                                                                                                             |
      > | `ciam_otpFallbackAllowed`      | A Boolean indicating whether a user can fall back to a one-time passcode (OTP) *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)* if a mobile push request times out.The default value is `true`. |
      > | `ciam_requireMFA`              | A Boolean that controls whether multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">&#xA;\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>&#xA;\</div>)* is required for all users.The default value is `true`.                                                  |
      > | `ciam_resendOtpLimit`          | The maximum number of times a user can resend an OTP.The default value is `5`.                                                                                                                                                                                                                                                                                                         |
      > | `ciam_magicLinkEnabled`        | A Boolean that controls whether magic links are enabled for your end users.The default value is `true`.                                                                                                                                                                                                                                                                                |
      > | `ciam_logoUrl`                 | The URL for the version of your company logo to display in flows.The default value is `https://assets.pingone.com/ux/ui-library/5.0.2/images/logo-pingidentity.png`.                                                                                                                                                                                                                   |
      > | `ciam_logoStyle`               | The CSS style to use for your company logo.The default value is `width: 65px; height:65px;`.                                                                                                                                                                                                                                                                                           |
      > | `ciam_companyName`             | The name of your company as it should be displayed in user-facing text.The default value is `Ping Identity`.                                                                                                                                                                                                                                                                           |
      > | `ciam_agreementEnabled`        | A Boolean that controls whether agreement is enabled in your environment.The default value is `true`.                                                                                                                                                                                                                                                                                  |
      > | `ciam_verificationLimit`       | The maximum number of times a user can attempt to verify their email address.The default value is `5`.                                                                                                                                                                                                                                                                                 |
      > | `ciam_protectAnalysisRequired` | A Boolean that controls whether PingOne Protect analysis is required.The default value is `true`.                                                                                                                                                                                                                                                                                      |
      > | `ciam_encodedCredentials`      | Your PingOne worker app encoded credentials.                                                                                                                                                                                                                                                                                                                                           |

3. Verify the configuration of the following connectors in your environment:

   | Connector             | Description                                                                                                                          | Connector documentation                                                                                     |
   | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
   | PingOne               | Enables DaVinci to view and update PingOne user information.                                                                         | [PingOne connector](https://docs.pingidentity.com/connectors/p1_connector.html)                             |
   | PingOne MFA           | Enables DaVinci to use the PingOne MFA service for MFA.                                                                              | [PingOne MFA connector](https://docs.pingidentity.com/connectors/p1_mfa_connector.html)                     |
   | PingOne Notifications | Enables DaVinci flows to send users general communications using SMS, email, and voice message with PingOne's notifications feature. | [PingOne Notifications connector](https://docs.pingidentity.com/connectors/p1_notifications_connector.html) |
   | PingOne Protect       | Enables DaVinci flows to perform a threat assessment of the current user through PingOne Protect.                                    | [PingOne Protect connector](https://docs.pingidentity.com/connectors/p1_protect_connector.html)             |
   | PingOne Authorize     | Enables DaVinci flows to use PingOne Authorize for policy-based authorization decisions.                                             | [PingOne Authorize connector](https://docs.pingidentity.com/connectors/p1az_connector.html)                 |
   | PingOne Verify        | Enables DaVinci flows to securely verify the user's identity.                                                                        | [PingOne Verify connector](https://docs.pingidentity.com/connectors/p1_verify_connector.html)               |
   | PingOne Credentials   | Enables DaVinci flows to issue and manage digital credentials for the user.                                                          | [PingOne Credentials connector](https://docs.pingidentity.com/connectors/p1_credentials_connector.html)     |

   1. On the **Connectors** tab, find the connector that you want to verify and go to **…​ > Edit**.

   2. Verify that the **Environment ID**, **Client ID**, and **Region** field values match your PingOne values.

   3. (Optional) Copy the **Client Secret** from your PingOne environment to the **Client Secret** field.

   4. For the PingOne Authorize connector, verify that the **Endpoint** matches the one found in PingOne in the **Authorization > Decision Endpoints** section.

   5. If you made changes to the values, click **Apply**.

   6. Repeat the previous steps for each remaining connector.

4. Configure the **Healthcare - Registration with Threat Detection and ID Verification - Main Flow**:

   1. Click **Flows**.

   2. Select the **Healthcare - Registration with Threat Detection and ID Verification - Main Flow** and go to **…​ > Edit**.

   3. Click the **Initialize Or Set Flow Variables** node and set values for the following variables:

      > **Collapse: Variables**
      >
      > | Variable                           | Description                                                                 |
      > | ---------------------------------- | --------------------------------------------------------------------------- |
      > | `p1AgreementId`                    | The ID of the agreement to use if your environment requires user agreement. |
      > | `p1MFAPolicyId`                    | The PingOne MFA policy to use.                                              |
      > | `p1RiskPolicyIdAuthZ`              | The PingOne risk policy to use for authorization.                           |
      > | `p1RiskPolicyIdReg`                | The PingOne risk policy to use for registration.                            |
      > | `p1RiskPolicyIdAuthn`              | The PingOne risk policy to use for authentication.                          |
      > | `p1RiskPolicyIdAR`                 | The PingOne risk policy to use for account recovery.                        |
      > | `flowCompanyLogo`                  | The company logo to use during the flow.                                    |
      > | `p1VerifyPolicyIdReg`              | The PingOne Verify Policy ID.                                               |
      > | `digitalWalletApplicationId`       | The application ID for the digital wallet solution.                         |
      > | `verifiedIdentityCredentialTypeId` | The ID for the verified identity credential solution.                       |

   4. In the **Sign Up Page & Call Account Registration Sub-Flow** section, select the **Send Account Created Email** node and verify that the **Notification Name** is set to **New Account Created**.

5. Configure the **Healthcare - Progressive Verification during Authentication - Main Flow**:

   1. Click **Flows**.

   2. Select the **Healthcare - Progressive Verification during Authentication - Main Flow** and go to **…​ > Edit**.

   3. Click the **Initialize Or Set Flow Variables** node and set values for the following variables:

      > **Collapse: Variables**
      >
      > | Variable              | Description                                                                 |
      > | --------------------- | --------------------------------------------------------------------------- |
      > | `p1AgreementId`       | The ID of the agreement to use if your environment requires user agreement. |
      > | `p1MFAPolicyId`       | The PingOne MFA policy to use.                                              |
      > | `p1RiskPolicyIdAuthZ` | The PingOne risk policy to use for authorization.                           |
      > | `p1RiskPolicyIdReg`   | The PingOne risk policy to use for registration.                            |
      > | `p1RiskPolicyIdAuthn` | The PingOne risk policy to use for authentication.                          |
      > | `p1RiskPolicyIdAR`    | The PingOne risk policy to use for account recovery.                        |
      > | `flowCompanyLogo`     | The company logo to use during the flow.                                    |

   4. In the **Threat Detection And Mitigation** section, select the **Notify User About High Risk Status** node and verify that the **Notification Name** is set to **Suspicious Activity**.

6. Configure the **Healthcare - Progressive Verification during Authentication - SignOn - Subflow**:

   1. Click **Flows**.

   2. Select the **Healthcare - Progressive Verification during Authentication - SignOn - Subflow** and go to **…​ > Edit**.

   3. Click the **Initialize Or Set Flow Variables** node and set values for the following variables:

      **Table 1. Variables**

      | Variable              | Description                                                                 |
      | --------------------- | --------------------------------------------------------------------------- |
      | `p1AgreementId`       | The ID of the agreement to use if your environment requires user agreement. |
      | `p1MFAPolicyId`       | The PingOne MFA policy to use.                                              |
      | `p1RiskPolicyIdAuthZ` | The PingOne risk policy to use for authorization.                           |
      | `p1RiskPolicyIdReg`   | The PingOne risk policy to use for registration.                            |
      | `p1RiskPolicyIdAuthn` | The PingOne risk policy to use for authentication.                          |
      | `p1RiskPolicyIdAR`    | The PingOne risk policy to use for account recovery.                        |
      | `flowCompanyLogo`     | The company logo to use during the flow.                                    |

   4. In the **Call Change Password Sub-Flow** section, select the **Send Password Has Been Reset Email** node and verify that the **Notification Name** is set to **Password Change**.

   5. In the **Threat Detection And Mitigation** section, select the **Notify User About High Risk Status** node and verify that the **Notification Name** is set to **Suspicious Activity**.

7. (Optional) If you plan to use a mobile application, configure the **Healthcare - Progressive Verification during Authentication - Device Registration - Subflow**:

   1. Click **Flows**.

   2. Select the **Healthcare - Progressive Verification during Authentication - Device Registration - Subflow** and go to **…​ > Edit**.

   3. In the **Mobile App Registration Flow** section, click the **Create Pairing Key** node.

   4. In the **Applications** field, enter one or more application IDs to specify which applications can be used with the pairing key. If you do not specify one or more application IDs, all applications can be used.

8. Verify that the PingOne flow setting is correct for your environment.

   ### Choose from:

   * If you want to launch the Healthcare flow pack solution using a redirect, the flow must be configured as a PingOne flow.

   * If you want to launch the Healthcare flow pack solution using the widget, the flow must not be configured as a PingOne flow.

     1. Click **Flows**.

     2. Click the **Healthcare - Registration with Threat Detection and ID Verification - Main Flow**.

     3. Go to **[icon: ellipsis-v, set=fa]> Flow Settings**.

     4. If you plan to launch the flow through a redirect, click the **PingOne Flow** toggle.

     5. If you made changes to the flow settings, click **Save**, close the flow settings pane, and click **Deploy**.

9. Configure DaVinci applications that invoke the main flows:

   * **Healthcare - Registration with Threat Detection and ID Verification - Main Flow**

   * **Healthcare - Progressive Verification during Authentication - Main Flow**

   * **Healthcare - CSR Help Desk - Main Flow**

   Learn more in [Creating an application](https://docs.pingidentity.com/davinci/applications/davinci_creating_an_application.html) and [Configuring a flow policy](https://docs.pingidentity.com/davinci/applications/davinci_configuring_a_flow_policy.html) in the DaVinci documentation.

   1. On the **Applications** tab, click **Add Application**.

   2. In the **Name** field, enter a name for the application.

   3. Click **Create**.

   4. On the **Applications** tab, find the application that you created and click **Edit**.

   5. On the **Flow Policy** tab, click **Add Flow Policy**.

   6. In the **Name** field, enter a name for the flow policy.

   7. Select **PingOne Flow Policy** if you plan to invoke the flow using a PingOne redirect.

   8. In the **Flows** section, select the **Healthcare - Registration with Threat Detection and ID Verification - Main Flow**.

   9. In the **Version** section, select one or more versions of the flow to use.

   10. Click **Create Flow Policy**.

   11. In the **Distribution** field, set the weight for the selected flow to `100`.

   12. Click **Save Flow Policy**.

   13. Click **Apply**.

   14. Repeat steps a - m for the **Healthcare - Progressive Verification during Authentication - Main Flow**.

   15. Repeat steps a - m for the **Healthcare - CSR Help Desk - Main Flow**.

10. If you're using a test environment, move the flows to your production environment:

    1. In your testing environment, click **Flows**.

    2. Click the **Healthcare - Registration with Threat Detection and ID Verification - Main Flow** flow.

    3. Go to **[icon: ellipsis-v, set=fa]> Download Flow JSON**.

       ### Result:

       The **Export Flow** panel opens.

    4. Click **Yes**.

       ### Result:

       The flow and its subflows are downloaded locally.

    5. Sign on to your production environment and click **Flows**.

    6. Click **Add Flow > Import from JSON**.

    7. Select the JSON file containing the flows.

    8. Click **Import**.

    9. Repeat the previous steps in your production environment.

11. Invoke the flow or flows using the widget or a redirect.

    ### Choose from:

    * If you want to launch the flow in a separate window using a PingOne redirect, use the procedure in [Launching a PingOne flow with a redirect](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launch_flow_redirect.html) in the DaVinci documentation. The Healthcare - Registration with Threat Detection and ID Verification - Main Flow flow can be launched with a redirect.

    * If you want to launch the flow in a widget within the user's current window, use the procedure in [Launching a flow with the widget](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launching_a_flow_with_the_widget.html) in the DaVinci documentation. The **Healthcare - Registration with Threat Detection and ID Verification - Main Flow** can be launched with the widget.

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | When you invoke the flow using the widget, you must include your company logo as a background image in the `dialog-content-header__logo` CSS class. For example:```
      .dialog-content-header__logo {
        background-image: url("./company-logo.svg");
      }
      ```You can include any of the following parameters. When present, the parameter value is used instead of the corresponding variable value.Use the following format to pass parameters to the flow:```
      flowParameters:{
           parameter1: "value",
           parameter2: "value"
      }
      ``` |

      > **Collapse: Parameters**
      >
      > | Parameter                 | Corresponding variable  | Description                                                              |
      > | ------------------------- | ----------------------- | ------------------------------------------------------------------------ |
      > | `isEmailMagicLinkEnabled` | `ciam_magicLinkEnabled` | A Boolean indicating whether magic links are enabled for your end users. |
      > | `isTermsOfServiceEnabled` | `ciam_agreementEnabled` | A Boolean indicating whether agreement is enabled in your environment.   |

---

---
title: Configuring PingOne for the Healthcare flow pack solution
description: Learn about how to configure PingOne as part of the Healthcare flow pack.
component: pingone-solutions
page_id: pingone-solutions:healthcare:getting-started/healthcare-configuring-p1
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/getting-started/healthcare-configuring-p1.html
revdate: September 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring PingOne for the Healthcare flow pack solution

Verify that your PingOne environment has the necessary configuration to run the Healthcare flow pack solution and enable all the features that you want to use.

## About this task

These steps ensure that the PingOne configuration is correct and enable features such as magic links, agreements, and social sign-on.

## Steps

1. Verify that you have an email server configured in PingOne.

   Learn more about email servers in [Configuring Trusted Email Addresses](https://docs.pingidentity.com/pingone/settings/p1_configure_trusted_email.html) in the PingOne documentation.

   1. Go to **Settings > Sender**.

   2. Click the **Pencil** icon.

   3. On the **Email** tab, in the **Email Sender** section, click **Ping Server**.

   4. In the **Domain** list, select your trusted email domain.

   5. Enter the sender details:

      **From Name**: Enter the name that appears as the sender's name in the email message.

      **From Address**: Select an email address in the list, or click **New** to open the **New Address** page and create a new address.

   6. Enter the reply-to details:

      **Reply-To Name**: Enter the name that appears as the reply-to name in the email message.

      **Reply-To Address**: Select an email address in the list, or click **New** to open the **New Address** page and create a new address.

   7. Click **Save**.

2. Create or verify the required pregenerated notification templates in your PingOne environment.

   Learn more about adding and customizing notification templates in [Adding a notification](https://docs.pingidentity.com/pingone/user_experience/p1_add_notification.html) and [Editing a notification](https://docs.pingidentity.com/pingone/user_experience/p1_edit_notification.html) in the PingOne documentation.

   1. Click one of the template links to view the corresponding template in the Ping Library:

      * [Account Disabled](https://library.pingidentity.com/page/ciam-plus-account-disabled-notification-template)

      * [Magic Link Authentication](https://library.pingidentity.com/page/ciam-plus-magic-link-authentication-notification-template)

      * [New Account Created](https://library.pingidentity.com/page/ciam-plus-new-account-created-notification-template)

      * [New Device Sign-in Activity](https://library.pingidentity.com/page/ciam-plus-new-device-signin-activity-notification-template)

      * [Password Changed](https://library.pingidentity.com/page/ciam-plus-password-changed-notification-template)

      * [Suspicious Activity](https://library.pingidentity.com/page/ciam-plus-suspicious-activity-notification-template)

   2. Click **Copy** to copy the template HTML.

   3. In PingOne, go to **User Experience > Notification Templates**.

   4. Click **[icon: plus, set=fa]**to create a new template.

   5. In the **Type** list, select **General**.

   6. In the **Name** field, enter the template's name as it is displayed on the Ping Library page.

   7. Click **Create**.

   8. In the **Email** section, in the **Subject** field, click the **Pencil** icon and enter a subject corresponding to the template:

      | Notification template       | Subject                                     |
      | --------------------------- | ------------------------------------------- |
      | Account Disabled            | Critical security alert                     |
      | Magic Link Authentication   | Magic link authentication                   |
      | New Account Created         | Welcome ${firstName} to \\{\\{Brand Name}}! |
      | New Device Sign-in Activity | Security alert                              |
      | Password Changed            | Password change                             |
      | Suspicious Activity         | Security alert                              |

   9. Click the **[icon: check, set=fa]**icon to save the subject changes.

   10. Click the **Edit** icon in the **New Email** field, then paste the template HTML you copied in step b.

   11. Click the **Save** icon to save the field changes.

   12. Click the **X** icon to close the template.

   13. Repeat steps a - l for each remaining template.

3. Create the **Change Password Magic Link** template:

   1. In PingOne, go to **User Experience > Notification Templates**.

   2. Click **[icon: plus, set=fa]**to create a new template.

   3. In the **Type** list, select **General**.

   4. In the **Name** field, enter `Change Password Magic Link`.

   5. Click **Create**.

   6. In the **Subject** field, configure a subject:

      1. Click the **Pencil** icon.

      2. Enter the subject `Password Change Request`.

      3. Click the **[icon: check, set=fa]**icon.

   7. In the **New Email** field, configure the message body:

      1. Click the **Pencil** icon.

      2. Enter a body for the new transaction message. For example:

         ```html
         <div
           style="display: block; text-align: center; font-family: sans-serif; border: 1px solid #c5c5c5; width: 400px; padding: 30px 20px;">
           <img src="https://assets.pingone.com/ux/ui-library/5.0.2/images/logo-pingidentity.png" alt="Company Logo" style="height: 65px; margin-bottom: 10px" />
           <h1>Password Change Request</h1>
           <div style="margin-top: 20px; margin-bottom:25px">
             <p>Please click the link below to change your password. </p>
             <a href="${magicLink}" style="font-size: 14pt">Change Password</a>
           </div>
         </div>
         ```

      3. Click the **[icon: check, set=fa]**icon.

   8. Click **X** to close the template.

4. Verify that you have a multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
   \<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
   \</div>)* policy configured in PingOne.

   Learn more in the PingOne [MFA policies](https://docs.pingidentity.com/pingone/authentication/p1_mfa_policies.html) documentation.

   1. In PingOne, go to **Authentication > MFA**.

   2. Click the MFA policy marked as the default.

   3. Verify that the **Method Selection** is set to **Prompt User to Select**.

   4. Verify that the policy's **Allowed Authentication Methods** include the authentication methods that you want to use from the following:

      * **Email**

      * **SMS**

      * **FIDO2**

      * **Voice**

      * **TOTP**

      * **Mobile**

5. Verify that the default population exists:

   1. Go to **Directory > Populations**.

   2. In the list of populations, verify that a population is marked as **Default**.

   3. If no existing population is marked as **Default**, select a population and go to **More options ( [icon: ellipsis-v, set=fa]) > Edit Population**.

   4. Click **Make Default Population**.

   5. Click **Switch**.

   6. Click **Save**.

6. Add the attributes required for the solution.

   1. Go to **Directory > User Attributes**.

   2. Click the [icon: plus, set=fa]icon.

   3. Click **Declared**.

   4. Click **Next**.

   5. Enter the information for one of the following attributes:

      | Name                      | Display name              | Description                                                                              |
      | ------------------------- | ------------------------- | ---------------------------------------------------------------------------------------- |
      | `emailVerifiedByP1Verify` | `emailVerifiedByP1Verify` | A string used to store the email verification status during PingOne Verify verification. |
      | `providerPhone`           | `providerPhone`           | The user's healthcare provider's phone number.                                           |
      | `providerName`            | `providerName`            | The user's healthcare provider's company name.                                           |
      | `providerAddress`         | `providerAddress`         | The user's healthcare provider's address.                                                |
      | `primaryPhone`            | `primaryPhone`            | The user's primary phone number.                                                         |
      | `policyNumber`            | `policyNumber`            | The user's policy ID number.                                                             |
      | `pharmacyPhone`           | `pharmacyPhone`           | The user's primary pharmacy's phone number.                                              |
      | `pharmacyName`            | `pharmacyName`            | The user's primary pharmacy's company name.                                              |
      | `medicalConditions`       | `medicalConditions`       | The user's medical conditions.                                                           |
      | `loginCount`              | `loginCount`              | The number of times the user has logged in.                                              |
      | `insuranceProvider`       | `insuranceProvider`       | The user's insurance provider company name.                                              |
      | `emergencyRelationship`   | `emergencyRelationship`   | The user's relationship with their emergency contact.                                    |
      | `emergencyPhone`          | `emergencyPhone`          | The user's emergency contact phone number.                                               |
      | `emergencyName`           | `emergencyName`           | The user's emergency contact name.                                                       |
      | `currentMedications`      | `currentMedications`      | The user's current medications.                                                          |

   6. Click **Save**.

   7. Repeat steps b - f for each remaining attribute.

   8. Populate these attributes with values for each user. Learn more in the [PingOne User Attribute documentation](https://docs.pingidentity.com/pingone/directory/p1_user_attributes.html).

7. Create a facial comparison policy in PingOne.

   1. Go to **Identity Verification > Verify Policies**.

   2. Click the [icon: plus, set=fa]icon.

   3. In the **Name** field, enter a name for the new policy.

   4. In the **Facial Comparison** section, select **Required**.

   5. For all other forms of identity verification, select **Disabled**.

   6. Click **Save**.

   7. Select the new policy and copy the **ID**.

8. (Optional) If you plan to use PingOne Protect and you don't want to use the default risk policy, create a new risk policy according to the [PingOne Protect documentation](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_adding_risk_policy.html).

9. (Optional) If you plan to use FIDO2, verify that the default **Passkeys** policy is selected.

   Learn more about FIDO policies in the [PingOne FIDO policies](https://docs.pingidentity.com/pingone/authentication/p1_fido_policies.html) documentation.

   1. Go to **Authentication > FIDO**.

   2. Verify that the **Passkeys** policy is set as the default.

   3. If the **Passkeys** policy is not the default, go to **⋮ > Make Default**, then click **Save**.

10. (Optional) If you plan to use an agreement, verify that you have an agreement configured in PingOne and copy the agreement ID.

    Learn more about configuring agreements in [Adding an agreement](https://docs.pingidentity.com/pingone/user_experience/p1_add_an_agreement.html) in the PingOne documentation.

    1. Go to **User Experience > Agreements**.

    2. Verify that the agreement exists and is enabled.

    3. Click the agreement to open the details panel.

    4. On the **API** tab, copy the **ID**.

    The agreement ID is used in a later procedure to configure the flows in DaVinci.

11. (Optional) Verify that you have an external identity provider (IdP) *(tooltip: \<div class="paragraph">
    \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
    \</div>)* configured in PingOne for each valid third party you want to use as a social sign-on option.

    Learn more about how IdPs are used in PingOne in [Identity Providers](https://docs.pingidentity.com/pingone/integrations/p1_external_idps.html) in the PingOne documentation.

    1. If you want to use Google as a social sign-on option, verify that Google is configured as an IdP according to the procedure in [Adding an identity provider - Google](https://docs.pingidentity.com/pingone/integrations/p1_addidentityprovidergoogle.html) in the PingOne documentation. During configuration, use the following property mappings:

       | Google property | PingOne property |
       | --------------- | ---------------- |
       | `email address` | `username`       |
       | `email address` | `email`          |
       | `family name`   | `family name`    |
       | `given name`    | `given name`     |

    2. If you want to use Facebook as a social sign-on option, verify that Facebook is configured as an IdP according to the procedure in [Adding an identity provider - Facebook](https://docs.pingidentity.com/pingone/integrations/p1_addidentityproviderfacebook.html) in the PingOne documentation. During configuration, use the following property mappings:

       | Facebook property | PingOne property |
       | ----------------- | ---------------- |
       | `email address`   | `username`       |
       | `email address`   | `email`          |
       | `family name`     | `family name`    |
       | `given name`      | `given name`     |

    3. If you want to use Apple as a social sign-on option, verify that Apple is configured as an IdP according to the procedure in [Adding an identity provider - Apple](https://docs.pingidentity.com/pingone/integrations/p1_add_idp_apple_prereqs.html) in the PingOne documentation. During configuration, use the following property mappings:

       | Apple property  | PingOne property |
       | --------------- | ---------------- |
       | `email address` | `username`       |
       | `email address` | `email`          |

---

---
title: Flow Reference
description: Learn about the flows included in the Healthcare flow pack and find links to reference documentation about them.
component: pingone-solutions
page_id: pingone-solutions:healthcare:flow-reference/healthcare-flow-reference
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/flow-reference/healthcare-flow-reference.html
revdate: January 29, 2025
page_aliases: ["flow-reference/index.adoc"]
---

# Flow Reference

The Healthcare flow pack solution uses three main flows and multiple subflows. This section explains what each flow does and how it works.

A DaVinci flow consists of nodes, each of which presents a page to the user, performs a backend action, or launches another flow. These nodes are connected by logical operators, allowing you to construct a user journey such as authenticating with a known device or making a transfer.

The flows included in the Healthcare flow pack solution are designed to work together to provide the solution. They require no configuration beyond that described in [Configuring flows in DaVinci](../getting-started/healthcare-configuring-flows-in-davinci.html). However, you can customize these flows to provide additional services to your end users. Learn more in [How To Manage Flows](https://docs.pingidentity.com/davinci/flows/davinci_how_to_manage_existing_flows.html) in the PingOne DaVinci documentation.

The main section of the Healthcare flow pack solution contains the following flows:

* [Healthcare - Registration with Threat Detection and ID Verification - Main Flow](healthcare-registration-with-threat-detection-and-id-verification-main-flow.html)

  This flow is the beginning of the process by which a user registers a new account. It's meant to be invoked directly.

  * [Healthcare - Account Registration - Subflow](healthcare-account-registration-subflow.html)

    This flow lets users register an account.

  * [Healthcare - Agreement (ToS) - Subflow](healthcare-agreement-tos-subflow.html)

    This flow lets users read and agree to any agreements required by the environment.

  * [Healthcare - Identity Verification and Managed Credential Issuance with Biometric Binding - Subflow](healthcare-identity-verification-and-managed-credential-issuance-with-biometric-binding-subflow.html)

    This flow uses PingOne Verify to verify the user and issue credentials.

  * [Healthcare - Pair A Digital Wallet - Subflow](healthcare-pair-a-digital-wallet.html)

    This flow lets users pair a new digital wallet.

  * [Healthcare - Registration with Threat Detection and ID Verification - Main Flow](healthcare-registration-with-threat-detection-and-id-verification-main-flow.html)

    This flow lets users register an account after performing threat detection and ID verification.

  * [Healthcare - Threat Detection - Subflow](healthcare-threat-detection-subflow.html)

    This flow uses PingOne Protect to perform a threat assessment of the user.

  * [Healthcare - Verify Email - Subflow](healthcare-verify-email-subflow.html)

    This flow lets users verify their email address using PingOne SSO.

* [Healthcare - Progressive Verification during Authentication - Main Flow](healthcare-authentication-with-username-and-password-main-flow.html)

  This flow is the beginning of the process by which a user signs on. It's meant to be invoked directly.

  * [Healthcare - Progressive Verification during Authentication - Agreement (ToS) - Subflow](healthcare-authentication-agreement-tos-subflow.html)

    This flow lets users read and agree to any agreements required by the environment.

  * [Healthcare - Progressive Verification during Authentication - Change Password - Subflow](healthcare-authentication-change-password-subflow.html)

    This flow lets users change their password.

  * [Healthcare - Progressive Verification during Authentication - Device Authentication - Subflow](healthcare-authentication-device-authentication-subflow.html)

    This flow lets users authenticate using a known device.

  * [Healthcare - Progressive Verification during Authentication - Device Registration - Subflow](healthcare-authentication-device-registration-subflow.html)

    This flow lets users register a new device.

  * [Healthcare - Progressive Verification during Authentication - Magic Link Authentication - Subflow](healthcare-authentication-magic-link-authentication-subflow.html)

    This flow lets users authenticate using a magic link.

  * [Healthcare - Progressive Verification during Authentication - SignOn - Subflow](healthcare-authentication-signon-subflow.html)

    This flow lets users sign on.

  * [Healthcare - Progressive Verification during Authentication - Threat Detection - Subflow](healthcare-authentication-threat-detection-subflow.html)

    This flow uses PingOne Protect to perform a threat assessment of the user.

  * [Healthcare - Progressive Verification during Authentication - Verify Email - Subflow](healthcare-authentication-verify-email-subflow.html)

    This flow lets users verify their email address using PingOne SSO.

* [Healthcare - CSR Help Desk - Main Flow](healthcare-csr-help-desk-main-flow.html)

  This flow is the beginning of the process by which customer service representatives assist users with account management. It's meant to be invoked directly by the CSR.

  * [Healthcare - CSR Help Desk - Verify User Magic Link Authentication - Subflow](healthcare-csr-help-desk-verify-user-magic-link.html)

    This flow verifies the user using a magic link.

  * [Healthcare - CSR Help Desk - Change Password - Subflow](healthcare-csr-change-password-subflow.html)

    This flow enables the CSR to have the user's password changed.

  * [Healthcare - CSR Help Desk - Active Directory - User Functions API - Subflow](healthcare-csr-active-directory-user-functions-api-subflow.html)

    This flow takes account management actions such as enabling or disabling the user account based on parameters passed by other flows.

  * [Healthcare - CSR Help Desk - Password reset Magic Link - Subflow](healthcare-csr-password-reset-magic-link-subflow.html)

    This flow enables the CSR to reset the user's password with a magic link.

  * [Healthcare - CSR Help Desk - Device Authentication - Subflow](healthcare-csr-device-authentication-subflow.html)

    This flow lets the CSR perform device authentication for the user.

---

---
title: Getting Started
description: Learn about how to configure PingOne and DaVinci for the Healthcare flow pack.
component: pingone-solutions
page_id: pingone-solutions:healthcare:getting-started/healthcare-getting-started
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/getting-started/healthcare-getting-started.html
revdate: May 29, 2024
page_aliases: ["getting-started/index.adoc"]
---

# Getting Started

There are two configuration stages for the Healthcare flow pack solution.

To get started with the solution:

1. [Configure the settings in PingOne](healthcare-configuring-p1.html).

2. [Perform additional configuration in PingOne DaVinci to begin using the solution](healthcare-configuring-flows-in-davinci.html).

---

---
title: Healthcare  - Progressive Verification during Authentication - Agreement (ToS) - Subflow
description: Learn about the Healthcare  - Progressive Verification during Authentication - Agreement (ToS) - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:healthcare:flow-reference/healthcare-authentication-agreement-tos-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/flow-reference/healthcare-authentication-agreement-tos-subflow.html
revdate: May 29, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Healthcare - Progressive Verification during Authentication - Agreement (ToS) - Subflow

The **Healthcare - Progressive Verification during Authentication - Agreement (ToS) - Subflow** lets users read and confirm any agreement required in your environment.

## Purpose

The **Healthcare - Progressive Verification during Authentication - Agreement (ToS) - Subflow** determines whether the user needs to consent to an agreement. If so, it displays the agreement for the user and stores the user's consent if they consent to the agreement.

## Structure

This flow is divided into sections using teleport nodes:

* **Check if agreement form needs to be displayed**

  Uses comparison nodes to check if agreement is enabled in the environment and if agreement is necessary for the current user. If so, a PingOne node checks the user's consent status.

  If consent isn't present, the flow progresses to the **Present & Accept Agreement** section.

  If consent is present, a function node checks if a success message should be displayed. The flow progresses to the **Present & Accept Agreement** section if a success message should be displayed and to the **Return Success** section if a success message should not be displayed.

* **Present & Accept Agreement**

  Uses a PingOne node to retrieve the required agreement, then presents the user with an HTML page. If the user has not yet agreed, this page lets them review and accept or decline the agreement. If the user has agreed, the form displays a success message, then the flow progresses to the **Return Success** section.

  If the user accepts the agreement, a PingOne node stores the user's agreement. The flow then returns to the beginning of the **Present & Accept Agreement** section if a success message should be displayed and to the **Return Success** section if a success message should not be displayed.

  If the user declines the agreement, an error message displays.

* **Return Success**

  Sends a success JSON response, indicating that the flow completed successfully.

* **Return Error**

  Uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input name           | Required | Description                                                                                   |
| -------------------- | -------- | --------------------------------------------------------------------------------------------- |
| `p1UserId`           | Yes      | The current user's PingOne user ID.                                                           |
| `agreementId`        | Yes      | The ID of the agreement to present to the user.                                               |
| `checkRequired`      | Yes      | Indicates whether the flow should check for existing consent before presenting the agreement. |
| `agreementEnabled`   | No       | Indicates whether the agreement is required.                                                  |
| `showSuccessMessage` | No       | Indicates whether a success message should be displayed after the user accepts the agreement. |
| `companyLogo`        | No       | The company logo.Used only when the main flow was launched using a redirect.                  |

## Output schema

This flow has the following outputs:

| Output name     | Description                                   |
| --------------- | --------------------------------------------- |
| `subflowResult` | The result status of the flow.                |
| `errorMessage`  | The error message to pass to the parent flow. |
| `errorDetails`  | The details of the error that occurred.       |

## Variables and parameters

This flow uses the following variable or parameter values:

| Parameter name       | Description                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------- |
| `p1UserId`           | The current user's PingOne user ID.                                                           |
| `agreementId`        | The ID of the agreement to present to the user.                                               |
| `checkRequired`      | Indicates whether the flow should check for existing consent before presenting the agreement. |
| `agreementEnabled`   | Indicates whether the agreement is required.                                                  |
| `showSuccessMessage` | Indicates whether a success message should be displayed after the user accepts the agreement. |

---

---
title: Healthcare - Account Registration - Subflow
description: Learn about the Healthcare - Account Registration - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:healthcare:flow-reference/healthcare-account-registration-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/flow-reference/healthcare-account-registration-subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Healthcare - Account Registration - Subflow

The **Healthcare - Account Registration - Subflow** lets users register a new account.

## Purpose

The **Healthcare - Account Registration - Subflow** presents users with the ability to create a new account. Depending on your environment's properties, the flow can let a user create a password, add email as a multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* device, and view and consent to an agreement.

## Structure

This flow is divided into sections using teleport nodes:

* **Fetch User Details for Registration**

  Uses function nodes to set flow instance variables and check whether agreement is enabled. If agreement is enabled, a PingOne node reads the agreement content. The flow then presents users with an HTML form on which to enter their email address.

  If the user clicks **Register**, the flow progresses to the **PingOne Protect Threat Detection And Mitigation**. When this section completes, the flow progresses to the **Validate Govt ID & Create account** section.

  If an option other than **Register** is selected, the flow progresses to the **Return Success** section.

* **PingOne Protect Threat Detection And Mitigation**

  If PingOne Protect analysis is required, uses a PingOne node to look up the user, then invokes the **Healthcare - Threat Detection - Subflow** subflow.

  If the **Healthcare - Threat Detection - Subflow** subflow completes successfully, the PingOne Protect values are saved as variables.

  A function node then examines the risk score:

  * If the risk score is low, medium, or high, the flow returns to the **Fetch User Details for Registration** section.

  * If the risk score cannot be found, the flow progresses to the **Return error** section.

  If the **Healthcare - Threat Detection - Subflow** subflow does not complete successfully, an error message is displayed.

* **Validate Govt ID & Create account**

  Uses a PingOne node to look up the user, then uses a function node to verify that the user has accepted the agreement. The flow then progresses to the **PingOne Neo: Govt Id Verification Using P1 Verify, Credentials Issuance To Wallet Using P1 Credentials & Creation of Account** section. When this section completes, a function node verifies that the user's government ID has been verified, then a PingOne node enables the user. The flow then progresses to the **Accept Agreement and Verify Email** section.

* **Accept Agreement and Verify Email**

  Uses a function node to check whether an agreement is enabled. If an agreement is enabled, a PingOne node updates the user's information to include their consent to the agreement. A function node then checks if email verification is required, and if it is required, the flow then invokes the **Healthcare - Verify Email - Subflow** flow. The flow then progresses to the **Auto enroll email as a MFA device** section.

* **Auto enroll email as a MFA device**

  Uses a PingOne node to read the available devices. A function node checks if email is already an MFA device, and if it is not, a PingOne node enrolls email as a device. A PingOne node then enables MFA for the user, and the flow progresses to the **Return Success** section.

* **PingOne Neo: Govt Id Verification Using P1 Verify, Credentials Issuance To Wallet Using P1 Credentials & Creation of Account**

  Invokes the **Healthcare - Identity Verification and Managed Credential Issuance with Biometric Binding - Subflow** subflow. A function node then examines the subflow status:

  * If the subflow completed successfully, a function node saves the variables from the subflow, then the flow returns to the **Validate Govt ID & Create account** section.

  * If the user canceled the subflow, the flow returns to the **Fetch user details for registration** section.

* **Return Success**

  Uses a PingOne node to update the risk evaluation if the risk evaluation ID is available and sends a success JSON response indicating that the flow completed successfully.

* **Return Error**

  Uses a PingOne node to update the risk evaluation if the risk evaluation ID is available and sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs.

| Input name                         | Required | Description                                                                                                                                                                                                                                                                                              |
| ---------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `email`                            | No       | The user's email address.                                                                                                                                                                                                                                                                                |
| `agreementEnabled`                 | No       | Indicates whether agreement is enabled for user registration.                                                                                                                                                                                                                                            |
| `agreementId`                      | No       | The ID of the agreement to present to users.                                                                                                                                                                                                                                                             |
| `socialRegistrationEnabled`        | No       | A Boolean indicating whether registration through third-party authentication is enabled.                                                                                                                                                                                                                 |
| `googleEnabled`                    | No       | A Boolean indicating whether authentication through Google is enabled in your environment.                                                                                                                                                                                                               |
| `facebookEnabled`                  | No       | A Boolean indicating whether authentication through Facebook is enabled in your environment.                                                                                                                                                                                                             |
| `appleEnabled`                     | No       | A Boolean indicating whether authentication through Apple is enabled in your environment.                                                                                                                                                                                                                |
| `companyLogo`                      | No       | The company logo.Used only when the main flow was launched using a redirect.                                                                                                                                                                                                                             |
| `isProtectAnalysisRequired`        | No       | Indicates whether PingOne Protect analysis is required.                                                                                                                                                                                                                                                  |
| `protectRiskPolicyId`              | No       | The PingOne Protect risk policy ID to use. If not specified, the default policy is used.                                                                                                                                                                                                                 |
| `p1VerifyPolicyIdReg`              | No       | The PingOne Verify policy ID to use.                                                                                                                                                                                                                                                                     |
| `digitalWalletApplicationId`       | No       | The ID of the digital wallet application.                                                                                                                                                                                                                                                                |
| `verifiedIdentityCredentialTypeId` | No       | The ID of the credential type to be used.                                                                                                                                                                                                                                                                |
| `verificationLimit`                | Yes      | The number of times a user can attempt verification.                                                                                                                                                                                                                                                     |
| `resendOtpLimit`                   | Yes      | The number of times a user can resend a one-time passcode (OTP) *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)*. |
| `govtIdVerificationLimit`          | No       | The number of times a user can attempt government ID verification.                                                                                                                                                                                                                                       |

## Output schema

This flow has the following outputs.

| Output name       | Description                                                                               |
| ----------------- | ----------------------------------------------------------------------------------------- |
| `subflowResult`   | The result status of the flow.                                                            |
| `p1UserId`        | The user ID of the current user.                                                          |
| `authMethod`      | The authentication method chosen by the user.                                             |
| `email`           | The email address associated with the new account.                                        |
| `firstName`       | The user's first name.                                                                    |
| `isSocialIDpAuth` | A Boolean that indicates whether the user signed on using social identity provider (IdP). |
| `errorMessage`    | The error message text to display, if any.                                                |
| `errorDetails`    | The details of the error that occurred in this flow.                                      |

## Variables and parameters

This flow uses the following variable or parameter values.

| Variable name       | Parameter name | Description                                         |
| ------------------- | -------------- | --------------------------------------------------- |
| `cachedEmail`       | None           | The user's cached email address.                    |
| `errorMessage`      | None           | The error message text to display, if any.          |
| `protectRiskEvalId` | None           | The risk evaluation ID returned by PingOne Protect. |

---

---
title: Healthcare - Agreement (ToS) - Subflow
description: Learn about the Healthcare - Agreement (ToS) - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:healthcare:flow-reference/healthcare-agreement-tos-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/flow-reference/healthcare-agreement-tos-subflow.html
revdate: May 29, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Healthcare - Agreement (ToS) - Subflow

The **Healthcare - Agreement (ToS) - Subflow** lets users read and confirm any agreement required in your environment.

## Purpose

The **Healthcare - Agreement (ToS) - Subflow** determines whether the user needs to consent to an agreement. If so, it displays the agreement for the user and stores the user's consent if they consent to the agreement.

## Structure

This flow is divided into sections using teleport nodes:

* **Check if agreement form needs to be displayed**

  Uses comparison nodes to check if agreement is enabled in the environment and if agreement is necessary for the current user. If so, a PingOne node checks the user's consent status.

  If consent isn't present, the flow progresses to the **Present & Accept Agreement** section.

  If consent is present, a function node checks if a success message should be displayed. The flow progresses to the **Present & Accept Agreement** if a success message should be displayed, and to the **Return Success** section if a success message should not be displayed.

* **Present & Accept Agreement**

  Uses a PingOne node to retrieve the required agreement, then presents the user with an HTML page. If the user hasn't yet agreed, this page lets them review and accept or decline the agreement. If the user has agreed, the form displays a success message, then the flow progresses to the **Return Success** section.

  If the user accepts the agreement, a PingOne node stores the user's agreement. The flow then returns to the beginning of the **Present & Accept Agreement** section if a success message should be displayed and to the **Return Success** section if a success message should not be displayed.

  If the user declines the agreement, an error message displays.

* **Return Success**

  Sends a success JSON response, indicating that the flow completed successfully.

* **Return Error**

  Uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input name           | Required | Description                                                                                   |
| -------------------- | -------- | --------------------------------------------------------------------------------------------- |
| `p1UserId`           | Yes      | The current user's PingOne user ID.                                                           |
| `agreementId`        | Yes      | The ID of the agreement to present to the user.                                               |
| `checkRequired`      | Yes      | Indicates whether the flow should check for existing consent before presenting the agreement. |
| `agreementEnabled`   | No       | Indicates whether the agreement is required.                                                  |
| `showSuccessMessage` | No       | Indicates whether a success message should be displayed after the user accepts the agreement. |
| `companyLogo`        | No       | The company logo.Used only when the main flow was launched using a redirect.                  |

## Output schema

This flow has the following outputs:

| Output name     | Description                                   |
| --------------- | --------------------------------------------- |
| `subflowResult` | The result status of the flow.                |
| `errorMessage`  | The error message to pass to the parent flow. |
| `errorDetails`  | The details of the error that occurred.       |

## Variables and parameters

This flow uses the following variable or parameter values:

| Parameter name       | Description                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------- |
| `p1UserId`           | The current user's PingOne user ID.                                                           |
| `agreementId`        | The ID of the agreement to present to the user.                                               |
| `checkRequired`      | Indicates whether the flow should check for existing consent before presenting the agreement. |
| `agreementEnabled`   | Indicates whether the agreement is required.                                                  |
| `showSuccessMessage` | Indicates whether a success message should be displayed after the user accepts the agreement. |

---

---
title: Healthcare - CSR Help Desk - Active Directory - User Functions API - Subflow
description: Learn about the Healthcare - CSR Help Desk - Active Directory - User Functions API - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:healthcare:flow-reference/healthcare-csr-active-directory-user-functions-api-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/flow-reference/healthcare-csr-active-directory-user-functions-api-subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Healthcare - CSR Help Desk - Active Directory - User Functions API - Subflow

The **Healthcare - CSR Help Desk - Active Directory - User Functions API - Subflow** takes account management actions on users.

## Purpose

The **Healthcare - CSR Help Desk - Active Directory - User Functions API - Subflow** accepts a user identifier and an action (enable, disable, or get user account information) as inputs. It finds the user using the identifier, then performs the specified action.

## Structure

This flow is divided into sections using teleport nodes:

* **Identify the CSR action from the input schema.**

  Uses a PingOne node to identify the user, then uses a function node to set flow variables. A function node then branches the flow based on the desired action, and the flow progresses to the portion of the **User Functions** section that corresponds with the desired action.

* **User Functions**

  Performs an action corresponding to the **action** input:

  * If the **action** is **getUserAccountStatus**, the flow uses a PingOne node to retrieve user information, then uses a function node to determine the correct account status button text. The flow then progresses to the **Return Success** section.

  * If the **action** is **disableUser**, the flow uses a PingOne node to disable the user. The flow then progresses to the **Return Success** section.

  * If the **action** is **enableUser**, the flow uses a PingOne node to enable the user. The flow then progresses to the **Return Success** section.

* **Return Success**

  Sends a success JSON response, indicating that the flow completed successfully.

* **Return Error**

  Sends an error JSON response, indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input name   | Required | Description                               |
| ------------ | -------- | ----------------------------------------- |
| `action`     | No       | The action to be taken during the flow.   |
| `identifier` | No       | The identifier to be used in user lookup. |

## Output schema

This flow has the following outputs:

| Output name       | Description                                                                |
| ----------------- | -------------------------------------------------------------------------- |
| `p1UserName`      | The user's PingOne user name.                                              |
| `p1Email`         | The email address associated with the user's PingOne account.              |
| `p1emailVerified` | A Boolean indicating whether the user's email address is verified.         |
| `accountStatus`   | The user's PingOne account status.                                         |
| `pwdLastChange`   | The date when the user's password was last changed.                        |
| `buttonLabel`     | The button label that should be displayed for the user's account status.   |
| `buttonValue`     | The action that the button should take based on the user's account status. |
| `responseData`    | An object containing additional error parameters.                          |
| `action`          | The action that was attempted during the flow.                             |
| `identifier`      | The identifier used in user lookup.                                        |

## Variables and parameters

This flow uses the following variable or parameter values:

| Variable name        | Description                                     |
| -------------------- | ----------------------------------------------- |
| `userAccountControl` | The user's account status.                      |
| `pwdLastSet`         | The date when the user's password was last set. |

---

---
title: Healthcare - CSR Help Desk - Change Password - Subflow
description: Learn about the Healthcare - CSR Help Desk - Change Password - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:healthcare:flow-reference/healthcare-csr-change-password-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/flow-reference/healthcare-csr-change-password-subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Healthcare - CSR Help Desk - Change Password - Subflow

The **Healthcare - CSR Help Desk - Change Password - Subflow** lets users change their passwords.

## Purpose

The **Healthcare - CSR Help Desk - Change Password - Subflow** displays a password reset form, letting users enter their current password and enter and verify a new password. If the new passwords match, the user's password is updated in PingOne.

## Structure

This flow is divided into sections using teleport nodes:

* **User Enter Password**

  Presents the user with an HTML template that that either displays a password reset form or displays a success message depending on the `showSuccessMessage` value. The flow then progresses to the **Update Password** section.

* **Update Password**

  Compares the new password and confirmed password, then validates the new password. If the new password meets the requirements, a PingOne node updates the user's password. The flow then either returns to the beginning of the **User Enter Password** section or progresses to the **Return Success** section, depending on the value of the `showSuccessMessage` input.

* **Return Success**

  Sends a JSON success message.

* **Return Error**

  Uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input name           | Required | Description                                                                                   |
| -------------------- | -------- | --------------------------------------------------------------------------------------------- |
| `p1UserId`           | Yes      | The current user's PingOne user ID.                                                           |
| `companyLogo`        | No       | The company logo.Used only when the main flow was launched using a redirect.                  |
| `showSuccessMessage` | No       | Indicates whether a success message should be displayed after the user accepts the agreement. |

## Output schema

This flow has the following outputs:

| Output name     | Description                                   |
| --------------- | --------------------------------------------- |
| `subflowResult` | The result status of the flow.                |
| `errorMessage`  | The error message to pass to the parent flow. |
| `errorDetails`  | The details of the error that occurred.       |

## Variables and parameters

This flow uses the following variable or parameter values:

| Parameter name       | Description                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------- |
| `p1UserId`           | The current user's PingOne user ID.                                                           |
| `showSuccessMessage` | Indicates whether a success message should be displayed after the user accepts the agreement. |

---

---
title: Healthcare - CSR Help Desk - Device Authentication - Subflow
description: Learn about the Healthcare - CSR Help Desk - Device Authentication - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:healthcare:flow-reference/healthcare-csr-device-authentication-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/flow-reference/healthcare-csr-device-authentication-subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Healthcare - CSR Help Desk - Device Authentication - Subflow

The **Healthcare - CSR Help Desk - Device Authentication - Subflow** lets users authenticate using a known device.

## Purpose

The **Healthcare - CSR Help Desk - Device Authentication - Subflow** enables users to authenticate using a known device. The flow evaluates the devices associated with the user account, then enables the user to select an authentication method and authenticates the user with the selected method.

## Structure

This flow is divided into sections using teleport nodes:

* **Gather Devices Data**

  Uses a PingOne node to gather the user's existing devices. Next, a function node filters the list of available devices to create a list of usable devices. The flow then progresses to the **Filter and Mask Devices** section.

* **Filter and Mask Devices**

  Uses a function node to mask the device information so that the devices can be identified without displaying the full device information, then uses a PingOne node to check the user's multi-factor authentication (MFA) status. The flow then progresses to the **Check If MFA Enabled And Any Device Active** section.

* **Check If MFA Enabled And Any Device Active**

  If MFA is enabled and the user has active devices, the flow uses a PingOne node to begin MFA. The flow then progresses to the **Decide Authentication Path Based On MFA Policy** section.

* **Decide Authentication Path Based On MFA Policy**

  Uses a function node to branch based on the response status:

  * If a one-time passcode (OTP) is required, the flow progresses to the **Default Device Enrichment** section.

  * If device selection is required, a function node checks if the user has one available device:

    * If the user has one device, a PingOne node begins MFA, then the flow progresses to the **Default Device Enrichment** section.

    * If the user has more than one device, the flow progresses to the **Device Selection** section.

- **Device Selection**

  Presents the user with an HTML page on which they can select a device:

  * If the user cancels, the flow progresses to the **Return Success** section.

  * If the user selects a device, a PingOne node processes the device selection, and the flow progresses to the **Default Device Enrichment** section.

* **Default Device Enrichment**

  Uses a function node to enrich the device details, then the flow progresses to the **Handle SMS, Voice, Email OTP Authentication** section if an OTP is required.

* **Handle SMS, Voice, Email OTP Authentication**

  Uses function nodes to begin tracking the number of attempts and check the device type, then presents the user with an HTML page with options to enter the passcode, change devices, or resend the OTP:

  * If the user selects resend, the number of resend attempts is incremented and compared to the maximum. If the maximum hasn't been reached, a PingOne node resends the OTP and a confirmation message displays.

  * If the user selects a different method, the flow progresses to the **Device Selection** section.

  * If the user enters a passcode, a function node converts the value to lowercase, then a PingOne MFA node evaluates the passcode. If the passcode is validated successfully, the authentication method is saved as a variable and the flow progresses to the **Return Success** section.

- **Mobile Passcode Flow**

  Presents users with an HTML form, with options for retrying, cancelling, or submitting an OTP:

  * If the user retries, a PingOne MFA node performs device selection, and the flow returns to the **Mobile Passcode Flow** section.

  * If the user cancels, the flow progresses to the **Device Selection** section.

  * If the user submits an OTP, a PingOne MFA node checks the device passcode. A function node then saves the authentication method as a variable, and the flow progresses to the **Return Success** section.

* **Return Success**

  Sends a success JSON response, indicating that the flow completed successfully.

* **Return Error**

  Sends an error JSON response, indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input name           | Required | Description                                                                                                     |
| -------------------- | -------- | --------------------------------------------------------------------------------------------------------------- |
| `p1UserId`           | Yes      | The current user's PingOne user ID.                                                                             |
| `resendOtpLimit`     | Yes      | The maximum number of times a new OTP can be sent to the user.                                                  |
| `email`              | No       | The user's email address.                                                                                       |
| `p1MFAPolicyId`      | No       | The PingOne MFA policy to apply.                                                                                |
| `allowedDeviceTypes` | No       | A string containing any or all of `SMS, EMAIL, FIDO2, TOTP, VOICE, MOBILE` indicating the allowed device types. |
| `companyLogo`        | No       | The company logo.Used only when the main flow was launched using a redirect.                                    |
| `cancelEnabled`      | No       | A Boolean indicating whether the user can cancel an authentication method selection.                            |

## Output schema

This flow has the following outputs:

| Output name     | Description                                                             |
| --------------- | ----------------------------------------------------------------------- |
| `subflowResult` | The result status of the flow.                                          |
| `authMethod`    | The authentication method used, if the user successfully authenticated. |
| `errorMessage`  | The error message to pass to the parent flow.                           |
| `errorDetails`  | The details of the error that occurred.                                 |

## Variables and parameters

This flow uses the following variable or parameter values:

| Variable name       | Parameter name | Description                                     |
| ------------------- | -------------- | ----------------------------------------------- |
| `resendOtpAttempts` | None           | The number of times the user has resent an OTP. |
| `authenticators`    | None           | The authentication method used.                 |

---

---
title: Healthcare - CSR Help Desk - Main Flow
description: Learn about the Healthcare - CSR Help Desk - Main Flow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:healthcare:flow-reference/healthcare-csr-help-desk-main-flow
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/flow-reference/healthcare-csr-help-desk-main-flow.html
revdate: September 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Healthcare - CSR Help Desk - Main Flow

The **Healthcare - CSR Help Desk - Main Flow** lets a customer service representative assist a customer in changing their password or regaining account access.

## Purpose

The **Healthcare - CSR Help Desk - Main Flow** presents lets a customer service representative assist users with a variety of account management tasks. The CSR enters the user's email address, then the flow verifies the user's identity using the **Healthcare - CSR Help Desk - Verify User Magic Link Authentication - Subflow**.

The CSR is then presented with multiple account management options:

* Enable the user's account using the **Healthcare - CSR Help Desk - Active Directory - User Functions API - Subflow**.

* Reset the user's password using the **Healthcare - CSR Help Desk - Password reset Magic Link - Subflow**.

* Disable the user's account using the **Healthcare - CSR Help Desk - Active Directory - User Functions API - Subflow**.

## Structure

This flow is divided into sections using teleport nodes:

* **Flow Configuration**

  Uses multiple function nodes to save the variable and parameter values so that the correct values are available in the flow and in subflows. The flow then progresses to the **CSR Flow for Verification** section.

* **CSR Flow for Verification**

  Uses an HTML node to request a username, then uses a PingOne node to look up the user. If the user has a configured email address, the flow progresses to the **Check if some MFA device is registered for user and can be used** section. When this section completes, the **Healthcare - CSR Help Desk - Verify User Magic Link Authentication - Subflow** is invoked.

  When the subflow completes, a success message is displayed and the user ID is saved as a variable. The flow then progresses to the **User Account management** section.

* **User Account management**

  Invokes the **Healthcare - CSR Help Desk - Active Directory - User Functions API - Subflow**. When the subflow completes, a function node adjusts the date format, then an HTML node presents a form with the account management options:

  * If the agent selects **Disable**, the **Healthcare - CSR Help Desk - Active Directory - User Functions API - Subflow** is invoked with the `disableUser` action. If the subflow completes successfully, a success message displays, then the flow returns to the beginning of the **User Account management** section.

  * If the agent selects **Reset**, the **Healthcare - CSR Help Desk - Password reset Magic Link - Subflow** is invoked. If the subflow completes successfully, a success message appropriate to the subflow completion status displays, then the flow returns to the beginning of the **User Account management** section.

  * If the agent selects **Enable**, the **Healthcare - CSR Help Desk - Active Directory - User Functions API - Subflow** is invoked with the `enableUser` action. If the subflow completes successfully, a success message displays, then the flow returns to the beginning of the **User Account management** section.

  * If the agent selects **Back**, the flow progresses to the **CSR Flow for Verification** section.

* **Check if some MFA device is registered for user and can be used**

  Uses a PingOne MFA node to read the user's devices, then uses a hidden HTML node to check if the user's browser is compatible with WebAuthn. Function nodes then filter the user's usable devices and verify that the user has at least one active device. The flow then returns to the **CSR Flow for Verification** section.

* **Return Error**

  Uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has no inputs.

## Output schema

This flow has the following outputs:

| Output name    | Description                                          |
| -------------- | ---------------------------------------------------- |
| `errorMessage` | The error message to display in the parent flow.     |
| `errorDetails` | The details of the error that occurred in this flow. |

## Variables and parameters

This flow uses the following variable or parameter values:

| Variable name                  | Description                                                                                                    |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| `flowCompanyLogo`              | The URL for your company logo.                                                                                 |
| `p1MFAPolicyId`                | The ID of the PingOne MFA policy to use in the flow.                                                           |
| `p1AgreementId`                | The ID of the agreement to present to users.                                                                   |
| `p1RiskPolicyIdAuthn`          | The PingOne risk policy ID to use for authentication.                                                          |
| `p1RiskPolicyIdAR`             | The PingOne risk policy ID to use for account recovery.                                                        |
| `p1RiskPolicyIdReg`            | The PingOne risk policy ID to use for registration.                                                            |
| `protectRiskEvalId`            | The risk ID of the current user as used by PingOne Protect.                                                    |
| `authMethod`                   | The authentication method used in the flow.                                                                    |
| `flowProtectAnalysisRequired`  | Indicates whether a PingOne Protect analysis must be performed for all users.                                  |
| `ciam_accountRecoveryEnabled`  | A Boolean that controls whether account recovery is enabled in your environment.                               |
| `ciam_appleEnabled`            | Indicates whether authentication through Apple is enabled in your environment.                                 |
| `ciam_facebookEnabled`         | Indicates whether authentication through Facebook is enabled in your environment.                              |
| `ciam_googleEnabled`           | Indicates whether authentication through Google is enabled in your environment.                                |
| `ciam_magicLinkEnabled`        | Indicates whether magic link authentication is enabled.                                                        |
| `ciam_agreementEnabled`        | Indicates whether the agreement is required.                                                                   |
| `ciam_protectAnalysisRequired` | Indicates whether PingOne Protect analysis is required.                                                        |
| `ciam_logoUrl`                 | The URL for your company logo.This value is used only when the flow is launched with a redirect.               |
| `ciam_companyName`             | Displays the name of your company.This value is used only when the flow is launched with a redirect.           |
| `ciam_logoStyle`               | The HTML style to use for your company logo.This value is used only when the flow is launched with a redirect. |
| `ciam_requireMFA`              | A Boolean that controls whether MFA enrollment is required for all users.                                      |
| `flowRequireMFA`               | A Boolean that indicates whether MFA enrollment is required for all users in the current flow.                 |
| `flowMethod`                   | The method used to launch the flow.                                                                            |

---

---
title: Healthcare - CSR Help Desk - Password reset Magic Link - Subflow
description: Learn about the Healthcare - CSR Help Desk - Password reset Magic Link - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:healthcare:flow-reference/healthcare-csr-password-reset-magic-link-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/flow-reference/healthcare-csr-password-reset-magic-link-subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Healthcare - CSR Help Desk - Password reset Magic Link - Subflow

The **Healthcare - CSR Help Desk - Password reset Magic Link - Subflow** lets existing users authenticate using a link sent to the email address that's associated with their account.

## Purpose

The **Healthcare - CSR Help Desk - Password reset Magic Link - Subflow** presents users with the option to send a magic link to the email address associated with their account. After the link is sent, the flow checks the status of the link.

* If the user clicks the link, the flow authenticates the user.

* If the link expires, the flow presents an error message. The magic link expires after 2.5 minutes (150 seconds).

## Structure

This flow is divided into sections using teleport nodes:

* **Display Magic Link Form**

  Uses a PingOne node to look up the user, then presents an HTML form from which the user can send a magic link. If the user clicks **Submit**, the flow simultaneously progresses to the **Create Challenge and Send Email** and **Challenge Acceptance By The User** sections. If the user clicks any other option, the flow progresses to the **Return Success** section.

* **Create Challenge and Send Email**

  Uses a flow conductor to begin an out-of-band process, then uses a PingOne node to send a magic link email. The flow then progresses to the **Display Magic Link Polling And Check For Challenge Status** section.

* **Challenge Acceptance By The User**

  Checks the challenge status and displays a success message if the magic link is clicked and an error message if the magic link times out.

* **Display Magic Link Polling And Check For Challenge Status**

  Displays a custom HTML template directing users to click the magic link. When the challenge is approved, the flow progresses to the **Go To Success** section. If the challenge expires, the flow progresses to the **Challenge Expiration** section.

* **Go To Success**

  Progresses to the **Return Success** section.

* **Challenge Expiration**

  Denies the challenge if the magic link expires. The flow then progresses to the **Return Error** section.

* **Return Success**

  Sends a success JSON response, indicating that the flow completed successfully.

* **Return Error**

  Uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input name    | Required | Description                                                                  |
| ------------- | -------- | ---------------------------------------------------------------------------- |
| `p1UserId`    | Yes      | The current user's PingOne user ID.                                          |
| `companyLogo` | No       | The company logo.Used only when the main flow was launched using a redirect. |

## Output schema

This flow has the following outputs:

| Output name     | Description                                          |
| --------------- | ---------------------------------------------------- |
| `subflowResult` | The result status of the flow.                       |
| `errorMessage`  | The error message to display in the parent flow.     |
| `errorDetails`  | The details of the error that occurred in this flow. |

## Variables and parameters

This flow does not directly use any variable or parameter values.

---

---
title: Healthcare - CSR Help Desk - Verify User Magic Link Authentication - Subflow
description: Learn about the Healthcare - CSR Help Desk - Verify User Magic Link Authentication - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:healthcare:flow-reference/healthcare-csr-help-desk-verify-user-magic-link
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/flow-reference/healthcare-csr-help-desk-verify-user-magic-link.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Healthcare - CSR Help Desk - Verify User Magic Link Authentication - Subflow

The **Healthcare - CSR Help Desk - Verify User Magic Link Authentication - Subflow** lets existing users authenticate using a link sent to the email address that's associated with their account.

## Purpose

The **Healthcare - CSR Help Desk - Verify User Magic Link Authentication - Subflow** presents users with the option to send a magic link to the email address associated with their account. After the link is sent, the flow checks the status of the link.

* If the user clicks the link, the flow authenticates the user.

* If the link expires, the flow presents an error message. The magic link expires after 2.5 minutes (150 seconds).

## Structure

This flow is divided into sections using teleport nodes:

* **Display Magic Link Form**

  Uses a PingOne node to look up the user, then presents an HTML form from which the user can send a magic link. If the user clicks **Submit**, the flow simultaneously progresses to the **Create Challenge and Send Email** and **Challenge Acceptance By The User** sections. If the user clicks **Cancel**, the flow progresses to the **Return Success** section.

* **Create Challenge and Send Email**

  Uses a flow conductor to begin an out-of-band process, then uses a PingOne node to send a magic link email. The flow then progresses to the **Display Magic Link Polling And Check For Challenge Status** section.

* **Challenge Acceptance By The User**

  Checks the challenge status. If the challenge is not expired, the flow displays a UI holding screen, then invokes the **Healthcare - CSR Help Desk - Device Authentication - Subflow**. When the subflow completes, the challenge status is set to approved and a success message displays for the user. If the challenge expires, an error message displays.

* **Display Magic Link Polling And Check For Challenge Status**

  Displays a custom HTML template directing users to click the magic link. When the challenge is approved, the flow progresses to the **Go To Success** section. If the challenge expires, the flow progresses to the **Challenge Expiration** section.

* **Go To Success**

  Progresses to the **Return Success** section.

* **Challenge Expiration**

  Denies the challenge if the magic link expires. The flow then progresses to the **Return Error** section.

* **Return Success**

  Sends a success JSON response, indicating that the flow completed successfully.

* **Return Error**

  Uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input name           | Required | Description                                                                                                     |
| -------------------- | -------- | --------------------------------------------------------------------------------------------------------------- |
| `p1UserId`           | Yes      | The current user's PingOne user ID.                                                                             |
| `canChangeDevice`    | Yes      | Indicates whether the user can change MFA devices.                                                              |
| `p1MFAPolicyId`      | No       | The PingOne MFA policy to apply.                                                                                |
| `allowedDeviceTypes` | No       | A string containing any or all of `SMS, EMAIL, FIDO2, TOTP, VOICE, MOBILE` indicating the allowed device types. |
| `companyLogo`        | No       | The company logo.Used only when the main flow was launched using a redirect.                                    |

## Output schema

This flow has the following outputs:

| Output name     | Description                                          |
| --------------- | ---------------------------------------------------- |
| `subflowResult` | The result status of the flow.                       |
| `errorMessage`  | The error message to display in the parent flow.     |
| `errorDetails`  | The details of the error that occurred in this flow. |

## Variables and parameters

This flow does not directly use any variable or parameter values.

---

---
title: Healthcare - Identity Verification and Managed Credential Issuance with Biometric Binding - Subflow
description: Learn about the Healthcare - Identity Verification and Managed Credential Issuance with Biometric Binding - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:healthcare:flow-reference/healthcare-identity-verification-and-managed-credential-issuance-with-biometric-binding-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/flow-reference/healthcare-identity-verification-and-managed-credential-issuance-with-biometric-binding-subflow.html
revdate: September 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Healthcare - Identity Verification and Managed Credential Issuance with Biometric Binding - Subflow

The **Healthcare - Identity Verification and Managed Credential Issuance with Biometric Binding - Subflow** uses PingOne Verify to verify the user and issue credentials.

## Purpose

The **Healthcare - Identity Verification and Managed Credential Issuance with Biometric Binding - Subflow** lets users supply email and phone number information, then verifies their identity using PingOne Verify. It uses the **Healthcare - Pair A Digital Wallet - Subflow** to pair a digital wallet and issues relevant credentials to that wallet.

## Structure

This flow is divided into sections using teleport nodes:

* **Registration using Identity Verification + Managed Credential Issuance**

  Uses a hidden HTML node and function nodes to gather user information and set variables, then presents the user with a consent form.

  If the user consents, an HTML node gathers the user's email and phone number. A function node discards any modifications to the user's email, then a PingOne node looks for existing users with a matching email. If no user exists with a matching email, a new user is created:

  * If the new user creation succeeds, a PingOne node disables the new user and the flow progresses to the **Verify And Issue Credentials To Wallet** section.

  * If the new user creation fails, a function node evaluates the phone number and displays a targeted error message if the phone number isn't valid.

* **Verify And Issue Credentials To Wallet**

  The flow progresses to the **Initiate Verification** section.

  When this section completes, a function node increments the number of verification attempts, then the flow progresses to the **Process Verification** section.

  When this section completes, a function node checks whether the verification was successful:

  * If the verification was successful, a function node checks whether credentials should be issued to a digital wallet:

    * If credentials shouldn't be issued to a digital wallet, the flow progresses to the **Return Success Response** section.

    * If credentials should be issued to a digital wallet, the **Healthcare - Pair A Digital Wallet - Subflow** is invoked. If the subflow completes successfully, HTTP nodes get an access token and issue credentials to the user's wallet, then a PingOne node reads the updated user information. The flow then progresses to the **Return Success Response** section.

  * If the verification wasn't successful, a function node checks if the verification limit has been exceeded. If not, an error page lets the user choose an action, and the flow progresses to the beginning of the **Verify And Issue Credentials To Wallet** section if the user retries or to the **Return Success Response** section if the user cancels.

* **Initiate Verification**

  Uses a PingOne Verify node to create a transaction:

  * If the transaction creation succeeds, a verification QR code is displayed, then a PingOne Verify node reads the transaction. A function node confirms that the verification has begun, then the flow progresses to the **Process Verification** section.

  * If the transaction creation fails, a function node checks if the user email or phone number was invalid. If so, a PingOne node deletes the user and an error message is displayed.

* **Process Verification**

  Displays an HTML node indicating that verification is in progress, then uses a PingOne Verify node to read the verification transaction. A function node then checks the verification status:

  * If the verification succeeded, PingOne Verify nodes retrieve the user's selfie, user data, and transaction metadata. An HTML node requests that the user verify the data, then custom functions package the data and a PingOne node updates the user information. The flow then returns to the **Verify And Issue Credentials To Wallet** section.

  * If the verification failed, the flow returns to the **Verify And Issue Credentials To Wallet** section.

  * If the verification has no status yet, polling continues.

* **Return Success Response**

  Uses a PingOne node to delete the user entry if the user canceled and the user ID is known, then ends a success JSON response, indicating that the flow completed successfully.

* **Return Error Response**

  Uses a PingOne node to delete the user entry if the user ID is known. The flow then uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input name                         | Required | Description                                                                                                                                                     |
| ---------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `emailAddress`                     | No       | The user's email address.                                                                                                                                       |
| `verifyPolicyId`                   | Yes      | The PingOne Verify policy ID.                                                                                                                                   |
| `verificationLimit`                | No       | The maximum number of times the user can attempt verification.                                                                                                  |
| `issueCredentialsToWallet`         | No       | A Boolean that controls whether credentials are issued to the user's wallet. If it is set to `false`, the flow only performs verification using PingOne Verify. |
| `digitalWalletApplicationId`       | No       | The ID of the user's digital wallet application.                                                                                                                |
| `verifiedIdentityCredentialTypeId` | No       | The ID of the user's credential type.                                                                                                                           |
| `companyLogo`                      | No       | The company logo.Used only when the main flow was launched using a redirect.                                                                                    |

## Output schema

This flow has the following outputs:

| Output name       | Description                                                              |
| ----------------- | ------------------------------------------------------------------------ |
| `subflowResult`   | The result status of the flow.                                           |
| `p1UserId`        | The user's PingOne user ID.                                              |
| `email`           | The user's email address.                                                |
| `firstName`       | The user's first name.                                                   |
| `isEmailVerified` | A Boolean indicating whether the user's email address has been verified. |
| `errorMessage`    | The error message to display in the parent flow.                         |
| `errorDetails`    | The details of the error that occurred in this flow.                     |

## Variables and parameters

This flow uses the following variable or parameter values:

| Variable name                      | Description                                                          |
| ---------------------------------- | -------------------------------------------------------------------- |
| `p1VerifyPolicyId`                 | The PingOne Verify policy ID.                                        |
| `digitalWalletApplicationId`       | The ID of the user's digital wallet application.                     |
| `pingOneAPIBaseUrl`                | The URL of the PingOne APIs for the user's region.                   |
| `verifiedIdentityCredentialTypeId` | The ID of the user's credential type.                                |
| `authPath`                         | The authorization URL using the user's region and the company ID.    |
| `verificationValidationAttempts`   | The number of times the user has attempted to verify their identity. |

---

---
title: Healthcare - Pair A Digital Wallet - Subflow
description: Learn about the Healthcare - Pair A Digital Wallet - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:healthcare:flow-reference/healthcare-pair-a-digital-wallet
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/flow-reference/healthcare-pair-a-digital-wallet.html
revdate: September 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Healthcare - Pair A Digital Wallet - Subflow

The **Healthcare - Pair A Digital Wallet - Subflow** lets users pair a new digital wallet.

## Purpose

The **Healthcare - Pair A Digital Wallet - Subflow** checks if the user has a verified mobile number.

* If the user does have a verified mobile number, the flow lets them pair a digital wallet using their mobile device, with a QR code as an alternate option.

* If the user doesn't have a verified mobile number, the flow lets them pair a digital wallet using a QR code.

## Structure

This flow is divided into sections using teleport nodes:

* **Choose QR Path Or SMS**

  Uses a PingOne node to retrieve the user's devices. The flow then progresses to the **Deliver Wallet Pairing Request via Trusted Mobile Channel** section if the user has a verified mobile number, and to the **Pair Wallet using QR Code** section if the user does not have a verified mobile number.

* **Deliver Wallet Pairing Request via Trusted Mobile Channel**

  Uses a PingOne Credentials node to create a pairing request. Function nodes then retrieve the pairing notification information and verify the notification was sent.

  An HTML node directs the user to follow the instructions on their mobile device, providing the option of using a QR code instead.

  If the user selects the QR code option, the flow checks the user's device. If the user is using a mobile or laptop, a pairing QR code is displayed, and the flow progresses to the **Process Pairing Status** section.

  If the user has not selected the QR code option, the flow progresses to the **Process Pairing Status** section.

* **Pair Wallet using QR Code**

  Uses a PingOne Credentials node to create a pairing request. The flow then checks the user's device. If the user is using a mobile or laptop, a pairing QR code is displayed, and the flow progresses to the **Process Pairing Status** section.

* **Process Pairing Status**

  Uses a PingOne node to check the wallet pairing status. If pairing is complete, the flow sends a success JSON response indicating that the flow completed successfully. If pairing is incomplete, the flow continues polling.

* **Return Error**

  Uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input name    | Required | Description                                                                  |
| ------------- | -------- | ---------------------------------------------------------------------------- |
| `p1UserId`    | Yes      | The user ID of the current user.                                             |
| `companyLogo` | No       | The company logo.Used only when the main flow was launched using a redirect. |

## Output schema

This flow has the following outputs:

| Output name                  | Description                                          |
| ---------------------------- | ---------------------------------------------------- |
| `digitalWalletPairingStatus` | The user's wallet pairing status.                    |
| `digitalWalletId`            | The ID of the user's paired wallet.                  |
| `digitalWalletDeviceData`    | The device data associated with the user's wallet.   |
| `errorMessage`               | The error message to display in the parent flow.     |
| `errorDetails`               | The details of the error that occurred in this flow. |

## Variables and parameters

This flow uses the following variable or parameter values:

| Variable name        | Description                                                                 |
| -------------------- | --------------------------------------------------------------------------- |
| `canEnrollOnlyEmail` | A Boolean indicating whether email should be the only permitted MFA device. |
| `resendOtpAttempts`  | The number of times the user has resent the OTP.                            |
| `p1MFADeviceId`      | The device ID for the device being registered.                              |

---

---
title: Healthcare - Progressive Verification during Authentication - Change Password - Subflow
description: Learn about the Healthcare - Progressive Verification during Authentication - Change Password - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:healthcare:flow-reference/healthcare-authentication-change-password-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/flow-reference/healthcare-authentication-change-password-subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Healthcare - Progressive Verification during Authentication - Change Password - Subflow

The **Healthcare - Progressive Verification during Authentication - Change Password - Subflow** lets users change their passwords.

## Purpose

The **Healthcare - Progressive Verification during Authentication - Change Password - Subflow** displays a password reset form, letting users enter their current password and enter and verify a new password. If the new passwords match, the user's password is updated in PingOne.

## Structure

This flow is divided into sections using teleport nodes:

* **User Enter Password**

  Presents the user with an HTML template that that either displays a password reset form or displays a success message depending on the `showSuccessMessage` value. The flow then progresses to the **Update Password** section.

* **Update Password**

  Compares the new password and confirmed password, then validates the new password. If the new password meets the requirements, a PingOne node updates the user's password. The flow then either returns to the beginning of the **User Enter Password** section or progresses to the **Return Success** section, depending on the value of the `showSuccessMessage` input.

* **Return Success**

  Sends a JSON success message.

* **Return Error**

  Uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input name           | Required | Description                                                                                   |
| -------------------- | -------- | --------------------------------------------------------------------------------------------- |
| `p1UserId`           | Yes      | The current user's PingOne user ID.                                                           |
| `companyLogo`        | No       | The company logo.Used only when the main flow was launched using a redirect.                  |
| `showSuccessMessage` | No       | Indicates whether a success message should be displayed after the user accepts the agreement. |

## Output schema

This flow has the following outputs:

| Output name     | Description                                   |
| --------------- | --------------------------------------------- |
| `subflowResult` | The result status of the flow.                |
| `errorMessage`  | The error message to pass to the parent flow. |
| `errorDetails`  | The details of the error that occurred.       |

## Variables and parameters

This flow uses the following variable or parameter values:

| Parameter name       | Description                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------- |
| `p1UserId`           | The current user's PingOne user ID.                                                           |
| `showSuccessMessage` | Indicates whether a success message should be displayed after the user accepts the agreement. |

---

---
title: Healthcare - Progressive Verification during Authentication - Device Authentication - Subflow
description: Learn about the Healthcare - Progressive Verification during Authentication - Device Authentication - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:healthcare:flow-reference/healthcare-authentication-device-authentication-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/flow-reference/healthcare-authentication-device-authentication-subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Healthcare - Progressive Verification during Authentication - Device Authentication - Subflow

The **Healthcare - Progressive Verification during Authentication - Device Authentication - Subflow** lets users authenticate using a known device.

## Purpose

The **Healthcare - Progressive Verification during Authentication - Device Authentication - Subflow** enables users to authenticate using a known device. The flow evaluates the devices associated with the user account, invoking the **Healthcare - Progressive Verification during Authentication - Magic Link Authentication - Subflow** flow if necessary. It then enables the user to select an authentication method and authenticates the user with the selected method.

## Structure

This flow is divided into sections using teleport nodes:

* **Gather Browser And Devices Data**

  Uses a PingOne node to gather the user's existing devices. Next, an HTML node evaluates the user's browser to determine if biometrics are available. The flow then progresses to the **Filter and Mask Devices** section.

* **Filter and Mask Devices**

  Filters the list of available devices to create a list of usable devices, then masks the device information so that the devices can be identified without displaying the full device information. The flow then progresses to the **Check If MFA Enabled And Any Device Active** section.

* **Check If MFA Enabled And Any Device Active**

  Uses a PingOne node to check the user's multi-factor authentication (MFA) status. If MFA is enabled and the user has active devices, the flow progresses to the **Decide Authentication Path Based On MFA Policy** section. If MFA is not enabled, or the user has no active devices, the flow progresses to the **Call Magic Link Authentication** section.

* **Decide Authentication Path Based On MFA Policy**

  Uses a PingOne node to begin MFA. If an assertion or a one-time passcode (OTP) is required, the flow progresses to the **Default Device Enrichment** section. If the user has multiple devices, or if the user has only one usable device and magic link is enabled, the flow progresses to the **Device Selection** section. If the user has one usable device and magic link isn't enabled, the flow progresses to the **Default Device Enrichment** section.

* **Call Magic Link Authentication**

  Invokes the **Healthcare - Progressive Verification during Authentication - Magic Link Authentication - Subflow** flow if magic link authentication is enabled. The flow then progresses to the **Return Success** section.

* **Device Selection**

  Presents the user with an HTML page on which they can select a device:

  * If the user selected magic link, the **Healthcare - Progressive Verification during Authentication - Magic Link Authentication - Subflow** flow is invoked, and the flow then progresses to the **Return Success** section or to the **Device Selection** section depending on the subflow results.

  * If the user selected another authentication method, a PingOne node records their selection and the flow progresses to the **Default Device Enrichment** section.

* **Default Device Enrichment**

  Uses a function node to enrich the device details, then the flow progresses to the **Handle TOTP, SMS, Voice, Mobile and Email OTP Authentication** section if an OTP is required, to the **Handle FIDO2 Authentication** section if assertion is required, or to the **Start Mobile Push** section if push confirmation is required.

* **Handle TOTP, SMS, Voice, Mobile and Email OTP Authentication**

  Uses function nodes to begin tracking the number of attempts and check the device type, then presents the user with an HTML page with options to enter the passcode, change devices, or resend the OTP:

  * If the user selects resend, the number of resend attempts is incremented and compared to the maximum. If the maximum hasn't been reached, a PingOne node resends the OTP and a confirmation message displays.

  * If the user selects a different method, the flow progresses to the **Device Selection** section.

  * If the user enters a passcode, a function node converts the value to lowercase, then a PingOne MFA node evaluates the passcode. If the passcode is validated successfully, the authentication method is saved as a variable and the flow progresses to the **Return Success** section.

* **Handle FIDO2 Authentication**

  Presents users with the option to select a different device or continue with the current device. If the user selects a different device, it progresses to the **Device Selection** section. If the user continues, it uses a PingOne MFA node with FIDO assertion to authenticate the user. If the authentication succeeds, the flow progresses to the **Return Success** section.

* **Mobile Push Flow**

  Displays a polling page, then branches based on the user's selection:

  * If the user chooses to use a passcode, the flow progresses to the **Mobile Passcode Flow** section.

  * If the user chooses to use a different device, the flow progresses to the **Device Selection** section.

  * If the user attempts to authenticate using the current device, a PingOne MFA node reads the device authentication.

  The flow branches again based on the authentication status:

  * If the status is complete, a function node saves the authentication method as a variable and the flow progresses to the **Return Success** section.

  * If the status is failed, a function node checks whether the attempt timed out. If so, the flow progresses to the **Mobile App Timed Out** section.

  * If the status is `push configuration required`, polling continues.

  * If the status is `push configuration timed out`, a function node checks if OTP fallback is allowed. If so, the flow progresses to the **Mobile Passcode Flow** section.

* **Mobile Passcode Flow**

  Presents users with an HTML form, with options for retrying, cancelling, or submitting an OTP.:

  * If the user retries, a PingOne MFA node performs device selection, and the flow returns to the **Mobile Push Flow** section.

  * If the user cancels, the flow progresses to the **Device Selection** section.

  * If the user submits an OTP, a PingOne MFA node checks the device passcode. A function node then saves the authentication method as a variable, and the flow progresses to the **Return Success** section.

* **Mobile App Timed Out**

  Displays an error screen which presents the user with multiple options:

  * If the user retries, a PingOne MFA node performs device selection, and the flow returns to the **Mobile Push Flow** section.

  * If the user selects `Change Device`, the flow progresses to the **Device Selection** section.

* **Return Success**

  Sends a success JSON response, indicating that the flow completed successfully.

* **Return Error**

  Sends an error JSON response, indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input name           | Required | Description                                                                                                     |
| -------------------- | -------- | --------------------------------------------------------------------------------------------------------------- |
| `p1UserId`           | Yes      | The current user's PingOne user ID.                                                                             |
| `resendOtpLimit`     | Yes      | The maximum number of times a new OTP can be sent to the user.                                                  |
| `email`              | No       | The user's email address.                                                                                       |
| `p1MFAPolicyId`      | No       | The PingOne MFA policy to apply.                                                                                |
| `allowedDeviceTypes` | No       | A string containing any or all of `SMS, EMAIL, FIDO2, TOTP, VOICE, MOBILE` indicating the allowed device types. |
| `otpFallbackAllowed` | No       | A Boolean indicating whether a user can fall back to an OTP after an authentication failure.                    |
| `magicLinkEnabled`   | No       | A Boolean indicating whether magic link is enabled.                                                             |
| `companyLogo`        | No       | The company logo.Used only when the main flow was launched using a redirect.                                    |
| `cancelEnabled`      | No       | A Boolean indicating whether the user can cancel an authentication method selection.                            |

## Output schema

This flow has the following outputs:

| Output name     | Description                                                             |
| --------------- | ----------------------------------------------------------------------- |
| `subflowResult` | The result status of the flow.                                          |
| `authMethod`    | The authentication method used, if the user successfully authenticated. |
| `errorMessage`  | The error message to pass to the parent flow.                           |
| `errorDetails`  | The details of the error that occurred.                                 |

## Variables and parameters

This flow uses the following variable or parameter values:

| Variable name       | Parameter name | Description                                     |
| ------------------- | -------------- | ----------------------------------------------- |
| `resendOtpAttempts` | None           | The number of times the user has resent an OTP. |

---

---
title: Healthcare - Progressive Verification during Authentication - Device Registration - Subflow
description: Learn about the Healthcare - Progressive Verification during Authentication - Device Registration - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:healthcare:flow-reference/healthcare-authentication-device-registration-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/flow-reference/healthcare-authentication-device-registration-subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Healthcare - Progressive Verification during Authentication - Device Registration - Subflow

The **Healthcare - Progressive Verification during Authentication - Device Registration - Subflow** lets users register a new device.

## Purpose

The **Healthcare - Progressive Verification during Authentication - Device Registration - Subflow** presents users with options to register any available device type. The flow finds the available devices, then uses an HTML node to let the user select one of the following options:

* If the user selects **Mobile Application**, the flow creates a pairing key to pair the application with the account.

* If the user selects **Biometrics/Security Key**, the flow pairs the current FIDO-supported device.

* If the user selects **Authenticator App**, the flow uses a key URL to pair an authenticator app with the account.

* If the user selects **Text Message**, the flow gathers the number and uses a one-time passcode (OTP) *(tooltip: \<div class="paragraph">
  \<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
  \</div>)* to verify the SMS number.

* If the user selects **Voice** the flow gathers the number and uses an OTP to verify the phone number.

* If the user selects **Email**, the flow uses an OTP to verify the email address.

After any successful device registration, or if the user selects password, the flow returns to the parent flow.

## Structure

This flow is divided into sections using teleport nodes:

* **Gather Device Types That User Can Register With**

  Uses a PingOne node to retrieve the user's current devices, then uses a hidden HTML form to gather browser information. If the user has compatible devices and can register at least one device, the flow progresses to the **Check Whether MFA Greetings Required To Be Displayed To User?** section.

* **Check Whether MFA Greetings Required To Be Displayed To User?**

  Uses a function node to check if the greeting page should be displayed.

  If the greeting should be displayed, an HTML node asks for user consent to add an MFA device. If the user clicks **Skip** or **Back**, the flow progresses to the **Return Success** section.

  If the user doesn't select **Skip** or **Back**, or if the greeting page isn't displayed, a function node checks whether the user's email is known:

  * If the user's email address isn't known, the flow progresses to the **User select device to register with** section.

  * If the user's email address is known, a function node checks whether direct enrollment of the user's email is requested:

    * If direct enrollment isn't requested, the flow progresses to the **User select device to register with** section.

    * If direct enrollment is requested, function nodes verify that the email address isn't in use and set the `canEnrollOnlyEmail` variable to true, then the flow progresses to the **Prepare to register OTP device** section.

* **User select device to register with**

  Presents the user with an HTML page that provides them with the available authentication method options:

  * If the user selects **Voice** or **SMS**, the flow progresses to the **User selected SMS/VOICE** section.

  * If the user selects **Email**, the flow progresses to the **User selected email** section.

  * If the user selects **TOTP**, the flow progresses to the **Prepare to register OTP device** section.

  * If the user selects **FIDO2**, the flow progresses to the **Register FIDO2 device and enable MFA for user** section.

  * If the user selects **Mobile**, the flow progresses to the **Mobile app registration flow** section.

  * If the user selects **Cancel**, a function node determines whether MFA is required:

    * If MFA is required, the flow progresses to the **Return Success** section with the `cancel` result.

    * If MFA isn't required, the flow progresses to the **Return Success** section with the `skip` result.

* **User Selected SMS/VOICE**

  Displays an HTML page gives the user the option to provide a voice or SMS number:

  * If the user enters a voice or SMS number, a function node verifies that the number isn't in use, then the flow progresses to the **Prepare to register OTP device** section.

  * If the user clicks **Cancel**, the flow returns to the **User select device to register with** section.

* **User Selected email**

  Uses a function node to check for a known user email.

  If the user's email isn't present, an HTML node lets the user enter an email and submit it or cancel.

  If the user clicks **Cancel**, the flow returns to the **User select device to register with** section.

  If the user submits an email, or if their email is already present, a function node verifies that the email isn't already registered. If the email isn't already registered, the flow progresses to the **Prepare to register OTP device** section. If the email is already registered, a function node determines the correct error message to display.

* **Prepare To Register OTP Device**

  Uses a PingOne node to create an OTP device.

  If the OTP device creation succeeds, a function node sets the device ID, then the flow progress to the **TOTP (Authenticator app) registration flow** section if the device type is TOTP, or to the **Ask for OTP** section if the device is SMS, voice, or email.

  If the OTP device creation fails, an error message displays.

* **Ask For OTP**

  Uses function nodes to begin tracking the number of resend attempts, mask the phone number or email, and determine the cancel behavior, then displays an HTML node prompting the user for the OTP.

  If the user submits a code, the flow progresses to the **Activate OTP device and enable MFA for user** section. Otherwise, the flow progresses to the **Resend OTP** section.

* **Resend OTP**

  If the user clicks **Resend** at the OTP prompt screen, function nodes increment the resend attempts and check if the maximum has been reached. If the maximum hasn't been reached, PingOne nodes delete the previous OTP device and create a new device, a function node updates the device ID, and a message displays for the user.

  If the user clicks **Cancel** at the OTP prompt screen, a PingOne node deletes the OTP device. A function node then redirects the flow based on the cancel button behavior. If this value is `Back`, the flow progresses to the **User select device to register with** section. If this value is `Skip`, the flow progresses to the **Return Success** section with the `Skip` result. If this value is `Cancel`, the flow progresses to the **Return Success** section with the `Cancel` result.

* **TOTP (Authenticator App) Registration Flow**

  Uses a function node to create a QR code for the key URL, then displays an HTML page on which the user can scan the QR code and enter a secret.

  If the user enters the secret, the flow progresses to the **Activate OTP device and enable MFA for user** section.

  If the user clicks **Cancel**, a PingOne node deletes the OTP device, and the flow returns to the **User select device to register with** section.

* **Activate OTP Device And Enable MFA For User**

  Uses a PingOne node to activate the OTP device. If the new device should be the default, a PingOne node sets it as the default, then another PingOne node updates the user's MFA status. The flow then progresses to the **Return Success** section.

* **Register FIDO2 Device And Enable MFA For User**

  Uses a PingOne node to create a FIDO2 device, then presents the user with an HTML registration page.

  If the user successfully registers the device, a PingOne node activates the device. If the new device should be the default, a PingOne node sets it as the default, then another PingOne node updates the user's MFA status. The flow then progresses to the **Return Success** section.

  If the user clicks **Cancel**, a PingOne node deletes the device and the flow returns to the **User select device to register with** section.

* **Mobile App Registration Flow**

  Uses a PingOne node to create a pairing key, then creates a QR code using the key. An HTML node then presents the QR code to the user.

  If the user clicks **Cancel**, a PingOne node deletes the pairing key and the flow returns to the **User select device to register with** section.

  A PingOne node reads the key, then a polling node determines when to proceed. If the polling status is claimed, a function node determines whether the user has any pre-registered devices. If the user has no pre-registered devices, a PingOne node activates MFA for the user and the flow progresses to the **Return Success** section.

  If the user has pre-registered devices, a function node determines whether the new device should be set as the default. If the new device should not be set as default, a PingOne node enables MFA for the user. If the new device should be the default, a PingOne node reads the user's mobile devices, a function node finds the device ID, and a PingOne node sets the device as default. A PingOne node then enables MFA for the user.

  If the polling fails, an error message displays, a PingOne node deletes the pairing key, and the flow returns to the **User select device to register with** section.

* **Return Success**

  Sends a success JSON response, indicating that the flow completed successfully.

* **Return Error**

  Uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input name                | Required | Description                                                                                                     |
| ------------------------- | -------- | --------------------------------------------------------------------------------------------------------------- |
| `email`                   | No       | The email address to use for registration.                                                                      |
| `p1UserId`                | Yes      | The user ID of the current user.                                                                                |
| `notShowMFAGreetingsPage` | No       | A Boolean indicating whether to show the user greetings page.                                                   |
| `allowOnlyEmail`          | No       | A Boolean indicating whether email should be the only permitted MFA device.                                     |
| `requireMFA`              | No       | A Boolean indicating whether MFA is required.                                                                   |
| `setNewDeviceAsDefault`   | No       | A Boolean indicating whether a newly added device should be set as the default device.                          |
| `allowedDeviceTypes`      | No       | A string containing any or all of `SMS, EMAIL, FIDO2, MOBILE, VOICE, TOTP` indicating the allowed device types. |
| `companyLogo`             | No       | The company logo.Used only when the main flow was launched using a redirect.                                    |
| `resendOtpLimit`          | Yes      | The maximum number of times the user can resend the OTP.                                                        |

## Output schema

This flow has the following outputs:

| Output name     | Description                                                |
| --------------- | ---------------------------------------------------------- |
| `subflowResult` | The result status of the flow.                             |
| `authMethod`    | The authentication method that was configured by the flow. |
| `errorMessage`  | The error message to display in the parent flow.           |
| `errorDetails`  | The details of the error that occurred in this flow.       |

## Variables and parameters

This flow uses the following variable or parameter values:

| Variable name        | Description                                                                 |
| -------------------- | --------------------------------------------------------------------------- |
| `canEnrollOnlyEmail` | A Boolean indicating whether email should be the only permitted MFA device. |
| `resendOtpAttempts`  | The number of times the user has resent the OTP.                            |
| `p1MFADeviceId`      | The device ID for the device being registered.                              |