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

---

---
title: Active sessions
description: The Active sessions screen displays information about the active users connected to PingIntelligence UI sessions.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_active_session
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_active_session.html
revdate: April 3, 2024
---

# Active sessions

The **Active sessions** screen displays information about the active users connected to PingIntelligence UI sessions.

The **Active sessions** screen displays the **Active sessions list**.

![Screen capture of PingIntelligence active sessions list.](_images/hcq1640162453560.png)

In the **Active sessions list**, your user and session entry is marked `(Current Session)`.

To view a user's session details, expand the user entry in the **Active sessions list** by clicking the control on the right. The following session parameter values display:

* **Role** of the user.

* **Source IP** origin accessing the UI.

* **User agent**, typically the user's browser and version.

* **Created** date and time of the user session.

* **Last active** date and time of the user session.

If there are sessions listed other than the `(Current Session)`, the **Delete all** control appears, permitting termination of all sessions other than the current session.

---

---
title: Adding, deleting, and moving APIs
description: You can add, delete, or move an application programming interface (API) from an API group.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_adding_deleting_moving_apis
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_adding_deleting_moving_apis.html
revdate: April 3, 2024
section_ids:
  steps: Steps
---

# Adding, deleting, and moving APIs

You can add, delete, or move an application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* from an API group.

## Steps

* To add an API to group, click **Add APIs** on the top-right corner of the API group. Select the API from the **Add APIs to the Group** pop-up and click **Submit**. You can select more than one API and add them to a group in one instance.

  ![Screen capture of the PingIntelligence Add API to group page.](_images/its1601183586643.png)

* To delete an API from an API group, click **Move API**. Select **Delete API** in the **Move/Delete from the Group** pop-up. Click **Submit**. After an API which does not belong to any other group is deleted from a group, then it automatically gets added to the default group.

  ![Screen capture of the PingIntelligence Delete API from group page.](_images/tqe1601259242494.png)

* To move an API to a different API group, click **Move API**. Select **Move API** in the **Move/Delete from the Group** pop-up. Now select the target API group and click **Submit**. You can move the API to more than one target API groups. Once the API is moved it'll no longer be part of that API group.

  ![Screen capture of the PingIntelligence Move API to group page.](_images/fck1601188700848.png)

---

---
title: Administering API groups
description: This topic discusses administrative tasks associated with your application programming interface (API) groups.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_administering_api_groups
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_administering_api_groups.html
revdate: April 3, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  creating-and-deleting-api-groups: Creating and deleting API groups
  steps: Steps
  adding-deleting-and-moving-apis: Adding, deleting, and moving APIs
  steps-2: Steps
  merging-a-user-defined-api-group-into-the-default-api-group: Merging a user-defined API group into the default API group
  about-this-task-2: About this task
  steps-3: Steps
  searching-or-sorting-api-groups-and-apis: Searching or sorting API groups and APIs
  steps-4: Steps
---

# Administering API groups

This topic discusses administrative tasks associated with your application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* groups.

## Before you begin

Make sure you have admin user privileges to administer the API groups in the dashboard.

## About this task

You can perform the following administrative operations on API groups:

* [Creating and deleting API groups](pingintelligence_creating_deleting_api_groups.html)

* [Adding, deleting, and moving APIs](pingintelligence_adding_deleting_moving_apis.html)

* [Merging a user-defined API group into the default API group](pingintelligence_merging_api_group.html)

* [Searching or sorting API groups and APIs](pingintelligence_searching_sorting_apis.html)

|   |                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A successful execution of these operations is followed by a success notification. Click the **Refresh** ![A screenshot of the Refresh button.](_images/jie1602140098489.png) button on the top-right corner, to reflect the changes made to the API groups. |

## Creating and deleting API groups

### Steps

* To create an API *(tooltip: \<div class="paragraph">
  \<p>A specification of interactions available for building software to access an application or service.\</p>
  \</div>)* group, click **Create New API group** on the top-right corner. Fill in the following details for the new API group, and click **Save**:

  * **Group name**: The display name of the API group.

  * **Group description**: Additional information about the API group.

  * **Custom attribute key**: The metadata key for the API group.

  * **Custom attribute value**: Metadata about the API group. This can be used in search operations.

    ![Screen capture of PingIntelligence create new API group popup window showing.](_images/bye1640167393569.png)

* Click the **Pencil** ![nua1601190800641](_images/nua1601190800641.png) icon, to edit an API group. You can modify the metadata of the group.

* Click the **Delete** ![flm1601182421248](_images/flm1601182421248.png) icon on the bottom-right corner of the API group, to delete an API group. APIs in the group that are not part of any other API groups, will be added to the default API group. You cannot delete the default API group.

## Adding, deleting, and moving APIs

You can add, delete, or move an API *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* from an API group.

### Steps

* To add an API to group, click **Add APIs** on the top-right corner of the API group. Select the API from the **Add APIs to the Group** pop-up and click **Submit**. You can select more than one API and add them to a group in one instance.

  ![Screen capture of the PingIntelligence Add API to group page.](_images/its1601183586643.png)

* To delete an API from an API group, click **Move API**. Select **Delete API** in the **Move/Delete from the Group** pop-up. Click **Submit**. After an API which does not belong to any other group is deleted from a group, then it automatically gets added to the default group.

  ![Screen capture of the PingIntelligence Delete API from group page.](_images/tqe1601259242494.png)

* To move an API to a different API group, click **Move API**. Select **Move API** in the **Move/Delete from the Group** pop-up. Now select the target API group and click **Submit**. You can move the API to more than one target API groups. Once the API is moved it'll no longer be part of that API group.

  ![Screen capture of the PingIntelligence Move API to group page.](_images/fck1601188700848.png)

## Merging a user-defined API group into the default API group

You can merge a user-defined API *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* group into the default API group.

### About this task

Complete the following steps:

### Steps

1. Click **Settings → API grouping settings**.

2. From the **Select group** list, select the API group that you want to move to the default group.

3. Click **Save**.

![Screen capture of the PingIntelligence API default group settings, select group showing.](_images/yoz1640173355917.png)

## Searching or sorting API groups and APIs

### Steps

* You can search for a specific API *(tooltip: \<div class="paragraph">
  \<p>A specification of interactions available for building software to access an application or service.\</p>
  \</div>)* in an API group or across multiple API groups. For quick and easy retrieval, when you search at the API group level, you can filter your search based on **Group name**, **Attribute**, or **API**. When API is chosen for filtering, only non-empty API groups are loaded.

* You can sort API groups based on**Group name**, **Group creation date**, or **Last modified date**.

![Screen capture of PingIntelligence API group sorting, group name, creation date, and last modified date showing.](_images/bog1640174026568.png)

