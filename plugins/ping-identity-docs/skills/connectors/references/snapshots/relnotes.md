---
title: April 2023
description: Release notes for PingOne DaVinci connectors for April 2023
component: connectors
page_id: connectors::relnotes/archive/2023-04-April
canonical_url: https://docs.pingidentity.com/connectors/relnotes/archive/2023-04-April.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  april-22: April 22
  the-forms-connector-is-now-available: The Forms connector is now available
  find-multiple-users: Find multiple users
  pingone-mfa-connector: PingOne MFA Connector
  new-flows-for-the-pingone-radius-gateway-connector: New flows for the PingOne RADIUS Gateway connector
  pingid-connector: PingID Connector
---

# April 2023

## April 22

### The Forms connector is now available

New Form Connector

You can use the [Form Connector](../../form_connector.html) to:

* Build flows around user experiences that you create on the **Experiences > Forms** tab in PingOne.

* Show messages using the branding that you define on the **Experiences > Branding & Themes** tab in PingOne.

### Find multiple users

New PingOne Connector

You can now use the [PingOne Connector](../../p1_connector.html) **Find Multiple Users** capability to search and return up to 100 users.

### PingOne MFA Connector

Improved PingOne MFA Connector

We've enhanced the [PingOne MFA Connector](../../p1_mfa_connector.html) to enable the user to enter their One-time Passcode (OTP) when triggering Multi-factor Authentication (MFA). It's now possible for the user to enter a TOTP/HOTP-generated OTP when starting authentication using the Create Device Authentication endpoint.

### New flows for the PingOne RADIUS Gateway connector

Improved PingOne RADIUS Gateway Connector

We have added the following [PingOne RADIUS Gateway Connector](../../p1_radius_gateway_connector.html) flow templates to support authentication for MS-CHAP v2 protocol, authentication in no-challenge mode, and on-the-fly registration:

