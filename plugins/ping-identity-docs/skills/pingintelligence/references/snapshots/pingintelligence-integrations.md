---
title: Add API definitions to ASE
description: Add the API definition files to help API Security Enforcer (ASE) extract metadata from API traffic, set decoys to trap intruding attacks, perform health checks on backend servers, and so on.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_apigee_add_api_definitions
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_apigee_add_api_definitions.html
revdate: May 6, 2024
---

# Add API definitions to ASE

Add the API definition files to help API Security Enforcer (ASE) extract metadata from API traffic, set decoys to trap intruding attacks, perform health checks on backend servers, and so on.

The API definitions also help the artificial intelligence (AI) engine to build AI models to detect any Indicators of Attacks (IoAs) on APIs. After the policy has been deployed to Apigee using the PingIntelligence automated policy tool, add APIs to ASE.

For more information on defining APIs, see:

* [API naming guidelines](../pingintelligence_reference_guide/pingintelligence_api_naming_guidelines.html)

* [Defining an API using API JSON configuration file in sideband mode](../pingintelligence_reference_guide/pingintelligence_define_api_json_file_sideband.html)

For more information on ASE sideband deployment, see [Sideband ASE](../pingintelligence_reference_guide/pingintelligence_sideband_ase.html).

---

---
title: Adding a PingIntelligence policy
description: To add a PingIntelligence policy to the Akana API Gateway:
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_akana_add_policy
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_akana_add_policy.html
revdate: April 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding a PingIntelligence policy

## About this task

To add a PingIntelligence policy to the Akana API Gateway:

## Steps

1. Sign on to **Akana Policy Manager**, navigate to the **Tenant**, and click **Operational Policies** under **Policies**.

2. Select **Add Policy**.

3. For **Type**, select **Private Operational Script Policy** from the drop-down list, and click **Next**.

![A screenshot of the Select Policy Creation Option page in Akana Policy Manager.](../_images/mfl1579954034176.png)

1. Enter **Policy Name** and **Description**, click **Finish**, and then click **Close**.

![A screenshot of the Specify Policy Details page in Akana Policy Manager.](../_images/rze1579954203473.png)

1. Navigate to **Workbench**.

2. In the **Private Operational Script Policy** section, select the policy name and click **Modify**.

![A screenshot of the Workbench tab in Akana Policy Manager.](../_images/vxr1579954340568.png)

1. Click on **Imports**. Select the script added in [Adding an input script](pingintelligence_akana_input_script.html) and import it by clicking **<<**.

2. Select **JavaScript** for **Language** from the list.

3. Copy the contents of the `pi_policy.js` script and paste them into **Expression** under **Source**.

![A screenshot of the Modify Script Policy page in Akana Policy Manager.](../_images/vio1579954532678.png)

1. Click **Finish** and then click **Close**.

2. In the **WorkFlow Actions**, click **Activate Policy** to activate the PingIntelligence policy.

---

---
title: Adding an input script
description: To add an input script to the Akana API gateway:
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_akana_input_script
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_akana_input_script.html
revdate: April 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
---

# Adding an input script

## About this task

To add an input script to the Akana API gateway:

## Steps

1. Sign on to **Akana Policy Manager**, navigate to **Tenant**, and click **Scripts**.

2. Click **Add Script**.

3. Enter **Script Name** and **Script Description**, and click**Next**.

   ![A screenshot of the Specify Script Details page in Akana Policy Manager.](../_images/rjc1579953577408.png)

4. Select **JavaScript** for **Language** from the list.

5. Copy the contents of the `config.js` script provided by PingIntelligence and paste them into the **Source**.

   ![A screenshot of the Script Editor page in Akana Policy Manager.](../_images/wmo1579953724862.png)

6. Paste the values of **Service\_QName**, **Interface\_Name**, and **Operation\_Name** that were copied in [Capturing ASE details](pingintelligence_akana_capture.html).

   This needs to be done for both primary and secondary ASE nodes. The following table lists the variables in `config.js` that need to be populated.

   | Variable                              | Description                                                    |
   | ------------------------------------- | -------------------------------------------------------------- |
   | *ase\_token*                          | Variable for the ASE sideband authentication token.            |
   | *primary\_ase\_service*               | Service QName for primary ASE.                                 |
   | *primary\_ase\_interface*             | Interface Name for primary ASE.                                |
   | *primary\_ase\_request\_operation*    | Operation Name for posting Request Metadata in primary ASE.    |
   | *primary\_ase\_response\_operation*   | Operation Name for posting Response Metadata in primary ASE.   |
   | *secondry\_ase\_service*              | Service QName for secondary ASE.                               |
   | *secondary\_ase\_interface*           | Interface Name for secondary ASE.                              |
   | *secondary\_ase\_request\_operation*  | Operation Name for posting Request Metadata in secondary ASE.  |
   | *secondary\_ase\_response\_operation* | Operation Name for posting Response Metadata in secondary ASE. |

   ### Example:

   Below is a sample substitution snippet:

   ```
   var ase_token = "ASE-Token-123";
   /Primary ASE Configuration/
   var primary_ase_service = "{pi-as-ase-primary_0.0.0}svc_314492f1-ecdc-4184-93a0-57ee2258154b.smshargi.sandbox";
   var primary_ase_interface = "{pi-as-ase-primary_0.0.0}pi-as-ase-primary_PortType_0";
   var primary_ase_request_operation = "postRequestMetadata";
   var primary_ase_response_operation = "postResponseMetadata";
   /**/
   /Secondary ASE Configuration/
   var secondry_ase_service = "{pi-as-ase-primary_0.0.0}svc_314492f1-ecdc-4184-93a0-57ee2258154b.smshargi.sandbox";
   var secondary_ase_interface = "{pi-as-ase-primary_0.0.0}pi-as-ase-primary_PortType_0";
   var secondary_ase_request_operation = "postRequestMetadata";
   var secondary_ase_response_operation = "postResponseMetadata";
   ```

7. Click **Finish**, and then click **Close**.

---

---
title: Adding PingIntelligence ASE APIs
description: Add a primary and secondary ASE node to the Akana API Gateway.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_akana_add_api
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_akana_add_api.html
revdate: April 3, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Adding PingIntelligence ASE APIs

Add a primary and secondary ASE node to the Akana API Gateway.

## Before you begin

You must:

* Install and configure the PingIntelligence software. For more information, refer to [Automated deployment](../installing_pingintelligence_for_apis/pingintelligence_automated_deployment.html) or [Manual deployment](../installing_pingintelligence_for_apis/pingintelligence_manual_deployment.html).

* Verify that API Security Enforcer (ASE) is in sideband mode by running the following ASE command:

  ```
  /opt/pingidentity/ase/bin/cli.sh status
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
  ```

  * If ASE is not in sideband mode, then stop ASE and change the mode by editing the `/opt/pingidentity/ase/config/ase.conf` file. Set mode as sideband and start ASE.

