---
title: SAML IdP Connector
description: Configure the SAML IdP connector to authenticate users with a SAML identity provider in your PingOne DaVinci flow
component: connectors
page_id: connectors::saml_connector
canonical_url: https://docs.pingidentity.com/connectors/saml_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-saml-idp-connector: Configuring the SAML IdP connector
  connector-configuration: Connector configuration
  pingone-davinci-saml-sp-metadata-url: PingOne DaVinci SAML SP Metadata URL
  identity-provider-saml-metadata: Identity Provider SAML Metadata
  application-redirect-url: Application Redirect URL
  using-the-connector-in-a-flow: Using the connector in a flow
  authenticating-users: Authenticating users
  capabilities: Capabilities
  loginFirstFactor: Sign On with SAML Identity Provider
  loginFirstFactorConnectionId: Sign On with SAML Identity Provider (Dynamic)
---

# SAML IdP Connector

The Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">
\<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>
\</div>)* IdP connector lets you authenticate users with a SAML IdP-based identity provider in your PingOne DaVinci flow.

SAML 2.0 is a well-supported standard for authentication and authorization. You can use this connector to show a customizable sign-on button that allows your users to authenticate with your organization's SAML IdP identity provider.

## Setup

### Resources

Learn more in the following:

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need administrator access to your identity provider's SAML IdP configuration.

### Configuring the SAML IdP connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

|   |                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------- |
|   | Consult your identity provider's documentation for help finding and configuring your SAML IdP settings. |

##### PingOne DaVinci SAML SP Metadata URL

Your PingOne DaVinci SAML IdP SP Metadata URL. This allows an identity provider to redirect the browser back to PingOne DaVinci. Enter this URL in your provider's SAML IdP configuration.

##### Identity Provider SAML Metadata

This field accepts the SAML IdP metadata provided by your identity provider. This information should be available in your identity provider's SAML IdP configuration.

|   |                                                                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The connector does not support the following in the **Identity Provider SAML Metadata** field:- The `md:` prefix, which is associated with the SAML Metadata specification

- The `ds:` prefix, which is associated with the XML Digital Signature specification

- The `xmlns` attribute in the `EntityDescriptor`, which is associated with XML Namespace. |

##### Application Redirect URL

Your application's redirect URL, such as `https://app.yourorganization.com/`. Enter this URL if you [embed the PingOne DaVinci widget in your application](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launching_a_flow_with_the_widget.html). This allows PingOne DaVinci to redirect the browser back to your application.

## Using the connector in a flow

### Authenticating users

The **Sign On with SAML Identity Provider** capability lets you show a customizable sign-on button in your flow. When a user clicks this button, the connector sends a SAML authentication request to your configured SAML provider.

You can configure standard SAML parameters, such as `relayState` and `notBeforeSkew`. For help with these, consult your preferred SAML documentation.

No special configuration is needed. Add the capability and populate its properties according to the help text.

## Capabilities

### Sign On with SAML Identity Provider

