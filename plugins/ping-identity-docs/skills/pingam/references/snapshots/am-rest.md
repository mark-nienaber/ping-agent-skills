---
title: Online REST API reference
description: Access the PingAM REST API Explorer to view available endpoints, versioning, and detailed information about each CRUDPAQ method for client applications
component: pingam
version: 8.1
page_id: pingam:am-rest:about-api-explorer
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-rest/about-api-explorer.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API"]
page_aliases: ["REST-guide:about-api-explorer.adoc"]
section_ids:
  access-api-explorer: Access the API Explorer
---

# Online REST API reference

AM provides an online REST API reference that you can access through the AM admin UI. The *API Explorer* displays the REST API endpoints that let client applications access AM's services.

|   |                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The API Explorer is enabled by default. For security reasons, it's strongly recommended that you disable it in production environments.To disable the API Explorer, go to Configure > Global Services > REST APIs, and select Disabled in the API Descriptors drop-down list. |

The key features of the API Explorer are as follows:

* API versioning

  The API Explorer displays the different API versions available depending on your deployment.

  ![API Explorer, accessible from the AM admin UI](_images/api-explorer.png)Figure 1. API Explorer

* Detailed information

  The API Explorer provides detailed information about each available CRUDPAQ method. Click the method name to view the endpoint's description, required parameters, and example responses.

  For the request payload and response codes, you can view example values, or click Model to view the associated schema.

  ![Detailed information about a sessions endpoint](_images/api-explorer-parameters.png)Figure 2. API Explorer parameters

* Try It Out

  The Try It Out feature lets you send a request to the endpoint and view the response.

  Click Try It Out, enter the required parameters, and click Execute to send the request to AM.

  The full curl command, request URL, and response are displayed in the API Explorer.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | When using the Try It Out feature:- The example payload values are auto-generated.

    Even if the data types are correct, the values might not be right for the API to function as expected. Check the Model tab for a description of the required value, and replace the example values before sending the REST request to AM.

  - Queries in the API Explorer are hard-coded to target the top-level realm.

    To access information in realms other than the top-level realm, use the API Explorer REST calls as an *example*, then construct your own REST calls targeting the endpoints in other realms.

    Learn more in [Specify realms in REST API calls](rest-realms.html). |

## Access the API Explorer

You can access the API Explorer in one of two ways:

1. Point your browser to the following URL:

   ```none
   https://am.example.com:8443/am/ui-admin/#api/explorer/applications
   ```

2. Click the help icon in the top-right corner of the AM admin UI, then click API Explorer.

   ![API Explorer, accessible from the help icon on the AM admin UI](_images/api-explorer-help-icon.png)Figure 3. API Explorer help icon
