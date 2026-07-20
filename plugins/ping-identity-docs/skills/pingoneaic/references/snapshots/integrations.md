---
title: Integrate PingOne services for enhanced IAM capabilities
description: Enhance your Advanced Identity Cloud capabilities by integrating with PingOne Protect, PingOne Verify, and PingOne Credentials
component: pingoneaic
page_id: pingoneaic:integrations:pingone
canonical_url: https://docs.pingidentity.com/pingoneaic/integrations/pingone.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Integrate PingOne services for enhanced IAM capabilities

You can enhance the IAM capabilities of Advanced Identity Cloud by integrating with PingOne services. This allows you to leverage the following cloud-native identity services to provide a more secure and seamless user experience:

[icon: shield-check, set=far, size=3x]

#### [PingOne Protect](pingone-protect.html)

Risk-based authentication and fraud detection. Integrate into Advanced Identity Cloud journeys using the PingOne Protect authentication nodes.

[icon: id-card, set=far, size=3x]

#### [PingOne Verify](pingone-verify.html)

Identity verification and proofing. Integrate into Advanced Identity Cloud journeys using the PingOne Verify authentication nodes.

[icon: wallet, set=far, size=3x]

#### [PingOne Credentials](pingone-credentials.html)

Issue and manage digital verifiable credentials. Integrate into Advanced Identity Cloud journeys using the PingOne Credentials authentication nodes.

---

---
title: PingOne Protect use cases
description: Learn key use cases for integrating PingOne Protect including fraud prevention, MFA effectiveness, zero trust initiatives, and passwordless authentication
component: pingoneaic
page_id: pingoneaic:integrations:pingone-protect-use-cases
canonical_url: https://docs.pingidentity.com/pingoneaic/integrations/pingone-protect-use-cases.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# PingOne Protect use cases

Integrate PingOne Protect with Advanced Identity Cloud to significantly enhance your organization's security posture and user experience by leveraging advanced risk-based authentication and fraud detection capabilities. Here are the key use cases:

* **Prevent account takeover (ATO) and new account fraud**:

  * **Real-time risk assessment**: PingOne Protect continuously evaluates various signals (for example, location, device, behavior, IP reputation) in real-time during sign-on, registration, and transaction flows. This allows it to identify suspicious activities indicative of ATO attempts (for example, credential stuffing, brute force attacks, impossible travel) or fraudulent new account creation.

  * **Adaptive authentication**: Based on the calculated risk score, Advanced Identity Cloud can dynamically adjust the authentication requirements. For low-risk users, access can be frictionless (for example, passwordless). For medium-risk scenarios, it might trigger step-up authentication (for example, MFA challenge like a push notification or a CAPTCHA). For high-risk attempts, access can be denied or flagged for further investigation.

  * **Bot detection and mitigation**: PingOne Protect can identify and block automated bot attacks aimed at compromising accounts or creating fake ones, thus protecting your digital assets.

* **Enhance multi-factor authentication (MFA) effectiveness and reduce friction (MFA fatigue)**:

  * **Context-aware MFA**: Instead of enforcing MFA for every sign-on, PingOne Protect informs Advanced Identity Cloud when MFA is truly needed based on risk. This reduces "MFA fatigue" for legitimate users, improving their experience, while still applying strong authentication when it matters most.

  * **Optimized user journeys**: By intelligently assessing risk, the integration ensures that users only face friction (like an MFA prompt) when their activity deviates from their typical behavior or presents a higher risk, leading to smoother and more convenient digital experiences.

* **Strengthen zero trust initiatives**:

  * **Continuous risk evaluation**: PingOne Protect provides continuous risk signals throughout the user's session, enabling Advanced Identity Cloud to enforce granular, real-time access policies based on the principle of "never trust, always verify."

  * **Dynamic authorization**: Access decisions in Advanced Identity Cloud can be made more intelligent and dynamic by incorporating the real-time risk scores from PingOne Protect. This means authorization can adapt based on the ongoing risk level of an end user's session.

* **Gain deeper visibility into risk and fraud trends**:

  * **Comprehensive dashboards and reporting**: The integration provides rich data and insights into risk events, high-risk locations, risky user behavior, and attack trends. This visibility helps security teams understand their fraud posture, identify vulnerabilities, and proactively address emerging threats.

  * **Forensic analysis**: Detailed audit logs and risk data allow for in-depth investigation of suspicious activities, helping security teams understand the "who, what, when, and where" of potential breaches.

* **Support passwordless authentication journeys**:

  * **Risk-based passwordless**: By continuously evaluating risk in the background, PingOne Protect enables Advanced Identity Cloud to facilitate truly passwordless experiences. Second-factor authentication methods (like biometrics or magic links) are only triggered when necessary, based on the risk assessment, making passwordless even more secure and user-friendly.

* **Integrating with existing fraud detection investments**:

  * **Ingest third-party signals**: PingOne Protect allows organizations to incorporate custom or third-party risk signals into its evaluation, enriching the overall risk assessment and leveraging existing security investments. In essence, the integration of PingOne Protect into Advanced Identity Cloud transforms static identity and access management into a dynamic, intelligent, and risk-aware system that prioritizes both security and user experience.

---

---
title: Set up mapped PingOne environments
description: Set up mapped PingOne environments for each Advanced Identity Cloud tenant environment to enable PingOne product integration
component: pingoneaic
page_id: pingoneaic:integrations:pingone-set-up-environments
canonical_url: https://docs.pingidentity.com/pingoneaic/integrations/pingone-set-up-environments.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  create-mapped-pingone-environments: Create mapped PingOne environments
  naming-convention-for-mapped-pingone-environments: Naming convention for mapped PingOne environments
---

# Set up mapped PingOne environments

To integrate with PingOne, you need to set up a [PingOne environment](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started_adding_environment.html) for each of your Advanced Identity Cloud tenant environments. To help you keep track of your PingOne environments, use the following rules:

* **Naming convention**: Use this [naming convention](#naming-convention-for-mapped-pingone-environments) when you create PingOne environments. Because the naming convention is based on your tenant environment FQDNs, each name acts as an informal mapping and makes it easy to identify which PingOne environment corresponds to which Advanced Identity Cloud tenant environment.

* **Reuse environments**: Use these same mapped PingOne environments for all PingOne products you integrate into Advanced Identity Cloud. Reusing environments reduces the number of PingOne environments and OIDC credentials you need to keep track of.

You also need to add the outbound static IP addresses of each of your Advanced Identity Cloud tenant environments to the server-sourced traffic exclusion list in the mapped PingOne environment. This prevents rate limits being applied to calls from Advanced Identity Cloud to PingOne services.

## Create mapped PingOne environments

For each of your Advanced Identity Cloud tenant environments:

1. In the Advanced Identity Cloud admin console:

   1. Find the tenant environment's FQDN using the instructions in [Confirm the FQDN in tenant settings](../tenants/environments.html#confirm-the-tenant-environment-fqdn-in-tenant-settings). An example FQDN is `openam-mycompany-ew2-dev.id.forgerock.io`.

   2. Find the tenant environment's outbound static IP addresses:

      1. Open the TENANT menu (upper right), then click Tenant Settings > Global Settings > IP Addresses.

      2. Make a note of the one or more listed IP addresses.

      |   |                                                                                                                                                                                                                                                                                                                     |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you don't have this menu option, your tenant environment may not have outbound static IP addresses enabled. Learn more in [How do I enable outbound static IP addresses for my tenants?](../tenants/environments-outbound-static-ip-addresses.html#how-do-i-enable-outbound-static-ip-addresses-for-my-tenants). |

2. In the PingOne admin console:

   1. In the sidebar, click the Ping Identity logo to open the Environments page.

   2. Check if you already have a mapped PingOne environment (a PingOne environment with a name that corresponds to the FQDN of your Advanced Identity Cloud tenant environment). An example environment name is `env-pingoneaic-mycompany-ew2-dev`.

      * If a mapped environment exists, you can use that environment. You don't need to create new environments for each PingOne product you integrate into Advanced Identity Cloud.

      * If no mapped environment exists, [create one](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started_adding_environment.html) using the [naming convention](#naming-convention-for-mapped-pingone-environments).

   3. Return to the Environments page, click the mapped PingOne environment, then click Manage Environment > Settings > Rate Limits.

   4. In the Server-Sourced Traffic section, under the Allowed IP addresses or CIDR ranges label, enter the outbound static IP addresses you noted from the Advanced Identity Cloud admin console. Enter each IP address in a separate field, and click the [icon: add, set=material, size=inline] Add button to add more fields as needed.

   5. Click Save.

## Naming convention for mapped PingOne environments

The naming convention of the PingOne environments should follow the [FQDN naming convention](../tenants/environments.html#tenant-environment-fqdn-format) of your Advanced Identity Cloud tenant environments.

The following table shows an example of how to name PingOne environments based on the example FQDNs in [Tenant environment FQDNs](../tenants/environments.html#tenant-environment-fqdns).

|             | Tenant environment FQDN                                  | Mapped PingOne environment name                   |
| ----------- | -------------------------------------------------------- | ------------------------------------------------- |
| Sandbox     | openam-**mycompanysandbox1**-**ew2**.forgeblocks.com     | env-pingoneaic-**mycompany**-**ew2**-**sandbox1** |
| Sandbox 2   | openam-**mycompanysandbox2**-**ew2**.forgeblocks.com     | env-pingoneaic-**mycompany**-**ew2**-**sandbox2** |
| Development | openam-**mycompany**-**ew2**-**dev**.id.forgerock.io     | env-pingoneaic-**mycompany**-**ew2**-**dev**      |
| UAT         | openam-**mycompany**-**ew2**-**uat**.id.forgerock.io     | env-pingoneaic-**mycompany**-**ew2**-**uat**      |
| UAT 2       | openam-**mycompany**-**ew2**-**uat2**.id.forgerock.io    | env-pingoneaic-**mycompany**-**ew2**-**uat2**     |
| Staging     | openam-**mycompany**-**ew2**-**staging**.id.forgerock.io | env-pingoneaic-**mycompany**-**ew2**-**staging**  |
| Production  | openam-**mycompany**-**ew2**.id.forgerock.io             | env-pingoneaic-**mycompany**-**ew2**-**prod**     |

---

---
title: Set up PingOne product connections
description: Set up PingOne product connections to quickly integrate PingOne services with Advanced Identity Cloud authentication journeys
component: pingoneaic
page_id: pingoneaic:integrations:pingone-set-up-product-connections
canonical_url: https://docs.pingidentity.com/pingoneaic/integrations/pingone-set-up-product-connections.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["integrations:pingone-set-up-workers.adoc", "integrations:pingone-set-oidc-clients.adoc"]
section_ids:
  prerequisites: Prerequisites
  create-a-product-connection-in-your-development-tenant-environment: "Task 1: Create a product connection for your development tenant environment"
  create-a-pingone-integration-in-your-development-tenant-environment: "Task 2: Create a PingOne integration in your development tenant environment"
  promote-the-integration-to-your-other-tenant-environments: "Task 3: Promote the integration to your other tenant environments"
---

# Set up PingOne product connections

Integrate your Advanced Identity Cloud tenant environments with PingOne [product connections](https://docs.pingidentity.com/pingone/integrations/p1_creating_product_connection.html) so that you can configure PingOne services (such as PingOne Protect and PingOne Verify) in your Advanced Identity Cloud authentication journeys.

PingOne product connections are preconfigured OIDC integrations designed for quick setup. They streamline the connection process by automatically providing the necessary client credentials and PingOne environment ID within a signed JWT for easier consumption by Advanced Identity Cloud. Advanced Identity Cloud can consume the JWT credential and automatically configure a worker service that's ready to use in your authentication journeys.

|   |                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you're looking for the previous instructions for setting up PingOne integrations, refer to [Set up PingOne OIDC clients and configure Advanced Identity Cloud services](_attachments/Set_up_PingOne_OIDC_clients_and_configure_Advanced_Identity_Cloud_services.pdf) (PDF). |

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You only need to set up a product connection once for each of your Advanced Identity Cloud tenant environments and their mapped PingOne environments. |

## Prerequisites

Before you set up PingOne product connections, make sure you've [mapped PingOne environments](pingone-set-up-environments.html) for each of your Advanced Identity Cloud tenant environments.

## Task 1: Create a product connection for your development tenant environment

Create a product connection for your development tenant environment. Product connections give access to the PingOne admin APIs using OIDC and provide a single JWT credential containing connection information.

In the PingOne admin console:

1. In the sidebar, click the Ping Identity logo to open the Environments page.

2. Select the environment that's mapped to your development tenant environment from the list, then click Manage Environment.

3. Go to Integrations > Products, then click the add icon ([icon: circle-plus, set=fas, size=lg]).

4. In the Add Connection modal:

   1. In the Target Product field, select Advanced Identity Cloud.

   2. In the Name field, enter a unique name for the connection. For example, `PingOne Connection AIC`.

   3. (Optional) Enter a Description for the connection.

   4. Click Save.

5. In the New Credential Created modal:

   1. Click the copy icon ([icon: copy, set=material, size=inline]) to copy the new JWT credential to your clipboard. Make a note of the JWT credential, as you won't be able to access it again after closing the modal.

   2. Click Close.

## Task 2: Create a PingOne integration in your development tenant environment

Create a PingOne Integration in your Advanced Identity Cloud development tenant environment using the JWT credential from its mapped PingOne environment.

In your development tenant environment:

1. In the Advanced Identity Cloud admin console, go to PingOne Integrations.

2. Click [icon: add, set=material, size=inline] Add PingOne Integration.

3. In the Add a PingOne Integration modal:

   1. Paste the JWT credential from the development tenant environment's mapped PingOne environment.

   2. Review the Decoded Claims. In particular, check that the `environmentName` corresponds to the name of the correct PingOne environment.

   3. Click Next.

   4. In the Name field, accept the default value (derived from the `environmentName` claim) or enter a name of your choice (for example, `PingOne-Integration-AIC`). Only alphanumeric characters and hyphens are allowed.

   5. Click Connect.

   6. Wait for Advanced Identity Cloud to perform these steps:

      * Create an ESV for the JWT credential with the value of the JWT you entered.

      * Create a [PingOne Worker Service](../am-reference/services-configuration.html#realm-pingone-worker-service) in the current realm of your development tenant environment.

      * Map the ESV to the secret label identifier of the worker service.

      * Perform a connection test to the PingOne environment to verify that the integration is working correctly.

   7. In the PingOne Integrations page, confirm that the new integration is listed with a status of `Active`.

## Task 3: Promote the integration to your other tenant environments

Once you have successfully created the integration in your development tenant environment, you can promote the worker service configuration to your other tenant environments (UAT\[[1](#_footnotedef_1 "View footnote.")], staging, production).

1. Determine the promotion order of your tenant environments. This will depend on whether you have a [standard promotion group of environments](../tenants/self-service-promotions.html#standard-promotion-group-of-environments) or whether you also have [additional UAT environments](../tenants/self-service-promotions.html#additional-uat-environments).

2. In promotion order, for each upper tenant environment in your promotion group, perform the following steps:

   1. Create a product connection in the mapped PingOne environment for the upper tenant environment. To do this, repeat the steps in task 1, but substitute your upper tenant environment details wherever the development tenant environment is mentioned.

   2. Create the necessary ESV in the upper tenant environment. To do this, repeat task 2, steps 1 — 3e, but substitute your upper tenant environment details wherever the development tenant environment is mentioned.

      |   |                                                                                                                                                               |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | As the upper tenant environments are immutable, this step doesn't create the worker configuration. This is created when you run a promotion in the next step. |

   3. Run a promotion to move the worker configuration to the upper tenant environment from its respective lower tenant environment. Learn more in:

      * [Manage self-service promotions using the admin console](../tenants/self-service-promotions-ui.html)

      * [Manage self-service promotions using the API](../tenants/self-service-promotions-api.html)

   4. In the PingOne Integrations page in the upper tenant environment, confirm that the new integration is listed with a status of `Active`.

3. (Optional) If you have sandbox\[[2](#_footnotedef_2 "View footnote.")] tenant environments, repeat tasks 1 and 2 for each of those.

***

[1](#_footnoteref_1). A [user acceptance testing (UAT) environment](../tenants/environments-uat.html) is an [add-on capability](../product-information/add-on-capabilities.html).[2](#_footnoteref_2). A [sandbox environment](../tenants/environments-sandbox.html) is an [add-on capability](../product-information/add-on-capabilities.html).

---

---
title: Use PingOne Credentials to issue and manage digital verifiable credentials
description: Integrate PingOne Credentials to issue and manage cryptographically secure digital verifiable credentials for passwordless access
component: pingoneaic
page_id: pingoneaic:integrations:pingone-credentials
canonical_url: https://docs.pingidentity.com/pingoneaic/integrations/pingone-credentials.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  why-use-pingone-credentials: Why use PingOne Credentials?
  how-to-integrate-with-pingone-credentials: How to integrate with PingOne Credentials
  how-to-load-test-pingone-credentials: How to load test PingOne Credentials
---

# Use PingOne Credentials to issue and manage digital verifiable credentials

Integrate your Advanced Identity Cloud tenant environments with PingOne Credentials to replace manual, error-prone verification processes with cryptographically secure, tamper-proof digital credentials that can be instantly verified without exposing a user's full identity data.

PingOne Credentials lets you create, issue, manage, and revoke cryptographically secure digital verifiable credentials, which users can store in a digital wallet and selectively share to prove identity, entitlements, or authorizations.

## Why use PingOne Credentials?

* **Frictionless onboarding**: Accelerates new user sign-ups by allowing them to present previously verified digital credentials, eliminating redundant data entry and identity checks.

* **Privacy-first access**: Enhances user privacy and security by enabling selective disclosure, where users share only the minimum required attributes from their credentials for access.

* **Simplified compliance**: Minimizes the burden of storing sensitive personally identifiable information (PII) by relying on verifiable credentials.

* **Modern entitlements**: Lets you easily issue and manage digital memberships, certifications, and roles, which can be presented and verified in real-time across various applications and services.

* **Cross-organization trust**: Leverages an open standards-based approach to create a portable digital identity that's verifiable and trusted across multiple services and organizations.

## How to integrate with PingOne Credentials

To integrate with PingOne Credentials:

1. Set up PingOne integration:

   |   |                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------- |
   |   | You only need to perform this setup for the first PingOne product you integrate with Advanced Identity Cloud. |

   1. [Set up mapped PingOne environments](pingone-set-up-environments.html) for each of your tenant environments.

   2. [Set up PingOne product connections](pingone-set-up-product-connections.html) in each of your tenant environments.

2. Set up an authentication journey in your development environment using the PingOne Credentials authentication nodes:

   * [PingOne Credentials Find Wallets node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-find-wallet.html)

   * [PingOne Credentials Pair Wallet node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-pair-wallet.html)

   * [PingOne Credentials Delete Wallet node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-delete-wallet.html)

   * [PingOne Credentials Issue node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-issue.html)

   * [PingOne Credentials Update node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-update.html)

   * [PingOne Credentials Revoke node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-revoke.html)

   * [PingOne Credentials Verification node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-verify.html)

   Find [an example journey](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-overview.html#p1-cred-example-journey) in the PingOne Credentials node reference.

3. Promote the authentication journey to your other tenant environments.

## How to load test PingOne Credentials

When you plan to load test your integration with PingOne Credentials, select the Performance/Load Test Request - Credentials Integration option in the support case submission wizard when submitting your plan. This ensures that PingOne Credentials can be scaled appropriately to handle the expected load during your test.

Learn more in [Create a test plan](../product-information/penetration-and-load-testing-policy.html#create-a-test-plan).

---

---
title: Use PingOne Protect for risk-based authentication and fraud detection
description: Integrate PingOne Protect for risk-based authentication and fraud detection using real-time behavioral and contextual risk signals
component: pingoneaic
page_id: pingoneaic:integrations:pingone-protect
canonical_url: https://docs.pingidentity.com/pingoneaic/integrations/pingone-protect.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  why-use-pingone-protect: Why use PingOne Protect?
  how-to-integrate-with-pingone-protect: How to integrate with PingOne Protect
  how-to-load-test-pingone-protect: How to load test PingOne Protect
  how-to-set-up-a-pingone-risk-authentication-journey: How to set up a PingOne Protect authentication journey
  set-up-an-authentication-journey-with-mfa: "Task 1: Set up an authentication journey with MFA"
  add-pingone-protect-risk-evaluation: "Task 2: Add PingOne Protect risk evaluation"
  view-risk-evaluation-output: "Task 3: View risk evaluation output"
  how-to-train-pingone-protect-risk-models: How to train PingOne Protect risk models
  run-with-production-data-passive-training: "Stage 1: Run with production data (passive training)"
  monitor-and-analyze-with-the-threat-protection-dashboard: "Stage 2: Monitor and analyze with the threat protection dashboard"
  refine-risk-policies-and-predictor-scores-active-optimization: "Stage 3: Refine risk policies and predictor scores (active optimization)"
---

# Use PingOne Protect for risk-based authentication and fraud detection

Integrate your Advanced Identity Cloud tenant environments with PingOne Protect to add risk-based authentication and fraud detection to your user journeys.

PingOne Protect uses continuous, intelligence-based fraud detection to evaluate real-time risk signals from a user's device, network, and behavior. This allows for an adaptive response to authentication requests, enhancing security while minimizing user friction.

## Why use PingOne Protect?

* **Adaptive security**: Dynamically adjusts authentication requirements based on real-time risk signals (for example, location, device, behavioral anomalies). This means low-risk logins are frictionless, while high-risk attempts trigger additional challenges (MFA, step-up authentication) enhancing security without burdening legitimate users.

* **Reduced fraud**: Proactively identifies and mitigates fraudulent activities, such as account takeover (ATO), credential stuffing, and bot attacks, by analyzing a wide range of contextual factors during authentication.

* **Improved user experience**: Minimizes friction for legitimate users by only prompting for additional authentication when truly necessary, leading to higher conversion rates and user satisfaction.

* **Granular control**: Provides detailed insights into risk scores and enables administrators to define specific policies for different risk levels within Advanced Identity Cloud authentication journeys.

Learn more about [PingOne Protect integration use cases](pingone-protect-use-cases.html).

## How to integrate with PingOne Protect

To integrate with PingOne Protect:

1. Set up PingOne integration:

   |   |                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------- |
   |   | You only need to perform this setup for the first PingOne product you integrate with Advanced Identity Cloud. |

   1. [Set up mapped PingOne environments](pingone-set-up-environments.html) for each of your tenant environments.

   2. [Set up PingOne product connections](pingone-set-up-product-connections.html) in each of your tenant environments.

2. Set up an authentication journey in your development environment using the PingOne Protect authentication nodes:

   * [PingOne Protect Initialization node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html)

   * [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html)

   * [PingOne Protect Result node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html)

   Learn more in [How to set up a PingOne Protect authentication journey](#how-to-set-up-a-pingone-risk-authentication-journey).

3. Promote the authentication journey to your production tenant environment.

4. [Train the PingOne Protect risk models](#how-to-train-pingone-protect-risk-models) to optimize risk evaluation for your company.

## How to load test PingOne Protect

When you plan to load test your integration with PingOne Protect, select the Performance/Load Test Request - Protect Integration option in the support case submission wizard when submitting your plan. This ensures that PingOne Protect can be scaled appropriately to handle the expected load during your test.

Learn more in [Create a test plan](../product-information/penetration-and-load-testing-policy.html#create-a-test-plan).

## How to set up a PingOne Protect authentication journey

### Task 1: Set up an authentication journey with MFA

1. Create the following authentication journey. It's a basic username and password journey with OATH authentication nodes added to provide a second factor of authentication, also known as multifactor authentication (MFA).

   ![Example of an Advanced Identity Cloud journey with basic MFA.](_images/pingone-protect-mfa-journey-unmodified.png)

   1. a OATH Token Verifier node: This node verifies a one-time password (OTP) generated by an OATH-compliant mobile authenticator application.

   2. b OATH Registration node: This node allows a user to register and link a new OATH-compliant mobile authenticator application to their account by scanning a QR code.

   |   |                                                                                                                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This example is a minimum viable journey that is missing important features such as recovery code display, recovery code entry, and retry logic. For a more complete example, refer to [OATH Token Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/oath-token-verifier.html). |

2. Configure the OATH nodes as follows:

   > **Collapse: OATH Token Verifier node**
   >
   > * Location:
   >
   >   * Insert the node after the Identity Store Decision node.
   >
   > * Connections:
   >
   >   * Connect the Success outcome to the Success node.
   >
   >   * Connect the Failure outcome to the Failure node.
   >
   >   * Connect the Not registered outcome to the OATH Registration node.
   >
   > * Configuration:
   >
   >   * Accept the default values for all fields.

   > **Collapse: OATH Registration node**
   >
   > * Location:
   >
   >   * Insert the node after the OATH Token Verifier node.
   >
   > * Connections:
   >
   >   * Connect the Success outcome to the OATH Token Verifier node.
   >
   >   * Connect the Failure outcome to the Failure node.
   >
   > * Configuration:
   >
   >   * In the Issuer field, enter a name suited to your company. For example, `My Company`. This is the name that appears in the authenticator application when users register for OATH.
   >
   >   * Accept the default values for the other fields.

3. Test the journey by running the journey's Preview URL in a new incognito browser window as an end user. You can use the following authenticator applications to register for OATH and generate OATH tokens:

   * [The PingID app](https://www.pingidentity.com/en/resources/downloads/pingid.html).

   * Any third-party authenticator application that supports the Time-Based One-Time Password (TOTP) open standard. For example, Google Authenticator or Salesforce Authenticator.

### Task 2: Add PingOne Protect risk evaluation

1. Modify the authentication journey you created in task 1 using the following diagram as guidance. It adds PingOne Protect nodes to perform risk evaluation and reduce MFA fatigue. Only users with a high risk score require MFA to complete sign on, while users with a low or medium risk score can sign on without MFA. Users with a risk score above a defined threshold redirect to the Failure node.

   ![Example of an Advanced Identity Cloud journey with PingOne Protect and basic MFA.](_images/pingone-protect-mfa-journey.png)

   1. a PingOne Protect Initialize node: This node initializes the PingOne Signals (Protect) SDK to collect contextual data for risk evaluation.

   2. b PingOne Protect Evaluation node: This node evaluates the risk score based on the contextual data collected by the PingOne Signals (Protect) SDK.

   3. c PingOne Protect Result nodes: These nodes send transaction feedback to PingOne Protect, which is vital for the continuous learning and optimization of the PingOne Protect models. Over time, this feedback helps PingOne Protect learn what constitutes legitimate and fraudulent activity in your environment.

2. Configure the PingOne Protect nodes as follows:

   > **Collapse: PingOne Protect Initialize node**
   >
   > * Location:
   >
   >   * Insert the node at the start of the journey, before the Page node.
   >
   > * Connections:
   >
   >   * Reconnect the Start node to this node.
   >
   >   * Connect the True outcome to the Page node.
   >
   >   * Connect the False outcome to the Failure node.
   >
   > * Configuration:
   >
   >   * In the PingOne Worker Service ID field, select a worker service. For example, `PingOne Worker AIC`.
   >
   >   * Select the Store Risk Evaluation checkbox. This enables the node to store the risk evaluation in the session. This lets you view the risk evaluation output when debugging and testing the journey.
   >
   >   * Accept the default values for the other fields.

   > **Collapse: PingOne Protect Evaluation node**
   >
   > * Location:
   >
   >   * Insert the node after the Identity Store Decision node.
   >
   > * Connections:
   >
   >   * Connect the High outcome to the OATH Token Verifier node.
   >
   >   * Connect the Medium and Low outcomes to the PingOne Protect Result success node.
   >
   >   * Connect the Exceed Score Threshold, Failure, and ClientError outcomes to the PingOne Protect Result failure node.
   >
   > * Configuration:
   >
   >   * In the PingOne Worker Service ID field, select a worker service. For example, `PingOne Worker AIC`.
   >
   >   * Accept the default values for the other fields.

   > **Collapse: PingOne Protect Result node (connected to the Success node)**
   >
   > * Location:
   >
   >   * Insert the node before the Success node.
   >
   > * Connections:
   >
   >   * Reconnect the Success outcome of the OATH Token Verifier node to this node.
   >
   >   * Connect the outcome of this node to the Success node.
   >
   > * Configuration:
   >
   >   * In the Name field, enter `PingOne Protect Success`.
   >
   >   * In the Completion Status field, select `SUCCESS`.

   > **Collapse: PingOne Protect Result node (connected to the Failure node)**
   >
   > * Location:
   >
   >   * Insert the node before the Failure node.
   >
   > * Connections:
   >
   >   * Reconnect the Failure outcome of the OATH Token Verifier node to this node.
   >
   >   * Reconnect the Failure outcome of the OATH Registration node to this node.
   >
   >   * Connect the outcome of this node to the Failure node.
   >
   > * Configuration:
   >
   >   * In the Name field, enter `PingOne Protect Failure`.
   >
   >   * In the Completion Status field, select `FAILURE`.

3. Test the journey by running the journey's Preview URL in a new incognito browser window as an end user:

   * If you use the same test user, device, and IP address as the test in task 1, you should receive a low risk score and be able to sign on without being prompted for MFA.

   * If you use a different device, IP address, or both, you may receive a high risk score and need to sign on using MFA.

### Task 3: View risk evaluation output

To view the risk evaluation output, enable debug mode for the journey. This lets you view the risk evaluation output in a pop-up window when running the journey:

1. As a tenant administrator, follow the instructions in [Enable debug mode](../end-user/debug-enduser-journeys.html#enable-debug-mode).

2. As an end user, follow the instructions in [View debug information in a pop-up window](../end-user/debug-enduser-journeys.html#view-debug-information-in-a-pop-up-window) to run tests on the journey:

   * As you navigate the journey, the debug pop-up window displays the risk evaluation output, including the risk score and details about the risk predictors that contributed to the score.

   * To trigger a high risk score, you can use a different device, IP address, or both. For example, if you used a desktop computer in task 2, try using a mobile phone or tablet with a different IP address.

   These are some examples of risk evaluation outputs you might see in the debug pop-up window:

   * Low risk evaluation output

     > **Collapse: Example low-risk response**
     >
     > ```json
     > {
     >     "universalId": "id=d646ed76-6b7e-4e47-993a-1b2fc672e588,ou=user,o=alpha,ou=services,ou=am-config",
     >     "transactionId": "4ca6d66e-e857-4127-ada7-4d01d97e2801-request-7/0",
     >     "PingOneProtectEvaluationNode.worker": "PingOne Worker AIC",
     >     "PingOneProtectEvaluationNode.RISK": {
     >         "_links": {
     >             "self": {
     >                 "href": "https://api.pingone.eu/v1/environments/89693e13-3ad2-4b3d-9b66-b9c723f134a2/riskEvaluations/34e40f28-0fe8-4dba-a963-b03481b9723f"
     >             },
     >             "environment": {
     >                 "href": "https://api.pingone.eu/v1/environments/89693e13-3ad2-4b3d-9b66-b9c723f134a2"
     >             },
     >             "event": {
     >                 "href": "https://api.pingone.eu/v1/environments/89693e13-3ad2-4b3d-9b66-b9c723f134a2/riskEvaluations/34e40f28-0fe8-4dba-a963-b03481b9723f/event"
     >             }
     >         },
     >         "id": "34e40f28-0fe8-4dba-a963-b03481b9723f",
     >         "environment": {
     >             "id": "89693e13-3ad2-4b3d-9b66-b9c723f134a2"
     >         },
     >         "createdAt": "2025-07-31T18:19:11.868Z",
     >         "updatedAt": "2025-07-31T18:19:11.868Z",
     >         "event": {
     >             "completionStatus": "IN_PROGRESS",
     >             "ip": "123.123.123.123",
     >             "flow": {
     >                 "type": "AUTHENTICATION"
     >             },
     >             "user": {
     >                 "id": "id=d646ed76-6b7e-4e47-993a-1b2fc672e588,ou=user,o=alpha,ou=services,ou=am-config",
     >                 "name": "barbara.jensen",
     >                 "type": "EXTERNAL"
     >             },
     >             "sharingType": "SHARED",
     >             "browser": {
     >                 "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
     >             }
     >         },
     >         "riskPolicySet": {
     >             "id": "2671d412-c9cb-08ee-2582-ec7e080c58cb",
     >             "name": "Default Risk Policy"
     >         },
     >         "result": {
     >             "level": "LOW",
     >             "score": 0,
     >             "source": "AGGREGATED_SCORES",
     >             "type": "VALUE"
     >         },
     >         "details": {
     >             "ipAddressReputation": {
     >                 "score": 0,
     >                 "domain": {
     >                     "asn": 2856,
     >                     "sld": "btcentralplus",
     >                     "tld": "com",
     >                     "organization": "bt-central-plus",
     >                     "isp": "british telecommunications plc"
     >                 },
     >                 "level": "LOW"
     >             },
     >             "estimatedSpeed": 0,
     >             "anonymousNetworkDetected": false,
     >             "country": "united kingdom",
     >             "previousSuccessfulTransaction": {
     >                 "ip": "123.123.123.123",
     >                 "timestamp": "2025-07-31T18:09:41.024Z",
     >                 "anonymousNetworkDetected": false,
     >                 "country": "united kingdom",
     >                 "state": "kent",
     >                 "city": "willesborough"
     >             },
     >             "device": {
     >                 "id": "Id-ddd38f1d-50ee-4742-bbad-75b02ef242a0",
     >                 "estimatedDistance": 0,
     >                 "os": {
     >                     "name": "Mac OS X"
     >                 },
     >                 "browser": {
     >                     "name": "Chrome"
     >                 },
     >                 "lastSeen": "2025-07-31T18:09:41.547Z"
     >             },
     >             "state": "kent",
     >             "city": "willesborough",
     >             "estimatedDistance": 0,
     >             "impossibleTravel": false,
     >             "suspiciousDevice": {
     >                 "level": "LOW",
     >                 "type": "DEVICE"
     >             },
     >             "userLocationAnomaly": {
     >                 "reason": "Not enough information to assess risk score",
     >                 "status": "IN_TRAINING_PERIOD",
     >                 "type": "USER_LOCATION_ANOMALY"
     >             },
     >             "ipVelocityByUser": {
     >                 "level": "LOW",
     >                 "threshold": {
     >                     "source": "MIN_NOT_REACHED"
     >                 },
     >                 "velocity": {
     >                     "distinctCount": 1,
     >                     "during": 3600
     >                 },
     >                 "type": "VELOCITY"
     >             },
     >             "userVelocityByIp": {
     >                 "level": "LOW",
     >                 "threshold": {
     >                     "source": "MIN_NOT_REACHED"
     >                 },
     >                 "velocity": {
     >                     "distinctCount": 1,
     >                     "during": 3600
     >                 },
     >                 "type": "VELOCITY"
     >             },
     >             "geoVelocity": {
     >                 "level": "LOW",
     >                 "type": "GEO_VELOCITY"
     >             },
     >             "botDetection": {
     >                 "level": "LOW",
     >                 "type": "BOT"
     >             },
     >             "newDevice": {
     >                 "level": "LOW",
     >                 "reason": "This device has been used recently",
     >                 "status": "KNOWN_DEVICE",
     >                 "type": "DEVICE"
     >             },
     >             "ipRisk": {
     >                 "level": "LOW",
     >                 "type": "IP_REPUTATION"
     >             },
     >             "userBasedRiskBehavior": {
     >                 "level": "LOW",
     >                 "reason": "NA",
     >                 "type": "USER_RISK_BEHAVIOR"
     >             },
     >             "anonymousNetwork": {
     >                 "level": "LOW",
     >                 "type": "ANONYMOUS_NETWORK"
     >             },
     >             "adversaryInTheMiddle": {
     >                 "reason": "Not enough information to assess risk score",
     >                 "status": "IN_TRAINING_PERIOD",
     >                 "type": "ADVERSARY_IN_THE_MIDDLE"
     >             },
     >             "trafficAnomaly": {
     >                 "level": "LOW",
     >                 "type": "TRAFFIC_ANOMALY"
     >             }
     >         }
     >     },
     >     "pageNodeCallbacks": {
     >         "0": 0,
     >         "1": 1
     >     },
     >     "PingOneProtectEvaluationNode.riskEvalID": "34e40f28-0fe8-4dba-a963-b03481b9723f",
     >     "realm": "/alpha",
     >     "authLevel": 0,
     >     "objectAttributes": {
     >         "userName": "barbara.jensen"
     >     },
     >     "username": "barbara.jensen"
     > }
     > ```

     The key information is the `result` object, which contains the risk evaluation result:

     ```json
     ...
         "result": {
             "level": "LOW",
             "score": 0,
             "source": "AGGREGATED_SCORES",
             "type": "VALUE"
         },
     ...
     ```

     The granular risk evaluation details are in the `details` object, which contains information about the risk predictors that contributed to the low risk score:

     ```json
     ...
         "botDetection": {
             "level": "LOW",
             "type": "BOT"
         },
         "newDevice": {
             "level": "LOW",
             "reason": "This device has been used recently",
             "status": "KNOWN_DEVICE",
             "type": "DEVICE"
         },
         "ipRisk": {
             "level": "LOW",
             "type": "IP_REPUTATION"
         },
         "userBasedRiskBehavior": {
             "level": "LOW",
             "reason": "NA",
             "type": "USER_RISK_BEHAVIOR"
         },
         "anonymousNetwork": {
             "level": "LOW",
             "type": "ANONYMOUS_NETWORK"
         },
     ...
     ```

   * High risk evaluation output

     > **Collapse: Example high-risk response**
     >
     > ```json
     > {
     >     "universalId": "id=d646ed76-6b7e-4e47-993a-1b2fc672e588,ou=user,o=alpha,ou=services,ou=am-config",
     >     "transactionId": "73522655-5f0b-4665-a93b-1942029fcbc5-request-7/0",
     >     "PingOneProtectEvaluationNode.worker": "PingOne AIC Worker",
     >     "PingOneProtectEvaluationNode.RISK": {
     >         "_links": {
     >             "self": {
     >                 "href": "https://api.pingone.eu/v1/environments/89693e13-3ad2-4b3d-9b66-b9c723f134a2/riskEvaluations/e232ee9f-30c4-4744-9196-6fa933a21af4"
     >             },
     >             "environment": {
     >                 "href": "https://api.pingone.eu/v1/environments/89693e13-3ad2-4b3d-9b66-b9c723f134a2"
     >             },
     >             "event": {
     >                 "href": "https://api.pingone.eu/v1/environments/89693e13-3ad2-4b3d-9b66-b9c723f134a2/riskEvaluations/e232ee9f-30c4-4744-9196-6fa933a21af4/event"
     >             }
     >         },
     >         "id": "e232ee9f-30c4-4744-9196-6fa933a21af4",
     >         "environment": {
     >             "id": "89693e13-3ad2-4b3d-9b66-b9c723f134a2"
     >         },
     >         "createdAt": "2025-07-18T17:22:21.604Z",
     >         "updatedAt": "2025-07-18T17:22:21.604Z",
     >         "event": {
     >             "completionStatus": "IN_PROGRESS",
     >             "ip": "163.5.241.56",
     >             "flow": {
     >                 "type": "AUTHENTICATION"
     >             },
     >             "user": {
     >                 "id": "barbara.jensen",
     >                 "name": "barbara.jensen",
     >                 "type": "EXTERNAL"
     >             },
     >             "sharingType": "SHARED",
     >             "browser": {
     >                 "userAgent": "Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
     >             }
     >         },
     >         "riskPolicySet": {
     >             "id": "2671d412-c9cb-08ee-2582-ec7e080c58cb",
     >             "name": "Default Risk Policy"
     >         },
     >         "result": {
     >             "level": "HIGH",
     >             "score": 125,
     >             "source": "AGGREGATED_SCORES",
     >             "type": "VALUE"
     >         },
     >         "details": {
     >             "ipAddressReputation": {
     >                 "score": 0,
     >                 "domain": {
     >                     "asn": 206092,
     >                     "sld": "",
     >                     "tld": "",
     >                     "organization": "",
     >                     "isp": "internet utilities europe and asia limited"
     >                 },
     >                 "level": "LOW"
     >             },
     >             "anonymousNetworkDetected": true,
     >             "country": "france",
     >             "previousSuccessfulTransaction": {
     >                 "ip": "31.53.231.23",
     >                 "timestamp": "2025-07-18T17:08:04.339Z",
     >                 "anonymousNetworkDetected": false,
     >                 "country": "united kingdom",
     >                 "state": "kent",
     >                 "city": "willesborough"
     >             },
     >             "device": {
     >                 "id": "Id-fd394416-0fb6-4856-86a8-5d5b1ca44f6a",
     >                 "os": {
     >                     "name": "Chrome OS"
     >                 },
     >                 "browser": {
     >                     "name": "Chrome"
     >                 }
     >             },
     >             "state": "paris",
     >             "city": "paris",
     >             "estimatedDistance": 273568.0437,
     >             "impossibleTravel": false,
     >             "suspiciousDevice": {
     >                 "level": "LOW",
     >                 "type": "DEVICE"
     >             },
     >             "ipVelocityByUser": {
     >                 "level": "LOW",
     >                 "threshold": {
     >                     "source": "MIN_NOT_REACHED"
     >                 },
     >                 "velocity": {
     >                     "distinctCount": 2,
     >                     "during": 3600
     >                 },
     >                 "type": "VELOCITY"
     >             },
     >             "userLocationAnomaly": {
     >                 "reason": "Not enough information to assess risk score",
     >                 "status": "IN_TRAINING_PERIOD",
     >                 "type": "USER_LOCATION_ANOMALY"
     >             },
     >             "geoVelocity": {
     >                 "level": "LOW",
     >                 "type": "GEO_VELOCITY"
     >             },
     >             "userVelocityByIp": {
     >                 "level": "LOW",
     >                 "threshold": {
     >                     "source": "MIN_NOT_REACHED"
     >                 },
     >                 "velocity": {
     >                     "distinctCount": 1,
     >                     "during": 3600
     >                 },
     >                 "type": "VELOCITY"
     >             },
     >             "botDetection": {
     >                 "level": "LOW",
     >                 "type": "BOT"
     >             },
     >             "newDevice": {
     >                 "level": "HIGH",
     >                 "reason": "This device has not been used recently",
     >                 "status": "UNKNOWN_DEVICE",
     >                 "type": "DEVICE"
     >             },
     >             "ipRisk": {
     >                 "level": "LOW",
     >                 "type": "IP_REPUTATION"
     >             },
     >             "userBasedRiskBehavior": {
     >                 "level": "LOW",
     >                 "reason": "NA",
     >                 "type": "USER_RISK_BEHAVIOR"
     >             },
     >             "anonymousNetwork": {
     >                 "level": "HIGH",
     >                 "type": "ANONYMOUS_NETWORK"
     >             },
     >             "adversaryInTheMiddle": {
     >                 "reason": "Not enough information to assess risk score",
     >                 "status": "IN_TRAINING_PERIOD",
     >                 "type": "ADVERSARY_IN_THE_MIDDLE"
     >             },
     >             "trafficAnomaly": {
     >                 "level": "LOW",
     >                 "type": "TRAFFIC_ANOMALY"
     >             }
     >         }
     >     },
     >     "pageNodeCallbacks": {
     >         "0": 0,
     >         "1": 1
     >     },
     >     "PingOneProtectEvaluationNode.riskEvalID": "e232ee9f-30c4-4744-9196-6fa933a21af4",
     >     "realm": "/alpha",
     >     "authLevel": 0,
     >     "objectAttributes": {
     >         "userName": "barbara.jensen"
     >     },
     >     "username": "barbara.jensen"
     > }
     > ```

     The key information is the `result` object, which contains the risk evaluation result:

     ```json
     ...
         "result": {
             "level": "HIGH",
             "score": 125,
             "source": "AGGREGATED_SCORES",
             "type": "VALUE"
         },
     ...
     ```

     The granular risk evaluation details are in the `details` object, which contains information about the risk predictors that contributed to the high risk score:

     ```json
     ...
         "botDetection": {
             "level": "LOW",
             "type": "BOT"
         },
         "newDevice": {
             "level": "HIGH",
             "reason": "This device has not been used recently",
             "status": "UNKNOWN_DEVICE",
             "type": "DEVICE"
         },
         "ipRisk": {
             "level": "LOW",
             "type": "IP_REPUTATION"
         },
         "userBasedRiskBehavior": {
             "level": "LOW",
             "reason": "NA",
             "type": "USER_RISK_BEHAVIOR"
         },
         "anonymousNetwork": {
             "level": "HIGH",
             "type": "ANONYMOUS_NETWORK"
         },
     ...
     ```

## How to train PingOne Protect risk models

By default, PingOne Protect is preconfigured with a default machine learning model that assesses risk based on various [predictors](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_predictors.html) such as user behavior, device characteristics, and network context.

PingOne Protect's default risk model isn't something you train in the traditional sense of a machine learning model where you feed it large datasets directly. Instead, it's an intelligent, pre-configured system that continuously learns and adapts based on the real-world data it processes from your authentication and user activities.

The following stages describe how to train (or, more accurately, optimize) the default risk model in PingOne Protect.

### Stage 1: Run with production data (passive training)

The primary training mechanism for PingOne Protect's underlying machine learning models is simply to integrate it into your authentication flows and let it observe real user behavior.

Ping Identity recommends running with the default risk policy for 1 - 3 weeks for workforce usage or 2 - 4 weeks for customer usage. During this period, PingOne Protect's models will build a baseline understanding of normal behavior for your users and environment. This includes learning patterns related to device, location, network, and user-specific habits.

Crucially, ensure you send transaction feedback. After an authentication or transaction is completed, you should use the PingOne Protect Result nodes to tell PingOne Protect whether the transaction was a `SUCCESS` or `FAIL`. This feedback loop is essential for the machine learning models to correctly learn and differentiate between legitimate and fraudulent activities.

### Stage 2: Monitor and analyze with the threat protection dashboard

After the initial observation period, use the PingOne Protect [threat protection dashboard](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_dashboard.html) to analyze the activity in your environment. This dashboard provides insights into risk evaluations, including:

* Number of abnormal activities

* High-risk locations and factors

* Riskiest users

* Distribution of browser and operating systems

Focus on identifying false positives. These are legitimate user interactions that PingOne Protect flagged as high or medium risk. Analyze why these were flagged as risky by looking at the specific predictors involved.

### Stage 3: Refine risk policies and predictor scores (active optimization)

You don't directly modify the default model itself. Instead, you fine-tune how its output is translated into a final risk score and level using [risk policies](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_policies.html):

* Based on your analysis of false positives (and false negatives, though these are harder to spot immediately), you can adjust the scores assigned to individual predictors within your risk policies.

* You can modify the default risk policy or create new targeted policies.

* For each predictor (for example, `Anonymous Network`, `IP Velocity`, or `User Location Anomaly`), you can map its calculated risk level (low, medium, or high) to a specific numerical score.

* You also define the risk thresholds that determine when a total aggregated score results in a low, medium, or high overall risk level.

For example, if `IP Location Anomaly` frequently causes false positives for your legitimate users who travel, you might reduce the score assigned to a high risk for that specific predictor, or create a more lenient predictor for specific user groups.

This active optimization process is iterative. You should continue to monitor the threat protection dashboard and adjust your risk policies as needed based on ongoing user behavior and risk evaluations.

---

---
title: Use PingOne Verify for identity verification and proofing capabilities
description: Integrate PingOne Verify to add identity verification and proofing capabilities for preventing fraud during registrations and transactions
component: pingoneaic
page_id: pingoneaic:integrations:pingone-verify
canonical_url: https://docs.pingidentity.com/pingoneaic/integrations/pingone-verify.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  why-use-pingone-verify: Why use PingOne Verify?
  how-to-integrate-with-pingone-verify: How to integrate with PingOne Verify
  how-to-load-test-pingone-verify: How to load test PingOne Verify
---

# Use PingOne Verify for identity verification and proofing capabilities

Integrate your Advanced Identity Cloud tenant environments with PingOne Verify to add identity verification and proofing to your user journeys.

PingOne Verify reduces fraud by letting you securely and conveniently confirm an end user's identity. You can use it to verify identities during high-risk transactions, new user registrations, or any other scenario where identity proofing is required.

## Why use PingOne Verify?

* **Streamlined onboarding**: Accelerates and secures the new user onboarding process by enabling real-time identity verification (for example, document scanning, facial biometrics) directly within the Advanced Identity Cloud registration flows.

* **Fraud prevention at inception**: Prevents fraudulent accounts from being created in the first place by accurately confirming user identities, reducing the long-term risk of synthetic identities or account abuse.

* **Compliance and trust**: Helps meet regulatory requirements for "Know Your Customer" (KYC) and anti-money laundering (AML) by providing auditable proof of identity, building greater trust with users.

* **Reduced manual effort**: Automates what would otherwise be a manual and time-consuming identity verification process, freeing up support staff.

## How to integrate with PingOne Verify

To integrate with PingOne Verify:

1. Set up PingOne integration:

   |   |                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------- |
   |   | You only need to perform this setup for the first PingOne product you integrate with Advanced Identity Cloud. |

   1. [Set up mapped PingOne environments](pingone-set-up-environments.html) for each of your tenant environments.

   2. [Set up PingOne product connections](pingone-set-up-product-connections.html) in each of your tenant environments.

2. Set up an authentication journey in your development environment using the PingOne Verify authentication nodes:

   * [PingOne Verify Completion Decision node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-completion-decision.html)

   * [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html)

   Find [an example journey](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-completion-decision.html#example_journey) in the PingOne Verify node reference.

3. Promote the authentication journey to your other tenant environments.

## How to load test PingOne Verify

When you plan to load test your integration with PingOne Verify, select the Performance/Load Test Request - Verify Integration option in the support case submission wizard when submitting your plan. This ensures that PingOne Verify can be scaled appropriately to handle the expected load during your test.

Learn more in [Create a test plan](../product-information/penetration-and-load-testing-policy.html#create-a-test-plan).