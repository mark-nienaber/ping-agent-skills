---
title: Create
description: "There are two ways to create a resource: HTTP POST or HTTP PUT."
component: pingoneaic-api
page_id: pingoneaic-api::crest/create
canonical_url: https://developer.pingidentity.com/pingoneaic-api/crest/create.html
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
title: Delete
description: To delete a single resource, perform an HTTP DELETE by its case-sensitive identifier (_id) and accept a JSON response:
component: pingoneaic-api
page_id: pingoneaic-api::crest/delete
canonical_url: https://developer.pingidentity.com/pingoneaic-api/crest/delete.html
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
title: HTTP status codes
description: When working with a Advanced Identity Cloud REST API, client applications should expect at least the following HTTP status codes. Not all services necessarily return all status codes identified here:
component: pingoneaic-api
page_id: pingoneaic-api::crest/status-codes
canonical_url: https://developer.pingidentity.com/pingoneaic-api/crest/status-codes.html
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
description: To patch a resource, send an HTTP PATCH request with an array of operation objects in the payload. Each operation object uses some combination of these fields:
component: pingoneaic-api
page_id: pingoneaic-api::crest/patch
canonical_url: https://developer.pingidentity.com/pingoneaic-api/crest/patch.html
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
description: To query a resource collection, which you can think of as a resource container, perform an HTTP GET and accept a JSON response including at least a _queryFilter or _queryId parameter. These parameters cannot be used together.
component: pingoneaic-api
page_id: pingoneaic-api::crest/query
canonical_url: https://developer.pingidentity.com/pingoneaic-api/crest/query.html
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
description: To retrieve a single resource, perform an HTTP GET on the resource by its case-sensitive identifier (_id) and accept a JSON response:
component: pingoneaic-api
page_id: pingoneaic-api::crest/read
canonical_url: https://developer.pingidentity.com/pingoneaic-api/crest/read.html
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
title: Update
description: To update a resource, perform an HTTP PUT including the case-sensitive identifier (_id) as the final element of the path to the resource and the JSON resource as the payload.
component: pingoneaic-api
page_id: pingoneaic-api::crest/update
canonical_url: https://developer.pingidentity.com/pingoneaic-api/crest/update.html
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