* For a secure communication between the Akana Gateway and ASE, enable sideband authentication by entering the following ASE command:

  ```
  # ./bin/cli.sh enable_sideband_authentication -u admin –p
  ```

* Ensure SSL is configured in ASE for client side connection using CA-signed certificate.Please refer to [Configuring SSL for external APIs](../pingintelligence_reference_guide/pingintelligence_confguring_ssl_external_apis.html) for more details.

* Generate sideband authentication token by entering the following command in the ASE command-line interface (CLI):

  ```
  # ./bin/cli.sh -u admin -p admin create_sideband_token
  ```

* Enable the connection keepalive between gateway and ASE by navigating to `/opt/pingidentity/ase/config/` and setting the value of `enable_sideband_keepalive` to `true` in the `ase.conf` file.

  * If ASE is running, stop it before making the change and start ASE after setting the value. For more information on ASE configuration, see [Sideband ASE configuration using the `ase.conf` file](../pingintelligence_reference_guide/pingintelligence_sideband_ase_configuration.html).

## About this task

|   |                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The primary and secondary ASE APIs should not be exposed to external API clients. For more details on securing ASE APIs, see [Securing PingIntelligence ASE APIs](pingintelligence_akana_secure_api.html). |

To add ASE APIs to the Akana API Gateway:

## Steps

1. Sign on to the **Akana portal** and click **Add API** from the **APIs** drop-down list.

2. Select **I want to design my API from scratch (REST) only**.

3. Enter the following details for ASE:

   1. Enter the name of the API in the **Name** field.

   2. Enter the **Endpoint**: *\<http/https>*://*\<ASE-Hostname or IP>*/ase.

   3. Click the toggle to enable **Advanced Options**.

   4. Enter the API version in the **Version ID** field.

   5. For **Pattern**, select **Proxy**.

   6. Select **Implementation**.

   7. Select **Deployment Zones**.

4. Click **Save** after entering the details.

   ![A screenshot of the Add API page in the Akana portal.](../_images/tvl1581658826645.png)

5. Add two resources under **Resources**: one to post request metadata to ASE and another to post response metadata to ASE.To add a resource to the ASE API, open API Designer:

   1. Navigate to the **Overview** page of the API.

   2. Choose **Details** from the left menu pane. The summary of the API is displayed in the details.

   3. In the **Design** section, click **Edit** to enter API Designer.

      ![A screenshot of API Designer.](../_images/dwb1579949414329.png)

6. Add the Request resource to the API:

   ![A screenshot of the Resources page in API Designer.](../_images/cum1579949559737.png)

   1. Click **Add Resource** to open the **Edit Resource** window.

   2. Enter `/request` in the **Path** to post request metadata to ASE.

   3. For **Verb**, choose `POST`.

   4. Enter **Operation ID**. If the user does not provide the value, a random value is generated for Operation ID.

   5. Click **Finish** after updating the other optional details like **Description**, **Summary**, and **Tags**.

   6. Click **Save**.

      ![A screenshot of the Edit Resource window.](../_images/bni1579949811722.png)

      |   |                                                                                                                                 |
      | - | ------------------------------------------------------------------------------------------------------------------------------- |
      |   | A default resource is created when an API is added to Akana API Gateway. This resource can be edited to add the first resource. |

7. To add the Response resource to the API:

   1. Click **Add Resource** to open the **Edit Resource** window.

   2. Enter `/response` in the **Path** field to post request metadata to ASE.

   3. For **Verb**, choose `POST`.

   4. Enter **Operation ID**. If the user does not provide the value, a random value is generated for Operation ID.

   5. Click **Finish** after updating the other optional details like **Description**, **Summary**, and **Tags**.

      ![A screenshot of the Edit Resource window.](../_images/pwg1579949959144.png)

8. To add the secondary (backup) ASE node, repeat steps 1- 5.

---

---
title: Adding the PingIntelligence policy
description: The imported PingIntelligence policy must be tied to a virtual server. Add the PingIntelligence policy to the existing or recently created virtual server
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_f5_big_ip_add_policy
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_f5_big_ip_add_policy.html
revdate: April 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding the PingIntelligence policy

The imported PingIntelligence policy must be tied to a virtual server. Add the PingIntelligence policy to the existing or recently created virtual server

## About this task

To add the PingIntelligence policy to the virtual server:

## Steps

1. Navigate to **Local Traffic → Virtual Servers → Virtual Server List**.

2. Select the virtual server to which you want to add the PingIntelligence policy.

3. Click the **Resources** tab.

4. In the **iRules** section, click the **Manage** button.

5. Choose the iRule under the **pi\_plugin** that you want to attach to the virtual server.

   ![A screenshot of the Frontend, Virtual Server List page with pi\_rule highlighted by a yellow box.](../_images/gpx1582878749382.png)

6. Move the **pi\_irule** to the **Enabled** window and click **Finished**.

   ![A screen capture of the Virtual Server List, Frontend page with the Enabled rules highlighted with a yellow box.](../_images/kkw1582878864944.png)

---

---
title: Adding the PingIntelligence policy components
description: Add the PingIntelligence policy components to your API.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_ibm_datapower_add_policy
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_ibm_datapower_add_policy.html
revdate: April 3, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Adding the PingIntelligence policy components

Add the PingIntelligence policy components to your API.

## Before you begin

Make sure to:

