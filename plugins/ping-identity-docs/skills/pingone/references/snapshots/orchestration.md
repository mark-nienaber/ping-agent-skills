---
title: Adding an authentication experience
description: Add sign-on experiences to PingOne in the Design Center.
component: pingone
page_id: pingone:orchestration:p1_design_center_adding_experiences
canonical_url: https://docs.pingidentity.com/pingone/orchestration/p1_design_center_adding_experiences.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 23, 2026
---

# Adding an authentication experience

Create experiences in the **Design Center** that you can then assign to applications to determine how users sign on.

You must have the Environment Admin role or a custom role with equivalent permissions to add experiences.

The sign-on pattern you select determines the available settings for the experience.

You can add the following types of sign-on experiences:

* [Username and Password](p1_design_center_add_experience_email_pw.html)

* [Identifier First](p1_design_center_add_experience_ident_first.html)

* [Identity Provider First](p1_design_center_add_experience_idp_first.html)

---

---
title: Adding an experience - Identifier First
description: Quickly add an Identifier First experience in the PingOne Design Center.
component: pingone
page_id: pingone:orchestration:p1_design_center_add_experience_ident_first
canonical_url: https://docs.pingidentity.com/pingone/orchestration/p1_design_center_add_experience_ident_first.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 5, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result
---

# Adding an experience - Identifier First

You can add sign-on experiences from the PingOne **Design Center**.

The **Identifier First** experience allows you to identify users before you authenticate them. You can set up rules that will take different authentication actions based on who the user is.

## Before you begin

You must have the Environment Admin role or a custom role with equivalent permissions to add experiences.

## Steps

1. In the PingOne admin console, go to **Orchestration > Design Center** and click the **Plus** icon ([icon: plus, set=fa]).

2. On the **Choose a Sign-On Pattern** page, click **Identifier First**, then click **Next**.

   ![A screenshot of the Choose a Sign-On Pattern page with the Identifier First sign-on type selected. The Preview pane on the right shows a visualization of the experience you're building.](_images/p1-experiences-choose-sign-on-type-identifier-first.png)

   You configure the experience using controls in the left pane. As you update your configuration, the **Preview** pane on the right updates to display a visualization of the experience you're building.

3. On the **Details** tab, enter a name and description for the experience, then click **Next**.

4. []()(Optional) Configure additional primary sign-on methods and the **Remember Username** option.

   You can select multiple sign-on methods.

   | Method                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Password**           | **Password** is selected by default because it is required as a fallback method for identifier first authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | **Passwordless**       | Select this option to allow passwordless authentication for the experience.![A screenshot of the Passwordless option for an Identifier First\] experience. The FIDO2 Passkey Sign-On option is selected.](_images/p1-design-center-id-first-passwordless-fido2-only.png)**FIDO2 Passkey Sign-On (No Username)**Select to allow users to sign on using device-level credentials according to the FIDO2 standard.You must have at least one multi-factor authentication (MFA) policy that allows FIDO2 authentication configured in the environment to select this option. Learn more in [Configuring FIDO2 authentication (Passkeys)](../strong_authentication_mfa/p1_strong_auth_configuring_fido.html).After you select this option, select the applicable MFA policy from the **Policy to Evaluate** list.                                                                                      |
   | **Identity Providers** | Select to allow users to authenticate using an external identity provider (IdP), such as Google, Facebook, or a custom OIDC or SAML provider.You must have at least one IdP configured in the environment to use this option. Learn more in [External IdPs](../integrations/p1_external_idps.html).After you select this option, select an IdP from the **Identity Providers** list and click **Add Identity Provider**.![A screenshot of the Identity Providers options in Design Center. The BX IdP is added to the list.](_images/p1-experiences-idp-options.png)You can add multiple IdPs by clicking **Add another Identity Provider**. If you select more than one, users can choose which IdP to use when signing on.Click the **More Options** (⋮) icon and select **Edit Identity Provider** to view and edit the IdP in a new tab, or click **Remove** to remove the IdP from the list. |
   | **Remember Username**  | The **Remember Username** option is independent of the sign-on methods you select.Select to save the username for users that have authenticated successfully at least once. The user must still provide their password or other credentials to complete sign-on.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | **Session Timeout**    | The **Session Timeout** option is independent of the sign-on methods you select.Select to require users to reauthenticate after the specified time period.After you select this option, configure the time period by selecting a number and a unit of time in the **Authentication Timeout** fields. For example, if you select **4 Hours**, users must sign on again if their last sign-on was more than 4 hours ago.![A screenshot of the Session Timeout options in Design Center. The timeout is set to 4 Hours.](_images/p1-design-center-session-to.png)&#xA;&#xA;If you configure PingOne Protect features in your experience, the risk policy might override this setting based on the policy settings and whether or not a potential security risk is indicated. Learn more in Risk policies.                                                                                            |

5. Click **Next**.

