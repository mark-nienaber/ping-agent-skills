---
title: API discovery in your environment
description: PingIntelligence supports API discovery in sideband and inline mode as an automated method of building API definitions that provide the properties of the managed APIs.
component: pingintelligence
version: 5.2
page_id: pingintelligence:getting_started_with_pingintelligence:pingintelligence_api_discovery_environment
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/getting_started_with_pingintelligence/pingintelligence_api_discovery_environment.html
revdate: April 3, 2024
section_ids:
  configuring-ase-with-api-discovery: Configuring ASE with API discovery
  about-this-task: About this task
  steps: Steps
  example: Example:
  configuring-discovery-settings-in-the-dashboard: Configuring discovery settings in the Dashboard
  about-this-task-2: About this task
  steps-2: Steps
  example-2: Example:
---

# API discovery in your environment

PingIntelligence supports API discovery in sideband and inline mode as an automated method of building API definitions that provide the properties of the managed APIs.

These API definitions are then used to provide API visibility and detection of anomalous client behavior. You can configure API discovery through the Dashboard, which displays, manages, and renders the discovered APIs. The Dashboard also allows you to edit the discovered APIs and export their definition files.

To set up PingIntelligence for discovery, you must:

1. [Configure ASE with API discovery](pingintelligence_configure_ase_discovery_api.html)

2. [Configure discovery settings in the Dashboard](pingintelligence_configure_discovery_settings.html)

## Configuring ASE with API discovery

### About this task

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Configure API discovery when API Security Enforcer (ASE) is deployed in sideband mode. To configure ASE for inline discovery, contact Ping Identity support. |

ASE requires a `root` definition that enables it to route all API traffic to the AI engine. The AI engine receives and monitors all API traffic that is not associated with a known API. It analyzes the traffic and builds API models for the unknown APIs, which are shown on the Discovery dashboard.

To add a `root` API in ASE:

### Steps

1. Use the sample `root` API JSON shipped with ASE in the `<ASE_Installation path>/pingidentity/ase/config/api/` directory and configure the API JSON for the `root` API.

   For sideband environments, use the following settings:

   | Parameter  | Setting |
   | ---------- | ------- |
   | `protocol` | `http`  |
   | `url`      | `/`     |
   | `hostname` | `*`     |

2. To capture client identifiers such as token, cookies, API keys, IP addresses, and username, configure the `root` API JSON file with the following client identifiers.

   |   |                                                                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the identifiers are not present in at least 50% of the traffic received for a discovered API, then the identifiers are not reported or used in Indicator of Attack (IoA) detection. |

   | Client Identifier              | Description                                                                      |
   | ------------------------------ | -------------------------------------------------------------------------------- |
   | `oauth2_access_token`          | If a bearer token is present, set to `true`.                                     |
   | `cookie`                       | If cookies are used as the primary client identifier, configure the cookie name. |
   | `apikey_qs` or `apikey_header` | Set for the API key in query parameter or for the API key in header.             |

   #### Example:

   The following is a sample API JSON for the `root` API:

   ```json
   {
    "api_metadata": {
    "protocol": "http",
    "url": "/",
    "hostname": "*",
    "cookie": "",
    "oauth2_access_token": true,
    "apikey_qs": "",
    "apikey_header": "",
    "login_url": "",
    "enable_blocking": true,
    "api_memory_size": "1mb",
    "decoy_config":
   { "decoy_enabled": false, "response_code": 200, "response_def": "", "response_message": "", "decoy_subpaths": [] }
   }
    }
   ```

   |   |                                                     |
   | - | --------------------------------------------------- |
   |   | IP addresses and usernames are captured separately. |

3. After configuring an API JSON file for the `root` API, add it to ASE to initiate the API discovery process by running the following command:

   ```
   /<ASE_Installation path>/pingidentity/ase/bin/cli.sh –u admin -p admin add_api {file_path/api_name}
   ```

## Configuring discovery settings in the Dashboard

### About this task

To customize the discovery process, configure the discovery parameters on the Dashboard.

### Steps

1. Go to **Discovered APIs → Settings**.

![A screen capture of the Discovered APIs page in PingIntelligence with the Discovered APIs and Settings links highlighted in yellow. Discovered APIs is numbered 1, and Settings is numbered 2 to show the order of your clicks.](_images/hkd1607595182330.png)

1. Click the **Discovery Configuration** tab and set the value for **AI Engine Subpath Depth**.

   **AI Engine Subpath Depth** defines the number of subpaths used to uniquely discover the base path of a new API. The maximum allowed value is 6 when ASE is deployed in inline mode and 10 when ASE is deployed in sideband mode.

   #### Example:

   The following are examples of subpath values and what they mean:

   * `1` indicates `/atmapp` is the base path for `/atmapp/zipcode`,`/atmapp/update`, and so on.

   * `3` indicates `v1/cust1/atmapp` is the base path for `v1/cust1/atmapp/zipcode`, and so on.

