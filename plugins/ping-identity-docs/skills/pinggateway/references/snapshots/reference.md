---
title: About Common REST
description: "Reference for the Common REST API framework: CRUDPAQ verbs, query parameters, pagination, PATCH operations, and HTTP status codes"
component: pinggateway
version: 2026
page_id: pinggateway:reference:AboutCrest
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/AboutCrest.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-08-14T11:14:52Z
section_ids:
  about-crest-resources: Common REST resources
  about-crest-verbs: Common REST verbs
  about-crest-parameters: Common REST parameters
  about-crest-extensions: Common REST extension points
  crest-accept-api-version: Common REST headers
  accept_api_version: Accept-API-Version
  x_forgerock_transactionid: X-ForgeRock-TransactionId
  about-crest-api-descriptors: Common REST API documentation
  about-crest-create: Create
  about-crest-read: Read
  about-crest-update: Update
  about-crest-delete: Delete
  about-crest-patch: Patch
  crest-patch-add: "Patch operation: add"
  crest-patch-copy: "Patch operation: copy"
  crest-patch-increment: "Patch operation: increment"
  crest-patch-move: "Patch operation: move"
  crest-patch-remove: "Patch operation: remove"
  crest-patch-replace: "Patch operation: replace"
  crest-patch-transform: "Patch operation: transform"
  crest-patch-limitations: Patch operation limitations
  about-crest-action: Action
  about-crest-query: Query
  about-crest-response-codes: HTTP status codes
---

# About Common REST

Common REST is a common REST API framework. It provides Ping Identity Platform software common ways to access web resources and collections of resources. Adapt the examples in this section to your resources and deployment.

|   |                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This page describes the full Common REST framework. Some platform component products do not implement all Common REST behaviors exactly as described. For details, refer to the product-specific examples and reference information. |

## Common REST resources

Servers generally return JSON-format resources, though resource formats can depend on the implementation.

Resources in collections can be found by their unique identifiers (IDs). IDs are exposed in the resource URIs. For example, if a server has a user collection under `/users`, then you can access a user at `/users/user-id`. The ID is also the value of the `_id` field of the resource.

Resources are versioned using revision numbers. A revision is specified in the resource's `_rev` field. Revisions make it possible to figure out whether to apply changes without resource locking and without distributed transactions.

## Common REST verbs

The Common REST APIs use the following verbs, sometimes referred to collectively as `CRUDPAQ`. For details and HTTP-based examples of each, follow the links to the sections for each verb.