1. Download the PingIntelligence policy from the [Ping Identity Downloads](https://www.pingidentity.com/en/resources/downloads/pingintelligence.html) site.

2. Extract the policy by using the following command:

   ```
   # tar –zxvf  <<file name>>
   ```

   For example:

   ```
   # tar –zxvf pi-api-ibm-policy-4.1.0.tar.gz
   ```

## About this task

To add the PingIntelligence policy components:

## Steps

1. Sign on to IBM API Manger.

   ![A screen capture of the IBM API Connect API Manager sign-on page.](../_images/slt1582872404867.png)

2. To open the navigation pane, click the **Menu** ![bgq1582013473323](../_images/bgq1582013473323.png) icon on the top-left corner.

   ![A screen capture of the left navigation menu icon with a red arrow pointing to it.](../_images/xcv1582874439031.png)

3. Click **Drafts** in the navigation pane.

   ![A screen capture of the Drafts link selected in the left navigation with a red box around it.](../_images/yxs1582875288330.png)

4. Click the **APIs** tab.

   ![A screen capture of the APIs tab with a red box around it.](../_images/ikr1582875875209.png)

5. Click on your API under **TITLE** list or enter the API name in the **Search APIs** dialog box and select the API.

   ![A screen capture of the APIs tab with a red arrow pointing to the Search APIs field and a red box around the API Title list.](../_images/jpw1582902361778.png)

6. Click the **Source** tab to edit your API definition.

   ![A screen capture of the Source tab with a red box around it.](../_images/pdg1582902426419.png)

7. Copy and paste the contents of the PingIntelligence policy into the **Assembly** block of your API definition at three places:

   1. Open the `pi_policy.yaml` file, copy the contents of the **set-variable:** block with the ASE Config component and paste it in the next line after the **execute:** block in your API.

      ![A screen capture of the source editor with a red arrow pointing to set-variable.](../_images/lzv1582210794237.png)

   2. Next, copy the contents of the **gateway script:** block containing the ASE Request component from the `pi_policy.yaml` file and paste it after the last line of the ASE Config component.

      ![A screen capture of the source editor with a red arrow pointing to the value.](../_images/oxr1582212454931.png)

   3. Copy the contents of the **gateway script:** block containing the ASE Response component from the `pi_policy.yaml` file and paste it as the last component of your API.

      ![A screen capture of the source editor with a red arrow pointing to title.](../_images/jrt1582877124330.png)

   4. Copy the contents of the **gateway script:** block containing the ASE Response component from the `pi_policy.yaml` file and paste it as the last component of your API.

      ![A screen capture of the source editor with a red arrow pointing to title.](../_images/jrt1582877124330.png)

      |   |                                                                                                 |
      | - | ----------------------------------------------------------------------------------------------- |
      |   | The assembly component ASE Reponse should always be the last component of your policy assembly. |

8. Click the **Validate** icon to validate your changes, and then click the **Save** icon after completing the validation.

9. Click the **Assemble** tab to open the **Assemble** view. Verify the sequence of the components ASE Config, ASE Request, and ASE Response in the Policy Assembly.

   The order must match as highlighted in the red boxes in the following image.

   ![A screen capture of the Assemble page with red boxes around ASE Config, ASE Request, and ASE Response.](../_images/ejh1582040678382.png)

---

---
title: Adding the RetainHeader policy
description: To add the RetainHeader policy to the Akana API Gateway:
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_akana_add_retainheader
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_akana_add_retainheader.html
revdate: April 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding the RetainHeader policy

## About this task

To add the RetainHeader policy to the Akana API Gateway:

## Steps

1. Sign on to **Akana Policy Manager** and click **Tenant** in the left navigation.

2. Under **Policies**, click **Operational Policies**.

3. Select **Add Policy** and choose **Private Operational Script Policy** from the **Type** drop-down list.

   ![A screenshot of the Select Policy Creation Option page in Akana Policy Manager.](../_images/mfl1579954034176.png)

4. Click **Next**.

5. Enter **Policy Name** and **Description**, click **Finish**, and then click **Close**.

![A screenshot of the Specify Policy Details page in Akana Policy Manager.](../_images/rmt1581325031595.png)

1. Navigate to the **Workbench** tab.

2. In the **Private Operational Script Policy** section, select the policy name and click **Modify**.

![A screenshot of the Workbench tab in Akana Policy Manager.](../_images/ywk1581325705849.png)

1. For **Script Language**, select **JavaScript** from the drop-down list.

2. Copy the contents of the `retain-header-policy.js` script and paste them into **Expression**.

3. For **Function**, select **Pre-policy Auditing** from the drop-down list.

   ![A screenshot of the Modify Script Policy page in Akana Policy Manager.](../_images/wic1581327121243.png)

4. Click **Finish** and then click **Close**.

5. Under the **WorkFlow Actions**, click **Activate Policy** to activate the RetainHeader policy.

---

---
title: Akana API gateway sideband integration
description: This integration guide discusses PingIntelligence for APIs deployment in a sideband configuration with the Akana API Gateway.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_akana_integration
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_akana_integration.html
revdate: April 3, 2024
---

# Akana API gateway sideband integration

This integration guide discusses PingIntelligence for APIs deployment in a sideband configuration with the Akana API Gateway.

PingIntelligence for APIs in a sideband deployment mode integrates with the Akana API Gateway to provide in-depth analytics on API traffic. A PingIntelligence policy is installed in the Policy Manager component of the Akana API Gateway to pass API metadata to PingIntelligence for detailed API activity reporting and attack detection. For more information on sideband deployment, see [Sideband ASE](../pingintelligence_reference_guide/pingintelligence_sideband_ase.html).

PingIntelligence for APIs provides the JavaScript policy that extracts API metadata from a request and response processed by the Akana API Gateway. The API metadata is passed to API Security Enforcer (ASE). The following are a few highlights of the integration solution:

* Support for SSL connectivity through a valid certificate authority (CA)-signed certificate.

* Support for connection keep alive between the Akana Gateway and ASE for faster processing of request and response data.

* Support for ASE-failover by provisioning a secondary ASE.

* OAuth attribute extraction and username support for OAuth-enabled APIs.

* Interception of OAuth tokens sent as part of query parameters.

|   |                                                              |
| - | ------------------------------------------------------------ |
|   | The Akana Gateway does not support self-signed certificates. |

Three PingIntelligence policies are made available to support the integration. The policies are packaged in the `pi-api-akana-policy-4.x.x.tar.gz` file. The following diagram shows the directory structure for reference.

![A diagram of the PingIntelligence Akana directory strucutre.](../_images/arz1579618135863.png)

`pi_policy.js`: This is the main PingIntelligence policy. It extracts the metadata for each API call, formats it into JSON and makes API calls to pass the metadata to ASE.

`retain-header-policy.js`: After validating a token with the OAuth server, Akana gateway deletes the incoming Authorization header. As a result, this header does not get forwarded to ASE. The `retainHeader.js` remedies this by capturing the deleted Authorization header and passes it to `pi_policy.js` for metadata extraction. The `retainHeader.js` policy gets executed before `pi_policy.js`.

`config.js`: This script takes ASE configuration as input from the user. The script then connects the ASE nodes and the policy.

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `retain-header.js` policy needs to be attached to all OAuth-enabled APIs to ensure user information is extracted from API reqeusts. |

The following diagram shows the logical setup of PingIntelligence for APIs components and the Akana API Gateway:

![A diagram of the PingIntelligence components and Akana API gateway setup.](../_images/foo1579668498425.png)

The traffic flow through the Akana API Gateway and PingIntelligence for APIs components is explained below:

1. The client sends an incoming request to Akana API gateway.

2. PingIntelligence policy deployed on the Akana API Gateway is executed on the request to extract the metadata from the incoming request.

3. Akana API gateway makes an API call to send the request metadata to API Security Enforcer (ASE). The ASE checks the client identifiers, such as usernames and tokens, against the deny list. If all checks pass, ASE returns a `200-OK` response to the Akana API gateway. If not, a different response code is sent to the Akana API Gateway (400 or 403). The request information is also logged by ASE and sent to the PingIntelligence API Behavioral Security (ABS) artificial intelligence (AI) engine for processing.

4. The Akana API gateway forwards the API requests to the backend server after the ASE processes it. If the gateway receives a `403-Forbidden` response from ASE, it blocks the client. Otherwise, it forwards the request to the backend server.

5. The response from the backend server is received by the Akana API Gateway.

6. The PingIntelligence policy is again applied on the response to extract the metadata from the server response.

7. The Akana API gateway makes a second API call to pass the response information to ASE, which sends the information to the AI engine for processing. ASE sends a `200-OK` to the API Gateway.

8. The Akana API gateway sends the response received from the backend server to the client.

---

---
title: API discovery
description: PingIntelligence API discovery is a process to discover and report APIs from your API environment.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_axway_api_discovery
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_axway_api_discovery.html
revdate: April 3, 2024
---

# API discovery

PingIntelligence API discovery is a process to discover and report APIs from your API environment.

The discovered APIs are reported in the PingIntelligence Dashboard. APIs are discovered when a global API JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
\</div>)* is defined in API Security Enforcer (ASE).

