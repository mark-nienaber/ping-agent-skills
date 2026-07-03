---
title: Apigee API gateway integration
description: Ping Identity's shared flow for Apigee extends Apigee's authorization capabilities through an external policy evaluation service.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_integrations:paz_apigee_integration
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_integrations/paz_apigee_integration.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 16, 2025
---

# Apigee API gateway integration

Ping Identity's shared flow for Apigee extends Apigee's authorization capabilities through an external policy evaluation service.

Integration with Apigee allows centralized management of API access control and application protection in PingAuthorize while delegating enforcement to Apigee. Learn more about how this integration kit interacts with PingAuthorize in [API gateway integration](../pingauthorize_server_administration_guide/paz_api_gw_integration.html).

Install and configure the integration kit in Apigee to enable management of access control rules in PingAuthorize.

To configure the integration kit:

1. [Set up PingAuthorize](paz_apigee_integration_paz_setup.html) for Apigee integration.

2. [Configure Apigee](paz_apigee_integration_apigee_setup.html) for PingAuthorize integration.

---

---
title: Applying the custom MuleSoft policy for PingAuthorize
description: You must apply the deployed custom MuleSoft policy to use MuleSoft as an application programming interface (API) gateway with PingAuthorize.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_integrations:paz_apply_mulesoft_policy_paz
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_integrations/paz_apply_mulesoft_policy_paz.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Applying the custom MuleSoft policy for PingAuthorize

You must apply the deployed custom MuleSoft policy to use MuleSoft as an application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* gateway with PingAuthorize.

## About this task

The PingAuthorize policy supports HTTP APIs configured with the `Endpoint with proxy` or `Basic Endpoint` options.

## Steps

1. Sign on to your MuleSoft Anypoint account.

2. Go to the API manager, expand the API to which you want to attach the PingAuthorize policy, and click **Version**.

   ![Screen capture of the Manage API screen in the MuleSoft API Manager with a callout highlighting the Version value](_images/bhz1626284943995.png)

3. In the left navigation pane, click **Policies**.

   The **Policies** page supports applying the PingAuthorize policy to the API.

   ![Screen capture of the PingAuthorizeAPI v1 - Settings window under the Policies tab (highlighted) in the MuleSoft API Manager](_images/ewo1626284987474.png)

4. Click **Apply New Policy**.

   ![Screen capture of the PingAuthorizeAPI v1 Policies window under the Policies tab with the Apply New Policy button highlighted in lower center of the screen](_images/pyz1626285305789.png)

   ### Result:

   The **Select Policy** window opens.

5. In the **Select Policy** window, select the PingAuthorize policy and current version. Click **Configure Policy**.

   ![Screen capture of the Select Policy page with the PingAuthorize policy highlighted](_images/ame1626285146143.png)

