---
title: ABS Discovery API
description: The Discovery API uses the GET method to display the discovered application programming interface (API) details and is reported only when the host, basepath, schemes, paths, and responses information is populated.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_abs_discovery_api
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_abs_discovery_api.html
revdate: April 3, 2024
---

# ABS Discovery API

The Discovery API uses the GET method to display the discovered application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* details and is reported only when the `host`, `basepath`, `schemes`, `paths`, and `responses` information is populated.

API Behavioral Security (ABS) provides the following external REST API, which uses the GET method to view the discovered APIs:

URL: `/v4/abs/discovery`

The following is a snippet of the summary output of `discovery` API:

```json
{
    "company": "ping identity",
    "name": "api_discovery_summary",
    "description": "This report contains summary of discovered APIs",
    "summary": [
        {
            "api_name": "api_0",
            "host": "bothcookientoken.com",
            "basePath": "/path1",
            "created": "Fri Mar 06 09:29:51:591 2020",
            "updated": "Fri Mar 06 09:50:03:372 2020"
        },
        {
            "api_name": "api_1",
            "host": "path5",
            "basePath": "/path1/path2/path3",
            "created": "Fri Mar 06 10:59:38:975 2020",
            "updated": "Fri Mar 06 11:36:45:596 2020"
        },
        {
            "api_name": "api_14",
            "host": "path5",
            "basePath": "/path1/path2/path3/path4/path5",
            "created": "Fri Mar 06 11:59:14:804 2020",
            "updated": "Fri Mar 06 12:18:24:732 2020"
        },
        {
            "api_name": "api_15",
            "host": "pathx",
            "basePath": "/path1/path2/path3/path4",
            "created": "Fri Mar 06 11:59:16:092 2020",
            "updated": "Fri Mar 06 13:19:25:283 2020"
        },
        {
            "api_name": "api_16",
            "host": "pathx",
            "basePath": "/path1/path2/path3/path4/path5",
            "created": "Fri Mar 06 11:59:16:244 2020",
            "updated": "Fri Mar 06 12:18:26:227 2020"
        },
        {
            "api_name": "api_17",
            "host": "path6",
            "basePath": "/path1/path2/path3/path4/path5/path6",
            "created": "Fri Mar 06 11:59:14:952 2020",
            "updated": "Fri Mar 06 12:18:24:876 2020"
        },
        {
            "api_name": "api_19",
            "host": "path7",
            "basePath": "/path1/path2/path3/path4/path5/path6",
            "created": "Fri Mar 06 11:59:15:096 2020",
            "updated": "Fri Mar 06 12:18:25:028 2020"
        },
        {
            "api_name": "api_9",
            "host": "path2",
            "basePath": "/path1/path2",
            "created": "Fri Mar 06 10:59:00:616 2020",
            "updated": "Fri Mar 06 13:19:23:003 2020"
        }
    ]
}
}
```

Each API name (for example, `api_1`) is auto-generated and starts from `api_0`. This API name can be specified in the `api_name` query parameter to request more details as shown in the next example.

URL: `/v4/abs/discovery?api_name=api_1`

The following is a snippet of a discovered API:

```json
{
    "company": "ping identity",
    "name": "api_discovery_details",
    "description": "This report contains details of discovered APIs",
    "info": {
        "title": "api_7"
    },
    "host": "127.0.0.1",
    "basePath": "/shop-books3",
    "cookie": "",
    "oauth2_access_token": false,
    "apikey_qs": "",
    "apikey_header": "",
    "schemes": [
        "HTTP/1.1"
    ],
    "consumes": [],
    "produces": [
        "text/html"
    ],
    "server_ssl": true,
    "backendHosts": [
        "127.0.0.1:4001"
    ],
    "backendServers": [
        "127.0.0.1:4001"
    ],
    "username_header": "",
    "jwt": {
        "username": "username",
        "clientid": "client_id",
        "location": "h:authorization:bearer"
    },
    "paths": {
        "/shop-books3": {
            "GET": {
                "produces": [
                    "text/html"
                ],
                "responses": {
                    "200": {
                        "description": "OK"
                    }
                }
            }
        }
    }
}
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If the API Security Enforcer (ASE) is deployed in sideband mode, then backend host field in the output shows the Internet Protocol (IP) *(tooltip: \<div class="paragraph">&#xA;\<p>The method by which data is sent across the internet from the source host to the destination host.\</p>&#xA;\</div>)* address as `not available: 0`. The backend server field shows the IP address as `0.0.0.0`. For more information on ASE sideband mode, see the ASE Admin Guide. |