* You can also sort the APIs within an API group based on**Creation date** or **Training start date**.

![Screen capture of PingIntelligence API grouping - group based sorting showing.](_images/iho1640174184806.png)

---

---
title: AI engine training variables
description: PingIntelligence AI training depends on a set of parameters configured using Global configuration update REST API.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_ai_engine_training_variables
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_ai_engine_training_variables.html
revdate: April 3, 2024
---

# AI engine training variables

PingIntelligence AI training depends on a set of parameters configured using [Global configuration update REST API](../pingintelligence_reference_guide/pingintelligence_global_configuration_update_rest_api.html).

These parameters should be configured before starting the system. It is recommended that you review the variables and configure the best values for your environment. Frequent updates to the training variables may lead to a change in behavior of the AI system. The following are the parameters that need to be configured:

* `attack_initial_training`

* `attack_update_interval`

* `continuous_learning`

* `window_length`

The following table describes the various training variables.

**Training variables**

| Variable                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `attack_initial_training`     | The number of hours that you want to train the AI model before it moves to the prediction mode. The default value is 24-hours. The minimum value is 1 hour.                                                                                                                                                                                                                                                                |
| `attack_update_interval`      | The time interval in hours at which you would want the model thresholds to be updated. The default value is 24 hours. The minimum value is 1 hour. The value in this variable takes effect only when `continuous_learning` is set to `true`.                                                                                                                                                                               |
| `continuous_learning`         | Setting this value to `true` configures the AI model to learn continuously based on the live traffic. If it is set to `false`, the AI model detects attack based on the initial training.                                                                                                                                                                                                                                  |
| `window_length`               | The maximum time period that the AI model uses to detect attacks across application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)*s. The default and maximum value for `window_length` is 24 hours. The training period should be longer than the `window_length` period. |
| `root_api_attack`             | Configure as `true` if you want AI engine to detect attacks on the root API. Set it to `false` if you do not wish the AI engine to detect attacks on the root API. The default value is `false`.                                                                                                                                                                                                                           |
| `session_inactivity_duration` | The time in minutes for an inactive user session after which API Behavioral Security (ABS) decides that the session has terminated. The default value is 30 minutes. You can configure it to any value in minutes.&#xA;&#xA;This variable only applies to account take over attack.                                                                                                                                        |

The following is a snippet from the response global config API:

```json
{
    "company": "ping identity",
    "name": "api_globalconfig",
    "description": "This report contains status information of ABS global configurations",
    "global_config": {
        "attack_initial_training": 2,

        "attack_update_interval": 1,

        "api_discovery": true,
        "discovery_initial_period": 100,
        "discovery_subpath": 3,
        "discovery_update_interval": 1,
        "poc": false,
        "url_limit": 120,
        "response_size": 150,
        "continuous_learning": false,

        "attack_list_count": 400000,
        "root_api_attack": true,
        "session_inactivity_duration": 10

    }
}
```

**Miscellaneous variables**

| Variable        | Description                                                                                                                                                                                                                                                                                        |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `response_size` | Maximum size in MB of the data fetched by external calls to ABS REST APIs. The default value is 100 MB.                                                                                                                                                                                            |
| `enable_ssl`    | By default it is set to `true`, and SSL communication is enabled between API Security Enforcer (ASE) and ABS, and for external systems making rest API calls to ABS. See [Configure SSL](../pingintelligence_reference_guide/pingintelligence_configure_ssl.html) on page 10 for more information. |

---

---
title: API activity
description: The API activity dashboard provides breakdown details about an application programming interface (API) activity in the reported period.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_api_activity
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_api_activity.html
revdate: June 5, 2024
---

# API activity

The **API activity** dashboard provides breakdown details about an application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* activity in the reported period.

![Screen capture of the PingIntelligence dashboard API activity.](_images/grx1639486705781.png)

The API's request counts for the reported period display in the upper part of the **API Activity** dashboard. You can adjust the reporting period to display the API's request counts for the past day, week, month or 6 month period.

In the lower part of the screen the following panes display details about requests to the API, for the reported period.

| Pane             | Description                                                                                                                                                                                                                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **IoAs**         | List of the types of IoAs detected on the API, and the count of IoAs per type.                                                                                                                                                                                                                 |
| **Error Codes**  | List of error codes returned from requests to the API.                                                                                                                                                                                                                                         |
| **Tokens**       | List of the names of tokens used when issuing requests to the API, and the count of requests per token.                                                                                                                                                                                        |
| **User**         | List of the usernames issuing requests to the API, and the count of requests per username.                                                                                                                                                                                                     |
| **IP Address**   | List of the Internet Protocol (IP) *(tooltip: \<div class="paragraph">&#xA;\<p>The method by which data is sent across the internet from the source host to the destination host.\</p>&#xA;\</div>)* addresses where requests to the API originated, and the count of requests per IP address. |
| **Device Types** | List of the device types where requests to the API originated, and the count of requests per device type.                                                                                                                                                                                      |
| **Endpoints**    | List of the API endpoints that received requests, and the count of requests per API endpoint.                                                                                                                                                                                                  |

Click **Back** to return to the previous dashboard.

Click **Close** to return to the main dashboard screen.

---

---
title: API activity
description: The API activity dashboard provides breakdown details about an application programming interface (API) activity in the reported period.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_dashboard_api_activity
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_dashboard_api_activity.html
revdate: June 7, 2024
---

# API activity

The **API activity** dashboard provides breakdown details about an application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* activity in the reported period.

![Screen capture of the PingIntelligence dashboard API activity.](_images/grx1639486705781.png)

The API's request counts for the reported period display in the upper part of the **API Activity** dashboard. You can adjust the reporting period to display the API's request counts for the past day, week, month or 6 month period.

In the lower part of the screen the following panes display details about requests to the API, for the reported period.

| Pane             | Description                                                                                                                                                                                                                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **IoAs**         | List of the types of IoAs detected on the API, and the count of IoAs per type.                                                                                                                                                                                                                 |
| **Error Codes**  | List of error codes returned from requests to the API.                                                                                                                                                                                                                                         |
| **Tokens**       | List of the names of tokens used when issuing requests to the API, and the count of requests per token.                                                                                                                                                                                        |
| **User**         | List of the usernames issuing requests to the API, and the count of requests per username.                                                                                                                                                                                                     |
| **IP Address**   | List of the Internet Protocol (IP) *(tooltip: \<div class="paragraph">&#xA;\<p>The method by which data is sent across the internet from the source host to the destination host.\</p>&#xA;\</div>)* addresses where requests to the API originated, and the count of requests per IP address. |
| **Device Types** | List of the device types where requests to the API originated, and the count of requests per device type.                                                                                                                                                                                      |
| **Endpoints**    | List of the API endpoints that received requests, and the count of requests per API endpoint.                                                                                                                                                                                                  |

Click **Back** to return to the previous dashboard.

Click **Close** to return to the main dashboard screen.

---

---
title: API discovery and configuration
description: The API Behavioral Security (ABS) AI Engine works in tandem with API Security Enforcer (ASE) to automatically discover new and unknown application programming interface (API)s in your ecosystem.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_api_discovery_configuration
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_api_discovery_configuration.html
revdate: May 6, 2024
section_ids:
  configuring-api-discovery: Configuring API discovery
  about-this-task: About this task
  steps: Steps
  configuring-ase-for-api-discovery: Configuring ASE for API discovery
  about-this-task-2: About this task
  steps-2: Steps
  example: Example:
---

# API discovery and configuration

The API Behavioral Security (ABS) AI Engine works in tandem with API Security Enforcer (ASE) to automatically discover new and unknown application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)*s in your ecosystem.

You can view the discovered APIs by using the [ABS discovery REST API](pingintelligence_abs_discovery_api.html). You can also add the discovered APIs to ASE by using API Discovery in the PingIntelligence for APIs Dashboard. For more information, see [Discovered APIs](pingintelligence_discovered_apis.html).

## Configuring API discovery

### About this task

To configure API discovery in your environment:

### Steps

1. Enable ABS in ASE.

2. Define `root` API JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
   \<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
   \</div>)* in ASE.

   |   |                                                       |
   | - | ----------------------------------------------------- |
   |   | ABS discovers APIs only for a `root` API JSON in ASE. |

