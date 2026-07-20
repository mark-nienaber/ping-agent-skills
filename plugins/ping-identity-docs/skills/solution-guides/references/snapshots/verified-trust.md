---
title: Introduction to verified trust
description: Learn how verified trust enables you to verify identities to provide a higher level of security and trust for your applications and resources.
component: solution-guides
page_id: solution-guides:verified-trust:verified-trust-overview
canonical_url: https://docs.pingidentity.com/solution-guides/verified-trust/verified-trust-overview.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["verified trust", "identity verification", "identity proofing", "identity assurance", "PingOne", "DaVinci", "Verify"]
page_aliases: ["index.adoc"]
section_ids:
  what-is-verified-trust: What is verified trust?
  why-implement-verified-trust: Why implement verified trust?
  use-cases: Use cases
---

# Introduction to verified trust

![A shield with a checkmark in the center, representing verified trust.](_images/verified-trust-logo.png)

Verified trust represents a fundamental paradigm shift from *implicit* to *explicit* trust. Traditionally, identity management acted as a gatekeeper, and if a user had the right credentials, they were granted access. However, the threat landscape has dramatically changed, and traditional credentials are dangerously vulnerable.

Attackers are using agentic AI to automate and scale identity attacks, launching brute force attempts, credential testing, and multi-factor authentication (MFA) prompt-bombing campaigns at machine speed. They've shifted focus from hardened "front doors" to softer "side doors," leveraging social engineering to manipulate privileged users and admins. For example, some attackers have employed real-time deepfakes and synthetic identities to bypass standard checks.

Traditional access controls are insufficient, and the mantra "trust, but verify" is outdated. The new necessity is to verify every interaction because you can no longer assume trust.

## What is verified trust?

Verified trust changes the role of the identity provider by combining verification, authentication, and authorization into a single, real-time control plane for the enterprise. It answers the critical question "Are you really you?" before granting access to sensitive assets. It's a strategic identity framework that fundamentally shifts the focus from managing access to confirming the reality of the user behind the screen. This framework depends on the convergence of three distinct disciplines:

* **Identity security:** Traditional access management, ensuring the right user has access at the right time (authentication and authorization).

* **Identity fraud:** Preventing impersonation and the use of synthetic identities or deepfakes to gain unauthorized access.

* **Identity assurance:** Establishing high confidence that the user is genuinely who they claim to be through the verification of biometrics and government documents.

![A Venn diagram showing the three disciplines of verified trust: identity security, identity fraud, and identity assurance.](_images/verified-trust-venn-diagram.png)

By layering core identity functions like authentication and access with advanced capabilities, including real-time threat detection and identity verification, verified trust empowers organizations to verify users continuously, contextually, and seamlessly.

## Why implement verified trust?

Businesses face daily challenges that can be mitigated by using a verified trust architecture. Now that you understand the concepts, you might be wondering how exactly verified trust can help your organization:

* Organizations are facing "bait-and-switch" schemes, where candidates use deepfakes to pass interviews. Verified onboarding stops this by verifying candidate identities before they can access company systems.

* Attackers target help desk agents to get account credentials reset. A verified help desk experience closes this vulnerability by enforcing biometric and credential verification before an agent can assist.

* Many organizations have experienced internal account takeover (ATO), often driven by MFA fatigue (bombarding users with prompts until they accept). Verified access uses real-time risk signals to stop these attacks without frustrating legitimate users.

Verified trust applies rigorous verification standards to help ensure that the digital identity presented matches the human behind it—for every user, device, and system interaction. Consider how this verification secures the following high-risk workflows:

* **Hiring and onboarding:** Rather than verifying identity days after a candidate has accessed systems, verified trust shifts this process to day zero. By integrating government ID checks, liveness detection, and biometric binding during the application phase, organizations can prevent "bait-and-switch" hiring and issue a reusable digital credential immediately upon offer acceptance.

* **Account recovery and help desk:** The help desk has become a primary "side door" for attackers using social engineering. Verified trust requires that a user verifies their identity (through a mobile biometric check) before an agent resets a password or recovers an account. This heavily reduces reliance on knowledge-based authentication (KBA) or agent discretion.

## Use cases

Learn more about the specific verified trust workflows that we've already built for you in the following use cases:

* [Workforce helpdesk solution using PingOne](verified-trust-helpdesk-pingone.html)

* [Workforce helpdesk solution using PingOne Advanced Identity Cloud](verified-trust-helpdesk-aic.html)

---

---
title: Setting up verified trust for help desk account recovery using PingOne
description: Learn how to implement the verified trust for workforce help desk solution using PingOne to secure your help desk operations and prevent account takeover.
component: solution-guides
page_id: solution-guides:verified-trust:verified-trust-helpdesk-pingone
canonical_url: https://docs.pingidentity.com/solution-guides/verified-trust/verified-trust-helpdesk-pingone.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["verified trust", "identity verification", "help desk", "password reset", "end user", "PingOne", "DaVinci", "Verify"]
section_ids:
  goals: Goals
  what-youll-do: What you'll do
  before-you-begin: Before you begin
  tasks: Tasks
  task_1_import_flows: "Task 1: Importing the DaVinci flow"
  steps: Steps
  result: Result
  task_2_configure_p1verify: "Task 2: Configuring PingOne Verify components to verify end users"
  steps-2: Steps
  task_3_configure_admin_group: "Task 3: Configuring the admin group for account recovery"
  steps-3: Steps
  result-2: Result
  task_4_optional_nodes: "(Optional) Task 4: Enabling optional nodes for expanded functionality"
  vt_helpdesk_ext_idp: Adding an external IdP
  steps-4: Steps
  result-3: Result
  vt_helpdesk_record_failures: Recording end-user verification failures
  steps-to-enable-jira: Steps to enable Jira
  result-4: Result
  steps-to-enable-servicenow: Steps to enable ServiceNow
  result-5: Result
  vt_helpdesk_p1_validation: Validation
  before-you-begin-2: Before you begin
  steps-5: Steps
  troubleshooting: Troubleshooting
  whats-next: What's next
  explore-further: Explore further
  helpdesk_solution_concepts: Concepts
  helpdesk_solution_reference: Reference material
  inputs: Inputs
  outputs: Outputs
---

# Setting up verified trust for help desk account recovery using PingOne

The Verified Trust for Workforce Help Desk Solution provides a robust approach for confirming a user's identity before performing sensitive account actions, such as password resets. This solution lets authorized help desk agents initiate real-time verification requests using government IDs and liveness-checked selfies. This ensures that agents can perform account recovery services with high confidence that the end user is who they say they are.

To implement this solution in your environment, you'll take our pre-built PingOne DaVinci flow and configure the PingOne Verify connector with your environment and policy information. You'll also determine what next steps to take in the account reset journey.

## Goals

After completing this use case, you'll know how to do the following:

* Execute a guided journey where an agent verifies a workforce employee's identity in real time to securely authorize account recovery.

* Configure PingOne Verify to validate government-issued IDs and liveness (selfies) as part of an identity verification policy.

* Configure the DaVinci orchestration flow to manage the interaction between the help desk agent's portal and the end user's verification experience.

## What you'll do

In this use case, you'll learn how to implement the Verified Trust for Workforce Help Desk Solution by doing the following in DaVinci:

* Import the pre-built flow.

* Configure the PingOne Verify connector.

* Specify a PingOne Verify policy to use.

* Specify a PingOne group authorized to perform an account reset.

* Review key optional configurations.

The following diagram provides a high-level overview of the implementation workflow. You can refer back to this map as you work through the steps.

![A diagram showing the workflow for the Verified Trust for Workforce Help Desk solution. The map starts with a review of prerequisites, then moves to importing the pre-built DaVinci flow and configuring the solution. An optional path extends the solution to include functionality for external IdPs and recording verification failures. The map ends with validation steps, troubleshooting tips, and next steps for further customization.](_images/docs-metro-map-vt-helpdesk-p1.png)

## Before you begin

Ensure you have the following:

* A basic understanding of [PingOne Verify](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_start.html)

