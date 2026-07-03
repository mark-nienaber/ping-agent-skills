---
title: Agentless Integration Kit
description: The Agentless Integration Kit allows PingFederate to integrate with identity provider (IdP) and service provider (SP) applications for single sign-on (SSO).
component: agentless
page_id: agentless::pf_agentless_ik
canonical_url: https://docs.pingidentity.com/integrations/agentless/pf_agentless_ik.html
revdate: March 7, 2025
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Agentless Integration Kit

The Agentless Integration Kit allows PingFederate to integrate with identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* and service provider (SP) *(tooltip: \<div class="paragraph">
\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
\</div>)* applications for single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*.

This integration uses a RESTful approach that doesn't require you to integrate agent software into your application. Instead, your application exchanges user-session attributes with PingFederate through direct HTTP calls to the adapter endpoints.

The Reference ID IdP Adapter can also redirect OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)* authorization consent requests to an external application, as described in [External consent approval](custom_application_setup/pf_agentless_ik_external_consent_approval.html).

## Components

* Reference ID IdP Adapter

  Allows PingFederate to integrate with IdP applications for SSO.

* Reference ID SP Adapter

  Allows PingFederate to integrate with SP applications for SSO.

* Agentless IdP Java sample application

  An example IdP application that you can use to test the IdP adapter.

* Agentless SP Java sample application

  An example SP application that you can use to test the SP adapter.