6. (Optional) On the **MFA and Security** tab, select **Enable Multi-Factor Authentication** to require MFA in the experience, then configure the MFA settings:

   | Method                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Multi-Factor Authentication** | Select one of the following two options for MFA:* **Adaptive MFA (Risk-based)**

     Applicable only to environments that include PingOne Protect.

     After you select this option, select a risk policy in the **Policy to Evaluate** list.

     Based on the selected policy, risk signals are evaluated to determine whether to require users to complete an MFA step. For example, the policy might require MFA only when a user is signing on from a new device or location.

     &#xA;&#xA;This list only shows risk policies that include a mitigation rule configured to support MFA. The Returned Action for the mitigation must be one of the following:&#xA;&#xA;Deny: Don't allow the user to sign on if the risk policy is triggered.&#xA;&#xA;MFA: Prompt the user to complete an MFA step if the risk policy is triggered.&#xA;&#xA;Approve: Allow the user to sign on without requiring MFA even if the risk policy is triggered.

     Learn more in [Risk policies](../threat_protection_using_pingone_protect/p1_protect_risk_policies.html).- **Standard MFA**

     You must have at least one MFA policy configured in the environment to use this option.

     After you select this option, select an MFA policy in the **Policy to Evaluate** list. Based on the policy, users must confirm their identity during sign on using a second factor enabled in the policy. Learn more in [Configuring an MFA policy for strong authentication](../strong_authentication_mfa/p1_creating_an_mfa_policy_for_strong_auth.html).![A screenshot of the Multi-factor Authentication section. The Adaptive MFA (Risk-based) option is selected.](_images/p1-experiences-mfa-security-options.png) |
   | **MFA Session Timeout**         | Select to require users to complete MFA again after a specified time period. This option is independent of the **Session Timeout** option, which determines when users must reauthenticate with their primary credentials. With **MFA Session Timeout** enabled, users must complete an MFA step again if their session exceeds the specified time period.After you select this option, configure the time period by selecting a number and a unit of time in the **MFA Session Timeout** fields. For example, if you select **12 Hours**, users must complete an MFA step again if their last MFA prompt was completed more than 12 hours ago.![A screenshot of the MFA Session Timeout options in Design Center. The timeout is set to 12 Hours.](_images/p1-design-center-mfa-session-to.png)&#xA;&#xA;If you've enabled adaptive (risk-based) MFA in the experience, the risk policy might override this setting based on the policy settings and whether or not a potential security risk is indicated. Learn more in Risk policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | **MFA Enrollment**              | Select to allow users to sign on with just their username and password, but then require them to configure a second authentication method, such as a passkey or one-time passcode (OTP).After you select this option, select the applicable MFA policy from the **Policy to Evaluate** list. Allowed methods are determined by the MFA policy you select.To require users to enroll in MFA during sign-on, select the **MFA Enrollment Required** checkbox. If disabled, users who didn't enroll an MFA device during registration are prompted to enroll during their next authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

7. Click **Next**.

8. (Optional) On the **Account Recovery** tab, select **Allow Account Recovery** to enable users to recover their accounts if they forget their password.

   An OTP is sent to the email address configured in the PingOne user directory for account recovery.

   If your environment includes PingOne Protect, after selecting **Allow Account Recovery** you can select a risk policy from the **Policy to Evaluate** list. Selecting a risk policy allows you to evaluate risk signals and prevent unauthorized account recovery attempts. For example, the policy might block account recovery attempts from certain locations or devices, or require users to complete an MFA step to recover their account. Learn more in [Risk policies](../threat_protection_using_pingone_protect/p1_protect_risk_policies.html).

9. Click **Next**.

10. (Optional) On the **Registration** tab, select **Allow Registration** to let users register for an account if they don't have one yet.

    After you select this option, configure the following registration settings:

    | Setting                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | **Population**            | Select the population to add users to when they register using this experience. You can select only one population for registration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | **Attributes to Collect** | **Email Address** and **Password** are selected and required by default. **Email Address** is also used as the **Username** for users that register through this experience.![A screenshot of the Attributes to Collect options for an Identifier First experience. The Email Address and Password attributes are selected. Both are marked as required, but Password can be removed or marked optional.](_images/p1-design-center-atts-to-collect-id-first.png)Click **+ Add Attribute** to select additional attributes to collect during registration. You can select from standard attributes that are configured in the environment directory.Select the **Required** checkbox to require users to provide a value for an attribute. If **Required** isn't selected, the attribute is optional.The attributes you select are added to the registration form in the order you select them.Click the **Delete** icon ([icon: trash, set=fa]) to remove an attribute.&#xA;&#xA;If you selected a Passwordless sign-on method in step 4, you can't make the Password attribute optional, but you can remove it. The Email Address attribute can't be removed.Learn more in [User Attributes](../directory/p1_user_attributes.html). |
    | **MFA Enrollment**        | Select to allow users to configure a second authentication method, such as a passkey or one-time passcode (OTP), during the registration process.&#xA;&#xA;If you selected a passwordless sign-on method on the First Factor tab, this option is selected by default, but you can clear the checkbox to remove it.After you select this option, select the applicable MFA policy from the **Policy to Evaluate** list. Allowed methods are determined by the MFA policy you select.To require MFA enrollment during the registration process, select the **MFA Enrollment Required** checkbox. If this option is disabled, MFA enrollment during registration is optional during registration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    | **Account Verification**  | Select the **Require Verification** checkbox to require users to verify their email address by entering an OTP sent to their email to complete the registration process. This option uses the email address collected during registration and stored in the PingOne user directory.&#xA;&#xA;Account verification is a one-time process that occurs only during registration. It is not an MFA step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | **Bot Detection**         | Applicable only to environments that include PingOne Protect.Select the **Enable Bot Detection** checkbox to help prevent denial-of-service (DOS) attacks and the creation of fake user accounts by detecting non-human behavior, automated frameworks, and recorders.After you select this option, select the applicable policy from the **Risk Policy** list. Learn more in [Risk policies](../threat_protection_using_pingone_protect/p1_protect_risk_policies.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | **Terms of Service**      | You must have at least one agreement configured in the environment to use this option. Learn more in [Agreements](../user_experience/p1_agreements.html).Select the **Require Consent** checkbox to require that users consent to a terms of service agreement when they register for an account.After you select this option, select the applicable agreement from the **Agreement** list.The agreement description and available languages display for your review.![A screenshot of the Terms of Service options in the experience builder. The Require Consent checkbox is selected, and the New agreement is selected in the Agreement list.](_images/p1-design-center-terms-of-service.png)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

11. Click **Next**.

12. On the **Branding & Theme** tab, select a theme to apply to the experience.

    * By default, the active theme for the environment is selected. Click a different theme to select it.

      The **Preview** pane updates to show the experience with the new theme applied.

    * Click the **More Options** (⋮) icon and select **Edit** to view and edit the theme in a new tab, or click the **Create a new theme** link to add a new one. Learn more in [Branding and Themes](../user_experience/p1_branding_themes.html).

