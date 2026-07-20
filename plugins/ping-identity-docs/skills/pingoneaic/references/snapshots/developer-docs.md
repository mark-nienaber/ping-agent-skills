---
title: Action
description: Use the Action verb to perform predefined operations on Advanced Identity Cloud REST API resources via HTTP POST
component: pingoneaic
page_id: pingoneaic:developer-docs:crest/action
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/crest/action.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  parameters: Parameters
---

# Action

Actions are a means of extending Advanced Identity Cloud REST APIs and are defined by the resource provider. The actions you can use depend on the implementation.

The standard action indicated by `_action=create` is described in [Create](create.html).

## Parameters

You can use the following query string parameters. Other parameters depend on the specific action implementation:

| Parameter                  | Description                                                                                                                                                                                                                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_fields=field[,field...]` | Return only the specified fields in the body of the response.The `field` values are JSON pointers. For example, if the resource is `{"parent":{"child":"value"}}`, `parent/child` refers to the `"child":"value"`.If the `field` is left blank, the endpoint returns all default values. |
| `_prettyPrint=true`        | Format the body of the response.                                                                                                                                                                                                                                                         |

---

---
title: Advanced Identity Cloud API reference
description: Overview of Advanced Identity Cloud REST APIs covering access management, identity management, and scripting endpoints
component: pingoneaic
page_id: pingoneaic:developer-docs:api-reference
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/api-reference.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "Integration"]
section_ids:
  api_versions: API versions
  the_apis: The APIs
---

# Advanced Identity Cloud API reference

Many of the features available through Advanced Identity Cloud UIs are also available through REST APIs.

|   |                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some documented APIs aren't active in all Advanced Identity Cloud tenants.The REST APIs have *Evolving* interface stability. This interface is continuing to evolve and so is subject to change in backwards-incompatible ways. All changes are documented at the time of release. |

## API versions

To maintain compatibility between releases, many REST APIs are versioned (`v1.0`, `v2.0`, and so on). The version number of a feature increases when Advanced Identity Cloud introduces breaking changes to an API.

Advanced Identity Cloud provides versions for these API aspects:

* *resource*

  Any changes to the structure or syntax of a returned response result in a change to the *resource* version. For example, changing `errorMessage` to `message` in a JSON response.

* *protocol*

  Any changes to the methods used to make REST API calls result in change to the *protocol* version. For example, changing `_action` to `$action` in the required parameters of an API feature.

When an API is versioned, include resource versions in your REST calls by setting the `Accept-API-Version` request header. The following example requests *resource* version 2.0 and *protocol* version 1.0:

```
Accept-API-Version: resource=2.0, protocol=1.0
```

This header ensures you call the correct version of the API, avoiding unexpected behavior due to incompatible changes.

## The APIs

Learn more in the API reference pages:

* [Authenticate over REST](../am-authentication/authn-rest.html)

- [Identity Governance APIs](../_attachments/api/identity-governance-openapi.html) 1

- [Identity management](../_attachments/api/index-idm.html), [PingIDM REST API reference](../idm-rest-api/preface.html)

* [Manage scripts over REST](../am-scripting/manage-scripts-rest.html)

* [Manage sessions over REST](../am-sessions/managing-sessions-REST.html)

* [OAuth 2.0 administration endpoints](../am-oauth2/oauth2-admin-endpoints.html)

* [OAuth 2.0 APIs](../am-oauth2/oauth2-client-endpoints.html)

* [OIDC APIs](../am-oidc1/oidc-client-endpoints.html)

- [Tenant administration](../_attachments/api/index.html)

1 Identity Governance is an add-on capability to Advanced Identity Cloud. Contact your Ping Identity representative if you want to add PingOne® Identity Governance to your Advanced Identity Cloud subscription.

---

---
title: Advanced Identity Cloud Postman collection
description: Import and configure the Advanced Identity Cloud Postman collection to explore and test REST APIs for identity and access management
component: pingoneaic
page_id: pingoneaic:developer-docs:postman-collection
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/postman-collection.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "Third-Party", "Integration"]
page_aliases: ["pingoneaic::developers-postman-collection.adoc", "pingoneaic::developers-rest-apis.adoc"]
section_ids:
  download-postman-and-import-the-advanced-identity-cloud-collection: Download Postman and import the Advanced Identity Cloud collection
  service_account: Create a service account and download its private key
  configuring_the_collection: Configure collection variables
  required-values: Required variable values
  server_urls: Server URLs
  user_credentials: User credentials
  logging_api: Logging API
  optional-values: Optional variable values
  hard-codedvalues: Hard-coded variable values
  using_the_collection: Use the collection
  running_the_prerequisite_requests: Running the prerequisite requests
  running_the_requests: Running the requests
  intelligent_access: Intelligent access
  identity_profiles: Identity profiles
---

# Advanced Identity Cloud Postman collection

Advanced Identity Cloud provides REST APIs to help you manage identities, authenticate to the system, monitor Advanced Identity Cloud, and more.

You can also use the [AM and IDM APIs](authenticate-to-rest-api-with-access-token.html) with Advanced Identity Cloud.

To help you quickly use and understand these REST APIs, Advanced Identity Cloud provides a [Postman](https://www.postman.com/) collection, containing example requests grouped into features.

**Features include**:\
 \
・Intelligent Access\
・User Self-Service\
・Session Management\
・Identity Profiles\
・Managed Identities\
・Auditing/Monitoring\
・OAuth 2.0 Flows

![postman collection overview](_images/postman-collection-overview.png)

## Download Postman and import the Advanced Identity Cloud collection

1. Download and install the [Postman application](https://www.postman.com/downloads/).

2. Download the [Advanced Identity Cloud Postman collection](_attachments/Advanced_Identity_Cloud.postman_collection.20260311.json).

3. In Postman:

   1. Go to File > Import... > Upload Files.

   2. Browse to the collection JSON file you downloaded in the previous step, and then click Open.

   3. Click Import to bring the collection into your workspace.

## Create a service account and download its private key

To use the Advanced Identity Cloud Postman collection, you must create a service account that the requests in the collection can use to connect to your Advanced Identity Cloud instance.

Follow the steps in [Create a new service account](../tenants/service-accounts.html#create-a-new-service-account).

* In step 9, save the private key as a local file called `key.jwk`.

* Make a note of the ID for the service account you created.

  An example of an ID is `449d7e27-7889-47af-a736-83b6bbf97ec5`.

Proceed to the next section to learn how to enter these values into the collection, plus other settings necessary to use Postman with Advanced Identity Cloud.

## Configure collection variables

The Advanced Identity Cloud Postman collection uses a number of configurable variables to populate the requests.

These variables are stored at the collection level. To view them, click on the top level of the collection menu labeled PingOne Advanced Identity Cloud Collection, and then select the Variables tab.

![Editing the default variables used by the Postman collection](_images/postman-collection-variables.png)Figure 1. Editing the default variables used by the Postman collection

The variables are initially set with placeholder values that you must modify or replace. For example, the collection needs to know the Advanced Identity Cloud URL, as well as your admin access credentials.

To edit the variables, enter new values in the INITIAL VALUE column. Then click Save to make the edits permanent.

To understand which variables you need to edit before you can use the collection, learn more in [Required variable values](#required-values). To understand which variables you can optionally edit to customize the collection to suit your environment, learn more in [Optional variable values](#optional-values).

You can then start [using the collection](#using_the_collection).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can also override the default collection-level variables by creating a *Postman Environment*. Use the same variable names as the [Required variable values](#required-values).This is useful if you have more than one Advanced Identity Cloud tenant, as you can configure the connection and username values as separate environments in Postman.You can also enter potentially sensitive values in an environment to keep them separate from the collection. This means you can share the collection without sharing your credentials.For information on creating a Postman Environment, learn more in [Managing environments](https://learning.postman.com/docs/sending-requests/managing-environments) in the "*Postman Learning Center*". |

### Required variable values

Before using the collection, you must provide the correct values for the following variables. You can provide the value at the collection level or add them at the [environment level](#enviroment).

|   |                                                         |
| - | ------------------------------------------------------- |
|   | Ensure you use strong passwords for access credentials. |

#### Server URLs

* `platformUrl`

  * Default

    `https://<tenant-env-fqdn>`

  * Description

    Specifies the root URL of your Advanced Identity Cloud.

* `amUrl`

  * Default

    `https://<tenant-env-fqdn>/am`

  * Description

    Specifies the URL of the Access Management (AM) component of your Advanced Identity Cloud.

* `idmUrl`

  * Default

    `https://<tenant-env-fqdn>/openidm`

  * Description

    Specifies the URL of the Identity Management (IDM) component of your Advanced Identity Cloud.

#### User credentials