2. Click **Discovered APIs** on the Dashboard and click **Export** to download the API definition in `.json` format .

   ![A screen capture of the Discovered APIs page in the PingIntelligence Dashboard with a yellow arrow pointing to Discovered APIs in the left navigation pane and a second yellow arrow pointing to the Export link next to an API definition.](_images/qyl1631090190432.png)

3. Add the downloaded API JSON definitions to ASE by running the following command:

   ```
   # /<ASE_Installation path>/pingidentity/ase/bin/cli.sh –u admin -p admin add_api {file_path/api_name}
   ```

---

---
title: API environment integration with on-premise ASE
description: Configure the deployment mode in API Security Enforcer (ASE) and integrate your API environment with ASE.
component: pingintelligence
version: 5.2
page_id: pingintelligence:getting_started_with_pingintelligence:pingintelligence_api_environment_ase
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/getting_started_with_pingintelligence/pingintelligence_api_environment_ase.html
revdate: May 6, 2024
section_ids:
  sideband-deployment: Sideband deployment
  configure-ase-for-sideband-deployment: Configure ASE for sideband deployment
  inline-environment: Inline environment
---

# API environment integration with on-premise ASE

Configure the deployment mode in API Security Enforcer (ASE) and integrate your API environment with ASE.

Ping Identity supports two integration options for your API environment:

* Sideband deployment

* Inline deployment

## Sideband deployment

When deployed in sideband mode, ASE receives API calls from an API gateway, which passes API traffic information for artificial intelligence (AI) processing. ASE requires no changes to clients or backend API servers. In sideband deployment, ASE works along with the API gateway to protect your API environment. A custom sideband policy is provided, which is deployed in the gateway to route the API traffic. The following diagram shows ASE in sideband deployment mode.

![A diagram of PingIntelligence ASE in sideband deployment mode.](_images/lqz1631624498743.png)

