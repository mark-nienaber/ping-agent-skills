---
title: Accessing the API interactive documentation
description: PingFederate ships with interactive documentation for both developers and non-developers to explore the API endpoints, view documentation for the API, and experiment with API calls.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_access_api_interact_documentation
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_access_api_interact_documentation.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 8, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Accessing the API interactive documentation

PingFederate ships with interactive documentation for both developers and non-developers to explore the API endpoints, view documentation for the API, and experiment with API calls.

## About this task

In general, you can make API calls from an interactive user interface, custom applications, or from command line tools such as cURL. The endpoint is only available at the administrative port, as defined by the `pf.admin.https.port` property in `<pf_install>/pingfederate/bin/run.properties`.

|   |                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For enhanced API security, you must include `X-XSRF-Header: PingFederate` in all requests and use the `application/json` content type for PUT and POST requests. |

To access the administrative API documentation, follow these steps:

## Steps

1. Start PingFederate.

2. Start a web browser.

3. Browse to the following URL: https\://*\<pf\_host>*:9999/pf-admin-api/api-docs/

   |   |                                                                                                                                                                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | *\<pf\_host>* is the network address of your PingFederate server. It can be an IP address, a host name, or a fully qualified domain name. It must be reachable from your computer.`9999` is the default value of the `pf.admin.https.port` property in the `run.properties` file. |

   |   |                                                                                                                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The administrative API is also documented in the OpenAPI Specification, previously known as the Swagger Specification. Click on the `/pf-admin-api/v1/swagger.json` URL on the Administrative API Documentation page to access the contents. |

4. To test an administrative API, follow these steps:

   1. Select a section of the administrative API you would like to explore; for example, **/dataStores**.

   2. Expand the method you want to use; for example, **GET /dataStores**.

   3. Enter required parameters, if any. For more information, see **Operation Models** underneath the selected API endpoint.

   4. Click **Try it out**.

      |   |                                                                                                                                                                                                        |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | You might be prompted to sign on using administrative credentials over HTTP Basic authentication. The role assigned to the respective administrative accounts affects the access to the requested API. |

      ### Result:

   If the request completes successfully, the administrative API returns the **Request URL**, the **Response Body**, the **Response Code**, and the **Response Headers**.
