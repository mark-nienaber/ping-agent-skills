---
title: Adding a connector
description: Add a new connector to enable new capabilities for your flows.
component: davinci
page_id: davinci:connectors:davinci_adding_a_connector
canonical_url: https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 15, 2024
section_ids:
  steps: Steps
---

# Adding a connector

Add a new connector to enable new capabilities for your flows.

## Steps

1. Click the **Connectors** tab.

2. Click **Add Connector**.

   The list of available connectors is displayed. The list is divided into three sections:

   * Core Connectors (Basic flow components and standards-based integrations)

   * Ping Identity Connectors (Ping Identity products)

   * Service Connectors (Third-party platforms and services)

3. Find the connector you want to add and click the **[icon: plus, set=fa]**icon.

   The new connector modal opens.

4. In the **Name** field, enter a name for the new connector.

5. Click **Create**.

6. Find the newly-created connector in the list of your connectors and click **... > Edit**.

7. Update the connector's properties.

   Each connector has different properties. See the connector's reference documentation for more information about required and optional properties.

8. Click **Apply**.

---

---
title: Cloning a connector
description: Clone an existing connector to create a new connector with the same settings.
component: davinci
page_id: davinci:connectors:davinci_cloning_a_connection
canonical_url: https://docs.pingidentity.com/davinci/connectors/davinci_cloning_a_connection.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2024
section_ids:
  steps: Steps
---

# Cloning a connector

Clone an existing connector to create a new connector with the same settings.

## Steps

1. Click the **Connectors** tab.

2. Find the connector and click **... > Clone**.

   A new connector is created with the same type and settings as the original, with a suffix indicating that it was cloned.

3. (Optional) Edit the new connector as described in [Editing a connector](davinci_editing_a_connection.html).

---

---
title: Connector types
description: Ping Identity offers a variety of connector types to help meet specific needs when building user experiences in PingOne DaVinci.
component: davinci
page_id: davinci:connectors:davinci_connector_types
canonical_url: https://docs.pingidentity.com/davinci/connectors/davinci_connector_types.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 21, 2025
---

# Connector types

Ping Identity offers a variety of connector types to help meet specific needs when building user experiences in PingOne DaVinci.

