---
title: Connect AM to PingOne
description: Set up the shared PingOne configuration that PingAM uses for PingOne Protect and PingOne Verify.
component: pingam
version: 8.1
page_id: pingam:integrations:connect-am-to-pingone
canonical_url: https://docs.pingidentity.com/pingam/8.1/integrations/connect-am-to-pingone.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  create-worker-application: Create a worker application in PingOne
  create-worker-service: Create a PingOne Worker service in AM
---

# Connect AM to PingOne

Connect your AM deployments to PingOne so that you can configure PingOne services such as PingOne Protect and PingOne Verify in your AM authentication journeys.

To connect AM to PingOne, you must:

1. **Set up PingOne environments**

   Set up at least one [PingOne environment](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started_adding_environment.html) using the Customer solution option. Use the same PingOne environment for integrating PingOne Protect and PingOne Verify into AM.

   Reusing environments reduces the number of PingOne environments and OIDC credentials you need to keep track of.

   You can use additional PingOne environments if required. For example, to separate development, test, and production deployments, or to serve users in different regions or countries.

2. **Create PingOne worker applications**

   Create a [worker application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html) in each of your PingOne environments. These provide access to the PingOne admin APIs using OIDC.

   Learn more in [Create a worker application in PingOne](#create-worker-application).

3. **Create secrets for the OIDC credentials**

   Store your worker application client secret in an AM secret store that's accessible to the realm where you'll create your PingOne Worker service configuration.

   Learn more in [Secret stores](../security/secret-stores.html).

4. **Create PingOne worker services**

   For each worker application, create a PingOne worker service configuration in the realm where you'll configure your PingOne journeys.

   Learn more in [Create a PingOne Worker service in AM](#create-worker-service).

5. **Map secrets for the PingOne worker services**

   Map the secret you created to the `am.services.pingone.worker.identifier.clientsecret` secret label.

   Where identifier is the value you entered in the Client Secret Label Identifier field when you created the PingOne Worker service configuration.

   Learn more in [Map and rotate secrets](../security/secret-mapping.html).

6. **Test the PingOne worker service configuration**

   Before you configure any journeys, verify that AM can use the worker service configuration to connect to PingOne.

   Learn more in [Test the connection](../setup/services-configuration.html#test-connection).

|   |                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Complete this setup for each PingOne environment that AM uses. After that, reuse the same AM worker service configuration across the PingOne Protect and PingOne Verify journeys that target that environment. |

## Create a worker application in PingOne

Create a [worker application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html) in PingOne for AM to use when calling PingOne APIs.

1. In the PingOne admin console, open the target environment and click Manage Environment.

2. Go to Applications > Applications, then click the [icon: plus, set=fas]icon.

3. Add an application of type `Worker` and save your changes.

4. Click Grant Roles.

5. Select the `Identity Data Admin` role, choose your target environment, and save your changes.

6. Go to the Overview tab and enable the worker application using the toggle switch in the top-right corner.

   The worker application should now resemble the following:

   ![AM Worker application](_images/am-worker-app.png)

7. Make a note of the following values:

   Environment ID\
   Client ID\
   Client Secret

   You'll need them when you create the PingOne Worker service in AM.

## Create a PingOne Worker service in AM

Create a [PingOne Worker service](../setup/services-configuration.html#realm-pingone-worker-service) configuration for your worker application.

1. In the AM admin UI, go to Realms > *realm name* > Services and click Add a Service.

2. Select `PingOne Worker Service` and click Create.

3. On the Secondary Configurations tab, click Add a Secondary Configuration.

4. Enter a name for the configuration, for example, `AM Worker` and click Create.

5. Enter the client ID and environment ID you copied earlier in the Client ID and Environment ID fields.

6. Enter an identifier in the Client Secret Label Identifier field. This identifier is used to create a secret label for the client secret.

   The secret label uses the template `am.services.pingone.worker.identifier.clientsecret` where identifier is the Client Secret Label Identifier value.

   This field can only contain characters `a-z`, `A-Z`, `0-9`, and `.` and can't start or end with a period.

7. Ensure that the PingOne API Server URL and PingOne Authorization Server URL are correct for the region where your PingOne environment is located:

   | Region                           | API URL                       | Authorization URL           |
   | -------------------------------- | ----------------------------- | --------------------------- |
   | North America (excluding Canada) | `https://api.pingone.com/v1`  | `https://auth.pingone.com`  |
   | Canada                           | `https://api.pingone.ca/v1`   | `https://auth.pingone.ca`   |
   | Europe                           | `https://api.pingone.eu/v1`   | `https://auth.pingone.eu`   |
   | Asia-Pacific                     | `https://api.pingone.asia/v1` | `https://auth.pingone.asia` |

---

---
title: Integrate PingOne Protect
description: Integrate PingAM with PingOne Protect to add risk-based authentication and fraud detection to authentication journeys using real-time behavioral and contextual risk signals.
component: pingam
version: 8.1
page_id: pingam:integrations:pingone-protect
canonical_url: https://docs.pingidentity.com/pingam/8.1/integrations/pingone-protect.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  why_use_pingone_protect: Why use PingOne Protect?
  set_up_a_pingone_protect_journey: Set up a PingOne Protect journey
  optimize-risk-models: Optimize the PingOne Protect risk models
---

# Integrate PingOne Protect

Integrate AM with PingOne Protect to add risk-based authentication and fraud detection to your authentication journeys.

PingOne Protect uses continuous, intelligence-based fraud detection to evaluate real-time risk signals from a user's device, network, and behavior to determine when additional authentication is required.

## Why use PingOne Protect?

* Adaptive security

  Dynamically adjusts authentication requirements based on real-time risk signals such as location, device, and behavioral anomalies. This means low-risk logins are frictionless, while high-risk attempts trigger additional challenges, such as multi-factor authentication (MFA).

* Reduced fraud

  Proactively identifies and mitigates fraudulent activities, such as account takeover (ATO), credential stuffing, and bot attacks, by analyzing a wide range of contextual factors during authentication.

* Improved user experience

  Reduces friction for legitimate users by prompting for additional authentication only when necessary.

* Granular control

  Provides detailed risk scores and lets you define policies for different risk levels within journeys.

## Set up a PingOne Protect journey

|   |                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   | Make sure you've completed the steps in [Connect AM to PingOne](connect-am-to-pingone.html) before configuring a PingOne Protect journey. |

AM provides the following nodes to integrate PingOne Protect into your authentication journeys:

* PingOne Protect Initialize node

  The [PingOne Protect Initialize node](https://docs.pingidentity.com/auth-node-ref/8.1/pingone/pingone-protect-initialize.html) instructs the client to initialize a PingOne Signals (Protect) SDK so that it can start gathering device signals and contextual information.

* PingOne Protect Evaluation node

  The [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/8.1/pingone/pingone-protect-evaluation.html) contacts PingOne to calculate the risk level and other risk-related details associated with an event.

  Depending on how you configure your risk policies in PingOne, the response could return:

  * A risk score.

  * A risk level, such as high, medium, or low.

  * Recommended actions to take, such as mitigation against bots.

* PingOne Protect Result node

  The [PingOne Protect Result node](https://docs.pingidentity.com/auth-node-ref/8.1/pingone/pingone-protect-result.html) updates the risk evaluation configuration or modifies the completion status of the resource while the risk evaluation is still in progress.

  You can check the results of the evaluation in the PingOne admin console by filtering for Risk Evaluation Updated event types.

Create a journey using these nodes to integrate PingOne Protect into your authentication flow. For example:

![Example PingOne Protect journey](_images/pingone-protect-example-journey.png)

Learn more in the [PingOne Protect example](https://docs.pingidentity.com/auth-node-ref/8.1/pingone/pingone-protect-initialize.html#example).

## Optimize the PingOne Protect risk models

PingOne Protect is preconfigured with a default machine learning model that assesses risk based on various [predictors](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_predictors.html) such as user behavior, device characteristics, and network context. You can optimize the model by letting it observe real authentication data and then refine the risk policies it applies to that data:

1. **Run with production data**

   Integrate PingOne Protect into your journeys and let it observe real user behavior. Ping Identity recommends running with the default risk policy for:

   * 1 to 3 weeks for workforce use cases

   * 2 to 4 weeks for customer use cases

   During this period, PingOne Protect builds a baseline of normal behavior for your users and environments. This includes learning patterns related to device, location, network, and user-specific habits.

   Make sure you send transaction feedback using PingOne Protect Result nodes to report whether each transaction was a `SUCCESS` or `FAILURE`. This feedback loop is essential for the models to learn to distinguish legitimate activity from fraud.

2. **Monitor and analyze**

   Use the PingOne Protect [threat protection dashboard](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_dashboard.html) to analyze activity after the initial observation period. The dashboard provides insights into risk evaluations, including:

   * Number of abnormal activities

   * High-risk locations and factors

   * Riskiest users

   * Distribution of browser and operating systems

   Focus on identifying false positives. These are legitimate user interactions that PingOne Protect flagged as high or medium risk. Analyze why these were flagged as risky by looking at the specific predictors involved.

3. **Refine risk policies**

   Based on your analysis, fine-tune how predictor output is translated into a final risk score and level using [risk policies](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_policies.html):

   * Adjust the numerical score assigned to individual predictors within your risk policies based on your analysis of false positives and false negatives.

   * For each predictor (for example, `Anonymous Network`, `IP Velocity`, or `User Location Anomaly`), map its calculated risk level (low, medium, high) to a specific score.

   * Define the risk thresholds that map to a low, medium, or high overall risk level.

   For example, if `IP Location Anomaly` frequently causes false positives for users who travel, you might reduce the score assigned to a high risk for that specific predictor, or create a more lenient predictor for specific user groups.

   Optimization is an iterative process. Continue to monitor the threat protection dashboard and adjust risk policies as needed.

---

---
title: Integrate PingOne Verify
description: Integrate PingAM with PingOne Verify to add identity verification and proofing to authentication journeys, preventing fraud during registrations and high-risk transactions.
component: pingam
version: 8.1
page_id: pingam:integrations:pingone-verify
canonical_url: https://docs.pingidentity.com/pingam/8.1/integrations/pingone-verify.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  why_use_pingone_verify: Why use PingOne Verify?
  set_up_a_pingone_verify_journey: Set up a PingOne Verify journey
---

# Integrate PingOne Verify

Integrate AM with PingOne Verify to add identity verification and proofing to your authentication journeys.

PingOne Verify reduces fraud by letting you securely confirm an end user's identity during registration, high-risk transactions, or any scenario where identity proofing is required.

## Why use PingOne Verify?

* Streamlined onboarding

  Accelerates and secures the new user onboarding process by enabling real-time identity verification, such as document scanning and facial biometrics, directly within registration flows.

* Fraud prevention at inception

  Prevents fraudulent accounts from being created by accurately confirming user identities, reducing the long-term risk of synthetic identities or account abuse.

* Compliance and trust

  Helps meet regulatory requirements for "Know Your Customer" (KYC) and anti-money laundering (AML) by providing auditable proof of identity, building greater trust with users.

* Reduced manual effort

  Automates identity verification, which would otherwise require manual review by support staff.

## Set up a PingOne Verify journey

|   |                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   | Make sure you've completed the steps in [Connect AM to PingOne](connect-am-to-pingone.html) before configuring a PingOne Verify journey. |

AM provides the following nodes to integrate PingOne Verify into your authentication journeys:

* PingOne Verify Evaluation node

  The [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/8.1/pingone/pingone-verify-evaluation.html) uses the PingOne Verify service to initiate a new or continue an existing verification transaction. It offers a range of delivery methods, such as a QR code, email, or SMS to start the identity verification process.

* PingOne Verify Completion Decision node

  The [PingOne Verify Completion Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/pingone/pingone-verify-completion-decision.html) determines the completion status of the most recent identity verification transaction for a PingOne user.

  The node checks the previous identity verification transaction for the user and returns an outcome based on the verification status.

  You can use this node to prevent users from repeatedly having to verify their identity by checking their most recent verification transaction. You can also determine if a transaction is already in progress, to prevent multiple ongoing transactions.

Create a journey using these nodes to integrate PingOne Verify into your authentication flow. For example:

![Example PingOne Verify journey](_images/pingone-verify-example-journey.png)

Learn more in the [PingOne Verify example](https://docs.pingidentity.com/auth-node-ref/8.1/pingone/pingone-verify-evaluation.html#example).

---

---
title: PingOne Protect and PingOne Verify
description: Integrate PingAM with PingOne Protect and PingOne Verify to add risk-based authentication and identity verification to your authentication journeys.
component: pingam
version: 8.1
page_id: pingam:integrations:pingone-protect-verify
canonical_url: https://docs.pingidentity.com/pingam/8.1/integrations/pingone-protect-verify.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# PingOne Protect and PingOne Verify

You can enhance the Identity and Access Management (IAM) capabilities of AM by connecting AM to PingOne. After creating the connection, you can use the following cloud-native identity services to provide a more secure and seamless user experience:

[icon: shield-check, set=far, size=3x]

#### [PingOne Protect](pingone-protect.html)

Risk-based authentication and fraud detection. Integrate into AM journeys using the PingOne Protect authentication nodes.

[icon: id-card, set=far, size=3x]

#### [PingOne Verify](pingone-verify.html)

Identity verification and proofing. Integrate into AM journeys using the PingOne Verify authentication nodes.