* Proficiency in:

  * [PingOne SSO](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_p1sso_start.html)

  * [PingOne applications](https://docs.pingidentity.com/pingone/applications/p1_application_types.html)

  * [Using DaVinci flows in applications](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_how_to_implement_a_flow.html)

* A PingOne test environment with the following [services](https://docs.pingidentity.com/pingone/settings/p1_add_a_service.html):

  * PingOne SSO

    * Already configured for authentication with DaVinci

    * Populated with test user data

  * DaVinci

  * PingOne Verify

* Access to your PingOne test environment with the Environment Admin [role assigned](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_manage_admin_roles.html)

If you want to extend the solution's functionality for external identity providers (IdPs) and optional services, as described in [Task 4](#task_4_optional_nodes), you'll need the following additional prerequisites:

* A configured [external IdP](https://docs.pingidentity.com/pingone/integrations/p1_external_idps.html) in PingOne

* A ServiceNow license and administrator access to your account

* A Jira license and the ability to generate a bearer authorization token

Learn more about the concepts and components used in this solution in the [Concepts](#helpdesk_solution_concepts) section.

## Tasks

* [Task 1: Importing the DaVinci flow](#task_1_import_flows)

* [Task 2: Configuring PingOne Verify components to verify end users](#task_2_configure_p1verify)

* [Task 3: Configuring the admin group for account recovery](#task_3_configure_admin_group)

* [(Optional) Task 4: Enabling optional nodes for expanded functionality](#task_4_optional_nodes)

### Task 1: Importing the DaVinci flow

Learn how to import the pre-built DaVinci flow into your test environment.

The DaVinci flow authenticates a help desk agent and confirms their authorization to reset accounts. The agent then specifies an end user and sends them a verification request. The end user verifies their identity and performs a liveness check, which the agent monitors from a real-time dashboard.

#### Steps

1. Download the [Verified Trust for Workforce Help Desk Solution](https://marketplace.pingone.com/item/verified-trust-for-workforce-helpdesk-solution) from the Ping Identity Marketplace.

2. In your DaVinci test environment, on the **Flows** tab, click **Add Flow** and select **Import Flow**.

3. Upload the `verified-trust-for-workforce-helpdesk-solution.json` flow and confirm that the **Import Flow** modal displays the following:

   * In the **Main Workflow** field: `Help Desk Agent Login and End User Verification`

   * In the **Subflows** field: `Help Desk Verify Evaluation`

     ![A screenshot of the Import Flow modal with a main workflow of Help Desk Agent Login and End User Verification and a subflow of Help Desk Verify Evaluation.](_images/import-verified-trust-flows.png)

4. Click **Import**.

#### Result

The DaVinci canvas now displays the Help Desk Agent Login and End User Verification flow. This is the parent flow for the solution and contains a call to the Help Desk Verify Evaluation subflow. You can find both flows listed on the **Flows** page.

### Task 2: Configuring PingOne Verify components to verify end users

Learn how to specify which PingOne Verify policy to use and how to configure the PingOne Verify connector to communicate with your PingOne test environment.

#### Steps

1. In the PingOne admin console, go to your test environment, and then go to **Applications > Applications**.

2. Click the **PingOne DaVinci Connection** application to open the details panel. The **Overview** tab contains values for **Environment ID**, **Client ID**, and **Client Secret**.

   You'll use these to configure the PingOne Verify connector, so keep this panel open.

   ![A screenshot of the PingOne DaVinci Connection application details panel highlighting the Environment ID, Client ID, and Client Secret.](_images/davinci-app-info.png)

   |   |                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | PingOne automatically creates the **PingOne DaVinci Connection** application when you deploy the DaVinci service. The application enables PingOne and DaVinci to communicate with each other. |

3. To open DaVinci, click **DaVinci**.

4. On the **Connectors** tab, click **PingOne Verify** in the list of connectors to open the **PingOne Verify Details** modal.

   ![A screenshot of the PingOne Verify Details modal with the PingOne Environment tab selected.](_images/pingone-verify-details-modal.png)

5. Go back to your PingOne test environment. In the **PingOne DaVinci Connection** details panel, click the **Copy** icon to copy the **Environment ID** value.

6. Paste the value of **Environment ID** into the **Environment ID** field of the **PingOne Verify Details** modal in DaVinci.

7. Repeat the previous two steps for **Client ID** and **Client Secret**.

8. In the **PingOne Verify Details** modal, click **Apply**.

   You've now successfully configured the PingOne Verify connector.

9. In the PingOne admin console, go to your test environment, and then go to **Identity Verification > Verify Policies**.

10. Click **Default Verify Policy** to open the policy details panel.

11. Copy the **ID** value at the top of the panel. This is the PingOne Verify policy ID.

    ![A screenshot of the Default Verify Policy details panel with the ID field highlighted.](_images/pingone-verify-default-policy.png)

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | The default policy is sufficient for testing purposes, but might not be appropriate for production environments.You should configure a custom PingOne Verify policy appropriate for use in your organization's production environments before deploying this solution outside of a test environment. Learn more in [Identity verification using PingOne Verify](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_start.html). |

12. In DaVinci, click the **Variables** tab.

13. Locate the **cv-VerifyPolicyId** variable and click **Edit** to open the **Update Variable** modal.

    ![A screenshot of the Update Variable modal for the cv-VerifyPolicyId variable with the Value field highlighted.](_images/davinci-update-variable-modal.png)

14. Paste the value of **ID** (from the **Default Verify Policy**) into the **Value** field and click **Update**.

    You've now configured the PingOne Verify policy that the flow will use to verify end users.

### Task 3: Configuring the admin group for account recovery

Learn how to authorize help desk agents to perform account resets by specifying an admin group in the Help Desk Agent Login and End User Verification flow.

#### Steps

1. In the PingOne admin console, create a group in your test environment and add a user that is allowed to perform account resets. Learn more in [Create a group](https://docs.pingidentity.com/pingone/pingone_tutorials/p1_p1tutorial_create_a_group.html).

2. Copy the group name. You'll use this name to configure a Functions connector named **Group Check**.

3. To open DaVinci, click **DaVinci**.

4. On the **Flows** tab, select **Help Desk Agent Login and End User Verification**.

5. In the DaVinci flow canvas, go to the **Verification Experience** section and click the Functions connector named **Group Check**.

   ![A screenshot of the DaVinci canvas with the Group Check connector highlighted in the Verification Experience section.](_images/group-check-node-location.png)

6. On the **General** tab of the **Functions** configuration panel, enter the PingOne group name in the **Value** field for **Input Variable 1**. Click **Apply**.

   ![A screenshot of the Functions configuration panel with the Value field for Input Variable 1 highlighted.](_images/group-input-variable.png)

7. At the top of the DaVinci canvas, click **Deploy** to deploy the configured flow in your test environment.

#### Result

You've now configured the PingOne group authorized to perform account recovery.

|   |                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You've now completed the standard configuration for the Verified Trust for Workforce Help Desk Solution. The following task extends the solution's functionality for external IdPs and additional services. If you're not extending the solution, skip to the [Validation](#vt_helpdesk_p1_validation) section. |

### (Optional) Task 4: Enabling optional nodes for expanded functionality

The provided DaVinci flow and subflow contain optional nodes that you can enable and configure. However, you can still take full advantage of the Verified Trust for Workforce Help Desk Solution without performing these steps.

* [Adding an external IdP](#vt_helpdesk_ext_idp)

* [Recording end-user verification failures](#vt_helpdesk_record_failures)

#### Adding an external IdP

You can add an external IdP to authenticate the end user whose account is being verified for recovery. The help desk agent will continue to authenticate using PingOne.

##### Steps

1. In the PingOne admin console, go to your test environment, and then go to **Integrations > External IdPs**. Copy the ID number listed below the name of your external IdP.

2. In DaVinci, open the Help Desk Agent Login and End User Verification flow and navigate to the **Verification Experience** section of the canvas.

3. Right-click the PingOne connector named **Find User** and select **Disable**. The node should become grayed out.

   ![A screenshot of the DaVinci canvas with the context-sensitive menu displayed for the Find User connector. The Disable option is highlighted.](_images/disable-find-user.png)

4. Right-click the grayed-out PingOne Authentication connector named **Sign On with External Identity Provider** and select **Enable**.

   ![A screenshot of the DaVinci canvas with the context-sensitive menu displayed for the Sign On with External Identity Provider connector. The Enable option is highlighted.](_images/enable-ext-id-provider.png)

5. Click the **Sign On with External Identity Provider** connector.

6. In the **PingOne External Identity Provider** list, select your external IdP. Alternatively, you can enter the ID number of the external IdP in the **PingOne External Identity Provider ID** field. Click **Apply**.

   ![A screenshot of the configuration panel for the Sign On with External Identity Provider connector. The PingOne External Identity Provider list is open, with an example external IdP highlighted.](_images/select-ext-idp.png)

7. Click the Flow connector named **Start Verify for Help Desk**.

8. On the **General** tab, do the following:

   1. Configure the **p1UserId** field:

      1. Clear the existing value.

      2. Click **{}**, and then click to enable the **Show all nodes** toggle.

         ![A screenshot of the configuration panel for the Start Verify for Help Desk connector. The Show all nodes toggle is highlighted and enabled.](_images/show-all-nodes-toggle.png)

      3. In the **Choose Connector** list, select the **PingOne Authentication** node named **Sign On With External IDP**.

         ![A screenshot of the options for the Choose Connector list for the p1UserId field. The PingOne Authentication - Sign On With External IDP node is highlighted.](_images/select-pingone-authentication.png)

         A list of available objects and variables displays below the **p1UserId** field.

         ![A screenshot of the available objects and variables that can be used to populate the p1UserId field.](_images/available-pingone-objects.png)

      4. In the list, go to **output > user** and select **id**.

         ![A screenshot of the available objects and variables that can be used to populate the p1UserId field. The id variable is highlighted.](_images/select-external-user-id.png)

         This populates an **id** attribute in the **p1UserId** field. Click above the field to close the list.

         |   |                                                                                              |
         | - | -------------------------------------------------------------------------------------------- |
         |   | Verify that you selected the **id** attribute for **user** and not for **identityProvider**. |

   2. Update all of the remaining user fields, from **userName** to **userReferencePhoto**, with the corresponding user attribute names from your external IdP. This step maps your user attributes to the PingOne schema, enabling the solution to correctly verify your users.

   3. Clear any user fields that don't apply for your users.

   4. Click **Apply**.

9. At the top of the DaVinci canvas, click **Deploy** to redeploy the updated flow in your test environment.

##### Result

You've now enabled and configured the DaVinci flow for end-user authentication with an external IdP.

#### Recording end-user verification failures

You can create a Jira ticket or a ServiceNow incident to record any end-user verification failures for further action.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | You can choose to enable and configure one or both of these services. |

* [Jira](#steps-to-enable-jira)

* [ServiceNow](#steps-to-enable-servicenow)

##### Steps to enable Jira

1. On the DaVinci **Connectors** tab, from the list of connectors, select **Jira Service Desk**.

2. In the **Jira Service Desk Details** modal, configure the required fields according to the [Jira connector](https://docs.pingidentity.com/connectors/jira_connector.html) documentation and click **Apply**.

   ![A screenshot of the Jira Service Desk Details modal.](_images/jira-connector-details.png)

3. On the **Flows** tab, select the **Help Desk Verify Evaluation** flow and go to the **Verification Failure** section of the canvas.

4. Right-click the grayed-out **Create Jira Ticket** connector and select **Enable**.

   ![A screenshot of the DaVinci canvas with the context-sensitive menu displayed for the Create Jira Ticket connector. The Enable option is highlighted.](_images/enable-optional-services.png)

5. To configure the Jira Service Desk connector, click **Create Jira Ticket**.

6. If you haven't already done so, in the **Jira Service Desk** modal, enter the required JSON code in the **Raw JSON for creating new JIRA service desk request** field.

   ![A screenshot of the configuration panel for the Jira Service Desk connector with the Raw JSON for creating new JIRA service desk request field highlighted.](_images/jira-connector-config.png)

7. Enter any other desired configuration values and click **Apply**.

8. At the top of the DaVinci canvas, click **Deploy** to redeploy the updated flow in your test environment.

##### Result

You've now enabled and configured the DaVinci flow to create Jira tickets to record any end-user verification failures.

##### Steps to enable ServiceNow

1. On the DaVinci **Connectors** tab, from the list of connectors, select **ServiceNow**.

2. In the **ServiceNow Details** modal, configure the required fields according to the [ServiceNow Connector](https://docs.pingidentity.com/connectors/servicenow_connector.html) documentation and click **Apply**.

   ![A screenshot of the ServiceNow Details modal.](_images/servicenow-connector-details.png)

3. On the **Flows** tab, select the **Help Desk Verify Evaluation** flow and go to the **Verification Failure** section of the canvas.

4. Right-click the grayed-out **Service Now Incident** connector and select **Enable**.

   ![A screenshot of the DaVinci canvas with the context-sensitive menu displayed for the ServiceNow Incident connector. The Enable option is highlighted.](_images/enable-optional-services.png)

5. To configure the ServiceNow connector, click **Service Now Incident**.

6. In the **ServiceNow** modal, enter the desired configuration values and click **Apply**.

   ![A screenshot of the configuration panel for the ServiceNow connector.](_images/servicenow-connector-config.png)

7. At the top of the DaVinci canvas, click **Deploy** to redeploy the updated flow in your test environment.

##### Result

You've now enabled and configured the DaVinci flow to create ServiceNow incidents to record any end-user verification failures.

## Validation

Now that you've imported the DaVinci flows, configured your PingOne Verify connection, and specified an authorized group for account recovery, you're ready to test the solution.

### Before you begin

Ensure you have the following:

* Access to the username and password for a help desk agent who's a member of the PingOne group authorized for account recovery.

* The email or username of an end user in your PingOne test environment. At minimum, their account should be connected to an email address that you can access to perform verification.

* A mobile device that can access the test end user's email and that has a working camera.

* A valid ID that you can use for testing purposes. Learn more in [PingOne Verify types of verification](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_types_of_verification.html).

### Steps

1. Sign on as the help desk agent:

   1. In the PingOne admin console, go to your test environment, and then go to **Applications > Applications**.

   2. Click the **PingOne DaVinci Connection** application to open the details panel.

   3. On the **Overview** tab, click the **Copy** icon to copy the **Signon URL** value.

   4. Open a web browser and enter the value of **Signon URL**. The **Help Desk Verification** page displays.

      ![A screenshot of the Help Desk Verification page with a Continue button.](_images/help-desk-splash.png)

   5. Click **Click Here to Continue**.

   6. Enter the username of your help desk agent and click **Submit**.

   7. Enter the help desk agent's password and click **Submit**.

2. Initiate the end-user verification:

   1. On the **Help Desk** page, enter the end user's email address or username and click **Continue**.

      ![A screenshot of the Help Desk page with an email address field and a Continue button.](_images/help-desk-username.png)

   2. Click **Email** as the verification method. This sends an email to the end user you specified in the previous step.

      ![A screenshot of the End User Verification page with the Email verification method highlighted.](_images/helpdesk-email-verification-method.png)

   3. Click **Skip** on the **Confirm Verify Transaction Code** page to proceed to the **Call Center Verification** page, which displays a status chip of **Requested**. You are now ready to monitor the end-user verification from the help desk agent's perspective.

      ![A screenshot of the Confirm Verify Transaction Code page with the Skip option highlighted.](_images/helpdesk-skip-code.png)![A screenshot of the Call Center Verification page with a status chip showing Requested.](_images/helpdesk-ready-to-verify.png)

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                              |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | In the end-user experience, on the **Verification Requested** screen, there is a verification code that the help desk agent can enter to confirm that the agent and end user are participating in the same PingOne Verify transaction. In most cases, it's unnecessary to use this code, because the agent typically initiates the PingOne Verify transaction and sends it to the end user during a live phone conversation. |

3. Verify the end-user ID:

   1. Access the test end user's email account from your mobile device. Look for an email from PingOne with the subject line "Finish your ID verification."

   2. Tap the verification link in the email to load the **Verification Requested** screen on your mobile device, and then tap **Begin Verification**.

      ![A screenshot of the Verification Requested screen on a mobile device with a Begin Verification button.](_images/mobile-verification-requested.png)

   3. On the **Scan Your ID** screen, tap **Continue**.

      ![A screenshot of the Scan Your ID screen on a mobile device with a Continue button.](_images/mobile-scan-id.png)

   4. When prompted, allow apps.pingone.com and your mobile browser to use your camera.

   5. Scan the front of your ID and follow the on-screen prompts until you see a checkmark.

   6. When prompted, flip your ID over and scan the back of it.

   7. On the results screen that shows pictures of both sides of your ID, tap **Yes, Continue**.

      The help desk agent's **Call Center Verification** page now updates with the status of the ID check. If the verification was successful, you should see a **Success** status chip next to **Government ID** in the **Verification Requirements** section.

      ![A screenshot of the Call Center Verification page with a Success status chip next to Government ID in the Verification Requirements section.](_images/helpdesk-status-id-verified.png)

4. Verify user liveness and compare with the ID:

   1. On the mobile device, on the **Take a Selfie** screen, tap **Continue**.

      ![A screenshot of the Take a Selfie screen on a mobile device with a Continue button.](_images/mobile-take-selfie.png)

   2. Follow the prompts on your mobile device. After you take the selfie, tap **Continue**.

      The mobile device now displays a **Complete** screen. The end user's portion is completed successfully.

      ![A screenshot of the Complete screen on a mobile device.](_images/mobile-complete.png)

5. Complete the verification:

   The help desk agent's **Call Center Verification** page now displays the status of the verification. If the verification passes, the page displays a **Success** status chip for the overall status, as well as **Success** chips for **User Liveness** and **Facial and Document Comparison**.

   ![A screenshot of the Call Center Verification page with a Success status chip for the overall status, as well as Success chips for User Liveness and Facial and Document Comparison in the Verification Requirements section.](_images/helpdesk-status-success-complete.png)

   At this point, the help desk agent is ready to reset the end user's account. If you click **Continue** to accept the verification, the DaVinci flow proceeds to a success response and displays the **SAML Response** page.

   |   |                                                                                                                                                                                                                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You need to configure the flow to determine the next logical steps to take, including where to redirect the help desk agent's browser, depending on the outcome of the end-user verification.When customizing the solution, you must preserve the required inputs and outputs. Learn more in the [Reference](#helpdesk_solution_reference) section. |

## Troubleshooting

This section provides troubleshooting tips for common issues related to the Verified Trust for Workforce Help Desk Solution.

* The **Try Flow** button doesn't work

  This solution is built to be launched from PingOne. You'll need to go to the sign-on URL of the **PingOne DaVinci Connection** application, as described in the [Validation](#vt_helpdesk_p1_validation) steps.

* The help desk agent can't sign on

  When you enter the help desk agent's credentials on the **Help Desk Verification** page, you receive an error message. Confirm the following:

  * Your PingOne SSO authentication flow is properly configured, as described in [PingOne SSO](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_p1sso_start.html) and [Integrating flows into applications](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_how_to_implement_a_flow.html).

  * Your PingOne connector is configured with the correct application information. For this solution, we used the **PingOne DaVinci Connection** application. Learn more in [Viewing application details](https://docs.pingidentity.com/pingone/applications/p1_viewapplications.html) and [Editing a connector](https://docs.pingidentity.com/davinci/connectors/davinci_editing_a_connection.html).

  * Your two solution flows are properly saved and deployed. Learn more in [Getting started with DaVinci](https://docs.pingidentity.com/davinci/flows/davinci_getting_started.html#testing-early-and-often).

* The help desk agent isn't authorized

  After you sign on as the help desk agent, the flow displays the **Unauthorized** page with the message **You are not authorized for this action**.

  This happens because the help desk agent you specified isn't a member of the appropriate administrator group. You either need to add this agent to the group or specify a different agent who is already a group member. Refer back to the steps in [Configuring the admin group for account recovery](#task_3_configure_admin_group) for more information.

* The end user can't access the verification link

  If the end user doesn't have access to the email addresses or phone numbers configured in their PingOne user account, you can select **No Methods Available** on the help desk agent's **End User Verification** page. The **Provide Details** page then displays, and you can enter an alternate phone number or email address to send the link to.

  ![A screenshot of the End User Verification page with the No Methods Available option highlighted.](_images/helpdesk-troubleshooting-no-methods.png)

* The verification timed out

  If the help desk agent's **Call Center Verification** page displays a message that the verification has timed out, that means the end user didn't perform the verification steps quickly enough. You can click **Retry** to start a new verification transaction and send a new link to the end user. Clicking **Cancel** ends the verification process.

* I want to manually approve a failed verification

  If the end user verification wasn't successful, the help desk agent's **Call Center Verification** page displays a **Fail** status chip. To complete the transaction and record the verification as a failure, click **Continue with Failed Transaction**.

  Alternatively, you can proceed as if the verification didn't fail. To manually approve the verification, click **Bypass Failed Transaction**, and then click **Continue** when asked to confirm.

  |   |                                                                                                                             |
  | - | --------------------------------------------------------------------------------------------------------------------------- |
  |   | As configured, the solution doesn't reset end user accounts, whether verifications succeed, fail, or are manually bypassed. |

## What's next

In the **Help Desk Agent Login and End User Verification** flow, locate the **Sign On Success** and **Sign On Fail** nodes at the bottom of the canvas. These [Teleport connectors](https://docs.pingidentity.com/connectors/teleport_connector.html) lead to the only two outcomes for this solution, returning either a success or error response to the PingOne DaVinci Connection application. As configured, the flow displays these responses on a **SAML Response** page.

As you integrate and promote this solution into higher environments, you should configure your PingOne application to handle these responses according to your desired workflow.

## Explore further

### Concepts

Learn more about the concepts used in the Verified Trust for Workforce Help Desk Solution in the following table:

| Concept                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [DaVinci applications](https://docs.pingidentity.com/davinci/applications/davinci_applications.html)                                            | An application acts as a gateway between your site and the flows you've created in DaVinci.The application contains settings to determine how external sites can send requests for flows, what flows can be requested, and how users and resources from other sites are managed. External sites can only run flows that are made available through an application.                                |
| [DaVinci connectors](https://docs.pingidentity.com/davinci/connectors/davinci_connections.html)                                                 | Connectors form the building blocks for flows. They connect DaVinci with third parties, HTML pages, and other tools.Each connector enables one or more capabilities that you can use as nodes in a flow. When you add a connector, you gain the ability to use its capabilities in your flows.                                                                                                    |
| [DaVinci flows](https://docs.pingidentity.com/davinci/flows/davinci_flows.html)                                                                 | A flow is a user journey, such as authentication or verification, built from a set of capabilities and logical operators.Every flow consists of one or more nodes joined together by logical operators. Each node performs a specific task, using one of the capabilities of your connectors. After the task is complete, the logical operators determine which task or tasks are performed next. |
| [DaVinci flows in applications](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_how_to_implement_a_flow.html) | Integrating a flow into an application lets your users launch the flow from that application.Choose an integration method based on the type of flow and the desired user experience.                                                                                                                                                                                                              |
| [PingOne applications](https://docs.pingidentity.com/pingone/applications/p1_application_types.html)                                            | Add applications to your PingOne environment to manage access to those applications. PingOne supports multiple application types, including SAML, OpenID Connect (OIDC), native, and single-page applications (SPAs).                                                                                                                                                                             |
| [PingOne environments](https://docs.pingidentity.com/pingone/introduction_to_pingone/p1_introduction.html#p1-environments-intro)                | In PingOne, tenants are called environments. Environments define separate working domains within an organization and contain assets such as your PingOne services and Ping Identity products, application connections, and user identities.                                                                                                                                                       |
| [PingOne external IdPs](https://docs.pingidentity.com/pingone/integrations/p1_external_idps.html)                                               | Using an external IdP allows linked users to authenticate using the credentials provided by the external IdP.                                                                                                                                                                                                                                                                                     |
| [PingOne groups](https://docs.pingidentity.com/pingone/directory/p1_groups.html)                                                                | Using groups to organize a collection of user identities makes it easier to manage access to applications.You can create groups within an environment or within a population.                                                                                                                                                                                                                     |
| [PingOne SSO](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_p1sso_start.html)                                           | Using PingOne SSO, users can sign on to all their applications and services with a single set of credentials.PingOne SSO uses identity standards like SAML, OAuth, and OIDC, which allow for encrypted tokens to be transmitted securely between the server and the apps.                                                                                                                         |
| [PingOne Verify](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_start.html)                         | The PingOne Verify service lets you enable secure user verification based on a government-issued document and live face capture (a selfie).                                                                                                                                                                                                                                                       |

### Reference material

If you customize the Help Desk Verify Evaluation subflow, you'll need to make sure to preserve the following flow input and output variables to ensure that the flow operates correctly.

#### Inputs

| Variable name                | Data type | Example value                          | Description                                                                                                                                |
| ---------------------------- | --------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `verifyPolicyId`             | String    | `a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6` | The PingOne Verify policy ID that specifies your verification requirements.                                                                |
| `allowedVerificationMethods` | Array     | `["QR", "SMS", "EMAIL"]`               | The delivery methods you allow for sending a verification transaction link to the end user.                                                |
| `isHelpDesk`                 | Boolean   | `true`                                 | Set this value to `true` if this flow is being invoked by a help desk agent assisting a user.                                              |
| `isAdvancedBioRequired`      | Boolean   | `false`                                | Set this value to `true` to enable advanced logic that compares the available end user data in the directory against the verified ID data. |
| `p1UserId`                   | String    | `z9y8x7w6-v5u4-t3s2-r1q0-p9o8n7m6l5k4` | The generic user ID from PingOne.                                                                                                          |
| `userEmail`                  | String    | `john.doe@example.com`                 | The end user's email (for delivery or matching).                                                                                           |
| `userPhone`                  | String    | `+15551234567`                         | The end user's phone number (for delivery or matching).                                                                                    |
| `userFirstName`              | String    | `John`                                 | The end user's first name.                                                                                                                 |
| `userLastName`               | String    | `Doe`                                  | The end user's last name.                                                                                                                  |
| `userDOB`                    | String    | `1900-12-06`                           | The end user's date of birth.                                                                                                              |
| `cv-navBarHeader`            | String    | `Ping Identity ID Verification Portal` | The text to display in the navigation bar of the help desk agent's UI.                                                                     |

#### Outputs

| Variable name             | Data type | Description                                                                    |
| ------------------------- | --------- | ------------------------------------------------------------------------------ |
| `verifyEvaluationId`      | String    | The unique ID of the completed PingOne Verify transaction.                     |
| `verifyEvaluationOutcome` | String    | The final status of the verification.                                          |
| `selfie`                  | String    | A base64 encoded string of the end user's selfie with the background replaced. |
| `errorMessage`            | String    | If the flow fails, this variable contains a description of the error.          |
| `flowInteractionId`       | String    | The unique identifier for this specific flow execution instance.               |

---

---
title: Setting up Verified Trust for help desk account recovery using PingOne Advanced Identity Cloud
description: Learn how to implement the Verified Trust for Workforce Help Desk Solution with PingOne Advanced Identity Cloud to secure your help desk operations and prevent account takeover.
component: solution-guides
page_id: solution-guides:verified-trust:verified-trust-helpdesk-aic
canonical_url: https://docs.pingidentity.com/solution-guides/verified-trust/verified-trust-helpdesk-aic.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["verified trust", "identity verification", "help desk", "password reset", "end user", "Advanced Identity Cloud", "journeys", "backchannel", "PingOne Verify"]
section_ids:
  goals: Goals
  what-youll-do: What you'll do
  before-you-begin: Before you begin
  tasks: Tasks
  task_1_prerequisites: "Task 1: Setting up prerequisites"
  task_1a_esv: "Step 1a: Configuring ESVs for the PingOne Worker Service"
  steps: Steps
  result: Result
  task_1b_worker: "Step 1b: Configuring the PingOne Worker Service"
  steps-2: Steps
  result-2: Result
  task_1c_email_templates: "Step 1c: Importing email templates"
  steps-3: Steps
  result-3: Result
  task_1d_custom_nodes: "Step 1d: Importing custom nodes"
  steps-4: Steps
  result-4: Result
  task_1e_custom_attributes: "Step 1e: Creating custom user attributes"
  steps-5: Steps
  result-5: Result
  task_2_import_journeys: "Task 2: Importing the journeys"
  phase-1-importing-backchannel-and-inner-journeys: "Phase 1: Importing backchannel and inner journeys"
  steps-6: Steps
  result-6: Result
  phase-2-importing-the-main-and-profile-management-journeys: "Phase 2: Importing the main and profile management journeys"
  steps-7: Steps
  result-7: Result
  task_3_configure_post_import: "Task 3: Configuring post-import journey settings"
  task_3a_journey_settings: "Step 3a: Updating journey settings"
  steps-8: Steps
  result-8: Result
  task_3b_send_verification_link: "Step 3b: Configuring the Send ID Verification Link journey"
  steps-9: Steps
  result-9: Result
  task_3c_user_profile_management: "Step 3c: Configuring the User Profile Management journey"
  steps-10: Steps
  result-10: Result
  task_3d_backchannel_verify: "Step 3d: Configuring the User ID Verification Backchannel journey"
  steps-11: Steps
  result-11: Result
  task_4_configure_worker_service: "Task 4: Extending the journey timeout (optional)"
  steps-12: Steps
  result-12: Result
  task_5_configure_agent_access: "Task 5: Configuring help desk agent access"
  steps-13: Steps
  result-13: Result
  task_6_configure_end_user: "Task 6: Create an end-user account"
  steps-14: Steps
  result-14: Result
  vt_helpdesk_aic_validation: Validation
  before-you-begin-2: Before you begin
  steps-15: Steps
  troubleshooting: Troubleshooting
  whats-next: What's next
  explore-further: Explore further
  helpdesk-aic-concepts: Concepts
---

# Setting up Verified Trust for help desk account recovery using PingOne Advanced Identity Cloud

The Verified Trust for Workforce Help Desk Solution provides a way to confirm a user's identity before performing sensitive account actions, such as password resets and multi-factor authentication (MFA) device resets. This solution lets authorized help desk agents look up a workforce employee, send them a verification link, and monitor the verification status in real time. After the employee verifies their identity using a government-issued ID and a liveness selfie, the agent can securely reset their password or MFA device.

This implementation uses a set of pre-built PingOne Advanced Identity Cloud journeys that work together through PingOne Advanced Identity Cloud's backchannel authentication mechanism. The main agent-facing journey coordinates identity verification and account recovery through a set of inner and backchannel journeys. To implement this solution in your environment, you'll import these journeys and configure them with your PingOne Worker Service and PingOne Verify policy.

## Goals

After completing this use case, you'll know how to:

* Execute a guided journey where a help desk agent verifies a workforce employee's identity in real time to securely authorize account recovery

* Configure PingOne Verify to validate government-issued IDs and liveness (selfies) as part of an identity verification policy.

* Configure the PingOne Advanced Identity Cloud journey nodes to communicate with PingOne using the PingOne Worker Service.

## What you'll do

In this use case, you'll learn how to implement the Verified Trust for Workforce Help Desk Solution by doing the following in PingOne Advanced Identity Cloud:

* Set up prerequisites: email templates, custom nodes, and custom user attributes.

* Import the pre-built journeys in two phases.

* Configure post-import journey settings and node connections.

* Configure help desk agent access using a HelpDesk group.

The following map provides a high-level overview of the implementation workflow. You can refer back to this map as you work through the steps.

![A map showing the workflow for the Verified Trust for Workforce Help Desk solution on PingOne Advanced Identity Cloud. The map starts by preparing prerequisites, then moves to importing the pre-built journeys and configuring the solution. The map ends with validation steps and troubleshooting tips.](_images/docs-metro-map-vt-helpdesk-aic.png)

## Before you begin

Ensure you have:

* A basic understanding of [key PingOne Advanced Identity Cloud concepts](https://docs.pingidentity.com/pingoneaic/getting-started/getting-started-concepts.html) including tenants and realms.

* A basic understanding of [PingOne Verify in PingOne Advanced Identity Cloud](https://docs.pingidentity.com/pingoneaic/integrations/pingone-verify.html).

* Familiarity with:

  * [PingOne Advanced Identity Cloud journeys and nodes](https://docs.pingidentity.com/pingoneaic/journeys/journeys.html).

  * [Setting up PingOne workers as PingOne Advanced Identity Cloud services](https://docs.pingidentity.com/pingoneaic/integrations/pingone-set-up-oidc-clients.html).

  * [Environment secrets and variables (ESVs)](https://docs.pingidentity.com/pingoneaic/tenants/esvs.html).

* A PingOne Advanced Identity Cloud development tenant with the following configured:

  * A PingOne environment mapped to the tenant, with the PingOne Verify service configured

  * A PingOne Worker App configured in PingOne

  * The PingOne Worker App client ID, client secret, and environment ID

* A configured [PingOne Verify policy](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_start.html) in your mapped PingOne environment.

* The PingOne Verify policy ID to use when configuring scripts in PingOne Advanced Identity Cloud.

* Access to the PingOne Advanced Identity Cloud admin console with administrator permissions.

* Access to the PingOne admin console with the [Environment Admin](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_manage_admin_roles.html) role assigned.

* Your mobile device and government-issued identity document to validate the solution.

Learn more about the concepts and components used in this solution in the [Concepts](#helpdesk-aic-concepts) section.

## Tasks

* [Task 1: Setting up prerequisites](#task_1_prerequisites)

* [Task 2: Importing the journeys](#task_2_import_journeys)

* [Task 3: Configuring post-import journey settings](#task_3_configure_post_import)

* [Task 4: Extending the journey timeout (optional)](#task_4_configure_worker_service)

* [Task 5: Configuring help desk agent access](#task_5_configure_agent_access)

* [Task 6: Create an end-user account](#task_6_configure_end_user)

### Task 1: Setting up prerequisites

Learn how to set up the email templates, custom nodes, and custom user attributes required before importing the journeys.

#### Step 1a: Configuring ESVs for the PingOne Worker Service

The journeys use a PingOne Worker Service to communicate with PingOne. You must create ESVs in your PingOne Advanced Identity Cloud tenant to hold the credentials for the worker application.

##### Steps

1. In the PingOne Advanced Identity Cloud admin console, go to **Tenant Settings > Environment Secrets & Variables**.

2. Create the following ESV secret:

   | Name                                  | Description                                  |
   | ------------------------------------- | -------------------------------------------- |
   | `esv-hd-pingone-worker-client-secret` | The client secret of your PingOne Worker App |

3. Create the following ESV variables:

   | Name                              | Description                                           |
   | --------------------------------- | ----------------------------------------------------- |
   | `esv-hd-pingone-environment-id`   | The environment ID of your mapped PingOne environment |
   | `esv-hd-pingone-worker-client-id` | The client ID of your PingOne Worker App              |

4. Apply the ESV updates.

##### Result

The ESVs are created and available for use in your PingOne Worker Service configuration.

#### Step 1b: Configuring the PingOne Worker Service

The journeys reference a PingOne Worker Service named `HelpDesk PingOne Worker`. You must create this service before importing the journeys.

##### Steps

1. In the PingOne Advanced Identity Cloud admin console, go to **Native Consoles > Access Management**.

2. In the AM admin UI, go to **Services > PingOne Worker Service**.

3. Create a new PingOne Worker Service secondary configuration using the following hints, replacing the URL values with those for your PingOne region:

   | Field                          | Value                                                                  |
   | ------------------------------ | ---------------------------------------------------------------------- |
   | Name                           | `HelpDesk PingOne Worker`                                              |
   | Environment ID                 | `esv-hd-pingone-environment-id` (the ESV you created)                  |
   | Client ID                      | `esv-hd-pingone-worker-client-id` (the ESV you created)                |
   | Client Secret Label Identifier | `pingoneworkhelpdesk`                                                  |
   | PingOne API Server             | For example, `https://api.pingone.eu/v1` (use the URL for your region) |
   | PingOne Auth Server            | For example, `https://auth.pingone.eu` (use the URL for your region)   |

4. In the AM admin UI, go to **Secret Stores > ESV > Mappings** and map `am.services.pingone.worker.pingoneworkhelpdesk.clientsecret` to `esv-hd-pingone-worker-client-secret` (the ESV you created).

5. Go back to the PingOne Worker Service configuration and use **Save and Test Connection** to verify the connection to PingOne.

##### Result

The PingOne Worker Service is configured in your PingOne Advanced Identity Cloud tenant and available for the journey nodes to use.

#### Step 1c: Importing email templates

The journeys send backchannel links to end users by email. Three email templates are required.

##### Steps

1. Download the [Verified Trust for Workforce — Helpdesk Solution](https://marketplace.pingone.com/item/verified-trust-for-workforce-helpdesk-solution) package from the Ping Identity Marketplace. The package includes a `Prerequisites` folder with the email templates and custom nodes.

2. In the PingOne Advanced Identity Cloud admin console, go to **Email Templates**.

3. Import or create each of the following templates using the HTML files in the `Prerequisites/Email Templates` folder:

   | Template name                               | File                                                      |
   | ------------------------------------------- | --------------------------------------------------------- |
   | `Help Desk BackChannel Verification Link`   | `Help Desk BackChannel Verification Link Template.html`   |
   | `Help Desk BackChannel Password Reset Link` | `Help Desk BackChannel Password Reset Link Template.html` |
   | `Help Desk BackChannel MFA Reset Link`      | `Help Desk BackChannel MFA Reset Link Template.html`      |

   |   |                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------- |
   |   | The template names must match exactly as shown. The journeys reference these templates by name. |

##### Result

The three email templates are available in your PingOne Advanced Identity Cloud tenant and will be used by the journeys to deliver backchannel links to end users.

#### Step 1d: Importing custom nodes

The journeys use custom nodes that must be imported before the journeys themselves.

##### Steps

1. In the PingOne Advanced Identity Cloud admin console, go to **Journeys > Custom Nodes**.

2. Click **Import** and upload the `Prerequisites/Custom Nodes/Custom Nodes.json` file from the downloaded package.

   ![A screenshot of the Custom Nodes import dialog in the PingOne Advanced Identity Cloud admin console.](_images/aic-hd-custom-node-import.png)

3. Confirm that the following custom nodes are listed after import:

   * User Message to Display

   * Select MFA Method

   * Remove MFA Device

   * Get IDM User Attributes

   * Display Node State Variables

##### Result

The custom nodes are available in your PingOne Advanced Identity Cloud tenant and can be used by the imported journeys.

#### Step 1e: Creating custom user attributes

The journeys use custom attributes on user profiles to track verification state. You must create these attributes before importing the journeys.

##### Steps

1. In the PingOne Advanced Identity Cloud admin console, go to **Identities > Configure > Alpha realm - user > Properties**.

2. Create the following custom attributes:

   | Name                                  | Type   | Purpose                                                                                                                                                                                                                                                                                                                                                                                 |
   | ------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `custom_backChannelVerifyLinkExpired` | String | Tracks whether the backchannel verification link has already been used or has expired.                                                                                                                                                                                                                                                                                                  |
   | `custom_lastVerifyTransactionID`      | String | Stores the last PingOne Verify transaction ID to detect whether a new transaction has started.                                                                                                                                                                                                                                                                                          |
   | `custom_backChannelTransactionId`     | String | Stores the current backchannel transaction ID.                                                                                                                                                                                                                                                                                                                                          |
   | `custom_DOB`                          | String | Stores the user's date of birth. Set the readable title to `DOB (YYYY-MM-DD)` to specify the required format.If it's required for advanced data matching by the PingOne Verify policy, set the field to the end-user date-of-birth. PingOne Advanced Identity Cloud provides the value to PingOne Verify for comparison with the date-of-birth on the end-user identification document. |

##### Result

The custom attributes are created and available on user profiles in the alpha realm.

### Task 2: Importing the journeys

Learn how to import the pre-built PingOne Advanced Identity Cloud journeys into your development environment. The journeys are split across two import files that must be imported in order.

#### Phase 1: Importing backchannel and inner journeys

The first import file contains the supporting backchannel and MFA registration journeys that the main journey depends on.

##### Steps

1. In the PingOne Advanced Identity Cloud admin console, select your development environment and the **alpha** realm.

2. In the sidebar click **Journeys**.

3. Click **Import**, and then select **Import journeys from file**.

4. Upload the `Help_Desk_Import_Phase_1_Dependencies.json` file from the downloaded package.

   ![A screenshot of the Import journeys dialog showing the Phase 1 journeys listed for import.](_images/aic-hd-journey-import-1.png)

5. Confirm that the import dialog lists the following journeys:

   * `Help_Desk-OATH_MFA_Method_Registration_Inner_Journey`

   * `Help_Desk-Push_MFA_Method_Registration_Inner_Journey`

   * `Help_Desk-WebAuthn_MFA_Method_Registration_Inner_Journey`

   * `Help_Desk-Reset_Password_Backchannel_Journey`

   * `Help_Desk-MFA_Device_Reset_Backchannel_Journey`

   * `Help_Desk-User_ID_Verification_Backchannel_Journey`

6. Click **Start Import**.

##### Result

The Phase 1 journeys are imported into your development environment.

#### Phase 2: Importing the main and profile management journeys

The second import file contains the main agent-facing journey, the user profile management journey, and the ID verification link journey.

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | Wait a few minutes before importing the second journeys file in PingOne Advanced Identity Cloud to make sure phase 1 fully completed. |

##### Steps

1. Click **Import**, and then select **Import journeys from file**.

2. Upload the `Help_Desk_Import_Phase_2_Profile_Send_Main.json` file from the downloaded package.

   ![A screenshot of the Import journeys dialog showing the Phase 2 journeys listed for import.](_images/aic-hd-journey-import-2.png)

3. Confirm that the import dialog lists the following journeys:

   * `Help_Desk-Send_ID_Verification_Link_Inner_Journey`

   * `Help_Desk-User_Profile_Management_Inner_Journey`

   * `Help_Desk-Agent_Login_and_End_User_ID_Verification_Main_Journey`

4. Click **Start Import**.

##### Result

All nine journeys are now imported and appear in the **Journeys** list. Find the `Help Desk` scripts included in the journeys under **Scripts > Auth Scripts**.

### Task 3: Configuring post-import journey settings

After importing both phases, you must update the journey settings and configure several nodes that require manual setup.

#### Step 3a: Updating journey settings

Some journeys require specific runtime settings to operate correctly.

##### Steps

1. In the PingOne Advanced Identity Cloud admin console, select your development environment and the **alpha** realm, then go to **Journeys**.

2. Edit the following journeys to use **Run journey for all users regardless of current session** and **No Session**:

   * `Help_Desk-Agent_Login_and_End_User_ID_Verification_Main_Journey`

   * `Help_Desk-User_ID_Verification_Backchannel_Journey`

3. Edit the following journeys to **Run journey for all users regardless of current session** only:

   * `Help_Desk-MFA_Device_Reset_Backchannel_Journey`

   * `Help_Desk-Reset_Password_Backchannel_Journey`

##### Result

The journey settings are configured correctly.

#### Step 3b: Configuring the Send ID Verification Link journey

The `Help_Desk-Send_ID_Verification_Link_Inner_Journey` requires you to configure the backchannel node, select scripts for two Verify nodes, and assign the PingOne Worker Service.

##### Steps

1. Open the `Help_Desk-Send_ID_Verification_Link_Inner_Journey` journey.

2. Click the Backchannel Initialize node and set the following:

   | Field              | Value                                                      |
   | ------------------ | ---------------------------------------------------------- |
   | Journey            | `Help_Desk-User_ID_Verification_Backchannel_Journey`       |
   | Subject Name Key   | `backchannelUser`                                          |
   | Data Object Key    | `backchannelData`                                          |
   | Max Time (Seconds) | `600` (or longer if needed to allow time for verification) |
   | Allow Retry        | Not enabled                                                |

3. Click the Read Previous Verification Transaction node, enable **Use a script to process Verify transactions**, and select the script `Help Desk - Read Previous Verification`.

4. Click the Get Transaction Data and Verified Data node, enable **Use a script to process Verify transactions**, and select the script `Help Desk - Get Transaction Data and Verified Data`.

5. On the following nodes, set the **PingOne Worker Service** to `HelpDesk PingOne Worker`:

   * PingOne Verify Completion Decision

   * PingOne Create User

   * PingOne Identity Match

6. Click **Save** on the journey.

##### Result

The Send ID Verification Link journey is configured to trigger the user-facing backchannel journey and use the correct PingOne Verify scripts and worker service.

#### Step 3c: Configuring the User Profile Management journey

The `Help_Desk-User_Profile_Management_Inner_Journey` contains two Backchannel Initialize nodes that connect to the password reset and MFA reset backchannel journeys.

##### Steps

1. Open the `Help_Desk-User_Profile_Management_Inner_Journey` journey.

2. Click the Backchannel Initialize node connected to the **Reset Password** path and set the following:

   | Field              | Value                                          |
   | ------------------ | ---------------------------------------------- |
   | Journey            | `Help_Desk-Reset_Password_Backchannel_Journey` |
   | Subject Name Key   | `backchannelUser`                              |
   | Data Object Key    | `backchannelData`                              |
   | Max Time (Seconds) | `600` (or as required for your users)          |

3. Click the Backchannel Initialize node connected to the **Reset MFA Device** path and set the following:

   | Field              | Value                                            |
   | ------------------ | ------------------------------------------------ |
   | Journey            | `Help_Desk-MFA_Device_Reset_Backchannel_Journey` |
   | Subject Name Key   | `backchannelUser`                                |
   | Data Object Key    | `backchannelData`                                |
   | Max Time (Seconds) | `600` (or as required for your users)            |

4. Click **Save** on the journey.

##### Result

The User Profile Management journey is configured to trigger the correct backchannel journeys for password reset and MFA device reset.

#### Step 3d: Configuring the User ID Verification Backchannel journey

The `Help_Desk-User_ID_Verification_Backchannel_Journey` contains the PingOne Verify evaluation configuration and requires you to specify the Verify Policy ID and PingOne Worker Service.

##### Steps

1. In the PingOne admin console, [open the PingOne Verify policy for editing](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_managing_a_verify_policy.html) and copy the policy ID at the top of the configuration panel.

2. In the PingOne Advanced Identity Cloud admin console, open the `Help_Desk-User_ID_Verification_Backchannel_Journey` journey.

3. Click the Verify Evaluation node.

4. In the node's configuration script (the Provider node script), set the following values:

   | Field            | Value                                                              |
   | ---------------- | ------------------------------------------------------------------ |
   | `pingOneWorker`  | `HelpDesk PingOne Worker` (the name of the PingOne Worker Service) |
   | `verifyPolicyId` | The ID of your PingOne Verify policy from your PingOne environment |

5. On the following nodes, set the **PingOne Worker Service** to `HelpDesk PingOne Worker`:

   * PingOne Create User

   * PingOne Identity Match

6. Click **Save** on the journey.

##### Result

The backchannel verification journey is configured to use your PingOne Verify policy and worker service.

### Task 4: Extending the journey timeout (optional)

By default, PingOne Advanced Identity Cloud journeys time out after 5 minutes. For end users who need more time to complete identity verification, you can extend this timeout.

#### Steps

1. In the PingOne Advanced Identity Cloud admin console, go to **Native Consoles > Access Management**.

2. In the AM admin UI, go to **Authentication > Settings > Trees**.

3. Set **Max duration (minutes)** to `15`.

4. Click **Save Changes**.

#### Result

Journeys now allow up to the configured duration before timing out.

### Task 5: Configuring help desk agent access

Learn how to authorize help desk agents to perform account resets.

The `Help_Desk-Agent_Login_and_End_User_ID_Verification_Main_Journey` uses a Set Admin Group node to check that the authenticated agent belongs to the `HelpDesk` group (specifically, that `adminGroup: HelpDesk` is present in the node state). You must create this group and add your help desk agents to it.

#### Steps

1. In the PingOne Advanced Identity Cloud admin console, select your development environment and the **alpha** realm.

2. In the sidebar, go to **Identities > Groups**, then create a new group named `HelpDesk`.

3. In the sidebar, go to **Identities > Manage**, then select **Alpha realm - Users**.

4. Click a help desk agent's user account to open their profile, then add them to the `HelpDesk` group.

5. Repeat for each help desk agent who should be authorized to perform account resets.

#### Result

Help desk agents in the `HelpDesk` group can sign on to the main journey and proceed to the end-user lookup and verification steps.

### Task 6: Create an end-user account

Prepare an end-user account to validate your work.

#### Steps

1. In the PingOne Advanced Identity Cloud admin console, select your development environment and the **alpha** realm.

2. In the sidebar, go to **Identities > Manage**, then select **Alpha realm - Users**.

3. Create an end user account based on these hints:

   | Field           | Value                                                                                                                                 |
   | --------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
   | `First Name`    | The given and middle names on your identification document                                                                            |
   | `Last Name`     | The surname on your identification document                                                                                           |
   | `Email Address` | A valid email address where PingOne Advanced Identity Cloud can send you messages with links for the validation process               |
   | `Address`       | (Optional) If required for advanced data matching in the PingOne Verify policy, include the address on your identification document   |
   | `DOB`           | (Optional) If required for advanced data matching in the PingOne Verify policy, include the birthdate on your identification document |

#### Result

The end-user account is ready for the verification steps.

|   |                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You've now completed the configuration for the Verified Trust for Workforce Help Desk Solution on PingOne Advanced Identity Cloud. Learn how to test the solution in the [Validation](#vt_helpdesk_aic_validation) section. |

## Validation

Now that you've imported the journeys, configured the PingOne Worker Service, specified a PingOne Verify policy, and prepared a help desk agent and end-user account, you're ready to test the solution.

### Before you begin

Ensure you have the following:

* The username and password of a help desk agent whose account belongs to the `HelpDesk` group.

* The username of an end user in the alpha realm whose account has a valid email address you can access.

* A mobile device that can access the test end user's email and has a working camera.

* A valid government-issued ID that you can use for testing purposes. Learn more in [PingOne Verify types of verification](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_types_of_verification.html).

### Steps

1. Open the agent journey in an incognito browser window by navigating to the following URL, replacing `<tenant-fqdn>` with your PingOne Advanced Identity Cloud tenant domain:

   ```text
   https://<tenant-fqdn>/am/XUI/?realm=alpha&authIndexType=service&authIndexValue=Help_Desk-Agent_Login_and_End_User_ID_Verification_Main_Journey
   ```

2. Sign on as the help desk agent:

   1. Enter the help desk agent's username and click **Next**.

   2. Enter the help desk agent's password and click **Sign On**.

3. Look up the end user:

   1. When prompted, search for the end user by username or email address, then select the user's account.

      The journey verifies that the agent belongs to the `HelpDesk` group and retrieves the end user's profile.

4. Send the verification request:

   The journey sends a verification link to the end user's email address and displays a status-monitoring screen while waiting for the end user to respond.

5. Verify the end user's identity:

   1. As the end user, open a separate incognito browser window and access the verification link from the email.

   2. As the help desk agent, get the code shown on the end-user mobile device and enter it in your browser to get updates about the end user's progress.

   3. As the end user, click **Begin Verification** and follow the on-screen prompts to scan your government-issued ID and take a selfie.

      After completing verification, the screen confirms that identity verification was successful.

      ![A screenshot confirming that identity verification was successful.](_images/aic-hd-verification-success.png)

6. As the help desk agent, update the status in the agent window. When verification succeeds, choose to either reset the end user's password or reset their MFA devices:

   ![A screenshot of the agent's screen showing the option to reset the end user's password or MFA devices after successful verification.](_images/aic-hd-post-verification-choice.png)

7. Complete the account recovery:

   PingOne Advanced Identity Cloud sends the end user another email with a link to complete the reset. As the end user, open the link and follow the prompts. For a password reset, enter and confirm a new password:

   ![A screenshot of the Reset Password screen.](_images/aic-hd-reset-password.png)

   On success, the end user is signed on and the end-user profile page is displayed, confirming that account access has been restored.

## Troubleshooting

This section provides troubleshooting tips for common issues with the Verified Trust for Workforce Help Desk Solution on PingOne Advanced Identity Cloud.

* The help desk agent can't sign on

  When you enter the help desk agent's credentials, the journey returns an error or failure page. Confirm the following:

  * The agent's user account exists in the alpha realm of your PingOne Advanced Identity Cloud development environment.

  * The journey is enabled. In the PingOne Advanced Identity Cloud admin console, go to **Journeys** and confirm that **Help\_Desk-Agent\_Login\_and\_End\_User\_ID\_Verification\_Main\_Journey** is toggled on.

* The help desk agent is not authorized

  After signing on, the journey exits with a failure rather than proceeding to the end-user lookup step. Confirm that the agent's user account belongs to the `HelpDesk` group as described in [Task 5](#task_5_configure_agent_access).

* The end user lookup fails

  The journey exits with a failure after you search for the end user. Confirm that:

  * The end user account exists in the alpha realm.

  * The end user account has a valid email address (required for backchannel link delivery).

* The PingOne Worker Service connection fails

  A node in the verification or backchannel journeys fails with a connection or authentication error. Confirm the following:

  * The `HelpDesk PingOne Worker` service in your PingOne Advanced Identity Cloud development environment is correctly configured with valid ESV values for the client ID, client secret, and environment ID from your mapped PingOne environment. Learn more in [Set up PingOne workers and configure them as PingOne Advanced Identity Cloud services](https://docs.pingidentity.com/pingoneaic/integrations/pingone-set-up-oidc-clients.html).

  * All nodes that reference `HelpDesk PingOne Worker` in the `Help_Desk-Send_ID_Verification_Link_Inner_Journey` and `Help_Desk-User_ID_Verification_Backchannel_Journey` are configured with the correct service name.

* The verification link has expired or the backchannel timed out

  The backchannel journey's **Max Time (Seconds)** has elapsed before the end user completed verification. The agent's status screen reflects the failure. The agent can restart the main journey to send a new verification request. Consider increasing the **Max Time** value in the Backchannel Initialize node and extending the journey timeout as described in [Task 4](#task_4_configure_worker_service).

* The PingOne Verify evaluation timed out

  The end user didn't complete the ID and liveness steps within the PingOne Verify evaluation window. The agent can restart the main journey to initiate a new verification session.

## What's next

As you integrate and promote this solution to higher environments, consider the following:

* Customizing the `HelpDesk` group name and the Set Admin Group node's group check to align with your organization's group naming conventions.

* Adding extension points to the journey to integrate with external ticketing systems. For example, creating a Jira ticket or ServiceNow incident when an end user fails identity verification.

* Configuring a custom PingOne Verify policy appropriate for your organization before deploying to production. The default policy is sufficient for testing but might not meet your production requirements.

## Explore further

### Concepts

Learn more about the concepts used in the Verified Trust for Workforce Help Desk Solution in the following table:

| Concept                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [PingOne Advanced Identity Cloud journeys](https://docs.pingidentity.com/pingoneaic/journeys/journeys.html)                 | A journey is a visual, node-based workflow that defines how users or agents authenticate, verify their identity, or perform account management tasks. In this solution, a main agent-facing journey coordinates identity verification and account recovery through a set of inner and backchannel journeys.                                                                                                             |
| [Backchannel authentication](https://docs.pingidentity.com/pingoneaic/am-authentication/backchannel-authentication.html)    | Backchannel authentication lets a journey start a separate, asynchronous journey for a different subject — in this case, the end user — while the originating journey monitors the outcome. The main journey uses Backchannel Initialize nodes to trigger user-facing journeys and polls for their results using Backchannel Status nodes.                                                                              |
| [PingOne Worker Service](https://docs.pingidentity.com/pingoneaic/integrations/pingone-set-up-oidc-clients.html)            | The PingOne Worker Service is a service configuration in PingOne Advanced Identity Cloud that gives journey nodes the credentials they need to call PingOne APIs. It acts as the bridge between PingOne Advanced Identity Cloud journey nodes (such as PingOne Verify Evaluation) and your connected PingOne environment. Each node that communicates with PingOne must reference a configured worker service instance. |
| [ESVs](https://docs.pingidentity.com/pingoneaic/tenants/esvs.html)                                                          | ESVs let you store sensitive configuration values, such as API credentials, outside of journey configuration. This solution uses ESVs to store the PingOne Worker App's client ID, client secret, and environment ID, which the PingOne Worker Service reads at runtime.                                                                                                                                                |
| [Backchannel Initialize node](https://docs.pingidentity.com/auth-node-ref/latest/backchannel-initialize.html)               | The Backchannel Initialize node starts an asynchronous journey for a different subject. It takes the end user's ID from shared state, generates a magic link URL to the target journey, and writes the backchannel transaction ID to shared state so the Backchannel Status node can track the outcome.                                                                                                                 |
| [Backchannel Status node](https://docs.pingidentity.com/auth-node-ref/latest/backchannel-status.html)                       | The Backchannel Status node checks the current status of an active backchannel transaction. Together with the Polling Wait node, it repeatedly polls the transaction until the end user completes (or fails) the target journey.                                                                                                                                                                                        |
| [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html) | The PingOne Verify Evaluation node starts or resumes a PingOne Verify evaluation transaction. In this solution, it is configured with a policy ID that defines the verification requirements (government ID, liveness detection, and facial comparison). On success, the journey proceeds to the account recovery step.                                                                                                 |
| [PingOne Identity Match node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-identity-match.html)       | The PingOne Identity Match node checks whether the PingOne Advanced Identity Cloud user has a corresponding user account in PingOne. If no match is found, the journey creates one using the PingOne Create User node. This step is required before PingOne Verify can target the correct user for a verification transaction.                                                                                          |
| [PingOne Verify](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_start.html)     | The PingOne Verify service lets you enable secure user verification based on a government-issued document and a live face capture (a selfie). In this solution, PingOne Verify is triggered within the ID verification backchannel journey after the help desk agent initiates the request.                                                                                                                             |