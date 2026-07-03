---
title: Administrative API endpoints
description: PingAccess ships with interactive documentation for both developers and non-developers to explore the PingAccess application programming interface (API) endpoints, view a reference of the metadata for each API, and experiment with API calls.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_admin_api_endpoints
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_admin_api_endpoints.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 3, 2023
section_ids:
  admin-api-documentation-swagger-ui-specifications: Admin API documentation Swagger-UI specifications
---

# Administrative API endpoints

PingAccess ships with interactive documentation for both developers and non-developers to explore the PingAccess application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* endpoints, view a reference of the metadata for each API, and experiment with API calls.

PingAccess APIs are REST APIs that provide complete administrative capabilities of the product. They can be called from custom applications or from command line tools, such as cURL.

These endpoints are only available on the `admin.port` defined in the `/pa-admin-api/v3/api-docs/<PA_HOME>/conf/run.properties` file. For example, https\://*\<PA\_HOME>*:*\<PORT>*/pa-admin-api/v3/api-docs/.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you selected the **Use context root as reserved resource base path** check box in your PingAccess application, this feature creates an instance of any reserved PingAccess resources under the application's context root. As such, the context root of the application needs to prepend the reserved context application root (`/pa` by default) in any file paths that reference it. If the context root of your application is `myApp`, the file path would start with `/myApp/pa`. |

|   |                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | For enhanced API security, you must include `X-XSRF-Header: PingAccess` in all requests and use the `application/json` content type for `PUT` and `POST` requests. |

## Admin API documentation Swagger-UI specifications

The Swagger-UI component that displays the PingAccess admin API documentation uses OpenAPI specification (OAS) 2.0.

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The specification that the PingAccess admin API docs used previously, Swagger 1.2, has been deprecated. The Swagger 1.2 specification is still available at https\://*\<PA\_HOME>*:*\<PORT>*/pa-admin-api/v3/api-docs/pa/api-docs.json but might be removed from future versions of PingAccess. |

You can find the PingAccess admin API's OAS 2.0 specifications at either of the following:

* https\://*\<PA\_HOME>*:*\<PORT>*/pa-admin-api/v3/api-docs/pa/api-docs-v2.json

* https\://*\<PA\_HOME>*:*\<PORT>*/pa-admin-api/v3/api-docs/pa/api-docs-v2.yaml

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | Access to these specifications simplifies the process of integrating the PingAccess admin API with modern API clients, such as Postman. |
