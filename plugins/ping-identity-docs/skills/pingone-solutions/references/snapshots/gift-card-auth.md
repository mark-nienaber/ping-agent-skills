---
title: About Gift Card Redemption
description: The Gift Card Redemption solution lets you offer your end users a secure way to redeem gift cards, including step-up authentication and the ability for users to update their email address and other information, using a simple getting started experience and pre-built DaVinci flows.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:index
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/index.html
revdate: January 28, 2025
---

# About Gift Card Redemption

The Gift Card Redemption solution lets you offer your end users a secure way to redeem gift cards, including step-up authentication and the ability for users to update their email address and other information, using a simple getting started experience and pre-built DaVinci flows.

This flow pack enables robust threat detection against bots, disposable email, and adversary in the middle attacks. It also analyzes risk signals to detect high, medium, and low threats to reduce the risk of account takeovers leading to gift card fraud.

You can view additional information about the solution, including download links, in the marketplace. Learn more at [Gift Card Redemption on the Marketplace](https://marketplace.pingone.com/item/gift-card-fraud-detection-flow-pack).

Preparing the Gift Card Redemption solution involves configuration steps in PingOne and DaVinci:

* In PingOne, perform basic configuration to prepare the flows to be launched and enable features such as multi-factor authentication (MFA) and PingOne notifications.

* In DaVinci, configure variables and flow settings to customize the flow behavior for your environment and customers.

* Clone the flows for use in your production environment.

The Gift Card Redemption solution offers many of the available DaVinci capabilities. However, the solution limits the pre-built components to common use cases and selected best practices.

The solution includes a variety of authentication methods, such as email magic link, email and SMS OTP, FIDO2, voice, mobile applications, and Time-based One-Time Passwords (TOTPs).

|   |                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Gift Card Redemption solution offers pre-built flow templates and configurations. Review these components with your Ping Identity account representative to understand the limitations and risks associated with this solution. Your account representative can also help you customize the pre-built flow templates to satisfy any compliance or regulatory requirements that relate to your business. |

This solution uses PingOne and DaVinci. Learn more about managing users and other PingOne tasks in the [PingOne documentation](https://docs.pingidentity.com/pingone/p1_cloud__platform_main_landing_page.html). Learn more about customizing flows in the [DaVinci documentation](https://docs.pingidentity.com/davinci/davinci_landing_page.html).

---

---
title: Best Practices
description: These guidelines help you make effective use of the Gift Card Redemption solution in your environment.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:gift-card-best-practices
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/gift-card-best-practices.html
revdate: January 9, 2025
section_ids:
  select-a-user-journey-that-fits-your-users: Select a user journey that fits your users
  select-an-appropriate-flow-timeout: Select an appropriate flow timeout
  clone-your-flows-before-using-or-customizing-them: Clone your flows before using or customizing them
  use-caution-when-customizing-flows: Use caution when customizing flows
---

# Best Practices

These guidelines help you make effective use of the Gift Card Redemption solution in your environment.

## Select a user journey that fits your users

The Gift Card Redemption solution includes two user journey options, offer MFA or require MFA.

Offer MFA is appropriate for organizations who want to introduce multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* to users during registration as an option for additional security. Users who already have a registered MFA device should have their MFA attribute enabled in their user profile in PingOne. Use this option if you plan to or currently issue MFA to your users.

Require MFA is appropriate for organizations looking to enhance security during the registration and authentication event. Use this option if you're experiencing a high volume of password breaches or credential attacks.

## Select an appropriate flow timeout

When you're configuring your DaVinci flows, you can set a timeout value for the flow as a whole. Because the user's account could be updated later by anyone with access to the device, a flow with a very long or indefinite timeout could be a security risk. Set a value that minimizes that risk.

## Clone your flows before using or customizing them

Flows with the original name can be updated by PingOne when we publish flow updates. These updates are not applied automatically, but they add a new latest version to each flow.

By cloning the flows before you apply any customization or use them with customers, you prevent any of your changes or customizations from being overwritten accidentally.

## Use caution when customizing flows

If you want to customize the flows in the Gift Card Redemption solution, do so carefully.

Clone the flows before making customizations so that:

* You can revert to the earlier versions if you encounter breaking changes.

* If you download an updated version of the solution, you don't overwrite your customizations.

Test your customizations in a test environment before importing them into your production environment. Because any additional nodes or flows you add are not part of the standard solution, you must test them to make sure that they're working as you intend.

---

---
title: Configuring flows in DaVinci
description: After you configure PingOne and test the solution using the wizard, perform additional configuration in DaVinci to enable all features and make the flows available to end users.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:getting_started/gift_card_configuring_flows_in_davinci
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/getting_started/gift_card_configuring_flows_in_davinci.html
revdate: September 6, 2024
section_ids:
  steps: Steps
  example: Example:
  choose-from: Choose from:
  result: Result:
  result-2: Result:
  choose-from-2: Choose from:
---

# Configuring flows in DaVinci

After you configure PingOne and test the solution using the wizard, perform additional configuration in DaVinci to enable all features and make the flows available to end users.

## Steps

1. Enter or verify the values for each company variable that's used in the Gift Card Redemption solution.

   These variables determine whether some processes and subflows are included or excluded.

   |   |                                                                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you plan to invoke the flow using the widget, you can pass in parameter values that override some of these variables. These parameters are described later in this procedure. |

   1. In DaVinci, click the **Variables** tab.

   2. Locate a variable and click the **Pencil** icon.

   3. In the **Value** field, verify that the value is correct, or enter a new value for the variable.

   4. Click **Update**.

   5. Repeat steps b - d for each remaining variable.

      > **Collapse: Company variables**
      >
      > | Variable                      | Description                                                                                                                                                                                                                                                                                                                                                                            |
      > | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      > | `ciam_sessionLengthInMinute`  | The maximum allowed session length for a user in the flow\.The default value is 5 minutes.                                                                                                                                                                                                                                                                                             |
      > | `ciam_appleEnabled`           | A boolean that controls whether Apple is enabled as a social sign-on option.The default value is `true`.                                                                                                                                                                                                                                                                               |
      > | `ciam_facebookEnabled`        | A boolean that controls whether Facebook is enabled as a social sign-on option.The default value is `true`.                                                                                                                                                                                                                                                                            |
      > | `ciam_googleEnabled`          | A boolean that controls whether Google is enabled as a social sign-on option.The default value is `true`.                                                                                                                                                                                                                                                                              |
      > | `ciam_otpFallbackAllowed`     | A boolean indicating whether a user can fall back to a one-time passcode (OTP) *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)* if a mobile push request times out.The default value is `true`. |
      > | `ciam_endUserErrMsg`          | A string that is displayed to the user in an error message if an unexpected error occurs.The default value is `An error occurred`.                                                                                                                                                                                                                                                     |
      > | `ciam_requireMFA`             | A boolean that controls whether MFA is required for all users.The default value is `true`.                                                                                                                                                                                                                                                                                             |
      > | `ciam_resendOtpLimit`         | The maximum number of times a user can resend a one-time passcode.The default value is `5`.                                                                                                                                                                                                                                                                                            |
      > | `ciam_passwordlessRequired`   | A boolean that controls whether all end users must use passwordless authentication.The default value is `true`.                                                                                                                                                                                                                                                                        |
      > | `ciam_magicLinkEnabled`       | A boolean that controls whether magic links are enabled for your end users.The default value is `true`.                                                                                                                                                                                                                                                                                |
      > | `ciam_logoUrl`                | The URL for the version of your company logo to display in flows.The default value is `https://assets.pingone.com/ux/ui-library/5.0.2/images/logo-pingidentity.png`.                                                                                                                                                                                                                   |
      > | `ciam_logoStyle`              | The CSS style to use for your company logo.The default value is `width: 65px; height:65px;`.                                                                                                                                                                                                                                                                                           |
      > | `ciam_companyName`            | The name of your company as it should be displayed in user-facing text.The default value is `Ping Identity`.                                                                                                                                                                                                                                                                           |
      > | `ciam_agreementEnabled`       | A boolean that controls whether agreement is enabled in your environment.The default value is `true`.                                                                                                                                                                                                                                                                                  |
      > | `ciam_agreementId`            | The ID of the agreement to present to users if agreement is enabled.This value was copied in the [Configuring PingOne for the Gift Card Redemption solution](gift_card_configuring_p1.html) procedure. There is no default value.                                                                                                                                                      |
      > | `ciam_recoveryLimit`          | The maximum number of times a user can attempt to recover an account.The default value is `5`.                                                                                                                                                                                                                                                                                         |
      > | `ciam_verificationLimit`      | The maximum number of times a user can attempt to verify their email address.The default value is `5`.                                                                                                                                                                                                                                                                                 |
      > | `ciam_smsOtpEnabled`          | A boolean that controls whether OTP using SMS is enabled in your environment.The default value is `true`.                                                                                                                                                                                                                                                                              |
      > | `ciam_emailOtpEnabled`        | A boolean that controls whether OTP using email is enabled in your environment.The default value is `true`.                                                                                                                                                                                                                                                                            |
      > | `ciam_fidoPasskeyEnabled`     | A boolean that controls whether Fast IDentity Online (FIDO) *(tooltip: \<div class="paragraph">&#xA;\<p>A set of open technical specifications developed by the FIDO Alliance for strong authentication.\</p>&#xA;\</div>)* passkey is enabled in your environment.The default value is `true`.                                                                                        |
      > | `ciam_accountRecoveryEnabled` | A boolean that controls whether account recovery is enabled in your environment.The default value is `true`.                                                                                                                                                                                                                                                                           |

2. Verify the configuration of the following connectors in your environment:

   | Connector             | Description                                                                                                                                                                                                                                                                                        | Connector documentation                                                                                     |
   | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
   | PingOne               | Enables DaVinci to view and update PingOne user information.                                                                                                                                                                                                                                       | [PingOne Connector](https://docs.pingidentity.com/connectors/p1_connector.html)                             |
   | PingOne MFA           | Enables DaVinci to use the PingOne MFA service for multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">&#xA;\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>&#xA;\</div>)*. | [PingOne MFA Connector](https://docs.pingidentity.com/connectors/p1_mfa_connector.html)                     |
   | PingOne Notifications | Enables DaVinci flows to send users general communications using SMS, email, and voice message with PingOne's notifications feature.                                                                                                                                                               | [PingOne Notifications Connector](https://docs.pingidentity.com/connectors/p1_notifications_connector.html) |
   | PingOne Protect       | Enables DaVinci flows to perform a threat assessment of the current user through PingOne Protect.                                                                                                                                                                                                  | [PingOne Protect Connector](https://docs.pingidentity.com/connectors/p1_protect_connector.html)             |

   1. On the **Connectors** tab, find the connector that you want to verify and go to **…​ > Edit**.

   2. Verify that the **Environment ID**, **Client ID**, and **Region** field values match your PingOne values.

   3. (Optional) Copy the **Client Secret** from your PingOne environment to the **Client Secret** field.

   4. If you have made any changes to the values, click **Apply**.

   5. Repeat the previous steps for each remaining connector.

3. Configure the PingOne Authentication node.

   1. Click **Flows**.

   2. Select the **Gift Card Redemption - Update Email & Redeem Rewards - Main Flow** and go to **…​ > Edit**.

   3. In the **Return Success** section, click the **Return Success Response** node.

   4. Verify that the **PingOne Application** list is set to **Use Application ID**.

   5. Verify that your application ID is present in the **Application ID** field.

   6. Click **Apply**.

   7. Click **Save**.

4. If you want to use social sign-on, update the `skIdp` component in the **Gift Card Redemption - Update Email & Redeem Rewards - Main Flow** flow to use your PingOne identity provider (IdP) *(tooltip: \<div class="paragraph">
   \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
   \</div>)*.

   1. Click **Flows**.

   2. Select the **Gift Card Redemption - Update Email & Redeem Rewards - Main Flow** flow and go to **…​ > Edit**.

   3. Click the **Password Sign On Page** node.

   4. Click the `skIdp` component corresponding to a social IdP option that you want to provide.

      The section of the node contents that contains these components looks like this:

      ```json
      {{#if googleEnabled}}
           {{skIDP}}

      {{/if}}
      {{#if facebookEnabled}}
           {{skIDP}}
      {{/if}}
      {{#if appleEnabled}}
           {{skIDP}}
      {{/if}}
      ```

   5. In the **Identity Provider Connector** list, select **PingOne Authentication**.

   6. In the **PingOne External Identity Provider** list, select an external IdP.

   7. Select **Link with PingOne User**.

   8. In the **PingOne Population** list, select **Default**.

   9. Click **Save**.

   10. Click **Apply**.

   11. Repeat steps d - j for each additional social IdP option that you want to use.

5. Verify or add values for the **Agreement ID** and **MFA Policy ID**.

   1. Click **Flows**.

   2. Select the **Gift Card Redemption - Update Email & Redeem Rewards - Main Flow** flow and go to **…​ > Edit**.

   3. Click the **Initialize Or Set Flow Variables** node.

   4. For the `ciam_agreementID` variable value, enter the **Agreement ID** value that you copied in [Configuring PingOne for the Gift Card Redemption solution](gift_card_configuring_p1.html) if it's not already present.

      |   |                                                                                    |
      | - | ---------------------------------------------------------------------------------- |
      |   | If your environment has only one agreement, this value is automatically populated. |

   5. For the `ciam_mfaPolicyID` variable value, enter the MFA policy ID that you want to use.

      |   |                                                                   |
      | - | ----------------------------------------------------------------- |
      |   | If you do not enter an MFA policy ID, the default policy is used. |

   6. Click **Apply**.

   7. Click **Save**.

6. Verify or add a value for the **Risk Policy ID**.

   1. Click **Flows**.

   2. Select the **Gift Card Redemption - Update Email & Redeem Rewards - Main Flow** flow and go to **…​ > Edit**.

   3. Click the **Set Flow Constants** node.

   4. For the `riskPolicyID` variable value, enter the MFA policy ID that you want to use.

      |   |                                                                   |
      | - | ----------------------------------------------------------------- |
      |   | If you do not enter a risk policy ID, the default policy is used. |

   5. Click **Apply**.

   6. Click **Save**.

7. If you want to launch the solution using the widget, add your company name:

   1. Click **Flows**.

   2. Select the **Gift Card Redemption - Update Email & Redeem Rewards - Main Flow** flow and go to **…​ > Edit**.

   3. Click the **Set Industry Variables** node.

   4. In the **Code** section, update the text to include your company name.

      ### Example:

      ```
           const flowCompanyGreeting = (flowMethod === 'WIDGET' )
                ? '<p class="text-muted text-center mb-5">Welcome to  Company Name</p>'
                : <p class="text-muted text-center">Welcome to ${ciam_companyName}</p>;
      ```

   5. Click **Apply**.

8. Verify that the PingOne flow setting is correct for your environment.

   ### Choose from:

   * If you want to launch the Gift Card Redemption solution using a redirect, the flow must be configured as a PingOne flow.

     1. Click **Flows**.

     2. Click the **Gift Card Redemption - Update Email & Redeem Rewards - Main Flow** flow.

     3. Go to **More Options ( [icon: ellipsis-v, set=fa]) → Flow Settings**.

     4. Enable the **PingOne Flow** toggle if it's not already enabled.

     5. If you made changes to the flow settings, click **Save**, close the flow settings pane, and click **Deploy**.

   * If you want to launch the Gift Card Redemption solution using the widget, the flow must not be configured as a PingOne flow.

     1. Click **Flows**.

     2. Click the **Gift Card Redemption - Update Email & Redeem Rewards - Main Flow** flow.

     3. Go to **More Options ( [icon: ellipsis-v, set=fa]) → Flow Settings**.

     4. Disable the **PingOne Flow** toggle if it's not already disabled.

     5. If you made changes to the flow settings, click **Save**, close the flow settings pane, and click **Deploy**.

9. Configure DaVinci applications that invoke the **Gift Card Redemption - Update Email & Redeem Rewards - Main Flow** and **Gift Card Redemption - Account Recovery - Main Flow** flows.

   Learn more in [Creating an application](https://docs.pingidentity.com/davinci/applications/davinci_creating_an_application.html) and [Configuring a flow policy](https://docs.pingidentity.com/davinci/applications/davinci_configuring_a_flow_policy.html) in the DaVinci documentation.

   1. On the **Applications** tab, click **Add Application**.

   2. In the **Name** field, enter a name for the application.

   3. Click **Create**.

   4. On the **Applications** tab, find the application that you created and click **Edit**.

   5. On the **Flow Policy** tab, click **Add Flow Policy**.

   6. In the **Name** field, enter a name for the flow policy.

   7. Select **PingOne Flow Policy** if you plan to invoke the flow using a PingOne redirect.

   8. In the **Flows** section, select one of the following flows:

      * **Gift Card Redemption - Update Email & Redeem Rewards - Main Flow**: This flow is the entry point for the solution as a whole.

      * **Gift Card Redemption - Account Recovery - Main Flow**: This flow is used when a user attempts to recover an account and can be included in the **Account Disabled** notification template.

   9. In the **Version** section, select one or more versions of the flow to use.

   10. Click **Next**.

   11. In the **Distribution** field, set the weight for the selected flow to `100`.

   12. Click **Create Flow Policy**.

   13. Click **Apply**.

   14. Repeat steps a - m for the remaining main flow.

10. If you are using a test environment, move the flows to your production environment:

    1. In your testing environment, click **Flows**.

    2. Click the **Gift Card Redemption - Update Email & Redeem Rewards - Main Flow** flow.

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

    9. Repeat steps a - h for the Gift Card Redemption - Account Recovery - Main Flow flow.

    10. Repeat the previous steps in your production environment.

11. Invoke the flow or flows using the widget or a redirect.

    ### Choose from:

    * If you want to launch the flow in a separate window using a PingOne redirect, use the procedure in [Launching a PingOne flow with a redirect](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launch_flow_redirect.html) in the DaVinci documentation. The Gift Card Redemption - Update Email & Redeem Rewards - Main Flow flow can be launched with a redirect.

    * If you want to launch the flow in a widget within the user's current window, use the procedure in [Launching a flow with the widget](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launching_a_flow_with_the_widget.html) in the DaVinci documentation. The following flows can be launched with the widget:

      * Gift Card Redemption - Update Email & Redeem Rewards - Main Flow

      * Gift Card Redemption - Account Recovery - Main Flow

      |   |                                                                                                                                                                                                                                                         |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | When you invoke the flow using the widget, you must include your company logo as a background image in the `dialog-content-header__logo` CSS class. For example:```
      .dialog-content-header__logo {
        background-image: url("./company-logo.svg");
      }
      ``` |

      |   |                                                                                                                                                                                                                                                                                                                         |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | When you invoke the flow using the widget, you can include any of the following parameters. When present, the parameter value is used instead of the corresponding variable value.Use the following format to pass parameters to the flow:```
      flowParameters:{
           parameter1: "value",
           parameter2: "value"
      }
      ``` |

      > **Collapse: Parameters**
      >
      > | Parameter                  | Corresponding variable        | Description                                                                                |
      > | -------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------ |
      > | `isAppleEnabled`           | `ciam_appleEnabled`           | A boolean indicating whether Apple is enabled as a social sign-on option.                  |
      > | `isFacebookEnabled`        | `ciam_facebookEnabled`        | A boolean indicating whether Facebook is enabled as a social sign-on option.               |
      > | `isGoogleEnabled`          | `ciam_googleEnabled`          | A boolean indicating whether Google is enabled as a social sign-on option.                 |
      > | `isPasswordlessRequired`   | `ciam_passwordlessRequired`   | A boolean indicating whether all end users must use passwordless authentication.           |
      > | `isEmailMagicLinkEnabled`  | `ciam_magicLinkEnabled`       | A boolean indicating whether magic links are enabled for your end users.                   |
      > | `isTermsOfServiceEnabled`  | `ciam_agreementEnabled`       | A boolean indicating whether agreement is enabled in your environment.                     |
      > | `isSmsOTPEnabled`          | `ciam_smsOtpEnabled`          | A boolean indicating whether one-time passcode using SMS is enabled in your environment.   |
      > | `isEmailOTPEnabled`        | `ciam_emailOtpEnabled`        | A boolean indicating whether one-time passcode using email is enabled in your environment. |
      > | `isFidoPasskeyEnabled`     | `ciam_fidoPasskeyEnabled`     | A boolean indicating whether FIDO passkey is enabled in your environment.                  |
      > | `isAccountRecoveryEnabled` | `ciam_accountRecoveryEnabled` | A boolean indicating whether account recovery is enabled in your environment.              |

---

---
title: Configuring PingOne for the Gift Card Redemption solution
description: Verify that your PingOne environment has the necessary configuration to run the Gift Card Redemption solution and enable all the features that you want to use.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:getting_started/gift_card_configuring_p1
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/getting_started/gift_card_configuring_p1.html
revdate: September 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring PingOne for the Gift Card Redemption solution

Verify that your PingOne environment has the necessary configuration to run the Gift Card Redemption solution and enable all the features that you want to use.

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

2. Create or verify the required notification templates in your PingOne environment.

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

      | Notification Template       | Subject                                     |
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

3. Update the content of the existing **New Device Paired** notification template.

   1. Open the [New Device Paired](https://library.pingidentity.com/page/ciam-plus-new-device-paired-notification-template) template entry in the Ping Library.

   2. Click **Copy** to copy the template HTML.

   3. In PingOne, go to **User Experience > Notification Templates**.

   4. Find the **New Device Paired** notification template and click **⋮ > Edit**.

   5. In the **New Email** field, click the **\*Pencil** icon, then paste the template HTML you copied in step b.

   6. Click the **Save** icon to save the field changes.

   7. Click the **X** icon to close the template.

4. Verify that you have a multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
   \<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
   \</div>)* policy configured in PingOne.

   Learn more in the PingOne [MFA policies](https://docs.pingidentity.com/pingone/authentication/p1_mfa_policies.html) documentation.

   1. In PingOne, go to **Authentication → MFA**.

   2. Click the MFA policy marked as the default and verify that its **Allowed Authentication Methods** include the authentication methods that you want to use from the following:

      * **Email**

      * **SMS**

      * **FIDO2**

      * **Voice**

      * **TOTP**

      * **Mobile**

5. Verify that the default population exists:

   1. Go to **Directory → Populations**.

   2. In the list of populations, verify that a population is marked as **Default**.

   3. If no existing population is marked as **Default**, select a population and go to **More options ( [icon: ellipsis-v, set=fa]) → Edit Population**.

   4. Click **Make Default Population**.

   5. Click **Switch**.

   6. Click **Save**.

6. Add the **rewardsBalance** attribute.

   |   |                                                                                                                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The **rewardsCurrency** and **rewardsBalance** attributes are displayed concatenated with each other. For example, if the `rewardsBalance` is `500.00` and the `rewardsCurrency` is `$`, they are displayed as `$500.00`. |

   1. Go to **Directory > User Attributes**.

   2. Click the [icon: plus, set=fa]icon.

   3. Click **Declared**.

   4. Click **Next**.

   5. Enter the information for the attribute:

      * **Name:** `rewardsBalance`

      * **Display name:** `rewardsBalance`

      * **Description:** `The user's current rewards balance`.

   6. Click **Save**.

7. Add the **rewardsCurrency** attribute.

   1. Go to **Directory > User Attributes**.

   2. Click the [icon: plus, set=fa]icon.

   3. Click **Declared**.

   4. Click **Next**.

   5. Enter the information for the attribute:

      * **Name:** `rewardsCurrency`

      * **Display name:** `rewardsCurrency`

      * **Description:** `The currency of the user's rewards balance`.

   6. Click **Save**.

8. (Optional) If you plan to use FIDO2, verify that the default **Passkeys** policy is selected.

   Learn more about FIDO policies in the [PingOne FIDO policies](https://docs.pingidentity.com/pingone/authentication/p1_fido_policies.html) documentation.

   1. Go to **Authentication > FIDO**.

   2. Verify that the **Passkeys** policy is set as the default.

   3. If the **Passkeys** policy is not the default, go to **⋮ > Make Default**, then click **Save**.

9. (Optional) If you plan to use an agreement, verify that you have an agreement configured in PingOne and copy the agreement ID.

   Learn more about configuring agreements in [Adding an agreement](https://docs.pingidentity.com/pingone/user_experience/p1_add_an_agreement.html) in the PingOne documentation.

   1. Go to **User Experience > Agreements**.

   2. Verify that the agreement exists and is enabled.

   3. Click the agreement to open the details panel.

   4. On the **API** tab, copy the **ID**.

   The agreement ID is used in a later procedure to configure the flows in DaVinci.

10. (Optional) Verify that you have an external identity provider (IdP) configured in PingOne for each valid third party you want to use as a social sign-on option.

    Learn more about how IdPs are used in PingOne in [Identity Providers](https://docs.pingidentity.com/pingone/integrations/p1_external_idps.html) in the PingOne documentation.

    1. If you want to use Google as a social sign-on option, verify that Google is configured as an IdP according to the procedure in [Adding an identity provider - Google](https://docs.pingidentity.com/pingone/integrations/p1_addidentityprovidergoogle.html). During configuration, use the following property mappings:

       | Google Property | PingOne Property |
       | --------------- | ---------------- |
       | `email address` | `username`       |
       | `email address` | `email`          |
       | `family name`   | `family name`    |
       | `given name`    | `given name`     |

    2. If you want to use Facebook as a social sign-on option, verify that Facebook is configured as an IdP according to the procedure in [Adding an identity provider - Facebook](https://docs.pingidentity.com/pingone/integrations/p1_addidentityproviderfacebook.html). During configuration, use the following property mappings:

       | Facebook Property | PingOne Property |
       | ----------------- | ---------------- |
       | `email address`   | `username`       |
       | `email address`   | `email`          |
       | `family name`     | `family name`    |
       | `given name`      | `given name`     |

    3. If you want to use Apple as a social sign-on option, verify that Apple is configured as an IdP according to the procedure in [Adding an identity provider - Apple](https://docs.pingidentity.com/pingone/integrations/p1_add_idp_apple_prereqs.html). During configuration, use the following property mappings:

       | Apple Property  | PingOne Property |
       | --------------- | ---------------- |
       | `email address` | `username`       |
       | `email address` | `email`          |

---

---
title: Flow Reference
description: The Gift Card Redemption solution uses a main flow and multiple subflows. This section explains what each flow does and how it works.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:flow_reference/gift-card-flow-reference
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/flow_reference/gift-card-flow-reference.html
revdate: January 29, 2025
page_aliases: ["flow_reference/index.adoc"]
---

# Flow Reference

The Gift Card Redemption solution uses a main flow and multiple subflows. This section explains what each flow does and how it works.

A DaVinci flow consists of nodes, each of which presents a page to the user, performs a backend action, or launches another flow. These nodes are connected by logical operators, allowing you to construct a user journey.

The flows included in the Gift Card Redemption solution are designed to work together to provide the solution, and they require no configuration beyond that described in the [Configuring flows in DaVinci](../getting_started/gift_card_configuring_flows_in_davinci.html) document. However, you can customize these flows to provide additional services to your end users. Learn more in [How To Manage Flows](https://docs.pingidentity.com/davinci/flows/davinci_how_to_manage_existing_flows.html) in the DaVinci documentation.

The main section of the Gift Card Redemption solution contains the following flows:

* [Gift Card Redemption - Update Email & Redeem Rewards - Main Flow](gift_card_update_email_redeem_rewards_main_flow.html)

  This flow is the beginning of the gift card redemption process. It is meant to be invoked directly.

* [Gift Card Redemption - Account Recovery - Email - Subflow](gift_card_account_recovery_email_subflow.html)

  This flow lets users regain account access.

* [Gift Card Redemption - Account Recovery - Main Flow](gift_card_account_recovery_main_flow.html)

  This flow lets users regain account access.

* [Gift Card Redemption - Account Registration - Subflow](gift_card_account_registration_subflow.html)

  This flow lets users register a new account.

* [Gift Card Redemption - Agreement (ToS) - Subflow](gift_card_agreement_tos_subflow.html)

  This flow lets users read and agree to any agreements required by the environment.

* [Gift Card Redemption - Change Password - Subflow](gift_card_change_password_subflow.html)

  This flow lets users change their password.

* [Gift Card Redemption - Device Authentication - Subflow](gift_card_device_authentication_subflow.html)

  This flow lets users authenticate using a known device.

* [Gift Card Redemption - Device Registration - Subflow](gift_card_device_registration_subflow.html)

  This flow lets users register a new device.

* [Gift Card Redemption - Magic Link Authentication - Subflow](gift_card_magic_link_authentication_subflow.html)

  This flow lets users authenticate using a magic link.

* [Gift Card Redemption - SignOn - Subflow](gift_card_signon_subflow.html)

  This flow lets users sign on.

* [Gift Card Redemption - Threat Detection - Subflow](gift_card_threat_detection_subflow.html)

  This flow uses PingOne Protect to perform a threat assessment of the user.

* [Gift Card Redemption - Verify Email - Subflow](gift_card_verify_email_subflow.html)

  This flow lets users verify their email address using PingOne SSO.

---

---
title: Getting Started
description: There are two configuration stages for the Gift Card Redemption solution.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:getting_started/gift_card_getting_started
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/getting_started/gift_card_getting_started.html
revdate: June 28, 2024
page_aliases: ["getting_started/index.adoc"]
---

# Getting Started

There are two configuration stages for the Gift Card Redemption solution.

To get started with the solution:

1. [Configure the settings in PingOne](gift_card_configuring_p1.html).

2. [Perform additional configuration in DaVinci to begin using the solution](gift_card_configuring_flows_in_davinci.html).

---

---
title: Gift Card Redemption - Account Recovery - Email - Subflow
description: The Gift Card Redemption - Account Recovery - Email - Subflow lets users recover a lost account using an email address.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:flow_reference/gift_card_account_recovery_email_subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/flow_reference/gift_card_account_recovery_email_subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables: Variables
---

# Gift Card Redemption - Account Recovery - Email - Subflow

The **Gift Card Redemption - Account Recovery - Email - Subflow** lets users recover a lost account using an email address.

## Purpose

The **Gift Card Redemption - Account Recovery - Email - Subflow** presents users who have forgotten their password with the ability to reset it using their email address. Users provide and verify their email address. The flow provides a form for the user to enter a new password, then verifies and saves the new password.

## Structure

This flow is divided into sections using teleport nodes:

* **Forgot Password Form**

  Initializes the variables used in the flow, then presents a custom HTML form on which users can enter their account's email address. When the user clicks **Submit**, the flow progresses to the **Do Protect Analysis & Send Recovery Code If Applicable** section.

* **Do Protect Analysis & Send Recovery Code If Applicable**

  The flow progresses to the **Threat Detection And Mitigation** section. When this section completes, the flow uses a PingOne node to find a user with the specified email address. If the user is found and has a password, PingOne nodes enable the user and send a recovery code, and the flow progresses to the **Recovery Code Form** section.

* **Recovery Code Form**

  Uses a function node to check if the user's account is enabled and a PingOne node to disable the account if it is enabled. A flow instance variable node then begins tracking the number of recovery attempts, and an HTTP node presents the user with a new password reset form.

  * If the user clicks **Submit**, the flow progresses to the **Verify Password** section.

  * If the user clicks **Cancel**, the flow progresses to the **Forgot Password Form** section.

  * If the user clicks **Resend**, the flow progresses to the **Resend Recovery Code** section.

* **Verify Password**

  Uses function nodes to verify that the new password and the confirmed password match and to validate the new password. If either condition isn't met, it displays an error message. The flow then uses a function node to increment the number of validation attempts and progresses to the **Update Password and Show Success Message** section.

* **Update Password And Show Success Message**

  The number of recovery attempts is compared to the maximum. If it doesn't exceed the maximum, PingOne nodes enable the user and save the new password.

  If the new password isn't set correctly, a PingOne node disables the user if not already disabled. Function nodes prepare the error details, then an error message displays.

  If the new password is set correctly, a PingOne node notifies the user and a success message displays. The flow then progresses to the **Return Success** section.

* **Resend Recovery Code**

  The number of resend attempts is incremented by one and compared to the maximum. If it does not exceed the maximum, a PingOne node sends a new recovery code. A confirmation message is then displayed.

* **Threat Detection And Mitigation**

  Uses a function node to check whether PingOne Protect analysis is required.

  If PingOne Protect analysis isn't required, the flow returns to the **Do Protect Analysis & Send Recovery Code If Applicable** section.

  If PingOne Protect analysis is required, the flow uses a PingOne node to look up the user, then invokes the **Gift Card Redemption - Threat Detection - Subflow**.

  If the **Gift Card Redemption - Threat Detection - Subflow** completes successfully, a function node stores the risk evaluation as a variable, then a second function node branches the flow based on the risk level:

  * If the risk level is low or medium, the flow returns to the previous section.

  * If the risk level is high, function nodes check if the PingOne user ID is empty or if the high risk was the result of a new device. If neither condition is true, PingOne node notifies the user of the suspicious activity. Regardless of conditions, an error message is then displayed.

  If the **Gift Card Redemption - Threat Detection - Subflow** completes unsuccessfully, an error message displays.

* **Return Success**

  Sends a success JSON response, indicating that the flow completed successfully. A function node also checks whether the risk evaluation ID is empty and uses a PingOne node to update the risk evaluation if the ID is present.

* **Return Error**

  Uses a function node to enrich the error details and sends an error JSON response, indicating that the flow completed unsuccessfully. A function node also checks whether the risk evaluation ID is empty and uses a PingOne node to update the risk evaluation if the ID is present.

## Input schema

This flow has the following inputs:

| Input Name            | Required? | Description                                                                                                                                                                                                                                                                                                      |
| --------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `companyLogo`         | No        | The company logo.Used only when the main flow was launched using the widget.                                                                                                                                                                                                                                     |
| `protectriskPolicyId` | No        | The ID of the PingOne Protect risk policy to use in the flow.                                                                                                                                                                                                                                                    |
| `username`            | No        | The username of the account being recovered.                                                                                                                                                                                                                                                                     |
| `resendOtpLimit`      | Yes       | The maximum number of times a user can resend a one-time passcode (OTP) *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)*. |
| `recoveryLimit`       | Yes       | The maximum number of times a user can attempt to recover an account.                                                                                                                                                                                                                                            |
| `hideBackButton`      | No        | Indicates whether to hide the back button on the **Forgot Password** form.                                                                                                                                                                                                                                       |

## Output schema

This flow has the following outputs:

| Output Name     | Description                                                |
| --------------- | ---------------------------------------------------------- |
| `p1UserId`      | The user ID of the current user.                           |
| `subflowResult` | The result status of the flow.                             |
| `authMethod`    | The authentication method that was configured by the flow. |
| `errorMessage`  | The error message to display in the parent flow.           |
| `errorDetails`  | The details of the error that occurred in this flow.       |

## Variables

This flow uses the following variables:

| Variable Name                | Description                                                    |
| ---------------------------- | -------------------------------------------------------------- |
| `resendOtpAttempts`          | The number of times the user has resent an OTP.                |
| `recoveryValidationAttempts` | The number of times the user has attempted account validation. |
| `protectRiskEvalId`          | The risk ID of the current user returned by PingOne Protect.   |

---

---
title: Gift Card Redemption - Account Recovery - Main Flow
description: The Gift Card Redemption - Account Recovery - Main Flow lets users recover a lost account using the Gift Card Redemption - Account Recovery - Email - Subflow.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:flow_reference/gift_card_account_recovery_main_flow
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/flow_reference/gift_card_account_recovery_main_flow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Gift Card Redemption - Account Recovery - Main Flow

The **Gift Card Redemption - Account Recovery - Main Flow** lets users recover a lost account using the **Gift Card Redemption - Account Recovery - Email - Subflow**.

## Purpose

The **Gift Card Redemption - Account Recovery - Main Flow** lets users recover a lost account by invoking the **Gift Card Redemption - Account Recovery - Email - Subflow**, then directs the user to the **Gift Card Redemption - SignOn - Subflow**.

## Structure

This flow is divided into sections using teleport nodes:

* **Flow Configuration**

  Uses function nodes to set variables, then progresses to the **Call For Account Recovery Sub-Flow And Offer Sign On Page** section.

* **Call For Account Recovery Sub-Flow And Offer Sign On Page**

  A function node confirms that account recovery is enabled, then a second function node checks whether the user can skip email recovery code verification.

  If the user can skip email recovery code verification, the flow progresses to the **Reset Password, Enable Account And Send User To SignOn Page** section.

  If the user can't skip email recovery code verification, a hidden HTML node activates relevant CSS files. The flow then invokes the **Gift Card Redemption - Account Recovery - Email - Subflow**, followed by the **Gift Card Redemption - SignOn - Subflow**. A PingOne node creates a session for the user and a confirmation page is displayed. The flow then progresses to the **Return Success** section.

* **Reset Password, Enable Account And Send User To SignOn Page**

  Uses a PingOne node to find the user. A function node sets the number of validation attempts to zero, then presents the user with an HTTP password reset form.

  If the user submits a new password, function nodes validate the new password and verify that the password and confirmed password match. A function node then increments the number of validation attempts. If the maximum number of validation attempts hasn't been met, PingOne nodes enable the user and set the new password.

  If the new password setting fails, a PingOne node disables the user. Function nodes prepare an error message, which is then presented to the user.

  If the new password setting succeeds, a PingOne notification node notifies the user of the new password and a success message is presented to the user. If the user clicks `Sign On`, the **Gift Card Redemption - SignOn - Subflow** is invoked. When the subflow completes, a PingOne authentication node creates a session, and a success message is displayed.

* **Return Success**

  Sends a success JSON response, indicating that the flow completed successfully.

* **Return Error**

  Sends an error JSON response, indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs.

| Input name                            | Required | Description                                                                                                                                                                                   |
| ------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `flowParameters`                      | No       | An object containing parameters from the parent flow.                                                                                                                                         |
| `canUserSkipRecoveryCodeVerification` | No       | Determines whether the user can reset their password without verifying their email with a recovery code. This value is only used if email verification is not required to reset the password. |
| `p1UserId`                            | No       | The PingOne ID of the user.                                                                                                                                                                   |

## Output schema

This flow has no outputs.

## Variables and parameters

This flow uses the following variable or parameter values:

| Variable name                 | Parameter name | Description                                                                                                                                                                                                                                                                                                      |
| ----------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ciam_logoStyle`              | None           | The HTML style to use for your company logo.This value is only used when the flow is launched with a redirect.                                                                                                                                                                                                   |
| `ciam_resendOtpLimit`         | None           | The maximum number of times a user can resend a one-time passcode (OTP) *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)*. |
| `ciam_recoveryLimit`          | None           | The maximum number of times a user can attempt to recover an account.                                                                                                                                                                                                                                            |
| `ciam_logoUrl`                | None           | The URL for your company logo.This value is only used when the flow is launched with a redirect.                                                                                                                                                                                                                 |
| `ciam_companyName`            | None           | Displays the name of your company.This value is only used when the flow is launched with a redirect.                                                                                                                                                                                                             |
| `ciam_accountRecoveryEnabled` | None           | Indicates whether account recovery is enabled.                                                                                                                                                                                                                                                                   |
| `p1RiskPolicyIdAuthZ`         | None           | The PingOne risk policy ID to use for authorization.                                                                                                                                                                                                                                                             |
| `p1RiskPolicyIdAuthn`         | None           | The PingOne risk policy ID to use for authentication.                                                                                                                                                                                                                                                            |
| `p1RiskPolicyIdReg`           | None           | The PingOne risk policy ID to use for registration.                                                                                                                                                                                                                                                              |
| `p1RiskPolicyIdAR`            | None           | The PingOne risk policy ID to use for account recovery.                                                                                                                                                                                                                                                          |
| `p1MFAPolicyId`               | None           | The ID of the PingOne MFA policy to use in the flow.                                                                                                                                                                                                                                                             |
| `flowCompanyLogo`             | None           | The URL for your company logo.                                                                                                                                                                                                                                                                                   |
| `p1AgreementId`               | None           | The ID of the agreement to present to users.                                                                                                                                                                                                                                                                     |

---

---
title: Gift Card Redemption - Account Registration - Subflow
description: The Gift Card Redemption - Account Registration - Subflow lets users register a new account.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:flow_reference/gift_card_account_registration_subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/flow_reference/gift_card_account_registration_subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Gift Card Redemption - Account Registration - Subflow

The **Gift Card Redemption - Account Registration - Subflow** lets users register a new account.

## Purpose

The **Gift Card Redemption - Account Registration - Subflow** presents users with the ability to create a new account. Depending on your environment's properties, the flow can let a user create a password, add a multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* device using the **Gift Card Redemption - Device Registration - Subflow** flow, and view and consent to an agreement.

## Structure

This flow is divided into sections using teleport nodes:

* **Fetch User Details for Registration**

  Uses function nodes to set flow instance variables and check whether agreement is enabled. If agreement is enabled, a PingOne node reads the agreement content. The flow then presents users with an HTML form on which to enter their email address.

  If the user clicks **Sign On**, the flow progresses to the **Return Success** section.

  If the user clicks **Register**, the flow progresses to the **PingOne Protect Threat Detection And Mitigation**. When this section completes, a PingOne node verifies that the email address is not already in use, then a function node checks whether the user consented to the agreement if one is in use. If the user consented to the agreement or no agreement is in use, an HTML form lets the user enter a first and last name and click **Register** or **Back**.

  If the user clicks **Register**, a second HTML form lets the user enter and confirm a password. The flow then progresses to the **Create Account** section.

  If the user clicks **Back**, the flow returns to the email address form.

* **PingOne Protect Threat Detection And Mitigation**

  If PingOne Protect analysis is required, uses a PingOne node to look up the user, then invokes the **Gift Card Redemption - Threat Detection - Subflow** subflow.

  If the **Gift Card Redemption - Threat Detection - Subflow** subflow completes successfully, the PingOne Protect values are saved as variables.

  A function node then examines the risk score.

  * If the risk score is low or medium, the flow returns to the **Fetch User Details for Registration** section.

  * If the risk score is high, a PingOne node updates PingOne Protect with the failed evaluation and an error message is displayed.

  If the **Gift Card Redemption - Threat Detection - Subflow** subflow does not complete successfully, an error message is displayed.

* **Validate Password & Create Account**

  Uses a function node to process the user's selection on the password form. If the user clicks **Back**, the flow returns to the name entry page. If the user clicks **Register**, function nodes verify that the password is valid and matches the confirmed password, then a PingOne node creates the new account. The flow then progresses to the **Accept Agreement and Verify Email** section.

* **Accept Agreement and Verify Email**

  Uses a function node to check whether an agreement is enabled. If an agreement is enabled, a PingOne updates the user's information to include their consent to the agreement. The flow then invokes the **Gift Card Redemption - Verify Email - Subflow** flow to ensure that the user's email address is verified, then progresses to the **Auto enroll email as a MFA device** section.

* **Auto enroll email as a MFA device**

  Uses PingOne nodes to enroll the user's email as an MFA device and enable MFA for the user. The flow then progresses to the **Return Success** section.

* **Return Success**

  Uses a PingOne node to update the risk evaluation if the risk evaluation ID is available and sends a success JSON response indicating that the flow completed successfully.

* **Return Error**

  Uses a PingOne node to update the risk evaluation if the risk evaluation ID is available and sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs.

| Input name                  | Required | Description                                                                                                                                                                                                                                                                                              |
| --------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `email`                     | No       | The user's email address.                                                                                                                                                                                                                                                                                |
| `agreementEnabled`          | No       | Indicates whether agreement is enabled for user registration.                                                                                                                                                                                                                                            |
| `agreementId`               | No       | The ID of the agreement to present to users.                                                                                                                                                                                                                                                             |
| `socialRegistrationEnabled` | No       | A boolean indicating whether registration through a third-party authentication is enabled.                                                                                                                                                                                                               |
| `googleEnabled`             | No       | A boolean indicating whether authentication through Google is enabled in your environment.                                                                                                                                                                                                               |
| `facebookEnabled`           | No       | A boolean indicating whether authentication through Facebook is enabled in your environment.                                                                                                                                                                                                             |
| `appleEnabled`              | No       | A boolean indicating whether authentication through Apple is enabled in your environment.                                                                                                                                                                                                                |
| `companyLogo`               | No       | The company logo.Used only when the main flow was launched using a redirect.                                                                                                                                                                                                                             |
| `protectRiskPolicyId`       | No       | The PingOne Protect risk policy ID to use. If not specified, the default policy is used.                                                                                                                                                                                                                 |
| `verificationLimit`         | No       | The number of times a user can attempt verification.                                                                                                                                                                                                                                                     |
| `resendOtpLimit`            | No       | The number of times a user can resend a one-time passcode (OTP) *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)*. |

## Output schema

This flow has the following outputs.

| Output name       | Description                                                                               |
| ----------------- | ----------------------------------------------------------------------------------------- |
| `subflowResult`   | The result status of the flow.                                                            |
| `p1UserId`        | The user ID of the current user.                                                          |
| `authMethod`      | The authentication method chosen by the user.                                             |
| `isSocialIDpAuth` | A boolean that indicates whether the user signed on using social identity provider (IdP). |
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
title: Gift Card Redemption - Agreement (ToS) - Subflow
description: The Gift Card Redemption - Agreement (ToS) - Subflow lets users read and confirm any agreement required in your environment.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:flow_reference/gift_card_agreement_tos_subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/flow_reference/gift_card_agreement_tos_subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Gift Card Redemption - Agreement (ToS) - Subflow

The **Gift Card Redemption - Agreement (ToS) - Subflow** lets users read and confirm any agreement required in your environment.

## Purpose

The **Gift Card Redemption - Agreement (ToS) - Subflow** determines whether the user needs to consent to an agreement. If so, it displays the agreement for the user and stores the user's consent if they consent to the agreement.

## Structure

This flow is divided into sections using teleport nodes:

* **Check if agreement form needs to be displayed**

  Uses comparison nodes to check if agreement is enabled in the environment and if agreement is necessary for the current user. If so, a PingOne node checks the user's consent status.

  If consent isn't present, the flow progresses to the **Present & Accept Agreement** section.

  If consent is present, a function node checks if a success message should be displayed. The flow progresses to the **Present & Accept Agreement** if a success message should be displayed, and to the **Return Success** section if a success message should not be displayed.

* **Present & Accept Agreement**

  Uses a PingOne node to retrieve the required agreement, then presents the user with an HTML page. If the user has not yet agreed, this page lets them review and accept or decline the agreemnt. If the user has agreed, the form displays a success message.

  If the user accepts the agreement, a PingOne node stores the user's agreement. The flow then returns to the beginning of the **Present & Accept Agreement** section if a success message should be displayed, and to the **Return Success** section if a success message should not be displayed.

  If the user declines the agreement, an error message displays.

* **Return Success**

  Sends a success JSON response, indicating that the flow has completed successfully.

* **Return Error**

  Uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs.

| Input name           | Required | Description                                                                                   |
| -------------------- | -------- | --------------------------------------------------------------------------------------------- |
| `p1UserId`           | Yes      | The current user's PingOne user ID.                                                           |
| `agreementId`        | Yes      | The ID of the agreement to present to the user.                                               |
| `checkRequired`      | Yes      | Indicates whether the flow should check for existing consent before presenting the agreement. |
| `agreementEnabled`   | No       | Indicates whether the agreement is required.                                                  |
| `showSuccessMessage` | No       | Indicates whether a success message should be displayed after the user accepts the agreement. |

## Output schema

This flow has the following outputs.

| Output Name     | Description                                   |
| --------------- | --------------------------------------------- |
| `subflowResult` | The result status of the flow.                |
| `errorMessage`  | The error message to pass to the parent flow. |
| `errorDetails`  | The details of the error that occurred.       |

## Variables and parameters

This flow uses the following variable or parameter values.

| Parameter name       | Description                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------- |
| `p1UserId`           | The current user's PingOne user ID.                                                           |
| `agreementId`        | The ID of the agreement to present to the user.                                               |
| `checkRequired`      | Indicates whether the flow should check for existing consent before presenting the agreement. |
| `agreementEnabled`   | Indicates whether the agreement is required.                                                  |
| `showSuccessMessage` | Indicates whether a success message should be displayed after the user accepts the agreement. |

---

---
title: Gift Card Redemption - Change Password - Subflow
description: The Gift Card Redemption - Change Password - Subflow lets users change their passwords.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:flow_reference/gift_card_change_password_subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/flow_reference/gift_card_change_password_subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Gift Card Redemption - Change Password - Subflow

The **Gift Card Redemption - Change Password - Subflow** lets users change their passwords.

## Purpose

The **Gift Card Redemption - Change Password - Subflow** displays a password reset form, letting users enter their current password and enter and verify a new password. If the new passwords match, the user's password is updated in PingOne.

## Structure

This flow is divided into sections using teleport nodes:

* **User Enter Password**

  Presents the user with an HTML template that that either displays a password reset form or displays a success message depending on the show success message value. The flow then progresses to the **Update Password** section.

* **Update Password**

  Compares the new password and confirmed password. If they match, a PingOne node updates the user's password. The flow then either returns to the beginning of the **User Enter Password** section or progresses to the **Return Success** section, depending on the value of the `showSuccessMessage` input.

* **Return Success**

  Sends a JSON success message.

* **Return Error**

  Uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs.

| Input name           | Required | Description                                                                                   |
| -------------------- | -------- | --------------------------------------------------------------------------------------------- |
| `p1UserId`           | Yes      | The current user's PingOne user ID.                                                           |
| `companyLogo`        | No       | The company logo.Used only when the main flow was launched using a redirect.                  |
| `showSuccessMessage` | No       | Indicates whether a success message should be displayed after the user accepts the agreement. |

## Output schema

This flow has the following outputs.

| Output Name     | Description                                   |
| --------------- | --------------------------------------------- |
| `subflowResult` | The result status of the flow.                |
| `errorMessage`  | The error message to pass to the parent flow. |
| `errorDetails`  | The details of the error that occurred.       |

## Variables and parameters

This flow uses the following variable or parameter values.

| Parameter name       | Description                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------- |
| `p1UserId`           | The current user's PingOne user ID.                                                           |
| `showSuccessMessage` | Indicates whether a success message should be displayed after the user accepts the agreement. |

---

---
title: Gift Card Redemption - Device Authentication - Subflow
description: The Gift Card Redemption - Device Authentication - Subflow lets users authenticate using a known device.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:flow_reference/gift_card_device_authentication_subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/flow_reference/gift_card_device_authentication_subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Gift Card Redemption - Device Authentication - Subflow

The **Gift Card Redemption - Device Authentication - Subflow** lets users authenticate using a known device.

## Purpose

The **Gift Card Redemption - Device Authentication - Subflow** enables users to authenticate using a known device. The flow evaluates the devices associated with the user account, invoking the **Gift Card Redemption - Magic Link Authentication - Subflow** flow if necessary. It then enables the user to select an authentication method and authenticates the user with the selected method.

## Structure

This flow is divided into sections using teleport nodes:

* **Gather Browser And Devices Data**

  Uses a PingOne node to gather the user's existing devices. Next, an HTML node evaluates the user's browser to determine if biometrics are available. The flow then progresses to the **Filter and Mask Devices** section.

* **Filter and Mask Devices**

  Filters the list of available devices to create a list of usable devices, then masks the device information so that the devices can be identified without displaying the full device information. The flow then progresses to the **Check If MFA Enabled And Any Device Active** section.

* **Check If MFA Enabled And Any Device Active**

  Uses a PingOne node to check the user's MFA status. If MFA is enabled and the user has active devices, the flow progresses to the **Decide Authentication Path Based On MFA Policy** section. If MFA is not enabled or the user has no active devices, the flow progresses to the **Call Magic Link Authentication** section.

* **Decide Authentication Path Based On MFA Policy**

  Uses a PingOne node to begin MFA authentication. If an assertion or an OTP is required, the flow progresses to the **Default Device Enrichment** section. If the user has multiple devices, or if the user has only one usable device and magic link is enabled, the flow progresses to the **Device Selection** section. If the user has one usable device and magic link is not enabled, the flow progresses to the **Default Device Enrichment** section.

* **Call Magic Link Authentication**

  Invokes the **Gift Card Redemption - Magic Link Authentication - Subflow** flow if magic link authentication is enabled. The flow then progresses to the **Return Success** section.

* **Device Selection**

  Presents the user with an HTML page on which they can select a device.

  * If the user selected magic link, the **Gift Card Redemption - Magic Link Authentication - Subflow** flow is invoked, and the flow then progresses to the **Return Success** section or to the **Device Selection** section depending on the subflow results.

  * If the user selected another authentication method, a PingOne records their selection and the flow progresses to the **Default Device Enrichment** section.

* **Default Device Enrichment**

  Uses a function node to enrich the device details, then the flow progresses to the **Handle TOTP, SMS, Voice, Mobile and Email OTP Authentication** section if an OTP is required, to the **Handle FIDO2 Authentication** section if assertion is required, or to the **Start Mobile Push** section if push confirmation is required.

* **Handle TOTP, SMS, Voice, Mobile and Email OTP Authentication**

  Uses function nodes to begin tracking the number of attempts and check the device type, then presents the user with an HTML page with options to enter the passcode, change devices, or resend the OTP.

  * If the user selects resend, the number of resend attempts is incremented and compared to the maximum. If the maximum has not yet been reached, a PingOne node resends the OTP and a confirmation message is displayed.

  * If the user selects a different method, the flow progresses to the **Device Selection** section.

  * If the user enters a passcode, a function node converts the value to lowercase, then a PingOne MFA node evaluates the passcode. If the passcode is validated successfully, the authentication method is saved as a variable and the flow progresses to the **Return Success** section.

* **Handle FIDO2 Authentication**

  Presents users with the option to select a different device or continue with the current device. If the user selects a different device, it progresses to the **Device Selection** section. If the user continues, it uses a PingOne MFA node with FIDO assertion to authenticate the user. If the authentication succeeds, the flow progresses to the **Return Success** section.

* **Mobile Push Flow**

  Displays a polling page, then branches based on the user's selection.

  * If the user chooses to use a passcode, the flow progresses to the **Mobile Passcode Flow** section.

  * If the user chooses to use a different device, the flow progresses to the **Device Selection** section.

  * If the user attempts to authenticate using the current device, a PingOne MFA node reads the device authentication.

  The flow branches again based on the authentication status.

  * If the status is complete, a function node saves the authentication method as a variable and the flow progresses to the **Return Success** section.

  * If the status is failed, a function node checks whether the attempt timed out. If so, the flow progresses to the **Mobile App Timed Out** section.

  * If the status is `push configuration required`, polling continues.

  * If the status is `push configuration timed out`, a function node checks if OTP fallback is allowed. If so, the flow progresses to the **Mobile Passcode Flow** section.

* **Mobile Passcode Flow**

  Presents users with an HTML form, with options for retrying, cancelling, or submitting an OTP.

  * If the user retries, a PingOne MFA node performs device selection and the flow returns to the **Mobile Push Flow** section.

  * If the user cancels, the flow progresses to the **Device Selection** section.

  * If the user submits an OTP, a PingOne MFA node checks the device passcode. A function node then saves the authentication method as a variable and the flow progresses to the **Return Success** section.

* **Mobile App Timed Out**

  Displays an error screen which presents the user with multiple options.

  * If the user retries, a PingOne MFA node performs device selection and the flow returns to the **Mobile Push Flow** section.

  * If the user selects `Change Device`, the flow progresses to the **Device Selection** section.

* **Return Success**

  Sends a success JSON response, indicating that the flow has completed successfully.

* **Return Error**

  Sends an error JSON response, indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs.

| Input name           | Required | Description                                                                                                     |
| -------------------- | -------- | --------------------------------------------------------------------------------------------------------------- |
| `p1UserId`           | Yes      | The current user's PingOne user ID.                                                                             |
| `resendOtpLimit`     | Yes      | The maximum number of times a new OTP can be sent to the user.                                                  |
| `email`              | No       | The user's email address.                                                                                       |
| `p1MFAPolicyId`      | No       | The PingOne MFA policy to apply.                                                                                |
| `allowedDeviceTypes` | No       | A string containing any or all of `SMS, EMAIL, FIDO2, TOTP, VOICE, MOBILE` indicating the allowed device types. |
| `otpFallbackAllowed` | No       | A boolean indicating whether a user can fall back to an OTP after an authentication failure.                    |
| `magicLinkEnabled`   | No       | A boolean indicating whether magic link is enabled.                                                             |
| `companyLogo`        | No       | The company logo.Used only when the main flow was launched using a redirect.                                    |
| `cancelEnabled`      | No       | A boolean indicating whether the user can cancel an authentication method selection.                            |

## Output schema

This flow has the following outputs.

| Output Name     | Description                                                             |
| --------------- | ----------------------------------------------------------------------- |
| `subflowResult` | The result status of the flow.                                          |
| `authMethod`    | The authentication method used, if the user successfully authenticated. |
| `errorMessage`  | The error message to pass to the parent flow.                           |
| `errorDetails`  | The details of the error that occurred.                                 |

## Variables and parameters

This flow uses the following variable or parameter values.

| Variable name       | Parameter name | Description                                     |
| ------------------- | -------------- | ----------------------------------------------- |
| `resendOtpAttempts` | None           | The number of times the user has resent an OTP. |

---

---
title: Gift Card Redemption - Device Registration - Subflow
description: The Gift Card Redemption - Device Registration - Subflow lets users register a new device.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:flow_reference/gift_card_device_registration_subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/flow_reference/gift_card_device_registration_subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Gift Card Redemption - Device Registration - Subflow

The **Gift Card Redemption - Device Registration - Subflow** lets users register a new device.

## Purpose

The **Gift Card Redemption - Device Registration - Subflow** presents users with options to register any available device type. The flow finds the available devices, then uses an HTML node to let the user select one:

* If the user selects **Mobile Application**, the flow creates a pairing key to pair the application with the account.

* If the user selects **Biometrics/Security Key**, the flow pairs the current FIDO-supported device.

* If the user selects **Authenticator App**, the flow uses a key URL to pair an authenticator app with the account.

* If the user selects **Text Message**, the flow gathers the number and uses a one-time passcode (OTP) *(tooltip: \<div class="paragraph">
  \<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
  \</div>)* to verify the SMS number.

* If the user selects **Voice** the flow gathers the number and uses an OTP to verify the phone number.

* If the user selects **Email**, the flow uses an OTP to verify the email address.

After any successful device registration, or if the user selects password, the flow returns to the **Gift Card Redemption - Account Registration - Subflow** parent flow.

## Structure

This flow is divided into sections using teleport nodes:

* **Gather device types that user can register with**

  Uses a PingOne node to retrieve the user's current devices, then uses a hidden HTML form to gather browser information. If the user has compatible devices and can register at least one device, the flow progresses to the **Check Whether MFA Greetings Required To Be Displayed To User?** section.

* **Check Whether MFA Greetings Required To Be Displayed To User?**

  Uses a function node to check if the greeting page should be displayed.

  If the greeting should be displayed, an HTML node asks for user consent to add an MFA device. If the user clicks **Skip** or **Back**, the flow progresses to the **Return Success** section.

  If the user does not select **Skip** or **Back**, or if the greeting page is not displayed, a function node checks whether the user's email is known. If the user's email address is not known, the flow progresses to the **User select device to register with** section.

  If the user's email address is known, a function node checks whether direct enrollment of the user's email is requested. If direct enrollment is not requested, the flow progresses to the **User select device to register with** section. If direct enrollment is requested, function nodes verify that the email address is not in use and set the `canEnrollOnlyEmail` variable to true, then the flow progresses to the **Prepare to register OTP device** section.

* **User select device to register with**

  Presents the user with an HTML page that provides them with the available authentication method options.

  If the user selects **Voice** or **SMS**, the flow progresses to the **User selected SMS/VOICE** section.

  If the user selects **Email**, the flow progresses to the **User selected email** section.

  If the user selects **TOTP**, the flow progresses to the **Prepare to register OTP device** section.

  If the user selects **FIDO2**, the flow progresses to the **Register FIDO2 device and enable MFA for user** section.

  If the user selects **Mobile**, the flow progresses to the **Mobile app registration flow** section.

  If the user selects **Cancel**, a function node determines whether MFA is required. If MFA is required, the flow progresses to the **Return Success** section with the `cancel` result. If MFA is not required, the flow progresses to the **Return Success** section with the `skip` result.

* **User selected SMS/VOICE**

  Displays an HTML page gives the user the option to provide a voice or SMS number.

  If the user enters a voice or SMS number, a function node verifies that the number is not in use, then the flow progresses to the **Prepare to register OTP device** section.

  If the user clicks **Cancel**, the flow returns to the **User select device to register with** section.

* **User selected email**

  Uses a function node to check for a known user email.

  If the user's email is not present, an HTML node lets the user enter an email and submit it or cancel.

  If the user clicks **Cancel**, the flow returns to the **User select device to register with** section.

  If the user submits an email, or if their email was already present, a function node verifies that the email is not already registered. If the email is not already registered, the flow progresses to the **Prepare to register OTP device** section. If the email is already registered, a function node determines the correct error message to display.

* **Prepare to register OTP device**

  Uses a PingOne node to create an OTP device.

  If the OTP device creation succeeds, a function node sets the device ID, then the flow progress to the **TOTP (Authenticator app) registration flow** section if the device type is TOTP, or to the **Ask for OTP** section if the device is SMS, voice, or email.

  If the OTP device creation fails, an error message is displayed.

* **Ask for OTP**

  Uses function nodes to begin tracking the number of resend attempts, mask the phone number or email, and determine the cancel behavior, then displays an HTML node prompting the user for the OTP.

  If the user submits a code, the flow progresses to the **Activate OTP device and enable MFA for user** section. Otherwise, the flow progresses to the **Resend OTP** section.

* **Resend OTP**

  If the user clicks **Resend** at the OTP prompt screen, function nodes increment the resend attempts and check if the maximum has been reached. If the maximum has not been reached, PingOne nodes delete the previous OTP device and create a new device, a function node updates the device ID, and a message is displayed for the user.

  If the user clicks **Cancel** at the OTP prompt screen, a PingOne node deletes the OTP device. A function node then redirects the flow based on the cancel button behavior. If this value is `Back`, the flow progresses to the **User select device to register with** section. If this value is `Skip`, the flow progresses to the **Return Success** section with the `Skip` result. If this value is `Cancel`, the flow progresses to the **Return Success** section with the `Cancel` result.

* **TOTP (Authenticator app) registration flow**

  Uses a function node to create a QR code for the key URL, then displays an HTML page on which the user can scan the QR code and enter a secret.

  If the user enters the secret, the flow progresses to the **Activate OTP device and enable MFA for user** section.

  If the user clicks **Cancel**, a PingOne node deletes the OTP device, and the flow returns to the **User select device to register with** section.

* **Activate OTP device and enable MFA for user**

  Uses a PingOne node to activate the OTP device. If the new device should be the default, a PingOne node sets it as the default, then another PingOne node updates the user's MFA status. The flow then progresses to the **Return Success** section.

* **Register FIDO2 device and enable MFA for user**

  Uses a PingOne node to create a FIDO2 device, then presents the user with an HTML registration page.

  If the user successfully registers the device, a PingOne node activates the device. If the new device should be the default, a PingOne node sets it as the default, then another PingOne node updates the user's MFA status. The flow then progresses to the **Return Success** section.

  If the user clicks **Cancel**, a PingOne node deletes the device and the flow returns to the **User select device to register with** section.

* **Mobile app registration flow**

  Uses a PingOne node to create a pairing key, then creates a QR code using the key. An HTML node then presents the QR code to the user.

  If the user clicks **Cancel**, a PingOne node deletes the pairing key and the flow returns to the **User select device to register with** section.

  A PingOne node reads the key, then a polling node determines when to proceed. If the polling status is claimed, a function node determines whether the user has any pre-registered devices. If the user has no pre-registered devices, a PingOne node activates MFA for the user and the flow progresses to the **Return Success** section.

  If the user has pre-registered devices, a function node determines whether the new device should be set as the default. If the new device should not be set as default, a PingOne node enables MFA for the user. If the new device should be the default, a PingOne node reads the user's mobile devices, a function node finds the device ID, and a PingOne node sets the device as default. A PingOne node then enables MFA for the user.

  If the polling fails, an error message is displayed, a PingOne node deletes the pairing key, and the flow returns to the **User select device to register with** section.

* **Return Success**

  Sends a success JSON response, indicating that the flow completed successfully.

* **Return Error**

  Uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs.

| Input name                | Required | Description                                                                                                     |
| ------------------------- | -------- | --------------------------------------------------------------------------------------------------------------- |
| `email`                   | No       | The email address to use for registration.                                                                      |
| `p1UserId`                | Yes      | The user ID of the current user.                                                                                |
| `notShowMFAGreetingsPage` | No       | A boolean indicating whether to show the user greetings page.                                                   |
| `allowOnlyEmail`          | No       | A boolean indicating whether email should be the only permitted MFA device.                                     |
| `requireMFA`              | No       | A boolean indicating whether MFA is required.                                                                   |
| `setNewDeviceAsDefault`   | No       | A boolean indicating whether a newly added device should be set as the default device.                          |
| `allowedDeviceTypes`      | No       | A string containing any or all of `SMS, EMAIL, FIDO2, MOBILE, VOICE, TOTP` indicating the allowed device types. |
| `companyLogo`             | No       | The company logo.Used only when the main flow was launched using a redirect.                                    |
| `resendOtpLimit`          | Yes      | The maximum number of times the user can resend the OTP.                                                        |

## Output schema

This flow has the following outputs.

| Output name     | Description                                                |
| --------------- | ---------------------------------------------------------- |
| `subflowResult` | The result status of the flow.                             |
| `authMethod`    | The authentication method that was configured by the flow. |
| `errorMessage`  | The error message to display in the parent flow.           |
| `errorDetails`  | The details of the error that occurred in this flow.       |

## Variables and parameters

This flow uses the following variable or parameter values.

| Variable name        | Description                                                                 |
| -------------------- | --------------------------------------------------------------------------- |
| `canEnrollOnlyEmail` | A boolean indicating whether email should be the only permitted MFA device. |
| `resendOtpAttempts`  | The number of times the user has resent the OTP.                            |
| `p1MFADeviceId`      | The device ID for the device being registered.                              |

---

---
title: Gift Card Redemption - Magic Link Authentication - Subflow
description: The Gift Card Redemption - Magic Link Authentication - Subflow lets existing users authenticate using a link sent to the email address that's associated with their account.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:flow_reference/gift_card_magic_link_authentication_subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/flow_reference/gift_card_magic_link_authentication_subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Gift Card Redemption - Magic Link Authentication - Subflow

The **Gift Card Redemption - Magic Link Authentication - Subflow** lets existing users authenticate using a link sent to the email address that's associated with their account.

## Purpose

The **Gift Card Redemption - Magic Link Authentication - Subflow** presents users with the option to send a magic link to the email address associated with their account. After the link is sent, the flow checks the status of the link. If the link is clicked, the flow authenticates the user. If the link expires, the flow presents an error message. The magic link expires after 2.5 minutes (150 seconds).

## Structure

This flow is divided into sections using teleport nodes:

* **Display Magic Link Form**

  Uses a PingOne node to look up the user, then presents an HTML form from which the user can send a magic link. The flow then simultaneously progresses to the **Create Challenge and Send Email** and **Challenge Acceptance By The User** sections.

* **Create Challenge and Send Email**

  Uses a PingOne node to send a magic link email. The flow then progresses to the **Display Magic Link Polling And Check For Challenge Status** section.

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

This flow has the following inputs.

| Input name        | Required | Description                                                                  |
| ----------------- | -------- | ---------------------------------------------------------------------------- |
| `p1UserId`        | Yes      | The user ID of the user to be authenticated.                                 |
| `canChangeDevice` | Yes      | Indicates whether the user can change the device used for authentication.    |
| `companyLogo`     | No       | The company logo.Used only when the main flow was launched using a redirect. |

## Output schema

This flow has the following outputs.

| Output name     | Description                                          |
| --------------- | ---------------------------------------------------- |
| `subflowResult` | The result status of the flow.                       |
| `errorMessage`  | The error message to display in the parent flow.     |
| `errorDetails`  | The details of the error that occurred in this flow. |

## Variables and parameters

This flow uses the following variable or parameter values.

| Variable name      | Description                                  |
| ------------------ | -------------------------------------------- |
| `ciam_logoStyle`   | The HTML style to use for your company logo. |
| `ciam_logoUrl`     | The URL for your company logo.               |
| `ciam_companyName` | Displays the name of your company.           |

---

---
title: Gift Card Redemption - SignOn - Subflow
description: TheGift Card Redemption - SignOn - Subflow lets users sign on, create a new account, or recover an account.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:flow_reference/gift_card_signon_subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/flow_reference/gift_card_signon_subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Gift Card Redemption - SignOn - Subflow

The**Gift Card Redemption - SignOn - Subflow** lets users sign on, create a new account, or recover an account.

## Purpose

The **Gift Card Redemption - SignOn - Subflow** enables existing users to sign on using a password, uses the **Gift Card Redemption - Account Registration - Subflow** to let new users register, uses the **Gift Card Redemption - Account Recovery - Email - Subflow** to let existing users recover their account, and uses the **Gift Card Redemption - Device Authentication - Subflow** flow to let existing users sign on using a known device.

## Structure

This flow is divided into sections using teleport nodes:

* **Flow Configuration**

  Uses multiple function nodes to save the variable and parameter values so that the correct values are available in the flow and in subflows. The flow then progresses to the **Offer Sign On Page** section.

* **Offer Sign On Page**

  Displays an HTML page with options to sign on using a password, recover from a forgotten password, or register a new account.

  If the user clicks **Sign On**, a PingOne node looks up the user using their email address. The flow then progresses to the **Threat Detection And Mitigation** section. When this section completes, the flow progresses to the **Password Authentication** section.

  If the user selects the forgot password option, the flow progresses to the **Call Account Recovery Sub-Flow** section.

  If the user selects the registration option, the flow progresses to the **Call Account Registration Sub-Flow** section.

  If no options match, a hidden HTML node activates CSS files for social login, and the flow progresses to the **Call Check Agreement and Email Verification Sub-Flow** section.

* **Call Account Recovery Sub-Flow**

  Invokes the **Gift Card Redemption - Account Recovery - Email - Subflow** flow, then progresses to the **Offer Sign On Page** section.

* **Call Account Registration Sub-Flow**

  Invokes the **Gift Card Redemption - Account Registration - Subflow** flow. If the subflow's result is `signOn`, the flow progresses to the **Offer Sign On Page** section. If the subflow's result is `complete`, the flow invokes the **Gift Card Redemption - Device Registration - Subflow** flow, uses a PingOne node to send an account creation email, and then progresses to the **Return Success** section.

* **Threat Detection And Mitigation**

  Invokes the **Gift Card Redemption - Threat Detection - Subflow**.

  If the **Gift Card Redemption - Threat Detection - Subflow** completes successfully, a function node stores the risk evaluation as a variable, then a second function node branches the flow based on the risk level:

  * If the risk level is low, a function node sets the `isMFAAuthnReq` variable to false. The flow then progresses to the **Return Success** section if an existing session is found, and to the **Password Authentication** section if no session is found.

  * If the risk level is medium, a function node sets the `isMFAAuthnReq` variable to true. The flow then progresses to the **Password Authentication** section.

  * If the risk level is high, function nodes check if the PingOne user ID is unknown and if the high risk was the result of a new device. If the PingOne ID is unknown, and the high risk is not the result of a new device, a PingOne node sends an email notifying the user of suspicious activity. A function node sets the `isMFAAuthnReq` variable to true, and the flow progresses to the **Password Authentication** section.

  If the **Gift Card Redemption - Threat Detection - Subflow** completes unsuccessfully, an error message displays.

* **Password Authentication**

  Uses two PingOne nodes to look up the user and validate the provided password. If the password is correct and current, the flow progresses to the **Return Success** section. If the password is correct but must be changed or is expired, the flow progresses to the **Call Change Password Sub-Flow** section. If the password is incorrect or the user cannot be found, a comparison node checks whether the account is locked. If the account is locked, the flow progresses to the **Return Error** section. If the account is not locked, an error message displays to the user.

* **MFA Authentication**

  Uses a PingOne node to look up the user's existing devices. An HTML node then checks the user's current device for Webauthn support, and comparison nodes filter for unusable devices and check if at least one device is configured.

  If the user has no active devices, or the user's device information could not be found, the flow progresses to the **Step up to register Email MFA device if no MFA devices found during authentication** section.

  If the user has active devices, a PingOne node enables MFA, then invokes the **Gift Card Redemption - Device Authentication - Subflow**. If the subflow completes successfully, the flow progresses to the **Check Password Status** node in the **Password Authentication** section.

* **Call Change Password Sub-Flow**

  Invokes the **Gift Card Redemption - Change Password - Subflow** flow. If the subflow completes successfully, the flow displays a success message and a PingOne node sends a password change email the flow. The flow then progresses to the **Call Check Agreement and Email Verification Sub-Flow** section.

* **Step up to register Email MFA device if no MFA devices found during authentication**

  A comparison node checks whether email verification is required.

  If email verification is not required, invokes the **Gift Card Redemption - Device Registration - Subflow**, then progresses to the **Check Password Status** node in the **Password Authentication** section.

  If email verification is required, invokes the **Gift Card Redemption - Verify Email - Subflow**, then uses PingOne nodes to enroll email as an MFA device, enable MFA for the user, and send an email confirming the email device registration. The flow then progresses to the **Check Password Status** node in the **Password Authentication** section.

* **Call Check Agreement and Email Verification Sub-Flow**

  Invokes the **Gift Card Redemption - Agreement (ToS) - Subflow**, then uses a PingOne node to retrieve user information. A function node checks whether email verification is required, and if email verification is required, the **Gift Card Redemption - Verify Email - Subflow** is invoked. The flow then progresses to the **Handle Remember Me if Applicable** section.

* **Handle Remember Me if Applicable**

  Adds **Remember Me** as an authentication method if it is enabled, then progresses to the **Return Success** section.

* **Return Success**

  Displays an HTML success message to the user, then sends a success response, indicating that the flow completed successfully.

* **Return Error**

  Displays an error screen and sends an error JSON response, indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input Name                            | Required | Description                                                                                                               |
| ------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------- |
| `flowParameters`                      | No       | An object containing parameters passed in if the flow was launched with the widget. This input replaces all other inputs. |
| `p1AgreementId`                       | No       | The ID of the PingOne agreement to present to users.                                                                      |
| `p1MFAPolicyId`                       | No       | The PingOne MFA policy ID.                                                                                                |
| `p1RiskPolicyIdReg`                   | No       | The PingOne risk policy ID to use for registration.                                                                       |
| `p1RiskPolicyIdAuthn` - REMOVE        | No       | The PingOne risk policy ID to use for authentication.                                                                     |
| `p1RiskPolicyIdAR`                    | No       | The PingOne risk policy ID to use for account recovery.                                                                   |
| `canUserEnableMFA`                    | No       | Indicates whether the user can enable MFA for their account.                                                              |
| `disableAccountRegistrationButton`    | No       | Indicates whether the account registration button should be disabled. This option is set to true by default.              |
| `disableAccountRecoveryButton`        | No       | Indicates whether the account recovery button should be disabled. This option is set to true by default.                  |
| `disableSocialRegistrationButton`     | No       | Indicates whether the social registration option should be disabled. This option is set to true by default.               |
| `bypassRiskEvaluationUpdateOnSuccess` | No       | Indicates whether the flow should update the PingOne Protect evaluation information when the flow succeeds.               |

## Output schema

This flow has the following outputs:

| Output Name    | Description                                          |
| -------------- | ---------------------------------------------------- |
| `errorMessage` | The error message to display in the parent flow.     |
| `errorDetails` | The details of the error that occurred in this flow. |
| `authMethod`   | The authentication method used in the flow.          |
| `p1UserId`     | The PingOne user ID of the user.                     |

## Variables and parameters

This flow uses the following variable or parameter values:

| Variable name                 | Parameter name            | Description                                                                                                                                                                                                                                                                                                      |
| ----------------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ciam_logoStyle`              | None                      | The HTML style to use for your company logo.                                                                                                                                                                                                                                                                     |
| `ciam_logoUrl`                | None                      | The URL for your company logo.                                                                                                                                                                                                                                                                                   |
| `ciam_appleEnabled`           | `isAppleEnabled`          | Indicates whether authentication through Apple is enabled in your environment.                                                                                                                                                                                                                                   |
| `ciam_facebookEnabled`        | `isFacebookEnabled`       | Indicates whether authentication through Facebook is enabled in your environment.                                                                                                                                                                                                                                |
| `ciam_googleEnabled`          | `isGoogleEnabled`         | Indicates whether authentication through Google is enabled in your environment.                                                                                                                                                                                                                                  |
| `ciam_companyName`            | None                      | Displays the name of your company.                                                                                                                                                                                                                                                                               |
| `ciam_magicLinkEnabled`       | `isEmailMagicLinkEnabled` | Indicates whether magic link is enabled in your environment.                                                                                                                                                                                                                                                     |
| `ciam_agreementEnabled`       | `isTermsOfServiceEnabled` | A boolean indicating whether agreement is enabled in your environment.                                                                                                                                                                                                                                           |
| `ciam_requireMFA`             | `isRequireMFA`            | A boolean that controls whether MFA is required for all users.                                                                                                                                                                                                                                                   |
| `ciam_resendOtpLimit`         | None                      | The maximum number of times a user can resend a one-time passcode (OTP) *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)*. |
| `ciam_verificationLimit`      | None                      | The maximum number of times a user can attempt to verify their email address.                                                                                                                                                                                                                                    |
| `ciam_otpFallbackAllowed`     | None                      | A boolean indicating whether a user can fall back to an OTP if a mobile push request times out.                                                                                                                                                                                                                  |
| `ciam_recoveryLimit`          | None                      | The maximum number of times a user can attempt to recover an account.                                                                                                                                                                                                                                            |
| `ciam_accountRecoveryEnabled` | None                      | A boolean that controls whether account recovery is enabled in your environment.                                                                                                                                                                                                                                 |
| `p1AgreementId`               | None                      | The ID of the PingOne agreement to present to users.                                                                                                                                                                                                                                                             |
| `p1RiskPolicyIdAuthn`         | None                      | The PingOne risk policy ID to use for authentication.                                                                                                                                                                                                                                                            |
| `protectRiskEvalId`           | None                      | The risk evaluation ID returned by PingOne Protect.                                                                                                                                                                                                                                                              |
| `p1RiskPolicyIdReg`           | None                      | The PingOne risk policy ID to use for registration.                                                                                                                                                                                                                                                              |
| `p1RiskPolicyIdAR`            | None                      | The PingOne risk policy ID to use for account recovery.                                                                                                                                                                                                                                                          |
| `flowCompanyLogo`             | None                      | The company logo to use during the flow.                                                                                                                                                                                                                                                                         |
| `p1MFAPolicyId`               | None                      | The PingOne MFA policy ID.                                                                                                                                                                                                                                                                                       |
| `authMethod`                  | None                      | The authentication method used by the user.                                                                                                                                                                                                                                                                      |
| `protectDeviceStatus`         | None                      | The status of the user's device as determined by PingOne Protect.                                                                                                                                                                                                                                                |
| `flowRequireMFA`              | None                      | Indicates whether MFA enrollment is required in the flow.                                                                                                                                                                                                                                                        |
| `isMFAAuthnReq`               | None                      | Indicates whether MFA authentication is required.                                                                                                                                                                                                                                                                |

---

---
title: Gift Card Redemption - Threat Detection - Subflow
description: The Gift Card Redemption - Threat Detection - Subflow uses PingOne Protect to provide a risk assessment of the current user.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:flow_reference/gift_card_threat_detection_subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/flow_reference/gift_card_threat_detection_subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Gift Card Redemption - Threat Detection - Subflow

The **Gift Card Redemption - Threat Detection - Subflow** uses PingOne Protect to provide a risk assessment of the current user.

## Purpose

The **Gift Card Redemption - Threat Detection - Subflow** passes user information to PingOne Protect to perform a risk assessment. The assessment results are made available to other flows.

## Structure

This flow is divided into sections using teleport nodes:

* **Detect Threat using PingOne Protect**

  A function node verifies that the username, flow type, and `skriskcomponent` are all present. If all values are present, a PingOne Protect node creates a risk evaluation.

  If the evaluation succeeds, comparison nodes verify that no bot, AITM, or disposable email was detected. If a bot is detected, the flow progresses to the **Return Error** section. If an AITM or disposable email is detected, the flow progresses to the **Disable User, Notify User With Password Reset Link And Return Error If AITM/Disposable Mail Detected** section.

  If no AITM or disposable email is detected, a function node checks the risk level. If a high risk is detected, function nodes verify that the calling flow is not Gift Card Redemption - Account Registration - Subflow, that the user's PingOne user ID is known, and that the user is active. PingOne nodes then either notify the user of the new device login if a new device was found or notify the user of the high risk if a new device was not found.

  Regardless of the risk level, function nodes check for a PingOne user ID and verify that the user's account is not disabled. The flow then proceeds to the **Return Success** section.

* **Disable User, Notify User With Password Reset Link And Return Error If AITM/Disposable Mail Detected**

  Function nodes verify that the calling flow is not Gift Card Redemption - Account Registration - Subflow, that the user's PingOne user ID is known, and that the user is active. If these conditions are met, a PingOne node disables the user, then the flow progresses to the **Create And Send Link To User's Email To Reset Password And Enable Account After Password Reset** section.

* **Create And Send Link To User's Email To Reset Password And Enable Account After Password Reset**

  Uses a flow connector node to create a magic link with an out-of-band start while simultaneously progressing to the **Challenge Acceptance By The User By Clicking On The Link From Email** section. The section then uses a PingOne node to notify the user of the account suspesnsion and progresses to the **Return Error** section.

* **Challenge Acceptance By The User By Clicking On The Link From Email**

  Uses function nodes to check the challenge status. When the challenge is approved, invokes the **Gift Card Redemption - Account Recovery - Main Flow**.

* **Return Success**

  Sends a JSON success message.

* **Return Error**

  Uses a function node to enrich the error details, then sends a JSON error message. If the PingOne Protect evaluation ID is not present, a PingOne Protect node updates the PingOne Protect risk evaluation to `Failed`.

## Input schema

This flow has the following inputs:

| Input name              | Required | Description                                                                                                 |
| ----------------------- | -------- | ----------------------------------------------------------------------------------------------------------- |
| `skriskcomponent`       | Yes      | The `SKRisk` component to be used in the risk evaluation.                                                   |
| `p1UserId`              | No       | The user ID to be passed to PingOne Protect.                                                                |
| `p1UserName`            | Yes      | The username to be evaluated by PingOne Protect.                                                            |
| `p1ProtectRiskPolicyId` | No       | The risk policy ID to be passed to PingOne Protect. If it is not provided, the default risk policy is used. |
| `flowType`              | Yes      | The flow type to be passed to PingOne Protect.                                                              |
| `ipAddress`             | Yes      | The user IP address to be passed to PingOne Protect.                                                        |
| `isAccountEnabled`      | No       | A boolean indicating whether the user's account is enabled.                                                 |
| `applicationID`         | No       | The application ID to be passed to PingOne Protect.                                                         |
| `sessionID`             | No       | The session ID to be passed to PingOne Protect.                                                             |
| `customAttributes`      | No       | Any custom PingOne attributes to be passed to PingOne Protect.                                              |
| `userAgent`             | No       | The PingOne Protect user agent.                                                                             |
| `usercookie`            | No       | The PingOne Protect user cookie.                                                                            |

## Output schema

This flow has the following outputs:

| Output name            | Description                                                                                                            |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `protectRiskEvalID`    | The risk ID of the current user as used by PingOne Protect.                                                            |
| `protectActivityState` | The user's state or province, as determined by PingOne Protect.                                                        |
| `protectActivityCity`  | The user's city, as determined by PingOne Protect.                                                                     |
| `protectDeviceStatus`  | The status of the user's device as determined by PingOne Protect.                                                      |
| `protectPredictor`     | The action recommended by PingOne Protect.                                                                             |
| `protectRiskLevel`     | The risk level of the current user as determined by PingOne Protect.                                                   |
| `errorMessage`         | The error message returned by the flow. Sent only if the flow progressed to the **Return Error** section.              |
| `errorDetails`         | The detailed error information returned by the flow. Sent only if the flow progressed to the **Return Error** section. |

## Variables and parameters

This flow does not directly use any variable or parameter values.

---

---
title: Gift Card Redemption - Update Email &amp; Redeem Rewards - Main Flow
description: The Gift Card Redemption - Update Email & Redeem Rewards - Main Flow lets users update their email addresses and redeem rewards.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:flow_reference/gift_card_update_email_redeem_rewards_main_flow
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/flow_reference/gift_card_update_email_redeem_rewards_main_flow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Gift Card Redemption - Update Email & Redeem Rewards - Main Flow

The Gift Card Redemption - Update Email & Redeem Rewards - Main Flow lets users update their email addresses and redeem rewards.

## Purpose

The Gift Card Redemption - Update Email & Redeem Rewards - Main Flow is the initial flow in the Gift Card solution. It performs a PingOne Protect assessment using the **Gift Card Redemption - Threat Detection - Subflow** and enables users to sign on. It then presents users with forms that let them update their email address or redeem rewards.

## Structure

This flow is divided into sections using teleport nodes:

* **Flow Configuration**

  Uses multiple function nodes to save the variable and parameter values so that the correct values are available in the flow and in subflows. The flow then progresses to the **Check Session, Call To Protect Analysis & MFA Step-Up** section.

* **Check Session, Call To Protect Analysis & MFA Step-Up**

  Uses a PingOne node to determine whether the user has an existing session.

  If the user has a session, a hidden HTML node captures risk information and a PingOne node fetches additional user information, then the flow progresses to the **Threat Detection and Mitigation** section. When this section completes, a function node checks if the user's account is enabled, and if so, the flow progresses to the **Manage Account: Prompt User To Update Email / Redeem Rewards and step-up with MFA based on risk level** section.

  If the user does not have a session, the flow checks for any existing session tokens and uses a PingOne node to delete the prior session before invoking the **Gift Card Redemption - SignOn - Subflow** with the `disableAccountRegistrationButton`, `disableAccountRecoveryButton`, and `disableSocialRegistrationButton` values set to `true`. When the subflow completes, a function node saves the protect risk level and a PingOne node creates a session for the user. A loading screen is displayed for the user, then a PingOne node retrieves user information. The flow then progresses to the **Manage Account: Prompt User To Update Email / Redeem Rewards and step-up with MFA based on risk level** section.

* **Threat Detection & Mitigation**

  Uses a function node to check whether PingOne Protect analysis is required.

  If PingOne Protect analysis isn't required, the flow returns to the **Check Session, Call To Protect Analysis & MFA Step-Up** section.

  If PingOne Protect analysis is required, the flow invokes the **Gift Card Redemption - Threat Detection - Subflow**.

  If the **Gift Card Redemption - Threat Detection - Subflow** completes successfully, a function node stores the risk evaluation as a variable, then a second function node branches the flow based on the risk level:

  * If the risk level is low, the flow returns to the **Check Session, Call To Protect Analysis & MFA Step-Up** section.

  * If the risk level is medium, the flow progresses to the **MFA Authentication** section. When this section completes, the flow returns to the **Check Session, Call To Protect Analysis & MFA Step-Up** section.

  * If the risk level is high, a function nodes checks if the high risk was the result of a new device. If not, a PingOne node notifies the user of the suspicious activity. A PingOne node deletes the user session. The flow then progresses to the **Check Session, Call To Protect Analysis & MFA Step-Up** section.

  If the **Gift Card Redemption - Threat Detection - Subflow** completes unsuccessfully, a function node stores the risk evaluation ID and an error message is displayed.

* **MFA Authentication**

  A PingOne node retrieves the user's existing devices, and a hidden HTML node gathers information about biometrics and security keys.

  Function nodes then filter the user's active devices and verify that the user has at least one active device. If the devices could not be filtered or if the user has no active devices, the flow progresses to the **Step Up To Register Email MFA Device, If No MFA Devices Found During Authentication** section.

  If the user has active devices, the **Gift Card Redemption - Device Authentication - Subflow** is invoked. The flow then splits by the subflow result.

  * If the **Gift Card Redemption - Device Authentication - Subflow** completed successfully, a function node stores the authentication method as a variable. The flow then returns to the previous section.

  * If the **Gift Card Redemption - Device Authentication - Subflow** was canceled, the flow returns to the previous section.

* **Step Up To Register Email MFA Device, If No MFA Devices Found During Authentication**

  A function node checks whether verification is required for the account.

  If verification is not required, the **Gift Card Redemption - Device Registration - Subflow** is invoked. The flow then splits based on the subflow result.

  * If the subflow completed successfully, the authentication method is stored as a variable, then the flow returns to the **MFA Authentication** section.

  * If the user canceled, the flow returns to the **Manage Account: Prompt User To Update Email / Redeem Rewards and step-up with MFA based on risk level** section if that was the previous section.

  If verification is required, the **Gift Card Redemption - Verify Email - Subflow** is invoked. If the subflow completes successfully, PingOne nodes enroll email as an MFA device and enable MFA for the user. A function node stores the authentication method as a variable, then the flow returns to the **MFA Authentication** section.

* **Manage Account: Prompt User To Update Email / Redeem Rewards and step-up with MFA based on risk level**

  An HTML page presents the user with a choice of updating their email or redeeming rewards. If risk mitigation is required, a function node examines the PingOne Protect risk level. If the risk level is low, a PingOne node updates the risk evaluation if the risk evaluation ID is known. If the risk level is medium or high, the flow progresses to the **Step Up To Register Email MFA Device, If No MFA Devices Found During Authentication** section.

  The flow then progresses to the **Update Email** section or the **Redeem Rewards** section depending on the user's selection.

* **Update Email**

  Uses a PingOne node to look up the user, then displays an email update form. The flow then branches based on the user's selection.

  If the user cancels, the flow returns to the **Manage Account: Prompt User To Update Email / Redeem Rewards and step-up with MFA based on risk level** section.

  If the user submits an email, function nodes verify that the new email is valid and that the current email matches the user's profile email. PingOne nodes then verify that the new email is not used by another user before updating the user's email address.

  The **Gift Card Redemption - Verify Email - Subflow** is then invoked. If the subflow completes successfully, a success message is displayed, then the flow returns to the **Manage Account: Prompt User To Update Email / Redeem Rewards and step-up with MFA based on risk level** section.

* **Redeem Rewards**

  Uses a PingOne node to look up the user, then displays a reward redemption form. The flow then branches based on the user's selection.

  If the user cancels, the flow returns to the **Manage Account: Prompt User To Update Email / Redeem Rewards and step-up with MFA based on risk level** section.

  If the user proceeds, a function node calculates the user's remaining balance, then a PingOne node updates the user's balance. A success message displays, showing the user's updated balance, then the flow returns to the **Manage Account: Prompt User To Update Email / Redeem Rewards and step-up with MFA based on risk level** section.

* **Return Success**

  Sends a success response, indicating that the flow completed successfully. If the risk evaluation ID is present and the user did not cancel, a PingOne node also updates the evaluation status.

* **Return Error**

  Displays an error screen and sends an error JSON response, indicating that the flow completed unsuccessfully. If the risk evaluation ID is present, a PingOne node also updates the evaluation status.

## Input schema

This flow has the following inputs:

| Input Name       | Required | Description                                                                                                               |
| ---------------- | -------- | ------------------------------------------------------------------------------------------------------------------------- |
| `flowParameters` | No       | An object containing parameters passed in if the flow was launched with the widget. This input replaces all other inputs. |

## Output schema

This flow has the following outputs:

| Output name    | Description                                                                                                            |
| -------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `p1UserId`     | The user ID of the current user.                                                                                       |
| `flowResult`   | The result status of the flow.                                                                                         |
| `errorMessage` | The error message returned by the flow. Sent only if the flow progressed to the **Return Error** section.              |
| `errorDetails` | The detailed error information returned by the flow. Sent only if the flow progressed to the **Return Error** section. |

## Variables and parameters

This flow uses the following variable or parameter values.

| Variable name                 | Description                                                                                                    |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `flowCompanyLogo`             | The URL for your company logo.                                                                                 |
| `p1MFAPolicyId`               | The ID of the PingOne MFA policy to use in the flow.                                                           |
| `p1AgreementId`               | The ID of the agreement to present to users.                                                                   |
| `p1RiskPolicyIdAuthn`         | The PingOne risk policy ID to use for authentication.                                                          |
| `p1RiskPolicyIdAR`            | The PingOne risk policy ID to use for account recovery.                                                        |
| `p1RiskPolicyIdAuthZ`         | The PingOne risk policy ID to use for authorization.                                                           |
| `p1RiskPolicyIdReg`           | The PingOne risk policy ID to use for registration.                                                            |
| `protectRiskEvalId`           | The risk ID of the current user as used by PingOne Protect.                                                    |
| `protectRiskLevel`            | The risk level of the current user as determined by PingOne Protect.                                           |
| `authMethod`                  | The authentication method used in the flow.                                                                    |
| `flowProtectAnalysisRequired` | Indicates whether a PingOne Protect analysis must be performed for all users.                                  |
| `ciam_magicLinkEnabled`       | Indicates whether magic link authentication is enabled.                                                        |
| `ciam_agreementEnabled`       | Indicates whether the agreement is required.                                                                   |
| `ciam_logoUrl`                | The URL for your company logo.This value is used only when the flow is launched with a redirect.               |
| `ciam_companyName`            | Displays the name of your company.This value is used only when the flow is launched with a redirect.           |
| `ciam_logoStyle`              | The HTML style to use for your company logo.This value is used only when the flow is launched with a redirect. |
| `ciam_sessionLengthInMinute`  | The maximum time a user can spend in the flow before it times out.                                             |

---

---
title: Gift Card Redemption - Verify Email - Subflow
description: The Gift Card Redemption - Verify Email - Subflow lets a user verify their email address using a one-time passcode (OTP) sent by the PingOne Single Sign-on connector.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:flow_reference/gift_card_verify_email_subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/flow_reference/gift_card_verify_email_subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables: Variables
---

# Gift Card Redemption - Verify Email - Subflow

The Gift Card Redemption - Verify Email - Subflow lets a user verify their email address using a one-time passcode (OTP) *(tooltip: \<div class="paragraph">
\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
\</div>)* sent by the PingOne Single Sign-on connector.

## Purpose

The **Gift Card Redemption - Verify Email - Subflow** sends a verification code, then displays an HTML page giving users the option to enter a verification code sent to their email or resend the code. If the user enters the code, a PingOne node verifies the code. If the user requests that the code be resent, a PingOne node resends the code, then the user is returned to the beginning of the flow.

## Structure

This flow is divided into sections using teleport nodes:

* **Prompt for OTP**

  Uses a flow instance variable to track the number of verification attempts. Uses a PingOne to send a verification code, then presents the user with an HTML page on which they can enter the verification code or request that the code be resent. If the user submits a verification code, the flow progresses to the **Validate OTP** section. If the user requests a new code, the flow progresses to the **Resend verification code** section.

* **Validate OTP**

  Increments the number of validation attempts. If the number of attempts has not reached the maximum, a PingOne node validates the verification code. If the validation succeeds, a JSON success message is sent. If the validation fails, an error message is displayed.

* **Resend OTP**

  Increments the number of resend attempts. If the number of attempts has not reached the maximum, a PingOne node sends a new verification code and a confirmation message indicates that the new verification code has been resent.

* **Return Error**

  Sends a JSON error message.

## Input schema

This flow has the following inputs:

| Input Name          | Required? | Description                                                                   |
| ------------------- | --------- | ----------------------------------------------------------------------------- |
| `p1UserID`          | Yes       | The user ID of the current user.                                              |
| `companyLogo`       | No        | The company logo.Used only when the main flow was launched using a redirect.  |
| `verificationLimit` | Yes       | The maximum number of times a user can attempt to verify their email.         |
| `resendOtpLimit`    | Yes       | The maximum number of times a user can attempt to resend a verification code. |

## Output schema

This flow has the following outputs.

| Output Name     | Description                                          |
| --------------- | ---------------------------------------------------- |
| `errorMessage`  | The error message to display in the parent flow.     |
| `errorDetails`  | The details of the error that occurred in this flow. |
| `subflowResult` | The result status of the flow.                       |

## Variables

This flow uses the following variables.

| Variable Name                    | Description                                                    |
| -------------------------------- | -------------------------------------------------------------- |
| `resendOtpAttempts`              | The number of times the user has resent an OTP.                |
| `verificationValidationAttempts` | The number of times the user has attempted email verification. |

---

---
title: Gift Card Redemption Release Notes
description: New features and improvements in Gift Card Redemption.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:release_notes/gift_card_release_notes
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/release_notes/gift_card_release_notes.html
revdate: June 28, 2024
section_ids:
  january-1: January 1
  initial-release: Initial Release
---

# Gift Card Redemption Release Notes

New features and improvements in Gift Card Redemption.

Subscribe to get automatic updates: [icon: rss-square, set=fa][Gift Card Redemption Release Notes RSS feed](release_notes/gift_card_release_notes.xml)

## January 1

### Initial Release

New

This is the initial release of the Gift Card Redemption solution.

---

---
title: Strong Authentication Methods
description: The Gift Card Redemption solution offers the following strong authentication methods, which each have advantages and disadvantages.
component: pingone-solutions
page_id: pingone-solutions:gift-card-auth:gift-card-authentication-methods
canonical_url: https://docs.pingidentity.com/pingone-solutions/gift-card-auth/gift-card-authentication-methods.html
revdate: January 29, 2025
section_ids:
  email-magic-link: Email magic link
  one-time-passcodes-email-and-sms: One-time passcodes (email and SMS)
  fido2-biometrics-passkeys-security-keys: FIDO2 (biometrics, passkeys, security keys)
  authenticator-app-totp: Authenticator app (TOTP)
  voice-otp: Voice (OTP)
  mobile-application: Mobile application
---

# Strong Authentication Methods

The Gift Card Redemption solution offers the following strong authentication methods, which each have advantages and disadvantages.

## Email magic link

An email magic link *(tooltip: \<div class="paragraph">
\<p>A passwordless authentication method that involves the authentication service sending a single-use sign on link to the user by email or SMS.\</p>
\</div>)*, also known as a magic sign-on link, is a convenient way to sign on to an online service, website, or application without entering a traditional username and password. Instead, it relies on a unique link that's sent to the user's email address, which acts as a one-time authentication token.

| Use cases                        | Benefits                          | Challenges                         |
| -------------------------------- | --------------------------------- | ---------------------------------- |
| Web applications                 | Reduced password fatigue          | Email security concerns            |
| Mobile apps                      | Lower support costs               | User skepticism                    |
| Temporary or infrequent sign ons | Mobile-friendly                   | Expired links and usability issues |
| Password recovery                | Reduced risk of password breaches | Phishing risks                     |

## One-time passcodes (email and SMS)

A one-time passcode (OTP) *(tooltip: \<div class="paragraph">
\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
\</div>)* is an authentication method used to provide a secure and convenient way for users to sign on to their accounts or access sensitive information. In this method, users are authenticated with username and password and issued a step-up authentication request through a one-time code delivered using the email address or phone number (through SMS) registered with their account.

| Use cases                       | Benefits                     | Challenges                        |
| ------------------------------- | ---------------------------- | --------------------------------- |
| Low-risk accounts               | Improved security            | Delivery reliability and security |
| Account recovery                | No passwords to remember     | Mobile number changes             |
| Limited access                  | User trust and adoption      | Phishing risks                    |
| Early stages of user onboarding | Frictionless user experience | Expired OTPs                      |

## FIDO2 (biometrics, passkeys, security keys)

Fast IDentity Online (FIDO) *(tooltip: \<div class="paragraph">
\<p>A set of open technical specifications developed by the FIDO Alliance for strong authentication.\</p>
\</div>)* 2 is an authentication standard developed by the [FIDO Alliance](https://fidoalliance.org/) that enables passwordless or step-up authentication using biometric data. FIDO2 is designed to enhance the security and user experience of online authentication by adding an additional authentication factor or by replacing traditional passwords with the following more secure and convenient methods:

* FIDO2 biometrics

  Incorporates biometric authentication techniques, such as fingerprint recognition, facial recognition, iris scanning, or voice recognition, to verify a user's identity. Instead of relying on static passwords, FIDO2 biometrics relies on unique biological characteristics that are difficult to replicate, providing a higher level of security against various authentication threats.

* FIDO2 passkeys

  Enable users the ability to sign on to their accounts by accessing their FIDO2 credentials on many of their devices that they've enrolled in multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
  \<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
  \</div>)*. Passkeys reduce the risk of phishing, all forms of password theft (including password spraying brute force attacks), and credential stuffing attacks.

* FIDO2 security keys

  Physical hardware devices used for strong authentication based on the FIDO2 standard. These devices are designed to provide a highly secure way for users to authenticate to online services and applications.

  | Use cases            | Benefits                     | Challenges                                      |
  | -------------------- | ---------------------------- | ----------------------------------------------- |
  | Online banking       | Enhanced security            | Biometric accuracy                              |
  | Healthcare records   | High phishing resistance     | Potential for spoofing and presentation attacks |
  | Government services  | Multi-platform compatibility | Data privacy and regulations                    |
  | E-commerce platforms | Privacy protection           | User acceptance                                 |

## Authenticator app (TOTP)

An authenticator app is a strong authentication method used to enhance security and streamline authentication by generating temporary OTPs. This method offers a convenient and secure method for implementing two-factor authentication, significantly enhancing the security of online accounts and protecting users from cyber threats, such as phishing attacks and credential theft.

| Use cases                      | Benefits                                                         | Challenges                                 |
| ------------------------------ | ---------------------------------------------------------------- | ------------------------------------------ |
| Time-based password generation | Enhanced security through short-lived passcodes                  | User adoption and education                |
| Multi-account support          | Better user experience                                           | Backup and recovery mechanisms             |
| Security                       | Strong encryption techniques                                     | Expired codes and usability issues         |
| Customization and branding     | Reduced dependency on less secure MFA methods (for example, SMS) | Technical issues impeding brand reputation |

## Voice (OTP)

Voice OTP is a strong authentication method that can be used as a step-up authentication request following a password. When initiated, the system sends a voice OTP to the user through a phone call to the number already associated with the account. After receiving the OTP, the user enters it in the relevant field before it expires. This method is highly accessible because all it requires is a phone.

| Use cases                       | Benefits                     | Challenges                        |
| ------------------------------- | ---------------------------- | --------------------------------- |
| Low-risk accounts               | Improved security            | Delivery reliability and security |
| Account recovery                | No passwords to remember     | Phone number changes              |
| Limited access                  | User trust and adoption      | Phishing risks                    |
| Early stages of user onboarding | Frictionless user experience | Expired OTPs                      |

## Mobile application

PingOne MFA has an SDK for mobile that allows you to integrate MFA capabilities into your mobile apps for Android and iOS. The mobile app can be either an authenticator-only app that handles second-factor authentication or a complete business app that handles the full user experience, meaning both access and authentication.

| Use cases                  | Benefits                                         | Challenges                                |
| -------------------------- | ------------------------------------------------ | ----------------------------------------- |
| Security                   | Strong encryption techniques                     | Expired codes and usability issues        |
| Customization and branding | Seamless native experience from your application | Requires additional development resources |