For more information, see [API discovery and configuration](../managing_pingintelligence_for_apis/pingintelligence_api_discovery_configuration.html) . You can edit the discovered API's JSON definition in theDashboard before adding them to ASE. For more information on editing and configuring API discovery, see [Discovered APIs](../managing_pingintelligence_for_apis/pingintelligence_discovered_apis.html).

---

---
title: Apigee integration
description: PingIntelligence provides a shared flow to integrate Apigee Edge with PingIntelligence for APIs platform.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_apigee_integration
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_apigee_integration.html
revdate: April 3, 2024
---

# Apigee integration

PingIntelligence provides a shared flow to integrate Apigee Edge with PingIntelligence for APIs platform.

The two mechanisms of calling shared flows are flow hook and flow callout policies. A flow hook in Apigee Edge applies the PingIntelligence shared flow globally to all APIs in an environment in an organization. The FlowCallout policy in Apigee Edge applies the PingIntelligence shared flow on a per API basis in an environment in an organization.

PingIntelligence provides an automated tool to deploy both flow hook and flow callout polices.

The following diagram shows the logical setup of PingIntelligence API Security Enforcer (ASE) and Apigee Edge.

![A diagram of the traffic flow between Apigee Edge and PingIntelligence components](../_images/sce1631518881347.png)

Traffic flows through the Apigee Edge andPingIntelligence for APIs components as follows:

1. Incoming request to Apigee Edge from a client.

2. Apigee Edge makes an API call to send the request information to ASE.

3. ASE checks the request against a registered set of APIs and checks the origin Internet Protocol (IP) *(tooltip: \<div class="paragraph">
   \<p>The method by which data is sent across the internet from the source host to the destination host.\</p>
   \</div>)*, cookie, OAuth2 token, or API key against the deny list. If all checks pass, ASE returns a `200-OK` response to the Apigee Edge. If not, a different response code (403) is sent to Apigee Edge. The request information is also logged by ASE and sent to the ABS artificial intelligence (AI) engine for processing.

4. If Apigee Edge receives a `200-OK` response from ASE, then it forwards the request to the backend server. Otherwise, the gateway optionally blocks the client. In synchronous mode, the gateway waits for a response from ASE before forwarding the request to backend server. However, if asynchronous mode is enabled, the gateway forwards the request to the backend server without waiting for the response from ASE. The ASE passively logs the request and forwards it to ABS for attack analysis. It performs attack detection without blocking of attacks.

5. Apigee Edge receives the response from the backend server.

6. Apigee Edge makes a second API call to pass the response information to ASE, which sends the information to the AI engine for processing.

7. ASE receives the response information and sends a `200-OK` to Apigee Edge.

8. Apigee Edge sends the response received from the backend server to the client.

---

---
title: Apigee properties file configuration
description: The apigee.properties file is required for all sideband Apigee configurations.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_apigee_properties
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_apigee_properties.html
revdate: April 3, 2024
---

# Apigee properties file configuration

The `apigee.properties` file is required for all sideband Apigee configurations.

The properties file is used to set properties for the PingIntelligence policy tool after installation. You can optionally configure it to capture user information. You can find the file in the `/pingidentity/apigee/config/` directory.

The following tables describe the variables in the file.

**General variables**

| Variable              | Description                                                                                                                                                                                                                                                                                     |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `configuration_store` | Where to store the ASE token.The possible values are `kvm` and `custom`. The default is `custom`.When you choose `custom`, the ASE token is configured inside the PingIntelligence policy and uploaded to Apigee Edge directly. When `kvm` is chosen, the ASE token is stored in the KVM store. |
| `apigee_url`          | URL to connect to Apigee Edge.&#xA;&#xA;If your Apigee installation is on a private cloud, change the URL to the one that matches your Apigee management server API IP:Port or hostname with protocol.                                                                                          |
| `apigee_username`     | The username to connect to Apigee Edge.                                                                                                                                                                                                                                                         |
| `apigee_password`     | The password to connect to Apigee Edge.                                                                                                                                                                                                                                                         |
| `apigee_environment`  | The target environment for the PingIntelligence shared flow.                                                                                                                                                                                                                                    |
| `apigee_organization` | The target organization for the PingIntelligence shared flow.                                                                                                                                                                                                                                   |
| `ase_host_primary`    | The ASE primary host IP address and port or hostname and port.                                                                                                                                                                                                                                  |
| `ase_host_secondary`  | The ASE secondary host IP address and port or hostname and port.&#xA;&#xA;This field cannot be left empty. In a testing environment, you can provide the same IP address for primary and secondary ASE host.                                                                                    |
| `ase_ssl`             | Enable or disable SSL communication between Apigee Edge and ASE. The default value is `true`.                                                                                                                                                                                                   |
| `ase_sideband_token`  | Configure the ASE token generated in [Preparing to deploy the PingIntelligence shared flow](pingintelligence_prepare_apigee.html).                                                                                                                                                              |
| `enable_mtls`         | Enable or disable mutual authentication between ASE and the Apigee API gateway. The default is `false`.&#xA;&#xA;This feature requires ASE version 5.1.3 or later.                                                                                                                              |
| `mtls_password`       | When mutual TLS (MTLS) is enabled, the password to access the keystore.&#xA;&#xA;If the private key is password protected, then the keystore and private key password must be the same.                                                                                                         |

**Configuration properties to extract user information**

