---
title: Access token modification scripting API
description: Reference for PingAM OAuth 2.0 access token modification scripting API bindings and methods to manipulate token content and fields
component: pingam
version: 8.1
page_id: pingam:am-scripting:access-token-modification-api
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/access-token-modification-api.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["scripting-guide:access-token-modification-api.adoc"]
section_ids:
  atmapi-modify-access-token: Modify the access token
  set_values: Set values
  atmapi-add-json: Add JSON to the response
  atmapi-client-properties: Access client properties
  atmapi-request-properties: Access request properties
  atmapi-profile: Access profile data
---

# Access token modification scripting API

The following bindings are available to [access token modification](../am-oauth2/modifying-access-tokens-scripts.html) scripts.

|   |                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This script can be either a legacy or a next-generation script. It has access to all the [common bindings](script-bindings.html) for its scripting context.Learn about converting existing scripts in [Migrate OAuth scripts to next-generation scripts](access-token-modification-migrate.html). |

| Binding                                           | Description                                                                                                                                                | Legacy type                                                                                  | Next-generation type                                                                                                                                               |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`accessToken`](#atmapi-modify-access-token)      | The OAuth 2.0 access token.                                                                                                                                | An [AccessToken](../_attachments/apidocs/org/forgerock/oauth2/core/AccessToken.html) object. | A wrapper object that lets you access [AccessToken](../_attachments/apidocs/org/forgerock/oauth2/core/AccessToken.html) methods.                                   |
| [`clientProperties`](#atmapi-client-properties)   | A map of properties configured in the client profile. Only present if the client was correctly identified.                                                 | Map                                                                                          | Map                                                                                                                                                                |
| [`identity`](#atmapi-profile)                     | Represents an identity that AM can access.                                                                                                                 | An [AMIdentity](../_attachments/apidocs/com/sun/identity/idm/AMIdentity.html) object.        | A wrapper object for a scripted identity.                                                                                                                          |
| [`requestProperties`](#atmapi-request-properties) | A map of the properties present in the request.                                                                                                            | Map                                                                                          | Map                                                                                                                                                                |
| `scopes`                                          | An array of the requested scopes. For example:`["read", "transfer", "download"]`.                                                                          | Set                                                                                          | List                                                                                                                                                               |
| `session`                                         | Access the user's SSO session object if the request contains a session cookie.	The session isn't available for resource owner password credentials grants. | An [SSOToken](../_attachments/apidocs/com/iplanet/sso/SSOToken.html) object.                 | A `ScriptedSession` object.> **Collapse: Methods**
>
> ```java
> public String getProperty(String name)
> public void setProperty(String name, String value)
> ``` |

## Modify the access token

Use the `accessToken` binding to manipulate the content and fields of the token with methods such as `addExtraJsonData`, `setField`, and `setExpiryTime`.

You can find all the available methods listed in the [AccessToken](../_attachments/apidocs/org/forgerock/oauth2/core/AccessToken.html) Javadoc.

### Set values

The following example shows how to set different values in the access token:

* Next-generation

* Legacy

```javascript
// add values to the token using available bindings
accessToken.setField('foo', 'bar');
var customProperties = clientProperties.get('customProperties');
accessToken.setField('customClientProperty', customProperties.get('testCustomProp'));
accessToken.setField('oauth2ClientId', clientProperties.get('clientId'));
accessToken.setField('requestUri', requestProperties.get('requestUri'));
// set UMA permissions
accessToken.setPermissions('permissions');
// set a new expiry time in milliseconds
accessToken.setExpiryTime(1755242153837);
```

```javascript
// add values to the token using available bindings
accessToken.setField('foo', 'bar');
var customProperties = clientProperties.get('customProperties');
accessToken.setField('customClientProperty', customProperties.get('testCustomProp'));
accessToken.setField('oauth2ClientId', clientProperties.get('clientId'));
accessToken.setField('requestUri', requestProperties.get('requestUri'));
// set UMA permissions
accessToken.setPermissions(JsonValue.json('permissions'));
// set a new expiry time in milliseconds
accessToken.setExpiryTime(1755242153837);
```

### Add JSON to the response

The following example shows how to add extra data to the JSON response:

* Next-generation

* Legacy

```javascript
// add value
accessToken.addExtraData('myKey', 'value');
// add JSON value
accessToken.addExtraJsonData('myJsonKey', 'value');
// add list
accessToken.addExtraJsonData('myListJsonKey', ['listValue']);
// add map
accessToken.addExtraJsonData('myMapJsonKey', {'mapKey': 'mapValue'});
```

```javascript
import org.forgerock.json.JsonValue;
// add value
accessToken.addExtraData('myKey', { -> 'value' });
// add JSON value
JsonValue myJsonValue = JsonValue.json('value');
accessToken.addExtraJsonData('myJsonKey', { -> myJsonValue });
// add list
JsonValue myListJsonValue = JsonValue.json(JsonValue.array('listValue'));
accessToken.addExtraJsonData('myListJsonKey', { -> myListJsonValue });
// add map
JsonValue myMapJsonValue = JsonValue.json(JsonValue.object(JsonValue.field('mapKey', 'mapValue')));
accessToken.addExtraJsonData('myMapJsonKey', { -> myMapJsonValue });
```

## Access client properties

The client properties map has the following keys:

* `allowedGrantTypes`

  An array of [grant types](../_attachments/apidocs/org/forgerock/oauth2/core/GrantType.html).

* `allowedResponseTypes`

  An array of strings listing response types.

* `allowedScopes`

  An array of strings listing scopes.

* `clientId`

  The client's URI for the request locale.

* `customProperties`

  A map of any custom properties added to the client.

  These properties can include lists or maps as sub-maps. For example, the script includes `customMap[Key1]=Value1` as `customMap` > `Key1` > `Value1` in the object.

  In the AM admin UI, go to OAuth 2.0 > Clients > *Client ID* > Advanced, and update the Custom Properties field.

  Add custom properties as shown in these examples:

  ```bash
  customproperty=custom-value1
  customList[0]=customList-value-0
  customMap[key1]=customMap-value-1
  ```

  Scripts can then access the custom properties in the following way:

  ```javascript
  var customProperties = clientProperties.get("customProperties");
  var property = customProperties.get("myProperty");
  ```

  The map is `null` if AM} didn't successfully identify the client.

* `redirectUris`

  Access the redirect URIs as a list of strings, for example:

  ```javascript
  var uris = clientProperties.get("redirectUris");
  ```

## Access request properties

The request properties map has the following keys:

* `requestUri`

  The URI as a string

* `realm`

  The realm as a string

* `requestParams`

  A map of request parameters and posted data, where each value is an array of parameters.

  |   |                                                                                                                                                                                                                                          |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | To mitigate the risk of reflection-type attacks, use OWASP best practices when handling these parameters. Find more information in [Unsafe use of Reflection](https://owasp.org/www-community/vulnerabilities/Unsafe_use_of_Reflection). |

* `requestHeaders`

  The value of the named request header. Returns a map of `<String, List<String>>` as a native JavaScript object, for example:

  `var ipAddress = requestProperties.requestHeaders["X-Forwarded-For"][0]`

  Header names are case-sensitive.

## Access profile data

Use the `identity` binding to get data about the subject of the authorization request.

* Methods

  The following actions are available to the `identity` binding:

  * Get attribute values

  * Set attribute values

  * Add attribute values

  - Next-generation

  - Legacy

  For next-generation scripts, the `identity` object is a wrapper object that allows access to the following methods:

  ```java
  public List<String> getAttributeValues(String attributeName)
  public String getName()
  public String getUniversalId()
  public void setAttribute(String attributeName, List<String> attributeValues)
  public void addAttribute(String attributeName, String attributeValue) {
  public void store() throws IdentityUpdateException {
  public boolean exists()
  ```

  Learn about the available methods in the [AMIdentity](../_attachments/apidocs/com/sun/identity/idm/AMIdentity.html) Javadoc.

* Examples

  These examples use the methods of the `identity` binding to get and set profile data.

  * Next-generation

  * Legacy

  ```javascript
  // Returns all values as an array, for example: ["test@example.com", "user@example.com"]
  identity.getAttributeValues("mail");
  // Returns the first value, for example:  test@example.com
  identity.getAttributeValues("mail")[0];
  // Create / replace attribute with the specified value
  identity.setAttribute("attrName", ["newValue"]);
  // Add attribute to the list
  identity.addAttribute("attrName", ["newValue"]);
  // Explicitly persist data when setting attributes
  identity.store();
  ```

  ```javascript
  // Returns all values as a set, for example: [test@example.com, user@example.com]
  identity.getAttribute("mail").toString();
  // Returns the first value, for example:  test@example.com
  identity.getAttribute("mail").iterator().next();
  // Create / replace attribute with the specified value
  identity.setAttribute("attrName", ["newValue"]);
  // Add attribute to the list
  identity.addAttribute("attrName", ["newValue"]);
  ```
