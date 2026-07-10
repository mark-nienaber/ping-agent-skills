---
title: Authorization flow
description: When using the PingOne MFA IdP Adapter through the PingFederate authentication application programming interface (API), the following flow is used for requesting authorization using a push notification to the user's paired mobile app.
component: pingone
page_id: pingone:pingone_mfa_integration_kit_3.2:pf_p1_mfa_ik_authorization_flow
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit_3.2/pf_p1_mfa_ik_authorization_flow.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2024
section_ids:
  authorization-via-the-mobile-app: Authorization via the mobile app
---

# Authorization flow

When using the PingOne MFA IdP Adapter through the PingFederate authentication application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)*, the following flow is used for requesting authorization using a push notification to the user's paired mobile app.

## Authorization via the mobile app

![A flow diagram showing the authorization process](_images/qjy1611964552690.png)

1. The user completes first-factor authentication. Completion of first-factor authentication is a prerequisite before progressing to multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
   \<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
   \</div>)*, when using the PingOne MFA IdP Adapter with the PingFederate Authentication API flow.

2. The status of `AUTHENTICATION_REQUIRED` is returned in the response to the Mobile app (API client).

3. The Mobile app (API client) gets a mobile payload from the mobile SDK.

4. The Mobile app (API client) invokes the `authenticate` action, using the mobile payload.

5. The status of `PUSH_CONFIRMATION_WAITING` together with the `selectedDeviceRef` object are returned in the response to the Mobile app (API client).

6. The Mobile app (API client) invokes the `poll` action, so that PingFederate gets the status of the mobile push. This is repeated until either a successful status is received or a timeout is reached.

7. The status of `MFA_COMPLETED` together with the `device_authorized` code are returned in the response to the Mobile app (API client).

8. The Mobile app (API client) invokes the `continueAuthentication` action. The Mobile app (API client) must call `continueAuthentication` in order to progress in the OIDC flow, and to complete it.

9. PingFederate returns an access token to the Mobile app (API client).

---

---
title: Building a flow in DaVinci
description: To integrate with PingFederate, configure your DaVinci flow to expect the parameters that you defined in the PingOne DaVinci IdP Adapter and end the flow with a JavaScript Object Notation (JSON) response.
component: pingone
page_id: pingone:pingone_davinci_integration_kit:pf_p1_davinci_ik_building_a_flow_in_davinci
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_davinci_integration_kit/pf_p1_davinci_ik_building_a_flow_in_davinci.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 19, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Building a flow in DaVinci

To integrate with PingFederate, configure your DaVinci flow to expect the parameters that you defined in the PingOne DaVinci IdP Adapter and end the flow with a JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
\</div>)* response.

## About this task

|   |                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The following example builds and configures a widget-based DaVinci flow for integration with PingFederate. To show that the integration works, it displays the passed PingFederate values in a user-facing page.Flows can have different user-facing elements or none at all, depending on whether you build a widget-based flow or an API-based flow. |

![A screen capture of the example flow.](_images/ltt1649454442858.jpg)

## Steps

1. In the DaVinci admin portal, go to **Flows**, and open the blank flow that you created in [Adding an application in DaVinci](pf_p1_davinci_ik_adding_an_application_in_davinci.html).

2. Add PingFederate to your flow's input schema.

   1. Go to **Flow Options ( [icon: ellipsis-v, set=fa]) > Input Schema**.

   2. Click **Add**.

   3. In the **Parameter Name** field, enter the exact name that you defined in the **DaVinci Parameter Name** column in your DaVinci adapter configuration.

      |   |                                                                                                                                                                                                                        |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You must add `nonce` as a parameter with the **Data Type** set to **String**.![Screen capture of the nonce parameter with the Data Type set to String and the Required setting enabled.](_images/wgd1678213439935.png) |

   4. Repeat steps b-c for each parameter that you defined in the **Simple Parameter Mappings** and **Advanced Parameter Mappings** tables.

   5. Click **Save**.