3. Optionally, configure OAuth token and API Key parameters in `root` API JSON.

4. Configure discovery related parameters using [Global configuration update REST API](../pingintelligence_reference_guide/pingintelligence_global_configuration_update_rest_api.html).

   |   |                                                                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Use the `update.sh` script to edit the default values related to API discovery. For more information on update script, see [Managing discovery intervals](pingintelligence_managing_discovery_intervals.html). |

## Configuring ASE for API discovery

### About this task

The following table summarizes the variables related to API discovery that you need to configure.

**API discovery variables**

| Variable                    | Description                                                                                                                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_discovery`             | Set this variable to **true** to switch on API discovery. To switch off API discovery, set it to **false**. The default value is **true**.                                                      |
| `discovery_initial_period`  | The initial time in hours during which APIs are discovered in your API ecosystem. The default and minimum value is 1-hour.                                                                      |
| `discovery_update_interval` | The time interval in hours at which any new discovered APIs are reported. The default and minimum value is 1-hour.                                                                              |
| `discovery_subpath`         | The number of sub-paths that is discovered in an API. The minimum value is 1 and maximum value is 6. For more information, see [Discovery sub-paths](pingintelligence_discovery_subpaths.html). |
| `url_limit`                 | Defines the maximum number of URLs that are reported in a discovered API.                                                                                                                       |

To configure ASE for API discovery:

### Steps

* Enable ABS in ASE by running the `enable_abs` command in ASE:

  ```
  ./bin/cli.sh -u admin -p admin enable_abs
  ABS is now enabled
  ```

* To verify, run the `status` command in ASE:

  ```
  ./bin/cli.sh status
  API Security Enforcer
  status                  : started
  mode                    : sideband
  http/ws                 : port 80
  https/wss               : port 443
  firewall                : enabled
  abs                     : enabled, ssl: enabled
  abs attack              : disabled
  audit                   : enabled
  sideband authentication : disabled
  ase detected attack     : disabled
  attack list memory      : configured 128.00 MB, used 25.60 MB, free 102.40 MB
  google pubsub           : disabled
  ```

* To configure root API in ASE, define `root` API in ASE.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If you have configured other APIs in ASE along with the `root` API, ABS monitors traffic only on the root API for the discovery process. A `root` API in ASE is an API for which the API JSON file has `url` as `"/"` and `hostname` as `"*"`.If API discovery is enabled in ABS without `root` API in ASE and you run the `discovery` REST API, it displays an error message: `root API not configured in ASE. To discover APIs configure root API in ASE`. |

  #### Example:

  The following is a snippet of `root` API JSON:

  ```json
  {
      "api_metadata": {
          "protocol": "http",
          "url": "/",
          "hostname": "*",

          "cookie": "",
          "oauth2_access_token": false,
          "apikey_qs": "",
          "apikey_header": "",
          "enable_blocking": false,
          "cookie_idle_timeout": "200m",
          "logout_api_enabled": false,
          "cookie_persistence_enabled": false,
          "login_url": "",
          "api_mapping": {
              "internal_url": ""
          },
  ```

  |   |                                                                                 |
  | - | ------------------------------------------------------------------------------- |
  |   | A sample `root` API ships with ASE in `/pingidentity/ase/config/api` directory. |

* Configure API JSON by configuring the settings for `cookie`, `oauth2_access_token`, `apikey_qs`, or `apikey_header` in the `root` API JSON file in ASE.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | API discovery process discovers these parameters in an API only when you set these in the root API. API discovery reports these attributes of an API only when it receives at least 50% of traffic having these attributes. For example, if the root API receives 100 requests and 51 requests have OAuth token, then the OAuth token is reported in the discovered API. Similarly, if the same traffic has less than 50% traffic for API keys or cookies, then they are not reported in the discovered API. |

* Configure API discovery in ABS by setting the `api_discovery` parameter to `true` using [Global configuration update REST API](../pingintelligence_reference_guide/pingintelligence_global_configuration_update_rest_api.html).

  |   |                                                                                                                                                                                                                            |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you want update the values on an already running system, use the `update.sh` script. For more information on the update script, see [Managing discovery intervals](pingintelligence_managing_discovery_intervals.html). |

---

---
title: API discovery process
description: API Behavioral Security (ABS) discovery process starts when the API Security Enforcer (ASE) sends the access log files to ABS.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_api_discovery_process
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_api_discovery_process.html
revdate: April 3, 2024
---

# API discovery process

API Behavioral Security (ABS) discovery process starts when the API Security Enforcer (ASE) sends the access log files to ABS.

The discovery process and reporting interval are defined by the variables configured using [Global configuration update REST API](../pingintelligence_reference_guide/pingintelligence_global_configuration_update_rest_api.html).

1. ABS processes the ASE log files and looks for new APIs. During the discovery period, ABS monitors the traffic on the API JSON (root API) and requires only one valid request to report an API. ABS considers only valid (200-OK response) requests for discovering APIs. At the end of the discovery period, ABS publishes the discovered APIs. ABS specifically looks for the following four values in the incoming traffic on the root API:

   * Hostname

   * Pathinfo

   * Scheme or protocol

   * Backend server. If ASE is deployed in a sideband mode, then backend server is not reported.

2. At the end of the initial discovery period, ABS does one of the following:

   * If the API definition was learned, then ABS outputs the discovered APIs with the parameters as detailed in the [\[table\_discovery\_parameters\]](#table_discovery_parameters) below.

   * If the API definition is incomplete, then ABS repeats the discovery process (Step 1) for a `discovery_update_interval` (default is 1 hour).

The following illustration shows an example of the API discovery process:

![Image of API discover process example](_images/moe1576230582578.png)

The illustration shows three APIs, API 1, API 2, and API 3 are the undiscovered APIs in your environment. The traffic for these APIs is coming through the root API configured in ASE. The following points explain the discovery process:

* API 1 receives a request in the initial training period with a 200-OK response. This API is discovered at the end of` discovery_initial_period` T1.

* API 2 receives one invalid request (404 response) during the initial discovery period. This API is not reported at T1.

* API 3 did not receive any request in the initial discovery period. Hence it was not reported at T1. However, API 3 got one valid request (200-OK response) in the time-period T1-T2, hence it was reported at time T2. The time period T1-T2 is `discovery_update_interval`.

|   |                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The initial discovery period applies only to fresh installation of PingIntelligence components. If you are upgrading an existing deployment, the `discovery_update_interval` applies. |

ABS API definition reports include the following information for each discovered API:

| Information    | Description                                                                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `host`         | Hostname or IP address that is serving the API.                                                                                                      |
| `basePath`     | The base path on which the API is served. The base path is relative to the host. The value starts with a leading / (slash).                          |
| `schemes`      | API protocol - value must be HTTP, HTTPS, WS, or WSS.                                                                                                |
| `consumes`     | A list of MIME types that the APIs can consume.                                                                                                      |
| `produces`     | A list of MIME types that the APIs can produce.                                                                                                      |
| `paths`        | Relative paths to the individual endpoints.                                                                                                          |
| `responses`    | Placeholder to hold responses.                                                                                                                       |
| `backendHosts` | Backend servers for the API.                                                                                                                         |
| `server_ssl`   | Value is `true` if backend API server supports encrypted connection. Set to `false` if the backend API server does not support encrypted connection. |

You can add the discovered APIs automatically to ASE using [Discovered APIs](pingintelligence_discovered_apis.html) in PingIntelligence for APIs Dashboard. Note that when the root API is configured with the token, cookie, or API key parameter, PingIntelligence will expect all discovered APIs to use the defined identifiers for authentication. If this is not the case, then add the discovered APIs manually in ASE.

---

---
title: API groups
description: The PingIntelligence dashboard provides the capability to organize the application programming interface (API) in your environment into logical groups. You can create API groups as per your requirements. For example, you can group your APIs location-wise, functionality-wise, and so on.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_api_groups
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_api_groups.html
revdate: April 3, 2024
section_ids:
  api-details: API details
---

# API groups

The PingIntelligence dashboard provides the capability to organize the application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* in your environment into logical groups. You can create API groups as per your requirements. For example, you can group your APIs location-wise, functionality-wise, and so on.

The **API** tab displays all the APIs being managed by PingIntelligence. Every API will be part of at least one API group in the Dashboard. The APIs grouping feature makes searching for a specific API quick and easy. The Dashboard supports two kinds of groups:

* Default API group: This is the global API group. All the existing as well as newly discovered APIs will be part of it initially. APIs that do not belong to any other API group will automatically get added to the default API group. You can only view and move APIs from the default APIs group. You cannot delete an API from the default API group.

* User-defined API groups: These are the API groups that you can create based on your requirements. You can add or delete an API from the user-defined API groups.

  ![Screen capture of PingIntelligence APIs grouping.](_images/ouq1640165945552.png)

## API details

Click on the **Expand** icon ![dpp1601176082307](_images/dpp1601176082307.png) to expand an API group. The following details are available for each API within an API group.

| API                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API name                                     | API name used by PingIntelligence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Prediction mode                              | A `true` status means that at least one training threshold value is set. It does not necessarily mean that all the training is complete. A `false` status means that the API is still in training mode.                                                                                                                                                                                                                                                                                                                                                                                                  |
| Training duration                            | The minimum configured time in hours to train an API. For more information, see [Managing AI engine training](pingintelligence_managing_ai_engine_training.html).                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| URL                                          | API basepath Uniform Resource Locator (URL) *(tooltip: \<div class="paragraph">&#xA;\<p>Identifies a resource according to its internet location.\</p>&#xA;\</div>)* configured in the API JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">&#xA;\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>&#xA;\</div>)* file. For more information, see [Defining an API using API JSON configuration file in inline mode](../pingintelligence_reference_guide/pingintelligence_defining_api_json_configuration_inline.html). |
| Host name                                    | Host name of the API configured in the API JSON file. For more information, see [Defining an API using API JSON configuration file in inline mode](../pingintelligence_reference_guide/pingintelligence_defining_api_json_configuration_inline.html).                                                                                                                                                                                                                                                                                                                                                    |
| Protocol                                     | The protocol configured in the API JSON file. For more information, see [Defining an API using API JSON configuration file in inline mode](../pingintelligence_reference_guide/pingintelligence_defining_api_json_configuration_inline.html).                                                                                                                                                                                                                                                                                                                                                            |
| API type                                     | API type can be `regular`, `decoy - incontext`, or `decoy-out-of-context`. For more information on deception, see [API deception environment in inline mode](../pingintelligence_reference_guide/pingintelligence_api_deception_environment_inline.html).                                                                                                                                                                                                                                                                                                                                                |
| Token                                        | A `true` status means that PingIntelligence will use OAuth tokens for reporting and attack detection. For more information, see [Defining an API using API JSON configuration file in inline mode](../pingintelligence_reference_guide/pingintelligence_defining_api_json_configuration_inline.html).                                                                                                                                                                                                                                                                                                    |
| API Key header and API key query string (QS) | The API Key values configured in the API JSON file and used for reporting and attack detection. For more information, see [Defining an API using API JSON configuration file in inline mode](../pingintelligence_reference_guide/pingintelligence_defining_api_json_configuration_inline.html).                                                                                                                                                                                                                                                                                                          |
| Cookie                                       | The cookie value configured in the API JSON file and used for reporting and attack detection. Displays blank if a cookie was not configured in API JSON. For more information, see [Defining an API using API JSON configuration file in inline mode](../pingintelligence_reference_guide/pingintelligence_defining_api_json_configuration_inline.html).                                                                                                                                                                                                                                                 |
| Servers                                      | The back end API server configured in the API JSON file - "\*" supports all the host names. For more information, see [Defining an API using API JSON configuration file in inline mode](../pingintelligence_reference_guide/pingintelligence_defining_api_json_configuration_inline.html).                                                                                                                                                                                                                                                                                                              |

Click the **Toggle** button ![gcp1602745795031](_images/gcp1602745795031.png) to hide or display information for the API in the PingIntelligence Dashboard. This provides the flexibility to display only selected APIs. Even if an API is hidden from the API dashboard, the dashboard engine continues processing its metadata. The hidden API is moved to the end of list. If the APIs are paginated, the hidden APIs are moved to the last page. When you toggle the button to display a hidden API, the Dashboard displays data for the API on the Dashboard. You can also go to the [API activity](pingintelligence_api_activity.html) dashboard for the API, by clicking the API analytics icon ![A screen capture of the API analytics icon.](_images/gdq1601115889397.png).

![Screen capture of PingIntelligence APIs grouping - API details.](_images/cuf1640166749190.png)

---

---
title: Attack management
description: The Attack management dashboard shows the clients which were flagged for an Indicator of Attack (IoA) for the specified period.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_attack_management
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_attack_management.html
revdate: April 3, 2024
section_ids:
  sorting-and-filtering: Sorting and filtering
  drill-downs-and-actions: Drill downs and actions
  actions: Actions
  drill-down: Drill down
---

# Attack management

The **Attack management** dashboard shows the clients which were flagged for an Indicator of Attack (IoA) for the specified period.

To view the **Attack list** summary information, click **Attack management**.

![Screen capture of PingIntelligence Attack List.](_images/njr1639658295544.png)

The **Attack list** has the following columns:

| Column      | Description                                                                                                      |
| ----------- | ---------------------------------------------------------------------------------------------------------------- |
| Client ID   | The unique ID of the client that originated the IoA.                                                             |
| IoAs        | The number of IoAs for the client for the time range.                                                            |
| Client type | The type of client:- Token

- IP address

- Cookie

- Username

- API key                                        |
| Reviewed    | Reviewed status toggle:- Reviewed (On)

- Not reviewed (Off)                                                     |
| Actions     | Possible actions to take (three-dots) drop down:- Client activity

- Tune IoA detection

- Remove from blocklist |

## Sorting and filtering

Sort the **Attack list** output according to one of the following:

* **Detected time** (default), from the most recent date and time to the least recent.

* **IoA count**, ordered by **Client ID**, from the client with the highest number of IoAs to the client with the least IoAs.

Apply filters to narrow down the **Attack list**.

* Select one or more **Client ID Types** from the drop down menu:

  * Token

  * IP address

  * Cookie

  * Username

  * API key

* Select a date range from the **Quick dates** drop down menu:

  * Last 1 day (default)

  * Last 7 days

  * Last 30 days

  * Custom: define a period from a starting date and time to an ending date and time

Click **Go** to apply the filters to the **Attack list** output.

You can filter the **Attack list** further:

* **Search client identifiers**: Enter search strings or partial strings of the **Client ID**

  |   |                                                                                                                                                                                                                                                                                                                                      |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | * The search is case-insensitive.

  * Wildcard searches, for example using an asterisk (`\*`), are not supported.

  * Use of quotation marks is not supported.

  * Be aware of the use of spaces in a search string. A leading or trailing space can filter out results. A single space is not regarded as multiple consecutive spaces. |

* Click **Filter** to apply the following filter parameters:

  * **Reviewed**

    * All (default)

    * Reviewed

    * Not reviewed

  * Select one or more **APIs** from the drop down

  * Select one or more **IoA types** from the drop down

## Drill downs and actions

### Actions

On the right side of the row in the main **Attack management** list, or at the top right of the **IoAs** dashboard, click the three-dots drop down to choose an action option:

* [Client activity](pingintelligence_client_activity.html): Navigate to the **Client activity** dashboard, for further inspection and analysis of the client's activities during the reported period.

* **Tune IoA detection**: Select this option to update models to not flag this behavior in the future.

* **Remove from blocklist**: Select this option to update models to remove this entry from the blocklist.

### Drill down

Click on a row to navigate to the client's [IoAs (Indicators of Attack)](pingintelligence_ioas.html) dashboard, for further drill downs, inspection and analysis of the client's activities during the reported period.

---

---
title: Blocklist
description: The Blocklist chart shows the distribution of blocklists by client type, for the specified period.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_blocklist
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_blocklist.html
revdate: June 5, 2024
section_ids:
  graph-filters: Graph filters
  blocklist-table: Blocklist table
  sorting: Sorting
  api-drill-down: API drill-down
---

# Blocklist

The **Blocklist** chart shows the distribution of blocklists by client type, for the specified period.

To view the **Blocklist** chart details and drill-down information, click **Dashboard → Blocklist**.

![Screen capture of the PingIntelligence dashboard blocklist by client type.](_images/lbz1639557294831.png)

## Graph filters

The following **Client type** graph filters are available. Select or clear the check boxes to include or exclude blocked **Client types** in the report, for the specified period:

* Token

* IP

* Cookie

* API Key

* Username

## Blocklist table

The filtered graph results are displayed in a table below the graph, for further drill-down, inspection and analysis.

| Column      | Description                                  |
| ----------- | -------------------------------------------- |
| Client type | The type of client.                          |
| Client ID   | The unique ID of the client that is blocked. |

## Sorting

Click on a table column heading to sort the table according to that column. Click on the column heading again to display a reverse sort according to that column.

## API drill-down

In the **Clients** table, click on an entry in the **Client ID** column, to display the [Client activity](pingintelligence_blocklist_client_activity.html) dashboard with further details about that client's activity in the reported period.

---

---
title: Client activity
description: The Client activity dashboard provides breakdown details about a client's application programming interface (API) activity in the reported period.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_blocklist_client_activity
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_blocklist_client_activity.html
revdate: June 5, 2024
---

# Client activity

The **Client activity** dashboard provides breakdown details about a client's application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* activity in the reported period.

You can navigate to the **Client activity** dashboard in one of the following ways:

* Go to [Dashboard](pingintelligence_dashboard_reference.html)\* → \*[Blocklist](pingintelligence_blocklist.html).

  In the blocked **Clients** table, click the entry in the **Client ID** column to navigate to its detailed breakdown in the **Client activity** dashboard.

* Go to [Attack management](pingintelligence_attack_management.html).

  Choose:

  * On the right side of a client's row in the main **Attack management** list, click the three-dots drop down, then click **Client activity** to navigate to its detailed breakdown in the **Client activity** dashboard.

  * Click a client's row in the main **Attack management** list to navigate to the client's **IoAs** dashboard. At the top of the screen, on the right side of the client's summary line, click the three-dots drop down, then click **Client activity** to navigate to its detailed breakdown in the **Client activity** dashboard.

At the top right, **Close** returns you to the previous dashboard screen that you viewed.

If you navigate to the **Client activity** dashboard from the **Blocklist** dashboard, the **Blocklist** and **Back** navigation controls also appear at the top of the screen, and will return you to the **Blocklist** dashboard.

![Screen capture of PingIntelligence dashboard APIs accessed by the client.](_images/fxd1639559399450.png)

The summary count of APIs accessed by the client for the reported period display in the upper part of the **Client activity** dashboard. You can adjust the reporting period to display counts of APIs accessed for the past day, week, month or six-month periods.

In the lower part of the screen, the following panes display details about the APIs accessed by the client, for the reported period:

| Pane             | Description                                                                                                                                                                                                                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **IoAs**         | List of the types of IoAs based on the client's activity, and the count of IoAs per type.                                                                                                                                                                                                      |
| **Error Codes**  | List of error codes returned from the client's requests to the APIs.                                                                                                                                                                                                                           |
| **Methods**      | List of the API methods used when the client issued API requests, and the count per method.                                                                                                                                                                                                    |
| **APIs**         | List of the APIs receiving requests from the client, and the count of requests per API.                                                                                                                                                                                                        |
| **User**         | List of the usernames issuing requests to the API, and the count of requests per username.                                                                                                                                                                                                     |
| **Device Types** | List of the device types where requests to the API originated, and the count of requests per device type.                                                                                                                                                                                      |
| **Endpoints**    | List of the API endpoints that received requests, and the count of requests per API endpoint.                                                                                                                                                                                                  |
| **IP Address**   | List of the Internet Protocol (IP) *(tooltip: \<div class="paragraph">&#xA;\<p>The method by which data is sent across the internet from the source host to the destination host.\</p>&#xA;\</div>)* addresses where requests to the API originated, and the count of requests per IP address. |

Click **Close** at the top right, to return to the previous dashboard screen.

---

---
title: Client activity
description: The Client activity dashboard provides breakdown details about a client's application programming interface (API) activity in the reported period.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_client_activity
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_client_activity.html
revdate: June 5, 2024
---

# Client activity

The **Client activity** dashboard provides breakdown details about a client's application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* activity in the reported period.

You can navigate to the **Client activity** dashboard in one of the following ways:

* Go to [Dashboard](pingintelligence_dashboard_reference.html)\* → \*[Blocklist](pingintelligence_blocklist.html).

  In the blocked **Clients** table, click the entry in the **Client ID** column to navigate to its detailed breakdown in the **Client activity** dashboard.

* Go to [Attack management](pingintelligence_attack_management.html).

  Choose:

  * On the right side of a client's row in the main **Attack management** list, click the three-dots drop down, then click **Client activity** to navigate to its detailed breakdown in the **Client activity** dashboard.

  * Click a client's row in the main **Attack management** list to navigate to the client's **IoAs** dashboard. At the top of the screen, on the right side of the client's summary line, click the three-dots drop down, then click **Client activity** to navigate to its detailed breakdown in the **Client activity** dashboard.

At the top right, **Close** returns you to the previous dashboard screen that you viewed.

If you navigate to the **Client activity** dashboard from the **Blocklist** dashboard, the **Blocklist** and **Back** navigation controls also appear at the top of the screen, and will return you to the **Blocklist** dashboard.

![Screen capture of PingIntelligence dashboard APIs accessed by the client.](_images/fxd1639559399450.png)

The summary count of APIs accessed by the client for the reported period display in the upper part of the **Client activity** dashboard. You can adjust the reporting period to display counts of APIs accessed for the past day, week, month or six-month periods.

In the lower part of the screen, the following panes display details about the APIs accessed by the client, for the reported period:

| Pane             | Description                                                                                                                                                                                                                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **IoAs**         | List of the types of IoAs based on the client's activity, and the count of IoAs per type.                                                                                                                                                                                                      |
| **Error Codes**  | List of error codes returned from the client's requests to the APIs.                                                                                                                                                                                                                           |
| **Methods**      | List of the API methods used when the client issued API requests, and the count per method.                                                                                                                                                                                                    |
| **APIs**         | List of the APIs receiving requests from the client, and the count of requests per API.                                                                                                                                                                                                        |
| **User**         | List of the usernames issuing requests to the API, and the count of requests per username.                                                                                                                                                                                                     |
| **Device Types** | List of the device types where requests to the API originated, and the count of requests per device type.                                                                                                                                                                                      |
| **Endpoints**    | List of the API endpoints that received requests, and the count of requests per API endpoint.                                                                                                                                                                                                  |
| **IP Address**   | List of the Internet Protocol (IP) *(tooltip: \<div class="paragraph">&#xA;\<p>The method by which data is sent across the internet from the source host to the destination host.\</p>&#xA;\</div>)* addresses where requests to the API originated, and the count of requests per IP address. |

Click **Close** at the top right, to return to the previous dashboard screen.

---

---
title: Client IoAs
description: The Client IoAs (Indicators of Attack) summary chart on the main dashboard screen lists the top IoA counts per client, in descending order.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_client_ioas
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_client_ioas.html
revdate: April 3, 2024
---

# Client IoAs

The **Client IoAs** (Indicators of Attack) summary chart on the main dashboard screen lists the top IoA counts per client, in descending order.

![Screen capture of the PingIntelligence dashboard client IoAs chart.](_images/hwy1639570002755.png)

Click **Dashboard → Client IoAs** to view the **Attack list** on the [Attack management](pingintelligence_attack_management.html) dashboard for further drill-down, inspection and analysis.

---

---
title: Configure API discovery
description: To customize the discovery process, configure the discovery parameters on the Dashboard.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_configure_api_discovery
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_configure_api_discovery.html
revdate: June 5, 2024
section_ids:
  mode: Mode
  discovery-configuration: Discovery Configuration
  default-api-properties: Default API Properties
---

# Configure API discovery

To customize the discovery process, configure the discovery parameters on the **Dashboard**.

Navigate to **Settings → Discovered API**.

Discovery settings consists of the following three parts:

* **Mode** - Configure the mode in which application programming interface (API) *(tooltip: \<div class="paragraph">
  \<p>A specification of interactions available for building software to access an application or service.\</p>
  \</div>)* are published to API Security Enforcer (ASE). The mode can be **Manual** or **Auto**.

* **Discovery Configuration** - Switch discovery on or off, configure the subpath depth of the API base path and discovery interval.

* **Default API Properties** - Configure the default properties of discovered APIs. You can edit the properties of an individual API in manual mode before publishing it to ASE.

The following sections explain each part of Discovery settings in detail.

## Mode

Configure the mode in which dashboard publishes the discovered APIs to ASE. The two modes are:

* **Manual**: In manual mode, you can review the discovered APIs, edit the properties of the APIs and then publish one or more APIs. For more information on editing the discovered APIs, see [Editing discovered APIs](pingintelligence_editing_discovered_apis.html).

  ![Screen capture of PingIntelligence discovery settings- manual mode.](_images/wso1640178994111.png)

* **Auto**: In auto mode, dashboard automatically publishes the APIs after a configured time interval. In auto mode, if you edit an API, it is published in the subsequent interval. Configure the following for auto mode:

  * **Polling Interval** - The time interval at which dashboard publishes APIs to ASE. It is a good practice to have a minimum of a 10 minute interval.

  * **Delete non-discovered APIs** - When enabled, any APIs manually added to ASE are deleted.

  ![Screen capture of PingIntelligence discovery settings - auto mode.](_images/zck1640178316528.png)

* **ASE Deployment** - Displays the ASE deployment mode - inline or sideband.

## Discovery Configuration

Enable or disable discovery from the **Discovery Configuration** tab by toggling the **AI Engine Discovery** button. Configure the following:

* **Discovery Source** - the source for newly discovered APIs. Different options are available based on the platform:

  * PingIntelligence for APIs software supports three sources:

    * AI engine

    * PingAccess

    * Axway API gateway

Refer to [Configure API discovery](pingintelligence_configure_api_discovery.html) for setup instructions.

* **AI Engine Discovery** - Toggle the button to start or stop API discovery. Make sure a root API is configured in ASE for the AI engine to discover APIs. For more information on discovery process, see [API discovery and configuration](pingintelligence_api_discovery_configuration.html).

* **AI Engine Subpath Depth** - Defines the number of subpaths used to uniquely discover the base path of a new API. The maximum allowed value is 6 when ASE is deployed in inline mode and it is 10 when ASE is deployed in sideband mode. For more information, see [Discovery sub-paths](pingintelligence_discovery_subpaths.html).

* **AI Engine Discovery Update Interval** - Defines the time interval at which new discovered APIs are updated in the Dashboard. The minimum value is 1 hour.

![Screen capture of PingIntelligence discovery configuration.](_images/vhc1640179321985.png)

## Default API Properties

You can configure the default API JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
\</div>)* properties from this tab. These properties apply to all discovered APIs. You can edit the properties of the discovered APIs in **manual** mode before publishing. For more information on the API properties, see [Defining an API using API JSON configuration file in inline mode](../pingintelligence_reference_guide/pingintelligence_defining_api_json_configuration_inline.html).

![Screen capture of PingIntelligence discovery settings- default API properties.](_images/lvz1640179585880.png)

---

---
title: Configure API discovery
description: To customize the discovery process, configure the discovery parameters on the Dashboard.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_settings_configure_api_discovery
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_settings_configure_api_discovery.html
revdate: June 5, 2024
section_ids:
  mode: Mode
  discovery-configuration: Discovery Configuration
  default-api-properties: Default API Properties
---

# Configure API discovery

To customize the discovery process, configure the discovery parameters on the **Dashboard**.

Navigate to **Settings → Discovered API**.

Discovery settings consists of the following three parts:

* **Mode** - Configure the mode in which application programming interface (API) *(tooltip: \<div class="paragraph">
  \<p>A specification of interactions available for building software to access an application or service.\</p>
  \</div>)* are published to API Security Enforcer (ASE). The mode can be **Manual** or **Auto**.

* **Discovery Configuration** - Switch discovery on or off, configure the subpath depth of the API base path and discovery interval.

* **Default API Properties** - Configure the default properties of discovered APIs. You can edit the properties of an individual API in manual mode before publishing it to ASE.

The following sections explain each part of Discovery settings in detail.

## Mode

Configure the mode in which dashboard publishes the discovered APIs to ASE. The two modes are:

* **Manual**: In manual mode, you can review the discovered APIs, edit the properties of the APIs and then publish one or more APIs. For more information on editing the discovered APIs, see [Editing discovered APIs](pingintelligence_editing_discovered_apis.html).

  ![Screen capture of PingIntelligence discovery settings- manual mode.](_images/wso1640178994111.png)

* **Auto**: In auto mode, dashboard automatically publishes the APIs after a configured time interval. In auto mode, if you edit an API, it is published in the subsequent interval. Configure the following for auto mode:

  * **Polling Interval** - The time interval at which dashboard publishes APIs to ASE. It is a good practice to have a minimum of a 10 minute interval.

  * **Delete non-discovered APIs** - When enabled, any APIs manually added to ASE are deleted.

  ![Screen capture of PingIntelligence discovery settings - auto mode.](_images/zck1640178316528.png)

* **ASE Deployment** - Displays the ASE deployment mode - inline or sideband.

## Discovery Configuration

Enable or disable discovery from the **Discovery Configuration** tab by toggling the **AI Engine Discovery** button. Configure the following:

* **Discovery Source** - the source for newly discovered APIs. Different options are available based on the platform:

  * PingIntelligence for APIs software supports three sources:

    * AI engine

    * PingAccess

    * Axway API gateway

Refer to [Configure API discovery](pingintelligence_configure_api_discovery.html) for setup instructions.

* **AI Engine Discovery** - Toggle the button to start or stop API discovery. Make sure a root API is configured in ASE for the AI engine to discover APIs. For more information on discovery process, see [API discovery and configuration](pingintelligence_api_discovery_configuration.html).

* **AI Engine Subpath Depth** - Defines the number of subpaths used to uniquely discover the base path of a new API. The maximum allowed value is 6 when ASE is deployed in inline mode and it is 10 when ASE is deployed in sideband mode. For more information, see [Discovery sub-paths](pingintelligence_discovery_subpaths.html).

* **AI Engine Discovery Update Interval** - Defines the time interval at which new discovered APIs are updated in the Dashboard. The minimum value is 1 hour.

![Screen capture of PingIntelligence discovery configuration.](_images/vhc1640179321985.png)

## Default API Properties

You can configure the default API JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
\</div>)* properties from this tab. These properties apply to all discovered APIs. You can edit the properties of the discovered APIs in **manual** mode before publishing. For more information on the API properties, see [Defining an API using API JSON configuration file in inline mode](../pingintelligence_reference_guide/pingintelligence_defining_api_json_configuration_inline.html).

![Screen capture of PingIntelligence discovery settings- default API properties.](_images/lvz1640179585880.png)

---

---
title: Configuring API discovery
description: To configure API discovery in your environment:
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_configuring_api_discovery
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_configuring_api_discovery.html
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring API discovery

## About this task

To configure API discovery in your environment:

## Steps

1. Enable ABS in ASE.

2. Define `root` API JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
   \<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
   \</div>)* in ASE.

   |   |                                                       |
   | - | ----------------------------------------------------- |
   |   | ABS discovers APIs only for a `root` API JSON in ASE. |

3. Optionally, configure OAuth token and API Key parameters in `root` API JSON.

4. Configure discovery related parameters using [Global configuration update REST API](../pingintelligence_reference_guide/pingintelligence_global_configuration_update_rest_api.html).

   |   |                                                                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Use the `update.sh` script to edit the default values related to API discovery. For more information on update script, see [Managing discovery intervals](pingintelligence_managing_discovery_intervals.html). |

---

---
title: Configuring ASE for API discovery
description: The following table summarizes the variables related to API discovery that you need to configure.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_configuring_ase_api_discovery
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_configuring_ase_api_discovery.html
revdate: April 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
---

# Configuring ASE for API discovery

## About this task

The following table summarizes the variables related to API discovery that you need to configure.

**API discovery variables**

| Variable                    | Description                                                                                                                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_discovery`             | Set this variable to **true** to switch on API discovery. To switch off API discovery, set it to **false**. The default value is **true**.                                                      |
| `discovery_initial_period`  | The initial time in hours during which APIs are discovered in your API ecosystem. The default and minimum value is 1-hour.                                                                      |
| `discovery_update_interval` | The time interval in hours at which any new discovered APIs are reported. The default and minimum value is 1-hour.                                                                              |
| `discovery_subpath`         | The number of sub-paths that is discovered in an API. The minimum value is 1 and maximum value is 6. For more information, see [Discovery sub-paths](pingintelligence_discovery_subpaths.html). |
| `url_limit`                 | Defines the maximum number of URLs that are reported in a discovered API.                                                                                                                       |

To configure ASE for API discovery:

## Steps

* Enable ABS in ASE by running the `enable_abs` command in ASE:

  ```
  ./bin/cli.sh -u admin -p admin enable_abs
  ABS is now enabled
  ```

* To verify, run the `status` command in ASE:

  ```
  ./bin/cli.sh status
  API Security Enforcer
  status                  : started
  mode                    : sideband
  http/ws                 : port 80
  https/wss               : port 443
  firewall                : enabled
  abs                     : enabled, ssl: enabled
  abs attack              : disabled
  audit                   : enabled
  sideband authentication : disabled
  ase detected attack     : disabled
  attack list memory      : configured 128.00 MB, used 25.60 MB, free 102.40 MB
  google pubsub           : disabled
  ```

* To configure root API in ASE, define `root` API in ASE.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If you have configured other APIs in ASE along with the `root` API, ABS monitors traffic only on the root API for the discovery process. A `root` API in ASE is an API for which the API JSON file has `url` as `"/"` and `hostname` as `"*"`.If API discovery is enabled in ABS without `root` API in ASE and you run the `discovery` REST API, it displays an error message: `root API not configured in ASE. To discover APIs configure root API in ASE`. |

  ### Example:

  The following is a snippet of `root` API JSON:

  ```json
  {
      "api_metadata": {
          "protocol": "http",
          "url": "/",
          "hostname": "*",

          "cookie": "",
          "oauth2_access_token": false,
          "apikey_qs": "",
          "apikey_header": "",
          "enable_blocking": false,
          "cookie_idle_timeout": "200m",
          "logout_api_enabled": false,
          "cookie_persistence_enabled": false,
          "login_url": "",
          "api_mapping": {
              "internal_url": ""
          },
  ```

  |   |                                                                                 |
  | - | ------------------------------------------------------------------------------- |
  |   | A sample `root` API ships with ASE in `/pingidentity/ase/config/api` directory. |

* Configure API JSON by configuring the settings for `cookie`, `oauth2_access_token`, `apikey_qs`, or `apikey_header` in the `root` API JSON file in ASE.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | API discovery process discovers these parameters in an API only when you set these in the root API. API discovery reports these attributes of an API only when it receives at least 50% of traffic having these attributes. For example, if the root API receives 100 requests and 51 requests have OAuth token, then the OAuth token is reported in the discovered API. Similarly, if the same traffic has less than 50% traffic for API keys or cookies, then they are not reported in the discovered API. |

* Configure API discovery in ABS by setting the `api_discovery` parameter to `true` using [Global configuration update REST API](../pingintelligence_reference_guide/pingintelligence_global_configuration_update_rest_api.html).

  |   |                                                                                                                                                                                                                            |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you want update the values on an already running system, use the `update.sh` script. For more information on the update script, see [Managing discovery intervals](pingintelligence_managing_discovery_intervals.html). |

---

---
title: Configuring training settings
description: Artificial intelligence (AI) training depends on a set of training parameters in the AI engine. You can configure training variables or reset the trained application programming interface (API) in the AI engine from the Dashboard.
component: pingintelligence
version: 5.2
page_id: pingintelligence:managing_pingintelligence_for_apis:pingintelligence_configuring_training_settings
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/managing_pingintelligence_for_apis/pingintelligence_configuring_training_settings.html
revdate: April 3, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  related-links: Related links
---

# Configuring training settings

Artificial intelligence (AI) training depends on a set of training parameters in the AI engine. You can configure training variables or reset the trained application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* in the AI engine from the Dashboard.

## Before you begin

You must have:

* Admin user privileges to configure and update the training settings.

## About this task

The following steps provide an overview of the training parameters that can be configured through the Dashboard. It is recommended that you review the variables and configure the best values for your environment.

## Steps

* Click **Settings → Training Settings**. By default, you will reach the**Global Configuration** page.

  ![Screen capture of PingIntelligence training settings - global configuration.](_images/xoh1640181471971.png)

* You can configure the following settings in the **Global Configuration** page.

  * **TRAINING PERIOD**: The number of hours to train the AI model before it moves to attack detection mode. It is recommended that you configure the training for at least a week's duration in a production environment.

  * **TRAINING UPDATE INTERVAL**: The time interval at which continuous learning model thresholds are updated in the AI engine.

These variables are specified in hours with an allowable range of 1 to 10000. Click **Save** on the bottom-left to reflect the changes.

* You can reset the training of an API or multiple APIs from the**Reset Training** page. To reset the training, select the APIs in **RESET TRAINING** and click **Go**.

  |   |                                                                                                                                                                                                                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If there are any pending jobs in the AI engine, the reset will fail with an error notification. You can re-run the reset training after a few minutes. If the reset fails multiple times, follow the steps explained in [Resetting trained APIs in ABS](pingintelligence_resetting_trained_apis.html) to manually reset the API. |

  ![Screen capture of PingIntelligence training settings - reset training.](_images/foc1640181689517.png)

## Related links

* [Training the ABS model](pingintelligence_training_abs_model.html)

* [AI engine training variables](pingintelligence_ai_engine_training_variables.html)

* [Update the training variables](pingintelligence_update_training_variables.html)

* [Resetting trained APIs](pingintelligence_resetting_trained_apis.html)