| Variable                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enable_oauth_policy`   | Choose whether to use the PingIntelligence OAuth policy to extract `user_info` or not. Possible values are `true` or `false`. The default value is `false`.- When set to `true`, the PingIntelligence OAuthPolicy is executed and `user_info` is sent to ASE.

- When set to `false`, the PingIntelligence OAuthPolicy is not executed. The`user_info` is captured from an existing custom OAuthPolicy, if available, and sent to ASE.In both the cases, even if authorization token is deleted by the gateway,`user_info` and token information are still sent to ASE.For more information on the PingIntelligence OAuth policy, see [Extract user information from access tokens](pingintelligence_extract_user_info.html). |
| `enable_async`          | Choose synchronous or asynchronous mode between the gateway and ASE. In synchronous mode, the gateway waits for a response from ASE before forwarding the request to backend server.If asynchronous mode is enabled, the gateway forwards the request to the backend server without waiting for the response from ASE. The ASE passively logs the request and forwards it to ABS for attack analysis. It performs attack detection without blocking of attacks. Possible values are `true` or `false`.                                                                                                                                                                                                                        |
| `access_token_position` | Location of `access_token` in the API request. Possible values are `header` or `queryparam`. The default value is `header`. It is used in the OAuthPolicy.```
access_token_position=queryparam
```&#xA;&#xA;At present, Apigee supports only the Bearer prefix in an authorization header.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `access_token_variable` | A variable to hold `access_token` value, as shown in the following example.```
access_token_variable=access_token => -H "access_token: Rft3dqrs56Blirls56a"
```The default value is `Authorization`. It is used in the OAuthPolicy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `username_key_mapping`  | This is used in the PingIntelligence policy to set the key of `username` attribute in `access_token` info. The default value is `username`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `client_id_key_mapping` | This is used in the PingIntelligence policy to set the key of `client_id` attribute in the `access_token` info. The default value is `client_id`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

**Timeout configurations**

| Variable            | Description                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout`   | Connection timeout in milliseconds between Apigee API gateway and PingIntelligence ASE.                                                                                                                                                                                                                                                                                                                                                   |
| `io_timeout`        | Read timeout in milliseconds between Apigee API gateway and PingIntelligence ASE.                                                                                                                                                                                                                                                                                                                                                         |
| `keepalive_timeout` | Connection keepalive timeout between Apigee API gateway and PingIntelligence ASE. Make sure that `enable_keepalive` to `true` in `ase.conf` for the keep-alive configuration to take effect.&#xA;&#xA;Make sure that the enable\_sideband\_keepalive is set to true in ase.conf file for keep-alive connection between Apigee API gateway and ASE.&#xA;&#xA;For more information, see Sideband ASE configuration using the ase.conf file. |