Flow templates in the [Ping Identity Marketplace](https://marketplace.pingone.com/browse?products=davinci\&contentType=davinciConnectors) provide premade solutions for common DaVinci use cases that you can modify or use as examples for orchestration flows. Learn more in [Using DaVinci flow templates](../flows/davinci_using_davinci_flow_templates.html).

The following table lists and explains the different connector types:

| Connector type                                          | Description                                                                                        |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| [Core connectors](davinci_core_connectors.html)         | Provide the foundation for your DaVinci flows by performing basic functions.                       |
| [Ping connectors](davinci_ping_connectors.html)         | Help you integrate other Ping Identity products and features into your DaVinci flows.              |
| [Service connectors](davinci_service_connectors.html)   | Help you integrate flows with other products and services that your organization is already using. |
| [Use case connectors](davinci_use_case_connectors.html) | Eliminate the need for complex subflows by consolidating common use cases into a single node.      |

---

---
title: Connectors
description: Connectors form the building blocks for flows. They provide logic, user interfaces, and connect DaVinci with other services from Ping Identity and third-party providers.
component: davinci
page_id: davinci:connectors:davinci_connections
canonical_url: https://docs.pingidentity.com/davinci/connectors/davinci_connections.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2024
section_ids:
  finding-connectors: Finding connectors
---

# Connectors

Connectors form the building blocks for flows. They provide logic, user interfaces, and connect DaVinci with other services from Ping Identity and third-party providers.

Each connector has its own configuration. Third-party service connectors, for example, let you define connection information for the tenant. This allows you build your flows quickly without having to re-enter basic information for every step of your flow.

In most cases, you only need one instance of a given connector. However, if you have more than one tenant with a particular third-party service (for test and production, for example), you can add the same connector multiple times and configure them differently. When building your flow, you can then choose the connector that represents the tenant you want to use for that step of the flow. All connectors are available in all flows, and you can mix and match as needed.

Connectors typically provide several capabilities that represent a specific action to take in the flow. For example, the Salesforce connector stores information about a tenant and includes capabilities for creating, reading, and updating users in that tenant. The Functions connector doesn't have any configuration itself, but it contains a variety of similar capabilities that branch the flow by comparing values. To add a step to your flow, you select the connector instance, then select the capability that you want to use.

Each flow that uses a specific instance of a connector respects changes to that connector's configuration. For example, if you update your production "Salesforce - Production" connector to use a new environment ID, every node that use that connector in every flow will use the new tenant information. Nodes that use your "Salesforce - Test" connector will not be affected.

## Finding connectors

Every connector requires specific information during configuration and provides a unique set of capabilities. See the [Core connectors](davinci_core_connectors.html) documentation and the [Integration Directory](https://marketplace.pingone.com/browse?products=davinci) for a list of connectors and their capabilities.

---

---
title: Core connectors
description: Core connectors provide the foundation for your DaVinci flows by performing basic functions.
component: davinci
page_id: davinci:connectors:davinci_core_connectors
canonical_url: https://docs.pingidentity.com/davinci/connectors/davinci_core_connectors.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 22, 2024
---

# Core connectors

Core connectors provide the foundation for your DaVinci flows by performing basic functions.

For other connector types, you can search the complete list of connectors in the [Ping Identity Marketplace](https://marketplace.pingone.com/home).

The following table lists and describes the core connectors and provides links to the related documentation.

| Core connector                                                                               | Description                                                                                         |
| -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [Challenge](https://docs.pingidentity.com/connectors/challenge_connector.html)               | Handle asynchronous events by pausing or continuing a flow based on a transaction status.           |
| [Code Snippet](https://docs.pingidentity.com/connectors/code_snippet_connector.html)         | Create custom JavaScript code that you can reuse in any flow.                                       |
| [Cookie](https://docs.pingidentity.com/connectors/cookie_connector.html)                     | Set and retrieve session cookies.                                                                   |
| [Device Policy](https://docs.pingidentity.com/connectors/device_policy_connector.html)       | Check the user agent, browser information, and operating system version.                            |
| [Error Message](https://docs.pingidentity.com/connectors/error_message_connector.html)       | Show customizable error messages.                                                                   |
| [FingerprintJS](https://docs.pingidentity.com/connectors/fingerprintjs_connector.html)       | Create a unique visitor ID based on browser attributes for use in fraud and analytics.              |
| [Flow Analytics](https://docs.pingidentity.com/connectors/flow_analytics_connector.html)     | Log details about flow outcomes to be used in flow analytics.                                       |
| [Flow Conductor](https://docs.pingidentity.com/connectors/flow_conductor_connector.html)     | Handle events in external systems and link to subflows.                                             |
| [Form Connector](https://docs.pingidentity.com/connectors/form_connector.html)               | Include branded PingOne forms and messages in your flow.                                            |
| [Functions](https://docs.pingidentity.com/connectors/functions_connector.html)               | Branch your flow using logical conditions (A > B) or based on the result of custom JavaScript code. |
| [HTTP](https://docs.pingidentity.com/connectors/http_connector.html)                         | Create forms and custom HTML pages or make REST API calls.                                          |
| [LDAP](https://docs.pingidentity.com/connectors/ldap_connector.html)                         | Gain access to entries in an LDAP directory to be used in your flow.                                |
| [Location Policy](https://docs.pingidentity.com/connectors/location_policy_connector.html)   | Check a user's IP and geographic location.                                                          |
| [OIDC & OAuth IdP](https://docs.pingidentity.com/connectors/oidc_oauth_idp_connector.html)   | Authenticate users with OpenID or OAuth, get user info, and create access tokens.                   |
| [SAML IdP Connector](https://docs.pingidentity.com/connectors/saml_connector.html)           | Authenticate users with a SAML IdP-based identity provider in your DaVinci flow.                    |
| [Screen](https://docs.pingidentity.com/connectors/screen_connector.html)                     | Display forms and customized UI to retrieve information from a user or show flow progress.          |
| [String](https://docs.pingidentity.com/connectors/string_connector.html)                     | Create and transform string variables.                                                              |
| [Teleport](https://docs.pingidentity.com/connectors/teleport_connector.html)                 | Visually organize and subdivide a flow within the same flow canvas.                                 |
| [Token Management](https://docs.pingidentity.com/connectors/token_management_connector.html) | Create and read JWT tokens and manage OIDC redirects                                                |
| [Variable](https://docs.pingidentity.com/connectors/variable_connector.html)                 | Store and retrieve flow and user attributes as variables.                                           |

---

---
title: Deleting a connector
description: Delete a connector to permanently remove it.
component: davinci
page_id: davinci:connectors:davinci_deleting_a_connection
canonical_url: https://docs.pingidentity.com/davinci/connectors/davinci_deleting_a_connection.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deleting a connector

Delete a connector to permanently remove it.

## About this task

|   |                                                                                     |
| - | ----------------------------------------------------------------------------------- |
|   | Verify that the connector is not being used in any active flows before deleting it. |

## Steps

1. Click the **Connectors** tab.

2. Find the connector and click **... > Delete**. On the confirmation modal, click **Delete**.

---

---
title: Editing a connector
description: Edit an existing connector to update its properties.
component: davinci
page_id: davinci:connectors:davinci_editing_a_connection
canonical_url: https://docs.pingidentity.com/davinci/connectors/davinci_editing_a_connection.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 2, 2023
section_ids:
  steps: Steps
---

# Editing a connector

Edit an existing connector to update its properties.

## Steps

1. Click the **Connectors** tab.

2. Find the connector in the list of your connectors and click **... > Edit**.

3. Update the connector's properties.

   Each connector has different properties. See the connector's reference documentation for more information about required and optional properties.

4. Click **Apply**.

---

---
title: Ping connectors
description: Ping connectors help you integrate your flows with other Ping Identity products and features.
component: davinci
page_id: davinci:connectors:davinci_ping_connectors
canonical_url: https://docs.pingidentity.com/davinci/connectors/davinci_ping_connectors.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 22, 2024
---

# Ping connectors

Ping connectors help you integrate your flows with other Ping Identity products and features.

For other connector types, you can search the complete list of connectors in the [Ping Identity Marketplace](https://marketplace.pingone.com/home).

The following table lists and describes the Ping connectors and provides links to the related documentation.

| Ping connector                                                                                                                                                | Description                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [PingFederate](https://docs.pingidentity.com/connectors/pf_connector.html)                                                                                    | Integrate your existing PingFederate authentication policies.                                                                                                                                                                                                                                    |
| [PingID](https://docs.pingidentity.com/connectors/pid_connector.html)                                                                                         | Use PingID for multi-factor authentication (MFA).                                                                                                                                                                                                                                                |
| [PingOne](https://docs.pingidentity.com/connectors/p1_connector.html)                                                                                         | Create and manage user accounts in PingOne, including resetting passwords and managing groups and agreements.                                                                                                                                                                                    |
| [PingOne Advanced Identity Cloud Access Request Connector](https://docs.pingidentity.com/connectors/p1_advanced_identity_cloud_access_request_connector.html) | Manage users and create access requests in PingOne Advanced Identity Cloud in your flow.                                                                                                                                                                                                         |
| [PingOne Advanced Identity Cloud Login Connector](https://docs.pingidentity.com/connectors/p1_advanced_identity_cloud_login_connector.html)                   | Authenticate users using the default journey in PingOne Advanced Identity Cloud in your flow.                                                                                                                                                                                                    |
| [PingOne Authentication](https://docs.pingidentity.com/connectors/p1_authentication_connector.html)                                                           | Authenticate users and manage PingOne user authentication sessions. This connector is required to [integrate flows into your application](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_how_to_implement_a_flow.html) using the redirect and widget methods. |
| [PingOne Authorize](https://docs.pingidentity.com/connectors/p1az_connector.html)                                                                             | Use PingOne Authorize for policy-based authorization decisions.                                                                                                                                                                                                                                  |
| [PingOne Credentials](https://docs.pingidentity.com/connectors/p1_credentials_connector.html)                                                                 | Use PingOne Credentials to issue, verify, and manage digital verifiable credentials.                                                                                                                                                                                                             |
| [PingOne MFA](https://docs.pingidentity.com/connectors/p1_mfa_connector.html)                                                                                 | Use PingOne MFA for multi-factor authentication (MFA) and device enrollment.                                                                                                                                                                                                                     |
| [PingOne Notifications](https://docs.pingidentity.com/connectors/p1_notifications_connector.html)                                                             | Send custom voice, SMS, and email notifications to cover a wide range of use cases for your customers.                                                                                                                                                                                           |
| [PingOne Protect](https://docs.pingidentity.com/connectors/p1_protect_connector.html)                                                                         | Use PingOne Protect to issue MFA challenges or deny access in high-risk situations.                                                                                                                                                                                                              |
| [PingOne RADIUS Gateway](https://docs.pingidentity.com/connectors/p1_radius_gateway_connector.html)                                                           | Authenticate users when accessing RADIUS clients that support the RADIUS PAP protocol.                                                                                                                                                                                                           |
| [PingOne Scope Consent](https://docs.pingidentity.com/connectors/p1_scope_consent_connector.html)                                                             | View and update user consent records.                                                                                                                                                                                                                                                            |
| [PingOne Verify](https://docs.pingidentity.com/connectors/p1_verify_connector.html)                                                                           | Use PingOne Verify to securely verify a user's identity based on a government-issued document and live face capture, also known as a selfie.                                                                                                                                                     |

---

---
title: Renaming a connector
description: Rename a connector to display a new name for the connector in the user interface.
component: davinci
page_id: davinci:connectors:davinci_renaming_a_connection
canonical_url: https://docs.pingidentity.com/davinci/connectors/davinci_renaming_a_connection.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 2, 2023
section_ids:
  steps: Steps
---

# Renaming a connector

Rename a connector to display a new name for the connector in the user interface.

## Steps

1. Click the **Connectors** tab.

2. Find the connector and click **... > Rename**.

   The **Rename Connector** modal opens.

3. In the **Name** field, enter a new name for the connector.

4. Click **Rename**.

---

---
title: Service connectors
description: "Service connectors help you integrate your flows with other services' products and features."
component: davinci
page_id: davinci:connectors:davinci_service_connectors
canonical_url: https://docs.pingidentity.com/davinci/connectors/davinci_service_connectors.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 21, 2025
---

# Service connectors

Service connectors help you integrate your flows with other services' products and features.

For other connector types, you can search the complete list of connectors in the [Ping Identity Marketplace](https://marketplace.pingone.com/home).

The following table lists and describes the service connectors and provides links to the related documentation.

| Service connector                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Accertify Connector](https://docs.pingidentity.com/connectors/accertify_connector.html)                                | Send identity lifecycle events to Accertify for real-time fraud detection and risk scoring in your flow.                                                                                                                                                                                                                                                                                                   |
| [Adobe Experience Manager Connector](https://docs.pingidentity.com/connectors/adobe_experience_manager_connector.html)  | Manage data privacy and consent within Adobe Experience Platform from your flow.                                                                                                                                                                                                                                                                                                                           |
| [Apple Login Connector](https://docs.pingidentity.com/connectors/apple_login_connector.html)                            | Authenticate users with Sign in with Apple and retrieve Apple ID attributes in your flow.                                                                                                                                                                                                                                                                                                                  |
| [AuthenticID Connector](https://docs.pingidentity.com/connectors/authenticid_connector.html)                            | Use AuthenticID for identity verification in your PingOne DaVinci flow.                                                                                                                                                                                                                                                                                                                                    |
| [Azure AD User Managment](https://docs.pingidentity.com/connectors/azure_ad_user_management_connector.html)             | Manage users, groups, and software licenses in your PingOne DaVinci flow.                                                                                                                                                                                                                                                                                                                                  |
| [Babel Street Connector](https://docs.pingidentity.com/connectors/babelstreet_connector.html)                           | Use the Babel Street Analytics API for name and address similarity, name transliteration, and language identification in your flow.                                                                                                                                                                                                                                                                        |
| [Castle](https://docs.pingidentity.com/connectors/castle_connector.html)                                                | Add additional risk signals with Castle's fraud and risk management platform in your PingOne DaVinci flow.                                                                                                                                                                                                                                                                                                 |
| [CLEAR Connector](https://docs.pingidentity.com/connectors/clear_connector.html)                                        | Verify users using CLEAR's hosted identity verification UI in your flow.                                                                                                                                                                                                                                                                                                                                   |
| [Cloudflare Connector](https://docs.pingidentity.com/connectors/cloudflare_connector.html)                              | Integrate Cloudflare threat intelligence and Zero Trust security capabilities into your flow.                                                                                                                                                                                                                                                                                                              |
| [Constella Connector](https://docs.pingidentity.com/connectors/constella_connector.html)                                | Use the Constella Intelligence risk evaluation API to detect account takeover attempts in your flow.                                                                                                                                                                                                                                                                                                       |
| [CrowdStrike](https://docs.pingidentity.com/connectors/crowdstrike_connector.html)                                      | Use CrowdStrike to improve authentication security in your PingOne DaVinci flow.                                                                                                                                                                                                                                                                                                                           |
| [Daon](https://docs.pingidentity.com/connectors/daon_connector.html)                                                    | Use Daon IdentityX for multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">&#xA;\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>&#xA;\</div>)* in your PingOne DaVinci flow.                                                                                                        |
| [Duo Connector](https://docs.pingidentity.com/connectors/duo_connector.html)                                            | Use Duo for multi-factor authentication (MFA) in your flow.                                                                                                                                                                                                                                                                                                                                                |
| [Entrust](https://docs.pingidentity.com/connectors/entrust_connector.html)                                              | Use Entrust adaptive authentication in your PingOne DaVinci flow.                                                                                                                                                                                                                                                                                                                                          |
| [Facebook Login Connector](https://docs.pingidentity.com/connectors/facebook_login_connector.html)                      | Authenticate users with Facebook and retrieve user attributes in your flow.                                                                                                                                                                                                                                                                                                                                |
| [Google Login Connector](https://docs.pingidentity.com/connectors/google_login_connector.html)                          | Authenticate users with Google and retrieve user attributes in your flow.                                                                                                                                                                                                                                                                                                                                  |
| [Google Workspace Admin](https://docs.pingidentity.com/connectors/google_workspace_admin_connector.html)                | Manage Google Workspace users, groups, and application licenses in your PingOne DaVinci flow.                                                                                                                                                                                                                                                                                                              |
| [HYPR](https://docs.pingidentity.com/connectors/hypr_connector.html)                                                    | Use HYPR for passwordless authentication in your PingOne DaVinci flow.                                                                                                                                                                                                                                                                                                                                     |
| [ID DataWeb](https://docs.pingidentity.com/connectors/id_dataweb_connector.html)                                        | Use ID DataWeb for identity verification in your PingOne DaVinci flow.                                                                                                                                                                                                                                                                                                                                     |
| [Island Connector](https://docs.pingidentity.com/connectors/island_connector.html)                                      | Use Island device trust signals in your flow.                                                                                                                                                                                                                                                                                                                                                              |
| [Jira](https://docs.pingidentity.com/connectors/jira_connector.html)                                                    | Create and manage Jira tickets in your PingOne DaVinci flow.                                                                                                                                                                                                                                                                                                                                               |
| [LexisNexis](https://docs.pingidentity.com/connectors/lexisnexis_connector.html)                                        | Perform risk assessments with ThreatMetrix and other Dynamic Decision Platform services, send a one-time passcode (OTP) *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)*, and prompt users with security questions. |
| [Marketo](https://docs.pingidentity.com/connectors/marketo_connector.html)                                              | Add, search, and update leads into Marketo in your PingOne DaVinci flow.                                                                                                                                                                                                                                                                                                                                   |
| [Microsoft Defender for Endpoint Connector](https://docs.pingidentity.com/connectors/microsoft_defender_connector.html) | Integrate endpoint detection and response capabilities into your flow to enforce device trust in real time.                                                                                                                                                                                                                                                                                                |
| [Microsoft Edge for Business](https://docs.pingidentity.com/connectors/microsoft_edge_connector.html)                   | Use Microsoft Edge for Business to improve authentication security in your PingOne DaVinci flow.                                                                                                                                                                                                                                                                                                           |
| [Microsoft Teams](https://docs.pingidentity.com/connectors/microsoft_teams_connector.html)                              | Manage user memberships and send messages in Microsoft Teams from your PingOne DaVinci flow.                                                                                                                                                                                                                                                                                                               |
| [Mitek Connector](https://docs.pingidentity.com/connectors/mitek_connector.html)                                        | Create Mitek identity verification journeys and deliver them by email or SMS in your flow.                                                                                                                                                                                                                                                                                                                 |
| [OneTrust](https://docs.pingidentity.com/connectors/onetrust_connector.html)                                            | Use OneTrust to manage receipts for user consent in your PingOne DaVinci flow.                                                                                                                                                                                                                                                                                                                             |
| [Salesforce](https://docs.pingidentity.com/connectors/salesforce_connector.html)                                        | Manage users and records in Salesforce from your PingOne DaVinci flows.                                                                                                                                                                                                                                                                                                                                    |
| [ScrambleID Connector](https://docs.pingidentity.com/connectors/scrambleid_connector.html)                              | Use OpenID Connect (OIDC) login with ScrambleID in your flow.                                                                                                                                                                                                                                                                                                                                              |
| [Secret Double Octopus Connector](https://docs.pingidentity.com/connectors/secret_double_octopus_connector.html)        | Use Secret Double Octopus for passwordless authentication in your flow.                                                                                                                                                                                                                                                                                                                                    |
| [SecurID](https://docs.pingidentity.com/connectors/securid_connector.html)                                              | Use RSA SecurID for multi-factor authentication (MFA) in your PingOne DaVinci flow.                                                                                                                                                                                                                                                                                                                        |
| [SentinelOne Connector](https://docs.pingidentity.com/connectors/sentinelone_connector.html)                            | Integrate SentinelOne endpoint detection and response capabilities into your flow to enforce device trust in real time.                                                                                                                                                                                                                                                                                    |
| [SEON](https://docs.pingidentity.com/connectors/seon_connector.html)                                                    | Uncover fraud patterns through SEON's device fingerprinting and intelligent insights in your PingOne DaVinci flow.                                                                                                                                                                                                                                                                                         |
| [ServiceNow](https://docs.pingidentity.com/connectors/servicenow_connector.html)                                        | Manage users, group memberships, and incidents in ServiceNow from your PingOne DaVinci flow.                                                                                                                                                                                                                                                                                                               |
| [Socure](https://docs.pingidentity.com/connectors/socure_connector.html)                                                | Verify identity documents and get fraud scores in your PingOne DaVinci flows.                                                                                                                                                                                                                                                                                                                              |
| [Splunk](https://docs.pingidentity.com/connectors/splunk_connector.html)                                                | Gain real-time operational intelligence through Splunk in your PingOne DaVinci flow.                                                                                                                                                                                                                                                                                                                       |
| [TransUnion TLOxp](https://docs.pingidentity.com/connectors/transunion_tloxp_connector.html)                            | Verify a user's identity information in your PingOne DaVinci flow by checking TransUnion's trusted data sources.                                                                                                                                                                                                                                                                                           |
| [Veriff](https://docs.pingidentity.com/connectors/veriff_connector.html)                                                | Verify users with Veriff's artificial intelligence (AI)-powered identity solution for identity fraud prevention in your PingOne DaVinci flow.                                                                                                                                                                                                                                                              |
| [Yoti](https://docs.pingidentity.com/connectors/yoti_connector.html)                                                    | Provide customers with a safe way to prove who they are through Yoti's identity verification, age estimate, and age verification services in your PingOne DaVinci flow.                                                                                                                                                                                                                                    |

---

---
title: Understanding and troubleshooting unavailable capabilities
description: When a capability is unavailable, nodes that use that capability still function during runtime but cannot be edited or added.
component: davinci
page_id: davinci:connectors:davinci_managing_unavailable_capabilities
canonical_url: https://docs.pingidentity.com/davinci/connectors/davinci_managing_unavailable_capabilities.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2024
section_ids:
  causes: Causes
  troubleshooting-unavailable-capabilities: Troubleshooting unavailable capabilities
  available-actions: Available actions
  disabled-actions: Disabled actions
---

# Understanding and troubleshooting unavailable capabilities

When a capability is unavailable, nodes that use that capability still function during runtime but cannot be edited or added.

If a capability is unavailable in your environment, nodes that use that capability are indicated with warning text in the flow canvas. These nodes function normally when the flow is run so that the runtime behavior for your users isn't degraded, but they cannot be edited, updated, or added while the capability is unavailable.

![A screen capture showing the flow canvas with an unavailable capability. The node displays a message that the node cannot be edited, the Add Connector menu displays the connector in grey, and the node details display a message indicating that the node cannot be edited.](_images/qpp1714422780533.png)

## Causes

Multiple conditions can cause a capability to be unavailable:

* The flow was exported from an environment with access to a connector or capability and imported into an environment without the same access. This can occur if the connector or capability is in early access or requires a specific license or service.

* The connector or capability is temporarily unavailable because of administrative portal issues.

* The connector or capability is being deprecated.

## Troubleshooting unavailable capabilities

If you have one or more nodes with unavailable capabilities in your environment, there are multiple troubleshooting steps you can take:

1. If you imported the flow from another environment, make sure that the current environment has the same licensing and services as the original environment.

2. Review the connector's release notes or integration directory entry to see if it is being deprecated.

3. Wait for 2 to 5 days to see if the issue resolves itself.

4. Contact Ping support.

## Available actions

When a capability is unavailable, you can take these actions:

* Manipulate the node on the canvas:

  * Move the node

  * Change the lines leading into or out of the node

* Use right-click options on the node:

  * **Clone** (the cloned node has the same limitation)

  * **Copy** (the pasted node has the same limitation)

  * **Replace**

  * **Change Linked Connector**

  * **Disable**

  * **Delete**

* Open the node properties to:

  * See the node configuration

  * See the deprecation message if one is present

  * Open the capabilities list to select another capability from the same connector

## Disabled actions

When a capability is unavailable, you cannot:

* Edit the capability configuration

* Add a new node that uses the capability

---

---
title: Use case connectors
description: Use case connectors are the fastest way to implement common user experiences, such as authentication, registration, password change, account recovery, and MFA. Compared with the more granular connector types, such as core connectors, Ping connectors, and service connectors, use case connectors eliminate the need for complex subflows by consolidating common use cases into a single node.
component: davinci
page_id: davinci:connectors:davinci_use_case_connectors
canonical_url: https://docs.pingidentity.com/davinci/connectors/davinci_use_case_connectors.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 21, 2025
---

# Use case connectors

Use case connectors are the fastest way to implement common user experiences, such as authentication, registration, password change, account recovery, and MFA. Compared with the more granular connector types, such as core connectors, Ping connectors, and service connectors, use case connectors eliminate the need for complex subflows by consolidating common use cases into a single node.

For other connector types, you can search the complete list of connectors in the [Ping Identity Marketplace](https://marketplace.pingone.com/home).

The following table lists and describes the use case connectors and provides links to the related documentation.

| Connector                                                                                | Uses                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Authentication](https://docs.pingidentity.com/connectors/authentication_connector.html) | The Authentication use case connector covers the following common user experiences:- Sign On

- Register account

- Accept agreement

- Verify email

- Recover account

- Change password                                                                 |
| [MFA](https://docs.pingidentity.com/connectors/mfa_connector.html)                       | The MFA use case connector covers the following common user experiences:- MFA registration

- MFA authentication                                                                                                                                           |
| [Protect](https://docs.pingidentity.com/connectors/protect_use_case_connector.html)      | The Protect use case connector lets you use PingOne Protect in a DaVinci flow to:- Improve the user experience by reducing MFA fatigue

- Lower the probability of unintentional push approvals

- Issue challenges or deny access in high-risk situations |

---

---
title: Using connectors securely
description: While Ping Identity provides many proprietary integrations for PingOne DaVinci, some connectors work with third-party services. You should review the security best practices documentation for those services.
component: davinci
page_id: davinci:connectors:davinci_using_connectors_securely
canonical_url: https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 29, 2023
section_ids:
  changing-the-logging-level: Changing the logging level
  about-this-task: About this task
  steps: Steps
  result: Result
  marking-output-fields-as-secure: Marking output fields as secure
  about-this-task-2: About this task
  steps-2: Steps
  result-2: Result
---

# Using connectors securely

While Ping Identity provides many proprietary integrations for PingOne DaVinci, some connectors work with third-party services. You should review the security best practices documentation for those services.

Some general security best practices to consider when using third-party connectors in your DaVinci flow are:

* When passing any secrets, keys, or passwords as output variables through the HTTP connector, mark them as `Secure` in the connector configuration.

* The account with the third-party service or on-premise resource should follow the principle of least privilege and only be granted the permissions necessary to perform the actions required by the connector.

* Whenever using custom JavaScript, HTML, or CSS in a DaVinci connector, you should follow general secure coding guidelines to avoid the introduction of any security vulnerabilities, privacy violations, or other unintended behavior.

## Changing the logging level

Some connectors can process a user's personally identifiable information (PII) such as name, address, email, and birthdate. To prevent inadvertent logging of any sensitive user data, you should not enable debug logging in any production-level flows that use connectors that can process PII.

### About this task

To view and change the logging level for your DaVinci flow:

### Steps

1. Click the **More Options ( [icon: ellipsis-v, set=fa])** icon and select **Flow Settings**.

2. On the **Logging** tab, view the **Log Level** list.

3. If the current selection is **Debug**, select **Info**.

4. Click **Save**.

## Result

You can now see if your flow is in Debug mode and disable debug logging. Learn more in [Debugging and analytics](../davinci_best_practices/davinci_best_practices_debugging_and_analytics.html).

## Marking output fields as secure

You should mark output fields secure when adding custom output fields for a connector such as the HTTP connector.

### About this task

To mark output fields as secure in the **Custom HTML Template** of the HTTP connector:

### Steps

1. Add an HTTP connector in DaVinci.

2. Complete the **Property Name** and **Display Name** fields.

   ![A GIF depicting a user entering the Property Name and Display name, then switching on the Secure toggle.](_images/zbk1694535064943.gif)

3. Click the **Secure** toggle and click **Apply**.

### Result

The output field is now marked as secure, which acts as an additional safeguard against the logging of any sensitive PII.