* Create

  Add a new resource.

  This verb maps to HTTP PUT or HTTP POST.

  For details, see [Create](#about-crest-create).

* Read

  Retrieve a single resource.

  This verb maps to HTTP GET.

  For details, see [Read](#about-crest-read).

* Update

  Replace an existing resource.

  This verb maps to HTTP PUT.

  For details, see [Update](#about-crest-update).

* Delete

  Remove an existing resource.

  This verb maps to HTTP DELETE.

  For details, see [Delete](#about-crest-delete).

* Patch

  Modify part of an existing resource.

  This verb maps to HTTP PATCH.

  For details, see [Patch](#about-crest-patch).

* Action

  Perform a predefined action.

  This verb maps to HTTP POST.

  For details, see [Action](#about-crest-action).

* Query

  Search a collection of resources.

  This verb maps to HTTP GET.

  For details, see [Query](#about-crest-query).

## Common REST parameters

Common REST reserved query string parameter names start with an underscore, `_`. Reserved query string parameters include, but are not limited to, the following names:

* `_action`

* `_api`

* `_crestapi`

* `_fields`

* `_mimeType`

* `_pageSize`

* `_pagedResultsCookie`

* `_pagedResultsOffset`

* `_prettyPrint`

* `_queryExpression`

* `_queryFilter`

* `_queryId`

* `_sortKeys`

* `_totalPagedResultsPolicy`

|   |                                                                                           |
| - | ----------------------------------------------------------------------------------------- |
|   | Some parameter values are not safe for URLs, so URL-encode parameter values as necessary. |

Continue reading for details about how to use each parameter.

## Common REST extension points

The *action* verb is the main vehicle for extensions. For example, to create a new user with HTTP POST rather than HTTP PUT, you might use `/users?_action=create`. A server can define additional actions. For example, `/tasks/1?_action=cancel`.

A server can define *stored queries* to call by ID. For example, `/groups?_queryId=hasDeletedMembers`. Stored queries can call for additional parameters. The parameters are also passed in the query string. Which parameters are valid depends on the stored query.

## Common REST headers

### Accept-API-Version

Common REST APIs use the `Accept-API-Version` header to specify protocol and resource versions:

Accept-API-Version: protocol=*version*,resource=*version*

* `protocol`

  The version reflects changes in the Common REST protocol, such as common method parameters and headers specified by the protocol itself, or the input or response conventions it prescribes.

  For example, protocol version 2.2 introduced the `_countOnly` parameter.

* `resource`

  The version reflects changes in the resource implementation, including JSON representation of resources, input parameters required, and incompatible behavior changes.

  For example, the version changes when `errorMessage` changes to `message` in a JSON response.

Whether this header is required depends on the product and API you make the request to.

### X-ForgeRock-TransactionId

Common REST APIs use the `X-ForgeRock-TransactionId` header to track related requests through Ping Identity Platform.

X-ForgeRock-TransactionId: *transactionID*

The *transactionID* consists of a unique identifier for the transaction optionally followed by a sequence number for the individual request.

This header is optional. In self-managed deployments, you configure products to trust transaction IDs and let them propagate for audit purposes.

## Common REST API documentation

Common REST APIs often depend at least in part on runtime configuration. Many Common REST endpoints therefore serve *API descriptors* at runtime. An API descriptor documents the actual API as it is configured.

Use the following query string parameters to retrieve API descriptors:

* `_api`

  Serves an API descriptor that complies with the [OpenAPI specification](https://github.com/OAI/OpenAPI-Specification).

  This API descriptor represents the API accessible over HTTP. It is suitable for use with popular tools such as [Swagger UI](http://swagger.io/swagger-ui/).

* `_crestapi`

  Serves a native Common REST API descriptor.

  This API descriptor provides a compact representation that is not dependent on the transport protocol. It requires a client that understands Common REST, as it omits many Common REST defaults.

|   |                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Consider limiting access to API descriptors in production environments in order to avoid unnecessary traffic.To provide documentation in production environments, see [To publish OpenAPI documentation](#use-openapi-descriptors) instead. |

To publish OpenAPI documentation

In production systems, developers expect stable, well-documented APIs. Rather than retrieving API descriptors at runtime through Common REST, prepare final versions, and publish them alongside the software in production.

Use the OpenAPI-compliant descriptors to provide API reference documentation for your developers:

1. Configure the software to produce production-ready APIs.

   In other words, configure the software as for production so that the APIs match exactly.

2. Retrieve the OpenAPI-compliant descriptor.

   The following command saves the descriptor to a file. :

   ```
   $ curl -o <filename>.json <endpoint>?_api
   ```

   |   |                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The *endpoint* must be a valid endpoint. For example:```
   $ curl -o myapi.json https://am.example.com:8443/am/json/realms/root/authenticate?_api
   ``` |

3. If necessary, edit the descriptor.

   For example, add security definitions to describe the API protection.

4. Publish the descriptor using a tool such as [Swagger UI](https://github.com/swagger-api/swagger-ui).

## Create

There are two ways to create a resource, HTTP POST or HTTP PUT.

To create a resource using POST, perform an HTTP POST with the query string parameter `_action=create`, and the JSON resource as a payload. Accept a JSON response. The server creates the identifier if not specified:

```http
POST /users?_action=create HTTP/1.1
Host: example.com
Accept: application/json
Content-Length: ...
Content-Type: application/json
{ JSON resource }
```

To create a resource using PUT, perform an HTTP PUT including the case-sensitive identifier for the resource in the URL path, and the JSON resource as a payload. Use the `If-None-Match: *` header. Accept a JSON response:

```http
PUT /users/some-id HTTP/1.1
Host: example.com
Accept: application/json
Content-Length: ...
Content-Type: application/json
If-None-Match: *
{ JSON resource }
```

The `_id` and content of the resource depend on the server implementation. The server is not required to use the `_id` that the client provides. The server response to the request indicates the resource location as the value of the `Location` header.

If you include the `If-None-Match` header, you must use `If-None-Match: *`. In this case, the request creates the object if it does not exist, and fails if the object does exist. If you include any value other `If-None-Match: *`, the server returns an HTTP 400 Bad Request error. For example, creating an object with `If-None-Match: revision` returns a bad request error.

If you do not include `If-None-Match: *`, the request creates the object if it does not exist, and *updates* the object if it does exist.

Parameters

* `_fields=field[,field…​]`

  Return only the specified fields in the body of the response.

  The `field` values are JSON pointers. For example if the resource is `{"parent":{"child":"value"}}`, `parent/child` refers to the `"child":"value"`.

  If the `field` is left blank, the server returns all default values.

* `_prettyPrint=true`

  Format the body of the response.

## Read

To retrieve a single resource, perform an HTTP GET on the resource by its case-sensitive identifier (`_id`), and accept a JSON response:

```http
GET /users/some-id HTTP/1.1
Host: example.com
Accept: application/json
```

Parameters

* `_fields=field[,field…​]`

  Return only the specified fields in the body of the response.

  The `field` values are JSON pointers. For example if the resource is `{"parent":{"child":"value"}}`, `parent/child` refers to the `"child":"value"`.

  If the `field` is left blank, the server returns all default values.

* `_mimeType=mime-type`

  Some resources have fields whose values are multi-media resources, such as a profile photo.

  If the feature is enabled for the endpoint, you can read a single field that is a multi-media resource by specifying the *field* and *mime-type*.

  In this case, the content type of the field value returned matches the *mime-type* that you specify, and the body of the response is the multi-media resource.

  Do not use the `Accept` header in this case. For example, `Accept: image/png` does not work. Use the `_mimeType` query string parameter instead.

* `_prettyPrint=true`

  Format the body of the response.

## Update

To update a resource, perform an HTTP PUT including the case-sensitive identifier (`_id`) as the final element of the path to the resource, and the JSON resource as the payload. Use the `If-Match: _rev` header to check that you are actually updating the version you modified. Use `If-Match: *` if the version does not matter. Accept a JSON response:

```http
PUT /users/some-id HTTP/1.1
Host: example.com
Accept: application/json
Content-Length: ...
Content-Type: application/json
If-Match: _rev
{ JSON resource }
```

When updating a resource, include all the attributes to retain. Omitting an attribute in the resource amounts to deleting the attribute unless it is not under the control of your application. Attributes not under the control of your application include private and read-only attributes. In addition, virtual attributes and relationship references might not be under the control of your application.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Product-specific implementations may differ. Not all products use the payload to replace the state of the resource in its entirety. For example, attributes that are omitted from the request payload to AM will not be deleted. Instead, you need to specify the attribute and set the value to an empty array to delete the attribute from the resource.For more information, see the product-specific examples and reference information. |

Parameters

* `_fields=field[,field…​]`

  Return only the specified fields in the body of the response.

  The `field` values are JSON pointers. For example if the resource is `{"parent":{"child":"value"}}`, `parent/child` refers to the `"child":"value"`.

  If the `field` is left blank, the server returns all default values.

* `_prettyPrint=true`

  Format the body of the response.

## Delete

To delete a single resource, perform an HTTP DELETE by its case-sensitive identifier (`\_id`) and accept a JSON response:

```http
DELETE /users/some-id HTTP/1.1
Host: example.com
Accept: application/json
```

Parameters

* `_fields=field[,field…​]`

  Return only the specified fields in the body of the response.

  The `field` values are JSON pointers. For example if the resource is `{"parent":{"child":"value"}}`, `parent/child` refers to the `"child":"value"`.

  If the `field` is left blank, the server returns all default values.

* `_prettyPrint=true`

  Format the body of the response.

## Patch

To patch a resource, send an HTTP PATCH request with the following parameters:

* `operation`

* `field`

* `value`

* `from` (optional with copy and move operations)

You can include these parameters in the payload for a PATCH request, or in a JSON PATCH file. If successful, you'll see a JSON response similar to the following:

```http
PATCH /users/some-id HTTP/1.1
Host: example.com
Accept: application/json
Content-Length: ...
Content-Type: application/json
If-Match: _rev
{ JSON array of patch operations }
```

PATCH operations apply to three types of targets:

* **single-valued**, such as an object, string, boolean, or number.

* **list semantics array**, where the elements are ordered, and duplicates are allowed.

* **set semantics array**, where the elements are not ordered, and duplicates are not allowed.

Common REST PATCH supports multiple `operations`:

### Patch operation: add

The `add` operation ensures that the target field contains the value provided, creating parent fields as necessary.

If the target field is single-valued, then the value you include in the PATCH replaces the value of the target. A single-valued field is an `object`, `string`, `boolean`, or `number`.

An `add` operation has different results on two standard types of arrays:

* **List semantic arrays**: you can run any of these `add` operations on that type of array:

  * If you `add` an array of values, the PATCH operation appends it to the existing list of values.

  * If you `add` a single value, specify an ordinal element in the target array, or use the `{-}` special index to add that value to the end of the list.

* **Set semantic arrays**: The value included in the patch is merged with the existing set of values. Any duplicates within the array are removed.

As an example, start with the following list semantic array resource:

```javascript
{
    "fruits" : [ "orange", "apple" ]
}
```

The following add operation includes the pineapple to the end of the list of fruits, as indicated by the `-` at the end of the `fruits` array.

```javascript
{
    "operation" : "add",
    "field" : "/fruits/-",
    "value" : "pineapple"
}
```

The following is the resulting resource:

```javascript
{
    "fruits" : [ "orange", "apple", "pineapple" ]
}
```

You can add only one array element one at a time, as per the corresponding [JSON Patch specification](https://www.rfc-editor.org/rfc/rfc6902.html#appendix-A.16). If you add an array of elements, for example:

```javascript
{
    "operation" : "add",
    "field" : "/fruits/-",
    "value" : ["pineapple", "mango"]
}
```

The resulting resource would have the following invalid JSON structure:

```javascript
{
    "fruits" : [ "orange", "apple", ["pineapple", "mango"]]
}
```

### Patch operation: copy

The copy operation takes one or more existing values from the source field. It then adds those same values on the target field. Once the values are known, it is equivalent to performing an `add` operation on the target field.

The following `copy` operation takes the value from a field named `mail`, and then runs a `replace` operation on the target field, `another_mail`.

```javascript
[
  {
     "operation":"copy",
     "from":"mail",
     "field":"another_mail"
  }
]
```

If the source and target field values are arrays, the result depends on whether the array has list semantics or set semantics, as described in [Patch operation: add](#crest-patch-add).

### Patch operation: increment

The `increment` operation changes the value or values of the target field by the amount you specify. The value that you include must be one number, and may be positive or negative. The value of the target field must accept numbers. The following `increment` operation adds `1000` to the target value of `/user/payment`.

```javascript
[
  {
    "operation" : "increment",
    "field" : "/user/payment",
    "value" : "1000"
  }
]
```

Since the `value` of the `increment` is a single number, arrays do not apply.

### Patch operation: move

The move operation removes existing values on the source field. It then adds those same values on the target field. This is equivalent to a `remove` operation on the source, followed by an `add` operation with the same values, on the target.

The following `move` operation is equivalent to a `remove` operation on the source field, `surname`, followed by a `replace` operation on the target field value, `lastName`. If the target field does not exist, it is created:

```javascript
[
  {
     "operation":"move",
     "from":"surname",
     "field":"lastName"
  }
]
```

To apply a `move` operation on an array, you need a compatible single-value, list semantic array, or set semantic array on both the source and the target. For details, see the criteria described in [Patch operation: add](#crest-patch-add).

### Patch operation: remove

The `remove` operation ensures that the target field no longer contains the value provided. If the remove operation does not include a value, the operation removes the field. The following `remove` deletes the value of the `phoneNumber`, along with the field.

```javascript
[
  {
    "operation" : "remove",
    "field" : "phoneNumber"
  }
]
```

If the object has more than one `phoneNumber`, those values are stored as an array.

A `remove` operation has different results on two standard types of arrays:

* **List semantic arrays**: A `remove` operation deletes the specified element in the array. For example, the following operation removes the first phone number, based on its array index (zero-based):

  ```javascript
  [
     {
        "operation" : "remove",
        "field" : "/phoneNumber/0"
     }
  ]
  ```

* **Set semantic arrays**: The list of values included in a patch are removed from the existing array.

### Patch operation: replace

The `replace` operation removes any existing value(s) of the targeted field, and replaces them with the provided value(s). It is essentially equivalent to a `remove` followed by a `add` operation. If the arrays are used, the criteria is based on [Patch operation: add](#crest-patch-add). However, indexed updates are not allowed, even when the target is an array.

The following `replace` operation removes the existing `telephoneNumber` value for the user, and then adds the new value of `+1 408 555 9999`.

```javascript
[
  {
    "operation" : "replace",
    "field" : "/telephoneNumber",
    "value" : "+1 408 555 9999"
  }
]
```

A PATCH replace operation on a list semantic array works as a PATCH remove operation. The following example demonstrates how the effect of both operations. Start with the following resource:

```javascript
{
    "fruits" : [ "apple", "orange", "kiwi", "lime" ],
}
```

Apply the following operations on that resource:

```javascript
[
  {
    "operation" : "remove",
    "field" : "/fruits/0",
    "value" : ""
  },
  {
    "operation" : "replace",
    "field" : "/fruits/1",
    "value" : "pineapple"
  }
]
```

The PATCH operations are applied sequentially. The `remove` operation removes the first member of that resource, based on its array index, (`fruits/0`), with the following result:

```javascript
[
  {
    "fruits" : [ "orange", "kiwi", "lime" ],
  }
]
```

The second PATCH operation, a `replace`, is applied on the second member (`fruits/1`) of the intermediate resource, with the following result:

```none
[
  {
    "fruits" : [ "orange", "pineapple", "lime" ],
  }
]
```

### Patch operation: transform

The `transform` operation changes the value of a field based on a script, or some other data transformation command. The following `transform` operation takes the value from the field named `/objects`, and applies the `something.js` script as shown:

```javascript
[
  {
    "operation" : "transform",
    "field" : "/objects",
    "value" : {
      "script" : {
        "type" : "text/javascript",
        "file" : "something.js"
      }
    }
  }
]
```

### Patch operation limitations

Some HTTP client libraries do not support the HTTP PATCH operation. Make sure that the library you use supports HTTP PATCH before using this REST operation.

For example, the Java Development Kit HTTP client does not support PATCH as a valid HTTP method. Instead, the method `HttpURLConnection.setRequestMethod("PATCH")` throws `ProtocolException`.

Parameters

* `_fields=field[,field…​]`

  Return only the specified fields in the body of the response.

  The `field` values are JSON pointers. For example if the resource is `{"parent":{"child":"value"}}`, `parent/child` refers to the `"child":"value"`.

  If the `field` is left blank, the server returns all default values.

* `_prettyPrint=true`

  Format the body of the response.

## Action

Actions are a means of extending Common REST APIs and are defined by the resource provider, so the actions you can use depend on the implementation.

The standard action indicated by `_action=create` is described in [Create](#about-crest-create).

Parameters

In addition to these parameters, specific action implementations have their own parameters:

* `_fields=field[,field…​]`

  Return only the specified fields in the body of the response.

  The `field` values are JSON pointers. For example if the resource is `{"parent":{"child":"value"}}`, `parent/child` refers to the `"child":"value"`.

  If the `field` is left blank, the server returns all default values.

* `_prettyPrint=true`

  Format the body of the response.

## Query

To query a resource collection (or resource container), perform an HTTP GET, and accept a JSON response, including either a `_queryExpression`, `_queryFilter`, or `_queryId` parameter. The parameters cannot be used together:

```http
GET /users?_queryFilter=true HTTP/1.1
Host: example.com
Accept: application/json
```

The server returns the result as a JSON object including a `"results"` array, and other fields that depend on the parameters.

Parameters

* `_countOnly=true`

  Return a count of query results without returning the resources.

  This parameter requires protocol version 2.2 or later.

* `_fields=field[,field…​]`

  Return only the specified fields in the body of the response.

  The `field` values are JSON pointers. For example if the resource is `{"parent":{"child":"value"}}`, `parent/child` refers to the `"child":"value"`.

  If the `field` is left blank, the server returns all default values.

* `_queryFilter=filter-expression`

  Query filters request that the server return entries that match the filter expression. You must URL-escape the filter expression.

  The string representation is summarized as follows. Continue reading for additional explanation:

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

  *JsonValue* components of filter expressions follow [RFC 7159: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc7159.html). In particular, as described in section 7 of the RFC, the escape character in strings is the backslash character. For example, to match the identifier `test\`, use `_id eq 'test\\'`. In the JSON resource, the `\` is escaped the same way: `"_id":"test\\"`.

  When using a query filter in a URL, the filter expression is part of a query string parameter. A query string parameter must be URL encoded, as described in [RFC 3986: Uniform Resource Identifier (URI): Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986.html). For example, white space, double quotes (`"`), parentheses, and exclamation characters must be URL encoded in HTTP query strings. The following rules apply to URL query components:

  ```none
  query       = *( pchar / "/" / "?" )
  pchar       = unreserved / pct-encoded / sub-delims / ":" / "@"
  unreserved  = ALPHA / DIGIT / "-" / "." / "_" / "~"
  pct-encoded = "%" HEXDIG HEXDIG
  sub-delims  = "!" / "$" / "&amp;" / "'" / "(" / ")"
                    / "*" / "+" / "," / ";" / "="
  ```

  `ALPHA`, `DIGIT`, and `HEXDIG` are core rules of [RFC 5234: Augmented BNF for Syntax Specifications](https://www.rfc-editor.org/rfc/rfc5234.html):

  ```none
  ALPHA       =  %x41-5A / %x61-7A   ; A-Z / a-z
  DIGIT       =  %x30-39             ; 0-9
  HEXDIG      =  DIGIT / "A" / "B" / "C" / "D" / "E" / "F"
  ```

  As a result, a backslash escape character in a *JsonValue* component is percent-encoded in the URL query string parameter as `%5C`. To encode the query filter expression `_id eq 'test\\'`, use `_id+eq+'test%5C%5C'`, for example.

  A simple filter expression can represent a comparison, presence, or a literal value.

  For comparison expressions, use `json-pointer comparator json-value`, where the *comparator* is one of the following:

  ```none
  eq (equals)
  co (contains)
  sw (starts with)
  lt (less than)
  le (less than or equal to)
  gt (greater than)
  ge (greater than or equal to)
  ```

  For presence, use `json-pointer pr` to match resources where the JSON pointer is present, and the value it points to is not `null`.

  Literal values include `true` (match anything) and `false` (match nothing).

  Complex expressions employ `and`, `or`, and `!` (not), with parentheses, `(expression)`, to group expressions.

* `_queryId=identifier`

  Specify a query by its identifier.

  Specific queries can take their own query string parameter arguments, which depend on the implementation.

* `_pagedResultsCookie=string`

  The string is an opaque cookie used by the server to keep track of the position in the search results. The server returns the cookie in the JSON response as the value of `pagedResultsCookie`.

  In the request `_pageSize` must also be set and non-zero. You receive the cookie value from the provider on the first request, and then supply the cookie value in subsequent requests until the server returns a `null` cookie, meaning the final page of results has been returned.

  The `_pagedResultsCookie` parameter is supported when used with the `_queryFilter` parameter. The `_pagedResultsCookie` parameter is not guaranteed to work with the `_queryExpression` or `_queryId` parameters.

  The `_pagedResultsCookie` and `_pagedResultsOffset` parameters are mutually exclusive, and not to be used together.

* `_pagedResultsOffset=integer`

  When `_pageSize` is non-zero, use this as an index in the result set indicating the first page to return.

  The `_pagedResultsCookie` and `_pagedResultsOffset` parameters are mutually exclusive, and not to be used together.

* `_pageSize=integer`

  Return query results in pages of this size. After the initial request, use `_pagedResultsCookie` or `_pageResultsOffset` to page through the results.

* `_prettyPrint=true`

  Format the body of the response.

* `_totalPagedResultsPolicy=string`

  When a `_pageSize` is specified, and non-zero, the server calculates the `"totalPagedResults"`, in accordance with the `totalPagedResultsPolicy`, and provides the value as part of the response.

  The `"totalPagedResults"` is either an estimate of the total number of paged results (`_totalPagedResultsPolicy=ESTIMATE`), or the exact total result count (`_totalPagedResultsPolicy=EXACT`). If no count policy is specified in the query, or if `_totalPagedResultsPolicy=NONE`, result counting is disabled, and the server returns value of -1 for `"totalPagedResults"`.

* `_sortKeys=(|-)__field__[,(|-)field…​]`

  Sort the resources returned based on the specified field(s), either in `+` (ascending, default) order, or in `-` (descending) order.

  Because ascending order is the default, including the ` `` character in the query is unnecessary. If you do include the `` ` character, it must be URL-encoded as `%2B`, for example:

  ```
  http://localhost:8080/api/users?_queryFilter=true&_sortKeys=%2Bname/givenName
  ```

  The `_sortKeys` parameter is not supported for predefined queries (`_queryId`).

## HTTP status codes

When working with a Common REST API over HTTP, client applications should expect at least these HTTP status codes. Not all servers necessarily return all status codes identified here:

* 200 OK

  The request was successful and a resource returned, depending on the request.

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

  The requested resource is no longer available, and will not become available again. This can happen when resources expire for example.

* 412 Precondition Failed

  The resource's current version does not match the version provided.

* 415 Unsupported Media Type

  The request is in a format not supported by the requested resource for the requested method.

* 428 Precondition Required

  The resource requires a version, but no version was supplied in the request.

* 500 Internal Server Error

  The server encountered an unexpected condition that prevented it from fulfilling the request.

* 501 Not Implemented

  The resource does not support the functionality required to fulfill the request.

* 503 Service Unavailable

  The requested resource was temporarily unavailable. The service may have been disabled, for example.

---

---
title: AccessAuditExtensionContext
description: Reference for the AccessAuditExtensionContext scripting context, used to add custom data to PingGateway access audit events, including FAPI audit fields
component: pinggateway
version: 2026
page_id: pinggateway:reference:AccessAuditExtensionContext
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/AccessAuditExtensionContext.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-04-02T14:30:00Z
section_ids:
  properties: Properties
  more_information: More information
---

# AccessAuditExtensionContext

Context for additional custom access audit data for the current request. Includes FAPI-related audit information when FAPI is enabled.

You can find an example of how to use this context in [Extend audit events with custom data](../maintenance-guide/auditing.html#extend-audit-events-custom-data).

## Properties

The context is named `accessAuditExtension` and is accessible at `${contexts.accessAuditExtension}`. The context has the following properties:

* `"extensions"`: `Map<String, Object>`

  Map of custom `key:value` pairs that PingGateway includes in the `ig.ext` object of access audit events for the current request.

  When FAPI is enabled, this map can contain the following FAPI-related entries:

  * `fapi-interaction-id`

  * `fapi-client-id`

  * `fapi-client-name`

  * `fapi-organization-id`

  * `fapi-organization-name`

  * `fapi-software-id`

## More information

[org.forgerock.openig.audit.AccessAuditExtensionContext](../_attachments/apidocs/org/forgerock/openig/audit/AccessAuditExtensionContext.html)

[InteractionIdFapiContext](InteractionIdFapiContext.html)

[ApiClientFapiContext](ApiClientFapiContext.html)

---

---
title: AdminHttpApplication (<code>admin.json</code>)
description: Configure the PingGateway AdminHttpApplication (admin.json) to manage administrative routes, ports, monitoring, and OpenTelemetry settings
component: pinggateway
version: 2026
page_id: pinggateway:reference:AdminHttpApplication
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/AdminHttpApplication.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-02-23T12:00:00Z
section_ids:
  admin-default-objects: Default objects
  auto-created-objects: Provided objects (deprecated)
  AdminHttpApplication-usage: Usage
  AdminHttpApplication-properties-list: Properties
  AdminHttpApplication-heap: heap
  AdminHttpApplication-adminConnector: adminConnector
  AdminHttpApplication-auditService: auditService
  AdminHttpApplication-connectors: connectors
  AdminHttpApplication-vertx: vertx
  AdminHttpApplication-gatewayUnits: gatewayUnits
  AdminHttpApplication-adminMaxBodyLength: adminMaxBodyLength
  AdminHttpApplication-maxBodyLength: maxBodyLength
  AdminHttpApplication-mode: mode
  AdminHttpApplication-prefix: prefix (deprecated)
  AdminHttpApplication-properties: properties
  AdminHttpApplication-temporaryDirectory: temporaryDirectory
  AdminHttpApplication-temporaryStorage: temporaryStorage
  AdminHttpApplication-pidFileMode: pidFileMode
  AdminHttpApplication-preserveOriginalQueryString: preserveOriginalQueryString
  AdminHttpApplication-session: session
  AdminHttpApplication-streamingEnabled: streamingEnabled
  AdminHttpApplication-serveDeprecatedPrometheusEndpoint: serveDeprecatedPrometheusEndpoint
  AdminHttpApplication-openTelemetry: openTelemetry
  AdminHttpApplication-apiProtectionFilter: apiProtectionFilter
  AdminHttpApplication-metricsProtectionFilter: metricsProtectionFilter
  AdminHttpApplication-studioProtectionFilter: studioProtectionFilter
  AdminHttpApplication-example: Default configuration
  AdminHttpApplication-moreinfo: More information
---

# AdminHttpApplication (`admin.json`)

The AdminHttpApplication serves requests on the administrative route, such as the creation of routes and the collection of monitoring information. The administrative route and its subroutes are reserved for administration endpoints.

The configuration is loaded from a JSON-encoded file, expected at `$HOME/.openig/config/admin.json`. Objects configured in `admin.json` cannot be used by `config.json` or any PingGateway routes.

## Default objects

PingGateway provides default objects in `admin.json`. To override a default object, configure an object with the same name in `admin.json`.

Configure default objects in `admin.json` and `config.json` separately. An object configured in `admin.json` with the same name as an object configured in `config.json` isn't the same object.

* `AuditService`

  Records no audit events. The default AuditService is `NoOpAuditService`. Learn more from [NoOpAuditService](NoOpAuditService.html).

* `CaptureDecorator`

  Captures requests and response messages. The default CaptureDecorator is named `capture`, and uses the default settings given in [CaptureDecorator](CaptureDecorator.html).

  When a capture point for the default CaptureDecorator is defined in a route, for example, when `"capture: "all"` is set as a top-level attribute of the JSON, log messages for requests and responses passing through the route are written to a log file in `$HOME/.openig/logs`.

  When no capture point is defined in a route, only exceptions thrown during request or response processing are logged.

  By default, request and response contexts and entities aren't captured. Do one of the following to capture information:

  * Override the default capture decorator declaration, and set `captureEntity` to `true`.

  * Declare another CaptureDecorator object with an appropriate configuration and use it at your capture points.

  The capture decorator logs information about the HTTP request and response messages, along with their respective headers.

* `ClientHandler`

  Communicates with third-party services. Learn more from [ClientHandler](ClientHandler.html).

* `ForgeRockClientHandler`

  Sends transaction IDs when communicating with protected applications. The default [ForgeRockClientHandler](ForgeRockClientHandler.html) is a [Chain](Chain.html), composed of a [TransactionIdOutboundFilter](TransactionIdOutboundFilter.html) and a [ClientHandler](ClientHandler.html).

* `IssuerRepository` (deprecated)

  A repository of Issuers declared in the heap. To overwrite the default issuer, configure a local IssuerRepository with the name `IssuerRepository`. To create a new IssuerRepository containing a subset of Issuers, configure a local IssuerRepository with a different name.

  |   |                                                                                                                                                                                                                                                                                                                    |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | The [IssuerRepository (deprecated)](IssuerRepository.html) is deprecated. For issuers known in advance, add their settings to the [ClientRegistration](ClientRegistration.html). For discovery, configure an [AuthorizationCodeOAuth2ClientFilter](AuthorizationCodeOAuth2ClientFilter.html) `"discoveryHandler"`. |

* `ProxyOptions`

  A proxy to which a [ClientHandler](ClientHandler.html) or [ReverseProxyHandler](ReverseProxyHandler.html) can submit requests, and an [AmService](AmService.html) can submit Websocket notifications. For more information, refer to [ProxyOptions](ProxyOptions.html).

* `ReverseProxyHandler`

  Communicates with third-party services. For more information, refer to [ReverseProxyHandler](ReverseProxyHandler.html).

* `ScheduledExecutorService`

  Specifies the number of threads in a pool.

* `TemporaryStorage`

  Manages temporary buffers. For more information, refer to [TemporaryStorage](TemporaryStorage.html).

* `TimerDecorator`

  Records time spent within filters and handlers. The default TimerDecorator is named `timer`. For more information, refer to [TimerDecorator](TimerDecorator.html).

* `TracingDecorator`

  Pushes traces to an [OpenTelemetry](https://opentelemetry.io/) service.

  |   |                                                                                                                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This feature has [Evolving](https://docs.pingidentity.com/pinggateway/release-notes/stability.html#interface-stability) interface stability. It is subject to change without notice, even in a minor or maintenance release. |

  Use this to decorate the following:

  * [PingGateway access token resolvers](AccessTokenResolvers.html)

  * [AmService](AmService.html)

  * [AuditService](AuditService.html)

  * [PingGateway filters](Filters.html)

  * [PingGateway handlers](Handlers.html)

  The default [TracingDecorator](TracingDecorator.html) is named `tracing`. PingGateway traces include Vert.x traces where applicable.

* `TransactionIdOutboundFilter`

  Inserts the ID of a transaction into the header of a request.

## Provided objects (deprecated)

PingGateway creates the following objects when a filter with the name of the object is declared in `admin.json`.

|   |                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Overriding these objects by declaring objects with the same names in the heap is deprecated; define them [in the configuration](#AdminHttpApplication-usage) instead. |

* `"ApiProtectionFilter"`

  A filter to protect administrative APIs on reserved routes. By default, only the loopback address can access reserved routes.

* `"MetricsProtectionFilter"`

  A filter to protect the monitoring endpoints. By default, the Prometheus Scrape Endpoint and Common REST Monitoring Endpoint (deprecated) are open and accessible; no special credentials or privileges are required to access the monitoring endpoints.

* `"StudioProtectionFilter"`

  A filter to protect the Studio endpoint when PingGateway is running in development mode. When PingGateway is running in development mode, by default, the Studio endpoint is open and accessible.

## Usage

|   |                                                                                  |
| - | -------------------------------------------------------------------------------- |
|   | Restart PingGateway after making configuration changes to load the new settings. |

```none
{
  "heap": [ object, …​ ],
  "adminConnector": {
    "port": configuration expression<number>,
    "host": configuration expression<string>,
    "gracePeriod": configuration expression<duration>,
    "tls": ServerTlsOptions reference,
    "vertx": object,
    "maxTotalHeadersSize": configuration expression<integer>
  },
  "auditService": AuditService reference,
  "connectors": [ {
    "port": [ configuration expression<number>, …​ ],
    "host": configuration expression<string>,
    "gracePeriod": configuration expression<duration>,
    "tls": ServerTlsOptions reference,
    "vertx": object,
    "maxTotalHeadersSize": configuration expression<integer>
  }, …​ ],
  "vertx": object,
  "gatewayUnits": configuration expression<number>,
  "adminMaxBodyLength": configuration expression<number>,
  "maxBodyLength": configuration expression<number>,
  "mode": configuration expression<enumeration>,
  "prefix": configuration expression<string>, // deprecated
  "properties": object,
  "temporaryDirectory": configuration expression<string>,
  "temporaryStorage": TemporaryStorage reference,
  "pidFileMode": configuration expression<enumeration>,
  "preserveOriginalQueryString": configuration expression<boolean>,
  "session": AsyncSessionManager reference,
  "streamingEnabled": configuration expression<boolean>,
  "serveDeprecatedPrometheusEndpoint": configuration expression<boolean>,
  "openTelemetry": {
    "tracing": {
      "enabled": configuration expression<boolean>,
      "resourceAttributes": object,
      "exporter": {
        "type": "otlp",
        "config": {
          "endpoint": configuration expression<string>,
          "connectionTimeout": configuration expression<duration>,
          "headers": object,
          "proxyOptions": ProxyOptions reference,
          "retries": {
            "enabled": configuration expression<boolean>,
            "maxAttempts": configuration expression<number>
            "maxBackoff": configuration expression<duration>,
            "initialBackoff": configuration expression<duration>,
            "backoffMultiplier": configuration expression<number>
          },
          "timeout": configuration expression<duration>,
          "tls": ClientTlsOptions reference
        },
        "batch": {
          "enabled": configuration expression<boolean>,
          "compressionMethod": configuration expression<enumeration>,
          "scheduleDelay": configuration expression<duration>,
          "maxQueueSize": configuration expression<number>,
          "maxExportBatchSize": configuration expression<number>,
          "exporterTimeout": configuration expression<duration>,
          "exportUnsampledSpans": configuration expression<boolean>
        }
      },
      "sampler": {
        "type": configuration expression<string>,
        "ratio": configuration expression<number>
      },
      "spanLimits": {
        "maxNumberOfAttributesPerEvent": configuration expression<number>,
        "maxAttributeValueLength": configuration expression<number>,
        "maxNumberOfAttributes": configuration expression<number>,
        "maxNumberOfLinks": configuration expression<number>,
        "maxNumberOfEvents": configuration expression<number>,
        "maxNumberOfAttributesPerLink": configuration expression<number>
      }
    },
    "logging": {
      "enabled": configuration expression<boolean>,
      "resourceAttributes": object,
      "exporter": {
        "type": "otlp",
        "config": {
          "endpoint": configuration expression<string>,
          "compressionMethod": configuration expression<enumeration>,
          "connectionTimeout": configuration expression<duration>,
          "headers": object,
          "proxyOptions": ProxyOptions reference,
          "retries": {
            "enabled": configuration expression<boolean>,
            "maxAttempts": configuration expression<number>
            "maxBackoff": configuration expression<duration>,
            "initialBackoff": configuration expression<duration>,
            "backoffMultiplier": configuration expression<number>
          },
          "timeout": configuration expression<duration>,
          "tls": ClientTlsOptions reference
        },
        "batch": {
          "enabled": configuration expression<boolean>,
          "scheduleDelay": configuration expression<duration>,
          "maxQueueSize": configuration expression<number>,
          "maxExportBatchSize": configuration expression<number>,
          "exporterTimeout": configuration expression<duration>
        }
      }
    }
  },
  "apiProtectionFilter": object,
  "metricsProtectionFilter": object,
  "studioProtectionFilter": object
}
```

## Properties

### heap

`"heap"`: *array of [objects](preface.html#definition-object), optional*

The [heap object configuration](heap-objects.html).

### adminConnector

`"adminConnector"`: *[object](preface.html#definition-object), optional*

Port configuration for administrative traffic.

The following example requires administrative connections over HTTPS on port 9443 from the same computer (`localhost`):

```json
{
    "adminConnector": {
        "host": "localhost",
        "port": 9443,
        "tls": "ServerTlsOptions-1"
    }
}
```

Starting in PingGateway 2025.x, when you omit an `admin.json` file:

* The default port for administrative connections is 8085.

* The default protocol is HTTP. To require HTTPS for administrative connections, set TLS options as shown in the previous example.

* PingGateway no longer adds the deprecated `/openig` prefix to administrative endpoint paths. This is also the case when you explicitly define `"adminConnector"` settings.

**Administrative endpoints**

| Deprecated path                    | New path                    |
| ---------------------------------- | --------------------------- |
| `/openig/api/info`                 | `/api/info`                 |
| `/openig/health/live`              | `/health/live`              |
| `/openig/health/ready`             | `/health/ready`             |
| `/openig/health/startup`           | `/health/startup`           |
| `/openig/metrics/prometheus/0.0.4` | `/metrics/prometheus/0.0.4` |
| `/openig/ping`                     | `/ping`                     |

* `port`: *configuration expression<[number](preface.html#definition-number)>, required*

  The port where PingGateway listens for administrative connections.

  Don't reuse this port when setting [port numbers for `"connectors"`](#AdminHttpApplication-connectors-port).

- `host`: *configuration expression<[string](preface.html#definition-string)>, optional*

  The hostname where PingGateway listens for administrative connections.

  If this isn't `"localhost"` and you intend to permit connections from other systems, set an `"apiProtectionFilter"` in `admin.json` to allow access. For example, permit connections from systems in the private network address range `192.168.0.0`–`192.168.255.255`:

  ```json
  {
    "apiProtectionFilter": {
      "type": "AllowOnlyFilter",
      "config": {
        "rules": [
          {
            "name": "AdminAccessFromPrivateNetwork",
            "from": [
              {
                "ip": {
                  "list": [
                    "192.168.0.0/16"
                  ]
                }
              }
            ],
            "destination": [
              {
                "hosts": [
                  "ig.example.com"
                ],
                "ports": [
                  "9444"
                ],
                "methods": [
                  "POST",
                  "GET"
                ],
                "paths": [
                  "/*"
                ]
              }
            ]
          }
        ],
        "failureHandler": {
          "type": "StaticResponseHandler",
          "config": {
            "status": 403,
            "headers": {
              "Content-Type": [
                "text/html; charset=UTF-8"
              ]
            },
            "entity": "<html><p>Administrative access denied</p></html>"
          }
        }
      }
    }
  }
  ```

  Default: `0.0.0.0` (listen on all network interfaces)

* `gracePeriod`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

  When shutting down, PingGateway refuses new requests and waits for this period before forcing administrative connections to close.

  By default, the `stop.sh` and `stop.bat` scripts let the PingGateway process terminate gracefully. If you set a time limit for [forcible shutdown](../installation-guide/start-stop.html#forcible-shutdown), make sure it's longer than the `gracePeriod` defined here.

  Set `"gracePeriod": "disabled"` to force connections to close immediately.

  Default: 1 second

- `tls`: *ServerTlsOptions [reference](preface.html#definition-reference), optional*

  Configure [ServerTlsOptions](ServerTlsOptions.html) for connections to TLS-protected endpoints. Define the object inline or in the heap.

  Default: Connections to TLS-protected endpoints aren't configured.

* `vertx`: *[object](preface.html#definition-object), optional*

  Vert.x-specific configuration for administrative connections.

  Learn more about Vert.x options in [HttpServerOptions](https://vertx.io/docs/5.0.12/apidocs/io/vertx/core/http/HttpServerOptions.html).

  For properties where PingGateway provides its own first-class configuration, the PingGateway configuration option takes precedence over Vert.x options configured in `vertx`.

  Vert.x values are evaluated as configuration expressions.

  The following Vert.x configuration options are disallowed server-side:

  * `port`

  * `useAlpn`

  * `ssl`

  * `enabledCipherSuites`

  * `enabledSecureTransportProtocols`

  * `jdkSslEngineOptions`

  * `keyStoreOptions`

  * `openSslEngineOptions`

  * `pemKeyCertOptions`

  * `pemTrustOptions`

  * `pfxKeyCertOptions`

  * `pfxTrustOptions`

  * `trustStoreOptions`

  * `clientAuth`

  The following Vert.x configuration options are deprecated server-side:

  * `host`

  The following example sets a timeout for the DNS cache, so PingGateway can respond more quickly to DNS changes. Using [AddressResolverOptions](https://vertx.io/docs/5.0.12/apidocs/io/vertx/core/dns/AddressResolverOptions.html), it sets a maxiumum time-to-live (TTL) of 10 seconds for DNS responses:

  ```json
  {
    "vertx": {
      "addressResolverOptions": {
        "cacheMaxTimeToLive": 10
      }
    }
  }
  ```

  When PingGateway establishes a new connection, it uses the DNS cache to resolve the hostname. After the maximum TTL, PingGateway performs a new DNS lookup to get the most up-to-date IP address for the hostname.

- `maxTotalHeadersSize`: *[integer](preface.html#definition-integer), optional*

  The maximum size in bytes for the sum of all request headers. When the request headers exceed this limit, PingGateway returns an HTTP 431 error.

  Default: 8 192 bytes

### auditService

`"auditService"`: *AuditService [reference](preface.html#definition-reference), optional*

The [AuditService](AuditService.html) defined in `admin.json` to record audit events for administrative endpoints. This audit service differs from any audit service defined in `config.json` or in any route.

This audit service doesn't share settings with other audit services. Its settings don't impact or replace those in other audit services. When this audit service writes log files, make sure the `"logDirectory"` setting differs from other audit services to ensure unique log file paths.

This audit service must enable the `access` topic as shown in the [AuditService example](AuditService.html#AuditService-example).

Default: the `AuditService` defined in the heap

### connectors

`"connectors"`: *array of [objects](preface.html#definition-object), required*

Server port configuration, when PingGateway is acting *server-side*.

|   |                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When an application sends requests to or requests services from PingGateway, PingGateway is server-side. PingGateway serves the application acting as a client. |

* `port`: *array of configuration expression<[numbers](preface.html#definition-number)>, required*

  One or more ports where PingGateway listens for client application connections.

  When more than one port is defined, PingGateway listens on each port.

  Don't reuse these ports when setting the [port for the `"adminConnector"`](#AdminHttpApplication-adminConnector-port).

- `host`: *configuration expression<[string](preface.html#definition-string)>, optional*

  The hostname where PingGateway listens for administrative connections.

  Default: `0.0.0.0` (listen on all network interfaces)

* `gracePeriod`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

  When shutting down, PingGateway refuses new requests and waits for this period before forcing connections to close.

  By default, the `stop.sh` and `stop.bat` scripts let the PingGateway process terminate gracefully. If you set a time limit for [forcible shutdown](../installation-guide/start-stop.html#forcible-shutdown), make sure it's longer than the `gracePeriod` defined here.

  Set `"gracePeriod": "disabled"` to force connections to close immediately.

  Default: 1 second

- `tls`: *ServerTlsOptions [reference](preface.html#definition-reference), optional*

  Configure options for connections to TLS-protected endpoints based on [ServerTlsOptions](ServerTlsOptions.html). Define the object inline or in the heap.

  Default: Connections to TLS-protected endpoints aren't configured.

* `vertx`: *[object](preface.html#definition-object), optional*

  Vert.x-specific configuration for this connector when PingGateway is acting *server-side*. When PingGateway is acting *client-side*, configure the `vertx` property of a [ClientHandler](ClientHandler.html) or [ReverseProxyHandler](ReverseProxyHandler.html).

  Learn more about Vert.x options in [HttpServerOptions](https://vertx.io/docs/5.0.12/apidocs/io/vertx/core/http/HttpServerOptions.html).

  For properties where PingGateway provides its own first-class configuration, Vert.x configuration options are disallowed, and the PingGateway configuration option takes precedence over Vert.x options configured in `vertx`.

  Vert.x values are evaluated as configuration expressions.

  The following Vert.x configuration options are disallowed server-side:

  * `port`

  * `useAlpn`

  * `ssl`

  * `enabledCipherSuites`

  * `enabledSecureTransportProtocols`

  * `jdkSslEngineOptions`

  * `keyStoreOptions`

  * `openSslEngineOptions`

  * `pemKeyCertOptions`

  * `pemTrustOptions`

  * `pfxKeyCertOptions`

  * `pfxTrustOptions`

  * `trustStoreOptions`

  * `clientAuth`

  The following Vert.x configuration options are deprecated server-side:

  * `host`

  The following example configures connectors on ports 8080 and 8443 when PingGateway is acting server-side:

  ```json
  {
    "connectors": [{
      "port": 8080,
      "vertx": {
        "maxWebSocketFrameSize": 128000,
        "maxWebSocketMessageSize": 256000,
        "compressionLevel": 4
      }
    },
    {
      "port": 8443,
      "tls": "ServerTlsOptions-1"
    }]
  }
  ```

  The following example sets a timeout for the DNS cache, so PingGateway can respond more quickly to DNS changes. Using [AddressResolverOptions](https://vertx.io/docs/5.0.12/apidocs/io/vertx/core/dns/AddressResolverOptions.html), it sets a maxiumum time-to-live (TTL) of 10 seconds for DNS responses:

  ```json
  {
    "vertx": {
      "addressResolverOptions": {
        "cacheMaxTimeToLive": 10
      }
    }
  }
  ```

  When PingGateway establishes a new connection, it uses the DNS cache to resolve the hostname. After the maximum TTL, PingGateway performs a new DNS lookup to get the most up-to-date IP address for the hostname.

- `maxTotalHeadersSize`: *[integer](preface.html#definition-integer), optional*

  The maximum size in bytes of the sum of all request headers. When the request headers exceed this limit, PingGateway returns an HTTP 431 error.

  The following example configures HTTP/2 connections on port 7070 whenPingGateway is acting server-side. The configuration allows PingGateway to accept HTTP/2 requests with large headers:

  ```json
  {
    "connectors": [
      {
        "port": 7070,
        "maxTotalHeadersSize": 16384
      }
    ]
  }
  ```

  Default: 8 192 bytes

### vertx

`vertx`: *[object](preface.html#definition-object), optional*

This is the Vert.x-specific configuration used to more finely tune Vert.x instances. Vert.x values are evaluated as configuration expressions.

Use the Vert.x options described in [VertxOptions](https://vertx.io/docs/5.0.12/apidocs/io/vertx/core/VertxOptions.html) with the following exceptions:

* `metricsOptions`: Not used

* `metricsEnabled`: Enable Vertx metrics. Default: `true`.

Learn more in [Monitor Vert.x metrics](../maintenance-guide/monitoring.html#monitor-vertx).

PingGateway proxies all WebSocket subprotocols by default. To proxy specific WebSocket subprotocols only, list them as follows:

```none
"vertx": {
  "webSocketSubProtocols": ["v1.notifications.forgerock.org", ... ]
}
```

### gatewayUnits

`"gatewayUnits"`: *configuration expression<[number](preface.html#definition-number)>, optional*

The number of parallel instances of PingGateway to bind to an event loop. All instances listen on the same ports.

Default: The number of cores available to the JVM.

### adminMaxBodyLength

`"adminMaxBodyLength"`: *configuration expression<[number](preface.html#definition-number)>, optional*

Maximum body size in bytes for HTTP requests to the administration port.

This takes effect only when ["streamingEnabled"](#AdminHttpApplication-streamingEnabled) is `false`.

Default: `-1` (unlimited)

### maxBodyLength

`"maxBodyLength"`: *configuration expression<[number](preface.html#definition-number)>, optional*

Maximum body size in bytes for HTTP requests from client applications.

This takes effect only when ["streamingEnabled"](#AdminHttpApplication-streamingEnabled) is `false`.

Default: `-1` (unlimited)

### mode

`mode`: *configuration expression<[enumeration](preface.html#definition-enumeration)>, optional*

Set the PingGateway mode to `development` or `production`. The value is not case-sensitive.

If `mode` is not set, PingGateway resolves the provided configuration token `ig.run.mode` at startup to define the run mode.

Learn more in [PingGateway operating modes](../configure/operating-modes.html).

Default: `production`

### prefix (deprecated)

`"prefix"`: *configuration expression<[string](preface.html#definition-string)>, optional*

The base of the route for administration requests. This route and its subroutes are reserved for administration endpoints.

|   |                                                                    |
| - | ------------------------------------------------------------------ |
|   | This property is deprecated. Define an `"adminConnector"` instead. |

Default: `openig`

### properties

`"properties"`: *[object](preface.html#definition-object), optional*

Configuration parameters declared as property variables for use in the configuration. Learn more in [PingGateway route properties](Properties.html).

Default: No properties are defined.

### temporaryDirectory

`"temporaryDirectory"`: *configuration expression<[string](preface.html#definition-string)>, optional*

Directory containing temporary storage files.

Set this property to store temporary files in a different directory, for example:

```json
{
   "temporaryDirectory": "/path/to/my/temporary/directory"
}
```

Default: `$HOME/.openig/tmp` (on Windows, `%appdata%\OpenIG\tmp`)

### temporaryStorage

`"temporaryStorage"`: *TemporaryStorage [reference](preface.html#definition-reference), optional*

The [TemporaryStorage](TemporaryStorage.html) object to buffer content during processing.

Provide the name of a TemporaryStorage object defined in the heap or an inline TemporaryStorage configuration object.

Incoming requests use the temporary storage buffer as follows:

* Only used when `streamingEnabled` is `false`.

* The request is loaded into the PingGateway storage defined in `temporaryStorage` before it enters the chain.

* If the content length of the request is more than the buffer limit, PingGateway returns an `HTTP 413 Payload Too Large`.

Default: Use the heap object named `TemporaryStorage`. Otherwise, use an internally created TemporaryStorage object named `TemporaryStorage` with default settings for a TemporaryStorage object.

### pidFileMode

`"pidFileMode"`: *configuration expression<[enumeration](preface.html#definition-enumeration)>, optional*

Mode to allow or disallow startup if there is an existing PID file. Use one of the following values:

* `fail`: Startup fails if there is an existing PID file.

* `override`: Startup is allowed if there is an existing PID file. PingGateway removes the existing PID file and creates a new one during startup.

Default: `fail`

### preserveOriginalQueryString

`"preserveOriginalQueryString"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

Process query strings in URLs by applying or not applying a decode/encode process to the whole query string.

The following characters are disallowed in query string URL components: `"`, `{`, `}`, `<`, `>`, ``(space), and `|`. Learn more about which query string characters require encoding in [Uniform Resource Identifier (URI): Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986).

* `true`: Preserve query strings as they are presented.

  Select this option if the query string must not change during processing, for example, in signature verification.

  If a query string contains a disallowed character, the request returns HTTP 400 Bad Request.

* `false`: Tolerate disallowed characters in query string URL components by applying a decode/encode process to the whole query string.

  Select this option when a user agent or client produces query searches with disallowed characters. PingGateway transparently encodes the disallowed characters before forwarding requests to the protected application.

  Characters in query strings are transformed as follows:

  * Allowed characters aren't changed. For example, `sep=a` is not changed.

  * Percent-encoded values are re-encoded when the decoded value is an allowed character. For example, `sep=%27` is changed to `sep='` because `'` is an allowed character.

  * Percent-encoded values aren't changed when the decoded value is a disallowed character. For example, `sep=%22` is not changed because `"` is a disallowed character.

  * Disallowed characters are encoded. For example, `sep="` is changed to `sep=%22` because `"` is a disallowed character.

Default: `false`

### session

`"session"`: *AsyncSessionManager [reference](preface.html#definition-reference), optional*

An [InMemorySessionManager](InMemorySessionManager.html) or [JwtSessionManager](JwtSessionManager.html).

Learn more in [PingGateway sessions](../about/about-sessions.html).

Default: [InMemorySessionManager](InMemorySessionManager.html) with `IG_ADMIN_SESSIONID` as the session cookie name

### streamingEnabled

`"streamingEnabled"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

A flag to manage content:

* `true`: PingGateway streams the content of HTTP requests and responses. The content is available for processing bit-by-bit, as soon as it is received.

* `false`: PingGateway buffers the content of HTTP requests and responses into the storage defined in `temporaryStorage`. The content is available for processing only after it has all been received.

When this property is `true`, consider the following requirements to prevent PingGateway from blocking an executing thread to wait for streamed content:

* Write runtime expressions that consume streamed content with `#` instead of `$`. Learn more in the section on [runtime expressions](Expressions.html#runtime-expression).

* In scripts and Java extensions, never use a `Promise` blocking method, such as `get()`, `getOrThrow()`, or `getOrThrowUninterruptibly()` to obtain the response. Learn more in [PingGateway scripts](Scripts.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When `"streamingEnabled": true`:* A [CaptureDecorator](CaptureDecorator.html) with `"captureEntity": true` decorating a component interrupts streaming for the captured request or response until the whole entity is captured.

* For a client sharing connections to PingGateway, for example, because the client uses HTTP pipelining, any error consuming a chunked response causes PingGateway to reset (close) the client connection.

  This affects all requests associated with the connection.

* When PingGateway acts as a reverse proxy for client applications receiving few or infrequent [server-side events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events), set a high `soTimeout` value in the [ReverseProxyHandler](ReverseProxyHandler.html) configuration and implement mechanisms to keep the connection alive or reestablish it as needed. |

Default: `false`

### serveDeprecatedPrometheusEndpoint

"serveDeprecatedPrometheusEndpoint": *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

A flag to enable or disable the deprecated Prometheus metrics endpoint at `/metrics/prometheus`:

* `false`: Disable the deprecated Prometheus Scrape Endpoint

* `true`: Enable the deprecated Prometheus Scrape Endpoint

Default: `false`

### openTelemetry

`"openTelemetry"`: *[object](preface.html#definition-object), optional*

Configure how to push traces to an [OpenTelemetry](https://opentelemetry.io/) service. When you use it with other applications with OpenTelemetry support, the service helps you analyze the flows through PingGateway and the other applications to understand performance and system behavior.

|   |                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This feature has [Evolving](https://docs.pingidentity.com/pinggateway/release-notes/stability.html#interface-stability) interface stability. It is subject to change without notice, even in a minor or maintenance release. |

* `"tracing"`: *[object](preface.html#definition-object), required*

  PingGateway can push traces to an OpenTelemetry Protocol (OTLP) endpoint over HTTP where you collect and analyze system trace data. By default, this optional feature is disabled. To push traces to an OpenTelemetry service, you must at least enable it and set the decoration `"tracing": true` on routes or objects of interest to enable additional traces.

  The trace data and span content have [Evolving](https://docs.pingidentity.com/pinggateway/release-notes/stability.html#interface-stability) interface stability. It is subject to change without notice, even in a minor or maintenance release.

  The following configuration enables PingGateway to push traces to the default endpoint, `http://localhost:4318/v1/traces`:

  ```json
  {
      "openTelemetry": {
          "tracing": {
              "enabled": true
          }
      }
  }
  ```

  * `"enabled"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

    Set to `true` to enable OpenTelemetry tracing.

    Default: `false`

  - `"resourceAttributes"`: *object, optional*

    A map of additional resource attributes for processing traces. Learn more in the OpenTelemetry documentation about [Semantic Attributes with SDK-provided Default Value](https://opentelemetry.io/docs/specs/semconv/resource/#semantic-attributes-with-sdk-provided-default-value).

    For example, if there are multiple PingGateway instances in a deployment, set the `"service.instance.id"` resource attribute differently for each one to distinguish between them:

    ```json
    {
        "resourceAttributes": {
            "service.instance.id": "gateway1"
        }
    }
    ```

  * `"exporter"`: *object, optional*

    Configuration for the exporter, which pushes traces to the OpenTelemetry service.

    * `"type"`: *configuration expression<[string](preface.html#definition-string)>, optional*

      Set to `otlp` for OpenTelemetry Protocol (OTLP) support, which is the only supported protocol at this time.

      Default: `otlp`

    - `"config"`: *object, optional*

      Endpoint and timeout configuration:

      * `"endpoint"`: *configuration expression<[string](preface.html#definition-string)>, optional*

        The endpoint to publish traces to.

        For HTTPS, PingGateway trusts the default JVM CAs. To override this, set the `-Djavax.net.ssl.trustStore` and associated JVM settings when starting PingGateway. Learn more about the optional settings in the [Java Secure Socket Extension (JSSE) Reference Guide](https://docs.oracle.com/en/java/javase/25/security/java-secure-socket-extension-jsse-reference-guide.html).

        PingGateway doesn't support TLS configuration for the tracing endpoint at this time.

        Default: `http://localhost:4318/v1/traces`

      - `"connectionTimeout"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

        Time out a connection to the endpoint after this duration.

        Default: 10 seconds.

      * `"headers"`: *object, optional*

        Map of additional headers to include in the export span request.

        The following example sets the authorization header, `Authorization: Bearer ${bearer.token}`:

        ```none
        "headers": { "Authorization": "Bearer ${bearer.token}" }
        ```

      - `"proxyOptions"`: *ProxyOptions [reference](preface.html#definition-reference), optional*

        A [proxy](ProxyOptions.html) to send traces to.

        Default: Use the system proxy settings.

      * `"retries"`: *object, optional*

        This defines a retry policy for the export span requests.

        Default: Enabled

        * `"enabled"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

          Retry failed requests.

          Default: `true`

        - `"maxAttempts"`: *configuration expression<[number](preface.html#definition-number)>, optional*

          Maximum number of retries.

          Default: 5

        * `"initialBackoff"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

          How long to wait before the first retry.

          Default: 1 second

        - `"maxBackoff"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

          Maximum wait time between retries.

          Default: 5 seconds

        * `"backoffMultiplier"`: *configuration expression<[number](preface.html#definition-number)>, optional*

          Multiplier for the backoff wait time before retries.

          Default: 1.5

      - `"timeout"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

        Time out a request to publish data to the endpoint after this duration.

        Default: 10 seconds.

      * `"tls"`: *ClientTlsOptions [reference](preface.html#definition-reference), optional*

        Configure [ClientTlsOptions](ClientTlsOptions.html) for connections to a TLS-protected OpenTelemetry service. Define the object inline or in the heap.

        Default: Rely on the JVM settings to trust server certificates.

    * `"batch"`: *object, optional*

      Enable and configure batch processing for trace data.

      * `"enabled"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

        Leave batch processing enabled in deployment.

        Default: `true`

      - `"compressionMethod"`: *configuration expression<[enumeration](preface.html#definition-enumeration)>, optional*

        Method used to compress trace data; either `gzip` or `none`.

        Default: `gzip`

      * `"scheduleDelay"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

        Maximum interval between sending batches of trace data.

        Default: 50 seconds

      - `"maxQueueSize"`: *configuration expression<[number](preface.html#definition-number)>, optional*

        Maximum number of spans to queue before dropping them.

        Default: 1024

      * `"maxExportBatchSize"`: *configuration expression<[number](preface.html#definition-number)>, optional*

        Maximum number of spans in a batch.

        Default: 256

      - `"exporterTimeout"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

        Time out a data exporter after this duration.

        Default: 30 seconds

      * `"exportUnsampledSpans"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

        Whether to report on unsampled spans.

        Default: `false`

  - `"sampler"`: *object, optional*

    Configuration for sampling spans.

    * `"type"`: *configuration expression<[string](preface.html#definition-string)>, optional*

      The sampler strategy to use is one of the following:

      * `"alwaysOn"`: Send every span for processing.

      * `"alwaysOff"`: Never send any span for processing.

      * `"traceIdRatio"`: Sample the specified ratio of spans, deterministically based on the trace IDs of the spans.

      * `"parentBasedAlwaysOn"`: Always send the span for processing if the parent span was sampled. (Default)

      * `"parentBasedAlwaysOff"`: Never send the span for processing if the parent span was sampled.

      * `"parentBasedTraceIdRatio"`: Send the specified ratio of spans for processing if the parent span was sampled.

    - `"ratio"`: *configuration expression<[number](preface.html#definition-number)>, optional*

      For ratio-based types, a percentage of spans to process.

      Default: 50 (percent)

  * `"spanLimits"`: *object, optional*

    Configuration for limits enforced when recording spans.

    * `"maxNumberOfAttributesPerEvent"`: *configuration expression<[number](preface.html#definition-number)>, optional*

      The maximum number of metadata items (attributes) attached to a span per event. An event is an annotation to span at a particular, meaningful point in time during the span's duration.

      Default: 256

    - `"maxAttributeValueLength"`: *configuration expression<[number](preface.html#definition-number)>, optional*

      The maximum number of characters in a string attribute value.

      Default: 256

    * `"maxNumberOfAttributes"`: *configuration expression<[number](preface.html#definition-number)>, optional*

      The maximum number of attributes per span.

      Default: 256

    - `"maxNumberOfLinks"`: *configuration expression<[number](preface.html#definition-number)>, optional*

      The maximum number of links per span. Links associate the current span with one or more other spans.

      Default: 256

    * `"maxNumberOfEvents"`: *configuration expression<[number](preface.html#definition-number)>, optional*

      The maximum number of events per span.

      Default: 256

    - `"maxNumberOfAttributesPerLink"`: *configuration expression<[number](preface.html#definition-number)>, optional*

      The maximum number of attributes per link.

      Default: 256

- `"logging"`: *[object](preface.html#definition-object), required*

  PingGateway can log messages to an OpenTelemetry Protocol (OTLP) endpoint over HTTP where you collect and analyze system trace data. By default, this optional feature is disabled. To log to an OpenTelemetry service, you must at least enable logging.

  The following configuration enables PingGateway to log messages to `http://localhost:4318/v1/logs`:

  ```json
  {
      "openTelemetry": {
          "logging": {
              "enabled": true
          }
      }
  }
  ```

  * `"enabled"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

    Set to `true` to enable OpenTelemetry logging.

    Default: `false`

  - `"resourceAttributes"`: *object, optional*

    A map of additional resource attributes for processing logs. Learn more in the OpenTelemetry documentation about [Semantic Attributes with SDK-provided Default Value](https://opentelemetry.io/docs/specs/semconv/resource/#semantic-attributes-with-sdk-provided-default-value).

    For example, if you have multiple PingGateway servers in a deployment, set the `"service.instance.id"` resource attribute differently for each one to distinguish between them:

    ```json
    {
        "resourceAttributes": {
            "service.instance.id": "gateway1"
        }
    }
    ```

  * `"exporter"`: *object, optional*

    Configuration for the exporter, which logs to the OpenTelemetry service.

    * `"type"`: *configuration expression<[string](preface.html#definition-string)>, optional*

      Set to `otlp` for OpenTelemetry Protocol (OTLP) support, the only supported protocol at this time.

      Default: `otlp`

    - `"config"`: *object, optional*

      Endpoint and timeout configuration:

      * `"endpoint"`: *configuration expression<[string](preface.html#definition-string)>, optional*

        The endpoint to publish log messages to.

        For HTTPS, PingGateway trusts the default JVM CAs. To override this, set the `-Djavax.net.ssl.trustStore` and associated JVM settings when starting PingGateway. Learn more about the optional settings in the [Java Secure Socket Extension (JSSE) Reference Guide](https://docs.oracle.com/en/java/javase/25/security/java-secure-socket-extension-jsse-reference-guide.html).

        PingGateway doesn't support TLS configuration for the tracing endpoint at this time.

        Default: `http://localhost:4318/v1/logs`

      - `"compressionMethod"`: *configuration expression<[enumeration](preface.html#definition-enumeration)>, optional*

        Method used to compress log data; either `gzip` or `none`.

        Default: `gzip`

      * `"connectionTimeout"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

        Time out a connection to the endpoint after this duration.

        Default: 10 seconds.

      - `"headers"`: *object, optional*

        Map of additional headers to include in the export log request.

        The following example sets the authorization header, `Authorization: Bearer ${bearer.token}`:

        ```none
        "headers": { "Authorization": "Bearer ${bearer.token}" }
        ```

      * `"proxyOptions"`: *ProxyOptions [reference](preface.html#definition-reference), optional*

        A [proxy](ProxyOptions.html) to send log messages to.

        Default: Use the system proxy settings.

      - `"retries"`: *object, optional*

        This defines a retry policy for the export log requests.

        Default: Enabled

        * `"enabled"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

          Retry failed requests.

          Default: `true`

        - `"maxAttempts"`: *configuration expression<[number](preface.html#definition-number)>, optional*

          Maximum number of retries.

          Default: 5

        * `"initialBackoff"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

          How long to wait before the first retry.

          Default: 1 second

        - `"maxBackoff"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

          Maximum wait time between retries.

          Default: 5 seconds

        * `"backoffMultiplier"`: *configuration expression<[number](preface.html#definition-number)>, optional*

          Multiplier for the backoff wait time before retries.

          Default: 1.5

      * `"timeout"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

        Time out a request to publish log messages to the endpoint after this duration.

        Default: 10 seconds.

      - `"tls"`: *ClientTlsOptions [reference](preface.html#definition-reference), optional*

        Configure [ClientTlsOptions](ClientTlsOptions.html) for connections to a TLS-protected OpenTelemetry service. Define the object inline or in the heap.

        Default: Rely on the JVM settings to trust server certificates.

    * `"batch"`: *object, optional*

      Enable and configure batch processing for log messages.

      * `"enabled"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

        Leave batch processing enabled in deployment.

        Default: `true`

      - `"scheduleDelay"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

        Maximum interval between sending batches of log messages.

        Default: 50 seconds

      * `"maxQueueSize"`: *configuration expression<[number](preface.html#definition-number)>, optional*

        Maximum number of messages to queue before dropping them.

        Default: 1024

      - `"maxExportBatchSize"`: *configuration expression<[number](preface.html#definition-number)>, optional*

        Maximum number of messages in a batch.

        Default: 256

      * `"exporterTimeout"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

        Time out a data exporter after this duration.

        Default: 30 seconds

### apiProtectionFilter

`"apiProtectionFilter"`: *[object](preface.html#definition-object), optional*

A filter to protect administrative APIs on reserved routes.

Learn more in the section on [setting up UMA](../gateway-guide/uma.html#uma-configuration) and in [Reserved routes](preface.html#reserved-routes).

Default: only the loopback address can access reserved routes

### metricsProtectionFilter

`"metricsProtectionFilter"`: *[object](preface.html#definition-object), optional*

A filter to protect the monitoring endpoints.

Default: the Prometheus Scrape Endpoint and Common REST Monitoring Endpoint (deprecated) are open and accessible; no special credentials or privileges are required to access the monitoring endpoints.

Find an example in [Protect monitoring endpoints](../maintenance-guide/monitoring.html#proc-monitor-plat-protect).

### studioProtectionFilter

`"studioProtectionFilter"`: *[object](preface.html#definition-object), optional*

A filter to protect the Studio endpoint when PingGateway is running in development mode.

Learn more in [Restrict access to Studio](../studio-guide/restrict-access.html).

Default: the Studio endpoint is open and accessible when running PingGateway in development mode

## Default configuration

When your configuration doesn't include an `admin.json` file, PingGateway provides the following `admin.json` by default:

```json
{
  "connectors": [ { "port" : 8080 } ]
}
```

Source: [admin-sa.json](../_attachments/config/admin-sa.json)

By default, PingGateway implicitly defines 8085 as the `adminConnector` port, which is equivalent to `"adminConnector": { "port": 8085 }`. Also, by default, PingGateway no longer uses the (deprecated) prefix in paths to administrative endpoints. Learn more in [adminConnector](#AdminHttpApplication-adminConnector).

## More information

[org.forgerock.openig.http.AdminHttpApplication](../_attachments/apidocs/org/forgerock/openig/http/AdminHttpApplication.html)

---

---
title: AllowOnlyFilter
description: Configure AllowOnlyFilter to authorize requests in PingGateway based on rules that match sender IP address, certificate, destination, and HTTP method
component: pinggateway
version: 2026
page_id: pinggateway:reference:AllowOnlyFilter
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/AllowOnlyFilter.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-08-26T18:26:39Z
section_ids:
  AllowOnlyFilter-usage: Usage
  AllowOnlyFilter-properties: Properties
  AllowOnlyFilter-example: Examples
  certificate_and_ip_address_conditions: Certificate and IP address conditions
  destination_conditions: Destination conditions
  multiple_rules: Multiple rules
  AllowOnlyFilter-moreinfo: More information
---

# AllowOnlyFilter

Authorizes a request to continue processing if it satisfies at least one of the configured rules. Otherwise, passes the request to the FailureHandler or returns an HTTP 401 Unauthorized, with an empty response body.

This filter manages requests from the *last request sender*, otherwise called the *request from the last hop*, or the *request from a direct client*.

For debugging, configure the AllowOnlyFilter `name`, and add the following logger to `logback.xml`, replacing filter\_name with the name:

```
org.forgerock.openig.filter.allow.AllowOnlyFilter.filter_name
```

For more information, see [Managing PingGateway logs](../maintenance-guide/logging.html).

## Usage

```json
{
  "name": string,
  "type": "AllowOnlyFilter",
  "config": {
    "rules": [ object, ... ],
    "failureHandler": Handler reference
  }
}
```

## Properties

* `"rules"`: *array of [objects](preface.html#definition-object), required*

  An array of one or more `rules` configuration objects to specify criteria for the request.

  When more than one `rules` configuration object is included in the array, the request must match at least one of the configuration objects.

  When more than one property is specified in the `rules` configuration (for example, `from` and `destination`) the request must match criteria for each property.

  ```json
  {
    "rules": [
      {
        "name": configuration expression<string>,
        "from": [ object, ... ],
        "destination": [ object, ... ],
        "when": runtime condition<boolean>
      },
      ...
    ]
  }
  ```

  * `"name"`: *configuration expression<[string](preface.html#definition-string)>, optional*

    A name for the `rules` configuration. When logging is configured for the AllowOnlyFilter, the rule name appears in the logs.

  * `"from"`: *array of [objects](preface.html#definition-object), required*

    An array of one or more `from` configuration objects to specify criteria about the last request sender (the direct client).

    When more than one `from` configuration object is included in the array, the last request sender must match at least one of the configuration objects.

    When both `ip` and `certificate` properties are included in the configuration, the last request sender must match criteria for both properties.

    ```json
    "from": [
      {
        "ip": {
          "list": [configuration expression<string>, ...],
          "resolver": runtime expression<string>
        },
        "certificate" : {
          "subjectDNs" : Pattern[]
        }
      },
      ...
    ]
    ```

    * `"ip"`: *[object](preface.html#definition-object), optional*

      Criteria about the IP address of the last request sender.

      * `"list"`: *array of configuration expression<[strings](preface.html#definition-string)>, required*:

        An array of IP addresses or IP address ranges, using IPv4 or IPv6, and CIDR notation. The following example includes different formats:

        ```json
        "list": ["127.0.0.1", "::1", "192.168.0.0/16", "1234::/16"]
        ```

        The IP address of the last request sender must match at least one of the specified IP addresses or IP address ranges.

        * `"resolver"`: *runtime expression<[string](preface.html#definition-string)>, optional*:

          An expression that returns an IP address as a string.

          The following example returns an IP address from the first item in the first [`X-Forwarded-For` header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For):

          ```none
          "resolver": "${split(request.headers['X-Forwarded-For'][0], ',')[0]}"
          ```

          Default: Resolve the IP address from the following items, in the following order:

          1. If there is a `Forwarded` header, use the IP address of the last hop.

          2. Otherwise, if there is an `X-Forwarded-For` header, use the IP address of the last hop.

          3. Otherwise, use the IP address of the connection.

    * `"certificate"`: *[object](preface.html#definition-object), optional*

      A `certificate` configuration object specifying criteria about the certificate of the last request sender.

      * `"subjectDNs"`: *array of [patterns](preface.html#definition-pattern), required*:

        An array of patterns to represent the expected distinguished name of the certificate subject, the `subjectDN`. The `subjectDN` of the last request sender must match at least one of the patterns.

  * `"destination"`: *array of [objects](preface.html#definition-object), optional*

    An array of `destination` configuration objects to specify criteria about the request destination.

    When more than one `destination` configuration object is included in the array, the request destination must match at least one of the configuration objects.

    When more than one property is specified in the `destination` configuration, for example `hosts` and `ports`, the request destination must match criteria for each property.

    ```json
    "destination": [
      {
        "hosts": [pattern, ... ],
        "ports": [configuration expression<string>, ... ],
        "methods": [configuration expression<string>, ... ],
        "paths": [pattern, ... ]
      },
      ...
    ]
    ```

    * `"hosts"`: *array of [patterns](preface.html#definition-pattern), optional*

      An array of *case-insensitive* patterns to match the `request.host` attribute. Patterns are matched with the Java [Pattern](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/regex/Pattern.html) class.

      When this property is configured, the request destination must match at least one host pattern in the array.

      Default: Any host is allowed.

    * `"ports"`: *array of configuration expression<[strings](preface.html#definition-string)>, optional*

      An array of strings to match the `request.port` attribute. Specify values in the array as follows:

      * Array of single ports, for example `["80", "90"]`.

      * Array of port ranges, for example `["100:200"]`.

      * Array of single ports and port ranges, for example `["80", "90", "100:200"]`.

      When this property is configured, the destination port must match at least one entry in the array.

      Default: Any port is allowed.

    * `"methods"`: *array of configuration expression<[strings](preface.html#definition-string)>, optional*

      An array of HTTP methods to match the `request.method` attribute.

      When this property is configured, the request method must match at least one method in the array.

      Default: Any method is allowed.

    * `"paths"`: *array of [patterns](preface.html#definition-pattern), optional*

      An array of *case-sensitive* patterns to match the `request.url_path` attribute. Patterns are matched with the Java [Pattern](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/regex/Pattern.html) class.

      When this property is configured, the destination path must match at least one path in the array.

      Default: Any path is allowed.

  * `"when"`: *runtime condition<[boolean](preface.html#definition-boolean)>, optional*

    A [condition](Conditions.html) whose expression indicates the request meets a condition. When the condition's expression evaluates to `true`, PingGateway allows the request.

    The following condition is met when the first value of `h1` is `1`:

    ```json
    "when": "${request.headers['h1'][0] == '1'}"
    ```

    Default: `true`

* `"failureHandler"`: *Handler [reference](preface.html#definition-reference), optional*

  Handler to treat the request if none of the declared rules are satisfied.

  Provide either the name of a Handler object defined in the heap or an inline Handler configuration object.

  Default: HTTP 401 Unauthorized, with an empty response body.

  See also [PingGateway handlers](Handlers.html).

## Examples

### Certificate and IP address conditions

In the following example, a request is authorized if the last request sender satisfies *either* of the following conditions:

* Certificate subject DN matches `.*CN=test$` *or* `CN=me`, *and* the IP address is in the range 1.2.3.0/24.

* IP address is 123.43.56.8.

```json
"from": [
   {
     "certificate": {
          "subjectDNs": [".*CN=test$", "CN=me"]
     },
     "ip": {
       "list": ["1.2.3.0/24"]
     }
   },
   {
     "ip": {
       "list": ["123.43.56.8"]
     }
   },
]
```

### Destination conditions

In the following example, a request is authorized if the request destination satisfies *all* of the following conditions:

* The host is `myhost1.com` *or* `www.myhost1.com`

* The port is `80`.

* The method is `POST` *or* `GET`

* The path matches `/user/*`.

```json
"destination": [
  {
    "hosts": ["myhost1.com", "www.myhost1.com"],
    "ports": ["80"],
    "methods": ["POST", "GET"],
    "paths": ["/user/*"]
  }
]
```

### Multiple rules

The following example authorizes a request to continue processing if the requests meets the conditions set by *either* `rule1` or `rule2`:

```json
{
  "type": "AllowOnlyFilter",
  "config": {
    "rules": [
      {
        "name": "rule1",
        "from": [
          {
            "certificate": {
              "subjectDNs": [".*CN=test$", "CN=me"]
            },
            "ip": {
              "list": ["1.2.3.0/24"]
            }
          }
        ],
        "destination": [
          {
            "hosts": ["myhost1.com", "www.myhost1.com"],
            "ports": ["80"],
            "methods": ["POST", "GET"],
            "paths": ["/user/*"]
          }
        ],
        "when": "${request.headers['h1'][0] == '1'}"
      },
      {
        "name":"rule2",
        "when": "${request.headers['h1'][0] == '2'}"
      }
    ]
  }
}
```

## More information

[org.forgerock.openig.filter.allow.AllowOnlyFilter](../_attachments/apidocs/org/forgerock/openig/filter/allow/AllowOnlyFilter.html)

---

---
title: AmService
description: Configure AmService to connect PingGateway to PingAM, including agent authentication, WebSocket notifications, and session caching
component: pinggateway
version: 2026
page_id: pinggateway:reference:AmService
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/AmService.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-09-01T17:49:57Z
section_ids:
  AmService-usage: Usage
  AmService-properties-list: Properties
  AmService-agent: agent
  AmService-secretsProvider: secretsProvider
  AmService-url: url
  AmService-realm: realm
  AmService-amHandler: amHandler
  AmService-notifications: notifications
  AmService-sessionCache: sessionCache
  AmService-sessionIdleRefresh: sessionIdleRefresh
  AmService-sessionProperties: sessionProperties
  AmService-ssoTokenHeader: ssoTokenHeader
  AmService-version: version
  AmService-moreinfo: More information
---

# AmService

Holds information about the configuration of an instance of AM. The AmService is available to PingGateway filters that communicate with that instance.

When PingGateway uses an AmService, PingGateway is positioned as the client of the service. By default, PingGateway is subscribed to Websocket notifications from AM, and the WebSocket connection can be secured by ClientTlsOptions.

## Usage

```none
{
  "name": string,
  "type": "AmService",
  "config": {
    "agent": {
      "username": configuration expression<string>,
      "passwordSecretId": configuration expression<secret-id>,
      "journey": configuration expression<string>
    },
    "secretsProvider": SecretsProvider reference,
    "url": configuration expression<url>,
    "realm": configuration expression<string>,
    "amHandler": Handler reference,
    "notifications": {
      "audit": {
        "auditService": AuditService reference,
        "auditIgnoredNotifications": configuration expression<boolean>
      },
      "enabled": configuration expression<boolean>,
      "initialConnectionAttempts": configuration expression<number>,
      "reconnectDelay": configuration expression<duration>,
      "renewalDelay": configuration expression<duration>,
      "heartbeatInterval": configuration expression<duration>,
      "connectionTimeout": configuration expression<duration>,
      "idleTimeout": configuration expression<duration>,
      "tls": ClientTlsOptions reference,
      "proxyOptions": ProxyOptions reference,
      "vertx": object
    },
    "sessionCache": {
      "enabled": configuration expression<boolean>,
      "executor": Executor service reference,
      "maximumSize": configuration expression<number>,
      "maximumTimeToCache": configuration expression<duration>,
      "onNotificationDisconnection": configuration expression<enumeration>
    },
    "sessionIdleRefresh": {
      "enabled": configuration expression<boolean>,
      "interval": configuration expression<duration>
    },
    "sessionProperties": [ configuration expression<string>, …​ ],
    "ssoTokenHeader": configuration expression<string>,
    "version": configuration expression<string>
  }
}
```

## Properties

### agent

`"agent"`: *[object](preface.html#definition-object), required*

An PingGateway agent profile. When the agent is authenticated, PingGateway can use the token for tasks, such as getting the user profile, making policy evaluations, and connecting to the AM notification endpoint.

* `"username"`: *configuration expression<[string](preface.html#definition-string)>, required*

  Name of the AM agent profile.

- `"passwordSecretId"`: *configuration expression<[secret-id](preface.html#definition-secretid)>, required*

  The secret ID of the AM agent password.

  This secret ID must point to a [GenericSecret](../security-guide/keys.html#secret-types).

* `"journey"`: *configuration expression<[string](preface.html#definition-string)>, required*

  The authentication journey (tree) to use when authenticating to AM.

  Default: `Agent`

### secretsProvider

`"secretsProvider"`: *SecretsProvider [reference](preface.html#definition-reference), required*

The [SecretsProvider](SecretsProvider.html) to query for the agent password.

### url

`"url"`: *configuration expression<[url](preface.html#definition-url)>, required*

The URL of the AM service.

When AM is running locally, this value could be `https://am.example.com/openam`. When AM is running in PingOne Advanced Identity Cloud, this value could be `https://myTenant.forgeblocks.com/am`.

### realm

`"realm"`: *configuration expression<[string](preface.html#definition-string)>, optional*

The AM realm in which the PingGateway agent is created.

Default: `/` (top level realm).

### amHandler

`"amHandler"`: *Handler [reference](preface.html#definition-reference), optional*

The [Handler](Handlers.html) to use for communicating with AM. In production, use a [ClientHandler](ClientHandler.html) capable of making an HTTPS connection to AM.

AmService doesn't use `amHandler` to subscribe to WebSocket notifications from AM. To subscribe to WebSocket notifications from AM, configure a [ClientTlsOptions](ClientTlsOptions.html) object in the heap and refer to it from the `amHandler` object and `notifications.tls`.

For auditing, use a [ForgeRockClientHandler](ForgeRockClientHandler.html) to send a transaction ID when communicating with protected applications. Alternatively, configure this handler as a chain with a [TransactionIdOutboundFilter](TransactionIdOutboundFilter.html):

```none
"amHandler": {
  "type": "Chain",
  "config": {
    "handler": "MySecureClientHandler",
    "filters": [ "TransactionIdOutboundFilter" ]
  }
}
```

Default: `ForgeRockClientHandler`

### notifications

`"notifications"`: *[object](preface.html#definition-object), optional*

Configure a WebSocket notification service to subscribe to Websocket notifications from AM.

To subscribe to WebSocket notifications from AM, configure a [ClientTlsOptions](ClientTlsOptions.html) object in the heap and refer to it from the `amHandler` object and `notifications.tls`. Alternatively, use `proxyOptions` to share a proxy configuration between the `amHandler` and the notification service.

Learn more in [WebSocket notifications](../maintenance-guide/tuning.html#amservice-websocket).

* `"audit"`: *[object](preface.html#definition-object), optional*

  Audit service settings.

  * `"auditService"`: *Handler [reference](preface.html#definition-reference), optional*

    The [AuditService](AuditService.html) to use for notifications.

    This audit service must enable the `notifications` topic as in the following example:

    ```json
    {
        "name": "JsonAuditService",
        "type": "AuditService",
        "config": {
            "config": {
                "filterPolicies": {
                    "field": {
                        "_comment": "Optionally hide specific items; here, the universalId:",
                        "excludeIf": [
                            "/notifications/notification/body/universalId"
                        ]
                    }
                }
            },
            "eventHandlers": [
                {
                    "class": "org.forgerock.audit.handlers.json.JsonAuditEventHandler",
                    "config": {
                        "name": "json",
                        "logDirectory": "&{ig.instance.dir}/auditLogs",
                        "topics": [
                            "notifications"
                        ]
                    }
                }
            ]
        }
    }
    ```

    The file suffix depends on the audit service implementation. For this example, the file's named `notifications.audit.json`.

    With tracing enabled as in the example, the traces include an additional attribute in the span to indicate the topic triggered, `code.namespace`, containing either `access` or `notifications`.

    The `transactionId` in an audit event doesn't come from AM. PingGateway generates a new `transactionId` for each event. At present, you can't link the AM event that generated the notification with the PingGateway audit event.

    Default: the `AuditService` defined in the heap

  - `"auditIgnoredNotifications"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

    If `true`, audit all notifications. If `false` audit only notifications that trigger a change in state, such as a removing an item from a cache.

    If the notification triggered something to change, PingGateway records `"triggered":true` in the audit log entry. Otherwise, it records `"triggered":false`.

    Default: `false`

- `"enabled"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

  A flag to enable WebSocket notifications. Set to `false` to disable WebSocket notifications.

  Default: `true`

* `"initialConnectionAttempts"`: *configuration expression<[number](preface.html#definition-number)>, optional*

  The maximum number of times PingGateway attempts to open a WebSocket connection before failing to deploy a route. For no limit, set this property to `-1`.

  If the WebSocket connection fails **after** it has been opened and the route is deployed, PingGateway attempts to reconnect to it an unlimited number of times.

  Default: `5`

- `"reconnectDelay"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

  The time between attempts to reestablish a lost WebSocket connection.

  When a WebSocket connection is lost, PingGateway waits for this delay and attempts to reestablish the connection. If subsequent attempts fail, PingGateway waits and tries again an unlimited number of times.

  Default: `5 seconds`

* `"renewalDelay"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

  The time before automatically renewing a WebSocket connection between PingGateway and AM. PingGateway renews connections transparently.

  PingOne Advanced Identity Cloud closes WebSocket connections every 60 minutes. This property is set by default to prevent connection closure by automatically renewing connections every 50 minutes.

  Set to `0` or `unlimited` to never automatically renew connections.

  Default: `50 minutes`

- `"heartbeatInterval"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

  The interval at which the AmService issues a heartbeat on WebSocket connections. When activity on the connection is low, the heartbeat prevents middleware or policies situated between PingGateway and AM from closing the connection for timeout.

  Set to zero or unlimited to disable heartbeats.

  Default: `1 minute`

* `"connectionTimeout"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

  The time PingGateway waits to establish a Websocket connection to AM before it considers the attempt as failed.

  Default: `60 seconds`

- `"idleTimeout"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

  The time that a WebSocket connection to AM can be inactive before PingGateway closes it.

  Default: `unlimited`

* `"tls"`: *ClientTlsOptions [reference](preface.html#definition-reference), optional*

  Configure options for WebSocket connections to TLS-protected endpoints.

  Define a [ClientTlsOptions](ClientTlsOptions.html) object inline or in the heap.

  Default: Connections to TLS-protected endpoints aren't configured.

- `"proxyOptions"`: *ProxyOptions [reference](preface.html#definition-reference)>, optional*

  A proxy server to which requests can be submitted. Use this property to relay requests to other parts of the network. For example, use it to submit requests from an internal network to the internet.

  Provide the name of a [ProxyOptions](ProxyOptions.html) object defined in the heap or an inline configuration.

  Default: A heap object named `ProxyOptions`.

* `"vertx"`: *[object](preface.html#definition-object), optional*

  Vert.x-specific configuration for WebSocket connections to AM. Vert.x values are evaluated as configuration expressions.

  Use the Vert.x options described in [VertxOptions](https://vertx.io/docs/5.0.12/apidocs/io/vertx/core/VertxOptions.html).

### sessionCache

`"sessionCache"`: *[object](preface.html#definition-object), optional*

In AM, if the realm includes a customized session property safelist, include `AMCtxId` in the list of properties. The customized session property safelist overrides the global session property safelist.

Enable and configure caching of session information from AM based on [Caffeine](https://github.com/ben-manes/caffeine).

When `sessionCache` is enabled, PingGateway can reuse session token information without repeatedly asking AM to verify the token. Each instance of AmService has an independent cache content. The cache isn't shared with other AmService instances, either in the same or different routes and is not distributed among clustered PingGateway instances.

When `sessionCache` is disabled, PingGateway must ask AM to verify the token for each request.

PingGateway evicts session info entries from the cache for the following reasons:

* AM cache timeout, based on whichever of the following events occur first:

  * `maxSessionExpirationTime` from SessionInfo

  * `maxSessionTimeout` from the AmService configuration

  When PingGateway evicts session info entries from the cache, the next time the token is presented, PingGateway must ask AM to verify the token.

* If Websocket notifications are enabled, AM session revocation; for example, when a user logs out of AM.

  When Websocket notifications are enabled, PingGateway evicts a cached token almost as soon as it is revoked on AM, and in this way, stays synchronized with AM. Later requests to PingGateway that present the revoked token are rejected.

  When Websocket notifications are disabled, the token remains in the cache after it is revoked on AM. Later requests to PingGateway that present the revoked token are considered as valid and can cause incorrect authentication and authorization decisions until its natural eviction from the cache.

- `"enabled"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

  Enable caching.

  Default: `false`

* `"executor"`: *Executor service [reference](preface.html#definition-reference), optional*

  An executor service to schedule the execution of tasks, such as the eviction of entries in the cache.

  Default: `ForkJoinPool.commonPool()`

- `"maximumSize"`: *configuration expression<[number](preface.html#definition-number)>, optional*

  The maximum number of entries the cache can contain.

  Default: Unlimited/unbound

* `"maximumTimeToCache"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

  The maximum duration for which to cache session info. Set this duration to be less than the idle timeout of AM.

  If `maximumTimeToCache` is longer than `maxSessionExpirationTime` from SessionInfo, `maxSessionExpirationTime` is used.

  Default:

  * When `sessionIdleRefresh` is set, idle timeout of AM minus 30 seconds.

  * When `sessionIdleRefresh` is not set, `maxSessionExpirationTime`, from SessionInfo.

- `"onNotificationDisconnection"`: *configuration expression<[enumeration](preface.html#definition-enumeration)>, optional*

  The strategy to manage the cache when the WebSocket notification service is disconnected, and PingGateway receives no notifications for AM events. If the cache is not cleared it can become outdated, and PingGateway can allow requests on revoked sessions or tokens.

  Cached entries that expire naturally while the notification service is disconnected are removed from the cache.

  Use one of the following values:

  * `NEVER_CLEAR`

    * When the notification service is disconnected:

      * Continue to use the existing cache.

      * Deny access for requests that aren't cached, but don't update the cache with these requests.

    * When the notification service is reconnected:

      * Continue to use the existing cache.

      * Query AM for incoming requests that aren't found in the cache, and update the cache with these requests.

  * `CLEAR_ON_DISCONNECT`

    * When the notification service is disconnected:

      * Clear the cache.

      * Deny access to all requests, but don't update the cache with these requests.

    * When the notification service is reconnected:

      * Query AM for all requests that aren't found in the cache. (Because the cache was cleared, the cache is empty after reconnection.)

      * Update the cache with these requests.

  * `CLEAR_ON_RECONNECT`

    * When the notification service is disconnected:

      * Continue to use the existing cache.

      * Deny access for requests that aren't cached, but don't update the cache with these requests.

    * When the notification service is reconnected:

      * Query AM for all requests that aren't found in the cache. (Because the cache was cleared, the cache is empty after reconnection.)

      * Update the cache with these requests.

  Default: `CLEAR_ON_DISCONNECT`

### sessionIdleRefresh

`"sessionIdleRefresh"`: *[object](preface.html#definition-object), optional*

Enable and configure periodic refresh of idle sessions. When this property is enabled, PingGateway requests session refresh:

* The first time PingGateway gets an SSO token from AM, irrespective of the age of the token.

* When `sessionIdleRefresh.interval` has elapsed.

Use this property when AM is using CTS-based sessions. AM doesn't monitor idle time for client-side sessions and so refresh requests are ignored.

When the SingleSignOnFilter is used for authentication with AM, AM can view a session as idle even though a user continues to interact with PingGateway. The user session eventually times out, and the user must reauthenticate.

When the SingleSignOnFilter filter is used with the PolicyEnforcementFilter, the session is refreshed each time PingGateway requests a policy decision from AM. The session is less likely to become idle, and this property isn't required.

* `"enabled"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

  Enable refresh of idle sessions.

  Default: `false`

- `"interval"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

  Duration to wait after a session becomes idle before requesting a session refresh.

  Set the refresh interval in line with the latest access time update frequency of AM. For example, if PingGateway requests a refresh every 60 seconds, but the update frequency of AM is 5 minutes, AM ignores most of the PingGateway requests.

  |   |                                                                                                                                                                    |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | Each session refresh must be reflected in the AM core token service. Setting the interval to a duration lower than one minute can adversely impact AM performance. |

  Default: `5 minutes`

### sessionProperties

`"sessionProperties"`: *array of configuration expression<[strings](preface.html#definition-string)>, optional*

The list of user session properties to retrieve from AM by the [SessionInfoFilter](SessionInfoFilter.html).

Default: All available session properties are retrieved from AM.

### ssoTokenHeader

`"ssoTokenHeader"`: *configuration expression<[string](preface.html#definition-string)>, optional*

The header name or cookie name where this AM server expects to find SSO tokens.

If a value for `ssoTokenHeader` is provided, PingGateway uses that value. Otherwise, PingGateway queries the AM `/serverinfo/*` endpoint for the header or cookie name.

Default: Empty. PingGateway queries AM for the cookie name.

### version

`"version"`: *configuration expression<[string](preface.html#definition-string)>, optional*

The version number of the AM server. PingGateway uses the AM version to establish endpoints for its interaction with AM.

The AM version is derived as follows, in order of precedence:

* Discovered value: The AmService discovers the AM version.

  If `"version"` is configured with a different value, the AmService ignores the value of `"version"` and logs a warning.

* Value in `"version"`: The AmService cannot discover the AM version and `"version"` is configured.

* Default value of AM 7.3: When the AmService cannot discover the AM version and `"version"` is not configured.

If you use a feature that is supported only in a higher AM version than discovered or specified, PingGateway logs a message or throws an error.

Default: AM 7.3.

## More information

[org.forgerock.openig.tools.am.AmService](../_attachments/apidocs/org/forgerock/openig/tools/am/AmService.html)

---

---
title: AmSessionIdleTimeoutFilter
description: Configure AmSessionIdleTimeoutFilter to track PingAM session idle time in PingGateway and force session revocation when the idle timeout expires
component: pinggateway
version: 2026
page_id: pinggateway:reference:AmSessionIdleTimeoutFilter
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/AmSessionIdleTimeoutFilter.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-08-13T11:08:28Z
section_ids:
  AmSessionIdleTimeoutFilter-usage: Usage
  AmSessionIdleTimeoutFilter-properties: Properties
  AmSessionIdleTimeoutFilter-example: Example
  AmSessionIdleTimeoutFilter-moreinfo: More information
---

# AmSessionIdleTimeoutFilter

Forces the revocation of AM sessions that have been idle for a specified duration. The AmSessionIdleTimeoutFilter issues an authenticated and encrypted JWT to track activity on the AM session and conveys it within a persistent cookie.

To help honor timeout, the persistent cookie is configured to expire at the same time as the tracking token. Without a persistent cookie, the browser is more likely to clear the side-car cookie and PingGateway is more likely to consider the session as timed out.

The tracking token contains the following parts:

* The time when the user was last active

* A hash of the AM session cookie, used to bind the tracking token to the AM session cookie

* The idle timeout

Multiple filter instances can share the same tracking token, for example, in a clustered PingGateway configuration, or when a federation of applications protected by authentication filters need to have a flexible idle timeout strategy.

AmSessionIdleTimeoutFilter requires the following configuration:

* In AM, client-side sessions must be enabled for the realm in which the tracking token operates. See [Configure client-side sessions](https://docs.pingidentity.com/pingam/8.1/am-sessions/impl-client-based-sessions.html#proc-configure-client-based-sessions) in AM's *Sessions Guide*.

* In AM, client-side session denylisting must be enabled. See [Configure client-side session denylisting](https://docs.pingidentity.com/pingam/8.1/am-sessions/session-state-session-termination.html#session-state-configure-denylist) in AM's *Sessions Guide*.

* The AmSessionIdleTimeoutFilter must be placed in a route before a filter that uses the AM session token, such as a SingleSignOnFilter or PolicyEnforcementFilter.

* In production environments, and when multiple AmSessionIdleTimeoutFilters use the same tracking token, the encryption must not rely on the default configuration. It must be configured identically on each filter that uses the tracking token.

The following image shows the flow of information when an AmSessionIdleTimeoutFilter sits in front of a CrossDomainSingleSignOnFilter, to manage AM session timeout.

![idletime](_images/idletime.svg)

\[1-5] When the AmSessionIdleTimeoutFilter receives an unauthenticated request, it passes the request along the chain, and the CrossDomainSingleSignOnFilter manages authentication.

\[6-8] When the AmSessionIdleTimeoutFilter receives an authenticated request, it checks that the AM session token is valid, and then passes the request along the chain.

\[9-10] If the AM session was valid, the AmSessionIdleTimeoutFilter issues a tracking token on the response flow, containing the following information:

* Hash of the AM session token

* Current timestamp

* Idle timeout of the current filter

If the AM session was not valid, the AmSessionIdleTimeoutFilter does nothing on the response flow.

\[11-12] The AmSessionIdleTimeoutFilter places the tracking token in persistent tracking cookie, and sends it with the response, to be used in the next request.

\[13-15] When the same or another AmSessionIdleTimeoutFilter receives an authenticated request with a tracking token, it checks that the AM session token is valid, and checks that tracking token hash is bound to the AM session.

\[16] Depending on the strategy set by `idleTimeoutUpdate`, the AmSessionIdleTimeoutFilter selects the value for `idleTimeout` from the tracking token (set by the AmSessionIdleTimeoutFilter in a previous request) or from its own value of `idleTimeout` (if this is a different instance of AmSessionIdleTimeoutFilter).

The AmSessionIdleTimeoutFilter checks for AM session timeout. If the last activity time plus the idle timeout is before the current time, the session has timed out. For example, a session with the following values has timed out:

* last activity time: 15h30 today

* idle timeout: 5 mins

* current time: 15h40

\[17-21] The AM session has timed out, so the AmSessionIdleTimeoutFilter does the following:

* Forces AM to revoke the session.

* Passes the request along the chain.

* Expires the tracking cookie on the response flow, and sends it with the response.

\[22-26] The session has not timed out, so the AmSessionIdleTimeoutFilter does the following:

* Passes the request along the chain.

* Updates the tracking token on the response flow based on the `idleTimeoutUpdate` strategy.

* Places the tracking token in a persistent tracking cookie, and sends it with the response, to be used in the next request.

## Usage

```json
{
  "name": string,
   "type": "AmSessionIdleTimeoutFilter",
   "config": {
     "amService": AmService reference,
     "idleTimeout": configuration expression<duration>,
     "sessionToken": runtime expression<string>,
     "removeAmSessionFilter": Filter reference,
     "idleTimeoutUpdate": configuration expression<enumeration>,
     "secretsProvider": SecretsProvider reference,
     "encryptionSecretId": configuration expression<secret-id>,
     "encryptionMethod": configuration expression<string>,
     "cookie": object
   }
}
```

## Properties

* `"amService"`: *AmService [reference](preface.html#definition-reference), required*

  The AmService that refers to the AM instance that issue tracked session token.

* `"idleTimeout"`: *configuration expression<[duration](preface.html#definition-duration)>, required*

  The time a session can be inactive before it is considered as idle.

  When an AmSessionIdleTimeoutFilter creates the tracking token, the token's value for `idleTimeout` is set by this property. When a different AmSessionIdleTimeoutFilter accesses the same tracking token, depending on the strategy set by `idleTimeoutUpdate`, the token's value for `idleTimeout` can be updated by the second AmSessionIdleTimeoutFilter.

* `"sessionToken"`: *runtime expression<[string](preface.html#definition-string)>, optional*

  The location of the AM session token in the request. The following example accesses the first value of the request cookie `iPlanetDirectoryPro`:

  ```none
  "sessionToken": "${request.cookies['iPlanetDirectoryPro'][0].value}"
  ```

  You can find more information in [Find the AM session cookie name](../gateway-guide/preface.html#am-session-cookie).

  Default: `${request.cookies['<cookie name defined in the referenced AmService>'][0].value}`

* `"removeAmSessionFilter"`: *Filter [reference](preface.html#definition-reference), optional*

  A filter to remove the AM session details from the request when the session is no longer valid.

  This helps in load-balanced AM deployments with client-side sessions where AM servers aren't necessarily in sync regarding expired client-side sessions. Set this to a custom filter if the AM session token isn't in the AM session cookie.

  Default: a filter that removes the AM session token based on the AM session cookie name.

* `"idleTimeoutUpdate"`: *configuration expression<[enumeration](preface.html#definition-enumeration)>, required*

  When multiple AmSessionIdleTimeoutFilters use the same tracking token, this property defines what idle timeout to use for the request and how to set the idle timeout for the tracking token in the response.

  Use one of the following values:

  * `ALWAYS`: Enforce the idle timeout from this filter; in the response, set the new tracking token idle timeout to the idle timeout of this filter.

  * `DECREASE_ONLY`: Enforce the shortest idle timeout from either this filter or the tracking token; in the response, set the new tracking token idle timeout to the shortest of the two.

  * `INCREASE_ONLY`: Enforce the longest idle timeout from either this filter or the tracking token; in the response, set the new tracking token idle timeout to the longest of the two.

  * `INCREASE_ONLY_THEN_ALWAYS`: Enforce the longest idle timeout from either this filter or the tracking token; in the response, set the new tracking token idle timeout to the idle timeout of this filter.

  * `NEVER`: Enforce the idle timeout from the tracking token; in the response, set the new tracking token idle timeout to the idle timeout of the old tracking token.

  PingGateway uses the new tracking token on the next interaction with an AmSessionIdleTimeoutFilter.

  Default: `ALWAYS`

* `"secretsProvider"`: *SecretsProvider [reference](preface.html#definition-reference), optional*

  The [SecretsProvider](SecretsProvider.html) to query for secrets to encrypt the tracking token.

* `"encryptionSecretId"`: *configuration expression<[secret-id](preface.html#definition-secretid)>, optional*

  The secret ID of the encryption key used to encrypt the tracking cookie.

  This secret ID must point to a [CryptoKey\`](../security-guide/keys.html#secret-types).

  In production environments, and when multiple AmSessionIdleTimeoutFilters use the same tracking cookie, the encryption must not rely on the default configuration. It must be configured identically on each filter that uses the cookie.

  Authenticated encryption is achieved with a symmetric encryption key. Therefore, the secret must refer to a symmetric key.

  For more information, refer to [RFC 5116](https://datatracker.ietf.org/doc/html/rfc5116).

  Default: When no `secretsProvider` is provided, PingGateway generates a random symmetric key for authenticated encryption.

- `"encryptionMethod"`: *configuration expression<[string](preface.html#definition-string)>, optional*

  The algorithm to use for authenticated encryption. For information about allowed encryption algorithms, refer to [RFC 7518: "enc" (Encryption Algorithm) Header Parameter Values for JWE](https://www.rfc-editor.org/rfc/rfc7518#section-5.1).

  Default: A256GCM

- `"cookie"`: *[object](preface.html#definition-object), optional*

  Configuration of the activity tracking cookie.

  ```json
  {
    "name": configuration expression<string>,
    "domain": configuration expression<string>,
    "httpOnly": configuration expression<boolean>,
    "path": configuration expression<string>,
    "sameSite": configuration expression<enumeration>,
    "secure": configuration expression<boolean>
  }
  ```

  * `"name"`: *configuration expression<[string](preface.html#definition-string)>, optional*

    The cookie name.

    Default: `x-ig-activity-tracker`

  - `"domain"`: *configuration expression<[string](preface.html#definition-string)>, optional*

    Domain to which the cookie applies.

    Default: The fully qualified hostname of the PingGateway host.

  - `"httpOnly"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

    Flag to mitigate the risk of client-side scripts accessing protected cookies.

    Default: `true`

  - `"path"`: *configuration expression<[string](preface.html#definition-string)>, optional*

    Path to apply to the cookie.

    Default: `/`

  - `"sameSite"`: *configuration expression<[enumeration](preface.html#definition-enumeration)>, optional*

    Options to manage the circumstances in which a cookie is sent to the server. Use one of the following values to reduce the risk of CSRF attacks:

    * `STRICT`: Send the cookie only if the request was initiated from the cookie domain. Not case-sensitive. Use this value to reduce the risk of cross-site request forgery (CSRF) attacks.

    * `LAX`: Send the cookie only with GET requests in a first-party context, where the URL in the address bar matches the cookie domain. Not case-sensitive. Use this value to reduce the risk of cross-site request forgery (CSRF) attacks.

    * `NONE`: Send the cookie whenever a request is made to the cookie domain. With this setting, consider setting `secure` to `true` to prevent browsers from rejecting the cookie. For more information, refer to [SameSite cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite).

    Default: Null

  - `"secure"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

    Flag to limit the scope of the cookie to secure channels.

    Default: `false`

## Example

```json
{
  "type": "AmSessionIdleTimeoutFilter",
  "config": {
    "sessionToken": "${request.cookies['iPlanetDirectoryPro'][0].value}",
    "amService": "AmService",
    "idleTimeout": "1 minute",
    "idleTimeoutUpdate": "ALWAYS",
    "cookie": {
      "name": "x-ig-activity-tracker",
      "domain": null,
      "path": "/",
      "secure": false,
      "httpOnly": true,
      "sameSite": null
    },
   "secretsProvider": "secrets-provider-ref",
   "encryptionMethod": "A256GCM",
   "encryptionSecretId": "crypto.key.secret.id"
  }
}
```

## More information

[org.forgerock.openig.openam.session.AmSessionIdleTimeoutFilter](../_attachments/apidocs/org/forgerock/openig/openam/session/AmSessionIdleTimeoutFilter.html)

---

---
title: ApiClientFapiContext
description: Reference for the ApiClientFapiContext context object used in PingGateway FAPI interactions, including its properties and Javadoc link
component: pinggateway
version: 2026
page_id: pinggateway:reference:ApiClientFapiContext
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/ApiClientFapiContext.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-06-02T18:01:47Z
section_ids:
  properties: Properties
  more_information: More information
---

# ApiClientFapiContext

Context for the `ApiClient` during FAPI interactions.

## Properties

The context is named `FapiApiClient` and is accessible at `${contexts.FapiApiClient}`. The context has the following properties:

* `"apiClient"`: *[ApiClient](../_attachments/apidocs/org/forgerock/openig/fapi/apiclient/ApiClient.html)*

  The `ApiClient`; this is empty for requests unless the request is to an OAuth 2.0 endpoint.

## More information

[org.forgerock.openig.fapi.apiclient.ApiClientFapiContext](../_attachments/apidocs/org/forgerock/openig/fapi/apiclient/ApiClientFapiContext.html)

---

---
title: AssignmentFilter
description: Configure AssignmentFilter in PingGateway to assign values to targets based on conditions, evaluated before a request or after a response is handled
component: pinggateway
version: 2026
page_id: pinggateway:reference:AssignmentFilter
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/AssignmentFilter.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-02-23T12:00:00Z
section_ids:
  AssignmentFilter-usage: Usage
  AssignmentFilter-properties: Properties
  AssignmentFilter-example: Examples
  AssignmentFilter-example-addinfo: Add info to a session
  AssignmentFilter-example-capturecred: Capture and store login credentials
---

# AssignmentFilter

Verifies that a specified condition is met. If the condition is met or if no condition is specified, the value is assigned to the target. Values can be assigned before the request is handled and after the response is handled.

## Usage

```none
{
  "name": string,
  "type": "AssignmentFilter",
  "config": {
    "onRequest": [
      {
        "condition": runtime condition<boolean>,
        "target": lvalue-expression,
        "value": runtime expression
      }, ...
    ],
    "onResponse": [
      {
        "condition": runtime condition<boolean>,
        "target": lvalue-expression,
        "value": runtime expression
      }, ...
    ]
  }
}
```

## Properties

* `"onRequest"`: *array of [objects](preface.html#definition-object), optional*

  Defines a list of assignment bindings to evaluate before the request is handled.

* `"onResponse"`: *array of [objects](preface.html#definition-object), optional*

  Defines a list of assignment bindings to evaluate after the response is handled.

* `"condition"`: *runtime condition<[boolean](preface.html#definition-boolean)>, optional*

  A [condition](Conditions.html). If the condition's expression evaluates to `true`, PingGateway assigns the value to the target.

  Default: `true`

* `"target"`: *<[lvalue-expression](preface.html#definition-lvalue-expression)>, required*

  Expression that yields the target object whose value is to be set.

* `"value"`: *runtime expression<[object](preface.html#definition-object)> , optional*

  The value to be set in the target. The value can be a string, information from the context, or even a whole map of information.

## Examples

### Add info to a session

The following example assigns a value to a session to keep empty JWT-based session cookies:

```json
{
  "type": "AssignmentFilter",
  "config": {
    "onRequest": [{
      "target": "${session.authUsername}",
      "value": "I am root"
    }]
  }
}
```

### Capture and store login credentials

The following example captures credentials and stores them in the PingGateway session during a login request. Notice that the credentials are captured on the request but aren't marked as valid until the response returns a positive 302. The credentials could then be used to log a user in to a different application:

```json
{
  "name": "PortalLoginCaptureFilter",
  "type": "AssignmentFilter",
  "config": {
    "onRequest": [
      {
        "target": "${session.authUsername}",
        "value": "${request.queryParams['username'][0]}"
      },
      {
        "target": "${session.authPassword}",
        "value": "${request.queryParams['password'][0]}"
      },
      {
        "comment": "Authentication has not yet been confirmed.",
        "target": "${session.authConfirmed}",
        "value": "${false}"
      }
    ],
    "onResponse": [
      {
        "condition": "${response.status.code == 302}",
        "target": "${session.authConfirmed}",
        "value": "${true}"
      }
    ]
  }
}
```

---

---
title: AttributesContext
description: Reference for AttributesContext, which provides a map of transient per-request attributes accessible in PingGateway expressions
component: pinggateway
version: 2026
page_id: pinggateway:reference:AttributesContext
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/AttributesContext.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-06-02T18:01:47Z
section_ids:
  Attributes-properties: Properties
  Attributes-moreinfo: More information
---

# AttributesContext

Provides a map for request attributes. When PingGateway processes a single request, it injects transient state information about the request into this context. Attributes stored when processing one request aren't accessible when processing a subsequent request.

PingGateway automatically provides access to the `attributes` field through the `attributes` bindings in expressions. For example, to access a username with an expression, use `${attributes.credentials.username}` instead of `${contexts.attributes.attributes.credentials.username}`

Use [SessionContext](SessionContext.html) to maintain state between successive requests from the same logical client.

## Properties

The context is named `attributes`, and is accessible at `${attributes}`. The context has the following property:

* `"attributes"`: [map](preface.html#definition-map)

  Map with the format `Map<String,Object>`, where:

  * Key: Attribute name

  * Value: Attribute value

Cannot be null.

## More information

[org.forgerock.services.context.AttributesContext](../_attachments/apidocs/org/forgerock/services/context/AttributesContext.html)

---

---
title: AuditService
description: Configure PingGateway AuditService to record access and notification audit events, with event handlers, filter policies, and custom topic schemas
component: pinggateway
version: 2026
page_id: pinggateway:reference:AuditService
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/AuditService.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-09-01T17:49:57Z
section_ids:
  AuditService-usage: Usage
  AuditService-properties: Properties
  AuditService-example: Example
  AuditService-moreinfo: More information
---

# AuditService

The audit service records `access` and `notifications` audit events. Learn how to record other types of audit events in [Record custom audit events](../configure/extending.html#audit-custom).

By default, no routes in a configuration are audited; the [NoOpAuditService](NoOpAuditService.html) object type provides an empty audit service to the top-level heap and its child routes. PingGateway provides a default empty service based on the NoOpAuditService type. The top-level heap and child routes inherit from the setting and use a service equivalent to the following declaration:

```json
{
  "name": "AuditService",
  "type": "NoOpAuditService"
}
```

Configure auditing in the following ways:

* Override the NoOpAuditService for all routes in the configuration

  Define an AuditService object named `AuditService` in `config.json`. No other configuration is required; all routes use the same AuditService.

* Configure an audit service that can be optionally used by all routes in the configuration

  Do both of the following:

  * In `config.json` in the top-level heap, define an AuditService object that is **not** named `AuditService`.

  * In a route, configure the [Route](Route.html) property `auditService` to refer to the name of the declared `AuditService` heaplet.

* Configure an audit service specifically for a route

  Do one of the following:

  * Define an AuditService object named `AuditService` in the route heap.

  * In the route heap or a parent heap, define an AuditService object that is **not** named `AuditService`; configure the [Route](Route.html) property `auditService` to refer to the name of the declared `AuditService` heaplet.

  * Configure the [Route](Route.html) property `auditService` with an inline AuditService object.

One configuration can contain multiple AuditServices.

When you define multiple AuditServices that use JsonAuditEventHandler or CsvAuditEventHandler, configure each of the event handlers with a different `logDirectory`. This prevents the AuditServices from logging to the same audit logging file.

## Usage

```json
{
  "name": string,
  "type": "AuditService",
  "config": {
    "config": object,
    "eventHandlers": [ object, ...],
    "topicSchemasDirectory": configuration expression<string>
  }
}
```

## Properties

* `"config"`: *[object](preface.html#definition-object), required*

  Configures the audit service itself, rather than event handlers. If the configuration uses only default settings, you can omit the field instead of including an empty object as the field value.

  ```json
  {
    "config": {
      "handlerForQueries": configuration_expression<string>,
      "availableAuditEventHandlers": [configuration_expression<string>, ...],
      "caseInsensitiveFields": [configuration_expression<string>, ...],
      "filterPolicies": {
        "field": {
          "includeIf": [configuration_expression<string>, ...],
          "excludeIf": [configuration_expression<string>, ...]
        }
      }
    }
  }
  ```

  * `"handlerForQueries"`: *configuration expression<[string](preface.html#definition-string)>, optional*

    The name of the event handler to use when querying audit event messages over REST.

  * `"availableAuditEventHandlers"`: *array of configuration expression<[strings](preface.html#definition-string)>, optional*

    A list of fully qualified event handler class names for event handlers available to the audit service.

  * `"caseInsensitiveFields"`: *array of configuration expression<[strings](preface.html#definition-string)>, optional*

    A list of audit event fields to be considered as case-insensitive for filtering. The fields are referenced using JSON pointer syntax. The list can be `null` or empty.

    Default: `/access/http/request/headers` and `/access/http/response/headers` fields are considered case-insensitive for filtering. All other fields are considered case-sensitive.

  * `"filterPolicies"`: *[object](preface.html#definition-object), optional*

    To prevent logging of sensitive data for an event, PingGateway uses a safelist to specify which event fields appear in the logs. By default, only event fields that are safelisted are included in the audit event logs. For more information about safelisting, refer to [Safelisting audit event fields for the logs](../maintenance-guide/auditing.html#common-audit-safelist).

    * `"field"`: *[object](preface.html#definition-object), optional*

      This property specifies non-safelisted event fields to include in the logs, and safelisted event fields to exclude from the logs.

      If `includeIf` and `excludeIf` are specified for the same field, `excludeIf` takes precedence.

      Audit event fields use JSON pointer notation, and are taken from the JSON schema for the audit event content.

      Default: Include only safelisted event fields in the logs.

      * `"includeIf"`: *array of configuration expression<[strings](preface.html#definition-string)>, optional*:

        A list of non-safelisted audit event fields to include in the logs. Specify the topic and the hierarchy to the field. Any child fields of the specified field are encompassed.

        |   |                                                                                                                                                                                                                                                                                                                  |
        | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | Before you include non-safelisted event fields in the logs, consider the impact on security. Including some headers, query parameters, or cookies in the logs could cause credentials or tokens to be logged, and allow anyone with access to the logs to impersonate the holder of these credentials or tokens. |

      - `"excludeIf"`: *array of configuration expression<[strings](preface.html#definition-string)>, optional*:

        A list of safelisted audit event fields to exclude from the logs. Specify the topic and the hierarchy to the field. Any child fields of the specified field are encompassed.

        The following example excludes fields for the `access` topic:

        ```json
        {
          "field": {
            "excludeIf": [
              "/access/http/request/headers/host",
              "/access/http/request/path",
              "/access/server",
              "/access/response"
            ]
          }
        }
        ```

        For an example route that excludes fields, see [Exclude safelisted audit event fields from logs](../maintenance-guide/auditing.html#proc-audit-exclude).

* `"eventHandlers"`: *array of Event Handler [objects](preface.html#definition-object), required*

  An array of one or more audit event handler configuration objects to deal with audit events.

  The configuration of the event handler depends on type of event handler. PingGateway supports the event handlers listed in [AuditFramework](AuditFramework.html).

* `"topicSchemasDirectory"`: *configuration expression<[string](preface.html#definition-string)>, optional*

  Directory containing the JSON schema for the topic of a custom audit event. The schema defines which fields are included in the topic. For information about the syntax, see [JSON Schema](https://json-schema.org).

  Default: `$HOME/.openig/audit-schemas` (Windows, `%appdata%\OpenIG\audit-schemas`)

  For an example of how to configure custom audit events, see [Record custom audit events](../configure/extending.html#audit-custom).

  The following example schema includes the mandatory fields, `_id`, `timestamp`, `transactionId`, and `eventName`, and an optional `customField`:

  ```json
  {
    "schema": {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "id": "/",
      "type": "object",
      "properties": {
        "_id": {
          "type": "string"
        },
        "timestamp": {
          "type": "string"
        },
        "transactionId": {
          "type": "string"
        },
        "eventName": {
          "type": "string"
        },
        "customField": {
          "type": "string"
        }
      }
    }
  }
  ```

  Source: [customTopic.json](../_attachments/audit-schemas/customTopic.json)

## Example

The following example audit service logs access event messages in a comma-separated variable file, named `/path/to/audit/logs/access.csv`:

```json
{
  "name": "AuditService",
  "type": "AuditService",
  "config": {
    "config": {},
    "eventHandlers": [
      {
        "class": "org.forgerock.audit.handlers.csv.CsvAuditEventHandler",
        "config": {
          "name": "csv",
          "logDirectory": "/path/to/audit/logs",
          "topics": [
            "access"
          ]
        }
      }
    ]
  }
}
```

The following example route uses the audit service:

```json
{
  "handler": "ReverseProxyHandler",
  "auditService": "AuditService"
}
```

## More information

[NoOpAuditService](NoOpAuditService.html)

[org.forgerock.audit.AuditService](../_attachments/apidocs/org/forgerock/audit/AuditService.html)

---

---
title: AuthorizationCodeOAuth2ClientFilter
description: Configure AuthorizationCodeOAuth2ClientFilter to authenticate end users in PingGateway using the OAuth 2.0 authorization code grant flow
component: pinggateway
version: 2026
page_id: pinggateway:reference:AuthorizationCodeOAuth2ClientFilter
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/AuthorizationCodeOAuth2ClientFilter.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-04-21T12:00:00Z
section_ids:
  AuthorizationCodeOAuth2ClientFilter-serviceuri: Service URIs
  AuthorizationCodeOAuth2ClientFilter-usage: Usage
  AuthorizationCodeOAuth2ClientFilter-properties: Properties
  AuthorizationCodeOAuth2ClientFilter-clientEndpoint: clientEndpoint
  AuthorizationCodeOAuth2ClientFilter-failureHandler: failureHandler
  AuthorizationCodeOAuth2ClientFilter-loginHandler: loginHandler
  AuthorizationCodeOAuth2ClientFilter-registrations: registrations
  AuthorizationCodeOAuth2ClientFilter-metadata: metadata
  AuthorizationCodeOAuth2ClientFilter-cacheExpiration: cacheExpiration
  AuthorizationCodeOAuth2ClientFilter-draftMixUpMitigation: draftMixUpMitigation
  AuthorizationCodeOAuth2ClientFilter-executor: executor
  AuthorizationCodeOAuth2ClientFilter-defaultLoginGoto: defaultLoginGoto
  AuthorizationCodeOAuth2ClientFilter-defaultLogoutGoto: defaultLogoutGoto
  AuthorizationCodeOAuth2ClientFilter-requireHttps: requireHttps
  AuthorizationCodeOAuth2ClientFilter-requireLogin: requireLogin
  AuthorizationCodeOAuth2ClientFilter-revokeOauth2TokenOnLogout: revokeOauth2TokenOnLogout
  AuthorizationCodeOAuth2ClientFilter-openIdEndSessionOnLogout: openIdEndSessionOnLogout
  AuthorizationCodeOAuth2ClientFilter-prompt: prompt
  AuthorizationCodeOAuth2ClientFilter-issuerRepository: issuerRepository (deprecated)
  AuthorizationCodeOAuth2ClientFilter-useDeprecatedIssuerRepository: useDeprecatedIssuerRepository (deprecated)
  AuthorizationCodeOAuth2ClientFilter-discoveryHandler: discoveryHandler
  AuthorizationCodeOAuth2ClientFilter-discoverySecretId: discoverySecretId
  AuthorizationCodeOAuth2ClientFilter-tokenEndpointAuthMethod: tokenEndpointAuthMethod
  AuthorizationCodeOAuth2ClientFilter-tokenEndpointAuthSigningAlg: tokenEndpointAuthSigningAlg
  AuthorizationCodeOAuth2ClientFilter-oAuth2SessionKey: oAuth2SessionKey
  AuthorizationCodeOAuth2ClientFilter-secretsProvider: secretsProvider
  AuthorizationCodeOAuth2ClientFilter-example: Examples
  AuthorizationCodeOAuth2ClientFilter-moreinfo: More information
---

# AuthorizationCodeOAuth2ClientFilter

Uses OAuth 2.0 delegated authorization to authenticate end users. The filter can act as an OpenID Connect (OIDC) relying party (RP) or as an OAuth 2.0 client.

AuthorizationCodeOAuth2ClientFilter performs the following tasks:

* Allows the user to select an Authorization Server from one or more static client registrations or by discovery and dynamic registration.

  In static client registration, Authorization Servers are provided by [Issuer](Issuer.html), and registrations are provided by [ClientRegistration](ClientRegistration.html).

* Redirects the user through the authentication and authorization steps of an OAuth 2.0 authorization code grant, which results in the Authorization Server returning an access token to the filter.

* When an authorization grant succeeds, injects the access token data into the [OAuth2InfoContext](OAuth2InfoContext.html) so that subsequent filters and handlers can access the access token. Subsequent requests can use the access token without authenticating again.

* When an authorization grant fails, the filter injects information about the failure into the [OAuth2FailureContext](OAuth2FailureContext.html), which is provided to the `failureHandler` object.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When this filter acts as an OIDC RP, avoid sharing the ID token with other applications or relying on the ID token claims after authentication completes and the end user's redirected to the final landing page.When this filter requests the `openid` scope, the OpenID provider returns both an access token and an ID token. If the ID token claims must remain fresh as long as the access token remains valid, align the access token and ID token lifetimes. |

## Service URIs

Service URIs are constructed from the `clientEndpoint`, as follows:

* `clientEndpoint/login/?discovery=user-input&goto=url`

  Discover and register dynamically with the end user's OpenID Provider or with the client registration endpoint as described in RFC 7591, using the value of user-input.

  After successful registration, redirect the end user to the provider for authentication and authorization consent. Then redirect the user agent back to the callback client endpoint, and then the goto URI.

  The goto URL must use the same scheme, host, and port as the original URI, or be a relative URI (just the path). Otherwise, the request fails with an error.

  To redirect a request to a site that doesn't meet the goto URL criteria, change the original URI by using a ForwardedRequestFilter.

* `clientEndpoint/login?registration=clientId&issuer=issuerName&goto=url`

  Redirect the end user for authorization with a registration defined by the [ClientRegistration](ClientRegistration.html) properties `clientId` and `issuerName`.

  The provider corresponding to the registration then authenticates the end user and obtains authorization consent before redirecting the user agent back to the callback client endpoint.

  If successful, the filter saves the authorization state in the session and redirects the user agent to the goto URL.

  The goto URL must use the same scheme, host, and port as the original URI, or be a relative URI (just the path). Otherwise, the request fails with an error.

  To redirect a request to a site that doesn't meet the goto URL criteria, change the original URI by using a ForwardedRequestFilter.

* `clientEndpoint/logout?goto=url`

  Remove the authorization state for the end user, and redirect the request to the goto URL.

  The goto URL must use the same scheme, host, and port as the original URI, or be a relative URI (just the path). Otherwise, the request fails with an error.

  To redirect a request to a site that doesn't meet the goto URL criteria, change the original URI by using a ForwardedRequestFilter.

  If no goto URL is specified in the request, use `defaultLogoutGoto`.

* `clientEndpoint/callback`

  Handle the callback from the OAuth 2.0 Authorization Server occuring as part of the authorization process.

  If the callback is handled successfully, the filter saves the authorization state in the [OAuth2InfoContext](OAuth2InfoContext.html) and redirects to the URL provided to the login endpoint during login.

* Other request URIs

  Restore the authorization state in the [OAuth2InfoContext](OAuth2InfoContext.html) and call the next filter or handler in the chain.

## Usage

```none
{
  "name": string,
  "type": "AuthorizationCodeOAuth2ClientFilter",
  "config": {
    "clientEndpoint": runtime expression<uri string>,
    "failureHandler": Handler reference,
    "loginHandler": Handler reference,
    "registrations": [ ClientRegistration reference, …​ ],
    "metadata": object,
    "draftMixUpMitigation": configuration expression<boolean>,
    "cacheExpiration": configuration expression<duration>,
    "executor": ScheduledExecutorService reference,
    "defaultLoginGoto": runtime expression<url>,
    "defaultLogoutGoto": runtime expression<url>,
    "requireHttps": configuration expression<boolean>,
    "requireLogin": configuration expression<boolean>,
    "revokeOauth2TokenOnLogout": configuration expression<boolean>,
    "openIdEndSessionOnLogout": configuration expression<boolean>,
    "prompt": configuration expression<string>,
    "issuerRepository": IssuerRepository reference, // deprecated
    "useDeprecatedIssuerRepository": configuration expression<boolean>, // deprecated
    "discoveryHandler": Handler reference,
    "discoverySecretId": configuration expression<secret-id>,
    "tokenEndpointAuthMethod": configuration expression<enumeration>,
    "tokenEndpointAuthSigningAlg": configuration expression<string>,
    "oAuth2SessionKey": configuration expression<string>,
    "secretsProvider": SecretsProvider reference
  }
}
```

## Properties

### clientEndpoint

`"clientEndpoint"`: *runtime expression<[url](preface.html#definition-url)>, required*

The URI to the client endpoint.

|   |                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------- |
|   | This endpoint must remain unique to this filter and route. Don't reuse it in other routes or filters or in protected applications. |

So that routes can accept redirects from the Authorization Server to the callback endpoint, the `clientEndpoint` must be the same as the route condition or a sub path of the route condition:

* The same as the route condition:

  ```none
  "condition": "${find(request.uri.path, '^/discovery')}"
  ```

  ```none
  "clientEndpoint": "/discovery"
  ```

* As a sub path of the route condition:

  ```none
  "condition": "${find(request.uri.path, '^/home/id_token')}"
  ```

  ```none
  "clientEndpoint": "/home/id_token/sub-path"
  ```

Service URIs are constructed from the `clientEndpoint`. For example, when `clientEndpoint` is `openid`, the service URIs are `/openid/login`, `/openid/logout`, and `/openid/callback`. These endpoints are implicitly reserved and attempts to access them directly can cause undefined errors.

The result of the expression must be a string that represents a valid URI, but isn't a real `java.net.URI` object. For example, it would be incorrect to use `${request.uri}`, which isn't a String but a MutableUri. Learn more in [PingGateway expressions](Expressions.html).

### failureHandler

`"failureHandler"`: *Handler [reference](preface.html#definition-reference), optional*

An inline handler configuration object or the name of a handler object defined in the heap.

When the OAuth 2.0 Resource Server denies access to a resource, the failure handler can only be invoked if the error response contains a WWW-Authenticate header, which means there was a problem with the OAuth 2.0 exchange. All other responses are forwarded to the user agent without invoking the failure handler.

If the value of the WWW-Authenticate header is `invalid_token`, the AuthorizationCodeOAuth2ClientFilter tries to refresh the access token:

* If the token is refreshed, the AuthorizationCodeOAuth2ClientFilter tries again to access the protected resource.

* If the token isn't refreshed, or if the second attempt to access the protected resource fails, the AuthorizationCodeOAuth2ClientFilter invokes the failure handler.

You can configure the handler to access information in [OAuth2FailureContext](OAuth2FailureContext.html).

Default: Fail with an HTTP 500 Internal Server error and log an exception with the failure context.

### loginHandler

`"loginHandler"`: *Handler [reference](preface.html#definition-reference), required if there are zero or multiple client registrations, optional if there is one client registration*

The handler to invoke when the user must select a registered identity provider for login. When `registrations` contains only one client registration, this handler is optional but is displayed if specified.

Provide the name of a [Handler](Handlers.html) object defined in the heap or an inline handler configuration object.

When you use `loginHandler` in AuthorizationCodeOAuth2ClientFilter, retrieve the original target URI for the request from `${contexts.idpSelectionLogin.originalUri}`. Learn more in [IdpSelectionLoginContext](IdpSelectionLoginContext.html).

### registrations

`"registrations"`: *array of ClientRegistration [references](preface.html#definition-reference) optional*

List of client registrations to authenticate PingGateway to the Authorization Server.

The value represents a static [ClientRegistration](ClientRegistration.html) with an Authorization Server.

### metadata

`"metadata"`: *<[object](preface.html#definition-object)>, required for dynamic client registration and ignored otherwise*

The values of the object are evaluated as configuration expression<[strings](preface.html#definition-string)>.

This object holds the client metadata described in [OpenID Connect Dynamic Client Registration 1.0](https://openid.net/specs/openid-connect-registration-1_0.html#ClientMetadata) and optionally a list of scopes.

This object can also hold the client metadata described in RFC 7591, [OAuth 2.0 Dynamic Client Registration Protocol](https://www.rfc-editor.org/rfc/rfc7591).

The following partial list of metadata fields isn't exhaustive. It includes metadata that is useful with AM as OpenID Provider:

* `"redirect_uris"`: *array of configuration expression<[url](preface.html#definition-url)>, required*

  The array of redirection URIs to use when dynamically registering this client.

  One of the registered values **must** match the `clientEndpoint`.

* `"client_name"`: *configuration expression<[string](preface.html#definition-string)>, optional*

  Name of the client to present to the end user.

* `"scope"`: *\_configuration expression<[string](preface.html#definition-string)>, optional*

  Space-separated string of scopes to request of the OpenID Provider, for example:

  ```none
  "scope": "openid profile"
  ```

  This property is available for dynamic client registration with AM and with Authorization Servers that support RFC 7591, [OAuth 2.0 Dynamic Client Registration Protocol](https://www.rfc-editor.org/rfc/rfc7591).

* `"pkce_method"`: *configuration expression<[string](preface.html#definition-string)>, optional*

  The [Proof Key for Code Exchange (PKCE)](https://www.rfc-editor.org/rfc/rfc7636.html) code challenge method; one of:

  * `S256`: Use a SHA256-based encoding of the code verifier.

  * `none`: Disable PKCE.

  Default: `S256`

### cacheExpiration

`"cacheExpiration"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

Duration for which to cache user-info resources.

PingGateway lazily fetches user info from the OpenID provider. In other words,PingGateway only fetches the information when a downstream Filter or Handler uses the user info. Caching allows PingGateway to avoid repeated calls to OpenID providers when reusing the information over a short period.

Set this to disabled or zero to disable caching. When caching is disabled, user info is still lazily fetched.

Default: 10 minutes

### draftMixUpMitigation

`"draftMixUpMitigation"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

|   |                                                    |
| - | -------------------------------------------------- |
|   | This feature requires PingGateway 2026.6 or later. |

Whether to enable the mitigation of OAuth 2.0 mix-up attacks as described in [OAuth 2.0 Mix-Up Mitigation](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-mix-up-mitigation-01) (draft 1). If enabled, PingGateway adds the mitigation data to the `"state"` parameter as described in the draft.

Advanced Identity Cloud and AM support this Internet-Draft as an optional OAuth 2.0 authorization server (AS) feature. Set this property to `true` to enable the mitigation in PingGateway when the AS supports the feature.

Default: false

### executor

`"executor"`: *ScheduledExecutorService [reference](preface.html#definition-reference), optional*

A [ScheduledExecutorService](ScheduledExecutorService.html) to schedule the execution of tasks, such as the eviction of entries in the OpenID Connect user information cache.

Default: `ScheduledExecutorService`

### defaultLoginGoto

`"defaultLoginGoto"`: *runtime expression<[url](preface.html#definition-url)>,optional*

After successful authentication and authorization, if the user accesses the `clientEndpoint/login` endpoint without providing a landing page URL in the `goto` parameter, the request is redirected to this URI.

The goto URL must use the same scheme, host, and port as the original URI, or be a relative URI (just the path). Otherwise, the request fails with an error.

To redirect a request to a site that doesn't meet the goto URL criteria, change the original URI with a [ForwardedRequestFilter](ForwardedRequestFilter.html).

The result of the expression must be a string that represents a valid URI, but isn't a real `java.net.URI` object. For example, it would be incorrect to use `${request.uri}`, which is not a String but a MutableUri.

Default: return an empty page.

### defaultLogoutGoto

`"defaultLogoutGoto"`: *runtime expression<[url](preface.html#definition-url)>,optional*

If the user accesses the `clientEndpoint/logout` endpoint without providing a goto URL, the request is redirected to this URI.

The goto URL must use the same scheme, host, and port as the original URI, or be a relative URI (just the path). Otherwise, the request fails with an error.

To redirect a request to a site that doesn't meet the goto URL criteria, change the original URI with a [ForwardedRequestFilter](ForwardedRequestFilter.html).

The result of the expression must be a string that represents a valid URI, but is not a real `java.net.URI` object. For example, it would be incorrect to use `${request.uri}`, which is not a String but a MutableUri.

Default: return an empty page.

### requireHttps

`"requireHttps"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

Whether to require that original target URI of the request uses the HTTPS scheme.

If the received request doesn't use HTTPS, it is rejected.

Default: `true`

### requireLogin

`"requireLogin"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

Whether to require authentication for all incoming requests.

Default: `true`

### revokeOauth2TokenOnLogout

`"revokeOauth2TokenOnLogout"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

When `true`, call the `revocationEndpoint` defined in [Issuer](Issuer.html) to revoke the access token or refresh token issued by the Authorization Server during login.

If this property is `false` or if `revocationEndpoint` in Issuer isn't defined, PingGateway doesn't revoke the tokens.

Processing errors generate warnings in the logs but don't break the logout flow.

Default: `false`

### openIdEndSessionOnLogout

`"openIdEndSessionOnLogout"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

When `true`, redirect the user to the `endSessionEndpoint` defined in [Issuer](Issuer.html) to log the user out of the Authorization Server. Use this property to initiate logout from an OpenID Connect resource provider.

If this property is `false` or if `endSessionEndpoint` in Issuer isn't defined, PingGateway doesn't redirect the user to log the user out of the Authorization Server.

If the user accesses the `endSessionEndpoint` endpoint without providing a goto URL, PingGateway redirects the request to the `defaultLogoutGoto`.

Learn more in [OpenID Connect Session Management](https://openid.net/specs/openid-connect-session-1_0-10.html).

Default: `false`

### prompt

`"prompt"`: *configuration expression<[string](preface.html#definition-string)>, optional*

A space-separated, case-sensitive list of strings that indicate whether to prompt the end user for authentication and consent. Use in [OIDC flows](https://openid.net/specs/openid-connect-core-1_0.html) only.

Read the Authorization Server documentation for information about supported `prompt` values. For example, learn more in [prompt](https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-parameters.html#prompt) in the PingOne Advanced Identity Cloud documentation or [prompt](https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-parameters.html#prompt) in the AM documentation.

PingGateway provides the following values:

* `none`: Don't display authentication or consent pages. Don't use this value in the same list as `login`, `consent`, or `select_account`.

* `login`: Prompt the end user to reauthenticate even if they have a valid session on the Authorization Server.

* `consent`: Prompt the end user to consent before returning information to the client, even if they have already consented in the session.

* `select_account`: Prompt the end user to select a user account.

Prompt the end user to reauthenticate

```none
"prompt": "login"
```

Prompt the end user to reauthenticate and consent

```none
"prompt": "login consent"
```

### issuerRepository (deprecated)

`"issuerRepository"`: *Issuer repository [reference](preface.html#definition-reference), optional*

A repository of OAuth 2.0 issuers, built from discovered issuers and the PingGateway configuration.

|   |                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The [IssuerRepository (deprecated)](IssuerRepository.html) is deprecated.For issuers known in advance, add their settings to the [ClientRegistration](ClientRegistration.html).For discovery, if the `IssuerRepository` had an `"issuerHandler"`, configure an `AuthorizationCodeOAuth2ClientFilter` `"discoveryHandler"` instead. |

Provide the name of an IssuerRepository object defined in the heap.

Default: Look up an issuer repository named `IssuerRepository` in the heap. If none is explicitly defined, a default one named `IssuerRepository` is created in the current route.

### useDeprecatedIssuerRepository (deprecated)

`"useDeprecatedIssuerRepository"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

Whether to use the deprecated default `"IssuerRepository"` from the heap.

|   |                              |
| - | ---------------------------- |
|   | This property is deprecated. |

* `true`: When the `"issuerRepository"` isn't set, use the deprecated default `"IssuerRepository"` from the heap.

* `false`: When the `"issuerRepository"` isn't set, don't use the deprecated default `"IssuerRepository"` and don't share registered or discovered issues with any [AuthorizationCodeOAuth2ClientFilter](AuthorizationCodeOAuth2ClientFilter.html)s.

Default: `false`

### discoveryHandler

`"discoveryHandler"`: *Handler [reference](preface.html#definition-reference), optional*

Use this property for discovery and dynamic registration of OpenID Connect clients.

Provide either the name of a Handler object defined in the heap or an inline [Handler](Handlers.html) configuration object. Usually, set this to the name of a [ClientHandler](ClientHandler.html) configured in the heap or a [Chain](Chain.html) that ends in a ClientHandler.

Default: The default ClientHandler.

### discoverySecretId

`"discoverySecretId"`: *configuration expression<[secret-id](preface.html#definition-secretid)>, required for discovery and dynamic registration*

Use this property for discovery and dynamic registration of OAuth 2.0 clients.

This secret ID must point to a [CryptoKey](../security-guide/keys.html#secret-types).

This specifies the secret ID of the secret used to sign a JWT before the JWT is sent to the Authorization Server.

If `discoverySecretId` is used, then the `tokenEndpointAuthMethod` is always `private_key_jwt`.

### tokenEndpointAuthMethod

`"tokenEndpointAuthMethod"`: *configuration expression<[enumeration](preface.html#definition-enumeration)>, optional*

Use this property for discovery and dynamic registration of OAuth 2.0 clients.

The authentication method with which a client authenticates to the authorization server or OpenID provider at the token endpoint. Learn about client authentication methods in the OpenID document on [Client Authentication](https://openid.net/specs/openid-connect-core-1_0.html#ClientAuthentication).

The following client authentication methods are allowed:

* `client_secret_basic`: Clients that have received a `client_secret` value from the Authorization Server authenticate with the Authorization Server with HTTP basic access authentication:

  ```http
  POST /oauth2/token HTTP/1.1
  Host: as.example.com
  Authorization: Basic ....
  Content-Type: application/x-www-form-urlencoded

  grant_type=authorization_code&
  code=...
  ```

* `client_secret_post`: Clients that have received a `client_secret` value from the Authorization Server authenticate with the Authorization Server with the client credentials in the request body:

  ```http
  POST /oauth2/token HTTP/1.1
  Host: as.example.com
  Content-Type: application/x-www-form-urlencoded

  grant_type=authorization_code&;
  client_id=...&
  client_secret=...&
  code=...
  ```

* `private_key_jwt`: Clients send a signed JSON Web Token (JWT) to the Authorization Server. PingGateway builds and signs the JWT and prepares the request:

  ```http
  POST /token HTTP/1.1
  Host: as.example.com
  Content-Type: application/x-www-form-urlencoded

  grant_type=authorization_code&
  code=...&
  client_id=<clientregistration_id>&
  client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&
  client_assertion=PHNhbWxwOl ... ZT
  ```

  If the Authorization Server doesn't support `private_key_jwt`, the dynamic registration falls back on the method returned by the Authorization Server; for example, `client_secret_basic` or `client_secret_post`.

  If `tokenEndpointAuthSigningAlg` is not configured, the `RS256` signing algorithm is used for `private_key_jwt`.

Consider these points for identity providers:

* Some providers accept more than one authentication method.

* If a provider strictly enforces how the client must authenticate, align the authentication method with the provider.

* If a provider doesn't support the authentication method, the provider sends an HTTP 400 Bad Request response with an `invalid_client` error message, according to [RFC 6749: Error Response](https://www.rfc-editor.org/rfc/rfc6749#section-5.2).

* If the authentication method is invalid, the provider sends an `IllegalArgumentException`.

Default: If `discoverySecretId` is used, then the `tokenEndpointAuthMethod` is always `private_key_jwt`. Otherwise, it is `client_secret_basic`.

### tokenEndpointAuthSigningAlg

`"tokenEndpointAuthSigningAlg"`: *configuration expression<[string](preface.html#definition-string)>, optional*

The JSON Web Algorithm (JWA) used to sign the JWT that is used to authenticate the client at the token endpoint. The property is used when `private_key_jwt` is used for authentication.

If the Authorization Server sends a notification to use a different algorithm to sign the JWT, that algorithm is used.

Default: If `discoverySecretId` is used, then the `tokenEndpointAuthSigningAlg` is `RS256`. Otherwise, it is not used.

### oAuth2SessionKey

`"oAuth2SessionKey"`: *configuration expression<[string](preface.html#definition-string)>, optional*

A key to identify an OAuth 2.0 session. The key can be any character string.

To share the same OAuth 2.0 session when a user accesses different applications protected by PingGateway, use the same key in each filter.

Default: The complete client endpoint URI. AuthorizationCodeOAuth2ClientFilters don't share OAuth 2.0 sessions.

### secretsProvider

`"secretsProvider"`: *SecretsProvider [reference](preface.html#definition-reference), required if `discoverySecretId` is used*

The [SecretsProvider](SecretsProvider.html) to query for passwords and cryptographic keys.

## Examples

You can find more information in the following pages:

* [AM as OIDC provider](../gateway-guide/oidc-am.html)

* [Multiple OIDC providers using PingAM and PingOne Advanced Identity Cloud](../gateway-guide/oidc-nascar.html)

* [Discovery and dynamic registration with PingAM](../gateway-guide/oidc-dynamic.html)

## More information

[org.forgerock.openig.filter.oauth2.client.AuthorizationCodeOAuth2ClientFilter](../_attachments/apidocs/org/forgerock/openig/filter/oauth2/client/AuthorizationCodeOAuth2ClientFilter.html)

[Issuer](Issuer.html)

[ClientRegistration](ClientRegistration.html)

[The OAuth 2.0 Authorization Framework](https://www.rfc-editor.org/rfc/rfc6749)

[The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://www.rfc-editor.org/rfc/rfc6750)

[OpenID Connect](https://openid.net/developers/how-connect-works/) site, in particular the list of standard OpenID Connect 1.0 [scope values](https://openid.net/specs/openid-connect-basic-1_0.html#Scopes).

---

---
title: AuthRedirectContext
description: Reference for AuthRedirectContext, used in PingGateway to track pending login redirects and manage query parameters on redirect URIs
component: pinggateway
version: 2026
page_id: pinggateway:reference:AuthRedirectContext
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/AuthRedirectContext.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-06-02T18:01:47Z
section_ids:
  AuthRedirectContext-properties: Properties
  AuthRedirectContext-moreinfo: More information
---

# AuthRedirectContext

Used by the following filters to indicate that a login redirect is pending:

* [FragmentFilter](FragmentFilter.html)

* [DataPreservationFilter](DataPreservationFilter.html)

This context isn't intended for use in scripts or extensions.

For a single request there must be at most one instance of AuthRedirectContext in the context hierarchy. Confirm for the presence of an AuthRedirectContext before adding a new instance or adding query parameters to an existing instance.

The context is named `AuthRedirectAwareContext`, and is accessible at `${contexts.AuthRedirectContext}`.

## Properties

* `"impendingIgRedirectNotified"`: *boolean*

  Returns `true` if a PingGateway redirect attempt is pending. Otherwise, returns `false`.

* `"notifyImpendingIgRedirectAndUpdateUri"`: *URI*

  Notifies that a PingGateway redirection has been attempted, and returns an updated URI as follows:

  * If no query parameters are added to the context, return the original URI.

  * If query parameters are added to the context, apply them to the URI and return an updated URI.

  * If the added query parameters have the same name as existing query parameters, replace the existing parameters and return an updated URI.

  For example, a request to `example.com/profile` triggers a login redirect to `example.com/login`. After authentication, the request is expected to be redirected to the original URI, `example.com/profile`.

* `"addQueryParameter"`: *[java.lang.String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html)*

  Adds a query parameter to the context, for use by `notifyImpendingIgRedirectAndUpdateUri`.

## More information

[org.forgerock.openig.filter.AuthRedirectContext](../_attachments/apidocs/org/forgerock/openig/filter/AuthRedirectContext.html)

---

---
title: Base64EncodedSecretStore
description: Configure Base64EncodedSecretStore to manage base64-encoded secrets hard-coded in PingGateway routes, for testing and evaluation only
component: pinggateway
version: 2026
page_id: pinggateway:reference:Base64EncodedSecretStore
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/Base64EncodedSecretStore.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-06-02T18:01:47Z
section_ids:
  Base64EncodedSecretStore-usage: Usage
  Base64EncodedSecretStore-properties: Properties
  Base64EncodedSecretStore-log: Log level
  Base64EncodedSecretStore-example: Example
  Base64EncodedSecretStore-moreinfo: More information
---

# Base64EncodedSecretStore

Manage a repository of generic secrets, such as passwords or simple shared secrets, whose values are base64-encoded, and hard-coded in the route.

This Secret store can only manage the [GenericSecret](../security-guide/keys.html#secret-types) type.

The secrets provider queries the Base64EncodedSecretStore for a named secret, identified by the `secret-id` in the `"secret-id": "string"` pair. The Base64EncodedSecretStore returns the matching secret.

The secrets provider builds the secret, checking that the secret's constraints are met, and returns a unique secret. If the secret's constraints aren't met, the secrets provider cannot build the secret and the secret query fails.

Secrets from Base64EncodedSecretStore never expire.

|   |                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use Base64EncodedSecretStore for testing or evaluation only, to store passwords locally. In production, use an alternative secret store. |

Learn how PingGateway manages secrets in [About secrets](../security-guide/keys.html#about-secrets).

## Usage

```json
{
  "name": string,
  "type": "Base64EncodedSecretStore",
  "config": {
    "secrets": map or configuration expression<map>
  }
}
```

## Properties

* `"secrets"`: *[map](preface.html#definition-map) or configuration expression\<map>, required*

  Map of one or more data pairs with the format `Map<String, String>`, where:

  * The key is the ID of a secret used in a route

  * The value is the base64-encoded value of a secret, or a configuration expression that evaluates to the base64-encoded value of a secret

  The following formats are allowed:

  ```json
  {
    "secrets": {
      "secret-id": "configuration expression<string>",
      ...
    }
  }
  ```

  ```json
  {
    "secrets": "configuration expression<map>"
  }
  ```

  In the following example, the property is a map whose values are provided by strings:

  ```json
  {
    "type": "Base64EncodedSecretStore",
    "config": {
      "secrets": {
        "agent.password": "d2VsY29tZQ==",
        "crypto.header.key": "Y2hhbmdlaXQ="
      }
    }
  }
  ```

  In the following example, the property is a map whose values are provided by a configuration token and a configuration expression. The values are substituted when the route is loaded:

  ```json
  {
    "type": "Base64EncodedSecretStore",
    "config": {
      "secrets": {
        "agent.password": "&{secret.value|aGVsbG8=}",
        "crypto.header.key": "${readProperties('file.property')['b64.key.value']}"
      }
    }
  }
  ```

## Log level

To facilitate debugging secrets for the Base64EncodedSecretStore, in `logback.xml` add a logger defined by the fully qualified package name of the Base64EncodedSecretStore. The following line in `logback.xml` sets the log level to `ALL`:

```xml
<logger name="org.forgerock.openig.secrets.Base64EncodedSecretStore" level="ALL" />
```

## Example

For an example that uses Base64EncodedSecretStore, refer to `client-credentials.json` in [Client credentials grant with PingAM](../gateway-guide/oauth2-clientcredentials.html).

## More information

[Secrets](secrets.html)

[org.forgerock.openig.secrets.Base64EncodedSecretStore](../_attachments/apidocs/org/forgerock/openig/secrets/Base64EncodedSecretStore.html)

---

---
title: BaseUriDecorator
description: Configure BaseUriDecorator in PingGateway to override the scheme, host, and port of a request URI, rebasing requests to a new base URI
component: pinggateway
version: 2026
page_id: pinggateway:reference:BaseUriDecorator
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/BaseUriDecorator.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-06-02T18:01:47Z
section_ids:
  BaseUriDecorator-usage-decorator: Decorator Usage
  BaseUriDecorator-usage-object: Decorated Object Usage
  BaseUriDecorator-example: Examples
  BaseUriDecorator-moreinfo: More information
---

# BaseUriDecorator

Overrides the scheme, host, and port of the existing request URI, rebasing the URI and so making requests relative to a new base URI. Rebasing changes only the scheme, host, and port of the request URI. Rebasing doesn't affect the path, query string, or fragment.

## Decorator Usage

```json
{
    "name": string,
    "type": "BaseUriDecorator"
}
```

A BaseUriDecorator doesn't have configurable properties.

PingGateway creates a default BaseUriDecorator named baseURI at startup time in the top-level heap, so you can use baseURI as the decorator name without adding the decorator declaration

## Decorated Object Usage

```json
{
    "name": string,
    "type": string,
    "config": object,
    decorator name: runtime expression<url>
}
```

* `"name"`: *[string](preface.html#definition-string), required except for inline objects*

  The unique name of the object, just like an object that isn't decorated.

* `"type"`: *<[string](preface.html#definition-string)>, required*

  The class name of the decorated object, which must be either a [PingGateway filters](Filters.html) or a [PingGateway handlers](Handlers.html).

* `"config"`: [object](preface.html#definition-object) required unless empty

  The configuration of the object, just like an object that isn't decorated

* decorator name: runtime expression<[url](preface.html#definition-url)>, required

  The scheme, host, and port of the new base URI. The port is optional when using the defaults (80 for HTTP, 443 for HTTPS).

  The value of the string must not contain underscores, and must conform to the syntax specified in [RFC 3986](https://www.ietf.org/rfc/rfc3986.txt).

## Examples

Add a custom decorator to the heap named myBaseUri:

```json
{
    "name": "myBaseUri",
    "type": "BaseUriDecorator"
}
```

Set a Router's base URI to `https://www.example.com:8443`:

```json
{
    "name": "Router",
    "type": "Router",
    "myBaseUri": "https://www.example.com:8443/"
}
```

## More information

[org.forgerock.openig.decoration.baseuri.BaseUriDecorator](../_attachments/apidocs/org/forgerock/openig/decoration/baseuri/BaseUriDecorator.html)

---

---
title: CacheAccessTokenResolver
description: Configure Caffeine-based caching of OAuth 2.0 access tokens in PingGateway, delegating resolution to another AccessTokenResolver
component: pinggateway
version: 2026
page_id: pinggateway:reference:CacheAccessTokenResolver
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/CacheAccessTokenResolver.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2024-07-10T14:05:34Z
section_ids:
  CacheAccessTokenResolver-usage: Usage
  CacheAccessTokenResolver-properties: Properties
  CacheAccessTokenResolver-example: Example
---

# CacheAccessTokenResolver

Enable and configure caching of OAuth 2.0 access tokens, based on *Caffeine*. For more information, refer to the GitHub entry, [Caffeine](https://github.com/ben-manes/caffeine).

This resolver configures caching of OAuth 2.0 access tokens, and delegates their resolution to another AccessTokenResolver. Use this resolver with AM or any OAuth 2.0 access token provider.

For an alternative way to cache OAuth 2.0 access tokens, configure the `cache` property of OAuth2ResourceServerFilter.

## Usage

```json
{
  "name": string,
  "type": "CacheAccessTokenResolver",
  "config": {
    "delegate": AccessTokenResolver reference,
    "enabled": configuration expression<boolean>,
    "defaultTimeout": configuration expression<duration>,
    "executor": Executor reference,
    "maximumSize": configuration expression<number>,
    "maximumTimeToCache": configuration expression<duration>,
    "amService": AmService reference,
    "onNotificationDisconnection": configuration expression<enumeration>
  }
}
```

## Properties

* `"delegate"`: *AccessTokenResolver [reference](preface.html#definition-reference), required*

  Delegate access token resolution to one of the access token resolvers in [PingGateway access token resolvers](AccessTokenResolvers.html).

  To use AM WebSocket notification to evict revoked access tokens from the cache, the delegate must be able to provide the token metadata required to update the cache.

  * The `notification` property of AmService is enabled.

  * The delegate AccessTokenResolver provides the token metadata required to update the cache.

* `enabled`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

  Enable caching.

  When an access token is cached, PingGateway can reuse the token information without repeatedly asking the Authorization Server to verify the access token. When caching is disabled, PingGateway must ask the Authorization Server to validate the access token for each request.

  Default: `true`

* `defaultTimeout`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

  The duration for which to cache an OAuth 2.0 access token when it doesn't provide a valid expiry value or `maximumTimeToCache`.

  If the `defaultTimeout` is longer than the `maximumTimeToCache`, then the `maximumTimeToCache` takes precedence.

  Default: `1 minute`

* `"executor"`: *Executor [reference](preface.html#definition-reference), optional*

  An executor service to schedule the execution of tasks, such as the eviction of entries from the cache.

  Default: `ForkJoinPool.commonPool()`

* `"maximumSize"`: *configuration expression<[number](preface.html#definition-number)>, optional*

  The maximum number of entries the cache can contain.

  Default: Unlimited/unbound

* `"maximumTimeToCache"`: *configuration expression<[duration](preface.html#definition-duration)>, optional*

  The maximum duration for which to cache access tokens.

  Cached access tokens are expired according to their expiry time and `maximumTimeToCache`, as follows:

  * If the expiry time is *before* the current time plus the `maximumTimeToCache`, the cached token is expired when the expiry time is reached.

  * If the expiry time is *after* the current time plus the `maximumTimeToCache`, the cached token is expired when the `maximumTimeToCache` is reached

    The duration cannot be `zero` or `unlimited`.

  Default: The token expiry time or `defaultTimeout`

* `"amService"`: *AmService [reference](preface.html#definition-reference), optional*

  An AmService to use for the WebSocket notification service.

  When an access token is revoked on AM, the CacheAccessTokenResolver can delete the token from the cache when both of the following conditions are true:

  * The `notification` property of AmService is enabled.

  * The delegate AccessTokenResolver provides the token metadata required to update the cache.

    When a refresh\_token is revoked on AM, all associated access tokens are automatically and immediately revoked.

  See also [AmService](AmService.html).

* `onNotificationDisconnection`: *configuration expression<[enumeration](preface.html#definition-enumeration)>, optional*

  An `amService` must be configured for this property to have effect.

  The strategy to manage the cache when the WebSocket notification service is disconnected, and PingGateway receives no notifications for AM events. If the cache is not cleared it can become outdated, and PingGateway can allow requests on revoked sessions or tokens.

  Cached entries that expire naturally while the notification service is disconnected are removed from the cache.

  Use one of the following values:

  * `NEVER_CLEAR`

    * When the notification service is disconnected:

      * Continue to use the existing cache.

      * Deny access for requests that aren't cached, but don't update the cache with these requests.

    * When the notification service is reconnected:

      * Continue to use the existing cache.

      * Query AM for incoming requests that aren't found in the cache, and update the cache with these requests.

  * `CLEAR_ON_DISCONNECT`

    * When the notification service is disconnected:

      * Clear the cache.

      * Deny access to all requests, but don't update the cache with these requests.

    * When the notification service is reconnected:

      * Query AM for all requests that aren't found in the cache. (Because the cache was cleared, the cache is empty after reconnection.)

      * Update the cache with these requests.

  * `CLEAR_ON_RECONNECT`

    * When the notification service is disconnected:

      * Continue to use the existing cache.

      * Deny access for requests that aren't cached, but don't update the cache with these requests.

    * When the notification service is reconnected:

      * Query AM for all requests that aren't found in the cache. (Because the cache was cleared, the cache is empty after reconnection.)

      * Update the cache with these requests.

  Default: `CLEAR_ON_DISCONNECT`

## Example

For an example that uses the CacheAccessTokenResolver, refer to [Caching PingAM access tokens](../gateway-guide/oauth2-rs-cacheatr.html).

---

---
title: CachingJwkSetService
description: Configure CachingJwkSetService in PingGateway to cache a JWK set from a URI, with configurable timeout and cache size
component: pinggateway
version: 2026
page_id: pinggateway:reference:CachingJwkSetService
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/CachingJwkSetService.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-06-02T18:01:47Z
section_ids:
  usage: Usage
  properties: Properties
  more_information: More information
---

# CachingJwkSetService

Service for caching a JWK set from a URI.

## Usage

```none
{
  "name": string,
  "type": "CachingJwkSetService",
  "config": {
    "endpointHandler": Handler reference,
    "cacheTimeout": configuration expression<duration>,
    "cacheMissTimeout": configuration expression<duration>,
    "cacheMaxSize": configuration expression<number>
  }
}
```

## Properties

* `"endpointHandler"`: *IdmService [reference](preface.html#definition-reference), optional*

  The [Handler](Handlers.html) to use to get the JWK set.

  Default: The default [ForgeRockClientHandler](ForgeRockClientHandler.html)

* `"cacheTimeout"`: *[duration](preface.html#definition-duration), optional*

  Reload the cache after this duration.

  Default: 2 minutes

* `"cacheMissTimeout"`: *[duration](preface.html#definition-duration), optional*

  Reload the cache after this duration when a JWK isn't found in the cache.

  Default: 2 minutes

* `"cacheMaxSize"`: *[number](preface.html#definition-number), optional*

  The maximum number of JWKs in the cache.

  Default: 500

## More information

[org.forgerock.openig.fapi.jwks.CachingJwkSetService](../_attachments/apidocs/org/forgerock/openig/fapi/jwks/CachingJwkSetService.html)

---

---
title: CaptureDecorator
description: Configure the CaptureDecorator to capture HTTP request and response messages, entities, and context in PingGateway SLF4J logs, with header masking support
component: pinggateway
version: 2026
page_id: pinggateway:reference:CaptureDecorator
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/CaptureDecorator.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-06-02T18:01:47Z
section_ids:
  CaptureDecorator-usage-decorator: Decorator Usage
  CaptureDecorator-usage-object: Decorated Object Usage
  CaptureDecorator-example: Examples
  CaptureDecorator-example-entity: Log the entity
  CaptureDecorator-example-noentity: Don't log the entity
  CaptureDecorator-example-context: Log the context
  CaptureDecorator-example-entity-req-resp: Log requests and responses with the entity
  CaptureDecorator-example-transformed: Capture transformed requests and responses
  CaptureDecorator-example-json: Capture the context as JSON
  CaptureDecorator-moreinfo: More information
---

# CaptureDecorator

Captures request and response messages in SLF4J logs, named in this format:

```none
org.forgerock.openig.decoration.capture.CaptureDecorator.<decoratorName>.<decoratedObjectName>
```

If the decorated object isn't named, the object path is used in the log.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When debugging, use a `CaptureDecorator` to capture and log details of requests and responses.Be aware increased logging consumes resources, such as disk space, and can cause performance issues.In production deployments, avoid setting `"captureEntity": true`. This causes PingGateway to log the entire body, including sensitive data. Usually, `"captureContext": true` logs sufficient information to debug problems. If it isn't needed, reduce logging further by setting `"captureContext": false`. |

You can find more information about using default or custom logging in [Managing PingGateway logs](../maintenance-guide/logging.html).

## Decorator Usage

```json
{
  "name": string,
  "type": "CaptureDecorator",
  "config": {
    "captureEntity": configuration expression<boolean>,
    "captureContext": configuration expression<boolean>,
    "maxEntityLength": configuration expression<number>,
    "masks": object
  }
}
```

* `"captureEntity"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

  A flag for capture of the message entity:

  * `true`: Capture the request and response message entity and write it to the logs. The message entity is the body of the HTTP message, which can be a JSON document, XML, HTML, image, or other information.

    When the message is binary, PingGateway writes a `[binary entity]`.

    When streaming is enabled in [admin.json](AdminHttpApplication.html), the decorator interrupts streaming for the captured request or response until the whole entity is captured.

  * `false`: Don't capture the message entity.

  If the `Content-Type` header is set for a request or response, the decorator uses it to decode the request or response messages, and then writes them to the logs. If the `Content-Type` header isn't set, the decorator doesn't write the request or response messages to the logs.

  Default: `false`

* `"captureContext"`: *configuration expression<[boolean](preface.html#definition-boolean)>, optional*

  A flag for capture of contextual data about the handled request, such as client, session, authentication identity, authorization identity, or any other state information associated with the request:

  * `true`: Capture contextual data about the handled request.

    The context is captured as JSON. The context chain is used when processing the request inside PingGateway in the filters and handlers.

  * `false`: Don't capture contextual data about the handled request.

  Default: `false`

* `"maxEntityLength"`: *configuration expression<[number](preface.html#definition-number)>, optional*

  The maximum number of bytes that can be captured for an entity. This property is used when `captureEntity` is `true`.

  If the captured entity is bigger than `maxEntityLength`, everything up to `maxEntityLength` is captured, and an `[entity truncated]` message is written in the log.

  Set `maxEntityLength` to be big enough to allow capture of normal entities, but small enough to prevent excessive memory use or `OutOfMemoryError` errors. Setting `maxEntityLength` to 2 GB or more causes an exception at startup.

  Default: 524 288 bytes (512 KB)

* `"masks"`: *[object](preface.html#definition-object), optional*

  The configuration to mask the values of headers and attributes in the logs.

  ```json
  {
    "masks": {
      "headers": [ pattern, ... ],
      "trailers": [ pattern, ... ]
      "attributes": [ pattern, ... ]
      "mask": [ configuration expression<string>, ... ]
    }
  }
  ```

  * `"headers"`: *array of [patterns](preface.html#definition-pattern), optional*

    The case-insensitive name of one or more headers whose value to mask in the logs.

    The following value masks headers called `X-OpenAM-Username`, `X-OpenAM-Password` and `x-openam-token`:

    ```json
    "headers": ["X-OpenAM-.*"]
    ```

    Default: None

  * `"trailers"`: *array of [patterns](preface.html#definition-pattern), optional*

    The case-insensitive name of one or more trailers whose value to mask in the logs.

    The following value masks trailers called `Expires`:

    ```json
    "trailers": ["Expires"]
    ```

    Default: None

  * `"attributes"`: *array of [patterns](preface.html#definition-pattern), optional*

    The case-insensitive name of one or more attributes whose value to mask in the logs.

    Default: None

  * `"mask"`: *configuration expression<[string](preface.html#definition-string)>, optional*

    Text to replace the masked header value or attribute value in the logs.

    Default: `*****`

## Decorated Object Usage

```json
{
    "name": string,
    "type": string,
    "config": object,
    decorator name: capture point(s)
}
```

* `"name"`: *[string](preface.html#definition-string), required except for inline objects*

  The unique name of the decorated object.

* `"type"`: *[string](preface.html#definition-string), required except for inline objects*, required\_

  The class name of the decorated object, which must be either a Filter or a Handler. See also [PingGateway filters](Filters.html) and [PingGateway handlers](Handlers.html).

* `"config"`: [object](preface.html#definition-object) required unless empty

  The configuration of the decorated object, as documented in the object reference page.

* decorator name: capture point(s), optional

  The decorator name must match the name of the CaptureDecorator. For example, if the CaptureDecorator has `"name": "capture"`, then decorator name is `capture`.

  The capture point(s) are either a single string, or an array of strings. The strings are documented here in lowercase, but aren't case-sensitive:

  * `"all"`

    Capture at all available capture points.

  * `"none"`

    Disable capture. If `none` is configured with other capture points, `none` takes precedence.

  * `"request"`

    Capture the request as it enters the Filter or Handler.

  * `"filtered_request"`

    Capture the request as it leaves the Filter. Only applies to Filters.

  * `"response"`

    Capture the response as it enters the Filter or leaves the Handler.

  * `"filtered_response"`

    Capture the response as it leaves the Filter. Only applies to Filters.

## Examples

### Log the entity

The following example decorator is configured to log the entity:

```json
{
    "name": "capture",
    "type": "CaptureDecorator",
    "config": {
        "captureEntity": true
    }
}
```

### Don't log the entity

The following example decorator is configured not to log the entity:

```json
{
  "name": "capture",
  "type": "CaptureDecorator"
}
```

### Log the context

The following example decorator is configured to log the context in JSON format, excluding the request and the response:

```json
{
  "name": "capture",
  "type": "CaptureDecorator",
  "config": {
    "captureContext": true
  }
}
```

### Log requests and responses with the entity

The following example decorator is configured to log requests and responses with the entity, before sending the request and before returning the response:

```json
{
  "heap": [
    {
      "name": "capture",
      "type": "CaptureDecorator",
      "config": {
        "captureEntity": true
      }
    },
    {
      "name": "ReverseProxyHandler",
      "type": "ReverseProxyHandler",
      "capture": [
        "request",
        "response"
      ]
    }
  ],
  "handler": "ReverseProxyHandler"
}
```

### Capture transformed requests and responses

The following example uses the default CaptureDecorator to capture transformed requests and responses, as they leave filters:

```json
{
  "handler": {
    "type": "Chain",
    "config": {
      "filters": [{
        "type": "HeaderFilter",
        "config": {
          "messageType": "REQUEST",
          "add": {
            "X-RequestHeader": [
              "Capture at filtered_request point",
              "And at filtered_response point"
            ]
          }
        }
      },
        {
          "type": "HeaderFilter",
          "config": {
            "messageType": "RESPONSE",
            "add": {
              "X-ResponseHeader": [
                "Capture at filtered_response point"
              ]
            }
          }
        }
      ],
      "handler": {
        "type": "StaticResponseHandler",
        "config": {
          "status": 200,
          "headers": {
            "Content-Type": [ "text/html; charset=UTF-8" ]
          },
          "entity": "<html><body><p>Hello world!</p></body></html>"
        }
      }
    }
  },
  "capture": [
    "filtered_request",
    "filtered_response"
  ]
}
```

### Capture the context as JSON

The following example captures the context as JSON, excluding the request and response, before sending the request and before returning the response:

```json
{
  "heap": [
    {
      "name": "capture",
      "type": "CaptureDecorator",
      "config": {
        "captureContext": true
      }
    },
    {
      "name": "ReverseProxyHandler",
      "type": "ReverseProxyHandler",
      "capture": [
        "request",
        "response"
      ]
    }
  ],
  "handler": "ReverseProxyHandler"
}
```

## More information

[org.forgerock.openig.decoration.capture.CaptureDecorator](../_attachments/apidocs/org/forgerock/openig/decoration/capture/CaptureDecorator.html)

---

---
title: CapturedUserPasswordContext
description: CapturedUserPasswordContext provides the decrypted PingAM password of the current user, injected into the context by CapturedUserPasswordFilter
component: pinggateway
version: 2026
page_id: pinggateway:reference:CapturedUserPasswordContext
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/CapturedUserPasswordContext.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-06-02T18:01:47Z
section_ids:
  CapturedUserPasswordContext-properties: Properties
  CapturedUserPasswordContext-moreinfo: More information
---

# CapturedUserPasswordContext

Provides the decrypted AM password of the current user. When the [CapturedUserPasswordFilter](CapturedUserPasswordFilter.html) processes a request, it injects the decrypted password from AM into this context.

## Properties

The context is named `capturedPassword`, and is accessible at `${contexts.capturedPassword}`. The context has the following properties:

* `"raw"`: *byte*

  The decrypted password as bytes.

* `"value"`: *[java.lang.String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html)*

  The decrypted password as a UTF-8 string.

## More information

[org.forgerock.openig.openam.CapturedUserPasswordContext](../_attachments/apidocs/org/forgerock/openig/openam/CapturedUserPasswordContext.html)

---

---
title: CapturedUserPasswordFilter
description: Configure CapturedUserPasswordFilter to retrieve and decrypt a PingAM captured user password and store it in CapturedUserPasswordContext
component: pinggateway
version: 2026
page_id: pinggateway:reference:CapturedUserPasswordFilter
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/CapturedUserPasswordFilter.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-05
section_ids:
  CapturedUserPasswordFilter-usage: Usage
  CapturedUserPasswordFilter-properties: Properties
  CapturedUserPasswordFilter-moreinfo: More information
---

# CapturedUserPasswordFilter

Makes an AM password available to PingGateway in the following steps:

* Checks for the presence of the SessionInfoContext context, at `${contexts.amSession}`.

  * If the context isn't present, or if `sunIdentityUserPassword` is `null`, the CapturedUserPasswordFilter collects session info and properties from AM.

  * If the context is present and `sunIdentityUserPassword` isn't `null`, the CapturedUserPasswordFilter uses that value for the password.

* The CapturedUserPasswordFilter decrypts the password and stores it in the CapturedUserPasswordContext, at `${contexts.capturedPassword}`.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In PingOne Advanced Identity Cloud and from AM 7.5, the password capture and replay feature can optionally manage the replay password through AM's secret service. The secret label for the replay password must be `am.authentication.replaypassword.key`.For backward compatibility, if a secret isn't defined, is empty, or can't be resolved, AM manages the replay password through the AM system property `am.authentication.replaypassword.key`. |

## Usage

```json
{
  "name": string,
   "type": "CapturedUserPasswordFilter",
   "config": {
     "amService": AmService reference,
     "keySecretId": configuration expression<secret-id>,
     "secretsProvider": SecretsProvider reference,
     "ssoToken": runtime expression<string>
   }
}
```

## Properties

* `"amService"`: *AmService [reference](preface.html#definition-reference), required*

  The AmService heap object to use for the password. See also, [AmService](AmService.html).

* `"keySecretId"`: *configuration expression<[secret-id](preface.html#definition-enumeration)>, required*

  The secret ID for the key required decrypt the AM password.

  This secret ID must point to a [CryptoKey](../security-guide/keys.html#secret-types) whose algorithm is AES.

* `"secretsProvider"`: *SecretsProvider [reference](preface.html#definition-reference), required*

  The [SecretsProvider](SecretsProvider.html) to query for secrets to decrypt the user password.

* `"ssoToken"`: *runtime expression<[string](preface.html#definition-string)>, required*

  Location of the AM SSO token.

  Default: `${request.cookiesAmService-ssoTokenHeader'][0].value}`, where `AmService-ssoTokenHeader` is the name of the header or cookie where the AmService expects to find SSO tokens.

## More information

[org.forgerock.openig.openam.CapturedUserPasswordFilter](../_attachments/apidocs/org/forgerock/openig/openam/CapturedUserPasswordFilter.html)

[org.forgerock.openig.openam.CapturedUserPasswordContext](../_attachments/apidocs/org/forgerock/openig/openam/CapturedUserPasswordContext.html)

[CapturedUserPasswordContext](CapturedUserPasswordContext.html)

[SessionInfoFilter](SessionInfoFilter.html)

---

---
title: CdSsoContext
description: Reference for CdSsoContext, which provides cross-domain SSO properties, session ID, and claims set injected by CrossDomainSingleSignOnFilter
component: pinggateway
version: 2026
page_id: pinggateway:reference:CdSsoContext
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/CdSsoContext.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-06-02T18:01:47Z
section_ids:
  CdSsoContext-properties: Properties
  CdSsoContext-moreinfo: More information
---

# CdSsoContext

Provides the cross-domain SSO properties for the CDSSO token, the user ID of the session, and the full claims set. When the [CrossDomainSingleSignOnFilter](CrossDomainSingleSignOnFilter.html) processes a request, it injects the information in this context.

## Properties

The context is named `cdsso`, and is accessible at `${contexts.cdsso}`. The context has the following properties:

* `"claimsSet"`: *[org.forgerock.json.jose.jwt.JwtClaimsSet](../_attachments/apidocs/org/forgerock/json/jose/jwt/JwtClaimsSet.html)*

  Full JwtClaimsSet for the identity of the authenticated user. Cannot be null.

  Access claims as follows:

  * Claims with a getter by using the property name. For example, access `getSubject` with `contexts.cdsso.claimsSet.subject`.

  * All other claims by using the `getClaim` method. For example, access `subname` with `contexts.cdsso.claimsSet.getClaim('subname')`.

* `"cookieInfo"`: *org.forgerock.openig.http.protocol.CookieBuilder*

  Configuration data for the CDSSO authentication cookie, with the following attributes:

  * `name`: Cookie name (string)

  * `domain`: (Optional) Cookie domain (string)

  * `path`: Cookie path (string)

  No attribute can be null.

* `"redirectEndpoint"`: *[java.lang.String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html)*

  Redirect endpoint URI configured for communication with AM. Cannot be null.

* `"sessionUid"`: *[java.lang.String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html)*

  Universal session ID. Cannot be null.

* `"token"`: *[java.lang.String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html)*

  Value of the CDSSO token. Cannot be null.

## More information

[org.forgerock.openig.openam.CdSsoContext](../_attachments/apidocs/org/forgerock/openig/openam/CdSsoContext.html)