6. On the **Apply Policy** page, enter the following values:

   1. In the **PAZ Token** field, enter the sideband adapter shared secret generated as part of the prerequisites in [Deploying the custom MuleSoft policy for PingAuthorize](paz_deploy_mulesoft_policy_paz.html).

   2. In the **PAZ Host** field, enter the PingAuthorize host and port.

      |   |                                                               |
      | - | ------------------------------------------------------------- |
      |   | Do not include the connection scheme (http\:// or https\://). |

   3. Select the **Enable SSL** check box for a secure HTTPS connection between MuleSoft and PingAuthorize.

   4. Select the **Allow self-signed certificate** check box to enable MuleSoft to accept a self-signed certificate from PingAuthorize.

      For information about configuring PingAuthorize to use trusted certificates, see [Importing signed and trusted certificates](../pingauthorize_server_administration_guide/paz_import_signed_certs.html).

   5. Select an access token type:

      Choose from:

      * Use Authorization Header: Indicates that the authorization header of an incoming request should be passed to PingAuthorize and used to authorize the client.

      * Use hard-coded parsed access token: Allows configuration of an access token that will be used for every request. Use this only for testing purposes.

      * Use parsed access token: Allows configuration of a DataWeave expression for retrieving a parsed access token from the Mule message. When you use MuleSoft's OAuth 2.0 Token Enforcement policies to obtain a parsed access token, use the expression `#[authentication.properties.userProperties]`. For more information, see [DataWeave Language](https://docs.mulesoft.com/mule-runtime/4.3/dataweave).

   6. **Optional:** Configure the **Connection Timeout** and **Read Timeout**.

   Timeouts govern the behavior of the API gateway when it cannot connect to PingAuthorize or the response from PingAuthorize is delayed.

   \+

   | Timeout parameter  | Description                                                                                                                                             |
   | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Connection Timeout | Governs the time the API gateway waits to establish a connection with PingAuthorize, following which it sends the client request to the backend server. |
   | Read Timeout       | Governs the time the API Gateway waits for PingAuthorize's response before sending the request to the backend server.                                   |

   \+

   |   |                                                                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The default value is 5000 milliseconds (5 seconds). It's good practice to configure a small value to limit the delay in case PingAuthorize isn't reachable or is unresponsive. |

   1. **Optional:** Select the **Enable debug logging** check box to see requests sent to PingAuthorize Server along with responses.

   2. **Optional:** Configure **Methods & Resource Conditions**.

      See [Resource-Level Policies](https://docs.mulesoft.com/api-manager/2.x/policies-policy-level) for more information.

      ![Screen capture of the Apply PingAuthorize policy page with fields completed as directed in steps 6a-h and in the Apply button in the lower right](_images/fej1626285074831.png)

## Next steps

If there are any changes to PingAuthorize endpoints, repeat the process explained in step 6 and re-deploy the configuration.

---

---
title: Configuring Apigee for PingAuthorize integration
description: Install the PingAuth shared flow bundle in Apigee and configure it to integrate with PingAuthorize.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_integrations:paz_apigee_integration_apigee_setup
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_integrations/paz_apigee_integration_apigee_setup.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 16, 2025
page_aliases: ["paz_apigee_integration_oauth.adoc"]
section_ids:
  before-you-begin: Before you begin
  adding-the-pingauthorize-shared-flow-to-apigee: Adding the PingAuthorize shared flow to Apigee
  steps: Steps
  adding-an-api-proxy-in-apigee: Adding an API proxy in Apigee
  steps-2: Steps
  attaching-the-pingauthorize-shared-flow-to-api-proxies: Attaching the PingAuthorize shared flow to API proxies
  steps-3: Steps
  next-steps: Next steps
---

# Configuring Apigee for PingAuthorize integration

Install the PingAuth shared flow bundle in Apigee and configure it to integrate with PingAuthorize.

## Before you begin

Ensure you have:

* A supported Apigee environment. The Ping Identity shared flow for Apigee supports Apigee Edge, Apigee Private Cloud, and Apigee X.

* The PingAuth shared flow bundle `.zip` archive. Download the integration kit for Apigee from the [Ping Identity Marketplace](https://marketplace.pingone.com/item/external-authorization-for-apigee-api-management).

## Adding the PingAuthorize shared flow to Apigee

### Steps

1. Upload the shared flow bundle:

   1. In Apigee, go to **Develop > Shared Flows** and do one of the following:

      * In Apigee X, click **Upload Bundle**.

      * In Apigee Edge or Apigee Private Cloud, click **+Shared Flow**, and then click **Upload Bundle**.

   2. For the shared flow name, enter `PingAuth`.

   3. In **File Picker**, select the PingAuth shared flow bundle `.zip` archive.

   4. Click **Create**.

2. In Apigee X, configure the connection to PingAuthorize.

   |   |                                                                                                                                                                                                                                                                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Skip this step if you're using Apigee Edge or Apigee Private Cloud.Apigee X doesn't support managing the configuration values stored in key-value maps through the Apigee UI. You must add these configuration values to the key-value map policy. The key-value map is created and the configuration values are added the first time the PingAuth shared flow executes at runtime. |

   1. To access the PingAuth shared flow, go to **Develop > Shared Flows > PingAuth**.

   2. Click the **Develop** tab and examine **Revisions** to make sure you're on the latest revision.

   3. In the **Policies** panel on the left, click the **Load KVM Config** policy.

   4. In the **Code** panel, remove the comment lines above and below the `InitialEntries` element.

   5. Edit the value for `service_host_port` to match the host name of your PingAuthorize server instance and the port of the HTTPS connection handler.

      For example, `pingauthorize:8443`.

      |   |                                                                                                                                                                          |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | You can find the HTTPS connection handler port from the **Configuration** page of the PingAuthorize administrative console by going to **System > Connection Handlers**. |

   6. Edit the value of `shared_secret` to match the shared secret that you created in PingAuthorize.

   7. Click **Save**.

      Your flow configuration should look like this:

      ![Screen capture of the Apigee X key-value map configuration for the PingAuth shared flow](_images/ffq1673453482242.png)

3. In Apigee Edge or Apigee Private Cloud, configure the connection to PingAuthorize.

   Apigee Edge stores environment-specific configuration values in key-value maps so that the same policies can be used across multiple deployment environments without any changes to the policies.

   1. Go to **Environment > Key Value Maps** and click **+Key Value Map**.

   2. Edit the key-value map and click **Add Entry**.

   3. Add a `service_host_port` key and set the value to the host name of your PingAuthorize Server instance and the port of the HTTPS connection handler.

      For example, `pingauthorize:8443`.

   4. Add a `shared_secret` key and set the value to the shared secret that you created in PingAuthorize.

   5. Click **Save**.

      Your key-value map configuration should look like this:

      ![Screen capture of the Apigee Edge and Private Cloud key-value map configuration for the PingAuth shared flow](_images/bsl1673464931416.png)

4. (Optional) Configure HTTPS trust for PingAuthorize.

   By default, the PingAuth shared flow only trusts the PingAuthorize HTTPS connection handler certificate if the certificate is issued from a well-known certificate authority. To enable Apigee to trust specific HTTPS certificates from PingAuthorize Server:

   1. Go to **Environment > TLS Keystores** and click **+Keystore**.

   2. Give the key store a name that helps you identify your PingAuthorize environment.

      For example, `PingAuthorize-dev-truststore`.

   3. Click the **[icon: plus, set=fa]**button to add a certificate.

   4. Enter a certificate alias and upload the certificate configured for the HTTPS connection handler in PingAuthorize.

      ![Screen capture of the TLS keystores page in Apigee with a PingAuth key store that contains the server certificate](_images/lvb1673472356000.png)

   5. Click **Save**.

   6. Go to **Environment > References** and click **+Reference**.

   7. Name the new reference `PingAuthTrust`.

   8. Select the key store that you created previously and click **Save**.

      ![Screen capture of the Apigee References page after creating a PingAuthorize key store reference called PingAuthTrust](_images/wzr1673478146725.png)

   9. Go to **Develop > Shared Flows > PingAuth**.

   10. On the **Develop** tab, examine **Revisions** to make sure you're on the latest revision.

   11. In the **Policies** panel on the left, click the **Sideband Call** policy.

   12. In the **Code** panel, remove the comment characters surrounding the `TrustStore` element.

       ![Screen capture of the Apigee Sideband Call policy with the PingAuthTrust key store trust enabled](_images/oiz1673481545287.png)

   13. Click **Save**.

5. Go to **Develop > Shared Flows > PingAuth** and deploy the most recent revision to your environment.

## Adding an API proxy in Apigee

Configure the API proxy in Apigee to point to the target endpoint that you want to reach.

### Steps

1. Go to **API Proxies > Create Proxy** and click the **Reverse proxy** tile.

   ![Screen capture of the Apigee API proxy creation menu](_images/ady1673482825535.png)

2. On the **Proxy details** page, enter the **Name**, **Base path**, and **Target (Existing API)**.

   ![Screen capture of the Apigee API proxy configuration details](_images/lys1673482884351.png)

3. On the **Common policies** page, click **Pass through (no authorization)**.

   ![Screen capture of the Apigee API proxy authorization options with Pass through (no authorization) selected in the Security: Authorization section](_images/oba1673482953561.png)

4. Select the checkbox for your deployment environment.

   ![Screen capture of the Apigee API proxy deployment environment option](_images/lvh1673483013667.png)

5. Click **Create and Deploy**.

## Attaching the PingAuthorize shared flow to API proxies

Attach the PingAuth shared flow to the API proxies where you want to use PingAuthorize as the external authorization policy runtime service.

### Steps

1. Add a Flow Callout policy:

   1. Go to one of your APIs in **Develop > API Proxies** and click the **Develop** tab.

      |   |                                                     |
      | - | --------------------------------------------------- |
      |   | Ensure you are on the latest revision of the proxy. |

   2. In the **Policies** panel on the left, click the **[icon: plus, set=fa]**icon.

   3. In the **Add Policy** modal, in the **Extension** panel on the left, click **Flow Callout**.

   4. Enter a **Name** for the policy.

      ![Screen capture of the Apigee Add Policy window for Flow Callout policy creation](_images/lbu1673538233229.png)

   5. In the **Shared Flow** list, select **PingAuth**, and then click **Add**.

2. Attach the Flow Callout policy to flows.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Because PingAuthorize provides fine-grained authorization, you should integrate PingAuthorize late in the PreFlow of the request to the proxy endpoint, after coarse-grained authentication and authorization functions. Learn more about other ways to integrate PingAuthorize in [Controlling API proxies with flows](https://cloud.google.com/apigee/docs/api-platform/fundamentals/what-are-flows) in the Apigee documentation. |

   1. In the **Proxy Endpoints** panel on the left, click **PreFlow**.

   2. In the **Request** section, click **+Step** to add a flow step to the request.

      ![Screen capture of the Apigee proxy endpoint PreFlow step creation](_images/enw1673557889222.png)

   3. In the **Add Step** modal, click the **Existing** tab, and then select the Flow Callout policy you created previously.

      ![Screen capture of the Apigee proxy endpoint PreFlow step configuration details](_images/tcv1673558059654.png)

   4. Click **Add**.

   5. In the **Target Endpoints** panel on the left, select **PreFlow**.

   6. In the **Response** section, click **+Step** to add a flow step to the response.

      |   |                                                                                                            |
      | - | ---------------------------------------------------------------------------------------------------------- |
      |   | This allows PingAuthorize to process the API response from the target API before it's processed by Apigee. |

   7. In the **Add Step** modal, click the **Existing** tab, and then select the Flow Callout policy you created previously.

3. Save and deploy the updated proxy.

   ![Screen capture of Apigee target endpoint PreFlow step configuration](_images/hce1673558453257.png)

### Next steps

Configure fine-grained authorization policies in the PingAuthorize Policy Editor. You can find information on how to target specific API requests and extract other HTTP metadata to use in your policies in [Sideband API policy requests](../pingauthorize_server_administration_guide/paz_sideband_api_policy_reqs.html).

---

---
title: Configuring Konnect for PingAuthorize integration
description: For Kong Konnect to use PingAuthorize as an external authorization policy runtime service, you must download, install, and configure the ping-auth plugin.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_integrations:paz_configuring_konnect_for_integration
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_integrations/paz_configuring_konnect_for_integration.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2025
section_ids:
  add_pingauth_plugin_konnect: Adding the ping-auth plugin to your control plane
  adding-the-plugin-using-the-konnect-ui: Adding the plugin using the Konnect UI
  about-this-task: About this task
  steps: Steps
  adding-the-plugin-using-the-konnect-api: Adding the plugin using the Konnect API
  about-this-task-2: About this task
  steps-2: Steps
  result: Result:
  result-2: Result:
  upload_files_to_data_plane: Uploading files to data plane nodes
  about-this-task-3: About this task
  steps-3: Steps
  example: Example:
  configure_pingauth_plugin_konnect: Configuring the ping-auth plugin in Konnect
  configuring-the-plugin-using-the-gateway-manager-ui: Configuring the plugin using the Gateway Manager UI
  steps-4: Steps
  result-3: Result
  configuring-the-plugin-using-the-kong-api: Configuring the plugin using the Kong API
  steps-5: Steps
  result-4: Result:
---

# Configuring Konnect for PingAuthorize integration

For Kong Konnect to use PingAuthorize as an external authorization policy runtime service, you must download, install, and configure the `ping-auth` plugin.

To configure the `ping-auth` plugin in Kong Konnect, you must:

1. [Add the ping-auth plugin to your control plane](#add_pingauth_plugin_konnect)

2. [Upload files to your data plane nodes](#upload_files_to_data_plane)

3. [Configure the ping-auth plugin in Konnect](#configure_pingauth_plugin_konnect)

## Adding the ping-auth plugin to your control plane

Use the `ping-auth` plugin's `schema.lua` file to create the configurable entity required by Konnect. Konnect uses this file to create a plugin entry in the plugin catalog for your control plane. If the plugin schema should be available in multiple control planes, add the schema individually to each one.

You can manage schemas for custom plugins through the Konnect UI or the Konnect Control Planes Config API.

* Using the Konnect UI

* Using the Konnect API

### Adding the plugin using the Konnect UI

#### About this task

|   |                                                                                 |
| - | ------------------------------------------------------------------------------- |
|   | The UI is not available when using KIC in Konnect. Use the Konnect API instead. |

#### Steps

1. Download version 1.0.8-1 or later of the `kong-plugin-ping-auth` src from <https://luarocks.org/modules/pingidentity/kong-plugin-ping-auth>.

   |   |                                                                                 |
   | - | ------------------------------------------------------------------------------- |
   |   | Support for Kong Konnect is available in version 1.0.8 and later of the plugin. |

2. Extract the `src.rock` file and store it on your local computer.

   Verify that you have the following files in the extracted `/kong-plugin/ping-auth` folder:

   * `access.lua`

   * `handler.lua`

   * `Network_handle.lua`

   * `response.lua`

   * `schema.lua`

3. In Gateway Manager, open a control plane.

4. In the sidebar, open Plugins, then click New Plugin.

5. Click the Custom Plugins tab, then click Create on the Custom Plugin tile.

6. Click Select File, then select the `schema.lua` file for the `ping-auth` plugin that you extracted in step 1.

7. Make sure your file displays correctly in the preview, then click Save.

### Adding the plugin using the Konnect API

#### About this task

When using the `/plugin-schemas` API, authenticate your requests with either a personal access token or a system account token by including it in the authorization header:

```
--header 'Authorization: Bearer kpat_xgfT'
```

#### Steps

1. Upload the `schema.lua` file for your plugin using the `/plugin-schemas` endpoint:

   ```shell
   curl -i -X POST \
   https://{region}.api.konghq.com/konnect-api/api/runtime_groups/{controlPlaneId}/v2/plugin-schemas \
   --header 'Content-Type: application/json' \
   --data "{\"lua_schema\":  <your escaped Lua schema>}"
   ```

   ##### Result:

   You should get an `HTTP 201` response.

2. To check that your schema was uploaded, use the following request:

   ```shell
   curl -i -X GET \
   https://{region}.api.konghq.com/konnect-api/api/runtime_groups/{controlPlaneId}/v1/available-plugins
   ```

   ##### Result:

   This request returns an `HTTP 200` response with the schema for your plugin as a JSON object.

## Uploading files to data plane nodes

### About this task

After you upload the `ping-auth` plugin's schema to Konnect, upload the following files for the plugin to each Kong Konnect data plane node:

* `access.lua`

* `handler.lua`

* `Network_handle.lua`

* `response.lua`

* `schema.lua`

|   |                                                                                                |
| - | ---------------------------------------------------------------------------------------------- |
|   | If a data plane node doesn't have these files, the `ping-auth` plugin cannot run on that node. |

Follow the Kong Gateway plugin deployment instructions to set up the plugin on each node. Instructions can vary depending on the platform. If you're running Kong Gateway on Docker, the following instructions are provided as an example.

Install the `ping-auth` plugin inside the Kong Konnect Docker container for each node. Copy or mount the plugin's source code into the container.

### Steps

1. In your control plane, go to **Data Plane Nodes**, then click **New Data Plane Node**.

2. Select a **Platform**, for example **Linux (Docker)**, and **Generate a certificate**.

   ![Screen capture of the "Self-managed Hybrid Data Plane Node" screen](_images/mhy1702679880472.png)

3. Copy the generated Docker run command and add the following snippet to it.

   Substitute your own source and target paths.

   * The *\<source\_path>* is the location where you extracted the `ping-auth` plugin files. This is the parent folder that contains the `ping-auth` folder.

   * The *\<target\_path>* is where you keep custom Kong plugins. This is the path to the `ping-auth` plugin.

     ```
     -v "/<source_path>:/ping-auth:/<target_path>/ping-auth" \
     -e "KONG_PLUGINS=bundled,ping-auth" \
     -e "KONG_LUA_PACKAGE_PATH=/<target_path>/?.lua;;" \
     ```

4. To start a data plane node with the `ping-auth` plugin loaded, run the command.

   #### Example:

   For example, the command will look something like this, including the three snippet lines from the previous step. In this example, `plugins/kong` represents the *\<source\_path>* and `/usr/local/share/lua/5.1/kong/plugins` represents the *\<target\_path>*.

   ```shell
   docker run -d \
   -v "/plugins/kong/ping-auth:/usr/local/share/lua/5.1/kong/plugins/ping-auth" \
   -e "KONG_PLUGINS=bundled,ping-auth" \
   -e "KONG_LUA_PACKAGE_PATH=/usr/local/share/lua/5.1/kong/plugins/?.lua;;" \
   -e "KONG_ROLE=data_plane" \
   -e "KONG_DATABASE=off" \
   -e "KONG_VITALS=off" \
   -e "KONG_NGINX_WORKER_PROCESSES=1" \
   -e "KONG_CLUSTER_MTLS=pki" \
   -e "KONG_CLUSTER_CONTROL_PLANE=<example>.cp0.konghq.com:443" \
   -e "KONG_CLUSTER_SERVER_NAME=<example>.cp0.konghq.com" \
   -e "KONG_CLUSTER_TELEMETRY_ENDPOINT=<example>.tp0.konghq.com:443" \
   -e "KONG_CLUSTER_TELEMETRY_SERVER_NAME=<example>.tp0.konghq.com" \
   -e "KONG_CLUSTER_CERT=<cert>" \
   -e "KONG_CLUSTER_CERT_KEY=<key>" \
   -e "KONG_LUA_SSL_TRUSTED_CERTIFICATE=system" \
   -e "KONG_KONNECT_MODE=on" \
   -p 8000:8000 \
   -p 8443:8443 \
   kong/kong-gateway:<version>
   ```

5. To confirm the Docker deployment, run the following command:

   ```
   "docker logs [container id]"
   ```

   ![Screen capture of the "Create a Data Plane Node" confirming deployment of the configured Data Plane Node](_images/xew1702680032882.png)

## Configuring the ping-auth plugin in Konnect

After you've uploaded the `ping-auth` plugin's schema to Konnect, configure the plugin in Gateway Manager or use the Kong API.

|   |                                                                               |
| - | ----------------------------------------------------------------------------- |
|   | Test the operation of the `ping-auth` plugin before you use it in production. |

* Using the Gateway Manager UI

* Using the Kong API

### Configuring the plugin using the Gateway Manager UI

#### Steps

1. In Gateway Manager, open Plugins from the sidebar, then click New Plugin.

2. On the Custom Plugins tab, click the ping-auth plugin.

3. **Optional:** To enable the plugin for specific consumers, services, or routes, click Scoped, and then enter the Service, Route, and Consumer information.

4. In the Service Url field, enter the host name of your PingAuthorize server and the port of the HTTPS Connection Handler.

   To find this port number in the PingAuthorize administrative console, go to Configuration → System → Connection Handlers. For example, `https://pingauthorize:8443`.

5. In the Shared Secret field, enter the PingAuthorize sideband client's shared secret.

6. Verify that the Secret Header Name matches the secret header name configured for the Sideband API Servlet Extension in PingAuthorize.

   ![Screen capture of the Kong Konnect configure plugin screen with the "Secret Header Name" field highlighted](_images/ong1702680219153.png)

7. Configure the following additional fields:

   | Option                     | API Field Name               | Description                                                                                                                                                                             |
   | -------------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Connection KeepAlive Ms    | `connection_keepAlive_ms`    | The duration to keep the connection alive for reuse. The default is `60000`.                                                                                                            |
   | Connection Timeout Ms      | `connection_timeout_ms`      | The duration to wait before the connection times out. The default is `10000`.                                                                                                           |
   | Enable Debug Logging       | `enable_debug_logging`       | Controls if the requests and responses are logged at the debug level. The default is `false`. For log messages to show in `error.log`, you must set `log_level = debug` in `kong.conf`. |
   | Verify Service Certificate | `verify_service_certificate` | Controls whether the service certificate is verified. This is intended for testing purposes and the default is `true`.                                                                  |

8. Click Save.

#### Result

Kong Konnect is now configured to work with PingAuthorize.

### Configuring the plugin using the Kong API

#### Steps

1. Send the following in a `POST` request to `https://{region}.api.konghq.com/konnect-api/api/runtime_groups/{controlPlaneId}/plugins`:

   ```json
   {
   "name": "ping-auth",
   "enabled": true,
   "config": {
   "enable_debug_logging": true,
   "verify_service_certificate": false,
   "secret_header_name": "<shared secret header name>",
   "service_url": "https://<PingAuthorize Server hostname>:<HTTPS Connection Handler port>",
   "shared_secret": "<shared secret>"
     }
   }
   ```

   The following list describes the required fields for this API request:

   * `Service_url`: The full URL of the Ping policy provider. This should not contain `/sideband` in the path.

   * `Shared_secret`: The shared secret value to authenticate this plugin to the policy provider.

   * `Secret_header_name`: The header name in which the shared secret is provided. You can provide additional configuration in accordance with the Kong API specification.

2. Configure the optional fields:

   | Option                         | API Field Name               | Description                                                                                                                                                                             |
   | ------------------------------ | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Connection KeepAlive Ms**    | `connection_keepAlive_ms`    | The duration to keep the connection alive for reuse. The default is `60000`.                                                                                                            |
   | **Connection Timeout Ms**      | `connection_timeout_ms`      | The duration to wait before the connection times out. The default is `10000`.                                                                                                           |
   | **Enable Debug Logging**       | `enable_debug_logging`       | Controls if the requests and responses are logged at the debug level. The default is `false`. For log messages to show in `error.log`, you must set `log_level = debug` in `kong.conf`. |
   | **Verify Service Certificate** | `verify_service_certificate` | Controls whether the service certificate is verified. This is intended for testing purposes and the default is `true`.                                                                  |

   ##### Result:

   Kong Konnect is configured to work with PingAuthorize.

---

---
title: Deploying the custom MuleSoft policy for PingAuthorize
description: Deploy the custom MuleSoft policy to make it available to your integrated APIs.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_integrations:paz_deploy_mulesoft_policy_paz
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_integrations/paz_deploy_mulesoft_policy_paz.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 16, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  example: Example:
  result: Result
---

# Deploying the custom MuleSoft policy for PingAuthorize

Deploy the custom MuleSoft policy to make it available to your integrated APIs.

## Before you begin

You must:

* Have the correct MuleSoft version.

  The custom policy supports MuleSoft 4.3.0. If you are using any other version, contact Ping Identity support.

* Install and configure PingAuthorize software.

  See the [PingAuthorize installation information](../installing_and_uninstalling_pingauthorize/paz_install_pingauthorize.html) for your environment.

* Download the [MuleSoft integration kit for PingAuthorize](https://marketplace.pingone.com/item/mulesoft-integration-kit-for-pingauthorize), which contains the custom MuleSoft policy.

* Create a sideband adapter shared secret.

  Sideband adapters like the custom MuleSoft policy use a shared secret header to authorize against PingAuthorize. Learn more in [Creating a shared secret](../pingauthorize_server_administration_guide/paz_authn_sideband_api.html#create_sideband_shared_secret).

  |   |                                                                                             |
  | - | ------------------------------------------------------------------------------------------- |
  |   | Make sure you record the shared secret value. You need it to configure the MuleSoft policy. |

* Configure the sideband adapter request context.

  For more information, see [Request context configuration](../pingauthorize_server_administration_guide/paz_request_context_config.html). Complete the section titled Request context using the state field.

* Install Apache Maven.

## Steps

1. Extract the policy files to create a project folder.

2. Edit the `pom.xml` file to enter your organization's `groupID`.

   ### Example:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <project xmlns="http://maven.apache.org/POM/4.0.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchemainstance"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
       <modelVersion>4.0.0</modelVersion>

        <groupId>aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee</groupId>

       <artifactId>PingAuthorize</artifactId>
       <version>0.4.0</version>
       <name>PingAuthorize</name>
       <description>PingAuthorize sideband policy for Mule 4.X APIs deployed on Mule Cloudhub from Ping Identity</description>
   ```

3. From the command line in your project folder, run the following command to package the PingAuthorize policy and create a deployable `.jar` file. `> mvn clean install`

   |   |                                                                                                                                                                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You must have a MuleSoft Enterprise Repository license to compile the policy. For more information, see *Configure Maven to Access MuleSoft Enterprise Repository* in [Maven Reference](https://docs.mulesoft.com/mule-runtime/4.3/maven-reference#configure-maven-to-access-mulesoft-enterprise-repository). |

4. Upload the PingAuthorize policy to **Exchange**.

   For more information, see [Deploying a Policy Created Using the Maven Archetype](https://docs.mulesoft.com/api-manager/2.x/custom-policy-uploading-to-exchange).

## Result

The custom MuleSoft policy is now available to your APIs. For more information, see [Applying the custom MuleSoft policy for PingAuthorize](paz_apply_mulesoft_policy_paz.html).

---

---
title: Kong API gateway integration
description: Ping Identity provides the ping-auth Kong Gateway integration plugin, which enables PingAuthorize to be used for attribute-based access control and policy decisions.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_integrations:paz_kong_gateway_integration
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_integrations/paz_kong_gateway_integration.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 12, 2023
---

# Kong API gateway integration

Ping Identity provides the `ping-auth` Kong Gateway integration plugin, which enables PingAuthorize to be used for attribute-based access control and policy decisions.

Integration with Kong Gateway allows PingAuthorize to handle the complexities of attribute-based access control and dynamic authorization, making it easier for you to control access to your application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* resources. Instead of configuring policies multiple times, deploy the Kong Gateway integration once and manage your policy rules in PingAuthorize.

The following are important to consider when using the `ping-auth` Kong Gateway integration plugin for PingAuthorize:

* Mutual TLS (mTLS)

  This plugin supports client certificate authentication using mTLS. However, this feature requires using the `mtls-auth` plugin, only available in the enterprise edition of Kong, in conjunction with `ping-auth`. For more information, see the [Kong mTLS documentation](https://docs.konghq.com/hub/kong-inc/mtls-auth/). When configured, `mtls-auth` uses the mTLS process to retrieve the client certificate, which allows `ping-auth` to provide the certificate in the `client_certificate` field of the sideband requests.

* Transfer-encoding

  Because of an outstanding defect in Kong, `ping-auth` is unable to support the Transfer-Encoding header, regardless of the value.

* Logging limit

  Because of OpenResty's log level limit, log messages are limited to 2048 bytes by default, which is less than the size of many requests and responses. For more information, see the [OpenResty reference documentation](https://openresty-reference.readthedocs.io/en/latest/Lua_Nginx_API/#ngxlog).

---

---
title: Kong Konnect integration
description: Ping Identity's integration kit for Kong Konnect extends Kong's authorization capabilities through an external policy evaluation service.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_integrations:paz_kong_konnect_integration
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_integrations/paz_kong_konnect_integration.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2025
---

# Kong Konnect integration

Ping Identity's integration kit for Kong Konnect extends Kong's authorization capabilities through an external policy evaluation service.

Integration with Kong Konnect allows centralized management of API access control and application protection in PingAuthorize while delegating enforcement to Kong Konnect. For information about how traffic flows through Kong Konnect and PingAuthorize, refer to [PingAuthorize Integrations](paz_integrations_main.html).

Configure the integration kit in Kong Konnect to enable management of access control rules in PingAuthorize. The same kit supports both Kong Gateway and Kong Konnect.

|   |                                                                          |
| - | ------------------------------------------------------------------------ |
|   | Kong Konnect is supported in `ping-auth` plugin version 1.0.8 and later. |

To configure the integration kit:

1. [Prepare PingAuthorize](paz_preparing_paz_konnect_integration.html) for Kong Konnect integration.

2. [Add the ping-auth plugin](paz_configuring_konnect_for_integration.html#add_pingauth_plugin_konnect) to your Kong Konnect control plane.

3. [Upload ping-auth plugin files](paz_configuring_konnect_for_integration.html#upload_files_to_data_plane) to each data plane node.

4. [Configure the ping-auth plugin](paz_configuring_konnect_for_integration.html#configure_pingauth_plugin_konnect) in Kong Konnect.

Learn more in [Adding custom plugins in Konnect](https://docs.konghq.com/konnect/gateway-manager/plugins/add-custom-plugin/) in the Kong Konnect documentation.

---

---
title: MuleSoft API gateway integration
description: Learn how to enable fine-grained access control through the MuleSoft API gateway by deploying the PingAuthorize API adapter and connecting to the sideband API.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_integrations:paz_mulesoft_integration
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_integrations/paz_mulesoft_integration.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 16, 2025
---

# MuleSoft API gateway integration

Learn how to enable fine-grained access control through the MuleSoft API gateway by deploying the PingAuthorize API adapter and connecting to the sideband API.

Ping Identity provides a custom MuleSoft policy to enable this configuration.

You can find information on integrating PingAuthorize with the MuleSoft gateway in the following:

1. [Deploying the custom MuleSoft policy for PingAuthorize](paz_deploy_mulesoft_policy_paz.html)

2. [Applying the custom MuleSoft policy for PingAuthorize](paz_apply_mulesoft_policy_paz.html)

---

---
title: PingAuthorize Integrations
description: API gateway integrations enable you to use PingAuthorize for attribute-based access control and policy decisions with your API gateway.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_integrations:paz_integrations_main
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_integrations/paz_integrations_main.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 23, 2026
---

# PingAuthorize Integrations

API gateway integrations enable you to use PingAuthorize for attribute-based access control and policy decisions with your API gateway.

PingAuthorize supports authorization integrations with third-party API gateways through integration kits. PingAuthorize also integrates natively with PingGateway.

The following diagram outlines how API requests flow through your API gateway and PingAuthorize:

![Diagram of the API gateway request and response flow between the API client, the API gateway, the PingAuthorize policy engine, policy information points, and the API target](_images/brz1673969858956.png)

1. The client sends a request to the API gateway.

2. The API gateway-specific integration kit processes the client's request and sends it to the PingAuthorize Server for policy processing.

3. The PingAuthorize Server determines whether to permit or deny the API request based on policies defined in the PingAuthorize Policy Editor.

4. The API gateway analyzes the response from the PingAuthorize Server to determine whether to forward the request to the upstream API and, if so, whether to modify the request.

5. The API gateway passes the original or modified request to the API target.

6. The API resource server sends a response to the gateway with the requested resources.

7. The integration kit processes the resource server's response and forwards it to the PingAuthorize Server for policy processing.

8. The PingAuthorize Server determines whether to forward the API response to the client based on policies defined in the PingAuthorize Policy Editor.

9. The PingAuthorize Server sends a final response to the API gateway.

10. The API gateway processes the response and forwards the requested API resource to the client.

PingAuthorize supports the following API gateway integrations:

* [Apigee API gateway integration](paz_apigee_integration.html)

* [Kong API gateway integration](paz_kong_gateway_integration.html)

* [Kong Konnect integration](paz_kong_konnect_integration.html)

* [MuleSoft API gateway integration](paz_mulesoft_integration.html)

* [PingGateway](https://docs.pingidentity.com/pinggateway/latest/reference/PingAuthorizeFilter.html)

---

---
title: Preparing PingAuthorize for Kong Gateway integration
description: Prepare PingAuthorize to receive authorization requests from Kong Gateway.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_integrations:paz_kong_prepare_paz
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_integrations/paz_kong_prepare_paz.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 2, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Preparing PingAuthorize for Kong Gateway integration

For Kong Gateway to use PingAuthorize as an external authorization policy runtime service, you must prepare PingAuthorize to receive authorization requests from Kong Gateway.

## Before you begin

* Install and start Kong Gateway. Learn more in the [Kong Gateway](https://docs.konghq.com/gateway/) documentation.

* Install and start PingAuthorize. Learn more in [Installing PingAuthorize](../installing_and_uninstalling_pingauthorize/paz_install_pingauthorize.html).

## Steps

1. In the PingAuthorize admin console, go to **Configuration > Web Services and Applications > HTTP Servlet Extensions**.

2. Click **Sideband API**.

3. In the **Request Context Method** list, select **State**.

   ![Screen capture of the Sideband API HTTP Servlet Extension window with settings configured as previously specified for Kong Gateway](_images/paz_sideband_api_servlet_config.png)

4. In the **Shared Secret Header Name** field, enter `CLIENT-TOKEN`.

5. To create a new shared secret, in the **Shared Secret Header Name** list, select **New Sideband API Shared Secret**.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The shared secret authenticates the `ping-auth` plugin to PingAuthorize. Version 1.2.0 of the plugin supports referenceable secrets. For security reasons, store the shared secret in a vault supported by Kong. Learn more in [Secrets Management](https://docs.konghq.com/gateway/latest/kong-enterprise/secrets-management/) and [Environment Variables Vault](https://docs.konghq.com/gateway/latest/kong-enterprise/secrets-management/backends/env/) in the Kong documentation. |

6. In the **New Sideband API Shared Secret** modal, create a suitably long shared secret value, and then click **Save**.

7. Click **Save**.

---

---
title: Preparing PingAuthorize for Konnect integration
description: Prepare PingAuthorize to receive authorization requests from Kong Konnect.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_integrations:paz_preparing_paz_konnect_integration
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_integrations/paz_preparing_paz_konnect_integration.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 2, 2025
section_ids:
  steps: Steps
---

# Preparing PingAuthorize for Konnect integration

For Kong Konnect to use PingAuthorize as an external authorization policy runtime service, you must prepare PingAuthorize to receive authorization requests from Kong Konnect.

## Steps

1. In the PingAuthorize admin console, go to **Configuration > Web Services and Applications > HTTP Servlet Extensions**.

2. Click **Sideband API**.

3. In the **Request Context Method** list, select **State**.

   ![Screen capture of the "Sideband API" screen in the administrative console with the Request Context Method set to state, the Shared Secret Header Name set to CLIENT-TOKEN, and Kong Konnect added as the selected Shared Secret.](_images/paz_sideband_api_servlet_config.png)

4. In the **Shared Secret Header Name** field, enter `CLIENT-TOKEN`.

5. To create a new shared secret, in the **Shared Secret Header Name** list, select **New Sideband API Shared Secret**.

6. In the **New Sideband API Shared Secret** modal, create a suitably long shared secret value, and then click **Save**.

7. Click **Save**.

---

---
title: Setting up Kong Gateway
description: Download, install, and configure the ping-auth plugin to set up Kong Gateway with PingAuthorize.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_integrations:paz_kong_gateway_setup
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_integrations/paz_kong_gateway_setup.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 26, 2025
section_ids:
  steps: Steps
  result: Result
---

# Setting up Kong Gateway

Download, install, and configure the `ping-auth` plugin to set up Kong Gateway with PingAuthorize.

## Steps

1. Install the plugin by running the `luarocks install kong-plugin-ping-auth` command.

   Learn more in the [Kong Gateway plugin installation guide](https://docs.konghq.com/gateway/latest/plugin-development/distribution/).

2. After installation, load the plugin into Kong by editing the `plugins = bundled,ping-auth` property in the `kong.conf` file.

3. Restart Kong Gateway.

4. To confirm the plugin loads successfully, look for the debug-level `Loading plugin: ping-auth` message in Kong's `error.log` file.

5. Use the Kong Gateway UI or API to complete the configuration.

* Kong Gateway UI

* Kong Gateway API

1. In Kong Manager, select the **default** workspace, and then click **Plugins**.

   ![Screen capture of the Plugins window in the default workspace of Kong Manager with the ping-auth plugin loaded](_images/xow1658432018704.png)

2. Next to the **ping-auth** plugin, click **Edit**, and then click the toggle to enable the plugin.

   ![Screen capture of the Update ping-auth plugin window enabling the ping-auth plugin in Kong Manager](_images/she1658433603588.png)

3. (Optional) To enable the plugin for specific consumers, services, or routes, click **Scoped**, and then enter **Service**, **Route**, and **Consumer** information as needed.

4. Connect Kong Gateway to PingAuthorize.

   1. Make sure the **Config.Secret Header Name** value in Kong Manager matches the secret header name configured for the [Sideband API Servlet Extension](../pingauthorize_server_administration_guide/paz_sideband_api_config.html) in PingAuthorize.

      ![Screen capture of the Config.Shared Secret and Config.Service Url configuration for the ping-auth plugin in Kong Manger](_images/lwg1658437330617.png)

   2. In the **Config.Service URL** field in Kong Manager, enter the hostname of your PingAuthorize Server instance and the port of the HTTPS Connection Handler.

      For example, `https://pingauthorize:8443`.

      |   |                                                                                                                                                       |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | To find the HTTPS Connection Handler port number in the PingAuthorize administrative console, go to **Configuration > System > Connection Handlers**. |

   3. In the **Config.Shared Secret** field, enter the sideband client's shared secret you created in [Preparing PingAuthorize for Kong Gateway integration](paz_kong_prepare_paz.html).

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The shared secret authenticates the `ping-auth` plugin to PingAuthorize. Version 1.2.0 of the plugin supports referenceable secrets. For security reasons, store the shared secret in a vault supported by Kong. Learn more in [Secrets Management](https://docs.konghq.com/gateway/latest/kong-enterprise/secrets-management/) and [Environment Variables Vault](https://docs.konghq.com/gateway/latest/kong-enterprise/secrets-management/backends/env/) in the Kong documentation. |

5. (Optional) Configure the rest of the optional fields in Kong Manager or the API.

   | Option                                | API Field Name               | Description                                                                                                                                                                         |
   | ------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Config.Connection KeepAlive Ms**    | `connection_keepAlive_ms`    | The duration to keep the connection alive for reuse. The default is `60000`.                                                                                                        |
   | **Config.Connection Timeout Ms**      | `connection_timeout_ms`      | The duration to wait before the connection times out. The default is `10000`.                                                                                                       |
   | **Config.Enable Debug Logging**       | `enable_debug_logging`       | Controls if requests and responses are logged at the debug level. The default is `false`. For log messages to show in `error.log`, you must set `log_level = debug` in `kong.conf`. |
   | **Config.Verify Service Certificate** | `verify_service_certificate` | Controls whether the service certificate is verified. This is intended for testing purposes and the default is `true`.                                                              |

6. Click **Update**, and then click **Update Plugin**.

1) Include the following JSON object in a `POST` request to https\://\<KONG\_URL>/plugins:

   ```json
   {
     "name": "ping-auth",
     "enabled": true,
     "config": {
       "service_url": "https://<PingAuthorize Server hostname>:<HTTPS Connection Handler port>/",
       "shared_secret": "<shared secret>",
       "secret_header_name": "<shared secret header name>"
     }
   }
   ```

   * `service_url`: The hostname of your PingAuthorize Server instance and the port of the HTTPS Connection Handler. This URL should not contain `/sideband` in the path.

     For example, `https://pingauthorize:8443`.

   * `shared_secret`: The shared secret value you created in the PingAuthorize administrative console.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The shared secret authenticates the `ping-auth` plugin to PingAuthorize. Version 1.2.0 of the plugin supports referenceable secrets. For security reasons, store the shared secret in a vault supported by Kong. Learn more in [Secrets Management](https://docs.konghq.com/gateway/latest/kong-enterprise/secrets-management/) and [Environment Variables Vault](https://docs.konghq.com/gateway/latest/kong-enterprise/secrets-management/backends/env/) in the Kong documentation. |

   * `secret_header_name`: The name of the header in which the shared secret is provided.

     Learn more in the [Kong Gateway Admin API](https://docs.konghq.com/gateway/2.8.x/admin-api/#add-plugin) documentation.

2) (Optional) Configure additional options.

   | Option                                | API Field Name               | Description                                                                                                                                                                         |
   | ------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Config.Connection KeepAlive Ms**    | `connection_keepAlive_ms`    | The duration to keep the connection alive for reuse. The default is `60000`.                                                                                                        |
   | **Config.Connection Timeout Ms**      | `connection_timeout_ms`      | The duration to wait before the connection times out. The default is `10000`.                                                                                                       |
   | **Config.Enable Debug Logging**       | `enable_debug_logging`       | Controls if requests and responses are logged at the debug level. The default is `false`. For log messages to show in `error.log`, you must set `log_level = debug` in `kong.conf`. |
   | **Config.Verify Service Certificate** | `verify_service_certificate` | Controls whether the service certificate is verified. This is intended for testing purposes and the default is `true`.                                                              |

## Result

Kong Gateway is now configured to work with PingAuthorize.

---

---
title: Setting up PingAuthorize for Apigee integration
description: Set up PingAuthorize to receive authorization requests from Apigee.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_integrations:paz_apigee_integration_paz_setup
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_integrations/paz_apigee_integration_paz_setup.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 2, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Setting up PingAuthorize for Apigee integration

To allow Apigee to use PingAuthorize as an external runtime authorization service, set up PingAuthorize to receive authorization requests from Apigee.

## Before you begin

[Install PingAuthorize](../installing_and_uninstalling_pingauthorize/paz_install_pingauthorize.html).

## Steps

1. In the PingAuthorize admin console, go to **Configuration > Web Services and Applications > HTTP Servlet Extensions**.

2. Click **Sideband API**.

3. In the **Request Context Method** list, select **State**.

   ![Screen capture of the Edit Sideband API HTTP Servlet Extension page in the PingAuthorize administrative console.](_images/paz_sideband_api_servlet_config.png)

4. In the **Shared Secret Header Name** field, enter `CLIENT-TOKEN`.

5. To create a new shared secret, in the **Shared Secrets** list, select **New Sideband API Shared Secret**.

6. In the **New Sideband API Shared Secret** modal, enter a shared secret name and value, and then click **Save**.

7. Click **Save**.

---

---
title: Troubleshooting the Apigee integration
description: Troubleshoot the most common issues with the Apigee gateway integration with PingAuthorize.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_integrations:paz_apigee_integration_troubleshooting
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_integrations/paz_apigee_integration_troubleshooting.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2025
section_ids:
  troubleshooting-api-client-http-5xx-errors: Troubleshooting API client HTTP 5xx errors
  steps: Steps
  troubleshooting-api-client-http-4xx-errors: Troubleshooting API client HTTP 4xx errors
  setting-up-error-response-handling-in-the-target-server: Setting up error response handling in the target server
  steps-2: Steps
  apigee_logging: Enable logging in Apigee
---

# Troubleshooting the Apigee integration

Troubleshoot the most common issues with the Apigee gateway integration with PingAuthorize.

## Troubleshooting API client HTTP 5xx errors

Apigee might return `HTTP 502` when there is misconfiguration or miscommunication between the PingAuth shared flow for Apigee and PingAuthorize Server.

To address 5xx errors, make adjustments to the **Load KVM Config** policy assigned to **PingAuth** in Apigee X or the key value map that you created for the PingAuth Shared Flow in Apigee Edge or Apigee Private Cloud.

The PingAuth Shared Flow for Apigee logs warning messages to the Apigee error log when it encounters problems communicating with PingAuthorize. Learn more in [Enable logging in Apigee](#apigee_logging).

### Steps

* Check the PingAuth Shared Flow `service_host_port` value.

  If the Apigee `service_host_port` value does not match your PingAuthorize server environment, the Apigee error log message might indicate that the plugin received an invalid response from the server.

  1. Confirm that the value entered for `service_host_port` matches the host name of your PingAuthorize server and the port of the HTTPS connection handler.

     You can find this port number on the **Configuration** page of the PingAuthorize administration console by going to **System → Connection Handlers**.

  2. If necessary, update the `service_host_port` value to match your PingAuthorize server.

* Check the PingAuth Shared Flow shared secret.

  If the shared secret doesn't match the API gateway credential in PingAuthorize, the Apigee error log message might indicate that the plugin received an `HTTP 401` error from PingAuthorize, which gets translated to a 5xx error and then sent to the API client.

  1. Confirm that the value of the **shared\_secret** key that you created in Apigee matches the shared secret value that you created for PingAuthorize.

  2. If necessary, on the **Configuration** page of the PingAuthorize administration console, go to **Web Services and Applications > HTTP Servlet Extensions > Sideband API** and update the value of the shared secret.

  3. Copy the new value of the shared secret and update the value of the Apigee **shared\_secret** key.

## Troubleshooting API client HTTP 4xx errors

The Apigee API gateway might return a 4xx error to the API client if the API client's request can't be authenticated by the PingAuthorize sideband API endpoint.

To troubleshoot 4xx errors caused by authentication issues against the PingAuthorize sideband API, refer to [Sideband API authentication](../pingauthorize_server_administration_guide/paz_authn_sideband_api.html).

## Setting up error response handling in the target server

You should have an Apigee policy that handles errors returned by the target server.

If you don't configure error handling using a policy, the API proxy goes into an error state in the `<TargetEndpoint>` response, and the normal API proxy flow won't continue to the `<ProxyEndpoint>`.

### Steps

1. Go to **API Proxies > httpbin\_bad\_response > Develop** and create a new **ReturnGenericError** policy of type **AssignMessage**. Configure the policy as desired.

   ![Screen capture of the ReturnGenericError policy creation within Apigee](_images/rzw1673906971414.png)

2. Select the **PreFlow** option in the **Target Endpoints** for your API proxy. Add the error policy you just created as a `<Step>` in the `<DefaultFaultRule>`.

   |   |                                                                  |
   | - | ---------------------------------------------------------------- |
   |   | There are multiple methods for adding the error handling policy. |

   ![Screen capture of adding the ReturnGenericError policy as a step within the DefaultFaultRule for the API proxy in Apigee](_images/zys1673907502466.png)

## Enable logging in Apigee

To view error log messages, configure Apigee error logging. Learn more in the [View message data with Trace](https://docs.apigee.com/api-platform/tutorials/view-with-trace) in the Apigee documentation.

Apigee also provides debug logging for further troubleshooting. Learn more in [Enabling debug logging](https://docs.apigee.com/private-cloud/v4.18.05/enabling-debug-logging) in the Apigee documentation.

---

---
title: Troubleshooting the Kong Gateway integration
description: Consult the following sections to troubleshoot issues with the Kong Gateway integration with PingAuthorize:
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_integrations:paz_kong_gateway_troubleshoot
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_integrations/paz_kong_gateway_troubleshoot.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2025
section_ids:
  kong_5xx_errors: Troubleshooting API client HTTP 5xx errors
  steps: Steps
  example: Example:
  example-2: Example:
  kong_4xx_errors: API client HTTP 4xx errors
  enable_error_logging_kong: Enabling error logging in Kong Gateway
  steps-2: Steps
  enable_debug_logging_kong_plugin: Enabling debug logging for the Kong Gateway plugin
  steps-3: Steps
---

# Troubleshooting the Kong Gateway integration

Consult the following sections to troubleshoot issues with the Kong Gateway integration with PingAuthorize:

* [Troubleshooting API client HTTP 5xx errors](#kong_5xx_errors)

* [API client HTTP 4xx errors](#kong_4xx_errors)

* [Enabling error logging in Kong Gateway](#enable_error_logging_kong)

* [Enabling debug logging for the Kong Gateway plugin](#enable_debug_logging_kong_plugin)

## Troubleshooting API client HTTP 5xx errors

Kong Gateway might return `HTTP 502` when there is misconfiguration or miscommunication between the Ping Identity plugin for Kong Gateway and PingAuthorize Server.

|   |                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The plugin for Kong Gateway logs warning messages to the Kong Gateway error log when it encounters problems communicating with PingAuthorize.Learn more in [Enabling error logging in Kong Gateway](#enable_error_logging_kong). |

### Steps

1. Check the `ping-auth` shared secret value in Kong Gateway to confirm it matches your PingAuthorize environment.

   #### Example:

   If the `ping-auth` **Config.Shared Secret** value doesn't match the PingAuthorize sideband client's shared secret value, the Kong error log message might indicate that the plugin received an `HTTP 401` error from PingAuthorize, which gets translated to a `5xx` error sent to the API client. For example:

   ```
   2022/03/28 16:19:49 [warn] 78**0: *85187 [lua] network_handler.lua:145: is_failed_request(): [ping-auth] Sideband request denied with status code 401: The Gateway Token is invalid
   ```

   1. If there is a shared secret mismatch, go to **Configuration > Web Services and Applications > Sideband API Shared Secrets** in the PingAuthorize administrative console.

   2. Update the shared secret value for PingAuthorize.

   3. Copy the value to the **Config.Shared Secret** field in the Kong Gateway `ping-auth` plugin configuration.

2. Check the `ping-auth` **Config.Service URL** value in Kong Gateway to confirm that it matches your PingAuthorize environment.

   #### Example:

   If the **Config.Service URL** value doesn't contain the hostname and HTTPS Connection Handler port configured for your PingAuthorize server, the Kong error log message might indicate that the plugin received an invalid response from the server. For example:

   ```
   2022/03/28 16:19:49 [error] 78#0: *90929 [lua] access.lua:114: handle_response(): [ping-auth] Unable to parse JSON body returned from policy provider. Error: Expected value but found T_END at character 1
   ```

   1. If necessary, confirm that the values entered in the **Config.Service Url** field of the `ping-auth` plugin in Kong Gateway correspond to the hostname and HTTPS Connection Handler port of your PingAuthorize server.

      You can find this port number in the PingAuthorize administrative console by going to **Configuration → System → Connection Handlers**.

   2. Update any mismatched values in **Config.Service Url**.

## API client HTTP 4xx errors

The API gateway could return `4xx` errors to API clients in these situations:

* PingAuthorize cannot match an API client's request to any of the base paths configured for a sideband API endpoint.

* The API client's request cannot be authenticated for a sideband API endpoint.

Learn more in [Sideband API authentication](../pingauthorize_server_administration_guide/paz_authn_sideband_api.html).

## Enabling error logging in Kong Gateway

### Steps

1. To view error log messages, configure Kong Gateway error logging.

   Learn more about logging levels in [Logging Reference](https://docs.konghq.com/gateway/2.8.x/configure/logging/) in the Kong Gateway documentation.

   For example, in a Docker environment, you can set the environment variable `KONG_PROXY_ERROR_LOG` to `/dev/stderr` to send the error log to the container console.

2. View the Kong Gateway error log.

   When using Docker Compose, you can use the `docker compose logs <kong-service> --follow` command.

## Enabling debug logging for the Kong Gateway plugin

Ping Identity Support might ask you to enable debug logging for the Kong Gateway integration kit. Changing these settings logs the full authorization request and response between the `ping-auth` plugin in Kong Gateway and PingAuthorize.

|   |                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Debug logs can contain sensitive and personally identifiable information (PII). Enable debug logging only when troubleshooting and disable it afterward. |

### Steps

1. [Enable error logging](#enable_error_logging_kong) in Kong Gateway.

2. To view debug messages, configure Kong error log verbosity.

   Learn more in [Logging Reference](https://docs.konghq.com/gateway/2.8.x/configure/logging/) in the Kong Gateway documentation.

   For example, in a Docker environment, you can set the environment variable `KONG_LOG_LEVEL` to `debug` to increase the error log verbosity.

3. To enable debug logging, edit settings for the `ping-auth` plugin and select the **Config.Enable Debug Logging** checkbox.

4. View the Kong Gateway error log.

   When using Docker Compose, you can use the `docker compose logs <kong-service> --follow` command.

5. Look for log messages containing `ping-auth`.

   A typical log message looks like: `[ping-auth] Sending sideband request to policy provider`.