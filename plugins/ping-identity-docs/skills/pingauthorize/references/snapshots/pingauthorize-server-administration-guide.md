---
title: Adding an Amazon S3 deployment package store to PingAuthorize
description: To use Amazon Simple Storage Service (S3) as your deployment package store, add read access for your S3 bucket to the PingAuthorize Server.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_amazons3_deploy_package
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_amazons3_deploy_package.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 25, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
  steps-2: Steps
  next-steps: Next steps
---

# Adding an Amazon S3 deployment package store to PingAuthorize

To use Amazon Simple Storage Service (S3) as your deployment package store, add read access for your S3 bucket to the PingAuthorize Server.

Use the admin console or `dsconfig` to add the Amazon S3 deployment package store. If necessary, review your existing S3 bucket configurations on the S3 dashboard in the Amazon Web Services (AWS) Management Console.

## Before you begin

If your environment doesn't use an IAM role to provide credentials (for example, IAM roles for service accounts on Amazon EKS or an instance profile on EC2), you must create an access key and accompanying secret key for your S3 bucket. Learn more in [Configuring the IAM user](paz_amazon_deployment_store_setup.html#create_amazon_iam_user).

* Admin console

* dsconfig

### Steps

1. In the PingAuthorize admin console, go to **Configuration > Authorization and Policies > Deployment Package Stores**.

2. Click **New Deployment Package Store**.

3. In the **New Deployment Package Store** modal, select **S3 Deployment Package Store**.