Authenticate the user with an identity provider that supports SAML.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - - Display Name button
>   - signRequest toggleSwitch
>
>   When enabled, DaVinci signs the SAML request using the X.509 certificate. The certificate is provided to the identity provider through the DaVinci SAML SP Metadata URL, which is available in the connector settings.
>
> - nameIdFormat dropDown
>
>   Select the name format used by the identity provider.
>
> - Force Authentication toggleSwitch
>
>   When enabled, the user must re-authenticate even if they have an existing session. Enable this for high-value and high-risk transactions.
>
> - Authentication Context Class Reference textArea
>
>   The Context Class Reference to use for the transaction, such as "{ "comparison": "exact", "class\_refs": \["urn:oasis:names:tc:SAML:2.0:ac:classes:Password"] }". This allows you to define the type of authentication required for the transaction.
>
> - requireSessionIndex toggleSwitch
>
>   When enabled, a unique session identifier is carried through the authentication process and allows DaVinci to identify the user's session. Enable this for improved security.
>
> - Allow Unencrypted Assertions toggleSwitch
>
>   When enabled, DaVinci accepts SAML assertions from the identity provider that are not encrypted. Only enable this for low-risk transactions in an environment where encryption is not possible.
>
> - RelayState Parameter textField
>
>   Optional information to include when sending the SAML request to the identity provider, formatted as a URL. This information is included in the response from the identity provider.
>
> - Audience Parameter textField
>
>   The audience value to provide in the SAML request, such as "https\://sp.example.com". This value must match one of the audiences listed in the SAML assertion. When this field is blank, the connector uses the DaVinci entity ID.
>
> - NotBeforeSkew Parameter textField
>
>   The allowable difference in time between when a SAML assertion becomes valid and the current time, in seconds. Use this to accommodate for differences in clock time between systems.
>
> - * showPoweredBy toggleSwitch
>   * skipButtonPress toggleSwitch
>
> * output object
>
>   * rawResponse object
>
>     * response\_header object
>
>       * version string
>
>       * destination string
>
>       * in\_response\_to string
>
>       * id string
>
>     * type string
>
>     * user object
>
>       * name\_id string
>
>       * session\_index string
>
>       * given\_name string
>
>       * surname string
>
>       * email string
>
>       * name string
>
>       * attributes object
>
>         * tenantid string
>
>         * objectidentifier string
>
>         * displayname string
>
>         * identityprovider string
>
>         * authnmethodsreferences array
>
>         * givenname string
>
>         * surname string
>
>         * emailaddress string
>
>         * name string
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "response_header": {
>       "version": "2.0",
>       "destination": "https://devapi.singularkey.com/auth/i7LnlNrP7eFpLTNxw7fMTHb/saml2/assert",
>       "in_response_to": "_fa95d1e27c6adf712baaf3d875eb4b21b4cb28940c",
>       "id": "_d7d681de-d33f-4e01-9bdf-49ec28eaa63b"
>     },
>     "type": "authn_response",
>     "user": {
>       "name_id": "joe_singularkey.com#EXT#_joesingularkey.onmicrosYPBIZ#EXT#@singularkeyb2c.onmicrosoft.com",
>       "session_index": "_d093086e-36bc-4dfd-b9eb-23d97032b800",
>       "given_name": "joe@singularkey.com",
>       "surname": "Smith",
>       "email": "joe@singularkey.com",
>       "name": "joe_singularkey.com#EXT#_joesingularkey.onmicrosYPBIZ#EXT#@singularkeyb2c.onmicrosoft.com",
>       "attributes": {
>         "tenantid": "06d45dd3-d5ac-498c-bf2c-78b17e619b3e",
>         "objectidentifier": "e48b41d4-7f30-4bec-a071-19ce0528adaf",
>         "displayname": "joe@singularkey.com Smith",
>         "identityprovider": "live.com",
>         "authnmethodsreferences": [
>           "http://schemas.microsoft.com/ws/2008/06/identity/authenticationmethod/password",
>           "http://schemas.microsoft.com/ws/2008/06/identity/authenticationmethod/unspecified"
>         ],
>         "givenname": "joe@singularkey.com",
>         "surname": "Smith",
>         "emailaddress": "joe@singularkey.com",
>         "name": "joe_singularkey.com#EXT#_joesingularkey.onmicrosYPBIZ#EXT#@singularkeyb2c.onmicrosoft.com"
>       }
>     }
>   }
> }
> ```

### Sign On with SAML Identity Provider (Dynamic)

Authenticate the user with an identity provider that supports SAML. Use a different connector based on a variable from the flow.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - - Display Name button
>   - ID of SAML IdP Connection textField
>
>   The ID of another DaVinci SAML connector instance, such as "f33f64e40bcf79c2ce86ad0dcc563457". Populate this with a variable to dynamically change which SAML connector is used based on the context of the flow.
>
> - signRequest toggleSwitch
>
>   When enabled, DaVinci signs the SAML request using the X.509 certificate. The certificate is provided to the identity provider through the DaVinci SAML SP Metadata URL, which is available in the connector settings.
>
> - RelayState Parameter textField
>
>   Optional information to include when sending the SAML request to the identity provider, formatted as a URL. This information is included in the response from the identity provider.
>
> - nameIdFormat dropDown
>
>   Select the name format used by the identity provider.
>
> - Force Authentication toggleSwitch
>
>   When enabled, the user must re-authenticate even if they have an existing session. Enable this for high-value and high-risk transactions.
>
> - Authentication Context Class Reference textArea
>
>   The Context Class Reference to use for the transaction, such as "{ "comparison": "exact", "class\_refs": \["urn:oasis:names:tc:SAML:2.0:ac:classes:Password"] }". This allows you to define the type of authentication required for the transaction.
>
> - requireSessionIndex toggleSwitch
>
>   When enabled, a unique session identifier is carried through the authentication process and allows DaVinci to identify the user's session. Enable this for improved security.
>
> - Allow Unencrypted Assertions toggleSwitch
>
>   When enabled, DaVinci accepts SAML assertions from the identity provider that are not encrypted. Only enable this for low-risk transactions in an environment where encryption is not possible.
>
> - Audience Parameter textField
>
>   The audience value to provide in the SAML request, such as "https\://sp.example.com". This value must match one of the audiences listed in the SAML assertion. When this field is blank, the connector uses the DaVinci entity ID.
>
> - NotBeforeSkew Parameter textField
>
>   The allowable difference in time between when a SAML assertion becomes valid and the current time, in seconds. Use this to accommodate for differences in clock time between systems.
>
> - * showPoweredBy toggleSwitch
>   * skipButtonPress toggleSwitch
>
> * output object
>
>   * rawResponse object
>
>     * response\_header object
>
>       * version string
>
>       * destination string
>
>       * in\_response\_to string
>
>       * id string
>
>     * type string
>
>     * user object
>
>       * name\_id string
>
>       * session\_index string
>
>       * given\_name string
>
>       * surname string
>
>       * email string
>
>       * name string
>
>       * attributes object
>
>         * tenantid string
>
>         * objectidentifier string
>
>         * displayname string
>
>         * identityprovider string
>
>         * authnmethodsreferences array
>
>         * givenname string
>
>         * surname string
>
>         * emailaddress string
>
>         * name string
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "response_header": {
>       "version": "2.0",
>       "destination": "https://devapi.singularkey.com/auth/i7LnlNrP7eFpLTNxw7fMTHb/saml2/assert",
>       "in_response_to": "_fa95d1e27c6adf712baaf3d875eb4b21b4cb28940c",
>       "id": "_d7d681de-d33f-4e01-9bdf-49ec28eaa63b"
>     },
>     "type": "authn_response",
>     "user": {
>       "name_id": "joe_singularkey.com#EXT#_joesingularkey.onmicrosYPBIZ#EXT#@singularkeyb2c.onmicrosoft.com",
>       "session_index": "_d093086e-36bc-4dfd-b9eb-23d97032b800",
>       "given_name": "joe@singularkey.com",
>       "surname": "Smith",
>       "email": "joe@singularkey.com",
>       "name": "joe_singularkey.com#EXT#_joesingularkey.onmicrosYPBIZ#EXT#@singularkeyb2c.onmicrosoft.com",
>       "attributes": {
>         "tenantid": "06d45dd3-d5ac-498c-bf2c-78b17e619b3e",
>         "objectidentifier": "e48b41d4-7f30-4bec-a071-19ce0528adaf",
>         "displayname": "joe@singularkey.com Smith",
>         "identityprovider": "live.com",
>         "authnmethodsreferences": [
>           "http://schemas.microsoft.com/ws/2008/06/identity/authenticationmethod/password",
>           "http://schemas.microsoft.com/ws/2008/06/identity/authenticationmethod/unspecified"
>         ],
>         "givenname": "joe@singularkey.com",
>         "surname": "Smith",
>         "emailaddress": "joe@singularkey.com",
>         "name": "joe_singularkey.com#EXT#_joesingularkey.onmicrosYPBIZ#EXT#@singularkeyb2c.onmicrosoft.com"
>       }
>     }
>   }
> }
> ```