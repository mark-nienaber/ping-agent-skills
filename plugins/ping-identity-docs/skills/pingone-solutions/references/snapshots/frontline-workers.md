---
title: About Verified Frontline Workers flow pack
description: The Verified Frontline Workers flow pack lets you provide end users (frontline workers) with secure ways to register an account and sign on, either with a phone or with assistance from an existing supervisor, all using a simple getting started experience and pre-built PingOne DaVinci flows.
component: pingone-solutions
page_id: pingone-solutions:frontline-workers:index
canonical_url: https://docs.pingidentity.com/pingone-solutions/frontline-workers/index.html
llms_txt: https://docs.pingidentity.com/pingone-solutions/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-14
---

# About Verified Frontline Workers flow pack

The Verified Frontline Workers flow pack lets you provide end users (frontline workers) with secure ways to register an account and sign on, either with a phone or with assistance from an existing supervisor, all using a simple getting started experience and pre-built PingOne DaVinci flows.

This flow pack enables robust threat detection against bots, disposable email, and Adversary-in-the-Middle (AITM) attacks. It also analyzes risk signals to detect high, medium, and low threats to reduce the risk of account takeovers.

The flow pack uses a single main flow to handle the entire process:

* **Frontline Worker - Registration, Authentication and Account Recovery with ID Verification and Recognize - Main Flow** lets users register an account, including performing a threat assessment and verifying the user's identity.

It also uses the following subflows and additional flows:

* **Frontline Worker - Recognize Authentication - Subflow** uses PingOne Recognize to authenticate users with a selfie.

* **Frontline Worker - In-Person Registration - Subflow** lets users register in person, including the user agreement.

* **Frontline Worker - ID Verification - Subflow** verifies a user's ID using PingOne Verify.

- **Frontline Worker - Recognize Image Enrollment - Subflow** uses PingOne Recognize to enroll a selfie image taken during ID verification.

- **Frontline Worker - Recognize Live Selfie Enrollment - Subflow** uses PingOne Recognize to enroll a live selfie image.

- **Frontline Worker - Remote User Registration** lets users register remotely using a phone, including the user agreement.

