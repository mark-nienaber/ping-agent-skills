---
title: About the Ping Autonomous Identity API
description: Ping Autonomous Identity provides a RESTful application programming interface (API) that lets you use HTTP request methods (GET, PUT, and POST) to interact with the system and its components. The API lets a developer make requests to send or receive data to an Ping Autonomous Identity endpoint, a point where the API communicates with the system. The data that is sent or returned is in JavaScript Object Notation (JSON) format.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-api-intro
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-api-intro.html
section_ids:
  using_postman: Using Postman
---

# About the Ping Autonomous Identity API

Ping Autonomous Identity provides a RESTful application programming interface (API) that lets you use HTTP request methods (GET, PUT, and POST) to interact with the system and its components. The API lets a developer make requests to send or receive data to an Ping Autonomous Identity endpoint, a point where the API communicates with the system. The data that is sent or returned is in JavaScript Object Notation (JSON) format.

|   |                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | With the release of version 2021.8.4, Ping Autonomous Identity no longer provides a Swagger client that you can access on the console. The Swagger UI was removed to tighten security within Ping Autonomous Identity. However, you can download the Ping Autonomous Identity API and import it into Postman. |

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | You cannot import the Ping Autonomous Identity API into Swagger as there is an existing CORS issue that breaks functionality. |

## Using Postman

**Download the Ping Autonomous Identity API**

1. On an upgraded Ping Autonomous Identity instance, open a browser, and log in using your account at `https://autoid-ui.forgerock.com/.`

2. Point your browser to `https://autoid-ui.forgerock.com/api/swagger.` An Opening Swagger dialog appears.

3. Save the file as `api.yml` or `conf.yml` to your local server or laptop.

4. Open Postman, and click Import. The file is imported into Postman.

5. Click Zoran-API-Service.

> **Collapse: Click an example**
>
> ![postman api](_images/postman-api.gif)

You now can access the Ping Autonomous Identity API in Postman.