|   |                                                                           |
| - | ------------------------------------------------------------------------- |
|   | Backslashes (`\`) are not supported in `username` and `client_id` values. |

The following is a sample `apigee.properties` file.

```
# Copyright 2020 Ping Identity Corporation. All Rights Reserved.
# Ping Identity reserves all rights in The program as delivered. Unauthorized use, copying,
# modification, reverse engineering, disassembling, attempt to discover any source code or
# underlying ideas or algorithms, creating other works from it, and distribution of this
# program is strictly prohibited. The program or any portion thereof may not be used or
# reproduced in any form whatsoever except as provided by a license without the written
# consent of Ping Identity.  A license under Ping Identity's rights in the Program may be
# available directly from Ping Identity.

# KVM Mode kvm/custom
configuration_store=custom
# Apigee management server URL
apigee_url=https://api.enterprise.apigee.com
# Apigee management server username
apigee_username=
# Apigee management server username
apigee_password=
# Apigee environment to which it should be deployed
apigee_environment=prod
# Apigee organization name
apigee_organization=

# ASE Primary Host  <IP/Host>:<port>
ase_host_primary=
# ASE Secondary Host  <IP/Host>:<port>
ase_host_secondary=
# ASE SSL status
ase_ssl=true
# ASE sideband authentication token
ase_sideband_token=none

# Enable OAuth Policy (allowed values: true | false)

enable_oauth_policy=false
# Enable async (allowed values: true | false)
enable_async=true

# Position of Access Token (allowed values: header | queryparam)
access_token_position=header
# access_token_position=header, access_token_variable=Authorization => -H "Authorization: Bearer Rft3dqrs56Blirls56a"
# access_token_position=header, access_token_variable=access_token => -H "access_token: Rft3dqrs56Blirls56a"
# access_token_position=queryparam, access_token_variable=access_token => ...?access_token=Rft3dqrs56Blirls56a
access_token_variable=Authorization

# username key mapping in access_token. This is the key of username in access_token attributes
username_key_mapping=username
# client_id key mapping in access_token. This is the key of client_id in access_token attributes
client_id_key_mapping=client_id

# connection timeout between Apigee and ASE. Value is in milliseconds
connect_timeout=5000
# read timeout between Apigee and ASE. Value is in milliseconds
io_timeout=5000
# keepalive timeout between Apigee and ASE. Value is in milliseconds
# set enable_keepalive to true in ase.conf for the below configuration to take effect
keepalive_timeout=30000
```

|   |                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If `configuration_store` is set to `custom`, the configuration will be embedded into the PingIntelligence policy.If `configuration_store` is set to `kvm`, the configuration is pushed to a key-value map store while deploying the policy and is retrieved during policy execution. |

---

---
title: Apply the PingIntelligence policy
description: The PingIntelligence bundle includes API Security Enforcer (ASE) Check Request and Check Response encapsulated assertions.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_ca_api_apply_policy
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_ca_api_apply_policy.html
revdate: April 3, 2024
section_ids:
  ase-check-request: ASE Check Request
  ase-check-response: ASE Check Response
  api-discovery: API discovery
---

# Apply the PingIntelligence policy

The PingIntelligence bundle includes API Security Enforcer (ASE) Check Request and Check Response encapsulated assertions.

Apply these assertions to each API that you want to monitor using PingIntelligence. You can include these assertions in global policies if you want each incoming API call to automatically be checked by PingIntelligence, or you can attach those assertions in service-level policies.

For service-level policies, each API will add two assertions:

* ASE Check Request: Applied before routing the request to the backend

* ASE Check Response: Used after a call to the downstream endpoint (which is on line 25 in the image below)

  ![A screen capture of the ASE Check Request and ASE Check Response.](../_images/tsl1567230155731.png)

## ASE Check Request

The ASE Check Request assertion is configured with the following properties:

![A screen capture of the ASE Check Request Properties menu.](../_images/mch1567229850526.png)

If you do not configure the properties, the assertion extracts all required details by itself. This includes:

* Retrieving all the request headers

* Generating a correlationId (used as X-CorrelationID)

* Retrieving the ASE token

* Retrieving the ASE HTTPS host

* Retrieving the ASE request path

* Sending a message to ASE

PingIntelligence recommends adding `username` to capture the user name when it is available. Examples of username variables include:

* `$\{request.http.parameter.username}`: The username variable included in the incoming request HTTP header

* `$\{session.subscriber_id}`: The username variable when authenticating users with the OAuth Toolkit (OTK)

* `$\{request.username}`: The username variable in the case of HTTP basic authentication

The variable name to use in this case will often be very implementation-specific. Use what you already defined as part of your CA API Gateway implementation.

You should change others if you are customizing to accommodate special use cases.

* `CorrelationID`: Optional, used if you want to override `correlationId`, which will otherwise automatically be assigned

* `Custom data`: Optional, used to modify the internal of that assertion

* `true`: Useful for users developing an API for debugging or auditing purposes

The assertion has an output that is the generated `correlationId:ase.correlationId` that is utilized by the ASE check response assertion.

## ASE Check Response

This ASE Check Response assertion must be configured for each API with the following variables:

.

| Variable                     | Description                                                                                                                                                                                                                           |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Correlation-ID               | The ASE request and response correlation IDs, if specified, must match. Otherwise, keep `ase.correlationId`.                                                                                                                          |
| All service response headers | The default value is `$\{response.http.allheadervalues}`. This variable is created by the routing assertion that executed the backend call. If it is customized, for example, `myresponse`, then the updated variable should be used. |
| Response code                | The HTTP response status of the backend call.                                                                                                                                                                                         |
| Response status              | This value is ignored and hard coded to OK.                                                                                                                                                                                           |
| Username (optional)          | This should match the username variable setting in the ASE Check Request assertion. The screenshot shows an example where the username is being extracted from the incoming HTTP request.                                             |
| Custom data (optional)       | Used by customers who would like to modify the internals of an assertion.                                                                                                                                                             |
| true                         | Useful for users developing an API for debugging or auditing purposes.                                                                                                                                                                |

![A screenshot of the ASE Check Response Properties menu with the values entered in the fields.](../_images/izy1567232135031.png)

## API discovery

PingIntelligence API discovery is a process to discover, and report APIs from your API environment. The discovered APIs are reported in the PingIntelligence Dashboard. APIs are discovered when a global API JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
\</div>)* is defined in the ASE.

For more information, see [API discovery and configuration](../managing_pingintelligence_for_apis/pingintelligence_api_discovery_configuration.html). You can edit the discovered API's JSON definition in the Dashboard before adding them to ASE. For more information on editing and configuring API discovery, see [Discovered APIs](../managing_pingintelligence_for_apis/pingintelligence_discovered_apis.html).

---

---
title: Applying the PingIntelligence policy
description: Complete the following steps to attach the PingIntelligence policy to your API.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_mulesoft_applying_policy
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_mulesoft_applying_policy.html
revdate: April 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Applying the PingIntelligence policy

Complete the following steps to attach the PingIntelligence policy to your API.

## About this task

|   |                                                                                                                                                                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are applying the PingIntelligence policy in MuleSoft 3.9 and there is an earlier version of the policy already applied to your API, then remove the policy before applying the PingIntelligence 4.3 policy. To remove the policy, follow the steps in [Removing an existing PingIntelligence policy](pingintelligence_mulesoft_remove_policy.html). |

## Steps

1. Sign on to your MuleSoft Anypoint account.

2. Navigate to the API Manager and click the **Version** of the API to which you want to attach the PingIntelligence policy.

   ![A screenshot of the API Administration page with the PingIntelligenceAPI highlighted with a yellow box.](../_images/asv1564009266687.png)

3. On the API page, click **Policies**.

   The Policies page supports applying the PingIntelligence policy to the API.

   ![A screen capture of the PingIntelligenceAPI Settings page with a box around the Policies link in the left navigation.](../_images/rzc1564009267962.png)

4. Click **Apply New Policy**.

   ![A screenshot of the Policies page with a box around the Apply New Policy button.](../_images/hue1564009269082.png)

5. In the **Select Policy** pop-up window, select the PingIntelligence policy and click **Configure Policy**.

   ![A screenshot of the Select Policy page with a box around the PingIntelligence Policy.](../_images/gph1564009270242.png)

6. In the Apply policy page, enter the following values:

   * ASE Token that was generated as part of [prerequisite](pingintelligence_mulesoft_prepare.html).

   * ASE primary and secondary host and port. The traffic is sent to the ASE secondary host only when the primary ASE node is unreachable.

   * Enable SSL for a secure HTTPS connection between Mulesoft and PingIntelligence ASE.

   * Check the **Allow self-signed certificate** check-box to enable Mulesoft to accept a self-signed certificate from ASE.

   * If the **Allow asynchronous (non-blocking) request forwarding** check box is selected, the API Gateway will not wait for a response from ASE before propagating the inbound request.

     |   |                                                                                         |
     | - | --------------------------------------------------------------------------------------- |
     |   | The asynchronous option is only available in the PingIntelligence MuleSoft Java policy. |

   * Configure the **Connection Timeout** and **Read Timeout**. The behavior of the API gateway is governed by Connection Timeout and Read Timeout, in the event of API Gateway not able to connect to ASE or the response from ASE is delayed.

     | Timeout parameter  | Description                                                                                                                                      |
     | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
     | Connection Timeout | It governs the time the API gateway waits to establish a connection with ASE, following which it sends the client request to the backend server. |
     | Read Timeout       | It governs the time the API Gateway waits for ASE's response before sending the request to the backend server.                                   |

     The default value is 5000 milliseconds or 5 seconds. It is good practice to configure a small value to limit the delay in case ASE is not reachable or unresponsive.

     ![A screen capture of the Apply policy page.](../_images/mhb1599734445149.png)

     |   |                                                                                                                        |
     | - | ---------------------------------------------------------------------------------------------------------------------- |
     |   | If there are any changes to the ASE endpoints, repeat the process explained in step 6 and re-deploy the configuration. |

7. Navigate to your API and click the version number as described in step 1. In the API page, scroll down to the **Deployment Configuration** section and click **Redeploy**.

   ![A screen capture of the Deployment Configuration page.](../_images/jlh1564009272575.png)

8. If your API is configured with Basic endpoint on MuleSoft version 3.9.x, then add the following properties in your MuleSoft application:

   * `http.status`

   * `http.reason`

   * `content-type`

   * `content-length`

   You can use the `set-property` element to configure these properties in the MuleSoft application. If required, you can also set other response side headers to send more information to the PingIntelligence policy.

   \+

   ### Result:

   The following is a sample configuration of setting response side details. For more information on setting the properties in a Mule application, see [property transformer](https://docs.mulesoft.com/mule-runtime/3.9/property-transformer-reference).

```
<set-property propertyName="http.status" value="200" doc:name="Property"/>
<set-property propertyName="http.reason" value="OK" doc:name="Property"/>
<set-property propertyName="content-type" value="application/json" doc:name="Property"/>
<set-property propertyName="content-length" value="21" doc:name="Property"/>
<set-property propertyName="set-cookie" value="PHPSESSIONID=CookieValue" doc:name="Property"/>
```

---

---
title: Applying the PingIntelligence policy to APIs
description: The PingIntelligence policy can be applied at tenant level, org level and at individual API level.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_akana_apply_policy
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_akana_apply_policy.html
revdate: April 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Applying the PingIntelligence policy to APIs

## About this task

The PingIntelligence policy can be applied at tenant level, org level and at individual API level.

To add a policy at the API level:

## Steps

1. Sign on to **Akana Portal**.

2. Click the API name.

3. In the left navigation, click **Implementations**.

![A screenshot of the Implementations page in Akana Policy Manager.](../_images/eto1581660045416.png)

1. Click the **API Implementation Name** icon.

   Possible values for **API Implementation** are `Live`, `Sandbox`, or `Development`.

2. In the **Policies** section, click **Edit**.

![A screenshot of the API Implementations page in Akana Policy Manager.](../_images/nrv1581661253141.png)

1. Find the PingIntelligence policy in the **Available Policies** pane, and click **Attach** under the PingIntelligence policy.

2. Click **Save**.

![A screenshot of Edit Policies page in Akana Policy Manager.](../_images/xni1579955621504.png)

---

---
title: Applying the RetainHeader policy to APIs
description: The RetainHeader policy can be applied at the tenant, org, and at individual API level.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_akana_apply_retainheader
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_akana_apply_retainheader.html
revdate: April 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Applying the RetainHeader policy to APIs

## About this task

The RetainHeader policy can be applied at the tenant, org, and at individual API level.

To add a policy at the API level:

## Steps

1. Sign on to the **Akana Portal**.

2. Click the API name.

3. In the left navigation, click **Implementations**.

![A screenshot of the Implementations page in the Akana Portal.](../_images/eto1581660045416.png)

1. Click the **API Implementation Name** icon.

   Possible values for **API Implementation** are `Live`, `Sandbox`, or `Development`.

2. In the **Policies** section, click **Edit**.

![A screenshot of the API Implementations Details page in Akana Policy Manager.](../_images/kpd1581660542419.png)

1. Under **Available Policies**, find the RetainHeader policy, and click **Attach** under the RetainHeader policy.

2. Click **Save**.

![A screenshot of the Edit Policies page in Akana Policy Manager.](../_images/xni1579955621504.png)

---

---
title: AWS API Gateway integration
description: This integration guide discusses the deployment of PingIntelligence for APIs in a sideband configuration with an AWS API Gateway through CloudFront.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_aws_integration
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_aws_integration.html
revdate: April 3, 2024
---

# AWS API Gateway integration

This integration guide discusses the deployment of PingIntelligence for APIs in a sideband configuration with an AWS API Gateway through CloudFront.

PingIntelligence for APIs provides a sideband policy that can be installed in CloudFront. The policy uses AWS Lambda functions to pass API metadata to PingIntelligence for detailed API activity reporting and attack detection with optional client blocking.

PingIntelligence for APIs provides an automated tool to deploy a the policy, which is implemented using the AWS Lambda functions. The policy requires AWS CloudFront to be present with all caching disabled. AWS Lambda functions must be initially deployed in the US-East-1 region, and the policy definition is pushed to any region with your API Gateways after the PingIntelligence policy is added.

The PingIntelligence sideband policy requires a CloudFront instance, which can be an existing or new instance.

|   |                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The default AWS Lambda memory is sufficient for up to 1000 QPS. For a larger QPS, contact Ping Identity support. See the [aws.properties](pingintelligence_configure_policy_tool.html#section_k4q_4hg_cgb) file for default origin response value. |

The following diagram shows the logical setup of PingIntelligence API Security Enforcer (ASE) and CloudFront.

![Diagram showing traffic flow between cloud front and PingIntelligence components](../_images/qpo1564009234899.png)

The traffic flow through the CloudFront and PingIntelligence for APIs components is as follows:

1. An incoming API client request destined for the API Gateway arrives at CloudFront.

2. A PingIntelligence AWS Lambda policy makes an API call to send the request metadata to PingIntelligence ASE.

3. ASE checks the request against a registered set of APIs and looks for the origin IP, cookie, OAuth2 token, or API key in the API Behavioral Security (ABS) artificial intelligence (AI) engine-generated deny list. If all checks pass, ASE returns a `200-OK` response to AWS Lambda. If the checks don't pass, ASE sends a `403` response code to AWS Lambda. The request information is also logged by ASE and sent to the ABS AI Engine for processing.

4. If CloudFront receives a `200-OK` response from ASE, it forwards the client request to the backend server. Otherwise, the CloudFront blocks the client when blocking is enabled for the API.

5. CloudFront receives the response from the backend server.

6. The Lambda response function makes a second API call to pass the response information to ASE.

7. ASE receives the response information and sends a `200-OK` to AWS Lambda. The response information is also logged by ASE and sent to the ABS AI Engine for processing.

8. CloudFront sends the response received from the backend server to the client.

---

---
title: Axway sideband integration
description: This guide describes the deployment of PingIntelligence for APIs in a sideband configuration with an Axway API Gateway.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_axway_integration
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_axway_integration.html
revdate: April 3, 2024
---

# Axway sideband integration

This guide describes the deployment of PingIntelligence for APIs in a sideband configuration with an Axway API Gateway.

A PingIntelligence policy is installed in the Axway API Gateway and passes API metadata to PingIntelligence for detailed API activity reporting and attack detection with optional client blocking. PingIntelligence 4.0 software adds support for reporting and attack detection based on usernames captured from token attributes.

The following diagram shows the complete deployment:

![A diagram of the deployment of PingIntelligence for APIs in a sideband configuration with an Axway API Gateway.](../_images/zdr1564009068653.png)

The following is the traffic flow through Axway and PingIntelligence for APIs components.

1. Client sends an incoming request to Axway.

2. Axway makes an API call to send the request metadata to API Security Enforcer (ASE).

3. ASE checks the request against a registered set of APIs and checks the origin IP, cookie, API Key, or OAuth2 token in the PingIntelligence artificial intelligence (AI) engine-generated deny list. If all checks pass, ASE returns a `200-OK` response to the Axway. If not, a different response code is sent to Axway. The request information is also logged by ASE and sent to the AI engine for processing.

4. If Axway receives a `200-OK` response from ASE, then it forwards the request to the backend server. Otherwise, the Gateway optionally blocks the client.

5. The response from the backend server is received by Axway.

6. Axway makes a second API call to pass the response information to ASE, which sends the information to the AI engine for processing.

7. ASE receives the response information and sends a `200-OK` to Axway.

8. Axway sends the response received from the backend server to the client.

---

---
title: Azure APIM sideband integration
description: This guide describes the deployment of PingIntelligence for APIs in a sideband configuration with Azure API Manager (APIM).
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_azure_apim
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_azure_apim.html
revdate: April 3, 2024
---

# Azure APIM sideband integration

This guide describes the deployment of PingIntelligence for APIs in a sideband configuration with Azure API Manager (APIM).

A PingIntelligence policy is installed in APIM and passes API metadata to PingIntelligence for detailed API activity reporting and attack detection with optional client blocking. The PingIntelligence policy for Azure also supports detecting attacks based on the username.

The APIM PingIntelligence policy works in the following two configurable modes:

* Asynchronous mode: When the PingIntelligence policy is configured in the Asynchronous mode, APIM does not wait for a response from PingIntelligence API Security Enforcer (ASE) before sending the API client request to the backend API server. In this mode, PingIntelligence deployment passively logs the API request and response. It performs detailed API activity reporting and attack detection without blocking of attacks.

* Synchronous mode: When the PingIntelligence policy is configured in the Synchronous mode, Azure API gateway waits for a response from PingIntelligence ASE before sending the request to the backend API server or blocking it. In this mode, PingIntelligence actively logs and responds to the API requests and response. It performs detailed API activity reporting with attack detection and blocking of attacks.

The following diagram shows the logical setup of PingIntelligence ASE and Azure:

![A diagram of the PingIntelligence ASE and Azure setup.](_images/aib1564009241883.png)

Below is the traffic flow through the Azure and PingIntelligence for APIs components.

1. Client sends an incoming request to APIM.

2. APIM makes an API call to send the request metadata to ASE.

3. ASE checks the request against a registered set of APIs and looks up the origin Internet Protocol (IP) *(tooltip: \<div class="paragraph">
   \<p>The method by which data is sent across the internet from the source host to the destination host.\</p>
   \</div>)*, cookie, OAuth2 token, or API key on the PingIntelligence AI engine-generated deny list. If all checks pass, ASE returns a `200-OK` response to APIM. If not, a different response code is sent to APIM. The request information is also logged by ASE and sent to the AI engine for processing.

4. If APIM receives a `200-OK` response from ASE, then it forwards the request to the backend server. Otherwise, if it receives a `403-forbidden` response, the APIM blocks the client when blocking is enabled for the API.

5. The response from the backend server is received by APIM.

6. APIM makes a second API call to pass the response information to ASE which sends the information to the AI engine for processing.

7. ASE receives the response information and sends a `200-OK` to Azure.

8. APIM sends the response received from the backend server to the client.

---

---
title: CA API gateway sideband integration
description: This guide describes the deployment of PingIntelligence for APIs in a sideband configuration with CA API gateway.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_ca_integration
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_ca_integration.html
revdate: April 3, 2024
---

# CA API gateway sideband integration

This guide describes the deployment of PingIntelligence for APIs in a sideband configuration with CA API gateway.

You can attach the PingIntelligence for APIs integration to your APIs in the CA API Gateway by incorporating the Encapsulated Assertions to a subset of or to each API policies. When these Encapsulated Assertions are executed inside an API Gateway policy, the gateway passes API metadata to PingIntelligence for detailed API activity reporting and attack detection with optional client blocking.

The following diagram shows the logical setup of PingIntelligence for APIs and CA API gateway:

![A diagram of the PingIntelligence and CA API gateway setup.](../_images/hyr1567065125490.png)

Here is the traffic flow through the CA API gateway and PingIntelligence for APIs components.

1. Incoming API Client request arrives at the CA API Gateway

2. A PingIntelligence assertion running on the CA API Gateway makes an API call to send the request metadata to PingIntelligence ASE

3. ASE checks the request against a registered set of APIs and looks for the origin IP, cookie, OAuth2 token, or API key in the PingIntelligence Blacklist. If all checks pass, ASE returns a `200-OK` response to CA. If the client is on the deny list and blocking is enabled, a `403 response` is sent to CA. The request information is also logged by ASE and sent to the AI engine for processing.

4. If CA receives a `200-OK` response from ASE, then it forwards the client request to the backend server. Otherwise, the CA blocks the client when a `403 response` is received.

5. The response from the backend server is received by CA.

6. CA makes a second API call to pass the response information to ASE.

7. ASE receives the response information and immediately sends a `200-OK` to CA. The response information is also logged by ASE and sent to the AI engine for processing.

8. CA sends the response received from the backend server to the client.

PingIntelligence encapsulated assertions include capabilities for enhanced sideband performance and availability including:

* Persistent SSL sessions: Support for flowing sideband calls across a persistent Secure Sockets Layer (SSL) *(tooltip: \<div class="paragraph">
  \<p>A protocol for authenticated and encrypted links between networked machines, typically over HTTPS. SSL was deprecated in 1999 in favor of Transport Layer Security (TLS).\</p>
  \</div>)* session between the API Gateway and PingIntelligence.

  |   |                                                                                                      |
  | - | ---------------------------------------------------------------------------------------------------- |
  |   | Requires enabling `enable_sideband_keepalive` parameter in the PingIntelligence ASE `ase.conf` file. |

* Redundant PingIntelligence nodes: Optional redundant PingIntelligence ASE nodes can be configured in the encapsulated assertion to bypass a node failure.

---

---
title: Capturing ASE details
description: Capture the Service QName, Interface Name, and Operation Name for the primary and secondary ASE nodes.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_integrations:pingintelligence_akana_capture
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_integrations/pingintelligence_akana_capture.html
revdate: April 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Capturing ASE details

Capture the **Service QName**, **Interface Name**, and **Operation Name** for the primary and secondary ASE nodes.

## About this task

The **Service QName**, **Interface Name**, and **Operation Name** are used in `config.js`.

To capture these values:

## Steps

1. Sign on to **Akana Policy Manager**, navigate to the **Organization Tree** on the left, and select the **Tenant** and then the **ASE API**.

2. Expand the **Services** and click on the **API**:

   1. Copy the **Service QName** and paste it into a text editor.

      ![A screenshot of the ASE API details in Akana Policy Manager with the Service QName highlighted.](../_images/mlj1579951710887.png)

   2. Under **Interfaces and Bindings**, copy the **Interface Name** and paste it into a text editor.

      ![A screenshot of the ASE API details in Akana Policy Manager with the Interface Name highlighted.](../_images/odv1579951926418.png)

   3. Click **Operations** tab on the menu, copy **Operation Name**, and paste it into a text editor.

      ![A screenshot of the ASE API details in Akana Policy Manager with the Operation Name highlighted.](../_images/zhg1579952225433.png)

3. To capture the Service Qname, Interface Name, and Operation Name details for a secondary ASE API, repeat steps 1-2.

## Next steps

Use the captured values to deploy a policy in the Akana API Gateway. See [Deploying PingIntelligence policies](pingintelligence_akana_deploy.html).