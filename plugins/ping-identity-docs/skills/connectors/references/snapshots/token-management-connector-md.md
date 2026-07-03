---
title: Token Management Connector
description: The Token Management connector lets you create and read JSON Web Token (JWT) tokens and manage OpenID Connect (OIDC) redirects in your PingOne DaVinci flow.
component: connectors
page_id: connectors::token_management_connector
canonical_url: https://docs.pingidentity.com/connectors/token_management_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  configuring-the-token-management-connector: Configuring the Token Management connector
  using-the-connector-in-a-flow: Using the connector in a flow
  token-creation: Token creation
  token-details: Token details
  validating-and-parsing-a-jwt-token: Validating and parsing a JWT token
  oidc-redirect-with-error: OIDC redirect with error
  capabilities: Capabilities
  create-tokens: Create Tokens
  create-tokens-with-custom-claims: Create Tokens with Custom Claims
  get-session-token-details: Get Session Token Details
  get-token-details: Get Token Details
  redirect-user-with-error: Redirect User with Error
  create-tokens-2: Create Tokens
---

# Token Management Connector

The Token Management connector lets you create and read JSON Web Token (JWT) *(tooltip: \<div class="paragraph">
\<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>
\</div>)* tokens and manage OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* redirects in your PingOne DaVinci flow.

You can use the Token Management connector to:

* Create ID, access, or JWT tokens.

* Get details about tokens.

* Redirect user with error.

## Setup

### Resources

Learn more in the following:

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Configuring the Token Management connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | This connector doesn't have a configuration at the environment level. You configure it in your flow instead. |

## Using the connector in a flow

### Token creation

The connector has several capabilities that allow you to create tokens:

* **Create Tokens with OIDC Redirect**

* **Create Tokens with Custom Claims**

* **Create Tokens without OIDC Redirect**

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Token details

The connector has several capabilities that allow you to get details about tokens:

* **Get Session Token Details**

* **Validate Token Details**

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Validating and parsing a JWT token

You can use the **Validate JWT Token** capability to parse and validate a JSON Web Token (JWT). The capability parses by getting the details, or claims, from the JWT token, such as the issuer, subject, or audience. Then, the capability validates by accepting the JWT token if it meets criteria, such as whether it has expired or if it has the correct issuer or audience.

If the validation rules are set and the JWT token passes, then the claims are parsed and output from the capability. If the validation rules are set and the JWT token fails, the flow continues down the False branch.

To validate a JWT token:

1. In your flow, add a **Token Management** connector with the **Validate JWT Token** capability.

2. In the **Token** field, enter the value or select the variable containing the JWT token to validate.

3. Select the **Public Key Type**. This field determines whether to provide a key directly from DaVinci, by pasting **Public Key PEM Contents**, or by pointing to a JWKS file by URL.

4. (Optional) Toggle the **Validate Expiration Time**. When enabled, the token must not be expired to be considered valid.

5. (Optional) Select which **Valid Algorithms** the token can be created from or select **Any**.

6. Enter any **Valid Issuers**, **Valid Subjects**, or **Valid Audiences** for the token to be considered valid. Click **Apply**.

### OIDC redirect with error

You can use the **Redirect User with Error** capability to redirect users with error.

No special configuration is needed. Add the capability and populate its properties according to the help text.

## Capabilities

### Create Tokens

ID/Access/Session JWT Tokens and OIDC Redirect

> **Collapse: Show details**
>
> * * Properties
>   * createSessionTokenFlag `toggleSwitch`
>   * Input Schema
>   * default `object`
>   * userInfo `object`
>   * skOpenId `object`
>   * domainPublicHost `string`

### Create Tokens with Custom Claims

ID/Access/Session JWT Tokens with Custom Claims and OIDC Redirect

> **Collapse: Show details**
>
> * * Properties
>   * claimsNameValuePairs `selectNameValueListColumn`
>   * idTokenExpiry `textField`
>   * claimsNameValuePairsAccessToken `selectNameValueListColumn`
>   * accessTokenExpiry `textField`
>   * createSessionTokenFlag `toggleSwitch`
>   * claimsNameValuePairsSessionToken `selectNameValueListColumn`
>   * sessionTokenExpiry `textField`
>   * customScopesFlag `toggleSwitch`
>   * customScopes `textField`
>   * customScopesSeparateField `toggleSwitch`
>   * customScopesSeparateFieldName `textField`
>   * encryptionFlag `toggleSwitch`
>   * encryptionKey `codeEditor`
>   * encryptionAlg `dropDown`
>   * encryptionContentAlg `dropDown`
>   * shadowUserNotPresentFlag `toggleSwitch`
>   * Input Schema
>   * default `object`
>   * userInfo `object`
>   * skOpenId `object`
>   * domainPublicHost `string`

### Get Session Token Details

Session Token claims are extracted from the JWT token

> **Collapse: Show details**
>
> * * Properties
>   * sessionTokenName `textField`
>
>   Default:
>
>   ```
>   sessionToken
>   ```
>
> * * sessionTokenLocation `dropDown`
>   * sessionToken `textField`
>   * resolveToUser `toggleSwitch`
>   * Input Schema
>   * default `object`
>   * type `object`
>   * Output Schema
>   * output `object`
>   * claims `object`
>   * properties `object`
>   * sub `string`
>   * aud `string`
>   * iss `string`
>   * usage `string`
>   * loa `number`
>   * scope `string`
>   * jti `string`
>   * iat `number`
>   * exp `number`

### Get Token Details

Claims are extracted from any JWT token signed by DaVinci

> **Collapse: Show details**
>
> * * Properties
>   * genericToken `textField`
>   * errorOnExpiry `toggleSwitch`
>   * Input Schema
>   * default `object`
>   * type `object`
>   * Output Schema
>   * output `object`
>   * claims `object`
>   * properties `object`
>   * sub `string`
>   * aud `string`
>   * iss `string`
>   * usage `string`
>   * loa `number`
>   * scope `string`
>   * jti `string`
>   * iat `number`
>   * exp `number`

### Redirect User with Error

Redirect user to RP with standard/customized error

> **Collapse: Show details**
>
> * * Properties
>   * customErrorFlag `toggleSwitch`
>   * errorMessage `textField`
>   * errorDescription `textField`
>   * errorCode `textField`
>   * errorReason `textField`
>   * Input Schema
>   * default `object`
>   * skOpenId `object`

### Create Tokens

Create Tokens (without any OIDC Redirect).

> **Collapse: Show details**
>
> * * Properties
>   * createIdTokenFlag `toggleSwitch`
>   * claimsNameValuePairs `selectNameValueListColumn`
>   * idTokenExpiry `textField`
>   * createAccessTokenFlag `toggleSwitch`
>   * claimsNameValuePairsAccessToken `selectNameValueListColumn`
>   * accessTokenExpiry `textField`
>   * createSessionTokenFlag `toggleSwitch`
>   * claimsNameValuePairsSessionToken `selectNameValueListColumn`
>   * sessionTokenExpiry `textField`
>   * customScopesFlag `toggleSwitch`
>   * customScopes `textField`
>   * customScopesSeparateField `toggleSwitch`
>   * customScopesSeparateFieldName `textField`
>   * Input Schema
>   * default `object`
>   * userInfo `object`
>   * skOpenId `object`
>   * domainPublicHost `string`
>   * Output Schema
>   * output `object`
>   * access\_token `string`
>   * id\_token `string`
>   * session\_token `string`
