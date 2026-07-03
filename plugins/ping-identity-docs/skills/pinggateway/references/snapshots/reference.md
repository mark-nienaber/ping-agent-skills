---
title: About Common REST
description: "Reference for the Common REST API framework: CRUDPAQ verbs, query parameters, pagination, PATCH operations, and HTTP status codes"
component: pinggateway
version: 2026
page_id: pinggateway:reference:AboutCrest
canonical_url: https://docs.pingidentity.com/pinggateway/2026/reference/AboutCrest.html
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