13. Click **Next**.

14. On the **Summary** tab, review the selections you've made for your authentication experience.

15. Click **Save**.

## Result

After you save the experience, you're returned to the **Design Center** and the following occurs:

* The new experience is available in the list of available experiences in the **Design Center**. You can edit, duplicate, or delete experiences from this list.

  ![A screenshot of the Design Center page showing the list of three available experiences and the More Options menu.](_images/p1-design-center-list-experiences-with-menu.png)

* The unique read-only sign-on and registration forms for the experience are listed in the **Design Center Forms** section of the **DaVinci Forms** page. You can view the forms, but you can't edit them directly. If you want to customize the forms, you can duplicate them and edit the copies. Learn more in [DaVinci Forms](../user_experience/p1_forms.html).

  ![A screenshot of the Forms page showing the read-only forms for experiences.](_images/p1-design-center-read-only-forms.png)

  |   |                                                                                                                                                              |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If you created an **Identity Provider First** experience or another experience for which you didn't enable registration, there won't be a registration form. |

  Additional read-only forms are created and shared across experiences.

* The experience is available on the **Policies** tab for applications as a DaVinci flow policy that you can assign to the application. Learn more in [Authentication policies for applications](../applications/p1_auth_policies_for_applications.html) and [Applying authentication policies to an application](../applications/p1_apply_auth_policy_to_applications.html).

  ![A screenshot of the DaVinci Policies tab for an application showing several experiences which are outlined with a red box.](_images/p1-experiences-in-app-for-policy-selection.png)