|   |                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The sample applications included in the integration `.zip` archive are built with Java. You can find sample applications built with other languages, such as .NET Core, PHP, and Python, and get the latest version of the Java sample applications in the [Ping Identity GitHub repository](https://github.com/pingidentity?q=agentless). |

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, you can find more information in the following sections of the PingFederate documentation:

* [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

* [Managing SP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_adaptermanagementtasklet_spadaptermanagementstate.html)

* [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

## System requirements

* PingFederate 11.3 or later

* Your application must be web-based and able to do the following:

  * Make REST API calls to PingFederate

  * Store a reference ID, resume path, and other values

---

---
title: Agentless Integration Kit Changelog
description: The following is the change history for the Agentless Integration Kit.
component: agentless
page_id: agentless:release_notes:pf_agentless_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/agentless/release_notes/pf_agentless_ik_changelog.html
revdate: February 23, 2026
section_ids:
  version-2-3-1: Version 2.3.1
  version-2-3: Version 2.3
  version-2-2-1: Version 2.2.1
  version-2-2: Version 2.2
  version-2-1: Version 2.1
  version-2-0-4: Version 2.0.4
  version-2-0-3: Version 2.0.3
  version-2-0-2: Version 2.0.2
  version-2-0-1: Version 2.0.1
  version-2-0: Version 2.0
  version-1-5-4: Version 1.5.4
  version-1-5-3: Version 1.5.3
  version-1-5-2: Version 1.5.2
  version-1-5-1: Version 1.5.1
  version-1-5: Version 1.5
  version-1-4-1: Version 1.4.1
  version-1-4: Version 1.4
  version-1-3-3: Version 1.3.3
  version-1-3-2: Version 1.3.2
  version-1-3-1: Version 1.3.1
  version-1-3: Version 1.3
  version-1-2-1: Version 1.2.1
  version-1-2: Version 1.2
  version-1-1: Version 1.1
  version-1-0: Version 1.0
---

# Agentless Integration Kit Changelog

The following is the change history for the Agentless Integration Kit.

## Version 2.3.1

Released in February 2026.

* Fixed an issue that could have caused `500` errors if both:

  * The **Preserve JSON** checkbox was selected in the [Reference ID IdP adapter configuration](../custom_application_setup/pf_agentless_ik_reference_id_idp_adapter_settings_reference.html).

  * A tracked HTTP parameter or chained attribute included a JSON array.

## Version 2.3

Released in November 2025.

* Added stricter enforcement for wildcard matching in the **Allowed Subject DN** and **Allowed Issuer DN** fields.

  Learn more in [Reference ID IdP Adapter settings reference](../custom_application_setup/pf_agentless_ik_reference_id_idp_adapter_settings_reference.html) and [Reference ID SP Adapter settings reference](../custom_application_setup/pf_agentless_ik_reference_id_sp_adapter_settings_reference.html).

* Updated the code to fix improper encoding and prevent information leaks in HTTP responses.

## Version 2.2.1

Released in May 2025.

* Fixed an issue that prevented the adapter configuration from supporting exclusive and dynamic scopes in Bearer access token authentication flow.

* Fixed an issue where certificate details were not correctly logged during certificate authentication failures.

* Updated the adapter to ensure proper validation behavior when only Bearer token authentication is configured.

## Version 2.2

Released in April 2025.

* Fixed an issue that caused null attributes to be excluded from the response of the pickup API endpoint and added the **Include Null Attributes** checkbox to the adapter configuration. Learn more in [Overview of the service provider SSO flow](../pf_agentless_ik_overview_of_the_service_provider_sso_flow.html), [Overview of the identity provider SSO flow](../overview_of_the_identity_provider_integration/pf_agentless_ik_overview_of_the_identity_provider_sso_flow.html), [Reference ID IdP Adapter settings reference](../custom_application_setup/pf_agentless_ik_reference_id_idp_adapter_settings_reference.html), and [Reference ID SP Adapter settings reference](../custom_application_setup/pf_agentless_ik_reference_id_sp_adapter_settings_reference.html).

* Added the ability to preserve the JSON format of chained attribute and tracked HTTP parameter values. Learn more in [Reference ID IdP Adapter settings reference](../custom_application_setup/pf_agentless_ik_reference_id_idp_adapter_settings_reference.html).

## Version 2.1

Released in March 2025.

* Added the ability to use Bearer token authentication as an authentication method.

  Learn more in [Authentication methods](../custom_application_setup/pf_agentless_ik_authentication_methods.html) and refer to the **Access Token Manager** - **Required Bearer Access Token Scopes** fields in [Reference ID IdP Adapter settings reference](../custom_application_setup/pf_agentless_ik_reference_id_idp_adapter_settings_reference.html) and [Reference ID SP Adapter settings reference](../custom_application_setup/pf_agentless_ik_reference_id_sp_adapter_settings_reference.html).

## Version 2.0.4

Released in November 2021.

* Fixed an issue that caused the adapter to incorrectly handle integers in JSON payloads.

* Fixed an issue that caused the adapter to incorrectly handle multi-value attributes in PingFederate 10 and later.

* Verified that the Reference ID IdP Adapter is compliant with US Federal Information Processing Standards (FIPS). Learn more in [Integrating Bouncy Castle FIPS providers](https://docs.pingidentity.com/pingfederate/latest/getting_started_with_pingfederate/pf_set_up_java8_java11.html) in the PingFederate documentation.

## Version 2.0.3

Released in June 2021.

* Fixed an issue with client certificate authentication handling. Learn more in security bulletin [SECADV025](https://support.pingidentity.com/s/article/SECADV025-Agentless-Integration-Kit-Client-Certificate-Authentication-Mishandling) (requires sign-on).

## Version 2.0.2

Released in May 2021.

* Improved the description for the **Relax Pass Phrase Requirements** setting.

* Fixed an issue that caused the adapter to format multi-value attributes incorrectly.

* Fixed an issue that could cause a validation error in the **Logout Service Endpoint** field when upgrading the adapter.

## Version 2.0.1

Released in September 2020.

* Fixed an issue that prevented an error from triggering when the wrong REF ID was provided.

## Version 2.0

Released in August 2020.

* Added the **Send Request Parameters** setting to control the information sent in query parameter mode.

* Added validation to the **Pass Phrase** field to enforce strong passwords.

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Improved support for applications that do not maintain sessions. In the adapter configuration, the **Logout Mode** setting includes a **None** option.

* Improved debug log entries to show the adapter instance ID more clearly.

* Improved info log entries to show invalid reference ID errors.

* Created new Java, .NET Core, PHP, and Python sample applications and example code. Learn more in the [Ping Identity GitHub repository](https://github.com/pingidentity?q=agentless).

## Version 1.5.4

Released in March 2020.

* Added support for header names with dashes at the attribute pick up and dropoff endpoints.

* Fixed an issue that could cause a PingFederate engine node to stop responding on configuration reload.

* Fixed an issue that caused multi-valued attributes to be treated as a single string.

* Fixed an issue that caused the drop-off endpoint to return HTML when an error occurred.

## Version 1.5.3

Released in January 2020.

* Fixed an issue that prevented the adapter from correctly linking federated users to application users.

* Removed `date` from the adapter response.

* Improved error messages.

* Improved default values for some adapter configuration fields.

## Version 1.5.2

Released in July 2019.

* Improved the query parameter transport mode. It now passes query parameters to the authentication endpoint.

## Version 1.5.1

Released in February 2019.

* Included all-new sample applications in the distribution file. You can find the latest source code in [PingFederate Agentless Integration Kit Sample](https://github.com/pingidentity/pf-agentless-ik-sample) on the Ping Identity GitHub page.

* Fixed a bug that caused an invalid content-type header value in some API responses.

## Version 1.5

Released in December 2018.

* Added the ability to direct authorization consent requests to an external application. Learn more in [External consent approval](../custom_application_setup/pf_agentless_ik_external_consent_approval.html).

* Added support for virtual host names in the Reference ID Adapter. Learn more in the [Configuring virtual host names](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managevirtualhostnamestasklet_virtualhostnamesstate.html) section of the PingFederate documentation.

* Fixed a cross-site scripting (XSS) issue. Learn more in security bulletin [SECBL013](https://support.pingidentity.com/s/article/SECBL013-Agentless-Integration-Kit-Cross-Site-Scripting-XSS-Vulnerability) (requires sign-on).

## Version 1.4.1

Released in November 2018.

* Improved the way Reference ID Adapter instance configurations are applied. Configuration changes now take effect without the need to restart PingFederate.

## Version 1.4

Released in September 2018.

* Reference ID IdP Adapter

  * Added the capability to prefix attribute keys with source information.

  * Added support for tracked parameters, a feature in the upcoming release ofPingFederate Server 9.2.

  * Added the ability to ignore untracked HTTP parameters.

  * Added support for JSON object based claims inside signed JWT request object.

* Reference ID IdP and SP Adapter

  * Improved logging for back-channel authentication failures.

  * Improved support for authentication method based on configured values.

## Version 1.3.3

Released in August 2018.

* Fixed issue with HTTP request parameters overriding signed JWT request parameter values.

* Target resource validation and error resource validation are now enabled in the sample configuration archive.

## Version 1.3.2

Released in April 2018.

* Fixed issue processing JSON-based request object claims.

* Fixed incorrect Content-Type header in Reference ID Adapter endpoint responses.

* Fixed data encoding issue with Form POST-based front-channel communication.

## Version 1.3.1

Released in September 2017.

* Fixed issue with exposing attributes to the IdP authentication endpoint.

## Version 1.3

Released in August 2017.

* Compatibility updates for JDK 8.

* Added support for exposing attributes to the IdP authentication endpoint.

* Added support for multi-value attributes.

## Version 1.2.1

Released in January 2016.

* Updated sample application data archive

## Version 1.2

Released in September 2012.

* Added two Transport Mode options (Query Parameter or Form Post) for Front Channel Communication for both the IdP and SP Reference ID Adapter.

* Added an authentication endpoint for the SP Adapter, which enables end-user redirection for authentication.

* Added Sample IdP/SP applications to the distribution. Sample applications provide a way to test an end-to-end identity provider (IdP) and service provider (SP) integration with PingFederate using the Agentless Integration Kit.

* Added the Certificate DN Compare Fix in the Agentless Integration Kit.

## Version 1.1

Released in November 2011.

* Support for multiple client certificates in a single Reference ID Adapter instance for client-certificate authentication.

* Allowed Subject DN and Allowed Issuer DN can be configured independently of each other.

* Basic authentication is no longer required when using client-certificate authentication.

* HTTP Header `ping.instanceId` is optional when a single Reference ID Adapter instance is configured.

* (Bug Fix) Unfound reference attribute association no longer returns a `Null Pointer Exception` error.

* Fixed an account linking issue with the Reference ID Adapter.

## Version 1.0

Released in October 2010.

* Initial Release.

---

---
title: Attribute drop-off process
description: To drop off user attributes to PingFederate, configure your application to authenticate itself, provide the encoded attributes, and store a reference ID from the response.
component: agentless
page_id: agentless:custom_application_setup:pf_agentless_ik_attribute_drop_off_process
canonical_url: https://docs.pingidentity.com/integrations/agentless/custom_application_setup/pf_agentless_ik_attribute_drop_off_process.html
revdate: June 7, 2024
section_ids:
  providing-the-user-attributes: Providing the user attributes
  parsing-the-reference-id-from-the-response: Parsing the reference ID from the response
---

# Attribute drop-off process

To drop off user attributes to PingFederate, configure your application to authenticate itself, provide the encoded attributes, and store a reference ID from the response.

![A diagram showing an overview of the attribute drop-off process.](_images/wzf1646074412793.png)

## Providing the user attributes

Configure your application to make an HTTP POST call to the Reference ID Adapter dropoff endpoint:

```
https://pf_host:pf_port/ext/ref/dropoff
```

In the call, provide the following:

* Authentication credentials, if you are using the HTTP Basic or HTTP header authentication. Learn more in [Authentication methods](pf_agentless_ik_authentication_methods.html).

* The ID of the Reference ID Adapter instance.

* The user attributes.

PingFederate expects the attributes to be encoded as a JSON object or as query parameters in the URL, depending on the **Incoming Attribute Format** setting in your adapter instance configuration.

Example code:

```
// Drop the attributes into PingFederate
String dropoffLocation = "https://localhost:9031/ext/ref/dropoff";
System.out.println(dropoffLocation);
URL dropUrl = new URL(dropoffLocation);
URLConnection urlConnection = dropUrl.openConnection();
HttpsURLConnection httpsURLConnection = (HttpsURLConnection)urlConnection;
httpsURLConnection.setSSLSocketFactory(socketFactory);
urlConnection.setRequestProperty("ping.uname", "changeme"); urlConnection.setRequestProperty("ping.pwd", "this is a default example and should not be used in production"); urlConnection.setRequestProperty("ping.instanceId", "idpadapter");

// Write the attributes in URL Connection, this example uses UTF-8 encoding
urlConnection.setDoOutput(true);
OutputStreamWriter outputStreamWriter = new OutputStreamWriter(urlConnection.getOutputStream(), StandardCharsets.UTF_8);
idpUserAttributes.writeJSONString(outputStreamWriter);
outputStreamWriter.flush();
outputStreamWriter.close();
```

## Parsing the reference ID from the response

The response from PingFederate includes a newly-generated reference ID associated with the attributes it received. You will use this `REF` value later in the authentication flow.

Example response:

```
HTTP/1.1 200 OK

{
"REF":"54321"
}
```

Configure your application to parse the response and store the reference ID.

Example code:

```
// Get the response and parse it into a JSON object
InputStream is = urlConnection.getInputStream();
InputStreamReader streamReader = new InputStreamReader(is, StandardCharsets.UTF_8);

JSONParser parser = new JSONParser();
JSONObject jsonRespObj = (JSONObject)parser.parse(streamReader);

// Grab the value of the reference Id from the JSON Object. This value
// must be passed to {pingfed} on resumePath as the parameter 'REF'
String referenceValue = (String)jsonRespObj.get("REF");
System.out.println("Reference ID = " + referenceValue);
```

---

---
title: Attribute formatting
description: Attribute formatting specifies how attribute names and values are passed between the application and PingFederate. To set the incoming and outgoing attribute formats, see the Advanced Fields section of the adapter instance configuration.
component: agentless
page_id: agentless:custom_application_setup:pf_agentless_ik_attribute_formatting
canonical_url: https://docs.pingidentity.com/integrations/agentless/custom_application_setup/pf_agentless_ik_attribute_formatting.html
revdate: February 8, 2022
section_ids:
  incoming-attributes: Incoming attributes
  outgoing-attributes: Outgoing attributes
---

# Attribute formatting

Attribute formatting specifies how attribute names and values are passed between the application and PingFederate. To set the incoming and outgoing attribute formats, see the **Advanced Fields** section of the adapter instance configuration.

By default, PingFederate uses JSON to format incoming and outgoing attributes.

## Incoming attributes

Incoming attribute formatting specifies how attributes are encoded into the HTTP request from the application to the PingFederate dropoff endpoint. Learn more in [Reference ID Adapter endpoints](pf_agentless_ik_reference_id_adapter_endpoints.adoc.html).

**Incoming attribute formats**

| Format          | Details                                                       |
| --------------- | ------------------------------------------------------------- |
| JSON            | Attributes are encoded according to the JSON data model.      |
| Query parameter | Attributes are encoded as query string parameters in the URL. |

## Outgoing attributes

Outgoing attribute formatting specifies how attributes are encoded into the HTTP response from PingFederate to the application at the pickup endpoint.

**Outgoing attribute formats**

| Format     | Details                                                           |
| ---------- | ----------------------------------------------------------------- |
| JSON       | Attributes are encoded according to the JSON data model.          |
| Properties | Attributes are encoded by using the `java.util.Properties` class. |

---

---
title: Attribute pickup process
description: To pick up user attributes from PingFederate, configure your application to authenticate itself, provide the reference ID, and store the user attributes from the response. This lets you get the user information needed to create a session in your application.
component: agentless
page_id: agentless:custom_application_setup:pf_agentless_ik_attribute_pickup_process
canonical_url: https://docs.pingidentity.com/integrations/agentless/custom_application_setup/pf_agentless_ik_attribute_pickup_process.html
revdate: June 7, 2024
section_ids:
  requesting-the-user-attributes: Requesting the user attributes
  parsing-the-attributes-from-the-response: Parsing the attributes from the response
---

# Attribute pickup process

To pick up user attributes from PingFederate, configure your application to authenticate itself, provide the reference ID, and store the user attributes from the response. This lets you get the user information needed to create a session in your application.

![A diagram showing an overview of the attribute pickup process.](_images/oev1646074325585.png)

## Requesting the user attributes

Configure your application to make an HTTP GET call to the Reference ID Adapter pickup endpoint:

```
https://pf_host:pf_port/ext/ref/pickup
```

In the call, provide the following:

* The `REF` value.

* Authentication credentials, if you are using the HTTP Basic or HTTP header authentication. Learn more in [Authentication methods](pf_agentless_ik_authentication_methods.html).

* The ID of the Reference ID Adapter instance.

Example code:

```
// Call back to PF to get the attributes associated with the reference
String pickupLocation = "https://localhost:9031/ext/ref/pickup?REF=" + referenceValue;
System.out.println(pickupLocation);
URL pickUrl = new URL(pickupLocation);
URLConnection urlConn = pickUrl.openConnection();
HttpsURLConnection httpsURLConn = (HttpsURLConnection)urlConn;
httpsURLConn.setSSLSocketFactory(socketFactory);
urlConn.setRequestProperty("ping.uname", "changeme"); urlConn.setRequestProperty("ping.pwd", "please change me before you go into production!"); urlConn.setRequestProperty("ping.instanceId", "spadapter");
```

## Parsing the attributes from the response

The response from PingFederate includes user attributes from earlier in the authentication flow. They are encoded as a JSON object or as properties using the `java.util.Properties` class.

|   |                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Your adapter instance configuration determines which attributes are included in the response and how they are formatted. See the **Send Request Parameters** and **Outgoing Attribute Format** settings. |

Example response:

```
HTTP/1.1 200 OK
{
"authnCtx":"urn:oasis:names:tc:SAML:2.0:ac:classes:unspecified",
"partnerEntityID":"company:saml20:idp",
"subject":"jsmith",
"instanceId":"sample_adapter",
"sessionid":"sFMcTOaropYv5gYQZi1ZOpX7DZ8",
"authnInst":"2013-03-28 20:42:10-0500"
}
```

Configure your application to parse the response and store the user attributes.

Example code:

```
// Get the response and parse it into another JSON object which are the 'user attributes'.
// This example uses UTF-8 if encoding is not found in request.
String encoding = urlConn.getContentEncoding();
InputStream is = urlConn.getInputStream();
InputStreamReader streamReader = new InputStreamReader(is, encoding != null ? encoding : "UTF-8");

JSONParser parser = new JSONParser();
JSONObject spUserAttributes = (JSONObject)parser.parse(streamReader);
System.out.println("User Attributes received = " + spUserAttributes.toString());
```

---

---
title: Authentication methods
description: When picking up and dropping off attributes, your application has to authenticate with PingFederate. There are four authentication methods that you can use:
component: agentless
page_id: agentless:custom_application_setup:pf_agentless_ik_authentication_methods
canonical_url: https://docs.pingidentity.com/integrations/agentless/custom_application_setup/pf_agentless_ik_authentication_methods.html
revdate: March 7, 2025
section_ids:
  bearer-token-authentication: Bearer token authentication
  certificate-authentication: Certificate authentication
  custom-http-header-variables: Custom HTTP header variables
  http-basic-authentication: HTTP Basic authentication
---

# Authentication methods

When picking up and dropping off attributes, your application has to authenticate with PingFederate. There are four authentication methods that you can use:

1. Bearer token authentication ([IETF RFC 6750](https://datatracker.ietf.org/doc/html/rfc6750))

2. Certificate authentication (mutual TLS)

3. Custom HTTP header variables (`ping.uname` and `ping.pwd`)

4. HTTP Basic authentication ([IETF RFC 7617](https://datatracker.ietf.org/doc/html/rfc7617))

|   |                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------- |
|   | If you enable both HTTP Basic authentication and certificate authentication methods, the application can authenticate with either. |

If authentication fails, PingFederate responds with a `401` HTTP response to the application.

## Bearer token authentication

The application depends on the PingFederate authorization server for authentication and authorization. If the adapter is configured for bearer token-based authentication, the resulting OAuth access token is included in the Authorization header of the HTTP requests for the pickup and drop-off APIs.

> **Collapse: Authorization header format:**
>
> ```
> "Authorization: Bearer " + <access token>
> ```

> **Collapse: Example HTTP request:**
>
> ```
> POST https://pf.example.com:9031/ext/ref/dropoff HTTP/1.1
> Content-Length: 20
> Content-Type: application/json
> Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImsxIiwicGkuYXRtIjoiNnBhYyJ9.eyJzY29wZSI6WyJvcGVuaWQiXSwiYXV0aG9yaXphdGlvbl9kZXRhaWxzIjpbXSwiY2xpZW50X2lkIjoiYWNfb2ljX2NsaWVudCIsImFnaWQiOiJhNjdxUTJnYXBVb3pKc2RUclp6U2VYVEh2T2tpTk01WCIsImp0aSI6IkNOYlp0UUFCZE1kaWVUVHJQR3h0UTAiLCJVc2VybmFtZSI6ImpvZSIsIk9yZ05hbWUiOiJQaW5nIElkZW50aXR5IENvcnBvcmF0aW9uIiwiZXhwIjoxNzQwMTc2OTMyfQ.YwjgJNKAVuwP9qUAPFyE9ag-g0NhLzC03oV0I4-PxMZWffSAn6UhvPyBwlAQ1KH0whdbQm84oSM93u2gffyF9qtf-34PycLIbhiR7syGS-uaTGSnGVKIoOrNp5GeKJ6gBA48sInSKzO9LnqTzvIeN-vDpU3SVb16EBCx5UjJRIHxTPHonzQLld7Au_FAKGpG6eQfzUbPt0DvJyealzWLdBsn4VgdegtZJNQbnF9UhmgS5ead2wn_skAG-g_dekkePUN44LMd5B5Yf0V-xSAJmU8LYMqyB8ZedLwH-9ObUKig4kJZwGGlsGyGALVnU9f60nOfXLUZSPb8H6YGmoy-Fw
> ping.instanceId: sample_adapter
>
> {
> "subject":"jsmith"
> }
> ```

To use this method, complete the **Access Token Manager**, **Allowed Bearer Access Token Client IDs**, and **Required Bearer Access Token Scopes** fields in the Reference ID Adapter instance configuration. Learn more in [Reference ID IdP Adapter settings reference](pf_agentless_ik_reference_id_idp_adapter_settings_reference.html) and [Reference ID SP Adapter settings reference](pf_agentless_ik_reference_id_sp_adapter_settings_reference.html).

## Certificate authentication

Authentication relies on a client SSL private key and the corresponding public certificate. The application sends a request to the Reference ID Adapter endpoints using the back-channel port.

|   |                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------ |
|   | The certificate is transported during the SSL/TLS negotiation and does not appear in the HTTP request. |

> **Collapse: Example HTTP request:**
>
> ```
> POST https://pf.example.com:9032/ext/ref/dropoff HTTP/1.1
> Content-Length: 20
> Content-Type: application/json
> ping.instanceId: sample_adapter
>
> {
>   "subject":"jsmith"
> }
> ```

To use this method, complete the steps in [Configuring certificate authentication](pf_agentless_ik_configuring_certificate_authentication.html).

## Custom HTTP header variables

The application includes the **User Name** and **Pass Phrase** as the value of the `ping.uname` and `ping.pwd` HTTP headers in the HTTP request.

|   |                                                                                                     |
| - | --------------------------------------------------------------------------------------------------- |
|   | Use this method if your application does not support Base64 encoding or certificate authentication. |

> **Collapse: Example HTTP request:**
>
> ```
> POST https://pf.example.com:9031/ext/ref/dropoff HTTP/1.1
> Content-Length: 20
> Content-Type: application/json
> ping.uname: sample_id ping.pwd: sample_password
> ping.instanceId: sample_adapter
>
> {
>   "subject":"jsmith"
> }
> ```

To use this method, complete the **User Name** and **Pass Phrase** fields in the Reference ID Adapter instance configuration. Learn more in [Reference ID IdP Adapter settings reference](pf_agentless_ik_reference_id_idp_adapter_settings_reference.html) and [Reference ID SP Adapter settings reference](pf_agentless_ik_reference_id_sp_adapter_settings_reference.html).

## HTTP Basic authentication

The application encodes the **User Name** and **Pass Phrase** together using Base64. It includes the result as the value of the `Authorization` header in the HTTP request.

> **Collapse: Authorization header format:**
>
> ```
> "Authorization: BASIC " + Base64_Encode(  <username>  + ":" +  <pass phrase> )
>
> "Authorization: BASIC " + Base64_Encode("myportal:q6^&2dR!Vc7PtA")
>
> "Authorization: BASIC c2FtcGxlX2lkOnNhbXBsZV9wYXNzd29yZA=="
> ```

> **Collapse: Example HTTP request:**
>
> ```
> POST https://pf.example.com:9031/ext/ref/dropoff HTTP/1.1
> Content-Length: 20
> Content-Type: application/json
> Authorization: BASIC c2FtcGxlX2lkOnNhbXBsZV9wYXNzd29yZA==
> ping.instanceId: sample_adapter
>
> {
>   "subject":"jsmith"
> }
> ```

To use this method, complete the **User Name** and **Pass Phrase** fields in the Reference ID Adapter instance configuration. Learn more in [Reference ID IdP Adapter settings reference](pf_agentless_ik_reference_id_idp_adapter_settings_reference.html) and [Reference ID SP Adapter settings reference](pf_agentless_ik_reference_id_sp_adapter_settings_reference.html).

---

---
title: Configuring a Reference ID IdP Adapter instance
description: Configure the Reference ID IdP Adapter to determine how PingFederate communicates with your identity provider application.
component: agentless
page_id: agentless:custom_application_setup:pf_agentless_ik_configuring_a_reference_id_idp_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/agentless/custom_application_setup/pf_agentless_ik_configuring_a_reference_id_idp_adapter_instance.html
revdate: June 7, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Configuring a Reference ID IdP Adapter instance

Configure the Reference ID IdP Adapter to determine how PingFederate communicates with your identity provider application.

## About this task

You can configure the adapter to direct authentication requests, authorization consent requests, or both to your application.

## Steps

1. In the PingFederate administrative console, create a new IdP adapter instance:

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **Reference ID IdP Adapter**. Click **Next**.

3. On the **IdP Adapter** tab, configure the adapter instance by referring to [Reference ID IdP Adapter settings reference](pf_agentless_ik_reference_id_idp_adapter_settings_reference.html). Click **Next**.

4. **Optional:** On the **Actions** tab, click **Show Pass Phrase** and copy the pass phrase to your application. Click **Next**.

5. On the **Extended Contract** screen, add any attributes that you expect to retrieve in addition to the SAML subject (user ID). If you have an external consent application, add the attribute that contains the authorization scopes. Click **Next**.

6. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

7. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

8. On the **Summary** tab, check and save your configuration:

   ### Choose from:

   * For PingFederate 10.1 or later: click **Save**.

   * For PingFederate 10.0 or earlier: click **Done**. On the **Manage IdP Adapter Instances** tab, click **Save**.

9. Create an SP connection using this Reference ID IdP Adapter instance. Learn more in [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html) in the PingFederate documentation.

---

---
title: Configuring a Reference ID SP Adapter instance
description: Configure the Reference ID IdP Adapter to determine how PingFederate communicates with your service provider (SP) application.
component: agentless
page_id: agentless:custom_application_setup:pf_agentless_ik_configuring_a_reference_id_sp_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/agentless/custom_application_setup/pf_agentless_ik_configuring_a_reference_id_sp_adapter_instance.html
revdate: June 7, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Configuring a Reference ID SP Adapter instance

Configure the Reference ID IdP Adapter to determine how PingFederate communicates with your service provider (SP) application.

## Steps

1. In the PingFederate administrative console, create a new SP adapter instance.

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Adapters**. Click **Create New Instance**.

   * For PingFederate 10.0 or earlier: go to **Service Provider > Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **Reference ID SP Adapter**. Click **Next**.

3. On the **Instance Configuration** tab, configure the adapter instance by referring to [Reference ID SP Adapter settings reference](pf_agentless_ik_reference_id_sp_adapter_settings_reference.html). Click **Next**.

4. **Optional:** On the **Actions** tab, click **Show Pass Phrase** and copy the pass phrase to your application. Click **Next**.

5. On the **Extended Contract** tab, add any attributes that you expect to retrieve other than the SAML subject. Click **Next**.

6. On the **Target App Info** tab, enter the basic information about your SP application. Click **Next**.

7. On the **Summary** tab, check and save your configuration.

   ### Choose from:

   * For PingFederate 10.1 or later: click **Save**.

   * For PingFederate 10.0 or earlier: click **Done**. On the **Manage SP Adapter Instances** tab, click **Save**.

8. Create an IdP connection using this Reference ID SP Adapter instance. Learn more in [Service provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_servic_provid_sso_config.html) in the PingFederate documentation.

---

---
title: Configuring certificate authentication
description: You can configure certificate authentication between your application and PingFederate.
component: agentless
page_id: agentless:custom_application_setup:pf_agentless_ik_configuring_certificate_authentication
canonical_url: https://docs.pingidentity.com/integrations/agentless/custom_application_setup/pf_agentless_ik_configuring_certificate_authentication.html
revdate: June 7, 2024
section_ids:
  steps: Steps
---

# Configuring certificate authentication

You can configure certificate authentication between your application and PingFederate.

## Steps

1. Check that the client certificate issuer is a trusted root certificate authority (CA) in PingFederate. If not, add the intermediate and root CA certificates.

   Learn more in [Manage trusted certificate authorities](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_trustedcas_certmanagementstate.html) in the PingFederate documentation.

2. In PingFederate, export your signing certificate.

   1. On the PingFederate admin console, go to **Security > Signing & Decryption Keys & Certificates**.

   2. For the certificate that you want to use, in the **Action** column, click **Export**.

   3. On the **Export Certificate** screen, click **Next**.

   4. On the **Export & Summary** screen, click **Export**.

   5. Open the `*.crt` file in a text editor.

3. Import your PingFederate signing certificate into your application.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can use OpenSSL to convert the PCKS12 certificate and key to PEM format. Use one of the following commands.PEM certificate only```
    openssl pkcs12 -in  <certname>.p12-passin pass:<password>  -nokeys -out  <certname>.cert.pem
   ```PEM key only```
    openssl pkcs12 -in  <certname>.p12 -passin pass:<password>  -nocerts -out  <certname>.key.pem
   ```PEM certificate and key```
    openssl pkcs12 -in  <certname>.p12 -passin pass:<password>  -out  <certname>.certandkey.pem
   ``` |

4. If you have already configured a Reference ID Adapter instance, update it by setting the **Allowed Subject DN** field, the **Allowed Issuer DN** field, or both to match the client certificate.

5. Configure a second port for PingFederate to receive back-channel calls.

   1. Stop PingFederate.

   2. Open the `<pf_install>/pingfederate/bin/run.properties` file for editing.

   3. Change the value of the `pf.secondary.https.port` property to a valid port number, such as 9032.

      You can find information about this property in [Configuring PingFederate properties](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_pf_propert.html) in the PingFederate documentation.

   4. Save the file.

   5. Start PingFederate.

6. Configure your application to send requests to the Reference ID Adapter endpoints using the back-channel port:

   ```none
   POST https://pf.example.com:9032/ext/ref/dropoff HTTP/1.1
   Content-Length: 20
   Content-Type: application/json
   ping.instanceId: sample_adapter

   {
     "subject":"jsmith"
   }
   ```

7. Configure your application to send the client certificate with the request.

   |   |                                                                                                                                                                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Learn more about exporting your PingFederate certificate in [Manage SSL server certificates](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_sslservercerts_certmanagementstate.html) in the PingFederate documentation. |

   The following code uses PHP to send the client certificate:

   ```shell
   $client_cert = dirname(__FILE__).'/sample_cert.cert.pem';
   $client_key = dirname(__FILE__).'/sample_cert.key.pem';
   $client_key_password = 'sample_key_password';
   $http_headers[] = 'ping.instanceId: '.$adapter_instance_id;

   // PHP can use curl to make the HTTP calls to the pickup endpoint
   $crl = curl_init();

   // Dropoff URL
   curl_setopt($crl, CURLOPT_URL, $dropoff_loc);
   curl_setopt($crl, CURLOPT_SSLCERT, $client_cert);
   curl_setopt($crl, CURLOPT_SSLKEYTYPE, 'PEM');
   curl_setopt($crl, CURLOPT_SSLKEY, $client_key);
   curl_setopt($crl, CURLOPT_SSLKEYPASSWD, $client_key_password);
   ...
   $result = curl_exec($crl);
   ```

---

---
title: Custom application setup
description: You can integrate PingFederate with your identity provider or service provider application by modifying your application and configuring a Reference ID Adapter instance.
component: agentless
page_id: agentless:custom_application_setup:pf_agentless_ik_custom_application_setup
canonical_url: https://docs.pingidentity.com/integrations/agentless/custom_application_setup/pf_agentless_ik_custom_application_setup.html
revdate: June 7, 2024
---

# Custom application setup

You can integrate PingFederate with your identity provider or service provider application by modifying your application and configuring a Reference ID Adapter instance.

|   |                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you would like to see a working demonstration of the Agentless Integration Kit before integrating your own applications, see [Sample application setup](../sample_application_setup/pf_agentless_ik_sample_application_setup.html). |

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Agentless Integration Kit files to your PingFederate directory.
component: agentless
page_id: agentless:custom_application_setup:pf_agentless_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/agentless/custom_application_setup/pf_agentless_ik_deploying_the_integration_files.html
revdate: March 7, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Agentless Integration Kit files to your PingFederate directory.

## About this task

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | If you operate PingFederate in a cluster, the following steps refer to the console node. |

## Steps

1. Download the Agentless Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/agentless-integration-kit).

2. Stop PingFederate.

3. If you are upgrading an existing deployment, delete `pf-referenceid-adapter-<version>.jar` from `<pf_install>/pingfederate/server/default/deploy`.

4. Extract the `.zip` archive and copy the contents of the `dist` directory to your `<pf_install>/pingfederate/server/default` directory.

5. If there is more than one version of the `pf-authn-api-sdk-<version>.jar` file in your `<pf_install>/pingfederate/server/default/lib` directory, delete all but the latest version of the file.

6. Start PingFederate.

7. If you operate PingFederate in a cluster, repeat steps 2 - 6 for each engine node.

---

---
title: Deploying the integration files and sample applications
description: To get started with the integration, deploy the Agentless Integration Kit files to your PingFederate directory.
component: agentless
page_id: agentless:sample_application_setup:pf_agentless_ik_deploying_the_integration_files_and_sample_applications
canonical_url: https://docs.pingidentity.com/integrations/agentless/sample_application_setup/pf_agentless_ik_deploying_the_integration_files_and_sample_applications.html
revdate: March 7, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deploying the integration files and sample applications

To get started with the integration, deploy the Agentless Integration Kit files to your PingFederate directory.

## About this task

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | If you operate PingFederate in a cluster, the following steps refer to the console node. |

## Steps

1. Download the Agentless Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/agentless-integration-kit).

2. Stop PingFederate.

3. If you are upgrading from a previous deployment, delete the following directories and files from `<pf_install>/pingfederate/server/default/deploy`.

   * `/AgentlessIntegrationKitSampleIdP`

   * `/AgentlessIntegrationKitSampleSP`

   * `AgentlessIdPSample.war`

   * `AgentlessSPSample.war`

   * `pf-referenceid-adapter-<version>.jar`

4. Extract the `.zip` archive and copy the contents of the `dist` directory to your `<pf_install>/pingfederate/server/default` directory.

5. From the `.zip` archive, copy the following files from `sample` to `<pf_install>/pingfederate/server/default/deploy`.

   * `AgentlessIdPSample.war`

   * `AgentlessSPSample.war`

6. If there is more than one version of the `pf-authn-api-sdk-<version>.jar` file in your `<pf_install>/pingfederate/server/default/lib` directory, delete all but the latest version of the file.

7. Start PingFederate.

---

---
title: Deploying the sample configuration archive
description: The sample configuration archive configures a single instance of PingFederate with an example integration that uses both the IdP and SP sample applications. It automatically creates instances of the Reference ID IdP Adapter and Reference ID SP Adapter.
component: agentless
page_id: agentless:sample_application_setup:pf_agentless_ik_deploying_the_sample_configuration_archive
canonical_url: https://docs.pingidentity.com/integrations/agentless/sample_application_setup/pf_agentless_ik_deploying_the_sample_configuration_archive.html
revdate: June 7, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deploying the sample configuration archive

## About this task

The sample configuration archive configures a single instance of PingFederate with an example integration that uses both the IdP and SP sample applications. It automatically creates instances of the Reference ID IdP Adapter and Reference ID SP Adapter.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Deploying the sample application configuration archive will destroy your existing PingFederate configuration. We recommend that you test it on a fresh installation of PingFederate, or back up your current configuration as shown in [Exporting an archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_configurationarchiveexportstate.html) in the PingFederate documentation. |

## Steps

1. Start PingFederate.

2. From the Agentless Integration Kit `.zip` archive, copy `config/data.zip` to `<pf_install>/pingfederate/server/default/data/drop-in-deployer`.

---

---
title: Developing your application
description: The Agentless Integration Kit doesn't require you to install special agent software, but you will have to modify your application to communicate with the PingFederate Reference ID Adapter through HTTP calls. The following information and recommendations should guide your development process.
component: agentless
page_id: agentless:custom_application_setup:pf_agentless_ik_developing_your_application
canonical_url: https://docs.pingidentity.com/integrations/agentless/custom_application_setup/pf_agentless_ik_developing_your_application.html
revdate: June 7, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Developing your application

The Agentless Integration Kit doesn't require you to install special agent software, but you will have to modify your application to communicate with the PingFederate Reference ID Adapter through HTTP calls. The following information and recommendations should guide your development process.

## About this task

|   |                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This section provides example code in Java. You can find the latest example code for a variety of languages (including .NET, PHP, and Python) in the Agentless Integration Kit projects in the [Ping Identity GitHub repository](https://github.com/pingidentity?q=agentless). Choose the language you use and see the `example-code` directory to help you with the following steps. |

## Steps

1. Determine whether your application will need to pick up attributes, drop off attributes, or both.

   Typically, if your application acts as an identity provider, it will drop off attributes with PingFederate. If your application acts as a service provider, it will pick up attributes from PingFederate.

   Learn more about the two flows in [Overview of the identity provider SSO flow](../overview_of_the_identity_provider_integration/pf_agentless_ik_overview_of_the_identity_provider_sso_flow.html) and [Overview of the service provider SSO flow](../pf_agentless_ik_overview_of_the_service_provider_sso_flow.html).

2. Configure an endpoint in your application to receive `REF` and `resumePath` values from PingFederate.

   |   |                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Note the endpoint URL. You'll enter it in the **Authentication Endpoint** field when you configure a Reference ID Adapter instance later in the setup process. |

3. Decide how your application will authenticate with PingFederate.

   Learn more in [Authentication methods](pf_agentless_ik_authentication_methods.html).

4. Configure your application to do one or both of the following:

   * Request attributes from PingFederate and parse the response as shown in [Attribute pickup process](pf_agentless_ik_attribute_pickup_process.html).

   * Encode attributes and provide them to PingFederate as shown in [Attribute drop-off process](pf_agentless_ik_attribute_drop_off_process.html).

5. Configure your application to redirect the browser to the URL provided in the `resumePath` parameter, which PingFederate provided in the attribute drop-off process.

   Redirect URL format:

   ```
   https://pf_host:pf_port/resume_path?REF=reference_ID
   ```

   Example code:

   ```
   String resumeURL = String.format("https://localhost:9031%s?REF=%s", resumePath, ref);

   response.sendRedirect(resumeURL);
   ```

---

---
title: Development considerations
description: The Agentless Integration Kit does not require you to install special agent software in your application, but it does require your application to be modified to communicate with the PingFederate Reference ID Adapter. The following information and recommendations should guide your modifications.
component: agentless
page_id: agentless:custom_application_setup:pf_agentless_ik_development_considerations
canonical_url: https://docs.pingidentity.com/integrations/agentless/custom_application_setup/pf_agentless_ik_development_considerations.html
revdate: June 7, 2024
section_ids:
  reference-id-length: Reference ID length
  error-handling: Error handling
  timeouts: Timeouts
  session-management: Session management
  deep-linking: Deep linking
  application-authorization: Application authorization
  application-user-profile-management: Application user profile management
---

# Development considerations

The Agentless Integration Kit does not require you to install special agent software in your application, but it does require your application to be modified to communicate with the PingFederate Reference ID Adapter. The following information and recommendations should guide your modifications.

## Reference ID length

The reference ID is a long hexadecimal string. Length is determined by the **Reference Length** setting in the Reference ID Adapter instance configuration. The default length is 30 bytes.

For example:

```
A9C020F7CF8C21002CDC774B48A7CFE6B3ECA5FC6CCA507EE419B4432DB
```

Each reference ID is specific to the instance of the Reference ID Adapter that issued it.

## Error handling

During the attribute pickup or drop-off processes, PingFederate returns any errors as HTTP status codes. For example when an incorrect client ID or password is provided, PingFederate returns a 401 HTTP error.

If an error occurs during an authentication attempt, then the authentication form should handle the error (that is, display a message to the user) and abort the sign on process. Your application will only receive a sign-in request from a user that was authenticated by the identity provider (IdP). Failed authentications are not redirected back to the application. Any errors received during the authentication process should be handled with the assumption that the user has already completed the authentication process at the IdP.

If your application presents an invalid reference ID to PingFederate, the Reference ID Adapter returns an empty set of attributes.

|   |                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Locate error screens outside the protected content. When a user receives an error during the sign-on or authorization stages, they need to be able to see the error without being sent back through the authentication process. |

## Timeouts

A given reference value can only be used once and expires after a set duration. This improves security by preventing "replay" attacks. The duration is determined by the **Reference Duration** field in the Reference ID Adapter instance configuration. The default duration is three seconds.

To prevent unexpected timeouts, make sure the clock is reasonably synchronized between the application server and the federation server. You can also adjust the value of the **Reference Duration** configuration setting can also be used to allow for a larger tolerance for time skew.

## Session management

The IdP adapter should maintain a session for the user so that subsequent calls for authentication can re-use the existing sign-on session. This creates a single sign-on experience for the user.

The IdP adapter should honor the `forceAuthn` parameter to force the user to enter credentials even if the user has an existing session.

## Deep linking

Deep linking (also called direct linking) is the ability to link to a page nested inside the protected content. This saves the user from having to navigate to the content from a generic landing page.

Your application receives a deep link in the `TargetResource` parameter. This parameter is included in the initial redirect to the sign-on URL.

Your application should honor this URL during the sign-on process by redirecting the user to the deep link after the application session is created. When recovering from a timeout or other scenario that might require re-authentication, your application should include the requested URL in the request.

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | When passing the `TargetResource` parameter, or any URL parameter, remember to URL-encode the value. |

## Application authorization

Authorization includes determining whether the user has access to the application and what roles the user has when they are inside the application.

Your service provider application will only receive users that have already been authenticated. Your application should perform any authorization decisions before creating an application session.

|   |                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Locate error pages outside the protected content. When a user receives an error during the sign-on or authorization stages, they need to be able to see the error without being sent back through the authentication process. |

## Application user profile management

Your application will receive an already authenticated user from a trusted identity provider that can contain additional attributes. This authenticated identity can be used to provision new accounts into the application store or update existing user profile information.

---

---
title: Download manifest
description: The following files are included in the Agentless Integration Kit .zip archive:
component: agentless
page_id: agentless:release_notes:pf_agentless_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/agentless/release_notes/pf_agentless_ik_download_manifest.html
revdate: March 7, 2025
---

# Download manifest

The following files are included in the Agentless Integration Kit `.zip` archive:

* `Legal.pdf`: Copyright and license information.

* `config/data.zip`: A PingFederate configuration archive to use with the sample applications.

* `dist/pingfederate/server/default`: Contains the integration files.

  * `lib/pf-authn-api-sdk-<version>.jar`: A JAR file that contains the PingFederate Authentication API SDK.

  * `deploy`: Contains the Java libraries.

    * `pf-referenceid-adapter-<version>.jar`: `.jar` file that contains the Reference ID IdP Adapter and Reference ID SP Adapter.

  * `conf`: Contains the HTML template that presents the application sign-on form.

    * `language-packs`: Contains files with customizable user-facing messages.

      * `authn-api-messages.properties`: A version of the common PingFederate authentication API variable file that includes adapter-specific messages.

* `sample`: Contains files needed to set up a working demonstration of this integration kit.

  * `AgentlessIdPSample.war`: The compiled Agentless identity provider Java sample application.

  * `AgentlessSPSample.war`: The compiled Agentless service provider Java sample application.

  |   |                                                                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | You can find the latest Java, .NET Core, PHP, and Python sample applications in the [Ping Identity GitHub repository](https://github.com/pingidentity?q=agentless). |

---

---
title: Enabling logging
description: Include Reference ID adapter events in the PingFederate server log file.
component: agentless
page_id: agentless:troubleshooting:pf_agentless_ik_enabling_logging
canonical_url: https://docs.pingidentity.com/integrations/agentless/troubleshooting/pf_agentless_ik_enabling_logging.html
revdate: November 6, 2025
section_ids:
  steps: Steps
---

# Enabling logging

Include Reference ID adapter events in the PingFederate server log file.

You can find more information about using Log4j in:

* [Log4j 2 logging service and configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_log4j_2_loggin_service_and_config.html) in the PingFederate documentation

* [PingFederate Log4J articles](https://support.pingidentity.com/s/global-search/%40uri#q=Log4j\&sort=relevancy\&f:@commonsource=%5BKnowledge%20Base%5D\&f:@commonproduct=%5BPingFederate%5D) in the Ping Identity Knowledge Base

## Steps

1. In your Java Virtual Machine options, set the `javax.net.debug` property to `ssl` or `all`.

2. Restart PingFederate.

3. Review the debug messages in the `<pf_install>/pingfederate/log/server.log` file.

---

---
title: External consent approval
description: During the OAuth authorization flow, after a user authenticates, PingFederate directs the user to an authorization consent screen. On this screen, users can consent to a scope of privileges that the client has requested.
component: agentless
page_id: agentless:custom_application_setup:pf_agentless_ik_external_consent_approval
canonical_url: https://docs.pingidentity.com/integrations/agentless/custom_application_setup/pf_agentless_ik_external_consent_approval.html
revdate: June 7, 2024
section_ids:
  identifying-consent-requests: Identifying consent requests
  passing-consent-declined-results-to-pingfederate: "Passing \"consent declined\" results to PingFederate"
---

# External consent approval

During the OAuth authorization flow, after a user authenticates, PingFederate directs the user to an authorization consent screen. On this screen, users can consent to a scope of privileges that the client has requested.

Instead of using the consent screen that is provided with PingFederate, you can direct users to your own application to process the consent requests. This gives you more control over the presentation of the consent request.

Learn more in [Consent approval](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_consent_appr.html) in the PingFederate documentation.

## Identifying consent requests

PingFederate sends authentication requests and authorization consent requests to your application through the same endpoint URL. To process the request and display the appropriate page to the user, your application must be able to differentiate authentication requests from consent requests.

All consent requests contain the following attribute:

Key: `com.pingidentity.adapter.input.parameter.adapter.action`

Value: `com.pingidentity.adapter.action.external.consent`

Because authentication requests do not contain this attribute, your application can differentiate authentication and consent requests based on whether this attribute is present.

## Passing "consent declined" results to PingFederate

If a user rejects the scope of privileges requested by a client, your application needs to signal that rejection to PingFederate.

In this case, your application must drop off the following attribute to PingFederate:

Key: `com.pingidentity.adapter.refid.external.application.failure.message`

Value: An optional error message.

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the Agentless Integration Kit.
component: agentless
page_id: agentless:release_notes:pf_agentless_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/agentless/release_notes/pf_agentless_ik_known_issues_and_limitations.html
revdate: March 7, 2025
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the Agentless Integration Kit.

## Known issues

* Using the PingFederate admin API to create or import a Reference ID Adapter instance using the adapter descriptor from Agentless Integration Kit 1.5.3 or earlier can cause an invalid single logout (SLO) configuration when you deploy a later version of the Agentless Integration Kit.

## Known limitations

There are no known limitations.

---

---
title: Overview of the identity provider integration
description: You can use the Agentless Integration Kit to extend your sign-on flow to include a custom authentication application.
component: agentless
page_id: agentless:overview_of_the_identity_provider_integration:pf_agentless_ik_overview_of_the_identity_provider_integration
canonical_url: https://docs.pingidentity.com/integrations/agentless/overview_of_the_identity_provider_integration/pf_agentless_ik_overview_of_the_identity_provider_integration.html
revdate: June 7, 2024
section_ids:
  use-case: Use case
  high-level-view-of-the-sign-on-flow: High-level view of the sign-on flow
---

# Overview of the identity provider integration

You can use the Agentless Integration Kit to extend your sign-on flow to include a custom authentication application.

## Use case

Some proprietary, third-party, or complex authentication applications might not be covered by the ready-made solutions that are included with PingFederate or available in the [Ping Identity Marketplace](https://marketplace.pingone.com/home).

The Agentless Integration Kit offers a flexible way to integrate any application into the PingFederate authentication flow. This allows you to use your existing application without needing to develop a custom adapter for PingFederate. The only requirement is that your application can make REST API calls.

## High-level view of the sign-on flow

Your application gets information from PingFederate, performs any number of authentication steps, then passes the user back to PingFederate to complete the sign-on process.

![A diagram showing the flow of information between the application, PingFederate, and the a service provider.](_images/ebh1597687658074.jpg)

1. The user initiates the sign-on process, either at the identity provider (IdP) or service provider (SP).

2. PingFederate starts the authentication policy, which can include any number of adapters or authentication steps.

3. When the Reference ID IdP Adapter is triggered in the authentication policy, PingFederate sends a set of values to the application's authentication endpoint, including the following:

   * `REF`

     The unique reference ID that the application uses to pick up user attributes.

   * `resumePath`

     The PingFederate URI that the application redirects the user to after authentication. This includes a random string that is unique to the user session.

   The application stores these values.

4. The application makes a call to the Reference ID IdP Adapter to pick up any user attributes that PingFederate has associated with the reference ID, such as the user ID, LDAP attributes, tracked HTTP parameters, and any claims.

   The application stores these attributes.

5. The application completes any number of authentication steps, then drops off resulting attributes to the Reference ID IdP Adapter using an HTTP POST call.

6. PingFederate continues executing the authentication policy, now with access to the user attributes provided by the application. PingFederate provides a response to the service provider.

For a detailed description of the flow, see [Overview of the identity provider SSO flow](pf_agentless_ik_overview_of_the_identity_provider_sso_flow.html).