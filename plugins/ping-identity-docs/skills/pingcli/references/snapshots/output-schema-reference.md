---
title: JSON output schema reference
description: Reference the JSON envelope structure returned by all Ping CLI -O json output.
component: pingcli
version: 1.11
page_id: pingcli:output_schema_reference:output-schema-reference
canonical_url: https://developer.pingidentity.com/pingcli/1.11/output_schema_reference/output-schema-reference.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 14, 2026
section_ids:
  envelope-fields: Envelope fields
  status-values: status values
  errors-object: errors[] object
  error-category-values: errors[].category values
  meta-object: meta object
  warnings-object: warnings[] object
  ndjson-envelope-behaviour: NDJSON envelope behaviour
  ndjson-typed-line-types: ndjson-typed line types
  jsonschema: JSONSchema
  learn-more: Learn more
---

# JSON output schema reference

All `-O json` output from Ping CLI uses a consistent envelope structure. Every response — success or failure — always contains the same seven top-level fields, making it straightforward to parse reliably without checking the shape of the output first.

NDJSON output has three modes:

* `-O ndjson` (default) — each line is a raw record with no envelope.

* `-O ndjson-typed` — typed discriminated stream: zero or more `record` lines followed by exactly one `summary` or `error` terminal line.

* `-O ndjson-wrapped` *(deprecated)* — each line is the full envelope wrapping a single record.

Errors are always envelope-wrapped regardless of output format.

## Envelope fields

