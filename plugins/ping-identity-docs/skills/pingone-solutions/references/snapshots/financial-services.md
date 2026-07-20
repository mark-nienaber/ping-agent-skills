---
title: About Financial Services
description: Learn about the purpose and configuration of the Financial Services.
component: pingone-solutions
page_id: pingone-solutions:financial-services:index
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/index.html
revdate: January 28, 2025
---

# About Financial Services

The Financial Services solution lets you offer your end users a secure way to make payments and transfers, as well as manage account and privacy settings, using a simple getting started experience and pre-built DaVinci flows.

This flow pack enables robust threat detection against bots, disposable email, and Adversary-in-the-Middle (AITM) attacks. It also analyzes risk signals to detect high, medium, and low threats to reduce the risk of account takeovers.

You can view additional information about the solution, including download links, in the Ping Identity Marketplace. Learn more at [Financial Services on the Marketplace](https://marketplace.pingone.com/item/financial-services-davinci-flow-pack).

Preparing the Financial Services solution involves configuration steps in PingOne and DaVinci:

* In PingOne, perform basic configuration to prepare the flows to be launched and enable features such as multi-factor authentication (MFA) and PingOne notifications.

* In DaVinci, configure variables and flow settings to customize the flow behavior for your environment and customers.

* Clone the flows for use in your production environment.

The Financial Services solution offers many of the available DaVinci capabilities. However, the solution limits the pre-built components to common use cases and selected best practices.

The solution includes a variety of authentication methods, such as email magic link, email and SMS OTP, FIDO2, voice, mobile applications, and Time-based One-Time Passwords (TOTPs).

|   |                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Financial Services solution offers pre-built flow templates and configurations. Review these components with your Ping Identity account representative to understand the limitations and risks associated with this solution. Your account representative can also help you customize the pre-built flow templates to satisfy any compliance or regulatory requirements that relate to your business. |

This solution uses PingOne and DaVinci. Learn more about managing users and other PingOne tasks in the [PingOne documentation](https://docs.pingidentity.com/pingone/p1_cloud__platform_main_landing_page.html). Learn more about customizing flows in the [DaVinci documentation](https://docs.pingidentity.com/davinci/davinci_landing_page.html).

---

---
title: Best Practices
description: Learn about how to effectively use the Financial Services.
component: pingone-solutions
page_id: pingone-solutions:financial-services:financial-services-best-practices
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/financial-services-best-practices.html
revdate: January 9, 2025
section_ids:
  select-an-appropriate-flow-timeout: Select an appropriate flow timeout
  clone-your-flows-before-using-or-customizing-them: Clone your flows before using or customizing them
  use-caution-when-customizing-flows: Use caution when customizing flows
---

# Best Practices

These guidelines help you make effective use of the Financial Services solution in your environment.

## Select an appropriate flow timeout

When you're configuring your DaVinci flows, you can set a timeout value for the flow as a whole. Because the user's account could be updated later by anyone with access to the device, a flow with a very long or indefinite timeout could be a security risk. Set a value that minimizes that risk.

## Clone your flows before using or customizing them

Flows with the original name can be updated by PingOne when we publish flow updates. These updates are not applied automatically, but they add a new latest version to each flow.

By cloning the flows before you apply any customization or use them with customers, you prevent any of your changes or customizations from being overwritten accidentally.

## Use caution when customizing flows

If you want to customize the flows in the Financial Services solution, do so carefully.

Clone the flows before making customizations so that:

* You can revert to the earlier versions if you encounter breaking changes.

* If you download an updated version of the solution, you don't overwrite your customizations.

Test your customizations in a test environment before importing them into your production environment. Because any additional nodes or flows you add are not part of the standard solution, you must test them to make sure that they're working as you intend.

---

---
title: Configuring flows in DaVinci
description: Learn about how to configure flows in DaVinci as part of the Financial Services.
component: pingone-solutions
page_id: pingone-solutions:financial-services:getting-started/financial-services-configuring-flows-in-davinci
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/getting-started/financial-services-configuring-flows-in-davinci.html
revdate: September 6, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
  result: Result:
  result-2: Result:
  choose-from-2: Choose from:
---

# Configuring flows in DaVinci

After you configure PingOne and test the solution using the wizard, perform additional configuration in DaVinci to enable all features and make the flows available to end users.

## Steps

1. Import the solution into your initial environment:

   1. Sign on to your production DaVinci environment and click **Flows**.

   2. Click **Add Flow > Import from JSON**.

   3. Select the JSON file containing the flows.

   4. Click **Import**.

2. Enter or verify the values for each company variable that's used in the Financial Services solution.

   These variables determine whether some processes and subflows are included or excluded.

   |   |                                                                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you plan to invoke the flow using the widget, you can pass in parameter values that override some of these variables. These parameters are described later in this procedure. |

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
      > | `ciam_requireMFA`              | A Boolean that controls whether MFA is required for all users.The default value is `true`.                                                                                                                                                                                                                                                                                             |
      > | `ciam_resendOtpLimit`          | The maximum number of times a user can resend an OTP.The default value is `5`.                                                                                                                                                                                                                                                                                                         |
      > | `ciam_magicLinkEnabled`        | A Boolean that controls whether magic links are enabled for your end users.The default value is `true`.                                                                                                                                                                                                                                                                                |
      > | `ciam_logoUrl`                 | The URL for the version of your company logo to display in flows.The default value is `https://assets.pingone.com/ux/ui-library/5.0.2/images/logo-pingidentity.png`.                                                                                                                                                                                                                   |
      > | `ciam_logoStyle`               | The CSS style to use for your company logo.The default value is `width: 65px; height:65px;`.                                                                                                                                                                                                                                                                                           |
      > | `ciam_companyName`             | The name of your company as it should be displayed in user-facing text.The default value is `Ping Identity`.                                                                                                                                                                                                                                                                           |
      > | `ciam_agreementEnabled`        | A Boolean that controls whether agreement is enabled in your environment.The default value is `true`.                                                                                                                                                                                                                                                                                  |
      > | `ciam_verificationLimit`       | The maximum number of times a user can attempt to verify their email address.The default value is `5`.                                                                                                                                                                                                                                                                                 |
      > | `ciam_protectAnalysisRequired` | A Boolean that controls whether PingOne Protect analysis is required.The default value is `true`.                                                                                                                                                                                                                                                                                      |

3. Verify the configuration of the following connectors in your environment:

   | Connector             | Description                                                                                                                                                                                                                                                                                        | Connector documentation                                                                                     |
   | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
   | PingOne               | Enables DaVinci to view and update PingOne user information.                                                                                                                                                                                                                                       | [PingOne connector](https://docs.pingidentity.com/connectors/p1_connector.html)                             |
   | PingOne MFA           | Enables DaVinci to use the PingOne MFA service for multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">&#xA;\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>&#xA;\</div>)*. | [PingOne MFA connector](https://docs.pingidentity.com/connectors/p1_mfa_connector.html)                     |
   | PingOne Notifications | Enables DaVinci flows to send users general communications using SMS, email, and voice message with PingOne's notifications feature.                                                                                                                                                               | [PingOne Notifications connector](https://docs.pingidentity.com/connectors/p1_notifications_connector.html) |
   | PingOne Protect       | Enables DaVinci flows to perform a threat assessment of the current user through PingOne Protect.                                                                                                                                                                                                  | [PingOne Protect connector](https://docs.pingidentity.com/connectors/p1_protect_connector.html)             |
   | PingOne Authorize     | Enables DaVinci flows to use PingOne Authorize for policy-based authorization decisions.                                                                                                                                                                                                           | [PingOne Authorize connector](https://docs.pingidentity.com/connectors/p1az_connector.html)                 |

   1. On the **Connectors** tab, find the connector that you want to verify and go to **…​ > Edit**.

   2. Verify that the **Environment ID**, **Client ID**, and **Region** field values match your PingOne values.

   3. (Optional) Copy the **Client Secret** from your PingOne environment to the **Client Secret** field.

   4. For the PingOne Authorize connector, verify that the **Endpoint** matches the one found in PingOne in the **Authorization > Decision Endpoints** section.

   5. If you made changes to the values, click **Apply**.

   6. Repeat the previous steps for each remaining connector.

4. Configure the **OOTB - Financial Services - Main Flow**:

   1. Click **Flows**.

   2. Select the **OOTB - Financial Services - Main Flow** and go to **…​ > Edit**.

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

5. (Optional) If you plan to use a mobile application, configure the **OOTB - Financial Services - Device Registration - Subflow**:

   1. Click **Flows**.

   2. Select the **OOTB - Financial Services - Device Registration - Subflow** and go to **…​ > Edit**.

   3. In the **Mobile App Registration Flow** section, click the **Create Pairing Key** node.

   4. In the **Applications** field, enter one or more application IDs to specify which applications can be used with the pairing key. If you do not specify one or more application IDs, all applications can be used.

6. Verify that the PingOne flow setting is correct for your environment.

   ### Choose from:

   * If you want to launch the Financial Services solution using a redirect, the flow must be configured as a PingOne flow.

   * If you want to launch the Financial Services solution using the widget, the flow must not be configured as a PingOne flow.

     1. Click **Flows**.

     2. Click the **OOTB - Financial Services - Main Flow** flow.

     3. Go to **[icon: ellipsis-v, set=fa]> Flow Settings**.

     4. If you plan to launch the flow through a redirect, click the **PingOne Flow** toggle.

     5. If you made changes to the flow settings, click **Save**, close the flow settings pane, and click**Deploy**.

7. Configure a DaVinci application that invokes the **OOTB - Financial Services - Main Flow**.

   Learn more in [Creating an application](https://docs.pingidentity.com/davinci/applications/davinci_creating_an_application.html) and [Configuring a flow policy](https://docs.pingidentity.com/davinci/applications/davinci_configuring_a_flow_policy.html) in the DaVinci documentation.

   1. On the **Applications** tab, click **Add Application**.

   2. In the **Name** field, enter a name for the application.

   3. Click **Create**.

   4. On the **Applications** tab, find the application that you created and click **Edit**.

   5. On the **Flow Policy** tab, click **Add Flow Policy**.

   6. In the **Name** field, enter a name for the flow policy.

   7. Select **PingOne Flow Policy** if you plan to invoke the flow using a PingOne redirect.

   8. In the **Flows** section, select the **OOTB - Financial Services - Main Flow**.

   9. In the **Version** section, select one or more versions of the flow to use.

   10. Click **Create Flow Policy**.

   11. In the **Distribution** field, set the weight for the selected flow to `100`.

   12. Click **Save Flow Policy**.

   13. Click **Apply**.

8. If you are using a test environment, move the flows to your production environment:

   1. In your testing environment, click **Flows**.

   2. Click the **OOTB - Financial Services - Main Flow** flow.

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

9. Invoke the flow or flows using the widget or a redirect.

   ### Choose from:

   * If you want to launch the flow in a separate window using a PingOne redirect, use the procedure in [Launching a PingOne flow with a redirect](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launch_flow_redirect.html) in the DaVinci documentation. The OOTB - Financial Services - Main Flow flow can be launched with a redirect.

   * If you want to launch the flow in a widget within the user's current window, use the procedure in [Launching a flow with the widget](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launching_a_flow_with_the_widget.html) in the DaVinci documentation. The **OOTB - Financial Services - Main Flow** can be launched with the widget.

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
     > | Parameter                 | Corresponding variable  | Description                                                              |
     > | ------------------------- | ----------------------- | ------------------------------------------------------------------------ |
     > | `isEmailMagicLinkEnabled` | `ciam_magicLinkEnabled` | A Boolean indicating whether magic links are enabled for your end users. |
     > | `isTermsOfServiceEnabled` | `ciam_agreementEnabled` | A Boolean indicating whether agreement is enabled in your environment.   |

---

---
title: Configuring PingOne for the Financial Services solution
description: Learn about how to configure PingOne as part of the Financial Services.
component: pingone-solutions
page_id: pingone-solutions:financial-services:getting-started/financial-services-configuring-p1
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/getting-started/financial-services-configuring-p1.html
revdate: September 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring PingOne for the Financial Services solution

Verify that your PingOne environment has the necessary configuration to run the Financial Services solution and enable all the features that you want to use.

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

2. Create or verify the required pre-generated notification templates in your PingOne environment.

   Learn more about adding and customizing notification templates in [Adding a notification](https://docs.pingidentity.com/pingone/user_experience/p1_add_notification.html) and [Editing a notification](https://docs.pingidentity.com/pingone/user_experience/p1_edit_notification.html) in the PingOne documentation.

   1. Click one of the template links to view the corresponding template in the Ping Library:

      * [Account Disabled](https://library.pingidentity.com/page/ciam-plus-account-disabled-notification-template)

      * [Magic Link Authentication](https://library.pingidentity.com/page/ciam-plus-magic-link-authentication-notification-template)

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

      | Notification Template       | Subject                   |
      | --------------------------- | ------------------------- |
      | Account Disabled            | Critical security alert   |
      | Magic Link Authentication   | Magic link authentication |
      | New Device Sign-in Activity | Security alert            |
      | Password Changed            | Password change           |
      | Suspicious Activity         | Security alert            |

   9. Click the **[icon: check, set=fa]**icon to save the subject changes.

   10. Click the **Edit** icon in the **New Email** field, then paste the template HTML you copied in step b.

   11. Click the **Save** icon to save the field changes.

   12. Click the **X** icon to close the template.

   13. Repeat steps a - l for each remaining template.

3. Create the **Money Transfer/Payment Request** template:

   1. In PingOne, go to **User Experience > Notification Templates**.

   2. Click **[icon: plus, set=fa]**to create a new template.

   3. In the **Type** list, select **General**.

   4. In the **Name** field, enter `Money Transfer/Payment Request`.

   5. Click **Create**.

   6. In the **Subject** field, configure a subject:

      1. Click the **Pencil** icon.

      2. Enter the subject `Action Required: ${flowType} Request`.

      3. Click the **[icon: check, set=fa]**icon.

   7. In the **New Email** field, configure the message body:

      1. Click the **Pencil** icon.

      2. Enter a body for the new transaction message. For example:

         ```html
         <div style="display: block; width: 400px; margin: 0 auto; font-family: sans-serif; padding: 30px 20px; text-align: center;">
             <img src="https://assets.pingone.com/ux/ui-library/5.0.2/images/logo-pingidentity.png" alt="Company Logo" style="height: 65px; margin-bottom: 10px" />
             <h1>${flowType} Request</h1>
             <div style="margin-top: 20px; margin-bottom:25px; text-align:left">
                 <p> A request for ${flowType} of ${currency}${amount} from ${moneyFrom} to ${moneyTo} has been made. If this wasn't you, do not approve this ${flowType} and change your password.</p>
                 <p>
                     <a href=${magicLink}>
                         <button style="color: #fff; background-color: #007bff;
         border: 1px solid transparent; padding: .375rem
         .75rem; border-radius: .25rem ">Approve ${flowType}</button>
                     </a>
                 </p>
             </div>
         </div>
         ```

      3. Click the **[icon: check, set=fa]**icon.

   8. Click **X** to close the template.

4. Update the content of the existing **New Device Paired** notification template:

   1. Open the [New Device Paired](https://library.pingidentity.com/page/ciam-plus-new-device-paired-notification-template) template entry in the Ping Library.

   2. Click **Copy** to copy the template HTML.

   3. In PingOne, go to **User Experience > Notification Templates**.

   4. Find the **New Device Paired** notification template and click **⋮ > Edit**.

   5. In the **New Email** field, click the **Pencil** icon, then paste the template HTML you copied in step b.

   6. Click the **Save** icon to save the field changes.

   7. Click the **X** icon to close the template.

5. Verify that you have a multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
   \<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
   \</div>)* policy configured in PingOne.

   Learn more in the PingOne [MFA policies](https://docs.pingidentity.com/pingone/authentication/p1_mfa_policies.html) documentation.

   1. In PingOne, go to **Authentication > MFA**.

   2. Click the MFA policy marked as the default and verify that its **Allowed Authentication Methods** include the authentication methods that you want to use from the following:

      * **Email**

      * **SMS**

      * **FIDO2**

      * **Voice**

      * **TOTP**

      * **Mobile**

6. Verify that the default population exists:

   1. Go to **Directory > Populations**.

   2. In the list of populations, verify that a population is marked as **Default**.

   3. If no existing population is marked as **Default**, select a population and go to **More options ( [icon: ellipsis-v, set=fa]) > Edit Population**.

   4. Click **Make Default Population**.

   5. Click **Switch**.

   6. Click **Save**.

7. Add the attributes required for the solution.

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | These attributes must be populated for the Financial Services to function correctly. |

   1. Go to **Directory > User Attributes**.

   2. Click the [icon: plus, set=fa]icon.

   3. Click **Declared**.

   4. Click **Next**.

   5. Enter the information for one of the following attributes:

      | Name                   | Display Name           | Description                                                               |
      | ---------------------- | ---------------------- | ------------------------------------------------------------------------- |
      | `minPaymentLimit`      | `minPaymentLimit`      | The user's minimum payment size.                                          |
      | `maxPaymentLimit`      | `maxPaymentLimit`      | The user's maximum payment size.                                          |
      | `currency`             | `currency`             | The currency symbol for the user's locale.                                |
      | `userPaymentOnline`    | `userPaymentOnline`    | Indicates whether online transactions are enabled or disabled.            |
      | `userPaymentThreshold` | `userPaymentThreshold` | A threshold above which approval is required for transfer and payment.    |
      | `userPaymentLimit`     | `userPaymentLimit`     | A limit above which online payment or transfer requests are denied.       |
      | `checkingBalance`      | `checkingBalance`      | The user's checking account balance.                                      |
      | `savingsBalance`       | `savingsBalance`       | The user's savings account balance.                                       |
      | `accountVisibility`    | `accountVisibility`    | Contains user preferences for sharing data with third parties.            |
      | `mortgageAccount`      | `mortgageAccount`      | Contains user mortgage account data including balance and account number. |
      | `creditCardAccount`    | `creditCardAccount`    | Contains user credit card data including balance and account number.      |

   6. Click **Save**.

   7. Repeat steps b - f for each remaining attribute.

   8. Populate these attributes with values for each user. Learn more in the [PingOne User Attribute documentation](https://docs.pingidentity.com/pingone/directory/p1_user_attributes.html).

8. (Optional) If you plan to use PingOne Protect and you don't want to use the default risk policy, create a new risk policy according to the [PingOne Protect documentation](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_adding_risk_policy.html).

9. Create a PingOne Authorize policy:

   1. Go to **Authorization > Policies**.

   2. Click the **Plus** icon and select **Add Policy**.

   3. In the **Name** field, enter `Payment checks`.

   4. Add a maximum payment rule:

      1. Click **+ Add Rule**.

      2. In the **Name** field, enter **Deny payments over maximum payment limit**.

      3. In the hamburger menu, click **Add "Applies When"**.

      4. In the **Applies When** section, click **Comparison**, then enter the parameters `Amount`, `Greater Than`, and `PingOne.User.userPaymentLimit`.

      5. In the **Effect** list, select **Deny**.

      6. Click **Save Changes**.

   5. Add a rule to allow payments between the minimum and the maximum threshold:

      1. Click **+ Add Rule**.

      2. In the **Name** field, enter `Permit payment more than minimum payment limit and less than threshold limit`.

      3. In the hamburger menu, click **Add "Applies When"**.

      4. In the **Applies When** section, click **Comparison**, then enter the parameters `Amount`, `Greater Than`, and `PingOne.User.userPaymentThreshold`.

      5. In the **Applies When** section, click **Comparison**, then enter the parameters `Amount`, `Less Than or Equal`, and `PingOne.User.userPaymentLimit`.

      6. In the **Effect** list, select **Permit**.

      7. Click **Save Changes**.

   6. Add a maximum payment rule:

      1. Click **+ Add Rule**.

      2. In the **Name** field, enter `Require approval for payment more than payment threshold limit`.

      3. In the hamburger menu, click **Add "Applies When"**.

      4. In the **Applies When** section, click **Comparison**, then enter the parameters `Amount`, `Less Than or Equal`, and `PingOne.User.userPaymentThreshold`.

      5. In the **Effect** list, select **Permit**.

      6. Click **+ Add Statement**.

      7. In the **Name** field, enter `Approval required when amount more than threshold limit`.

      8. Click **Save Changes**.

10. Add the transaction amount as an attribute:

    1. Go to **Authorization > Trust Framework**.

    2. Click the plus icon and select **Add Policy**.

    3. Click the **Attributes** tab, then click **Create new Attribute**.

    4. In the **Name** field, enter `Amount`.

    5. Click **Add Resolver** and select the **Request Parameter** resolver type.

    6. In the **Type** list, select **Number**.

    7. Click **Save Changes**.

11. (Optional) If you plan to use FIDO2, verify that the default **Passkeys** policy is selected.

    Learn more about FIDO policies in the [PingOne FIDO policies](https://docs.pingidentity.com/pingone/authentication/p1_fido_policies.html) documentation.

    1. Go to **Authentication > FIDO**.

    2. Verify that the **Passkeys** policy is set as the default.

    3. If the **Passkeys** policy is not the default, go to **⋮ > Make Default**, then click **Save**.

12. (Optional) If you plan to use an agreement, verify that you have an agreement configured in PingOne and copy the agreement ID.

    Learn more about configuring agreements in [Adding an agreement](https://docs.pingidentity.com/pingone/user_experience/p1_add_an_agreement.html) in the PingOne documentation.

    1. Go to **User Experience > Agreements**.

    2. Verify that the agreement exists and is enabled.

    3. Click the agreement to open the details panel.

    4. On the **API** tab, copy the **ID**.

    The agreement ID is used in a later procedure to configure the flows in DaVinci.

13. (Optional) Verify that you have an external identity provider (IdP) configured in PingOne for each valid third party you want to use as a social sign-on option.

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
title: Financial Services Release Notes
description: Learn about changes to the Financial Services.
component: pingone-solutions
page_id: pingone-solutions:financial-services:release-notes/financial-services-release-notes
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/release-notes/financial-services-release-notes.html
revdate: June 28, 2024
section_ids:
  may-29: May 29
  initial-release: Initial Release
---

# Financial Services Release Notes

New features and improvements in Financial Services.

Subscribe to get automatic updates: [icon: rss-square, set=fa][Financial Services Release Notes RSS feed](release-notes/financial-services-release-notes.xml)

## May 29

### Initial Release

New

This is the initial release of the Financial Services solution.

---

---
title: Flow Reference
description: Learn about the flows included in the Financial Services and find links to reference documentation about them.
component: pingone-solutions
page_id: pingone-solutions:financial-services:flow-reference/financial-services-flow-reference
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/flow-reference/financial-services-flow-reference.html
revdate: January 29, 2025
page_aliases: ["flow-reference/index.adoc"]
---

# Flow Reference

The Financial Services solution uses a main flow and multiple subflows. This section explains what each flow does and how it works.

A DaVinci flow consists of nodes, each of which presents a page to the user, performs a backend action, or launches another flow. These nodes are connected by logical operators, allowing you to construct a user journey such as authenticating with a known device or making a transfer.

The flows included in the Financial Services solution are designed to work together to provide the solution. They require no configuration beyond that described in [Configuring flows in DaVinci](../getting-started/financial-services-configuring-flows-in-davinci.html). However, you can customize these flows to provide additional services to your end users. Learn more in [How To Manage Flows](https://docs.pingidentity.com/davinci/flows/davinci_how_to_manage_existing_flows.html) in the DaVinci documentation.

The main section of the Financial Services solution contains the following flows:

* [OOTB - Financial Services - Main Flow](financial-services-main-flow.html)

  This flow is the beginning of the financial services process. It's meant to be invoked directly.

* [OOTB - Financial Services - Account Settings Subflow](financial-services-account-settings-subflow.html)

  This flow lets users update their account settings.

* [OOTB - Financial Services - Agreement (ToS) - Subflow](financial-services-agreement-tos-subflow.html)

  This flow lets users read and agree to any agreements required by the environment.

* [OOTB - Financial Services - Change Password - Subflow](financial-services-change-password-subflow.html)

  This flow lets users change their password.

* [OOTB - Financial Services - Device Authentication - Subflow](financial-services-device-authentication-subflow.html)

  This flow lets users authenticate using a known device.

* [OOTB - Financial Services - Device Registration - Subflow](financial-services-device-registration-subflow.html)

  This flow lets users register a new device.

* [OOTB - Financial Services - Magic Link Authentication - Subflow](financial-services-magic-link-authentication-subflow.html)

  This flow lets users authenticate using a magic link.

* [OOTB - Financial Services - Make Payment Subflow](financial-services-make-payment-subflow.html)

  This flow lets users make a payment.

* [OOTB - Financial Services - Make Transfer Subflow](financial-services-make-transfer-subflow.html)

  This flow lets users make a transfer.

* [OOTB - Financial Services - Manage Account Subflow](financial-services-manage-account.html)

  This flow lets users manage their account.

* [OOTB - Financial Services - Privacy Settings Subflow](financial-services-privacy-settings-subflow.html)

  This flow lets users update their privacy settings.

* [OOTB - Financial Services - SignOn - Subflow](financial-services-signon-subflow.html)

  This flow lets users sign on.

* [OOTB - Financial Services - Threat Detection - Subflow](financial-services-threat-detection-subflow.html)

  This flow uses PingOne Protect to perform a threat assessment of the user.

* [OOTB - Financial Services - Transfer Approval via Email - Subflow](financial-services-transfer-approval-via-email.html)

  This flow lets users provide approval for transfers or payments through a known email.

* [OOTB - Financial Services - Verify Email - Subflow](financial-services-verify-email-subflow.html)

  This flow lets users verify their email address using PingOne SSO.

---

---
title: Getting Started
description: Learn about how to configure PingOne and DaVinci for the Financial Services.
component: pingone-solutions
page_id: pingone-solutions:financial-services:getting-started/financial-services-getting-started
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/getting-started/financial-services-getting-started.html
revdate: May 29, 2024
page_aliases: ["getting-started/index.adoc"]
---

# Getting Started

There are two configuration stages for the Financial Services solution.

To get started with the solution:

1. [Configure the settings in PingOne](financial-services-configuring-p1.html).

2. [Perform additional configuration in DaVinci to begin using the solution](financial-services-configuring-flows-in-davinci.html).

---

---
title: OOTB - Financial Services - Account Settings Subflow
description: Learn about the OOTB - Financial Services - Account Settings Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:financial-services:flow-reference/financial-services-account-settings-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/flow-reference/financial-services-account-settings-subflow.html
revdate: July 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# OOTB - Financial Services - Account Settings Subflow

The **OOTB - Financial Services - Account Settings Subflow** lets users update account settings.

## Purpose

The **OOTB - Financial Services - Account Settings Subflow** presents users with a form that lets them change their account settings including payment limits and whether online transactions are enabled. The user's updated settings are saved by PingOne.

## Structure

This flow is divided into sections using teleport nodes:

* **OOTB - Financial Services - Account Settings Subflow**

  A function node sets flow variables, and a PingOne node verifies that the user exists. An HTML node then presents the user with account management options.

  If the user cancels, the flow progresses to the **Return Success** section.

  If the user submits the form, a function node validates the responses, and a PingOne node verifies that the user exists. The flow then branches based on the user's selection:

  * If the user enabled online transactions, a PingOne node saves the user attributes, and a success message displays. The flow then progresses to the **Return Success** section.

  * If the user disabled online transactions, a PingOne node saves the user attributes, and a warning message displays indicating that online transactions are disabled. The flow then progresses to the **Return Success** section.

* **Return Success**

  Sends a success JSON response, indicating that the flow completed successfully.

* **Return Error**

  Uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input name    | Required | Description                                            |
| ------------- | -------- | ------------------------------------------------------ |
| `p1UserId`    | Yes      | The current user's PingOne user ID.                    |
| `companyLogo` | No       | The company logo to display in user-facing HTML pages. |
| `flowMethod`  | No       | The flow method.                                       |

## Output schema

This flow has the following outputs:

| Output Name     | Description                                   |
| --------------- | --------------------------------------------- |
| `subflowResult` | The result status of the flow.                |
| `errorMessage`  | The error message to pass to the parent flow. |
| `errorDetails`  | The details of the error that occurred.       |

## Variables and parameters

This flow uses the following variable or parameter values:

| Parameter name         | Description                                                                                                 |
| ---------------------- | ----------------------------------------------------------------------------------------------------------- |
| `p1UserId`             | The current user's PingOne user ID.                                                                         |
| `minPaymentLimit`      | The minimum payment size for the user.                                                                      |
| `maxPaymentLimit`      | The maximum payment size for the user.                                                                      |
| `currency`             | The currency symbol for the user's locale.                                                                  |
| `userPaymentOnline`    | Indicates whether online transactions are enabled or disabled.                                              |
| `userPaymentThreshold` | A threshold above which payments and transfers require approval.                                            |
| `userPaymentLimit`     | The maximum size of online payments or transfers. Online payments or transfers above this limit are denied. |

---

---
title: OOTB - Financial Services - Agreement (ToS) - Subflow
description: Learn about the OOTB - Financial Services - Agreement (ToS) - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:financial-services:flow-reference/financial-services-agreement-tos-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/flow-reference/financial-services-agreement-tos-subflow.html
revdate: May 29, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# OOTB - Financial Services - Agreement (ToS) - Subflow

The **OOTB - Financial Services - Agreement (ToS) - Subflow** lets users read and confirm any agreement required in your environment.

## Purpose

The **OOTB - Financial Services - Agreement (ToS) - Subflow** determines whether the user needs to consent to an agreement. If so, it displays the agreement for the user and stores the user's consent if they consent to the agreement.

## Structure

This flow is divided into sections using teleport nodes:

* **Check if agreement form needs to be displayed**

  Uses comparison nodes to check if agreement is enabled in the environment and if agreement is necessary for the current user. If so, a PingOne node checks the user's consent status.

  If consent isn't present, the flow progresses to the **Present & Accept Agreement** section.

  If consent is present, a function node checks if a success message should be displayed. The flow progresses to the **Present & Accept Agreement** if a success message should be displayed, and to the **Return Success** section if a success message should not be displayed.

* **Present & Accept Agreement**

  Uses a PingOne node to retrieve the required agreement, then presents the user with an HTML page. If the user has not yet agreed, this page lets them review and accept or decline the agreemnt. If the user has agreed, the form displays a success message, then the flow progresses to the **Return Success** section.

  If the user accepts the agreement, a PingOne node stores the user's agreement. The flow then returns to the beginning of the **Present & Accept Agreement** section if a success message should be displayed, and to the **Return Success** section if a success message should not be displayed.

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

| Output Name     | Description                                   |
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
title: OOTB - Financial Services - Change Password - Subflow
description: Learn about the OOTB - Financial Services - Change Password - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:financial-services:flow-reference/financial-services-change-password-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/flow-reference/financial-services-change-password-subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# OOTB - Financial Services - Change Password - Subflow

The **OOTB - Financial Services - Change Password - Subflow** lets users change their passwords.

## Purpose

The **OOTB - Financial Services - Change Password - Subflow** displays a password reset form, letting users enter their current password and enter and verify a new password. If the new passwords match, the user's password is updated in PingOne.

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

| Output Name     | Description                                   |
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
title: OOTB - Financial Services - Device Authentication - Subflow
description: Learn about the OOTB - Financial Services - Device Authentication - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:financial-services:flow-reference/financial-services-device-authentication-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/flow-reference/financial-services-device-authentication-subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# OOTB - Financial Services - Device Authentication - Subflow

The **OOTB - Financial Services - Device Authentication - Subflow** lets users authenticate using a known device.

## Purpose

The **OOTB - Financial Services - Device Authentication - Subflow** enables users to authenticate using a known device. The flow evaluates the devices associated with the user account, invoking the **OOTB - Financial Services - Magic Link Authentication - Subflow** flow if necessary. It then enables the user to select an authentication method and authenticates the user with the selected method.

## Structure

This flow is divided into sections using teleport nodes:

* **Gather Browser And Devices Data**

  Uses a PingOne node to gather the user's existing devices. Next, an HTML node evaluates the user's browser to determine if biometrics are available. The flow then progresses to the **Filter and Mask Devices** section.

* **Filter and Mask Devices**

  Filters the list of available devices to create a list of usable devices, then masks the device information so that the devices can be identified without displaying the full device information. The flow then progresses to the **Check If MFA Enabled And Any Device Active** section.

* **Check If MFA Enabled And Any Device Active**

  Uses a PingOne node to check the user's multi-factor authentication (MFA) status. If MFA is enabled and the user has active devices, the flow progresses to the **Decide Authentication Path Based On MFA Policy** section. If MFA is not enabled or the user has no active devices, the flow progresses to the **Call Magic Link Authentication** section.

* **Decide Authentication Path Based On MFA Policy**

  Uses a PingOne node to begin MFA. If an assertion or a one-time passcode (OTP) is required, the flow progresses to the **Default Device Enrichment** section. If the user has multiple devices, or if the user has only one usable device and magic link is enabled, the flow progresses to the **Device Selection** section. If the user has one usable device and magic link is not enabled, the flow progresses to the **Default Device Enrichment** section.

* **Call Magic Link Authentication**

  Invokes the **OOTB - Financial Services - Magic Link Authentication - Subflow** flow if magic link authentication is enabled. The flow then progresses to the **Return Success** section.

* **Device Selection**

  Presents the user with an HTML page on which they can select a device.

  * If the user selected magic link, the **OOTB - Financial Services - Magic Link Authentication - Subflow** flow is invoked, and the flow then progresses to the **Return Success** section or to the **Device Selection** section depending on the subflow results.

  * If the user selected another authentication method, a PingOne records their selection and the flow progresses to the **Default Device Enrichment** section.

* **Default Device Enrichment**

  Uses a function node to enrich the device details, then the flow progresses to the **Handle TOTP, SMS, Voice, Mobile and Email OTP Authentication** section if an OTP is required, to the **Handle FIDO2 Authentication** section if assertion is required, or to the **Start Mobile Push** section if push confirmation is required.

* **Handle TOTP, SMS, Voice, Mobile and Email OTP Authentication**

  Uses function nodes to begin tracking the number of attempts and check the device type, then presents the user with an HTML page with options to enter the passcode, change devices, or resend the OTP.

  * If the user selects resend, the number of resend attempts is incremented and compared to the maximum. If the maximum hasn't been reached, a PingOne node resends the OTP and a confirmation message displays.

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

  * If the user retries, a PingOne MFA node performs device selection, and the flow returns to the **Mobile Push Flow** section.

  * If the user cancels, the flow progresses to the **Device Selection** section.

  * If the user submits an OTP, a PingOne MFA node checks the device passcode. A function node then saves the authentication method as a variable, and the flow progresses to the **Return Success** section.

* **Mobile App Timed Out**

  Displays an error screen which presents the user with multiple options.

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

| Output Name     | Description                                                             |
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
title: OOTB - Financial Services - Device Registration - Subflow
description: Learn about the OOTB - Financial Services - Device Registration - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:financial-services:flow-reference/financial-services-device-registration-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/flow-reference/financial-services-device-registration-subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# OOTB - Financial Services - Device Registration - Subflow

The **OOTB - Financial Services - Device Registration - Subflow** lets users register a new device.

## Purpose

The **OOTB - Financial Services - Device Registration - Subflow** presents users with options to register any available device type. The flow finds the available devices, then uses an HTML node to let the user select one of the following options:

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

* **Gather device types that user can register with**

  Uses a PingOne node to retrieve the user's current devices, then uses a hidden HTML form to gather browser information. If the user has compatible devices and can register at least one device, the flow progresses to the **Check Whether MFA Greetings Required To Be Displayed To User?** section.

* **Check Whether MFA Greetings Required To Be Displayed To User?**

  Uses a function node to check if the greeting page should be displayed.

  If the greeting should be displayed, an HTML node asks for user consent to add an MFA device. If the user clicks **Skip** or **Back**, the flow progresses to the **Return Success** section.

  If the user does not select **Skip** or **Back**, or if the greeting page isn't displayed, a function node checks whether the user's email is known. If the user's email address isn't known, the flow progresses to the **User select device to register with** section.

  If the user's email address is known, a function node checks whether direct enrollment of the user's email is requested. If direct enrollment isn't requested, the flow progresses to the **User select device to register with** section. If direct enrollment is requested, function nodes verify that the email address isn't in use and set the `canEnrollOnlyEmail` variable to true, then the flow progresses to the **Prepare to register OTP device** section.

* **User select device to register with**

  Presents the user with an HTML page that provides them with the available authentication method options.

  If the user selects **Voice** or **SMS**, the flow progresses to the **User selected SMS/VOICE** section.

  If the user selects **Email**, the flow progresses to the **User selected email** section.

  If the user selects **TOTP**, the flow progresses to the **Prepare to register OTP device** section.

  If the user selects **FIDO2**, the flow progresses to the **Register FIDO2 device and enable MFA for user** section.

  If the user selects **Mobile**, the flow progresses to the **Mobile app registration flow** section.

  If the user selects **Cancel**, a function node determines whether MFA is required. If MFA is required, the flow progresses to the **Return Success** section with the `cancel` result. If MFA isn't required, the flow progresses to the **Return Success** section with the `skip` result.

* **User selected SMS/VOICE**

  Displays an HTML page gives the user the option to provide a voice or SMS number.

  If the user enters a voice or SMS number, a function node verifies that the number isn't in use, then the flow progresses to the **Prepare to register OTP device** section.

  If the user clicks **Cancel**, the flow returns to the **User select device to register with** section.

* **User selected email**

  Uses a function node to check for a known user email.

  If the user's email isn't present, an HTML node lets the user enter an email and submit it or cancel.

  If the user clicks **Cancel**, the flow returns to the **User select device to register with** section.

  If the user submits an email, or if their email is already present, a function node verifies that the email isn't already registered. If the email isn't already registered, the flow progresses to the **Prepare to register OTP device** section. If the email is already registered, a function node determines the correct error message to display.

* **Prepare to register OTP device**

  Uses a PingOne node to create an OTP device.

  If the OTP device creation succeeds, a function node sets the device ID, then the flow progress to the **TOTP (Authenticator app) registration flow** section if the device type is TOTP, or to the **Ask for OTP** section if the device is SMS, voice, or email.

  If the OTP device creation fails, an error message displays.

* **Ask for OTP**

  Uses function nodes to begin tracking the number of resend attempts, mask the phone number or email, and determine the cancel behavior, then displays an HTML node prompting the user for the OTP.

  If the user submits a code, the flow progresses to the **Activate OTP device and enable MFA for user** section. Otherwise, the flow progresses to the **Resend OTP** section.

* **Resend OTP**

  If the user clicks **Resend** at the OTP prompt screen, function nodes increment the resend attempts and check if the maximum has been reached. If the maximum hasn't been reached, PingOne nodes delete the previous OTP device and create a new device, a function node updates the device ID, and a message displays for the user.

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

---

---
title: OOTB - Financial Services - Magic Link Authentication - Subflow
description: Learn about the OOTB - Financial Services - Magic Link Authentication - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:financial-services:flow-reference/financial-services-magic-link-authentication-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/flow-reference/financial-services-magic-link-authentication-subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# OOTB - Financial Services - Magic Link Authentication - Subflow

The **OOTB - Financial Services - Magic Link Authentication - Subflow** lets existing users authenticate using a link sent to the email address that's associated with their account.

## Purpose

The **OOTB - Financial Services - Magic Link Authentication - Subflow** presents users with the option to send a magic link to the email address associated with their account. After the link is sent, the flow checks the status of the link.

* If the user clicks the link, the flow authenticates the user.

* If the link expires, the flow presents an error message. The magic link expires after 2.5 minutes (150 seconds).

## Structure

This flow is divided into sections using teleport nodes:

* **Display Magic Link Form**

  Uses a PingOne node to look up the user, then presents an HTML form from which the user can send a magic link. If the user clicks **Submit**, the flow simultaneously progresses to the **Create Challenge and Send Email** and **Challenge Acceptance By The User** sections. If the user clicks **Cancel**, the flow progresses to the **Return Success** section.

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

| Input name        | Required | Description                                                                  |
| ----------------- | -------- | ---------------------------------------------------------------------------- |
| `p1UserId`        | Yes      | The user ID of the user to be authenticated.                                 |
| `canChangeDevice` | Yes      | Indicates whether the user can change the device used for authentication.    |
| `companyLogo`     | No       | The company logo.Used only when the main flow was launched using a redirect. |

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
title: OOTB - Financial Services - Main Flow
description: Learn about the OOTB - Financial Services - Main Flow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:financial-services:flow-reference/financial-services-main-flow
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/flow-reference/financial-services-main-flow.html
revdate: July 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# OOTB - Financial Services - Main Flow

The OOTB - Financial Services - Main Flow lets users manage account properties and make payments and transfers.

## Purpose

The OOTB - Financial Services - Main Flow is the initial flow in the Financial Services solution. It performs a PingOne Protect assessment using the **OOTB - Financial Services - Threat Detection - Subflow** and enables users to sign on. It then presents users with forms that let them manage account and privacy settings and make payments and transfers.

## Structure

This flow is divided into sections using teleport nodes:

* **Flow Configuration**

  Uses multiple function nodes to save the variable and parameter values so that the correct values are available in the flow and in subflows. The flow then progresses to the **Check Session, Call To Protect Analysis & MFA Step-Up** section.

* **Check Session, Call To Protect Analysis & MFA Step-Up**

  Uses a PingOne node to determine whether the user has an existing session.

  If the user has a session:

  1. A hidden HTML node captures risk information and a PingOne node fetches additional user information.

  2. The flow progresses to the **Threat Detection and Mitigation** section, then returns when this section completes.

  3. A function node checks if the user's account is enabled, and if so, the flow progresses to the **Manage Account** section.

  If the user doesn't have a session:

  1. The flow checks for any existing session tokens and uses a PingOne node to delete the prior session.

  2. The flow invokes the **OOTB - Financial Services - SignOn - Subflow**.

  3. When the subflow completes, a function node saves the protect risk level and a PingOne node creates a session for the user.

  4. A loading screen displays for the user.

  5. A PingOne node retrieves user information.

  6. The flow progresses to the **Manage Account** section.

* **Threat Detection & Mitigation**

  Uses a function node to check whether PingOne Protect analysis is required.

  If PingOne Protect analysis isn't required, the flow returns to the **Check Session, Call To Protect Analysis & MFA Step-Up** section.

  If PingOne Protect analysis is required, the flow invokes the **OOTB - Financial Services - Threat Detection - Subflow**.

  If the **OOTB - Financial Services - Threat Detection - Subflow** completes successfully, a function node stores the risk evaluation as a variable, then a second function node branches the flow based on the risk level:

  * If the risk level is low, the flow returns to the **Check Session, Call To Protect Analysis & MFA Step-Up** section.

  * If the risk level is medium, the flow progresses to the **MFA Authentication** section. When this section completes, the flow returns to the **Check Session, Call To Protect Analysis & MFA Step-Up** section.

  * If the risk level is high, a function nodes checks if the high risk was the result of a new device. If not, a PingOne node notifies the user of the suspicious activity. A PingOne node deletes the user session. The flow then progresses to the **Check Session, Call To Protect Analysis & MFA Step-Up** section.

  If the **OOTB - Financial Services - Threat Detection - Subflow** completes unsuccessfully, a function node stores the risk evaluation ID and an error message displays.

* **MFA Authentication**

  A PingOne node retrieves the user's existing devices, and a hidden HTML node gathers information about biometrics and security keys.

  Function nodes then filter the user's active devices and verify that the user has at least one active device. If the devices couldn't be filtered or if the user has no active devices, the flow progresses to the **Step Up To Register Email MFA Device, If No MFA Devices Found During Authentication** section.

  If the user has active devices, the **OOTB - Financial Services - Device Authentication - Subflow** is invoked. The flow then splits by the subflow result.

  * If the **OOTB - Financial Services - Device Authentication - Subflow** completed successfully, a function node stores the authentication method as a variable. The flow then returns to the previous section.

  * If the **OOTB - Financial Services - Device Authentication - Subflow** was canceled, the flow returns to the previous section.

* **Step Up To Register Email MFA Device, If No MFA Devices Found During Authentication**

  A function node checks whether verification is required for the account.

  * If verification isn't required, the **OOTB - Financial Services - Device Registration - Subflow** is invoked. The flow then splits based on the subflow result.

    * If the subflow result was `COMPLETE`, the authentication method is stored as a variable, then the flow returns to the **MFA Authentication** section.

    * If the subflow result was `SKIP`, the flow returns to the **MFA Authentication** section.

  * If verification is required, the **OOTB - Financial Services - Verify Email - Subflow** is invoked. If the subflow completes successfully, PingOne nodes enroll email as an MFA device and enable MFA for the user. A function node stores the authentication method as a variable, then the flow returns to the **MFA Authentication** section.

* **Manage Account**

  A PingOne node verifies that the user exists and a function node verifies that the user has all necessary attributes.

  * If the user has all necessary attributes, the **OOTB - Financial Services - Manage Account Subflow** is invoked. The flow then progresses to the **Return Success** section.

  * If the user does not have all necessary attributes, a PingOne node deletes the session.

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
| `Result`       | The result status of the flow.                                                                                         |
| `errorMessage` | The error message returned by the flow. Sent only if the flow progressed to the **Return Error** section.              |
| `errorDetails` | The detailed error information returned by the flow. Sent only if the flow progressed to the **Return Error** section. |

## Variables and parameters

This flow uses the following variable or parameter values:

| Variable name                  | Description                                                                                                    |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| `flowCompanyLogo`              | The URL for your company logo.                                                                                 |
| `p1MFAPolicyId`                | The ID of the PingOne MFA policy to use in the flow.                                                           |
| `p1AgreementId`                | The ID of the agreement to present to users.                                                                   |
| `p1RiskPolicyIdAuthn`          | The PingOne risk policy ID to use for authentication.                                                          |
| `p1RiskPolicyIdAR`             | The PingOne risk policy ID to use for account recovery.                                                        |
| `p1RiskPolicyIdAuthZ`          | The PingOne risk policy ID to use for authorization.                                                           |
| `p1RiskPolicyIdReg`            | The PingOne risk policy ID to use for registration.                                                            |
| `protectRiskEvalId`            | The risk ID of the current user as used by PingOne Protect.                                                    |
| `authMethod`                   | The authentication method used in the flow.                                                                    |
| `flowProtectAnalysisRequired`  | Indicates whether a PingOne Protect analysis must be performed for all users.                                  |
| `ciam_magicLinkEnabled`        | Indicates whether magic link authentication is enabled.                                                        |
| `ciam_agreementEnabled`        | Indicates whether the agreement is required.                                                                   |
| `ciam_protectAnalysisRequired` | Indicates whether PingOne Protect analysis is required.                                                        |
| `ciam_logoUrl`                 | The URL for your company logo.This value is used only when the flow is launched with a redirect.               |
| `ciam_companyName`             | Displays the name of your company.This value is used only when the flow is launched with a redirect.           |
| `ciam_logoStyle`               | The HTML style to use for your company logo.This value is used only when the flow is launched with a redirect. |
| `flowMethod`                   | The method used to launch the flow.                                                                            |

---

---
title: OOTB - Financial Services - Make Payment Subflow
description: Learn about the OOTB - Financial Services - Make Payment Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:financial-services:flow-reference/financial-services-make-payment-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/flow-reference/financial-services-make-payment-subflow.html
revdate: July 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# OOTB - Financial Services - Make Payment Subflow

The **OOTB - Financial Services - Make Payment Subflow** lets users make a payment.

## Purpose

The **OOTB - Financial Services - Make Payment Subflow** presents users with a form for making payments. It then uses PingOne Authorize to approve before using PingOne to update the user information. If additional approval is required, it invokes the **OOTB - Financial Services - Transfer Approval via Email - Subflow** subflow.

## Structure

This flow is divided into sections using teleport nodes:

* **OOTB - Financial Services - Make Payment Subflow**

  Uses a function node to set flow variables, then uses a PingOne node to verify that the user exists. An HTML node then presents the user with payment options. The flow then branches based on the user's selection:

  * If the user clicks **Submit**, a function node validates the data, then a PingOne Authorize node makes a decision request. The flow then branches based on the PingOne Authorize result:

    * If the result is `PERMIT`, function nodes verify that the user has sufficient funds and calculate the balance after the transaction, then a PingOne node updates the user's balance. A success page displays to the user, then the flow progresses to the **Return Success** section.

    * If the result is `DENY`, an error message displays, then the flow progresses to the **Return Success** section.

    * If the result is `NOT_APPLICABLE`, a PingOne node verifies that the user exists. If the user exists, a function node verifies that the user has sufficient funds. The **OOTB - Financial Services - Transfer Approval via Email - Subflow** is invoked. If the subflow result is `COMPLETE`, the flow proceeds as if the PingOne Authorize result was `PERMIT`. If the subflow result was `MANAGE_ACCOUNT`, the flow returns to the beginning of the **OOTB - Financial Services - Make Payment Subflow** section.

  * If the user clicks **Cancel**, the flow progresses to the \[.uicontrol]\*\*

* **Return Success**

  Sends a success JSON response, indicating that the flow has completed successfully.

* **Return Error**

  Uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input name      | Required | Description                                            |
| --------------- | -------- | ------------------------------------------------------ |
| `pingOneUserId` | Yes      | The current user's PingOne user ID.                    |
| `companyLogo`   | No       | The company logo to display in user-facing HTML pages. |
| `flowMethod`    | No       | The flow method.                                       |

## Output schema

This flow has the following outputs:

| Output Name     | Description                                   |
| --------------- | --------------------------------------------- |
| `subflowResult` | The result status of the flow.                |
| `errorMessage`  | The error message to pass to the parent flow. |
| `errorDetails`  | The details of the error that occurred.       |

## Variables and parameters

This flow uses the following variable or parameter values:

| Parameter name      | Description                                                              |
| ------------------- | ------------------------------------------------------------------------ |
| `p1UserId`          | The current user's PingOne user ID.                                      |
| `currency`          | The currency symbol for the user's locale.                               |
| `checkingBalance`   | The balance in the user's checking account.                              |
| `savingsBalance`    | The balance in the user's savings account.                               |
| `mortgageAccount`   | An element containing the user's mortgage balance and account number.    |
| `creditCardAccount` | An element containing the user's credit card balance and account number. |

---

---
title: OOTB - Financial Services - Make Transfer Subflow
description: Learn about the OOTB - Financial Services - Make Transfer Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:financial-services:flow-reference/financial-services-make-transfer-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/flow-reference/financial-services-make-transfer-subflow.html
revdate: July 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# OOTB - Financial Services - Make Transfer Subflow

The **OOTB - Financial Services - Make Transfer Subflow** lets users make a transfer.

## Purpose

The **OOTB - Financial Services - Make Transfer Subflow** presents users with a form for making transfers. It then uses PingOne Authorize to approve before using PingOne to update the user information. If additional approval is required, it invokes the **OOTB - Financial Services - Transfer Approval via Email - Subflow** subflow.

## Structure

This flow is divided into sections using teleport nodes:

* **OOTB - Financial Services - Make Payment Subflow**

  Uses a function node to set flow variables, then uses a PingOne node to verify that the user exists. An HTML node then presents the user with transfer options. The flow then branches based on the user's selection:

  * If the user clicks **Submit**, a function node validates the data, then a PingOne Authorize node makes a decision request. The flow then branches based on the PingOne Authorize result:

    * If the result is `PERMIT`, a PingOne node verifies that the user exists. Function nodes verify that the user has sufficient funds and calculate the balance after the transfer, then a PingOne node updates the user's balance. A success page displays to the user, then the flow progresses to the **Return Success** section.

    * If the result is `DENY`, an error message displays, then the flow progresses to the **Return Success** section.

    * If the result is `NOT_APPLICABLE`, a PingOne node verifies that the user exists. If the user exists, a function node verifies that the user has sufficient funds. The **OOTB - Financial Services - Transfer Approval via Email - Subflow** is invoked. If the subflow result is `COMPLETE`, the flow proceeds as if the PingOne Authorize result was `PERMIT`. If the subflow result was `MANAGE_ACCOUNT`, the flow returns to the beginning of the **OOTB - Financial Services - Make Transfer Subflow** section.

  * If the user clicks **Cancel**, the flow progresses to the \[.uicontrol]\*\*

* **Return Success**

  Sends a success JSON response, indicating that the flow has completed successfully.

* **Return Error**

  Uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input name    | Required | Description                                            |
| ------------- | -------- | ------------------------------------------------------ |
| `p1UserId`    | Yes      | The current user's PingOne user ID.                    |
| `companyLogo` | No       | The company logo to display in user-facing HTML pages. |
| `flowMethod`  | No       | The flow method.                                       |

## Output schema

This flow has the following outputs:

| Output Name     | Description                                   |
| --------------- | --------------------------------------------- |
| `subflowResult` | The result status of the flow.                |
| `errorMessage`  | The error message to pass to the parent flow. |
| `errorDetails`  | The details of the error that occurred.       |

## Variables and parameters

This flow uses the following variable or parameter values:

| Parameter name    | Description                                 |
| ----------------- | ------------------------------------------- |
| `p1UserId`        | The current user's PingOne user ID.         |
| `currency`        | The currency symbol for the user's locale.  |
| `checkingBalance` | The balance in the user's checking account. |
| `savingsBalance`  | The balance in the user's savings account.  |

---

---
title: OOTB - Financial Services - Manage Account Subflow
description: Learn about the OOTB - Financial Services - Manage Account Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:financial-services:flow-reference/financial-services-manage-account
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/flow-reference/financial-services-manage-account.html
revdate: July 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# OOTB - Financial Services - Manage Account Subflow

The **OOTB - Financial Services - Manage Account Subflow** lets users manage payments, transfers, and account settings.

## Purpose

The **OOTB - Financial Services - Manage Account Subflow** presents users with options to make a payment, make a transfer, update account settings, or update privacy settings. It invokes a subflow to complete each of these actions.

## Structure

This flow is divided into sections using teleport nodes:

* **OOTB - Financial Services - Manage Account Subflow**

  Presents an HTML page giving users account management options. The flow then branches based on the user's selection:

  * If the user selects **Make a Payment**, the **OOTB - Financial Services - Make Payment Subflow** is invoked. If the user cancels this subflow, the flow progresses to the **OOTB - Financial Services - Manage Account Subflow** section.

  * If the user selects **Make a Transfer**, the **OOTB - Financial Services - Make Transfer Subflow** is invoked. If the user cancels this subflow, the flow progresses to the **OOTB - Financial Services - Manage Account Subflow** section.

  * If the user selects **Account Settings**, the **OOTB - Financial Services - Account Settings Subflow** is invoked. If the user cancels this subflow, the flow progresses to the **OOTB - Financial Services - Manage Account Subflow** section.

  * If the user selects **Privacy Settings**, the **OOTB - Financial Services - Privacy Settings Subflow** is invoked. If the user cancels this subflow, the flow progresses to the **OOTB - Financial Services - Manage Account Subflow** section.

  * If the user selects **Cancel**, the flow progresses to the **Return Success** section.

* **Return Success**

  Sends a success JSON response, indicating that the flow has completed successfully.

* **Return Error**

  Uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input name        | Required | Description                                            |
| ----------------- | -------- | ------------------------------------------------------ |
| `p1UserId`        | Yes      | The current user's PingOne user ID.                    |
| `flowCompanyLogo` | No       | The company logo to display in user-facing HTML pages. |
| `flowMethod`      | No       | The flow method.                                       |

## Output schema

This flow has the following outputs:

| Output Name     | Description                                   |
| --------------- | --------------------------------------------- |
| `subflowResult` | The result status of the flow.                |
| `errorMessage`  | The error message to pass to the parent flow. |
| `errorDetails`  | The details of the error that occurred.       |

## Variables and parameters

This flow does not directly use any variable or parameter values.

---

---
title: OOTB - Financial Services - Privacy Settings Subflow
description: Learn about the OOTB - Financial Services - Privacy Settings Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:financial-services:flow-reference/financial-services-privacy-settings-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/flow-reference/financial-services-privacy-settings-subflow.html
revdate: July 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# OOTB - Financial Services - Privacy Settings Subflow

The **OOTB - Financial Services - Privacy Settings Subflow** lets users update privacy settings.

## Purpose

The **OOTB - Financial Services - Privacy Settings Subflow** presents users with a form that lets them preview privacy changes and update their privacy settings. The user's updated settings are saved by PingOne.

## Structure

This flow is divided into sections using teleport nodes:

* **OOTB - Financial Services - Privacy Settings Subflow**

  A function node sets flow variables and a PingOne node verifies that the user exists. An HTML node then presents the user with privacy options. The flow then branches based on the user's selection:

  * If the user clicks **Submit**, function nodes validate the user's selections, then a PingOne node updates the user's privacy preferences. A success message is displayed, then the flow progresses to the **Return Success** section.

  * If the user clicks **Preview**, a function node stores the user's preferences, then an HTML node displays to preview the selected options. The flow then returns to the privacy options page.

  * If the user cancels, the flow progresses to the **Return Success** section.

* **Return Success**

  Sends a success JSON response, indicating that the flow has completed successfully.

* **Return Error**

  Uses a function node to enrich the error details, then sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input name      | Required | Description                                            |
| --------------- | -------- | ------------------------------------------------------ |
| `pingOneUserId` | Yes      | The current user's PingOne user ID.                    |
| `companyLogo`   | No       | The company logo to display in user-facing HTML pages. |
| `flowMethod`    | No       | The flow method.                                       |

## Output schema

This flow has the following outputs:

| Output Name     | Description                                   |
| --------------- | --------------------------------------------- |
| `subflowResult` | The result status of the flow.                |
| `errorMessage`  | The error message to pass to the parent flow. |
| `errorDetails`  | The details of the error that occurred.       |

## Variables and parameters

This flow uses the following variable or parameter values:

| Parameter name      | Description                                                                                      |
| ------------------- | ------------------------------------------------------------------------------------------------ |
| `p1UserId`          | The current user's PingOne user ID.                                                              |
| `currency`          | The currency symbol for the user's locale.                                                       |
| `accountVisibility` | A property containing the user's preferences for sharing account information with third parties. |

---

---
title: OOTB - Financial Services - SignOn - Subflow
description: Learn about the OOTB - Financial Services - SignOn - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:financial-services:flow-reference/financial-services-signon-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/flow-reference/financial-services-signon-subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# OOTB - Financial Services - SignOn - Subflow

The**OOTB - Financial Services - SignOn - Subflow** lets users sign on, create a new account, or recover an account.

## Purpose

The **OOTB - Financial Services - SignOn - Subflow** enables existing users to sign on using a password and uses the **OOTB - Financial Services - Device Authentication - Subflow** flow to let existing users sign on using a known device.

## Structure

This flow is divided into sections using teleport nodes:

* **Flow Configuration**

  Uses multiple function nodes to save the variable and parameter values so that the correct values are available in the flow and in subflows, and to verify that the agreement ID is present if agreement is enabled. The flow then progresses to the **Offer Sign On Page** section.

* **Offer Sign On Page**

  Displays an HTML page that lets the user sign on.

  If the user clicks **Sign On**:

  1. A PingOne node looks up the user using their email address.

  2. The flow progresses to the **Threat Detection And Mitigation** section.

  3. When the **Threat Detection And Mitigation** section completes, the flow progresses to the **Password Authentication** section.

* **Password Authentication**

  Uses two PingOne nodes to look up the user and validate the provided password.

  * If the password is correct, the flow progresses to the **MFA Authentication** section. When this section completes, a function node evaluates the password status.

    * If the password status is `OK`, the flow progresses to the **Call Check Agreement and Email Verification Sub-Flow** section.

    * If the password is correct but must be changed or is expired, the flow progresses to the **Call Change Password Sub-Flow** section.

  * If the password is incorrect, or the user can't be found, a comparison node checks whether the account is locked. If the account is locked, the flow progresses to the **Return Error** section. If the account is not locked, an error message displays to the user.

* **Threat Detection And Mitigation**

  Uses a function node to check if PingOne Protect analysis is required.

  * If PingOne Protect analysis is required, the **OOTB - Financial Services - Threat Detection - Subflow** is invoked. If the subflow completes unsuccessfully, an error message is displayed. If the subflow completes successfully, a function node branches based on the reported risk level:

    * If the risk level is low, a function node sets the `isMFAAuthnReq` variable to false. The flow then progresses to the **Password Authentication** section.

    * If the risk level is medium, a function node sets the `isMFAAuthnReq` variable to true. The flow then progresses to the **Password Authentication** section.

    * If the risk level is high, function nodes check if the PingOne user ID is unknown and if the high risk was the result of a new device. If the PingOne ID is unknown, and the high risk is not the result of a new device, a PingOne node sends an email notifying the user of suspicious activity. A function node sets the `isMFAAuthnReq` variable to true, and the flow progresses to the **Password Authentication** section.

  * If PingOne Protect analysis is not required, a function node sets the `isMFAAuthnReq` variable to true. The flow then progresses to the **Password Authentication** section.

* **Call Change Password Sub-Flow**

  Invokes the **OOTB - Financial Services - Change Password - Subflow** flow. If the subflow completes successfully, the flow displays a success message and a PingOne node sends a password change email the flow. The flow then progresses to the **Call Check Agreement and Email Verification Sub-Flow** section.

* **MFA Authentication**

  Uses function nodes to verify that multi-factor authentication (MFA) is required and that MFA is enabled for the user.

  * If both conditions are met, a PingOne node looks up the user's existing devices. An HTML node then checks the user's current device for Webauthn support, and comparison nodes filter for unusable devices and check if at least one device is configured.

    If the user has no active devices, or the user's device information could not be found, the flow progresses to the **Step up to register Email MFA device if no MFA devices found during authentication** section.

    If the user has active devices, the **OOTB - Financial Services - Device Authentication - Subflow** is invoked. If the subflow completes successfully, a function node saves the authentication method as a variable and the flow returns to the **Password Authentication** section. If the user canceled in the subflow, the flow progresses to the **Offer Sign-on Page** section.

  If MFA isn't enabled for the user, a function node checks if MFA can be enabled for the user.

  * If MFA can't be enabled, the section proceeds from the PingOne device lookup node as described above.

  * If MFA can be enabled, an HTML page presents the user with the option of enabling MFA. If the user selects this option, a PingOne node enables MFA for them. The section then proceeds from the PingOne device lookup node as described above.

* **Call Check Agreement and Email Verification Sub-Flow**

  Invokes the **OOTB - Financial Services - Agreement (ToS) - Subflow**, then uses a PingOne node to retrieve user information. A function node checks whether email verification is required, and if email verification is required, the **OOTB - Financial Services - Verify Email - Subflow** is invoked. The flow then progresses to the **Handle Remember Me if Applicable** section.

* **Handle Remember Me if Applicable**

  Adds **Remember Me** as an authentication method if it is enabled, then progresses to the **Return Success** section.

* **Step up to register Email MFA device if no MFA devices found during authentication**

  A comparison node checks whether email verification is required.

  * If email verification is not required, invokes the **OOTB - Financial Services - Device Registration - Subflow**, then branches based on the device registration result.

    * If the new device was registered successfully, a function node saves the authentication method as a variable, then the flow returns to the **Password Authentication** section.

    * If the user skipped the new device registration, the flow returns to the **Password Authentication** section.

    * If the user canceled, the flow progresses to the **Offer Sign On Page** section.

  * If email verification is required, invokes the **OOTB - Financial Services - Verify Email - Subflow**, then uses PingOne nodes to enroll email as an MFA device and enable MFA for the user. A function node saves the authentication method as a variable, then the flow returns to the **Password Authentication** section.

* **Return Success**

  Displays an HTML success message to the user, then sends a success response, indicating that the flow completed successfully.

* **Return Error**

  Uses a function node to enrich error details, uses a PingOne node to update the evaluation status if it is empty, and sends an error JSON response indicating that the flow completed unsuccessfully.

## Input schema

This flow has the following inputs:

| Input Name            | Required | Description                                                                                                               |
| --------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------- |
| `flowParameters`      | No       | An object containing parameters passed in if the flow was launched with the widget. This input replaces all other inputs. |
| `p1AgreementId`       | No       | The ID of the PingOne agreement to present to users.                                                                      |
| `p1MFAPolicyId`       | No       | The PingOne MFA policy ID.                                                                                                |
| `p1RiskPolicyIdReg`   | No       | The PingOne risk policy ID to use for registration.                                                                       |
| `p1RiskPolicyIdAuthn` | No       | The PingOne risk policy ID to use for authentication.                                                                     |
| `p1RiskPolicyIdAR`    | No       | The PingOne risk policy ID to use for account recovery.                                                                   |
| `canUserEnableMFA`    | No       | Indicates whether the user can enable MFA for their account.                                                              |

## Output schema

This flow has the following outputs:

| Output Name         | Description                                          |
| ------------------- | ---------------------------------------------------- |
| `errorMessage`      | The error message to display in the parent flow.     |
| `errorDetails`      | The details of the error that occurred in this flow. |
| `authMethod`        | The authentication method used in the flow.          |
| `p1UserId`          | The PingOne user ID of the user.                     |
| `protectRiskLevel`  | The risk level found by PingOne Protect.             |
| `protectRiskEvalId` | The PingOne Protect evaluation ID.                   |

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
| `ciam_agreementEnabled`       | `isTermsOfServiceEnabled` | A Boolean indicating whether agreement is enabled in your environment.                                                                                                                                                                                                                                           |
| `ciam_requireMFA`             | `isRequireMFA`            | A Boolean that controls whether MFA is required for all users.                                                                                                                                                                                                                                                   |
| `ciam_resendOtpLimit`         | None                      | The maximum number of times a user can resend a one-time passcode (OTP) *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)*. |
| `ciam_verificationLimit`      | None                      | The maximum number of times a user can attempt to verify their email address.                                                                                                                                                                                                                                    |
| `ciam_otpFallbackAllowed`     | None                      | A Boolean indicating whether a user can fall back to an OTP if a mobile push request times out.                                                                                                                                                                                                                  |
| `ciam_recoveryLimit`          | None                      | The maximum number of times a user can attempt to recover an account.                                                                                                                                                                                                                                            |
| `ciam_accountRecoveryEnabled` | None                      | A Boolean that controls whether account recovery is enabled in your environment.                                                                                                                                                                                                                                 |
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
title: OOTB - Financial Services - Threat Detection - Subflow
description: Learn about the OOTB - Financial Services - Threat Detection - Subflow flow, including its purpose, structure, inputs, outputs, and variables.
component: pingone-solutions
page_id: pingone-solutions:financial-services:flow-reference/financial-services-threat-detection-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/financial-services/flow-reference/financial-services-threat-detection-subflow.html
revdate: January 1, 2025
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# OOTB - Financial Services - Threat Detection - Subflow

The **OOTB - Financial Services - Threat Detection - Subflow** uses PingOne Protect to provide a risk assessment of the current user.

## Purpose

The **OOTB - Financial Services - Threat Detection - Subflow** passes user information to PingOne Protect to perform a risk assessment. The assessment results are made available to other flows.

## Structure

This flow is divided into sections using teleport nodes:

* **Detect Threat using PingOne Protect**

  A function node verifies that the username, flow type, and `skriskcomponent` are all present. If all values are present, a PingOne Protect node creates a risk evaluation. A function node then checks if a new device was found.

  If a new device was found, function nodes check if the user's account is pre-existing and enabled. If both conditions are met, a PingOne node notifies the user of the new device.

  Regardless of whether a new device was found, a comparison node checks whether a bot, adversary-in-the-middle (AITM), or disposable email was detected.

  * If none were detected, function nodes verify that either the user ID is not known or that the user's account is enabled. The flow then progresses to the **Return Success** section.

  * If any were detected, the flow progresses to the **Disable User And Return Error If BOT/AITM/Disposable Mail Detected** section.

* **Disable User And Return Error If BOT/AITM/Disposable Mail Detected**

  Function nodes verify that the flow type passed to PingOne Protect was not `registration` and that the user is active. If these conditions are met, PingOne nodes disable the user and notify the user with an email.

* **Return Success**

  Sends a JSON success message.

* **Return Error**

  Uses a function node to enrich the error details, then sends a JSON error message. If the PingOne Protect evaluation ID isn't present, a PingOne Protect node updates the PingOne Protect risk evaluation to `Failed`.

## Input schema

This flow has the following inputs:

| Input name              | Required | Description                                                                                                |
| ----------------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
| `skriskcomponent`       | Yes      | The `SKRisk` component to be used in the risk evaluation.                                                  |
| `p1UserId`              | No       | The user ID to be passed to PingOne Protect.                                                               |
| `p1UserName`            | Yes      | The username to be evaluated by PingOne Protect.                                                           |
| `p1UserEmail`           | No       | The user email to be passed to PingOne Protect.                                                            |
| `p1ProtectRiskPolicyId` | No       | The risk policy ID to be passed to PingOne Protect. If it isn't provided, the default risk policy is used. |
| `flowType`              | Yes      | The flow type to be passed to PingOne Protect.                                                             |
| `ipAddress`             | Yes      | The user IP address to be passed to PingOne Protect.                                                       |
| `isAccountEnabled`      | No       | A Boolean indicating whether the user's account is enabled.                                                |
| `applicationID`         | No       | The application ID to be passed to PingOne Protect.                                                        |
| `sessionID`             | No       | The session ID to be passed to PingOne Protect.                                                            |
| `customAttributes`      | No       | Any custom PingOne attributes to be passed to PingOne Protect.                                             |
| `userAgent`             | No       | The PingOne Protect user agent.                                                                            |
| `usercookie`            | No       | The PingOne Protect user cookie.                                                                           |

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