* `postmanServiceAccountID`

  * Default

    *Not set*

  * Description

    Specifies the **ID** of the [service account you created](#service_account) to allow the Postman collection access to your tenant.

    The collection uses this ID when creating a JWT to sign, which it then uses to obtain an access token.

    The JWT is generated when you [run the Prerequisite requests](#running_the_prerequisite_requests).

  * Example

    `c41515a8e-9c7d-4c37-4b2a-58c0fdea2080`

* `postmanServiceAccountJWK`

  * Default

    *Not set*

  * Description

    Specifies the **private key** you downloaded as `key.jwk` when you [created the service account](#service_account).

    Open the downloaded `key.jwk` in a text editor, and then enter the entire JSON web key into the field in Postman, including the curly braces.

    The collection uses this key to sign a JWT token, which it then uses to obtain an access token.

    The JWK is used to sign the JWT when you [run the Prerequisite requests](#running_the_prerequisite_requests).

  * Example

    ```json
    {
      "d": "MsVF...dmvw",
      "dp": "0iic...jdrw",
      "dq": "BXja...4epQ",
      "e": "AQAB",
      "kty": "RSA",
      "n": "stO0...qNyU",
      "p": "3VoI-ZPcw",
      "q": "ztGg...EJBw",
      "qi": "NHkA...NV_Gw"
    }
    ```

* `postmanClientSecret`

  * Default

    *Not set*

  * Description

    Specifies the **secret** used by the OAuth 2.0 clients the collection creates.

    You create these clients when you [run the Prerequisite requests](#running_the_prerequisite_requests).

* `postmanDemoPassword`

  * Default

    *Not set*

  * Description

    Specifies the **password** used by the managed realm user the collection creates for demonstration purposes.

    You create the realm user when you [run the Prerequisite requests](#running_the_prerequisite_requests).

#### Logging API

* `logApiKey`

  * Default

    *Not set*

  * Description

    Specifies the API key used to access the monitoring endpoints.

    Add this key to run the auditing and monitoring requests.

    Learn more in [Obtaining API Credentials](authenticate-to-rest-api-with-api-key-and-secret.html).

  * Example

    `0405de08ea73f1d84f`

* `logApiSecret`

  * Default

    *Not set*

  * Description

    Specifies the API secret used to access the monitoring endpoints.

    Add this key to run the auditing and monitoring requests.

    Learn more in [Obtaining API Credentials](authenticate-to-rest-api-with-api-key-and-secret.html).

  * Example

    `58932ad661ccf7ea5eda0b...a8d310e1676c9cac7f`

### Optional variable values

The collection uses the following additional variables that work using their default values; however, you can modify them.

> **Collapse: List of optional variable values**
>
> * `postmanDemoUsername`
>
>   * Default
>
>     `postmanDemoUser`
>
>   * Description
>
>     Specifies the **username** of the managed realm user the collection creates for demonstration purposes.
>
> * `postmanDemoEmail`
>
>   * Default
>
>     `demo.user@postman.example.com`
>
>   * Description
>
>     Specifies the **email** of the managed realm user the collection creates for demonstration purposes.
>
>     |   |                                                                                                                                                            |
>     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
>     |   | Enter an email address you have access to if you want to test the forgotten username or password flows in the user self-service section of the collection. |
>
> * `realm`
>
>   * Default
>
>     `/realms/root/realms/alpha`
>
>   * Description
>
>     Specifies the realm that the majority of the requests in the collection use.
>
>     You must specify the entire hierarchy of the realm, starting at the root realm.
>
>     Prefix each realm in the hierarchy with the `realms` keyword.
>
>   * Example
>
>     `/realms/root/realms/customers/realms/europe`.
>
> * `cookieName`
>
>   * Default
>
>     Not set
>
>   * Description
>
>     Specifies the name of the session cookie the tenant uses to store session tokens.
>
>     The collection sets this value automatically when you run the first request in the Prerequisites folder.
>
> * `loginJourney`
>
>   * Default
>
>     `Login`
>
>   * Description
>
>     Specifies the authorization journey name to use.
>
>     For information on the default journeys that Advanced Identity Cloud provides, learn more in [Login](../journeys/journeys.html#login).
>
> * `redirect_uri`
>
>   * Default
>
>     `https://httpbin.org/anything`
>
>   * Description
>
>     Specifies the URI to which the OAuth 2.0 client will redirect the user upon a successful authentication request.
>
> * `postmanConfidentialClientId`
>
>   * Default
>
>     `postmanConfidentialClient`
>
>   * Description
>
>     Specifies the ID of the OAuth 2.0 private client.
>
> * `postmanPublicClientId`
>
>   * Default
>
>     `postmanPublicClient`
>
>   * Description
>
>     Specifies the ID of the OAuth 2.0 public client.

### Hard-coded variable values

The collection uses the following additional variables that must not be modified.

> **Collapse: List of hard-coded variable values**
>
> * `postmanUtilLib`
>
>   * Description
>
>     Contains the `postman-util-lib` utility library that the collection uses to sign requests and generate certain keys.
>
>     Learn more in [postman-util-lib](https://joolfe.github.io/postman-util-lib/) on GitHub.

## Use the collection

Before using the Advanced Identity Cloud Postman collection, you should run the Prerequisite requests. The requests configure your Advanced Identity Cloud with the necessary elements, such as OAuth 2.0 clients and managed users

### Running the prerequisite requests

|   |                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Ensure you have configured the required collection variables as described in [Configure collection variables](#configuring_the_collection) before running the prerequisite requests. |

1. In Postman, with the Advanced Identity Cloud collection loaded, open the Prerequisites section.

2. Select the first request in the list, examine the details, and when you're satisfied the request is properly formed, click Send.

   Many of the requests have associated tests; for example, that the response code was `200`. Postman displays the test results alongside the response to the request.

   Many of the requests set a global variable containing a value returned in the response for use in subsequent requests.

   View the details of these in the Tests tab of a request. You can also view the values of these global variables by clicking Environment Quick Look ([icon: eye, set=fa]).

3. Repeat the previous step for each request in the Prerequisites folder.

When completed, Advanced Identity Cloud contains the following:

* An alpha\_user identity, named `postmanDemoUser` by default, which demonstrates a number of user-related endpoints, such as identity profiles, and user self-service.

* Two OAuth 2.0 clients:

  1. A client named `postmanConfidentialClient`, which is used by the OAuth 2.0 requests to demonstrate a number of grant flows.

  2. A client named `postmanPublicClient`, which is used by the OAuth 2.0 requests to demonstrate a number of grant flows.

If you need to recreate any of the above, or decide to alter the default values, run each of the steps in the Prerequisite folder again.

### Running the requests

The requests in the collection are split into different features. To run the calls for a feature, open the relevant folder, and run each request in sequence.

The value in square brackets in the name shows what type of authentication the request requires:

* `[User]`

  The request acts on a user's data or profile.

  These requests often authenticate as `postmanDemoUser` in the collection.

* `[fr:am:*]`

  The request requires an access token that has the `fr:am:*` scope so that it can perform access management related actions.

  These requests authenticate as the [service account](#service_account) you created earlier.

* `[fr:idm:*]`

  The request requires an access token that has the `fr:idm:*` scope so that it can perform identity management related actions.

  These requests authenticate as the [service account](#service_account) you created earlier.

Note that [intelligent access](#intelligent_access) and [identity profiles](#identity_profiles) have additional functionality. Refer to each section for details.

#### Intelligent access

There are scripts in the Intelligent Access requests that attempt to detect the callbacks that the first step returns, and sets the next request to handle it.

To view the details of this script:

1. Click on the top level of the collection menu (labelled PingOne Advanced Identity Cloud Collection), then select the Pre-request Scripts tab.

2. Within the tab, examine the `detectCallbacks` script.

When manually running through the steps, examine the response returned in the first call, and run the relevant next step. The collection is able to handle the following ready-to-use callbacks:

**Intelligent Access Callback Steps**

| Step    | Callback                                                                                                           |
| ------- | ------------------------------------------------------------------------------------------------------------------ |
| Step 2a | Username and password callbacks, together in a page node.                                                          |
| Step 2b | *Validated* create username and password callbacks, together in a page node.                                       |
| Step 2c | Choice callbacks.                                                                                                  |
| Step 2d | Text input callbacks.                                                                                              |
| Step 2e | Device profile callbacks. Learn more in [Configure Device Profiling](../solution-configure-device-profiling.html). |
| Step 2f | Progressive profile callbacks.                                                                                     |

#### Identity profiles

Some endpoints require the ID of an identity, rather than the username.

An example of this is when getting the OAuth 2.0 profiles a user has provided consent to.

When running the *Identity Profiles* requests, ensure you have also executed the request named Step 3: \[User] Read session info and store ID in the Authenticate as "Postman Demo User" folder.

The result is stored in the `demoUserId` global variable.

---

---
title: Advanced Identity Cloud REST
description: Overview of the Advanced Identity Cloud REST framework including resources, CRUDPAQ verbs, query parameters, and extension points
component: pingoneaic
page_id: pingoneaic:developer-docs:crest/about-crest
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/crest/about-crest.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  about-crest-resources: Resources
  about-crest-verbs: Verbs
  about-crest-parameters: Query parameters
  about-crest-extensions: Extension points
---

# Advanced Identity Cloud REST

Advanced Identity Cloud REST is a REST API framework defining common APIs to access web resources and collections of resources.

## Resources

Endpoints generally return JSON-format resources, though resource formats can depend on the implementation.

Resources in collections can be found by their unique identifiers (IDs). IDs are exposed in the resource URIs. For example, if a service has a user collection under `/users`, you can access a user at `/users/user-id`. The ID is also the value of the `_id` field of the resource.

Resources are versioned using revision numbers. A revision is specified in the resource's `_rev` field. Revisions make it possible to figure out whether to apply changes without resource locking and without distributed transactions.

## Verbs

The Advanced Identity Cloud REST APIs use the following verbs, sometimes referred to collectively as CRUDPAQ. For details and HTTP-based examples of each, follow the links to the sections for each verb.

| Verb                  | Description                                          |
| --------------------- | ---------------------------------------------------- |
| [Create](create.html) | Add a new resource with HTTP PUT or HTTP POST.       |
| [Read](read.html)     | Retrieve a single resource with HTTP GET.            |
| [Update](update.html) | Replace an existing resource with HTTP PUT.          |
| [Delete](delete.html) | Remove an existing resource with HTTP DELETE.        |
| [Patch](patch.html)   | Modify part of an existing resource with HTTP PATCH. |
| [Action](action.html) | Perform a predefined action with HTTP POST.          |
| [Query](query.html)   | Search a collection of resources with HTTP GET.      |

## Query parameters

Advanced Identity Cloud REST reserved query string parameter names start with an underscore (`_`).

Reserved query string parameters include, but are not limited to, the following names:

`_action`\
`_api`\
`_countOnly`\
`_crestapi`\
`_fields`\
`_mimeType`\
`_pageSize`\
`_pagedResultsCookie`\
`_pagedResultsOffset`\
`_prettyPrint`\
`_queryExpression`\
`_queryFilter`\
`_queryId`\
`_sortKeys`\
`_totalPagedResultsPolicy`

|   |                                                                                        |
| - | -------------------------------------------------------------------------------------- |
|   | Some parameter values are not safe for URLs; URL-encode parameter values as necessary. |

## Extension points

The *action* verb is the main vehicle for extensions. For example, to create a new user with HTTP POST rather than HTTP PUT, you might use `/users?_action=create`. An endpoint can define additional actions. For example, `/tasks/1?_action=cancel`.

A service can define *stored queries* to call by ID. For example, `/groups?_queryId=hasDeletedMembers`. Stored queries can call for additional parameters. The parameters are also passed in the query string. Which parameters are valid depends on the stored query.

---

---
title: Advanced Identity Cloud REST API custom headers
description: Reference for Advanced Identity Cloud REST API custom headers including client IP, geolocation, and transaction ID headers
component: pingoneaic
page_id: pingoneaic:developer-docs:api-custom-headers
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/api-custom-headers.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: you might use the country code
section_ids:
  debugging: Debugging
  client-ip-addresses: Client IP addresses
  client-geolocation: Client geolocation
  other: Other
---

# Advanced Identity Cloud REST API custom headers

in the [X-Client-Region](#x-client-region) header to enforce MFA in a sign-on journey for clients originating from a specific country or set of countries.

## Debugging

* X-ForgeRock-TransactionID

  This header contains a unique value, such as `f89da9de-22f4-4e0b-8527-26b8d9c53d7b-request-1/0`, that can be used to identify the current request and correlate it with Advanced Identity Cloud log entries from all log sources. Learn more in [Filter logs for a specific request](../tenants/audit-debug-logs.html#filter-logs-for-a-specific-request).

|   |                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Advanced Identity Cloud adds a similar header `X-Cloud-Trace-Context` for tracing requests. This is used internally by the Ping Identity support team. It's also deprecated, so you shouldn't use this header in your integrations. |

## Client IP addresses

* X-Forwarded-For

  This header contains a comma-separated list of originating IP addresses for the client.

  * If the request doesn't have an `X-Forwarded-For` header set before it connects to the tenant environment load balancer, the header is added to the request and contains the following IP addresses:

    ```
    X-Forwarded-For: <client-ip-address>, <load-balancer-ip-address>
    ```

    * `<client-ip-address>` is the IP address of the client when it connects to the tenant environment load balancer.

    * `<load-balancer-ip-address>` is the IP address of the tenant environment load balancer.

  * If the request already has an `X-Forwarded-For` header set before it connects to the tenant environment load balancer, the header is modified to contain the following IP addresses:

    ```
    X-Forwarded-For: <existing-ip-address>, <client-ip-address>, <load-balancer-ip-address>
    ```

    * `<existing-ip-address>` is the IP address the `X-Forwarded-For` header contains when the client connects to the tenant environment load balancer.

    * `<client-ip-address>` is the IP address of the client when it connects to the tenant environment load balancer.

    * `<load-balancer-ip-address>` is the IP address of the tenant environment load balancer.

  |   |                                                                                                                                                                                                         |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | There are security and privacy concerns associated with the use of this header. Learn more in the MDN doc [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For). |

- X-Trusted-Forwarded-For

  This header contains a comma-separated list of trusted IP addresses for the client:

  ```
  X-Trusted-Forwarded-For: <trusted-ip-address>, <client-ip-address>, <load-balancer-ip-address>
  ```

  * `<trusted-ip-address>` is a trusted client IP address, verified by Ping Identity.

  * `<client-ip-address>` is the IP address of the client when it connects to the tenant environment load balancer.

  * `<load-balancer-ip-address>` is the IP address of the tenant environment load balancer.

* X-Real-IP

  This header contains a trusted client IP address, verified by Ping Identity:

  ```
  X-Real-IP: <trusted-ip-address>
  ```

|   |                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For the `X-Trusted-Forwarded-For` and `X-Real-IP` headers, if the client is behind a reverse proxy, the trusted client IP address contains the real IP address of the reverse proxy, not the client. |

Learn more in [Identify originating client IP addresses](../planning/plan-security.html#identify-originating-client-ip-addresses).

## Client geolocation

* X-Client-Region

  This header contains the country (or region) associated with the client's IP address in the form of a two-letter region code, such as `US` or `FR`. For most countries, these region codes correspond directly to ISO-3166-2 codes.

- X-Client-City

  This header contains the name of the city where the client request originated. For example, `Mountain View` for Mountain View, California. There's no canonical list of valid values for this header. The city names can contain ASCII letters, numbers, spaces, and the following characters: ``"!#$%&'*+-.^_`|~"``.

* X-Client-City-Lat-Long

  This header contains the latitude and longitude of the city where the client request originated. For example, `37.386051,-122.083851` for a request from Mountain View.

|   |                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For the `X-Client-Region`, `X-Client-City` and `X-Client-City-Lat-Long` headers, if the client is behind a reverse proxy, the geolocation information represents the reverse proxy, not the client. If you require greater accuracy, Ping Identity recommends that you integrate an IP lookup service into your end-user journeys. |

Learn more in [Identify client geolocation](../planning/plan-security.html#identify-client-geolocation).

## Other

* X-Forwarded-Proto

  This header contains the HTTP protocol the client used to connect to the tenant environment load balancer. Possible values are `http` or `https`. Learn more in the MDN doc [X-Forwarded-Proto](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For).

- X-Requested-With

  This header contains the name of the originating web technology or platform. For example, most JavaScript frameworks set the value as `XMLHttpRequest`. The header can be used to influence application behavior. For example, returning HTML data by default but returning JSON data for requests that set the value as `XMLHttpRequest`. The header can also be used to protect against CSRF attacks. Learn more in [CSRF attacks](../planning/plan-security.html#csrf-attacks).

---

---
title: Auth scripting
description: Create and manage auth scripts in Advanced Identity Cloud to extend authentication journeys, OAuth 2.0 flows, SAML, and policy conditions
component: pingoneaic
page_id: pingoneaic:developer-docs:scripting-auth
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/scripting-auth.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Scripts", "Authentication", "OAuth 2.0", "OpenID Connect (OIDC)", "Policies &amp; Entitlements", "Journeys"]
page_aliases: ["pingoneaic::scripts.adoc"]
section_ids:
  auth_script_types: Auth script types
  manage-auth-scripts: Manage auth scripts
  create-a-new-auth-script: Create a new auth script
  decision-scripts: Journey decision node scripts
  create-decision-scripts: Create a new journey decision node script
  more_information: More information
---

# Auth scripting

You can use authentication and authorization (auth) scripting to modify default Advanced Identity Cloud behavior in many situations: client-side authentication, policy conditions, handling OpenID Connect claims, and others.

Use JavaScript for auth scripting in Advanced Identity Cloud. Groovy scripts are deprecated and will eventually be completely replaced with JavaScript scripts.

For JavaScript examples of all [auth script types](#auth_script_types), review the [sample scripts](../am-scripting/sample-scripts.html). Each sample script includes a list of available variables.

|   |                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Scripts can potentially emit the personally identifiable information (PII) of your end users into Advanced Identity Cloud logs, and then into external services that consume Advanced Identity Cloud logs.Ping Identity recommends that you establish a review and testing process for all scripts to prevent PII leaking out of your Advanced Identity Cloud tenant environments. |

## Auth script types

The auth script types available in Advanced Identity Cloud include the following:

> **Collapse: Journeys**
>
> | Script type                 | Description                                                                                                                                           | Information                                                                                            |
> | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
> | Configuration Provider Node | Runs in a Configuration Provider node as a step in an authentication journey.                                                                         | [Configuration Provider node](https://docs.pingidentity.com/auth-node-ref/latest/config-provider.html) |
> | Journey Decision Node       | Runs in a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) as a step in an authentication journey. | [Scripted Decision node API](../am-scripting/scripting-api-node.html)                                  |

> **Collapse: OAuth2 / OIDC**
>
> | Script type                      | Description                                                                                                 | Information                                                                |
> | -------------------------------- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
> | OAuth2 Access Token Modification | Modifies the key-value pairs contained within access tokens before they're issued to a client.              | [Access tokens](../am-oauth2/modifying-access-tokens-scripts.html)         |
> | OAuth2 Evaluate Scope            | Retrieves and modifies scopes for OAuth 2.0 access token introspection.                                     | [Scope evaluation](../am-oauth2/plugins-scope-evaluator.html)              |
> | OAuth2 May Act                   | Adds the `may_act` claim to tokens when performing token exchanges.                                         | [Token exchange](../am-oauth2/token-exchange.html)                         |
> | OAuth2 Trusted JWT Issuer        | Dynamically retrieves the details of an issuer during the JWT profile for authorization grant.              | [JWT profile for authorization](../am-oauth2/oauth2-jwt-bearer-grant.html) |
> | OAuth2 Validate Scope            | Modifies how Advanced Identity Cloud validates requested OAuth 2.0 scopes.                                  | [Scope validation](../am-oauth2/plugins-scope-validator.html)              |
> | OIDC Claims                      | Modifies or overrides OIDC claims when issuing an ID token or in the response from the `userinfo` endpoint. | [OIDC claims](../am-oauth2/plugins-user-info-claims.html)                  |

> **Collapse: SAML**
>
> | Script type                | Description                                                                              | Information                                                          |
> | -------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
> | SAML2 SP Account Mapper    | Customize how SAML assertion attributes are mapped to user profiles on the SP.           | [SP account mapper](../am-saml2/custom-sp-account-mapper.html)       |
> | SAML2 SP Adapter           | Modifies the processing of the authentication request on the SP.                         | [SP adapter](../am-saml2/custom-sp-adapter.html)                     |
> | SAML2 SP Account Mapper    | Modifies how SAML 2.0 assertions are mapped to user profiles.                            | [SP account mapper](../am-saml2/custom-sp-account-mapper.html)       |
> | SAML2 IDP Adapter          | Modifies the processing of the authentication request on the IDP.                        | [IdP adapter](../am-saml2/custom-idp-adapter.html)                   |
> | SAML2 IDP Attribute Mapper | Maps user-configured attributes to SAML attributes in the assertion returned by the IDP. | [IdP attribute mapper](../am-saml2/custom-idp-attribute-mapper.html) |
> | SAML2 NameID Mapper        | Customize the value of the NameID attribute in the SAML assertion on the remote SP.      | [NameID mapper](../am-saml2/custom-nameid-mapper.html)               |

> **Collapse: Other**
>
> | Script type                                     | Description                                                                                                                                                                                                                                         | Information                                                                                          |
> | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
> | Client-side Authentication                      | Runs on the client during authentication.                                                                                                                                                                                                           |                                                                                                      |
> | Library                                         | Contains reusable functionality that can be imported into journey decision node scripts or other library scripts.                                                                                                                                   | [Library scripts](../am-scripting/library-scripts.html)                                              |
> | Policy Condition                                | Modifies authorization policy decisions.                                                                                                                                                                                                            | [Scripted policy conditions](../am-authorization/scripted-policy-condition.html)                     |
> | Social Identity Provider Profile Transformation | Runs in a [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html). Adapts the fields received from a social identity provider to align with the fields expected by Advanced Identity Cloud. | [Social IdP scripting API](../am-scripting/social-idp-profile-transformation-api.html)               |
> | PingOne Verify Completion Decision Node         | Runs in a [PingOne Verify Completion Decision node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-completion-decision.html) so that you can access information about the user's PingOne Verify transactions.            | [PingOne Verify Completion Decision node API](../am-scripting/p1verify-completion-decision-api.html) |

|   |                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some script types aren't yet available in the Advanced Identity Cloud admin console. To view a list of all the script types, under Native Consoles > Access Management, go to Realms > *Realm Name* > Scripts and click New Script. |

## Manage auth scripts

To manage your auth scripts, go to *Realm* > Scripts > Auth Scripts.

On the Scripts page, you can view a list of existing scripts. To edit, duplicate, or delete a script, click its More ([icon: ellipsis-h, set=fa]) menu.

The edit option in the More menu opens the script in a lightweight editor that features syntax highlighting and validation checking. You can maximize the editor to full screen to edit larger scripts:

![Script editor](_images/idcloudui-scripts-editor.png)

① JavaScript editor\
② Fullscreen option\
③ Syntax highlighting\
④ Syntax error highlighting and validation checking

## Create a new auth script

1. Go to *Realm* > Scripts > Auth Scripts, then click + New Script.

2. Choose an auth [script type](#auth_script_types).

   After you select a script type, the editor opens. The editor is prepopulated with a default script for that type, which is intended as a starting point for your custom script.

   If you selected the wrong script type, click Previous to select a different script type.

3. If the [next-generation script engine](../am-scripting/next-generation-scripts.html) is available for the script type, Advanced Identity Cloud displays the Choose Script Engine page.

   Select Legacy or Next Generation to set the script engine for your script.

4. Enter a unique Name and optional Description for the script, then click Save.

   After you save a script, you can't change its type.

## Journey decision node scripts

Learn more about journeys in [Journeys](../journeys/journeys.html).

You can also create, edit, and validate journey decision node scripts directly from within a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html).

1. Go to *Realm* > Journeys.

2. Open a journey in the journey editor.

3. Find an existing scripted decision node or add a new one.

4. Select the scripted decision node to open the context pane on the right side.

5. The following screenshot shows where you can create a new journey decision node script ④ or edit an existing one ⑤:

   ![Journey editor with Scripted Decision node](_images/idcloudui-journeys-scripted-decision-script-options.png)

   ① Scripted decision node\
   ② Context pane\
   ③ Journey decision node script drop-down\
   ④ Add new journey decision node script\
   ⑤ Edit existing journey decision node script

### Create a new journey decision node script

Add a new journey decision node script in the journey editor or from *Realm* > Scripts > Auth Scripts.

1. Select Legacy or Next Generation on the Choose Script Engine page.

   Learn more about the enhanced scripting engine in [Next-generation scripts](../am-scripting/next-generation-scripts.html).

2. If you create or edit a Next Generation script, click the Libraries icon in the top right to display the following side panel:

   ![Next generation journey decision node script editor](_images/nextgen-editor.png)

   ① View and search library scripts to import in your script.\
   ② Click to expand a library script and view its exported methods and constants.\
   The font colors indicate the exported types:

   * Blue for functions

   * Red for numbers

   * Green for strings

   * Orange for boolean types

   * Purple for objects / properties

   ③ Click the Docs icon to view links to context-related documentation.\
   A red dot denotes documentation updates.\
   ④ Edit your script and import library scripts as necessary.

3. Enter a unique Name and optional Description for the script, then click Save.

## More information

* [User identity attributes and properties reference](../identities/user-identity-properties-attributes-reference.html)

* [Scripting environment](../am-scripting/scripting-env.html)

* [Scripting API](../am-scripting/scripting-api.html)

* [Sample scripts](../am-scripting/sample-scripts.html)

* [Customize OAuth 2.0 using JavaScript extensions](../am-oauth2/plugins-customize.html)

---

---
title: Authenticate to Advanced Identity Cloud REST API
description: Overview of authentication methods for the Advanced Identity Cloud REST API, including API key and access token options
component: pingoneaic
page_id: pingoneaic:developer-docs:authenticate-to-rest-api-overview
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/authenticate-to-rest-api-overview.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Integration", "REST API", "Authentication"]
page_aliases: ["developer-docs:accessing-rest-api-overview.adoc"]
section_ids:
  summary_of_authentication_methods: Summary of authentication methods
---

# Authenticate to Advanced Identity Cloud REST API

The Advanced Identity Cloud REST API has two different authentication methods, depending on what you are trying to achieve:

* Use an API key and secret for read-only operations.\
  Examples: Advanced Identity Cloud monitoring and logging.

* Use an access token for access management operations or identity management operations.\
  Examples: Setting up authentication journeys or policies; configuring user profiles, roles, or assignments.

## Summary of authentication methods

The following table summarizes the REST API endpoints and their different authentication methods:

| REST endpoints                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Authentication method                                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| * `/monitoring/health`

* `/.well-known/*` (for `GET` requests)                                                                                                                                                                                                                                                                                                                                                                                                              | Not applicable (publicly accessible endpoint)                                                                                                                       |
| - `/monitoring`

- `/logs`                                                                                                                                                                                                                                                                                                                                                                                                                                                   | API key and secret.Learn more in [Authenticate to Advanced Identity Cloud REST API with API key and secret](authenticate-to-rest-api-with-api-key-and-secret.html). |
| * `/am/*`

* `/openidm/*`

* `/.well-known/*`

* `/environment/certificates`, `/environment/csrs` 

* `/environment/content-security-policy/*`

* `/environment/cookie-domains`

* `/environment/custom-domains`

* `/environment/promotion/*`

* `/environment/proxy-connect/*`

* `/environment/release`

* `/environment/restart`, `/environment/secrets`, `/environment/variables` 

* `/environment/release`

* `/environment/sso-cookie`

* `/environment/telemetry/*` | Access tokenLearn more in [Authenticate to Advanced Identity Cloud REST API with access token](authenticate-to-rest-api-with-access-token.html).                    |

---

---
title: Authenticate to Advanced Identity Cloud REST API with access token
description: Authenticate to the Advanced Identity Cloud REST API with a service account access token obtained using the JWT bearer grant flow
component: pingoneaic
page_id: pingoneaic:developer-docs:authenticate-to-rest-api-with-access-token
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/authenticate-to-rest-api-with-access-token.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Integration", "REST API", "Authentication"]
page_aliases: ["developer-docs:accessing-rest-api-with-access-token.adoc", "developer-docs:accessing-rest-api-with-session-token.adoc", "developer-docs:authenticate-to-rest-api-with-session-token.adoc", "release-notes:rapid-channel/service-accounts-authenticate-to-rest-api-with-access-token.adoc"]
section_ids:
  get_an_access_token: Get an access token
  prerequisites: Prerequisites
  create-a-service-account-and-download-its-private-key: "Task 1: Create a service account and download its private key"
  create-and-sign-a-jwt: "Task 2: Create and sign a JWT"
  get-an-access-token-using-the-jwt-profile-authorization-grant: "Task 3: Get an access token using the JWT profile authorization grant"
  use_an_access_token: Use an access token
---

# Authenticate to Advanced Identity Cloud REST API with access token

You need an access token to authenticate to the following Advanced Identity Cloud REST API endpoints:

* `/am/*`

* `/openidm/*`

* `/.well-known/*`

* `/environment/certificates`, `/environment/csrs` ([self-managed certificate endpoints](../realms/server-certificates-api.html))

* `/environment/content-security-policy/*`

* `/environment/cookie-domains` ([cookie domains endpoint](../realms/cookie-domains-api.html))

* `/environment/custom-domains`

* `/environment/promotion/*` ([self-service promotion endpoints](../tenants/self-service-promotions-api.html))

* `/environment/proxy-connect/*` ([Proxy Connect endpoints](../tenants/proxy-connect-api.html))

* `/environment/release` ([release endpoint](../tenants/environments-release-information.html#view-release-information-using-the-api))

* `/environment/restart`, `/environment/secrets`, `/environment/variables` ([ESV endpoints](../tenants/esvs-manage-api.html))

* `/environment/sso-cookie`

* `/environment/telemetry` ([log event exporter endpoints](../tenants/audit-debug-logs-push-api.html))

Summary of use:

1. Create a service account in the Advanced Identity Cloud admin console and download a private key.

2. Create a JSON Web Token (JWT) and sign it using the private key.

3. Create an access token using the JWT profile for OAuth 2.0 authorization grant flow.

4. Set the access token as a bearer token in the `Authorization` HTTP header for each API request:

   ```bash
    Authorization: Bearer <access-token>
   ```

## Get an access token

### Prerequisites

You need the [jose](https://github.com/latchset/jose) command-line tool to run some of the commands. The jose command-line tool is a C-language implementation of the Javascript Object Signing and Encryption (JOSE) standards. You can find installation instructions for your particular package manager in <https://command-not-found.com/jose>.

|   |                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The instructions won't work using any of the Node.js tools called jose. Although they have the same name, they're separate implementations of the JOSE standards. |

### Task 1: Create a service account and download its private key

1. Follow the steps in [Create a new service account](../tenants/service-accounts.html#create-a-new-service-account).

   1. In step 9, save the private key as a local file called `key.jwk`.

   2. Note the ID for the service account you created. An example of an ID is `449d7e27-7889-47af-a736-83b6bbf97ec5`.

### Task 2: Create and sign a JWT

1. Set the following variables in your terminal, to be used as claims in a JWT payload:

   1. Set `SERVICE_ACCOUNT_ID` to hold the ID of the service account. For use in the `iss` (issuer) and `sub` (subject) claims.

      ```bash
      $ SERVICE_ACCOUNT_ID="<service-account-id>"(1)
      ```

      |       |                                                                                                                  |
      | ----- | ---------------------------------------------------------------------------------------------------------------- |
      | **1** | Replace `<service-account-id>` with the service account ID; for example, `449d7e27-7889-47af-a736-83b6bbf97ec5`. |

   2. Set `AUD` to hold the URL (including port number) where the JWT will be used to request the access token. For use in the `aud` (audience) claim.

      ```bash
      $ AUD='https://<tenant-env-fqdn>:443/am/oauth2/access_token'
      ```

   3. Set `EXP` to hold a 15-minute expiration time for the JWT, expressed as a Unix timestamp. For use in the `exp` (expiration time) claim.

      ```bash
      $ EXP=$(($(date -u +%s) + 899))
      ```

      |   |                                                                                                                                                                                                                                                                                                                                         |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Service account access tokens have a non-configurable, fixed expiry of 899 seconds (15 minutes), so the previous example sets a timestamp value that matches the fixed expiry. Despite the expiry being non-configurable, you must supply the `exp` claim, set with a nominal future timestamp, to create an access token successfully. |

   4. Set `JTI` to hold a unique ID for the JWT. For use in the `jti` (JWT ID) claim.

      ```bash
      $ JTI=$(openssl rand -base64 16)
      ```

2. Combine the claims to create a payload for the JWT:

   ```bash
   $ echo -n "{
       \"iss\":\"${SERVICE_ACCOUNT_ID}\",
       \"sub\":\"${SERVICE_ACCOUNT_ID}\",
       \"aud\":\"${AUD}\",
       \"exp\":${EXP},
       \"jti\":\"${JTI}\"
   }" > payload.json
   ```

3. Sign the JWT using the private key you downloaded and saved as `key.jwk` in step 1a:

   ```bash
   $ jose jws sig -I payload.json -k key.jwk -s '{"alg":"RS256"}' -c -o jwt.txt
   ```

### Task 3: Get an access token using the JWT profile authorization grant

1. Request an access token from the `/oauth2/access_token` endpoint using the JWT:

   ```bash
   $ curl \
   --request POST ${AUD} \
   --data "client_id=service-account" \(1)
   --data "grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer" \(2)
   --data "assertion=$(< jwt.txt)" \(3)
   --data "scope=<scope>"(4)
   ```

   |       |                                                                                                                                                                                                                                                                                                                                                                                        |
   | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **1** | The client ID `service-account` targets the built-in OAuth 2.0 public client for service accounts. The client only allows the [JWT profile for OAuth 2.0 authorization grant flow](../am-oauth2/oauth2-jwt-bearer-grant.html).	Access the built-in OAuth 2.0 public client using the tenant FQDN. You cannot access it using an Alpha or Bravo realm alias URL or a custom domain URL. |
   | **2** | The grant type `urn:ietf:params:oauth:grant-type:jwt-bearer` represents the JWT profile for OAuth 2.0 authorization grant flow.                                                                                                                                                                                                                                                        |
   | **3** | The `assertion` parameter is populated with the output of the signed JWT from step 2c.                                                                                                                                                                                                                                                                                                 |
   | **4** | Replace `<scope>` with a scope or a space delimited set of scopes; for example, `fr:idc:esv:*` or `fr:am:* fr:idm:*`. Learn more in [Service account scopes](../tenants/service-accounts.html#service-account-scopes). The specified scopes must be the same as (or a subset of) the scopes that you assigned to the service account.                                                  |

2. Examine the response to find the access token, represented as `access_token`:

   ```json
   {
       "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9... ...8ECmkyDJKow8Qp_Tnp_lGNRJzLWi18iUGQrCTtxyTXw",
       "scope": "fr:am:* fr:idm:*",
       "token_type": "Bearer",
       "expires_in": 899
   }
   ```

## Use an access token

To use the access token with the REST API, set it as a bearer token in the `Authorization` HTTP header for each API request.

The following example uses the access token to get a list of identities:

> **Collapse: Show request**
>
> ```bash
> $ curl \
> --request GET 'https://<tenant-env-fqdn>/openidm/managed/<realm>_user?_fields=userName,givenName,sn,mail,accountStatus&_prettyPrint=true&_queryFilter=true' \(1)
> --header 'Authorization: Bearer <access-token>'(2)
> ```

|       |                                                                                                                                             |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | Replace \<realm> with the realm where you created the access token.                                                                         |
| **2** | Replace \<access-token> with the `access_token` in the authentication response (learn more in [Get an access token](#get_an_access_token)). |

> **Collapse: Show response**
>
> ```json
> {
>     "result": [
>         {
>             "_id": "f413db4c-cebd-4950-81e6-57bdb47921a4",
>             "_rev": "0000000016e6754b",
>             "userName": "exampleuser",
>             "accountStatus": "active",
>             "givenName": "Example",
>             "sn": "User",
>             "mail": "exampleuser@example.com"
>         },
>         {
>             "_id": "15249a65-8f9a-4063-9586-a2465963cee4",
>             "_rev": "0000000016e6754b",
>             "userName": "exampleuser2",
>             "accountStatus": "active",
>             "givenName": "Example",
>             "sn": "User",
>             "mail": "exampleuser2@example.com"
>         },
>         {
>             "_id": "30485bc4-fdbb-4946-8ce4-1a53c6824d92",
>             "_rev": "0000000016e6754b",
>             "userName": "exampleuser3",
>             "accountStatus": "active",
>             "givenName": "Example",
>             "sn": "User",
>             "mail": "exampleuser3@example.com"
>         }
>     ],
>     "resultCount": 3,
>     "pagedResultsCookie": null,
>     "totalPagedResultsPolicy": "NONE",
>     "totalPagedResults": -1,
>     "remainingPagedResults": -1
> }
> ```

---

---
title: Authenticate to Advanced Identity Cloud REST API with API key and secret
description: Authenticate to Advanced Identity Cloud monitoring and logging REST API endpoints using an API key and secret
component: pingoneaic
page_id: pingoneaic:developer-docs:authenticate-to-rest-api-with-api-key-and-secret
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/authenticate-to-rest-api-with-api-key-and-secret.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Integration", "REST API", "Authentication"]
page_aliases: ["developer-docs:accessing-rest-api-with-api-key-and-secret.adoc"]
section_ids:
  get_an_api_key_and_secret: Get an API key and secret
  use_an_api_key_and_secret: Use an API key and secret
---

# Authenticate to Advanced Identity Cloud REST API with API key and secret

You will need an API key and secret to authenticate to the following Advanced Identity Cloud REST API endpoints:

* `/monitoring`

* `/logs`

Summary of use:

1. Create an API key and secret in the Advanced Identity Cloud admin console.

2. Set the API key and secret as `x-api-key` and `x-api-secret` HTTP headers for each API request:

   ```
   x-api-key: <api-key>
   x-api-secret: <api-secret>
   ```

## Get an API key and secret

1. In the Advanced Identity Cloud admin console, click the user icon, and then click Tenant Settings.

   > **Collapse: Show me where**
   >
   > ![tenant menu](../tenants/_images/tenant-menu.png)

2. On the Global Settings tab, click Log API Keys.

3. Click New Log API Key, provide a name for the key, and then click Create Key.

   A dialog box appears containing the new keys:

   ![log api key](_images/log-api-key.png)

4. Store the `api_key_id` and `api_key_secret` values securely.

   |   |                                                                               |
   | - | ----------------------------------------------------------------------------- |
   |   | You **cannot** view the `api_key_secret` value again once you click **Done**. |

5. Click Done.

## Use an API key and secret

To use the API credentials, set them as `x-api-key` and `x-api-secret` HTTP headers:

> **Collapse: Show request**
>
> ```bash
> $ curl \
> --request GET 'https://<tenant-env-fqdn>/monitoring/logs/sources?_prettyPrint=true' \
> --header 'x-api-key: <api-key>' \
> --header 'x-api-secret: <api-secret>'
> ```

> **Collapse: Show response**
>
> ```json
> {
>     "result": [
>         "am-access",
>         "am-activity",
>         "am-authentication",
>         "am-config",
>         "am-core",
>         "am-everything",
>         "idm-access",
>         "idm-activity",
>         "idm-authentication",
>         "idm-config",
>         "idm-core",
>         "idm-everything",
>         "idm-recon",
>         "idm-sync"
>     ],
>     "resultCount": 14,
>     "pagedResultsCookie": null,
>     "totalPagedResultsPolicy": "NONE",
>     "totalPagedResults": 1,
>     "remainingPagedResults": 0
> }
> ```

---

---
title: Create
description: Use the Create verb to add new resources to the Advanced Identity Cloud REST API using HTTP POST or HTTP PUT
component: pingoneaic
page_id: pingoneaic:developer-docs:crest/create
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/crest/create.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  parameters: Parameters
---

# Create

There are two ways to create a resource: HTTP POST or HTTP PUT.

To create a resource using POST, perform an HTTP POST with the query string parameter `_action=create` and the JSON resource as a payload. The service creates the identifier if not specified:

```http
POST /users?_action=create HTTP/1.1
Host: example.com
Accept: application/json
Content-Length: ...
Content-Type: application/json
{ JSON resource }
```

To create a resource using PUT, perform an HTTP PUT with the case-sensitive identifier for the resource in the URL path and the JSON resource as a payload. Optionally, include the `If-None-Match: *` header to prevent overwriting an existing object:

```http
PUT /users/some-id HTTP/1.1
Host: example.com
Accept: application/json
Content-Length: ...
Content-Type: application/json
If-None-Match: *
{ JSON resource }
```

The `_id` and the content of the resource depend on the endpoint. The service is not required to use the `_id` the client provides. The response to the create request indicates the resource location as the value of the `Location` header.

* If you *do* include the `If-None-Match: *` header, the request creates the object if it does not exist or fails if the object does exist.

* If you *do not* include the `If-None-Match: *` header, the request creates the object if it does not exist or *updates* the object if it does exist.

* If you include the `If-None-Match` header with any value other than `*`, the response is an HTTP 400 Bad Request error. For example, creating an object with `If-None-Match: revision` returns a bad request error.

## Parameters

You can use the following query string parameters:

| Parameter                  | Description                                                                                                                                                                                                                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_fields=field[,field...]` | Return only the specified fields in the body of the response.The `field` values are JSON pointers. For example, if the resource is `{"parent":{"child":"value"}}`, `parent/child` refers to the `"child":"value"`.If the `field` is left blank, the endpoint returns all default values. |
| `_prettyPrint=true`        | Format the body of the response.                                                                                                                                                                                                                                                         |

---

---
title: Custom endpoints
description: Create and manage custom endpoints in Advanced Identity Cloud to run JavaScript code through the REST API and extend platform behavior
component: pingoneaic
page_id: pingoneaic:developer-docs:scripting-custom-endpoints
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/scripting-custom-endpoints.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Scripts", "REST API"]
page_aliases: ["developer-docs:scripting/custom-endpoints.adoc"]
section_ids:
  custom_endpoints_scripting_introduction: Custom endpoints scripting introduction
  manage_custom_endpoints: Manage custom endpoints
  create_a_custom_endpoint: Create a custom endpoint
  generate_a_curl_request_for_a_custom_endpoint: Generate a cURL request for a custom endpoint
  run_a_test_request_for_a_custom_endpoint: Run a test request for a custom endpoint
  http_request_methods_mapped_to_script_request_method_property_values: HTTP request methods mapped to script request.method property values
---

# Custom endpoints

You can use custom endpoints to run arbitrary JavaScript code through the REST API. Custom endpoint scripts are extremely flexible and can extend Advanced Identity Cloud behavior in many ways:

* Validate user input fields before storing them in a user profile.

* Create utility functions, such as getting today's date.

* Mandate user input fields during registration to support delegated administration decisions.

* Query identities with a particular relationship, such as being a member of an organization, and page the results.

You can consume custom endpoints within Advanced Identity Cloud or integrate them into your external UIs or system applications.

## Custom endpoints scripting introduction

For an introduction to custom endpoints scripting, read the following:

* [Create custom endpoints to launch scripts](../idm-scripting/script-custom-endpoints.html)

* [Variables available to scripts in custom endpoints](../idm-scripting/script-variables-custom-endpoints.html)

|   |                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To understand how to create identity object query expressions to use in the `request.queryExpression` property, learn more in [Define and call data queries](../idm-objects/queries.html). |

|   |                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Scripts can potentially emit the personally identifiable information (PII) of your end users into Advanced Identity Cloud logs, and then into external services that consume Advanced Identity Cloud logs.Ping Identity recommends that you establish a review and testing process for all scripts to prevent PII leaking out of your Advanced Identity Cloud tenant environments. |

## Manage custom endpoints

To manage your custom endpoints, go to *Realm* > Scripts > Custom Endpoints.

On the Custom Endpoints page, you can view a list of existing custom endpoints. To edit, duplicate, or delete a custom endpoint, click its More ([icon: ellipsis-h, set=fa]) menu.

The edit option in the More menu opens the custom endpoint script in a lightweight editor. The editor features syntax highlighting and validation checking. Maximize the editor to full screen to edit larger scripts:

![idcloudui custom endpoints editor](_images/idcloudui-custom-endpoints-editor.png)

① Endpoint name\
② JavaScript editor\
③ Fullscreen option\
④ Syntax highlighting\
⑤ Validation checking\
⑥ cURL request tab, learn more in [Generate a cURL request for a custom endpoint](#generate_a_curl_request_for_a_custom_endpoint)\
⑦ Test tab, learn more in [Run a test request for a custom endpoint](#run_a_test_request_for_a_custom_endpoint)

## Create a custom endpoint

1. Go to *Realm* > Scripts > Custom Endpoints, then click + New Script.

2. Enter a Name for your new endpoint; for example, `getDate`.

   * Access the new custom endpoint over HTTP at:\
     `https://<tenant-env-fqdn>/openidm/endpoint/<name>`

   * Access the new custom endpoint in a script using:\
     `openidm.read('endpoint/<name>')`

3. (Optional) Enter a Description for your new endpoint; for example, `Get the current date`.

4. Next, use the editor to create your script. The editor is prepopulated with a default script, which is intended as a starting point for your custom script.

5. To test your script, click Save, then either:

   1. [Generate a cURL request for a custom endpoint](#generate_a_curl_request_for_a_custom_endpoint)

   2. [Run a test request for a custom endpoint](#run_a_test_request_for_a_custom_endpoint)

6. When your testing is complete, click Save and Close.

## Generate a cURL request for a custom endpoint

In the script editor:

1. Click the angled brackets icon (**<>**) to open the cURL Request tab.

2. In the Method field, choose an HTTP request method for the cURL request. Learn more about how HTTP request methods relate to the script `request.method` property values in this [mapping table](#http_request_methods_mapped_to_script_request_method_property_values).

3. (Optional) In the Body field, enter a JSON-formatted body for the cURL request (except when using the `GET` HTTP request method). For example:

   ```json
   {
       "param1": "foo",
       "param2": "bar"
   }
   ```

   |   |                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | In the script, you can access the body using the `request.content` property. The example above maps to `request.content.param1` and `request.content.param2`. |

4. Click Generate to output the cURL request, which appears below your script. The cURL request is complete with an access bearer token and ready to run.

5. Click the copy icon ([icon: clone, set=fa]) to copy the cURL request from the editor, then paste and run it in a terminal window.

## Run a test request for a custom endpoint

In the script editor:

1. Click the triangle icon ([icon: play, set=fa]) to open the Test tab.

2. In the form field, enter a JSON-formatted configuration object for the cURL request. The form field is prepopulated with a default configuration object:

   ```json
     {
       "request": {
         "method": "create"
       }
     }
   ```

   This default configuration object creates a request using the `POST` HTTP request method. Learn more about how HTTP request methods relate to the script `request.method` variable parameter values in this [mapping table](#http_request_methods_mapped_to_script_request_method_property_values).

3. (Optional) To supply a body with the request, add a `request.content` property:

   ```json
     {
       "request": {
         "method": "create",
         "content": {
           "param1": "foo",
           "param2": "bar"
         }
       }
     }
   ```

   |   |                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | In the script, you access the body using the `request.content` property. The example above maps to `request.content.param1` and `request.content.param2`. |

4. Click Run to run the cURL request. The result appears below the editor.

## HTTP request methods mapped to script `request.method` property values

| HTTP request method | Script `request.method` |
| ------------------- | ----------------------- |
| `GET`               | `read`                  |
| `POST`              | `create`                |
| `PUT`               | `update`                |
| `PATCH`             | `patch`                 |
| `DELETE`            | `delete`                |

---

---
title: Delete
description: Use the Delete verb to remove a single resource from the Advanced Identity Cloud REST API using HTTP DELETE
component: pingoneaic
page_id: pingoneaic:developer-docs:crest/delete
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/crest/delete.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  parameters: Parameters
---

# Delete

To delete a single resource, perform an HTTP DELETE by its case-sensitive identifier (`_id`) and accept a JSON response:

```http
DELETE /users/some-id HTTP/1.1
Host: example.com
Accept: application/json
```

## Parameters

You can use the following query string parameters:

| Parameter                  | Description                                                                                                                                                                                                                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_fields=field[,field...]` | Return only the specified fields in the body of the response.The `field` values are JSON pointers. For example, if the resource is `{"parent":{"child":"value"}}`, `parent/child` refers to the `"child":"value"`.If the `field` is left blank, the endpoint returns all default values. |
| `_prettyPrint=true`        | Format the body of the response.                                                                                                                                                                                                                                                         |

---

---
title: Event hooks
description: Create event hooks in Advanced Identity Cloud to trigger JavaScript scripts during lifecycle events on users, roles, and other identity objects
component: pingoneaic
page_id: pingoneaic:developer-docs:scripting-event-hooks
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/scripting-event-hooks.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Scripts", "Identities"]
page_aliases: ["release-notes:rapid-channel/event-hooks.adoc", "developer-docs:event-hooks.adoc"]
section_ids:
  create_a_new_event_hook: Create a new event hook
  scripting-tips: Scripting tips
  use_a_variable_in_an_event_hook_script: Use a variable in an event hook script
  use_an_esv_in_an_event_hook_script: Use an ESV in an event hook script
---

# Event hooks

|   |                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The topics on this page are for tenants created on or after January 12, 2023. Learn more in [Event hooks migration FAQ](../product-information/migration-dependent-features/event-hooks-migration-faq.html). |

*Event hooks* let you trigger scripts during various stages of the lifecycle of users, roles, assignments, organizations, groups\[[1](#_footnotedef_1 "View footnote.")], and applications.

You can trigger scripts when one of these [identity objects](../identities/identity-cloud-identity-schema.html) is created, updated, retrieved, deleted, validated, or stored in the repository. You can also trigger a script when a change to an identity object triggers an implicit synchronization operation.

Post-action scripts let you manipulate identity objects after they are created, updated, or deleted.

For some links to help with writing scripts for event hooks, and a few examples, learn more in [Scripting tips](#scripting-tips).

|   |                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Scripts can potentially emit the personally identifiable information (PII) of your end users into Advanced Identity Cloud logs, and then into external services that consume Advanced Identity Cloud logs.Ping Identity recommends that you establish a review and testing process for all scripts to prevent PII leaking out of your Advanced Identity Cloud tenant environments. |

## Create a new event hook

1. In the Advanced Identity Cloud admin console, go to *Realm* > Event Hooks.

2. On the Event Hooks page, click + New Event Hook.

3. On the New Event Hook page, enter event hook details:

   1. Enter the Name for the event hook.

   2. (Optional) Enter a Description for the event hook.

   3. Identify a condition that will trigger a script to run. In the Condition field:

      * Select an identity object type—​a user, role, assignment, organization, group, or application—​from the Object Name drop-down list.

      * Select an event type from the Event drop-down list.\
        Note that event types that have already been configured in event hooks do not appear in the drop-down list. Advanced Identity Cloud lets you configure exactly one event hook per condition.

   4. Specify a [script to run](#scripting-tips) when the event hook is triggered. Either:

      * Type JavaScript code into the Script field.

      * Or, click the Upload File toggle, and then click Browse. Then, select the file that contains the JavaScript code that will run when the event hook is triggered.

   5. (Optional) Enter variables to be passed to the event hook's script. Either:

      * Click + Add Variables, and then enter variable names and values in the Variables > Name and Variables > Value fields.

      * Or, click the JSON toggle, and then type JSON-formatted values into the Variables field.

4. Click Save.

## Scripting tips

The following links contain general information to help you write scripts triggered by event hooks:

* [Script triggers defined in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)*](../idm-scripting/script-triggers-managedConfig.html)

* [Functions available in identity-related scripts](../idm-scripting/scripting-func-engine.html)

* [The `identityServer` variable](../idm-scripting/script-variables-identity-server.html)

The sections that follow contain code snippets that might be helpful when you start developing your own event hook scripts.

### Use a variable in an event hook script

This example adds a prefix to a user's last name (`sn` attribute) in the user creation event hook.

1. Add a variable named `myCompany` to the event hook, and set its value to the desired prefix.

2. Specify a script similar to the following in the event hook:

   ```javascript
   object.sn = myCompany + "-" + object.sn;
   ```

### Use an ESV in an event hook script

This example sets the value of a user's `Description` attribute to the value of an ESV in the user creation event hook.

* Either specify the ESV in a variable:

  1. Add a variable named `myDescriptionESVValue` to the event hook.

  2. Set the variable's value to `&{esv.myDescription}`.

  3. Specify a script similar to the following in the event hook:

     ```javascript
     object.description = myDescriptionESVValue;
     ```

* Or, use the `identityServer` object to get the ESV value:

  ```javascript
  object.description = identityServer.getProperty("esv.myDescription")
  ```

***

[1](#_footnoteref_1). Event hooks are available for groups if you have enabled the groups feature in your Advanced Identity Cloud tenant.

---

---
title: HTTP status codes
description: Reference for HTTP status codes returned by Advanced Identity Cloud REST APIs, including 2xx, 3xx, 4xx, and 5xx codes
component: pingoneaic
page_id: pingoneaic:developer-docs:crest/status-codes
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/crest/status-codes.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# HTTP status codes

When working with a Advanced Identity Cloud REST API, client applications should expect at least the following HTTP status codes. Not all services necessarily return all status codes identified here:

* 200 OK

  The request succeeded and a resource returned, depending on the request.

* 201 Created

  The request succeeded and the resource was created.

* 204 No Content

  The action request succeeded, and there was no content to return.

* 304 Not Modified

  The read request included an `If-None-Match` header, and the value of the header matched the revision value of the resource.

* 400 Bad Request

  The request was malformed.

* 401 Unauthorized

  The request requires user authentication.

* 403 Forbidden

  Access was forbidden during an operation on a resource.

* 404 Not Found

  The specified resource could not be found, perhaps because it does not exist.

* 405 Method Not Allowed

  The HTTP method is not allowed for the requested resource.

* 406 Not Acceptable

  The request contains parameters that are not acceptable, such as a resource or protocol version that is not available.

* 409 Conflict

  The request would have resulted in a conflict with the current state of the resource.

* 410 Gone

  The requested resource is no longer available, and will not become available again. This can happen when resources expire.

* 412 Precondition Failed

  The resource's current version does not match the version provided.

* 415 Unsupported Media Type

  The request is in a format not supported by the requested resource for the requested method.

* 428 Precondition Required

  The resource requires a version, but no version was supplied in the request.

* 500 Internal Server Error

  The service encountered an unexpected condition that prevented it from fulfilling the request.

* 501 Not Implemented

  The resource does not support the functionality required to fulfill the request.

* 503 Service Unavailable

  The requested resource was temporarily unavailable. The service may be disabled, for example.

---

---
title: Patch
description: Use the Patch verb to modify part of an Advanced Identity Cloud REST API resource, with add, copy, remove, replace, and other operations
component: pingoneaic
page_id: pingoneaic:developer-docs:crest/patch
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/crest/patch.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  crest-patch-add: Add operation
  crest-patch-copy: Copy operation
  crest-patch-increment: Increment operation
  crest-patch-move: Move operation
  crest-patch-remove: Remove operation
  crest-patch-replace: Replace operation
  crest-patch-transform: Transform operation
  crest-patch-limitations: Limitations
  parameters: Parameters
---

# Patch

To patch a resource, send an HTTP PATCH request with an array of operation objects in the payload. Each operation object uses some combination of these fields:

* `operation`

  The type of operation.

* `field`

  The target field.

* `value`

  The value to apply.

* `from`

  The source field.

The service applies the PATCH operations in order.

```http
PATCH /users/some-id HTTP/1.1
Host: example.com
Accept: application/json
Content-Length: ...
Content-Type: application/json
If-Match: _rev
{ JSON array of patch operations }
```

PATCH operations work differently depending on the field types:

* Single-value

  An object, string, boolean, or number.

* List semantics array

  The elements are ordered, and duplicates are allowed.

* Set semantics array

  The elements are not ordered, and duplicates are not allowed.

Whether an endpoint supports a specific `operation` depends on the implementation.

## Add operation

The `add` operation ensures the target field contains the value provided, creating parent fields as necessary.

If the target field is single-valued, the value replaces the value of the target.

If the value is an array, the outcome depends on the type:

* List semantics arrays

  If you `add` an array of values, the operation appends the array to the existing list of values.

  If you `add` a single value, specify an ordinal element in the target array, or use the `{-}` special index to add the value to the end of the list.

* Set semantics arrays

  The operation merges the value(s) in the patch with the existing set of values. Any duplicates in the array are removed.

As an example, start with the following list semantic array resource:

```json
{
  "fruits": ["orange", "apple"]
}
```

The following `add` operation appends `pineapple` at the end of the array:

```json
{
  "operation": "add",
  "field": "/fruits/-",
  "value": "pineapple"
}
```

The resulting resource is:

```json
{
  "fruits": ["orange", "apple", "pineapple"]
}
```

## Copy operation

The `copy` operation replaces the value(s) of the target field with the value(s) from the source field.

The following example replaces the value of `another_mail` with the value of `mail`:

```json
[{
  "operation": "copy",
  "from": "mail",
  "field": "another_mail"
}]
```

If the source field value and the target field value are arrays, the result depends on whether the array has list semantics or set semantics. Learn more in [Add operation](#crest-patch-add).

## Increment operation

The `increment` operation changes the value or values of the target field by the amount you specify. The value must be a positive or negative number. The target must be a single-valued number.

The following example adds `1000` to `/user/payment`:

```json
[{
  "operation": "increment",
  "field": "/user/payment",
  "value": "1000"
}]
```

## Move operation

The `move` operation removes existing values from the source and adds them to the target field. The operation creates the target field if it does not exist.

The following example moves `surname` values to `lastName`:

```json
[{
  "operation": "move",
  "from": "surname",
  "field": "lastName"
}]
```

To apply a `move` to an array, the source and target must have compatible semantics. Learn more in [Add operation](#crest-patch-add).

## Remove operation

The `remove` operation deletes values in the target field.

When no value is specified, the operation removes the field:

```json
[{
  "operation": "remove",
  "field": "phoneNumber"
}]
```

For arrays, the result depends on the semantics:

* List semantic arrays

  Delete the specified element in the array.

  The following example removes the first phone number (zero-based array index):

  ```json
  [{
    "operation": "remove",
    "field": "/phoneNumber/0"
  }]
  ```

* Set semantic arrays

  Delete the specified values from the array.

  The following example removes the specified phone number:

  ```json
  [{
    "operation": "remove",
    "field": "/phoneNumber",
    "value": "+1 408 555 9999"
  }]
  ```

## Replace operation

The `replace` operation removes existing values in the target, replacing them with the provided value(s).

The following example replaces existing `telephoneNumber` values with `+1 408 555 9999`:

```json
[{
  "operation": "replace",
  "field": "/telephoneNumber",
  "value": "+1 408 555 9999"
}]
```

For list semantic arrays, you can target items by their indexes. As an example, start with the following resource:

```json
{
  "fruits": ["apple", "orange", "kiwi", "lime"]
}
```

Apply the following operation:

```json
[{
  "operation": "replace",
  "field": "/fruits/1",
  "value": "pineapple"
}]
```

The result is:

```json
{
  "fruits": ["apple", "pineapple", "kiwi", "lime"]
}
```

## Transform operation

The `transform` operation changes the field value based on a script or a data transformation command.

The following example applies the `something.js` script to the `/objects` value:

```json
[{
  "operation": "transform",
  "field": "/objects",
  "value": {
    "script": {
      "type": "text/javascript",
      "file": "something.js"
    }
  }
}]
```

## Limitations

Some HTTP client libraries do not support the HTTP PATCH operation.

Make sure the library you use supports HTTP PATCH before using this REST operation. For example, the Java method `HttpURLConnection.setRequestMethod("PATCH")` throws `ProtocolException`.

## Parameters

You can use the following query string parameters:

| Parameter                  | Description                                                                                                                                                                                                                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_fields=field[,field...]` | Return only the specified fields in the body of the response.The `field` values are JSON pointers. For example, if the resource is `{"parent":{"child":"value"}}`, `parent/child` refers to the `"child":"value"`.If the `field` is left blank, the endpoint returns all default values. |
| `_prettyPrint=true`        | Format the body of the response.                                                                                                                                                                                                                                                         |

---

---
title: Query
description: Use the Query verb to search Advanced Identity Cloud REST API resource collections using filter expressions, paging, and sort keys
component: pingoneaic
page_id: pingoneaic:developer-docs:crest/query
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/crest/query.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  parameters: Parameters
  crest-query-queryFilter: Filter expressions
---

# Query

To query a resource collection, which you can think of as a resource container, perform an HTTP GET and accept a JSON response including at least a `_queryFilter` or `_queryId` parameter. These parameters cannot be used together.

```http
GET /users?_queryFilter=true HTTP/1.1
Host: example.com
Accept: application/json
```

The endpoint returns the result as a JSON object including a `results` array and other fields related to the query string parameters.

## Parameters

You can use the following query string parameters:

| Parameter                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_fields=field[,field...]`                   | Return only the specified fields in each element of the `results`.The `field` values are JSON pointers. For example, if the resource is `{"parent":{"child":"value"}}`, `parent/child` refers to the `"child":"value"`.If the `field` is left blank, the endpoint returns all default values.                                                                                                                                                                                                                                                                                                                                                                                          |
| `_pagedResultsCookie=string`                 | The string is an opaque cookie to keep track of the position in the search results. The service returns the cookie in the JSON response as the value of `pagedResultsCookie`.In the request `_pageSize` must be set and non-zero. You receive the cookie value from the provider on the first request. You supply the cookie value in subsequent requests until the service returns a `null` cookie when the final page of results has been returned.Use this parameter with the `_queryFilter` parameter. It is not guaranteed to work with the `_queryId` parameter.The `_pagedResultsCookie` and `_pagedResultsOffset` parameters are mutually exclusive. Do not use them together. |
| `_pagedResultsOffset=integer`                | When `_pageSize` is non-zero, use this as an index in the result set indicating the first page to return.The `_pagedResultsCookie` and `_pagedResultsOffset` parameters are mutually exclusive. Do not use them together.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `_pageSize=integer`                          | Return query results in pages of this size.After the initial request, use `_pagedResultsCookie` or `_pageResultsOffset` to page through the results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `_prettyPrint=true`                          | Format the body of the response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `_queryFilter=filter-expression`             | Query filters request entries matching the filter expression. You must URL-escape the filter expression.Learn more in [Filter expressions](#crest-query-queryFilter).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `_queryId=identifier`                        | Specify a query by its identifier.Specific queries can take their own query string parameter arguments depending on the implementation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `_sortKeys=[-][.var]##field##[,[-]field...]` | Sort the resources returned based on the specified field(s) in `+` (ascending, default) or in `-` (descending) order.As ascending order is the default, including the `` ` character in the query is unnecessary. If you do include the ` ``, it must be URL-encoded as `%2B`:```none
https://<tenant-env-fqdn>/api/users?_prettyPrint=true&_queryFilter=true&_sortKeys=%2Bname/givenName
```The `_sortKeys` parameter is not supported for predefined queries (`_queryId`).                                                                                                                                                                                                           |
| `_totalPagedResultsPolicy=string`            | When a non-zero `_pageSize` is specified, the service calculates the `totalPagedResults` in accordance with the `totalPagedResultsPolicy`, and provides the value as part of the response.The `totalPagedResults` is:- An estimate of the total number of paged results (`_totalPagedResultsPolicy=ESTIMATE`).

- The exact total result count (`_totalPagedResultsPolicy=EXACT`).If no count policy is specified in the query, or if `_totalPagedResultsPolicy=NONE`, result counting is disabled. The service returns `"totalPagedResults": -1`.                                                                                                                                     |

## Filter expressions

Query filters request entries matching the filter expression. You must URL-escape the filter expression.

The string representation is summarized as follows:

```none
Expr           = OrExpr
OrExpr         = AndExpr ( 'or' AndExpr ) *
AndExpr        = NotExpr ( 'and' NotExpr ) *
NotExpr        = '!' PrimaryExpr | PrimaryExpr
PrimaryExpr    = '(' Expr ')' | ComparisonExpr | PresenceExpr | LiteralExpr
ComparisonExpr = Pointer OpName JsonValue
PresenceExpr   = Pointer 'pr'
LiteralExpr    = 'true' | 'false'
Pointer        = JSON pointer
OpName         = 'eq' |  # equal to
                 'co' |  # contains
                 'sw' |  # starts with
                 'lt' |  # less than
                 'le' |  # less than or equal to
                 'gt' |  # greater than
                 'ge' |  # greater than or equal to
                 STRING  # extended operator
JsonValue      = NUMBER | BOOLEAN | '"' UTF8STRING '"'
STRING         = ASCII string not containing white-space
UTF8STRING     = UTF-8 string possibly containing white-space
```

JsonValue components of filter expressions follow [RFC 7159: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc7159.html). In particular, as described in section 7 of the RFC, the escape character in strings is the backslash character. For example, to match the identifier `test\`, use `_id eq 'test\\'`. In the JSON resource, the `\` is escaped the same way: `"_id":"test\\"`.

When using a query filter in a URL, notice the filter expression is part of a query string parameter. URL-encoded the filter expression. Learn more in [RFC 3986: Uniform Resource Identifier (URI): Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986.html). For example, whitespace, double quotes (`"`), parentheses, and exclamation characters need URL encoding. The following rules apply to URL query components:

```none
query       = *( pchar / "/" / "?" )
pchar       = unreserved / pct-encoded / sub-delims / ":" / "@"
unreserved  = ALPHA / DIGIT / "-" / "." / "_" / "~"
pct-encoded = "%" HEXDIG HEXDIG
sub-delims  = "!" / "$" / "&" / "'" / "(" / ")"
                  / "*" / "+" / "," / ";" / "="
```

`ALPHA`, `DIGIT`, and `HEXDIG` are core rules of [RFC 5234: Augmented BNF for Syntax Specifications](https://www.rfc-editor.org/rfc/rfc5234.html):

```none
ALPHA       =  %x41-5A / %x61-7A   ; A-Z / a-z
DIGIT       =  %x30-39             ; 0-9
HEXDIG      =  DIGIT / "A" / "B" / "C" / "D" / "E" / "F"
```

As a result, a backslash escape character in a JsonValue component is percent-encoded in the URL query string parameter as `%5C`. To encode the query filter expression `_id eq 'test\\'`, use `_id+eq'test%5C%5C'+`, for example.

A simple filter expression can represent a comparison, presence, or a literal value.

For comparison expressions use json-pointer comparator json-value, where the comparator is one of the following:

`eq` (equals)\
`co` (contains)\
`sw` (starts with)\
`lt` (less than)\
`le` (less than or equal to)\
`gt` (greater than)\
`ge` (greater than or equal to)

For presence, use json-pointer pr to match resources where:

* The JSON pointer is present.

* The value it points to is not `null`.

Literal values include true (match anything) and false (match nothing).

Complex expressions employ `and`, `or`, and `!` (not), with parentheses, `(expression)`, to group expressions.

---

---
title: Read
description: Use the Read verb to retrieve a single resource from the Advanced Identity Cloud REST API using HTTP GET
component: pingoneaic
page_id: pingoneaic:developer-docs:crest/read
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/crest/read.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  parameters: Parameters
---

# Read

To retrieve a single resource, perform an HTTP GET on the resource by its case-sensitive identifier (`_id`) and accept a JSON response:

```http
GET /users/some-id HTTP/1.1
Host: example.com
Accept: application/json
```

## Parameters

You can use the following query string parameters:

| Parameter                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `_fields=field[,field...]` | Return only the specified fields in the body of the response.The `field` values are JSON pointers. For example, if the resource is `{"parent":{"child":"value"}}`, `parent/child` refers to the `"child":"value"`.If the `field` is left blank, the endpoint returns all default values.                                                                                                                                                                                 |
| `_mimeType=mime-type`      | Some resources have fields containing multimedia resources, such as a profile photo.If the feature is enabled for the endpoint, read a single multimedia resource field by specifying the field and mime-type.The content type of the field value returned matches the mime-type. The body of the response is the multimedia resourceDo not use the `Accept` header. For example, `Accept: image/png` does not work. Use the `_mimeType` query string parameter instead. |
| `_prettyPrint=true`        | Format the body of the response.                                                                                                                                                                                                                                                                                                                                                                                                                                         |

---

---
title: Scripting
description: Overview of scripting options in Advanced Identity Cloud including auth scripting, custom endpoints, and event hooks
component: pingoneaic
page_id: pingoneaic:developer-docs:scripting
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/scripting.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Scripts"]
---

# Scripting

You can extend Advanced Identity Cloud features with JavaScript.

[icon: sign-in-alt, set=fas, size=3x]

#### [Auth scripting](scripting-auth.html)

[icon: wrench, set=fas, size=3x]

#### [Custom endpoints](scripting-custom-endpoints.html)

[icon: handshake, set=fas, size=3x]

#### [Event hooks](event-hooks.html)

---

---
title: Update
description: Use the Update verb to replace an existing Advanced Identity Cloud REST API resource using HTTP PUT with revision control
component: pingoneaic
page_id: pingoneaic:developer-docs:crest/update
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/crest/update.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Update

To update a resource, perform an HTTP PUT including the case-sensitive identifier (`_id`) as the final element of the path to the resource and the JSON resource as the payload.

Use the `If-Match: _rev` header to verify the version you modify. Use `If-Match: *` if the version does not matter.

```http
PUT /users/some-id HTTP/1.1
Host: example.com
Accept: application/json
Content-Length: ...
Content-Type: application/json
If-Match: _rev
{ JSON resource }
```

When updating a resource, include all the attributes to retain. Omitting an attribute in the resource amounts to deleting it unless it is not under the control of your application. Attributes not under the control of your application include private and read-only attributes. Virtual attributes and relationship references might not be under the control of your application.

| Parameter                  | Description                                                                                                                                                                                                                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_fields=field[,field...]` | Return only the specified fields in the body of the response.The `field` values are JSON pointers. For example, if the resource is `{"parent":{"child":"value"}}`, `parent/child` refers to the `"child":"value"`.If the `field` is left blank, the endpoint returns all default values. |
| `_prettyPrint=true`        | Format the body of the response.                                                                                                                                                                                                                                                         |