3. **Optional:** If you're building a widget-based flow, create a registration form.

   |   |                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This example node represents the functional part of the flow. When you build your own flow, this step is where you customize the flow. |

   1. On the flow canvas, add the **HTTP** connector and select the **HTML Form** capability. Select the node that appears in your flow.

   2. In the **Title** field, enter a title, such as `Registration`.

   3. In the **Fields List** section, add fields for the following:

      * Username

      * Password

      |   |                                                                                                   |
      | - | ------------------------------------------------------------------------------------------------- |
      |   | For help, see the [HTTP connector](https://docs.pingidentity.com/connectors/http_connector.html). |

   4. In the **Next Button Text** field, enter `Sign Up`.

   5. Click **Apply**.

4. **Optional:** For widget-based flows, show the parameters DaVinci received from PingFederate.

   |   |                                                                                               |
   | - | --------------------------------------------------------------------------------------------- |
   |   | This node is for demonstration purposes only. You don't need it when you build your own flow. |

   1. Following your **HTML Form** node in your flow, add the **HTTP** connector and select the **Custom HTML Message** capability. Select the node that appears in your flow.

   2. In the **Title** field, enter a title, such as `Welcome`.

   3. In the **Message** field, enter the following:

      ```none
      Confirm your information:

      Chained Attributes

      Specified chained val:

      Extended Properties

      Specified extended array:

      PAR Object

      Specified PAR:

      Server Base URL:
      ```

   4. Populate the message by clicking **{}** and inserting variables from your flow's input schema.

      ![A screen recording of a user inserting the chainedAttributes variable into the Message field.](_images/ugc1649886713104.gif)

   5. In the **Next Button Text** field, enter `Sign Up`.

   6. Click **Apply**.

5. Send a JSON response back to PingFederate.

   |   |                                                                               |
   | - | ----------------------------------------------------------------------------- |
   |   | When you build your own flow, make sure that you end the flow with this node. |

   1. Following the **Custom HTML Message** node in your flow, add the **HTTP** connector and select the **Send Success JSON Response** capability. Select the node that appears in your flow.

   2. Make sure that **Return Request Parameters** is enabled.

   3. In the **Additional Fields in the Response** section, click **[icon: plus, set=fa]Field**.

   4. In the **Value** field, click **\\{}** and select the **username** variable from your **HTML Form** node.

      ![A screen recording that shows the user inserting the username variable in the value field.](_images/ged1650915377831.gif)

   5. In the **Name of the field containing the additional properties** field, enter `additionalProperties`.

      If you customized the **Additional Properties Attribute** field in your PingOne DaVinci IdP Adapter configuration, enter the same value here.

   6. Make sure **Signed Response** is enabled.

   7. Click **Apply**.

6. If you're building a widget-based flow, on the **HTTP** node, click the **Gear** icon to open the connector configuration. In the **Select an OpenID token management connection for signed HTTP responses** list, select **Token Management**.

   ![A pair of screen captures that show the user selecting token management for OpenID in the connector configuration.](_images/mhl1650918712933.jpg)

   |   |                                                                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If your list doesn't have a token management connector to select, save your flow, go to **Connections > New Connection**, and then add a **Token Management** connection. |

7. Save and deploy your flow.

---

---
title: Changelog
description: The following is the change history for the Magic Link Integration Kit. Updated April 26, 2024.
component: pingone
page_id: pingone:magic_link_integration_kit:pf_magic_link_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/pingone/magic_link_integration_kit/pf_magic_link_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2024
section_ids:
  magic-link-integration-kit-1-0-april-2024: Magic Link Integration Kit 1.0 — April 2024
---

# Changelog

The following is the change history for the Magic Link Integration Kit. Updated April 26, 2024.

## Magic Link Integration Kit 1.0 — April 2024

* Initial release.

---

---
title: Changelog
description: The following is the change history for the PingOne DaVinci Integration Kit.
component: pingone
page_id: pingone:pingone_davinci_integration_kit:pf_p1_davinci_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_davinci_integration_kit/pf_p1_davinci_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 14, 2025
section_ids:
  pingone-davinci-integration-kit-1-3-april-2025: PingOne DaVinci Integration Kit 1.3 - April 2025
  pingone-davinci-integration-kit-1-2-1-july-2024: PingOne DaVinci Integration Kit 1.2.1 - July 2024
  pingone-davinci-integration-kit-1-2-july-2023: PingOne DaVinci Integration Kit 1.2 – July 2023
  pingone-davinci-integration-kit-1-1-2-june-2023: PingOne DaVinci Integration Kit 1.1.2 – June 2023
  pingone-davinci-integration-kit-1-1-1-april-2023: PingOne DaVinci Integration Kit 1.1.1 – April 2023
  pingone-davinci-integration-kit-1-1-march-2023: PingOne DaVinci Integration Kit 1.1 – March 2023
  pingone-davinci-integration-kit-1-0-1-november-2022: PingOne DaVinci Integration Kit 1.0.1 – November 2022
  pingone-davinci-integration-kit-1-0-august-2022: PingOne DaVinci Integration Kit 1.0 – August 2022
---

# Changelog

The following is the change history for the PingOne DaVinci Integration Kit.

## PingOne DaVinci Integration Kit 1.3 - April 2025

* Added the ability to use the default PingFederate template parameters, including extended properties, in the `pingone-davinci.html` template. Learn more in the updated template file and [Customizable user-facing pages](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_custom_user_facing_pages.html) in the PingFederate documentation.

## PingOne DaVinci Integration Kit 1.2.1 - July 2024

* Fixed an issue that caused an unexpected system error when using a DaVinci connector that redirected to PingFederate.

## PingOne DaVinci Integration Kit 1.2 – July 2023

* Added the ability to select API-based DaVinci flows for a highly performant integration to support use cases that don't require user interaction. Use the new **Flow Type** adapter setting to specify either widget-based or API-based DaVinci flows.

## PingOne DaVinci Integration Kit 1.1.2 – June 2023

* Fixed an issue with error handling in certain scenarios with the HTTP connector.

## PingOne DaVinci Integration Kit 1.1.1 – April 2023

* Fixed an issue that caused an inconsistent response error.

* Added support to custom DaVinci domains.

## PingOne DaVinci Integration Kit 1.1 – March 2023

* Added support for the **Nonce Attribute Path** field.

* Resolved a potential security vulnerability.

## PingOne DaVinci Integration Kit 1.0.1 – November 2022

* Fixed an issue that caused the adapter to return an error during an SLO event.

## PingOne DaVinci Integration Kit 1.0 – August 2022

* Initial release.

* Added support for DaVinci connectors with redirect.

* Added the ability for the adapter to bypass or fail when PingOne is unavailable.

* Added the ability to send specific attributes to send to DaVinci using simple and advanced parameter definitions.

* Added the raw response from DaVinci to the log in DEBUG mode.

---

---
title: Changelog
description: The following is the change history for the PingOne Integration Kit.
component: pingone
page_id: pingone:pingone_integration_kit:pf_p1_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_integration_kit/pf_p1_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 20, 2025
section_ids:
  pingone-integration-kit-3-1-1-may-2026: PingOne Integration Kit 3.1.1 - May 2026
  pingone-integration-kit-3-1-november-2025: PingOne Integration Kit 3.1 - November 2025
  pingone-integration-kit-2-7-september-2024: PingOne Integration Kit 2.7 - September 2024
  pingone-integration-kit-2-6-1-may-2024: PingOne Integration Kit 2.6.1 - May 2024
  pingone-integration-kit-2-6-may-2024: PingOne Integration Kit 2.6 - May 2024
  pingone-integration-kit-2-5-1-march-2024: PingOne Integration Kit 2.5.1 - March 2024
  pingone-integration-kit-2-5-february-2022: PingOne Integration Kit 2.5 - February 2022
  pingone-integration-kit-2-4-1-october-2021: PingOne Integration Kit 2.4.1 - October 2021
  pingone-integration-kit-2-4-september-2021: PingOne Integration Kit 2.4 – September 2021
  pingone-integration-kit-2-3-august-2021: PingOne Integration Kit 2.3 – August 2021
  pingone-integration-kit-2-2-2-june-2021: PingOne Integration Kit 2.2.2 – June 2021
  pingone-integration-kit-2-2-1-may-2021: PingOne Integration Kit 2.2.1 – May 2021
  pingone-integration-kit-2-2-march-2021: PingOne Integration Kit 2.2 – March 2021
  pingone-integration-kit-2-1-november-2020: PingOne Integration Kit 2.1 – November 2020
  pingone-integration-kit-2-0-september-2020: PingOne Integration Kit 2.0 – September 2020
  pingone-integration-kit-1-2-1-september-2019: PingOne Integration Kit 1.2.1 – September 2019
  pingone-integration-kit-1-2-may-2019: PingOne Integration Kit 1.2 – May 2019
  pingone-integration-kit-1-1-february-2019: PingOne Integration Kit 1.1 – February 2019
  pingone-integration-kit-1-0-september-2018: PingOne Integration Kit 1.0 – September 2018
---

# Changelog

The following is the change history for the PingOne Integration Kit.

## PingOne Integration Kit 3.1.1 - May 2026

* Added support for specifying a custom MFA Device Policy ID in attribute mapping for the PingOne provisioning connection.

## PingOne Integration Kit 3.1 - November 2025

* Fixed an issue that caused the HTML Form IdP adapter to fail when using the PingOne Password Credential Validator if attempting to authenticate a PingOne user that has a backslash (`\`) in the username.

## PingOne Integration Kit 2.7 - September 2024

* Fixed an issue that could cause a delay in retrieving an updated user schema.

* Added the ability to skip retrieving user group and device details during datastore lookup.

## PingOne Integration Kit 2.6.1 - May 2024

* Added support for the Australia region to the PingOne Connector.

## PingOne Integration Kit 2.6 - May 2024

* Added the ability to exclude retrieving user group, device details, and password expiration information during [password credential validation](pf_p1_ik_configuring_the_password_credential_validator.html).

## PingOne Integration Kit 2.5.1 - March 2024

* Fixed an issue that caused values retrieved from the PingOne datastore for custom multi-value attributes to be formatted incorrectly.

* Fixed an issue that caused disabled user accounts to receive an account recovery email if the account recovery flow was triggered.

## PingOne Integration Kit 2.5 - February 2022

* Fixed an issue that caused an error when trying to update the `population ID` attribute.

## PingOne Integration Kit 2.4.1 - October 2021

* Changed North America region to North America (US) in the PingOne Connector.

* Added support for the North America (Canada) region to the PingOne Connector.

## PingOne Integration Kit 2.4 – September 2021

* Added support for group provisioning.

* Added the ability to select which device will be the default device on user creation.

* Added the ability to select voice as an option for offline device pairing.

* Fixed an issue that prevented all of a user's authentication methods from being provisioned if any of them were invalid.

* Fixed an issue that allowed duplicate local attributes to be defined when configuring an adapter.

* Fixed an issue that could cause an attribute containing an array of objects to be returned in the incorrect format.

* Fixed an issue that caused password validation to fail intermittently when the user's access token expires.

## PingOne Integration Kit 2.3 – August 2021

* Added support for custom string attributes for provisioning to the PingOne Datastore.

* Fixed an error that prevented a user with an expired password from changing their password.

## PingOne Integration Kit 2.2.2 – June 2021

* Added the provisioning connection status to the PingOne connection summary page.

* Fixed an issue that, after upgrading the PingOne Datastore component, caused an error when using the administrative API to bulk import an earlier version of the PingOne Datastore.

## PingOne Integration Kit 2.2.1 – May 2021

* Fixed an issue that could cause an error in the sign-on flow when the user entered an invalid password.

## PingOne Integration Kit 2.2 – March 2021

* Added support for the PingOne platform connection that was introduced in PingFederate 10.2.

* Added support for the [identifier first action](https://apidocs.pingidentity.com/pingone/platform/v1/api/#identifier-first-action) in PingOne. You can now map an **Authoritative IdP** value when configuring the provisioning channel.

* Added the ability to select PingOne populations from a pre-populated list when configuring the provisioning channel.

* Added support for authentication method nicknames. The provisioning connector can now use nicknames to identify and update authentication methods.

* Added the ability to get a user's group membership information from PingOne.

* Improved the error message that appears when a user tries to change their password too frequently.

* Improved validation rules and error messages for some configuration fields.

## PingOne Integration Kit 2.1 – November 2020

* Added a PingOne region list to provisioning options. This allows the provisioning engine to target the PingOne API in your region.

## PingOne Integration Kit 2.0 – September 2020

* Changed name to PingOne Integration Kit in support of new and future PingOne services.

* Added support for managing users' SMS and email devices for PingOne MFA.

* Improved logging abilities.

## PingOne Integration Kit 1.2.1 – September 2019

* Fixed an issue that caused the adapter to fail when a key-value attribute was mapped with JSON Pointer syntax.

* Improved the input validation for the **Custom Proxy Host** field in the password credential validator configuration.

* Improved the error message that a user sees when they try to change their password too frequently.

## PingOne Integration Kit 1.2 – May 2019

* Added the ability to override the system-default proxy settings in the data store configuration.

* Added the ability to customize authentication error messages in the password credential validator configuration.

* Improved the error messages that appear when a user tries to set a password that doesn't meet the password policy.

* Fixed an issue that prevented users with empty attributes from being provisioned to PingOne.

* Removed support for obsolete scopes from the provisioning connector and data store configuration screen.

## PingOne Integration Kit 1.1 – February 2019

* Added the ability to use PingOne as a data store and password credential validator.

## PingOne Integration Kit 1.0 – September 2018

* Initial release with support for provisioning to PingOne.

---

---
title: Changelog
description: The following is the change history for the PingOne Protect Integration Kit.
component: pingone
page_id: pingone:pingone_protect_integration_kit:pf_p1_protect_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_protect_integration_kit/pf_p1_protect_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  pingone-protect-integration-kit-1-0-8-june-2026: PingOne Protect Integration Kit 1.0.8 — June 2026
  pingone-protect-integration-kit-1-0-7-march-2026: PingOne Protect Integration Kit 1.0.7 — March 2026
  pingone-protect-integration-kit-1-0-6-september-2025: PingOne Protect Integration Kit 1.0.6 — September 2025
  pingone-protect-integration-kit-1-0-5-march-2025: PingOne Protect Integration Kit 1.0.5 — March 2025
  pingone-protect-integration-kit-1-0-4-november-2024: PingOne Protect Integration Kit 1.0.4 — November 2024
  pingone-protect-integration-kit-1-0-3-january-2024: PingOne Protect Integration Kit 1.0.3 — January 2024
  pingone-protect-integration-kit-1-0-2-november-2023: PingOne Protect Integration Kit 1.0.2 — November 2023
  pingone-protect-integration-kit-1-0-1-july-2023: PingOne Protect Integration Kit 1.0.1 — July 2023
  pingone-protect-integration-kit-1-0-july-2023: PingOne Protect Integration Kit 1.0 — July 2023
---

# Changelog

The following is the change history for the PingOne Protect Integration Kit.

## PingOne Protect Integration Kit 1.0.8 — June 2026

* The integration kit now supports targeted risk policies, including mapping of mitigations defined in your policies.

* The included PingOne Protect (Signals) SDK has been updated to version 5.6.6.

* Security improvements.

## PingOne Protect Integration Kit 1.0.7 — March 2026

* This version includes only bug fixes.

## PingOne Protect Integration Kit 1.0.6 — September 2025

* The included PingOne Protect (Signals) SDK has been updated to version 5.6.3.

* The integration kit now has an option to instruct the Signals SDK to include browser-based user location data if the user has provided their consent (option is available on both the adapter and provider configuration pages).

## PingOne Protect Integration Kit 1.0.5 — March 2025

* Modifications have been made to allow use of the PingID Device Trust risk predictor in risk evaluations, based on the data provided by the PingID Device Trust agent installed on user computers.

* The included PingOne Protect (Signals) SDK has been updated to version 5.5.0.

## PingOne Protect Integration Kit 1.0.4 — November 2024

* The included PingOne Protect (Signals) SDK has been updated to version 5.3.7.

* PingFederate now takes into account the additional "recommended actions" that were added for risk evaluations.

* PingFederate now takes into account the flow subtype if one was specified for a risk evaluation.

## PingOne Protect Integration Kit 1.0.3 — January 2024

* There were cases where user authentication would fail if the flow involved an X.509 certificate. This issue has been fixed (STAGING-21876).

## PingOne Protect Integration Kit 1.0.2 — November 2023

* A new setting called **Custom Connection Pool** has been added to allow adjustment of the number of connections to PingOne Protect. Default value is 50.

* General performance improvements

## PingOne Protect Integration Kit 1.0.1 — July 2023

* Critical bug fix

## PingOne Protect Integration Kit 1.0 — July 2023

* Initial release

---

---
title: Changelog
description: The following is the change history for the PingOne Risk Integration Kit.
component: pingone
page_id: pingone:pingone_risk_integration_kit:pf_p1_risk_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 13, 2024
section_ids:
  pingone-risk-integration-kit-1-3-september-2022: PingOne Risk Integration Kit 1.3 — September 2022
  pingone-risk-integration-kit-1-2-1-february-2022: PingOne Risk Integration Kit 1.2.1 — February 2022
  pingone-risk-integration-kit-1-2-september-2021: PingOne Risk Integration Kit 1.2 — September 2021
  pingone-risk-integration-kit-1-1-march-2021: PingOne Risk Integration Kit 1.1 — March 2021
  pingone-risk-integration-kit-1-0-december-2020: PingOne Risk Integration Kit 1.0 — December 2020
---

# Changelog

The following is the change history for the PingOne Risk Integration Kit.

## PingOne Risk Integration Kit 1.3 — September 2022

* Changed the product name to PingOne Risk Integration Kit.

* Added the ability to set a **Policy ID** as a chained attribute and use it to set the risk policy.

* Added Signals SDK Javascript and mechanism to capture device profiling.

* Added support for **Risk Score** as an attribute returned by the adapter.

* Fixed an issue that caused page expired issues when the target application did not respond during the Risk Timeout.

## PingOne Risk Integration Kit 1.2.1 — February 2022

* Fixed an issue that caused an error when users attempted the get risk predictors action.

## PingOne Risk Integration Kit 1.2 — September 2021

* Added support for including third-party risk predictors in risk evaluations. Learn more in [Using custom risk predictors](pf_p1_risk_ik_using_custom_risk_predictors.html).

* Improved the **PingOne Risk Policy** list by clarifying that the default selection uses the default PingOne Risk policy.

* Improved the clarity of the tooltips in the adapter configuration.

* Improved the device profiling script by excluding low-value attributes, such as `fonts`, `touchSupport`, `webgl` and `audio`. This reduces the size of the device profile cookie by up to 86% without impacting the quality of the risk evaluations.

## PingOne Risk Integration Kit 1.1 — March 2021

* Added support for pre-populating adapter settings based on the selected PingOne environment. Available in PingFederate 10.2 or later.

* Fixed an issue that caused an error when the adapter received an unexpected attribute type.

* Fixed an issue that skipped device profiling in Internet Explorer 11 when **Captured by this device** was selected.

## PingOne Risk Integration Kit 1.0 — December 2020

* Initial release.

* Added support for getting risk results and transaction information from PingOne Risk.

* Added the ability to send a device profile and transaction information to PingOne Risk.

* Added the ability to add device profiling into any browser-based authentication source.

* Added support for risk models based on user behavior, IP reputation, geovelocity, and anonymous network detection.

* Added the ability to map any PingOne Risk API response attribute to an attribute in the PingFederate authentication policy.

* Added authentication success/failure reporting to PingOne Risk.

* Added the ability to test the connection to PingOne Risk.

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Added settings for API connection and request timeouts.

* Added settings to override the PingFederate system-default proxy settings.

---

---
title: Changelog
description: The following is the change history for the PingOne Verify Integration Kit.
component: pingone
page_id: pingone:pingone_verify_integration_kit:pf_p1_verify_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_verify_integration_kit/pf_p1_verify_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 18, 2025
section_ids:
  pingone-verify-integration-kit-2-3-3-december-2025: PingOne Verify Integration Kit 2.3.3 - December 2025
  pingone-verify-integration-kit-2-3-2-october-2025: PingOne Verify Integration Kit 2.3.2 - October 2025
  pingone-verify-integration-kit-2-3-1-august-2025: PingOne Verify Integration Kit 2.3.1 - August 2025
  pingone-verify-integration-kit-2-3-february-2025: PingOne Verify Integration Kit 2.3 - February 2025
  pingone-verify-integration-kit-2-2-1-august-2023: PingOne Verify Integration Kit 2.2.1 – August 2023
  pingone-verify-integration-kit-2-2-july-2023: PingOne Verify Integration Kit 2.2 – July 2023
  pingone-verify-integration-kit-2-1-december-2022: PingOne Verify Integration Kit 2.1 – December 2022
  pingone-verify-integration-kit-2-0-july-2022: PingOne Verify Integration Kit 2.0 – July 2022
  pingone-verify-integration-kit-1-1-july-2021: PingOne Verify Integration Kit 1.1 – July 2021
  pingone-verify-integration-kit-1-0-january-2021: PingOne Verify Integration Kit 1.0 – January 2021
---

# Changelog

The following is the change history for the PingOne Verify Integration Kit.

## PingOne Verify Integration Kit 2.3.3 - December 2025

* Upgraded the Jackson library to version 2.20.x to ensure continued alignment with maintained upstream dependencies.

## PingOne Verify Integration Kit 2.3.2 - October 2025

* Added support for data-based identity verification. This update introduces new core contract attributes and adapter configuration fields, plus changes to the **First Name Chained Attribute** and **Last Name Chained Attribute** fields.

  Learn more about these updates in [Core contract attributes](pf-p1-verify-ik-core-contract-attributes.html) and the **National ID Number Chained Attribute** through **Country Code Chained Attribute** table entries in [PingOne Verify IdP Adapter settings reference](pf_p1_verify_ik_p1_verify_idp_adapter_settings_reference.html).

  You can find more information about data-based identity verification in [PingOne Verify and data-based verification](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_data_based_verification.html) in the PingOne Verify documentation, and [Verify Data Based Identity Verification](https://apidocs.pingidentity.com/pingone/verify/v1/api/#verify-data-based-identity-verification) in the PingOne Verify API documentation.

* Added the ability to define a policy path if verification fails, but data collection and submission proceed.

  Learn more in the **Verification Failure Mode** table entry in [PingOne Verify IdP Adapter settings reference](pf_p1_verify_ik_p1_verify_idp_adapter_settings_reference.html).

* Updated dependencies to address a potential security vulnerability.

## PingOne Verify Integration Kit 2.3.1 - August 2025

* Added the ability to redirect users automatically when performing verification on a mobile device, letting the user complete document and selfie captures in the same tab instead of opening them in a new tab.

  Redirects simplify the verification process, especially for users with pop-up blockers. Learn more in the same device verification flow in [Overview of the verification flow](pf_p1_verify_ik_overview_of_the_verification_flow.html).

* Updated the velocity template designs that the PingOne Verify Integration Kit uses.

  To use the updated template files, make sure to follow the steps in [Deploying the integration files](pf_p1_verify_ik_deploying_the_integration_files.html) when upgrading to PingOne Verify Integration Kit 2.3.1.

## PingOne Verify Integration Kit 2.3 - February 2025

* Added support for biographic matching. Configure the expected names of incoming chain attributes to collect the actual user values during verification and send them to PingOne Verify.

  Learn more in the **First Name Chained Attribute** through **Date of Birth Chained Attribute** table entries in the [PingOne Verify IdP Adapter settings reference](pf_p1_verify_ik_p1_verify_idp_adapter_settings_reference.html). Learn more about biographic matching in [Types of verification](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_types_of_verification.html) in the PingOne Verify documentation.

  |   |                                                                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Currently, you must parse the biographic matching metadata to view results and decide how to proceed. Verify policy support for biographic matching results will be added in a future release. |

* Added the ability to configure a redirect URL and message. Learn more in the **Redirect URL** and **Redirect Message** table entries in the [PingOne Verify IdP Adapter settings reference](pf_p1_verify_ik_p1_verify_idp_adapter_settings_reference.html).

* Added the ability to provision a user during the password reset flow if **Provision User** is selected in the adapter configuration. Learn more about **Provision User** in the [PingOne Verify IdP Adapter settings reference](pf_p1_verify_ik_p1_verify_idp_adapter_settings_reference.html).

  |   |                                                                                                                               |
  | - | ----------------------------------------------------------------------------------------------------------------------------- |
  |   | Learn more about mitigating risk for password reset flows in the [Account recovery use case](pf_p1_verify_ik_use_cases.html). |

* Removed a deprecated endpoint, `verifyStatus`.

* Fixed an issue that caused a `Null Pointer Exception` when creating a new adapter instance if the PingOne environment didn't include the [PingOne Verify service](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_introduction.html).

  The PingOne environment must include at least one verify policy because you must select something in the **Verify Policy** list in the [adapter configuration](pf_p1_verify_ik_p1_verify_idp_adapter_settings_reference.html) before you can save your configuration. Learn more in [Verify policies](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_policies.html) in the PingOne Verify documentation.

* Improved the error messaging when a user fails a verification attempt and renamed the **Cancel** button **Retry** for clarification and alignment.

  To use the updated template files, make sure to follow the steps in [Deploying the integration files](pf_p1_verify_ik_deploying_the_integration_files.html) when upgrading to PingOne Verify Integration Kit 2.3.

## PingOne Verify Integration Kit 2.2.1 – August 2023

* The adapter now syncs its dependencies with PingFederate 11.3.

## PingOne Verify Integration Kit 2.2 – July 2023

* Added an adapter configuration option to reset a user's verification status for every sign-on attempt.

* Added support for password reset in the PingOne Verify IdP Adapter. To ensure maximum security, the password reset flow requires full verification for all users, even if they're already verified.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | For password reset and sign-on flows, a malicious user might try to reset the password of another account by using their own ID. To prevent this:1) Set up a comparison in the PingFederate policy to check if the identity verified matches the user's record.

  2) After the PingOne Verify Integration Kit succeeds, confirm that the first and last names of the verified ID match those in the directory for the username that was entered on the sign-on or forgot password page. |

* Fixed an issue where administrators had to map whether to block or bypass authentication for a user with a disabled verify status in **Service Unavailable Failure Mode** instead of **User Not Found Failure Mode**.

## PingOne Verify Integration Kit 2.1 – December 2022

* Added support for **facial comparison only** verify policy in the adapter.

* Added support for the verify policy.

* Added support for the PingOne Verify Mobile SDK version 2 with QR verification flows.

## PingOne Verify Integration Kit 2.0 – July 2022

* Added support for web authentication flow.

* Added `gender`, `issuingCountry`, `nationality`, and `weight` as core attributes.

* Added `selfie` and `metadata` as option attributes.

* Removed support for PingOne Verify Mobile SDK.

## PingOne Verify Integration Kit 1.1 – July 2021

* Added support for changes to PingOne Verify, including:

  * The adapter now gets the user's `verifyEnabledState` attribute when getting the verification result

  * Updated the list of core contract attributes to support changes to the structure of the `verifiedUserData` attribute

  * Added support for change to the flow behavior when the `verifyDocument` flag is off

  * Updated the core contract to support changes in PingOne Verify:

    | Change description          | Version 1.0          | Version 1.1         |
    | --------------------------- | -------------------- | ------------------- |
    | Attribute name change       | `verificationStatus` | `transactionStatus` |
    | Attribute name change       | `dateOfBirth`        | `birthDate`         |
    | Attribute name change/merge | `addressLine1`       | `addressStreet`     |
    | Attribute name change/merge | `addressLine2`       |                     |
    | Attribute name change       | `city`               | `addressCity`       |
    | Attribute name change       | `state`              | `addressState`      |
    | Attribute name change       | `postalCode`         | `addressZip`        |
    | Attribute name change       | `documentId`         | `idNumber`          |
    | New attribute               |                      | `idType`            |

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | You can find upgrade instructions in [Deploying the integration files](pf_p1_verify_ik_deploying_the_integration_files.html). |

## PingOne Verify Integration Kit 1.0 – January 2021

* Initial release.

* Added the ability to direct users to an identity verification app as part of a sign-on or registration flow.

* Added the ability to control which message pages (templates) are shown to the user.

* Added the ability to customize template messages using a language pack file.

* Added the ability to test the connection to PingOne Verify.

* Added a setting to automatically provision new users to PingOne.

* Added settings to control how the adapter handles sign-on and registration attempts when errors occur.

* Added support for the platform connection to PingOne introduced in PingFederate 10.2.

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html)

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

* Added settings for API connection and request timeouts.

* Added settings to override the PingFederate system-default proxy settings.

---

---
title: Changelog
description: The following is the change history for the PingOne Verify Integration Kit.
component: pingone
page_id: pingone:pingone_verify_integration_kit_11:pf_p1_verify_ik_changelog_11
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_verify_integration_kit_11/pf_p1_verify_ik_changelog_11.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
section_ids:
  pingone-verify-integration-kit-1-1-july-2021: PingOne Verify Integration Kit 1.1 – July 2021
  pingone-verify-integration-kit-1-0-january-2021: PingOne Verify Integration Kit 1.0 – January 2021
---

# Changelog

The following is the change history for the PingOne Verify Integration Kit.

## PingOne Verify Integration Kit 1.1 – July 2021

Added support for changes to PingOne Verify, including:

* The adapter now gets the user's `verifyEnabledState` attribute when getting the verification result

* Updated the list of core contract attributes to support changes to the structure of the `verifiedUserData` attribute

* Added support for change to the flow behavior when the `verifyDocument` flag is off

* Updated the core contract to support changes in PingOne Verify:

  | Change description          | Version 1.0          | Version 1.1         |
  | --------------------------- | -------------------- | ------------------- |
  | Attribute name change       | `verificationStatus` | `transactionStatus` |
  | Attribute name change       | `dateOfBirth`        | `birthDate`         |
  | Attribute name change/merge | `addressLine1`       | `addressStreet`     |
  | Attribute name change/merge | `addressLine2`       |                     |
  | Attribute name change       | `city`               | `addressCity`       |
  | Attribute name change       | `state`              | `addressState`      |
  | Attribute name change       | `postalCode`         | `addressZip`        |
  | Attribute name change       | `documentId`         | `idNumber`          |
  | New attribute               |                      | `idType`            |

|   |                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------- |
|   | For upgrade instructions, see [Deploying the integration files](pf_p1_verify_ik_deploying_the_integration_files_11.html). |

## PingOne Verify Integration Kit 1.0 – January 2021

* Initial release.

* Added the ability to direct users to an identity verification app as part of a sign-on or registration flow.

* Added the ability to control which message pages (templates) are shown to the user.

* Added the ability to customize template messages using a language pack file.

* Added the ability to test the connection to PingOne Verify.

* Added a setting to automatically provision new users to PingOne.

* Added settings to control how the adapter handles sign-on and registration attempts when errors occur.

* Added support for the platform connection to PingOne introduced in PingFederate 10.2.

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html)

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

* Added settings for API connection and request timeouts.

* Added settings to override the PingFederate system-default proxy settings.

---

---
title: CIBA prompt customizations
description: Client-initiated backchannel authentication (CIBA) involves prompting a user to accept or reject a request. You can customize the request prompt using pre-defined attributes or map complex custom attributes.
component: pingone
page_id: pingone:pingone_mfa_integration_kit:pf_p1_mfa_ik_ciba_prompt_customizations_4.0
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit/pf_p1_mfa_ik_ciba_prompt_customizations_4.0.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2024
section_ids:
  simple-prompt-customizations: Simple prompt customizations
  advanced-prompt-customizations: Advanced prompt customizations
---

# CIBA prompt customizations

Client-initiated backchannel authentication (CIBA) involves prompting a user to accept or reject a request. You can customize the request prompt using pre-defined attributes or map complex custom attributes.

## Simple prompt customizations

For simple, centralized customizations, you can modify the notification template that PingOne uses to generate the request prompt. Notification template customizations allow you to use the following:

* Static text

* A pre-defined set of attributes from the client request context

Simple prompt customizations require changes to the PingOne notification template only.

* Location: **PingOne console > Experiences > Notifications**.

You can find more descriptions and examples in [Simple CIBA prompt customizations](pf_p1_mfa_ik_simple_ciba_prompt_customizations_4.0.html).

## Advanced prompt customizations

If you need more advanced customizations in the request prompt, you can define custom attributes in PingFederate and pass them to PingOne.

The PingOne MFA CIBA Authenticator allows you to use the following:

* Static text

* Modified attributes from the client request context

* Contract attributes from the PingFederate CIBA request policy

* Messages from the PingFederate language-pack localization files

* Apache Velocity Template Language code to manipulate any of the above

Advanced prompt customizations require coordinated changes to all the following:

* The PingOne notification template

  * Location: **PingOne console > Experiences > Notifications**.

* The **PingOne Template Variables** table of the PingOne MFA CIBA Authenticator instance

  * Location: **PingFederate console > Authentication > OAuth > CIBA Authenticators > Your PingOne MFA CIBA Authenticator instance > Instance Configuration**.

* The **Extended Contract** tab of the PingOne MFA CIBA Authenticator instance

  * Location: **PingFederate console > Authentication > OAuth > CIBA Authenticators > Your PingOne MFA CIBA Authenticator instance > Instance Configuration**.

* The PingFederate CIBA request policy

  * Location: **PingFederate console > Applications > OAuth > CIBA Request Policies > Your CIBA request policy > Contract Fulfillment**.

You can find more descriptions and examples in [Advanced CIBA prompt customizations](pf_p1_mfa_ik_advanced_ciba_prompt_customizations_4.0.html).

---

---
title: CIBA prompt customizations
description: Client-initiated backchannel authentication (CIBA) involves prompting a user to accept or reject a request. You can customize the request prompt using pre-defined attributes or map complex custom attributes.
component: pingone
page_id: pingone:pingone_mfa_integration_kit_3.2:pf_p1_mfa_ik_ciba_prompt_customizations
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit_3.2/pf_p1_mfa_ik_ciba_prompt_customizations.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2024
section_ids:
  simple-prompt-customizations: Simple prompt customizations
  advanced-prompt-customizations: Advanced prompt customizations
---

# CIBA prompt customizations

Client-initiated backchannel authentication (CIBA) involves prompting a user to accept or reject a request. You can customize the request prompt using pre-defined attributes or map complex custom attributes.

## Simple prompt customizations

For simple, centralized customizations, you can modify the notification template that PingOne uses to generate the request prompt. Notification template customizations allow you to use the following:

* Static text

* A pre-defined set of attributes from the client request context

Simple prompt customizations require changes to the PingOne notification template only.

* Location: **PingOne console > Experiences > Notifications**.

You can find more descriptions and examples in [Simple CIBA prompt customizations](pf_p1_mfa_ik_simple_ciba_prompt_customizations.html).

## Advanced prompt customizations

If you need more advanced customizations in the request prompt, you can define custom attributes in PingFederate and pass them to PingOne.

The PingOne MFA CIBA Authenticator allows you to use the following:

* Static text

* Modified attributes from the client request context

* Contract attributes from the PingFederate CIBA request policy

* Messages from the PingFederate language-pack localization files

* Apache Velocity Template Language code to manipulate any of the above

Advanced prompt customizations require coordinated changes to all the following:

* The PingOne notification template

  * Location: **PingOne console > Experiences > Notifications**.

* The **PingOne Template Variables** table of the PingOne MFA CIBA Authenticator instance

  * Location: **PingFederate console > Authentication > OAuth > CIBA Authenticators > Your PingOne MFA CIBA Authenticator instance > Instance Configuration**.

* The **Extended Contract** tab of the PingOne MFA CIBA Authenticator instance

  * Location: **PingFederate console > Authentication > OAuth > CIBA Authenticators > Your PingOne MFA CIBA Authenticator instance > Instance Configuration**.

* The PingFederate CIBA request policy

  * Location: **PingFederate console > Applications > OAuth > CIBA Request Policies > Your CIBA request policy > Contract Fulfillment**.

You can find more descriptions and examples in [Advanced CIBA prompt customizations](pf_p1_mfa_ik_advanced_ciba_prompt_customizations.html).

---

---
title: CIBA request flow
description: When a client makes a Client Initiated Backchannel Authentication (CIBA) request to PingFederate, PingFederate can modify and add to the request information before sending it to PingOne MFA.
component: pingone
page_id: pingone:pingone_mfa_integration_kit:pf_p1_mfa_ik_ciba_request_flow_4.0
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit/pf_p1_mfa_ik_ciba_request_flow_4.0.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2024
---

# CIBA request flow

When a client makes a Client Initiated Backchannel Authentication (CIBA) request to PingFederate, PingFederate can modify and add to the request information before sending it to PingOne MFA.

The following steps are involved in conveying the CIBA request information from the client application to the request prompt that the user sees on their mobile device.

1. The client application sends a CIBA request to PingFederate that includes some request context attributes.

2. The CIBA request policy collects attributes from the client request and other attribute sources that you configure, such as a data store.

3. The PingOne MFA CIBA Authenticator parses the client request attributes. The authenticator also processes any custom attribute definitions, as described in [CIBA prompt customizations](pf_p1_mfa_ik_ciba_prompt_customizations_4.0.html).

4. The authenticator sends the attributes to PingOne along with information to identify which PingOne notification template to use for the user prompt.

5. PingOne uses the attributes from the PingOne MFA CIBA Authenticator to populate the variables in a customizable notification template.

6. PingOne sends the notification to the mobile app, which is built with the PingOne Mobile SDK.

7. The mobile app show the request prompt to the user to approve or deny.

---

---
title: CIBA request flow
description: When a client makes a Client Initiated Backchannel Authentication (CIBA) request to PingFederate, PingFederate can modify and add to the request information before sending it to PingOne MFA.
component: pingone
page_id: pingone:pingone_mfa_integration_kit_3.2:pf_p1_mfa_ik_ciba_request_flow
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit_3.2/pf_p1_mfa_ik_ciba_request_flow.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2024
---

# CIBA request flow

When a client makes a Client Initiated Backchannel Authentication (CIBA) request to PingFederate, PingFederate can modify and add to the request information before sending it to PingOne MFA.

The following steps are involved in conveying the CIBA request information from the client application to the request prompt that the user sees on their mobile device.

1. The client application sends a CIBA request to PingFederate that includes some request context attributes.

2. The CIBA request policy collects attributes from the client request and other attribute sources that you configure, such as a data store.

3. The PingOne MFA CIBA Authenticator parses the client request attributes. The authenticator also processes any custom attribute definitions, as described in [CIBA prompt customizations](pf_p1_mfa_ik_ciba_prompt_customizations.html).

4. The authenticator sends the attributes to PingOne along with information to identify which PingOne notification template to use for the user prompt.

5. PingOne uses the attributes from the PingOne MFA CIBA Authenticator to populate the variables in a customizable notification template.

6. PingOne sends the notification to the mobile app, which is built with the PingOne Mobile SDK.

7. The mobile app show the request prompt to the user to approve or deny.

---

---
title: CIBA setup
description: When a client application sends a Client Initiated Backchannel Authentication (CIBA) request to PingFederate, the PingOne MFA CIBA Authenticator allows PingFederate to initiate an out-of-band authentication request using PingOne MFA.
component: pingone
page_id: pingone:pingone_mfa_integration_kit:pf_p1_mfa_ik_ciba_setup_4.0
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit/pf_p1_mfa_ik_ciba_setup_4.0.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# CIBA setup

When a client application sends a Client Initiated Backchannel Authentication (CIBA) request to PingFederate, the PingOne MFA CIBA Authenticator allows PingFederate to initiate an out-of-band authentication request using PingOne MFA.

## About this task

By completing the steps below, you can show CIBA prompts on the mobile device that a user has paired with their PingOne MFA account.

For general information about CIBA, see [Client Initiated Backchannel Authentication (CIBA)](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ciba.html) in the PingFederate documentation. Note that the CIBA Authenticator mentioned on that page is different from the PingOne MFA CIBA Authenticator.

For detailed information about the following steps, see [CIBA request flow](pf_p1_mfa_ik_ciba_request_flow_4.0.html) and [CIBA prompt customizations](pf_p1_mfa_ik_ciba_prompt_customizations_4.0.html).

|   |                                                                                |
| - | ------------------------------------------------------------------------------ |
|   | The CIBA setup section is optional and independent from the MFA setup section. |

## Steps

1. In PingOne, complete the steps in [Creating a CIBA authentication policy in PingOne](pf_p1_mfa_ik_creating_a_ciba_authentication_policy_p1_4.0.html).

2. In PingFederate, complete the steps in [Configuring a CIBA authenticator instance](pf_p1_mfa_ik_configuring_a_ciba_authenticator_instance_4.0.html).

3. In PingFederate, create a CIBA request policy as shown in [Managing CIBA request policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_cibapoliciesmanagementtasklet_cibapoliciesmanagementstate.html) in the PingFederate documentation.

---

---
title: CIBA setup
description: When a client application sends a Client Initiated Backchannel Authentication (CIBA) request to PingFederate, the PingOne MFA CIBA Authenticator allows PingFederate to initiate an out-of-band authentication request using PingOne MFA.
component: pingone
page_id: pingone:pingone_mfa_integration_kit_3.2:pf_p1_mfa_ik_ciba_setup
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit_3.2/pf_p1_mfa_ik_ciba_setup.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# CIBA setup

When a client application sends a Client Initiated Backchannel Authentication (CIBA) request to PingFederate, the PingOne MFA CIBA Authenticator allows PingFederate to initiate an out-of-band authentication request using PingOne MFA.

## About this task

By completing the steps below, you can show CIBA prompts on the mobile device that a user has paired with their PingOne MFA account.

For general information about CIBA, see [Client Initiated Backchannel Authentication (CIBA)](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ciba.html) in the PingFederate documentation. Note that the CIBA Authenticator mentioned on that page is different from the PingOne MFA CIBA Authenticator.

For detailed information about the following steps, see [CIBA request flow](pf_p1_mfa_ik_ciba_request_flow.html) and [CIBA prompt customizations](pf_p1_mfa_ik_ciba_prompt_customizations.html).

|   |                                                                                |
| - | ------------------------------------------------------------------------------ |
|   | The CIBA setup section is optional and independent from the MFA setup section. |

## Steps

1. In PingOne, complete the steps in [Creating a CIBA authentication policy in PingOne](pf_p1_mfa_ik_creating_a_ciba_authentication_policy_p1.html).

2. In PingFederate, complete the steps in [Configuring a CIBA authenticator instance](pf_p1_mfa_ik_configuring_a_ciba_authenticator_instance.html).

3. In PingFederate, create a CIBA request policy as shown in [Managing CIBA request policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_cibapoliciesmanagementtasklet_cibapoliciesmanagementstate.html) in the PingFederate documentation.

---

---
title: Comparison of FOS vs. Direct MFA API flows
description: In PingOne MFA Integration Kit version 4.0, the PingOne MFA IdP Adapter migrates from integrating with PingOne via the authentication policy in the Flow Orchestration Service (FOS), used in previous versions, to direct MFA Device Authentication APIs.
component: pingone
page_id: pingone:pingone_mfa_integration_kit:pf_p1_mfa_ik_overview_of_the_sso_flow_comparison_4.0
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit/pf_p1_mfa_ik_overview_of_the_sso_flow_comparison_4.0.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2026
section_ids:
  flow-changes: Flow changes
  setup-and-migration-from-version-3-2: Setup and migration from version 3.2
  core-contract-and-attribute-changes: Core contract and attribute changes
  mfa-policy-for-authentication: MFA Policy for Authentication
  user-not-found-failure-mode: User Not Found Failure Mode
  one-time-device-display-mode: One-Time Device Display Mode
  user-agent-header-format: User-Agent header format
  migrating-configuration-from-the-pingone-authentication-policy: Migrating configuration from the PingOne Authentication Policy
  adapter-configuration-changelog: Adapter configuration changelog
  added_or_updated_fields_table: Added or updated fields
  removed-or-changed-fields: Removed or changed fields
  authentication-initiation: Authentication initiation
  attribute-and-claim-mapping: Attribute and claim mapping
  removed-tokens: Removed tokens
  new-core-contract-attributes: New core contract attributes
  parameter-mapping: Parameter mapping
---

# Comparison of FOS vs. Direct MFA API flows

In PingOne MFA Integration Kit version 4.0, the PingOne MFA IdP Adapter migrates from integrating with PingOne via the authentication policy in the Flow Orchestration Service (FOS), used in previous versions, to direct MFA Device Authentication APIs.

## Flow changes

This table compares the legacy FOS-based orchestration used in earlier versions with the direct API architecture introduced in version 4.0.

| Capability           | Deprecated FOS-Based Flow                         | New Direct MFA API Flow                                              |
| -------------------- | ------------------------------------------------- | -------------------------------------------------------------------- |
| **Orchestration**    | Managed by FOS via `/as/authorize`.               | Managed directly by the MFA Adapter.                                 |
| **API Endpoint**     | Invokes OIDC-based Flow APIs.                     | Invokes `/deviceAuthentications` service APIs.                       |
| **State Management** | Handled internally by FOS.                        | Managed by the MFA Adapter across API calls.                         |
| **Token Handling**   | Returns OIDC tokens (`access_token`, `id_token`). | Returns specific attributes (device ID, enrollment status) directly. |
| **Session Context**  | Relies on PingOne OIDC session tracking.          | Uses PingFederate as the source of truth for session information.    |

## Setup and migration from version 3.2

Upgrading to version 4.0 requires moving decision logic from the authentication policy (FOS) into the PingFederate environment.

### Core contract and attribute changes

The `id_token` and `access_token` core contracts have been removed. If existing policy rules reference these attributes, they must be updated.

For the `p1.enrollment` attribute source, do one of the following:

* Update the expression value to `pingone.mfa.enrollment`.

  Or

* Remove the `p1.enrollment` attribute entirely and use the core contract attribute `pingone.mfa.enrollment`, ensuring it is mapped in all relevant locations.

### MFA Policy for Authentication

The **MFA Policy for Authentication** field replaces the **PingOne Authentication Policy** text field. If you are upgrading from version 3.2, you must manually select the appropriate MFA policy from this list.

### User Not Found Failure Mode

This setting now exclusively covers users who do not exist in the directory. It no longer applies to disabled users or those with the MFA service disabled.

For those cases, use the new settings available in the MFA Policy under **User Access Configuration**:

* **Block authentication when user status is disabled**

* **Block authentication when user's MFA is disabled**

|   |                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When **Block authentication when user's MFA is disabled** is enabled, blocked authentication attempts now return `com.pingidentity.pingone.mfa_bypassed_user_mfa_disabled` instead of `com.pingidentity.pingone.mfa_bypassed_invalid_user`, providing more accurate status reporting. |

### One-Time Device Display Mode

The default display mode is now **Standalone**. If your previous adapter instance had **One-Time Device Display Mode** enabled, you must manually select **With Paired Devices**.

### User-Agent header format

The `User-Agent` header format has changed from `PingFederate` to `PingFederate/{version} PingOne-MFA-Integration-Kit/{version}`.

### Migrating configuration from the PingOne Authentication Policy

* **Risk and Protect conditions:** Conditions such as IP reputation, geo-velocity, and anonymous network detection are no longer handled by the MFA Adapter. You must now configure these in the **PingFederate Authentication Policy** using the **PingOne MFA Protect Integration Kit**.

* **NONE OR INCOMPATIBLE METHODS:** If configured, migrate this to the **No Device Failure Mode** field in the MFA Adapter.

  |   |                                                                                                                                                        |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | Change in behavior: **No Device Failure Mode** covers only users with zero registered devices. Users with incompatible devices are treated as BLOCKED. |

* **Last Sign-on Older Than:** If configured, migrate this to PingFederate native session management. The MFA Adapter does not handle sessions.

* **Accessing from an Out-of-Range IP Address:** If configured, migrate this to the **MFA for Accessing from IP out of range** field in the MFA Adapter.

* **Being a Member of Any of These Populations:** If configured, migrate this to the **MFA by User Population** field in the MFA Adapter.

* **User Attributes:** If configured, migrate this to the **MFA for User Attributes** table in the MFA Adapter.

## Adapter configuration changelog

The architectural shift to direct APIs results in several changes to the adapter's configuration UI.

### Added or updated fields

| Field                                      | Description                                                                             |
| ------------------------------------------ | --------------------------------------------------------------------------------------- |
| **MFA Policy for Authentication**          | Replaces the legacy Authentication Policy text field with a dynamic list.               |
| **No Device Failure Mode**                 | New setting to Block or Bypass authentication when no usable MFA methods exist.         |
| **MFA by User Population**                 | New text field to trigger MFA based on PingOne MFA population membership.               |
| **MFA for Accessing from IP out of range** | New field for CIDR-based MFA enforcement within the adapter.                            |
| **MFA for User Attributes**                | A new table-based configuration to trigger MFA based on specific user attribute values. |

### Removed or changed fields

* **JWKS Cache Duration:** Removed. Direct API calls eliminate the need for JWKS endpoint polling.

* **User Not Found Failure Mode:** Changed behavior. This now only applies when a user does not exist in the directory; it no longer covers disabled users or disabled MFA service states.

* **CIBA Authenticator:** The change to the **MFA Policy for Authentication** list also applies to all CIBA authenticator configurations.

## Authentication initiation

In earlier versions, the MFA Adapter initiated authentication using the OAuth Authorization API (`/as/authorize`), which triggered FOS to coordinate multiple PingOne MFA calls.

In version 4.0, OAuth authorization is decoupled from MFA execution. The MFA Adapter invokes the **PingOne MFA Device Authentication APIs** directly as a discrete step within the PingFederate authentication policy.

## Attribute and claim mapping

With the removal of FOS, the adapter no longer receives or returns synthetic OIDC tokens. Instead, the adapter receives raw metadata from the MFA service and injects it into the PingFederate attribute map.

### Removed tokens

To simplify security semantics and avoid unnecessary key management, the following attributes are no longer returned in the `authnAdapterResponse.attributeMap`:

* **access\_token**

* **id\_token**

|   |                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If existing PingFederate policy rules or OGNL expressions rely on `id_token`, they must be updated to use the new core contract attributes below. |

### New core contract attributes

The required claims for downstream applications are now returned directly as adapter attributes:

* `pingone.mfa.device.id`

* `pingone.mfa.enrollment`

## Parameter mapping

The transition to direct APIs changes how specific parameters are passed from PingFederate to PingOne MFA.

* **MFA Policy:** Parameters previously passed as `acr_values` are now mapped to `policy.id`.

Learn more about specific field configurations in [PingOne MFA IdP Adapter settings reference](pf-p1-mfa-ik-p1-mfa-idp-adapter-settings-reference_4.0.html).

---

---
title: Configuring a channel
description: To complete your PingOne provisioning configuration, map the necessary attributes in your channel configuration.
component: pingone
page_id: pingone:pingone_integration_kit:pf_p1_ik_configuring_a_channel
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_integration_kit/pf_p1_ik_configuring_a_channel.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Configuring a channel

To complete your PingOne provisioning configuration, map the necessary attributes in your channel configuration.

## About this task

Learn more about the following steps in [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation.

## Steps

1. On the **Manage Channels** tab, click **Create**.

2. On the **Channel Info** tab, in the **Channel Name** field, enter a unique name, then click **Next**.

3. On the **Source** tab, in the **Active Data Store** list, select the datastore that you configured in [Supported attributes reference](pf_p1_ik_supported_attributes_reference.html), then click **Next**.

4. On the **Source Settings** tab, click **Next**.

5. On the **Source Location** tab, in the **Base DN** field, enter a base DN that includes the users that you want to provision.

6. In the **Users** section, complete the **Group DN** or **Filter** fields to identify the users that you want to provision, then click **Next**.

7. On the **Attribute Mapping** tab, map the required attributes.

   You can find a list of attributes in the [Supported attributes reference](pf_p1_ik_supported_attributes_reference.html). Learn more about attribute mapping in [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html) in the PingFederate documentation.

   |   |                                                                                                                                                                                                                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can also map custom attributes after adding them. Learn more about adding custom attributes in [Adding user attributes](https://docs.pingidentity.com/pingone/directory/p1_adduserattributes.html) and the [PingOne Platform API Reference](https://apidocs.pingidentity.com/pingone/platform/v1/api/#schemas). |

   1. On the **Username** row, click **Edit**.

   2. On the `Username` **Attribute Mapping** tab, in the **Root Object Class** and **Attribute** lists, select the attribute in your datastore that matches the `Username` attribute in PingOne.

      Learn more in [User and group management](pf_p1_ik_user_and_group_management.html).

   3. Click **Add Attribute**, and then click **Done**.

   4. On the **Population ID** row, click **Edit**.

   5. On the **Population ID** mapping tab, do one of the following:

      ### Choose from:

      * Map a static population ID:

        1. In the **Default Value** list, select the PingOne population that you want to target, then click **Done**.

           |   |                                                                                                                                                                                                                              |
           | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
           |   | The **Default Value** list is only available if you entered the correct client credentials from [Connecting PingFederate to PingOne](pf_p1_ik_connecting_pf_to_p1.html). The provisioner will populate the list accordingly. |

      * Map a dynamic population ID.

        |   |                                                                                                                                                                                 |
        | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | Learn more about getting the ID for a population in [Viewing populations](https://docs.pingidentity.com/pingone/directory/p1_viewpopulation.html) in the PingOne documentation. |

        1. In the **Root Object Class** and **Attribute** lists, select the user attribute in your datastore that contains the population ID.

        2. Click **Add Attribute**, and then click **Done**.

   6. If you want to manage users and devices for the PingOne MFA service, map any combination of the `MFA Device Email` and `MFA Device SMS` attributes, and map or assign the `MFA Enabled` attribute.

      Learn more in [Supported attributes reference](pf_p1_ik_supported_attributes_reference.html).

   7. Click **Next**.

8. On the **Activation and Summary** tab, on the **Channel Status** row, click **Active**, then click **Done**.

9. On the **Manage Channels** tab, click **Done**.

---

---
title: Configuring a CIBA authenticator instance
description: Configure the PingOne MFA CIBA Authenticator to determine how PingFederate communicates with PingOne MFA for client-initiated backchannel authentication (CIBA) requests.
component: pingone
page_id: pingone:pingone_mfa_integration_kit:pf_p1_mfa_ik_configuring_a_ciba_authenticator_instance_4.0
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit/pf_p1_mfa_ik_configuring_a_ciba_authenticator_instance_4.0.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 18, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a CIBA authenticator instance

Configure the PingOne MFA CIBA Authenticator to determine how PingFederate communicates with PingOne MFA for client-initiated backchannel authentication (CIBA) *(tooltip: \<div class="paragraph">
\<p>An extension to OpenID Connect defining a new OAuth grant type where user consent can be requested and granted through an out-of-band authentication flow. CIBA uses direct relying party to OpenID provider communication without redirects through the user's browser.\</p>
\</div>)* requests.

## About this task

These steps are only required if you want to enable CIBA support. Learn more in [CIBA request flow](pf_p1_mfa_ik_ciba_request_flow_4.0.html).

## Steps

1. In the PingFederate administrative console, go to **Authentication > OAuth > CIBA Authenticators** and click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the authenticator instance.

   2. In the **Instance ID** field, enter a unique identifier for the authenticator instance.

   3. In the **Type** list, select **PingOne MFA CIBA Authenticator**. Click **Next**.

3. (Optional) If you want to use the advanced prompt customizations described in [CIBA prompt customizations](pf_p1_mfa_ik_ciba_prompt_customizations_4.0.html), on the **Instance Configuration** tab, in the **PingOne Template Variables** section, map dynamic values to the variables in your PingOne notification template.

   You can find more details and examples in [Advanced CIBA prompt customizations](pf_p1_mfa_ik_advanced_ciba_prompt_customizations_4.0.html).

   1. Click **Add a new row to 'PingOne Template Variables'**.

   2. In the **PingOne Template Variable Name** field, enter the name of a variable in your PingOne notification template.

   3. In the **PingOne Template Variable Value** field, define the value based on the examples shown in [Advanced CIBA prompt customizations](pf_p1_mfa_ik_advanced_ciba_prompt_customizations_4.0.html).

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a - d.

4. On the **Instance Configuration** tab, configure the authenticator instance by referring to [PingOne MFA CIBA Authenticator settings reference](pf_p1_mfa_ik_p1_mfa_ciba_authenticator_settings_reference_4.0.html). Click **Next**.

5. On the **Actions** tab, test your connection to PingOne MFA. Resolve any issues that are reported, and then click **Next**.

6. On the **Extended Contract** tab, add any attributes that you used in the **PingOne Template Variable Value** fields on the **Instance Configuration** tab, then click **Next**.

   The **Extended Contract** tab acts as an input that defines which attributes are available to use in the **PingOne Template Variable Value** fields. The `subject` attribute is always included. Learn more in [Advanced CIBA prompt customizations](pf_p1_mfa_ik_advanced_ciba_prompt_customizations_4.0.html).

7. On the **Summary** tab, check your configuration, then click **Save**.

---

---
title: Configuring a CIBA authenticator instance
description: Configure the PingOne MFA CIBA Authenticator to determine how PingFederate communicates with PingOne MFA for client-initiated backchannel authentication (CIBA) requests.
component: pingone
page_id: pingone:pingone_mfa_integration_kit_3.2:pf_p1_mfa_ik_configuring_a_ciba_authenticator_instance
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit_3.2/pf_p1_mfa_ik_configuring_a_ciba_authenticator_instance.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 18, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a CIBA authenticator instance

Configure the PingOne MFA CIBA Authenticator to determine how PingFederate communicates with PingOne MFA for client-initiated backchannel authentication (CIBA) *(tooltip: \<div class="paragraph">
\<p>An extension to OpenID Connect defining a new OAuth grant type where user consent can be requested and granted through an out-of-band authentication flow. CIBA uses direct relying party to OpenID provider communication without redirects through the user's browser.\</p>
\</div>)* requests.

## About this task

These steps are only required if you want to enable CIBA support. Learn more in [CIBA request flow](pf_p1_mfa_ik_ciba_request_flow.html).

## Steps

1. In the PingFederate administrative console, go to **Authentication > OAuth > CIBA Authenticators** and click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the authenticator instance.

   2. In the **Instance ID** field, enter a unique identifier for the authenticator instance.

   3. In the **Type** list, select **PingOne MFA CIBA Authenticator**. Click **Next**.

3. (Optional) If you want to use the advanced prompt customizations described in [CIBA prompt customizations](pf_p1_mfa_ik_ciba_prompt_customizations.html), on the **Instance Configuration** tab, in the **PingOne Template Variables** section, map dynamic values to the variables in your PingOne notification template.

   You can find more details and examples in [Advanced CIBA prompt customizations](pf_p1_mfa_ik_advanced_ciba_prompt_customizations.html).

   1. Click **Add a new row to 'PingOne Template Variables'**.

   2. In the **PingOne Template Variable Name** field, enter the name of a variable in your PingOne notification template.

   3. In the **PingOne Template Variable Value** field, define the value based on the examples shown in [Advanced CIBA prompt customizations](pf_p1_mfa_ik_advanced_ciba_prompt_customizations.html).

   4. In the **Action** column, click **Update**.

   5. To add more attributes, repeat steps a - d.

4. On the **Instance Configuration** tab, configure the authenticator instance by referring to [PingOne MFA CIBA Authenticator settings reference](pf_p1_mfa_ik_p1_mfa_ciba_authenticator_settings_reference.html). Click **Next**.

5. On the **Actions** tab, test your connection to PingOne MFA. Resolve any issues that are reported, and then click **Next**.

6. On the **Extended Contract** tab, add any attributes that you used in the **PingOne Template Variable Value** fields on the **Instance Configuration** tab, then click **Next**.

   The **Extended Contract** tab acts as an input that defines which attributes are available to use in the **PingOne Template Variable Value** fields. The `subject` attribute is always included. Learn more in [Advanced CIBA prompt customizations](pf_p1_mfa_ik_advanced_ciba_prompt_customizations.html).

7. On the **Summary** tab, check your configuration, then click **Save**.

---

---
title: Configuring a provider instance
description: The PingOne Protect provider works similarly to CAPTCHA providers and can detect bot activity before the password credential validator (PCV) is triggered.
component: pingone
page_id: pingone:pingone_protect_integration_kit:pf_p1_protect_ik_configuring_a_provider_instance
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_protect_integration_kit/pf_p1_protect_ik_configuring_a_provider_instance.html
llms_txt: https://docs.pingidentity.com/integrations/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  direct-changes-to-javascript-files: Direct changes to Javascript files
  provider-settings-reference: Provider settings reference
---

# Configuring a provider instance

The PingOne Protect provider works similarly to CAPTCHA providers and can detect bot activity before the password credential validator (PCV) is triggered.

## About this task

|   |                                                                                    |
| - | ---------------------------------------------------------------------------------- |
|   | A provider instance isn't required, but having one is necessary for bot detection. |

## Steps

1. In the PingFederate administrative console, go to **System > External Systems > CAPTCHA and Risk Providers**. Click **Create New Instance**.

2. On the **Type** tab, set the basic provider instance attributes:

   1. In the **Instance Name** field, enter a name for the provider instance.

   2. In the **Instance ID** field, enter a unique identifier for the provider instance.

   3. In the **Type** list, select **PingOne Protect Provider**. Click **Next**.

3. On the **Instance Configuration** tab:

   1. In the **PingOne Environment** field, select your **PingOne Connection** and **Environment Name**.

   2. In the **Field Value** list for **PingOne Risk Policy** section, select the risk policy to use.

   3. Click **Show Advanced Fields**.

   4. To allow the adapter to evaluate the risk rather than the provider, clear the **Enable Risk Evaluation** check box.

   5. Continue configuring the provider instance using the settings listed in [Provider settings reference](#provider-settings-reference).

   6. Click **Next**.

4. On the **Summary** tab, review the settings for the provider and click **Save**.

5. Enable the HTML Form adapter to use the provider:

   1. Go to **Authentication > Integration > IdP Adapters**. Select your HTML Form IdP Adapter from the list.

   2. On the **IdP Adapter** tab, click **Show Advanced Fields**.

   3. In the **Risk Provider** list, select your PingOne Protect provider instance.

   4. Select one or more of the following check boxes.

      | Check box                      | Description                                                                            |
      | ------------------------------ | -------------------------------------------------------------------------------------- |
      | **Risk for authentication**    | Enable for the login form to prevent automated attacks                                 |
      | **Risk for password change**   | Enable for the password change form to prevent automated attacks                       |
      | **Risk for password reset**    | Enable for the password reset and account unlock features to prevent automated attacks |
      | **Risk for username recovery** | Enable for the username recovery features to prevent automated attacks                 |

6. **Optional:** Set the device profile settings for the PingOne Protect adapter:

   1. Go to **Authentication > Integration > IdP Adapters**.

   2. Select your PingOne Protect IdP adapter from the list.

   3. On the **IdP Adapter** tab, click **Show Advanced Fields**.

   4. **Optional:** Enable **Include Device Dynamic Profile**.

   When enabled, the adapter will load the device profiling page if it hasn't already received the device profile payload from the provider.

## Direct changes to Javascript files

In addition to the configuration in the PingFederate administrative console, you must make the following change directly to the relevant Javascript file if you want the device data in the SDK payload to be provided as a signed JWT.

* Open the file `<installation directory>\server\default\conf\template\assets\scripts\captcha\signals.js`.

* Add this line: `universalDeviceIdentification: true`

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | The option of using a signed JWT was introduced in version 1.0.4 of the integration kit. |

## Provider settings reference

**Standard fields**

| Field                   | Value                         | Description                                                                                                                                                                            |
| ----------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PingOne Environment** | *\<PingOne Connection>*       | Your PingOne Environment. Create connections in **System > External Systems > PingOne Connections**.This field is blank by default.                                                    |
| **PingOne Risk Policy** | *\<PingOne Risk Policy Name>* | The risk policy used by PingOne for the risk evaluation. Overrides the environment and global default policy selections. This list is populated when you select a PingOne Environment. |

**Advanced fields**

| Field                                      | Value                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Use Targeted Policies**                  | * **Enabled**

* **Disabled**                                                                                                                           | When enabled, PingFederate uses the targeted risk policies that have been defined for the environment, rather than using a specific risk policy.&#xA;&#xA;If you select the Use Targeted Policies checkbox, the targeted policies will be used even if a specific risk policy is currently selected from the PingOne Risk Policy list.                                                                                                                     |
| **Password Encryption**                    | - **SHA-256**

- **SHA-384**

- **Disable**                                                                                                             | For improved detection of bots and brute force attacks, use the **Password Encryption** option by selecting one of the SHA-2 hash functions. When this option is enabled, part of the password is hashed and passed to PingOne Protect.                                                                                                                                                                                                                    |
| **Follow Recommended Action**              | * **Enabled**

* **Disabled**                                                                                                                           | In certain situations, the response from PingOne Protect includes not just an overall risk level but also a "recommended action", for example, BOT\_MITIGATION or AITM MITIGATION. These recommended actions are passed forward and you can configure the PingFederate policy to act upon the recommendation. Enable this option if you want the provider to automatically stop the transaction if the response includes one of these recommended actions. |
| **Failure Mode**                           | - **Continue with fallback policy decision**

- **Fail**                                                                                                | Use this option to specify how to proceed if PingOne Protect is unavailable or an error occurs: fail the user's sign-on attempt or continue with a pre-determined policy decision (set with **Fallback Policy Decision Value**).                                                                                                                                                                                                                           |
| **Fallback Policy Decision Value**         | * **LOW**

* **MEDIUM** (default)

* **HIGH**

* **unknown**                                                                                            | If you set **Failure Mode** to **Continue with fallback policy decision**, use the **Fallback Policy Decision Value** field to enter the risk result to use if PingOne Protect is unavailable or an error occurs ("LOW", "MEDIUM", "HIGH", or "unknown") .                                                                                                                                                                                                 |
| **API Request Timeout**                    | `2000` (default)                                                                                                                                        | The amount of time in milliseconds that PingFederate allows when establishing a connection with PingOne Protect or waiting for a response to a request. A value of `0` disables the timeout.                                                                                                                                                                                                                                                               |
| **Proxy Settings**                         | - **No Proxy**

- **System Defaults** (default)

- **Custom**                                                                                           | To use a proxy for outbound HTTP requests, set **Proxy Settings** to **System Defaults** or set the value to **Custom** to specify a custom proxy host and port.                                                                                                                                                                                                                                                                                           |
| **Custom Proxy Host**                      | *\<Proxy server host>*                                                                                                                                  | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                             |
| **Custom Proxy Port**                      | *\<Proxy server port>*                                                                                                                                  | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                  |
| **Custom Connection Pool**                 | `50` (default)                                                                                                                                          | The number of connections to PingOne Protect. Can be between `25` and `200`. Recommended that the number be left at the default value.                                                                                                                                                                                                                                                                                                                     |
| **Collect PingID Device Trust Attributes** | * **Enabled**

* **Disabled**                                                                                                                           | When enabled, the Protect (Signals) SDK collects attributes from the PingID Device Trust Agent and sends them to PingOne Protect.                                                                                                                                                                                                                                                                                                                          |
| **PingID Device Trust Agent Port**         | *\<Port number>*                                                                                                                                        | The port number to use when connecting to the PingID Device Trust Agent. If left blank, the default port (9400) is used.                                                                                                                                                                                                                                                                                                                                   |
| **PingID Device Trust Agent Timeout**      | *\<Number of milliseconds>*                                                                                                                             | The time, in milliseconds, that PingFederate allows for establishing a connection with the PingID Device Trust Agent. Value must be between 200 and 10,000. If left blank, the value used is the value that was set in the Protect (Signals) SDK.                                                                                                                                                                                                          |
| **Browser-based Location**                 | - **Don't get location (default)**

- **Get location - consent window shown by Protect Provider**

- **Get location - consent window shown separately** | This option instructs the Protect (Signals) SDK to include the browser-based location if the user consents to the inclusion of this information. Select **Get location - consent window shown by Protect Provider** if you want PingFederate to trigger the consent window. Select **Get location - consent window shown separately** if you want one of your own pages to trigger the consent window.                                                     |