4. Complete the **General Configuration**:

   1. Enter a **Name** for the deployment package store.

   2. In the **Poll Interval** field, enter a value, in seconds, for how often the Amazon S3 bucket should be polled for changes.

      |   |                                                                                                                                                                         |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you set the poll interval to `0`, the server won't scan for new packages after initializing the store. The server will only load new deployment packages on restart. |

   3. In the **S3 Bucket Name** field, enter the name of your Amazon S3 bucket as shown on the AWS services page.

   4. In the **S3 Bucket Prefix** field, enter the S3 bucket prefix.

   5. In the **S3 Server Endpoint** field, enter the S3 bucket endpoint.

   6. In the **S3 Region Name** field, enter the AWS region for the S3 bucket.

   7. Next to the **S3 Access Key ID** field, click **Set Value** and enter the S3 access key ID you copied in [Configuring the IAM user](paz_amazon_deployment_store_setup.html#create_amazon_iam_user).

   8. Enter the S3 access key ID value again to confirm and click **OK**.

      |   |                                                                                                  |
      | - | ------------------------------------------------------------------------------------------------ |
      |   | Your access key value isn't displayed after you enter it. The page still displays **Set Value**. |

   9. Next to the **S3 Secret Key** field, click **Set Value** and enter the S3 secret key you copied in [Configuring the IAM user](paz_amazon_deployment_store_setup.html#create_amazon_iam_user).

   10. Enter the S3 secret key value again to confirm and click **OK**.

       |   |                                                                                                  |
       | - | ------------------------------------------------------------------------------------------------ |
       |   | Your secret key value isn't displayed after you enter it. The page still displays **Set Value**. |

5. If your S3 bucket uses a legacy path-style URL, select the **Enabled** checkbox under **S3 Use Path Style Access**.

   |   |                                                                                                                                                                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Starting with PingAuthorize 11.0, the PingAuthorize Server expects virtual-hosted-style URLs by default when connecting to Amazon S3.Learn more in [Virtual hosting of general purpose buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html) in the Amazon S3 documentation. |

6. (Optional) Complete the **Policy Security** configuration.

   |   |                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you select **Signed** in the **Deployment Package Security Level** list, you must select a **Deployment Package Trust Store**. |

7. Click **Save**.

   #### Result:

   Your Amazon S3 deployment package store is displayed on the **Deployment Package Stores** page.

### Steps

* To create an Amazon S3 deployment package store, use the the `dsconfig create-deployment-package-store` command with the following arguments:

  | Argument                                     | Required | Description                                                                                                                                                                                                                                                                                             |
  | -------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `--type <type>`                              | Required | Set to `s3`.                                                                                                                                                                                                                                                                                            |
  | `--store-name: <store-name>`                 | Required | Specifies a unique name for the configuration object.                                                                                                                                                                                                                                                   |
  | `--set poll-interval:"<poll-interval>"`      | Required | Specifies how often, in seconds, the PingAuthorize Server scans the deployment package store for new deployment packages.If you set the poll interval to `0`, the server won't scan for new packages after initializing the store. The server will only load new deployment packages on restart.        |
  | `--set s3-bucket-name:<bucket-name>`         | Required | Specifies the name of the S3 bucket in AWS.                                                                                                                                                                                                                                                             |
  | `--set s3-bucket-prefix:<bucket-prefix>`     | Required | Specifies the prefix value for the S3 bucket.                                                                                                                                                                                                                                                           |
  | `--set s3-server-endpoint:<server-endpoint>` | Optional | Specifies the S3 service endpoint.                                                                                                                                                                                                                                                                      |
  | `--set s3-region-name:<server-region>`       | Optional | Specifies the AWS region for the S3 bucket.                                                                                                                                                                                                                                                             |
  | `--set s3-access-key-id:<access-key-id>`     | Optional | Specifies the access key ID used to authenticate to the S3 bucket. If omitted, the server uses the AWS SDK default credentials provider chain (for example, IRSA on Amazon EKS, an instance profile on Amazon EC2, or environment variables).                                                           |
  | `--set s3-secret-key:<secret-key>`           | Optional | Specifies the secret key used to authenticate to the S3 bucket. If omitted, the server uses the AWS SDK default credentials provider chain.                                                                                                                                                             |
  | `--set s3-use-path-style-access:true`        | Optional | Enables legacy S3 path-style access. Defaults to `false`.&#xA;&#xA;Starting with PingAuthorize 11.0, the PingAuthorize Server uses virtual-hosted–style URLs by default when connecting to Amazon S3.&#xA;&#xA;Learn more in Virtual hosting of general purpose buckets in the Amazon S3 documentation. |

## Next steps

[Configure the PingAuthorize Server to use embedded PDP mode with your deployment package store](paz_config_embedded_pdp.html#config_embedded_dps_store).

---

---
title: Adding an Azure deployment package store
description: To use the Deployment Manager, add a deployment package store for read access to the PingAuthorize server.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_azure_deploy_package_store
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_azure_deploy_package_store.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
section_ids:
  about-this-task: About this task
  adding-an-azure-deployment-package-store-using-the-administrative-console: Adding an Azure deployment package store using the administrative console
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
  next-steps: Next steps
  adding-an-azure-deployment-package-store-using-dsconfig: Adding an Azure deployment package store using dsconfig
  steps-2: Steps
  choose-from: Choose from:
  next-steps-2: Next steps
---

# Adding an Azure deployment package store

To use the Deployment Manager, add a deployment package store for read access to the PingAuthorize server.

## About this task

Use the administrative console or `dsconfig` to add the deployment package store.

* Administrative console

* Dsconfig

## Adding an Azure deployment package store using the administrative console

### Before you begin

Set up your Azure storage account:

* If you don't already have an Azure storage account, create one.

* Add a container to your storage account.

* Record the Connection string value found in your account's Access key settings.

For information on setting up an Azure storage account, see your Azure Blob Storage documentation.

### Steps

1. In the administrative console, go to Configuration → Authorization and Policies → Deployment Package Stores.

2. Click New Deployment Package Store.

3. In the New Deployment Package Store menu, select Azure Deployment Package Store.

4. Complete the General Configuration fields.

   1. In the Name field, enter a name for the deployment package store.

   2. In the Poll Interval field, enter a value in seconds for how often the Azure store should be polled for changes.

      |   |                                         |
      | - | --------------------------------------- |
      |   | A value of `0` only updates on restart. |

   3. In the Azure Blob Connection String field, enter the connection string shown in your Azure storage account's Access key settings.

      |   |                                                                                                      |
      | - | ---------------------------------------------------------------------------------------------------- |
      |   | Your connection string value is not displayed after you enter it. The page still displays Set Value. |

   4. In the Azure Blob Container field, enter the name of your container.

   5. In the Azure Blob Prefix field, enter the [prefix you defined](paz_config_pe_publish_policies.html) for the deployment package store.

5. **Optional:** Complete the Policy Security fields.

   |   |                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you select signed in the Deployment Package Security Level field, you must complete the Deployment Package Trust Store field. |

6. Click Save To PingAuthorize Server Cluster.

   #### Result:

   Your Azure deployment package store is displayed on the Deployment Package Stores page.

### Next steps

[Configure the PingAuthorize server to use embedded PDP mode with your deployment package store](paz_config_embedded_pdp.html#config_embedded_dps_store).

## Adding an Azure deployment package store using dsconfig

### Steps

* Run `dsconfig` with the `create-deployment-package-store` option:

  #### Choose from:

  * Create a store with an unsigned deployment package.

    ```
    dsconfig create-deployment-package-store \
      --store-name "<store-name>" \
      --type azure  \
      --set "poll-interval:<poll-interval>" \
      --set "azure-blob-connection-string:<blob-connection-string>"  \
      --set "azure-blob-container:<blob-container>"  \
      --set "azure-blob-prefix:<blob-prefix>"
    ```

  * Create a store with `deployment-package-security-level` set to `signed`.

    ```
    dsconfig create-deployment-package-store \
      --store-name "<store-name>"  \
      --type azure  \
      --set "poll-interval:<poll-interval>" \
      --set "azure-blob-connection-string:<blob-connection-string>"  \
      --set "azure-blob-container:<blob-container>"  \
      --set "azure-blob-prefix:<blob-prefix>"
      --set deployment-package-security-level:signed  \
      --set "deployment-package-trust-store:<trust-store-provider-name>"  \
      --set "deployment-package-verification-key-nickname:<key-nickname>"
    ```

### Next steps

[Configure the PingAuthorize server to use embedded PDP mode with your deployment package store](paz_config_embedded_pdp.html#config_embedded_dps_store).

---

---
title: Administration accounts
description: "Administration accounts, called root distinguished names (DNs), are stored in a branch of the configuration backend: cn=Root DNs,cn=config."
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_admin_accts
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_admin_accts.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# Administration accounts

Administration accounts, called root distinguished names (DNs), are stored in a branch of the configuration backend: `cn=Root DNs,cn=config`.

When setup is run, the process creates a superuser account that is typically named `cn=Directory Manager`. Although PingAuthorize Server is not an LDAP directory server, it follows this convention by default. As a result, its superuser account is also typically named `cn=Directory Manager`.

To create additional administration accounts, use `dsconfig` or, to add root DN users, use the PingAuthorize administrative console.

---

---
title: API gateway integration
description: Enable attribute-based access control (ABAC) through your API gateway by installing the PingAuthorize API integration adapter (where supported) and connecting to the Sideband API.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_api_gw_integration
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_api_gw_integration.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 12, 2023
section_ids:
  processing-steps: Processing steps
---

# API gateway integration

Enable attribute-based access control (ABAC) through your API gateway by installing the PingAuthorize API integration adapter *(tooltip: \<div class="paragraph">
\<p>Plug-in software that allows Ping products to interact with web applications and authentication systems.\</p>
\</div>)* (where supported) and connecting to the Sideband API.

For more information on specific API gateway integrations, see [PingAuthorize Integrations](../pingauthorize_integrations/paz_integrations_main.html).

Sequence diagram of the PingAuthorize sideband API inbound and outbound data flow involving the client, the API gateway, PingAuthorize, the PDP, and the REST API

## Processing steps

1. When the API gateway receives a request from an API gateway adapter, it makes a call to the Sideband API to process the request.

2. The Sideband API returns a response that contains a modified version of the HTTP client's request.

   The API gateway forwards the response to the REST API.

3. If the Sideband API returns a response that indicates the request is unauthorized or not to be forwarded, the response includes the response to be returned to the client.

   The API gateway returns the response to the client without forwarding the request to the REST API.

4. When the API gateway receives a response from the REST API, it makes a call to the Sideband API to process the response.

5. The Sideband API returns a response that contains a modified version of the REST API's response.

   The API gateway forwards the response to the client.

---

---
title: API gateway path parameters
description: Path parameters are dynamic values in the request URI that are extracted and included in policy requests as fields of the Gateway policy request attribute.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_sec_gw_path_parameters
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_sec_gw_path_parameters.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 30, 2026
section_ids:
  basic-example: Basic example
  advanced-example: Advanced example
---

# API gateway path parameters

The `inbound-base-path` property value can include parameters. If parameters are found and matched, they are included in policy requests as fields of the `Gateway` policy request attribute.

Other configuration properties can use these parameters. Learn more in [Gateway API Endpoint configuration properties](paz_gw_api_endpoint_config_parms.html).

You must use the `inbound-base-path` property to introduce parameters. Other configuration properties cannot introduce new parameters.

## Basic example

The following example configuration demonstrates how request URIs are mapped to the outbound path to alter policy requests:

| Gateway API Endpoint property | Example value                               |
| ----------------------------- | ------------------------------------------- |
| `inbound-base-path`           | `/accounts/{accountId}/transactions`        |
| `outbound-base-path`          | `/api/v1/accounts/{accountId}/transactions` |
| `policy-request-attribute`    | `foo=bar`                                   |

A request URI with the path `/accounts/XYZ/transactions/1234` matches the inbound base path and is mapped to the outbound path `/api/v1/accounts/XYZ/transactions/1234`.

The following properties are added to the policy request:

* `HttpRequest.ResourcePath : 1234`

* `Gateway.accountId : XYZ`

* `Gateway.foo : bar`

## Advanced example

Unlike the basic example, which extracted a single path parameter, this example demonstrates how multiple parameters can be extracted from the request URI and referenced in other configuration properties.

Consider the following example configuration:

| Gateway API Endpoint property | Example value                            |
| ----------------------------- | ---------------------------------------- |
| `inbound-base-path`           | `/health/{tenant}/{resourceType}`        |
| `outbound-base-path`          | `/api/v1/health/{tenant}/{resourceType}` |
| `service`                     | `HealthAPI.{resourceType}`               |
| `resource-path`               | `{resourceType}/{_TrailingPath}`         |

A request URI with the path `/health/OmniCorp/patients/1234` matches the inbound base path and is mapped to the outbound path `/api/v1/health/OmniCorp/patients/1234`.

The following properties are added to the policy request:

* `service : HealthAPI.patients`

* `HttpRequest.ResourcePath : patients/1234`

* `Gateway.tenant : OmniCorp`

* `Gateway.resourceType : patients`

---

---
title: API gateway request and response flow
description: Using the API gateway pattern, PingAuthorize processes JSON requests and responses in two distinct phases according to a defined sequence.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_sec_gw_request_response_flow
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_sec_gw_request_response_flow.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 7, 2022
---

# API gateway request and response flow

Using the API gateway pattern, PingAuthorize processes JSON requests and responses in two distinct phases according to a defined sequence.

The gateway handles proxied requests in the following phases:

* Inbound phase – When a client submits an API request to PingAuthorize Server, the gateway forms a policy request based on the API request and submits it to the policy decision point (PDP) for evaluation. If the policy result allows it, PingAuthorize Server forwards the inbound *(tooltip: \<div class="paragraph">
  \<p>A direction of message flow coming into a service. The type of message depends service's identity access management role.\</p>
  \</div>)* request to the API server.

* Outbound phase – After PingAuthorize Server receives the upstream API server's response, the gateway again forms a policy request, this time based on the API server response, and submits it to the PDP. If the policy result is positive, PingAuthorize Server forwards the outbound *(tooltip: \<div class="paragraph">
  \<p>The direction of transaction flow from a service or server.\</p>
  \</div>)* response to the client.

Sequence diagram of the PingAuthorize API security gateway inbound and outbound data flow involving the client, PingAuthorize, the PDP, and the REST API

The API gateway supports only JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
\</div>)* requests and responses.

---

---
title: API security gateway authentication
description: The API security gateway authenticates requests through bearer tokens by default, and you can configure it to handle authentication according to your preferences.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_api_security_gw_authn
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_api_security_gw_authn.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 28, 2025
section_ids:
  example: Example
  example-2: Example
---

# API security gateway authentication

The API security gateway authenticates requests through bearer tokens by default, and you can configure it to handle authentication according to your preferences.

Although the gateway doesn't require the authentication of requests, the default policy set requires bearer token authentication.

To support this, the gateway uses the configured access token validators to evaluate bearer tokens that are included in incoming requests. The validation result is supplied to the policy request in the `HttpRequest.AccessToken` attribute, and the user identity associated with the token is provided in the `TokenOwner` attribute.

Policies use this authentication information to affect the processing of requests and responses. For example, a policy in the default policy set requires that all requests are made with an active access token.

```
Rule: Deny if HttpRequest.AccessToken.active Equals false

Statement:
  Code: denied-reason
  Applies To: Deny
  Payload: {"status":401, "message": "invalid_token", "detail":"Access token is expired or otherwise invalid"}
```

Gateway API Endpoints include the following configuration properties to specify how client authentication is handled:

* `http-auth-evaluation-behavior`

  Determines whether the Gateway API Endpoint evaluates or modifies the HTTP authentication scheme and whether this scheme is forwarded to the API server.

  This property accepts the following values:

  * `do-not-evaluate`

    The Gateway API Endpoint doesn't evaluate or modify the HTTP authentication scheme. This can be useful when implementing an authentication scheme that doesn't evaluate bearer tokens, such as MTLS.

    If the client request includes an `Authorization` header, the PingAuthorize Server forwards the unmodified header to the external API server.

    |   |                                                                                                                                                                                                                                                           |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If you specify this value, policies protecting this endpoint should not enforce constraints on request authentication, such as the validity of the access token. The default policy snapshot enforces such a constraint in the `Token Validation` policy. |

  * `evaluate-and-forward`

    The Gateway API Endpoint evaluates the provided authentication credentials and makes authentication information available for policy evaluation. If the client request includes an `Authorization` header, the PingAuthorize Server forwards the unmodified header to the external API server unless a policy decision directs otherwise.

    This value is set by default.

  * `evaluate-and-discard`

    The Gateway API Endpoint evaluates the provided authentication credentials and makes authentication information available for policy evaluation. If the client request includes an `Authorization` header, the PingAuthorize Server removes this header before forwarding the request to the external API server.

  * `evaluate-and-replace`

    The Gateway API Endpoint evaluates the provided authentication credentials and makes authentication information available for policy evaluation. If the client request includes an `Authorization` header, the PingAuthorize Server replaces this header with one containing the basic authentication credentials defined for the external API server.

    |   |                                                                                                                                |
    | - | ------------------------------------------------------------------------------------------------------------------------------ |
    |   | If you specify this value, make sure your authorization policies enforce an appropriate level of authorization for the client. |

  ## Example

  ```
  bin/dsconfig set-gateway-api-endpoint-prop \
    --endpoint-name <your-endpoint-name> \
    --set http-auth-evaluation-behavior:evaluate-and-replace
  ```

  In this example, the `http-auth-evaluation-behavior` property is set to `evaluate-and-replace`.

* `access-token-validator`

  Sets the access token validators that the Gateway API Endpoint uses. By default, this property has no value, and the Gateway API Endpoint can evaluate every bearer token by using each access token validator that is configured on the server. To constrain the set of access token validators that a Gateway API Endpoint uses, set this property to use one or more specific values.

  If `http-auth-evaluation-behavior` is set to `do-not-evaluate`, this setting is ignored.

  ## Example

  ```
  bin/dsconfig set-gateway-api-endpoint-prop \
    --endpoint-name <your-endpoint-name> \
    --set access-token-validator:example-token-validator
  ```

  In this example, the `access-token-validator` property is set to `example-token-validator`.

---

---
title: API security gateway HTTP 1.1 support
description: As a reverse proxy, the API security gateway modifies HTTP requests and responses in addition to the changes required by policy processing.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_api_security_gw_http_support
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_api_security_gw_http_support.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2026
section_ids:
  forwarded-http-request-headers: Forwarded HTTP request headers
  forwarded-http-response-headers: Forwarded HTTP response headers
  unsupported-http-request-header: Unsupported HTTP request header
  unsupported-statement-changes: Unsupported statement changes
---

# API security gateway HTTP 1.1 support

As a reverse proxy, the API security gateway modifies HTTP requests and responses in addition to the changes required by policy processing.

## Forwarded HTTP request headers

HTTP requests often pass through several intermediaries before reaching their destination server. HTTP 1.1 defines two relevant types of headers:

* End-to-end headers

  Headers requiring transmission to all recipients on the chain, such as `Content-Type`.

* Hop-by-hop headers

  Headers that are only relevant to the next recipient on the chain, such as `Connection` and `Keep-Alive`.

  The API security gateway never forwards hop-by-hop headers. It forwards all end-to-end headers, with the following exceptions:

  * Headers related to HTTP resource versioning and conditional requests, such as `If-None-Match` and `If-Modified-Since`, are never forwarded.

  * Headers related to CORS, such as `Origin` or `Access-Control-Request-Method`, are never forwarded.

  * Headers that you exclude by using the `allowed-headers` configuration property of an API External Server to define an allow list of forwarded headers.

  * Headers that you remove by using a custom statement extension.

The API security gateway always adds the `Host`, `Accept-Encoding`, `Via`, `X-Forwarded-For`, `X-Forwarded-Host`, `X-Forwarded-Port`, and `X-Forwarded-Proto` headers to forwarded requests. If the `use-correlation-id-header` property is enabled on the HTTP Connection Handler, the gateway also adds a correlation ID header to the forwarded request. Learn more in [Configuring correlation IDs](paz_config_corr_id.html).

You can use the `http-auth-evaluation-behavior` property of a Gateway API Endpoint to alter the `Authorization` header of a forwarded request.

## Forwarded HTTP response headers

The API security gateway forwards most HTTP response headers, with the following exceptions:

* The `Date` header is replaced with a value generated by the API security gateway.

* The `Content-Length` header is replaced with a value generated by the API security gateway.

* The `Location` header is replaced with a value generated by the API security gateway.

* If the `use-correlation-id-header` property is enabled on the HTTP Connection Handler, the gateway adds a correlation ID header to the response. Learn more in [Configuring correlation IDs](paz_config_corr_id.html).

* Headers related to HTTP resource versioning and conditional requests, such as `ETag` and `Last-Modified`, are never forwarded.

* Headers related to CORS, such as `Access-Control-Allow-Origin` or `Access-Control-Allow-Headers`, are never forwarded.

## Unsupported HTTP request header

The API security gateway doesn't support the `Upgrade` header.

## Unsupported statement changes

The API security gateway doesn't support using statements to add, modify, or delete the following headers:

* Hop-by-hop headers that the gateway always removes, such as `Connection` and `Keep-Alive`

* Conditional request headers that the gateway always removes, such as `If-None-Match` and `ETag`

* Proxy-specific headers that the gateway always adds, such as `Via` and `X-Forwarded-For`

The gateway overrides any changes to these headers.

---

---
title: API security gateway policy request attributes
description: The API security gateway generates a set of attributes from inbound and outbound HTTP traffic.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_sec_gw_policy_request_attrs
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_sec_gw_policy_request_attrs.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2026
section_ids:
  top_level_gateway_attrs: Top-level Gateway request attributes
  additional_gateway_attrs: Additional request attributes
  gateway_access_token_attrs: Access token attributes
  gateway_client_cert_attrs: Client certificate attributes
  gateway_config_attrs: Gateway configuration attributes
---

# API security gateway policy request attributes

The API security gateway generates a set of attributes from inbound and outbound HTTP traffic. These attributes are available to access control policies and reflect details such as the HTTP request, the access token, client certificates, and gateway-specific routing information.

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | These attributes are automatically included in `defaultPolicies.SNAPSHOT` in the Policy Editor distribution. |

The following table describes these attributes:

## Top-level Gateway request attributes

| Attribute            | Value type | Description                                                                                                                                                                                                                                                      |
| -------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **action**           | String     | Returns the request processing phase and the HTTP method.This value is formatted as `<phase>-<method>`. Example values include `inbound-GET`, `inbound-POST`, `outbound-GET`, and `outbound-POST`.                                                               |
| **attributes**       | Object     | Returns additional attributes that don't correspond to a specific element type in the Trust Framework.You can find more information in the [next table](#additional_gateway_attrs).                                                                              |
| **domain**           | String     | This value isn't used.                                                                                                                                                                                                                                           |
| **identityProvider** | String     | Returns the name of the access token validator that evaluates the bearer token in an incoming request.                                                                                                                                                           |
| **service**          | String     | Returns an identifier for the API service.By default, this value is set to the name of the Gateway API Endpoint. To override the default value, set the Gateway API Endpoint's `service` property.Multiple Gateway API Endpoints can use the same service value. |

## Additional request attributes

The following table describes the additional attributes included in **attributes**.

| Attribute                         | Value type | Description                                                                                                                                                                |
| --------------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gateway**                       | Object     | Returns gateway-specific information about the request not provided by the other attributes in this table.                                                                 |
| **HttpRequest.AccessToken**       | Object     | Returns the parsed access token.You can find more information on this object in [Access token attributes](#gateway_access_token_attrs).                                    |
| **HttpRequest.ClientCertificate** | Object     | Returns properties of the client certificate, if one was used.You can find more information on this object in [Client certificate attributes](#gateway_client_cert_attrs). |
| **HttpRequest.CorrelationId**     | String     | Returns the ID that uniquely identifies the request and response, if available.                                                                                            |
| **HttpRequest.IPAddress**         | String     | Returns the client IP address.                                                                                                                                             |
| **HttpRequest.QueryParameters**   | Object     | Returns the request URI query parameters.                                                                                                                                  |
| **HttpRequest.RequestBody**       | Object     | Returns the request body, if available.                                                                                                                                    |
| **HttpRequest.RequestHeaders**    | Object     | Returns the request headers.                                                                                                                                               |
| **HttpRequest.RequestURI**        | String     | Returns the request URI.                                                                                                                                                   |
| **HttpRequest.ResourcePath**      | String     | Returns the portion of the request URI path that follows the inbound base path defined by the Gateway API Endpoint.                                                        |
| **HttpRequest.ResponseBody**      | Object     | Returns the response body, if available.This attribute is only provided for outbound policy requests.                                                                      |
| **HttpRequest.ResponseHeaders**   | Object     | Returns the response headers, if available.                                                                                                                                |
| **HttpRequest.ResponseStatus**    | Number     | Returns the response status code, if available.                                                                                                                            |
| **TokenOwner**                    | Object     | Returns the access token subject as a SCIM resource, as obtained by the access token validator.                                                                            |

### Access token attributes

The following table describes the child attributes of **HttpRequest.AccessToken**. These attributes are populated by the access token validator.

|   |                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These attributes correspond approximately to the fields defined by the IETF Token Introspection specification: [RFC 7662](https://datatracker.ietf.org/doc/html/rfc7662). |

| Attribute                  | Value type      | Description                                                                                                                                                                                                                                                                                                                                        |
| -------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **access\_token**          | String          | Returns the access token from the client request.                                                                                                                                                                                                                                                                                                  |
| **active**                 | Boolean         | Indicates whether this access token is currently active, as determined by the access token validator.                                                                                                                                                                                                                                              |
| **audience**               | String\[]       | Returns the recipients for whom the access token is intended. Typically, the authorization server sets this field to identify the resource servers that can accept the token.                                                                                                                                                                      |
| **authentication\_age**    | Number          | Returns the number of seconds since the end user was authenticated by the token issuer.This attribute uses the `System Current DateTime` resolver and a SpEL processor to calculate the number of seconds since the **authentication\_time**. This calculation requires the `auth_time` claim in the access token.                                 |
| **authentication\_policy** | String          | Returns the authentication policy that was satisfied when the access token was issued. An authentication policy is also called an authentication context class reference (ACR).If the access token contains an `acr` claim, this attribute uses a JSON Path processor to extract the date and time from the **HttpRequest.AccessToken** attribute. |
| **authentication\_time**   | Zoned Date Time | Returns the date and time when the end user was authenticated.If the access token contains an `auth_time` claim, this attribute uses a JSON Path processor to extract the date and time from the **HttpRequest.AccessToken** attribute. If the claim is missing from the token, the default value is January 1, 1970.                              |
| **client\_id**             | String          | Returns the client ID of the application that was granted the access token.                                                                                                                                                                                                                                                                        |
| **expiration**             | DateTime        | Returns the date and time at which the access token expired.                                                                                                                                                                                                                                                                                       |
| **issued\_at**             | DateTime        | Returns the date and time at which the access token was issued.                                                                                                                                                                                                                                                                                    |
| **issuer**                 | String          | Returns the token issuer.Typically, this value is a URI that identifies the authorization server.                                                                                                                                                                                                                                                  |
| **not\_before**            | DateTime        | Returns the date and time before which a resource server doesn't accept an access token.                                                                                                                                                                                                                                                           |
| **scope**                  | Collection      | Returns the list of scopes granted to this token.                                                                                                                                                                                                                                                                                                  |
| **subject**                | String          | Returns the token subject.This value represents a user identifier set by the authorization server.                                                                                                                                                                                                                                                 |
| **token\_owner**           | String          | Returns the user identifier resolved by the access token validator's token resource lookup method.This value is a SCIM ID of the form `<resource type>/<resource ID>`.                                                                                                                                                                             |
| **token\_type**            | String          | Returns the token type set by the authorization server.Typically, this value is `bearer`.                                                                                                                                                                                                                                                          |
| **user\_token**            | Boolean         | Returns a flag set by the access token validator to indicate whether the token includes a subject. When this flag is `false`, the token contains no subject and was issued directly to a client.                                                                                                                                                   |
| **username**               | String          | Returns the subject's user name.This value represents a user identifier set by the authorization server.                                                                                                                                                                                                                                           |

### Client certificate attributes

The following table describes the child attributes of **HttpRequest.ClientCertificate**:

| Attribute        | Value type | Description                                                                                                                                             |
| ---------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **algorithm**    | String     | Returns the name of the certificate signature algorithm, such as `SHA256withRSA`.                                                                       |
| **algorithmOID** | String     | Returns the signature algorithm OID.                                                                                                                    |
| **issuer**       | String     | Returns the distinguished name (DN) of the certificate issuer.                                                                                          |
| **notAfter**     | DateTime   | Returns the expiration date and time of the certificate.                                                                                                |
| **notBefore**    | DateTime   | Returns the earliest date on which the certificate is considered valid.                                                                                 |
| **subject**      | String     | Returns the DN of the certificate subject.                                                                                                              |
| **subjectRegex** | String     | Returns the regular expression that must be matched by the subject field of the certificate to ensure the certificate belongs to the requesting client. |
| **valid**        | Boolean    | Indicates whether the SSL client certificate is valid.                                                                                                  |

## Gateway configuration attributes

The following table describes the child attributes of **Gateway**:

| Attribute            | Value type | Description                                                                                                                 |
| -------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------- |
| **BasePath**         | String     | Returns the portion of the HTTP request URI that matches the Gateway API Endpoint's `inbound-base-path` value.              |
| **TrailingPath**     | String     | Returns the portion of the HTTP request URI that follows the **BasePath**.                                                  |
| Base path parameters | String     | Returns parameters defined in the Gateway API Endpoint's `inbound-base-path` configuration property.                        |
| Custom attributes    | String     | Returns custom attributes that are defined in the Gateway API Endpoint's `policy-request-attribute` configuration property. |

---

---
title: API security gateway policy requests
description: The API security gateway creates policy requests for incoming requests and API responses, and you can observe how it creates them.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_api_security_gw_policy_reqs
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_api_security_gw_policy_reqs.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 15, 2025
---

# API security gateway policy requests

The API security gateway creates policy requests for incoming requests and API responses, and you can observe how it creates them.

Before accepting an incoming request and forwarding it to the API server, the gateway creates a policy request based on the incoming request and sends it to the policy decision point (PDP) for authorization. Before accepting an API server response and forwarding it back to the client, the gateway creates a policy request based on the incoming request and response and sends it to the PDP for authorization. An understanding of the manner in which the gateway formulates policy requests can help you create and troubleshoot policies more effectively.

You can selectively disable response policy processing on a per-API-Endpoint basis. This ability is useful if the Gateway authorizes requests but does not filter responses. Disabling this processing can improve performance for frequent requests or requests that return very large responses. To disable processing, set the Gateway API Endpoint's `disable-response-processing` property to `true`.

To better understand how the gateway formulates policy requests, enable detailed decision logging to view policy request attributes in action. This is especially helpful when first developing API security gateway policies. Learn more in [Policy Decision logger](paz_enable_detailed_logging.html#policy_decision_logger).

---

---
title: API server request authentication
description: As with the API security gateway, API server requests authorized by the Sideband API don't require authentication. However, the default policy set requires bearer token authentication.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_authn_api_server_reqs
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_authn_api_server_reqs.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 30, 2025
section_ids:
  example: Example
  example-2: Example
---

# API server request authentication

As with the [API security gateway](paz_api_security_gw_authn.html), API server requests authorized by the Sideband API don't require authentication. However, the default policy set requires bearer token authentication.

The Sideband API uses configured Access Token Validators to evaluate bearer tokens that are included in incoming requests. The `HttpRequest.AccessToken` attribute supplies the validation result to the policy request, and the `TokenOwner` attribute provides the user identity that is associated with the token.

Policies use this authentication information to affect the processing requests and responses. For example, the following policy in the default policy set requires all requests to be made with an active access token:

```
Rule: Deny if HttpRequest.AccessToken.active Equals false

Statement:
  Code: denied-reason
  Applies To: Deny
  Payload: {"status":401, "message": "invalid_token", "detail":"Access token is expired or otherwise invalid"}
```

Sideband API Endpoints include the following configuration properties to specify how client authentication is handled:

* `http-auth-evaluation-behavior`

  Determines whether the Sideband API Endpoint evaluates or modifies the HTTP authentication scheme and whether this scheme is forwarded to the API server through the API gateway.

  This property accepts the following values:

  * `do-not-evaluate`

    The Sideband API Endpoint doesn't evaluate or modify the HTTP authentication scheme. This can be useful when implementing an authentication scheme that doesn't evaluate bearer tokens, such as MTLS.

    If the client request includes an `Authorization` header, the PingAuthorize Server forwards the unmodified header to the external API server through the API gateway.

    |   |                                                                                                                                                                                                                                                           |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If you specify this value, policies protecting this endpoint should not enforce constraints on request authentication, such as the validity of the access token. The default policy snapshot enforces such a constraint in the `Token Validation` policy. |

  * `evaluate-and-forward`

    The Sideband API Endpoint evaluates the provided authentication credentials and makes authentication information available for policy evaluation. If the client request includes an `Authorization` header, the PingAuthorize Server forwards the unmodified header to the external API server through the API gateway unless a policy decision directs otherwise.

    This value is set by default.

  * `evaluate-and-discard`

    The Sideband API Endpoint evaluates the provided authentication credentials and makes authentication information available for policy evaluation. If the client request includes an `Authorization` header, the PingAuthorize Server removes this header before forwarding the request to the external API server through the API gateway.

  * `evaluate-and-replace`

    The Sideband API Endpoint evaluates the provided authentication credentials and makes authentication information available for policy evaluation. If the client request includes an `Authorization` header, the PingAuthorize Server replaces this header with one containing the basic authentication credentials defined for the external API server.

    |   |                                                                                                                                |
    | - | ------------------------------------------------------------------------------------------------------------------------------ |
    |   | If you specify this value, make sure your authorization policies enforce an appropriate level of authorization for the client. |

  ## Example

  ```
  bin/dsconfig set-sideband-api-endpoint-prop \
    --endpoint-name <your-endpoint-name> \
    --set http-auth-evaluation-behavior:evaluate-and-replace
  ```

  In this example, the `http-auth-evaluation-behavior` property is set to `evaluate-and-replace`.

* `access-token-validator`

  Sets the access token validators that the Sideband API Endpoint uses. By default, this property has no value, and the Sideband API Endpoint can evaluate every bearer token by using each access token validator that is configured on the server. To constrain the set of access token validators that a Sideband API Endpoint uses, set this property to use one or more specific values.

  If `http-auth-evaluation-behavior` is set to `do-not-evaluate`, this setting is ignored.

  ## Example

  ```
  bin/dsconfig set-sideband-api-endpoint-prop \
    --endpoint-name <your-endpoint-name> \
    --set access-token-validator:example-token-validator
  ```

  In this example, the `access-token-validator` property is set to `example-token-validator`.

---

---
title: Authenticating to the JSON PDP API
description: The JSON PDP API can require a client to authenticate to it by using a shared secret.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_authenticate_json_pdp_api
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_authenticate_json_pdp_api.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2025
section_ids:
  json_create_shared_secret: Creating a shared secret
  steps: Steps
  example: Example:
  example-2: Example:
  json_delete_shared_secret: Deleting a shared secret
  steps-2: Steps
  example-3: Example:
  example-4: Example:
  rotating-shared-secrets: Rotating shared secrets
  steps-3: Steps
  customizing-the-shared-secret-header: Customizing the shared secret header
  steps-4: Steps
  example-5: Example:
---

# Authenticating to the JSON PDP API

The JSON PDP API can require a client to authenticate to it by using a shared secret.

To define shared secrets, use JSON PDP API Shared Secret configuration objects. To manage shared secrets, use the JSON PDP API HTTP Servlet Extension.

## Creating a shared secret

Define the authentication credentials that the JSON PDP API might require a client to present.

### Steps

1. To create a shared secret, run the following example `dsconfig` command, substituting values of your choosing.

   #### Example:

   ```
   PingAuthorize/bin/dsconfig create-authorization-policy-decision-shared-secret \
     --secret-name "Shared Secret A" \
     --set "shared-secret:secret123"
   ```

   |   |                                                                                                                                                                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * The `shared-secret` property sets the value that the JSON PDP API requires the client to present. After you set this value, it is no longer visible.

   * The `secret-name` property is a label that allows an administrator to distinguish one JSON PDP API Shared Secret from another. |

2. To update the `shared-secrets` property, run the following example `dsconfig` command.

   #### Example:

   ```
   PingAuthorize/bin/dsconfig set-http-servlet-extension-prop \
     --extension-name "JSON PDP API" \
     --add "shared-secrets:Shared Secret A"
   ```

   A new JSON PDP API Shared Secret is not used until the `shared-secrets` property of the JSON PDP API HTTP Servlet Extension is updated.

## Deleting a shared secret

You can remove a shared secret from use or delete it entirely.

### Steps

* To remove a JSON PDP API Shared Secret from use, run the following example `dsconfig` command, substituting values of your choosing.

  #### Example:

  ```json
  {pingauthorize}/bin/dsconfig set-http-servlet-extension-prop \
    --extension-name "JSON PDP API" \
    --remove "shared-secrets:Shared Secret A"
  ```

* To delete a JSON PDP API Shared Secret, run the following example `dsconfig` command.

  #### Example:

  ```json
  {pingauthorize}/bin/dsconfig delete-authorization-policy-decision-shared-secret \
    --secret-name "Shared Secret A"
  ```

## Rotating shared secrets

To avoid service interruptions, the JSON PDP API allows multiple, distinct shared secrets to be accepted at the same time.

You can configure a new shared secret that the JSON PDP API accepts alongside an existing shared secret. This allows time to update the client to use the new shared secret.

### Steps

1. Create a new JSON PDP API shared secret and assign it to the JSON PDP API HTTP Servlet Extension. Learn more in [Creating a shared secret](#json_create_shared_secret).

2. Update the client to use the new shared secret.

3. Remove the previous JSON PDP API shared secret. Learn more in [Deleting a shared secret](#json_delete_shared_secret).

## Customizing the shared secret header

By default, the JSON PDP API accepts a shared secret from a client through the CLIENT-TOKEN header.

### Steps

* To customize a shared secret header, change the value of the JSON PDP API HTTP Servlet Extension's `shared-secret-header` property.

  #### Example:

  The following command changes the shared secret header to `x-shared-secret`.

  ```json
  {pingauthorize}/bin/dsconfig set-http-servlet-extension-prop \
    --extension-name "JSON PDP API" \
    --set shared-secret-header-name:x-shared-secret
  ```

  The following command resets the shared secret header to its default value.

  ```json
  {pingauthorize}/bin/dsconfig set-http-servlet-extension-prop \
    --extension-name "JSON PDP API" \
    --reset shared-secret-header-name
  ```

---

---
title: Auto-healing for unavailable servers
description: Using gauges, set up auto-healing in a container deployment to address an unavailable server.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_auto_healing
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_auto_healing.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
section_ids:
  steps: Steps
---

# Auto-healing for unavailable servers

Using gauges, set up auto-healing in a container deployment to address an unavailable server.

## Steps

1. Configure one or more of the gauges described in [Server availability](paz_server_availability.html).

2. Configure the gauges to trigger the UNAVAILABLE status.

   By default, the gauges do not trigger the UNAVAILABLE status.

   As discussed in [Endpoint Average Response Time (Milliseconds) gauge](paz_endpoint_avg_resp.html) and [HTTP Processing (Percent) gauge](paz_http_proc_gauge.html), use the `dsconfig` command to adjust the following values for your environment. Each system is different so you might need to adjust the values several times to determine your ideal configuration.

   1. For the `Endpoint Average Response Time (Milliseconds)` gauge, set `critical-value`.

   2. For the `HTTP Processing (Percent)` gauge, set both `critical-value` and `server-unavailable-severity-level`.

3. Configure the container orchestrator to use the `available-or-degraded-state` endpoint to detect whether the server is alive.

   For information about the endpoint, see [Availability servlet](paz_server_status.html#availability_servlet).

---

---
title: Automatic backend LDAP server discovery
description: Instead of explicitly specifying all backend LDAP servers in the configuration as LDAP external servers, you can configure PingAuthorize Server to automatically discover its backend servers.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_auto_backend_discovery
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_auto_backend_discovery.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# Automatic backend LDAP server discovery

Instead of explicitly specifying all backend LDAP servers in the configuration as LDAP external servers, you can configure PingAuthorize Server to automatically discover its backend servers.

|   |                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This feature requires that all backend LDAP servers be PingDirectory Servers running version 8.0.0.0 or later. Automatic backend discovery is not supported for PingDirectoryProxy Server or third-party LDAP servers. |

To configure automatic backend discovery, you must complete these tasks:

* Join the PingAuthorize Server to the same topology as the PingDirectory Servers.

* Configure the PingAuthorize Server's load-balancing algorithm with an LDAP external server template. This template provides the connection and health check settings that PingAuthorize Server uses for all PingDirectory Servers.

* Configure the topology registry entry for each PingDirectory Server to indicate the name of the PingAuthorize Server load-balancing algorithm.

---

---
title: Available gauges
description: PingAuthorize makes the following gauges available. You can manage these gauges using the administrative console or the dsconfig tool.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_available_gauges
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_available_gauges.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# Available gauges

PingAuthorize makes the following gauges available. You can manage these gauges using the administrative console or the `dsconfig` tool.

| Gauge name                                    | Enabled by default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Available File Descriptors                    | true               | Monitors the number of file descriptors available to the server process. The server allows for an unlimited number of connections by default but is restricted by the file descriptor limit on the operating system.You can configure the number of file descriptors that the server uses by either setting the `NUM_FILE_DESCRIPTORS` environment variable or by creating a `config/num-file-descriptors` file with a single line such as, `NUM_FILE_DESCRIPTORS=12345`. If you do not use either of these options, the server uses the default of 65535.Running out of available file descriptors can lead to unpredictable behavior and severe system instability.                                                                                                                                                                                                             |
| Certificate Expiration (Days)                 | true               | Monitors the expiration dates of key server certificates.A server certificate expiring can cause server unavailability, degradation, or loss of key server functionality.Replace certificates nearing the end of their validity as soon as possible.For more information about server certificates and how they are managed, see the `status` tool or **Status** in the administrative console.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| CPU Usage (Percent)                           | true               | Monitors server CPU use and provides an averaged percentage for the interval defined.The monitored resource is the host system's CPU, which does not include a resource identifier. If CPU use is high, check the server's current workload and other processes on the system and make any needed adjustments. Reducing the load on the system will lead to better response times.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Disk Busy (Percent)                           | true               | Monitors the percentage of disk use time averaged over the specified update interval.This gauge requires that you enable the Host System Monitor Provider and that you register any monitored disks by using the `disk-devices` property of that configuration object.The resource identifier for this gauge is the disk device name. Use the `iostat` command or a similar system utility to see a list of disk device names. A separate gauge monitor entry is created for each monitored disk.                                                                                                                                                                                                                                                                                                                                                                                 |
| Endpoint Average Response Time (Milliseconds) | false              | Monitors the average response time across all endpoints since the server was started. This number does not include requests to the upstream server.There is no resource identifier associated with this gauge.The monitored resource is overall response time of all requests to PingAuthorize servlets since the server was started.High response times might be indicative of a number of factors including a disk-bound server, network latency, or misconfiguration. Enabling the Stats Logger plugin can help isolate problems.For more information, see [Endpoint Average Response Time (Milliseconds) gauge](paz_endpoint_avg_resp.html).                                                                                                                                                                                                                                  |
| HTTP Processing (Percent)                     | true               | Monitors the percentage of time that request handler threads spend processing HTTP requests. This percentage represents the inverse of the server's ability to handle new requests without queueing.For more information, see [HTTP Processing (Percent) gauge](paz_http_proc_gauge.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| JVM Memory Usage (Percent)                    | true               | Monitors the percentage of Java Virtual Machine memory that is in use. This value naturally fluctuates due to garbage collection, so the minimum value within an interval is reported because it is a better indication of overall memory growth.When the memory usage exceeds 90%, open a case with [Ping Identity Support](https://support.pingidentity.com/) because the server is either misconfigured or has a memory leak.As memory usage approaches 100%, the server is more and more likely to experience garbage collection pauses, which leave the server unresponsive for a long time. Restarting the server is likely the only remedy for this situation. Before you restart the server, run `collect-support-data` and capture the output of `jmap -histo <server-pid>` to provide to customer support. The PID of the server is in `<server-root>/logs/server.pid`. |
| License Expiration (Days)                     | true               | Monitors the expiration date of the product license. An expired license causes warnings to appear in the server's logs and in the `status` tool output.Request a license key through the Ping Identity licensing website <https://www.pingidentity.com/en/account/request-license-key.html> or contact <sales@pingidentity.com>.Use the `dsconfig` tool to update the License configuration's license key property.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Memory Usage (Percent)                        | false              | Monitors the percentage of memory use averaged over the update interval defined. The monitored resource is the host system's memory use, which does not have a resource identifier.Some operating systems, including Linux, use the majority of memory for file system cache, which is freed as applications need it. If memory use is high, check the applications that are running on the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Policy Decision Service Availability          | true               | Monitors availability of the Policy Decision Service.If the Policy Decision Service is misconfigured or cannot reach the deployment package store, PingAuthorize services will be unavailable.Ensure that the `pdp-mode` and `trust-framework-version` are correctly set, and that the deployment package store is reachable.For more information, see [Policy Decision Service Availability gauge](paz_policy_dec_srv_avial_gauge.html).                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Strong Encryption Not Available               | true               | Indicates the JVM does not appear to support strong encryption algorithms, like 256-bit AES. The server will fall back to using weaker algorithms, like 128-bit AES.To enable support for strong encryption, update your JVM to a newer version that supports it by default; alternatively, install or enable the unlimited encryption strength jurisdiction policy files in your Java installation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| User Store Availability                       | true               | Monitors availability of the SCIM user store.If the LDAP directory servers are unavailable, the "UserStoreAdapter" cannot forward requests. Also, the server cannot process SCIM requests or perform token owner lookups.Ensure that LDAP directory servers are available.For more information, see [User Store Availability gauge](paz_user_store_avail_gauge.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

---

---
title: Available manage-certificates subcommands
description: The manage-certificates tool uses the following subcommands to indicate which function to invoke:
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_available_subcmds
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_available_subcmds.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# Available manage-certificates subcommands

The `manage-certificates` tool uses the following subcommands to indicate which function to invoke:

| Subcommand                                 | Function                                                                                                                                                                             |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `list-certificates`                        | Lists the certificates in a keystore.                                                                                                                                                |
| `import-certificate`                       | Imports a certificate into a trusted certificate entry or imports a certificate chain and private key into a private key entry.                                                      |
| `export-certificate`                       | Exports a certificate from a keystore.                                                                                                                                               |
| `export-private-key`                       | Exports a private key from a keystore.                                                                                                                                               |
| `generate-self-signed-certificate`         | Generates a self-signed certificate.                                                                                                                                                 |
| `generate-certificate-signing-request`     | Generates a certificate-signing request that can be provided to a certification authority.                                                                                           |
| `sign-certificate-signing-request`         | Signs a certificate-signing request with a specified issuer certificate.                                                                                                             |
| `check-certificate-usability`              | Checks a specified certificate in a keystore to verify whether it is suitable for use as a listener certificate.                                                                     |
| `trust-server-certificate`                 | Initiates the TLS-negotiation process with a specified server to obtain its certificate chain so that a truststore can be updated with the necessary information to trust the chain. |
| `display-certificate-file`                 | Displays the contents of a file that contains one or more PEM-encoded or DER-encoded X.509 certificates.                                                                             |
| `display-certificate-signing-request-file` | Displays the contents of a file that contains a PEM-encoded or DER-encoded PKCS #10 certificate-signing request (CSR).                                                               |
| `change-certificate-alias`                 | Changes the alias for an entry in a keystore.                                                                                                                                        |
| `change-keystore-password`                 | Changes the password for a keystore.                                                                                                                                                 |
| `change-private-key-password`              | Changes the password that protects the private key for a specified entry in a keystore.                                                                                              |

---

---
title: Certificate chains
description: A certificate chain is an ordered list of one or more certificates. In such a chain, each subsequent certificate is the issuer of the previous certificate.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_cert_chains
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_cert_chains.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# Certificate chains

A certificate chain is an ordered list of one or more certificates. In such a chain, each subsequent certificate is the issuer of the previous certificate.

During TLS negotiation, the server presents a certificate chain to the client, which determines whether to trust the chain and continue with the negotiation. The client can also present its own certificate chain to the server.

If a certificate is self-signed, its chain contains only that single certificate. If a certificate is signed by a self-signed certificate authority (CA) certificate, such as a root CA, the chain contains two certificates: the server certificate and the CA certificate that follows it. If a single intermediate CA (a CA certificate that is signed by a root CA) is present, the chain contains the server certificate, followed by the intermediate CA, and then the root CA.

Intermediate certificate authorities are useful for security purposes, especially in commercial authorities. If a client trusts a root CA certificate, it is likely to trust anything with that root CA certificate at the base of its chain. Consequently, the root CA certificate must be kept secure.

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | If the root CA certificate is compromised, any certificate that is directly or indirectly signed by it can no longer be trusted. |

With intermediate CA certificates, the root certificate can be kept offline in secure storage and used only when a new intermediate CA certificate must be signed. The intermediate CA certificates can be used to sign end-entity certificates, but must be protected to avoid compromising any of the certificates. A compromised certificate must be revoked along with all of the certificates that it signed. In such a scenario, the root CA can be used to sign a new certificate.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The certificate chain that the server presents to the client, or that the client presents to the server, during TLS negotiation does not always need to be the complete chain. If the root CA at the end of the chain is widely trusted, the server can assume that the client already has that root CA in its default set of trusted certificates. The server can leave that root CA off the chain with the assumption that the client will retrieve it from its default trust store. While the same assumption could theoretically be true for intermediate CA certificates, only the root CA certificate is commonly omitted. When a client receives an incomplete chain, the client looks in its default trust store to determine whether the trust store contains the issuer certificate, which it can identify by using properties like the issuer distinguished name (DN) or an authority key identifier extension. |

The certificate at the head of a certificate chain, which appears as the first one in the list, is often called the end-entity certificate. If this certificate appears at the head of the chain that a server presents during TLS negotiation, it is referred to as the server certificate. If the certificate appears at the head of a chain that a client presents, it is referred to as a client certificate. The certificate at the end of a complete chain must be a root CA certificate. In the case of a self-signed certificate, the chain contains only a single certificate that serves both roles.

---

---
title: Certificate extensions
description: Extensions provide additional context for a certificate.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_cert_extensions
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_cert_extensions.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# Certificate extensions

Extensions provide additional context for a certificate.

Some of the more common extension types include the following:

* Subject key identifier

  Holds a unique identifier for the certificate, which is generally derived from the certificate's public key.

* Authority key identifier

  Holds the subject key identifier for the issuer certificate. This extension type helps to identify the issuer certificate, especially when presented with an incomplete certificate chain.

* Subject alternative name

  Holds a list of ways that clients are expected to reference a server when establishing a connection to it.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Clients must take this information into account when deciding whether to trust a server's certificate.The most common types of values include DNS names, IP addresses, and URIs. DNS names must be fully qualified, but can optionally use an asterisk in the leftmost component to match any single name in that component. For example, `*.example.com` could match `www.example.com` or `ldap.example.com`, but would not match `ldap.east.example.com` or `example.com`. |

* Key usage

  Provides information about the manner in which the certificate is expected to be used. The following key usages are allowed:

  * `digitalSignature`

    Indicates that the certificate can be used for digitally signing data, excluding certificates and certificate revocation lists (CRL).

  * `nonRepudiation`

    Indicates that the certificate can be used to prevent denying the authenticity of a message. `nonRepudiation` is also known as `contentCommitment`.

  * `keyEncipherment`

    Indicates that the certificate can be used to protect encryption keys, such as symmetric keys that are derived during TLS key agreement.

  * `dataEncipherment`

    Indicates that the certificate can be used for encrypting data directly.

  * `keyAgreement`

    Indicates that the certificate's public key can be used for key agreement, such as deriving the symmetric key that protects TLS communication.

  * `keyCertSign`

    Indicates that the certificate can act as a certification authority and be used for signing other certificates.

  * `cRLSign`

    Indicates that the certificate can be used to sign CRLs.

  * `encipherOnly`

    When used in conjunction with `keyEncipherment`, indicates that the public key can be used only for encrypting data during key agreement.

  * `decipherOnly`

    When used in conjunction with `keyEncipherment`, indicates that the public key can be used only for decrypting data during key agreement.

* Extended key usage

  Acts as an alternative to the key usage extension and provides additional high-level functionality. The following extended key usages are allowed:

  * `serverAuth`

    Indicates that the server can present the certificate to the client during TLS negotiation.

  * `clientAuth`

    Indicates that the client can present the certificate to the server during TLS negotiation.

  * `codeSigning`

    Indicates that the certificate can be used to sign source and compiled code.

  * `emailProtection`

    Indicates that the certificate can be used to sign or encrypt email messages.

  * `timeStamping`

    Indicates that the certificate can be used to assert the time that an event occurred.

  * `ocspSigning`

    Indicates that the certificate can be used to sign an online certificate status protocol (OCSP) response.

* Basic constraints

  Indicates whether the certificate can act as a certification authority and, if so, the maximum number of intermediate certificates that can follow it in a certificate chain.

---

---
title: Certificate key pairs
description: Each certificate contains a key pair that consists of two keys that are linked cryptographically. If you encrypt data with one key, the data can be only decrypted with the other key.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_cert_key_pairs
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_cert_key_pairs.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# Certificate key pairs

Each certificate contains a key pair that consists of two keys that are linked cryptographically. If you encrypt data with one key, the data can be only decrypted with the other key.

Although a key pair can be created easily when both keys are generated simultaneously, the process of deriving one key from the other is extremely difficult, a process categorized in cryptographic terms as computationally infeasible.

When generating a key pair, one key is designated as the public key, and the other key is designated the private key. The public key can be made widely available, but the private key must be kept secret and not shared with anyone.

As long as the secrecy of the private key is maintained, the key pair can be used to perform the following functions:

* Encryption, sometimes referred to as confidentiality

  If someone wants to send you a secret message without anyone else viewing it, the message can be encrypted with your public key. Only you possess the private key, so only you can decrypt the message.

* Digital signatures

  If you encrypt data with your private key, it can be decrypted only with your public key. Because your public key can be made widely available, this encryption method does not actually protect the content. However, digital signatures prove that a message came from you because only your private key could have generated it.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                            |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | When generating a digital signature, the entire message is generally not encrypted. Only a hash of the message is encrypted, typically by using a digest algorithm like SHA-256.This approach protects the integrity of a message. A decrypted signature that matches the digest of the original message guarantees that the message came from you and that it has remained unaltered since you signed it. |

The following public key algorithms are used primarily in certificates that facilitate TLS communication:

* RSA, which is based on the multiplication of large prime numbers

* EC, which is based on computations that involve special types of elliptical curves

Although RSA is supported more widely than EC, it is slower and requires larger keys to achieve the same level of security. To support legacy clients, you should use an RSA certificate and choose a key size of at least 2,048 bits.

If all of your clients support EC certificates, you should use an EC certificate with a key size of at least 256 bits.

---

---
title: Certificate subject DNs
description: A certificate's subject distinguished name (DN) provides information about how the certificate should be used.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_cert_subject_dns
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_cert_subject_dns.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# Certificate subject DNs

A certificate's subject distinguished name (DN) provides information about how the certificate should be used.

Like an LDAP DN, a certificate's subject DN consists of a comma-delimited series of attribute-value pairs. However, unlike an LDAP DN, the attribute names in a certificate subject DN are typically written in all uppercase characters.

A certificate's subject DN is also referred to as its subject. The following attributes commonly appear in a certificate subject.

| Attribute name | Attribute description                                                                                                                                                                                                                                                                                                        |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CN`           | Common name&#xA;&#xA;For a listener certificate, the CN attribute typically identifies the host name that clients use to access the certificate. However, the subject alternative name extension is recommended more highly for accomplishing the same task. Most certificate subject DNs include at least the CN attribute. |
| `E`            | Email address                                                                                                                                                                                                                                                                                                                |
| `OU`           | Name of the organizational unit, such as the relevant department                                                                                                                                                                                                                                                             |
| `O`            | Name of the organization or company                                                                                                                                                                                                                                                                                          |
| `L`            | Name of the locality, such as the appropriate city                                                                                                                                                                                                                                                                           |
| `ST`           | Full name of the state or province                                                                                                                                                                                                                                                                                           |
| `C`            | ISO 3166 country code                                                                                                                                                                                                                                                                                                        |

A certificate subject includes at least one attribute-value pair, and the `CN` attribute is typically present. Other attributes can be omitted, although the `O` and `C` attributes are also common. For example, a listener certificate for a server with an address of `ldap.example.com`, which is run by the US-based company Example Corp, might have a subject of `CN=ldap.example.com,O=Example Corp,C=US`.