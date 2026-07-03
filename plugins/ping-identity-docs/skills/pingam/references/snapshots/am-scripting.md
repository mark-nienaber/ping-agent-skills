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

---

---
title: Authorization endpoint data provider scripting API
description: Scripting API bindings available to authorization endpoint data provider scripts in PingAM
component: pingam
version: 8.1
page_id: pingam:am-scripting:authorize-endpoint-data-provider-api
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/authorize-endpoint-data-provider-api.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Authorization endpoint data provider scripting API

The following bindings are available to [Authorize endpoint data provider](../am-oauth2/plugins-auth-endpoint-data-provider.html) scripts:

|   |                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This script can be either a legacy or a next-generation script. It has access to all the [common bindings](script-bindings.html) for its scripting context.Learn about converting existing scripts in [Migrate OAuth scripts to next-generation scripts](access-token-modification-migrate.html). |

| Binding   | Description                                        | Legacy type                                                                  | Next-generation type                                                                                                                                               |
| --------- | -------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `session` | A representation of the user's SSO session object. | An [SSOToken](../_attachments/apidocs/com/iplanet/sso/SSOToken.html) object. | A `ScriptedSession` object.> **Collapse: Methods**
>
> ```java
> public String getProperty(String name)
> public void setProperty(String name, String value)
> ``` |

---

---
title: Cache script values
description: Use the cache manager service from a Scripted Decision node script to store values for later use in the same or different journeys, reducing calls to external services
component: pingam
version: 8.1
page_id: pingam:am-scripting:cache-manager
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/cache-manager.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  how_the_script_cache_works: How the script cache works
  example_script_cache_implementation: Example script cache implementation
  cache-manager-load-script: Create a cache loader script
  cache-manager-service: Configure the cache
  cache-manager-journey: Access the cached values in a journey
  manage_script_caches: Manage script caches
  cache-manager-refresh: Refresh the cache
  cache-manager-remove: Remove cached values
  cache-manager-metrics: Monitor the cache usage
  cache-manager-REST: Clear a cache using REST
---

# Cache script values

Use the cache manager service from a Scripted Decision node script to store values for later use in the same journey (tree) or across different journeys. Caching values can help to improve performance by reducing calls to external services or storing values that are expensive to compute.

For example, cache an access token at the start of one journey and retrieve it in another, rather than getting a new one.

The scripting cache is set to evict entries automatically, but you can also invalidate values manually or configure your own eviction policy.

## How the script cache works

![How the script cache works](_images/cache-manager-service.png)

1 A Scripted Decision node accesses a named cache using the `cacheManager` binding.

The cache manager service returns the cache and the node requests a cached entry.

2 The cache returns the cached value if the entry exists and hasn't expired.\
3 The cache runs the `load()` function if:

* The entry doesn't exist *or*

* The entry exists but has expired and the cache isn't set to refresh (must have a `reload()` function *and* be configured to `Refresh after write`)

4 The cache runs the `reload()` function if the entry exists, hasn't expired, and the cache is set to refresh.\
5 The cache returns the value, saving it in the cache if `load()` or `reload()` were run.

## Example script cache implementation

To cache a value and retrieve it later in a journey, complete the following tasks:

1. [Write a script to load a value into the cache](#cache-manager-load-script)

2. [Create a cache and add to the cache manager service](#cache-manager-service)

3. [Access a cached value in a journey](#cache-manager-journey)

You also have the option to:

* [Refresh the cache](#cache-manager-refresh)

* [Remove cached values](#cache-manager-remove)

* [Monitor the cache usage](#cache-manager-metrics)

* [Clear a cache using REST](#cache-manager-REST)

The following example caches an access token for use later in the journey and provides the option to invalidate the token once displayed to the user.

### Create a cache loader script

The cache manager service calls the cache loader script's `load()` function when it's queried for a key that doesn't yet exist in the cache. The cache manager also calls a `reload()` function if [configured for refresh](#cache-manager-refresh).

This example script gets a secret from the secret store and calls the [Client credentials grant](../am-oauth2/oauth2-client-cred-grant.html) to get an access token. It assumes you have configured an OAuth 2.0 confidential client called `myClient` and a secret stored in a secret store under the label `scripted.node.myClient.secret`.

The token is added to the cache and returned. Next time the cache is queried with the same key, it returns the value from the cache, providing it's not expired.

The cache manager service follows the pattern of other cache loading implementations, such as [Guava Cache](https://www.baeldung.com/guava-cache).

To create your load script, you can use any [next-generation](next-generation-scripts.html) common bindings.

1. In the AM admin UI, go to Realms > *Realm Name* > Scripts, and click +New Script.

2. Provide a suitable name for your script and select the following values:

   * Script Type

     `Cache Loader`

   * Evaluator Version

     `Next Generation`

3. Click Create.

4. Replace the default JavaScript with the following script:

   ```javascript
   function load(key) {
       var url = key.url;
       var clientId = key.clientId;
       var clientSecret = secrets.getGenericSecret(key.clientSecretLabel);
       var scope = key.scope;

       var options = {
           method: "POST",
           headers: {
               "Content-Type": "application/x-www-form-urlencoded"
           },
           form: {
               grant_type: "client_credentials",
               client_id: clientId,
               client_secret: clientSecret,
               scope: scope
           }
       }

       var response = httpClient.send(url, options).get();
       if (!response || response.status != 200) {
           logger.error("Bad response from " + url);
           throw Error("Bad response from " + url);
       }
       return response.json();
   }

   function reload(key, oldValue) {
       return load(key);
   }
   ```

   The script uses the `load()` function from the sample [OAuth2 Cache Loader Script](sample-scripts.html#oauth2-cache-loader-js) that gets an access token and adds a `reload()` function. In this case, `reload()` ignores the old value and creates a new access token to add to the cache.

5. Save your changes.

### Configure the cache

To cache values, configure the cache manager service and add a cache for each type of data you want to store.

You can create and manage multiple caches within each realm. You can also configure a single global cache, which is used to create an instance in each realm with the same configuration.

The cache manager service is responsible for managing the different caches within a realm and their overall size.

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The total size for all caches in a realm is limited to 20MB, and each cache entry can't exceed 5KB. When this limit is reached, the cache manager evicts entries to make space. |

Complete these steps to configure an instance of the cache manager service in a realm:

1. In the AM admin UI, go to Realms > *Realm Name* > Services.

2. Click Add a Service and select Cache Manager Service from the service type list.

3. Enable the service and save your changes.

4. On the Secondary Configurations tab, click Add a Secondary Configuration.

5. Enter a name for the cache manager instance that describes its purpose, for example, `tokenCache`, and click Create.

   A cache is identified by its name, so you must enter a unique name.

6. Configure the cache:

   * Loading Script

     Select your [cache loading script](#cache-manager-load-script) from the list.

   * Eviction Policy

     For this example, set the policy to `Refresh after write` to make sure the cache runs the reload function when an entry is accessed after the expiry time.

   * Duration Unit

     Leave as the default, `Hours`.

   * Eviction Period

     Leave as the default, `1`.

   You can find information about these settings in the [Cache Manager service configuration](../setup/services-configuration.html#cachemanager-service).

7. Save your changes.

### Access the cached values in a journey

Use the `cacheManager` binding to access a cache and get the values that you've stored.

1. Create a [next-generation decision node script](scripting-api-node.html) to access your cached access token:

   ```javascript
   var tokenEndpoint = "https://am.example.com:8443/am/am/oauth2/realms/root/realms/alpha/access_token";

   if (cacheManager.exists("tokenCache")) {

       var accessToken = cacheManager.named("tokenCache").get({
           url: tokenEndpoint,
           clientId: "myClient",
           clientSecretLabel: "scripted.node.myClient.secret",
           scope: "profile"
       }).access_token;

       // add to nodeState to display later in the journey
       nodeState.putShared("accessToken", accessToken);
   }
   else {
       logger.warn("tokenCache is undefined");
   }
   action.goTo("true");
   ```

2. [Create a tree](../am-authentication/create-auth-trees.html) and include a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/scripted-decision.html) configured to use your script. For example:

   ![Script cache journey](_images/cache-manager-journey.png)

   * The Get Access Token node runs the script that uses the `cacheManager` binding to get a value from `tokenCache`. The cache invokes the `load()` function and returns the value for the specified key.

   * The Display Token node is a [Configuration Provider node](https://docs.pingidentity.com/auth-node-ref/8.1/config-provider.html) that imitates a Message node with the following configuration:

     ```javascript
     config = {
         "message": {"en-GB": `Current token: ${nodeState.get("accessToken")}`},
         "messageYes": {"en-GB": "Display token again"},
         "messageNo": {"en-GB": "Invalidate token"},
         "stateField" : null
     }
     ```

     The node retrieves the access token from node state to display to the end user.

   * If the end user selects to display the token again, the journey returns to the Get Access Token node.

     * The cache returns the stored value when it's accessed within the eviction period.

     * The cache runs the `reload()` function outside of this period when it's configured to `Refresh after Write`.

   * If the end user selects to invalidate the token, the journey continues to the Invalidate Token node.

   * The Invalidate Token node is a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/scripted-decision.html) configured with the following script:

     ```javascript
     cacheManager.named("tokenCache").invalidateAll();
     action.goTo("true");
     ```

     The script evicts all the entries and the journey continues.

   * The Refresh Token node offers the end user the chance to get a new token:

     * Yes

       The Get Access Token node queries the cache, which no longer has any entries. The cache manager runs the `reload()`, and in turn, the `load()` function to create a new access token. This is cached. The journey continues to display the new token.

     * No

       The journey completes.

## Manage script caches

This section covers how to refresh or remove entries, monitor cache performance, and clear caches using the REST API.

### Refresh the cache

You can refresh an entry in the cache in the following way:

1. Set the cache eviction policy to [Refresh after write](../setup/services-configuration.html#cachemanager-service-eviction-policy).

2. Define a `reload()` function in your cache loading script with the following signature:

   `Object reload(Map<String, String> key, Object oldValue)`

   For example, this implementation returns the first value in the `key` map.

   ```javascript
   function reload(key, oldValue) {
       return load(key);
   }
   ```

3. Call the `refresh()` method on the [`cacheManager`](scripting-api-node.html#scripting-api-node-cachemanager) binding to invoke the cache reload function.

### Remove cached values

To evict entries from the cache immediately before the expiry period is reached, use the cache methods, `invalidate` or `invalidateAll`, through the [`cacheManager`](scripting-api-node.html#scripting-api-node-cachemanager) binding.

For example:

```javascript
// remove a single entry
if (cacheManager.exists("A")) {
    var cacheA = cacheManager.named("A");
    cacheA.invalidate({"some":"key"});
}

// remove all entries from the cache
if (cacheManager.exists("B")) {
    cacheManager.named("B").invalidateAll();
}

action.goTo("true");
```

AM securely removes cached values by zeroizing the memory related to the entries.

### Monitor the cache usage

You can monitor the use and performance of a scripting cache by calling the [Prometheus endpoints](../monitoring/monitoring-prometheus.html) and checking for the `am_script_cache_*` metrics.

When you create a new cache, the monitoring service registers metrics with the following tags for filtering and querying:

* `cache_name`: The name of the cache.

* `event`: The possible events are: `eviction`, `hit`, `miss`, `invalidate`, `invalidateAll`, `load_failure`, `load_time_seconds`, `load_count`, `memory_bytes`, `size`.

* `realm`: The realm the cache belongs to.

Learn more in [Script cache metrics](../monitoring/monitoring-metrics.html#ref-script-cache-metrics).

### Clear a cache using REST

AM provides the following endpoints for clearing caches:

* Clear a specific cache

  `/realm-config/services/cache-manager/caches/cache-name?_action=clear`

  For example:

  ```bash
  $ curl \
  --request POST \
  --header "Accept-API-Version: resource=1.0" \
  --header "iPlanetDirectoryPro: AQIC5wM…​TU3OQ*" \
  "https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/services/cache-manager/caches/cache-name?_action=clear"
  {}
  ```

* Clear all caches in a realm

  `/realm-config/services/cache-manager?_action=clear`

  For example:

  ```bash
  $ curl \
  --request POST \
  --header "Accept-API-Version: resource=1.0" \
  --header "iPlanetDirectoryPro: AQIC5wM…​TU3OQ*" \
  "https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/services/cache-manager?_action=clear"
  {}
  ```

---

---
title: Common bindings
description: Reference common script bindings that PingAM injects into script execution contexts for accessing functionality and performing operations like logging
component: pingam
version: 8.1
page_id: pingam:am-scripting:script-bindings
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/script-bindings.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripts"]
page_aliases: ["scripting-guide:script-bindings.adoc"]
section_ids:
  common-cookiename: Retrieve cookie name
  common-httpclient: Access HTTP services
  methods: Methods
  httpclient-sync-get: "Example: Send a synchronous request (GET)"
  httpclient-sync: "Example: Send a synchronous request (POST)"
  httpclient-async: "Example: Send an asynchronous request"
  httpclient-mtls: "Example: Send a request using mTLS and set timeouts"
  httpclient-mtls-config-service: Configure the HTTP Client service
  httpclient-mtls-map-secret: Map a certificate to the secret label
  httpclient-mtls-create-script: Create a script to send the HTTP request
  httpclient-proxy: "Example: Route a request through a proxy"
  httpclient-proxy-service: Configure the HTTP Client service
  httpclient-proxy-map-secret: Map a secret to the secret label
  httpclient-proxy-create-script: Create a script to send the HTTP request
  common-locales: Get localized messages
  method: Method
  example: Example
  common-logger: Log script messages
  common-journey: Get journey details
  methods_2: Methods
  example_2: Example
  common-openidm: Access IDM scripting functions
  openidm-exception-handling: Handle openidm exceptions
  common-realm: Output realm name
  common-scriptName: Output script name
  common-secrets: Access secrets and credentials
  methods_3: Methods
  examples: Examples
  common-systemenv: Reference substituted properties in scripts
  common-utils: Access utility functions
  common-policy: Evaluate policies
  methods_4: Methods
  example_3: Example
---

# Common bindings

Each [script type](scripting-api.html) exposes a number of *bindings*, objects that AM injects into the script execution context. The bindings provide a stable way of accessing AM functionality, without the need to allowlist Java classes. Scripts are provided with all the bindings for their context at the point of execution.

Find information about context-specific bindings in the documentation for each script type.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | AM has introduced a [next-generation scripting engine](next-generation-scripts.html) that offers several benefits, including enhanced script bindings.The availability and usage of bindings depend on the script engine version of the script: legacy or next-generation. Both versions are described in this section.You can find information about migrating to the enhanced scripting engine in [Migrating to next-generation scripts](next-generation-scripts.html#migrate-to-v2-steps). |

The following bindings are common to many authentication and authorization scripts. Use these bindings to access data and perform script operations such as logging.

|              |                                                                                                                    |                  |                     |
| ------------ | ------------------------------------------------------------------------------------------------------------------ | ---------------- | ------------------- |
| **Binding**  | **Description**                                                                                                    | **Availability** |                     |
|              |                                                                                                                    | **Legacy**       | **Next-generation** |
| `cookieName` | Access the name of the current cookie.                                                                             | No               | Yes                 |
| `httpClient` | Make outbound HTTP calls.                                                                                          | Partial 1        | Yes                 |
| `locales`    | Get a localized message.                                                                                           | No               | Partial 3           |
| `logger`     | Write a message to the AM debug log.                                                                               | Yes              | Yes                 |
| `journey`    | Identify the current journey and get information about the journey and its configuration.                          | No               | Partial 3           |
| `openidm`    | Manage a IDM resource.                                                                                             | No               | Yes                 |
| `policy`     | Evaluate policies using the policy engine API.                                                                     | No               | Yes                 |
| `realm`      | Access the realm to which the user is authenticating.                                                              | Yes              | Yes                 |
| `scriptName` | Access the name of the running script.                                                                             | Partial 1        | Yes                 |
| `secrets`    | Reference secrets and credentials from scripts.                                                                    | Partial 2        | Yes                 |
| `systemEnv`  | Reference system properties.                                                                                       | Yes              | Yes                 |
| `utils`      | Access utility functions such as base64 encoding/decoding, cryptographic operations, and generating random values. | No               | Yes                 |

1 Available in OAuth 2.0 script types, Scripted Decision node scripts, and SAML 2.0 scripts.

2 Available in OAuth 2.0 JWT bearer and Scripted Decision node scripts.

3 Available in Configuration Provider node, Scripted Decision node, Device Match node, and custom node scripts.

|   |                                                                                                                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Make sure you don't use the same name for a local variable as that of a common binding in your script. These names are reserved for common bindings only.If you have already defined a local variable with the same name as one that's added to common bindings in a more recent version of AM; for example, `utils`, you must rename the variable in your scripts before you upgrade. |

## Retrieve cookie name

The `cookieName` binding lets you access the name of the cookie as a string. You can use the cookie name to perform session actions such as ending all open sessions for a user.

```javascript
// add cookie name to shared state, for example: iPlanetDirectoryPro
nodeState.putShared("myCookie", cookieName);
```

The `cookieName` binding is available in next-generation scripts only.

## Access HTTP services

Call HTTP services with the `httpClient.send` method. HTTP client requests are asynchronous, unless you invoke the `get()` method on the returned object.

### Methods

* Next-generation

* Legacy

The `httpClient` binding uses native JavaScript objects to send requests and receive responses, in a similar way to the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API).

* To invoke an HTTP request

  * **`ResponseScriptWrapper httpClient.send(String uri, Map requestOptions).get()`**

    Sends a synchronous request to the specified URI with request options.

    The `requestOptions` parameter is a native JavaScript object that supports these attributes:

    | Field        | Type                                                                                                                                                                                                                                                                                                                                    |
    | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `method`     | The HTTP request method. For example, `GET`, `POST`, `PUT`, `DELETE`, `HEAD`.                                                                                                                                                                                                                                                           |
    | `headers`    | The request headers. For example, `"Content-Type": "application/json"`.                                                                                                                                                                                                                                                                 |
    | `form`       | Required for sending a form request.The `form` attribute automatically URL-encodes fields, and you don't need to specify `"Content-Type": "application/x-www-form-urlencoded"` as part of the headers.For example:```javascript
    var requestOptions = {
      method: "POST",
      form: {
        field1: "value1",
        field2: "value2"
      }
    }
    ``` |
    | `clientName` | The HTTP client instance required for [sending a request using MTLS](#httpclient-mtls).                                                                                                                                                                                                                                                 |
    | `token`      | The token specified as the Authorization header, for example, when [sending a synchronous request](#httpclient-sync).                                                                                                                                                                                                                   |
    | `body`       | The content of the request. Not specified for `GET`, `HEAD`, or `TRACE` methods.                                                                                                                                                                                                                                                        |

  * **`ResponseScriptWrapper httpClient.send(String uri).get()`**

    Sends a synchronous GET request with no additional request options.

* To access response data

  Use the following methods to get response information:

  * **`Map response.formData()`**

  * **`Map response.json()`**

  * **`String response.text()`**

  The following fields provide response status information:

  | Field        | Type    |
  | ------------ | ------- |
  | `headers`    | Map     |
  | `ok`         | boolean |
  | `status`     | integer |
  | `statusText` | String  |

  The response is similar to [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) object behavior.

- To invoke a synchronous HTTP request

  * **`HTTPClientResponse httpClient.send(Request request).get()`**

- To access response data

  * **`JSON.parse(response.getEntity().getString())`**

    `HttpClientResponse` methods:

  * **`Map<String, String> getCookies()`**

  * **`String getEntity()`**

  * **`Map<String, String> getHeaders()`**

  * **`String getReasonPhrase()`**

  * **`Integer getStatusCode()`**

  * **`boolean hasCookies()`**

  * **`boolean hasHeaders()`**

|   |                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `httpClient` script binding automatically adds the current transaction ID as an HTTP header, `X-ForgeRock-TransactionId`. This lets you correlate caller and receiver logs when you use `httpClient` from your script to make requests to other AM products and services. |

The following examples demonstrate different ways to send HTTP client requests:

* [Example: Send a synchronous request (GET)](#httpclient-sync-get)

* [Example: Send a synchronous request (POST)](#httpclient-sync)

* [Example: Send an asynchronous request](#httpclient-async)

* [Example: Send a request using mTLS and set timeouts](#httpclient-mtls)

### Example: Send a synchronous request (GET)

The following example uses the `httpClient` binding in a next-generation script to make a GET request to generate random UUIDs.

```javascript
var BASE_URL = "http://www.randomnumberapi.com/api/v1.0/uuid";

var COUNT = 5;

var options = {
  method: "GET",
  headers: {
    "Content-Type": "application/json; charset=UTF-8"
  }
};
var requestURL = `${BASE_URL}?count=${COUNT}`;

var response = httpClient.send(requestURL, options).get();

if (response.status === 200) {
  var uuids = JSON.parse(response.text());
  nodeState.putShared("uuids", uuids);
  action.goTo("true");
} else {
  logger.error("Error generating UUIDs: " + response.statusText);
  action.goTo("false");
}
```

Use a [Debug node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/debug.html) to verify the UUIDs stored in `nodeState`. For example:

```json
{
    ...
    "uuids": [
        "d787a51e-7b2a-4eba-9d87-7ec555ec9f32",
        "f561381a-ec03-4b48-8d6d-828c80d43805",
        "6d9ef759-be3d-414d-a942-dce8d3840b59",
        "40737769-0c91-41e9-a0c4-7deab4a15aea",
        "5a40bdb6-62d3-406f-bd23-71be1d5a54f5"
    ]
}
```

### Example: Send a synchronous request (POST)

The following example uses the `httpClient` binding to send a synchronous authentication request and check for success.

* Next-generation

* Legacy

```javascript
var bearerToken = "Bearer abcd-1234";

var requestOptions = {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  token: bearerToken, // Equivalent to Authorization header
  body: {
    username: "bjensen"
  }
}

var requestURL = "https://my.auth.server/authenticate";
var response = httpClient.send(requestURL, requestOptions).get();

if (response.status === 200) {
    action.goTo("true");
} else {
    action.goTo("false");
}
```

```javascript
var fr = JavaImporter(org.forgerock.openam.auth.node.api.Action);

var requestURL = "https://my.auth.server/authenticate";
var request = new org.forgerock.http.protocol.Request();
request.setUri(requestURL);
request.setMethod("POST");
request.getHeaders().add("Content-Type", "application/json;");
request.getHeaders().add("Authorization", "Bearer abcd-1234");
request.setEntity(JSON.stringify({"username": "bjensen"}));

var response = httpClient.send(request).get();

var responseCode = response.getStatus().getCode();
if (responseCode === 200) {
    action = fr.Action.goTo("true").build();
} else {
    action = fr.Action.goTo("false").build();
}
```

### Example: Send an asynchronous request

The `httpclient` binding also supports asynchronous requests so that you can perform non-blocking operations, such as recording logging output after the script has completed.

To make an asynchronous request, use the same method signatures to send the request but without calling `get()` on the returned object. The `send()` method then initiates a separate thread to handle the response. Callers are unable to control when the asynchronous call is processed, so won't be able to use the response as part of authentication processing.

* Next-generation

* Legacy

```javascript
public Promise<ResponseScriptWrapper, HttpClientScriptException> send(String uri)
public Promise<ResponseScriptWrapper, HttpClientScriptException> send(String uri, Map<String, Object> requestOptions)
```

```javascript
public Promise<Response, NeverThrowsException> send(Request request)
```

For example:

* Next-generation

* Legacy

```javascript
var requestURL = "https://my.auth.server/audit";
// creates separate thread to handle response
var response = httpClient.send(requestURL).then((response) => {
  if (!response) {
    logger.error("Bad response from " + requestURL);
    return;
  }
  if (response.status != 200) {
    logger.error("Unexpected response: " + response.statusText);
    return;
  }
  logger.debug("Returned from async request");
});
// continues processing whilst awaiting response
action.goTo("true");
```

```javascript
var fr = JavaImporter(
    org.forgerock.http.protocol.Request,
    org.forgerock.http.protocol.Response,
    org.forgerock.openam.auth.node.api.Action);

var request = new fr.Request();
request.setUri("https://my.auth.server/audit");
request.setMethod("GET");

var response = httpClient.send(request).then((response) => {
  if (!response) {
    logger.error("Bad response from " + requestURL);
    return;
  }
  var status = response.getStatus().getCode();

  if (status != 200) {
    logger.error("Unexpected response: " + response.getEntity().getString());
    return;
  }
  logger.message("Returned from async request");
});

action = fr.Action.goTo("true").build();
```

### Example: Send a request using mTLS and set timeouts

Configure the `httpclient` to use mTLS to exchange data securely when making a request to an external service.

Follow these example steps to send an HTTP request using mTLS:

1. [Configure an instance of the HTTP Client service](#httpclient-mtls-config-service)

2. [Map a client certificate to a secret label](#httpclient-mtls-map-secret)

3. [Create a script to send the request](#httpclient-mtls-create-script)

#### Configure the HTTP Client service

Complete these steps to configure an instance of the HTTP Client service.

The instance defines settings such as timeout values and the client certificate or truststore secret labels required by the `httpclient` script binding to make a TLS connection.

You can configure the instance to override default values. For example, to set connection or response timeout values for a request initiated by the HTTP client, enable `Use Instance Timeouts` in the service instance and set the timeout accordingly.

You can find information about these settings in the [Http Client service configuration](../setup/services-configuration.html#global-httpclient).

1. In the AM admin UI, go to Realms > *realm name* > Services.

2. Click Add a Service and select Http Client Service from the list of service types.

3. Enable the service and save your changes.

4. On the Secondary Configurations tab, click Add a Secondary Configuration.

5. Provide a name for the HTTP client instance; for example, `myHttpClient`, and click Create.

6. Enable the configuration and save your changes.

   Make sure both the service *and* the secondary configuration are enabled.

7. On the TLS Configuration tab, enter an identifier to be used in your secret label in the Client Certificate Secret Label Identifier field.

   For example, `testCrt` creates the [dynamic secret label](../security/secret-mapping.html#httpclient-secret-labels), `am.services.httpclient.mtls.clientcert.testCrt.secret`.

   |   |                                                                                                                                                                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To specify a truststore to verify the target server's certificate, provide a value for Server Trust Certificates Secret Label Identifier.This creates the [dynamic secret label](../security/secret-mapping.html#httpclient-secret-labels), `am.services.httpclient.mtls.servertrustcerts.identifier.secret`. |

8. Optionally, configure connection and response timeout values on the Timeouts tab. Enable Use Instance Timeouts to override the default settings in advanced properties.

9. Save your changes.

#### Map a certificate to the secret label

1. Upload a PKCS#12 certificate (`.p12` file) to a directory accessible to your AM deployment. It must contain a private key and a certificate.

   For testing purposes, you can create your own `.p12` file using [openssl](https://docs.openssl.org/1.1.1/man1/pkcs12/).

   If you have a PEM file containing both the certificate and a private key, you can use `openssl` to create a PKCS#12 file:

   ```bash
   openssl pkcs12 -export -in myfile.pem -out mycert.p12 -name myAlias
   ```

   If your PEM file includes a certificate chain, for example, a client certificate issued by a certificate authority (CA), concatenate the certificates in the order required by [RFC 4346](https://www.rfc-editor.org/rfc/rfc4346.html#section-7.4.2):

   1. The client certificate (`client.crt`)

   2. Any intermediate CA certificates

   3. The root CA certificate (`ca.crt`)

   Then append the private key:

   ```bash
   cat client.crt ca.crt client.key > myfile.pem
   ```

   To verify the resulting PEM file is valid, you can use `openssl` to run the following command:

   ```bash
   openssl x509 -in myfile.pem -noout -text
   ```

   To check the details of the keystore file, run the following `keytool` command:

   ```bash
   keytool -list -v -keystore mycert.p12 -storetype pkcs12
   ```

   > **Collapse: Example output**
   >
   > ```bash
   > Keystore type: PKCS12
   > Keystore provider: SUN
   >
   > Your keystore contains 1 entry
   >
   > Alias name: myalias
   > Creation date: Mar 19, 2025
   > Entry type: PrivateKeyEntry
   > Certificate chain length: 1
   > Certificate[1]:
   > Owner: CN=BadSSL Client Certificate, O=BadSSL, L=San Francisco, ST=California, C=US
   > Issuer: CN=BadSSL Client Root Certificate Authority, O=BadSSL, L=San Francisco, ST=California, C=US
   > Serial number: adb285150f249509
   > Valid from: Tue Mar 18 21:00:15 UTC 2025 until: Thu Mar 18 21:00:15 UTC 2027
   > Certificate fingerprints:
   > SHA1: 0D:51:42:C2:2A:67:8D:14:11:2F:4E:04:C9:75:3F:36:AA:03:5E:AD
   > SHA256: 8A:CD:0E:83:1A:1F:6C:5F:0F:A0:50:2D:7C:48:5C:0A:96:84:9A:29:A7:02:54:57:BB:F1:0B:6D:53:89:21:5A
   > Signature algorithm name: SHA256withRSA
   > Subject Public Key Algorithm: 2048-bit RSA key
   > Version: 3
   >
   > Extensions:
   >
   > #1: ObjectId: 2.5.29.19 Criticality=false
   > BasicConstraints:[
   > CA:false
   > PathLen: undefined
   > ]
   >
   > #2: ObjectId: 2.5.29.15 Criticality=false
   > KeyUsage [
   > DigitalSignature
   > Non_repudiation
   > Key_Encipherment
   > ]
   >
   > #3: ObjectId: 2.16.840.1.113730.1.1 Criticality=false
   > NetscapeCertType [
   > SSL client
   > ]
   > ```

2. [Create secret label mappings](../security/secret-mapping.html#create-mappings) for the keystore and entry passwords in an existing store.

   For example, save the passwords in two files mapped to secrets in a file system secret volume, `mystorepass` and `myentrypass`.

3. [Create a keystore](../security/secret-stores.html#create-keystore-secret-stores) in AM with the following settings:

   * File

     `/path/to/mycert.p12`

   * Keystore type

     `PKCS12`

   * Store password secret label

     `mystorepass`

   * Entry password secret label

     `myentrypass`

4. Map the Http Client service secret label to the keystore. For example:

   * Secret Label

     `am.services.httpclient.mtls.clientcert.testCrt.secret`

   * Aliases

     `myalias`

#### Create a script to send the HTTP request

Write a [next-generation decision node script](next-generation-scripts.html) to send a request using the HTTP client instance in the request options.

1. In your script, specify your HTTP client instance as the value for `clientName` in `requestOptions`.

   For example:

   ```javascript
   var requestOptions = {
     "clientName": "<myhttpclient>"       (1)
   }
   var res = httpClient.send("https://client.badssl.com",
                             requestOptions).get();         (2)
   action.withHeader(`Response code: ${res.status}`);

   if (res.status == 200) {
     action.withDescription(res.text());
   } else {
     logger.error(res.text());
     action.goTo("false");
   };
   ```

   |       |                                                                                                                                           |
   | ----- | ----------------------------------------------------------------------------------------------------------------------------------------- |
   | **1** | The `clientName` attribute must reference an enabled instance of the HTTP Client service.                                                 |
   | **2** | This script uses a test site that checks that the request includes a particular client certificate. Replace this with your mTLS endpoint. |

2. Create a simple journey that includes the Scripted Decision node to test your changes.

3. Verify that the HTTP request is sent successfully.

   If successful, the example script results in a webpage displaying a response code of 200 on a green background.

### Example: Route a request through a proxy

Follow these example steps to send an external HTTP request by connecting to a proxy server:

1. [Configure an instance of the HTTP Client service](#httpclient-proxy-service)

2. [Map a secret to a secret label](#httpclient-proxy-map-secret)

3. [Create a script to send the request](#httpclient-proxy-create-script)

#### Configure the HTTP Client service

Configure an instance of the HTTP Client service to override the proxy connection defined in the [advanced server properties](../setup/server-advanced.html). This lets you use specific proxy settings per request.

This example configures a proxy connection with authentication, but this is optional.

1. In the AM admin UI, go to Realms > *Realm Name* > Services.

2. Click Add a Service and select Http Client Service from the list of service types.

3. Enable the service and save your changes.

4. On the Secondary Configurations tab, click Add a Secondary Configuration.

5. Provide a name for the HTTP client instance; for example, `myHttpClient`, and click Create.

6. Enable the configuration and save your changes.

   Make sure both the service *and* the secondary configuration are enabled.

7. On the Proxy Configuration tab, enable Use Instance Proxy, and enter values for the following fields:

   * Proxy URI

     The proxy server URI, for example: `https://proxyexample.com:8888`.

   * Proxy Username

     The username to use for proxy authentication, for example: `admin`.

   * Proxy Secret Label Identifier

     The identifier for the secret label mapping to use for proxy authentication, for example: `myProxy`.

     This creates the secret label `am.services.httpclient.proxy.myProxy.secret`.

   You can find information about these settings in the [Http Client proxy configuration](../setup/services-configuration.html#httpclient-secondary-config-proxy).

8. Save your changes.

#### Map a secret to the secret label

To enable proxy authentication, [create a secret in a secret store and map it](../security/secret-mapping.html#create-mappings) to the dynamic label generated from the proxy configuration.

For example, to map a label to a secret in a file:

1. [Configure a directory](../security/secret-stores.html#create-file-system-secret-volumes) as a file system secret store.

2. Create the required file to store your secret. If you set the proxy secret label identifier to `myProxy`, name your file `am.services.httpclient.proxy.myProxy.secret` (when no suffix is required).

3. Save your password to the file.

#### Create a script to send the HTTP request

Write a [next-generation decision node script](next-generation-scripts.html) to send a request using the HTTP client instance in the request options.

1. In your script, specify the name of your HTTP client instance as the value for `clientName` in `requestOptions`.

   For example:

   ```javascript
   var requestOptions = {
     "clientName": "<myHttpClient>"
   }
   var res = httpClient.send("https://example.com",
                             requestOptions).get();
   logger.info(`Status code: ${res.status}`);

   if (res.status == 200) {
     action.goTo("true");
   } else {
     logger.error(res.text());
     action.goTo("false");
   };
   ```

2. Create a simple journey that includes the Scripted Decision node to test your changes.

3. Verify that the HTTP request is sent successfully using the configured proxy connection.

## Get localized messages

Use the next-generation `locales` binding to return the localized version of a string from a translation map.

The binding determines the best locale based on the `Accept-Language` HTTP header or default system settings, in a similar way to the [Message node](https://docs.pingidentity.com/auth-node-ref/8.1/message.html).

If no match is found, the first entry in the map is returned.

### Method

`String getLocalizedMessage(Map<String, String> localizations)`

### Example

The following example sets the `greeting` property to `Hello` for a United States English locale. For *British* English settings, the greeting is set to the first entry in the map, `Gutentag`, because no match is found.

```javascript
var languageMap =
{
  'de': 'Gutentag',
  'no': 'Hei',
  'fr': 'Bonjour',
  'en-US': 'Hello'
};

var greeting = locales.getLocalizedMessage(languageMap);
```

## Log script messages

Write messages to AM debug logs by using the `logger` object.

Scripts that create debug messages have their own logger which is created after the script has executed at least once.

Logger names use the format: `scripts.<context>.<script UUID>.(<script name>)`; for example, `scripts.OIDC_CLAIMS.36863ffb-40ec-48b9-94b1-9a99f71cc3b5.(OIDC Claims Script)`.

You can find information about debug logs in [Debug logging](../monitoring/debug-logging.html).

* Next-generation

* Legacy

The `ScriptedLoggerWrapper` is based on the [SLF4J](https://www.slf4j.org) logging framework. You can log messages at the following levels:

* Trace

* Debug

* Info

* Warn

* Error

```javascript
var traceEnabled = logger.isTraceEnabled();
logger.trace("Trace with arg {}", arg);
var debugEnabled = logger.isDebugEnabled();
logger.debug("Debug with arg {}", arg);
var infoEnabled = logger.isInfoEnabled();
logger.info("Info with arg {}", arg);
var warnEnabled = logger.isWarnEnabled();
logger.warn("Warn with arg {}", arg);
var errorEnabled = logger.isErrorEnabled();
logger.error("Error with arg {}", arg);
```

The `Debug` logger lets you log messages at the following levels:

* Message

* Warning

* Error

```javascript
var messageEnabled = logger.messageEnabled();
logger.message("Message with arg {}", arg);
var warnEnabled = logger.warningEnabled();
logger.warning("Warn with arg {}", arg);
var errorEnabled = logger.errorEnabled();
logger.error("Error with arg {}", arg);
```

## Get journey details

The next-generation `journey` binding provides information about the current journey (tree).

Call the following methods to access details about the journey and how it's configured.

### Methods

* String name()

  Returns the name of the current journey. This can be an inner or an outer journey.

* String identityResource()

  Returns the identity resource of the current tree. For example, `managed/user`.

* boolean innerJourney()

  Returns true if the current journey is [configured to run as an inner journey only](../am-authentication/configure-auth-trees.html#disable-inner-tree).

* boolean mustRun()

  Returns true if the current journey is [set to always run](../am-authentication/configure-auth-trees.html#authn-mustrun-tree) regardless of whether the user authenticated successfully and a session exists or not.

### Example

* Next-generation

* Legacy

```javascript
var currentJourney = journey.name();

logger.info("Identity resource: " + journey.identityResource());

if (journey.innerJourney()){
  logger.info(currentJourney + " is an inner journey.");
}
if(journey.mustRun()){
  logger.info(currentJourney + " is a mustRun journey.");
}
```

*Not available in Legacy bindings*

## Access IDM scripting functions

The `openidm` binding lets you manage a IDM resource by calling scripting functions directly from a decision node script.

|   |                                                                         |
| - | ----------------------------------------------------------------------- |
|   | The `openidm` binding is only available when AM is integrated with IDM. |

The following CRUDPAQ functions are supported:

* create

* read

* update

* delete

* patch

* action

* query

For more information, refer to [Scripting functions](https://docs.pingidentity.com/pingidm/8.1/scripting-guide/scripting-func-ref.html).

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `openidm` binding provides administrative access to IDM functions. Use it with caution to prevent the exposure of sensitive data. |

The following example illustrates how to create a user, update their details, send an email, and finally delete the user:

* Next-generation

* Legacy

```javascript
var username = "bjensen";

// CREATE: returns the new user identity as a JSON object (wrapped in a MapScriptWrapper)
var newUser = openidm.create("managed/user", null, {
  "userName": username,
  "mail": "foo@bar.com",
  "givenName": "Foo",
  "sn": "Bar"});

// Access the fields directly, for example: ._id, .sn, .city, .country
var userID = newUser._id;

// READ: returns entire identity as a JSON object
var user = openidm.read("managed/user/" + userID);

// Debug to output all fields
logger.debug("user: " + JSON.stringify(user));

// UPDATE: replaces entire identity with specified object
// Returns the updated identity as a JSON object
user.description = 'New description';
var updatedUser = openidm.update("managed/user/" + userID, null, user);

// PATCH: selectively modify object, returns entire identity
var patchedUser = openidm.patch("managed/user/" + userID, null, [{
        "operation":"replace",
        "field":"/mail",
        "value":"new@example.com"
}]);

// QUERY: returns results array in a map
var queryRes = openidm.query("managed/user",
    {"_queryFilter":`/userName eq '${username}'`},["*", "_id"]);

// Debug query result count and the requested properties
logger.debug("Query result count: " + queryRes.resultCount);
logger.debug("Queried user: " + queryRes.result[0].givenName);

// ACTION: send email using the action function
var actionRes = openidm.action("external/email", "send", {
    "from": "admin@example.com",
    "to": patchedUser.mail,
    "subject": "Example email",
    "body": "This is an example"
});
// Example response if not null: {"status":"OK","message":"Email sent"}
logger.debug("Status: " + actionRes.status + " : " + actionRes.message);

// DELETE: returns deleted object if successful, throws exception if not
openidm.delete('managed/user/'+ userID, null);

action.goTo("true");
```

*Not available in Legacy bindings*

### Handle `openidm` exceptions

When an `openidm` call fails, the Rhino scripting engine wraps the thrown Java exception in a `WrappedException`. Access the underlying exception through the `javaException` property of the caught error.

The `javaException` object exposes the following methods:

* `getCode()`

  Returns the HTTP-style error code as an integer, for example, `404`.

* `getReason()`

  Returns a short string describing the reason for the error, for example, `"Not Found"`.

* `getDetail()`

  Returns additional detail as a `JsonValue` object.

* `isServerError()`

  Returns `true` if the error code is in the 5xx range.

The `message` property is available directly on the caught error without `.javaException`.

```javascript
try {
    var user = openidm.read("managed/alpha_user/some-id");
} catch (e) {
    var code     = e.javaException.getCode();
    var reason   = e.javaException.getReason();
    var detail   = e.javaException.getDetail();
    var isServer = e.javaException.isServerError();
    var message  = e.message;
}
```

This applies to all `openidm` binding methods: `read`, `create`, `update`, `delete`, `patch`, `action`, and `query`.

|   |                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | In promise-based `.thenCatch()` paths, the `javaException` object is passed directly to the handler, so you can call `e.getCode()` without using `.javaException`. |

## Output realm name

The `realm` binding lets you access the name of the realm to which the user is authenticating as a string.

For example, authenticating to the `alpha` realm returns a string value of `/alpha`.

* Next-generation

* Legacy

```javascript
// log current realm
logger.debug("User authentication realm: " + realm);
```

```javascript
// log current realm
logger.message("User authentication realm: " + realm);
```

## Output script name

Use the `scriptName` binding to get the name of the running script as a string.

* Next-generation

* Legacy

```javascript
// log current script name
logger.debug("Running script: " + scriptName);

// or use a library script to log script name
var mylib = require('loggingLibrary');
mylib.debug(logger, scriptName);
```

```javascript
// log current script name
logger.message("Running script: " + scriptName);
```

## Access secrets and credentials

Use the `secrets` binding to access secrets configured in [AM secret stores](../security/secrets-certs-keys.html).

For example, a script can access credentials or secrets defined in a file system secret volume to make outbound calls to a third-party REST service without hard-coding those credentials in the script.

|   |                                                                                           |
| - | ----------------------------------------------------------------------------------------- |
|   | Only secret labels that begin with the string `scripted.node.` are accessible to scripts. |

### Methods

Use the following method to return the value of the specified secret label:

* String secrets.getGenericSecret(String secretLabel)

  If the secret label is defined at the realm level, its value is returned; otherwise, the script returns the value defined at the global level.

  To format the returned secret value, use these supported methods:

  * getAsBytes()

    Retrieve the secret value in `byte[]` format.

  * getAsUtf8()

    Retrieve the secret value in UTF-8 format.

### Examples

The following example scripts show how to get a password from a secret label named `scripted.node.example.secret`. The scripts use the encoded username (`bjensen`) and password (`passwd`) in a basic authentication header to access the [http://httpbin.org/basic-auth/{user}/{passwd}](http://httpbin.org/#/Auth/get_basic_auth__user__passwd_) service.

* Next-generation

* Legacy

```javascript
// secret [cGFzc3dk] stored in file system secret store
var password = secrets.getGenericSecret("scripted.node.example.secret").getAsUtf8();

var auth = utils.base64.encode("bjensen:" + password);

var requestURL = "http://httpbin.org/basic-auth/bjensen/passwd";

var requestOptions = {
  method: "GET",
  headers: {
    "Content-Type": "application/json",
    "Authorization": "Basic ".concat(auth)
  },
}
var response = httpClient.send(requestURL, requestOptions).get();

if (!response) {
  logger.error("Bad response from " + requestURL);
  action.goTo("false");
} else {
  if (response.status != 200) {
    logger.warn("Authentication not successful. Code: " + response.status);
    action.goTo("false");
  } else {
    logger.debug("Authenticated: " + response.json().authenticated);
    action.goTo("true");
  }
}
```

|   |                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------- |
|   | To construct the header for basic authorization, make sure you use the `concat()` function rather than `+` to append credentials. |

|   |                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To use this sample script, add the following classes to the class allowlist property in the `AUTHENTICATION_TREE_DECISION_NODE` scripting engine configuration:- `org.mozilla.javascript.ConsString`

- `java.util.Base64`

- `java.util.Base64$Encoder`For details, refer to [Access Java classes](scripting-env.html#scripting-env-java-classes). |

```javascript
var fr = JavaImporter(org.forgerock.openam.auth.node.api.Action);

// secret [cGFzc3dk] stored in file system secret store
var password = secrets.getGenericSecret("scripted.node.example.secret").getAsUtf8();

var auth = java.util.Base64.getEncoder().encodeToString(java.lang.String("bjensen:" + password).getBytes());

var request = new org.forgerock.http.protocol.Request();
request.setMethod("GET");
request.setUri("http://httpbin.org/basic-auth/bjensen/passwd");
request.getHeaders().add("content-type","application/json; charset=utf-8");
request.getHeaders().add("Authorization", "Basic " + auth);

var response = httpClient.send(request).get();
var jsonResult = JSON.parse(response.getEntity().getString());
logger.message("Script result: " + JSON.stringify(jsonResult));

if (jsonResult.hasOwnProperty("authenticated")) {
  action = fr.Action.goTo("success").build();
} else {
  action = fr.Action.goTo("failure").build();
}
```

## Reference substituted properties in scripts

The `systemEnv` binding, available to all script types, includes an instance of the [ScriptPropertyResolver](../_attachments/apidocs/org/forgerock/openam/scripting/api/ScriptPropertyResolver.html) class. This interface exposes the following methods:

```java
String getProperty(String propertyName);
String getProperty(String propertyName, String defaultValue);
<T> T getProperty(String propertyName, String defaultValue, Class<T> returnType);
```

where:

* `propertyName` refers to a [configuration expression](../setup/property-value-substitution.html#configuration-expressions) (without the ampersand or braces)

  To reference a substituted property in a script, the property name *must* include a specific prefix; for example, `script.my.variable`. This prefix decreases the risk that random property values are resolved in scripts.

  The default prefix for all script types, is `script`. To change the prefix, go to Configure > Global Services > Scripting > Secondary Configurations > *Script Type* > Secondary Configurations > Engine Configuration > Property Name Prefix.

  Make sure `propertyName` is specific enough to distinguish it from other configuration expressions.

* `defaultValue` is the default value set for that property in the configuration expression

  The `defaultValue` must not be `null`.

* `returnType` is one of the following fully-qualified Java class names:

  * `java.lang.Boolean`

  * `java.lang.Double`

  * `java.lang.Integer`

  * `java.lang.String`

  * `java.util.List`

  * `java.util.Map`

The `getProperty(String propertyName)` method returns `null` when the `propertyName` is not valid.

For example:

The following example assumes that the property name prefix is set to `script` in the script engine configuration for the script type.

The script is used in a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/scripted-decision.html) to get the values such as the user's `email`, `hostname`, and `port`. The script also shows type transformation where the type isn't a string.

* JavaScript

* Groovy

```javascript
var fr = JavaImporter(org.forgerock.openam.auth.node.api.Action);

// Properties should get resolved (set in AM)
var email = systemEnv.getProperty('script.tree.decision.node.email');
var name = systemEnv.getProperty('script.tree.decision.node.hostname', 'defaultHostname');
var port = systemEnv.getProperty('script.tree.decision.node.port', '587', java.lang.Integer);
var double = systemEnv.getProperty('script.tree.decision.node.double', '2.0', java.lang.Double);
var hasPort = systemEnv.getProperty('script.tree.decision.node.hasPort', 'false', java.lang.Boolean);
var map = systemEnv.getProperty('script.tree.decision.node.map', '{"defaultKey":"defaultValue"}', java.util.Map);
var list = systemEnv.getProperty('script.tree.decision.node.list', 'defaultValue', java.util.List);

// Properties should get resolved to their defaults (not set in AM)
var defaultName = systemEnv.getProperty('script.tree.decision.node.hostname.unresolved', 'defaultHostname');
var defaultPort = systemEnv.getProperty('script.tree.decision.node.port.unresolved', '587', java.lang.Integer);
var defaultDouble = systemEnv.getProperty('script.tree.decision.node.double.unresolved', '2.0', java.lang.Double);
var defaultHasPort = systemEnv.getProperty('script.tree.decision.node.hasPort.unresolved', 'false', java.lang.Boolean);
var defaultMap = systemEnv.getProperty('script.tree.decision.node.map.unresolved', '{"defaultKey":"defaultValue"}', java.util.Map);
var defaultList = systemEnv.getProperty('script.tree.decision.node.list.unresolved', 'defaultFirstValue,defaultSecondValue', java.util.List);

// Assert all property values - set the appropriate outcome
if (email === 'test@example.com' && name === 'testHostname' && port === 25 && double === 1.0 && hasPort === true
    && map.get('testKey') == 'testValue' && list == '[testFirstValue, testSecondValue]'
    && defaultName === 'defaultHostname' && defaultPort === 587 && defaultDouble === 2.0 && defaultHasPort === false
    && defaultMap.get('defaultKey') == 'defaultValue' && defaultList == '[defaultFirstValue, defaultSecondValue]') {
  action = fr.Action.goTo("true").build();
} else {
  action = fr.Action.goTo("false").build();
}
```

```groovy
// Properties should get resolved (set in AM)
String email = systemEnv.getProperty('script.tree.decision.node.email');
String name = systemEnv.getProperty('script.tree.decision.node.hostname', 'defaultHostname');
Integer port = systemEnv.getProperty('script.tree.decision.node.port', '587', java.lang.Integer);
Double testDouble = systemEnv.getProperty('script.tree.decision.node.double', '2.0', java.lang.Double);
Boolean hasPort = systemEnv.getProperty('script.tree.decision.node.hasPort', 'false', java.lang.Boolean);
Map map = systemEnv.getProperty('script.tree.decision.node.map', '{\"defaultKey\":\"defaultValue\"}', java.util.Map);
List list = systemEnv.getProperty('script.tree.decision.node.list', 'defaultValue', java.util.List);

// Properties should get resolved to their defaults (not set in AM)
String defaultName = systemEnv.getProperty('script.tree.decision.node.hostname.unresolved', 'defaultHostname');
Integer defaultPort = systemEnv.getProperty('script.tree.decision.node.port.unresolved', '587', java.lang.Integer);
Double defaultDouble = systemEnv.getProperty('script.tree.decision.node.double.unresolved', '2.0', java.lang.Double);
Boolean defaultHasPort = systemEnv.getProperty('script.tree.decision.node.hasPort.unresolved', 'false', java.lang.Boolean);
Map defaultMap = systemEnv.getProperty('script.tree.decision.node.map.unresolved', '{\"defaultKey\":\"defaultValue\"}', java.util.Map);
List defaultList = systemEnv.getProperty('script.tree.decision.node.list.unresolved', 'defaultFirstValue,defaultSecondValue', java.util.List);

// Assert all property values - set the appropriate outcome
if (email.equals('test@example.com') && name.equals('testHostname') && port == 25 && testDouble == 1.0d && hasPort == true
    && defaultName.equals('defaultHostname') && defaultPort == 587 && defaultDouble == 2.0d && defaultHasPort == false
    && map.get('testKey').equals('testValue')
    && list.get(0).equals('testFirstValue') && list.get(1).equals('testSecondValue')
    && defaultMap.get('defaultKey').equals('defaultValue')
    && defaultList.get(0).equals('defaultFirstValue') && defaultList.get(1).equals('defaultSecondValue')) {

    outcome = 'true';
} else {
    outcome = 'false';
}
```

## Access utility functions

Use the next-generation `utils` binding to perform functions such as encoding/decoding and encryption/decryption, type conversion, and cryptographic operations.

|   |                                                        |
| - | ------------------------------------------------------ |
|   | The `utils` binding isn't available in legacy scripts. |

> **Collapse: Base64 encode and decode**
>
> * String base64.encode(String toEncode)
>
>   Encodes the specified text using base64.
>
> * String base64.encode(byte\[] toEncode)
>
>   Encodes the specified bytes using base64.
>
> * String base64.decode(String toDecode)
>
>   Decodes the specified text using base64.
>
> * byte\[] base64.decodeToBytes(String toDecode)
>
>   Decodes the specified text using base64 and returns the result as an array of bytes.
>
> * Example
>
> ```javascript
> var txt = "exampletext";
> var bytes = utils.types.stringToBytes(txt);
>
> var encoded = utils.base64.encode(txt);
> logger.debug("Encoded text: " + encoded); //ZXhhbXBsZXRleHQ=
>
> var decoded = utils.base64.decode(encoded);
> logger.debug("Decoded text: " + decoded);
>
> var encodedBytes = utils.base64.encode(bytes);
> logger.debug("Encoded bytes: " + encodedBytes);
>
> var decodedBytes = utils.base64.decode(encodedBytes);
> logger.debug("Decoded bytes: " + decodedBytes);
> ```

> **Collapse: Base64Url encode and decode**
>
> * String base64url.encode(String toEncode)
>
>   Encodes the specified text using base64url.
>
> * String base64url.encode(byte\[] toEncode)
>
>   Encodes the specified bytes using base64url.
>
> * String base64url.decode(String toDecode)
>
>   Decodes the specified text using base64url.
>
> * byte\[] base64url.decodeToBytes(String toDecode)
>
>   Decodes the specified text using base64url and returns the result as an array of bytes.
>
> * Example
>
> ```javascript
> var url = "http://exampletext=";
> var bytesUrl = utils.types.stringToBytes(url);
>
> var encodedURL = utils.base64url.encode(url);
> logger.debug("Encoded URL: " + encodedURL); //aHR0cDovL2V4YW1wbGV0ZXh0PQ
>
> var decodedURL = utils.base64url.decode(encodedURL);
> logger.debug("Decoded URL: " + decodedURL);
>
> var encodedBytesUrl = utils.base64url.encode(bytesUrl);
> logger.debug("Encoded bytes: " + encodedBytesUrl);
>
> var decodedBytesUrl = utils.base64url.decode(encodedBytesUrl);
> logger.debug("Decoded bytes: " + decodedBytesUrl);
> ```

> **Collapse: Generate random values**
>
> * String crypto.randomUUID()
>
>   Returns a type 4 pseudo-random generated UUID.
>
> * \<JavaScript array> crypto.getRandomValues(\<JavaScript array> array)
>
>   Returns the specified array filled with the same number of generated random numbers.
>
> * Example
>
> ```javascript
> // generate a pseudorandom UUID (version 4)
> var uuid = utils.crypto.randomUUID();
> logger.debug("UUID: " + uuid); //eef5b4e1-ae86-4c0a-9160-5afee2b5e791
>
> // generate an array of 5 random values
> var array = [0,0,0,0,0];
> utils.crypto.getRandomValues(array);
> array.forEach(function(element){
>   logger.debug("Random value: " + element);
> });
> ```

> **Collapse: Convert types**
>
> * String types.bytesToString(byte\[] toConvert)
>
>   Converts a byte array to a string.
>
> * byte\[] types.stringToBytes(String toConvert)
>
>   Converts a string to a byte array.
>
> * Example
>
> ```javascript
> var dataBytes = utils.types.stringToBytes("data");
> var dataString = utils.types.bytesToString(dataBytes);
> ```

> **Collapse: Generate keys**
>
> * Object crypto.subtle.generateKey(String algorithm)
>
>   Generates a key using the specified algorithm and default values.
>
> * Object crypto.subtle.generateKey(Map\<String, Object> algorithm)
>
>   Generates a key using the parameters provided, depending on the algorithm specified.
>
> * Parameters
>
> | Option          | Algorithm | Description                                                                           |
> | --------------- | --------- | ------------------------------------------------------------------------------------- |
> | `name`          | All       | *Required*. The name of the algorithm. Possible values: `AES`, `RSA`, `HMAC`, `ECDSA` |
> | `length`        | `AES`     | *Optional*. Default: `256`.                                                           |
> | `modulusLength` | `RSA`     | *Optional*. Default: `2048`.                                                          |
> | `namedCurve`    | `ECDSA`   | *Optional*. Possible values: `P-256` (default), `P-384`, `P-521`.                     |
> | `hash`          | `HMAC`    | *Optional*. Possible values: `SHA-1`, `SHA-256` (default), `SHA-384`, `SHA-512`.      |
>
> * Example
>
> ```javascript
> var aesKey = utils.crypto.subtle.generateKey("AES");
>
> // Optionally specify 'length' (default 256)
> var aesKeyCustom = utils.crypto.subtle.generateKey(
>   {
>     "name": "AES", length: 256
>   }
> );
>
> var rsaKey = utils.crypto.subtle.generateKey("RSA");
>
> // Optionally specify 'modulusLength' (default 2048)
> var rsaKeyCustom = utils.crypto.subtle.generateKey(
>   {
>     "name": "RSA", modulusLength: 4096
>   }
> );
>
> var hmacKey = utils.crypto.subtle.generateKey("HMAC");
>
> // Optionally specify 'hash' (default 'SHA-256')
> var hmacKeyCustom = utils.crypto.subtle.generateKey(
>   {
>     "name": "HMAC", "hash": "SHA-384"
>   }
> );
>
> var ecdsaKey = utils.crypto.subtle.generateKey("ECDSA");
>
> // Optionally specify 'namedCurve' (default P-256)
> var ecdsaKeyCustom = utils.crypto.subtle.generateKey(
>   {
>     "name": "ECDSA", namedCurve: "P-384"
>   }
> );
>
> logger.debug("AES key: " + aesKey.length);
> logger.debug("HMAC key: " + hmacKey.length);
> logger.debug("ECDSA key: " + ecdsaKey.publicKey.length + " : " + ecdsaKey.privateKey.length);
> logger.debug("RSA keys: " + rsaKey.publicKey.length + " : " + rsaKey.privateKey.length);
> ```

> **Collapse: Derive keys**
>
> * byte\[] crypto.subtle.deriveKey(String algorithm, byte\[] baseKey, Number derivedKeyLength)
>
>   Derives a key to the specified length, using the algorithm details and the base key provided.
>
>   This method supports the [PBKDF2](https://www.rfc-editor.org/rfc/rfc2898.html#appendix-A.2) key derivation function, which enhances key security by repeatedly applying a cryptographic function to a base key and salt. The more iterations, the more secure the key becomes.
>
> * Example
>
> ```javascript
> // get salt as byte[] - for example, from nodeState or API
> var salt = utils.types.stringToBytes("random-salt");
>
> // get key as byte[] - for example, from nodeState or secret store
> var baseKey = secrets.getGenericSecret("scripted.node.example.secret").getAsBytes();
>
> // length in octets, for example 128, 256, 512
> var derivedKeyLength = 256;
>
> // derivation algorithm must be PBKDF2
> // hash can be SHA-1, SHA-256, SHA-384, SHA-512
> var algorithmParams = {
> "name": "PBKDF2",
> "hash": "SHA-256",
> "salt": salt,
> "iterations": 10
> }
>
> var key = utils.crypto.subtle.deriveKey(algorithmParams, baseKey, derivedKeyLength);
>
> // verify that length is 32 (256 bits)
> logger.debug("Derived key length: " + key.length);
> ```

> **Collapse: Encrypt and decrypt**
>
> * byte\[] crypto.subtle.encrypt(String algorithm, byte\[] key, byte\[] data)
>
>   Encrypts the data using the specified key and algorithm (`AES` or `RSA`).
>
> * byte\[] crypto.subtle.decrypt(String algorithm, byte\[] key, byte\[] data)
>
>   Decrypts the data using the specified key and algorithm (`AES` or `RSA`).
>
> * Example
>
> ```javascript
> var data = utils.types.stringToBytes("data");
>
> var aesKey = utils.crypto.subtle.generateKey("AES");
> var rsaKey = utils.crypto.subtle.generateKey("RSA");
>
> var encryptedAes = utils.crypto.subtle.encrypt("AES", aesKey, data);
> var decryptedAes = utils.crypto.subtle.decrypt("AES", aesKey, encryptedAes);
>
> var encryptedRsa = utils.crypto.subtle.encrypt("RSA", rsaKey.publicKey, data);
> var decryptedRsa = utils.crypto.subtle.decrypt("RSA", rsaKey.privateKey, encryptedRsa);
>
> logger.debug("decryptedAes: " + decryptedAes + " decryptedRsa: " + decryptedRsa);
> ```

> **Collapse: Compute digest (hash) values**
>
> * String crypto.subtle.digest(String algorithm, byte\[] data)
>
>   Returns the digest of the data using the specified algorithm. The algorithm must be one of `SHA-1`, `SHA-256`, `SHA-384`, `SHA-512`.
>
> * Example
>
> ```javascript
> var data = utils.types.stringToBytes("data");
> var digest = utils.crypto.subtle.digest("SHA-256", data);
>
> logger.debug("Digest length: " + digest.length);
> ```

> **Collapse: Sign and verify**
>
> * byte\[] sign(String algorithm, byte\[] key, byte\[] data)
>
>   Signs the data using the specified algorithm and key.
>
> * byte\[] sign(Map\<String, Object> algorithmOptions, byte\[] key, byte\[] data)
>
>   Signs the data using the specified algorithm options and key.
>
> * boolean verify(String algorithm, byte\[] key, byte\[] data, byte\[] signature)
>
>   Verifies the signature of the data using the specified algorithm and key.
>
> * boolean verify(Map\<String, Object> algorithmOptions, byte\[] key, byte\[] data, byte\[] signature)
>
>   Verifies the signature of the data using the specified key and map of parameters.
>
> * Parameters
>
> | Option | Algorithm       | Description                                                                                          |
> | ------ | --------------- | ---------------------------------------------------------------------------------------------------- |
> | `name` | All             | *Required*. The name of the algorithm. Possible values: `RSA`, `HMAC`, `ECDSA`.                      |
> | `hash` | `HMAC`, `ECDSA` | *Optional*. Possible values: `SHA-1` (**HMAC only**), `SHA-256` (default), `SHA-384`, `SHA-512` (1). |
>
> (1) The `namedCurve` length must match the `hash` length for EDCSA keys. For example, `P-256` and `SHA-256`, or `P-521` and `SHA-512`.
>
> * Example
>
> ```javascript
> var data = utils.types.stringToBytes("data");
> var rsaKey = utils.crypto.subtle.generateKey("RSA");
> var hmacKey = utils.crypto.subtle.generateKey("HMAC");
> var ecdsaKey = utils.crypto.subtle.generateKey("ECDSA");
>
> var signRsa = utils.crypto.subtle.sign("RSA", rsaKey.privateKey, data);
> var verifyRsa = utils.crypto.subtle.verify("RSA", rsaKey.publicKey, data, signRsa);
>
>
> var hmacOpts = {
>   "name": "HMAC",
>   "hash": "SHA-512"
> }
> var signHmac = utils.crypto.subtle.sign(hmacOpts, hmacKey, data);
> var verifyHmac = utils.crypto.subtle.verify(hmacOpts, hmacKey, data, signHmac);
>
> var ecdsaOpts = {
>   "name": "ECDSA",
>   "hash": "SHA-256"
> }
>
> var signEcdsa = utils.crypto.subtle.sign(ecdsaOpts, ecdsaKey.privateKey, data);
> var verifyEcdsa = utils.crypto.subtle.verify(ecdsaOpts, ecdsaKey.publicKey, data, signEcdsa);
>
> logger.debug("RSA key verified: " + verifyRsa);
> logger.debug("HMAC key verified: " + verifyHmac);
> logger.debug("ECDSA key verified: " + verifyEcdsa);
> ```

## Evaluate policies

The next-generation `policy` binding lets you access the policy engine API and evaluate policies from within scripts.

### Methods

* List\<Map\<String, Object>> policy.evaluate(subject, application, resources, environment)

  Use the `evaluate()` method to request policy decisions for specific resources.

* Parameters

  The following parameters are required:

  | Parameter     | Type                        | Description                                                                                   |
  | ------------- | --------------------------- | --------------------------------------------------------------------------------------------- |
  | `subject`     | Map\<String, Object>        | The subject making the request, specified as an `ssoToken`, a `jwt`, or a `claims` value.     |
  | `application` | String                      | The name of the policy set.                                                                   |
  | `resources`   | List\<String>               | The resources to request decisions for.                                                       |
  | `environment` | Map\<String, List\<String>> | Specify environment conditions as a map of keys to lists of values, or `{}` to indicate none. |

* Returns

  The method returns evaluation decisions as a list of maps containing the following fields:

  | Field        | Description                                                                                                                                                                                                              |
  | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | `resource`   | The requested resource.                                                                                                                                                                                                  |
  | `actions`    | A map of actions and corresponding boolean values. For example:```json
  "actions":{
      "POST":false,
      "PATCH":false,
      "GET":false,
      "DELETE":false,
      "OPTIONS":true,
      "HEAD":false,
      "PUT":false
  }
  ``` |
  | `attributes` | A map of attribute names to their values if attributes exist for the policy.                                                                                                                                             |
  | `advices`    | A map of advice names to their values if advice exists for the policy.                                                                                                                                                   |

Learn how the `evaluate` method works and its parameters in [Request policy decisions for a specific resource](../am-authorization/rest-api-authz-policy-decisions.html#rest-api-authz-policy-decision-concrete). The `policy` binding works in a similar way to this REST API call.

### Example

The following example script requests a policy decision for a URL resource.

```javascript
var subject = {
    ssoToken: requestCookies[cookieName]
}

var application = "testPolicySet";

var resources = ["http://example.com:80/test"];

var environment = {
    "myField": ["myValue"]
}

var evaluationResult;
try {
    // policy.evaluate() returns List<Map<String, Object>>
    var results = policy.evaluate(subject, application, resources, environment);
    evaluationResult = results[0];
} catch(e) {
    logger.error(`Policy Evaluation Failed: ${e.message}`);
}

if (evaluationResult && evaluationResult.actions['GET'] === true) {
    action.goTo("authorized")
} else {
    action.goTo("unauthorized")
}
```

---

---
title: Create a script
description: Create scripts in PingAM realms using HTTP POST requests, encoding script content in Base64 format
component: pingam
version: 8.1
page_id: pingam:am-scripting:rest-api-scripts-create
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/rest-api-scripts-create.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripts", "JSON"]
page_aliases: ["scripting-guide:rest-api-scripts-create.adoc"]
section_ids:
  rest-api-scripts-create-global: Create a global library script
---

# Create a script

To create a script in a realm, send an HTTP POST request to the `/json{/realm}/scripts` endpoint, with an `_action` parameter set to `create`. Include a JSON representation of the script in the POST data.

The value for `script` must be in UTF-8 format and then encoded into Base64.

|   |                                                                                         |
| - | --------------------------------------------------------------------------------------- |
|   | If the realm is not specified in the URL, AM creates the script in the top level realm. |

The `iPlanetDirectoryPro` header is required and should contain the SSO token of an administrative user, such as `amAdmin`, who has access to perform the operation.

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Cookie:amlbcookie-01; iPlanetDirectoryPro: AQIC5wM…​TU3OQ*" \
--header "Accept-API-Version: resource=1.1" \
--data '{
  "name": "MyJavaScript",
  "script": "dmFyIGEgPSAxMjM7CnZhciBiID0gNDU2Ow==",
  "language": "JAVASCRIPT",
  "context": "POLICY_CONDITION",
  "description": "An example script"
}' \
https://am.example.com:8443/am/json/realms/root/realms/myrealm/scripts/?_action=create
{
  "_id": "0168d494-015a-420f-ae5a-6a2a5c1126af",
  "name": "MyJavaScript",
  "description": "An example script",
  "script": "dmFyIGEgPSAxMjM7CnZhciBiID0gNDU2Ow==",
  "language": "JAVASCRIPT",
  "context": "POLICY_CONDITION",
  "createdBy": "id=amadmin,ou=user,dc=am,dc=example,dc=com",
  "creationDate": 1436807766258,
  "lastModifiedBy": "id=amadmin,ou=user,dc=am,dc=example,dc=com",
  "lastModifiedDate": 1436807766258,
  "evaluatorVersion": "1.0"
}
```

## Create a global library script

To create a global library script that can be accessed from all realms, send an HTTP POST request to the `/json/scripts` endpoint, with an `_action` parameter set to `createGlobal`.

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Cookie: amlbcookie=01; iPlanetDirectoryPro: AQIC5wM…​TU3OQ*" \
--header "Accept-API-Version: resource=1.1" \
--data '{
  "name": "My global library",
  "script": "Ly2FnZSkgPT4gbGKTs=",
  "language": "JAVASCRIPT",
  "context": "LIBRARY",
  "description": "A global script"
}' \
https://am.example.com:8443/am/json/scripts/?_action=createGlobal
{
  "_id":"834e548d-5b38-4f7a-bb04-2ff54059b62a",
  "name":"My global library",
  "description": "A global script",
  "script":"Ly2FnZSkgPT4gbGKTs=",
  "default":false,
  "language":"JAVASCRIPT",
  "context":"LIBRARY",
  "createdBy": "id=amadmin,ou=user,dc=am,dc=example,dc=com",
  "creationDate":1767784565856,
  "lastModifiedBy": "id=amadmin,ou=user,dc=am,dc=example,dc=com",
  "lastModifiedDate":1767784565856,
  "evaluatorVersion":"2.0"
}
```

|   |                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To [list](rest-api-scripts-query.html) all the global library scripts you have created, include the `global` query filter field, for example:```bash
https://am.example.com:8443/am/json/scripts?_queryFilter=context%20eq%20%22LIBRARY%22%20and%20global%20eq%20true%20"
``` |

---

---
title: Delete a script
description: Delete an individual script from a realm using the REST API
component: pingam
version: 8.1
page_id: pingam:am-scripting:rest-api-scripts-delete
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/rest-api-scripts-delete.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripts", "JSON"]
page_aliases: ["scripting-guide:rest-api-scripts-delete.adoc"]
---

# Delete a script

To delete an individual script in a realm, perform an HTTP DELETE using the `/json{/realm}/scripts` endpoint, specifying the UUID in the URL.

|   |                                                                        |
| - | ---------------------------------------------------------------------- |
|   | If the realm is not specified in the URL, AM uses the top level realm. |

The `iPlanetDirectoryPro` header is required and should contain the SSO token of an administrative user, such as `amAdmin`, who has access to perform the operation.

```bash
$ curl \
--request DELETE \
--header "iPlanetDirectoryPro: AQIC5…​" \
--header "Accept-API-Version: resource=1.1" \
https://am.example.com:8443/am/json/realms/root/realms/myrealm/scripts/0168d494-015a-420f-ae5a-6a2a5c1126af
{}
```

---

---
title: Dynamic client registration scripting API
description: Access bindings available to dynamic client registration scripts in PingAM, including request properties, operation type, client identity, and software statement data
component: pingam
version: 8.1
page_id: pingam:am-scripting:dcr-api
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/dcr-api.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["scripting-guide:dcr-api.adoc"]
---

# Dynamic client registration scripting API

The following bindings are available to [dynamic client registration](../am-oidc1/dynamic-client-registration-script.html) scripts.

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The dynamic client registration script is a next-generation script and, therefore, has access to all the *next-generation* [common bindings](script-bindings.html) in addition to those described here. |

| Binding             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `requestProperties` | A map of the properties in the request. Always present.The keys in the map are as follows:- `requestUri`: The URI of the request.

- `realm`: The realm where the request was made.

- `requestParams`: The request parameters and posted data where each value is a list of one or more properties.

- `requestHeaders`: A map of the request headers. Header names are case-sensitive.

- `requestBody`: A map representing the body of the request.

  &#xA;&#xA;To mitigate the risk of reflection-type attacks, use OWASP best practices when handling these properties. Find an example in Unsafe use of Reflection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `operation`         | The dynamic client registration request operation as a String. Possible values: `CREATE`, `UPDATE`, and `DELETE`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `clientIdentity`    | The [ScriptedClient](../_attachments/apidocs/org/forgerock/openam/scripting/api/identity/ScriptedClient.html) that represents the created or updated client.Use methods such as `isAIAgent`, `setRedirectURIs`, and `setScope` to check or modify the client profile.> **Collapse: Example**
>
> ```javascript
> if (clientIdentity != null) {
>   clientIdentity.setRedirectURIs(["http://www.example.com/redirect"]);
>   clientIdentity.setGrantTypes(["client_credentials", "device_code"]);
>   clientIdentity.setClientType("Public");
>   clientIdentity.setAuthorizationCodeLifeTime(6000);
>   clientIdentity.setClientUri(["http://www.example.com/client"]);
>   clientIdentity.setDisplayName(["Test"]);
>   clientIdentity.setDefaultScopes(["scope_a", "scope_b"]);
>   clientIdentity.setClientDescription(["Test"]);
>   clientIdentity.setLogoUri(["http://www.example.com/logo"]);
>   clientIdentity.setPolicyUri(["http://www.example.com/policy"]);
>   clientIdentity.setTosUri(["http://www.example.com/tos"]);
>
>   if (clientIdentity.isAIAgent()) {
>     clientIdentity.setClientName(["Test AI Agent"]);
>   } else {
>     clientIdentity.setClientName(["Test OAuth2 Client"]);
>   }
>   clientIdentity.store();
> }
> ```When AM is integrated with PingIDM, you can use the following methods to access AI agent identity attributes:* `getAiAgentIdentityAttributes()`

  Returns the AI agent identity attributes for the client as a map. If the client isn't an AI agent, this method returns `null`.

* `updateAiAgentIdentityAttributes(attributes)`

  Patches the underlying PingIDM object with the supplied attributes map. The supplied attributes are merged with existing ones, so you don't need to retrieve the full attribute set first. To remove an existing key, supply `null` as its value. If the client isn't an AI agent, this method has no effect.> **Collapse: Example AI agent identity attribute methods**
>
> ```javascript
> if (operation === "CREATE" && clientIdentity.isAIAgent()) {
>   // Output the default AI agent attributes
>   logger.debug("AI attributes: " + clientIdentity.getAiAgentIdentityAttributes());
>   // Define new custom attribute values
>   var attribs = {
>     "description": "Example description",
>     "customAttributes": {
>         "foo": "bar"
>     }
>   };
>   // Update the AI agent identity with custom attribute values
>   try {
>     clientIdentity.updateAiAgentIdentityAttributes(attribs);
>   } catch (e) {
>       logger.error("Failed to update AI agent identity attributes", e);
>   }
> }
> ```	This binding is null if the operation is DELETE. |
| `softwareStatement` | A map representing the *decoded* JWT of the [software statement](../am-oidc1/oauth2-dynamic-client-registration.html#registration-software-statement) from the request, including the issuer and required claims.This is an empty map if no software statement is provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

---

---
title: IdP adapter scripting API
description: Reference for bindings available to custom IdP adapter scripts in PingAM, including authentication requests, SAML responses, and helper objects
component: pingam
version: 8.1
page_id: pingam:am-scripting:saml2-idp-adapter-api
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/saml2-idp-adapter-api.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["scripting-guide:saml2-idp-adapter-api.adoc"]
---

# IdP adapter scripting API

The following bindings are available to [IdP adapter](../am-saml2/custom-idp-adapter.html) scripts.

|   |                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | An IdP adapter script can be either a legacy or a next-generation script. It has access to all the [common bindings](script-bindings.html) for its scripting context. |

| Binding                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Legacy type                                                                                                                          | Next-generation type                                                                                                                                                                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `authnRequest`           | The original authentication request.Only available to SSO functions.> **Collapse: Example JSON (next-generation)**
>
> ```json
> {
>   "signature": null,
>   "subject": null,
>   "id": "s2c48de88f798137a410875437b1a4c0fa7bd9b239",
>   "consent": "",
>   "forceAuthn": false,
>   "protocolBinding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST",
>   "mutable": false,
>   "issueInstant": 1769521762000,
>   "issuer": {
>     "value": "serviceprovider1",
>     "format": "",
>     "nameQualifier": "",
>     "spnameQualifier": "",
>     "mutable": false,
>     "spprovidedID": ""
>   },
>   "@class": "com.sun.identity.saml2.protocol.impl.AuthnRequestImpl",
>   "assertionConsumerServiceURL": "https://sp.example.com/am/Consumer/metaAlias/alpha/sp1",
>   "extensions": null,
>   "destination": "https://idp.example.com/am/SSORedirect/metaAlias/alpha/idp1",
>   "passive": false,
>   "version": "2.0",
>   "requestedAuthnContext": {
>     "authnContextClassRef": [
>       "urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport"
>     ],
>     "@class": "com.sun.identity.saml2.protocol.impl.RequestedAuthnContextImpl",
>     "comparison": "exact",
>     "mutable": false,
>     "authnContextDeclRef": [],
>     "elementName": "RequestedAuthnContext"
>   },
>   "nameIDPolicy": {
>     "format": "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent",
>     "spnameQualifier": "serviceprovider1",
>     "@class": "com.sun.identity.saml2.protocol.impl.NameIDPolicyImpl",
>     "mutable": false,
>     "allowCreate": true
>   },
>   "attributeConsumingServiceIndex": null,
>   "conditions": null,
>   "scoping": null,
>   "signed": false,
>   "providerName": "",
>   "assertionConsumerServiceIndex": null
> }
> ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | An [AuthnRequest](../_attachments/apidocs/com/sun/identity/saml2/protocol/AuthnRequest.html) object.                                 | A JSON map.                                                                                                                                                                                                                                                            |
| `faultCode`              | The fault code returned in the SAML response.Only available to the `preSendFailureResponse` function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | String                                                                                                                               | String                                                                                                                                                                                                                                                                 |
| `faultDetail`            | Contains the details of the fault returned in the SAML response.Only available to the `preSendFailureResponse` function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | String                                                                                                                               | String                                                                                                                                                                                                                                                                 |
| `hostedEntityId`         | The entity ID for the hosted IDP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | String                                                                                                                               | String                                                                                                                                                                                                                                                                 |
| `idpAdapterScriptHelper` | A helper object that provides context information when customizing the IdP adapter extension points.Always present.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | An [idpAdapterScriptHelper](../_attachments/apidocs/com/sun/identity/saml2/plugins/scripted/IdpAdapterScriptHelper.html) object.     | An `IdpAdapterNextGenScriptHelper` object.> **Collapse: Methods**
>
> ```java
> public List getEntitlements(String applicationName, String realm)
>
> public List getEntitlements(String applicationName, String realm,
> Map<String, List<String>> environment)
> ``` |
| `relayState`             | Represents the `relayState` used in the redirect.Not available to the `preSingleSignOn` or `preSendFailureResponse` functions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | String                                                                                                                               | String                                                                                                                                                                                                                                                                 |
| `reqId`                  | The ID to use for continuation of processing if the adapter redirects.Not available to the `preSignResponse` or `preSendFailureResponse` functions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String                                                                                                                               | String                                                                                                                                                                                                                                                                 |
| `request`                | The HTTP request.Always present.> **Collapse: Example JSON (next-generation)**
>
> ```java
> {
>   "allowTrace": false,
>   "secure": true,
>   "requestedSessionIdValid": true,
>   "remoteAddr": "10.67.3.17",
>   "requestedSessionIdFromURL": false,
>   "parameterNames": {},
>   "protocol": "HTTP/1.1",
>   "localName": "am-5f87474849-f7b9m",
>   "asyncSupported": false,
>   "requestedSessionIdFromCookie": true,
>   "protocolRequestId": null,
>   "asyncStarted": false,
>   "localAddr": "10.67.3.6",
>   "contentLength": 873,
>   "servletConnection": {
>     "protocol": "http/1.1",
>     "connectionId": "a368",
>     "secure": false,
>     "protocolConnectionId": ""
>   },
>   "attributeNames": {},
>   "remotePort": 60476,
>   "queryString": "ReqID=s2c48de88f798137a410875437b1a4c0fa7bd9b239&index=null&acsURL=https://sp.example.com/am/Consumer/metaAlias/alpha/sp1&spEntityID=serviceprovider1&binding=urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST",
>   "requestId": "cbbc",
>   "characterEncoding": "UTF-8",
>   "authType": null,
>   "requestedSessionId": "3AECBCB5567836F65E08298982526907",
>   "remoteHost": "10.67.3.17",
>   "scheme": "https",
>   "trailerFieldsReady": true,
>   "serverName": "idp.example.com",
>   "remoteUser": null,
>   "requestURI": "/am/SSORedirect/metaAlias/alpha/idp1",
>   "method": "POST",
>   "pathTranslated": "/usr/local/tomcat/webapps/am/metaAlias/alpha/idp1",
>   "servletPath": "/SSORedirect",
>   "cookies": [
>     {
>       "path": null,
>       "name": "JSESSIONID",
>       "maxAge": -1,
>       "domain": null,
>       "value": "3AECBCB5567836F65E08298982526907",
>       "secure": false,
>       "attributes": {},
>       "comment": null,
>       "version": 0,
>       "httpOnly": false
>     },
>     {
>       "path": null,
>       "maxAge": -1,
>       "name": "amlbcookie",
>       "domain": null,
>       "secure": false,
>       "attributes": {},
>       "comment": null,
>       "value": "01",
>       "version": 0,
>       "httpOnly": false
>     },
>     {
>       "value": "6WcS7CVJ-a...lMxAAIwMQ.*",
>       "path": null,
>       "maxAge": -1,
>       "name": "58eaf95f29a4d6c",
>       "domain": null,
>       "secure": false,
>       "attributes": {},
>       "comment": null,
>       "version": 0,
>       "httpOnly": false
>     }
>   ],
>   "trailerFields": {},
>   "pathInfo": "/metaAlias/alpha/idp1",
>   "headerNames": {},
>   "requestURL": "https://idp.example.com/am/SSORedirect/metaAlias/alpha/idp1",
>   "userPrincipal": null,
>   "contentLengthLong": 873,
>   "httpServletMapping": {
>     "pattern": "/SSORedirect/*",
>     "mappingMatch": "PATH",
>     "servletName": "IDPSSOFederateServlet",
>     "matchValue": "metaAlias/alpha/idp1"
>   },
>   "locales": {},
>   "contextPath": "/am",
>   "localPort": 8080,
>   "serverPort": 443,
>   "contentType": "application/x-www-form-urlencoded",
>   "parameterMap": {
>     "acsURL": [
>       "https://sp.example.com/am/Consumer/metaAlias/alpha/sp1"
>     ],
>     "ReqID": [
>       "s2c48de88f798137a410875437b1a4c0fa7bd9b239"
>     ],
>     "spEntityID": [
>       "serviceprovider1"
>     ],
>     "binding": [
>       "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"
>     ],
>     "saml2Request": [
>       "eyJ0eXA ... YPA"
>     ],
>     "index": [
>       "null"
>     ]
>   },
>   "locale": "en_GB"
> }
> ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | An [HttpServletRequest](https://tomcat.apache.org/tomcat-10.0-doc/servletapi/jakarta/servlet/http/HttpServletRequest.html) object.   | A JSON map.                                                                                                                                                                                                                                                            |
| `requestHelper`          | Provides the following methods for accessing request details:- `public Object getAttribute(String name)`

- `public void setAttribute(String name, Object value)`

- `public String getHeader(String name)`

- `public List<String> getHeaders(String name)`

- `public String getParameter(String name)`

- `public String[] getParameterValues(String name)`Always present.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | *Not available*.                                                                                                                     | A `HttpServletRequestHelper` object.                                                                                                                                                                                                                                   |
| `res`                    | The SAML `Response` object.Only available to the `preSignResponse` function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | A [Response](../_attachments/apidocs/com/sun/identity/saml2/protocol/Response.html) object.                                          | *Not available*.Use [ssoResponse](#ssoresponse-idp-binding) instead.                                                                                                                                                                                                   |
| `response`               | The HTTP response.Always present.> **Collapse: Example JSON (next-generation)**
>
> ```java
> {
>   "trailerFields": null,
>   "status": 200,
>   "committed": false,
>   "headerNames": [
>     "X-Frame-Options",
>     "Content-Security-Policy-Report-Only",
>     "X-Content-Type-Options"
>   ],
>   "locale": "en_US",
>   "characterEncoding": "UTF-8",
>   "contentType": null,
>   "bufferSize": 8192
> }
> ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | An [HttpServletResponse](https://tomcat.apache.org/tomcat-10.0-doc/servletapi/jakarta/servlet/http/HttpServletResponse.html) object. | A JSON map.                                                                                                                                                                                                                                                            |
| `responseHelper`         | Provides the following methods for accessing request details:- `public void addHeader(String name, String value)`

- `public String getHeader(String name)`

- `public List<String> getHeaders(String name)`

- `public List<String> getHeaderNames()`

- `public void setHeader(String name, String value)`

- `public void sendRedirect(String location) throws IOException`Always present.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | *Not available*.                                                                                                                     | A `HttpServletResponseHelper` object.                                                                                                                                                                                                                                  |
| `session`                | Not available to the `preSingleSignOn` or `preSendFailureResponse` functions.Contains a representation of the user's SSO session object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | An [SSOToken](../_attachments/apidocs/com/iplanet/sso/SSOToken.html) object.                                                         | A `ScriptedSession` object.> **Collapse: Methods**
>
> ```java
> public String getProperty(String name)
>
> public void setProperty(String name, String value)
> ```                                                                                                   |
| []()`ssoResponse`        | An SSO response object.> **Collapse: Example JSON (next-generation)**
>
> ```json
> {
>   "assertion": [
>     {
>       "id": "s2b7a5c878dfac7b20ae926768e677b9a4aa393cc9",
>       "signature": null,
>       "advice": null,
>       "timeValid": true,
>       "issueInstant": 1769521769589,
>       "statements": [],
>       "authnStatements": [
>         {
>           "authnContext": {
>             "authenticatingAuthority": null,
>             "authnContextClassRef": "urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport",
>             "authnContextDeclRef": null,
>             "mutable": false,
>             "authnContextDecl": null
>           },
>           "subjectLocality": null,
>           "sessionNotOnOrAfter": null,
>           "sessionIndex": "s20a19e42789748e3dfd9763da0aa61abc13d89b01",
>           "mutable": true,
>           "authnInstant": 1769521769000
>         }
>       ],
>       "subject": {
>         "subjectConfirmation": [
>           {
>             "mutable": true,
>             "encryptedID": null,
>             "nameID": null,
>             "baseID": null,
>             "subjectConfirmationData": {
>               "elementName": "SubjectConfirmationData",
>               "address": null,
>               "notOnOrAfter": 1769522369604,
>               "inResponseTo": "s2c48de88f798137a410875437b1a4c0fa7bd9b239",
>               "mutable": true,
>               "recipient": "https://sp.example.com/am/Consumer/metaAlias/alpha/sp1",
>               "contentType": null,
>               "notBefore": null,
>               "content": []
>             },
>             "method": "urn:oasis:names:tc:SAML:2.0:cm:bearer"
>           }
>         ],
>         "mutable": true,
>         "encryptedID": null,
>         "nameID": {
>           "format": "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent",
>           "spnameQualifier": "serviceprovider1",
>           "value": "9EVQEze38h96WOxoJFGDTj9/9MZe",
>           "mutable": true,
>           "@class": "com.sun.identity.saml2.assertion.impl.NameIDImpl",
>           "spprovidedID": null,
>           "nameQualifier": "identityprovider1"
>         },
>         "baseID": null
>       },
>       "conditions": {
>         "audienceRestrictions": [
>           {
>             "mutable": true,
>             "audience": [
>               "serviceprovider1"
>             ]
>           }
>         ],
>         "proxyRestrictions": [],
>         "notOnOrAfter": 1769522369604,
>         "mutable": true,
>         "conditions": [],
>         "oneTimeUses": [],
>         "notBefore": 1769521169604
>       },
>       "authzDecisionStatements": [],
>       "issuer": {
>         "mutable": true,
>         "format": null,
>         "nameQualifier": null,
>         "value": "identityprovider1",
>         "spnameQualifier": null,
>         "spprovidedID": null
>       },
>       "attributeStatements": [],
>       "mutable": true,
>       "version": "2.0",
>       "signed": false
>     }
>   ],
>   "id": "s2d748a797f4c4f9f4e72b337f1c52168bd32cef63",
>   "signature": null,
>   "inResponseTo": "s2c48de88f798137a410875437b1a4c0fa7bd9b239",
>   "status": {
>     "@class": "com.sun.identity.saml2.protocol.impl.StatusImpl",
>     "mutable": true,
>     "statusDetail": null,
>     "statusCode": {
>       "mutable": true,
>       "@class": "com.sun.identity.saml2.protocol.impl.StatusCodeImpl",
>       "value": "urn:oasis:names:tc:SAML:2.0:status:Success",
>       "statusCode": null
>     },
>     "statusMessage": null
>   },
>   "destination": "https://sp.example.com/am/Consumer/metaAlias/alpha/sp1",
>   "consent": null,
>   "@class": "com.sun.identity.saml2.protocol.impl.ResponseImpl",
>   "extensions": null,
>   "issuer": {
>     "mutable": true,
>     "format": null,
>     "nameQualifier": null,
>     "value": "identityprovider1",
>     "spnameQualifier": null,
>     "spprovidedID": null
>   },
>   "issueInstant": 1769521769608,
>   "mutable": true,
>   "version": "2.0",
>   "encryptedAssertion": null,
>   "signed": false
> }
> ``` | *Not available*.                                                                                                                     | A JSON map.                                                                                                                                                                                                                                                            |

---

---
title: IdP attribute mapper scripting API
description: Configure custom attribute mapping for SAML 2.0 identity providers using scripting APIs with access to session, entity ID, and attribute mapping helper bindings
component: pingam
version: 8.1
page_id: pingam:am-scripting:saml2-idp-attribute-mapper-api
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/saml2-idp-attribute-mapper-api.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["scripting-guide:saml2-idp-attribute-mapper-api.adoc"]
---

# IdP attribute mapper scripting API

The following bindings are available to [IdP attribute mapper](../am-saml2/custom-idp-attribute-mapper.html) scripts.

|   |                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | An IdP attribute mapper script can be either a legacy or a next-generation script. It has access to all the [common bindings](script-bindings.html) for its scripting context. |

| Binding                          | Legacy                                                                                                                                                                                                                                                      | Next-generation                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `hostedEntityId`                 | The entity ID for the hosted IdP.                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                  |
| `idpAttributeMapperScriptHelper` | An [IdpAttributeMapperScriptHelper](../_attachments/apidocs/com/sun/identity/saml2/plugins/scripted/IdpAttributeMapperScriptHelper.html) instance containing methods used for IdP attribute mapping.                                                        | An instance of `IdpAttributeMapperScriptNextGenHelper`, which has the following method:`public List<Object> getStandardAttributes()`Returns a list of maps with the user attributes for the current session. For example:```json
[
  {
    "name:": "emailAddress",
    "nameFormat": null,
    "values": ["bjensen@example.com"]
  },
...
]
``` |
| `remoteEntityId`                 | The entity ID for the remote SP.                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                  |
| `session`                        | Contains a representation of the user's SSO session object. Refer to the [SSOToken](../_attachments/apidocs/com/iplanet/sso/SSOToken.html) interface for information about SSO token and authentication information, as well as session-related properties. |                                                                                                                                                                                                                                                                                                                                                  |

---

---
title: Library scripts
description: Create library scripts to define reusable JavaScript functionality and reference them from next-generation scripts using the require notation
component: pingam
version: 8.1
page_id: pingam:am-scripting:library-scripts
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/library-scripts.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripts"]
page_aliases: ["scripting-guide:library-scripts.adoc"]
section_ids:
  create-library-script: Create a library script
  import-library-script: Import a library script
---

# Library scripts

To use an existing script in a next-generation script, create a *library* script containing the functionality you want to reuse and reference it from your [next-generation](next-generation-scripts.html) script.

You can't use library scripts in a custom scripted node.

A library script can take the format of any JavaScript code. You can also import functionality from another library script.

For example:

* Create a library script using a minified third-party JavaScript utility library, such as [`lodash.js`](https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.21/lodash.min.js).

  |   |                                                                                                                                                                               |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Only import scripts from trusted third parties that you know take security seriously. It is your responsibility to ensure that third-party code is secure and to maintain it. |

* Write your own reusable snippet that enhances AM debugging functionality.

|   |                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Modules that use file systems, such as `node:fs` or `XMLHTTPRequest`, are not supported. Only modules that are self-contained and don't use a file system explicitly or indirectly are supported. |

## Create a library script

1. In the AM admin UI, [create a script](manage-scripts-console.html#create-scripts-with-console) of type `Library`.

   The Evaluator Version is automatically set to Next Generation.

   |   |                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To make a library script accessible from all realms, [create a global script over REST](rest-api-scripts-create.html#rest-api-scripts-create-global). |

2. In the Script field, paste the contents of a third-party JavaScript or write your own JavaScript code.

   Expose the reusable functions of your library script by defining properties on the `exports` object.

   For similar functionality, refer to the [CommonJS modules](https://nodejs.org/api/modules.html#modules-commonjs-modules).

   For this example, `myExampleLibrary` defines and exports three functions:

   ```javascript
   function add(i, j) {
     return i + j;
   }

   function logTotal(i) {
     logger.info("Total so far: " + i);
   }

   // export functions
   exports.add = add;
   exports.logTotal = logTotal;

   // export a constant
   exports.PI = 3.14;

   // direct export using an inline declaration
   exports.encodeURL = (url) => {
     return utils.base64url.encode(url);
   }
   ```

   |   |                                                                                        |
   | - | -------------------------------------------------------------------------------------- |
   |   | You can't create or export *classes* in library scripts, only functions and constants. |

   As a [next-generation](next-generation-scripts.html) script, a library script has access to all the next-generation [common bindings](script-bindings.html). You can also pass in parameters.

   |   |                                                                                                                                                                                                                                                                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Make sure you don't use the same name for a local variable as that of a common binding in your script. These names are reserved for common bindings only.If you have already defined a local variable with the same name as one that's added to common bindings in a more recent version of AM; for example, `utils`, you must rename the variable in your scripts before you upgrade. |

3. Save your changes.

## Import a library script

1. In the AM admin UI, [create or edit a next-generation script](manage-scripts-console.html#create-scripts-with-console).

2. In the Script field, load the library using the `require(LIBRARY_SCRIPT)` notation; for example:

   `var mylib = require('myExampleLibrary');`

3. Access the exported functions and constants using the library variable; in this case, `mylib`:

   ```javascript
   var i = mylib.add(10, mylib.PI);
   mylib.logTotal(i);

   var encoded = mylib.encodeURL("http://maths.example.com");
   ```

---

---
title: Manage scripts (REST)
description: Use the REST API to manage PingAM scripts, including creating, retrieving, modifying, and deleting realm-specific and global scripts in JSON format
component: pingam
version: 8.1
page_id: pingam:am-scripting:manage-scripts-rest
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/manage-scripts-rest.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripts", "Rest", "JSON"]
page_aliases: ["scripting-guide:manage-scripts-rest.adoc"]
---

# Manage scripts (REST)

AM provides the `scripts` endpoint to manage scripts using REST calls.

User-created scripts are realm-specific, so you must include the realm when you call the endpoint, for example, `/json{/realm}/scripts`. If you don't specify a realm in the URI, AM uses the Top Level Realm.

|   |                                                                        |
| - | ---------------------------------------------------------------------- |
|   | AM includes some global example scripts that you can use in any realm. |

Scripts are represented in JSON and are built from standard JSON objects and values (strings, numbers, objects, sets, arrays, `true`, `false`, and `null`). Each script has a system-generated *universally unique identifier* (UUID), which you must specify when modifying existing scripts. Renaming a script won't affect the UUID.

Example script:

```json
{
  "_id": "01e1a3c0-038b-4c16-956a-6c9d89328cff",
  "name": "Authentication Tree Decision Node Script",
  "description": "Default global script for a scripted decision node",
  "script": "LyoKICAtIERhdGE...",
  "default": true,
  "language": "JAVASCRIPT",
  "context": "AUTHENTICATION_TREE_DECISION_NODE",
  "createdBy": "id=dsameuser,ou=user,ou=am-config",
  "creationDate": 1433147666269,
  "lastModifiedBy": "id=dsameuser,ou=user,ou=am-config",
  "lastModifiedDate": 1433147666269,
  "evaluatorVersion": "1.0"
}
```

The values for the fields shown in the example are explained below:

* `_id`

  The UUID that AM generates for the script.

* `name`

  The name provided for the script.

* `description`

  An optional text string to help identify the script.

* `script`

  The source code of the script. The source code is in UTF-8 format and encoded into Base64.

  For example, a script such as the following:

  ```javascript
  var a = 123;
  var b = 456;
  ```

  When encoded into Base64 becomes:

  ```none
  dmFyIGEgPSAxMjM7IA0KdmFyIGIgPSA0NTY7
  ```

* `default`

  Whether the script is the default script for the context.

* `language`

  The language the script is written in: `JAVASCRIPT` or `GROOVY`. The script context determines the supported language(s).

* `context`

  The context type of the script.

* `context`

  The context type of the script.

  **Supported context values**

  | Legacy                                      | Next-generation                                        | Used by                                                                                                                             |
  | ------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
  | AUTHENTICATION\_CLIENT\_SIDE                | *Not available*                                        | Client-side authentication                                                                                                          |
  | AUTHENTICATION\_SERVER\_SIDE                | *Not available*                                        | Server-side authentication                                                                                                          |
  | AUTHENTICATION\_TREE\_DECISION\_NODE        | SCRIPTED\_DECISION\_NODE                               | [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/scripted-decision.html)                                    |
  |                                             | DEVICE\_MATCH\_NODE                                    | [Device Match node](https://docs.pingidentity.com/auth-node-ref/8.1/device-match.html)                                              |
  | *Not available*                             | CACHE\_LOADER                                          | [Cache manager](cache-manager.html)                                                                                                 |
  | CONFIG\_PROVIDER\_NODE                      | CONFIG\_PROVIDER\_NODE\_NEXT\_GEN                      | [Configuration Provider node](https://docs.pingidentity.com/auth-node-ref/8.1/config-provider.html)                                 |
  | *Not available*                             | LIBRARY                                                | [Library scripts](library-scripts.html)                                                                                             |
  | *Not available*                             | NODE\_DESIGNER                                         | [Custom scripted nodes](../am-authentication/node-designer.html)                                                                    |
  | OAUTH2\_ACCESS\_TOKEN\_MODIFICATION         | OAUTH2\_ACCESS\_TOKEN\_MODIFICATION\_NEXT\_GEN         | [Access token modification](../am-oauth2/modifying-access-tokens-scripts.html)                                                      |
  | OAUTH2\_AUTHORIZE\_ENDPOINT\_DATA\_PROVIDER | OAUTH2\_AUTHORIZE\_ENDPOINT\_DATA\_PROVIDER\_NEXT\_GEN | [Authorize endpoint data provider](../am-oauth2/plugins-auth-endpoint-data-provider.html)                                           |
  | *Not available*                             | OAUTH2\_DYNAMIC\_CLIENT\_REGISTRATION                  | [Customize dynamic client registration](../am-oidc1/dynamic-client-registration-script.html)                                        |
  | OAUTH2\_EVALUATE\_SCOPE                     | OAUTH2\_EVALUATE\_SCOPE\_NEXT\_GEN                     | [Scope evaluation](../am-oauth2/plugins-scope-evaluation.html)                                                                      |
  | OAUTH2\_MAY\_ACT                            | OAUTH2\_MAY\_ACT\_NEXT\_GEN                            | [Token exchange](../am-oauth2/token-exchange.html)                                                                                  |
  | OAUTH2\_SCRIPTED\_JWT\_ISSUER               | OAUTH2\_SCRIPTED\_JWT\_ISSUER\_NEXT\_GEN               | [Scripted trusted JWT issuer](../am-oauth2/oauth2-jwt-bearer-grant.html#configure-scripted-jwt-issuer)                              |
  | OAUTH2\_VALIDATE\_SCOPE                     | OAUTH2\_VALIDATE\_SCOPE\_NEXT\_GEN                     | [Scope validation](../am-oauth2/plugins-scope-validation.html)                                                                      |
  | OIDC\_CLAIMS                                | OIDC\_CLAIMS\_NEXT\_GEN                                | [OIDC claims](../am-oauth2/plugins-user-info-claims.html)                                                                           |
  | *Not available*                             | PINGONE\_VERIFY\_COMPLETION\_DECISION\_NODE            | [PingOne Completion Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/pingone/pingone-verify-completion-decision.html) |
  | POLICY\_CONDITION                           | POLICY\_CONDITION\_NEXT\_GEN                           | [Scripted policy conditions](../am-authorization/scripted-policy-condition.html)                                                    |
  | SAML2\_IDP\_ADAPTER                         | SAML2\_IDP\_ADAPTER\_NEXTGEN                           | [IdP adapter](../am-saml2/custom-idp-adapter.html)                                                                                  |
  | SAML2\_IDP\_ATTRIBUTE\_MAPPER               | SAML2\_IDP\_ATTRIBUTE\_MAPPER\_NEXT\_GEN               | [IdP attribute mapper](../am-saml2/custom-idp-attribute-mapper.html)                                                                |
  | *Not available*                             | SAML2\_NAMEID\_MAPPER                                  | [NameID mapper](../am-saml2/custom-nameid-mapper.html)                                                                              |
  | *Not available*                             | SAML2\_SP\_ACCOUNT\_MAPPER                             | [SP account mapper](../am-saml2/custom-sp-account-mapper.html)                                                                      |
  | SAML2\_SP\_ADAPTER                          | SAML2\_SP\_ADAPTER\_NEXTGEN                            | [SP adapter](../am-saml2/custom-sp-adapter.html)                                                                                    |
  | SOCIAL\_IDP\_PROFILE\_TRANSFORMATION        | SOCIAL\_IDP\_PROFILE\_TRANSFORMATION\_NEXT\_GEN        | [Social authentication](../am-authentication/social-registration.html)                                                              |
  |                                             | SOCIAL\_PROVIDER\_HANDLER\_NODE                        | [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/8.1/social-provider-handler.html)                        |
  |                                             | OIDC\_NODE                                             | [OIDC ID Token Validator node](https://docs.pingidentity.com/auth-node-ref/8.1/oidc-idtoken-validator.html)                         |

* `createdBy`

  A string containing the universal identifier DN of the subject that created the script.

* `creationDate`

  An integer containing the creation date and time, in ISO 8601 format.

* `lastModifiedBy`

  A string containing the universal identifier DN of the subject that most recently updated the resource type.

  If the script has not been modified since it was created, this property will have the same value as `createdBy`.

* `lastModifiedDate`

  A string containing the last modified date and time, in ISO 8601 format.

  If the script has not been modified since it was created, this property will have the same value as `creationDate`.

* `evaluatorVersion`

  A number representing the script engine version: `1.0` for legacy or `2.0` for next-generation. Refer to [Next-generation scripts](next-generation-scripts.html) for details.

  When invalid or unspecified, the value defaults to `1.0` for all script types except [library scripts](library-scripts.html), which are always `2.0` (next-generation).

---

---
title: Manage scripts (UI)
description: Create, modify, and delete scripts using the PingAM admin console
component: pingam
version: 8.1
page_id: pingam:am-scripting:manage-scripts-console
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/manage-scripts-console.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripts", "User Interface"]
page_aliases: ["scripting-guide:manage-scripts-console.adoc"]
section_ids:
  create-scripts-with-console: Create a script
  modify-scripts-with-console: Modify a script
  delete-scripts-with-console: Delete a script
---

# Manage scripts (UI)

The following procedures describe how to create, modify, and delete scripts using the AM admin UI.

## Create a script

1. In the AM admin UI, go to Realms > *realm name* > Scripts, and click + New Script.

2. Specify a name for the script.

3. Select the type of script from the Script Type drop-down list.

4. Select Legacy or for [supported scripts](next-generation-scripts.html#next-gen-availability), Next Generation, as the Evaluator Version.

   You can't change the evaluator version for other script types. Library scripts are set to Next Generation by default, whereas all other script types are set to Legacy.

   For information about the evaluator version used by the scripting engine and migrating to next-generation scripts, refer to [Next-generation scripts](next-generation-scripts.html).

5. Click Create.

   ![Complete the form and save your changes.](_images/script-editor.png)

6. Enter values on the *Script Name* page as follows:

   * Enter a description of the script.

   * Choose the script language, either JavaScript or Groovy. Note that not every script type supports both languages.

   * Enter the source code in the Script field.

     On supported browsers, you can click Upload, go to the script file, and click Open to upload the contents to the Script field.

   * Click Validate to check for compilation errors in the script.

     Correct any compilation errors, and revalidate the script until all errors have been fixed.

   * Save your changes.

## Modify a script

1. In the AM admin UI, go to Realms > *realm name* > Scripts.

2. Select the script you want to modify from the list of scripts.

3. Modify values on the *Script Name* page as needed.

   Note that if you change the Script Type, existing code in the script is replaced.

4. If you modified the code in the script, click Validate to check for compilation errors.

   Correct any compilation errors, and revalidate the script until all errors have been fixed.

5. Save your changes.

## Delete a script

1. In the AM admin UI, go to Realms > *realm name* > Scripts.

2. Choose one or more scripts to delete by activating the checkboxes in the relevant rows.

   |   |                                                                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can only delete user-created scripts—you can't delete the global sample scripts provided with AM.You can't delete a library script used by another library script. If you try to delete a nested script, the AM admin UI displays an error. |

3. Click Delete.

---

---
title: May act scripting API
description: Scripting API bindings for customizing May act token exchange behavior in PingAM
component: pingam
version: 8.1
page_id: pingam:am-scripting:may-act-api
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/may-act-api.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# May act scripting API

The following bindings are available to [May act](../am-oauth2/token-exchange.html#may_act_scripts) scripts for token exchange.

|   |                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This script can be either a legacy or a next-generation script. It has access to all the [common bindings](script-bindings.html) for its scripting context.Learn about converting existing scripts in [Migrate OAuth scripts to next-generation scripts](access-token-modification-migrate.html). |

| Binding             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Legacy                                                                                | Next-generation                                                                                                                                                                                                                                                                                                                                                |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `clientProperties`  | A map of properties configured in the client profile. Only present if the client was correctly identified.Find information about the keys in [Access client properties](access-token-modification-api.html#atmapi-client-properties).                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Map                                                                                   | Map                                                                                                                                                                                                                                                                                                                                                            |
| `identity`          | Represents an identity that AM can access.Find examples of how to use the binding in [Access profile data](access-token-modification-api.html#atmapi-profile).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | An [AMIdentity](../_attachments/apidocs/com/sun/identity/idm/AMIdentity.html) object. | A wrapper object for a scripted identity.                                                                                                                                                                                                                                                                                                                      |
| `requestProperties` | A read-only object (map) of the following request properties.- `requestUri`

  The URI as a string.

- `realm`

  The realm as a string.

- `requestParams`

  A map of request parameters and posted data, where each value is an array of parameters.

  To mitigate the risk of reflection-type attacks, use OWASP best practices when handling these parameters. Refer to Unsafe use of Reflection.

- `requestHeaders`

  The value of the named request header. Returns a map of `<String, List<String>>` as a native JavaScript object, for example:

  ```javascript
  var ipAddress = requestProperties.requestHeaders["X-Forwarded-For"][0]
  ```

  Header names are case-sensitive. | Map                                                                                   | Map                                                                                                                                                                                                                                                                                                                                                            |
| `scopes`            | The set of scopes in the client request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Set of Strings                                                                        | List of Strings                                                                                                                                                                                                                                                                                                                                                |
| `session`           | A representation of the user's SSO session object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | An [SSOToken](../_attachments/apidocs/com/iplanet/sso/SSOToken.html) object.          | A `ScriptedSession` object.> **Collapse: Methods**
>
> ```java
> public String getProperty(String name)
> public void setProperty(String name, String value)
> ```                                                                                                                                                                                             |
| `token`             | The token to be updated. The token is a mutable object, which means that changes directly update the underlying token state.Use the `token.setMayAct(JsonValue value)` method to add a `may_act` claim to a token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | An `ExchangeableToken` object                                                         | An `ExchangeableTokenScriptWrapper` object> **Collapse: Methods**
>
> ```javascript
> public void setMayAct(Map<String, Object> value) throws ServerException
> public Map<String, Object> getMayAct()
> public Map<String, Object> getAct()
> public void setAct(Map<String, Object> value) throws ServerException
> public Object getField(String key)
> ``` |

---

---
title: Migrate decision node scripts to next-generation scripts
description: Migrate decision node scripts from v1 to v2 scripting engine by updating bindings and script syntax
component: pingam
version: 8.1
page_id: pingam:am-scripting:scripting-api-node-migrate
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/scripting-api-node-migrate.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["scripting-guide:scripting-api-node-migrate.adoc"]
section_ids:
  v2-action: action
  v2-callbacksBuilder: callbacksBuilder
  v2-idRepository: idRepository
  v2-nodeState: nodeState
---

# Migrate decision node scripts to next-generation scripts

Different bindings are available to the decision node script depending on the scripting engine version; legacy or next-generation.

Complete the steps described in [Migrate to next-generation scripts](next-generation-scripts.html#migrate-to-v2-steps), using the examples listed in the following table as a guide when updating the bindings:

| Binding                                                                     | Next-generation change                                                                                                                                                                                                                                                  |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [action](#v2-action)                                                        | **New**.Use static method `goTo()` to set the script outcome.To send callbacks, instead of calling `Action.send()`, use the new [callbacksBuilder](#v2-callbacksBuilder) functionality.                                                                                 |
| [callbacksBuilder](#v2-callbacksBuilder)                                    | **New**.Instead of creating a `Callback` object and invoking `Action.send()`, add callbacks using static methods on the `callbacksBuilder` object; for example `nameCallback` and `passwordCallback`. These callbacks are automatically sent when the script completes. |
| [httpClient](next-generation-scripts.html#v2-httpClient)                    | Uses native JavaScript objects, similar to the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API).                                                                                                                                                 |
| [idRepository](#v2-idRepository)                                            | Use the `getIdentity()` method on the `idRepository` object to access attribute values.&#xA;&#xA;You must now explicitly call store() to persist changes to attribute values.                                                                                           |
| [jwtAssertion](scripting-api-node.html#jwt-support)                         | **New**.Generate JWT assertions in scripts.                                                                                                                                                                                                                             |
| [jwtValidator](scripting-api-node.html#jwt-support)                         | **New**.Validate JWT assertions in scripts.                                                                                                                                                                                                                             |
| [nodeState](#v2-nodeState)                                                  | The `sharedState` and `transientState` bindings are no longer supported.                                                                                                                                                                                                |
| [openidm](next-generation-scripts.html#v2-openidm)                          | **New**.Use this binding to access the `openidm` [scripting functions](https://docs.pingidentity.com/pingidm/8.1/scripting-guide/scripting-func-ref.html) supported in IDM.                                                                                             |
| [requestCookies](scripting-api-node.html#scripting-api-node-requestCookies) | **New**.Access the request cookies directly using this binding.                                                                                                                                                                                                         |

## `action`

| Legacy                                                                                                                                                                                 | Next-generation                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| ```javascript
var fr = JavaImporter(
    org.forgerock.openam.auth.node.api.Action;

 // Journey continues along the "false" path
action = fr.Action.goTo("false").build();      1
``` | ```javascript
 // Journey continues along the "false" path
action.goTo("false");                       1
``` |

1 No need to import the `Action` class to access the `goTo` method. Instead, call the `goTo` method directly on the `action` binding.

## `callbacksBuilder`

Use the `callbacksBuilder` object instead of importing `Callback` classes.

Learn more about using callbacks in [Callbacks](scripting-api-node.html#scripting-api-node-callbacks).

| Legacy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Next-generation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ```javascript
var fr = JavaImporter(                       1
  org.forgerock.openam.auth.node.api.Action,
  javax.security.auth.callback.NameCallback,
  javax.security.auth.callback.PasswordCallback,
  java.lang.String
);

if (callbacks.isEmpty()) {
  // Request callbacks
  action = fr.Action.send(                   2
    new fr.NameCallback("User Name"),
    new fr.PasswordCallback("Password", false)).build();
} else {
  // Callbacks returned with credentials
  var username =
    fr.String(callbacks.get(0).getName());
  var password =
    fr.String(callbacks.get(1).getPassword());

  sharedState.put("username", username);
  if (password === null || !password) {
    action = fr.Action.goTo("false").build();
  } else {                                   3
    transientState.put("password", password);
    action = fr.Action.goTo("true").build(); 4
  }
}
``` | ```javascript
if (callbacks.isEmpty()) {                   1
  // Request callbacks
  callbacksBuilder.nameCallback(
    "User Name", "User Name");
  callbacksBuilder.passwordCallback(
    "Password", false);
} else {
  // Callbacks returned with credentials
  var username =
    callbacks.getNameCallbacks().get(0);
  var password =
    callbacks.getPasswordCallbacks().get(0);

  nodeState.putShared("username", username);

  if (password === null || !password) {
    action.goTo("false");                    2
  } else {
    nodeState.putTransient("password",       3
        password);
    action.goTo("true");                     4
  }
}
``` |

1 Use `callbacksBuilder` to *request* callbacks, and the `callbacks` object to retrieve returned values.\
2 No need to explicitly call `send()`. The script sends every callback added to the `callbacksBuilder` when it completes.\
3 Use `nodeState.putShared()` instead of `sharedState.put()` and `nodeState.putTransient()` instead of `transientState.put()`.\
4 No need to set the outcome, because `action.goTo()` was invoked.

## `idRepository`

Get an `identity` from the `idRepository` object to access attribute values.

Learn more in [Access profile data](scripting-api-node.html#scripting-api-node-id-repo).

| Legacy                                                                                                                                                                                                                       | Next-generation                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ```javascript
var username = "bjensen";

var mail = idRepository.getAttribute(
    username, "mail");                    1 2

idRepository.setAttribute(username, "mail",
    ["new@example.com"]);                    3
``` | ```javascript
var username = "bjensen";

var identity =
    idRepository.getIdentity(username);      1

var mail =
    identity.getAttributeValues("mail");     2

 // Does NOT automatically persist data
identity.setAttribute("mail",
    ["new@example.com"]);                    3

try {
  identity.store();                            4
} catch(e) {
    logger.error("Unable to persist attribute. " + e);
}
``` |

1 The `idRepository` object is no longer used to get attribute values. Instead, use the `getIdentity()` method of the new `org.forgerock.openam.scripting.api.identity.ScriptIdentityRepository` interface to get the identity object.\
2 Use the `identity` object, instead of `idRepository`, to get or set attribute values.\
3 Setting or adding attributes on the `identity` object does *not* persist data.\
4 You *must* explicitly persist changes by calling the `store` method.

## `nodeState`

| Legacy                                                                                                                                                                                                                                                                       | Next-generation                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| ```javascript
 // var username = sharedState.get("username");
                                             1
var username =
    nodeState.get("username").asString();    2
var attributes =                             3
    nodeState.get('objectAttributes').asMap();
``` | ```javascript
var username = nodeState.get("username");    2
var attributes =
    nodeState.getObject("objectAttributes"); 3
``` |

1 Deprecated `sharedState` and `transientState` bindings are no longer available. Use `nodeState.get()` instead. To store state values, use `nodeState.putShared()` or `nodeState.putTransient()` instead of `sharedState.put()` and `transientState.put()`.\
2 No need to call methods such as `asString()` or `asMap()`.\
3 New `getObject()` method to retrieve a map with values stored across different states. The map is immutable.

For more information about the `nodeState` binding, refer to [Access shared state data](scripting-api-node.html#scripting-api-node-nodeState).

---

---
title: Migrate OAuth scripts to next-generation scripts
description: Migrate OAuth scripts from version 1 to version 2 scripting engines by updating bindings like accessToken, identity, and session to use Lists instead of Sets and simplified Object types
component: pingam
version: 8.1
page_id: pingam:am-scripting:access-token-modification-migrate
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/access-token-modification-migrate.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  v2-accesstoken: accessToken
  v2-identity: identity
---

# Migrate OAuth scripts to next-generation scripts

Different bindings are available to an OAuth script depending on the scripting engine version, legacy or next-generation.

To migrate legacy scripts to next-generation scripts:

1. Complete the steps to migrate common bindings, such as `httpclient` and `logger`, as described in [Migrate to next-generation scripts](next-generation-scripts.html#migrate-to-v2-steps).

   Review common bindings only available to next-generation scripts, such as `openidm` and `policy`. Consider using them to simplify and improve your scripts.

2. Update the script bindings that have changed for your OAuth script type by referring to the API and information in the following table.

   | Binding                        | Used in API                                                                                                                                   | Next-generation change                                                                                                                                                                                                                                                                                                                                                          |
   | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | [accessToken](#v2-accesstoken) | * [Access token](access-token-modification-api.html)

   * [Scope evaluation](scope-evaluation-api.html)                                         | The `get/setScope` methods now accept/return a `List` instead of a `Set`.The `List` format makes it easier to retrieve values because you can access values directly without converting the return objects.The `addExtraData`, `addExtraJsonData`, and `setPermissions` methods now accept/return an `Object` that is converted to the relevant type, instead of a `JsonValue`. |
   | [identity](#v2-identity)       | - [Access token](access-token-modification-api.html)

   - [May act](scope-evaluation-api.html)

   - [Scope evaluation](scope-evaluation-api.html) | Attribute values are now returned as a `List` so that you can access values directly.&#xA;&#xA;You must now explicitly call store() to persist changes to attribute values.                                                                                                                                                                                                     |
   | `requestedClaims`              | * [OIDC claims](user-info-claims-api.html)                                                                                                    | Access the requested claims as a Map of List instead of Set objects.                                                                                                                                                                                                                                                                                                            |
   | `requestedTypedClaims`         | - [OIDC claims](user-info-claims-api.html)                                                                                                    | No longer available. Use `requestedClaims` instead.                                                                                                                                                                                                                                                                                                                             |
   | `scopes`                       | * [Access token](access-token-modification-api.html)

   * [OIDC claims](user-info-claims-api.html)                                              | Access the scopes as a `List` instead of a `Set`.                                                                                                                                                                                                                                                                                                                               |
   | `session`                      | - [Access token](access-token-modification-api.html)

   - [Authorization endpoint data provider](authorize-endpoint-data-provider-api.html)     | The legacy `session` binding is an instance of [SSOToken](../_attachments/apidocs/com/iplanet/sso/SSOToken.html). Methods include `getProperty`, `getTimeLeft`, `getMaxIdleTime`, and `getTokenID`.The next-generation `session` binding is an instance of `ScriptedSession`.                                                                                                   |
   | `token`                        | * [May act](may-act-api.html)                                                                                                                 | A `ExchangeableTokenScriptWrapper` object.                                                                                                                                                                                                                                                                                                                                      |

## `accessToken`

| Legacy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Next-generation                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ```javascript
import org.forgerock.json.JsonValue;

accessToken.addExtraData('myKey', { → 'value' }) 1
JsonValue myJsonValue = JsonValue.json('value')  2
accessToken.addExtraJsonData('myJsonKey', { → myJsonValue })
JsonValue myListJsonValue = JsonValue.json(JsonValue.array('listValue'))
accessToken.addExtraJsonData('myListJsonKey', { → myListJsonValue })
JsonValue myMapJsonValue = JsonValue.json(JsonValue.object(JsonValue.field('mapKey', 'mapValue')))
accessToken.addExtraJsonData('myMapJsonKey', { → myMapJsonValue })
accessToken.setPermissions(JsonValue.json('permissions'))

accessToken.setField('scope',
                      accessToken.getScope()
                      .collect().join(' '))      3
``` | ```javascript
accessToken.addExtraData('myKey', 'value')        1
accessToken.addExtraJsonData('myJsonKey','value') 2
accessToken.addExtraJsonData('myListJsonKey', ['listValue'])
accessToken.addExtraJsonData('myMapJsonKey', {'mapKey': 'mapValue'})
accessToken.setPermissions('permissions')

accessToken.setField('scope',
                      Array.from( accessToken.getScope())
                      .join(' '));                3
``` |

1 Add values directly to the `addExtraData` method.\
2 Methods that accept/return `JsonValues` now use `Object`. The JavaScript engine converts the objects automatically to the appropriate type.\
3 Methods that accept/return `Sets` now return `Lists`. You can access values more easily with the `[]` notation.

Learn more about the `accessToken` binding in [Modify the access token](access-token-modification-api.html#atmapi-modify-access-token).

## `identity`

Use the `identity` binding to get data about the subject of the authorization request.

| Legacy                                                                                                                                                                                                                                                                                                                                                                                                                                              | Next-generation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ```javascript
 // Returns all values as a set,
 // for example: [test@example.com,user@example.com]
identity.getAttribute("mail").toString();   1

 // Returns the first value
 // for example: test@example.com
identity.getAttribute("mail")
    .iterator().next();                     2

 // persists data
identity.setAttribute("mail",
    ["new@example.com"]);                   3

identity.addAttribute("mail", "user@example.com");
``` | ```javascript
 // Returns all values as an array,
 // for example: ["test@example.com", "user@example.com"]
identity.getAttributeValues("mail");        1

 // Returns the first value, for example: test@example.com
identity.getAttributeValues("mail")[0];     2

 // Does NOT automatically persist data
identity.setAttribute("mail",
    ["new@example.com"]);                   3

 // Does NOT automatically persist data
identity.addAttribute("mail", "user@example.com");

 // persists data (throws an exception if add/setAttribute failed)
try {
    identity.store();                       4
} catch(e) {
    logger.error("Unable to persist attribute. " + e);
}
``` |

1 The `identity` object is now a `ScriptedIdentityScriptWrapper`, which returns a `List` instead of a `Set`.\
2 No need to convert objects by calling `toArray()[1]` or `iterator().next()`. Instead, you can access values directly, for example, `identity.getAttributeValues("KEY")[0]`.\
3 Adding or setting attributes on the `identity` object does *not* persist data.\
4 You *must* explicitly persist changes by calling the `store` method.

Learn more about the `identity` binding in [Access profile data](access-token-modification-api.html#atmapi-profile).

---

---
title: Migrate policy condition scripts to next-generation scripts
description: Migrate policy condition scripts from the legacy scripting engine to the next-generation scripting engine by updating bindings and calling store() to persist identity attribute changes
component: pingam
version: 8.1
page_id: pingam:am-scripting:policy-condition-migrate
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/policy-condition-migrate.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["scripting-guide:policy-condition-migrate.adoc"]
section_ids:
  v2-environment: environment
  v2-identity: identity
---

# Migrate policy condition scripts to next-generation scripts

Different bindings are available to a policy condition script depending on the scripting engine version, legacy or next-generation.

To migrate legacy scripts to next-generation scripts:

1. Complete the steps to migrate common bindings as described in [Migrate to next-generation scripts](next-generation-scripts.html#migrate-to-v2-steps).

2. Next, migrate the bindings specific to policy condition scripts by referring to the information in the following table.

   | Binding                        | Next-generation change                                                                                                                                                                                                          |
   | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | [environment](#v2-environment) | The binding now returns a `Map<String, List<String>>` rather than a `Map<String, Set<String>>`.The List format makes it easier to retrieve values because you can access values directly without converting the return objects. |
   | [identity](#v2-identity)       | Attribute values are now returned as a List so that you can access values directly.&#xA;&#xA;You must now explicitly call store() to persist changes to attribute values.                                                       |

## `environment`

Use the `environment` binding to get data from the client making the authorization request.

Learn more in [Access environment data](policy-condition-scripting-api.html#policy-condition-script-environment).

| Legacy                                                                                                         | Next-generation                                                                                                |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| ```javascript
var ipSet = environment.get("IP");          1

var userIP = ipSet.iterator().next();       2
``` | ```javascript
var ipList = environment.get("IP");         1

var userIP = ipList[0];                     2
``` |

1 The `environment` binding now returns `Map<String, List<String>>` instead of `Map<String, Set<String>>`.\
2 No need to convert objects by calling `toArray()[1]` or `iterator().next()`. Instead you can access values directly, for example, `environment.get("KEY")[0]`.

## `identity`

Use the `identity` binding to get data about the subject of the authorization request.

The following actions are available to the `identity` binding:

* Get attribute values

* Set attribute values

* Add attribute values

| Legacy                                                                                                                                                                                                                                                                                                                                                                                                                                              | Next-generation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ```javascript
 // Returns all values as a set,
 // for example: [test@example.com,user@example.com]
identity.getAttribute("mail").toString();   1

 // Returns the first value
 // for example: test@example.com
identity.getAttribute("mail")
    .iterator().next();                     2

 // persists data
identity.setAttribute("mail",
    ["new@example.com"]);                   3

identity.addAttribute("mail", "user@example.com");
``` | ```javascript
 // Returns all values as an array,
 // for example: ["test@example.com", "user@example.com"]
identity.getAttributeValues("mail");        1

 // Returns the first value, for example: test@example.com
identity.getAttributeValues("mail")[0];     2

 // Does NOT automatically persist data
identity.setAttribute("mail",
    ["new@example.com"]);                   3

 // Does NOT automatically persist data
identity.addAttribute("mail", "user@example.com");

 // persists data (throws an exception if add/setAttribute failed)
try {
    identity.store();                       4
} catch(e) {
    logger.error("Unable to persist attribute. " + e);
}
``` |

1 The `identity` object is now a `ScriptedIdentityScriptWrapper`, which returns a List instead of a Set.\
2 No need to convert objects by calling `toArray()[1]` or `iterator().next()`. Instead, you can access values directly, for example, `identity.getAttributeValues("KEY")[0]`.\
3 Adding or setting attributes on the `identity` object does *not* persist data.\
4 You *must* explicitly persist changes by calling the `store` method.

Learn more about the `identity` binding in [Access profile data](policy-condition-scripting-api.html#policy-condition-script-profile).

---

---
title: NameID mapper scripting API
description: Access the NameID mapper scripting API and use available bindings to customize SAML2 NameID values in PingAM scripts
component: pingam
version: 8.1
page_id: pingam:am-scripting:saml2-nameid-mapper-api
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/saml2-nameid-mapper-api.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["scripting-guide:saml2-nameid-mapper-api.adoc"]
---

# NameID mapper scripting API

The following bindings are available to [NameID mapper](../am-saml2/custom-nameid-mapper.html) scripts.

|   |                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The NameID mapper script is a next-generation script and therefore has access to all the *next-generation* [common bindings](script-bindings.html) in addition to those described here. |

| Binding              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `hostedEntityId`     | The entity ID for the hosted IDP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `remoteEntityId`     | The ID of the hosted SAML 2.0 entity.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `nameIDFormat`       | The requested SAML 2.0 NameID format.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `session`            | An instance of `ScriptedSession` representing the user's SSO session object interface for information about SSO token and authentication information, as well as session-related properties.Only present when the session object passed by the SAML engine is an SSOToken.Retrieve session property values with the following `ScriptedSession` supported method:`public String getProperty(String name)`                                                                                        |
| `nameIDScriptHelper` | The `NameIDScriptHelper` binding provides the following supporting methods and constants for customizing the NameID value:- Constants

  * `NAMEID_FORMAT_TRANSIENT`

  * `NAMEID_FORMAT_PERSISTENT`

  * `NAMEID_FORMAT_UNSPECIFIED`

  * `NAMEID_FORMAT_EMAIL`

- Methods

  * `public String createNameIdentifier()`

  * `public String getNameIDValue() throws SAML2Exception`

  * `public boolean shouldPersistNameIDFormat()`

  * `public String getNameIDFromSession()`Always present. |
| `identity`           | An instance of `ScriptedIdentityScriptWrapper` representing a scriptable implementation of an AM identity. The `identity` binding is derived from the session, so it's only present if the `session` object is.The `identity` object will also be missing if AM throws an exception during its creation. If this happens, AM records an entry in the logs.                                                                                                                                       |

---

---
title: Next-generation scripts
description: Use the next-generation scripting engine to build stable, modular scripts with enhanced bindings and library script support in PingAM
component: pingam
version: 8.1
page_id: pingam:am-scripting:next-generation-scripts
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/next-generation-scripts.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["scripting-guide:next-generation-scripts.adoc"]
section_ids:
  next-gen-availability: Availability
  migrate-to-v2-steps: Migrate to next-generation scripts
  v2-httpClient: httpClient
  v2-logger: logger
  v2-openidm: openidm
  v2-secrets: secrets
  error-handling: Exception handling when using next-generation script bindings
  general-exception-handling: General exception handling
  promise-exception-handling: Exception handling within a Promise
---

# Next-generation scripts

The next-generation scripting engine offers the following benefits:

* Stability

  * A stable set of enhanced bindings, available to JavaScript decision node scripts, that reduces the need to allowlist Java classes to access common functionality.

* Ease of use

  * Simplify your scripts with fewer imports and more intuitive return types that require less code.

  * Debug more easily with clear log messages and a simple logging interface based on SLF4J.

  * Make requests to other APIs from within scripts more easily with a more intuitive HTTP client.

* Reduced complexity

  * Simplify and modularize your scripts with [library scripts](library-scripts.html) by reusing commonly used code snippets as CommonJS modules.

    Reference library scripts from a next-generation script.

  * Access identity management information seamlessly through the `openidm` binding.

## Availability

The following script types use the next-generation scripting engine:

* [Configuration Provider node scripts](https://docs.pingidentity.com/auth-node-ref/8.1/config-provider.html)

* [Dynamic client registration scripts](../am-oidc1/dynamic-client-registration-script.html)

* [Library scripts](library-scripts.html)

* [OAuth 2.0 customization scripts](oauth2-scripting-api.html)

* [Policy condition scripts](policy-condition-scripting-api.html)

* [SAML 2.0 scripts](saml2-scripting-api.html)

* [Scripted Decision node scripts](scripting-api-node.html)

These are the only script types that can use library scripts and next-generation bindings.

## Migrate to next-generation scripts

To use next-generation bindings and library scripts, you must migrate [eligible](#next-gen-availability) legacy scripts.

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The next-generation engine can't use legacy scripts or scripts written in Groovy.Where possible, you should migrate legacy scripts to take advantage of next-generation stability. |

You can't change the script engine version after you have created a script.

To migrate existing scripts, create a new script and convert your legacy code:

1. [Create a script](manage-scripts-console.html#create-scripts-with-console) and select Next Generation as the Evaluator Version.

2. Copy and paste the legacy version of your script into the JavaScript field.

3. Review any Java classes that you needed to allowlist to use in your legacy script.

   *You can't add Java classes to the next-generation allowlist*.

   Instead, check if any next-generation bindings provide similar functionality, or reimplement the class as a [library script](library-scripts.html). Library scripts let you add third-party code as reusable JavaScript modules that can be referenced from other scripts.

   If this isn't possible, you can [request](https://support.pingidentity.com/s/article/Raising-an-RFE) the functionality to be included as a supported script binding in a future release.

4. Migrate the bindings specific to the script type by referring to the relevant API documentation, for example, [policy condition scripts](policy-condition-migrate.html) or [Scripted Decision node scripts](scripting-api-node-migrate.html).

5. Migrate the [common bindings](script-bindings.html) by referring to the examples listed in the following table.

   | Binding                                    | Next-generation change                                                                                                                                              |
   | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | [httpClient](#v2-httpClient)               | Uses native JavaScript objects, similar to the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API).                                             |
   | [logger](#v2-logger)                       | Logger is now based on `org.slf4j.Logger`, instead of `com.sun.identity.shared.debug.Debug`.                                                                        |
   | [openidm](#v2-openidm)                     | Use this binding to access the `openidm` [scripting functions](https://docs.pingidentity.com/pingidm/8.1/scripting-guide/scripting-func-ref.html) supported in IDM. |
   | [secrets](#v2-secrets)                     | Reference secrets and credentials from scripts.                                                                                                                     |
   | [utils](script-bindings.html#common-utils) | Use this utility binding to base64 encode/decode strings and to generate random UUIDs and random values.                                                            |

### `httpClient`

Call HTTP services with the `httpClient.send` method. HTTP client requests are asynchronous, unless the `get()` method is invoked on the returned object.

You can find examples of sending asynchronous and synchronous requests, sending requests over mTLS and setting timeouts for the HTTP client service, and more, in [Access HTTP services](script-bindings.html#common-httpclient).

| Legacy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Next-generation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ```javascript
var fr = JavaImporter(
    org.forgerock.openam.auth.node.api.Action);

var requestURL =
    "https://example.com/authenticate";
var request = new
    org.forgerock.http.protocol.Request();

request.setUri(requestURL);                 2
request.setMethod("POST");
request.getHeaders().add("Content-Type",    3
    "application/json;");
request.getHeaders().add("Authorization",
    "Bearer abcd-1234");                    4
request.setEntity(JSON.stringify(
    {"username": "bjensen"}));

var response =
    httpClient.send(request).get();         5

var responseCode =
    response.getStatus().getCode();         6

if (responseCode === 200) {
    action = fr.Action.goTo("true").build();
} else {
    action = fr.Action.goTo("false").build();
}
``` | ```javascript
 // import an external library to get token
var authLib = require('authLib');           1
var bearerToken =
    authLib.generateBearer(nodeState);

var options = {                             2
  method: "POST",
  headers: {                                3
    "Content-Type": "application/json"
  },
  token: bearerToken,                       4
  body: {
    username: "bjensen"
  }
}

var requestURL =
    "https://example.com/authenticate";
var response = httpClient.send(
    requestURL, options).get();             5

if (response.status === 200) {              6
    action.goTo("true");
} else {
    action.goTo("false");
}
``` |

1 The example assumes you've created a custom library script (`authLib`) that handles authentication.\
2 Set the request options as a native JavaScript object, instead of setting parameters on a `Request` object.\
3 To send a form request, you don't need to set `Content-Type` to url-encode parameters. Use the `form` attribute instead. For details, refer to [Access HTTP services](script-bindings.html#common-httpclient).\
4 Use Library scripts to reuse common pieces of code; for example, to get an authentication token.\
5 Call `httpClient.send` with the request URL and options as separate arguments, instead of a `Request` object.\
6 Access response data directly using the methods and properties of the returned `response` object.

### `logger`

The `com.sun.identity.shared.debug.Debug` logger class is deprecated and replaced by `org.forgerock.openam.scripting.logging.ScriptedLoggerWrapper`.

`ScriptedLoggerWrapper` provides a subset of the methods offered by [SLF4J](https://www.slf4j.org).

Learn more in [Log script messages](script-bindings.html#common-logger).

| Legacy                                                                                                                                                                                                                                                                              | Next-generation                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ```javascript
var messageEnabled = logger.messageEnabled();
logger.message("Message with arg {}", arg);

var warnEnabled = logger.warningEnabled();
logger.warning("Warn with arg {}", arg);

var errorEnabled = logger.errorEnabled();
logger.error("Error with arg {}", arg);
``` | ```javascript
var traceEnabled = logger.isTraceEnabled();
logger.trace("Trace with arg {}", arg);

var debugEnabled = logger.isDebugEnabled();
logger.debug("Debug with arg {}", arg);

var infoEnabled = logger.isInfoEnabled();
logger.info("Info with arg {}", arg);

var warnEnabled = logger.isWarnEnabled();
logger.warn("Warn with arg {}", arg);

var errorEnabled = logger.isErrorEnabled();
logger.error("Error with arg {}", arg);
``` |

### `openidm`

The `openidm` binding lets you manage an IDM resource by calling scripting functions directly from a decision node script.

The following CRUDPAQ functions are supported:

* create

* read

* update

* delete

* patch

* action

* query

The following example shows the extensive code required in a legacy script to query the existence of a user by their email address in IDM, compared to the ease of using the `openidm` binding.

You can find more examples about using the `openidm` binding in your next-generation scripts in [Access IDM scripting functions](script-bindings.html#common-openidm).

You can find more details about other supported functions in [Scripting functions](https://docs.pingidentity.com/pingidm/8.1/scripting-guide/scripting-func-ref.html).

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `openidm` binding provides administrative access to IDM functions. Use it with caution to prevent the exposure of sensitive data. |

| Legacy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Next-generation                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| ```javascript
function lookupUser (email) {
  try {
    var idmUserEndpoint =
         + '/openidm/managed/user?
        _queryFilter=userName+eq+%22'
        + email + '%22';
    var request = new
        org.forgerock.http.protocol.Request();
    var accessToken =
        transientState.get("idmAccessToken");     1

    request.setMethod('GET');
    request.setUri(idmUserEndpoint);              1
    request.getHeaders().add('Authorization',
        'Bearer ' + accessToken);
    request.getHeaders().add('Content-Type',
        'application/json');
    request.getHeaders().add('Accept-API-Version',
        'resource=1.0');

    var httpResponse =
        httpClient.send(request).get();           1
    var responseCode =
        httpResponse.getStatus().getCode();
    if (responseCode === 200) {
      var response = JSON.parse(
          httpResponse.getEntity().getString());
      if (response && response.result &&
            response.result.length > 0) {
        // User found
        return {
          success: true,
          user: response.result[0]};
      } else {
        // User NOT found
        return { success: true, user: null };
      }
    } else {
      return {
        success: false,
        error: 'Error looking up user: ' + responseCode
      };
    }
  } catch (e) {
    return {
      success: false,
      error: 'Error querying user: ' + e.toString()
    };
  }
}
``` | ```javascript
openidm.query("managed/user", {        1
    "_queryFilter":`/userName eq '${email}'`
  },
  ["userName", "_id"]
);
``` |

1 Replace code that gets an `idmAccessToken` and uses the HTTP client object to invoke a request on an `/openidm/*` endpoint, with the direct use of the `openidm` binding.

### `secrets`

The `secrets` binding is available to all next-generation scripts.

Learn more about the `secrets` binding in [Access secrets and credentials](script-bindings.html#common-secrets).

| Legacy                                                                                                                                                                                                                                                                                                                                                                                            | Next-generation                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ```javascript
var fr = JavaImporter(
    org.forgerock.openam.auth.node.api.Action);

var pw = secrets.getGenericSecret(          1
           "scripted.node.mysecret").getAsUtf8();

var auth = java.util.Base64.getEncoder()    2
    .encodeToString(java.lang.String().getBytes("bjensen:" + pw));

nodeState.putTransient("authString", auth);
action = fr.Action.goTo("true").build();
``` | ```javascript
var pw = secrets.getGenericSecret(          1
           "scripted.node.mysecret").getAsUtf8();

var auth =                                  2
    utils.base64.encode("bjensen:" + pw);

nodeState.putTransient("authString", auth);
action.goTo("true");
``` |

1 Access the secret from the AM secret store in the same way as the legacy binding.\
2 To encode sensitive information, the `utils` binding replaces the need to allowlist the `java.util.Base64` and `java.util.Base64$Encoder` Java classes.

## Exception handling when using next-generation script bindings

You must handle exceptions differently depending on whether the exception occurs within a JavaScript `Promise` or not.

Both types of exception handling can require that the Java exception class is allowlisted or marked as supported for you to access particular details about the exception. Otherwise, the script can throw an error.

|   |                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Next-generation doesn't support a configurable allowlist. Learn more in [Access Java classes](scripting-env.html#scripting-env-java-classes). |

### General exception handling

When you call a method on a script binding that throws an exception, the scripting engine wraps the exception object in a JavaScript error. You can use this to access the error message in the following way:

```javascript
try {
  myBinding.myMethod();
} catch (e) {
    // works without requiring support or allowlisting of the exception class
    logger.error(e.message);
}
```

If the exception class is allowlisted or the class and method are annotated as `@Supported`, you can access the underlying Java exception as follows:

```javascript
try {
  myBinding.myMethod();
} catch (e) {
    // throws an exception if getMyObject() isn't supported or the exception class isn't allowlisted
    myObject = e.javaException.getMyObject();
}
```

### Exception handling within a `Promise`

When you handle an exception in a `thenCatch` block of a `Promise`, the exception object isn't wrapped, so it still references the Java exception instead of a JavaScript error.

You can only access the exception object if the exception class is allowlisted or if the fields and methods you want to use are annotated with the `@Supported` annotation.

For example:

```javascript
var val = myBinding.methodReturningPromise()
  .then(() => {
    // function to handle the result of the promise
  })
  .thenCatch((e) => {
    // throws a new exception unless the "message" field is supported
    message = e.message;
    // throws an exception unless "getMyObject()" is supported or the exception class is allowlisted
    myObject = e.getMyObject();
    return false;
  }).get();
```

|   |                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | As an example, the [HttpClientScriptException](../_attachments/apidocs/org/forgerock/openam/scripting/wrappers/HttpClientScriptException.html) has a supported `message` field for logging purposes. |

---

---
title: OAuth 2.0 / OIDC scripting API
description: Use scripts to customize OAuth 2.0 authorization server behavior and OIDC dynamic client registration
component: pingam
version: 8.1
page_id: pingam:am-scripting:oauth2-scripting-api
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/oauth2-scripting-api.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["scripting-guide:oauth2-scripting-api.adoc"]
---

# OAuth 2.0 / OIDC scripting API

You can use scripts to customize OAuth 2.0 authorization server behavior or OIDC dynamic client registration.

The OAuth 2.0 and OIDC scripts all have access to [common bindings](script-bindings.html), such as `httpClient`, `logger`, and `scriptName`. The bindings available depend on whether you use a [legacy or a next-generation](scripting-env.html) script.

Refer to the individual scripting APIs for specific bindings.

---

---
title: OIDC claims scripting API
description: Customize OIDC claims returned in user info responses using scripting bindings in PingAM
component: pingam
version: 8.1
page_id: pingam:am-scripting:user-info-claims-api
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-scripting/user-info-claims-api.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# OIDC claims scripting API

The following bindings are available to [OIDC claims](../am-oauth2/plugins-user-info-claims.html) scripts:

|   |                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This script can be either a legacy or a next-generation script. It has access to all the [common bindings](script-bindings.html) for its scripting context.Learn about converting existing scripts in [Migrate OAuth scripts to next-generation scripts](access-token-modification-migrate.html). |

| Binding                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Legacy                                                                                | Next-generation                                                                                                                                                    |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `claims`               | An object (map) of the default OIDC claims AM provides.The keys are the claim strings. The values are the claim value objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Map                                                                                   | Map                                                                                                                                                                |
| `claimLocales`         | An array of string values from the `claims_locales` parameter.Learn more in [Claims Languages and Scripts](https://openid.net/specs/openid-connect-core-1_0.html#ClaimsLanguagesAndScripts) in the *OpenID Connect Core 1.0* specification.                                                                                                                                                                                                                                                                                                                                                                    | Array of Strings                                                                      | Array of Strings                                                                                                                                                   |
| `claimObjects`         | The default OIDC claims AM provides.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | An array of claim objects.                                                            | *Not available*                                                                                                                                                    |
| `clientProperties`     | A map of properties configured in the client profile. Only present if the client was correctly identified.Find information about the keys in [Access client properties](access-token-modification-api.html#atmapi-client-properties).                                                                                                                                                                                                                                                                                                                                                                          | Map                                                                                   | Map                                                                                                                                                                |
| `identity`             | Represents an identity that AM can access.Find information about how to use the binding in [Access profile data](access-token-modification-api.html#atmapi-profile).                                                                                                                                                                                                                                                                                                                                                                                                                                           | An [AMIdentity](../_attachments/apidocs/com/sun/identity/idm/AMIdentity.html) object. | A wrapper object for a scripted identity.                                                                                                                          |
| `requestedClaims`      | An object (map) of requested claims. This is empty unless the request includes the `claims` query string parameter and AM is configured to support its use.Under Native Consoles > Access Management, go to Realms > *Realm Name* > Services > OAuth2 Provider > Advanced OpenID Connect. Enable Enable "claims\_parameter\_supported" and save your change.Find more information about the `claims` query string parameter in [Requesting Claims using the "claims" Request Parameter](https://openid.net/specs/openid-connect-core-1_0.html#ClaimsParameter) in the *OpenID Connect Core 1.0* specification. | Map of Set objects                                                                    | Map of List objects                                                                                                                                                |
| `requestedTypedClaims` | This is empty unless the request includes claims.A claim with a single value means the script should return only that value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | An array of the requested claims objects.                                             | *Not available*. Use `requestedClaims` instead.                                                                                                                    |
| `requestProperties`    | A read-only object (map) of the request properties.Learn more in [Access request properties](access-token-modification-api.html#atmapi-request-properties).                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Map                                                                                   | Map                                                                                                                                                                |
| `scopes`               | The set of scopes in the client request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Set of Strings                                                                        | List of Strings                                                                                                                                                    |
| `session`              | A representation of the user's SSO session object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | An [SSOToken](../_attachments/apidocs/com/iplanet/sso/SSOToken.html) object.          | A `ScriptedSession` object.> **Collapse: Methods**
>
> ```java
> public String getProperty(String name)
> public void setProperty(String name, String value)
> ``` |