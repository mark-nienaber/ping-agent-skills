---
title: API references and operations
description: Use PingOne Verify API references and operations.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_developers_api_ref
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_developers_api_ref.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 7, 2026
---

# API references and operations

Learn more about PingOne Verify API references and operations in the following topics:

* [Get started with PingOne APIs](https://developer.pingidentity.com/pingone-api/getting-started/introduction.html)

* [PingOne Verify](https://developer.pingidentity.com/pingone-api/verify/introduction.html)

---

---
title: Configuring and setting up PingOne Verify
description: Configure and set up PingOne Verify as an administrator.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_configuration_setup
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_configuration_setup.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 7, 2026
page_aliases: ["p1_verify_language_localization.adoc"]
section_ids:
  p1_verify_language: Configuring PingOne Verify language localization
  steps: Steps
  p1-verify-orchestration: Configuring and orchestrating PingOne Verify
  before-you-begin: Before you begin
  steps-2: Steps
  choose-from: Choose from:
  integrating-with-pingone-advanced-identity-cloud-and-pingam: Integrating with PingOne Advanced Identity Cloud and PingAM
  before-you-begin-2: Before you begin
  steps-3: Steps
  using-pingfederate: Using PingFederate
  steps-4: Steps
  steps-5: Steps
  result: Result:
  choose-from-2: Choose from:
  before-you-begin-3: Before you begin
  steps-6: Steps
  result-2: Result:
  choose-from-3: Choose from:
  using-the-pingone-verify-mobile-sdk: Using the PingOne Verify mobile SDK
  steps-7: Steps
---

# Configuring and setting up PingOne Verify

To seamlessly integrate PingOne Verify into your identity workflows, first optionally configure language localization for your end users, then choose your orchestration method.

## Configuring PingOne Verify language localization

Optionally use language localization to configure one or more languages and modify the PingOne Verify text fields that are presented to end users in notifications and agreements.

Language localization detects the user's browser locale and refers to the corresponding language pack in PingOne.

Integrating PingOne language packs provides seamless localization and translation of PingOne Verify user interfaces, allowing users to interact with it in their preferred language. Learn more in [Languages](../user_experience/p1_languages.html).

## Steps

1. In the PingOne admin console, go to **User Experience > Languages**.

2. Click your preferred language or add a language. Learn more in [Adding a language](../user_experience/p1_add_a_language.html).

3. In the **Module** list, select **Identity Verification**.

4. In the **Page** list, select a page to view the associated keys. The **Identity Verification** module includes the following pages:

   * **Device**

   * **Document**

   * **Error Messages**

   * **General**

   * **ID Capture**

   * **Retry**

   * **Selfie**

   * **Voice**

   ![Identity Verification module showing pages.](_images/languagelocalization.png)

5. (Optional) In the **Compare to:** list, select another language to compare the text with a language other than the default language.

6. In the translation column, click the **Pencil** icon ([icon: pencil, set=fa]).

7. Edit the text in the translation field to your preferred translation.

8. Click **Save**.

9. In the upper right, click the toggle to enable the language.

|   |                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn more in [Downloading a language bundle](../user_experience/p1_downloading_language_bundle.html) and [Uploading a language bundle](../user_experience/p1_uploading_language_bundle.html). |

## Configuring and orchestrating PingOne Verify

Seamlessly integrate PingOne Verify into your identity workflows.

## Before you begin

Regardless of the configuration method you choose, you'll need:

* A PingOne account with at least one environment that includes the PingOne Verify service. Learn more in [Starting a PingOne trial](../pingone_tutorials/p1_start_a_trial_tutorial_basic_passwordless.html) and [Creating an environment](../getting_started_with_pingone/p1_getting_started_adding_environment.html).

* A PingOne Verify policy, which can be the default policy you modify or a new policy. Learn more in [Creating a verify policy](p1_verify_creating_verify_policy.html).

* (Optional) To [configure language](#p1_verify_language) localization and modify the PingOne Verify text fields that are presented to end users in notifications and agreements.

![Metro map of configuring and orchestrating PingOne Verify.](_images/p1-verify-metro-map.png)

The metro map shows:

1. The PingOne Verify service is enabled within the PingOne environment.

2. The default PingOne Verify policy is customized with specific rules and transaction requirements, such as **Facial Comparison** and **Liveness**.

3. Verification transactions are orchestrated using integrated identity options.

4. The verification flow is executed with the end user, and the results are retrieved.

5. Oversight is maintained by reviewing results and dashboards.

## Steps

1. Choose one of the following methods to orchestrate a verify transaction:

   ### Choose from:

   > **Collapse: PingOne Advanced Identity Cloud and PingAM**
   >
   > ## Integrating with PingOne Advanced Identity Cloud and PingAM
   >
   > Advanced Identity Cloud is a digital identity and access management (IAM) software as a service (SaaS) solution for any identity, workforce, or consumer.
   >
   > PingAM software manages access to resources, such as web pages, applications, or web services available over a network. PingAM centralizes access control by handling both authentication and authorization.
   >
   > To take advantage of PingOne Verify features, you can integrate PingOne Verify nodes into your Advanced Identity Cloud and PingAM journeys. Learn more in [Journeys](https://docs.pingidentity.com/pingoneaic/latest/realms/journeys.html).
   >
   > ### Before you begin
   >
   > Make sure you have:
   >
   > * A PingOne Advanced Identity Cloud or PingAM account. [Getting started with PingOne Advanced Identity Cloud](https://docs.pingidentity.com/pingoneaic/latest/home.html).
   >
   > * A PingOne account. Learn more in [Starting a PingOne trial](../pingone_tutorials/p1_start_a_trial_tutorial_basic_passwordless.html).
   >
   > * A verify policy configured in PingOne (or use the default verify policy).
   >
   > * A worker application with the Identity Data Admin role assigned in PingOne.
   >
   > ### Steps
   >
   > 1. [Configure the PingOne service](https://docs.pingidentity.com/pingoneaic/latest/home.html) in Advanced Identity Cloud.
   >
   > 2. Set up your user journey in Advanced Identity Cloud or PingAM with PingOne Verify nodes in the journey:
   >
   >    * The [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html) to start a new identity verification with PingOne Verify.
   >
   >    * The [PingOne Verify Completion Decision node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-completion-decision.html) to check the status of the last verify transaction.
   >
   >    * The [PingOne Verify Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-authn.html) to integrate biometric authentication functionality in your journey.
   >
   >    * The [PingOne Verify Proofing node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-proof.html) to integrate verification functionality using Government ID, Facial Comparison, and Liveness in a journey.
   >
   >      |   |                                                                                                                                                                                                                                                                                                |
   >      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   >      |   | For self-managed deployments, these nodes are available only PingAM 8.0 or later. If you're using an earlier version of PingAM, use Marketplace nodes, such as the [PingOne Verify Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-authn.html). |
   >
   > 3. Validate that the PingOne Verify Evaluation node is working by doing the following:
   >
   >    1. Configure the node with **Store Verification Metadata** and **Store Verified Data** enabled.
   >
   >    2. Use a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) to return the node state and make sure the values of the `pingOneVerifyMetadata`, `pingOneVerifyVerifiedData`, and `pingOneVerifyEvaluationFailureReason` properties are what you expect. You can also run the journey with Debugging enabled.
   >
   >    3. Add message nodes attached to individual results outputs to understand the flow.
   >
   > 4. Validate that the PingOne Verify Completion Decision node is working by doing the following:
   >
   >    1. Use logger messages in your Completion processing script to determine the processing goals and outcomes, and monitor the log.
   >
   >    2. Evaluate the `nodeState` values of the PingOne Verify nodes that were set in the script using a Scripted Decision node that returns the nodeState, or with the Debugger enabled
   >
   >    3. Add message nodes attached to individual results outputs to understand the flow.

   > **Collapse: PingFederate**
   >
   > ## Using PingFederate
   >
   > To use PingFederate to configure the PingOne Verify Integration Kit:
   >
   > ### Steps
   >
   > * Download PingFederate and the PingOne Verify Integration Kit from the [PingFederate Downloads website](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).
   >
   >   |   |                                                                                                     |
   >   | - | --------------------------------------------------------------------------------------------------- |
   >   |   | You'll need to work with your Ping Identity account team to start a trial license for PingFederate. |
   >
   >   Learn more about getting started in the [PingOne Verify Integration Kit documentation](https://docs.pingidentity.com/integrations/pingone/pingone_verify_integration_kit/pf_p1_verify_ik.html).

   > **Collapse: PingOne API**
   >
   > To configure PingOne Verify with the PingOne REST API:
   >
   > ## Steps
   >
   > 1. Create your theme in PingOne [Branding and themes](../user_experience/p1_branding_themes.html) to brand the PingOne Verify web experience for your end users.
   >
   > 2. (Optional) Use [language localization](#configuring-pingone-verify-language-localization) to configure one or more languages and modify the PingOne Verify text fields that are presented to end users.
   >
   > 3. (Optional) If you enabled one-time passcode (OTP) *(tooltip: \<div class="paragraph">
   >    \<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
   >    \</div>)* through phone or email verification in your policy, [create notification templates](../user_experience/p1_notifications.html).
   >
   > 4. Trigger your first verify transaction:
   >
   >    1. Read [Getting started with the PingOne APIs](https://developer.pingidentity.com/pingone-api/getting-started/introduction.html).
   >
   >    2. Download the [PingOne Postman collection](https://developer.pingidentity.com/pingone-api/getting-started/where-to-go-from-here.html#platform-postman-collection).
   >
   >    3. Note the [Variables you must value](https://developer.pingidentity.com/pingone-api/verify/working-with-pingone-apis/postman-and-pingone/use-the-pingone-postman-environment-template.html#variables-you-must-value).
   >
   >    4. Obtain a [PingOne access token](https://developer.pingidentity.com/pingone-api/getting-started/create-a-test-environment/step-1-get-access-token.html).
   >
   >       Your *{{authPath}}* environment variable in Postman should begin with `auth.pingone`. See [Variables you must value](https://developer.pingidentity.com/pingone-api/verify/working-with-pingone-apis/postman-and-pingone/use-the-pingone-postman-environment-template.html#variables-you-must-value) in the PingOne API documentation to determine the correct *{{authPath}}* for your geography. Note that nothing trails the domain in the *{{authPath}}* variable.
   >
   >    5. Create a new verify transaction with the [Create Verify Transaction API call](https://developer.pingidentity.com/pingone-api/verify/verify-transactions/create-verify-transaction.html).
   >
   >       Your *{{apiPath}}* environment variable in Postman should begin with `api.pingone`. See [Variables you must value](https://developer.pingidentity.com/pingone-api/verify/working-with-pingone-apis/postman-and-pingone/use-the-pingone-postman-environment-template.html#variables-you-must-value) in the PingOne API documentation to determine the correct *{{apiPath}}* for your geography. Note that the trailing `/v1` is required (for example, `api.pingone.com/v1`).
   >
   >       Learn more in [PingOne API requests](https://developer.pingidentity.com/pingone-api/foundations/conventions/pingone-api-requests.html).
   >
   >       ### Result:
   >
   >       Postman renders a QR code.
   >
   >       ![A screen capture of the QR code that Postman renders when creating a Verify transaction.](_images/wtk1692637325156.png)
   >
   >    6. Scan the QR code with a smartphone camera to try the mobile web flow.
   >
   > 5. View the data submitted in the transaction and the scores returned from verification services.
   >
   >    ### Choose from:
   >
   >    * Using the API: Use the [Verified Data](https://developer.pingidentity.com/pingone-api/verify/verified-data.html) and [Verification Metadata](https://developer.pingidentity.com/pingone-api/verify/verification-metadata.html) endpoints.
   >
   >    * Using the PingOne admin console:
   >
   >      1. In PingOne, go to **Environment → Audit**.
   >
   >      2. Edit the **Time Range** and **Within** fields as needed.
   >
   >      3. For **Filter Type**, select **Event Type**.
   >
   >      4. For **Filter**, enter `verify` in the **Search Filter Type** field.
   >
   >      5. Select any of the **Verify** event types.
   >
   >         |   |                                                                                                                                                                                                                       |
   >         | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   >         |   | You can find a complete list of events logged in PingOne in [Audit Reporting Events](https://developer.pingidentity.com/pingone-api/platform/reference/audit-reporting-events.html) in the PingOne API documentation. |
   >
   >         ![A screen capture of the PingOne Audit page with 'verify' entered in the Filter field.](_images/wse1692638943327.png)
   >
   >      6. Click **Run**.
   >
   >      7. To view the specific data and scores from an event, click **View** in the **Details** column in the report summary.

   > **Collapse: PingOne DaVinci**
   >
   > To configure PingOne Verify using PingOne DaVinci:
   >
   > ## Before you begin
   >
   > Add PingOne DaVinci to your PingOne environment. Learn more in [Creating an environment](../getting_started_with_pingone/p1_getting_started_adding_environment.html).
   >
   > ## Steps
   >
   > 1. Create your theme in PingOne [Branding and themes](../user_experience/p1_branding_themes.html) to brand the PingOne Verify web experience for your end users.
   >
   > 2. (Optional) Use [language localization](#configuring-pingone-verify-language-localization) to configure one or more languages and modify the PingOne Verify text fields that are presented to end users.
   >
   > 3. (Optional) If you enabled OTP *(tooltip: \<div class="paragraph">
   >    \<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
   >    \</div>)* through phone or email verification in your policy, [create notification templates](../user_experience/p1_notifications.html).
   >
   > 4. Import the [PingOne Verify quick start flow template](https://marketplace.pingone.com/item/pingone-verify-quick-start) in PingOne DaVinci by downloading it from the Ping Identity Marketplace.
   >
   > 5. Update the flow with your PingOne Verify policy:
   >
   >    1. Click the PingOne Verify `Create transaction` node in the flow.
   >
   >    2. In the **Verify Policy** list, select the policy to use.
   >
   >    ![A screen capture of the PingOne Verify Create transaction node details in PingOne DaVinci.](_images/mmx1692649385736.png)
   >
   > 6. To run the flow and trigger a PingOne Verify transaction, click **Try Flow**.
   >
   >    ### Result:
   >
   >    PingOne DaVinci renders a QR code.
   >
   >    ![A screen capture of the QR code that you can scan with your mobile device to start the verification process.](_images/qui1692650257383.png)
   >
   >    include::partial$p1\_verify\_scan\_qr\_code]
   >
   > 7. View the data submitted in the transaction and the scores returned from verification services.
   >
   >    ### Choose from:
   >
   >    * Using the API: Use the [Verified Data](https://developer.pingidentity.com/pingone-api/verify/verified-data.html) and [Verification Metadata](https://developer.pingidentity.com/pingone-api/verify/verification-metadata.html) endpoints.
   >
   >    * Using the PingOne admin console:
   >
   >      1. In PingOne, go to **Environment → Audit**.
   >
   >      2. Edit the **Time Range** and **Within** fields as needed.
   >
   >      3. For **Filter Type**, select **Event Type**.
   >
   >      4. For **Filter**, enter `verify` in the **Search Filter Type** field.
   >
   >      5. Select any of the **Verify** event types.
   >
   >         |   |                                                                                                                                                                                                                       |
   >         | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   >         |   | You can find a complete list of events logged in PingOne in [Audit Reporting Events](https://developer.pingidentity.com/pingone-api/platform/reference/audit-reporting-events.html) in the PingOne API documentation. |
   >
   >         ![A screen capture of the PingOne Audit page with 'verify' entered in the Filter field.](_images/wse1692638943327.png)
   >
   >      6. Click **Run**.
   >
   >      7. To view the specific data and scores from an event, click **View** in the **Details** column in the report summary.

   > **Collapse: Mobile SDK**
   >
   > ## Using the PingOne Verify mobile SDK
   >
   > Mobile application developers use the PingOne Verify mobile SDK for iOS and PingOne Verify mobile SDK for Android to create the PingOne Verify app for their users. The app is a self-service app for iOS or Android devices that guides the user through the process of taking photos of their ID and a selfie and submitting the photos to PingOne for verification.
   >
   > To use the PingOne Verify mobile SDK:
   >
   > ### Steps
   >
   > 1. Run the sample app from Github:
   >
   >    * [Running the sample app for iOS](https://developer.pingidentity.com/pingone-api/native-sdks/pingone-neo-native-sdks/pingone-verify-native-sdks/pingone-verify-native-sdk-for-ios.html)
   >
   >    * [Running the sample app for Android](https://developer.pingidentity.com/pingone-api/native-sdks/pingone-neo-native-sdks/pingone-verify-native-sdks/pingone-verify-native-sdk-for-android.html)
   >
   > 2. Integrate the PingOne Verify mobile SDK into your own app:
   >
   >    * [Integrating the PingOne Verify SDK into your own app (iOS)](https://github.com/pingidentity/pingone-verify-mobile-sdk-ios/blob/master/README.md)
   >
   >    * [Integrating the PingOne Verify SDK into your own app (Android)](https://github.com/pingidentity/pingone-verify-mobile-sdk-android/blob/master/README.md)

2. Review results and dashboards in [Reviewing and managing verification](p1_verify_managing_verification.html) and [Monitoring PingOne Verify transaction activity and license usage](p1_verify_monitoring.html).

---

---
title: Creating a verify policy
description: A verify policy in PingOne dictates what is required to verify a user, such as an ID verification, facial comparison, or liveness.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_creating_verify_policy
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_creating_verify_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 16, 2025
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Creating a verify policy

A verify policy dictates what's required to verify a user, such as an ID verification, facial comparison, or liveness.

A verify policy allows you to create PingOne Verify transactions for different scenarios, such as:

* Choosing documents for verification during employee onboarding

* Performing a selfie liveness check and comparison during multi-factor authentication (MFA) in PingID

* Enabling Aadhaar eID verification using DigiLocker to authenticate Indian residents using official government electronic credentials rather than physical document scans

## Steps

1. In the PingOne admin console, go to **Identity Verification > Verify Policies**.

   |   |                                                                           |
   | - | ------------------------------------------------------------------------- |
   |   | A default verify policy based on your environment capabilities is listed. |

2. Click the **[icon: plus, set=fa]**icon.

3. Enter or edit the following:

   > **Collapse: Policy configuration**
   >
   > | Field                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   > | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **Name**                             | The policy's name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   > | **Description**                      | The policy's description.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   > | **Store Verified Claims**            | Stores verified personally identifiable information (PII) in the Identity Assurance (IDA) object within the PingOne Directory. Learn more in [Viewing user details](../directory/p1_viewusers.html) and [Editing a user in PingOne](../directory/p1_edituser.html).Select the checkbox to enable storing verified claims.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   > | **Configuration**                    | * **Transaction Timeout**: Time period (in minutes) in which data can be collected after a transaction is created. The maximum transaction timeout is 30 minutes.
   >
   > * **Data Collection Timeout**: Time period (in minutes) in which data can be collected after initiating verification from the UI. By default, the data collection timeout is set to 15 minutes. The maximum data collection timeout is 30 minutes.
   >
   > * **Data Collection Only**: Click the toggle to enable data collection from a user without verification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   > | **Government ID**                    | Verification based on government-issued documents. For example, a driver license or a passport.Configure the following policy settings:* **ID Verification**: Select **Required** or **Disabled** to determine whether the end user must provide a government ID for verification.
   >
   >   &#xA;&#xA;If Government ID is Required, a government ID must be collected to compare with a selfie.
   >
   > * **Document Authentication Provider**: The provider used to authenticate government documents. Select **Mitek** or **Veriff** (default).
   >
   > * **Inspection Type**: Select the type of inspection performed on government-issued documents:
   >
   >   * **Automatic**: AI-based analytics examine the ID document to determine if it's original and unaltered.
   >
   >   * **Manual**: A human agent trained in document authentication examines the photo of the ID to determine its authenticity.
   >
   >   * **Step-Up to Manual**: Automated inspection is tried first. If the document cannot be verified, the service switches to manual inspection.
   >
   >     &#xA;&#xA;Manual and Step-Up to Manual inspection types require an additional license.
   >
   > * **Government ID Retry Attempts**: The number of times a user can retry scanning an ID if the first attempt fails. Possible values for government ID retry attempts are 0 - 3.
   >
   > * **Enable AAMVA**: Click the toggle to enable verification of ID information against the issuing agency database, the [AAMVA Driver's License Data Verification (DLDV)](https://www.aamva.org/technology/systems/verification-systems/dldv) service. Learn more in [PingOne Verify and the American Association of Motor Vehicle Administrator's system of record](p1_verify_aamva_dldv.html).
   >
   > * **Fail Expired IDs**: Click the toggle to fail verification for expired IDs.
   >
   > * **Enable Aadhaar Verification (India)**: Click the toggle to enable user verification of Aadhaar digital IDs through the DigiLocker wallet. |
   > | **Facial Comparison**                | A live photo (selfie) compared with government ID documents or reference selfie for verification.Configure the following policy settings:* **Facial Comparison**: Select **Required**, **Optional**, or **Disabled** to determine whether the end user must provide a selfie for verification.
   >
   >   &#xA;&#xA;If Facial Comparison is Required, a government ID and selfie must be collected.
   >
   > * **Threshold**: The probability that selfies are likely to match with document images (facial comparison) or pass liveness checks (liveness). Select **Low**, **Medium**, or **High** threshold.
   >
   >   &#xA;&#xA;Selfies are less likely to match or pass with a higher threshold.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   > | **Liveness**                         | A liveness check on the live photo (selfie) for verification.Configure the following policy settings:* **Liveness**: Select **Required**, **Optional**, or **Disabled** to determine whether the end user must provide a selfie for verification.
   >
   >   &#xA;&#xA;If Liveness is Required, a selfie must be collected.&#xA;&#xA;Disabling Liveness automatically deactivates the backend injection attack detection (IAD) process. IAD detects and blocks attempts to bypass the device camera using synthetic or prerecorded media.
   >
   > * **Threshold**: The probability that selfies are likely to match with document images (facial comparison) or pass liveness checks (liveness). Select **Low**, **Medium**, or **High** threshold.
   >
   >   &#xA;&#xA;Selfies are less likely to match or pass with a higher threshold.
   >
   > * **Selfie Retry Attempts**: The number of times a user can retake a selfie if the first attempt fails. Possible values for selfie retry attempts are 0 - 3.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | **Voice Verification**               | Verification using voice samples of the end user. There are two types of voice verification policies: enrollment and verification.&#xA;&#xA;Voice verification is deprecated and will be removed on October 17, 2026.	&#xA;&#xA;You must configure a separate enrollment policy and verification policy.Configure the following policy settings:* **Voice Verification**: Select **Required** or **Disabled** to determine whether the end user must use their voice to provide an audio sample for verification.
   >
   > * **Enrollment**: Click the toggle to enable an enrollment policy. Disable for a verification policy.
   >
   > * **Samples Required**: The number of voice samples the user must record for enrollment.
   >
   > * **Voice Phrase**: Phrase the user repeats for enrollment or verification.You can configure custom phrases with the API. Learn more in [Create Custom Voice Phrase](https://developer.pingidentity.com/pingone-api/verify/verify-voice-phrases/create-custom-voice-phrase.html) in the PingOne developer documentation.* **Comparison Threshold**: Voice samples are less likely to match with the voice template at higher thresholds.
   >
   > * **Liveness Threshold**: Voice samples are less likely to pass liveness testing at higher thresholds.
   >
   > * **Store Original Recordings**: Click the toggle to enable storing the original voice sample after a successful transaction.
   >
   > * **Enhance Reference On Re-Enrollment**: Click the toggle to enhance the existing voice reference on re-enrollment. If disabled, the voice reference is replaced instead of enhanced with additional data.
   >
   > * **Enhance Reference on Verification**: Click the toggle to enable improving the existing voice reference by adding a new template.
   >
   >   &#xA;&#xA;You can only enable or disable Enhance Reference on Verification if Enrollment is enabled.                                                                              |
   > | **Phone**                            | Configure the following policy settings:* **Phone Verification**: Select **Required** or **Disabled** to determine whether the end user must provide their phone number for verification.
   >
   > * **Create MFA Device**: Click the toggle to enable registration of a user's phone number as a trusted MFA device after successful OTP or web link verification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   > | **Email**                            | Configure the following policy settings:* **Email Verification**: Select **Required** or **Disabled** to determine whether the end user must provide their email address for verification.
   >
   > * **Create MFA Device**: Click the toggle to enable registration of a user's email address as a trusted MFA device after successful OTP or web link verification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   > | **Identity Data**                    | **Data Matching** compares the identity data extracted during verification with data from an identity record.Configure the following policy settings:* **Attribute**: Lists **Given Name**, **Family Name**, **Full Name**, **Date of Birth**, and **Address**.
   >
   > * **Confidence Threshold**: The probability that an attribute (the data extracted during verification) matches the data from an identity record. Select **None**, **Low**, **Medium**, or **High**.
   >
   >   &#xA;&#xA;Selecting None leaves an attribute unconfigured and no matching occurs.
   >
   > * **Required**: Select the checkbox to make the value of an attribute required.
   >
   >   &#xA;&#xA;The verification fails automatically if a required value can't be extracted during verification or isn't included in the transaction input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   > | **Data-Based Identity Verification** | Verify user identity attributes with trusted third-party data.Configure the following policy settings:* **US Data-Based Identity Verification**: Select **Enabled** or **Disabled**.
   >
   > * **Threshold**: Assesses whether there's fraud or risk associated with the user. Select **Low**, **Medium**, or **High**.
   >
   > * **Required Contractual Obligation**: Select the checkbox to acknowledge that by enabling this feature, you're contractually obligated to obtain user consent.
   >
   >   &#xA;&#xA;You must select the Required Contractual Obligation checkbox to enable the Data-Based Identity Verification policy.Learn more in [PingOne Verify and data-based verification](p1_verify_data_based_verification.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   > | **Device Ownership and Risk**        | Verify the end user legally owns or is associated with the phone number or email being used to complete the verification transaction.Configure the following policy settings:* **Device Ownership Check**: Select **Enabled** or **Disabled**.
   >
   > * **Phone Number Risk Threshold**: Determines the acceptable risk level for phone behavioral data inferred from the carrier history and other data sources. This field is required if **Device Ownership Check** is set to **Enabled**. Select **Medium** (default) or **High**.
   >
   > * **Phone-to-Name Threshold**: Determines linkage between phone and name. Select **Medium** (default) or **High**.You may also configure the following optional thresholds:* (Optional) **Email-to-Phone Threshold**: Select **Medium** or **High**.
   >
   > * (Optional) **Email-to-Name Threshold**: Select **Medium** or **High**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

4. Click **Save**.

### Next steps

Find your new policy on **Verify Policies** page, then trigger a verify transaction using the verify policy, following the steps in [Configuring and setting up PingOne Verify](p1_verify_configuration_setup.html).

---

---
title: Deleting a verify policy
description: You can delete a verify policy in PingOne from your Verify Policies page.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_deleting_a_verify_policy
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_deleting_a_verify_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  steps: Steps
  result: Result:
  result-2: Result:
---

# Deleting a verify policy

You can delete a verify policy from your **Verify Policies** page.

## Steps

1. In the PingOne admin console, go to **Identity Verification > Verify Policies**.

2. Next to the policy that you want to delete, click the **More Options** (⋮) icon, and then click **Delete**.

   ### Result:

   You see a message asking if you're sure you want to delete the policy.

   ![A screen capture of the deleting a policy message.](_images/aof1680101959817.png)

3. Click **Delete**.

   ### Result:

   Your policy is deleted and is no longer listed on the **Verify Policies** page.

---

---
title: Developers
description: The developers section in PingOne Verify serves as a resource for integration.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_developers_page
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_developers_page.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 16, 2026
---

# Developers

This section serves as a technical resource for integrating PingOne Verify into your applications. It includes links to detailed API documentation, orchestration guides for building automated workflows, and mobile SDK instructions.

You can use these resources to programmatically trigger identity checks and embed verification directly into your applications. This ensures your PingOne Verify environment remains secure and scalable while providing a seamless verification experience for your end users.

Learn more in the following topics:

* [API references and operations](p1_verify_developers_api_ref.html)

* [Integration and orchestration](p1_verify_developers_connectors.html)

* [PingOne Verify Mobile SDKs](p1_verify_developers_mobile_sdk.html)

---

---
title: Getting started
description: The getting started section in PingOne Verify provides a high-level overview.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_getting_started
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_getting_started.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 16, 2026
---

# Getting started

This section provides a high-level overview of the PingOne Verify service. It helps you familiarize yourself with core terminology and the basic logic of identity verification. By following the getting started path, you can establish a baseline understanding of the service before moving into more complex configurations.

A solid foundation in these core concepts ensures you can implement security workflows effectively and navigate the PingOne Verify service with confidence.

Learn more in the following topics:

* [Introduction to PingOne Verify](p1_verify_introduction.html)

* [PingOne Verify key concepts](p1_verify_key_concepts.html)

---

---
title: Identity Verification using PingOne Verify
description: PingOne Verify service in PingOne links.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_start
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_start.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 13, 2025
section_ids:
  getting-started: Getting started
  tasks: Tasks
  developers: Developers
  use-cases: Use cases
---

# Identity Verification using PingOne Verify

The PingOne Verify service lets you enable secure user verification based on a government-issued document and live face capture (a selfie).

## Getting started

[icon: rocket-launch, set=far, size=3x]

#### [Introduction](p1_verify_introduction.html)

What is PingOne Verify?

[icon: arrow-down-a-z, set=fas, size=3x]

#### [Key concepts](p1_verify_key_concepts.html)

Learn PingOne Verify key concepts

[icon: gear, set=far, size=3x]

#### [Set up](p1_verify_first_time_setup.html)

Set up PingOne Verify for the first time

## Tasks

[icon: shield-check, set=far, size=3x]

#### [Verify policies](p1_verify_policies.html)

Create, manage, and delete a PingOne Verify policy

[icon: gears, set=far, size=3x]

#### [Configuration and setup](p1_verify_configuration_setup.html)

Configure PingOne Verify

[icon: clipboard-list, set=far, size=3x]

#### [Implementing and managing](p1_verify_managing_verification.html)

View verification results or manually approve a user

[icon: display-chart-up, set=far, size=3x]

#### [Monitoring and system health](p1_verify_monitoring.html)

View the Identity Verification dashboard

## Developers

[icon: gear-api, set=far, size=3x]

#### [API references and operations](p1_verify_developers_api_ref.html)

Access the PingOne Verify API

[icon: diagram-project, set=far, size=3x]

#### [Integration and orchestration](p1_verify_developers_connectors.html)

Integrate PingOne Verify connectors and orchestration

[icon: wrench, set=far, size=3x]

#### [Mobile SDK](p1_verify_developers_mobile_sdk.html)

Download the PingOne Verify native SDK

## Use cases

[icon: suitcase, set=far, size=3x]

#### [New employee onboarding](p1_verify_onboarding_use_case.html)

Automate identity proofing for new hires

---

---
title: Integration and orchestration
description: PingOne Verify provides integration and orchestration resources.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_developers_connectors
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_developers_connectors.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 7, 2026
---

# Integration and orchestration

Learn more about PingOne Verify connectors and orchestration in the following topics:

* [Ping Identity Marketplace: PingOne Verify](https://marketplace.pingone.com/browse?products=verify)

* [PingOne Verify Integration Kit in PingFederate](https://docs.pingidentity.com/integrations/pingone/pingone_verify_integration_kit/pf_p1_verify_ik.html)

* [PingOne Verify Connector](https://docs.pingidentity.com/connectors/p1_verify_connector.html)

* [PingOne Verify Quickstart DaVinci Flow](https://marketplace.pingone.com/item/pingone-verify-quick-start)

---

---
title: Introduction to PingOne Verify
description: PingOne Verify service in PingOne secures user identity verification.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_introduction
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_introduction.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 25, 2024
section_ids:
  verification-flow: Verification flow
  pingone-verify-transaction-flow: PingOne Verify transaction flow
  features: Features
  custom-domains: Custom domains
  branding-and-themes: Branding and themes
  email-and-phone-notification-templates: Email and phone notification templates
  metrics-collection-and-messaging: Metrics collection and messaging
  language-localization: Language localization
---

# Introduction to PingOne Verify

PingOne Verify is a service that enables secure user identity verification based on a government-issued document and live face capture (a selfie), ensuring end users are who they claim to be. It bridges the gap between a person's physical identity and their digital presence.

PingOne Verify ensures the person behind the screen is genuine and ensures three essential benefits:

* **Prevents fraud**: Detects and blocks deepfakes, tampered documents, and synthetic identities during registration or high-risk transactions.

* **Minimizes user friction**: Substitutes manual reviews with a seamless, automated flow that takes only seconds to complete in a browser or application.

* **Strengthens compliance**: Helps meet strict Know Your Customer (KYC) and Anti-Money Laundering (AML) regulatory requirements.

## Verification flow

The PingOne Verify transaction flow orchestrates the end-to-end verification process, moving seamlessly from user data capture to automated validation and real-time status updates.

![Diagram of a PingOne Verify flow.](_images/p1-verify-flow.png)

The diagram shows the following verification flow:

1. The end user initiates verification by capturing a photo of their government-issued ID and a live selfie. This is supported through a mobile web browser, the PingOne Verify mobile SDK, or desktop browser with an integrated or external web camera.

2. The captured data is sent to PingOne Verify. The PingOne ID verification service uses optical character recognition (OCR) and barcode scanning to extract personally identifiable information (PII) from the document. This data is used to validate document authenticity and perform a biometric match against the live selfie. Learn more in [A note on extracted data](https://developer.pingidentity.com/pingone-api/verify/verified-data.html#verified-data-a-note-on-extracted-data) in the PingOne developer documentation.

3. When an end user's ID information and live selfie are successfully verified, the verification status is then instantly updated in the [PingOne admin console](p1_verify_managing_verification.html#p1_verify_view_status) and the [PingOne Verify API](https://developer.pingidentity.com/pingone-api/verify/verify-transactions.html).

   |   |                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | PingOne retains metadata about what was performed and the ID verification status. Any PII data passed to PingOne is deleted by the ID verification service. |

## PingOne Verify transaction flow

The transaction flow maps out the technical lifecycle of a verification request and shows how it's initiated using your integration, tracked across a session, and processed on the backend.

![Diagram of a PingOne Verify transaction flow.](_images/p1-verify-transaction-flow.png)

1. A verification transaction is triggered through the [PingOne Verify Integration Kit for PingFederate](https://docs.pingidentity.com/integrations/pingone/pingone_verify_integration_kit/pf_p1_verify_ik.html), [a PingOne DaVinci flow](https://docs.pingidentity.com/connectors/p1_verify_connector.html), or a [direct API call](https://developer.pingidentity.com/pingone-api/verify/verify-transactions.html). When an end user attempts to sign on or register for your application, they're prompted with instructions within your mobile app or desktop browser.

2. The end user scans a QR code that links their session to a unique transaction ID. This ID is sent to the mobile app or browser to track the verification process.

3. The end user is prompted to submit:

   * A photo of their government ID (driver license or passport).

   * A live selfie for biometric matching.

4. The mobile app or browser sends the data and transaction ID to the PingOne ID verification service, which coordinates with a specialized service provider (SP) to validate the information. Once the SP returns the results, PingOne stores only the final verification status. All PII is stored for 30 minutes and then deleted by the ID verification service.

5. The way this verification status is used depends on your specific integration and use case.

   For example, if you're using PingFederate you can use the authentication policy to check the stored status for all future sign-ons. You can also monitor all transaction activity in the [Identity Verification Dashboard](p1_verify_monitoring.html#p1_verify_dashboard) in the PingOne admin console.

## Features

Configure these core features to seamlessly integrate PingOne Verify into your application and workflows.

### Custom domains

Because PingOne Verify supports custom domains, your domain name can appear in any browser-based user interface that's presented to end users. PingOne routes your domain name to the relevant PingOne services. Learn more in [Domains](../settings/p1_domains.html).

### Branding and themes

PingOne Verify supports branding and themes to easily change the look of your registration pages, sign-on pages, and verification pages for a particular environment. Learn more in [Branding and Themes](../user_experience/p1_branding_themes.html).

### Email and phone notification templates

PingOne Verify supports email and phone notification templates so that you can create a notification for end users to verify their email address or phone number. Learn more in [Notification Templates](../user_experience/p1_notifications.html).

### Metrics collection and messaging

PingOne Verify supports metrics collection and messaging for admin users to collect and audit PingOne Verify transaction events. By configuring webhooks, you can subscribe to real-time transaction lifecycle events, such as when a verification check is initiated or completed. Learn more in [Webhooks](../integrations/p1_webhooks.html).

### Language localization

PingOne Verify supports language localization so end users can interact with PingOne Verify in their preferred language. Learn more in [Configuring PingOne Verify language localization](p1_verify_configuration_setup.html#configuring-and-setting-up-pingone-verify)

---

---
title: Managing a verify policy
description: Edit, rename, or set your verify policy in PingOne into the default policy.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_managing_a_verify_policy
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_managing_a_verify_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 12, 2025
section_ids:
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
---

# Managing a verify policy

Edit, rename, or set your verify policy as the default.

## Steps

* To edit a verify policy:

  1. In the PingOne admin console, go to **Identity Verification > Verify Policies**.

  2. Click the policy you want to edit.

     ### Result:

     The **Policy Details** panel opens.

  3. Click the **Pencil** icon.

  4. Enter or edit the following configurations:

     > **Collapse: Policy configuration**
     >
     > | Field                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
     > | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     > | **Name**                             | The policy's name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
     > | **Description**                      | The policy's description.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
     > | **Store Verified Claims**            | Stores verified personally identifiable information (PII) in the Identity Assurance (IDA) object within the PingOne Directory. Learn more in [Viewing user details](../directory/p1_viewusers.html) and [Editing a user in PingOne](../directory/p1_edituser.html).Select the checkbox to enable storing verified claims.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
     > | **Configuration**                    | * **Transaction Timeout**: Time period (in minutes) in which data can be collected after a transaction is created. The maximum transaction timeout is 30 minutes.
     >
     > * **Data Collection Timeout**: Time period (in minutes) in which data can be collected after initiating verification from the UI. By default, the data collection timeout is set to 15 minutes. The maximum data collection timeout is 30 minutes.
     >
     > * **Data Collection Only**: Click the toggle to enable data collection from a user without verification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
     > | **Government ID**                    | Verification based on government-issued documents. For example, a driver license or a passport.Configure the following policy settings:* **ID Verification**: Select **Required** or **Disabled** to determine whether the end user must provide a government ID for verification.
     >
     >   &#xA;&#xA;If Government ID is Required, a government ID must be collected to compare with a selfie.
     >
     > * **Document Authentication Provider**: The provider used to authenticate government documents. Select **Mitek** or **Veriff** (default).
     >
     > * **Inspection Type**: Select the type of inspection performed on government-issued documents:
     >
     >   * **Automatic**: AI-based analytics examine the ID document to determine if it's original and unaltered.
     >
     >   * **Manual**: A human agent trained in document authentication examines the photo of the ID to determine its authenticity.
     >
     >   * **Step-Up to Manual**: Automated inspection is tried first. If the document cannot be verified, the service switches to manual inspection.
     >
     >     &#xA;&#xA;Manual and Step-Up to Manual inspection types require an additional license.
     >
     > * **Government ID Retry Attempts**: The number of times a user can retry scanning an ID if the first attempt fails. Possible values for government ID retry attempts are 0 - 3.
     >
     > * **Enable AAMVA**: Click the toggle to enable verification of ID information against the issuing agency database, the [AAMVA Driver's License Data Verification (DLDV)](https://www.aamva.org/technology/systems/verification-systems/dldv) service. Learn more in [PingOne Verify and the American Association of Motor Vehicle Administrator's system of record](p1_verify_aamva_dldv.html).
     >
     > * **Fail Expired IDs**: Click the toggle to fail verification for expired IDs.
     >
     > * **Enable Aadhaar Verification (India)**: Click the toggle to enable user verification of Aadhaar digital IDs through the DigiLocker wallet. |
     > | **Facial Comparison**                | A live photo (selfie) compared with government ID documents or reference selfie for verification.Configure the following policy settings:* **Facial Comparison**: Select **Required**, **Optional**, or **Disabled** to determine whether the end user must provide a selfie for verification.
     >
     >   &#xA;&#xA;If Facial Comparison is Required, a government ID and selfie must be collected.
     >
     > * **Threshold**: The probability that selfies are likely to match with document images (facial comparison) or pass liveness checks (liveness). Select **Low**, **Medium**, or **High** threshold.
     >
     >   &#xA;&#xA;Selfies are less likely to match or pass with a higher threshold.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
     > | **Liveness**                         | A liveness check on the live photo (selfie) for verification.Configure the following policy settings:* **Liveness**: Select **Required**, **Optional**, or **Disabled** to determine whether the end user must provide a selfie for verification.
     >
     >   &#xA;&#xA;If Liveness is Required, a selfie must be collected.&#xA;&#xA;Disabling Liveness automatically deactivates the backend injection attack detection (IAD) process. IAD detects and blocks attempts to bypass the device camera using synthetic or prerecorded media.
     >
     > * **Threshold**: The probability that selfies are likely to match with document images (facial comparison) or pass liveness checks (liveness). Select **Low**, **Medium**, or **High** threshold.
     >
     >   &#xA;&#xA;Selfies are less likely to match or pass with a higher threshold.
     >
     > * **Selfie Retry Attempts**: The number of times a user can retake a selfie if the first attempt fails. Possible values for selfie retry attempts are 0 - 3.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
     > | **Voice Verification**               | Verification using voice samples of the end user. There are two types of voice verification policies: enrollment and verification.&#xA;&#xA;Voice verification is deprecated and will be removed on October 17, 2026.	&#xA;&#xA;You must configure a separate enrollment policy and verification policy.Configure the following policy settings:* **Voice Verification**: Select **Required** or **Disabled** to determine whether the end user must use their voice to provide an audio sample for verification.
     >
     > * **Enrollment**: Click the toggle to enable an enrollment policy. Disable for a verification policy.
     >
     > * **Samples Required**: The number of voice samples the user must record for enrollment.
     >
     > * **Voice Phrase**: Phrase the user repeats for enrollment or verification.You can configure custom phrases with the API. Learn more in [Create Custom Voice Phrase](https://developer.pingidentity.com/pingone-api/verify/verify-voice-phrases/create-custom-voice-phrase.html) in the PingOne developer documentation.* **Comparison Threshold**: Voice samples are less likely to match with the voice template at higher thresholds.
     >
     > * **Liveness Threshold**: Voice samples are less likely to pass liveness testing at higher thresholds.
     >
     > * **Store Original Recordings**: Click the toggle to enable storing the original voice sample after a successful transaction.
     >
     > * **Enhance Reference On Re-Enrollment**: Click the toggle to enhance the existing voice reference on re-enrollment. If disabled, the voice reference is replaced instead of enhanced with additional data.
     >
     > * **Enhance Reference on Verification**: Click the toggle to enable improving the existing voice reference by adding a new template.
     >
     >   &#xA;&#xA;You can only enable or disable Enhance Reference on Verification if Enrollment is enabled.                                                                              |
     > | **Phone**                            | Configure the following policy settings:* **Phone Verification**: Select **Required** or **Disabled** to determine whether the end user must provide their phone number for verification.
     >
     > * **Create MFA Device**: Click the toggle to enable registration of a user's phone number as a trusted MFA device after successful OTP or web link verification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
     > | **Email**                            | Configure the following policy settings:* **Email Verification**: Select **Required** or **Disabled** to determine whether the end user must provide their email address for verification.
     >
     > * **Create MFA Device**: Click the toggle to enable registration of a user's email address as a trusted MFA device after successful OTP or web link verification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
     > | **Identity Data**                    | **Data Matching** compares the identity data extracted during verification with data from an identity record.Configure the following policy settings:* **Attribute**: Lists **Given Name**, **Family Name**, **Full Name**, **Date of Birth**, and **Address**.
     >
     > * **Confidence Threshold**: The probability that an attribute (the data extracted during verification) matches the data from an identity record. Select **None**, **Low**, **Medium**, or **High**.
     >
     >   &#xA;&#xA;Selecting None leaves an attribute unconfigured and no matching occurs.
     >
     > * **Required**: Select the checkbox to make the value of an attribute required.
     >
     >   &#xA;&#xA;The verification fails automatically if a required value can't be extracted during verification or isn't included in the transaction input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
     > | **Data-Based Identity Verification** | Verify user identity attributes with trusted third-party data.Configure the following policy settings:* **US Data-Based Identity Verification**: Select **Enabled** or **Disabled**.
     >
     > * **Threshold**: Assesses whether there's fraud or risk associated with the user. Select **Low**, **Medium**, or **High**.
     >
     > * **Required Contractual Obligation**: Select the checkbox to acknowledge that by enabling this feature, you're contractually obligated to obtain user consent.
     >
     >   &#xA;&#xA;You must select the Required Contractual Obligation checkbox to enable the Data-Based Identity Verification policy.Learn more in [PingOne Verify and data-based verification](p1_verify_data_based_verification.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
     > | **Device Ownership and Risk**        | Verify the end user legally owns or is associated with the phone number or email being used to complete the verification transaction.Configure the following policy settings:* **Device Ownership Check**: Select **Enabled** or **Disabled**.
     >
     > * **Phone Number Risk Threshold**: Determines the acceptable risk level for phone behavioral data inferred from the carrier history and other data sources. This field is required if **Device Ownership Check** is set to **Enabled**. Select **Medium** (default) or **High**.
     >
     > * **Phone-to-Name Threshold**: Determines linkage between phone and name. Select **Medium** (default) or **High**.You may also configure the following optional thresholds:* (Optional) **Email-to-Phone Threshold**: Select **Medium** or **High**.
     >
     > * (Optional) **Email-to-Name Threshold**: Select **Medium** or **High**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

  5. Click **Save**.

* To rename a verify policy:

  1. In the PingOne admin console, go to **Identity Verification > Verify Policies**.

  2. Next to the policy you want to rename, click the **More Options** (⋮) icon, and then click **Rename**.

     ![A screen capture of the rename verify policy page.](_images/prt1680105478128.jpg)

  3. Enter a new **Name**.

  4. Click **Save**.

* To set the verify policy as the default:

  1. In the PingOne admin console, go to **Identity Verification > Verify Policies**.

  2. Next to the policy you want to set as the default, click the **More Options** (⋮) icon, and then click **Make Default**.

     ### Result:

     You see a message asking if you're sure you want to select this as your default policy.

  3. Click **Save**.

     ### Result:

     A **Default** icon is added next to your policy name on the **Verify Policies** page.

     |   |                                                                                                                           |
     | - | ------------------------------------------------------------------------------------------------------------------------- |
     |   | Default policies can't be deleted. You must set a different policy as the default before you can delete a default policy. |

---

---
title: Monitoring PingOne Verify transaction activity and license usage
description: Monitor and view license information for PingOne Verify.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_monitoring
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_monitoring.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 7, 2026
page_aliases: ["p1_verify_view_license_info.adoc", "p1_identity_verification_dashboard.adoc"]
section_ids:
  using-the-identity-verification-dashboard: Using the Identity Verification Dashboard
  steps: Steps
  result: Result:
  charts: Charts
  viewing-license-information: Viewing license information
  steps-2: Steps
  next-steps: Next steps
---

# Monitoring PingOne Verify transaction activity and license usage

Monitoring transaction activity and tracking license usage ensures your identity verification services remain operational, efficient, and within subscription limits.

## Using the Identity Verification Dashboard

The **Identity Verification Dashboard** shows identity verification transaction activity for your organization filtered by your choice of date and PingOne Verify policy. You can use this information for managing both identify verification and the handling of accepted and failed verifications in PingOne. Learn more in [Reviewing and managing verification](p1_verify_managing_verification.html).

![Screen capture of the Identity Verification Dashboard.](_images/p1-verify-dashboard.png)

## Steps

1. To access the **Identity Verification Dashboard**, in the PingOne admin console, go to **Monitoring > Identity Verification**.

2. Click one of the tabs:

   * **Verify Dashboard**: Displays volume data and comprehensive trends for successful and failed identity verification transactions over the selected time range.

   * **Error Reasons**: Displays failure analysis data, providing a detailed breakdown of the specific reasons why verification transactions were rejected.

3. To apply filtering to refine the data displayed on the dashboard:

   1. Select a specific time range.

      You can limit the data to:

      * **Today** (Default)

      * **Last 7 Days**

      * **Last 30 Days**

      * **6 Months**

      * **Custom Range**

        |   |                                   |
        | - | --------------------------------- |
        |   | Data begins on February 27, 2024. |

   2. Click a policy.

      ## Result:

      Charts appear showing identity verification transaction activity for the selected time range.

4. To adjust the charts, use the following controls:

   | Icon                                                                | Name         | Description                                                                                                                                                  |
   | ------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | ![The Maximize icon.](../_images/p1-dashboard-maximize.png)         | Maximize     | Expands the chart to fill the dashboard.To minimize the chart, click the icon again.                                                                         |
   | ![The Menu options icon.](../_images/p1-dashboard-menu-options.png) | Menu options | Click the icon to see the following options:- **View summary data**: Displays chart data as a table.

   - **Export to CSV**: Exports chart data to CSV format. |

### Charts

The **Identity Verification Dashboard** shows the following verification charts:

* Accepted Verifications

  Shows hows the total number of accepted verification transactions that occurred during a selected time period. A successful transaction means a user has been validated by the service provider (SP) and verified by the ID verification service. Hover over the bar graph to get more information.

* Failed Verifications

  Shows the total number of failed verification transactions that occurred during a selected time period. A failed transaction means a user has been rejected by the SP or ID verification service. Hover over the bar graph to get more information.

* Document Verification

  Shows successful and failed documentation verification transactions that occurred during a selected time period.

* Facial Verification

  Shows successful and facial verification transactions that occurred during a selected time period. Facial verification checks for the liveness of the user and then compares the selfie with the user's picture on their government-issued ID.

* Document Failure Reason

  Shows a breakdown of the specific reasons why government-issued documents failed validation, such as an expired ID, poor image quality, or unreadable barcodes, during the selected time period.

* Face Verification Failure Reason

  Shows a breakdown of the specific reasons why facial verification checks failed, such as a portrait mismatch with the document photo, poor lighting, or a failed liveness check, during the selected time period.

## Viewing license information

The PingOne Verify license is transaction-based. Your license information shows the quota for the total number of transactions that are allowed. The transactions can take place in any time period, with the limit enforced by the ID verification service.

## Steps

1. Click the Ping Identity logo in the upper-left of the PingOne admin console.

2. Click **Licenses**.

   |   |                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------- |
   |   | The list shows only active licenses by default. To see expired licenses, click **Show All Licenses**. |

   If you have a currently active PingOne Verify license, the console shows the license quota and the current number of transactions used.

## Next steps

To increase your license quota, click the **Please Contact Me** button. We'll contact you to answer any licensing questions and increase your license quota. Learn more in [Licenses and Platform Limits](../getting_started_with_pingone/p1_licenses.html).

---

---
title: PingOne Verify and data-based verification
description: "Data-based verification in PingOne Verify validates a user's identity."
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_data_based_verification
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_data_based_verification.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 7, 2025
section_ids:
  what-is-data-based-verification: What is data-based verification?
  progressive-identity-verification-step: Progressive identity verification step
  complementing-document-based-verification: Complementing document-based verification
  benefits-of-combining-both-verification-methods: Benefits of combining both verification methods
  pingone-verify-sku-groups-and-entitlements: PingOne Verify SKU groups and entitlements
---

# PingOne Verify and data-based verification

Data-based verification in PingOne Verify uses user-provided data, such as name, date of birth, and address, and trusted data sources (including credit bureaus and government databases) to validate a user's identity. Data-based verification provides organizations with seamless validation to ensure adherence to security standards and regulations. Learn more in [Creating a verify policy](p1_verify_creating_verify_policy.html).

## What is data-based verification?

Data-based verification validates a user's identity by comparing personal information submitted by users with trusted data sources through matching algorithms.

Common sources include:

* Credit bureaus

* Government databases

* Telecom and utility records

* Identity graphs

The data-based verification process typically includes:

* **Data input**: The user provides personal data.

* **Data matching**: PingOne Verify checks its sources to find a matching profile or record.

* **Verification outcome**: When you configure a verify policy using data-based verification, PingOne Verify assesses whether fraud or risk is associated with the user. PingOne Verify provides a match score or a pass or fail determination based on the strength of the match that's aligned with the configurable thresholds (low, medium, high).

Unlike document-based checks, this process is often completed in real time with minimal user friction. Learn more in [Creating a verify policy](p1_verify_creating_verify_policy.html).

## Progressive identity verification step

Data-based verification is more effective when used early in a multi-layered identity verification flow as an easy checkpoint, before thorough steps like document capture or biometric verification are initiated.

The following is an example onboarding flow with progressive steps:

1. **Data-based verification**: PingOne Verify validates user-provided data against authoritative sources, returning confidence scores, match results, and potentially additional verified attributes (such as phone type, email domain, and identity confidence level) to enhance user profiles.

2. **Risk evaluation**: When [creating a PingOne Verify policy](p1_verify_creating_verify_policy.html) using data-based verification, configurable thresholds provide the following risk evaluations:

   * **Low risk or strong match**: Proceed with onboarding.

   * **Moderate risk**: Request additional data or passive signals (such as device reputation, geolocation, and so on).

   * **High risk or no match**: Escalate to document-based identity verification.

3. **Document-based verification** (optional): PingOne Verify collects and validates a government-issued ID, performs biometric liveness detection and face match, and cross-checks extracted document data with data-based results to enhance assurance. Use this verification when risk evaluation returns a high risk, or no match is found.

This progressive, risk-based approach ensures low-friction onboarding for trusted users while preserving strong defenses against fraud and identity spoofing.

## Complementing document-based verification

While either verification method can be used independently, combining data-based verification and document-based verification provides stronger, layered identity assurance. These verification methods use different verification signals.

* Data-based verification

  Confirms knowledge-based attributes and helps prevent synthetic identity fraud by validating the user's existence and verifiable presence in trusted records.

* Document-based verification

  Confirms an individual's possession of a unique item (mobile phone, hardware tokens, security keys) by verifying the authenticity of an identity documentation and ensures the user matches the photo using biometric checks.

### Benefits of combining both verification methods

When implemented together, data-based verification and document-based verification offer a powerful, layered approach to identity proofing. Their combination addresses a broader spectrum of risks while enabling higher levels of assurance.

Combining both verification methods offers:

* Broader signal validation

  Organizations can validate both the identity data and the person presenting it.

  Data-based verification confirms that personal information matches real-world records in authoritative sources.

  Document-based verification verifies the authenticity of a government-issued ID and confirms that the person presenting it matches the document photo using biometric comparison and liveness detection.

* Enhanced fraud protection

  * **Stops synthetic identities**: Data-based verification relies on trusted sources to confirm that the individual exists in legitimate systems, making it difficult for fabricated personas to pass.

  * **Detects forged documents**: Document-based verification uses image analysis and validation techniques to identify altered, expired, or fake IDs.

  * **Prevents impersonation**: With biometric face matching and liveness checks, document-based verification ensures the person presenting the document is its rightful holder. When this is cross-checked against verified identity data, it becomes much harder to succeed with stolen or borrowed identities.

* Higher assurance and compliance

  Combining both methods makes it possible to achieve compliance with strict identity assurance frameworks, such as NIST Identity Assurance Level 2 (IAL2).

## PingOne Verify SKU groups and entitlements

To account for variations in regional data access and compliance standards, PingOne Verify organizes its capabilities into SKU groups that define the specific entitlement and registration process required for each country.

| SKU Group | Countries and data sources                                                                                                                                                                                                                         | Registration required?  |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| Group 1   | * Australia Document Verification Service (DVS)

* Cambodia

* China

* India

* Indonesia

* Malaysia

* Philippines

* Thailand

* Brazil

* Mexico

* Sweden                                                                                    | Yes, for Australia DVS  |
| Group 2   | - Canada, excluding Financial Transactions and Reports Analysis Centre of Canada (FINTRAC)

- Australia

- New Zealand

- Argentina

- Chile

- Colombia

- Peru

- UK

- France

- Belgium

- Italy

- Netherlands

- Spain

- Nigeria

- Morocco | No                      |
| Group 3   | * Hong Kong

* Denmark

* Germany                                                                                                                                                                                                                  | No                      |
| Group 4   | - Canada FINTRAC

- Ireland

- Norway

- Poland

- Czech Republic

- Slovakia

- Finland

- Greece                                                                                                                                                 | Yes, for Canada FINTRAC |
| Group 5   | * Bangladesh

* Austria

* Switzerland

* South Korea                                                                                                                                                                                              | No                      |

|   |                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------- |
|   | Verification for Australia DVS and all Canadian sources requires your organization to register with the data provider before use. |

---

---
title: PingOne Verify and documentation authentication
description: Document authentication in PingOne Verify uses machine learning and multiple verification checks to assess the validity of a document presented by a user.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_documentation_authentication
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_documentation_authentication.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Dec 10, 2024
section_ids:
  what-is-machine-learning-and-how-is-it-used-in-document-authentication: What is machine learning and how is it used in document authentication?
  what-are-the-steps-for-automated-document-authentication: What are the steps for Automated Document Authentication?
  types-of-document-authentication: Types of document authentication
  what-is-a-false-positive-what-is-a-false-negative: What is a false positive? What is a false negative?
---

# PingOne Verify and documentation authentication

Document authentication in PingOne Verify uses machine learning and multiple verification checks to assess the validity of a document presented by a user.

## What is machine learning and how is it used in document authentication?

Machine learning (ML) is a branch of artificial intelligence that allows computers to recognize patterns and make predictions based on data. In the context of document authentication (DocAuth), ML is employed to assess whether a document is genuine or fraudulent by comparing the features of the submitted document to a trained model.

Machine learning helps detect:

* Printed or photocopied documents

* Document tampering, such as changes to security features like holograms, text, or watermarks

* Subtle forgeries, such as improper alignment of text or altered photos

Models are trained on thousands of document samples to identify genuine versus fake documents, allowing for more accurate detection over time.

This continual learning process improves the accuracy of the verification system, particularly in high-volume geographies where more document types are processed.

## What are the steps for Automated Document Authentication?

The document authentication process in PingOne Verify is as follows:

1. **Capture document**: The user captures images of the front and back of their identity document, typically using a mobile device.

2. **Classify document**: The system classifies the document based on type (passport, driver license, and so on) and region of origin, using machine learning models trained on various document types.

3. **Compare to model**: The captured document is compared against the pre-trained model for that document type. The model checks for specific security features such as watermarks, barcodes, and holograms that must match what's expected for an authentic document.

4. **Check for tampering or forgery**: The system checks for signs of forgery or tampering, such as photocopied or altered documents, misaligned text, and improper security features.

5. **Extract data**: Relevant data (for example, name, date of birth, document number) is extracted using Optical Character Recognition (OCR) or, when available, directly from encoded barcodes like the PDF417 found on many driver licenses.

6. **Deliver result**: The result is delivered as either a successful authentication or a failure, accompanied by specific failure reasons if applicable (for example, "Document appears to be a photocopy" or "Expired ID").

## Types of document authentication

PingOne Verify offers multiple types of document authentication methods:

| Document authentication method | Definition                                                                                                                                                                                                                                           |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Automated                      | Machine learning models handle the entire authentication process without human intervention.This is the fastest, most scalable option and is ideal for most standard use cases.                                                                      |
| Manual                         | In specific situations where additional review is needed, manual verification can be performed by a human agent who reviews the document based on its visual features.                                                                               |
| Step-Up                        | In high-risk scenarios or when automated verification fails, users could be required to perform a step-up authentication.This can include re-verifying their identity through an additional document authentication check after the initial process. |

## What is a false positive? What is a false negative?

In machine learning and document authentication, the terms false positive and false negative are important for understanding the accuracy of the system:

| Term           | Definition                                                                                                                                                                                                                                                                                                       |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| False positive | Occurs when a fraudulent or altered document is incorrectly flagged as valid by the system.For example, if someone submits a doctored ID and the system verifies it as genuine, that is a false positive.This represents a security risk as unauthorized individuals could gain access to sensitive systems.     |
| False negative | Occurs when a valid, legitimate document is incorrectly flagged as fraudulent or invalid.For example, if a user's authentic ID is not verified due to poor image quality or unusual document features, this is a false negative.This can cause frustration for legitimate users trying to verify their identity. |

|   |                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Verify minimizes both false positives and false negatives through continuous improvement of its machine learning models, though some level of both is expected because of the complex nature of document verification across various geographies and document types. |

---

---
title: PingOne Verify and face verification
description: Face verification in PingOne Verify uses face matching, liveness detection, and injection attack detection to prevent fraud and ensure that the user presenting an ID is who they say they are.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_face_verification
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_face_verification.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 13, 2025
section_ids:
  what-is-face-matching-and-how-is-it-used-in-face-verification: What is face matching and how is it used in face verification?
  presentation-attacks-and-liveness-detection: Presentation attacks and liveness detection
  single-frame-liveness: Single-frame liveness
  deepfakes-and-injection-attack-detection: Deepfakes and injection attack detection
  how-are-injection-attacks-prevented: How are injection attacks prevented?
---

# PingOne Verify and face verification

Face verification in PingOne Verify uses face matching, liveness detection, and injection attack detection to prevent fraud and ensure that the user presenting an ID is who they say they are.

## What is face matching and how is it used in face verification?

PingOne Verify uses machine learning (ML) to detect the presence of a face in a government-issued document and compares it against a live selfie captured by the user. The system returns a confidence score indicating the likelihood that the faces match.

Face verification consists of two primary machine learning applications:

* **Face detection**: Determines if a face is present in an image, identifying its location, scale, and orientation.

* **Face comparison**: Evaluates whether two faces match, accounting for variations in expression, facial hair, and age.

PingOne Verify uses both face detection and face comparison to generate a reliable confidence score in face matching between the live selfie captured and the portrait of the ID document.

## Presentation attacks and liveness detection

Presentation attacks are when fraudsters attempt to bypass verification and physically present an artificial face to the camera by using printed images, digital screens, video replays, or masks. The types of presentation attacks are:

* Printed photo attack

  A fraudster presents a high-quality printed image of the victim's face.

* Screen replay attack

  A digital screen displays an image or video of the victim's face.

* 3D mask attack

  A realistic 3D mask of the victim's face is worn.

Liveness detection prevents presentation attacks. Presentation Attack Detection (PAD) determines whether the face being presented is a real, live person rather than a fake representation.

Liveness detection methods are categorized into:

* **Active liveness**: Requires user interaction, such as blinking, smiling, or turning the head. While effective, it introduces friction and can be bypassed with deepfake technology, a type of artificial intelligence (AI) that creates realistic-looking videos and images.

* **Passive liveness**: Requires no user interaction and detects fraud in a single image using AI-based analysis.

PingOne Verify uses single-frame passive liveness detection, eliminating friction while maintaining security. While PAD is effective against physical fraud, it doesn't protect against digital manipulation attacks, such as deepfakes, that don't rely on a physical medium.

## Single-frame liveness

Presentation attacks are prevented by liveness detection. Single-frame liveness leverages computer vision to detect features in an image that are invisible to the human eye.

AI models analyze factors such as:

* Lighting inconsistencies

* Pixel distortions

* Image artifacts from screen displays or printed documents

A deep neural network, trained on real and fraudulent images, assigns a liveness confidence score based on these subtle characteristics.

## Deepfakes and injection attack detection

In injection attacks, fraudsters bypass the camera entirely and inject synthetic or manipulated biometric data, such as a deepfake, directly into the system.

These attacks are more sophisticated and harder to detect because the fraudulent image isn't captured by the camera itself. Instead, it's digitally inserted into the verification process. The types of deepfakes and injection attacks are:

* Virtual camera attack

  A software-based camera injects pre-recorded images, deepfake videos, or synthetic faces instead of real-time captures.

* External camera manipulation

  Fraudsters use hardware-based techniques to feed a fake video or image into the system.

* JavaScript code injection

  Fraudsters modify browser code or install plugins to intercept and replace biometric data before it reaches the verification system.

* Deepfake injection

  AI-generated deepfake faces are directly fed into the biometric system instead of real faces.

## How are injection attacks prevented?

Injection attack detection works by analyzing and securing the channel through which biometric data is captured, rather than relying on confidence scores that assess the authenticity of an image or video.

Injection attack detection focuses on how the image reaches the system. This is done by monitoring signals that verify whether the camera input is coming from a real device camera or if it was manipulated through software, such as virtual cameras or code injections. These checks include analyzing hardware properties, device-level security features, and integrity signals to detect tampering.

For example, if a virtual camera or an external application attempts to simulate a camera feed, PingOne Verify will recognize this and reject the transaction.

Because these signals provide binary yes or no verification rather than confidence scores, they offer a highly reliable, non-bypassable method of detecting and blocking deepfake and synthetic identity fraud at the source. By ensuring that only genuine, real-time camera captures are accepted, injection attack detection strengthens biometric security without introducing unnecessary friction for legitimate users.

---

---
title: PingOne Verify and identity assurance
description: Identity assurance in PingOne Verify is an extension built on OIDC.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_ida
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_ida.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2025
section_ids:
  what-is-identity-assurance: What is identity assurance?
  why-it-matters: Why it matters
  how-it-works: How it works
  enabling-ida-in-your-verify-policy: Enabling IDA in your verify policy
  viewing-ida-in-pingone-directory: Viewing IDA in PingOne Directory
  using-ida-in-authorization-based-flows: Using IDA in authorization-based flows
---

# PingOne Verify and identity assurance

## What is identity assurance?

OpenID Connect for Identity Assurance (OIDC4IDA or IDA) is an extension built on OpenID Connect (OIDC) that allows identity providers to share verified identity claims, such as name, date of birth, and address about users, including how and when those claims were verified.

IDA works in the following ways:

* Acts like a receipt for identity proofing and records identity claims and details about how those claims were verified.

* Standardizes identity verification data and delivers identity claims and their verification metadata together in a standardized format.

* Enables quick trust assessment and shows what information was verified, when, and by what method. This allows relying parties, such as government services, banking, and healthcare to assess the trustworthiness of identity data without redoing the identity proofing process.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | IDA was developed and is maintained by the Electronic Know Your Customer (eKYC) and IDA Working Group at the OpenID Foundation. It was finalized in 2024, alongside schema and claims definition documents to ensure different security products from separate companies can easily work with each other. Learn more in [OpenID Connect for Identity Assurance 1.0](https://openid.net/specs/openid-connect-4-identity-assurance-1_0.html). |

## Why it matters

IDA provides verification evidence to support claims. Organizations need more than just authentication. Signing on proves that a person controls an account, but it doesn't prove that their claims are true. IDA solves this gap by providing verification evidence for claims. This gives relying parties the confidence they need for high-risk scenarios, which is crucial in industries where trust is regulated, such as banking, healthcare, or government services.

IDA also incorporates verification into the authentication process. Instead of treating identity proofing and sign on as separate steps, IDA allows both to move together in a single flow. The same transaction that confirms a user's identity can also deliver evidence of how their attributes were verified. This provides users with a seamless verification experience and ensures that authentication is always backed by a trustworthy level of assurance.

## How it works

### Enabling IDA in your verify policy

Enabling **Store Verified Claims** when creating a verify policy in PingOne turns on auto-storage of IDA in the PingOne Directory. Even when disabled, the verified data response returns an IDA object, allowing you to use storage options other than PingOne Directory. Learn more in [Creating a verify policy](p1_verify_creating_verify_policy.html).

### Viewing IDA in PingOne Directory

To view IDA:

1. In the PingOne admin console, go to **Directory > Users** and click the appropriate user.

2. On the **Services** tab, click **ID Verification** and then click **Show**. Learn more in [Viewing user details](../directory/p1_viewusers.html).

![A screen capture of IDA in the users page.](_images/p1-ida-user-view.png)

You can also obtain the IDA object from the API response and store it in your own directory or a verifiable credential.

### Using IDA in authorization-based flows

Using IDA in an existing OIDC authorization flow makes it easier to approve high-value transactions and reduce fraud without requiring additional steps for the user.

|   |                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Out-of-the-box inclusion of IDA in OIDC exchanges isn't available. Currently, you can obtain verified claims in PingOne from API responses and integrate them into your own flows or store them in verifiable credentials. |

---

---
title: PingOne Verify and identity data matching
description: Identity data matching in PingOne Verify manages how identity data is captured and presented across different document types.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_identity_data_matching
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_identity_data_matching.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 11, 2025
section_ids:
  how-identity-data-matching-works: How identity data matching works
  scoring-and-configuration: Scoring and configuration
  handling-middle-names-and-nicknames: Handling middle names and nicknames
  handling-identity-documents-without-name-delimiters: Handling identity documents without name delimiters
  ai-enhanced-identity-data-matching: AI-enhanced identity data matching
---

# PingOne Verify and identity data matching

Identity data matching in PingOne Verify manages how identity data is captured and presented across different document types to allow organizations to customize their verification criteria and meet their risk and user experience goals.

## How identity data matching works

Identity data matching compares user-provided identity attributes, such as name and date of birth, against attributes extracted from an identity document. The structure and encoding of these attributes vary by document type.

For example, U.S. driver licenses typically encode and display names using two fields:

* **Given Name**: Includes both the first and middle names.

* **Last Name**: The surname.

During the matching process, PingOne Verify treats these components independently.

## Scoring and configuration

If only a portion of a full name in a U.S. driver license is provided during verification (first name without the middle name), PingOne Verify can assign a medium confidence score for that attribute because of the partial match.

A common identity data match configuration that's widely used is:

* **Given Name**: Medium confidence allowed

* **Last Name**: High confidence required

* **Date of Birth**: High confidence required

This configuration provides strong identity assurance and flexibility for users who might not provide their full given name.

## Handling middle names and nicknames

PingOne Verify identity data matching also supports scenarios where users go by a middle name or nickname, which can differ from the first name on their ID.

If the provided name differs from the official first name but matches the middle name, PingOne Verify compares the full given name on the document against the input. This often results in a medium score rather than a full mismatch.

The AI-powered engine also recognizes common nickname variations across different languages and cultures. For example:

* **Kenny**: A shortened form for Kenneth

* **Kay**: A shortened form of Katherine

The matching algorithm incorporates these mappings into the score to improve match tolerance and user pass rates, while still protecting against fraud.

## Handling identity documents without name delimiters

Sometimes certain identity documents, especially international ones, don't include clear line breaks or structured delimiters between name components.

When names are presented as a single unbroken string, PingOne Verify extracts the full name without a reliable way to distinguish between given names and last names.

In these cases:

* Only the `fullName` attribute is returned from the document.

* Attempts to match against separate `givenName` or `lastName` attributes can result in a mismatch because there's no structural separation in the source data.

To ensure accurate results, you should:

* Provide the full expected name (given name, last name) for matching against these document types.

* Configure identity data matching rules to use the **Full Name** field for comparison. Learn more in [Creating a verify policy](p1_verify_creating_verify_policy.html).

* Adjust scoring configurations in the PingOne admin console **Verify Policies** page to evaluate the `fullName` attribute directly rather than relying on split name fields.

This approach ensures compatibility with a broader set of document formats and improves match rates when field separation is unavailable.

## AI-enhanced identity data matching

PingOne Verify uses AI models trained on global naming conventions and linguistic patterns to enhance the accuracy and flexibility of identity data matching.

This enables identity data matching to:

* Account for partial names

* Detect common nickname-to-full-name relationships

* Maintain a high-level confidence even in the presence of name variations

---

---
title: PingOne Verify and the American Association of Motor Vehicle Administrator&#8217;s system of record
description: "The American Association of Motor Vehicle Administrator's Driver License Data Verification service in PingOne Verify validates your identity."
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_aamva_dldv
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_aamva_dldv.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2026
section_ids:
  what-it-does: What it does
  what-it-doesnt-do: What it doesn't do
  why-it-matters: Why it matters
  where-the-service-works: Where the service works
  how-it-works: How it works
  understanding-a-result-of-a-no-match: Understanding a result of a no match
---

# PingOne Verify and the American Association of Motor Vehicle Administrator's system of record

The American Association of Motor Vehicle Administrator's (AAMVA's) Driver License Data Verification (DLDV) service offers a high-assurance way to validate identity by cross-referencing United States driver license and ID data directly against official state Department of Motor Vehicles (DMV) records. This dependable check simplifies Know Your Customer (KYC) and regulatory compliance while adding a layer of protection against fraud. Learn more in the [AAMVA's DLDV](https://www.aamva.org/technology/systems/verification-systems/dldv) service.

## What it does

* **Real-time DMV validation**: An online service that checks if supplied license or ID data matches DMV records for supported United States jurisdictions.

* **Multi-attribute matching**: Validates name, date of birth, state, and document number.

* **Fraud detection**: A System of Record (SoR) check that provides assurance by verifying that a document's data matches the issuing authority's master file rather than just appearing physically authentic. This process exposes forgeries that bypass visual inspection by identifying fabricated, stolen, or revoked credentials that lack a valid government record.

## What it doesn't do

* **Image analysis**: It doesn't perform optical character recognition (OCR), hologram checks, or liveness.

* **Universal dataset**: Coverage and specific fields returned vary by state. Nationwide coverage is unlikely to occur.

* **Effective against all fraud**: It can't detect injection attacks, deepfakes, or if someone has fraudulently obtained a genuine document.

## Why it matters

The AAMVA's DLDV service moves you beyond just looking at a physical ID. A card can look real, but only a check against official records can prove it's real. The DLDV service bridges this gap by confirming that the information on the ID matches the government's database in real time.

This is critical for:

* Accelerating workforce onboarding by clearing legitimate users faster with high-confidence results, adding less than 3 seconds to the average verification time.

* Identifying sophisticated forgeries that bypass traditional checks, flagging potential fraud in 0.5% of previously approved documents.

* Detecting documents that have been revoked, reported lost, or stolen, which visual-only checks can't detect.

Integrating the AAMVA's DLDV service into your verification policy is recommended for:

* High-value transactions when the risk of fraud outweighs the delay of an additional check.

* Satisfying strict regulatory requirements for identity certainty in banking and fintech.

* Healthcare or government services where knowing a license is valid is essential.

## Where the service works

The AAMVA's DLDV service currently covers 44 jurisdictions, reaching roughly 73% of the United States population. While most states work seamlessly with standard integration, Pennsylvania requires explicit written consent from the user before their data can be checked, and New York carries a significantly higher transaction fee.

## How it works

To enable AAMVA in PingOne Verify,

1. [Create a verify policy](p1_verify_creating_verify_policy.html).

2. **Enable AAMVA** in the policy.

3. [View user ID verification results](p1_verify_managing_verification.html#p1_verify_view_status).

## Understanding a result of a no match

A result of a no match doesn't always mean fraud and happens because the physical card is out of sync with the government's database.

A result of a no match can be caused by the following:

| Cause                   | Description                                                                                                                                                                                                                                                                                                                                           |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Address updates         | Many states don't require you to get a physical card when you move. The database can reflect the current address while the physical card displays the previous address.                                                                                                                                                                               |
| Renewals and extensions | Some states update the validity of a license behind the scenes without issuing a physical card.Some states, such as Illinois, Indiana, and Virginia, grant expiration date extensions digitally without printing a new card. In Massachusetts, a renewal might update the physical card, but the database might still retain the original issue date. |
| Database formatting     | Simple abbreviation or punctuation differences in how data is saved, such as St. instead of Street, can occasionally trigger a mismatch.                                                                                                                                                                                                              |

---

---
title: PingOne Verify key concepts
description: Use the PingOne Verify key concepts to improve understanding of different verification topics.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_key_concepts
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_key_concepts.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 7, 2026
---

# PingOne Verify key concepts

Use the PingOne Verify key concepts to better understand the following topics:

* [Types of verification](p1_verify_types_of_verification.html)

* [American Association of Motor Vehicle Administrator's system of record](p1_verify_aamva_dldv.html)

* [Data-based verification](p1_verify_data_based_verification.html)

* [Document authentication](p1_verify_documentation_authentication.html)

* [Face verification](p1_verify_face_verification.html)

* [Identity data matching](p1_verify_identity_data_matching.html)

* [Identity assurance](p1_verify_ida.html)

* [Policy and compliance](p1_verify_policy_compliance.html)

---

---
title: PingOne Verify mobile driver licenses
description: A mobile driver license (mDL) in PingOne Verify is a secure, digital representation of a physical government-issued identification stored on a mobile device.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_mdl_dc_api
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_mdl_dc_api.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 13, 2026
section_ids:
  standards: Standards
  isoiec-18013: ISO/IEC 18013
  oid4vp: OID4VP
  standards-based-vs-proprietary-apps: Standards-based vs proprietary apps
  standards-based-wallets-mdl-standard: Standards-based wallets (mDL standard)
  proprietary-state-apps-non-standard: Proprietary state apps (non-standard)
  why-it-matters: Why it matters
  how-it-works: How it works
  browser-and-os-support: Browser and OS support
---

# PingOne Verify mobile driver licenses

A mobile driver license (mDL) is a secure, digital representation of a physical government-issued identification stored on a mobile device. It functions as a verifiable credential that enables remote and contactless identity authentication.

The Digital Credentials (DC) API is a browser-based extension of the web credentials API that allows websites to request and verify cryptographically signed information, such as IDs or certificates, directly from a user's digital wallet. By replacing manual document uploads and data entry with a seamless verification flow, the API provides the same phishing-resistant, proximity-based interaction used for passkeys and digital payments.

## Standards

A digital ID is a new credential created using your United States passport and is used if you live in a state that hasn't adopted mDL yet. For a digital ID to work globally, devices must agree on what the data looks like. This is achieved through a combination of International Organization for Standardization (ISO) standards and OpenID protocols.

To maintain security and privacy, mobile device wallets require an approval process. Apple, for example, achieves this by using a trust anchor system. This framework requires any organization requesting identity documents to undergo a formal approval process through Apple Business Connect. By verifying relying parties before they can interact with the Apple Wallet, this process protects users from inadvertent sharing, data harvesting, and fraudulent websites. Google also requires similar approval of relying parties, but currently doesn't have a process in place.

### ISO/IEC 18013

The ISO and the International Electrotechnical Commission (IEC) 18013 define standards for mDLs, ensuring your digital license is cryptographically secure and recognized by authorities such as Transportation Security Administration (TSA) agents or police officers.

* ISO/IEC 18013-5 is the foundation for physical interactions. It allows you to tap your phone at a reader using Near Field Communication (NFC) or Bluetooth. It works offline, allowing verification of your ID without an internet connection.

* ISO/IEC 18013-7 is the internet standard for mDLs. It describes how a website or application can securely ask for your ID data remotely, by enabling age gating (restricting online access to content or features for users under a specific age) or identity proofing (verifying a person is who they say they are with documents and biometrics) without needing you to upload a picture of your physical card.

### OID4VP

While ISO defines the mDL, OpenID for Verifiable Credentials (OID4VP) is the protocol used by the DC API and provides the exchange framework to move the data in an mDL over the web.

OID4VP is a standardized, OpenID-based protocol that governs how a digital wallet securely and with user consent presents verifiable credentials to a relying party. This relying party can be a website, application, or service.

## Standards-based vs proprietary apps

Not all digital IDs are the same. Their underlying technology determines if they'll work with the DC API.

### Standards-based wallets (mDL standard)

For an ID to be compatible with the DC API, it must be stored in a wallet that supports international standards. A standards-based mDL issued by California will work with a verifier in New York because they both use the same communication protocol.

Apple Wallet and Google Wallet are built on these standards, ensuring they work with any website using the DC API. Apple users create IDs in Apple Wallet using Digital ID. Learn more in [Apple introduces Digital ID, a new way to create and present an ID in Apple Wallet](https://www.apple.com/newsroom/2025/11/apple-introduces-digital-id-a-new-way-to-create-and-present-an-id-in-apple-wallet/?utm_source=chatgpt.com).

### Proprietary state apps (non-standard)

Several early-adopter states built standalone applications that don't follow the ISO standards. These apps often rely on displaying a proprietary QR code or a visual animation on the screen that only a specific, state-issued reader can understand.

Because these apps don't use the standard handshake protocols, such as OID4VP, a web browser can't talk to them. If a website uses the DC API to request your ID, these proprietary apps won't show up in the wallet picker.

Users with proprietary state applications won't be able to use the one-tap verification flow and must take photos of their physical cards.

## Why it matters

An mDL is better than a physical ID because of its enhanced security, accuracy, and privacy features. Key differences include the following:

| Feature           | Physical ID                                                                                                                             | mDL                                                                                                       |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Trust source      | Relies on visual features, such as holograms, UV-reactive inks, and watermarks.                                                         | Utilizes cryptographic signatures, a digital seal that breaks if the data is tampered with.               |
| Verification      | Verification is performed by a human and makes the physical card susceptible to forgeries.                                              | A computer instantly verifies the digital seal against the Department of Motor Vehicles (DMV) public key. |
| Data presentation | Required presentation of the physical card exposes the entire dataset's personally identifiable information (PII) to the relying party. | Facilitates the release of specific claims or attributes, such as age, without exposing unrelated data.   |
| Storage           | Stored in a physical wallet and requires manual updates and physical reissuance for data changes.                                       | Stored in a digital wallet, such as Apple or Google Wallet.                                               |

## How it works

An mDL is a type of verifiable credential and works as a digital envelope to stay secure. The DC API is the engine inside your web browser and acts as a neutral mediator between a website and any digital wallet.

The following is an example of a digital identity flow using an mDL (digital envelope) and the DC API:

![A diagram of a digital identity flow using mDL and DC API.](_images/digitalidflow.png)

1. The DMV puts the end user's information in a digital envelope and seals it with a secure digital stamp.

2. The end user's mobile device stores this envelope in a secure app, such as Apple Wallet or Google Wallet.

3. When a web service, such as an online bank, requests the end user's mDL, it calls `navigator.credentials.get()` and asks their device if they have a valid government ID they can share.

4. The browser or operating system (OS) shows a system-level menu of all compatible wallets on the end user's device, such as Google Wallet, Apple Wallet, or a state-specific ID app, allowing the end user to select their preferred compatible digital wallet.

5. After the end user chooses a wallet, the DC API creates an encrypted link between that wallet and the web service that asked for their ID.

6. The wallet app opens, showing exactly what data is being requested, such as the end user's age. The end user authorizes the release with a handshake, using FaceID or a fingerprint.

7. The wallet sends a signed digital envelope back through the API, and the web service verifies the DMV's digital seal to ensure the data is authentic.

### Browser and OS support

You can use an mDL on almost any device:

| Platform      | Browser                          | Method                                                                          |
| ------------- | -------------------------------- | ------------------------------------------------------------------------------- |
| Android       | Google Chrome                    | Provides a direct link to Google Wallet or other compatible state applications. |
| iOS and macOS | Apple Safari                     | Deep integration with Apple Wallet.                                             |
| Desktop       | Google Chrome and Microsoft Edge | Displays a QR code for cross-device verification.                               |

---

---
title: PingOne Verify Mobile SDKs
description: PingOne Verify mobile SDKs.
component: pingone
page_id: pingone:identity_verification_using_pingone_verify:p1_verify_developers_mobile_sdk
canonical_url: https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_developers_mobile_sdk.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 7, 2026
---

# PingOne Verify Mobile SDKs

Learn how to collect information required for verifying a user's identity using PingOne Verify Native SDKs, learn more in [PingOne Verify Native SDKs](https://developer.pingidentity.com/pingone-api/native-sdks/pingone-neo-native-sdks/pingone-verify-native-sdks.html).