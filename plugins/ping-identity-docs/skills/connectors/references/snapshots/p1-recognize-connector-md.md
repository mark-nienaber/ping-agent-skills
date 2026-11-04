---
title: PingOne Recognize Connector
description: Use the PingOne Recognize DaVinci connector to bring biometric selfie enrollment and authentication into your flows.
component: connectors
page_id: connectors::p1_recognize_connector
canonical_url: https://docs.pingidentity.com/connectors/p1_recognize_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-04T00:00:00Z
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-the-connector: Setting up the connector
  connector-settings: Connector settings
  customer-name: Customer Name
  api-key: API Key
  region: Region
  using-the-pingone-recognize-connector-in-a-flow: Using the PingOne Recognize connector in a flow
  biometric-enrollment-and-sign-on: Biometric enrollment and sign-on
  removing-a-users-biometric-enrollment: Removing a user's biometric enrollment
  enrolling-a-user-from-an-identity-verification-flow: Enrolling a user from an identity verification flow
---

# PingOne Recognize Connector

The PingOne Recognize connector adds biometric selfie enrollment and authentication to PingOne DaVinci flows using a headless SDK. DaVinci Forms or Custom HTML components handle the user experience, while the Recognize SDK performs camera capture, liveness detection, face processing, and result verification. The connector also includes backend actions for validation and account management.

You can use the PingOne Recognize connector to:

* Enroll a user with a live selfie.

* Enroll a user with an image.

* Authenticate a user with a live selfie.

* Disenroll a user.

* Check a user's enrollment status.

## Setup

### Resources

Learn more about setup help in the following sections of PingOne Recognize and DaVinci:

* [PingOne Recognize documentation](https://docs.pingidentity.com/recognize/pingone-recognize.html)

* DaVinci documentation

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the PingOne Recognize connector, you'll need:

* A PingOne license with PingOne Recognize ([Try PingOne for free](https://www.pingidentity.com/en/try-ping.html)).

### Setting up the connector

In DaVinci, go to **Connections** and add a **PingOne Recognize** connection. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

#### Connector settings

You can find the following values in the [PingOne Recognize](https://docs.pingidentity.com/recognize/pingone-recognize.html) dashboard on the **Access Control** tab.

![A screen capture of the PingOne Recognize dashboard and Access Control tab.](_images/connector-images/dvc-p1-recognize-access-control.png)

##### **Customer Name**

The unique customer name used to identify your PingOne Recognize tenant, such as `ping_us`. This value is displayed at the top of the **Access Control** tab.

##### **API Key**

The PingOne Recognize **Secret API Key**. You must create the API key manually by clicking **Create Secret API Key** in the **Access Control** tab.

##### **Region**

The environment type and region for your PingOne Recognize tenant, such as `Europe`. This value is displayed at the top of the **Access Control** tab.

## Using the PingOne Recognize connector in a flow

The PingOne Recognize connector works alongside other DaVinci connectors to build end-to-end biometric enrollment and sign-on flows.

### Biometric enrollment and sign-on

You can use the PingOne Recognize connector to route users to enrollment or authentication based on their current biometric status. The **Check Enrollment Status** capability checks whether the user has a biometric record in PingOne Recognize, letting you direct first-time users through enrollment and returning users through authentication.

Before proceeding, you must present a form to collect user credentials and look up the user account.

|   |                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can use the [HTTP connector](http_connector.html) or [Form connector](form_connector.html) to present a message to the end user between steps in the flow. |

To use the PingOne Recognize connector for biometric enrollment and sign-on:

1. Add a [Form connector](form_connector.html) **Show Form** node to present the end user with a sign-on form.

2. Add an [Authentication connector](authentication_connector.html) **Find User** node to look up the user account.

3. Add a **Check Enrollment Status** node to determine whether the user has a biometric record in PingOne Recognize.

4. From the **True** outcome, the user is already enrolled. Add an **Authenticate User** node. The end user is prompted to capture a live selfie, which PingOne Recognize compares against their stored biometric record.

   The **Authenticate User** node produces the following outcomes, each of which branches to its own custom message node:

   * **Authenticated**: The selfie matched the stored biometric record. Continue the flow to a success message.

   * **Not Enrolled**: PingOne Recognize has no record for the user. You can redirect to the enrollment path or present an appropriate message.

   * **Error**: The liveness check failed, the biometric comparison did not match, or a system error occurred. You can branch to a fallback authentication method or an error message.

5. From the **False** outcome on **Check Enrollment Status**, the user is not yet enrolled. Add an **Enroll from Live Selfie** node. The end user is prompted to capture a live selfie to create their biometric record in PingOne Recognize.

   The **Enroll from Live Selfie** node produces the following outcomes, each of which branches to its own custom message node:

   * **True**: Enrollment succeeded. You can continue to authentication or a confirmation screen.

   * **False**: The user did not complete enrollment. You can present an error message or allow them to try again.

### Removing a user's biometric enrollment

You can use the **De-enroll User** capability to remove a user's biometric record from PingOne Recognize. This is useful for privacy compliance flows or when resetting a user's account.

To use the PingOne Recognize connector to remove a user's enrollment:

1. Add a **De-enroll User** node. PingOne Recognize attempts to remove the user's biometric record.

   The **De-enroll User** node produces the following outcomes:

   * **Unenrolled**: The biometric record was successfully removed. This outcome branches to its own confirmation message.

   * **Not Found** and **Error**: The user had no biometric record, or a system error occurred. Both outcomes share a message node where you can present an appropriate message.

### Enrolling a user from an identity verification flow

If an image of the user is already available from an earlier step in your flow, such as a selfie captured during an identity verification (IDV) check, you can use the **Enroll from Image** capability to silently enroll the user without requiring a live camera session.

To use the PingOne Recognize connector for silent enrollment from an image:

1. Ensure that an earlier node in your flow has produced a base64-encoded JPEG image of the user, such as from an identity verification step.

2. Add an **Enroll from Image** node and map the image output to the **Image** input field.

3. From the **True** outcome, the user is enrolled. Continue the flow to the next step.

4. From the **False** outcome, the image quality was insufficient or the user is already enrolled. You can branch to an appropriate message or retry path.