|                 |               |               |                                                                                                                                |
| --------------- | ------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| ***Field***     | ***Type***    | ***Present*** | ***Description***                                                                                                              |
| `schemaVersion` | string        | Always        | Schema version for the envelope. Currently `"1.1"`.                                                                            |
| `status`        | string        | Always        | Result status. One of `success`, `warning`, or `error`. Refer to [status values](#status-values).                              |
| `message`       | string        | Always        | Human-readable status message. Empty string when not applicable.                                                               |
| `data`          | any \| null   | Always        | The command result payload. An array for list commands; a single object for get, create, and update commands; `null` on error. |
| `errors`        | array \| null | Always        | Array of error objects on failure; `null` on success. Refer to [errors\[\] object](#errors-object).                            |
| `meta`          | object        | Always        | Metadata about the command invocation. Refer to [meta object](#meta-object).                                                   |
| `warnings`      | array         | Always        | Array of warning objects. Empty array `[]` when no warnings are present. Refer to [warnings\[\] object](#warnings-object).     |

## status values

|             |                                                                                                 |
| ----------- | ----------------------------------------------------------------------------------------------- |
| ***Value*** | ***When set***                                                                                  |
| `success`   | Command completed successfully; result is in `data`.                                            |
| `warning`   | Command completed but with non-fatal warnings; result is in `data` and `warnings` is non-empty. |
| `error`     | Command failed; `data` is `null` and `errors` is non-empty.                                     |

|   |                                                                      |
| - | -------------------------------------------------------------------- |
|   | The earlier `"info"` and `"fatal"` status values are no longer used. |

## errors\[] object

|              |            |                 |                                                                                                            |
| ------------ | ---------- | --------------- | ---------------------------------------------------------------------------------------------------------- |
| ***Field***  | ***Type*** | ***Present***   | ***Description***                                                                                          |
| `code`       | string     | Always          | Machine-readable error code, for example `SERVICE_ERROR` or `INVALID_ARGUMENT`.                            |
| `category`   | string     | Always          | Error category. Refer to [errors\[\].category values](#error-category-values).                             |
| `retryable`  | boolean    | Always          | Whether the request can be retried automatically. `true` only for `rate_limited` and `network` categories. |
| `message`    | string     | Always          | Human-readable description of the error.                                                                   |
| `suggestion` | string     | When applicable | A suggestion to help resolve the error.                                                                    |
| `details`    | object     | API errors only | Raw API response body for HTTP errors from `pingone api` or `pingfederate api` commands.                   |

### errors\[].category values

|                |                                                           |
| -------------- | --------------------------------------------------------- |
| ***Value***    | ***Condition***                                           |
| `validation`   | HTTP 400, or a CLI flag or argument error                 |
| `unauthorized` | HTTP 401                                                  |
| `forbidden`    | HTTP 403                                                  |
| `not_found`    | HTTP 404                                                  |
| `conflict`     | HTTP 409                                                  |
| `rate_limited` | HTTP 429                                                  |
| `internal`     | HTTP 5xx                                                  |
| `network`      | Network-level failure (connection refused, timeout, etc.) |

## meta object

|                  |            |                                           |                                                                                                               |
| ---------------- | ---------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| ***Field***      | ***Type*** | ***Present***                             | ***Description***                                                                                             |
| `command`        | string     | Always                                    | The full command that was invoked, reconstructed from `os.Args`. Present even for pre-parse errors.           |
| `count`          | integer    | Array results only                        | The number of records in `data`. Set automatically when `data` is an array; absent for single-object results. |
| `api.httpStatus` | integer    | `pingone api` and `pingfederate api` only | The HTTP status code returned by the upstream API. Absent on connector commands.                              |

## warnings\[] object

|             |            |                                            |
| ----------- | ---------- | ------------------------------------------ |
| ***Field*** | ***Type*** | ***Description***                          |
| `code`      | string     | Machine-readable warning code.             |
| `message`   | string     | Human-readable description of the warning. |

## NDJSON envelope behaviour

|                                    |                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ***Format***                       | ***Envelope behaviour***                                                                                                                                                                                                                                                                                                                                                                                             |
| `-O ndjson`                        | Each line is a raw record (the contents of `data`) with no envelope wrapper. Errors are always envelope-wrapped.                                                                                                                                                                                                                                                                                                     |
| `-O ndjson-typed`                  | Typed discriminated stream. Each line carries a `type` field: zero or more `{"type":"record","data":{…​}}` lines followed by exactly one terminal line — `{"type":"summary",…​}` on success or `{"type":"error",…​}` on failure. The summary line includes `meta.count` (number of records emitted). Use `--query` to filter per-record `data` values. Refer to [ndjson-typed line types](#ndjson-typed-line-types). |
| `-O ndjson-wrapped` *(deprecated)* | Each line is the full envelope wrapping a single record. `data` holds one record per line; `meta.count` is absent. Deprecated; use `-O ndjson-typed` instead.                                                                                                                                                                                                                                                        |

### ndjson-typed line types

|            |                |                                                                                                                                                                                |
| ---------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ***type*** | ***Terminal*** | ***Description***                                                                                                                                                              |
| `record`   | No             | One resource object. `data` holds the record payload. Zero or more per stream.                                                                                                 |
| `summary`  | Yes            | Stream completed successfully. `meta.count` is the number of `record` lines emitted. `meta.api.nextCursor` carries the HATEOAS next-page URL when the result set is paginated. |
| `error`    | Yes            | Stream failed. `error` carries the same fields as `errors[]` in the JSON envelope. No `record` lines follow.                                                                   |

## JSONSchema

The following [JSON Schema (draft-07)](https://json-schema.org/draft-07/schema) can be used to validate `-O json` output or to generate client code.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Ping CLI JSON output envelope",
  "type": "object",
  "required": ["schemaVersion", "status", "message", "data", "errors", "meta", "warnings"],
  "properties": {
    "schemaVersion": {
      "type": "string",
      "enum": ["1.1"]
    },
    "status": {
      "type": "string",
      "enum": ["success", "warning", "error"]
    },
    "message": {
      "type": "string"
    },
    "data": {},
    "errors": {
      "type": ["array", "null"],
      "items": {
        "type": "object",
        "required": ["code", "category", "retryable", "message"],
        "properties": {
          "code": { "type": "string" },
          "category": {
            "type": "string",
            "enum": [
              "validation",
              "unauthorized",
              "forbidden",
              "not_found",
              "conflict",
              "rate_limited",
              "internal",
              "network"
            ]
          },
          "retryable": { "type": "boolean" },
          "message": { "type": "string" },
          "suggestion": { "type": "string" },
          "details": { "type": "object" }
        }
      }
    },
    "meta": {
      "type": "object",
      "required": ["command"],
      "properties": {
        "command": { "type": "string" },
        "count": {
          "type": "integer",
          "description": "Present only when data is an array"
        },
        "api": {
          "type": "object",
          "properties": {
            "httpStatus": { "type": "integer" }
          }
        }
      }
    },
    "warnings": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["code", "message"],
        "properties": {
          "code": { "type": "string" },
          "message": { "type": "string" }
        }
      }
    }
  }
}
```

## Learn more

* [Output formats](../using_pingcli/output-formats.html)

* [Filtering and transforming output](../using_pingcli/filtering-output.html)

* [Return codes](../using_pingcli/return-codes.html)