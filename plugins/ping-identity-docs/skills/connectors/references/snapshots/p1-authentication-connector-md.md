---
title: PingOne Authentication Connector
description: The PingOne Authentication connector lets you authenticate users and manage PingOne user authentication sessions in your PingOne DaVinci flow
component: connectors
page_id: connectors::p1_authentication_connector
canonical_url: https://docs.pingidentity.com/connectors/p1_authentication_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-pingone-authentication-connector: Configuring the PingOne Authentication connector
  using-the-connector-in-a-flow: Using the connector in a flow
  authenticating-users-by-redirecting-the-browser-to-your-pingone-davinci-flow: Authenticating users by redirecting the browser to your PingOne DaVinci flow
  authenticating-users-by-embedding-the-pingone-davinci-widget-in-your-web-application: Authenticating users by embedding the PingOne DaVinci widget in your web application
  authenticating-users-with-an-external-identity-provider: Authenticating users with an external identity provider
  include-the-skidp-component-in-a-custom-html-template: Include the skIdP component in a Custom HTML Template
  use-the-sign-on-with-external-identity-provider-capability-in-a-flow: Use the Sign On with External Identity Provider capability in a flow
  checking-whether-a-user-has-an-active-session: Checking whether a user has an active session
  creating-or-updating-a-session: Creating or updating a session
  deleting-a-session: Deleting a session
  managing-device-authorization-with-a-user-code: Managing device authorization with a user code
  capabilities: Capabilities
  returnSuccessResponseRedirect: Return Success Response (Redirect Flows)
  returnSuccessResponseWidget: Return Success Response (Widget Flows)
  returnErrorResponseRedirect: Return Error Response (Redirect Flows)
  checkSession: Check Session
  setSession: Create or Update Session
  deleteSession: Delete Session
  loginFirstFactor: Sign On with External Identity Provider
  verifyUserCode: Verify User Code (Device Auth Flows)
  authorizeUserCode: Authorize User Code (Device Auth Flows)
  declineUserCode: Decline User Code (Device Auth Flows)
  return-ciba-success: Return CIBA Success
  return-ciba-error: Return CIBA Error
---

# PingOne Authentication Connector

The PingOne Authentication connector lets you authenticate users and manage PingOne user authentication sessions in your PingOne DaVinci flow.

You can use the PingOne Authentication connector to:

* Authenticate users by integrating PingOne DaVinci flows into your application using a browser redirect or the PingOne DaVinci widget

* Authenticate users with external identity providers *(tooltip: \<div class="paragraph">
  \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
  \</div>)* configured in PingOne

* Create, update, or delete PingOne authentication sessions

* Check whether a user has an active session

* Verify a user's code for device authorization flows

* Authorize or decline device access to a user's account

## Setup

### Resources

Learn more in the following:

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need a PingOne license.

### Configuring the PingOne Authentication connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

The PingOne Authentication connector automatically communicates with the PingOne environment associated with your PingOne DaVinci environment.

## Using the connector in a flow

### Authenticating users by redirecting the browser to your PingOne DaVinci flow

This is the recommended method for integrating a PingOne DaVinci flow into your application. It allows you to authenticate users by redirecting the browser from your application, through PingOne, to your PingOne DaVinci flow. This method supports either OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)*, Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">
\<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>
\</div>)*, or Microsoft 365 applications.

You can find detailed setup instructions in [Launching a PingOne flow with a redirect](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launch_flow_redirect.html).

To use this method, end your flow with the following two capabilities:

* Success path: **Return a Success Response (Redirect Flows)**

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | You can optionally configure **ID Token Custom Claims** to add additional attributes to the OIDC ID Token, SAML assertion, or WS-Federation security token for Microsoft 365.For SAML assertions, the default attribute format is `urn:oasis:names:tc:SAML:2.0:attrname-format:basic`. For WS-Federation security tokens, the default attribute format is `http://schemas.xmlsoap.org/ws/2005/05/identity/claims`.To override the default attribute format, append the pipe character followed by the desired format to the attribute name. For example:- If you enter `attr1` as the **Claim Name** value, the resulting attribute format is just the default value.

  - If you enter `attr1\|http://schemas.microsoft.com/ws/2008/06/identity/claims/5678` as the **Claim Name** value, the resulting attribute format is `http://schemas.microsoft.com/ws/2008/06/identity/claims/5678`. |

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | In addition to fulfilling an OIDC, SAML *(tooltip: \<div class="paragraph">&#xA;\<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>&#xA;\</div>)*, or Microsoft 365 authentication request, this capability creates a PingOne user authentication session. If you don't need session management capabilities, you can ignore the session that is created. |

* Error path: **Return an Error Response (Redirect Flows)**

### Authenticating users by embedding the PingOne DaVinci widget in your web application

This is an alternate method for integrating a PingOne DaVinci flow into your application when a redirect is not possible. It allows you to authenticate users with your PingOne DaVinci flow by embedding a widget within your application. The browser stays on your organization's domain throughout the transaction. This method only supports OIDC.

You can find detailed setup instructions in [Launching a flow with the widget](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launching_a_flow_with_the_widget.html).

To use this method, end your flow with the following two capabilities:

* Success path: **Return a Success Response (Widget Flows)**

  |   |                                                                                                                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | In addition to fulfilling an OIDC authentication request, this capability creates a PingOne user authentication session. If you don't need session management capabilities, you can ignore the session that is created. |

* Error path: **Send Error JSON Response**

  |   |                                                                  |
  | - | ---------------------------------------------------------------- |
  |   | This capability is in the [HTTP Connector](http_connector.html). |

### Authenticating users with an external identity provider

The connector allows you use an external identity provider that you have configured in PingOne to authenticate users in your flow.

You can use the **Link with PingOne User** setting to link the resulting user information to PingOne accounts to enable self-service features and centralize user management within your organization.

Attributes from the external provider are also made available in your flow as part of the output schema for the capability.

|   |                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can find more information about external identity providers in PingOne in [Identity Providers](https://docs.pingidentity.com/pingone/integrations/p1_external_idps.html) and [Adding an external identity provider sign-on step](https://docs.pingidentity.com/pingone/authentication/p1_add_idp_signon_step.html). |

There are two ways to do this:

#### Include the **skIdP** component in a Custom HTML Template

This approach allows you to build a custom HTML page with sign on buttons that are powered by DaVinci authentication connectors and identity providers configured in PingOne.

1. In a flow, add the HTTP connector with the **Custom HTML Template** capability.

2. In the **HTML Template** field, click **{}**, select **SK-Components**, and add the **skIdP** component.

3. In the **HTML Template** field, click the **skIdP** component to open the configuration.

4. From the **Identity Provider Connector** list, select your PingOne Authentication connector.

5. From the **PingOne External Identity Provider** list, select an identity provider.

   |   |                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------ |
   |   | To manage the identity providers on this list, go to **Integrations > External IdPs** in your PingOne environment. |

6. Complete the rest of the skIdP configuration according to the help text and click **Apply**.

#### Use the **Sign On with External Identity Provider** capability in a flow

1. In a flow, add the PingOne Authentication connector with the **Sign On with External Identity Provider** capability.

2. In the capability configuration, from the **Identity Provider** list, select an identity provider.

3. Complete the rest of the capability configuration according to the help text.

   |   |                                                                                                                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | In the **Authentication Context Reference** field, select whether to pass the requested authentication context via the `AuthnContextClassRef` or `AuthenContextDeclRef` element based on your agreement with the SAML IdP. |

4. Click **Apply**.

### Checking whether a user has an active session

The **Check a User's Session Status** capability lets you check whether a user has an active authentication session that matches the authentication method and time period you define.

This lets you create detailed sign on policies. For example, you could skip reauthentication when a user has already signed on with MFA in the past 8 hours.

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Creating or updating a session

The **Create or Update a Session** capability lets you capture information in your flow and use it to create a PingOne user authentication session.

When creating the session, you can include the authentication method or methods that the user used to sign on. This information is associated with the session, and it allows you to create detailed sign on policies that branch based on the authentication method. Learn more in **Checking whether a user has an active session**.

No special configuration is needed. Add the capability and populate its properties according to the help text.

|   |                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You don't need to add this capability in flows that end with the **Return a Success Response (Redirect Flows)** or **Return a Success Response (Widget Flows)** capability. Those capabilities already create sessions. |

### Deleting a session

The **Delete a Session** capability allows you to sign a user out and optionally delete their PingOne user authentication session.

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Managing device authorization with a user code

The **Verify User Code (Device Auth Flows)** capability allows you to grant device access to a user's PingOne account.

Once the user code is verified in the flow, you can use the following capabilities to authorize or decline device access:

* **Authorize User Code (Device Auth Flows)**

* **Decline User Code (Device Auth Flows)**

## Capabilities

### Return Success Response (Redirect Flows)

Create a PingOne session and redirect back to the source of the authentication request. Use this to complete flows that are initiated by a redirect to PingOne.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> - User ID textField required
>
>   The user's PingOne user ID.
>
> - Authentication Methods dropdownWithCreate required
>
>   The authentication method that the user signed on with. For a dynamic value, select Use Custom Authentication Method and enter a value in the Custom Authentication Method field.
>
>   * Password-based authentication (pwd) (Default)
>
>   * Multiple-factor authentication (mfa)
>
>   * Use Custom Authentication Methods
>
>   * One-time password (otp)
>
>   * Risk-based authentication (rba)
>
>   * Confirmation using SMS (sms)
>
> - Custom Authentication Methods textField
>
>   The authentication method that the user signed on with, such as "pwd". Use the abbreviations from the Authentication Methods list or enter a custom value. Separate multiple values with a space, such as "pwd geo fpt".
>
> - Reduced Scopes textField
>
>   The scopes to request for the user, such as "openid email". This field allows you to request a limited subset of the original scopes. You cannot add any scopes that are not part of the original request. Separate multiple scopes with a space. Leave this blank to pass along all of the scopes from the original request.
>
> - * idTokenClaims selectNameValueListColumn
>   * accessTokenClaims selectNameValueListColumn
>   * Idle Timeout timeInterval
>
>   The amount of time that the session will remain valid after the user becomes inactive.
>
>   Default: `43200`
>
> * default object
>
>   * authentication object
>
>     * userId string
>
>     * methods array
>
>   * ip string
>
>   * policyId string
>
>   * sessionToken string
>
>   * parameters object
>
>   * properties object
>
>     * userId string
>
>     * identifiedDeviceId string
>
>     * authenticationMethods string
>
>     * customAuthenticationMethods string
>
>     * scopes string
>
>     * idTokenClaims array
>
>     * accessTokenClaims array
>
>     * idleTimeout number

### Return Success Response (Widget Flows)

Create a PingOne session and return the OIDC tokens to the originating web application. Use this to complete flows that are initiated within a widget in a web application.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Application dropDown
>
>   The PingOne OIDC application to use to create the session in PingOne. For a dynamic value, select Use Application ID and enter a value in the Application ID field.
>
>   * Use Application ID (Default)
>
> - Application ID textField required
>
>   The unique identifier for the application.
>
> - User ID textField required
>
>   The user's PingOne user ID.
>
> - Authentication Methods dropdownWithCreate required
>
>   The authentication method that the user signed on with. For a dynamic value, select Use Custom Authentication Method and enter a value in the Custom Authentication Method field.
>
>   * Password-based authentication (pwd) (Default)
>
>   * Multiple-factor authentication (mfa)
>
>   * Use Custom Authentication Methods
>
>   * One-time password (otp)
>
>   * Risk-based authentication (rba)
>
>   * Confirmation using SMS (sms)
>
> - Custom Authentication Methods textField
>
>   The authentication method that the user signed on with, such as "pwd". Use the abbreviations from the Authentication Methods list or enter a custom value. Separate multiple values with a space, such as "pwd geo fpt".
>
> - Reduced Scopes textField
>
>   The scopes to request for the user, such as "openid email". Leave this blank to request all scopes configured in the PingOne application, or enter a subset of the application scopes. Separate multiple scopes with a space.
>
> - * idTokenClaims selectNameValueListColumn
>   * accessTokenClaims selectNameValueListColumn
>   * Idle Timeout timeInterval
>
>   The amount of time that the session will remain valid after the user becomes inactive.
>
>   Default: `43200`
>
> - Additional Properties selectNameValueListColumn
>
>   Define any additional information to include in the response.
>
> - Additional Properties Name textField
>
>   The name of the property that contains the information defined in Additional Properties, such as "additionalProperties".
>
>   Default: `additionalProperties`
>
> * default object
>
>   * authentication object
>
>     * userId string
>
>     * methods array
>
>   * ip string
>
>   * policyId string
>
>   * sessionToken string
>
>   * properties object
>
>     * application string required
>
>     * applicationId string
>
>     * userId string
>
>     * identifiedDeviceId string
>
>     * authenticationMethods string
>
>     * customAuthenticationMethods string
>
>     * widgetScopes string
>
>     * idTokenClaims array
>
>     * accessTokenClaims array
>
>     * idleTimeout number
>
> - success boolean
>
> - access\_token string
>
> - token\_type string
>
> - expires\_in number
>
> - scope string
>
> - id\_token string
>
> - sessionToken string
>
> - sessionTokenMaxAge number
>
> - identifiedDeviceId string
>
> - additionalProperties object::

### Return Error Response (Redirect Flows)

Return error information to the source of the authentication request. Use this to complete flows that are initiated by a redirect to PingOne.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> - Custom Error Message toggleSwitch
>
>   When enabled, you can provide detailed error information in the fields below.
>
> - Error Message dropdownWithCreate
>
>   Returned in error field in query parameter
>
>   * invalid\_request
>
>   * invalid\_client
>
>   * invalid\_grant
>
>   * unauthorized\_client
>
>   * unsupported\_grant\_type
>
>   * invalid\_scope
>
> - * errorCode textField
>   * errorDescription textField
>   * errorReason textField
>
> * default object
>
>   * parameters object

### Check Session

Check whether the user has an active session in PingOne.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Valid Authentication Method dropdownWithCreate required
>
>   The check only passes if the user signed on with the selected authentication method. For a custom value, enter your authentication method reference value in the field, such as "kba" or "mca". This field does not support multiple values.
>
>   * Password-based authentication (pwd) (Default)
>
>   * Multiple-factor authentication (mfa)
>
>   * Any authentication method
>
>   * One-time password (otp)
>
>   * Risk-based authentication (rba)
>
>   * Confirmation using SMS (sms)
>
> - Last Sign On Was Within…​ timeInterval
>
>   The check only passes if the user signed on within this period of time.
>
>   Default: `480`
>
> * default object
>
>   * sessionToken string
>
>   * parameters object
>
>   * properties object
>
>     * checkSessionAuthenticator string required
>
>     * authenticationMethodLastUsedIn number
>
> - output object
>
>   * session object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * createdAt string
>
>     * activeAt string
>
>     * idleTimeoutInMinutes number
>
>     * lastSignOn object
>
>       * remoteIp string
>
>       * authenticators array
>
>     * expiresAt string

### Create or Update Session

Create or update an authentication session.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField required
>
>   The user's PingOne user ID.
>
> - Authentication Methods dropdownWithCreate required
>
>   The authentication method that the user signed on with. For a dynamic value, select Use Custom Authentication Method and enter a value in the Custom Authentication Method field.
>
>   * Password-based authentication (pwd) (Default)
>
>   * Multiple-factor authentication (mfa)
>
>   * Use Custom Authentication Methods
>
>   * One-time password (otp)
>
>   * Risk-based authentication (rba)
>
>   * Confirmation using SMS (sms)
>
> - Custom Authentication Methods textField
>
>   The authentication method that the user signed on with, such as "pwd". Use the abbreviations from the Authentication Methods list or enter a custom value. Separate multiple values with a space, such as "pwd geo fpt".
>
> - Idle Timeout timeInterval
>
>   The amount of time that the session will remain valid after the user becomes inactive.
>
>   Default: `43200`
>
> * default object
>
>   * authentication object
>
>     * userId string
>
>     * methods array
>
>   * ip string
>
>   * policyId string
>
>   * sessionToken string
>
>   * properties object
>
>     * userId string
>
>     * identifiedDeviceId string
>
>     * authenticationMethods string
>
>     * customAuthenticationMethods string
>
>     * idleTimeout number
>
> - output object
>
>   * session object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * createdAt string
>
>     * activeAt string
>
>     * idleTimeoutInMinutes number
>
>     * lastSignOn object
>
>       * remoteIp string
>
>       * authenticators array
>
>     * expiresAt string

### Delete Session

Delete an authentication session.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Soft Delete toggleSwitch
>
>   When enabled, PingOne signs the user out but does not delete the session.
>
> * default object
>
>   * sessionToken string
>
>   * properties object
>
>     * softDelete boolean
>
> - output object

### Sign On with External Identity Provider

Authenticate the user using an external identity provider configured in PingOne.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne External Identity Provider dropDown
>
>   Select an external identity provider from your PingOne environment.
>
>   * Use Identity Provider ID (Default)
>
> - PingOne External Identity Provider ID textField
>
>   The ID of an external identity provider from your PingOne environment, such as "df417355-adc4-2846-41f1-6f4b0b9bd12c".
>
> - Policy Purpose radioSelect required
>
>   Specify whether this policy is intended for users to authenticate at Microsoft via the OpenID Connect protocol or to fulfill the multi-factor authentication requirement as defined in Entra ID external authentication method.
>
>   * OIDC Authentication (Default)
>
>   * Entra ID External Authentication Method
>
> - ID Token Hint textField
>
>   ID token hint provided by Entra ID for step up authentication.
>
> - Link with PingOne User toggleSwitch
>
>   When enabled, DaVinci creates or updates a linked PingOne user account using attributes from the external IdP.
>
> - PingOne Population dropDown
>
>   The PingOne population to use when authenticating the user.
>
>   * Use Population ID (Default)
>
> - Population ID textField
>
>   The ID of the PingOne population to use when authenticating the user, such as "aa4b3e81-cf7e-8685-4b7b-7ec89cfcf7c8".
>
> - ACR Values textField
>
>   Enter the space-separated list of values to pass context to the IdP via OIDC.
>
> - Login Hint textField
>
>   Username to prepopulate at the external IdP.
>
> - Application Return to Url textField
>
>   When using the embedded flow player widget and an IdP/Social Login connector, provide a callback URL to return back to the application.
>
> - Requested Authentication Context textField
>
>   Enter the space-separated list of values to pass context to the IdP via SAML 2.0.
>
> - Authentication Context Reference radioSelect
>
>   Select the reference element to pass the context based on your agreement with the SAML IdP. The Requested Authentication Context field must be populated beforehand.
>
>   * AuthnContextClassRef
>
>   * AuthnContextDeclRef
>
> * default object
>
>   * properties object
>
>     * identityProvider string required minLength: 0 maxLength: 100
>
>       Identity Provider
>
>     * identityProviderId string minLength: 0 maxLength: 100
>
>       Identity Provider ID
>
>     * population string minLength: 0 maxLength: 100
>
>       Population
>
>     * populationId string minLength: 0 maxLength: 100
>
>       Population ID
>
>     * linkWithP1User boolean
>
>       Link with PingOne User
>
>     * acrValues string minLength: 0 maxLength: 300
>
>       ACR Values
>
>     * loginHint string minLength: 0 maxLength: 100
>
>       Login Hint
>
>     * policyPurpose string
>
>       Describes whether this flow will be used for Microsoft OIDC or for EAM
>
>     * idTokenHint string minLength: 0 maxLength: 10000
>
>       ID Token Hint provided by Entra ID
>
>     * returnUrl string minLength: 0 maxLength: 300
>
>       Return URL
>
>     * requestedAuthenticationContext string minLength: 0
>
>       Requested Authentication Context
>
>     * authenticationContextReference
>
>       Authentication Context Reference
>
> - output object
>
>   * isLinkedUser boolean
>
>   * user object
>
>     * preferredLanguage string
>
>     * timezone string
>
>     * lastSignOn object
>
>       * at string
>
>       * remoteIp string
>
>     * title string
>
>     * type string
>
>     * locale string
>
>     * enabled boolean
>
>     * identityProvider object
>
>       * id string
>
>       * type string
>
>     * lifecycle object
>
>       * status string
>
>     * createdAt string
>
>     * verifyStatus string
>
>     * nickname string
>
>     * mfaEnabled boolean
>
>     * id string
>
>     * email string
>
>     * updatedAt string
>
>     * memberOfGroupIDs string
>
>     * address object
>
>       * streetAddress string
>
>       * locality string
>
>       * region string
>
>       * postalCode string
>
>       * countryCode string
>
>     * externalId string
>
>     * photo object
>
>       * href string
>
>     * memberOfGroupNames string
>
>     * population object
>
>       * id string
>
>     * primaryPhone string
>
>     * accountId string
>
>     * mobilePhone string
>
>     * name object
>
>       * formatted string
>
>       * given string
>
>       * middle string
>
>       * family string
>
>       * honorificPrefix string
>
>       * honorificSuffix string
>
>     * account object
>
>       * canAuthenticate boolean
>
>       * status string
>
>       * lockedAt string
>
>       * secondsUntilUnlock string
>
>       * unlockAt string
>
>     * username string
>
>   * rawIdpAttributes object
>
>   * statusCode integer

### Verify User Code (Device Auth Flows)

Verify that a given user code exists.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField required
>
>   The user's PingOne user ID.
>
> - User Code textField required
>
>   The user code provided by the end user
>
> * default object
>
>   * properties object
>
>     * userId string required
>
>     * userCode string required
>
> - output object
>
>   * scope string
>
>   * appId string
>
>   * remoteIp string

### Authorize User Code (Device Auth Flows)

Grant a device access to a user's account. Should be done only after the user code has been verified and the scopes have been accepted by the user.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> - User Code textField required
>
>   The user code provided by the end user
>
> - User ID textField required
>
>   The user's PingOne user ID.
>
> - Authentication Methods dropdownWithCreate required
>
>   The authentication method that the user signed on with. For a dynamic value, select Use Custom Authentication Method and enter a value in the Custom Authentication Method field.
>
>   * Password-based authentication (pwd) (Default)
>
>   * Multiple-factor authentication (mfa)
>
>   * Use Custom Authentication Methods
>
>   * One-time password (otp)
>
>   * Risk-based authentication (rba)
>
>   * Confirmation using SMS (sms)
>
> - Custom Authentication Methods textField
>
>   The authentication method that the user signed on with, such as "pwd". Use the abbreviations from the Authentication Methods list or enter a custom value. Separate multiple values with a space, such as "pwd geo fpt".
>
> - Reduced Scopes textField
>
>   The scopes to request for the user, such as "openid email". This field allows you to request a limited subset of the original scopes. You cannot add any scopes that are not part of the original request. Separate multiple scopes with a space. Leave this blank to pass along all of the scopes from the original request.
>
> - * idTokenClaims selectNameValueListColumn
>   * accessTokenClaims selectNameValueListColumn
>   * Idle Timeout timeInterval
>
>   The amount of time that the session will remain valid after the user becomes inactive.
>
>   Default: `43200`
>
> * default object
>
>   * authentication object
>
>     * userId string
>
>     * methods array
>
>   * ip string
>
>   * policyId string
>
>   * sessionToken string
>
>   * properties object
>
>     * userCode string required
>
>     * userId string
>
>     * identifiedDeviceId string
>
>     * authenticationMethods string
>
>     * customAuthenticationMethods string
>
>     * scopes string
>
>     * idTokenClaims array
>
>     * accessTokenClaims array
>
>     * idleTimeout number

### Decline User Code (Device Auth Flows)

Deny a device access to a user's account. This should be done after the user code has been verified if the user does not consent to the requested scopes.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> - User Code textField required
>
>   The user code provided by the end user
>
> * default object
>
>   * properties object
>
>     * userCode string required

### Return CIBA Success

Indicate a user has completed an out-of-band authentication and authorization request. It should only be used in a PingOne CIBA flow.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> - User ID textField required
>
>   The user's PingOne user ID.
>
> - Authentication Methods dropdownWithCreate required
>
>   The authentication method that the user signed on with. For a dynamic value, select **Use Custom Authentication Method** and enter a value in the **Custom Authentication Method** field.
>
>   * Password-based authentication (pwd) (Default)
>
>   * Multiple-factor authentication (mfa)
>
>   * Use Custom Authentication Methods
>
>   * One-time password (otp)
>
>   * Risk-based authentication (rba)
>
>   * Confirmation using SMS (sms)
>
> - Custom Authentication Methods textField
>
>   The authentication method that the user signed on with, such as `pwd`. Use the abbreviations from the **Authentication Methods** list or enter a custom value. Separate multiple values with a space, such as `pwd geo fpt`.
>
> - Reduced Scopes textField
>
>   The scopes to request for the user, such as `openid email`. This field allows you to request a limited subset of the original scopes. You cannot add any scopes that are not part of the original request. Separate multiple scopes with a space. Leave this blank to pass along all of the scopes from the original request.
>
> - idTokenClaims selectNameValueListColumn
>
>   Additional claims to include in the ID token.
>
> - accessTokenClaims selectNameValueListColumn
>
>   Additional claims to include in the access token.
>
> - Idle Timeout timeInterval
>
>   The amount of time that the session remains valid after the user becomes inactive.
>
>   Default: `43200`
>
> * default object
>
>   * authentication object
>
>     * userId string
>
>     * methods array
>
>   * ip string
>
>   * policyId string
>
>   * sessionToken string
>
>   * parameters object
>
>   * properties object
>
>     * userId string
>
>     * identifiedDeviceId string
>
>     * authenticationMethods string
>
>     * customAuthenticationMethods string
>
>     * scopes string
>
>     * idTokenClaims array
>
>     * accessTokenClaims array
>
>     * idleTimeout number

### Return CIBA Error

Indicate a user has declined or failed to complete an out-of-band authentication and authorization request. It should only be used in a PingOne CIBA flow.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> - User ID textField required
>
>   The user's PingOne user ID.
>
> - Custom Error Message toggleSwitch
>
>   When enabled, you can provide detailed error information in the following fields.
>
> - Error Message dropdownWithCreate
>
>   Returned in error field in query parameter
>
>   * `invalid_request`
>
>   * `invalid_client`
>
>   * `invalid_grant`
>
>   * `unauthorized_client`
>
>   * `unsupported_grant_type`
>
>   * `invalid_scope`
>
> - errorCode textField
>
>   Technical error code that categorizes the failure.
>
> - errorDescription textField
>
>   Description of the error.
>
> - errorReason textField
>
>   Additional context describing the underlying cause of the error.
>
> * default object
>
>   * authentication object
>
>     * userId string
>
>   * parameters object
>
>   * properties object
>
>     * userId string