* [RADIUS Gateway - Registration and Authentication](https://marketplace.pingone.com/item/radius-gateway-registration-and-authentication)

* [RADIUS Gateway - No Challenge Authentication](https://marketplace.pingone.com/item/radius-gateway-no-challenge-authentication)

* [RADIUS Gateway - Advanced Protocols Authentication](https://marketplace.pingone.com/item/radius-gateway-advanced-protocols-authentication)

### PingID Connector

Improved PingID Connector

We've enhanced the [PingID Connector](../../pid_connector.html) to enable the user to enter their One-time Passcode (OTP) when triggering Multi-factor Authentication (MFA). It's now possible for the user to enter a TOTP/HOTP-generated OTP when starting authentication using the Create Device Authentication endpoint.

---

---
title: April 2024
description: Release notes for PingOne DaVinci connectors for April 2024
component: connectors
page_id: connectors::relnotes/archive/2024-04-April
canonical_url: https://docs.pingidentity.com/connectors/relnotes/archive/2024-04-April.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  april-30: April 30
  specify-branding-and-theme-for-forms-within-the-pingone-forms-connector: Specify branding and theme for forms within the PingOne Forms Connector
  pingone-user-lookup-capabilities-now-update-the-global-variable-for-user-id: PingOne user lookup capabilities now update the global variable for user ID
  the-pingone-advanced-identity-cloud-access-connector-is-now-available: The PingOne Advanced Identity Cloud Access connector is now available
  the-pingone-advanced-identity-cloud-login-connector-is-now-available: The PingOne Advanced Identity Cloud Login connector is now available
---

# April 2024

## April 30

### Specify branding and theme for forms within the PingOne Forms Connector

New Form Connector

The [Form Connector](../../form_connector.html) **Show Form** and **Show Branded Message** capabilities now include the ability to specify a theme with the new **Form Theme** field, which displays the themes configured in your PingOne environment under **Branding & Themes**.

Additionally, you can also select **Use Theme ID** and paste the unique Theme ID. Learn more in [Selecting an active theme](https://docs.pingidentity.com/pingone/user_experience/p1_select_theme.html).

### PingOne user lookup capabilities now update the global variable for user ID

Improved PingOne Connector

The following [PingOne Connector](../../p1_connector.html) capabilities now update the `p1userid` global variable in PingOne DaVinci with the user ID when the user is successfully found:

* **Find User**

* **Check Password**

* **Create User**

* **Read User**

This update allows you to use the `p1userid` global variable in the flow to ensure the user ID will be populated at the right times.

### The PingOne Advanced Identity Cloud Access connector is now available

New PingOne Advanced Identity Cloud Access Connector

You can use the [PingOne Advanced Identity Cloud Access Request Connector](../../p1_advanced_identity_cloud_access_request_connector.html) to:

* Manage users

* Create access requests

* Make custom API calls

### The PingOne Advanced Identity Cloud Login connector is now available

New PingOne Advanced Identity Cloud Login Connector

You can use the [PingOne Advanced Identity Cloud Login Connector](../../p1_advanced_identity_cloud_login_connector.html) to authenticate users using the default journey.

---

---
title: April 2025
description: Release notes for PingOne DaVinci connectors for April 2025
component: connectors
page_id: connectors::relnotes/archive/2025-04-April
canonical_url: https://docs.pingidentity.com/connectors/relnotes/archive/2025-04-April.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  april-30: April 30
  the-splunk-connector-now-respects-localized-error-messages: The Splunk Connector now respects localized error messages
  april-25: April 25
  the-lexisnexis-connector-now-respects-localized-error-messages: The LexisNexis Connector now respects localized error messages
  april-4: April 4
  authenticate-user-via-kerberos: Authenticate User via Kerberos
  april-1: April 1
  the-location-policy-connector-now-outputs-country-result: The Location Policy connector now outputs country result
---

# April 2025

## April 30

### The Splunk Connector now respects localized error messages

Fixed Splunk Connector

Error handling for the [Splunk Connector](../../splunk_connector.html) has been corrected and now respects localized error messages. As a result, select error outcomes might produce different message text.

## April 25

### The LexisNexis Connector now respects localized error messages

Fixed LexisNexis Connector

Error handling for the [LexisNexis Connector](../../lexisnexis_connector.html) has been corrected and now respects localized error messages. As a result, select error outcomes might produce different message text.

## April 4

### Authenticate User via Kerberos

Improved PingOne Connector

The [PingOne Connector](../../p1_connector.html) **Authenticate User via Kerberos** capability now supports the selection of a user type, regardless of whether user migration is enabled or not.

The ability to select a user type without user migration allows you to create PingOne DaVinci flows to offer seamless SSO authentication experience to users provisioned from Microsoft Active Directory into PingOne through an [LDAP gateway provisioning connection](https://docs.pingidentity.com/pingone/integrations/p1_create_provisioning_connection_gateway.html) and an [inbound rule](https://docs.pingidentity.com/pingone/integrations/p1_create_inbound_provisioning_rule_gateway.html).

|   |                                                                           |
| - | ------------------------------------------------------------------------- |
|   | The selected LDAP gateway must be configured with at least one user type. |

## April 1

### The Location Policy connector now outputs country result

Updated Location Policy Connector

The [Location Policy Connector](../../location_policy_connector.html) **Allow by Location Name** and **Deny by Location Name** capabilities now provide the location information associated with the user's IP address. This makes it easy to branch the flow more specifically after an allow or deny result by evaluating the user's exact country.

---

---
title: April 2026
description: PingOne DaVinci connector release notes for April 2026
component: connectors
page_id: connectors::relnotes/2026-04-April
canonical_url: https://docs.pingidentity.com/connectors/relnotes/2026-04-April.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  april-1: April 1
  ability-to-notify-users-of-successful-account-creation: Ability to notify users of successful account creation
  ability-to-send-verification-code-notifications: Ability to send verification code notifications
---

# April 2026

## April 1

### Ability to notify users of successful account creation

New PingOne Connector

The [PingOne connector](../p1_connector.html)'s **Create User** capability now includes additional fields that allow you to notify users of successful account creation by email. Use the newly added **Notification Name**, **Notification Locale**, and **Notification Variables** fields within the capability to select the notification template from PingOne and configure for localization.

You can manage notification templates in PingOne. Learn more in [Notification Templates](https://docs.pingidentity.com/pingone/user_experience/p1_notifications.html) in the PingOne documentation.

### Ability to send verification code notifications

New PingOne Connector

The [PingOne connector](../p1_connector.html)'s **Create User** capability now allows you to send a verification code notification. Use the newly added **Notification Name**, **Notification Locale**, and **Notification Variables** fields within the capability to select the notification template from PingOne and configure for localization.

You can manage notification templates in PingOne. Learn more in [Notification Templates](https://docs.pingidentity.com/pingone/user_experience/p1_notifications.html) in the PingOne documentation.

---

---
title: August 2023
description: Release notes for PingOne DaVinci connectors for August 2023
component: connectors
page_id: connectors::relnotes/archive/2023-08-August
canonical_url: https://docs.pingidentity.com/connectors/relnotes/archive/2023-08-August.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  august-29: August 29
  search-for-users-with-a-custom-scim-filter: Search for users with a custom SCIM filter
  create-and-update-user-mappings-updated-to-resolve-error-from-pingone: Create and update user mappings updated to resolve error from PingOne
  character-limit-for-user-groups-field: Character limit for User Groups field
---

# August 2023

## August 29

### Search for users with a custom SCIM filter

New PingOne Connector

Previously, when searching for users with **Find User** and **Find Multiple Users** in the [PingOne Connector](../../p1_connector.html), the capability builds a SCIM filter based on a list of attributes and a search term.

You can now provide your own filter by toggling on the new **Custom SCIM Filter** field, allowing you to pick the operators used for filtering and allow different values to be searched for each attribute.

### Create and update user mappings updated to resolve error from PingOne

Improved PingOne Connector

The [PingOne Connector](../../p1_connector.html) **Create User** and **Update User** capabilities mappings no longer pass empty values to PingOne. Previously, PingOne sent an error to PingOne DaVinci due to empty values.

If a field is included with no value, the connector would normally pass it to PingOne as an empty string. If no field or value is included, the connector would normally pass it as a null value. Now, these values are omitted and not passed as empty values.

### Character limit for User Groups field

Fixed PingID Connector

When using the legacy [PingID Connector](../../pid_connector.html) in a PingOne DaVinci flow, there was a problem if the **User Groups** field contained more than 100 characters. This 100-character limit has been removed.

---

---
title: August 2025
description: Release notes for PingOne DaVinci connectors for August 2025
component: connectors
page_id: connectors::relnotes/2025-08-August
canonical_url: https://docs.pingidentity.com/connectors/relnotes/2025-08-August.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  august-27: August 27
  added-the-ability-to-block-redirects-in-make-rest-api-call-nodes: Added the ability to block redirects in Make REST API Call nodes
  august-19: August 19
  authenticate-user-via-kerberos: Authenticate User via Kerberos
---

# August 2025

## August 27

### Added the ability to block redirects in Make REST API Call nodes

Improved HTTP Connector

In the [HTTP Connector](../http_connector.html) **Make REST API Call** capability, the new **Block Redirects** option allows you to enhance the security of the flow by preventing the browser from automatically following redirects. When a redirect is attempted, an error occurs instead.

## August 19

### Authenticate User via Kerberos

New PingOne Connector

The [PingOne Connector](../p1_connector.html) **Authenticate User via Kerberos** capability now supports additional gateway and user type pairs. The ability to add multiple sets of gateway and user types help support large enterprises with multiple domains who need to validate Kerberos tokens.

---

---
title: December 2022
description: Release notes for PingOne DaVinci connectors for December 2022
component: connectors
page_id: connectors::relnotes/archive/2022-12-December
canonical_url: https://docs.pingidentity.com/connectors/relnotes/archive/2022-12-December.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  december-12: December 12
  pingone-radius-gateway-connector-now-available: PingOne RADIUS Gateway connector now available
  pingid-connector-now-available: PingID Connector now available
  pingid-policy-support: PingID policy support
  december-5: December 5
  html-form-capabilities-have-been-deprecated: "\"HTML Form\" capabilities have been deprecated"
---

# December 2022

## December 12

### PingOne RADIUS Gateway connector now available

New PingOne RADIUS Gateway Connector

The new [PingOne RADIUS Gateway Connector](../../p1_radius_gateway_connector.html) is now available.

Use this connector to orchestrate user authentication flows that are initiated by authentication requests using the RADIUS protocol.

### PingID Connector now available

New PingID Connector

The new [PingID Connector](../../pid_connector.html) is now available.

Use this connector to register and authenticate your users with PingID when the PingID tenant is connected to a PingOne environment.

The PingID connector is based on the PingOne API and includes an increased set of capabilities. It replaces the previous PingID connector (now called PingID Legacy Connector).

### PingID policy support

Issue PingID Connector

PingID policy is not currently supported.

## December 5

### "HTML Form" capabilities have been deprecated

Info HTTP Connector

The following [HTTP Connector](../../http_connector.html) capabilities are not available on environments created after December 5, 2022:

* **HTML Form**

* **HTML Form with reCAPTCHA**

These capabilities are being replaced by a new drag-and-drop form builder in PingOne. In the PingOne admin console, navigate to **Experiences > Forms** to create forms that use your existing branding and themes.

The PingOne Forms connector lets you include these forms in your flows.

---

---
title: December 2024
description: Release notes for PingOne DaVinci connectors for December 2024
component: connectors
page_id: connectors::relnotes/archive/2024-12-December
canonical_url: https://docs.pingidentity.com/connectors/relnotes/archive/2024-12-December.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  december-11: December 11
  read-population: Read Population
  december-4: December 4
  new-hashing-options-in-the-functions-connector: New hashing options in the Functions Connector
---

# December 2024

## December 11

### Read Population

Improved PingOne Connector

You can now use the [PingOne Connector](../../p1_connector.html) **Read Population** capability to determine a user's population based on an alternative identifier value and can also specify a theme to support multi-brand authentication experiences.

## December 4

### New hashing options in the [Functions Connector](../../functions_connector.html)

Updated Functions Connector

![dvc functions create hash](../../_images/connector-images/dvc-functions-create-hash.png)

Hashing a value is an effective way to verify data in your flow while keeping it secure. To make this easier, we've added new configuration options to the **Create a Hash** capability in the Functions connector. Select the hashing algorithm, use a generated salt value or provide your own, and choose the final encoding method.

---

---
title: February 2022
description: Release notes for PingOne DaVinci connectors for February 2022
component: connectors
page_id: connectors::relnotes/archive/2022-02-February
canonical_url: https://docs.pingidentity.com/connectors/relnotes/archive/2022-02-February.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  february-10: February 10
  the-pingone-connector-is-now-available: The PingOne connector is now available
---

# February 2022

## February 10

### The PingOne connector is now available

New PingOne Connector

You can use the [PingOne Connector](../../p1_connector.html) to:

* Create a sign-on flow for authentication

* Reset a user's password

* Register new users in the PingOne user store

* Create, edit, and delete users in the PingOne user store

* Verify a user's email address

* View a user's population

* View a user's group membership

* View agreements and consents for a user

---

---
title: February 2024
description: Release notes for PingOne DaVinci connectors for February 2024
component: connectors
page_id: connectors::relnotes/archive/2024-02-February
canonical_url: https://docs.pingidentity.com/connectors/relnotes/archive/2024-02-February.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  february-10: February 10
  authenticate-user-through-kerberos: Authenticate user through Kerberos
  added-capabilities-for-device-authorization: Added capabilities for device authorization
  added-requestedauthncontext-for-saml-external-idps: Added RequestedAuthnContext for SAML external IdPs
---

# February 2024

## February 10

### Authenticate user through Kerberos

New PingOne Connector

You can use the new [PingOne Connector](../../p1_connector.html) **Authenticate User Via Kerberos** capability to authenticate Active Directory users seamlessly through the Kerberos protocol.

### Added capabilities for device authorization

New PingOne Authentication Connector

The following capabilities have been added to the [PingOne Authentication Connector](../../p1_authentication_connector.html) to allow for device authorization:

* **Verify User Code (Device Auth Flows)**

* **Authorize User Code (Device Auth Flows)**

* **Decline User Code (Device Auth Flows)**

### Added RequestedAuthnContext for SAML external IdPs

New PingOne Authentication Connector

The [PingOne Authentication Connector](../../p1_authentication_connector.html) **Sign On with External Identity Provider** capability now includes the following fields:

* **Requested Authentication Context**

* **Authentication Context Reference**

You can now select whether to pass the requested authentication context using the `AuthnContextClassRef` or the `AuthnContextDeclRef` based on your agreement with the SAML IdP.

---

---
title: February 2025
description: Release notes for PingOne DaVinci connectors for February 2025
component: connectors
page_id: connectors::relnotes/archive/2025-02-February
canonical_url: https://docs.pingidentity.com/connectors/relnotes/archive/2025-02-February.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  february-15: February 15
  new-read-device-authentication-policy-capability: New Read Device Authentication Policy capability
  february-10: February 10
  improved-flexibility-with-saml-and-ws-federation-attributes-sent-to-pingone: Improved flexibility with SAML and WS-Federation attributes sent to PingOne
---

# February 2025

## February 15

### New Read Device Authentication Policy capability

New PingID Connector

The [PingID Connector](../../pid_connector.html) **Read Device Authentication Policy** capability allows you to read device authentication policies in your PingOne DaVinci flow.

## February 10

### Improved flexibility with SAML and WS-Federation attributes sent to PingOne

New PingOne Authentication Connector

When authenticating users by redirecting the browser to your PingOne DaVinci flow with the [PingOne Authentication Connector](../../p1_authentication_connector.html), the PingOne DaVinci flow policy returns additional attributes to PingOne. You can now override the default format of those attributes.

|   |                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The ability to use a flow to orchestrate authentication for Microsoft 365 applications is currently in limited release. To request access to these parameters, open a support case. |

---

---
title: February 2026
description: Release notes for PingOne DaVinci connectors for February 2026
component: connectors
page_id: connectors::relnotes/2026-02-February
canonical_url: https://docs.pingidentity.com/connectors/relnotes/2026-02-February.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  february-11: February 11
  search-special-character-usernames-toggle: Search Special-Character Usernames toggle
---

# February 2026

## February 11

### Search Special-Character Usernames toggle

New PingOne Connector

Several capabilities in the [PingOne Connector](../p1_connector.html) have a new configuration option to escape user attributes. You can now use a toggle to automatically escape input for each capability that executes a user search with a username. This allows customers to opt in based on their needs for each flow and doesn't break existing flows.

---

---
title: January 2023
description: Release notes for PingOne DaVinci connectors for January 2023
component: connectors
page_id: connectors::relnotes/archive/2023-01-January
canonical_url: https://docs.pingidentity.com/connectors/relnotes/archive/2023-01-January.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  january-20: January 20
  new-pingid-connector-flows: New PingID Connector flows
  pingid-devices-page-availability: PingID devices page availability
  localization-support: Localization support
  fixed-the-poll-is-not-defined-error: "Fixed the \"poll is not defined\" error"
---

# January 2023

## January 20

### New PingID Connector flows

New PingID Connector

Following the release of the new [PingID Connector](../../pid_connector.html), we've added the following out-of-the-box flows:

* [PingID Device Registration Subflow](https://marketplace.pingone.com/item/pingid-device-registration-subflow)

* [PingID Authentication Subflow](https://marketplace.pingone.com/item/pingid-authentication-subflow)

### PingID devices page availability

Issue PingID Connector

The [PingID Connector](../../pid_connector.html) Devices page is not available when using the PingID Authentication sub-flow. The 'Settings' button is therefore not displayed on the Authentication screen.

### Localization support

Issue PingID Connector

The [PingID Connector](../../pid_connector.html) only supports English language.

### Fixed the "poll is not defined" error

Fixed Challenge Connector

We've fixed an issue that caused the [Challenge Connector](../../challenge_connector.html) to report "poll is not defined" when using the **Poll for Transaction Status** capability.

---

---
title: January 2024
description: Release notes for PingOne DaVinci connectors for January 2024
component: connectors
page_id: connectors::relnotes/archive/2024-01-January
canonical_url: https://docs.pingidentity.com/connectors/relnotes/archive/2024-01-January.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  january-14: January 14
  pingone-scope-consent-connector-now-available: PingOne Scope Consent connector now available
---

# January 2024

## January 14

### PingOne Scope Consent connector now available

New PingOne Scope Consent Connector

The new [PingOne Scope Consent Connector](../../p1_scope_consent_connector.html) is now available.

Use this connector to view consent records on an application or user basis, revoke or update user consent records, or prompt users to provide or decline consent to sign-on policies and record these decisions.

---

---
title: January 2025
description: Release notes for PingOne DaVinci connectors for January 2025
component: connectors
page_id: connectors::relnotes/archive/2025-01-January
canonical_url: https://docs.pingidentity.com/connectors/relnotes/archive/2025-01-January.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  january-14: January 14
  simplified-get-user-consent-capability: Simplified Get User Consent capability
---

# January 2025

## January 14

### Simplified Get User Consent capability

Improved PingOne Scope Consent Connector

Previously, to select how the [PingOne Scope Consent Connector](../../p1_scope_consent_connector.html) capability identifies the application from the **Application Attribute** field, you had to select either **Application ID** or **Application Name** and enter a value into the corresponding field.

Now, you can always enter the applicable scope into the **Scopes** field regardless of the **Application Attribute** field value.

---

---
title: January 2026
description: Release notes for PingOne DaVinci connectors for January 2026
component: connectors
page_id: connectors::relnotes/2026-01-January
canonical_url: https://docs.pingidentity.com/connectors/relnotes/2026-01-January.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  january-8: January 8
  the-ldap-connector-is-deprecating-the-format-of-three-active-directory-ad-attribute-types: The LDAP connector is deprecating the format of three Active Directory (AD) attribute types
---

# January 2026

## January 8

### The LDAP connector is deprecating the format of three Active Directory (AD) attribute types

Improved LDAP Connector

The [LDAP Connector](../ldap_connector.html) is changing the format of Active Directory (AD) attributes `objectSid`, `objectGUID`, and `ms-ds-consistencyGUID` in the entry in response to capabilities such as `Create Entry`, `Modify DN`, `Replace Attributes`, and `Modify Attribute`.

Previously, these attribute values were returned in a binary format, such as `\u0001\u0005\u0000\u0000\u0000\u0000\u0000\u0005\u0015…​`. Now they are returned in a decoded, human-readable format, such as `S-1-5-21-…​`.

Existing customers already using these attributes in their PingOne DaVinci environments have been notified and advised to work with their account teams or support in order to update their flows and avoid any impact.

This change is generally available today for all other customers and any new environments.

---

---
title: July 2023
description: Release notes for PingOne DaVinci connectors for July 2023
component: connectors
page_id: connectors::relnotes/archive/2023-07-July
canonical_url: https://docs.pingidentity.com/connectors/relnotes/archive/2023-07-July.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  july-7: July 7
  ability-to-override-mfa-policy: Ability to override MFA policy
---

# July 2023

## July 7

### Ability to override MFA policy

Improved PingOne MFA Connector

We've enhanced the [PingOne MFA Connector](../../p1_mfa_connector.html) Policy ID field to the Create Device Authentication Capability that enables you to override the MFA policy that is configured in the MFA connector settings.

---

---
title: July 2025
description: Release notes for PingOne DaVinci connectors for July 2025
component: connectors
page_id: connectors::relnotes/2025-07-July
canonical_url: https://docs.pingidentity.com/connectors/relnotes/2025-07-July.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  july-18: July 18
  the-show-form-capability-now-includes-conditional-component-visibility: The Show Form capability now includes conditional component visibility
---

# July 2025

## July 18

### The Show Form capability now includes conditional component visibility

Improved Form Connector

The [Form Connector](../form_connector.html) conditional component visibility allows you to create a form in PingOne Forms with components that you can configure to be hidden or shown in a user-facing form based on Boolean values pulled from your PingOne DaVinci flow. Learn more in [Configuring conditional component visibility](https://docs.pingidentity.com/pingone/user_experience/p1_configuring_conditional_component_visibility.html).

When you include a form with conditional component visibility with the Show From capability, you'll see the additional **Component Visibility** field with key-value pairs to configure which components are shown or hidden.

---

---
title: June 2022
description: Release notes for PingOne DaVinci connectors for June 2022
component: connectors
page_id: connectors::relnotes/archive/2022-06-June
canonical_url: https://docs.pingidentity.com/connectors/relnotes/archive/2022-06-June.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  june-23: June 23
  the-crowdstrike-connector-is-now-available: The CrowdStrike connector is now available
---

# June 2022

## June 23

### The CrowdStrike connector is now available

New CrowdStrike Connector

You can use the [CrowdStrike Connector](../../crowdstrike_connector.html) to:

* Check whether a device is managed by CrowdStrike

* List the devices associated a username or IP address

* Get the incident scores for devices

* Get the CrowdStrike scores from multiple incidents

* Get the CrowdStrike Zero Trust Assessment scores for a device

* Get the CrowdScore for an environment

* Managed quarantined devices

---

---
title: June 2023
description: Release notes for PingOne DaVinci connectors for June 2023
component: connectors
page_id: connectors::relnotes/archive/2023-06-June
canonical_url: https://docs.pingidentity.com/connectors/relnotes/archive/2023-06-June.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  june-29: June 29
  unlock-user-account: Unlock user account
  new-group-crud-capabilities: New group CRUD capabilities
  the-make-rest-api-call-capability-now-supports-mtls: The Make REST API Call capability now supports mTLS
  added-variable-option-for-last-sign-on: Added Variable option for last sign on
---

# June 2023

## June 29

### Unlock user account

New PingOne Connector

The new [PingOne Connector](../../p1_connector.html) **Unlock User** capability allows you to unlock a locked PingOne user account:

### New group CRUD capabilities

New PingOne Connector

To support group manipulation during flows in PingOne DaVinci, we have added the following capabilities to the [PingOne Connector](../../p1_connector.html):

* **Create Group**

* **Read Group**

* **Update Group**

* **Delete Group**

* **Read Group Members**

These allow you to create, manage, and read groups in a PingOne environment.

### The Make REST API Call capability now supports mTLS

New HTTP Connector

The [HTTP Connector](../../http_connector.html) now supports mTLS. The **Make REST API Call** capability includes a new **MTLS Support** field to include keys configured in PingOne. You can view and create keys in PingOne by selecting the **Certificates and Keypairs** link under the field.

The default configuration is `None`, which will not use mTLS for API calls with the connector.

### Added `Variable` option for last sign on

New PingOne Authentication Connector

The [PingOne Authentication Connector](../../p1_authentication_connector.html) **Check Session** capability now includes a `Variable` option for the **Last Sign On** field, which enables variable and parameter use.