* The experience is available in the PingOne DaVinci admin console as a read-only DaVinci flow. If you want to view the flow, you can click **DaVinci** in the PingOne sidebar to open the DaVinci admin console, and then click **Flows**. The applicable flows include a **Design Center** label.

  If you want to refine your experience further to use it for more complex use cases, you can clone and edit the flow in DaVinci.

  |   |                                                                                                                                                                                                                                                      |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | You must have the DaVinci Admin role or a custom role with equivalent permissions to clone and customize these flows. If you only want to view the flow, you can have the DaVinci Admin Read Only role or a custom role with equivalent permissions. |

  Learn more in [Cloning a flow](https://docs.pingidentity.com/davinci/flows/davinci_cloning_a_flow.html) and [How to manage flows](https://docs.pingidentity.com/davinci/flows/davinci_how_to_manage_existing_flows.html) in the DaVinci documentation.

  ![A screenshot of the DaVinci admin console showing two read-only flows for experiences.](_images/p1-experiences-read-only-flow-in-dv.png)

---

---
title: Adding an experience - Identity Provider First
description: Quickly add an Identity Provider First experience in the PingOne Design Center.
component: pingone
page_id: pingone:orchestration:p1_design_center_add_experience_idp_first
canonical_url: https://docs.pingidentity.com/pingone/orchestration/p1_design_center_add_experience_idp_first.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 5, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result
---

# Adding an experience - Identity Provider First

You can add sign-on experiences from the PingOne **Design Center** page.

The **Identity Provider First** experience allows users to access your applications by bypassing the PingOne sign-on prompt and authenticating directly with the external identity provider (IdP). PingOne provides multi-factor authentication (MFA).

## Before you begin

You must have the Environment Admin role or a custom role with equivalent permissions to add experiences.

You must have at least one external IdP configured in your environment to select this experience. Learn more in [External IdPs](../integrations/p1_external_idps.html).

## Steps

1. In the PingOne admin console, go to **Orchestration > Design Center** and click the **Plus** icon ([icon: plus, set=fa]).

2. On the **Choose a Sign-On Pattern** page, click **Identity Provider First**, then click **Next**.

   ![A screenshot of the Choose a Sign-on Pattern page with the Identity Provider First sign-on pattern selected. The right panel shows a preview of the experience you're building.](_images/p1-experiences-choose-sign-on-type-idp.png)

   You configure the experience using controls in the left pane. As you update your configuration, the **Preview** pane on the right updates to display a visualization of the experience you're building.

3. On the **Details** tab, enter a name and description for the experience, then click **Next**.

4. On the **First Factor** tab, in the **Redirect-Based Sign-In** section, select an IdP in the list and click **Add Identity Provider**.

   ![A screenshot of the First Factor tab for an Identity Provider First experience. An Identity Provider is being added in the Redirect-Based Sign-In section.](_images/p1-experiences-idp-first-first-factor.png)

5. (Optional) Click the **More Options** (⋮) icon and select **Edit Identity Provider** to view and edit the IdP in a new tab, or click **Remove** to remove the IdP from the list.

6. Select the **Session Timeout** option to require users to reauthenticate after the specified time period.

   After you select this option, configure the time period by selecting a number and a unit of time in the **Authentication Timeout** fields. For example, if you select **4 Hours**, users must sign on again if their last sign-on was more than 4 hours ago.

   ![A screenshot of the Session Timeout option. The Session Timeout option is selected, and the Authentication Timeout is set to 4 hours.](_images/p1-design-center-session-to.png)

   |   |                                                                                                                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you configure PingOne Protect features in your experience, this setting might be overridden based on the risk policy selected and whether a potential security risk is indicated. Learn more in [Risk policies](../threat_protection_using_pingone_protect/p1_protect_risk_policies.html). |

7. Click **Next**.

8. (Optional) On the **MFA and Security** tab, select **Enable Multi-Factor Authentication** to require MFA in the experience, then configure the MFA settings:

   | Method                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Multi-Factor Authentication** | Select one of the following two options for MFA:* **Adaptive MFA (Risk-based)**

     Applicable only to environments that include PingOne Protect.

     After you select this option, select a risk policy in the **Policy to Evaluate** list.

     Based on the selected policy, risk signals are evaluated to determine whether to require users to complete an MFA step. For example, the policy might require MFA only when a user is signing on from a new device or location.

     &#xA;&#xA;This list only shows risk policies that include a mitigation rule configured to support MFA. The Returned Action for the mitigation must be one of the following:&#xA;&#xA;Deny: Don't allow the user to sign on if the risk policy is triggered.&#xA;&#xA;MFA: Prompt the user to complete an MFA step if the risk policy is triggered.&#xA;&#xA;Approve: Allow the user to sign on without requiring MFA even if the risk policy is triggered.

     Learn more in [Risk policies](../threat_protection_using_pingone_protect/p1_protect_risk_policies.html).- **Standard MFA**

     You must have at least one MFA policy configured in the environment to use this option.

     After you select this option, select an MFA policy in the **Policy to Evaluate** list. Based on the policy, users must confirm their identity during sign on using a second factor enabled in the policy. Learn more in [Configuring an MFA policy for strong authentication](../strong_authentication_mfa/p1_creating_an_mfa_policy_for_strong_auth.html).![A screenshot of the Multi-factor Authentication section. The Adaptive MFA (Risk-based) option is selected.](_images/p1-experiences-mfa-security-options.png) |
   | **MFA Session Timeout**         | Select to require users to complete MFA again after a specified time period. This option is independent of the **Session Timeout** option, which determines when users must reauthenticate with their primary credentials. With **MFA Session Timeout** enabled, users must complete an MFA step again if their session exceeds the specified time period.After you select this option, configure the time period by selecting a number and a unit of time in the **MFA Session Timeout** fields. For example, if you select **12 Hours**, users must complete an MFA step again if their last MFA prompt was completed more than 12 hours ago.![A screenshot of the MFA Session Timeout options in Design Center. The timeout is set to 12 Hours.](_images/p1-design-center-mfa-session-to.png)&#xA;&#xA;If you've enabled adaptive (risk-based) MFA in the experience, the risk policy might override this setting based on the policy settings and whether or not a potential security risk is indicated. Learn more in Risk policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | **MFA Enrollment**              | Select to allow users to sign on with just their username and password, but then require them to configure a second authentication method, such as a passkey or one-time passcode (OTP).After you select this option, select the applicable MFA policy from the **Policy to Evaluate** list. Allowed methods are determined by the MFA policy you select.To require users to enroll in MFA during sign-on, select the **MFA Enrollment Required** checkbox. If disabled, users who didn't enroll an MFA device during registration are prompted to enroll during their next authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

9. Click **Next**.

10. On the **Summary** tab, review the selections you've made for your authentication experience.

11. Click **Save**.

## Result

After you save the experience, you're returned to the **Design Center** and the following occurs:

* The new experience is available in the list of available experiences in the **Design Center**. You can edit, duplicate, or delete experiences from this list.

  ![A screenshot of the Design Center page showing the list of three available experiences and the More Options menu.](_images/p1-design-center-list-experiences-with-menu.png)

* The unique read-only sign-on and registration forms for the experience are listed in the **Design Center Forms** section of the **DaVinci Forms** page. You can view the forms, but you can't edit them directly. If you want to customize the forms, you can duplicate them and edit the copies. Learn more in [DaVinci Forms](../user_experience/p1_forms.html).

  ![A screenshot of the Forms page showing the read-only forms for experiences.](_images/p1-design-center-read-only-forms.png)

  |   |                                                                                                                                                              |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If you created an **Identity Provider First** experience or another experience for which you didn't enable registration, there won't be a registration form. |

  Additional read-only forms are created and shared across experiences.

* The experience is available on the **Policies** tab for applications as a DaVinci flow policy that you can assign to the application. Learn more in [Authentication policies for applications](../applications/p1_auth_policies_for_applications.html) and [Applying authentication policies to an application](../applications/p1_apply_auth_policy_to_applications.html).

  ![A screenshot of the DaVinci Policies tab for an application showing several experiences which are outlined with a red box.](_images/p1-experiences-in-app-for-policy-selection.png)

* The experience is available in the PingOne DaVinci admin console as a read-only DaVinci flow. If you want to view the flow, you can click **DaVinci** in the PingOne sidebar to open the DaVinci admin console, and then click **Flows**. The applicable flows include a **Design Center** label.

  If you want to refine your experience further to use it for more complex use cases, you can clone and edit the flow in DaVinci.

  |   |                                                                                                                                                                                                                                                      |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | You must have the DaVinci Admin role or a custom role with equivalent permissions to clone and customize these flows. If you only want to view the flow, you can have the DaVinci Admin Read Only role or a custom role with equivalent permissions. |

  Learn more in [Cloning a flow](https://docs.pingidentity.com/davinci/flows/davinci_cloning_a_flow.html) and [How to manage flows](https://docs.pingidentity.com/davinci/flows/davinci_how_to_manage_existing_flows.html) in the DaVinci documentation.

  ![A screenshot of the DaVinci admin console showing two read-only flows for experiences.](_images/p1-experiences-read-only-flow-in-dv.png)

---

---
title: Adding an experience - Username and Password
description: Quickly add a Username and Password experience in PingOne using the Design Center page.
component: pingone
page_id: pingone:orchestration:p1_design_center_add_experience_email_pw
canonical_url: https://docs.pingidentity.com/pingone/orchestration/p1_design_center_add_experience_email_pw.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 5, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result
---

# Adding an experience - Username and Password

You can add sign-on experiences from the PingOne **Design Center**.

The **Username and Password** experience is a common sign-on experience in which users enter a username and password to authenticate.

## Before you begin

You must have the Environment Admin role or a custom role with equivalent permissions to add experiences.

## Steps

1. In the PingOne admin console, go to **Orchestration > Design Center** and click the **Plus** icon ([icon: plus, set=fa]).

2. On the **Choose a Sign-On Pattern** page, click **Username and Password**, then click **Next**.

   ![A screenshot of the Choose a Sign-On Pattern page with Username and Password selected. The Preview pane on the right shows a visualization of the experience you're building.](_images/p1-experiences-choose-sign-on-type-username-pw.png)

   You configure the experience using controls in the left pane. As you update your configuration, the **Preview** pane on the right updates to display a visualization of the experience you're building.

3. On the **Details** tab, enter a name and description for the experience, then click **Next**.

4. (Optional) On the **First Factor** tab, configure additional primary sign-on methods and the **Remember Username** and **Session Timeout** options.

   You can select multiple sign-on methods.

   | Method                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Password**                | **Password** is selected by default because you selected the **Username and Password** sign-on pattern.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | **Passkey (FIDO2) Sign-On** | Select to allow users to sign on using device-level credentials according to the FIDO2 standard.You must have at least one multi-factor authentication (MFA) policy that allows FIDO2 authentication configured in the environment to select this option. Learn more in [Configuring FIDO2 authentication (Passkeys)](../strong_authentication_mfa/p1_strong_auth_configuring_fido.html).After you select this option, select the applicable policy from the **MFA Policy** list.![A screenshot of the Passkey (FIDO2) Sign-on options in the experience builder. The Default MFA Policy is selected in the MFA Policy list.](_images/p1-experiences-fido2-passkey-options.png)                                                                                                                                                                                                                   |
   | **Identity Providers**      | Select to allow users to authenticate using an external identity provider (IdP), such as Google, Facebook, or a custom OIDC or SAML provider.You must have at least one IdP configured in the environment to use this option. Learn more in [External IdPs](../integrations/p1_external_idps.html).After you select this option, select an IdP from the **Identity Providers** list and click **Add Identity Provider**.![A screenshot of the Identity Providers options in Design Center. The BX IdP is added to the list.](_images/p1-experiences-idp-options.png)You can add multiple IdPs by clicking **Add another Identity Provider**. If you select more than one, users can choose which IdP to use when signing on.Click the **More Options** (⋮) icon and select **Edit Identity Provider** to view and edit the IdP in a new tab, or click **Remove** to remove the IdP from the list. |
   | **Remember Username**       | The **Remember Username** option is independent of the sign-on methods you select.Select to save the username for users that have authenticated successfully at least once. The user must still provide their password or other credentials to complete sign-on.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | **Session Timeout**         | The **Session Timeout** option is independent of the sign-on methods you select.Select to require users to reauthenticate after the specified time period.After you select this option, configure the time period by selecting a number and a unit of time in the **Authentication Timeout** fields. For example, if you select **4 Hours**, users must sign on again if their last sign-on was more than 4 hours ago.![A screenshot of the Session Timeout options in Design Center. The timeout is set to 4 Hours.](_images/p1-design-center-session-to.png)&#xA;&#xA;If you configure PingOne Protect features in your experience, the risk policy might override this setting based on the policy settings and whether or not a potential security risk is indicated. Learn more in Risk policies.                                                                                            |

5. Click **Next**.

6. (Optional) On the **MFA and Security** tab, select **Enable Multi-Factor Authentication** to require MFA in the experience, then configure the MFA settings:

   | Method                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Multi-Factor Authentication** | Select one of the following two options for MFA:* **Adaptive MFA (Risk-based)**

     Applicable only to environments that include PingOne Protect.

     After you select this option, select a risk policy in the **Policy to Evaluate** list.

     Based on the selected policy, risk signals are evaluated to determine whether to require users to complete an MFA step. For example, the policy might require MFA only when a user is signing on from a new device or location.

     &#xA;&#xA;This list only shows risk policies that include a mitigation rule configured to support MFA. The Returned Action for the mitigation must be one of the following:&#xA;&#xA;Deny: Don't allow the user to sign on if the risk policy is triggered.&#xA;&#xA;MFA: Prompt the user to complete an MFA step if the risk policy is triggered.&#xA;&#xA;Approve: Allow the user to sign on without requiring MFA even if the risk policy is triggered.

     Learn more in [Risk policies](../threat_protection_using_pingone_protect/p1_protect_risk_policies.html).- **Standard MFA**

     You must have at least one MFA policy configured in the environment to use this option.

     After you select this option, select an MFA policy in the **Policy to Evaluate** list. Based on the policy, users must confirm their identity during sign on using a second factor enabled in the policy. Learn more in [Configuring an MFA policy for strong authentication](../strong_authentication_mfa/p1_creating_an_mfa_policy_for_strong_auth.html).![A screenshot of the Multi-factor Authentication section. The Adaptive MFA (Risk-based) option is selected.](_images/p1-experiences-mfa-security-options.png) |
   | **MFA Session Timeout**         | Select to require users to complete MFA again after a specified time period. This option is independent of the **Session Timeout** option, which determines when users must reauthenticate with their primary credentials. With **MFA Session Timeout** enabled, users must complete an MFA step again if their session exceeds the specified time period.After you select this option, configure the time period by selecting a number and a unit of time in the **MFA Session Timeout** fields. For example, if you select **12 Hours**, users must complete an MFA step again if their last MFA prompt was completed more than 12 hours ago.![A screenshot of the MFA Session Timeout options in Design Center. The timeout is set to 12 Hours.](_images/p1-design-center-mfa-session-to.png)&#xA;&#xA;If you've enabled adaptive (risk-based) MFA in the experience, the risk policy might override this setting based on the policy settings and whether or not a potential security risk is indicated. Learn more in Risk policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | **MFA Enrollment**              | Select to allow users to sign on with just their username and password, but then require them to configure a second authentication method, such as a passkey or one-time passcode (OTP).After you select this option, select the applicable MFA policy from the **Policy to Evaluate** list. Allowed methods are determined by the MFA policy you select.To require users to enroll in MFA during sign-on, select the **MFA Enrollment Required** checkbox. If disabled, users who didn't enroll an MFA device during registration are prompted to enroll during their next authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

7. Click **Next**.

8. (Optional) On the **Account Recovery** tab, select **Allow Account Recovery** to enable users to recover their accounts if they forget their password.

   An OTP is sent to the email address configured in the PingOne user directory for account recovery.

   If your environment includes PingOne Protect, after selecting **Allow Account Recovery** you can select a risk policy from the **Policy to Evaluate** list. Selecting a risk policy allows you to evaluate risk signals and prevent unauthorized account recovery attempts. For example, the policy might block account recovery attempts from certain locations or devices, or require users to complete an MFA step to recover their account. Learn more in [Risk policies](../threat_protection_using_pingone_protect/p1_protect_risk_policies.html).

9. Click **Next**.

10. (Optional) On the **Registration** tab, select **Allow Registration** to let users register for an account if they don't have one yet.

    After you select this option, configure the following registration settings:

    | Setting                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
    | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | **Population**            | Select the population to add users to when they register using this experience. You can select only one population for registration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
    | **Attributes to Collect** | **Email Address** and **Password** are required and selected by default. **Email Address** is also used as the **Username** for users that register through this experience.![A screenshot of the Attributes to Collect options when the Username and Password sign-on pattern is selected. The Email Address and Password attributes are selected and required.](_images/p1-design-center-atts-to-collect-un-pw.png)Click **+ Add Attribute** to select additional attributes to collect during registration. You can select from standard attributes that are configured in the environment directory.Select the **Required** checkbox to require users to provide a value for an attribute. If **Required** isn't selected, the attribute is optional.The attributes you select are added to the registration form in the order you select them.Click the **Delete** icon ([icon: trash, set=fa]) to remove an attribute.Learn more about user attributes in [User Attributes](../directory/p1_user_attributes.html). |
    | **MFA Enrollment**        | Select to allow users to configure a second authentication method, such as a passkey or one-time passcode (OTP), during the registration process.&#xA;&#xA;If you selected a passwordless sign-on method on the First Factor tab, this option is selected by default, but you can clear the checkbox to remove it.After you select this option, select the applicable MFA policy from the **Policy to Evaluate** list. Allowed methods are determined by the MFA policy you select.To require MFA enrollment during the registration process, select the **MFA Enrollment Required** checkbox. If this option is disabled, MFA enrollment during registration is optional during registration.                                                                                                                                                                                                                                                                                                                           |
    | **Account Verification**  | Select the **Require Verification** checkbox to require users to verify their email address by entering an OTP sent to their email to complete the registration process. This option uses the email address collected during registration and stored in the PingOne user directory.&#xA;&#xA;Account verification is a one-time process that occurs only during registration. It is not an MFA step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
    | **Bot Detection**         | Applicable only to environments that include PingOne Protect.Select the **Enable Bot Detection** checkbox to help prevent denial-of-service (DOS) attacks and the creation of fake user accounts by detecting non-human behavior, automated frameworks, and recorders.After you select this option, select the applicable policy from the **Risk Policy** list. Learn more in [Risk policies](../threat_protection_using_pingone_protect/p1_protect_risk_policies.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | **Terms of Service**      | You must have at least one agreement configured in the environment to use this option. Learn more in [Agreements](../user_experience/p1_agreements.html).Select the **Require Consent** checkbox to require that users consent to a terms of service agreement when they register for an account.After you select this option, select the applicable agreement from the **Agreement** list.The agreement description and available languages display for your review.![A screenshot of the Terms of Service options in the experience builder. The Require Consent checkbox is selected, and the New agreement is selected in the Agreement list.](_images/p1-design-center-terms-of-service.png)                                                                                                                                                                                                                                                                                                                        |

11. Click **Next**.

12. On the **Branding & Theme** tab, select a theme to apply to the experience.

    * By default, the active theme for the environment is selected. Click a different theme to select it.

      The **Preview** pane updates to show the experience with the new theme applied.

    * Click the **More Options** (⋮) icon and select **Edit** to view and edit the theme in a new tab, or click the **Create a new theme** link to add a new one. Learn more in [Branding and Themes](../user_experience/p1_branding_themes.html).

13. Click **Next**.

14. On the **Summary** tab, review the selections you've made for your authentication experience.

15. Click **Save**.

## Result

After you save the experience, you're returned to the **Design Center** and the following occurs:

* The new experience is available in the list of available experiences in the **Design Center**. You can edit, duplicate, or delete experiences from this list.

  ![A screenshot of the Design Center page showing the list of three available experiences and the More Options menu.](_images/p1-design-center-list-experiences-with-menu.png)

* The unique read-only sign-on and registration forms for the experience are listed in the **Design Center Forms** section of the **DaVinci Forms** page. You can view the forms, but you can't edit them directly. If you want to customize the forms, you can duplicate them and edit the copies. Learn more in [DaVinci Forms](../user_experience/p1_forms.html).

  ![A screenshot of the Forms page showing the read-only forms for experiences.](_images/p1-design-center-read-only-forms.png)

  |   |                                                                                                                                                              |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If you created an **Identity Provider First** experience or another experience for which you didn't enable registration, there won't be a registration form. |

  Additional read-only forms are created and shared across experiences.

* The experience is available on the **Policies** tab for applications as a DaVinci flow policy that you can assign to the application. Learn more in [Authentication policies for applications](../applications/p1_auth_policies_for_applications.html) and [Applying authentication policies to an application](../applications/p1_apply_auth_policy_to_applications.html).

  ![A screenshot of the DaVinci Policies tab for an application showing several experiences which are outlined with a red box.](_images/p1-experiences-in-app-for-policy-selection.png)

* The experience is available in the PingOne DaVinci admin console as a read-only DaVinci flow. If you want to view the flow, you can click **DaVinci** in the PingOne sidebar to open the DaVinci admin console, and then click **Flows**. The applicable flows include a **Design Center** label.

  If you want to refine your experience further to use it for more complex use cases, you can clone and edit the flow in DaVinci.

  |   |                                                                                                                                                                                                                                                      |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | You must have the DaVinci Admin role or a custom role with equivalent permissions to clone and customize these flows. If you only want to view the flow, you can have the DaVinci Admin Read Only role or a custom role with equivalent permissions. |

  Learn more in [Cloning a flow](https://docs.pingidentity.com/davinci/flows/davinci_cloning_a_flow.html) and [How to manage flows](https://docs.pingidentity.com/davinci/flows/davinci_how_to_manage_existing_flows.html) in the DaVinci documentation.

  ![A screenshot of the DaVinci admin console showing two read-only flows for experiences.](_images/p1-experiences-read-only-flow-in-dv.png)

---

---
title: Deleting an experience
description: Delete a sign-on experience that you no longer need from the Design Center in PingOne.
component: pingone
page_id: pingone:orchestration:p1_design_center_delete_experience
canonical_url: https://docs.pingidentity.com/pingone/orchestration/p1_design_center_delete_experience.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 23, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result
---

# Deleting an experience

You can remove a sign-on experience that you no longer need from the **Design Center**.

## Before you begin

To delete an experience, you must have the Environment Admin role or a custom role with equivalent permissions.

## Steps

1. In the PingOne admin console, go to **Orchestration > Design Center** and browse or search for the experience you want to delete.

2. Click the **More Options** (⋮) icon and select **Delete**.

3. In the confirmation modal, click **Delete**.

## Result

After you delete an experience, the following occurs:

* The experience is removed from your PingOne environment and is no longer visible in the **Design Center**.

* The experience is no longer available to assign to applications.

  If the experience was previously assigned to an application, the application reverts to using any other DaVinci policies that might be assigned, or to the default authentication policy if no other policies are set. Learn more about default policies in [Authentication policies for applications](../applications/p1_auth_policies_for_applications.html).

  |   |                                                                                                                                                                                                                                                                                                                                                                       |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Clean up any references to deleted experiences by removing the references to the policies in the application configuration.![A screenshot of the application configuration Policies tab showing the warning that a policy was deleted and advising to remove the reference to the deleted policy.](../_images/p1-applications-clean-up-deleted-policy-references.png) |

* The read-only flow for the experience is removed from PingOne DaVinci.

* The unique read-only sign-on and registration forms for the experience are removed from the **Design Center Forms** section of the **Forms** page.

---

---
title: Design Center
description: Use the Design Center in PingOne to quickly set methods for sign-on and define the conditions for when they are applied.
component: pingone
page_id: pingone:orchestration:p1_design_center_experiences
canonical_url: https://docs.pingidentity.com/pingone/orchestration/p1_design_center_experiences.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 12, 2026
section_ids:
  building-the-experience: Building the experience
---

# Design Center

Create and manage sign-on experiences for your users in the PingOne **Design Center**. You can quickly design a basic username and password experience or more advanced experiences that include registration and account recovery capabilities, risk-based multi-factor authentication (MFA), and more. These experiences are powered by PingOne DaVinci flows, and you can assign them to your applications to control how users authenticate.

You must have the Environment Admin role or a custom role with equivalent permissions to add and manage experiences.

![A screenshot of the Design Center page showing a list of experiences.](_images/p1-design-center-experiences-list-main.png)

You can choose from three types of sign-on patterns to implement in your experiences:

| Experience                  | Description                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Username and Password**   | A common sign-on experience in which users enter a username and password to authenticate. Learn more in [Adding an experience - Username and Password](p1_design_center_add_experience_email_pw.html).                                                                                                                                                                                           |
| **Identifier First**        | A sign-on experience that allows users to enter an identifier, such as a username or email address, before being prompted for additional authentication factors. Learn more in [Adding an experience - Identifier First](p1_design_center_add_experience_ident_first.html).                                                                                                                      |
| **Identity Provider First** | A sign-on experience that allows users to bypass the PingOne sign-on prompt and authenticate directly with an external identity provider (IdP) such as Google, Facebook, or a custom OpenID Connect (OIDC) or SAML provider. PingOne provides multi-factor authentication (MFA). Learn more in [Adding an experience - Identity Provider First](p1_design_center_add_experience_idp_first.html). |

Depending on your PingOne license and the services enabled in your environment, experiences can include the following advanced capabilities:

* Passwordless authentication (requires PingOne MFA)

* Adaptive authentication (requires PingOne MFA and PingOne Protect)

* Bot detection during new account registration (requires PingOne Protect)

* Account takeover mitigation (requires PingOne MFA and PingOne Protect)

Completed experiences generate read-only PingOne DaVinci flows that you can clone and edit in DaVinci to support more advanced use cases. You must have the DaVinci Admin role to clone and customize these flows.

## Building the experience

After you select the sign-on pattern you want to use, you're guided through the available capabilities for that sign-on pattern. As you make configuration selections in the left pane, the **Preview** pane on the right updates to show a visualization of the experience you're building.

![A screenshot of the Choose a sign-on pattern page with Username and Password selected. The right panel shows a preview of the experience you're building.](_images/p1-experiences-choose-sign-on-type-username-pw.png)

You can adjust the size of the objects in the **Preview** pane by either:

* Using the **Plus** ([icon: plus, set=fa]) or **Minus** ([icon: minus, set=fa]) icons in the right corner to increase or decrease the zoom level.

  ![A screenshot of the zoom controls in the Preview pane, showing the Plus and Minus icons and the zoom percentage.](_images/p1-experiences-zoom-controls.png)

* Clicking the **Fit-to-window** icon (![A screenshot of the fit-to-window icon.](_images/p1-experiences-fit-to-window-icon.png)) in the upper right corner to resize the contents to use the maximum size that fits in the pane.

---

---
title: Duplicating an experience
description: Duplicate an experience in the PingOne Design Center to use it as a starting point for a new experience.
component: pingone
page_id: pingone:orchestration:p1_design_center_copy_experience
canonical_url: https://docs.pingidentity.com/pingone/orchestration/p1_design_center_copy_experience.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 23, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Duplicating an experience

If you have an existing experience that you want to use as the basis for a new one, you can duplicate and update the experience in the PingOne **Design Center**.

## Before you begin

You must have the Environment Admin role or a custom role with equivalent permissions to duplicate experiences.

## Steps

1. In the PingOne admin console, go to **Orchestration > Design Center** and browse or search for the experience you want to duplicate.

2. Click the **More Options** (⋮) icon and select **Duplicate**.

   **Result**

   When you click **Duplicate**, the following occurs:

   * The copied experience is available from the list of available experiences in the **Design Center**. The experience is created with the same settings as the original experience, except for the name, which is appended with `- copy - <created-date-time>`.

     ![A screenshot of the Design Center page showing a duplicated experience.](_images/p1-experiences-duplicated-exp.png)

   * The copied experience is available on the **Policies** tab for applications as a PingOne DaVinci flow policy that you can assign to the application. Learn more in [Authentication policies for applications](../applications/p1_auth_policies_for_applications.html) and [Applying authentication policies to an application](../applications/p1_apply_auth_policy_to_applications.html).

     ![A screenshot of the Policies tab for an application showing a duplicated experience as a DaVinci policy.](_images/p1-experience-apppolicy-duped-exp.png)

   * The copied experience is available in the DaVinci admin console as a new read-only DaVinci flow.

     ![A screenshot of the DaVinci console showing a duplicated experience as a new read-only DaVinci flow.](_images/p1-experience-duped-in-dv.png)

   * The unique read-only sign-on and registration forms for the copied experience are listed in the **Design Center Forms** section of the **DaVinci Forms** page.

     ![A screenshot of the Design Center Forms page showing the unique read-only sign-on and registration forms for the duplicated experience.](_images/p1-experience-duplicated-readonly-forms.png)

     |   |                                                                                                                                                             |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you duplicated an identity provider first experience or another experience for which you didn't enable registration, there won't be a registration form. |

3. Click the **More Options** (⋮) icon for the new experience and select **Edit**.

4. Update the settings applicable to the experience you are editing.

   Learn more about the settings for the different types of experiences in the following topics:

   * [Adding an experience - Username and Password](p1_design_center_add_experience_email_pw.html)

   * [Adding an experience - Identifier First](p1_design_center_add_experience_ident_first.html)

   * [Adding an experience - Identity Provider First](p1_design_center_add_experience_idp_first.html)

5. Click **Save**.

---

---
title: Editing an experience
description: You can update a sign-on experience in the PingOne Design Center.
component: pingone
page_id: pingone:orchestration:p1_design_center_edit_experience
canonical_url: https://docs.pingidentity.com/pingone/orchestration/p1_design_center_edit_experience.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 23, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Editing an experience

You can make changes to an existing experience from the **Design Center** in PingOne.

|   |                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Changes are applied as soon as you save the updated experience. If the experience is assigned to an application, the sign-on experience for users accessing that application is updated immediately. |

## Before you begin

To edit an experience, you must have the Environment Admin role or a custom role with equivalent permissions.

## Steps

1. In the PingOne admin console, go to **Orchestration > Design Center** and browse or search for the experience you want to edit.

   ![A screenshot of the list of experiences in the Design Center.](_images/p1-design-center-experiences-list-main.png)

2. Click the **More Options** (⋮) icon and select **Edit Experience**.

   ![A screenshot of the list of experiences in the Design Center with the More Options menu open.](_images/p1-design-center-list-experiences-with-menu.png)

3. Update the settings applicable to the experience you're editing.

   Learn more about the settings for experiences in the following topics:

   * [Adding an experience - Username and Password](p1_design_center_add_experience_email_pw.html)

   * [Adding an experience - Identifier First](p1_design_center_add_experience_ident_first.html)

   * [Adding an experience - Identity Provider First](p1_design_center_add_experience_idp_first.html)

4. Click **Save**.

---

---
title: Orchestration
description: The Orchestration section in PingOne provides access to the Design Center and your authentication experiences.
component: pingone
page_id: pingone:orchestration:p1_orchestration_main
canonical_url: https://docs.pingidentity.com/pingone/orchestration/p1_orchestration_main.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 29, 2026
---

# Orchestration

The **Orchestration** section provides access to the **Design Center**, where you can create and manage experiences that define how users authenticate and sign on to your applications.

You must have a license for PingOne DaVinci to see the **Orchestration** section and use the **Design Center**.

Learn more in:

* [Design Center](p1_design_center_experiences.html)

---

---
title: Viewing experiences
description: View the sign-on experiences available in your environment in the PingOne Design Center.
component: pingone
page_id: pingone:orchestration:p1_design_center_view_experiences
canonical_url: https://docs.pingidentity.com/pingone/orchestration/p1_design_center_view_experiences.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 23, 2026
---

# Viewing experiences

View the sign-on experiences available in your PingOne environment by going to **Orchestration > Design Center** in the PingOne admin console.

![A screenshot of the list of experiences in the Design Center.](_images/p1-design-center-experiences-list-main.png)

You can browse or search for a specific experience and click the experience to open the details pane.

Additionally, you can click the **More Options** (⋮) icon for an experience to perform the following tasks:

* **Edit Experience**: Click to update the experience settings. Learn more in [Editing an experience](p1_design_center_edit_experience.html).

* **Duplicate**: Create a copy of the experience to use as a starting point for developing a new one that might have similar settings. Learn more in [Duplicating an experience](p1_design_center_copy_experience.html).

* **Delete**: Remove the experience from the environment. Learn more in [Deleting an experience](p1_design_center_delete_experience.html).