You can view additional information about the solution, including download links, in the Ping Identity Marketplace. Learn more at [Verified Frontline Workers flow pack on the Marketplace](https://marketplace.pingone.com/item/verified-trust-frontline-workers-onboarding-and-access).

If you want to add helpdesk support to the Verified Frontline Workers flow pack, you can add the **Verified Trust for Workforce - Helpdesk Solution**. Learn more about this solution on its [marketplace listing](https://marketplace.pingone.com/item/verified-trust-for-workforce-helpdesk-solution).

Preparing the Verified Frontline Workers flow pack solution involves configuration steps in PingOne and DaVinci:

* In PingOne, perform basic configuration to prepare the flows to be launched and enable features such as multi-factor authentication (MFA) and PingOne notifications.

* In DaVinci, configure variables and flow settings to customize the flow behavior for your environment and customers.

* Clone the flows for use in your production environment.

The Verified Frontline Workers flow pack solution offers many of the available DaVinci capabilities. However, the solution limits the pre-built components to common use cases and selected best practices.

The solution includes selfie authentication to enable users to sign on even in environments without desktop computer access.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Verified Frontline Workers flow pack solution offers pre-built flow templates and configurations. Review these components with your Ping Identity account representative to understand the limitations and risks associated with this solution. Your account representative can also help you customize the pre-built flow templates to satisfy any compliance or regulatory requirements that relate to your business. |

This solution uses DaVinci and PingOne, including PingOne Verify and PingOne Recognize. Learn more about managing users and other PingOne tasks in the [PingOne documentation](https://docs.pingidentity.com/pingone/p1_cloud__platform_main_landing_page.html). Learn more about customizing flows in the [DaVinci documentation](https://docs.pingidentity.com/davinci/davinci_landing_page.html).

---

---
title: Best Practices
description: These guidelines help you make effective use of the Verified Frontline Workers flow pack solution in your environment.
component: pingone-solutions
page_id: pingone-solutions:frontline-workers:frontline-best-practices
canonical_url: https://docs.pingidentity.com/pingone-solutions/frontline-workers/frontline-best-practices.html
llms_txt: https://docs.pingidentity.com/pingone-solutions/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-14
section_ids:
  select-an-appropriate-flow-timeout: Select an appropriate flow timeout
  clone-your-flows-before-using-or-customizing-them: Clone your flows before using or customizing them
  use-caution-when-customizing-flows: Use caution when customizing flows
---

# Best Practices

These guidelines help you make effective use of the Verified Frontline Workers flow pack solution in your environment.

## Select an appropriate flow timeout

When you're configuring your DaVinci flows, you can set a timeout value for the flow as a whole. Because the user's account could be updated later by anyone with access to the device, a flow with a very long or indefinite timeout could be a security risk. Set a value that minimizes that risk.

The flow timeout begins counting as soon as the flow is launched, which includes time spent at the user selection screen at the beginning of the flow. Since the flow might often wait at this screen in between user signons, you should use a timeout value long enough to cover the gap between signon attempts.

## Clone your flows before using or customizing them

Flows with the original name can be updated by PingOne when we publish flow updates. These updates are not applied automatically, but they add a new latest version to each flow.

By cloning the flows before you apply any customization or use them with customers, you prevent any of your changes or customizations from being overwritten accidentally.

## Use caution when customizing flows

If you want to customize the flows in the Verified Frontline Workers flow pack solution, do so carefully.

Clone the flows before making customizations so that:

* You can revert to the earlier versions if you encounter breaking changes.

* If you download an updated version of the solution, you don't overwrite your customizations.

Test your customizations in a test environment before importing them into your production environment. Because any additional nodes or flows you add are not part of the standard solution, you must test them to make sure that they're working as you intend.

---

---
title: Configuring flows in DaVinci
description: After you configure PingOne, perform additional configuration in PingOne DaVinci to enable all features and make the flows available to end users.
component: pingone-solutions
page_id: pingone-solutions:frontline-workers:getting-started/frontline-configuring-flows-in-davinci
canonical_url: https://docs.pingidentity.com/pingone-solutions/frontline-workers/getting-started/frontline-configuring-flows-in-davinci.html
llms_txt: https://docs.pingidentity.com/pingone-solutions/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-14
section_ids:
  steps: Steps
  choose-from: Choose from:
  result: Result:
  result-2: Result:
  choose-from-2: Choose from:
---

# Configuring flows in DaVinci

After you configure PingOne, perform additional configuration in PingOne DaVinci to enable all features and make the flows available to end users.

## Steps

1. Import the solution into your initial environment:

   1. In your production DaVinci environment, click **Flows**.

   2. Click **Add Flow > Import from JSON**.

   3. Select the JSON file containing the flows.

   4. Click **Import**.

2. Configure DaVinci applications that invoke the **Frontline Worker - Registration, Authentication and Account Recovery with ID Verification and Recognize - Main Flow** and **Frontline Worker - Remote User Registration**.

   Learn more in [Creating an application](https://docs.pingidentity.com/davinci/applications/davinci_creating_an_application.html) and [Configuring a flow policy](https://docs.pingidentity.com/davinci/applications/davinci_configuring_a_flow_policy.html) in the DaVinci documentation.

   1. On the **Applications** tab, click **Add Application**.

   2. In the **Name** field, enter a name for the application.

   3. Click **Create**.

   4. On the **Applications** tab, find the application that you created and click **Edit**.

   5. On the **Flow Policy** tab, click **Add Flow Policy**.

   6. In the **Name** field, enter a name for the flow policy.

   7. Select **PingOne Flow Policy** if you plan to invoke the flow using a PingOne redirect.

   8. In the **Flows** section, select the **Frontline Worker - Registration, Authentication and Account Recovery with ID Verification and Recognize - Main Flow**.

   9. In the **Version** section, select one or more versions of the flow to use.

   10. Click **Create Flow Policy**.

   11. In the **Distribution** field, set the weight for the selected flow to `100`.

   12. Click **Save Flow Policy**.

   13. Click **Apply**.

   14. Repeat steps a - m for the **Frontline Worker - Remote User Registration**.

3. Enter or verify the values for each company variable that's used in the Verified Frontline Workers flow pack solution.

   These variables determine whether some processes and subflows are included or excluded.

   1. Click the **Variables** tab.

   2. Locate a variable and click the **Pencil** icon.

   3. In the **Value** field, verify that the value is correct or enter a new value for the variable.

   4. Click **Update**.

   5. Repeat steps b - d for each remaining variable.

      > **Collapse: Company variables**
      >
      > | Variable                                     | Description                                                                                                                                                                                                                                                                                                                                                                                |
      > | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      > | `frontline_companyName`                      | The name of your company as it should be displayed in user-facing text.                                                                                                                                                                                                                                                                                                                    |
      > | `frontline_remoteRegistrationRetryLimit`     | The maximum number of times a user can retry remote registration if retries are enabled.                                                                                                                                                                                                                                                                                                   |
      > | `frontline_isRetryRemoteRegistrationEnabled` | A Boolean that indicates whether a user can retry remote registration.                                                                                                                                                                                                                                                                                                                     |
      > | `frontline_superviserAuthnRetryLimit`        | The maximum number of times a user can attempt to authenticate as a supervisor.                                                                                                                                                                                                                                                                                                            |
      > | `frontline_workerAuthnRetryLimit`            | The maximum number of times a user can attempt to authenticate as a worker.                                                                                                                                                                                                                                                                                                                |
      > | `frontline_threatDetectionRequired`          | A Boolean that indicates whether threat detection through PingOne Protect is required.                                                                                                                                                                                                                                                                                                     |
      > | `frontline_supportEmail`                     | An email address user should use for support. This can be included in email templates.                                                                                                                                                                                                                                                                                                     |
      > | `frontline_envDomain`                        | The PingOne regional domain for this environment. This is userd to construct the correct PingOne endpoints. Valid values for each region are:- North America (excluding Canada) (NA): **pingone.com**
      >
      > - Canada (CA): **pingone.ca**
      >
      > - European Union (EU): **pingone.eu**
      >
      > - Australia (AU): **pingone.com.au**
      >
      > - Singapore (SG): **pingone.sg**
      >
      > - Asia-Pacific (AP): **pingone.asia** |
      > | `frontline_helpdeskEmail`                    | The destination email for support requests.                                                                                                                                                                                                                                                                                                                                                |

4. Verify the configuration of the following connectors in your environment:

   | Connector             | Description                                                                                                                          | Connector documentation                                                                                     |
   | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
   | PingOne               | Enables DaVinci to view and update PingOne user information.                                                                         | [PingOne connector](https://docs.pingidentity.com/connectors/p1_connector.html)                             |
   | PingOne Notifications | Enables DaVinci flows to send users general communications using SMS, email, and voice message with PingOne's notifications feature. | [PingOne Notifications connector](https://docs.pingidentity.com/connectors/p1_notifications_connector.html) |
   | OIDC and OAuth IdP    | Enables users to authenticate with an Identity Provider (IdP).                                                                       | [OIDC and OAuth IdP connector](https://docs.pingidentity.com/connectors/oidc_oauth_idp_connector.html)      |

   1. On the **Connectors** tab, find the connector that you want to verify and go to **…​ > Edit**.

   2. Verify that the **Environment ID**, **Client ID**, and **Region** field values match your PingOne values.

   3. (Optional) Copy the **Client Secret** from your PingOne environment to the **Client Secret** field.

   4. For the PingOne Authorize connector, verify that the **Endpoint** matches the one found in PingOne in the **Authorization > Decision Endpoints** section.

   5. If you made changes to the values, click **Apply**.

   6. Repeat the previous steps for each remaining connector.

5. Configure the **Frontline Worker - Registration, Authentication and Account Recovery with ID Verification and Recognize - Main Flow**:

   1. Click **Flows**.

   2. Select the **Frontline Worker - Registration, Authentication and Account Recovery with ID Verification and Recognize - Main Flow** and go to **…​ > Edit**.

   3. Click the **Initialize Or Set Flow Variables** node and set values for the following variables:

      > **Collapse: Variables**
      >
      > | Variable                                  | Description                                                                                                                                                                                                |
      > | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      > | `protectRiskEvalId`                       | The ID of the PingOne risk policy you created in the previous procedure.                                                                                                                                   |
      > | `p1OnSiteRegistrationVerifyPolicyId`      | The ID of the PingOne Verify policy you created for the **Frontline Worker - Registration, Authentication and Account Recovery with ID Verification and Recognize - Main Flow** in the previous procedure. |
      > | `supervisorsPopulationId`                 | The supervisors population ID.                                                                                                                                                                             |
      > | `workersPopulationId`                     | The workers' population ID.                                                                                                                                                                                |
      > | `workerAppClientId`                       | The client ID for the worker app.                                                                                                                                                                          |
      > | `workerAppClientSecret`                   | The client secret for the worker app.                                                                                                                                                                      |
      > | `onboardingWorkersPopulationId`           | The currently onboarding workers' population ID.                                                                                                                                                           |
      > | `remoteInviteNotificationTemplateName`    | The name of the notification template to use for remote invites.                                                                                                                                           |
      > | `remoteInviteFlowLink`                    | The flow policy link for the Frontline Worker - Remote User Registration to use for remote invites.                                                                                                        |
      > | `inviteLinkTTL (in seconds)`              | The amount of time for which an invite should be active before it times out.                                                                                                                               |
      > | `p1AgreementId`                           | The ID of the agreement to use if your environment requires user agreement.                                                                                                                                |
      > | `helpdeskRequestNotificationTemplateName` | The name of the notification template to use for help desk requests.                                                                                                                                       |

   4. Click **Save**.

6. Configure the **Frontline Worker - Remote User Registration**:

   1. Click **Flows**.

   2. Select the **Frontline Worker - Remote User Registration** and go to **…​ > Edit**.

   3. Click the **Initialize Or Set Flow Variables** node and set values for the following variables:

      > **Collapse: Variables**
      >
      > | Variable                          | Description                                                                                                                        |
      > | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
      > | `welcomeNotificationTemplateName` | The name to display for the welcome notification.                                                                                  |
      > | `p1VerifyPolicyId`                | The ID of the PingOne Verify policy you created for the **Frontline Worker - Remote User Registration** in the previous procedure. |
      > | `workersPopulationId`             | The workers' population ID.                                                                                                        |
      > | `p1AgreementId`                   | The ID of the agreement to use if your environment requires user agreement.                                                        |

   4. Click **Save**.

7. Verify that the PingOne flow setting is correct for your environment.

   ### Choose from:

   * If you want to launch the Verified Frontline Workers flow pack solution using a redirect, the flow must be configured as a PingOne flow.

   * If you want to launch the Verified Frontline Workers flow pack solution using the widget, the flow must not be configured as a PingOne flow.

     1. Click **Flows**.

     2. Click the **Frontline Worker - Registration, Authentication and Account Recovery with ID Verification and Recognize - Main Flow**.

     3. Go to **[icon: ellipsis-v, set=fa]> Flow Settings**.

     4. If you plan to launch the flow through a redirect, click the **PingOne Flow** toggle.

     5. If you made changes to the flow settings, click **Save**, close the flow settings pane, and click **Deploy**.

8. If you're using a test environment, move the flows to your production environment:

   1. In your testing environment, click **Flows**.

   2. Click the **Frontline Worker - Registration, Authentication and Account Recovery with ID Verification and Recognize - Main Flow** flow.

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

   9. Repeat steps a-h for the **Frontline Worker - Remote User Registration**.

   10. Repeat the previous steps in your production environment.

9. Invoke the flow or flows using the widget or a redirect.

   ### Choose from:

   * If you want to launch the flow in a separate window using a PingOne redirect, use the procedure in [Launching a PingOne flow with a redirect](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launch_flow_redirect.html) in the DaVinci documentation. The Frontline Worker - Registration, Authentication and Account Recovery with ID Verification and Recognize - Main Flow flow can be launched with a redirect.

   * If you want to launch the flow in a widget within the user's current window, use the procedure in [Launching a flow with the widget](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launching_a_flow_with_the_widget.html) in the DaVinci documentation. The **Frontline Worker - Registration, Authentication and Account Recovery with ID Verification and Recognize - Main Flow** can be launched with the widget.

---

---
title: Configuring PingOne for the Verified Frontline Workers flow pack solution
description: Verify that your PingOne environment has the necessary configuration to run the Verified Frontline Workers flow pack solution and enable all the features that you want to use.
component: pingone-solutions
page_id: pingone-solutions:frontline-workers:getting-started/frontline-configuring-p1
canonical_url: https://docs.pingidentity.com/pingone-solutions/frontline-workers/getting-started/frontline-configuring-p1.html
llms_txt: https://docs.pingidentity.com/pingone-solutions/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring PingOne for the Verified Frontline Workers flow pack solution

Verify that your PingOne environment has the necessary configuration to run the Verified Frontline Workers flow pack solution and enable all the features that you want to use.

## About this task

These steps ensure that the PingOne configuration is correct and enable features such as magic links, agreements, and social sign-on.

## Steps

1. Create an Identity Verification policy for use in the **Frontline Worker - Registration, Authentication and Account Recovery with ID Verification and Recognize - Main Flow**.

   1. In the PingOne admin console, go to **Identity Verification** > **Verify Policies**.

   2. Click the **+** icon.

   3. Configure Government ID settings.

      1. Set **Government ID** to **Required**.

      2. Select a **Document Authentication Provider** to verify the government ID.

      3. Select an **Inspection Type** for the government ID.

      4. In the **Government ID Retry Attempts** field, enter a number of times a user can retry scanning an ID if the first attempt fails.

      5. If you have users in the USA, select the **Enable AAMVA** option to enable verification of ID information against the AAMVA Driver's License Data Verification (DLDV) service.

      6. Select the **Fail Expired IDs** option to fail verification if the government ID has expired.

      7. If you have users in India, select the **Enable Aadhaar Verification (India)** option to enable user verification of Aadhaar digital IDs through the DigiLocker wallet.

   4. Configure Facial Comparison settings.

      1. Set **Facial Comparison** to **Required**.

      2. Select a **Threshold** for matching the selfie to the ID.

   5. Configure Liveness settings.

      1. Set **Liveness** to **Required**.

      2. Select a **Threshold** for matching the selfie to the ID.

      3. Select a number of **Selfie Retry Attempts**, between 0 and 3.

   6. Configure Email settings.

      1. Set **Email Verification** to **Disabled**.

   7. Click **Save**.

2. Create an Identity Verification policy for use in the **Frontline Worker - Remote User Registration**.

   1. In the PingOne admin console, go to **Identity Verification** > **Verify Policies**.

   2. Click the **+** icon.

   3. Configure Government ID settings.

      1. Set **Government ID** to **Required**.

      2. Select a **Document Authentication Provider** to verify the government ID.

      3. Select an **Inspection Type** for the government ID.

      4. In the **Government ID Retry Attempts** field, enter a number of times a user can retry scanning an ID if the first attempt fails.

      5. If you have users in the USA, select the **Enable AAMVA** option to enable verification of ID information against the AAMVA Driver's License Data Verification (DLDV) service.

      6. Select the **Fail Expired IDs** option to fail verification if the government ID has expired.

      7. If you have users in India, select the **Enable Aadhaar Verification (India)** option to enable user verification of Aadhaar digital IDs through the DigiLocker wallet.

   4. Configure Facial Comparison settings.

      1. Set **Facial Comparison** to **Required**.

      2. Select a **Threshold** for matching the selfie to the ID.

   5. Configure Liveness settings.

      1. Set **Liveness** to **Required**.

      2. Select a **Threshold** for matching the selfie to the ID.

      3. Select a number of **Selfie Retry Attempts**, between 0 and 3.

   6. Configure Email settings.

      1. Set **Email Verification** to **Required**.

   7. Click **Save**.

3. (Optional) If you plan to use PingOne Protect, create a new predictor:

   1. In the PingOne admin console, go to **Threat Protection** > **Predictors**.

   2. Click the + icon to add a predictor.

   3. In the **Choose Type** list, select **Custom**.

   4. In the **Display Name** field, enter **Allowed IP List**.

   5. In the **Compact Name** field, enter **allowedIPList**.

   6. In the **Attribute Mapping** field, enter **${event.ip}**.

   7. In the **Risk Level Mapping** section, click **IP Ranges**.

   8. In the **Low**, **Medium**, and **High** fields, enter one or more IP ranges to match each risk rating.

   9. Click **Save**.

4. (Optional) If you plan to use PingOne Protect, create a new risk policy:

   1. In the PingOne admin console, go to **Threat Protection** > **Risk Policies**.

   2. Click the **Global** policy tab.

   3. Click the + icon to add a policy.

   4. For **Name**, enter **Allowed IP Risk Policy**.

   5. Click **+ Add Predictor**.

   6. In the **Risk Model** list, select the **Allowed IP List** predictor.

   7. Click **Apply**.

   8. In the **Rules** section, click **Mitigation**, then click **+ Add**.

   9. Set one or more mitigation rules.

      1. Click **Add**.

      2. In the **Rule** list, select a rule type.

      3. Use the **Operator**, **Level**, and **Returned Action** lists to configure the rule.

         For example, if the rule is Adversary in the Middle and you select Equals, High, and Deny, the rule denies access if a high risk of an adversary in the middle attack is detected.

      4. Click **Apply**.

   10. Set the Fallback action to Deny.

       1. Locate the **Fallback** rule and click **Edit**.

       2. In the **Returned Action** list, select **Deny**.

       3. Click **Apply**.

   11. Click **Apply**.

5. Create three PingOne populations for workers, supervisors, and onboarding workers.

   1. Go to **Directory > Populations**.

   2. Click the + icon to add a population.

   3. Enter a population name:

      | Name               | Description                                                                                                                                  |
      | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
      | Supervisors        | Contains users who can authenticate themselves and register new employees.                                                                   |
      | Workers            | Contains verified employee accounts who can authenticate themselves.                                                                         |
      | Onboarding workers | Temporarily contains employees who are invited to register by email. After registration, these employees are moved to the worker population. |

   4. Click **Save**.

   5. Note the population ID for the new population.

   6. Repeat steps a-e for the remaining populations.

6. Add the necessary user attributes.

   | Name                        | Description                                                                                                                                                                                                                                                                                                                                                         |
   | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `accountStatus`             | Controls whether the user account is active for authentication. Only enabled users appear on the login page.New accounts have a status of **DISABLED**. When the worker successfully completes the required identity verification and enrollment process, or when a supervisor approves the registration without ID verification, the status is set to **ENABLED**. |
   | `accountVerifyStatus`       | Tracks the worker's current identity verification status. Valid values are **ID\_NOT\_VERIFIED**, **VERIFIED**, and **ID Verification Pending (Approved by Supervisor on-site)**.                                                                                                                                                                                   |
   | `dateOfBirth`               | The user's date of birth.                                                                                                                                                                                                                                                                                                                                           |
   | `inviteLinkExpiresAt`       | The timestamp at which the invite link expires.                                                                                                                                                                                                                                                                                                                     |
   | `inviteTokenHash`           | Stores the hash of the raw invitation token.                                                                                                                                                                                                                                                                                                                        |
   | `registrationRetryAttempts` | Stores the number of failed or successful registration attempts. This is used to limit the number of retries.                                                                                                                                                                                                                                                       |
   | `inviteTokenSalt`           | Stores the per-invitation cryptographic salt used to generate and validate the invite token hash during remote registration.                                                                                                                                                                                                                                        |
   | `lastAuthenticatedAt`       | Stores the timestamp of the user's last successful authentication.                                                                                                                                                                                                                                                                                                  |

   1. In the PingOne admin console, go to **Directory** > **User Attributes**.

   2. Click the **+** icon.

   3. For the attribute type, select **Declared**.

   4. Click **Next**.

   5. In the **Name** field, enter an attribute name from the table above.

   6. In the **Display Name** field, enter the same attribute name from the table above.

   7. In the **Description** field, enter the description from the table above.

   8. Select **No Validation**.

   9. Click **Save**.

   10. Click the blue toggle to the right to enable the attribute.

   11. Repeat steps a-j for the remaining attributes.

7. Create the **Invite Notification** template:

   1. In PingOne, go to **User Experience > Notification Templates**.

   2. Click **[icon: plus, set=fa]**to create a new template.

   3. In the **Type** list, select **General**.

   4. In the **Name** field, enter a name for the template. For example: `Invite Notification`.

      |   |                                       |
      | - | ------------------------------------- |
      |   | Note the template name for later use. |

   5. Click **Create**.

   6. In the **Subject** field, configure a subject:

      1. Click the **Pencil** icon.

      2. Enter the subject `Frontline Worker Account Registration`.

      3. Click the **[icon: check, set=fa]**icon.

   7. In the **New Email** field, configure the message body:

      1. Click the **Pencil** icon.

      2. Enter a body for the new transaction message.

         |   |                                                                                                                                                                             |
         | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
         |   | You can use the following variables in the message:- `${link}`: The invite link.

         - `${username}`: The new user's user name.

         - `${companyName}`: The name of your company. |

         For example:

         ```html
         <!DOCTYPE html>
         <html lang="en">
         <head>
           <meta charset="UTF-8" />
           <meta name="viewport" content="width=device-width, initial-scale=1.0" />
           <title>Complete your registration</title>
           <style>
             html, body { margin: 0; padding: 0; }
             @media screen and (max-width: 560px) {
               .page-pad { padding: 18px 10px !important; }
               .hero-pad { padding: 24px 18px 21px !important; }
               .hero-title { font-size: 34px !important; }
               .content-pad { padding: 26px 20px 24px !important; }
               .body-copy { font-size: 15px !important; line-height: 27px !important; }
               .notice-pad { padding: 18px 18px !important; }
               .cta-button { display: block !important; padding-left: 22px !important; padding-right: 22px !important; }
             }
             @page { size: auto !important; }
           </style>
         </head>
         <body style="margin:0; padding:0; background-color:#eef2f7; font-family:Arial, Helvetica, sans-serif; color:#243648;">
           <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; background-color:#eef2f7; margin:0; padding:0;">
             <tr>
               <td class="page-pad" align="center" style="padding:32px 12px;">
                 <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="max-width:720px; width:100%;">
                   <tr>
                     <td style="padding-bottom:18px;">
                       <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; background-color:#ffffff; border:1px solid #d9e1ea; border-radius:24px;">
                         <tr>
                           <td class="hero-pad" data-glean-id="registration-email-hero" align="center" style="padding:28px 24px 24px; background-color:#f7fbfd; border-radius:24px;">
                             <div data-glean-id="registration-email-company-label" style="font-size:11px; line-height:16px; font-weight:700; letter-spacing:0.34em; color:#8a98a8; margin-bottom:10px;">
                               ${companyName}
                             </div>
                             <div class="hero-title" data-glean-id="registration-email-title" style="font-size:48px; line-height:1.08; font-weight:700; color:#243648; margin:0;">
                               Complete your registration
                             </div>
                             <div data-glean-id="registration-email-subtitle" style="font-size:16px; line-height:24px; color:#6c7c8d; margin-top:12px;">
                               You have been invited to complete your registration
                             </div>
                           </td>
                         </tr>
                       </table>
                     </td>
                   </tr>
                   <tr>
                     <td>
                       <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; background-color:#ffffff; border:1px solid #d9e1ea; border-radius:24px;">
                         <tr>
                           <td class="content-pad" data-glean-id="registration-email-content" style="padding:32px 32px 28px;">
                             <p data-glean-id="registration-email-recipient" style="margin:0 0 24px; font-size:16px; line-height:26px; font-weight:700; color:#243648;">
                               ${username},
                             </p>
                             <p class="body-copy" data-glean-id="registration-email-welcome" style="margin:0 0 22px; font-size:16px; line-height:30px; color:#243648;">
                               Welcome to ${companyName}.
                             </p>
                             <p class="body-copy" data-glean-id="registration-email-invitation" style="margin:0 0 22px; font-size:16px; line-height:30px; color:#243648;">
                               You have been invited to complete your registration. To get started, select the button below.
                             </p>
                             <p class="body-copy" data-glean-id="registration-email-verification" style="margin:0 0 26px; font-size:16px; line-height:30px; color:#243648;">
                               You will be asked to confirm your personal details and complete the required steps for your role.
                             </p>
                             <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; margin:0 0 28px; border:1px solid #f0d9b8; background-color:#fff7eb; border-radius:18px;">
                               <tr>
                                 <td class="notice-pad" data-glean-id="registration-email-notice" style="padding:22px 24px; font-size:15px; line-height:28px; font-weight:700; color:#8a5a12;">
                                   Before continuing, review your personal details carefully. If anything is incorrect, contact
                                   <a href="mailto:${supportEmail}" style="color:#c47b15; text-decoration:none; font-weight:700;">${supportEmail}</a>
                                   before continuing.
                                 </td>
                               </tr>
                             </table>
                             <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; margin:0 0 28px;">
                               <tr>
                                 <td align="center">
                                   <a class="cta-button" data-glean-id="registration-email-cta" href="${link}" style="display:inline-block; background-color:#1f86c7; color:#ffffff; text-decoration:none; font-size:17px; line-height:22px; font-weight:700; padding:16px 34px; border-radius:14px;">
                                     Begin Registration
                                   </a>
                                 </td>
                               </tr>
                             </table>
                             <p data-glean-id="registration-email-footer" style="margin:0; font-size:13px; line-height:24px; text-align:center; color:#6c7c8d;">
                               This message was sent by ${companyName}. If you were not expecting this email, contact support. Do not share your registration link with anyone else.
                             </p>
                           </td>
                         </tr>
                       </table>
                     </td>
                   </tr>
                 </table>
               </td>
             </tr>
           </table>
         </body>
         </html>
         ```

      3. Click the **[icon: check, set=fa]**icon.

   8. Click **X** to close the template.

8. Create the **Account Created** template:

   1. In PingOne, go to **User Experience > Notification Templates**.

   2. Click **[icon: plus, set=fa]**to create a new template.

   3. In the **Type** list, select **General**.

   4. In the **Name** field, enter a name for the template. For example: `Account Created`.

      |   |                                       |
      | - | ------------------------------------- |
      |   | Note the template name for later use. |

   5. Click **Create**.

   6. In the **Subject** field, configure a subject:

      1. Click the **Pencil** icon.

      2. Enter the subject `You are Welcome`.

      3. Click the **[icon: check, set=fa]**icon.

   7. In the **New Email** field, configure the message body:

      1. Click the **Pencil** icon.

      2. Enter a body for the new transaction message.

         |   |                                                                                                                                                                             |
         | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
         |   | You can use the following variables in the message:- `${link}`: The invite link.

         - `${username}`: The new user's user name.

         - `${companyName}`: The name of your company. |

         For example:

         ```html
         <!DOCTYPE html>
         <html lang="en">
         <head>
           <meta charset="UTF-8" />
           <meta name="viewport" content="width=device-width, initial-scale=1.0" />
           <title>Welcome to ${companyName}</title>
           <style>
             html, body { min-height: 100%; }
             * { box-sizing: border-box; }
             @media screen and (max-width: 620px) {
               .email-shell { padding: 18px 10px !important; }
               .hero-title { font-size: 36px !important; }
               .content-pad { padding: 26px 22px 24px !important; }
             }
             @media print {
               body { background: #eef2f7 !important; }
               .email-shell { padding: 18px 10px !important; }
             }
             @page { size: auto !important; }
           </style>
         </head>
         <body style="margin:0; padding:0; background-color:#eef2f7; font-family:Arial, Helvetica, sans-serif; color:#243648;">
           <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; background-color:#eef2f7; margin:0; padding:0;">
             <tr>
               <td align="center" class="email-shell" style="padding:32px 12px;">
                 <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="max-width:720px; width:100%;">
                   <tr>
                     <td style="padding-bottom:18px;">
                       <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; background-color:#ffffff; border:1px solid #d9e1ea; border-radius:24px;">
                         <tr>
                           <td align="center" data-glean-id="welcome-email-hero" style="padding:28px 24px 24px; background-color:#f7fbfd; border-radius:24px;">
                             <div data-glean-id="company-name-kicker" style="font-size:11px; line-height:16px; font-weight:700; letter-spacing:0.34em; color:#8a98a8; margin-bottom:10px;">
                               ${companyName}
                             </div>
                             <div data-glean-id="welcome-email-title" class="hero-title" style="font-size:48px; line-height:1.08; font-weight:700; color:#1d8f4d; margin:0;">
                               Welcome to ${companyName}
                             </div>
                             <div data-glean-id="registration-status" style="font-size:16px; line-height:24px; color:#6c7c8d; margin-top:12px;">
                               Your registration is complete
                             </div>
                           </td>
                         </tr>
                       </table>
                     </td>
                   </tr>
                   <tr>
                     <td>
                       <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; background-color:#ffffff; border:1px solid #d9e1ea; border-radius:24px;">
                         <tr>
                           <td data-glean-id="welcome-email-body" class="content-pad" style="padding:32px 32px 28px;">
                             <p data-glean-id="recipient-greeting" style="margin:0 0 24px; font-size:16px; line-height:26px; font-weight:700; color:#243648;">
                               ${username},
                             </p>
                             <p data-glean-id="registration-confirmation" style="margin:0 0 22px; font-size:16px; line-height:30px; color:#243648;">
                               Welcome to ${companyName}. Your registration is complete.
                             </p>
                             <p data-glean-id="identity-verification" style="margin:0 0 22px; font-size:16px; line-height:30px; color:#243648;">
                               You are all set to begin. Follow the instructions provided to continue with the next steps for your role.
                             </p>
                             <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" data-glean-id="support-callout" style="width:100%; margin:0 0 28px; border:1px solid #d9e1ea; background-color:#f8fafc; border-radius:18px;">
                               <tr>
                                 <td style="padding:20px 24px; font-size:15px; line-height:28px; color:#6c7c8d;">
                                   If you have questions or need help, contact
                                   <a data-glean-id="support-email-link" href="mailto:${supportEmail}" style="color:#1f86c7; text-decoration:none; font-weight:700;">${supportEmail}</a>.
                                 </td>
                               </tr>
                             </table>
                             <p data-glean-id="email-footer-notice" style="margin:0; font-size:13px; line-height:24px; text-align:center; color:#6c7c8d;">
                               This message was sent by ${companyName}. If you did not create this account, contact support. For your security, never share your sign-in details or access link with anyone else.
                             </p>
                           </td>
                         </tr>
                       </table>
                     </td>
                   </tr>
                 </table>
               </td>
             </tr>
           </table>
         </body>
         </html>
         ```

      3. Click the **[icon: check, set=fa]**icon.

   8. Click **X** to close the template.

9. Create the **Helpdesk Request** template:

   1. In PingOne, go to **User Experience > Notification Templates**.

   2. Click **[icon: plus, set=fa]**to create a new template.

   3. In the **Type** list, select **General**.

   4. In the **Name** field, enter a name for the template. For example: `Helpdesk Request`.

      |   |                                       |
      | - | ------------------------------------- |
      |   | Note the template name for later use. |

   5. Click **Create**.

   6. In the **Subject** field, configure a subject:

      1. Click the **Pencil** icon.

      2. Enter the subject `Frontline HelpDesk Request`.

      3. Click the **[icon: check, set=fa]**icon.

   7. In the **New Email** field, configure the message body:

      1. Click the **Pencil** icon.

      2. Enter a body for the new transaction message.

         |   |                                                                                                                                                                             |
         | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
         |   | You can use the following variables in the message:- `${link}`: The invite link.

         - `${username}`: The new user's user name.

         - `${companyName}`: The name of your company. |

         For example:

         ```html
         <!DOCTYPE html>
         <html lang="en">
         <head>
           <meta charset="UTF-8" />
           <meta name="viewport" content="width=device-width, initial-scale=1.0" />
           <title>Account Recovery Assistance Request - ${companyName}</title>
           <style>
             @media screen and (max-width: 600px) {
               .email-shell { padding: 18px 8px !important; }
               .email-card { border-radius: 18px !important; }
               .hero-title { font-size: 30px !important; }
               .content-cell { padding: 24px 20px 22px !important; }
               .details-cell { padding-left: 16px !important; padding-right: 16px !important; }
               .details-label { width: 38% !important; }
             }
             @media print {
               body { background-color: #ffffff !important; }
               .email-shell { padding: 0 !important; }
             }
             @page { size: auto !important; }
           </style>
         </head>
         <body style="margin:0; padding:0; background-color:#eef2f7; font-family:Arial, Helvetica, sans-serif; color:#243648;">
           <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; background-color:#eef2f7; margin:0; padding:0;">
             <tr>
               <td class="email-shell" align="center" style="padding:32px 12px;">
                 <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="max-width:720px; width:100%;">
                   <tr>
                     <td data-glean-id="email-header" style="padding-bottom:18px;">
                       <table class="email-card" role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; background-color:#ffffff; border:1px solid #d9e1ea; border-radius:24px;">
                         <tr>
                           <td align="center" style="padding:28px 24px 24px; background-color:#f7fbfd; border-radius:24px;">
                             <div data-glean-id="company-name" style="font-size:11px; line-height:16px; font-weight:700; letter-spacing:0.34em; color:#8a98a8; margin-bottom:10px;">
                               ${companyName}
                             </div>
                             <div class="hero-title" data-glean-id="email-title" style="font-size:40px; line-height:1.12; font-weight:700; color:#243648; margin:0;">
                               Account Recovery Assistance Request
                             </div>
                             <div data-glean-id="email-subtitle" style="font-size:16px; line-height:24px; color:#6c7c8d; margin-top:12px;">
                               Assistance requested by a frontline worker
                             </div>
                           </td>
                         </tr>
                       </table>
                     </td>
                   </tr>
                   <tr>
                     <td data-glean-id="email-body">
                       <table class="email-card" role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; background-color:#ffffff; border:1px solid #d9e1ea; border-radius:24px;">
                         <tr>
                           <td class="content-cell" style="padding:32px 32px 28px;">
                             <p data-glean-id="greeting" style="margin:0 0 24px; font-size:16px; line-height:26px; font-weight:700; color:#243648;">
                               Hello Helpdesk Team,
                             </p>
                             <p data-glean-id="recovery-description" style="margin:0 0 22px; font-size:16px; line-height:30px; color:#243648;">
                               I'm unable to complete the selfie verification step and need assistance recovering access to my account.
                             </p>
                             <p data-glean-id="verification-description" style="margin:0 0 22px; font-size:16px; line-height:30px; color:#243648;">
                               Review the information below and help me restart the identity verification process so I can regain access to my account.
                             </p>
                             <table data-glean-id="worker-details" role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; margin:0 0 26px; border:1px solid #d9e1ea; background-color:#f8fafc; border-radius:18px;">
                               <tr>
                                 <td class="details-cell" style="padding:22px 24px 8px; font-size:15px; line-height:24px; font-weight:700; color:#243648;">
                                   Frontline worker information
                                 </td>
                               </tr>
                               <tr>
                                 <td class="details-cell" style="padding:0 24px 22px;">
                                   <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%;">
                                     <tr data-glean-id="worker-full-name">
                                       <td class="details-label" width="42%" style="padding:8px 0; font-size:14px; line-height:22px; color:#6c7c8d;">Worker name</td>
                                       <td style="padding:8px 0; font-size:14px; line-height:22px; font-weight:700; color:#243648;">${fullName}</td>
                                     </tr>
                                     <tr data-glean-id="worker-email">
                                       <td class="details-label" width="42%" style="padding:8px 0; font-size:14px; line-height:22px; color:#6c7c8d;">Work email address</td>
                                       <td style="padding:8px 0; font-size:14px; line-height:22px; font-weight:700; color:#243648; word-break:break-word;">${email}</td>
                                     </tr>
                                     <tr data-glean-id="worker-username">
                                       <td class="details-label" width="42%" style="padding:8px 0; font-size:14px; line-height:22px; color:#6c7c8d;">Username</td>
                                       <td style="padding:8px 0; font-size:14px; line-height:22px; font-weight:700; color:#243648; word-break:break-word;">${username}</td>
                                     </tr>
                                     <tr data-glean-id="worker-id">
                                       <td class="details-label" width="42%" style="padding:8px 0; font-size:14px; line-height:22px; color:#6c7c8d;">Worker ID</td>
                                       <td style="padding:8px 0; font-size:14px; line-height:22px; font-weight:700; color:#243648; word-break:break-word;">${userId}</td>
                                     </tr>
                                     <tr data-glean-id="request-timestamp">
                                       <td class="details-label" width="42%" style="padding:8px 0; font-size:14px; line-height:22px; color:#6c7c8d;">Request submitted</td>
                                       <td style="padding:8px 0; font-size:14px; line-height:22px; font-weight:700; color:#243648;">${requestTimestamp}</td>
                                     </tr>
                                   </table>
                                 </td>
                               </tr>
                             </table>
                             <table data-glean-id="requested-action" role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%; margin:0 0 26px; border:1px solid #f0d9b8; background-color:#fff7eb; border-radius:18px;">
                               <tr>
                                 <td style="padding:20px 24px; font-size:15px; line-height:28px; font-weight:700; color:#8a5a12;">
                                   Requested assistance: Verify the information above and enable the frontline worker to complete identity verification again so they can regain access to their account.
                                 </td>
                               </tr>
                             </table>
                             <p data-glean-id="contact-details" style="margin:0 0 22px; font-size:16px; line-height:30px; color:#243648;">
                               Contact me at <a href="mailto:${email}" style="color:#1f86c7; text-decoration:none; font-weight:700;">${email}</a> if any additional information is required.
                             </p>
                             <p data-glean-id="privacy-notice" style="margin:0; font-size:13px; line-height:24px; text-align:center; color:#6c7c8d;">
                               This request was submitted by a frontline worker through ${companyName}. Handle this information in accordance with your organization's privacy and account-recovery procedures.
                             </p>
                           </td>
                         </tr>
                       </table>
                     </td>
                   </tr>
                 </table>
               </td>
             </tr>
           </table>
         </body>
         </html>
         ```

      3. Click the **[icon: check, set=fa]**icon.

   8. Click **X** to close the template.

10. (Optional) If you plan to use an agreement, verify that you have an agreement configured in PingOne and copy the agreement ID.

    Learn more about configuring agreements in [Adding an agreement](https://docs.pingidentity.com/pingone/user_experience/p1_add_an_agreement.html) in the PingOne documentation.

    1. Go to **User Experience > Agreements**.

    2. Verify that the agreement exists and is enabled.

    3. Click the agreement to open the details panel.

    4. On the **API** tab, copy the **ID**.

    The agreement ID is used in a later procedure to configure the flows in DaVinci.

---

---
title: Flow Reference
description: The Healthcare Patient Experience flow pack solution uses three main flows and multiple subflows. This section explains what each flow does and how it works.
component: pingone-solutions
page_id: pingone-solutions:frontline-workers:flow-reference/frontline-workers-flow-reference
canonical_url: https://docs.pingidentity.com/pingone-solutions/frontline-workers/flow-reference/frontline-workers-flow-reference.html
llms_txt: https://docs.pingidentity.com/pingone-solutions/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-14
page_aliases: ["flow-reference/index.adoc"]
---

# Flow Reference

The Healthcare Patient Experience flow pack solution uses three main flows and multiple subflows. This section explains what each flow does and how it works.

A DaVinci flow consists of nodes, each of which presents a page to the user, performs a backend action, or launches another flow. These nodes are connected by logical operators, allowing you to construct a user journey such as authenticating with a known device or making a transfer.

The flows included in the Healthcare Patient Experience flow pack solution are designed to work together to provide the solution. They require no configuration beyond that described in [Configuring flows in DaVinci](../getting-started/frontline-configuring-flows-in-davinci.html). However, you can customize these flows to provide additional services to your end users. Learn more in [How To Manage Flows](https://docs.pingidentity.com/davinci/flows/davinci_how_to_manage_existing_flows.html) in the PingOne DaVinci documentation.

The main section of the Healthcare Patient Experience flow pack solution contains the following flows:

---

---
title: Getting Started
description: There are two configuration stages for the Verified Frontline Workers flow pack solution.
component: pingone-solutions
page_id: pingone-solutions:frontline-workers:getting-started/frontline-getting-started
canonical_url: https://docs.pingidentity.com/pingone-solutions/frontline-workers/getting-started/frontline-getting-started.html
llms_txt: https://docs.pingidentity.com/pingone-solutions/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-14
page_aliases: ["getting-started/index.adoc"]
---

# Getting Started

There are two configuration stages for the Verified Frontline Workers flow pack solution.

To get started with the solution:

1. [Configure the settings in PingOne](frontline-configuring-p1.html).

2. [Perform additional configuration in PingOne DaVinci to begin using the solution](frontline-configuring-flows-in-davinci.html).

---

---
title: Healthcare - Account Registration - Subflow
description: The Healthcare - Account Registration - Subflow lets users register a new account.
component: pingone-solutions
page_id: pingone-solutions:frontline-workers:flow-reference/frontline-worker-template-subflow
canonical_url: https://docs.pingidentity.com/pingone-solutions/frontline-workers/flow-reference/frontline-worker-template-subflow.html
llms_txt: https://docs.pingidentity.com/pingone-solutions/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-14
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
title: Healthcare - Progressive Verification during Authentication - Main Flow
description: The Healthcare - Progressive Verification during Authentication - Main Flow lets users sign on. It can be launched through the widget or through PingOne.
component: pingone-solutions
page_id: pingone-solutions:frontline-workers:flow-reference/frontline-worker-registration-authentication-and-account-recovery-with-ID-verification-and-recognize-main-flow
canonical_url: https://docs.pingidentity.com/pingone-solutions/frontline-workers/flow-reference/frontline-worker-registration-authentication-and-account-recovery-with-ID-verification-and-recognize-main-flow.html
llms_txt: https://docs.pingidentity.com/pingone-solutions/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-14
section_ids:
  purpose: Purpose
  structure: Structure
  input-schema: Input schema
  output-schema: Output schema
  variables-and-parameters: Variables and parameters
---

# Healthcare - Progressive Verification during Authentication - Main Flow

The **Healthcare - Progressive Verification during Authentication - Main Flow** lets users sign on. It can be launched through the widget or through PingOne.

## Purpose

The **Healthcare - Progressive Verification during Authentication - Main Flow** is one of the initial flows in the Healthcare Patient Experience flow pack solution. It enables existing users to sign on using a password and uses the **Healthcare - Progressive Verification during Authentication - Device Authentication - Subflow** flow to let existing users sign on using a known device.

## Structure

This flow is divided into sections using teleport nodes:

* **Flow Configuration**

  Uses multiple function nodes to save the variable and parameter values so that the correct values are available in the flow and in subflows. The flow then progresses to the **Check Session, Call To Protect Analysis & MFA Step-Up** section.

* **Check Session, Call To Protect Analysis & MFA Step-Up**

  Uses a PingOne node to determine whether the user has an existing session:

  * If the user has a session, a hidden HTML node captures risk information, and a PingOne node fetches additional user information, then the flow progresses to the **Threat Detection and Mitigation** section. When this section completes, a function node checks if the user's account is enabled, and if the user's account is enabled, the flow progresses to the **Return Success** section.

  * If the user doesn't have a session, the flow checks for any existing session tokens and uses a PingOne node to delete the prior session before invoking the **Healthcare - Progressive Verification during Authentication - SignOn - Subflow** subflow.

  When the subflow completes, a function node updates the risk level, and a PingOne Authentication node creates a user session. A loading page displays, and a PingOne node retrieves user information.

  Function nodes then evaluate the number of times the user has logged in. If the count is 2, 4, or 6 logins, the flow progresses to the **Progressive profiling during authentication** section. If the login count is less than 10, a PingOne node updates the login count. The flow then progresses to the **Return Success** section.

* **Threat Detection and Mitigation**

  Uses a function node to check if PingOne Protect analysis is required:

  * If PingOne Protect analysis is not required, the flow returns to the previous section.

  * If PingOne Protect analysis is required, the flow invokes the **Healthcare - Progressive Verification during Authentication - Threat Detection - Subflow**.

    If the **Healthcare - Progressive Verification during Authentication - Threat Detection - Subflow** completes successfully, a function node stores the risk evaluation as a variable, then a second function node branches the flow based on the risk level:

    * If the risk level is low, the flow returns to the previous section.

    * If the risk level is medium, the flow progresses to the **MFA Authentication** section. When this section completes, the flow returns to the previous section.

    * If the risk level is high, a function node checks if the high risk was the result of a new device. If not, a PingOne node notifies the user. A PingOne node deletes the existing session, and a loading page displays. The flow then progresses to the **Check Session, Call To Protect Analysis & MFA Step-Up** section.

    If the **Healthcare - Progressive Verification during Authentication - Threat Detection - Subflow** completes unsuccessfully, a function node stores the risk evaluation as a variable and the flow progresses to the **Return Error** section.

- **MFA Authentication**

  Uses a PingOne node to look up the user's existing devices. An HTML node then checks the user's current device for WebAuthn support, and comparison nodes filter for unusable devices and check if at least one device is configured.

  If the user has no active devices or the user's device information could not be found, the flow progresses to the **Step up to register Email MFA device if no MFA devices found during authentication** section.

  If the user has active devices, the flow invokes the **Healthcare - Progressive Verification during Authentication - Device Authentication - Subflow**.

  If the subflow completes successfully, a function node saves the user's authentication method as a variable, and the flow returns to the previous section.

* **Step up to register Email MFA device if no MFA devices found during authentication**

  A comparison node checks whether email verification is required.

  If email verification isn't required, the flow invokes the **Healthcare - Progressive Verification during Authentication - Device Registration - Subflow**. The section then branches based on the device registration result:

  * If the result is **Complete**, the user's authentication method is stored as a variable and the flow returns to the previous section.

  * If the result is **Skip**, the flow returns to the previous section.

  * If the result is **Cancel**, the flow returns to the **Return Error** section if an existing session was found, and to the **Offer Sign On Page** section if no session was found.

  If email verification is required, the flow invokes the **Healthcare - Progressive Verification during Authentication - Verify Email - Subflow**, then uses PingOne nodes to enroll email as an MFA device and enable MFA for the user. The user's authentication method is stored as a variable, and the flow then returns to the previous section.

* **Progressive profiling during authentication**

  Uses a function node to branch the flow based on the number of successful logins:

  * If the user has had two successful logins, an HTML node gathers emergency details.

  * If the user has had four successful logins, an HTML node gathers insurance details.

  * If the user has had six successful logins, an HTML node gathers information about medical conditions.

  * If the user has any other number of successful logins, the flow progresses to the **Return Success** section.

The flow then branches based on the user's selection:

* If the user clicked **Save**, a PingOne node saves the provided information and a success message displays. The flow then progresses to the **Return Success** section.

* If the user clicked **Cancel**, the flow progresses to the **Return Success** section.

- **Return Success**

  Sends a JSON Success Response, indicating that the flow completed successfully. Simultaneously, the flow uses function nodes to check for a PingOne Protect risk evaluation ID and verify that the user did not cancel. If a PingOne Protect risk evaluation ID is found and the user did not cancel, the flow uses a PingOne node to update the evaluation status with a success.

- **Return Error**

  Uses a function node to enrich the error details, then displays an error message. The flow checks the flow invocation method, then sends an error JSON response with the appropriate parameters indicating tha the flow completed unsuccessfully.

  The flow also simultaneously uses a function node to check for a PingOne Protect risk evaluation ID, and if a PingOne Protect risk evaluation ID is found, uses a PingOne node to update the evaluation status with a failure.

## Input schema

This flow has the following inputs:

| Input name       | Required | Description                                                                         |
| ---------------- | -------- | ----------------------------------------------------------------------------------- |
| `flowParameters` | No       | An object containing parameters passed in if the flow was launched with the widget. |

## Output schema

This flow has the following outputs:

| Output name      | Description                                                |
| ---------------- | ---------------------------------------------------------- |
| `p1UserId`       | The user's PingOne user ID.                                |
| `p1Username`     | The user's PingOne username.                               |
| `authMethod`     | The authentication method that was configured by the flow. |
| `successMessage` | The success message to display.                            |
| `errorMessage`   | The error message to display.                              |

## Variables and parameters

This flow uses the following variable or parameter values:

| Variable name        | Description                                                                 |
| -------------------- | --------------------------------------------------------------------------- |
| `canEnrollOnlyEmail` | A Boolean indicating whether email should be the only permitted MFA device. |
| `resendOtpAttempts`  | The number of times the user has resent the OTP.                            |
| `p1MFADeviceId`      | The device ID for the device being registered.                              |

---

---
title: Verified Frontline Workers flow pack Release Notes
description: New features and improvements in Verified Frontline Workers flow pack.
component: pingone-solutions
page_id: pingone-solutions:frontline-workers:release-notes/frontline-release-notes
canonical_url: https://docs.pingidentity.com/pingone-solutions/frontline-workers/release-notes/frontline-release-notes.html
llms_txt: https://docs.pingidentity.com/pingone-solutions/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["release-notes/index.adoc"]
section_ids:
  september-21: September 21
  initial-release: Initial Release
---

# Verified Frontline Workers flow pack Release Notes

New features and improvements in Verified Frontline Workers flow pack.

Subscribe to get automatic updates: [icon: rss-square, set=fa][Verified Frontline Workers flow pack Release Notes RSS feed](release-notes/frontline-release-notes.xml)

## September 21

### Initial Release

New

This is the initial release of the Verified Frontline Workers flow pack solution.