To configure ASE for a sideband environment, see [#/section\_hrs\_jnh\_vqb](#/section_hrs_jnh_vqb).

## Configure ASE for sideband deployment

PingIntelligence provides custom sideband policies for API gateways, routers, and other API platforms to support integration with your API environments. See [API gateway integrations supported by PingIntelligence](https://www.pingidentity.com/en/resources/downloads/pingintelligence.html) for a list of gateway integrations supported along with the deployment instructions. The sideband policy is deployed in your API gateway, and it sends the request and response API metadata to ASE for processing. Follow the instructions in the integration guides to deploy a sideband policy in your environment.

After you determine which API gateways to integrate, set the deployment mode in the `ase.conf` file located in the `/<ASE installation path>/pingidentity/ase/config/` directory.

| Parameter                        | Description                                                                                                                                                                                                                                                                                                |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `mode`                           | Set the mode to `sideband` for ASE to work in a sideband mode.                                                                                                                                                                                                                                             |
| `enable_sideband_keepalive`      | When set to `true`, ASE sends a keep-alive in response header for the TCP connection between API gateway and ASE. With the default `false` value, ASE sends a connection close in the response header for connection between API gateway and ASE.&#xA;&#xA;Set to trueunless using a MuleSoft API gateway. |
| `enable_sideband_authentication` | Set to `true` if you intend to enable authentication between an API gateway and ASE. After setting it to `true`, generate a sideband authentication token using the ASE `create_sideband_token` command.&#xA;&#xA;Set to false for evaluation deployments to simplify setup.                               |

|   |                                                                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | After updating the settings, restart ASE using the following commands:- Change the working directory to `/bin` and run the `stop.sh` script:

  ```
  # /<ASE installation path>/pingidentity/ase/bin/stop.sh
  ```

- Change the working directory to `/bin` and run the `start.sh` script:

  ```
  # /<ASE installattion path>/pingidentity/ase/bin/start.sh
  ``` |

## Inline environment

When deployed in inline mode, ASE is a reverse proxy deployed between the API clients and servers. It is typically deployed behind load balancers, such as AWS Elastic Load Balancing (ELB), to distribute traffic across an ASE cluster for high availability. ASE terminates SSL connections from API clients and then routes the requests to the destination APIs on an API gateway or app servers, such as Node.js, WebLogic, or Tomcat. The following diagram shows an inline deployment.

![A diagram of PingIntelligence ASE inline mode.](_images/mhv1631624887581.png)

|   |                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------ |
|   | To continue with an inline deployment, see [Inline ASE](../pingintelligence_reference_guide/pingintelligence_inline_ase.html). |

---

---
title: Configuring ASE with API discovery
description: Configure API discovery when API Security Enforcer (ASE) is deployed in sideband mode. To configure ASE for inline discovery, contact Ping Identity support.
component: pingintelligence
version: 5.2
page_id: pingintelligence:getting_started_with_pingintelligence:pingintelligence_configure_ase_discovery_api
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/getting_started_with_pingintelligence/pingintelligence_configure_ase_discovery_api.html
revdate: April 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
---

# Configuring ASE with API discovery

## About this task

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Configure API discovery when API Security Enforcer (ASE) is deployed in sideband mode. To configure ASE for inline discovery, contact Ping Identity support. |

ASE requires a `root` definition that enables it to route all API traffic to the AI engine. The AI engine receives and monitors all API traffic that is not associated with a known API. It analyzes the traffic and builds API models for the unknown APIs, which are shown on the Discovery dashboard.

To add a `root` API in ASE:

## Steps

1. Use the sample `root` API JSON shipped with ASE in the `<ASE_Installation path>/pingidentity/ase/config/api/` directory and configure the API JSON for the `root` API.

   For sideband environments, use the following settings:

   | Parameter  | Setting |
   | ---------- | ------- |
   | `protocol` | `http`  |
   | `url`      | `/`     |
   | `hostname` | `*`     |

2. To capture client identifiers such as token, cookies, API keys, IP addresses, and username, configure the `root` API JSON file with the following client identifiers.

   |   |                                                                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the identifiers are not present in at least 50% of the traffic received for a discovered API, then the identifiers are not reported or used in Indicator of Attack (IoA) detection. |

   | Client Identifier              | Description                                                                      |
   | ------------------------------ | -------------------------------------------------------------------------------- |
   | `oauth2_access_token`          | If a bearer token is present, set to `true`.                                     |
   | `cookie`                       | If cookies are used as the primary client identifier, configure the cookie name. |
   | `apikey_qs` or `apikey_header` | Set for the API key in query parameter or for the API key in header.             |

   ### Example:

   The following is a sample API JSON for the `root` API:

   ```json
   {
    "api_metadata": {
    "protocol": "http",
    "url": "/",
    "hostname": "*",
    "cookie": "",
    "oauth2_access_token": true,
    "apikey_qs": "",
    "apikey_header": "",
    "login_url": "",
    "enable_blocking": true,
    "api_memory_size": "1mb",
    "decoy_config":
   { "decoy_enabled": false, "response_code": 200, "response_def": "", "response_message": "", "decoy_subpaths": [] }
   }
    }
   ```

   |   |                                                     |
   | - | --------------------------------------------------- |
   |   | IP addresses and usernames are captured separately. |

3. After configuring an API JSON file for the `root` API, add it to ASE to initiate the API discovery process by running the following command:

   ```
   /<ASE_Installation path>/pingidentity/ase/bin/cli.sh –u admin -p admin add_api {file_path/api_name}
   ```

---

---
title: Configuring discovery settings in the Dashboard
description: To customize the discovery process, configure the discovery parameters on the Dashboard.
component: pingintelligence
version: 5.2
page_id: pingintelligence:getting_started_with_pingintelligence:pingintelligence_configure_discovery_settings
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/getting_started_with_pingintelligence/pingintelligence_configure_discovery_settings.html
revdate: April 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
---

# Configuring discovery settings in the Dashboard

## About this task

To customize the discovery process, configure the discovery parameters on the Dashboard.

## Steps

1. Go to **Discovered APIs → Settings**.

![A screen capture of the Discovered APIs page in PingIntelligence with the Discovered APIs and Settings links highlighted in yellow. Discovered APIs is numbered 1, and Settings is numbered 2 to show the order of your clicks.](_images/hkd1607595182330.png)

1. Click the **Discovery Configuration** tab and set the value for **AI Engine Subpath Depth**.

   **AI Engine Subpath Depth** defines the number of subpaths used to uniquely discover the base path of a new API. The maximum allowed value is 6 when ASE is deployed in inline mode and 10 when ASE is deployed in sideband mode.

   ### Example:

   The following are examples of subpath values and what they mean:

   * `1` indicates `/atmapp` is the base path for `/atmapp/zipcode`,`/atmapp/update`, and so on.

   * `3` indicates `v1/cust1/atmapp` is the base path for `v1/cust1/atmapp/zipcode`, and so on.

2. Click **Discovered APIs** on the Dashboard and click **Export** to download the API definition in `.json` format .

   ![A screen capture of the Discovered APIs page in the PingIntelligence Dashboard with a yellow arrow pointing to Discovered APIs in the left navigation pane and a second yellow arrow pointing to the Export link next to an API definition.](_images/qyl1631090190432.png)

3. Add the downloaded API JSON definitions to ASE by running the following command:

   ```
   # /<ASE_Installation path>/pingidentity/ase/bin/cli.sh –u admin -p admin add_api {file_path/api_name}
   ```